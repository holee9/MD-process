#!/usr/bin/env bash
# 사이클 실행 — 마운트 밖 클론에서 수행 (audit #1034, 구조적 대책)
#
# 왜 마운트 밖인가:
#   락 문제의 진짜 원인은 "git이 자기 락을 지우지 못하는 곳에서 git을 돌리는 것"이다.
#   이 저장소가 놓인 마운트는 삭제가 세션 권한에 의존하고, 그 권한은 세션이 끝나면 사라진다.
#   반면 VM 자체 공간은 삭제 제약이 없다 — 실측 확인(2026-09-18).
#   따라서 사이클을 마운트 밖 클론에서 돌리면 락 문제 자체가 발생하지 않는다.
#   이는 README §자동화 시스템이 원래 정의한 설계('/tmp/wk-* 신규 클론에서 작업 → push')와도 일치한다.
#
# 동작: 마운트 밖 작업클론 준비 → 최신화 → 빌드 → 커밋 → push → (선택)마운트 폴더 동기화
# 사용: bash scripts/run_cycle.sh "<커밋 메시지>"

set -uo pipefail

MOUNT_REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WORK_DIR="${MDP_WORK_DIR:-$HOME/.mdprocess-work}"
MSG="${1:-chore(cycle): 자동 사이클 산출물 반영}"
TOKEN_FILE="$MOUNT_REPO/.secrets/token.txt"
REPO_PATH="holee9/MD-process.git"
REMOTE_USER="holee9-automation"

log() { echo "[cycle] $*"; }

[ -f "$TOKEN_FILE" ] || { log "토큰 없음: $TOKEN_FILE"; exit 1; }
TOKEN="$(tr -d '[:space:]' < "$TOKEN_FILE")"
URL="https://${REMOTE_USER}:${TOKEN}@github.com/${REPO_PATH}"
mask() { sed "s/${TOKEN}/***/g"; }

# --- 1. 작업 클론 준비 (마운트 밖) -----------------------------------------
if [ ! -d "$WORK_DIR/.git" ]; then
  log "작업 클론 신규 생성: $WORK_DIR"
  rm -rf "$WORK_DIR"
  git clone --quiet "$URL" "$WORK_DIR" 2>&1 | mask || { log "clone 실패"; exit 1; }
else
  log "기존 작업 클론 사용: $WORK_DIR"
fi
cd "$WORK_DIR" || exit 1

# 작업 클론은 마운트 밖이라 락 제약이 없다. 그래도 방어적으로 정리.
rm -f .git/*.lock 2>/dev/null

# 커밋 identity 승계 — 신규 클론에는 설정이 없어 커밋이 실패한다.
# 마운트 저장소의 설정을 그대로 물려받아 이력상 동일 주체로 남게 한다.
CI_NAME="$(git -C "$MOUNT_REPO" config --get user.name 2>/dev/null || echo 'md-process-auditor')"
CI_MAIL="$(git -C "$MOUNT_REPO" config --get user.email 2>/dev/null || echo 'auditor@md-process')"
git config user.name  "$CI_NAME"
git config user.email "$CI_MAIL"
log "커밋 주체: ${CI_NAME} <${CI_MAIL}>"

# --- 2. 최신화 (로컬 변경은 버리고 origin 기준으로 맞춘다) ------------------
git fetch --quiet "$URL" "main:refs/remotes/origin/main" --force 2>&1 | mask || { log "fetch 실패"; exit 1; }
git reset --hard --quiet origin/main || { log "reset 실패"; exit 1; }
git clean -qfd
log "기준: $(git log -1 --format='%h %s' | cut -c1-70)"

# --- 3. 마운트 폴더의 미반영 작업분 반입 ------------------------------------
# 마운트 폴더에는 두 종류의 미반영분이 있을 수 있고, 둘 다 가져와야 한다.
#   (a) 미커밋 변경  — git diff HEAD 로 캡처
#   (b) 커밋됐지만 origin 에 없는 커밋 — 로컬 전용 커밋. (a)만 보면 이걸 놓친다.
# 2026-09-18 최초 구현이 (b)를 누락해 새 스크립트가 push 되지 않는 일이 있었다.
if [ -n "${MDP_IMPORT_MOUNT:-}" ]; then
  log "마운트 폴더 변경분 반입 시도"
  ( cd "$MOUNT_REPO" && bash scripts/git_safe.sh --clean >/dev/null 2>&1 )

  # (b) 로컬 전용 커밋을 직접 가져온다. 마운트 저장소를 임시 원격으로 사용.
  git remote remove _mount 2>/dev/null
  git remote add _mount "$MOUNT_REPO" 2>/dev/null
  if git fetch --quiet _mount 2>/dev/null; then
    MOUNT_HEAD="$(git rev-parse _mount/main 2>/dev/null || echo '')"
    if [ -n "$MOUNT_HEAD" ] && [ "$(git rev-list --count HEAD.."$MOUNT_HEAD" 2>/dev/null || echo 0)" -gt 0 ]; then
      log "마운트 전용 커밋 $(git rev-list --count HEAD.."$MOUNT_HEAD")건 병합"
      git merge --no-edit "$MOUNT_HEAD" 2>&1 | tail -3 || log "병합 충돌 — 수동 확인 필요"
    else
      log "마운트 전용 커밋 없음"
    fi
  fi
  git remote remove _mount 2>/dev/null

  # (a) 미커밋 변경
  git -C "$MOUNT_REPO" diff HEAD --binary > /tmp/mdp_mount.patch 2>/dev/null
  if [ -s /tmp/mdp_mount.patch ]; then
    git apply --3way /tmp/mdp_mount.patch 2>&1 | head -3 && log "미커밋 변경 반입 완료" || log "미커밋 변경 반입 실패 — 건너뜀"
  else
    log "마운트 미커밋 변경 없음"
  fi
fi

# --- 4. 빌드 ---------------------------------------------------------------
python3 scripts/build_readiness.py >/dev/null 2>&1
python3 scripts/build_matrix.py >/dev/null 2>&1
python3 scripts/build_dashboard_html.py >/dev/null 2>&1

if ! python3 scripts/validate_frontmatter.py >/dev/null 2>&1; then
  log "frontmatter 검증 실패 — 커밋 중단"
  python3 scripts/validate_frontmatter.py 2>&1 | tail -5
  exit 1
fi

# --- 5. 커밋 & push --------------------------------------------------------
if [ -z "$(git status --porcelain)" ]; then
  log "변경 없음 — 커밋/push 생략"
else
  git add -A
  git commit -q -m "$MSG" || { log "커밋 실패"; exit 1; }
  log "커밋: $(git log -1 --format=%h)"
  git push --quiet "$URL" HEAD:main 2>&1 | mask || { log "push 실패"; exit 1; }
  log "push 완료"
fi

# --- 6. 사후 검증 -----------------------------------------------------------
git fetch --quiet "$URL" "main:refs/remotes/origin/main" --force 2>&1 | mask
if [ "$(git rev-list --count origin/main..HEAD)" -ne 0 ]; then
  log "경고: push 후에도 미반영분 존재"; exit 1
fi
log "검증 통과 — origin 일치"

# --- 7. 마운트 폴더 동기화 (사용자가 보는 폴더 최신화) -----------------------
log "마운트 폴더 동기화"
cd "$MOUNT_REPO" || exit 0
bash scripts/git_safe.sh --clean >/dev/null 2>&1
if [ -n "$(git status --porcelain)" ]; then
  log "마운트 폴더에 미커밋 변경 있음 — 덮어쓰지 않고 보존. 수동 확인 필요."
else
  bash scripts/git_safe.sh fetch "$URL" "main:refs/remotes/origin/main" --force >/dev/null 2>&1
  bash scripts/git_safe.sh merge --ff-only origin/main >/dev/null 2>&1 \
    && log "마운트 폴더 최신화 완료: $(git log -1 --format=%h)" \
    || log "마운트 폴더 ff-merge 불가 — 분기 상태, 수동 확인 필요"
fi

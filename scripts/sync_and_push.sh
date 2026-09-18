#!/usr/bin/env bash
# 사이클 종료 처리 — 커밋·push 완주 보장 (audit #1033)
#
# 배경: 2026-09-18 야간 사이클이 작업은 마쳤으나 커밋 단계에서 멈춰 12개 파일이 방치되고,
#       로컬 8커밋이 5주간 origin에 도달하지 못했다. 원인은 두 가지가 겹친 것:
#         (1) .git/*.lock 잔존 — 일부 실행 환경에서 파일 삭제가 막혀 락이 남으면 이후 git 명령이 전부 실패
#         (2) 커밋/push가 사이클의 '선택적 마무리'였을 뿐 보장된 단계가 아니었음
#
# 본 스크립트는 사이클 끝에서 호출되어 락 정리 → 커밋 → rebase → push 까지 완주시킨다.
# 멱등하며, 변경이 없으면 아무것도 하지 않는다.
#
# 사용: bash scripts/sync_and_push.sh "커밋 메시지"

set -uo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO" || exit 1

MSG="${1:-chore(cycle): 자동 사이클 산출물 반영}"
TOKEN_FILE="$REPO/.secrets/token.txt"
REMOTE_USER="holee9-automation"
REPO_PATH="holee9/MD-process.git"

log() { echo "[sync] $*"; }

# --- 1. 락 정리 -------------------------------------------------------------
# 삭제가 막힌 환경(마운트 제약)에서는 rm이 실패하므로 rename으로 우회한다.
clear_locks() {
  local moved=0
  for lock in "$REPO"/.git/*.lock; do
    [ -e "$lock" ] || continue
    if rm -f "$lock" 2>/dev/null; then
      moved=$((moved+1))
    elif mv "$lock" "${lock}.stale_$(date +%s)" 2>/dev/null; then
      moved=$((moved+1))
    else
      log "경고: 락 제거 실패 — $lock"
    fi
  done
  [ "$moved" -gt 0 ] && log "락 정리 ${moved}건"
  return 0
}
clear_locks

# --- 2. 커밋 ---------------------------------------------------------------
if [ -n "$(git status --porcelain)" ]; then
  git add -A || { log "git add 실패"; exit 1; }
  clear_locks
  if git commit -q -m "$MSG"; then
    log "커밋: $(git log -1 --format=%h)"
  else
    log "커밋 실패"; exit 1
  fi
else
  log "변경 없음 — 커밋 생략"
fi

# --- 3. 원격 동기화 ---------------------------------------------------------
if [ ! -f "$TOKEN_FILE" ]; then
  log "토큰 없음($TOKEN_FILE) — push 불가. 로컬 커밋까지만 완료."
  exit 1
fi
TOKEN="$(tr -d '[:space:]' < "$TOKEN_FILE")"
URL="https://${REMOTE_USER}:${TOKEN}@github.com/${REPO_PATH}"

clear_locks
# 원격추적 참조(refs/remotes/origin/main)까지 갱신한다.
# URL 직접 fetch/push 는 기본적으로 FETCH_HEAD 만 갱신하므로, 갱신하지 않으면
# `@{u}` 가 낡은 채로 남아 생존 점검이 "미push"로 오탐한다(2026-09-18 확인).
if ! git fetch "$URL" "main:refs/remotes/origin/main" --force 2>&1 | sed "s/${TOKEN}/***/g"; then
  log "fetch 실패 — 네트워크/자격증명 확인 필요"; exit 1
fi

AHEAD=$(git rev-list --count origin/main..HEAD)
BEHIND=$(git rev-list --count HEAD..origin/main)
log "동기화 전: ahead=${AHEAD} behind=${BEHIND}"

if [ "$BEHIND" -gt 0 ]; then
  clear_locks
  # 자동생성물 충돌은 재빌드로 해소 가능하므로 rebase보다 merge를 쓴다(이력 보존).
  if ! git merge origin/main --no-edit 2>&1 | tail -5; then
    log "병합 충돌 — 사람 개입 필요. push 중단(작업은 커밋되어 안전)."
    exit 2
  fi
  # 병합 후 자동생성물 재빌드
  python3 scripts/build_readiness.py >/dev/null 2>&1
  python3 scripts/build_matrix.py >/dev/null 2>&1
  python3 scripts/build_dashboard_html.py >/dev/null 2>&1
  if [ -n "$(git status --porcelain)" ]; then
    clear_locks
    git add -A && git commit -q -m "chore(build): 병합 후 자동생성물 재빌드 [skip ci]"
    log "재빌드 반영"
  fi
fi

# --- 4. push ---------------------------------------------------------------
clear_locks
if git push "$URL" main 2>&1 | sed "s/${TOKEN}/***/g" | tail -3; then
  log "push 완료 — $(git log -1 --format=%h)"
else
  log "push 실패"; exit 1
fi

# --- 5. 사후 검증 -----------------------------------------------------------
clear_locks
git fetch "$URL" "main:refs/remotes/origin/main" --force >/dev/null 2>&1
REMAIN=$(git rev-list --count origin/main..HEAD)
if [ "$REMAIN" -eq 0 ]; then
  log "검증 통과 — origin과 완전 일치"
else
  log "경고: push 후에도 미반영 ${REMAIN}건"; exit 1
fi

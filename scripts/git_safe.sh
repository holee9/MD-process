#!/usr/bin/env bash
# git 락 내성 래퍼 (audit #1034)
#
# 문제 구조:
#   git은 .git/*.lock 을 만들고 작업 후 스스로 unlink 한다. 그런데 이 저장소가 놓인
#   마운트는 삭제가 차단될 수 있어(세션 권한이 있을 때만 허용, 세션 종료 시 소멸)
#   락이 남는다. 락이 남으면 이후 **모든** git 명령이 "File exists"로 즉사한다.
#   실제로 .git 에는 과거 세션들이 손으로 치운 HEAD.lock.bak* 잔재가 쌓여 있었다.
#
# 대책:
#   - 모든 git 호출 전에 '오래된' 락을 정리한다(rm 실패 시 rename 우회 — rename은 항상 됨).
#   - 방금 생성된 락(= 다른 git이 실제 작업 중)은 건드리지 않는다. 나이로 구분한다.
#   - 정리 후에도 실패하면 명확히 보고한다(조용한 실패 금지).
#
# 사용:
#   source scripts/git_safe.sh          # 함수만 로드
#   bash scripts/git_safe.sh <git인자>  # 가드 적용된 git 1회 실행
#   bash scripts/git_safe.sh --clean    # 락 정리만 수행

GS_STALE_AFTER="${GS_STALE_AFTER:-45}"   # 초. 이보다 오래된 락은 죽은 것으로 본다.
GS_RETRY="${GS_RETRY:-3}"

_gs_repo() { git rev-parse --git-dir 2>/dev/null || echo ".git"; }

# 락 1개 제거: rm → 실패 시 rename. 성공 시 0.
_gs_drop() {
  local f="$1"
  rm -f "$f" 2>/dev/null && return 0
  mv "$f" "${f}.stale_$(date +%s%N)" 2>/dev/null && return 0
  return 1
}

# 오래된 락 정리. 정리 건수를 stdout 에 출력.
gs_clean_locks() {
  local gd n=0 age now
  gd="$(_gs_repo)"
  now=$(date +%s)
  shopt -s nullglob
  for f in "$gd"/*.lock "$gd"/refs/heads/*.lock "$gd"/refs/remotes/*/*.lock; do
    [ -e "$f" ] || continue
    age=$(( now - $(stat -c %Y "$f" 2>/dev/null || echo 0) ))
    if [ "$age" -lt "$GS_STALE_AFTER" ]; then
      echo "[git_safe] 활성 락으로 판단(${age}s) — 보존: $f" >&2
      continue
    fi
    if _gs_drop "$f"; then n=$((n+1)); else echo "[git_safe] 락 제거 실패: $f" >&2; fi
  done
  shopt -u nullglob
  echo "$n"
}

# 과거 세션들이 남긴 .lock.bak/.old/.rm/.stale 잔재 청소
gs_purge_debris() {
  local gd n=0
  gd="$(_gs_repo)"
  shopt -s nullglob
  for f in "$gd"/*.lock.* ; do
    [ -e "$f" ] || continue
    rm -f "$f" 2>/dev/null && n=$((n+1))
  done
  shopt -u nullglob
  echo "$n"
}

# 가드 적용 git 실행. 락 오류면 정리 후 재시도.
gs_git() {
  local try=1 out rc
  while : ; do
    out="$(git "$@" 2>&1)"; rc=$?
    [ $rc -eq 0 ] && { [ -n "$out" ] && echo "$out"; return 0; }
    if echo "$out" | grep -qi "File exists\|cannot lock ref\|Unable to create.*\.lock\|index\.lock"; then
      if [ "$try" -ge "$GS_RETRY" ]; then
        echo "[git_safe] 락 오류 ${try}회 — 중단" >&2; echo "$out" >&2; return $rc
      fi
      echo "[git_safe] 락 오류 감지 — 정리 후 재시도(${try}/${GS_RETRY})" >&2
      GS_STALE_AFTER=0 gs_clean_locks >/dev/null
      try=$((try+1)); sleep 1; continue
    fi
    echo "$out" >&2; return $rc
  done
}

if [ "${BASH_SOURCE[0]}" = "$0" ]; then
  case "${1:-}" in
    --clean)  echo "락 정리: $(GS_STALE_AFTER=0 gs_clean_locks)건 / 잔재 청소: $(gs_purge_debris)건" ;;
    --purge)  echo "잔재 청소: $(gs_purge_debris)건" ;;
    *)        gs_clean_locks >/dev/null; gs_git "$@" ;;
  esac
fi
# 반입 테스트 마커 211206

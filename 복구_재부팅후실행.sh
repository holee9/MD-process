#!/bin/bash
# === 재부팅 후 복구 (Git Bash) ===
# 사용법:
#   1) Windows 재부팅
#   2) Cowork·VS Code·탐색기 모두 닫은 상태 유지
#   3) Git Bash 열어서:
#        cd ~/Documents/Claude/Projects/의료기기\ 제조\ 업무규칙\ 개발
#        bash 복구_재부팅후실행.sh

set -u
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO="$SCRIPT_DIR"
PARENT="$(dirname "$REPO")"
LEAF="$(basename "$REPO")"
STAMP="$(date +%Y%m%d-%H%M%S)"
BROKEN="${LEAF}_broken_${STAMP}"

cd "$REPO" || { echo "❌ cd 실패"; exit 1; }

echo "=== 의료기기 제조 — 재부팅 후 복구 ==="
echo "  REPO: $REPO"
echo

echo "[1] index.lock 제거"
if [ -f .git/index.lock ]; then
  if rm -f .git/index.lock; then
    echo "  ✓ 제거"
  else
    echo "  ✗ 여전히 잠김 — STEP 2(rename+clone)로 진행"
  fi
else
  echo "  없음"
fi

echo "[2] 깨진 index 제거"
if [ -f .git/index ]; then
  rm -f .git/index 2>/dev/null && echo "  ✓ 제거" || echo "  ✗ 잠김"
fi

echo "[3] git status 동작 확인"
if git status --short >/dev/null 2>&1; then
  echo "  ✓ git 동작"

  echo "[4] reset --hard origin/main"
  git fetch origin main 2>&1 | tail -2
  if git reset --hard origin/main 2>&1 | tail -3 ; then
    echo
    echo "=== ✓ 복구 완료 ==="
    git log --oneline -3
    echo
    git status --short
    exit 0
  fi
fi

echo
echo "[fallback] rename + fresh clone"

# 토큰 백업
TOKEN_FILE="$REPO/.secrets/token.txt"
if [ ! -f "$TOKEN_FILE" ]; then
  echo "❌ 토큰 없음: $TOKEN_FILE"
  exit 1
fi
TOKEN="$(tr -d '[:space:]' < "$TOKEN_FILE")"
TMP_TOKEN="/tmp/mdp-token-$STAMP.txt"
cp "$TOKEN_FILE" "$TMP_TOKEN"
echo "  ✓ 토큰 백업"

cd "$PARENT" || exit 1

echo "  rename: $LEAF → $BROKEN"
if mv -- "$LEAF" "$BROKEN"; then
  echo "  ✓ rename 성공"
else
  echo "  ✗ rename 실패 — 모든 앱 종료 후 다시 재부팅 필요"
  exit 1
fi

echo "  fresh clone..."
URL="https://holee9-automation:${TOKEN}@github.com/holee9/MD-process.git"
if git clone "$URL" "$LEAF"; then
  echo "  ✓ clone 성공"
else
  echo "  ✗ clone 실패 — rollback"
  mv -- "$BROKEN" "$LEAF"
  exit 1
fi

mkdir -p "$LEAF/.secrets"
cp "$TMP_TOKEN" "$LEAF/.secrets/token.txt"
rm -f "$TMP_TOKEN"
echo "  ✓ 토큰 복원"

cd "$LEAF"
echo
echo "=== ✓ 복구 완료 (rename+clone) ==="
git log --oneline -3
echo
git status --short
echo
echo "이전 폴더: $PARENT/$BROKEN  (재부팅 후 수동 삭제)"

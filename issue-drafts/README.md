# issue-drafts

이 폴더의 `*.md` 파일은 **GitHub Actions**(`.github/workflows/auto-issue.yml`)에 의해
자동으로 GitHub Issues로 생성/동기화됩니다.

## 규칙

1. 파일 이름은 유일 키로 사용됩니다 — **한 번 정하면 변경 금지** (`_log.json`으로 매핑됨).
2. 파일 선두에 YAML frontmatter 필수: `title`, `labels`, (선택) `state`.
3. `_`로 시작하는 파일(`_TEMPLATE.md`, `_log.json`)은 무시됩니다.
4. 본문은 frontmatter 아래 전체. 수정 후 push 하면 이슈 본문 자동 업데이트.
5. 이슈를 닫을 때는 `state: closed` 추가, 다시 열 때는 `state: open`.

## 워크플로

```
Claude 스케줄러 → issue-drafts/NNN_*.md 생성/수정 → main push
                                                    ↓
                                     GitHub Actions: auto-issue.yml
                                                    ↓
                          신규: 이슈 생성 + _log.json 기록
                          기존: 이슈 제목/본문 업데이트 (±상태 변경)
```

## 파일명 권장 규칙
`NNN_분류_간단제목.md` — 예: `001_git_repo_점검.md`, `002_qms_절차_초안.md`

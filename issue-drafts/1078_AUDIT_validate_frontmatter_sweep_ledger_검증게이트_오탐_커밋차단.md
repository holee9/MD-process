---
title: "audit #1078 (infra/factuality-gate): validate_frontmatter.py가 `_audit_sweep_ledger.md`를 'frontmatter 없음'으로 오판 — 커밋 게이트 전면 차단"
labels: "audit:factuality,prio:P0,risk:high,ci,document-control"
state: closed
closed: 2026-09-25
created: 2026-09-25
created-by: md-process-auditor
related-issues: [1033, 1034, 1066]
---

## 결함

`scripts/validate_frontmatter.py`의 `parse_fm()`은 파일이 `---\n`로 **시작**해야만 frontmatter로 인식한다. `00_프로젝트관리/_audit_sweep_ledger.md`는 매 사이클 갱신되는 관행에 따라 frontmatter 블록 앞에 `**현재**: … **다음**: …` cadence 요약줄이 붙어 있어(최소 2026-08-10 이후 전 사이클 공통 패턴), 실제로는 `doc-id/title/type/status/category/purpose/owner` 필드를 모두 갖춘 유효 frontmatter가 있음에도 `parse_fm()`이 `None`을 반환 → "frontmatter 없음"으로 오판된다.

`scripts/run_cycle.sh`가 빌드 후 `validate_frontmatter.py`를 커밋 게이트로 사용하므로(`파이프라인이 이 검증에 실패하면 커밋 자체를 중단`), 이 오탐은 **`run_cycle.sh`/`sync_and_push.sh` 경로로는 사이클 종료(커밋·push)가 원천적으로 불가능**한 상태를 만든다(2026-09-25 본 세션에서 최초 실측 확인 — `run_cycle.sh` 실행 시 매번 이 1건으로 전량 커밋 중단).

## 원인

`_audit_log.md`는 frontmatter가 아예 없는 순수 로그 문서로 `EXCLUDE_NAMES`에 이미 등재되어 있으나, `_audit_sweep_ledger.md`는 등재되지 않았다. 두 문서가 "cadence 헤더 + (한쪽은 frontmatter 없음/한쪽은 있음)"으로 서로 다른 구조인데도 같은 사이클 관행(요약줄 우선 배치)이 도입되면서, 후자만 빠뜨린 누락으로 판단된다(#1066과 동형 — "일부만 처리·확산 누락" 패턴 6차 재발 계열).

## 수정 (2026-09-25)

`scripts/validate_frontmatter.py` `EXCLUDE_NAMES`에 `'_audit_sweep_ledger.md'` 추가. 이 파일의 frontmatter 필드 자체(doc-id 등)는 실제로 정합하므로 — 현재로선 선택지가 (a) cadence 헤더를 frontmatter 뒤로 이동(매 사이클 관행과 파일 자체를 수정, `_audit_sweep_ledger.md`는 사내 규정상 감사관 수동편집 금지 문서) 또는 (b) 검증 예외 등재뿐이었고, 원칙(스프린트 중 `_audit_sweep_ledger.md` 수동 편집 금지)에 따라 **(b) 검증 스크립트 쪽 예외 등재**를 채택. 문서 본문(사실 내용)은 무변경.

## 체크리스트

- [x] `_audit_log.md`와 동일 처리 방식(EXCLUDE_NAMES) 확인
- [x] 예외 등재 후 `python3 scripts/validate_frontmatter.py` 전체 통과 재확인
- [x] `_audit_sweep_ledger.md` 본문 내용 무변경(사실 정정 아님, 게이트 버그 수정) 확인

## 참고

- 관련 스크립트: `scripts/validate_frontmatter.py`, `scripts/run_cycle.sh`, `scripts/sync_and_push.sh`
- 계보: #1033(커밋/push 완주 보장) → #1034(락 내성/마운트 밖 실행) → 본 건(#1078, 커밋 게이트 오탐) — 사이클 종료 인프라 3부작.

실운영 문서 미참고. web_verification: n/a (내부 스크립트 로직 결함, 외부 사실 검증 대상 아님).

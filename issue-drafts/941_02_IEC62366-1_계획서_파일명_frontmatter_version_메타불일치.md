---
title: "[chore P2] IEC_62366-1_사용적합성_엔지니어링_계획서 — 파일명 v0.1 ↔ frontmatter version v0.3 메타불일치"
labels: "type:chore,source:emergent,prio:P2,risk:low"
state: open
created: 2026-07-02
created-by: holee9-builder
related-issues: [930]
target-doc: 02_품질경영시스템_QMS/IEC_62366-1_사용적합성_엔지니어링_계획서_v0.1.md
---

## 배경
audit #930 비고에서 지적된 메타불일치가 v0.3 갱신으로 격차가 더 벌어짐. 파일명은 여전히 `_v0.1.md`, frontmatter `version: v0.3`.

## 판정
**메타불일치 (P2, chore)** — 사실오류는 아니나 파일명이 SSOT 검색·문서_매트릭스 링크 무결성에 영향. 파일명 변경은 `절대 금지 — 파일명 변경` 규칙과 상충하므로, 다음 rename 사이클(별도 리팩터 세션)에서 문서_매트릭스 링크·자매문서 참조 동시 갱신 필요.

## DoD
- [ ] 파일명 변경 정책 재확인 (README/이슈관리규칙)
- [ ] 승인 후 v0.3 반영 rename 및 자매 링크(01_법규, 03_설계 참조 grep) 일괄 갱신
- [ ] 문서_매트릭스 자동 재빌드 확인

## 우선순위
P2 — 사실성 영향 없음, 유지보수성 개선.

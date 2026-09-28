---
title: "fix(scoring): build_readiness — status:draft 골격 문서 '충족' 판정 금지 (FDA RTA 83% 과대평가)"
labels: bug,compliance,review
state: open
created: 2026-09-28
created-by: md-process-quarterly
related-issues: [931, 1521, 208]
priority: P0
target-date: 2026-10-09
---

## 사실 근거

| 항목 | 값 |
|---|---|
| FDA RTA 점수 | 0%(06-28) → 83%(09-28) |
| 충족 판정 매칭 문서 | T-FDA510K-A1~A5, B1~B3, C2, E1, E2 (11건) |
| 해당 문서 상태 | 전부 `status: draft`, `v0.1`, "제품별 실 데이터 작성 예정" |
| 채점 로직 | `scripts/build_readiness.py` `score_item` — 문서 status 미참조 |
| #931 | open (실데이터 미기입) |

## 체크리스트
- [ ] `score_item`에 매칭 문서 status 가중 도입 (draft → 최대 '부분(골격)' 판정, approved만 '충족')
- [ ] 템플릿(`T-` 접두) 문서는 must 항목 단독 충족 근거에서 제외
- [ ] 재채점 후 주간 갭분석에 보정 전/후 병기
- [ ] 회귀 테스트: ISO 13485 점수 변동 영향 확인

## 참고
- `12_교차검증_보고서/분기_종합_2026-Q3.md` §2.1

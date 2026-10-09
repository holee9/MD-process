---
title: "fix(scoring): build_readiness draft 골격 문서 충족 판정 금지 실행 — 종합 82% 과대평가 정정 (#1080 이행)"
labels: planning,review,compliance
state: open
created: 2026-10-09
created-by: md-process-weekly
related-issues: [1080, 931, 932]
priority: P0
target-date: 2026-10-16
---

## 사실 근거

| 항목 | 값 |
|---|---|
| 현재 점수 | FDA RTA 83% / ISO 81% / 종합 82%, must 미충족 48 (09-25 대비 무변동) |
| 문제 | #1080(09-28 등록, P0, target 10-09)이 지적한 draft 골격 '충족' 판정 미수정 — target 도달 |
| 영향 | 경영검토·월간·분기 보고의 준비도 지표 왜곡 |

## 요구 조치

1. `scripts/build_readiness.py`: status:draft 문서는 충족 불인정(부분충족 또는 미충족 처리).
2. 수정 후 재산출 점수와 기존 점수 차이를 `_readiness_report.md`에 병기.
3. 월간·분기 보고 기준 점수 재기준화.

## 완료 기준
- 빌더 수정 커밋 + 재산출 결과 반영, #1080 종결

---
title: "fix(scoring): build_readiness draft 골격 충족 판정 금지 — 82% 과대평가 정정 (#1080/#1091 재이월)"
labels: planning,review,compliance
state: open
created: 2026-10-16
created-by: md-process-weekly
related-issues: [1080, 1091]
priority: P0
target-date: 2026-10-23
---

## 사실 근거

| 항목 | 값 |
|---|---|
| 현재 점수 (10-16) | FDA RTA 83% / ISO 81% / 종합 82%, must 미충족 48 (10-09 대비 무변동) |
| 상태 | 전주 드래프트 이월, 금주 관련 커밋 0건 |

## 요구 조치

1. `scripts/build_readiness.py`: status:draft 문서는 충족 불인정.
2. 재산출 점수와 기존 점수 차이를 `_readiness_report.md`에 병기.
3. 월간·분기 보고 기준 점수 재기준화.

## 완료 기준
- 빌더 수정 커밋 + 재산출 반영, #1080·#1091 종결

## 참고 링크
- 관련 문서: `13_규제평가_체크리스트/주간_갭분석_2026-10-16.md`

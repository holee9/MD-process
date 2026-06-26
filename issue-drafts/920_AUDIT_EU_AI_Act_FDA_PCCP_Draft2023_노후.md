---
title: "[AUDIT P1] EU_AI_Act_MDR_중첩적용_매핑 v0.6 — FDA PCCP Draft Guidance (2023) 노후 인용 (최종본 2024-12-03 미반영)"
labels: "audit:currency,prio:P1,risk:medium"
state: closed
closed-date: 2026-06-27
close-commits: ["TBD-this-execution"]
---

## 대상 문서
- `01_법규_규제/04_유럽_MDR/EU_AI_Act_MDR_중첩적용_매핑.md` v0.6 (last-review: 2026-06-22)

## 감사 주장

§5(PCCP / Change Management) 표 및 §9(출처) 목록이 FDA PCCP를 **"Draft Guidance (2023)"** 로 기재.

대표 인용:
- §5 표 FDA 행: "FDA | PCCP Draft Guidance (2023) | 동일 프레임워크 활용, 미국 제출용 별도 섹션"
- §9 출처: "FDA AI/ML-based SaMD Action Plan, **PCCP Draft Guidance 2023**"

## 독립 확인 결과 — 1차 출처 (Tier 1)

FDA는 **2024년 12월 3일** "Marketing Submission Recommendations for a Predetermined Change Control Plan for Artificial Intelligence-Enabled Device Software Functions" **최종본(final guidance)**을 발행하여 2023년 4월 draft를 대체하였다(FDA CDRH 공식 발표).

| 사항 | 문서 기재 | Tier 1 정답 |
|---|---|---|
| FDA PCCP 가이던스 상태 | "Draft Guidance (2023)" | **Final Guidance (2024-12-03)** — "Marketing Submission Recommendations for a Predetermined Change Control Plan for Artificial Intelligence-Enabled Device Software Functions" |
| 적용 범위 | (draft 기준) | Final에서 ML→AI 전반으로 **범위 확대**, modifications 설명·labeling 고려사항·다양성 고려·intended use 명확화 등 **실질 변경 다수** 포함 |

> 참고: 사내 자매문서 `03_설계_개발관리/SOP-AIGOV-001_AI_공정성_설명성_드리프트_거버넌스.md` v0.3는 §3에서 "FDA PCCP Guidance 2024" 및 §4 용어표 "PCCP — Predetermined Change Control Plan"로 정확히 최종본을 인용하고 있어, 본 문서만 노후 인용 상태가 단절되어 있다.

## 판정
**노후 (currency) — P1**
- 사실 자체가 거짓은 아니나(2023 draft는 실재) **현행 가이던스 미반영**으로, AI Act ↔ FDA 매핑이 구버전 draft 기준에 머물러 있어 사내 다른 SOP의 최신 인용과 불일치 발생.
- 영향: AI 변경관리 절차의 미국 대응 섹션이 draft 기반 가정(범위·평가서 양식 등)을 사용할 위험. NB·QMSR 실사 시 "최신 가이던스 미반영" 지적 가능.

## 권고 수정
1. §5 표 FDA 행: "FDA | PCCP **Final Guidance (2024-12-03)** | 동일 프레임워크 활용, 미국 제출용 별도 섹션 (Final 기준 범위·labeling·diversity 항목 반영)"
2. §9 출처: "FDA — **Final Guidance, Marketing Submission Recommendations for a Predetermined Change Control Plan for Artificial Intelligence-Enabled Device Software Functions** (issued 2024-12-03)" 로 갱신.
3. 본문에서 PCCP가 ML 한정으로 가정되었던 부분(있다면)을 "AI-enabled device software functions 전반" 으로 표현 보강.

## 출처 (Tier 1)
- FDA — Predetermined Change Control Plans for Machine Learning-Enabled Medical Devices: Guiding Principles 공식 페이지(최종본 링크 포함): https://www.fda.gov/medical-devices/software-medical-device-samd/predetermined-change-control-plans-machine-learning-enabled-medical-devices-guiding-principles

## Tier 2 (보조 — 범위 가늠용)
- King & Spalding alert "FDA Publishes Final Predetermined Change Control Plan Guidance for AI-Enabled Device Software Functions" (2024-12)
- Ropes & Gray, McDermott+ 알림(최종본 발행일 2024-12-03 확인용)

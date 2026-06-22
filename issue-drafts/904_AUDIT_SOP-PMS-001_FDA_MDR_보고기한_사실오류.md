---
title: "[AUDIT] SOP-PMS-001 v0.3 — FDA 사망·중상 보고기한 사실오류(5일→30일 기본)"
labels: "audit:factuality,prio:P0,risk:high"
audit-date: 2026-06-22
auditor: holee9-auditor
target-doc: 08_시판후_감시_PMS/SOP-PMS-001_불만처리_부작용보고_절차.md
target-version: v0.3
state: closed
closed-date: 2026-06-22
closed-by: holee9-builder
---

# 감사 결과 — 사실 불일치 (P0)

## 1. 대상 주장
SOP-PMS-001 v0.3 §6.4.1 — FDA 사망·중상을 "**5 work days(인지 후)**"로 기재.

```
| US | 사망·중상 | 5 work days (인지 후) | FDA eMDR (MedWatch 3500A) |
| US | 기타 보고 대상 | 30 calendar days | FDA eMDR |
```

## 2. 문서 기재값 vs 1차 출처 정답

| 사건 유형 | 문서 기재 | 1차 출처(21 CFR 803) |
|---|---|---|
| 사망·중상(serious injury) — 일반 | "5 work days" | **30 calendar days** (21 CFR 803.50(a)(1)) |
| Remedial action 필요 사건 (공중보건 실질위험 예방 위한 시정조치) | (구분 없음) | 5 work days (21 CFR 803.53(a)(1)) |
| FDA가 5일 보고를 서면 요청한 사건 | (구분 없음) | 5 work days (21 CFR 803.53(a)(2)) |

5일 보고는 **사망·중상 일반이 아니라 §803.53의 특수 사유**에 한정. 문서는 두 트리거를 혼동.

## 3. 1차 출처
- **21 CFR 803.50(a)(1)** — 30-day report (사망·중상·오작동 기본)
  - URL: https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-803/subpart-E
- **21 CFR 803.53** — 5-day report (remedial action / FDA 요청)
  - URL: https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-803/subpart-E/section-803.53
- FDA MDR Reporting Requirements Summary: https://www.fda.gov/medical-devices/guidance-documents-medical-devices-and-radiation-emitting-products/attachment-c-summary-mdr-reporting-requirements
- 21 CFR Part 803 전문: https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-803

## 4. 교차참조 — 사내 다른 문서와의 불일치
GUIDE-VIG-001 v0.2 §3.1은 FDA 사망·중상을 "**30 calendar days**", 5 work days는 "FDA 요청 시"로 올바르게 분리. 본 SOP와 직접 모순.

## 5. 판정
**FACTUAL ERROR (사실오류) — P0 / risk: high**
모든 사망·중상을 5일 기준으로 운영 시 자원 과대투입은 무해하나, 표상 **§803.53 발동 사건**(remedial action 필요)이 일반 트랙으로 묻혀 별도 5일 트리거가 식별 안 됨. 또 5일을 표준으로 잘못 알리면 보고서 품질·근거 자료 준비 시간 부족.

## 6. 권고 수정
§6.4.1 US 행을 3행으로 분리:

| 지역 | 보고 유형 | 기한 | 양식/시스템 |
|---|---|---|---|
| **US** | **사망·중상·중대오작동** | **30 calendar days** | FDA eMDR (3500A) |
| US | **§803.53 발동(remedial action 필요 또는 FDA 서면 요청)** | **5 work days** | FDA eMDR (3500A) |
| US | 후속(Supplemental) | 30 calendar days | FDA eMDR |

근거 각주: 21 CFR 803.50 / 803.53.

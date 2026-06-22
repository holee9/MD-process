---
title: "[AUDIT] SOP-PMS-001 v0.3 — EU MDR 사망 보고기한 사실오류(2일→10일)"
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
SOP-PMS-001 v0.3 §6.4.1 "보고 기한" 표 — EU 사망/심각위협을 **2일**로 통합 기재.

```
| 지역 | 보고 유형 | 기한 |
| EU   | 중대 AE (사망·심각 위협) | 2일 |
| EU   | 기타 중대 AE | 15일 |
```

## 2. 문서 기재값 vs 1차 출처 정답

| 사건 유형 | 문서 기재 | 1차 출처(EU MDR Art.87(3)) |
|---|---|---|
| **사망 / 예상치 못한 심각한 건강악화** | "2일" | **10일** (즉시, 늦어도 10일 이내) |
| **심각한 공중보건 위협(serious public health threat)** | (사망과 묶음) | **2일** (즉시, 늦어도 2일 이내) |
| 기타 중대사고 | 15일 | 15일 (일치) |

문서는 "사망"과 "심각 공중보건 위협" 두 유형을 **2일 칸으로 잘못 통합**했다. 사망은 10일, 2일은 공중보건 위협 한정.

## 3. 1차 출처
- **EU MDR 2017/745 Article 87(3)**
  - 원문 요지:
    - serious public health threat → "immediately... not later than **2 days**"
    - death or unanticipated serious deterioration → "immediately... not later than **10 days**"
    - any other serious incident → "immediately... not later than **15 days**"
  - URL: https://eur-lex.europa.eu/eli/reg/2017/745/oj/eng
  - 보조: https://www.medical-device-regulation.eu/2019/07/16/mdr-article-87-reporting-of-serious-incidents-and-field-safety-corrective-actions/
- MDCG 2023-3 Rev.2 (Vigilance Guidance) — 동일 기한
  - URL: https://health.ec.europa.eu/document/download/af1433fd-ed64-4c53-abc7-612a7f16f976_en

## 4. 교차참조 — 사내 다른 문서와의 불일치
GUIDE-VIG-001 v0.2 §3.1은 "EU 사망 10일 / 즉각 위험 2일 / 공중보건 위협 2일"로 **올바르게** 분리 기재 → 본 SOP와 직접 모순.

## 5. 판정
**FACTUAL ERROR (사실오류) — P0 / risk: high**
사망 사건을 2일 기준으로 운영 시 자원 과대투입은 무해하나, 표 구조상 **공중보건 위협을 사망과 동일 트랙으로 처리**해 별도 2일 트리거 식별이 누락될 위험. 반대로 사망 외 사건(즉각위험)을 10/15일로 운영 시 **2일 기한 위반**.

## 6. 권고 수정
§6.4.1 EU 행을 3행으로 분리:

| 지역 | 보고 유형 | 기한 | 양식/시스템 |
|---|---|---|---|
| EU | **심각한 공중보건 위협** | **2일** | EUDAMED MIR v7.3.1 |
| EU | **사망·예상치 못한 심각한 건강악화** | **10일** | EUDAMED MIR v7.3.1 |
| EU | 기타 중대 AE | 15일 | EUDAMED MIR v7.3.1 |

근거 각주: EU MDR Art.87(3).

---
title: "[AUDIT] GUIDE-VIG-001 — FDA MDR 기록보존기한 사실오류(수입 3년→2년)"
labels: "audit:factuality,prio:P0,risk:high"
audit-date: 2026-06-22
auditor: holee9-auditor
target-doc: 08_시판후_감시_PMS/GUIDE-VIG-001_안전경계_보고_요건_통합_가이드.md
target-version: v0.2
---

# 감사 결과 — 사실 불일치 (P0)

## 1. 대상 주장
GUIDE-VIG-001 v0.2 §6 "보고 기록 및 보존" — FDA 보존기한이 "**2년(제조)/3년(수입)**"로 기재됨.

```
| 보고 기록 보존 기간 | MFDS: 5년, FDA: 2년(제조)/3년(수입), EU: 10년(Class III)/15년(임플란트) |
```

## 2. 문서 기재값 vs 1차 출처 정답

| 항목 | 문서 기재 | 1차 출처 정답 |
|---|---|---|
| FDA MDR 보존기한 (제조자) | 2년 | 2년 또는 기기 수명 中 더 긴 기간 |
| FDA MDR 보존기한 (수입자) | **3년** | **2년 또는 기기 수명 中 더 긴 기간** (제조자와 동일) |

## 3. 1차 출처
- **21 CFR 803.18(b)(1)** — Medical Device Reporting, Recordkeeping
  - 원문 요지: User facility, importer, manufacturer 공통으로 MDR event file을 사건 발생일로부터 **2 years**, 또는 expected life of the device 중 더 긴 기간 보존.
  - URL: https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-803/subpart-A/section-803.18
- 21 CFR Part 803 전문: https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-803

## 4. 판정
**FACTUAL ERROR (사실오류) — P0 / risk: high**
수입자 보존기한 "3년"의 1차 출처 없음. 현행 21 CFR 803.18은 수입자도 2년(또는 기기 수명).

## 5. 권고 수정
§6 보존기간 행을 다음으로 수정:

```
FDA: 2년 또는 기기 예상수명 中 더 긴 기간 (제조자·수입자·User Facility 공통; 21 CFR 803.18)
```

## 6. 부속 결함 — EU 보존기한 인용 부정확 (P1, 별도 처리 권장)
"EU: 10년(Class III)/15년(임플란트)" 표기는 오해 소지. EU MDR Art.10(8) 정확 표현은 **"비임플란트 전체 10년, 임플란트 15년"**. Class III 한정 조건 아님. → 별도 audit 이슈로 분리 등록.

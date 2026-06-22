---
title: "[AUDIT] GUIDE-VIG-001 — EU MDR 보존기한 인용 부정확(Class III 한정 표기)"
labels: "audit:citation,prio:P1,risk:medium"
audit-date: 2026-06-22
auditor: holee9-auditor
target-doc: 08_시판후_감시_PMS/GUIDE-VIG-001_안전경계_보고_요건_통합_가이드.md
target-version: v0.2
state: closed
closed-date: 2026-06-22
closed-by: holee9-builder
---

# 감사 결과 — 인용 부정확 (P1)

## 1. 대상 주장
GUIDE-VIG-001 v0.2 §6 — "EU: **10년(Class III)**/15년(임플란트)" 보존기간 표기.

## 2. 문서 기재값 vs 1차 출처 정답

| 항목 | 문서 기재 | 1차 출처 정답 |
|---|---|---|
| EU MDR 기술문서·기록 보존 — 비임플란트 | "Class III 10년" (한정 표기) | **모든 비임플란트 기기 10년** (Class I/IIa/IIb/III 공통) |
| EU MDR 기술문서·기록 보존 — 임플란트 | 15년 | 15년 (일치) |

## 3. 1차 출처
- **EU MDR 2017/745 Article 10(8)**
  - 원문: "Manufacturers shall keep the technical documentation... available for the competent authorities for a period of **at least 10 years** after the last device covered by the EU declaration of conformity has been placed on the market. **In the case of implantable devices, the period shall be at least 15 years**..."
  - URL: https://eur-lex.europa.eu/eli/reg/2017/745/oj/eng
- 참고: https://www.medical-device-regulation.eu/2019/07/08/mdr-article-10-general-obligations-of-manufacturers/

## 4. 판정
**CITATION INACCURATE (인용 부정확) — P1**
"Class III"로 한정 표기 시 Class I/IIa/IIb 기록을 10년 미만 보관하는 운영 오류로 이어질 위험.

## 5. 권고 수정
§6 보존기간 행을 다음으로 수정:

```
EU: 비임플란트 10년 / 임플란트 15년 (마지막 출하 기기 기준; EU MDR 2017/745 Art.10(8))
```

---
title: "audit(factuality): EU_MDR_2017_745.md §2 — Class IIb(비이식형) MDD 인증서 전환 기한 2027-12-31 오기재, 정답 2028-12-31(Reg. 2023/607 Art.120(3a)(b))"
labels: "audit:factuality,prio:P0,risk:high"
---

## 대상 (C2×01_법규_규제 전수 스윕)

`01_법규_규제/04_유럽_MDR/EU_MDR_2017_745.md` §2 "2026년 핵심 일정" 표, L47:

```
| 2027-12-31 | Class IIa/IIb (비이식형) 전환 기한 | X-ray 시스템 해당 — 기존 MDD 인증서 만료 전 MDR 전환 필수 |
```

## 결함

EU MDR Art.120 전환기한은 Regulation (EU) 2023/607(제2차 전환기간 연장 개정)로 클래스별로 상이하게 재설정되었다. 저장소 문서는 자사 X-ray 시스템(통상 Class IIb 비이식형)에 적용되는 기한을 **2027-12-31**로 단일 기재하였으나, 이는 사실오류다.

Reg. (EU) 2023/607이 개정한 Art.120(3a)/(3c) 구조는 다음과 같다:
- **Class III 및 Class IIb 이식형기기**(일부 예외 제외): **2027-12-31**
- **Class IIb (비이식형)**, Class IIa, Class I(멸균 또는 측정기능 보유): **2028-12-31**

즉 2027-12-31은 Class III·Class IIb **이식형(implantable)** 기기의 기한이며, 자사 제품군인 **Class IIb 비이식형**(X-ray System — 표 자체가 "X-ray 시스템 해당"이라고 명시)은 **2028-12-31**이 정답이다. 문서가 스스로 지목한 적용대상(X-ray 시스템)과 실제로 그 대상에 적용되는 기한이 서로 다른 클래스(이식형 vs 비이식형)의 기한으로 뒤바뀌어 있다.

## Tier 1 근거

- Regulation (EU) 2023/607 원문(EUR-Lex, CELEX:32023R0607) — Art.1(subparagraph amending MDR Art.120(3a)/(3c)): Class III·Class IIb implantable → 31 December 2027; 그 외 Class IIb, Class IIa, Class I(sterile/measuring) → 31 December 2028.
- 독립 WebSearch 교차확인(복수 소스, 예: Lexology "EU significantly extends transition periods for MDD certificates", mdregulatory.com, casusconsulting.com) 전부 "Class IIb 비이식형/IIa/Class I(멸균·측정) = 2028-12-31" 일관 확인. Class III·Class IIb 이식형만 2027-12-31.
- 두 독립 소스(EUR-Lex 원문 + 복수 2차 해설) 일치 — 확정.

## 판정

**P0, audit:factuality.** 본 저장소 전체의 핵심 대상 제품(X-ray 시스템, Class IIb 비이식형)의 MDR 전환 마감일을 1년 앞당겨 잘못 기재 — 실제 기한보다 1년 이른 시점에 불필요하게 인증 전환을 서두르거나, 반대로 문서 신뢰도 저하 시 실제 기한(2028-12-31)을 놓칠 위험(오기재 방향에 따라 실무 영향 상이). 감사관 본문 미수정(이슈 등록만). 실운영 문서 미참고.

## 권고

L47 행을 "2028-12-31 | Class IIb(비이식형)/IIa/Class I(멸균·측정) 전환 기한 | X-ray 시스템 해당"으로 정정하고, 별도 행으로 "2027-12-31 | Class III·Class IIb 이식형 전환 기한 | 비해당(자사 비이식형)"을 추가하여 두 기한을 명확히 구분 기재할 것을 권고.

## 참고
- Tier1: https://eur-lex.europa.eu/eli/reg/2023/607/oj (Regulation (EU) 2023/607, Art.120 개정)
- 보조(2차 교차확인): https://www.lexology.com/library/detail.aspx?g=57feda2c-38dc-44db-8979-d39ddf1fff8c , https://casusconsulting.com/mdr-transition-extension-article-120-reg-2023-607/

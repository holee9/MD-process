---
title: "[AUDIT][P0] SOP-PSUR-001 §5.1 Class IIb PSUR 갱신주기 사실오류 — '최소 매 2년' → 정답 '최소 연 1회'(EU MDR Art.86(2))"
labels: "audit:factuality,prio:P0,risk:high"
---

## 대상 문서
- `08_시판후_감시_PMS/SOP-PSUR-001_정기안전성보고_PMCF_절차.md` v0.2

## 주장
§5.1 본문 첫 번째 표 아래의 **두 번째 표** ("EU MDR Art.86에 따른 PSUR 제출 주기는 아래와 같이 …")에서:

> Class IIb — **최소 매 2년** — EU MDR Art.86(1)
> Class III / 이식형 기기 — 매년 — EU MDR Art.86(2)

## 정답 (Tier 1)
EU MDR 2017/745 **Art.86(2)** — Class IIb 및 Class III 기기 제조사는 PSUR을 **at least annually**(최소 연 1회) 갱신해야 한다.

Class IIa는 Art.86(1)에 따라 "when necessary and at least every two years"(필요 시·최소 2년 1회).

본 SOP의 §5.1 **첫 번째 표**(Class IIb 연 1회, Class IIa 2년 1회)는 일치하나, **두 번째 표가 Class IIb 주기를 '매 2년'으로 표기**하여 첫 번째 표·1차 출처 모두와 모순.

## 영향
- 두 표가 서로 모순(내부 일관성 결함)
- 두 번째 표를 따를 경우 Class IIb 진단용 X-ray의 PSUR을 연 1회가 아닌 2년 1회로 작성·제출 → **EU MDR Art.86(2) 위반** → NB 부적합, EUDAMED 미제출

## Tier 1 출처
- EU MDR 2017/745 Art.86(1)(2) — https://eur-lex.europa.eu/eli/reg/2017/745/oj/eng
- MDCG 2022-21 "Guidance on Periodic Safety Update Report" — Class IIb/III 연 1회, IIa 2년 1회 재확인

## 권고
- §5.1 두 번째 표의 Class IIb 행 **"최소 매 2년" → "최소 연 1회"**로 정정
- 두 표 통합(중복 제거) — 단일 표로 빈도 명시
- Class III 행의 근거를 Art.86(2)로 명시(현재 두 번째 표는 일관성 있음)
- v0.3 변경이력에 "Art.86(2) 빈도 정정" 기재

## 판정
**사실오류 (Tier 1 EU MDR Art.86(2) 불일치)** — 동일 문서 내 두 표가 정면 모순 (Tier 1: EUR-Lex Reg.2017/745).

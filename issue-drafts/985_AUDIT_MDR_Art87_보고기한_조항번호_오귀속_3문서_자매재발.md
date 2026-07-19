---
title: "audit(factuality): EU MDR Art.87 보고기한 조항번호 오귀속 — (2)/(3)/(4) 오배정, 실제는 (3)일반15일/(4)공중보건2일/(5)사망10일 (3문서 자매재발, audit #929 기 '정정' 자체 오류)"
labels: "audit:factuality,prio:P0,risk:high"
state: closed
closed: 2026-07-20
---

## 대상 (C1×08_시판후_감시_PMS 전수 스윕)

- `08_시판후_감시_PMS/PMS_개요.md` L108, L142(주변 서술)
- `08_시판후_감시_PMS/GUIDE-VIG-001_안전경계_보고_요건_통합_가이드.md` L65 (각주 ³)
- `08_시판후_감시_PMS/SOP-PMS-001_불만처리_부작용보고_절차.md` L137-139 (§6.4.1 보고기한 표)

## 결함

Regulation (EU) 2017/745 Art.87 원문(구조):
- **Art.87(3)** — 일반 중대사고(serious incident) 보고: 인지 후 **15일**
- **Art.87(4)** — "Notwithstanding paragraph 3" — **공중보건에 대한 심각한 위협**: 즉시, 늦어도 **2일**
- **Art.87(5)** — "Notwithstanding paragraph 3" — **사망 또는 예기치 않은 심각한 건강 악화**: 즉시, 늦어도 **10일**

즉 조항번호 순서는 (3)=기타/일반(15일) → (4)=공중보건위협(2일) → (5)=사망(10일)이다. 저장소 3개 문서는 이를 **(2)/(3)/(4)로 오배정**:

1. **PMS_개요.md L108**: "Art.87(3) 사망…10일 / Art.87(2) 공중보건…2일 / Art.87(4) 기타…15일" — 3개 항목 모두 실제 조항번호와 불일치(정답 각각 (5)/(4)/(3)).
2. **GUIDE-VIG-001 L65 각주³**: "EU MDR 2017/745 Art.87(3) — 공중보건 위협 2일 / 사망 10일 / 기타 중대사고 15일" — 단일 조항 (3)을 세 항목 전부의 근거로 뭉뚱그려 인용. (3)은 실제로 "기타 15일" 항목에만 해당.
3. **SOP-PMS-001 L137-139**: "Art.87(3)(a)"(공중보건 2일)/"Art.87(3)(b)"(사망 10일)/"Art.87(3)(c)"(기타 15일) — **원문에 존재하지 않는 하위 문자 조항(3)(a)/(3)(b)/(3)(c) 형식을 창작**. Art.87(3)에는 (a)(b)(c) 세부 항목이 없으며, 세 항목은 각각 독립된 paragraph (3)/(4)/(5)이다.

**일수(2일/10일/15일) 자체는 3개 문서 모두 정확** — 이번 결함은 오직 조항번호(paragraph 식별자) 오귀속.

## 재발 계보

기존 audit #929(closed, 2026-07-02)가 "EU 사망=2일" 오류를 "Art.87(2)=2일공중보건/Art.87(3)=10일사망/Art.87(4)=15일기타"로 '정정'했으나, 이 정정 자체의 조항번호 배정이 원문과 불일치(정답은 (4)/(5)/(3)). 해당 오정정이 PMS_개요.md·GUIDE-VIG-001에 전파되었고, SOP-PMS-001은 별도로 존재하지 않는 (3)(a)/(3)(b)/(3)(c) 세부문자 형식으로 동일 오류를 재생산.

## Tier 1 근거

- Regulation (EU) 2017/745 Art.87 원문 전체 직접 확보(1차 출처 재게시 사이트 medical-device-regulation.eu가 조문 전문을 그대로 인용 — paragraph 1~11 전체 대조): paragraph 3="general…not later than 15 days", paragraph 4="Notwithstanding paragraph 3, in the event of a serious public health threat…not later than 2 days", paragraph 5="Notwithstanding paragraph 3, in the event of death…not later than 10 days".
- 독립 WebSearch 스니펫(별도 소스)도 "Paragraph 4=공중보건위협 2일 / Paragraph 5=사망 10일 / Paragraph 3=일반 15일" 동일 구조로 교차 확인.
- 두 독립 소스 일치 — 확정.

## 판정

**P0, audit:factuality/citation.** 법정 조항번호 오인용으로 규제기관 제출 서식·내부 SOP 근거란에 오기재된 조항이 실사·심사 시 지적 사유가 될 수 있음. 감사관 본문 미수정(이슈 등록만). 실운영 문서 미참고.

## 권고

3개 문서의 Art.87 조항번호를 (3)=기타15일 / (4)=공중보건위협2일 / (5)=사망10일로 통일 정정. SOP-PMS-001의 (3)(a)/(3)(b)/(3)(c) 표기는 삭제하고 독립 paragraph (3)/(4)/(5)로 교체.

## 참고
- Tier1: https://eur-lex.europa.eu/eli/reg/2017/745/oj/eng (Art.87 원문)
- 보조(원문 재게시, 조문 전문 대조용): https://www.medical-device-regulation.eu/2019/07/16/mdr-article-87-reporting-of-serious-incidents-and-field-safety-corrective-actions/

## 종결 메모 (2026-07-20)

Tier1 재확인: legislation.gov.uk 게재 Regulation (EU) 2017/745 Art.87 원문(Point in time 2017-04-05, EU 공식 채택본 그대로) 직접 대조 — paragraph 3="not later than 15 days"(일반), paragraph 4="Notwithstanding paragraph 3...serious public health threat...not later than 2 days", paragraph 5="Notwithstanding paragraph 3...death or unanticipated serious deterioration...not later than 10 days". WebSearch 독립 교차확인 결과도 동일 구조(Paragraph 4=2일/Paragraph 5=10일/Paragraph 3=15일) 일치.

정정 반영:
- `08_시판후_감시_PMS/PMS_개요.md` L108, L116 — (3)/(2)/(4) → (5)/(4)/(3)로 재배정. v0.3.1→v0.3.2.
- `08_시판후_감시_PMS/GUIDE-VIG-001_안전경계_보고_요건_통합_가이드.md` L65 각주³ — 단일 Art.87(3) 뭉뚱그림 인용을 공중보건(4)/사망(5)/기타(3)로 분리. v0.3→v0.3.1.
- `08_시판후_감시_PMS/SOP-PMS-001_불만처리_부작용보고_절차.md` L137-139 — 원문 미존재 (3)(a)/(3)(b)/(3)(c) 하위문자 표기 삭제, 독립 paragraph (4)/(5)/(3)로 교체. v0.4→v0.4.1.

동일 오류 클래스 일괄 점검(repo 전수 grep "Art.87"/"Article 87"): `00_프로젝트관리/증거기준_Evidence_Standard.md` §5 예시표에서도 동일 클래스 오류(Art.87(3)을 사망10일·공중보건2일 두 항목의 근거로 병기) 발견 — 공중보건=Art.87(4)/사망=Art.87(5)로 분리 정정(살아있는 참조 문서이므로 정정 대상; 날짜 고정 스냅샷 성격의 11_일일_리서치로그·12_교차검증_보고서·_audit_log.md 과거 기록은 시점 기록 보존 원칙에 따라 미수정).

일수(2일/10일/15일) 자체는 원래도 정확 — 조항번호(paragraph 식별자)만의 오류였음. 실운영 문서 미참고. web_verification: yes.

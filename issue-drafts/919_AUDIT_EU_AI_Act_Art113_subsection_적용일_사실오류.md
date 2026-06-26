---
title: "[AUDIT P0] EU_AI_Act_MDR_중첩적용_매핑 v0.6 — Art.113 하위항목·일반적용일 인용 사실오류 (Art.113(a)/(c) 혼동·2026-08-02 vs -03)"
labels: "audit:factuality,prio:P0,risk:high"
state: closed
closed-date: 2026-06-27
close-commits: ["TBD-this-execution"]
---

## 대상 문서
- `01_법규_규제/04_유럽_MDR/EU_AI_Act_MDR_중첩적용_매핑.md` v0.6 (last-review: 2026-06-22)

## 감사 주장

§3 적용 일정 표 및 §12 매트릭스에서 EU AI Act(Reg. 2024/1689) Article 113의 하위항목 인용과 일반 적용일이 다음과 같이 기재되어 있다.

대표 인용:
- §3 표: "**2025-02-02** | 금지 AI 관행(Chap.II) 적용 + **AI 리터러시 의무(Art.4) 적용일(applicability) — 이미 적용 중** | — | **Art.113(b)**; 의료기기 운영·사용 인력 대상"
- §3 표: "**2026-08-03** | **거버넌스·감독·과징금(Art.99 등) 적용일** ... | MDR 전면 적용 | **Art.113(c)**. Art.4 의무는 2025-02-02부터 이미 적용 중이므로 본 시점은 enforcement 트리거"
- §12: "Enforcement(Art.99 등) 적용일까지 **D-42**(**2026-08-03**)"
- §12.1 표: "D-20(**2026-08-02**)" (혼재된 표기)

본 인용은 audit #905(2026-06-22 close) 정정 권고 본문(§3 권고: "감독·집행 적용일(enforcement): 2026-08-03 (Art. 99 등)")을 그대로 반영한 것이나, **권고 자체가 Art.113 하위항목 및 일반 적용일 인용에서 1차 출처와 불일치**한다.

## 독립 확인 결과 — 1차 출처 (Tier 1)

Regulation (EU) 2024/1689 Article 113 본문(EUR-Lex):

> "This Regulation shall enter into force on the twentieth day following that of its publication in the Official Journal of the European Union. **It shall apply from 2 August 2026.** However: (a) Chapters I and II shall apply from 2 February 2025; (b) Chapter III Section 4, Chapter V, Chapter VII and Chapter XII and Article 78 shall apply from 2 August 2025, with the exception of Article 101; (c) Article 6(1) and the corresponding obligations in this Regulation shall apply from 2 August 2027."

| 사항 | 문서 기재 | Tier 1 정답 |
|---|---|---|
| Art.4(AI 리터러시, **Chapter I** 소재) 적용일 근거 | "2025-02-02 ... Art.**113(b)**" | 2025-02-02 — 근거 **Art.113(a)** (Chapters I and II shall apply from 2 February 2025) |
| 거버넌스·과징금(Art.99 등) 적용일 — 일자 | "**2026-08-03**" | **2026-08-02** (Art.113 chapeau "It shall apply from 2 August 2026") |
| 거버넌스·과징금(Art.99 등) 적용일 — 근거 | "Art.**113(c)**" | **Art.113 본문(chapeau, 일반 적용일)** — Art.113(c)은 Art.6(1) 고위험 의무로 **2027-08-02** 적용 |

추가 확인:
- Art.4(AI literacy)는 **Chapter I (General provisions)** 소재 — Chapter II(금지 관행)와 함께 Art.113(a) 대상(European Commission AI Literacy Q&A: "Article 4 of the AI Act entered into application on 2 February 2025").
- AI Act 일반 적용일은 **2 August 2026**(Art.113 chapeau)이며 일자에 "+1"을 적용한 2026-08-03은 1차 출처에 없는 표기이다.
- Art.113(c)은 "Article 6(1) and the corresponding obligations ... shall apply from **2 August 2027**"으로, Art.99 등 일반 적용일 근거가 될 수 없다.

## 판정
**사실오류 (factuality) — P0**
- 동일 표에서 Art.113 (a)·(c) 두 하위항목 인용이 모두 1차 출처와 불일치, 일자 1일 오차 동반.
- 영향: §12 enforcement 카운트다운이 1차 출처가 없는 일자(2026-08-03)와 무관 조항(Art.113(c))을 근거로 구성되어, NB·감독기관 실사 시 1차 인용 부정확으로 지적될 수 있음.
- 본 결함은 audit #905의 권고 본문에서 발생한 인용 오류가 v0.5→v0.6 정정 과정에서 그대로 이전된 패턴(#917과 유사한 단일정정 미전파)이며, audit #905 자체의 권고문도 동일 오류를 포함하므로 함께 정정 필요.

## 권고 수정

1. §3 적용 일정 표 — Art.4 행 근거 컬럼: "Art.113(b)" → **"Art.113(a)"**
2. §3 적용 일정 표 — Art.99 enforcement 행:
   - 일자: "2026-08-03" → **"2026-08-02"**
   - 근거: "Art.113(c)" → **"Art.113 본문(chapeau, 일반 적용일)"**
3. §12 본문 및 §12.1 표 D-Day 계산 — "2026-08-03" → **"2026-08-02"** 일괄 치환. 2026-06-26 기준 D-day는 D-37.
4. (사내 정합) audit #905 issue 본문의 같은 인용 오류도 정정 표기(또는 후속 보정 노트 추가).

## 출처 (Tier 1)

- Regulation (EU) 2024/1689, Article 113 — EUR-Lex 원문: https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng
- EU AI Act Service Desk — Article 113 페이지(European Commission 공식): https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-113
- European Commission — AI Act page (general application date 2 August 2026 명시): https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- European Commission — AI Literacy Q&A (Art.4 entered into application 2 February 2025): https://digital-strategy.ec.europa.eu/en/faqs/ai-literacy-questions-answers

## Tier 2 (보조 — 판정 근거 아님)
- artificialintelligenceact.eu Article 113 요약(범위 파악용)

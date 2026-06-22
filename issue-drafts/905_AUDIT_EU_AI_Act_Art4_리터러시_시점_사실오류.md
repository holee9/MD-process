---
title: "[AUDIT P0] EU_AI_Act_MDR_중첩적용_매핑 — Art.4 AI 리터러시 의무 시점 사실오류"
labels: "audit:factuality,prio:P0,risk:high"
---

## 대상 문서
- `01_법규_규제/04_유럽_MDR/EU_AI_Act_MDR_중첩적용_매핑.md` v0.5 (last-review: 2026-06-20)

## 감사 주장
문서는 EU AI Act Article 4(AI 리터러시 의무)의 "**발효 시점**"을 일관되게 **2026-08-02**로 기재하고, 그 날짜를 기준으로 D-43 카운트다운 매트릭스(§12)와 운영 일정을 구성하였다.

대표 인용:
- Line 65: "AI 리터러시 의무(Art. 4)의 2026-08-02 시한은 Omnibus 결과와 무관하게 유지된다."
- Line 186: "## 12. D-43 AI 리터러시(Art.4) 발효 준비도 매트릭스 (2026-06-20 기준 — v0.5 신규)"
- Line 188: "AI 리터러시 의무(Art.4) 발효 2026-08-02 = D-43 (영업일 기준 약 31일 잔여)"
- Line 222: "AI 리터러시(Art.4)는 어떤 경우든 D-43 충족."

## 독립 확인 결과 — 1차/공신력 출처

| 사항 | 문서 기재 | 독립 확인 정답 |
|---|---|---|
| Art.4 의무 적용(applicability) 시점 | 2026-08-02 (D-43 잔여 표기) | **2025-02-02** — 이미 약 16개월 전부터 적용 중 |
| 감독·집행(enforcement·penalties) 적용 시점 | (구분 없이 "발효"로 표기) | **2026-08-03** (Reg. 2024/1689 Art. 113(b)) |

- Regulation (EU) 2024/1689 Art. 113(b): "Chapter II [Art. 5 prohibitions, Art. 4 AI literacy 포함] shall apply from 2 February 2025."
- European Commission, "AI Literacy — Q&A": "Article 4 of the AI Act entered into application on 2 February 2025, therefore the obligation … already applies."
- Governance·penalty 조항(Art. 99 등)의 시점은 2026-08-03.

## 판정
- **사실오류 (factuality)** — Art.4 의무가 "2026-08-02부터 발효"라는 진술은 사실과 다름. 의무는 **2025-02-02부터 이미 적용** 중.
- 영향 P0: §12 D-43 매트릭스 전체와 운영 일정(D-43/D-30/D-15 마일스톤)이 잘못된 시점 가정 위에 설계되어, 운영진이 "아직 시간 여유가 있다"고 오인할 위험. 미준수 상태로 약 16개월간 노출 가능.

## 권고 수정
1. "발효"라는 단어를 두 시점으로 분리해 기재:
   - **적용일(applicability):** 2025-02-02 — Art.4 의무는 **이미 적용 중**
   - **감독·집행 적용일(enforcement):** 2026-08-03 (Art. 99 등 거버넌스·과징금 조항)
2. §12 제목·카운트다운 기준을 "enforcement 적용 대비 갭점검(이미 의무 적용 중)"으로 재설정.
3. 라인 222 "Art.4는 어떤 경우든 D-43 충족" → "Art.4 의무는 이미 적용 중이며, 2026-08-03 enforcement 이전 갭 제거 권고"로 수정.
4. 본문 65행 단서: "AI 리터러시 의무는 2025-02-02부터 이미 적용 중이며, 감독·집행은 2026-08-03부터. Omnibus와 무관"으로 명료화.

## 출처 (공식 1차)
- Regulation (EU) 2024/1689 (EUR-Lex): https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng (Art. 4, Art. 113)
- European Commission — AI Literacy Q&A: https://digital-strategy.ec.europa.eu/en/faqs/ai-literacy-questions-answers
- European Commission — AI Act page: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai

---
title: "[AUDIT P0] PMS_개요 v0.2 §3 + §8.1 — EU AI Act Art.72 '심각 사고 보고' 사실오류 (정답: Art.73 = Reporting of serious incidents / Art.72 = Post-market monitoring by providers)"
labels: "audit:factuality,prio:P0,risk:high"
---

## 대상 문서
- `08_시판후_감시_PMS/PMS_개요.md` (doc-id: PMS_개요, type: Overview, version: v0.2, last-review: 2026-05-02)
- 위치 ① §3 "관련 규제·표준" 표 마지막 행
- 위치 ② §8.1 "근거 (추가)" 불릿 3번째

## 주장 (기재값)
- §3 표: `| EU AI Act | Art. 72 | 심각 사고 보고 |`
- §8.1: `- EU AI Act Art. 72 — 심각한 사고(Serious Incident) 보고 의무`

즉 EU AI Act(Regulation (EU) 2024/1689)의 **심각 사고 보고 의무** 근거 조항을 **Art. 72**로 인용.

## Tier 1 정답
Regulation (EU) 2024/1689 본문 조항 구조:
- **Article 72** — *Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems* (시판후 모니터링 의무 및 PMM 계획)
- **Article 73** — *Reporting of serious incidents* (심각 사고 보고 의무, 인지 후 즉시 — 사망 가능 시 10일, 광범위 침해/중대 인프라 붕괴 시 2일, 그 외 15일)
- **Article 74** — Enforcement
- **Article 75** — Mutual assistance

즉 "심각 사고 보고"의 근거 조항은 **Art. 73**이며, **Art. 72는 PMS(post-market monitoring) 계획·운영** 조항. 두 조항은 동일한 시판후 클러스터에 속하지만 의무 성격(주기적 모니터링 vs 사고 보고)이 다르다.

## 판정
**사실오류 (P0, audit:factuality)** — 2건 (§3 표, §8.1) 자매 인용 동시 발생. 본 문서가 빌더 자체 12_교차검증을 거쳤음에도 동일 오류 잔존.

## Tier 1 출처
- EUR-Lex — Regulation (EU) 2024/1689: https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng
- AI Act Service Desk (EU Commission) — Article 73: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-73
- (보조) artificialintelligenceact.eu — Article 73: https://artificialintelligenceact.eu/article/73/

## 권고
1. §3 표 행을 `EU AI Act | Art. 73 | 심각 사고 보고`로 정정.
2. §8.1 불릿을 `EU AI Act Art. 73 — 심각한 사고(Serious Incident) 보고 의무 (인지 후 15일 / 사망 가능 시 10일 / 광범위 침해·중대 인프라 붕괴 시 2일)`로 정정.
3. 선택: PMM 계획 자체에 대한 EU AI Act 요구는 Art. 72에 있으므로, PMS 계획 수립(§4 [1단계]) 행에 별도 Art. 72 인용 추가하면 책무 분리 명확.
4. 자매 문서(SOP-PMS-001, EU_AI_Act_MDR_중첩매핑 v0.6, SOP-AIGOV-001 등) Art.72 ↔ Art.73 인용 일관성 사내 전수 확인.

## 비고
실운영 문서 미참고. 빌더의 자체 ✅ 신뢰 배제, EUR-Lex 1차 본문 기반 독립 재확인.

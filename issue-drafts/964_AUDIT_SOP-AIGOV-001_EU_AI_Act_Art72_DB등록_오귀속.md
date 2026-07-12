---
title: "audit(C1): SOP-AIGOV-001 §10.1 'EU AI Act Art.72에 따라 EU AI Database 등록' 사실오류 — Art.72=시판후모니터링, 정답 Art.49(등록의무)/Art.71(DB설치), audit #928 동일패턴 자매재발"
labels: "audit:factuality,prio:P0,risk:high"
state: closed
closed: 2026-07-13
---

## 대상
- 문서: `03_설계_개발관리/SOP-AIGOV-001_AI_공정성_설명성_드리프트_거버넌스.md`
- 위치: §10.1 (라인 312) — "EU AI Act Art. 72에 따라 고위험 AI 시스템은 EU AI Database에 등록해야 한다."
- 감사 클래스: C1 (조항번호 § 정확성) — 전수 클래스 스윕 (03_설계_개발관리, 2차)

## 독립 감사 요약

EU AI Act (Regulation (EU) 2024/1689) 원문상 **Art.71**이 "EU database for high-risk AI systems listed in Annex III"(EU 데이터베이스 설치·운영)를 규정하고, **Art.49**가 제공자(provider)의 등록 의무(registration obligation) 및 등록 데이터 항목(Annex VIII)을 규정한다. **Art.72는 "Post-market monitoring by providers"**(제공자의 시판 후 모니터링 의무)로, EU AI Database 등록과는 무관한 별개 조문이다.

이는 2026-06-28 사이클에서 이미 확정된 **audit #928**(PMS_개요 "EU AI Act Art.72 심각 사고 보고" 사실오류 — 정답 Art.73, Art.72=Post-market monitoring by providers)와 **동일 조문(Art.72)의 오귀속이 반복되는 자매재발 패턴**이다. 본 건은 Art.72를 "등록" 근거로 오인용한 점에서 #928(보고 근거로 오인용)과는 오귀속 맥락이 다르지만, 근본 원인(Art.72 조문 성격 혼동)은 동일하다.

## Tier 1 근거
- EU AI Act Service Desk(European Commission), Article 71: EU database for high-risk AI systems listed in Annex III.
- EU AI Act 원문 Article 49: Registration — providers shall register themselves and their system in the EU database referred to in Article 71, prior to placing on the market.
- Article 72 표제: "Post-market monitoring by providers" (등록·DB 설치와 무관).

## 결함
- **기재값:** "EU AI Act Art. 72에 따라 고위험 AI 시스템은 EU AI Database에 등록해야 한다."
- **정답:** "EU AI Act Art. 49(등록 의무) 및 Art. 71(EU 데이터베이스 설치)에 따라 고위험 AI 시스템은 EU AI Database에 등록해야 한다."
- P0, 1개소.

## 판정
- 근거: Tier 1 (EU AI Act Service Desk 공식 조문 페이지 + AI Act 원문 조문 구조)
- 자매재발 패턴: audit #928과 동일 조문(Art.72) 오귀속 반복 — 저장소 내 "Art.72"·"Art. 72" 잔존 인용 grep 재검색 권고
- 해석범위: 0건
- 본 감사관은 문서 본문을 직접 수정하지 않음. 정정은 빌더 세션 몫.
- 실운영 문서 미참고. web_verification: yes.


## 처리 (2026-07-13 빌더)
- Tier 1 재확인 후 대상 문서 정정 완료. 동일 오류 클래스 저장소 전수 스윕·일괄 교정 수행. state: closed.

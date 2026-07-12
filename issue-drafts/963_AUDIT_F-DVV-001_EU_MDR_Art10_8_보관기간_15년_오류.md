---
title: "audit(C1): F-DVV-001 §E 보관기간 'EU MDR Art.10(8) 단종 후 15년' 사실오류 — 비이식형(X-ray) 정답 10년, audit #914 동일패턴 자매재발"
labels: "audit:factuality,prio:P0,risk:high"
state: closed
closed: 2026-07-13
---

## 대상
- 문서: `03_설계_개발관리/F-DVV-001_설계검증_계획_결과서.md`
- 위치: §E 보관 (라인 64) — "보관 기간: 영구 + 단종 후 15년 (EU MDR Art.10(8))"
- 감사 클래스: C1 (조항번호 § 정확성) — 전수 클래스 스윕 (03_설계_개발관리, 2차)

## 독립 감사 요약

EU MDR 2017/745 Art.10(8) 원문(EUR-Lex Regulation (EU) 2017/745)은 기술문서·EU 적합성선언·인증서 보관기간을 "최종 제품 시판 후 최소 10년"으로 규정하며, **이식형(implantable) 기기에 한해 최소 15년**으로 연장한다. 자사 제품(X-ray Flat Panel Detector, X-ray System)은 비이식형이므로 정답은 **10년**이다.

이는 2026-06-23 사이클에서 이미 확정된 **audit #914**(SOP-PSUR-001 "단종 후 15년" 사실오류, 정답 Art.10(8) 비이식형 10년)와 **동일한 조항·동일한 오류 패턴**이다. #914 정정이 SOP-PSUR-001에만 적용되고 자매문서 F-DVV-001로 전파되지 않은 것으로 판단된다(자매재발).

## Tier 1 근거
- EUR-Lex, Regulation (EU) 2017/745, Article 10(8): "...for a period of at least 10 years... In the case of implantable devices the period shall be at least 15 years..."

## 결함
- **기재값:** "보관 기간: 영구 + 단종 후 15년 (EU MDR Art.10(8))"
- **정답:** "보관 기간: 영구 + 단종 후 10년 (EU MDR Art.10(8), 비이식형 기기 기준)"
- P0, 1개소. 조항번호(Art.10(8)) 자체는 정확 — 부속 수치(15년→10년)가 사실오류.

## 판정
- 근거: Tier 1 (EUR-Lex MDR 원문)
- 자매재발 패턴: audit #914(SOP-PSUR-001) 동일 조항 동일 오류 — grep 전수 재검색 권고("단종 후 15년" 잔존 여부 03/08 카테고리 전반)
- 해석범위: 0건
- 본 감사관은 문서 본문을 직접 수정하지 않음. 정정은 빌더 세션 몫.
- 실운영 문서 미참고. web_verification: yes.


## 처리 (2026-07-13 빌더)
- Tier 1 재확인 후 대상 문서 정정 완료. 동일 오류 클래스 저장소 전수 스윕·일괄 교정 수행. state: closed.

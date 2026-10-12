---
title: "audit(citation/C1): SOP-PKG-001 '의료기기 기호'를 EU MDR Annex I §23.2(a)로 귀속 — §23.2(a)=기기명/상표명, MD 표시는 §23.2(q)"
labels: "audit:citation,prio:P2,risk:low,regulatory"
opened: 2026-10-12
created-by: md-process-auditor
related-issues: [1094, 1088]
state: open
sweep: "표본 모드 15차 — MDR Annex I §n 인용 전수 재대조 (EUR-Lex 공식 PDF 재사용)"
---

## Tier1 근거
EUR-Lex 공식 PDF (CELEX 02017R0745-20250110) 직접 회수 → pdftotext 원문 대조.
- Annex I §23.2(a) = "the name or trade name of the device"
- Annex I §23.2(q) = "an indication that the device is a medical device" (의료기기 표시)
- Annex I §23.1(h) = 국제 인정 기호 사용 시 조화표준/CS 준수 요건

## 결함
| # | 파일:라인 | 표기 | 문제 |
|---|---|---|---|
| 1 | 04_제조공정_관리/SOP-PKG-001 L124 | `의료기기 기호 (MDR Annex I §23.2(a))` | §23.2(a)는 기기명/상표명. 의료기기 표시 요건은 §23.2(q) (기호 형식은 §23.1(h)) |

제안 정답(감사관 판단, 수정은 담당자): `Annex I §23.2(q)` (+§23.1(h)).

## PASS (대조 완료, 약 30개소)
§1·§3·§10.2·§11.1·§14.2(g)·§15·§15.1·§16(전체)·§16.1(a)·§16.2·§17·§17.1·§17.2·§17.4·§23 / Ch.I §1~9·Ch.II §10~22·Ch.III §23 구분 / §23.1(f) eIFU(Impl. Reg. 2021/2226 병기).

## 해석범위 (결함 미계수)
- EU_AI_Act매핑 L96/L156 Art.14 인간감독 ↔ Annex I §14.2 (§14.2(a)는 인체공학적 특징만 명시; 사용적합성 직접 조항 아님)
- EU_AI_Act매핑 L94/L154 Art.12 로깅 ↔ §17.2, L103 Robustness ↔ §17.2 (§17.1 반복성·신뢰성이 더 근접할 수 있음)
- 검사_시험_밸리데이션_개요 L31 측정장비 관리(ISO 13485 7.6) ↔ §15 (§15는 기기의 측정기능 요건, 제조자 측정장비 교정과 직접 대응 아님)
- F-SUP-001 L218 §17.2 ↔ 공급망 사이버보안 (§17.2 문언은 information security 포함 개발수명주기, 공급망 명시 없음)

실운영 문서 미참고.

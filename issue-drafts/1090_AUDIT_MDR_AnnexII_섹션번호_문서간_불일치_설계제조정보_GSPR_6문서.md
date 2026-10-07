---
title: "audit(citation/C1): EU MDR Annex II 섹션번호(§3 설계·제조정보 / §4 GSPR / §5 편익-위험) 문서 간 불일치 — 5문서 9개소"
labels: "audit:citation,prio:P2,risk:medium,regulatory"
opened: 2026-10-07
created-by: md-process-auditor
related-issues: [1088, 1089]
state: open
sweep: "표본 모드 10차 — MDR Annex 하위항(Annex I §n·Annex II §n) 글자 인용 전수"
---

## 근거 및 한계
- **저장소 내 기준 정의**: 06_문서_기록관리/TF-TD-001 L411~L462 = Annex II §1 제품설명·사양 / §2 제조자 정보 / §3 설계·제조 정보 / §4 GSPR / §5 편익-위험·위험관리 / §6 검증·확인. 이 매핑은 MDR Annex II 구조와 일치하는 것으로 판단.
- **Tier1 verbatim: 미확인.** EUR-Lex 통합본/PDF(CELEX 02017R0745-20250110, 32017R0745, 02017R0745-20230320) 전부 WebFetch 본문이 Art.16~47 부근(약 13~17만자)에서 절단되어 Annex II 원문 회수 불가. MDCG 2019-15(health.ec.europa.eu) Annex II 목록은 무번호라 섹션 번호 확증 불가. → 아래는 **문서 간 정합성 불일치(저장소 내 TF-TD-001 대비)**로 등록하며, 최종 정답은 Annex II 원문(EUR-Lex 접근 복구 시) 확인 필요.

## 결함 (원문서 01~10 전수 grep: `Annex II ?§`)

| # | 파일:라인 | 표기 | TF-TD-001 기준과의 불일치 | 제안 정답 |
|---|---|---|---|---|
| 1 | 03/SOP-DHF-001 L82 | Annex II §1 = Design and manufacturing information | §1=제품설명·사양 | §3 |
| 2 | 03/SOP-DHF-001 L83, L497 | Annex II §4 = 설계단계 산출물·검토 기록 | §4=GSPR | §3 (검증·확인은 §6) |
| 3 | 03/SOP-DT-001 L9·L38 | Annex II §4 = 설계·제조 정보, 공정 밸리데이션 | §4=GSPR | §3 (밸리데이션 §6) |
| 4 | 03/CHK-DR-001 L12·L41·L275 | Annex II §4 = 설계단계·검증결과·설계변경 이력 | §4=GSPR | §3/§6 |
| 5 | 04/F-CLN-001 L63 · 04/SOP-CLN-001 L135 | Annex II §5 = (설계·제조 정보) 사본 첨부 | §5=편익-위험·위험관리 | §3 |
| 6 | 08/GUIDE-VIG-001 L144 | 전자기록 허용 근거 = Annex II §4 | §4=GSPR (전자기록 규정 아님) | 근거 삭제 또는 해당 조문 재확인 |

## 미확인(결함 미계수)
- 06/문서_기록관리_개요 L163 'Annex II §6.2(c) 사용적합성' — 하위항 내용 Tier1 미확인.
- 03/ALARA_지원기능 L14 'Annex I §14.2(c), §16.2'; 02/SOP-ENV-001 L18 'Annex I §16 제조환경'(§16=방사선 방호 추정, '제조환경' 표기와 정합성 의문) — Annex I 원문 미회수로 판정 보류.
- AI Act 매핑 'Annex II §6.1'(Data Governance) — 해석 범위.

## PASS(문서 간 정합)
TF-TD-001 §1~§6 자체 정의, 설계개발_프로세스 'Annex II §1~6', SOP-DVV-001/F-DVV-002 'Annex II §6.1 (V&V)', GSPR 매핑 'Annex II §4'(GSPR 참조), CHK-DR-001/ SOP-DHF-001 'Annex II §1~4' 범위 표기.

## 권고 (감사관은 문서 수정 안 함)
Annex II 원문 확인 후 위 표 '제안 정답'으로 정정 검토. 확인 전까지 §번호 인용 시 TF-TD-001 매핑 우선.

실운영 문서 미참고. web:ok(부분) — Annex 본문 회수 실패(절단).

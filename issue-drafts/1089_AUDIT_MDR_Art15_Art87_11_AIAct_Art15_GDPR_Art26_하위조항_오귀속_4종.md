---
title: "audit(citation/C1): EU MDR Art.15(4)·Art.11(3)(a)·Art.87(11) / AI Act Art.15(3)(4) / GDPR Art.26 하위조항 오귀속 4종 (#1088 확산 점검)"
labels: "audit:citation,prio:P2,risk:medium,regulatory"
opened: 2026-10-06
created-by: md-process-auditor
related-issues: [1088, 1085]
state: closed
sweep: "표본 모드 9차 — #1088 확산(MDR Art.10 외 타 조문 하위항 인용 전수)"
---

## Tier1 근거
- Reg.(EU) 2017/745 CELEX 02017R0745-20250110 (EUR-Lex HTML, 2026-10-06 직접 회수 verbatim): Art.15(4)=복수 PRRC 공동책임 시 각자 책임영역 서면 명시 / **Art.15(5)=PRRC 불이익 금지** / **Art.15(6)=위임대리인(AR)의 PRRC 상시 확보** / Art.11(3)(a)=AR의 DoC·기술문서 작성 검증 / **Art.89(8)=FSN 작성 언어(회원국 결정 EU 공용어)** / Art.87(11)=회원국 CA가 의료인·사용자·환자 보고 접수 시 제조사 통지.
- Reg.(EU) 2024/1689 CELEX 32024R1689: Art.15(3)=정확도 지표 사용설명서 선언 / **Art.15(4)=오류·결함 강건성(robustness)·피드백루프** / **Art.15(5)=무권한 제3자 대응 사이버보안**.
- Reg.(EU) 2016/679 CELEX 32016R0679: Art.4(5)=가명처리 정의(정확) / Art.26=공동관리자(joint controllers) — 익명화 조문 아님(익명화는 Recital 26).

## 결함 (원문서 01~10 전수 grep, 해당 조문 인용 대조)

| # | 파일:라인 | 표기 | 판정 | 정답 |
|---|---|---|---|---|
| 1 | 01/04_유럽_MDR/PRRC_역할_및_한미_대응자_매핑 L92·L97·L113 | 보호 조항(불이익 금지) = Art.15(4) | 오귀속 | Art.15(5) |
| 2 | 동 문서 L84 | EUAR도 PRRC 별도 보유 = Art.11(3)(a) | 오귀속 ((a)=DoC/TD 검증) | Art.15(6) |
| 3 | 08/SOP-FSCA-001 L183 | FSN 언어 = 회원국 공용어 (Art.87(11)) | 오귀속 | Art.89(8) |
| 4 | 01/04_유럽_MDR/EU_AI_Act_MDR_중첩적용_매핑 L103 / L104 | Robustness = AI Act Art.15(3) / Cybersecurity = Art.15(4) | 1항씩 어긋남 | Robustness=Art.15(4) / Cybersecurity=Art.15(5) |
| 5 | 04/SOP-CA-001 L66 | 익명화 = GDPR Art.26 | 오귀속(Art.26=공동관리자) | 해당 조문 없음(Recital 26) — 'Art.4(5) 가명처리'는 정확 |

해석범위(이슈 비포함): GUIDE-VIG-001 L74 'Art.11(3)(d)'(AR의 CA 정보제공 — 보고 경로 취지 유사), AI Act 매핑 L80 'Art.9(2)' 위험허용기준(허용 잔여위험 판단은 Art.9(5)와 병존 — 해석 갈림).

## PASS 확인 (동 점검 범위)
Art.86(1)(2)(IIb·III 연1회/IIa 2년, III·이식형 전자제출), Art.87(3)(4)(5) 15/2/10일, Art.87(1), Art.89(8) FSN(GUIDE-VIG L46), Art.15(1)(2)(3), Art.2(65)(68), Art.61(11), Art.83(3), Art.123(1)(2), AI Act Art.43(4)·Art.6(1)·Art.15(1), GDPR Art.4(5).

## 권고 (감사관은 문서 수정 안 함)
위 표 '정답' 열대로 정정 검토.

실운영 문서 미참고. web:ok (EUR-Lex).

---

## 종결 (2026-10-07, audit-drain 스프린트)

- Tier1 직접 재확인: MDR Art.15(1)~(6) 문언(EUR-Lex 통합본 CELEX 02017R0745-20250110: (4)=복수 PRRC 공동책임, (5)=불이익 금지, (6)=AR의 PRRC 상시 확보), Art.11(3)(a)=DoC·기술문서 작성 검증; AI Act Art.15(3)=정확도 지표 선언 / (4)=오류·결함 resilient / (5)=무권한 제3자 대응(EC AI Act Service Desk 공식 조문). MDR Art.89(8)=FSN 시정조치 정보 제공 — EUR-Lex 페이지 분할로 직접 회수 실패, 공개 2차(advisera 전문본)+감사자 EUR-Lex verbatim으로 대조. GDPR Art.26=공동관리자(감사자 EUR-Lex 대조, 본 세션 미재회수).
- 정정 5건/8개소: PRRC 매핑 L84(11(3)(a)→15(6)), L92·L97·L113(15(4)→15(5)); AI Act 매핑 L103(15(3)→15(4))·L104(15(4)→15(5)); SOP-FSCA-001 L183(87(11)→89(8)); SOP-CA-001 L66(Art.26 익명화 삭제, Recital 26 안내).
- 동일 클래스 전수 grep(Art.15(x)·11(3)(a)·87(11)·GDPR Art.26, 리서치로그·교차검증·감사로그 시점기록 제외): 잔존 0.
- 해석범위(미수정): GUIDE-VIG-001 'Art.11(3)(d)', AI Act 매핑 'Art.9(2)'.

실운영 문서 미참고.

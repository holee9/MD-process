---
title: "audit #1069 (citation/C5): EU AI Act에서 의료기기가 고위험으로 분류되는 근거를 'Annex II'(3개소)·'Annex III'(1개소)로 기재 — 정답은 Art.6(1) + Annex I Section A point 11(MDR). Annex II는 형사범죄 목록"
labels: "audit:citation,audit:factuality,prio:P1,risk:medium,regulatory,classification,ai"
state: closed
created: 2026-09-24
created-by: md-process-auditor
related-issues: [1041]
sweep: "C5 x 01_법규_규제"
---

## 결함 개소

| 문서 | 위치 | 현행 기재 | 정답 |
|---|---|---|---|
| `04_유럽_MDR/EU_AI_Act_MDR_중첩적용_매핑.md` | §2.1 L29 | `EU 조화법령(Annex II) 대상인가?` | Annex I (Union harmonisation legislation) |
| 동 | §2.2 표 L48 | `Art. 6(1) + Annex II §11` | Art.6(1) + **Annex I Section A point 11** (Reg. (EU) 2017/745) |
| 동 | 출처 L175 | `Annex II/III/IV` | Annex I/III/IV(의도한 인용 기준) |
| `04_유럽_MDR/GSPR_정합표준_매핑표.md` | §9 L168 | `AI/ML 의료기기는 EU AI Act Annex III(고위험 AI)와 MDR이 중첩 적용` | MDR 적용 AI는 **Art.6(1)(Annex I 경로)**로 고위험. Annex III는 독립형 용도 목록이며 의료기기 경로가 아님 |

## 근거
- **Tier1 — MDCG 2025-6 / AIB 2025-1 (2025-06), Q2** (health.ec.europa.eu PDF 직접 열람): "A MDAI is considered a high-risk AI system under **Article 6(1)** AIA if … safety component … or is itself a medical device and … subject to a third-party conformity assessment by a notified body". Table 1에 Art.6(1) 적용 여부가 MDR 등급별로 제시됨. Annex III는 해당 경로가 아님.
- AI Act 최종 문안에서 **Annex II는 Art.5(1)(h)(iii) 형사범죄 목록**. 조화법령 목록은 Annex I. 번호 'Annex II'는 2021 집행위 제안서 번호로 보임.
- **Web:partial**: EUR-Lex ELI 페이지(32024R1689)에서 메타데이터만 확인했고 본문은 렌더링되지 않음. Annex II 표제는 복수 법령 미러(Tier2)로 교차 확인함.
- **문서 내부 모순**: 같은 문서 §3 L63이 `규제제품 탑재형(Annex I)`로 올바르게 표기되어 L29/L48과 충돌함.

## 부기(결함 아님)
L33 `Class I (self-cert) → 원칙상 비해당`은 MDCG 2025-6 Table 1과 정합한다. 단, Class Is/Im/Ir(멸균·측정·재사용 수술기구)은 NB가 관여하므로 **고위험 해당**(Table 1 "Yes")이다. 해당 문구를 보완할 것을 권고.

## 정정 권고
3개소 Annex II→Annex I(Section A point 11), GSPR L168 Annex III→Art.6(1)/Annex I. 확산 grep: `AI Act.*Annex II\b`, `Annex III\(고위험` 전 저장소.

---

## 종결 (2026-09-25, audit-drain)

| 항목 | 결과 |
|---|---|
| Tier1 재확인 | MDCG 2025-6/AIB 2025-1 PDF 직접 열람 — Q2 Art.6(1) 조건, Table 1(Class Is/Im/Ir = Yes). Annex I Section A point 11 = MDR |
| 정정 | EU_AI_Act_MDR_중첩적용_매핑 §2.1·§2.2·§9 'Annex II'→Annex I Section A point 11, §2.1 Class Is/Im/Ir 보완 (v0.9.1) · GSPR_정합표준_매핑표 §9 'Annex III'→Art.6(1)+Annex I (v0.3.2) |
| 동일 클래스 grep | `Annex II`+AI Act 문맥 잔존 0 (MDR Annex II TD 인용은 정상) · Annex III 표기는 독립형 일정 문맥만 잔존(정상) |
| 한계 | EUR-Lex 본문 직접 fetch 불가(provenance 제한) — Annex II 표제는 원문 미대조, MDCG 문서로 경로 확정 |

실운영 문서 미참고.

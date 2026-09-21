---
title: "audit #1063 (factuality/C4): Class III·이식형 PSUR의 EUDAMED 제출이 '2026-05-28부터 의무' — Vigilance/PMS 모듈 미의무화, 4개 모듈에 미포함 (2문서 2개소 + 자기모순, 발생원 11·12 확산 3개소)"
labels: "audit:factuality,prio:P1,risk:medium,regulatory,EU-MDR,EUDAMED"
state: closed
created: 2026-09-21
created-by: md-process-auditor
related-issues: [1041, 1045, 1050, 1052]
sweep: "C4 x 08_시판후_감시_PMS"
---

## 결함

| 문서 | 위치 | 기재 |
|---|---|---|
| `08_시판후_감시_PMS/SOP-FSCA-001_현장안전시정조치_절차.md` | L344 §5.12.2-3 | "PSUR 연계: Class III 및 이식형 기기 PSUR을 EUDAMED으로 제출 (**현재 이미 2026-05-28부터 의무**)" |
| `08_시판후_감시_PMS/SOP-PMS-001_불만처리_부작용보고_절차.md` | L241 §8.2 | "Class III 및 이식형 기기의 PSUR은 **2026-05-28부터 EUDAMED으로 제출 의무**" |

## Tier1 근거

유럽위원회 공식 공지 "The EUDAMED four first modules will be mandatory to use as from 28 May 2026"(DG SANTE, 2025-11-27) 원문 직접 열람 — Commission Decision (EU) 2025/2371 **of 26 November 2025**(OJEU 2025-11-27 게재) + Regulation (EU) 2024/1860 경과규정 6개월에 따라 **2026-05-28부터 의무화되는 모듈은 다음 4개로 한정**:

- Actor registration
- UDI/Devices registration
- Notified Bodies & Certificates
- Market Surveillance

**Post-Market Surveillance & Vigilance(VGL) 모듈과 Clinical Investigations/Performance Studies(CI/PS) 모듈은 미포함**이며 개발 중이다. PSUR은 EU MDR Art.86(2)에 따라 **Art.92 전자시스템(= Vigilance/PMS 모듈)** 경유 제출 대상이므로, 해당 모듈이 기능선언·경과 6개월을 거쳐 의무화되기 전까지 EUDAMED 경유 PSUR 제출 의무는 발생하지 않는다.

## 판정

- **사실오류 확정(C4 발효·의무화 일자 오귀속)**. 의무화 대상 모듈 목록에 없는 기능을 의무로 단정.
- **문서 자기모순**: SOP-FSCA-001 §5.12.1(L332)은 "EUDAMED Vigilance 모듈은 아직 의무화되지 않았으며, 2027년 Q2경 의무화가 예상된다"고 정확히 기술한다. 동일 문서 §5.12.2가 **Vigilance 모듈 의무화 후 전환계획 항목 안에** "현재 이미 의무"를 병기하여 논리적으로 성립 불가. SOP-PMS-001도 §8.3(L247)에서 "Vigilance 모듈 미의무화 기간"을 전제하면서 §8.2에서 PSUR 제출을 의무로 기재 — 동일 구조의 자기모순.
- **실질 영향**: 자사 제품군은 Class IIb(비이식형)로 Art.86(2) 직접 대상은 아니나, 본 SOP가 PSUR 제출 경로를 규정하는 문서이므로 **NB 제출 경로 오판·존재하지 않는 시스템 제출 시도**로 이어질 수 있다. 반대 방향(의무 과잉 인식)이므로 미보고 위험은 낮음.

## 발생원 및 확산 (스윕 범위 밖, 부기)

| 문서 | 위치 | 기재 |
|---|---|---|
| `11_일일_리서치로그/일일리서치_2026-06-07.md` | L56, L88 | "Class III 및 이식형 기기의 PSUR은 2026-05-28부터 EUDAMED으로 전자 제출 의무" — **1차 발생원 추정** |
| `12_교차검증_보고서/교차검증_2026-06-07.md` | L49, L80, L104 | "Class III PSUR EUDAMED 제출 의무 → **✅ 정확 / 근거: EU MDR Art.86, RegDesk**" |
| `issue-drafts/158`, `issue-drafts/159` | — | 동 주장 인용 |

**빌더 검증산출물 불신 원칙 4차 실증**(#1045 CP 7382.850 '✅ FDA 공식 발표', #1050 12_교차검증 체크리스트 축조, #1061 '✅ FDA RAPS 발표'에 이은 사례). 특히 12_교차검증 L49는 **RegDesk(Tier2 컨설팅 매체)를 사실 근거로 인용하여 ✅ 판정** — 증거기준 위반이 검증 단계에서 발생.

## 권고

1. SOP-FSCA-001 L344를 "Vigilance/PMS 모듈 의무화 시 Class III·이식형 PSUR을 EUDAMED 경유 제출로 전환"으로 정정(현재 의무 표기 삭제). §5.12.2는 전환계획 절로서 미래시제로 통일.
2. SOP-PMS-001 §8.2 첫 항목을 "Vigilance/PMS 모듈 의무화 이전 — PSUR은 NB에 기존 경로로 제출. 모듈 의무화 후 EUDAMED 제출로 전환(Art.86(2)·Art.92)"으로 정정.
3. 11·12 카테고리 확산 3개소 동반 교정, 12_교차검증 L49 판정을 `✅ 정확` → `❌ 오류(본 감사 #1063)`로 하향하고 Tier2 인용을 사실근거에서 제거.
4. 4개 모듈 목록(Actor / UDI-Devices / NB&Certificates / Market Surveillance)을 SOP-PMS-001 §8.1에 명시하여 재발 차단.

실운영 문서 미참고. web_verification: yes (health.ec.europa.eu 공식 공지 원문 직접 fetch + WebSearch 교차, 2026-09-21).

---

## 종결 (2026-09-22, audit-drain 스프린트)

- **Tier1 재확인(본 사이클 직접 재검증)**: Commission Decision (EU) 2025/2371 of 26 November 2025(OJEU 2025-11-27 게재) + Regulation (EU) 2024/1860 경과 6개월 → **2026-05-28 의무화 모듈은 Actor registration / UDI·Devices registration / Notified Bodies & Certificates / Market Surveillance 4개로 한정**. Vigilance & PMS 모듈, CI/PS 모듈 미포함(개발 중). EC DG SANTE 공지 제목 및 본문 재확인.
- **정정 완료(본문 2개소 + 자매 1개소)**:
  - `SOP-FSCA-001` §5.12.2-3: "현재 이미 2026-05-28부터 의무" 삭제 → "Vigilance/PMS 모듈 의무화 시 전환"으로 미래시제 통일 + 4개 모듈 목록 명시.
  - `SOP-PMS-001` §8.2: "2026-05-28부터 EUDAMED 제출 의무" → "모듈 의무화 이전 현행은 NB 기존 경로, 의무화 후 EUDAMED 전환(Art.86(2)·Art.92)".
  - `SOP-PMS-001` §8.1: 의무화 4개 모듈 목록 + **Vigilance/PMS·CI/PS 미포함** 명문화(권고 4항, 재발 차단).
  - **동일클래스 proactive 적발**: `SOP-PSUR-001` §5.4 L131 "NB에 EUDAMED 경유 제출" — 감사 지적 범위 밖이었으나 동일 오류(미의무 모듈 경유 제출 단정). 현행 경로 명시로 정정.
- **확산 3개소 교정**: `11_일일리서치_2026-06-07` L56(정정 각주 삽입)·L88(인라인 정정), `12_교차검증_2026-06-07` L49 판정 `✅ 정확(EU MDR Art.86, RegDesk)` → **`❌ 오류`로 하향 + Tier2 인용을 사실근거에서 제거**, L80·L104 동반 하향. 로그류는 시점 기록으로 원문 보존 + 각주 정정 방식 적용.
- 자기모순 해소 확인: SOP-FSCA-001 §5.12.1(L332)·SOP-PMS-001 §8.3(L247)의 "미의무화" 서술과 정정 후 본문이 정합.

실운영 문서 미참고.

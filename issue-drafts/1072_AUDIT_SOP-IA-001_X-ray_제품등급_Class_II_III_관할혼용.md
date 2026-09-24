---
title: "audit #1072 (factuality/C5): SOP-IA-001 §14.4 'X-ray → Class II/III' — 관할 미표기·등급체계 혼용 (FDA 21 CFR 892.1680 = Class II, EU MDR Rule 10 = IIb, MFDS = 2등급/투시 3등급)"
labels: "audit:factuality,prio:P2,risk:low,regulatory,classification"
state: closed
created: 2026-09-25
created-by: md-process-auditor
related-issues: [1068, 1070]
sweep: "C5 x 02_품질경영시스템_QMS"
---

## 결함 개소

| 위치 | 현행 | 판정 |
|---|---|---|
| `02_품질경영시스템_QMS/SOP-IA-001_내부감사_절차.md` §14.4 L360 | `제품 안전 등급 (X-ray → Class II/III)` | **부정확** — 관할이 적혀 있지 않고, 한 표기 안에 서로 다른 등급체계가 섞여 있음 |

## 근거 (Tier1)
- **21 CFR 892.1680(b)** Stationary x-ray system: "Class II (special controls)" — eCFR(2026-09-11 현행) 직접 확인. FDA 진단용 X-ray에는 Class III가 없음.
- **EU MDR Annex VIII Rule 10** → 진단용 전리방사선 기기 **Class IIb** (audit #1070에서 확인). EU에는 'Class II'라는 등급이 없음.
- **MFDS 의료기기 품목 및 품목별 등급에 관한 규정** 별표: DR은 2등급, 투시는 3등급 (audit #1068에서 law.go.kr로 확인).
- 이 문단(L355)은 'QMSR/CP 7382.850'을 근거로 드는데, 그렇게 읽으면 FDA 등급 'Class III'로 오해할 수 있다.

## 정정 권고
`X-ray → MFDS 2등급(투시 3등급) / FDA Class II / EU MDR Class IIb`처럼 관할별로 풀어서 적을 것.

---

## 종결 (2026-09-25, audit-drain)

- SOP-IA-001 §14.4 → 'MFDS 2등급 / FDA Class II(892.1680) / EU MDR IIb(Rule 10)' 관할별 병기 (v0.3.1).
- **본 이슈 근거의 'MFDS 투시 3등급'은 구판 값** — law.go.kr 현행 [별표 1](flSeq=153998841) 직접 확인 결과 A11040.01/.02 **[2]등급**. 정정문은 2등급으로 반영. (감사 원장 `_audit_sweep_ledger.md` L70의 동일 표기는 수동편집 금지 대상이라 미수정 — 감사자 확인 요청)

실운영 문서 미참고.

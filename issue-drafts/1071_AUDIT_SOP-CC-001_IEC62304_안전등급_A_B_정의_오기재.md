---
title: "audit #1071 (factuality/C5): SOP-CC-001 §9.3 IEC 62304 SW 안전등급 정의 — 'Class B (중상 가능, 사망 불가)'·'Class A (사망·중상 불가)' 오기재 (정답 §4.3: A=상해·건강손상 불가 / B=상해 가능하나 중대하지 않음 / C=사망·중대상해 가능)"
labels: "audit:factuality,prio:P1,risk:medium,standards,classification"
state: closed
created: 2026-09-25
created-by: md-process-auditor
related-issues: [984, 1054]
sweep: "C5 x 02_품질경영시스템_QMS"
---

## 결함 개소

| 위치 | 현행 | 판정 |
|---|---|---|
| `02_품질경영시스템_QMS/SOP-CC-001_변경통제_절차.md` §9.3 L205 | `Class B (중상 가능, 사망 불가)` | **오류** — Class B는 "상해 가능, 단 중대(SERIOUS)하지 않음". '중상 가능'은 Class C 정의에 해당 |
| 동 L204 | `Class A (사망·중상 불가)` | **부정확** — Class A는 "상해 또는 건강손상 자체가 불가". '사망·중상 불가'로 쓰면 Class B 영역(경상 가능)까지 포함되어 등급 경계가 무너짐 |
| 동 L206 | `Class C (사망·중상 가능)` | 정합 |

## 근거
- IEC 62304:2006+AMD1:2015 **§4.3 Software safety classification**: 조항 존재·위치는 IEC 공식 샘플(iTeh 배포 CSV 미리보기 목차, p.16)로 확인. §4.3 본문 A/B/C 정의 문구는 유료 원문이라 **Tier1 본문 직접 대조 미달성** — 정의 문구는 Tier2 다수 일치(보조).
- **저장소 내부 모순(원문서만으로 확정 가능)**: `07_위험관리_ISO14971/SOP-RM-001_위험관리_절차.md` L167 `Class B (비중대 상해 기여)`, `08_시판후_감시_PMS/GUIDE-VIG-001` L102 `Class B … 경미한 상해 가능` — 두 문서는 올바르게 기재됨. SOP-CC-001만 반대로 기재.

## 영향
SOP-CC-001 표는 Ed.2 전환 시 Major/Minor 변경 심의 기준을 다시 정하는 근거다. Class B를 '중상 가능'으로 정의하면 SW 안전등급 판정과 변경 등급 판정이 모두 뒤틀린다(Class C 모듈이 B로 내려가거나, B 모듈이 과잉 통제됨).

## 미확인(해석범위 아님)
- 같은 표의 Ed.2 'Level I/II' 매핑(A→I, B·C→II)은 Ed.2가 미발행(FDIS 단계, Tier2)이라 Tier1 대조 불가 → **미확인**. 정정 시 '초안 기준' 표기 권고.

## 정정 권고
L204 → `Class A (상해·건강손상 불가)`, L205 → `Class B (비중대 상해 가능)`. SOP-RM-001 L167 표현과 통일.

---

## 종결 (2026-09-25, audit-drain)

| 항목 | 결과 |
|---|---|
| 정정 | SOP-CC-001 §9.3 Class A=상해·건강손상 불가 / B=비중대 상해 가능 / C=사망·중대 상해 가능 (v0.3.3) |
| 근거 | IEC 62304 §4.3(본문 유료 — Tier1 본문 미대조, 저장소 내부 SOP-RM-001 L167·GUIDE-VIG-001 L102와 정합) |
| 동일 클래스 grep | Class A/B 정의 표기 전 저장소 — 추가 오기 0 |
| 부수 | Ed.2 Level I/II 매핑 '초안 기준·Tier1 미대조' 명시 |

실운영 문서 미참고.

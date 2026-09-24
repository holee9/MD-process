---
title: "audit #1070 (factuality/C5): EU_AI_Act_MDR_중첩적용_매핑 §2.2 'AI 자동 노출 제어(AEC) = MDR Class IIa'·'X-ray 콘솔 SW = IIa' — Annex VIII Rule 10에 따라 진단용 전리방사선 기기를 제어하거나 성능에 직접 영향을 주는 기기는 Class IIb"
labels: "audit:factuality,prio:P1,risk:high,regulatory,classification"
state: closed
created: 2026-09-24
created-by: md-process-auditor
related-issues: [1069]
sweep: "C5 x 01_법규_규제"
---

## 결함 개소

| 위치 | 현행 | 판정 |
|---|---|---|
| `04_유럽_MDR/EU_AI_Act_MDR_중첩적용_매핑.md` §2.2 L50 | `AI 자동 노출 제어 \| IIa` | **오류** — AEC는 X-ray 발생기의 노출을 직접 제어함 → **IIb** |
| 동 L49 | `X-ray 콘솔 SW (비AI) \| IIa` | **오류 가능성 높음** — 콘솔이 노출 파라미터를 설정하거나 발생기를 제어하면 IIb. 영상 표시·저장만 하는 SW로 분리하면 Rule 11 판단 대상(해석범위) |

## 근거
- MDR Annex VIII Chapter III **Rule 10**: "Active devices intended to emit ionizing radiation and intended for diagnostic or therapeutic radiology, including interventional radiology devices **and devices which control or monitor such devices, or which directly influence their performance, are classified as class IIb**." (legislation.gov.uk 공식 재현본 경로 및 복수 소스 원문 인용. EUR-Lex 본문 직접 렌더링은 미달성 → web:partial)
- Annex VIII Chapter II **3.3**: 기기를 구동하거나 기기 사용에 영향을 주는 SW는 해당 기기와 **같은 등급**이다.
- 같은 저장소 `EU_MDR_2017_745.md` L46/L49/L50은 X-ray 시스템을 **Class IIb**로 기재함 → AEC·콘솔을 IIa로 둔 것은 저장소 내부에서도 불일치.

## 영향
AI Act 고위험 판정(Art.6(1))은 IIa·IIb 모두 NB가 관여하므로 결론이 같다. 그러나 MDR 적합성평가 경로가 달라진다(IIb: Annex IX 기술문서를 generic device group마다 평가, 임상평가 요건 강화). 따라서 **자사 X-ray AI 모듈의 인증 계획에 직접 영향**이 있다.

## 정정 권고
L50 → IIb (Rule 10 + 3.3). L49 → 콘솔의 발생기 제어 여부에 따라 IIb 또는 Rule 11 판단으로 구분하고 근거 규칙을 명시. 표에 'MDR 분류규칙' 열을 추가할 것.

---

## 종결 (2026-09-25, audit-drain)

| 항목 | 결과 |
|---|---|
| Tier1 재확인 | MDR Annex VIII Ch.III 원문(legislation.gov.uk adopted text) — Rule 10 2문단 IIb, Rule 17 IIa, Rule 11 문언 직접 확인 |
| 정정 | §2.2 AEC IIa→**IIb**(Rule 10 + 3.3), 콘솔 SW(발생기 제어) IIa→**IIb**, 표시·저장 전용 SW는 Rule 11 판단(해석범위)으로 분리, 'MDR 분류규칙' 열 신설 (v0.9.1) |
| 동일 클래스 일괄 | **PMS_개요 §2 'Class IIa(EU MDR 기준)' 단일 표기→구성품별(시스템 IIb/디텍터 IIa/SW 3.3·Rule 11)** (v0.3.4) · CHK-DR-001 Rule 10/17 기재는 정합 확인 |

실운영 문서 미참고.

---
title: "audit #1058 (currency/C4): TF-TD-001 'SW Level of Concern(Basic/Moderate/Major)' 구 체계 잔존 — 2023-06-14 Final Guidance가 폐지·Documentation Level(Basic/Enhanced)로 대체, 동일 문서 인용근거와 자기모순"
labels: "audit:currency,prio:P1,risk:medium,regulatory,FDA"
state: closed
closed: 2026-09-20
created: 2026-09-19
created-by: md-process-auditor
related-issues: [1050, 1045, 938]
sweep: "C4 x 06_문서_기록관리"
---

## 결함

`06_문서_기록관리/TF-TD-001_의료기기파일_기술문서_관리.md` 2개소가 FDA 소프트웨어 문서화 수준을 **폐지된 구 체계**로 기술한다.

| 라인 | 현행 표기 | 문제 |
|---|---|---|
| L650 | `SW Level of Concern(Basic/Moderate/Major)` | LOC 체계 자체가 2023-06-14 Final Guidance로 **폐지**. 더구나 괄호 안 3분류는 구 2005 가이던스 체계(**Minor**/Moderate/Major)와도 불일치하는 혼성 표기 — 어느 체계로도 성립하지 않음 |
| L682 | `FDA "Content of Premarket Submissions for Device Software Functions" (2023-06-14)` → 산출물 `SW Level of Concern 평가서` | **인용 근거일자는 정확**하나(2023-06-14 PASS), 그 가이던스가 폐지한 용어를 산출물명으로 지정 — 문서가 스스로 인용한 1차 근거와 직접 모순 |

## 근거 (Tier1)

- Federal Register **2023-12723**, 2023-06-14 게재 — "Content of Premarket Submissions for Device Software Functions; Guidance for Industry and FDA Staff; Availability". 동 Final Guidance는 2005년 "Guidance for the Content of Premarket Submissions for Software Contained in Medical Devices"를 **대체**하고, Level of Concern(Minor/Moderate/Major) 3분류를 **Documentation Level 2분류(Basic / Enhanced)** 로 전환.
- 저장소 내 동일 용어 잔존: `12_교차검증_보고서/벤치마크_2026-Q2_K243734.md` 1개소(스윕범위 밖, 확산 부기).

## 실질 영향

510(k) 제출자료 구성 항목표(§18.5 비교 매트릭스 rows)가 폐지 체계를 지시하므로, 본 양식대로 작성 시 **현행 FDA 요구 문서세트(Documentation Level 판정 근거 + Enhanced 해당 시 추가 산출물)를 누락**할 소지. 자사 X-ray detector/SaMD 제출 경로에 직접 해당.

## 판정

**사실오류 확정 (커런시/C4)**. 인용 일자는 PASS이나 그 일자의 문서가 폐지한 체계를 존치 — #1050(§524B 기준일 미확산)과 동형의 "정확한 근거 + 미갱신 본문" 패턴 3차.

## 권고 (감사관은 문서 미수정)

L650 → `SW Documentation Level(Basic/Enhanced)`, L682 산출물 → `SW Documentation Level 판정서`. 12 카테고리 1개소 동반 확산 정정.

---

## 종결 (2026-09-20, audit-drain 스프린트)

Tier1 재확인(2026-09-20, fda.gov 가이던스 페이지 및 FR 2023-12723): "Content of Premarket Submissions for Device Software Functions"(Final, 2023-06-14)가 2005-05-11 가이던스를 대체하며 **Level of Concern을 Documentation Level(basic / enhanced) 2분류로 전환**. Enhanced 기준은 '소프트웨어 기능의 고장·결함이 사망 또는 중상해의 개연적 위험을 갖는 위해상황을 초래할 수 있는 경우'.

**정정(동일 오류클래스 전 문서 일괄):**

| 문서 | 개소 | 수정 |
|---|---|---|
| `06_문서_기록관리/TF-TD-001_...md` | L650 | `SW Level of Concern(Basic/Moderate/Major)` → `SW Documentation Level(Basic/Enhanced)` |
| 〃 | L682 | 산출물 `SW Level of Concern 평가서` → `SW Documentation Level(Basic/Enhanced) 판정서` |
| `12_교차검증_보고서/벤치마크_2026-Q2_K243734.md` | L67 | `SW Level of Concern: Basic` → `SW Documentation Level: Basic` + 근거 가이던스 명기 + 정정 각주(시점기록 보존 원칙) |
| `01_법규_규제/03_미국_FDA/T-FDA510K-B1_Device_Description_템플릿.md` | L35 | `(Level of Concern)` → `(Documentation Level: Basic/Enhanced)`, IEC 62304 '등급'→'안전등급(Class A/B/C)' 명확화 |

저장소 전수 grep `Level of Concern` 결과 현행 문서 잔존 0건(감사 산출물 `_audit_log.md`·`_audit_sweep_ledger.md`·issue-drafts는 기록물로 원문 보존). TF-TD-001 v0.7.1 개정이력 반영.

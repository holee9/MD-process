---
doc-id: FDA_QMSR_2026
title: "FDA QMSR (Quality Management System Regulation) — 21 CFR Part 820 개정 요약"
type: Guide
version: v0.3
status: draft
category: 01_법규_규제
purpose: "FDA QMSR 핵심 변경사항, ISO 13485 참조편입 구조, FDA 추가요구사항 상세 및 X-ray 시스템 적용 지침"
applicable: [FDA QMSR 21 CFR 820, ISO13485:2016, 21 CFR 803, 21 CFR 830, 21 CFR Part 11, UDI]
forms: [F-QMSR-READINESS-001]
related-docs:
  - ISO13485_2016_요약
  - FDA_QMSR_820.35_vs_ISO13485_4.2.5
  - SOP-DOC-001
  - SOP-IA-001
  - SOP-MR-001
  - SOP-CAPA-001
  - SOP-CC-001
  - SOP-TRC-001
  - SOP-VAL-001
related-issues: [18, 23, 24, 27, 28, 44, 45, 50, 61, 65]
owner: RA/QA Lead
last-review: 2026-06-26
review-due: 2027-05-25
---

# FDA QMSR (Quality Management System Regulation) — 21 CFR Part 820 개정 요약

## 1. 규정 개요

| 항목 | 내용 |
|------|------|
| 규정 | 21 CFR Part 820 |
| 명칭 변경 | Quality System Regulation(QSR) → **Quality Management System Regulation(QMSR)** |
| 최종규칙 공포 | Federal Register 2024-01709 (2024.2.2) |
| 기술적 수정 | Federal Register 2025-21955 |
| **발효일** | **2026년 2월 2일** |
| 핵심 변경 | ISO 13485:2016을 참조편입(Incorporation by Reference)하고, FDA 추가요구를 별도 조항으로 보존 |

## 2. QMSR 구조 — ISO 13485 참조편입 방식

### 2.1 기본 원리
QMSR 하에서 21 CFR Part 820은 대부분의 조항 텍스트를 삭제하고 ISO 13485:2016 해당 조항을 직접 참조한다. 즉, 제조사는 ISO 13485:2016 원문을 보유하고 이를 기준으로 QMS를 운영해야 한다.

### 2.2 구조 매핑

현행 21 CFR Part 820(QMSR, 89 FR 7523, 2026-02-02 시행)의 **실재 활성 조항은 §820.1·820.3·820.7·820.10·820.35·820.45 뿐**이다(eCFR 확인). 나머지(§820.5, §820.20–820.30, §820.40, Subparts C–O)는 모두 **[Reserved]**이며, 구 QSR의 설계관리·경영책임·불만처리 등 요건은 별도 조항으로 남지 않고 §820.10을 통해 편입된 ISO 13485:2016으로 이관되었다.

| QMSR (21 CFR 820) | 상태·내용 | 대응 ISO 13485 조항 |
|-------------------|-----------|-------------------|
| §820.1 | 범위(Scope) | — |
| §820.3 | 정의(Definitions) | ISO 13485 §3 + FDA 추가 정의 |
| §820.5 | [Reserved] | — |
| §820.7 | 참조편입(Incorporation by reference) — ISO 13485:2016을 법적으로 편입 | (편입 근거) |
| §820.10 | 품질경영시스템 요구(Requirements for a QMS) — 제조사 QMS가 ISO 13485:2016 §4~8을 준수하도록 요구 | 4~8 전체 |
| §820.20 – §820.30 | [Reserved] — 설계관리 등 대부분 요건이 ISO 13485로 이관 | 설계·개발관리 = **7.3** |
| §820.35 | 기록관리(Control of records) — ISO 13485 기록관리에 FDA 추가요구 보완 | 4.2.5 보완 |
| §820.40 | [Reserved] | — |
| §820.45 | 기기 표시·포장 관리(Device labeling and packaging controls) | 7.5.1 보완 |
| Subparts C–O | [Reserved] | — |

> **설계관리(Design controls) 위치 주의**: 구 QSR §820.30(설계관리)은 QMSR에서 **[Reserved]로 삭제**되었고, 설계·개발관리 요건은 전적으로 **ISO 13485:2016 §7.3**이 담당하며 §820.10(및 §820.7 참조편입)을 통해 법적 효력을 갖는다. FDA는 §7.3을 구 §820.30과 실질적으로 동등하다고 본다. 문서에 "§820.30 설계관리"로 인용하지 말고 "ISO 13485 §7.3(§820.10 경유)"으로 인용한다.

### 2.3 구 QSR 조항의 QMSR 내 위치
- 구 QSR §820.20(경영책임)·§820.22(품질감사)·§820.25(인원)·§820.30(설계관리)·§820.198(불만처리) 등은 QMSR에서 **독립 조항으로 존치되지 않고** ISO 13485(경영책임 §5, 내부감사 §8.2.4, 인적자원 §6.2, 설계 §7.3, 불만처리 §8.2.2)로 이관되었다.
- **비공개 예외 폐지**: 구 QSR이 두었던 경영검토·내부감사·공급자감사 보고서의 FDA 비공개 예외가 QMSR에는 없다 → 해당 보고서를 **FDA 조사관이 열람 가능**. 실무상 내부감사·경영검토 보고서를 외부감사 수준 품질로 작성해야 한다.

## 3. FDA 추가 요구사항 (ISO 13485 외)

### 3.1 §820.20 — 경영검토 추가 입력

ISO 13485 §5.6 경영검토 입력에 더하여 다음을 추가 입력으로 요구:
- 시정조치(Correction) 정보
- 이전 경영검토 후속 조치 상태
- QMS 변경 또는 제품/서비스 변경 영향
- 불만처리 결과 및 규제보고(MDR) 현황

### 3.2 §820.25 — 라벨링·포장 관리

ISO 13485에서 불충분하다고 판단한 라벨링 관리 요구를 보강:
- 출하 전 라벨 정확성 검사 절차 수립
- UDI-DI가 라벨에 정확히 표기되었는지 검증
- 라벨 인쇄/부착 공정의 적격성 확인

### 3.3 §820.35 — 기록관리 추가요구 (Tier 1: eCFR §820.35 현행본, 89 FR 7523, 2024-02-02)

ISO 13485 §4.2.5(기록관리)에 더하여 다음 4개 하위항목을 둔다(Part 11/전자서명은 §820.35의 하위가 아닌 독립 규정으로 §3.6 참조).

| 하위항목 | 명칭 (eCFR 원문) | 내용 요약 | 보완 대상 ISO 13485 조항 |
|---|---|---|---|
| §820.35(a) | Records of complaints | 불만 검토·평가·조사 기록 유지. Part 803 보고 대상/조사 수행 대상 불만은 기기명·접수일·UDI/UPC·불만자 정보·내용·시정조치·회신 기록. 유사 불만 미조사 시 정당 사유 기록 | §8.2.2 보완 |
| §820.35(b) | Records of servicing activities | 서비스 활동에 대해 기기명·UDI/UPC·서비스 일자·수행자·수행 내용·시험·검사 데이터 최소기록 | §7.5.4 보완 |
| §820.35(c) | Unique Device Identification | 의료기기/배치별 UDI 기록 | §7.5.1·§7.5.8·§7.5.9 보완 |
| §820.35(d) | Confidentiality | 제조자가 기밀로 판단한 기록에 표시 가능 — FDA가 21 CFR Part 20 공개정보 규정상 공개 여부 판단을 보조 | (FDA 추가 — ISO 13485 대응 없음) |

> **주의:** §820.35에는 "전자서명/Part 11" 하위항목이 존재하지 않는다. 21 CFR Part 11은 §820.35의 하위가 아닌 독립 규정으로, §3.6 참조.

### 3.4 §820.45 — 기기 표시(Device Labeling) 검사

- 출하 전 라벨의 정확성(UDI, 기기명, 제조사, 사용설명서 참조)을 검사
- 검사 기록 유지

### 3.5 §820.198 — 불만처리 추가

- MDR(21 CFR 803) 보고 여부 결정을 문서화
- 보고 기한(30일/5영업일) 관리
- 미보고 결정 시 정당 사유 기록

### 3.6 §820.35 외부 관련 규정 — 21 CFR Part 11 (전자기록·전자서명)

21 CFR Part 11은 **§820.35의 하위항목이 아니다.** Part 11은 FDA 규제 대상 기록을 전자기록/전자서명으로 작성·보관·송수신하는 경우의 무결성·인증 요건을 규정한 독립 규정으로, QMSR 적용 시에도 별도로 적용된다.

- 적용 범위: 전자기록·전자서명을 종이/육필 서명과 동등하게 취급하기 위한 시스템 검증·감사추적·접근통제·서명 관리 등.
- §820.35와의 관계: 기록 자체(complaints·servicing·UDI 등)는 §820.35 요구를 따르고, 그 기록을 **전자적으로** 작성·보관할 경우 Part 11이 추가 적용.
- Tier 1: 21 CFR Part 11 (eCFR), FDA "Part 11, Electronic Records; Electronic Signatures — Scope and Application" Guidance(2003, 현행).

## 4. FDA 검사 프로그램 변경

| 항목 | 변경 전 | 변경 후 (2026.2.2~) |
|------|---------|---------------------|
| 검사 지침 | QSIT (Quality System Inspection Technique) | **Compliance Program 7382.850** |
| 폐지 프로그램 | — | 7382.845, 7383.001 폐지 |
| 지적 근거 문구 | 구 QSR 조항 인용 | **ISO 13485 조항 기반 인용** |
| Form 483/WL | QSR 기반 | QMSR + ISO 13485 기반 |

### 4.1 검사 대응 실무 절차

**검사 전 준비 (Who: RA/QA Lead / When: 연 1회 또는 검사 통보 시)**:
1. ISO 13485 조항별 현행 SOP 매핑표 준비
2. 경영검토·내부감사 보고서 FDA 열람 대비 검토
3. CAPA 현황 정리 (미결 건 해소 우선)
4. UDI/GUDID 등록 현황 확인
5. Part 11 준수 현황 점검 (전자기록 시스템)

**검사 중 대응 (Who: RA/QA Lead + 부서별 SME)**:
1. 조사관 요청 문서를 ISO 13485 조항 번호로 즉시 매핑·제공
2. 구두 답변 시 ISO 13485 용어 사용 (예: "top management", "risk-based approach")
3. 관찰사항(483 Observation) 수령 시 즉시 내부 검토·대응 계획 수립

**검사 후 후속 (Who: RA/QA Lead / When: 관찰사항 수령 후 15영업일 이내)**:
1. 서면 응답서 작성 (ISO 13485 조항 참조 포함)
2. CAPA 개시 (필요 시)
3. 경영검토 입력으로 반영

## 5. X-ray 시스템 제조사 적용 시 핵심 고려사항

### 5.1 UDI 관련
- X-ray 시스템 본체, 검출기(Detector), 콜리메이터 등 각 부속품(accessory)별 UDI-DI 발급
- GUDID 등록·갱신 절차 (모델 변경, SW 버전 업그레이드 시)
- 라벨에 UDI 바코드(GS1 또는 HIBCC) 정확 인쇄 검증

### 5.2 MDR 보고 관련
- 환자 선량 과다 노출 사고 → MDR 5영업일 보고 대상 여부 판단
- 영상 품질 저하로 인한 오진 가능성 → MDR 30일 보고 검토
- SW 오류(AEC 오작동, 선량 표시 오류) → MDR 보고 + SW CAPA

### 5.3 설계관리 (ISO 13485 §7.3, §820.10 경유 — 구 §820.30은 [Reserved])
- Class II X-ray 시스템: 설계관리 적용 (Class I 면제 아님)
- IEC 62304 SW 수명주기 프로세스와 통합
- 설계변경 시 510(k) 재제출 필요성 판단 절차

### 5.4 Part 11 전자기록
- 선량 교정 기록, 영상품질 시험 기록의 전자서명
- DICOM 로그, 시스템 이벤트 로그의 무결성 보장
- Audit trail 구현 (변경 이력 추적)

## 6. QMSR 전환 준비 체크리스트 (F-QMSR-READINESS-001)

### F-QMSR-READINESS-001: QMSR 전환 준비도 점검 양식

| No. | 점검 항목 | 대응 상태 | 갭/조치 필요사항 | 담당 | 목표일 |
|-----|----------|----------|----------------|------|--------|
| 1 | ISO 13485:2016 원문 보유 및 사내 배포 | ☐완료 ☐진행중 ☐미착수 | | | |
| 2 | QMS 절차서 → ISO 13485 조항 매핑표 작성 | ☐완료 ☐진행중 ☐미착수 | | | |
| 3 | §820.20 경영검토 추가 입력 항목 반영 | ☐완료 ☐진행중 ☐미착수 | | | |
| 4 | §820.25 라벨링 검사 절차 수립 | ☐완료 ☐진행중 ☐미착수 | | | |
| 5 | §820.35(a) Records of complaints — 불만 기록 7개 항목(기기명·접수일·UDI/UPC·불만자정보·내용·시정조치·회신) 양식 점검 | ☐완료 ☐진행중 ☐미착수 | | | |
| 6 | §820.35(b) Records of servicing activities — 서비스 기록 6개 항목(기기명·UDI/UPC·서비스일·수행자·서비스내용·시험검사데이터) 양식 점검 | ☐완료 ☐진행중 ☐미착수 | | | |
| 7 | §820.35(c) Unique Device Identification — 의료기기/배치별 UDI 기록 체계 구축 | ☐완료 ☐진행중 ☐미착수 | | | |
| 7a | §820.35(d) Confidentiality — 기밀 표시(21 CFR Part 20 공개정보 규정 연계) 절차 수립 | ☐완료 ☐진행중 ☐미착수 | | | |
| 7b | (§820.35 외) 21 CFR Part 11 전자기록·전자서명 적합성 점검 — §820.35와 별도 독립 항목 | ☐완료 ☐진행중 ☐미착수 | | | |
| 8 | §820.45 라벨 정확성 검사 절차 수립 | ☐완료 ☐진행중 ☐미착수 | | | |
| 9 | §820.198 불만처리 MDR 연계 절차 갱신 | ☐완료 ☐진행중 ☐미착수 | | | |
| 10 | 내부감사 보고서 FDA 열람 대비 품질 검토 | ☐완료 ☐진행중 ☐미착수 | | | |
| 11 | 경영검토 보고서 FDA 열람 대비 품질 검토 | ☐완료 ☐진행중 ☐미착수 | | | |
| 12 | 검사 대응 절차 갱신 (7382.850 기반) | ☐완료 ☐진행중 ☐미착수 | | | |
| 13 | 교육훈련: QMSR 변경사항 전 직원 교육 | ☐완료 ☐진행중 ☐미착수 | | | |

**작성 지침**: RA/QA Lead가 분기별 점검. 미완료 항목은 CAPA 또는 경영검토 입력으로 에스컬레이션.

## 7. 출처

- FDA QMSR 공식 안내: fda.gov/medical-devices/postmarket-requirements-devices/quality-management-system-regulation-qmsr
- FDA QMSR FAQ: fda.gov/medical-devices/quality-management-system-regulation-qmsr/quality-management-system-regulation-frequently-asked-questions
- eCFR 21 CFR Part 820 (2026-02-02 시행): ecfr.gov/current/title-21/chapter-I/subchapter-H/part-820
- Federal Register: 2024-01709 (제정), 2025-21955 (기술적 수정)
- FDA Compliance Program 7382.850
- 확인일: 2026-05-25

## 8. 개정이력

| 버전 | 일자 | 변경사항 | 근거 |
|---|---|---|---|
| v0.1 | 2026-05-20 | 최초작성 | — |
| v0.2 | 2026-05-25 | §3.3 표 기재(추후 사실오류 식별) | — |
| v0.3 | 2026-06-26 | §3.3 §820.35(a)(b)(c)(d) Tier 1 정정(complaints/servicing/UDI/confidentiality), Part 11을 §3.6 독립 규정으로 분리, §6 F-QMSR-READINESS-001 No.5·6·7·7a·7b 재라벨 | audit #917 (P0), eCFR §820.35 현행본, 89 FR 7523 (2024-02-02) |

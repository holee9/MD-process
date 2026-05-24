---
doc-id: FDA_QMSR_2026
title: "FDA QMSR (Quality Management System Regulation) — 21 CFR Part 820 개정 요약"
type: Guide
version: v0.2
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
last-review: 2026-05-25
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

| QMSR (21 CFR 820) | 내용 | 대응 ISO 13485 조항 |
|-------------------|------|-------------------|
| §820.1 | 범위 | — |
| §820.3 | 정의 | ISO 13485 §3 + 추가 정의 |
| §820.10 | ISO 13485 참조편입 선언 | 4~8 전체 |
| §820.20 | 경영검토 추가 입력 | 5.6 보완 |
| §820.25 | 라벨링·포장 관리 | 7.5 보완 |
| §820.30 | 설계관리 유지 (Class I 면제 외) | 7.3 보완 |
| §820.35 | 기록관리 추가요구 | 4.2.5 보완 |
| §820.45 | 기기 표시 검사 | 신설 |
| §820.180 | (폐지) 기밀성 예외 | — |
| §820.198 | 불만처리 추가 | 8.2.2 보완 |

### 2.3 폐지된 조항 — 주요 영향
- **§820.180(c) 폐지**: 경영검토, 내부감사, 공급자 감사 보고서에 대한 FDA 비공개 예외 폐지 → **FDA 조사관이 열람 가능**
- 실무 영향: 내부감사·경영검토 보고서를 외부감사 수준의 품질로 작성해야 함

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

### 3.3 §820.35 — 기록관리 추가요구

| 구분 | 추가 요구 | 근거 규정 |
|------|-----------|-----------|
| (a) MDR 기록 | 불만·서비스 활동 정보, 보고 결정 근거, 미보고 사유 기록 | 21 CFR 803 |
| (b) UDI 기록 | UDI 발급·변경이력, GUDID 제출 기록 | 21 CFR 830 |
| (c) 기밀성 | FDA 송수신 기록의 기밀 표시 | 18 USC 1905 등 |
| (d) 전자서명 | 전자기록·전자서명 시 21 CFR Part 11 준수 | Part 11 |

### 3.4 §820.45 — 기기 표시(Device Labeling) 검사

- 출하 전 라벨의 정확성(UDI, 기기명, 제조사, 사용설명서 참조)을 검사
- 검사 기록 유지

### 3.5 §820.198 — 불만처리 추가

- MDR(21 CFR 803) 보고 여부 결정을 문서화
- 보고 기한(30일/5영업일) 관리
- 미보고 결정 시 정당 사유 기록

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

### 5.3 설계관리 (§820.30)
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
| 5 | §820.35(a) MDR 결정 기록 양식 준비 | ☐완료 ☐진행중 ☐미착수 | | | |
| 6 | §820.35(b) UDI 기록 관리 체계 구축 | ☐완료 ☐진행중 ☐미착수 | | | |
| 7 | §820.35(d) Part 11 전자기록 적합성 점검 | ☐완료 ☐진행중 ☐미착수 | | | |
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

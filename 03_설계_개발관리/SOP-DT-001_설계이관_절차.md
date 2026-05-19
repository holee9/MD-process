---
doc-id: SOP-DT-001
title: 설계이관(Design Transfer) 절차
type: SOP
version: v0.1
status: draft
category: 03_설계_개발관리
purpose: 설계·개발 산출물을 제조 공정으로 이관하는 절차, 책임, 검증 기준을 정의하여 생산 준비 상태 보장
applicable: [ISO13485:2016 §7.3.8, FDA QMSR, EU MDR 2017/745 Annex II §4, IEC62304, IEC60601-2-54, ISO14971:2019]
forms: [F-DT-001, F-DT-002]
related-docs: [설계개발_프로세스, CHK-DR-001, SOP-MFG-001, SOP-VAL-001, SOP-CAL-001, SOP-PKG-001, SOP-IQ-001, SOP-CC-001]
related-issues: []
owner: 설계개발 Lead / 생산기술 Lead
last-review: 2026-05-20
review-due: 2027-05-20
---

# 설계이관(Design Transfer) 절차 — v0.1

## 1. 목적

본 절차는 의료용 X-ray 시스템(HW, detector, SW, AI 구성요소 포함)의 설계·개발 산출물을 제조 공정으로 이관하는 전 과정을 정의한다. 설계 산출물이 제조에 적합함을 검증하고, 생산 역량이 제품 요구사항을 충족할 수 있음을 확인한다.

## 2. 적용 범위

- 신규 제품의 설계·개발 완료 후 양산 이관
- 주요 설계변경(Major Change) 후 재이관
- 제조 사이트 변경 시 이관
- SW/FW 릴리스의 생산 빌드 이관

## 3. 규제 근거

| 규제/표준 | 조항 | 핵심 요구 |
|-----------|------|-----------|
| ISO 13485:2016 | §7.3.8 | 설계·개발 출력의 제조 이관 절차 문서화, 이관 전 제조 적합성 검증, 생산 역량 충족 확인 |
| FDA QMSR | ISO 13485 §7.3.8 편입 | 구 21 CFR 820.30(h) Design Transfer 대응 |
| EU MDR 2017/745 | Annex II §4 | 설계·제조 정보, 공정 밸리데이션, 품질관리 정보 기술문서 포함 |
| IEC 62304 | §5.8 | SW 릴리스 관리 |
| IEC 60601-2-54 | 전체 | X-ray 장비 기본안전·필수성능 생산 시 유지 보장 |

## 4. 용어 정의

| 용어 | 정의 |
|------|------|
| DDF (Design and Development File) | 설계·개발 파일 (구 DHF) |
| MDF (Medical Device File) | 의료기기 파일 (구 DMR + DMR 관련 기록) |
| DTP (Design Transfer Plan) | 설계이관 계획서 |
| DTR (Design Transfer Report) | 설계이관 보고서 |
| Production Spec | 제조 사양서 (도면, BOM, SW 빌드, 시험사양 등) |

## 5. 책임과 권한

| 역할 | 책임 |
|------|------|
| 설계개발 Lead | DTP 작성, 설계 산출물 패키지 준비, 이관 검토 주관 |
| 생산기술 Lead | 제조 가능성 평가, 공정 밸리데이션 수행, 생산 라인 준비 |
| QA Manager | 이관 전 DDF 완결성 검토, 공정 밸리데이션 승인, 최종 이관 승인 |
| RA Lead | 규제 제출 서류 정합성 확인, UDI 발급 확인 |
| 구매/공급자 관리 | 공급자 승인 및 자재 조달 준비 확인 |
| 서비스 Lead | 설치·서비스 매뉴얼 준비, 현장 교육 자료 확인 |
| 경영진 | DR5 최종 이관 승인 |

## 6. 절차

### 6.1 Phase 1 — 이관 기획 (Transfer Planning)

**입력 조건**: DR4(설계 확인 완료 검토) 통과

1. 설계개발 Lead가 DTP(설계이관 계획서) 작성
   - 이관 범위 (HW, SW, AI, 라벨링, 문서 등)
   - 이관 산출물 목록 (도면, BOM, SW 빌드, 시험절차 등)
   - 공정 밸리데이션 대상 및 일정
   - 이관 완료 기준 (Acceptance Criteria)
   - 역할·책임·일정

2. 이관 산출물 패키지 준비:
   - 최종 제조 도면 (승인 버전)
   - BOM (부품표) 확정본
   - 자재 사양서 (원재료, 구성품)
   - 조립·제조 작업지시서 (Work Instruction)
   - SW 릴리스 패키지 (빌드 절차, 버전 태그, SBOM)
   - 출하검사 절차(ITP) 및 합격 기준
   - 라벨링·포장 사양
   - 설치·서비스 매뉴얼

3. 생산기술 Lead가 제조 가능성(Manufacturability) 사전 평가:
   - 장비·설비 가용성
   - 클린룸 등급 적합성 (SOP-MFG-002 참조)
   - 작업자 역량 및 교육 필요성

### 6.2 Phase 2 — 공정 밸리데이션 (Process Validation)

1. **IQ (Installation Qualification)**
   - 제조 장비·설비 설치 적격성 확인 (SOP-IQ-001 참조)
   - 측정 장비 교정 확인 (SOP-CAL-001 참조)

2. **OQ (Operational Qualification)**
   - 공정 파라미터 범위 내 동작 확인
   - 최악 조건(worst case) 시험

3. **PQ (Performance Qualification)**
   - 실제 생산 조건에서 연속 3배치 이상 합격 확인
   - 통계적 공정 관리(SPC) 초기 데이터 수집
   - X-ray 관련: 선량 재현성, 영상품질(QC 프로토콜) 합격 확인

4. **SW 빌드 검증**
   - 생산 빌드 환경에서 SW 빌드 재현성 확인
   - 빌드 해시값 일치 검증
   - 릴리스 노트 확정

### 6.3 Phase 3 — 이관 검증 (Transfer Verification)

1. **생산 시제품(Pilot Run) 제작**
   - 생산 라인에서 최소 3대 이상 시제품 제작
   - 시제품의 설계 사양 충족 여부 전수검사

2. **출하검사 절차 확인**
   - ITP(Inspection and Test Procedure) 실행 가능성 검증
   - 검사 장비 교정 상태 확인
   - 합격/불합격 판정 기준 명확성 검증

3. **추적성 확인**
   - UDI 부여 적정성 (SOP-UDI-001)
   - 자재 LOT 추적성 확보
   - DI(Device Identifier) 및 PI(Production Identifier) 연결

4. **라벨링·포장 확인**
   - 라벨 내용 정확성 (SOP-PKG-001)
   - 포장 무결성 시험

### 6.4 Phase 4 — 이관 승인 (Transfer Approval)

1. **DR5 (설계이관 승인 검토)**
   - CHK-DR-001 §5.6 체크리스트 항목 전수 확인
   - 모든 NCR/OFI 해결 확인

2. **DTR (설계이관 보고서) 작성**
   - 이관 활동 요약
   - 공정 밸리데이션 결과 요약
   - Pilot Run 결과
   - 미결 사항 및 후속 조치
   - 이관 판정: 승인(Approved) / 조건부 승인(Conditional) / 보류(Hold)

3. **최종 승인**
   - QA Manager, 설계개발 Lead, 생산기술 Lead, 경영진 서명
   - 승인 시 MDF(Medical Device File) 확정

4. **MDF 발행**
   - Production Spec 최종본 등록
   - 설계동결(Design Freeze) 선언
   - 이후 변경은 SOP-CC-001(변경통제 절차) 적용

## 7. 이관 완료 기준

다음 항목이 모두 충족되어야 이관 승인 가능:

| # | 기준 | 검증 방법 |
|---|------|-----------|
| 1 | DDF 완결성 — 모든 설계 단계 기록 포함 | QA 체크리스트 검토 |
| 2 | 공정 밸리데이션(IQ/OQ/PQ) 전 항목 합격 | 밸리데이션 보고서 |
| 3 | Pilot Run 시제품 출하검사 100% 합격 | 검사 기록 |
| 4 | SW 빌드 재현성 확인 | 빌드 로그, 해시 비교 |
| 5 | 잔여 위험 수용 — 경영진 승인 | 위험관리 보고서 |
| 6 | 라벨링·UDI 적정성 확인 | 라벨 검토 기록 |
| 7 | 교육 훈련 완료 (생산·QC·서비스) | 교육 기록 (F-TRN-001) |
| 8 | 공급자 승인 및 SQA 체결 확인 | 공급자 기록 |
| 9 | PMS 계획(PMCF, PSUR) 수립 확인 | PMS 계획서 |
| 10 | 규제 제출 준비 완료 (해당 시) | RA 확인서 |

## 8. 기록 및 양식

| 양식 ID | 명칭 | 용도 |
|---------|------|------|
| F-DT-001 | 설계이관 체크리스트 | Phase 1~4 활동 완료 확인 |
| F-DT-002 | 설계이관 보고서 양식 | DTR 표준 양식 |

## 9. 관련 문서

- 설계개발_프로세스 — 전체 설계·개발 프로세스
- CHK-DR-001 — 설계검토 체크리스트
- SOP-MFG-001 — 제조공정 관리 절차
- SOP-MFG-002 — 클린룸 관리
- SOP-VAL-001 — SW 검증·밸리데이션 절차
- SOP-CAL-001 — 교정관리 절차
- SOP-PKG-001 — 라벨링·포장관리
- SOP-IQ-001 — 설치검증·수용시험
- SOP-CC-001 — 변경통제 절차
- SOP-TRN-001 — 교육훈련 절차

## 10. 변경 이력

| 버전 | 일자 | 변경 내용 | 작성자 |
|------|------|----------|--------|
| v0.1 | 2026-05-20 | 초안 작성 — 4-Phase 이관 절차, X-ray/SW/AI 특수 요구 반영, 공정 밸리데이션 연계 | QA/RA |

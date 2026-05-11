---
doc-id: SOP-RM-001
title: 위험관리 절차
type: SOP
version: v0.1
status: draft
category: 07_위험관리_ISO14971
purpose: ISO 14971:2019 기반 의료기기 위험관리 프로세스 전주기 절차를 정의하고, FMEA·FTA 기법을 통합하여 위험 식별·평가·통제·잔여위험 수용의 체계를 확립한다
applicable:
  - ISO13485:2016 §7.1
  - ISO14971:2019
  - IEC60601-1 §14
  - IEC60601-2-54
  - EU MDR 2017/745 Annex I
  - FDA QMSR
  - IEC62304 §7
  - IEC81001-5-1
forms: [F-RM-001, F-RM-002, F-RM-003]
related-docs: [ISO14971_프로세스_상세, 위험관리_개요, SOP-CC-001]
related-issues: [7, 21, 48]
owner: RA/QA Lead
last-review: 2026-05-12
review-due: 2027-05-12
---

# SOP-RM-001 위험관리 절차 v0.1

## 1. 목적

본 절차는 의료용 X-ray 시스템(detector·SW 포함)의 구상 단계부터 폐기까지 전주기에 걸친 위험관리 프로세스를 정의한다. ISO 14971:2019 요구사항을 충족하고, EU MDR Annex I 일반 안전·성능 요구사항(GSPR) 및 FDA QMSR 위험 기반 접근법에 부합하는 것을 목표로 한다.

## 2. 적용 범위

- 의료기기 하드웨어(X-ray tube, generator, collimator, detector assembly)
- 내장 소프트웨어(영상 획득·처리·표시, DICOM 통신, 사이버보안 모듈)
- AI/ML 구성요소(영상 전처리, 자동 노출 제어, 화질 최적화)
- 부속품·소모품(grid, 환자 포지셔닝 보조기구)
- 서비스 활동(설치, PM, 교정, 해체)

## 3. 용어 정의

| 용어 | 정의 |
|------|------|
| 위해(Hazard) | 잠재적 피해 원인 |
| 위해상황(Hazardous Situation) | 사람·재산·환경이 위해에 노출되는 상황 |
| 피해(Harm) | 사람의 건강에 대한 상해 또는 손상 |
| 심각도(Severity) | 피해의 심각한 정도 |
| 발생확률(Probability of Occurrence) | 위해상황이 피해로 이어질 확률 |
| 위험(Risk) | 피해의 심각도와 발생확률의 조합 |
| 잔여위험(Residual Risk) | 위험 통제 수단 적용 후 남은 위험 |
| ALARP | As Low As Reasonably Practicable |

## 4. 책임과 권한

| 역할 | 책임 |
|------|------|
| 경영대표 | 위험관리 방침 승인, 자원 배분, 잔여위험 수용 최종 결정 |
| RA/QA Lead | 위험관리 파일(RMF) 총괄, 위험 평가·통제 조율 |
| 설계팀 | 위해 식별, FMEA·FTA 수행, 위험 통제 수단 설계·구현 |
| SW팀 | SW 관련 위해 식별(IEC 62304 §7), 사이버보안 위협 분석(IEC 81001-5-1) |
| 방사선안전관리자 | 방사선 관련 위해(ALARA, 선량 초과) 평가·통제 |
| 임상/규제 | 임상 benefit-risk 분석, 규제기관 보고 |

## 5. 절차

### 5.1 위험관리 계획 (Risk Management Plan)

위험관리 계획서(F-RM-001)에는 다음 사항을 포함한다.

1. 적용 범위 — 대상 의료기기·수명주기 단계
2. 책임·권한 배분
3. 위험 수용 기준(Acceptability Criteria)
4. 검증 활동 계획
5. 생산·시판 후 정보 수집 방법
6. 위험관리 활동 시기·검토 주기

**위험 수용 매트릭스:**

| 심각도 \ 확률 | 빈번(5) | 때때로(4) | 가끔(3) | 드묾(2) | 극히 드묾(1) |
|---|---|---|---|---|---|
| 치명적(5) | 불허 | 불허 | 불허 | ALARP | ALARP |
| 중대(4) | 불허 | 불허 | ALARP | ALARP | 수용 |
| 보통(3) | 불허 | ALARP | ALARP | 수용 | 수용 |
| 경미(2) | ALARP | ALARP | 수용 | 수용 | 수용 |
| 무시(1) | ALARP | 수용 | 수용 | 수용 | 수용 |

### 5.2 위해 식별 (Hazard Identification)

사용 시나리오·사용 오류·장애 모드·환경 조건·사이버 위협별로 위해를 식별한다. X-ray 시스템 특유 위해 범주:

- 방사선 과다 노출(tube output 초과, AEC 오작동, collimator 오정렬)
- 영상 품질 저하(detector defect pixel, gain drift → 오진)
- 전기적 위험(고전압 회로, 접지 결함)
- 기계적 위험(갠트리 충돌, 환자 낙상)
- SW 오동작(영상 좌우 반전, 환자 ID 불일치, DICOM 전송 실패)
- AI/ML 오류(drift에 의한 노출 파라미터 오산출, 편향)
- 사이버보안(랜섬웨어에 의한 가용성 상실, 환자정보 유출)
- 사용 오류(IEC 62366-1 연계)

### 5.3 위험 분석 (Risk Analysis)

식별된 위해별로 위해상황·피해·심각도·발생확률을 분석하여 위험을 추정한다.

**분석 기법:**
- **FMEA (Failure Mode and Effects Analysis):** 구성요소·기능별 고장 모드, 원인, 영향, RPN 산출
- **FTA (Fault Tree Analysis):** 최상위 사건(Top Event: 환자 과다 피폭 등)에서 역추적
- **HAZOP:** 공정·사용 시나리오 체계적 편차 분석
- **위협 모델링(Threat Modeling):** STRIDE/DREAD 기반 사이버보안 위해 분석

기록 양식: F-RM-002 위험분석 워크시트

### 5.4 위험 평가 (Risk Evaluation)

5.1항의 수용 기준 매트릭스 대비 각 위험을 판정한다.
- **불허(Unacceptable):** 반드시 위험 통제 필요
- **ALARP:** 실현 가능한 한 위험 저감 후 benefit-risk 분석으로 수용 여부 결정
- **수용(Acceptable):** 현 수준 유지, 모니터링

### 5.5 위험 통제 (Risk Control)

위험 통제 수단의 우선순위(ISO 14971 §7.1):
1. **본질적 안전 설계(Inherent Safety by Design):** 위해 자체 제거·감소
2. **보호 수단(Protective Measures):** 경보, 인터록, 차폐, SW safety function
3. **안전성 정보(Information for Safety):** 경고 라벨, 사용설명서, 교육

각 통제 수단의 구현·검증을 기록하고, 신규 위해 도입 여부를 확인한다.

**X-ray 특수 통제 예시:**
- AEC 최대 노출 시간 HW 인터록
- 투시(Fluoroscopy) 5분 경보, 10분 강제 차단
- Collimator 자동 추종 실패 시 노출 차단
- Detector 결함 pixel > 임계치 시 영상 획득 중단 + 경고

### 5.6 잔여위험 평가 (Residual Risk Evaluation)

모든 통제 수단 적용 후 개별 잔여위험 및 전체(Overall) 잔여위험을 평가한다.
- 전체 잔여위험이 수용 불가 시 benefit-risk 분석 수행
- 잔여위험 정보를 부속문서(IFU)에 반영

### 5.7 위험관리 검토 (Risk Management Review)

위험관리 파일의 완결성을 검토한다:
- 위험관리 계획이 적절히 이행되었는가
- 전체 잔여위험이 수용 가능한가
- 생산·시판 후 정보 수집 방법이 적절한가

검토 결과를 경영대표에게 보고, 승인을 득한다.

### 5.8 생산 및 시판 후 활동 (Production & Post-Production)

- PMS 데이터(불만, FSCA, PSUR)에서 신규 위해 또는 위험 변동 정보 수집
- 변경 발생 시 SOP-CC-001에 따라 위험 재평가
- AI/ML 모델 업데이트 시 성능 drift 재평가
- 수집 정보를 위험관리 파일에 피드백

## 6. 위험관리 파일(RMF) 구성

| 구성 항목 | 양식/문서 |
|-----------|-----------|
| 위험관리 계획서 | F-RM-001 |
| 위험분석 워크시트(FMEA/FTA) | F-RM-002 |
| 위험 통제 추적표 | F-RM-003 |
| Benefit-Risk 분석 | 해당 시 별도 첨부 |
| 검증 기록 | 설계·시험 문서 참조 |
| 위험관리 검토 보고서 | 별도 작성 |

## 7. 관련 문서

- ISO14971_프로세스_상세 (07_위험관리_ISO14971)
- 위험관리_개요 (07_위험관리_ISO14971)
- SOP-CC-001 변경통제 절차 (02_QMS)
- SOP-PMS-001 불만처리·부작용보고 (08_PMS)
- IEC 62304 SW 수명주기 (03_설계개발)
- IEC 81001-5-1 사이버보안 (03_설계개발)

## 8. 개정 이력

| 버전 | 일자 | 변경 내용 | 작성자 |
|------|------|-----------|--------|
| v0.1 | 2026-05-12 | 초안 작성 | RA/QA Lead |

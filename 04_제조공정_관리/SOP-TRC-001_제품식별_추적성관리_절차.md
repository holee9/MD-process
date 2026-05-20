---
doc-id: SOP-TRC-001
title: 제품식별 및 추적성관리 절차
type: SOP
version: v0.1
status: draft
category: 04_제조공정_관리
purpose: 의료용 X-ray 시스템·디텍터·SW의 원자재부터 최종 출하·시판후까지 전 수명주기 식별 및 추적성을 보장하는 절차
applicable:
  - ISO 13485:2016 §7.5.8
  - ISO 13485:2016 §7.5.9
  - FDA QMSR (21 CFR Part 820 → ISO 13485 편입)
  - 21 CFR Part 821 (Device Tracking)
  - 21 CFR Part 830 (UDI System)
  - EU MDR 2017/745 Article 25 (Identification within the supply chain)
  - EU MDR 2017/745 Article 27 (Unique Device Identification)
  - EU MDR 2017/745 Annex VI Part C (UDI System)
  - IEC 60601-1 §7.2.10 (Marking, serial/lot identification)
  - MFDS 의료기기 제조 및 품질관리 기준 §16 (식별 및 추적성)
forms:
  - F-TRC-001
  - F-TRC-002
related-docs:
  - SOP-MFG-001
  - SOP-PKG-001
  - SOP-UDI-001
  - SOP-NC-001
  - SOP-FSCA-001
  - SOP-PMS-001
related-issues: []
owner: QA/RA Lead
last-review: 2026-05-21
review-due: 2027-05-21
---

# SOP-TRC-001 — 제품식별 및 추적성관리 절차

## 1. 목적

본 절차는 의료용 X-ray 시스템(X-ray generator, tube assembly, detector, SW)의 원자재 입고부터 완제품 출하·설치·시판후 단계까지 모든 구성품 및 제품의 **식별(Identification)**과 **추적성(Traceability)**을 체계적으로 관리하기 위함이다.

## 2. 적용 범위

- X-ray 발생장치(generator), 튜브 어셈블리, 디지털 디텍터(flat panel detector)
- 임베디드 SW 및 AI 기반 영상처리 모듈
- 핵심 구성품: HV 케이블, 콜리메이터, 그리드, 기구부(stand/table)
- 포장재·라벨·IFU(사용설명서)
- 위탁 제조(OEM/ODM) 공급 구성품

## 3. 용어 정의

| 용어 | 정의 |
|------|------|
| UDI (Unique Device Identification) | EU MDR Article 27 / 21 CFR 830에 따른 고유기기식별코드 |
| UDI-DI (Device Identifier) | 제조자·제품 모델을 특정하는 정적 식별자 |
| UDI-PI (Production Identifier) | 로트·시리얼·제조일·유효기한 등 생산 단위 식별자 |
| Basic UDI-DI | 제품군 수준의 최상위 식별자 (EUDAMED 등록용) |
| DHR (Device History Record) | 개별 기기 또는 로트별 제조 이력 기록 |
| MDF (Medical Device File) | FDA QMSR 상 DMR 대체 용어 (ISO 13485 §4.2.3 편입) |
| 로트 번호 (Lot/Batch No.) | 동일 조건에서 제조된 단위 그룹 식별 번호 |
| 시리얼 번호 (Serial No.) | 개별 기기 고유 식별 번호 |

## 4. 책임과 권한

| 역할 | 책임 |
|------|------|
| QA/RA Lead | 본 SOP 수립·유지, UDI 등록 총괄, 추적성 감사 |
| 생산 관리자 | 로트/시리얼 번호 부여·기록, DHR 작성 |
| 자재 관리자 | 입고 원자재·구성품 식별 라벨 부착, 입고 검사 기록 |
| SW 개발팀 | SW 버전 식별(Git tag, SBOM), SW 빌드 추적성 |
| 물류/출하 담당 | 출하 기록, UDI 라벨 최종 확인 |
| 서비스 엔지니어 | 현장 설치·수리 시 시리얼 번호 확인 및 서비스 기록 |

## 5. 식별 체계

### 5.1 제품 식별 코드 구조

```
[제품군]-[모델코드]-[구성유형]-[시리얼/로트]
예: XRS-5000-GEN-SN240001   (X-ray System 5000, Generator, Serial No.)
    XRS-5000-DET-SN240001   (Detector)
    XRS-5000-SW-v2.3.1-B045 (SW version, Build)
```

### 5.2 원자재·구성품 식별

- 입고 시 자재 관리자가 **입고 검사 라벨** 부착
- 라벨 항목: 자재명, 공급자 로트 번호, 입고일, 입고 검사 상태(합격/불합격/보류)
- 불합격 자재는 별도 격리구역 보관, 빨간색 부적합 라벨 부착
- 입고 기록은 ERP/MES에 등록, 공급자 로트 번호 ↔ 사내 로트 번호 매핑

### 5.3 공정 중 식별

- 각 공정 단계에서 **공정 이동표(Traveler Card)** 또는 MES 바코드 스캔으로 상태 추적
- 공정 상태 라벨: 검사 대기(노란색), 합격(녹색), 부적합(빨간색), 재작업(주황색)
- 조립 공정에서 핵심 구성품(HV cable, X-ray tube, detector panel) 시리얼 번호를 DHR에 기록
- SW 빌드: Git commit hash + 빌드 번호를 제품 SW 정보에 내장

### 5.4 완제품 식별 및 UDI

- 완제품 라벨: 제품명, 모델명, 시리얼 번호, 제조일, 제조자명·주소, CE 마크(해당 시), UDI 바코드(GS1 또는 HIBCC)
- IEC 60601-1 §7.2.10 마킹 요구사항 준수
- UDI 구성:
  - UDI-DI: GS1 GTIN 또는 HIBCC 기반
  - UDI-PI: 시리얼 번호 + 제조일
- EUDAMED 및 FDA GUDID 데이터베이스에 UDI-DI 등록
- Class IIb 이상 X-ray 장비: 개별 시리얼 번호 기반 UDI-PI 필수

### 5.5 SW 식별 및 추적성

- SW 버전 관리: SOP-SBOM-001에 따른 SBOM(Software Bill of Materials) 생성
- 각 릴리스 버전의 Git tag, commit hash, 빌드 환경 기록
- AI 모델: 모델 버전, 학습 데이터셋 ID, 하이퍼파라미터 해시 기록
- SW 변경 시 SOP-CC-001(변경통제)에 따른 변경 이력 추적

## 6. 추적성 절차

### 6.1 전방 추적성 (Forward Traceability)

원자재 → 구성품 → 반제품 → 완제품 → 출하처 방향의 추적.

| 단계 | 추적 항목 | 기록 매체 |
|------|----------|----------|
| 원자재 입고 | 공급자 로트 → 사내 로트 매핑 | ERP/입고 대장 |
| 조립 | 구성품 시리얼 → 완제품 시리얼 매핑 | DHR/MES |
| 시험·검사 | 시험 성적서 → 완제품 시리얼 연결 | DHR |
| 출하 | 완제품 시리얼 → 고객/설치처 매핑 | 출하 대장/ERP |
| 설치 | 시리얼 → 설치처 주소·일자·설치자 | 설치 기록서 |

### 6.2 역방향 추적성 (Backward Traceability)

완제품 또는 시장 불만 접수 시 역추적하여 원인 자재·공정·작업자 특정.

- 완제품 시리얼 번호 → DHR 조회 → 구성품 로트/시리얼 → 원자재 로트 → 공급자 출하 기록
- FSCA(현장안전시정조치) 시 영향 받는 로트/시리얼 범위 24시간 이내 특정 가능해야 함
- SOP-FSCA-001과 연계하여 리콜 범위 신속 결정

### 6.3 DHR (Device History Record) 관리

각 완제품(또는 로트)별 DHR은 다음을 포함:

- 제품 식별 정보(모델, 시리얼, UDI)
- 사용된 원자재·구성품 로트/시리얼 목록
- 각 제조 공정 기록(작업자, 일시, 장비, 환경 조건)
- 공정 중 검사·시험 결과
- 최종 검사(출하 시험) 결과 — SOP-MFG-001 §6 출하 판정 연계
- 라벨링·포장 확인 기록 — SOP-PKG-001 연계
- 출하 승인 서명

### 6.4 X-ray 고유 추적 항목

X-ray 의료기기 특성상 다음 항목에 대한 추가 추적성 확보:

| 구성품 | 추적 항목 | 근거 |
|--------|----------|------|
| X-ray 관(tube) | 시리얼, 제조일, 누적 조사량, 교체 이력 | IEC 60601-2-54, 방사선안전관리규칙 |
| 고전압 발생기 | 시리얼, 교정 일자, 출력 정확도 시험 기록 | IEC 60601-2-54 §203 |
| 디지털 디텍터 | 시리얼, 픽셀 결함 맵, 교정 데이터 버전 | 내부 품질 기준 |
| 콜리메이터 | 시리얼, 조사야 정확도 검증 기록 | IEC 60601-2-54 |
| SW/펌웨어 | 버전, 빌드 번호, SBOM | IEC 62304, SOP-SBOM-001 |
| AI 영상처리 모듈 | 모델 버전, 학습 데이터셋 ID | SOP-AIGOV-001 |

### 6.5 추적성 기간

| 시장 | 보관 기간 | 근거 |
|------|----------|------|
| 한국(MFDS) | 제조일로부터 10년 또는 유효기간+2년 중 긴 기간 | 의료기기법 시행규칙 |
| 미국(FDA) | 기기 수명 기간 중 FDA가 요구하는 기간 | 21 CFR 821 |
| 유럽(EU MDR) | 최종 기기 출시 후 최소 10년, 이식형은 15년 | EU MDR Article 10(8) |

## 7. 부적합품 식별 및 격리

- 부적합품은 SOP-NC-001에 따라 즉시 격리·식별
- 부적합 라벨(빨간색) 부착, 부적합 보고서에 로트/시리얼 기록
- 추적성 기록을 활용하여 동일 로트 내 잠재 부적합 범위 평가
- CAPA(SOP-CAPA-001) 연계 시 영향 범위 결정에 추적성 데이터 활용

## 8. UDI 데이터베이스 등록 및 유지

### 8.1 등록 절차

1. 발급기관(GS1 Korea 또는 HIBCC) 가입 및 Company Prefix 확보
2. Basic UDI-DI 생성 → EUDAMED 등록
3. UDI-DI(GTIN) 생성 → EUDAMED 및 FDA GUDID 등록
4. UDI-PI 규칙 정의(시리얼 번호 체계, 제조일 형식)
5. 라벨 인쇄 시스템에 UDI 바코드(GS1-128 또는 DataMatrix) 연동

### 8.2 UDI 데이터 갱신

- 모델 변경, 라벨 변경, 규제 상태 변경 시 UDI 데이터 갱신
- SOP-CC-001(변경통제)에서 UDI 영향 평가 포함
- 연 1회 이상 UDI 데이터 정확성 검증

## 9. 기록 및 양식

| 양식 ID | 양식명 | 용도 |
|---------|--------|------|
| F-TRC-001 | 제품 추적성 기록서 | DHR 내 구성품-완제품 매핑 기록 |
| F-TRC-002 | 입고 자재 식별·추적 대장 | 원자재 입고 시 식별 및 로트 매핑 |

## 10. 관련 문서

| 문서 ID | 문서명 | 연관 |
|---------|--------|------|
| SOP-MFG-001 | 제조공정관리 절차 | 공정 중 DHR 작성 연계 |
| SOP-PKG-001 | 라벨링·포장관리 절차 | UDI 라벨 부착 |
| SOP-UDI-001 | UDI 통합관리 절차 | UDI 체계 상세 |
| SOP-NC-001 | 부적합제품 관리 절차 | 부적합품 격리·추적 |
| SOP-FSCA-001 | 현장안전시정조치 절차 | 리콜 시 추적성 활용 |
| SOP-SBOM-001 | SBOM 생성관리 절차 | SW 추적성 |
| SOP-CC-001 | 변경통제 절차 | 변경 시 UDI·추적성 영향 평가 |
| SOP-PMS-001 | 불만처리·부작용보고 절차 | 시판후 추적 연계 |

## 11. 개정 이력

| 버전 | 일자 | 변경 내용 | 작성자 |
|------|------|----------|--------|
| v0.1 | 2026-05-21 | 초안 작성 | QA/RA Lead |

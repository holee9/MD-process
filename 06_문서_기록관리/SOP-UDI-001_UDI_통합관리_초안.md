---
doc-id: SOP-UDI-001
title: SOP-UDI-001 UDI 통합 관리 절차 (v0.2)
type: SOP
version: v0.2
status: draft
category: 06_문서_기록관리
purpose: SOP-UDI-001 UDI 통합 관리 절차 (v0.2) 관련 문서
applicable: [EU MDR 2017/745, EU MDR GSPR, EU MDR PRRC, FDA QMSR, MFDS, UDI]
forms: [F-UDI-001, F-UDI-002]
related-issues: [57]
owner: TBD
last-review: 2026-05-04
review-due: 2027-05-04
---

# SOP-UDI-001 UDI 통합 관리 절차 (v0.2)

> v0.2 — 2026-05-05: 절차 흐름도 추가, F-UDI-001/002 양식 추가, DI 재발급 판정 기준 상세화, X-ray 시스템 적용예시 보강

## 1. 목적
본 SOP는 의료용 X-ray system / detector / SW 에 대해 미국 FDA(21 CFR Part 830, QMSR §820.35(b)), 유럽 EU MDR Art. 27–28(및 Annex VI), 한국 의료기기법 시행규칙 별표2의2·UDI 고시 요구를 통합 준수하기 위한 UDI (Unique Device Identification) 부여·등록·유지·변경관리 방식을 정의한다.

## 2. 적용 범위
- 제품: 의료용 X-ray 고정형/이동형 시스템, 디지털 Detector, 관련 Workstation/SW (Class II 이상)
- 대상 라이프사이클: 설계 기준고정 이후 시판 전 등록부터 단종·리콜까지
- 관련 부서: RA(등록), 설계개발, 제조, 품질, 서비스, IT

## 3. 용어 정의
- UDI-DI: Device Identifier (정적, 모델/포장단위별 고정)
- UDI-PI: Production Identifier (동적; LOT, S/N, 제조일, 유효기간, SW version 등)
- GUDID: FDA Global UDI Database
- EUDAMED UDI module: EU UDI 데이터베이스
- Basic UDI-DI: EU MDR에서 규제 분류 단위로 부여 (DoC·기술문서 매핑 키)
- UDR (UDI Data Record): 사내 통합 UDI 마스터 레코드
- ASL: Approved Supplier List (UDI 발급 기관 포함)

## 4. 역할 및 책임 (RACI)
| 활동 | RA | 품질 | 설계 | 제조 | IT |
|------|----|------|------|------|----|
| UDI-DI/Basic UDI-DI 결정 | R | C | C | I | I |
| GUDID / EUDAMED / 국내 UDI 제출 | R | A | I | I | C |
| 제조번호/LOT·S/N 부여 규칙 운영 | C | A | I | R | C |
| UDI 라벨 인쇄·검증 | I | A | I | R | C |
| UDR 마스터 유지 | A | C | C | C | R |
| 변경 시 DI 재발급 판정 | A | C | R | I | I |
| 리콜 시 UDI 기반 추적 | C | R | I | C | C |

## 5. 절차 흐름도

```
┌──────────────────────────────────────────────────────────┐
│               UDI 통합 관리 절차 흐름                       │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  [1] 신규 모델/구성 확정 (설계 기준고정)                    │
│       ├─ 입력: 설계출력 문서, 포장단위 정의                  │
│       └─ 판정: 기존 DI 재사용 가능? → YES → [4]            │
│              │ NO                                        │
│              ▼                                           │
│  [2] UDI-DI 발급                                         │
│       ├─ GS1 GTIN 또는 HIBCC LIC 신청                    │
│       ├─ Basic UDI-DI 결정 (EU MDR)                      │
│       ├─ Primary DI (FDA) 확정                            │
│       └─ 국내 UDI 코드 확정                                │
│              │                                           │
│              ▼                                           │
│  [3] UDR 마스터 등록                                      │
│       ├─ 사내 UDR DB에 DI·제품정보·분류 입력                │
│       ├─ DoC/기술문서/510(k) 교차참조 연결                  │
│       └─ 출력: UDR 등록 완료 확인서                         │
│              │                                           │
│              ▼                                           │
│  [4] 규제 데이터베이스 등록                                 │
│       ├─ GUDID 제출 (FDA)                                 │
│       ├─ EUDAMED Actor→Device 등록 (EU)                   │
│       ├─ MFDS UDI 시스템 등록 (국내)                       │
│       └─ 판정: 등록 접수 확인 → 불합격 시 보완 후 재제출     │
│              │                                           │
│              ▼                                           │
│  [5] 라벨 설계·검증                                       │
│       ├─ UDI-DI + PI 위치·크기·인코딩 설계                  │
│       ├─ 바코드/2D 판독 시험 (F-UDI-002)                   │
│       ├─ IEC/ISO 15223-1 기호 정합 확인                    │
│       └─ 판정: 판독률 ≥99.5% → 합격                       │
│              │                                           │
│              ▼                                           │
│  [6] PI(Production Identifier) 운영                       │
│       ├─ LOT/S/N 부여 (제조 시점)                          │
│       ├─ SW 버전 PI 반영 (Minor 이상 변경 시)               │
│       └─ 제조일·유효기간 AI(11)/AI(17) 적용                 │
│              │                                           │
│              ▼                                           │
│  [7] 변경 발생 시 — DI 재발급 판정 (F-UDI-001)              │
│       ├─ 변경 유형별 판정 트리 적용                          │
│       ├─ DI 재발급 필요 → [2]로 회귀                        │
│       └─ PI만 변경 → [6]에서 처리                           │
│              │                                           │
│              ▼                                           │
│  [8] 리콜·판매중지 시                                      │
│       ├─ UDI 기반 대상 LOT/S/N 추적                        │
│       ├─ FSN/FSCA에 UDI 명시                              │
│       └─ GUDID/EUDAMED/MFDS 상태 갱신                    │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

## 6. 프로세스 상세

### 6.1 신규 모델 UDI 발급
1. 제품 모델/구성·포장 단위 확정 → UDI 발급 기관(GS1 등) 선정
2. Basic UDI-DI (EU) / Primary DI (FDA) / 국내 UDI 동시 결정, UDR에 등재
3. DoC(EU), 기술문서, 510(k)/PMA(해당 시) 문서와 UDI 교차 참조
4. EUDAMED Actor→Device 등록, GUDID 제출, MFDS UDI 시스템 등록
5. 라벨/IFU/포장·기기 표시(AI/DI+PI) 설계·검증 (IEC/ISO 15223-1 정합)

### 6.2 PI(Production Identifier) 운영
- LOT·S/N 부여 규칙: 모델코드 + 연월 + 일련번호, 재사용 금지
- SW 버전: Major.Minor.Patch + Build; Minor 이상 변경 시 PI 반영
- 유효기간/제조일: 해당 시 AI(11), AI(17)

### 6.3 X-ray 시스템 UDI 적용 예시

| 구성품 | UDI-DI 단위 | PI 항목 | 비고 |
|--------|------------|---------|------|
| X-ray 본체 (고정형) | GTIN per 모델/구성 | S/N, 제조일, SW ver | 주기기 DI |
| X-ray 본체 (이동형) | GTIN per 모델/구성 | S/N, 제조일, SW ver | 별도 DI |
| 디지털 Detector | GTIN per 모델/사이즈 | S/N, 제조일, FW ver | 액세서리 DI |
| Workstation SW (SaMD) | GTIN per SW 제품명 | SW ver (Major.Minor.Patch) | SaMD UDI-DI |
| 콜리메이터 | 본체 DI에 포함 또는 별도 | S/N | 분류에 따라 결정 |
| HV Generator | 본체 DI에 포함 | S/N, 교정일 | 통합 구성품 |

**SaMD UDI 특수 요건:**
- FDA: SaMD는 물리적 라벨 없이 "About" 화면 또는 Splash 스크린에 UDI 표시 가능
- EU MDR MDCG 2019-4: SW Major 버전 변경 시 새 UDI-DI, Minor 변경은 PI만 갱신
- 국내: SaMD UDI 표시는 소프트웨어 내 화면 표시 허용 (MFDS UDI 고시)

### 6.4 변경 관리 — DI 재발급 판정 트리

| 변경 사유 | DI 재발급 | 근거 | 판정 기준 상세 |
|-----------|-----------|------|---------------|
| 의도된 용도 변경 | YES | 21 CFR 830.50, MDCG 2018-1 | Intended Use/Indications 문구 변경 시 |
| 포장/수량 변경 | YES | 〃 | 포장 단위·수량이 UDI-DI 단위와 불일치 시 |
| 멸균 방식 변경 | YES | 〃 | 멸균→비멸균 또는 방식 변경 |
| 모델명/상호 변경 | YES | 〃 | 법적 제조자명·모델명 변경 |
| 중대한 SW 기능 변경 | YES (SaMD UDI-DI) | MDCG 2019-4, FDA Guidance 2022 | 알고리즘 변경, 새 기능 추가, 표시단위 변경 |
| 마이너 버그 수정·성능 개선 | NO (PI만) | 〃 | SW version PI만 갱신 |
| 비의도성 표시 개선 | NO | 〃 | 라벨 디자인만 변경, DI 불변 |
| Detector 모델 교체 (호환) | 판정 필요 | F-UDI-001 | 기능·성능 동등 시 NO, 상이 시 YES |

### 6.5 리콜·판매중지 시
- UDI 기반 대상 Lot/S/N 식별 → 21 CFR 806 / 의료기기법 §31 / EU MDR Art. 87 보고
- FSN/FSCA에 UDI 명시
- UDR 상태 "Withdrawn/Recalled" 기록, GUDID/EUDAMED 상태 갱신

### 6.6 기록
- UDR 마스터 (버전 이력 포함)
- 라벨 검증 기록(판독률, 오류율)
- GUDID/EUDAMED/MFDS 제출·수정 이력
- DI 재발급 결정 기록지 (F-UDI-001, 판정 트리 적용 근거)

## 7. 양식: F-UDI-001 DI 재발급 판정 기록서

### 7.1 변경 정보

| 항목 | 내용 |
|------|------|
| 변경요청 번호 (CCR No.) | |
| 제품명/모델명 | |
| 현행 UDI-DI | |
| 변경 사유 | |
| 변경 상세 내용 | |
| 변경 분류 | □의도된 용도 □포장/수량 □멸균 □모델명/상호 □SW 기능 □기타 |

### 7.2 판정

| 판정 항목 | 결과 |
|-----------|------|
| DI 재발급 필요 여부 | □YES → 신규 DI 발급 절차 진행 □NO → PI만 갱신 |
| 판정 근거 (규정 조항) | |
| Basic UDI-DI 변경 필요 여부 (EU) | □YES □NO □해당없음 |
| GUDID 업데이트 필요 | □YES □NO |
| EUDAMED 업데이트 필요 | □YES □NO □해당없음 |
| MFDS UDI 업데이트 필요 | □YES □NO |

### 7.3 승인

| 구분 | 성명 | 서명 | 일자 |
|------|------|------|------|
| 작성자 (RA) | | | |
| 검토자 (품질) | | | |
| 승인자 (PRRC/QMR) | | | |

## 8. 양식: F-UDI-002 UDI 라벨 검증 기록서

### 8.1 검증 대상

| 항목 | 내용 |
|------|------|
| 제품명/모델명 | |
| UDI-DI | |
| 라벨 유형 | □본체 라벨 □포장 라벨 □SW 화면 |
| 인코딩 방식 | □GS1-128 □GS1 DataMatrix □HIBCC □기타 |
| 검증일 | |
| 검증자 | |

### 8.2 검증 항목

| No. | 검증 항목 | 판정 기준 | 결과 | Pass/Fail |
|-----|-----------|-----------|------|-----------|
| 1 | DI 값 정확성 | UDR 마스터와 일치 | | □ |
| 2 | PI 항목 완비 | S/N, LOT, 제조일, SW ver 등 해당 항목 포함 | | □ |
| 3 | 바코드/2D 판독률 | ≥99.5% (100회 스캔 기준) | ____% | □ |
| 4 | 인체 판독 가능성 | HRI(Human Readable Interpretation) 선명 | | □ |
| 5 | IEC/ISO 15223-1 기호 | 필수 기호 완비, 크기·색상 적합 | | □ |
| 6 | 내구성 (해당 시) | 세척·소독 100회 후 판독 가능 | | □ |
| 7 | SW UDI 표시 (SaMD) | About/Splash 화면에 UDI 표시 확인 | | □ |

### 8.3 판정

| 구분 | 내용 |
|------|------|
| 종합 판정 | □합격 □조건부합격 □불합격 |
| 부적합 시 조치사항 | |
| 검증자 서명/일자 | |
| 승인자 서명/일자 | |

## 9. 규제 참조
- FDA: 21 CFR Part 830, QMSR §820.35(b), FDA UDI Final Rule Preamble
- EU: Regulation 2017/745 Art. 27–28, Annex VI Part C, MDCG 2018-1 rev. 4, MDCG 2019-4
- KR: 의료기기법 시행규칙 별표2의2, MFDS UDI 고시 최신본
- 표준: ISO 15223-1:2021, ISO/IEC 15459 시리즈

## 10. 관련 문서

| 문서 | 연계 내용 |
|------|-----------|
| 06_문서/문서_기록관리_개요.md | 문서·기록 관리 체계, 보존 기한 |
| 02_QMS/SOP-CC-001 변경통제 절차 | 변경 시 DI 재발급 판정 연계 |
| 08_PMS/SOP-PMS-001 불만처리·부작용보고 | 리콜 시 UDI 기반 추적 |
| 09_공급자/공급자_관리_개요.md | UDI 연계 추적성 요건 |
| 00_프로젝트관리/JD-RA-001 | RA/PRRC 역할 — UDI 등록 책임 |
| 01_법규/04_유럽_MDR/GSPR_체크리스트_v0.2 | GSPR §23 UDI 요건 |

## 11. 개정 이력
| 버전 | 일자 | 내용 | 작성 |
|------|------|------|------|
| 0.1 | 2026-04-20 | 초안 작성 (FDA/EU/KR 통합 골격) | RA(자동화 세션) |
| 0.2 | 2026-05-05 | 절차 흐름도, F-UDI-001/002 양식, X-ray 적용예시, 판정기준 상세화 | holee9-automation |

## 출처
- 21 CFR Part 830 (UDI Rule)
- FDA QMSR §820.35(b) (2026-02-02 시행)
- EU MDR 2017/745 Art. 27–28, Annex VI
- MDCG 2018-1 rev. 4
- MDCG 2019-4 (UDI for SaMD)
- 의료기기법 시행규칙 별표2의2
- ISO 15223-1:2021
- 확인일: 2026-05-05

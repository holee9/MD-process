# 의료용 X-ray 장비 안전·성능 표준 매핑 (v0.1)

## 1. 목적
진단용 X-ray system / detector / 관련 SW의 국제·지역별 안전·성능 규제·표준을 단일 표로 정리하여
설계 입력(Design Input), 형식시험 항목, 기술문서(TD) 인덱스에 직접 활용 가능하도록 한다.

## 2. 적용 범위
- 진단용 X-ray system (투시·촬영·이동형·치과 제외 일반 진단)
- 디지털 Detector (flat panel detector)
- 영상처리·워크리스트 SW (구성품 또는 독립 SaMD 여부 구분)
- 부속 워크스테이션, PACS 연결 인터페이스(HW/SW)

## 3. 핵심 표준·규제 매핑표

| 영역 | 국제(IEC/ISO) | EU (Harmonized / SoTA) | FDA | 국내(MFDS/관련 부처) |
|------|----------------|------------------------|------|------------------------|
| 전기안전·기본 성능 공통 | IEC 60601-1:2005+A1:2012+A2:2020 | EN 60601-1:2006+A1:2013+A12:2014+A2:2021 (Harmonized) | FDA Recognized Consensus Standard DB 등재 | KS C IEC 60601-1 (식약처 공통기준규격) |
| 전자파 양립성(EMC) | IEC 60601-1-2:2014+A1:2020 (Ed.4.1) | EN 60601-1-2:2015+A1:2021 (Harmonized) | Recognized | KS C IEC 60601-1-2 |
| 방사선 방호 | IEC 60601-1-3:2008+A1:2013+A2:2021 | EN 60601-1-3:2008+A1:2013+A2:2021 (Harmonized) | Recognized | KS C IEC 60601-1-3 |
| 사용적합성 | IEC 62366-1:2015+A1:2020 | SoTA (OJEU 미등재) | Recognized (HFE Guidance 2016 병행) | 식약처 사용적합성 가이드라인(2017) |
| SW 수명주기 | IEC 62304:2006+A1:2015+A2:2020 | SoTA (OJEU 미등재, EN 62304:2006/A1:2015만 존재) | Recognized (부분) | 식약처 SW밸리데이션 가이드라인 |
| SW 보안(Product) | IEC 81001-5-1:2021 | SoTA (OJEU 미등재) | FDA Premarket Cybersecurity Guidance(2023-09) 참조 | 식약처 사이버보안 허가·심사 가이드라인(2022 개정) |
| 진단 X-ray 개별 규격 | IEC 60601-2-54:2009+A1:2015+A2:2018 (촬영·투시) | EN 60601-2-54:2009+A1:2015+A2:2019 (Harmonized) | Recognized | KS C IEC 60601-2-54 |
| 디지털 Detector 성능 | IEC 62220-1-1:2015 (DQE 측정) | SoTA | Recognized | KS C IEC 62220-1-1 |
| 사용자 방호·선량(DAP/AED) | IEC 60580:2019 (DAP meter) | SoTA | — | KS C IEC 60580 |
| 성능시험·선량표시 FDA 규제 | — | — | **21 CFR Part 1020 §1020.30/31** (Performance Standards for Diagnostic X-ray Systems, MQSA 제외) | — |
| 위험관리 | ISO 14971:2019 + ISO/TR 24971:2020 | EN ISO 14971:2019/A11:2021 (Harmonized) | Recognized | KS P ISO 14971 |
| 품질시스템 | ISO 13485:2016 | EN ISO 13485:2016 (Harmonized) | QMSR(21 CFR 820) 편입(2026-02-02) | 의료기기 제조 및 품질관리 기준 (고시 2025-22호 개정 예정) |

## 4. 규제별 필수 시험·보고 항목

### 4.1 EU MDR
- GSPR Annex I §14 (진단기기), §16.2 (방사선), §17 (전자 프로그래머블 시스템)
- Annex II TD: 안전·성능 기준(GSPR) 체크리스트에 상기 표의 Harmonized/SoTA 근거 명시
- Annex III PMS: 선량 관련 사용자 피드백·클레임 전용 코드 분류
- NB 심사 시 60601-2-54 형식시험 보고서, 62304 SW 수명주기 기록, 81001-5-1 사이버보안 Capability 보고서 요구

### 4.2 FDA
- 510(k) 또는 De Novo 제출 시 Recognized Consensus Standards Declaration of Conformity
- **21 CFR 1020.30/31 Radiation Performance Standards** 준수 보고(Abbreviated Reports 또는 Product Report)
- Premarket Cybersecurity Documentation (2023-09 Guidance):
  - SBOM, Threat Model, Security Architecture, Vulnerability Management Plan, Cybersecurity Testing
- 21 CFR 803 MDR, QMSR § 820.35(a) 불만·서비스 기록
- 21 CFR 830 UDI (QMSR § 820.35(b))

### 4.3 MFDS (국내)
- 의료기기법 제19조 허가·인증
- 「의료기기의 전기·기계적 안전에 관한 공통기준규격」 및 「방사선 안전관리 기준규격」
- 「진단용 방사선 발생장치의 안전관리에 관한 규칙」(보건복지부령) — 설치·검사 의무(3년 정기)
- 국가암검진 등 사용처는 건강보험심사평가원 장비 품질관리 검사(한국의료영상품질관리원, KIAQC) 정기 검사 별도
- 고시 2025-22호 개정 시 ISO 13485:2016 조항 직접 인용 예정(재확인 필요)

## 5. 설계 입력 체크포인트 (X-ray detector / system SW)
- 60601-1: 누설전류, PEMS Annex H, 필수 성능 선언
- 60601-1-2: EMC 4.1판 (Professional healthcare facility 환경 분류)
- 60601-1-3: **사용자·환자 선량 최소화 원리**, DAP/AED 표시, 자동 노출 제어(AEC)
- 60601-2-54: 선량 정확도 ±50%(진단용 투시·촬영) 허용오차 등 개별 규격
- 62220-1-1: Detector DQE 최소 성능 목표 설정
- 62366-1: 사용 시나리오·Use Error 분석 → Use Specification, UI Validation
- 62304: SW 안전성 클래스(본 프로젝트 AEC·노출제어·차폐 인터록 SW = Class C 확정)
- 14971: 방사선 과노출 시나리오, Interlock 실패, SW 결함, 사이버공격 → Hazard 목록

## 6. 형식시험 책임 분담(내부/공인시험소)
| 항목 | 내부 가능 | 공인시험소 필요 |
|------|-----------|------------------|
| 60601-1 전기안전 | 일부 사전시험 | 정식 시험성적서 (NRTL/MFDS 지정) |
| 60601-1-2 EMC | 사전 스크리닝 | 정식 |
| 60601-1-3 방사선방호 | 설계 검증 | 정식 |
| 60601-2-54 형식시험 | 불가 | 정식 |
| 62220-1-1 DQE | 가능(표준 Phantom) | 신뢰성 확보 시 내부 인정 가능 |
| 62304/81001-5-1 | 내부(SDLC 기록) | 불요 (TD 제출) |
| 62366-1 UE 평가 | 내부 + 실사용자 | 필요시 |

## 7. 오픈 이슈
1. 디지털의료제품법(2025-01-24 시행) SaMD/AI 영상처리 SW 요구 추가 확인 필요
2. FDA Part 1020 Abbreviated Reports ↔ QMSR 기록 항목 중복 최소화 방안
3. IEC 60601-1 Ed.4 초안 반영 시점 트래킹 (2027 전후 예상)
4. EN 60601-1-3 Harmonized 지위 OJEU 공식 게재일 재확인
5. 국내 진단용 방사선 발생장치 안전관리 규칙 2024 개정 여부 재확인

## 8. 연계 문서
- 03_설계_개발관리/설계개발_프로세스.md
- 03_설계_개발관리/IEC_62304_SW_수명주기.md
- 03_설계_개발관리/IEC_81001-5-1_FDA_Cybersecurity_SW보안.md (신규 2026-04-21)
- 07_위험관리_ISO14971/ISO14971_프로세스_상세.md
- 01_법규_규제/04_유럽_MDR/GSPR_정합표준_매핑표.md
- 01_법규_규제/03_미국_FDA/FDA_QMSR_2026.md

## 8. 영상품질 QC 프로토콜 매핑 (v0.1)

### 8.1 목적
진단용 방사선 발생장치 안전관리규칙(제1122호) 검사항목과 IEC/국제 표준의 영상품질 시험 프로토콜을 매핑하여, 출하 QC·정기검사·PMS 환류에 일관된 기준을 제공한다.

### 8.2 영상품질 검사 항목 매핑

| 검사 항목 | 규칙 제1122호 근거 | IEC/국제 표준 | 시험 방법·판정 기준 | 출하 QC 반영 |
|-----------|-------------------|--------------|-------------------|-------------|
| 공간 해상도(Spatial Resolution) | 별표 검사항목 — 해상력 | IEC 62220-1-1 §5.4 (MTF) | Line-pair phantom 또는 디지털 MTF 분석, ≥2.0 lp/mm @ 10% MTF (DR) | 출하 시 MTF 측정 기록 |
| 저대비 해상도(Low Contrast) | 별표 검사항목 — 저대비 해상력 | IEC 61223-3-2 (수용시험), AAPM TG-150 | 저대비 디테일 팬텀(Leeds TO.20 등), 가시 구멍 수 기준 | 출하 시 팬텀 촬영 기록 |
| 균일성(Uniformity) | 별표 — 감도 균일성 | IEC 62220-1-1 §5.6 (NNPS), AAPM TG-150 §6.3 | 균일 노출 → ROI 분석, 편차 ≤15% (제조사 내부 기준) | 출하 시 Flood-field 촬영 |
| 잡음 특성(Noise/NPS) | — | IEC 62220-1-1 §5.5 (NPS), AAPM TG-150 | Noise Power Spectrum 분석, DQE 산출 연동 | DQE 시험과 통합 |
| DQE(Detective Quantum Efficiency) | — | IEC 62220-1-1:2015 전체 | RQA5 빔조건, DQE(0) ≥ 제조사 목표값 | 형식시험 1회 + 출하 샘플링 |
| 잔상(Ghosting/Lag) | 별표 — 잔상 | IEC 62220-1-1 §5.7 | 고노출 후 무노출 프레임 비율, ≤1% (DR) | 출하 시 잔상 시험 |
| AEC 정확도(Auto Exposure Control) | 별표 — 자동노출제어 | IEC 60601-2-54 §203.7.8 | ±25% 선량 변동 이내 (피사체 두께 변화 시) | 출하 교정 기록 |
| 관전압 정확도(kVp Accuracy) | 제5조 검사항목 | IEC 60601-2-54 §201.12.1 | ±10% 이내 (비침습 kVp 미터) | 출하 교정 기록 |
| 반가층(HVL) | 제5조 검사항목 | IEC 60601-1-3 §7 | Al 추가 필터법, 관전압별 최소 HVL 표 충족 | 형식시험 기록 |
| 선량 재현성(Dose Reproducibility) | 제5조 검사항목 | IEC 60601-2-54 §203.6.4 | 변동계수(CoV) ≤ 0.05 (5%) | 출하 시 5회 반복 측정 |
| DAP 정확도(Dose Area Product) | 별표 — 선량표시 | IEC 60580:2019 §5 | 기준선량계 대비 ±25% 이내 | 출하 교정 기록 |

### 8.3 QC 프로토콜 단계

| 단계 | 시점 | 주체 | 적용 항목 |
|------|------|------|-----------|
| 형식시험(Type Test) | 설계 완료 후 1회 | 공인시험소 | DQE, MTF, NPS, HVL, 누설선량 전항목 |
| 출하시험(Release Test) | 매 출하 | 제조사 QC | 관전압, AEC, DAP, 해상도, 균일성, 잔상, 선량재현성 |
| 설치검사(Acceptance Test) | 설치 후 | 제조사+사용자 | 규칙 별표 전항목 + 환경 요인(전원, 접지) |
| 정기검사(Periodic Test) | 3년 주기 | 지정검사기관 | 규칙 제5조 항목 전체 |
| 일상 QC(Routine QC) | 일/주/월 | 사용자(방사선사) | 균일성(일), AEC확인(주), 해상도 팬텀(월) |

### 8.4 판정 기준 출처 정리
- AAPM TG-150: Performance Evaluation of Digital Radiography Systems (2024)
- KFDA/KIAQC 정기검사 매뉴얼 (한국의료영상품질관리원)
- IEC 61223-3-2: Acceptance and Constancy Tests — Imaging Performance of X-ray Equipment for Radiographic and Radioscopic Systems
- ACR-AAPM-SIIM Technical Standard for Electronic Practice of Medical Imaging

### 8.5 PMS 환류
- 정기검사 부적합 데이터 → `08_시판후_감시_PMS/PMS_개요.md` §3 데이터원천에 반영
- 현장 영상품질 클레임 코드: IQ-001(해상도), IQ-002(균일성), IQ-003(잔상), IQ-004(AEC) 분류
- CAPA 트리거: 동일 코드 3건/분기 발생 시 경향분석 착수

### 8.6 오픈 이슈
1. KIAQC 정기검사 매뉴얼 최신판(2025) 입수 후 판정기준 수치 교차확인 필요
2. 투시(Fluoroscopy) 모드 별도 QC 항목 추가 여부 검토

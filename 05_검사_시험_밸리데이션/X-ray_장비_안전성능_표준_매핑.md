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

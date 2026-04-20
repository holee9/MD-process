# SOP-UDI-001 UDI 통합 관리 절차 (v0.1 초안)

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

## 4. 역할 및 책임 (RACI 개요)
| 활동 | RA | 품질 | 설계 | 제조 | IT |
|------|----|------|------|------|----|
| UDI-DI/Basic UDI-DI 결정 | R | C | C | I | I |
| GUDID / EUDAMED / 국내 UDI 제출 | R | A | I | I | C |
| 제조번호/LOT·S/N 부여 규칙 운영 | C | A | I | R | C |
| UDI 라벨 인쇄·검증 | I | A | I | R | C |
| UDR 마스터 유지 | A | C | C | C | R |
| 변경 시 DI 재발급 판정 | A | C | R | I | I |

## 5. 프로세스
### 5.1 신규 모델 UDI 발급
1. 제품 모델/구성·포장 단위 확정 → UDI 발급 기관(GS1 등) 선정
2. Basic UDI-DI (EU) / Primary DI (FDA) / 국내 UDI 동시 결정, UDR에 등재
3. DoC(EU), 기술문서, 510(k)/PMA(해당 시) 문서와 UDI 교차 참조
4. EUDAMED Actor→Device 등록, GUDID 제출, MFDS UDI 시스템 등록
5. 라벨/IFU/포장·기기 표시(AI/DI+PI) 설계·검증 (IEC/ISO 15223-1 정합)

### 5.2 PI(Production Identifier) 운영
- LOT·S/N 부여 규칙: 모델코드 + 연월 + 일련번호, 재사용 금지
- SW 버전: Major.Minor.Patch + Build; Minor 이상 변경 시 PI 반영
- 유효기간/제조일: 해당 시 AI(11), AI(17)

### 5.3 변경 관리 — DI 재발급 판정 트리
| 변경 사유 | DI 재발급 | 근거 |
|-----------|-----------|------|
| 의도된 용도 변경 | YES | 21 CFR 830.50, MDCG 2018-1 |
| 포장/수량 변경 | YES | 〃 |
| 멸균 방식 변경 | YES | 〃 |
| 모델명/상호 변경 | YES | 〃 |
| 중대한 SW 기능 변경 (알고리즘/표시단위 등) | YES (SaMD UDI-DI) | MDCG 2019-4, FDA Guidance 2022 |
| 마이너 버그 수정·성능 개선 | NO (PI만) | 〃 |
| 비의도성 표시 개선 | NO | 〃 |

### 5.4 리콜·판매중지 시
- UDI 기반 대상 Lot/S/N 식별 → 21 CFR 806 / 의료기기법 §31 / EU MDR Art. 87 보고
- FSN/FSCA에 UDI 명시
- UDR 상태 "Withdrawn/Recalled" 기록, GUDID/EUDAMED 상태 갱신

### 5.5 기록
- UDR 마스터 (버전 이력 포함)
- 라벨 검증 기록(판독률, 오류율)
- GUDID/EUDAMED/MFDS 제출·수정 이력
- DI 재발급 결정 기록지 (판정 트리 적용 근거)

## 6. 규제 참조
- FDA: 21 CFR Part 830, QMSR §820.35(b), FDA UDI Final Rule Preamble
- EU: Regulation 2017/745 Art. 27–28, Annex VI Part C, MDCG 2018-1, MDCG 2019-4
- KR: 의료기기법 시행규칙 별표2의2, MFDS UDI 고시 최신본
- 표준: ISO 15223-1:2021, ISO/IEC 15459 시리즈

## 7. 관련 문서
- SOP-DOC-001 문서·기록관리
- SOP-PMS-002 불만·MDR
- QM-GSPR-CHK-001 GSPR 체크리스트
- JD-RA-001 RA/PRRC 통합 직무기술서

## 8. 개정 이력
| 버전 | 일자 | 내용 | 작성 |
|------|------|------|------|
| 0.1 | 2026-04-20 | 초안 작성 (FDA/EU/KR 통합 골격) | RA(자동화 세션) |

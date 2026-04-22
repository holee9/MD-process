# SOP-SBOM-001 — SBOM 생성·관리 절차 (v0.1 초안)

문서번호: SOP-SBOM-001
버전: v0.1 (초안)
작성일: 2026-04-22
작성자: 의료기기 업무규칙 개발팀

## 1. 목적
의료용 X-ray 시스템/검출기/소프트웨어 제품에 탑재·사용되는 모든 소프트웨어 구성요소를 식별·추적하여
FDA Section 524B, MDCG 2019-16, MFDS 의료기기 사이버보안 허가·심사 가이드라인(2025-01-10), 디지털의료기기
전자적 침해행위 보안 지침(제16조)에 부합하는 SBOM을 생성·유지·관리한다.

## 2. 적용 범위
- 펌웨어(Detector, Generator, Workstation 등)
- OS 및 3rd-party 미들웨어(FreeRTOS, Yocto Linux, Qt, DICOM Toolkit 등)
- 영상처리/재구성 SW, AI 추론 모델 및 런타임(ONNX, TensorRT 등)
- 오픈소스 및 상용 라이선스 소프트웨어 전체

## 3. 용어 정의
- SBOM: Software Bill of Materials
- VEX: Vulnerability Exploitability eXchange
- VDR: Vulnerability Disclosure Report
- NTIA Baseline: 미 상무성 NTIA 최소 필수 요소 7종
- CPE/PURL: Common Platform Enumeration / Package URL

## 4. 책임·권한
| 역할 | 책임 |
|------|------|
| 제품 책임자(PM) | SBOM 산출물 범위 최종 승인 |
| SW Engineer | 빌드 파이프라인에서 SBOM 자동 생성, 품질 검증 |
| Security Officer | SBOM→취약점 매핑, VEX 결정, VDR 배포 |
| QA | SBOM·VEX·VDR 기록 DHF 편입, ISO 13485 4.2.4 관리 |
| RA | FDA/MDR/MFDS 제출물에 SBOM·VEX 포함 확인 |

## 5. 포맷 및 필수 메타데이터
- **포맷**: SPDX 2.3 또는 CycloneDX 1.5 (NTIA 최소필수 요소 7종 충족)
- **최소 필드**: Supplier, Component Name, Version, Unique Identifier(PURL/CPE), Dependency Relationship, Author, Timestamp
- **확장 필드(권장)**: License, Hash(SHA-256), Origin URL, Build Environment, Support Status, EOL Date

## 6. 생성 절차
### 6.1 빌드 파이프라인 통합
1. 소스 빌드 시 SBOM 자동 생성 툴 호출(예: Syft, CycloneDX CLI, SPDX Tools, Black Duck, Snyk SBOM)
2. 빌드 산출물과 함께 SBOM 파일을 아티팩트 저장소에 함께 저장(파일명 규칙: `<product>_<version>_<YYYYMMDD>.cdx.json`)
3. 서명(SHA-256 Hash + GPG/Sigstore)으로 무결성 확보

### 6.2 수작업 보완
- 빌드에서 포착되지 않는 펌웨어 블롭, Binary-only 라이브러리는 수작업 항목 추가
- 추가 항목은 `components[].evidence.analysis = "manual"` 플래그 기록

### 6.3 검증
- NTIA Baseline 체크리스트 통과
- 누락 필드·버전 불일치 자동 린터 통과
- 빌드 ID와 1:1 대응되는지 QA 샘플링 검증

## 7. 유지·갱신 주기
- 모든 SW 릴리즈(메이저/마이너/패치)마다 SBOM 재생성
- SBOM은 Living Document — 릴리즈 노트와 함께 PLM 시스템에 등록
- 시판 후 취약점 발견·패치 반영 시 SBOM·VEX 동시 갱신

## 8. 취약점 매핑(VEX 포함)
1. SBOM 컴포넌트 PURL/CPE를 NVD/OSV/CISA KEV와 매핑
2. CVSS v3.1 + Medical Rubric(IMDRF/CYBER/N60) 반영하여 위험도 재평가
3. VEX 결정 상태 4종 기록: `not_affected | affected | fixed | under_investigation`
4. VEX는 OpenVEX 또는 CycloneDX VEX 포맷으로 SBOM과 함께 배포

## 9. 제출 및 배포
### 9.1 FDA
- Premarket Submission에 SBOM·VEX·VDR 포함 (2025-10-01 이후 필수)
- Postmarket: Section 524B에 따라 업데이트·배포 계획서 유지

### 9.2 EU MDR / NB
- Technical Documentation(Annex II) Cybersecurity Annex에 SBOM 첨부
- MDCG 2019-16 및 IMDRF N73 원칙 준수

### 9.3 MFDS
- 사이버보안 허가·심사 가이드라인의 RA-07(SBOM), RA-08(취약점 관리) 대응
- 디지털의료제품법 보안 지침 제16조 SBOM 관리 활동 권고 준수

### 9.4 고객/운영자 배포
- VDR 또는 Customer Security Advisory 형태로 배포
- 운영자는 SBOM 열람을 통해 자산 관리·취약점 대응

## 10. 기록·이력 관리
- SBOM, VEX, VDR 모두 DHF 및 DMR에 편입 (ISO 13485 4.2.4 / 4.2.5)
- 보존 기간: 제품 수명 + 10년(MDR) / 제품 수명 + 2년(QMSR)
- 변경 시 SOP-CC-001 Change Control 연동 판정

## 11. 참조
- FDA "Cybersecurity in Medical Devices" Final Guidance (2023-09; 2025-06-27 개정 Section VII 추가)
- IMDRF/CYBER WG/N73FINAL:2023 SBOM Principles and Practices
- MDCG 2019-16 Rev.1 / MDCG 2021-5
- MFDS 의료기기 사이버보안 허가·심사 가이드라인(2025-01-10)
- 디지털의료기기 전자적 침해행위 보안 지침(안) 제16조
- NTIA "The Minimum Elements For a Software Bill of Materials" (2021-07)
- ISO/IEC 5962:2021 (SPDX), ISO/IEC 13335
- IEC 81001-5-1:2021 §4.SM, §7.SR, §8.PM

## 12. 개정 이력
| 버전 | 일자 | 작성자 | 비고 |
|------|------|--------|------|
| v0.1 | 2026-04-22 | 업무규칙 개발팀 | 초안 작성 |

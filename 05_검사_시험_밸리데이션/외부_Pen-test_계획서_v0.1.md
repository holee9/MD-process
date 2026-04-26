# 외부 침투시험(Penetration Test) 계획서 (v0.1 초안)

문서번호: PLAN-PEN-001
버전: v0.1 (초안)
작성일: 2026-04-26
작성자: 의료기기 업무규칙 개발팀
관련 문서: 02_QMS/SOP-CVD-001_조정된_취약점_공개_정책.md, 03_설계_개발관리/IEC_81001-5-1_FDA_Cybersecurity_SW보안.md, 03_설계_개발관리/SOP-SBOM-001_SBOM_생성관리_절차.md, 06_문서_기록관리/SOP-UDI-001_UDI_통합관리_초안.md, 12_교차검증_보고서/2026-04-24_FDA_SBOM_제출물_사전점검.md

## 1. 목적
의료용 X-ray 시스템(콘솔·검출기·서버·클라우드 연계 SW)에 대한 외부 보안 침투시험을 발주·수행·결과보고 하기 위한 계획을 수립한다.

본 계획은 FDA Premarket Cybersecurity Guidance(2023-09-26) §V.D, §VI.D 의 "security testing" 의무 및
MFDS 의료기기 사이버보안 허가·심사 가이드라인(2025-01-10) 제6장의 시험요구를 충족하는 외부 검증 산출물을 확보한다.

## 2. 규제·표준 근거
- FD&C Act §524B(b)(1)(B): "design, develop, and maintain ... reasonable assurance that the device and related systems are cybersecure"
- FDA Premarket Cybersecurity Guidance(2023-09-26) §V.D Vulnerability Testing, §VI.D Penetration Testing
- MFDS "의료기기 사이버보안 허가·심사 가이드라인"(2025-01-10) 제6장 시험요구
- 디지털의료기기 전자적 침해행위 보안지침 제15조 (취약점 점검)
- AAMI TIR57:2016 (Principles for medical device security – Risk management)
- IEC 81001-5-1:2021 §7.4 (Security testing)
- IEC TR 60601-4-5:2021 (Security capabilities for medical electrical equipment)
- NIST SP 800-115 (Technical Guide to Information Security Testing and Assessment)
- OWASP WSTG v4.2 / OWASP MASTG v1.7 / OWASP IoT Security Verification Standard

## 3. 적용 범위 (Scope)
| 자산 | 위협 표면 | 시험 범위 |
|------|----------|----------|
| X-ray 콘솔 SW(Workstation) | 로컬·네트워크 | OS hardening, 인증·세션·권한, USB·미디어, 입력 검증 |
| 검출기 펌웨어 | 무선/유선 통신 | 펌웨어 무결성, OTA 업데이트, 통신암호화 |
| DICOM/HL7 인터페이스 | LAN | 프로토콜 fuzzing, AE-Title 위변조, TLS 검증 |
| 원격 서비스 모듈 | WAN/VPN | 인증, 세션관리, 명령주입, 권한상승 |
| 클라우드 백엔드(있을 시) | Public Internet | OWASP Top 10, API 인증·인가, 멀티테넌시 분리 |
| 모바일/웹 뷰어 | Mobile/Web | OWASP MASVS/ASVS L2 |

비범위(Out-of-Scope): 환자 임상 데이터 직접 추출(법적·윤리적 제약), 물리 침입(별도 평가)

## 4. 시험 방법론
### 4.1 단계
1. **사전 정보 수집** (1주) — SBOM(SOP-SBOM-001 산출물) · 아키텍처 · TM(STRIDE) 검토
2. **위협 모델링 검증** (1주) — 자체 STRIDE 결과와 외부 평가 격차 분석
3. **취약점 스캔** (1주) — 자동 도구(Nessus·Greenbone·OWASP ZAP 등) 1차
4. **수동 침투시험** (3주) — Black/Grey/White Box 혼합
5. **익스플로잇 검증** (1주) — Critical/High 항목 재현·영향분석
6. **보고서 초안 → 협의** (1주) — 임시 보고서 → 사내 검토 → 최종
7. **재시험(선택)** (2주, 별도 계약) — 패치 후 재현 시험

총 기간: 7주(주요 보고)+2주(재시험)

### 4.2 접근 모델
- Black Box: 외부자 관점 — 인증 정보 없이 시작
- Grey Box: 일반 사용자 권한 — 운영자 계정 발급
- White Box: 설계 정보 제공 — SBOM·아키텍처·소스 부분 검토

### 4.3 도구 및 표준 매핑
| 영역 | 표준/도구 |
|------|-----------|
| 네트워크 스캔 | Nmap, Nessus, Greenbone |
| 웹/API | OWASP ZAP, Burp Pro, Postman |
| DICOM Fuzzing | DICOM Fuzzer, Sulley/Boofuzz |
| 펌웨어 | Binwalk, Ghidra, Radare2, FACT |
| 모바일 | MobSF, Frida, Drozer, OWASP MASTG |
| 권한·코드 | Semgrep, OSS Review Toolkit |

## 5. 발주 요건 (RFP 핵심)
- 자격: ISO/IEC 27001 인증 보유 + ICS/Medical IoT 경험 ≥3년 + CREST/OSCP 보유 평가자
- 산출물 언어: 한·영 동시 또는 영문 + 국문 요약
- 비공개 계약(NDA), 결과 데이터 안전한 채널 전달, 시험 환경 격리
- CVE/CVSS v3.1 점수 부여, OWASP Risk Rating, FDA SPDF Cybersecurity Section 형식 부합
- VEX(JSON, OpenVEX 또는 CSAF 2.0) 산출물 함께 납품

## 6. 시험 환경
| 환경 | 용도 |
|------|------|
| 격리 시험실(LAB-SEC-01) | HW 콘솔·검출기 실물, 외부 인터넷 차단, 트래픽 캡처 가능 |
| Staging 클라우드(CL-STAGE) | 운영과 동등 구성, 익명 데이터만 |
| 가상 임상 데이터셋 | DICOM 익명 샘플(병원 협력 데이터셋, IRB 비대상) |

## 7. 결과 분류 및 SLA
| 등급 | CVSS v3.1 | 패치 SLA(SOP-CVD-001 §7) | 발견 시 즉시조치 |
|------|----------|----------------------|------------------|
| Critical | ≥9.0 | 30d | 임시 회피책 24h 내 전사 공유 |
| High | 7.0–8.9 | 60d | 위험 등급화 |
| Medium | 4.0–6.9 | 90d | 다음 정기 패치 포함 |
| Low | <4.0 | 180d | 변경관리 흐름 |

## 8. 산출물 (FDA·MFDS 제출용)
1. Penetration Test Plan (본 문서, v최종)
2. Threat Model Validation Report
3. Vulnerability Test Report (자동스캔 결과 통합)
4. Penetration Test Report — Findings · Reproduction · Remediation
5. VEX(SBOM-CVE 영향성 매트릭스, OpenVEX/CSAF)
6. Re-test Report(패치 후)
7. Executive Summary(영문, FDA SPDF Cyber Section 인용)

## 9. 책임·승인
| 역할 | 인원 | 책임 |
|------|------|------|
| Security Officer | 1 | 발주·총괄·결과 검토 |
| QA/RA | 2 | 규제 적합성·문서화·VEX 통합 |
| SW Architect | 1 | 시험 환경 구성·재현 검증 |
| Clinical Affairs | 1 | 임상 데이터 익명화 검증 |
| 외부 감사(선택) | 1 | 결과 독립 검토 |

## 10. 일정 (예시)
| 마일스톤 | 시점 |
|----------|------|
| RFP 발행·평가 | T0+1m |
| 계약 체결 | T0+2m |
| Kick-off | T0+2m |
| 시험 본 수행 | T0+3 ~ T0+4.5m |
| 보고서 최종 | T0+5m |
| 재시험(필요 시) | T0+5 ~ T0+6m |
| 510(k)/MFDS 제출 패키지 통합 | T0+6m |

## 11. 예산 추정 (참고)
- 외부 평가기관 발주: 8~15만 USD (범위·기간 따라 변동)
- 도구·인프라(자체 스캔 인프라 보강): 2만 USD
- 재시험: 본 계약의 30~50%

## 12. 변경관리 트리거
- 주요 SW 릴리스(IEC 81001-5-1 §6.5 의 변경 분류)·OS·미들웨어·OSS 컴포넌트 메이저 버전 업
- SBOM의 Critical CVE 발견(SOP-SBOM-001 §6 → SOP-CVD-001 §6 연계)
- 신규 시장(미국·EU·KR) 출시 또는 신규 인터페이스(클라우드, 모바일) 추가
- PMS(08) 또는 CVD(02_QMS) 흐름에서 사이버 침해사고 발생 시 즉시 재계획

## 13. 변경이력
| 버전 | 일자 | 작성자 | 내용 |
|------|------|--------|------|
| v0.1 | 2026-04-26 | 의료기기 업무규칙 개발팀 | 초안 작성 |

## 출처
- FDA Premarket Cybersecurity Guidance (2023-09-26)
- MFDS 의료기기 사이버보안 허가·심사 가이드라인 (2025-01-10)
- AAMI TIR57:2016, IEC 81001-5-1:2021, IEC TR 60601-4-5:2021
- NIST SP 800-115, OWASP WSTG/MASTG/IoTSVS
- 확인일: 2026-04-26

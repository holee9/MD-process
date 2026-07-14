---
doc-id: SOP-CVD-001
title: SOP-CVD-001 — Coordinated Vulnerability Disclosure 정책
type: SOP
version: v0.3.1
status: draft
category: 02_품질경영시스템_QMS
purpose: 보안 취약점의 조정된 공개·접수·처리·공시 절차를 수립하여 제품 사이버보안 유지
applicable: [IEC81001-5-1:2021, FDA Premarket Cybersecurity Guidance 2026-02-03, EU MDR 2017/745, ISO13485:2016, MFDS]
forms: [F-CVD-001]
related-docs: [SOP-SBOM-001, SOP-CC-001, SOP-CAPA-001]
related-issues: [19]
owner: TBD
last-review: 2026-07-10
review-due: 2027-05-21
---

# SOP-CVD-001 — Coordinated Vulnerability Disclosure 정책 (v0.1 초안)

문서번호: SOP-CVD-001
버전: v0.1 (초안)
작성일: 2026-04-25
작성자: 의료기기 업무규칙 개발팀
관련 문서: SOP-SBOM-001, SOP-CC-001, IEC_81001-5-1_FDA_Cybersecurity_SW보안.md

## 1. 목적
의료용 X-ray 시스템/검출기/SW 제품에서 발견되는 보안 취약점을 외부 신고자(보안 연구자, 사용자, 공급자)와
조정된 절차로 접수·평가·해결·공시하기 위한 정책을 수립한다.

본 정책은 다음 규제·표준 요구를 충족한다.
- FDA FD&C Act §524B(b)(1): "have a plan to monitor, identify, and address ... vulnerabilities and exploits" (CVD 포함)
- FDA Final Guidance "Cybersecurity in Medical Devices: Quality Management System Considerations and Content of Premarket Submissions" (February 2026, Docket FDA-2021-D-1158, supersedes 2025-06-27 및 2023-09-27 final): SBOM·VEX·CVD plan 제출 의무 (Attachment 1/2 신·구 판본 조항 대응표는 별도 확인 필요 — 미확인)
- MFDS 의료기기 사이버보안 허가·심사 가이드라인(2025-01-10) 제5장
- 디지털의료기기 전자적 침해행위 보안지침 제18조
- ISO/IEC 29147:2018 (Vulnerability Disclosure)
- ISO/IEC 30111:2019 (Vulnerability Handling Processes)
- IMDRF/CYBER WG/N60 (Principles and Practices for Medical Device Cybersecurity)

## 2. 적용 범위
- 시판 중인 모든 의료기기 SW(펌웨어, OS, 미들웨어, 응용 SW, AI 모델, 클라우드 서비스 포함)
- 출시 후 EoS(End of Support) 선언 전까지 전 기간
- 사외 공급자 컴포넌트(OSS, 상용 SW)에서 발견된 취약점도 포함

## 3. 용어 정의
| 용어 | 정의 |
|------|------|
| CVD | Coordinated Vulnerability Disclosure — 신고자·제조사·관계기관이 합의된 일정·범위 내에서 취약점을 처리·공시하는 절차 |
| Reporter | 취약점을 신고한 외부 또는 내부 주체 |
| Triage | 신고된 취약점의 진위·심각도·범위 1차 판정 |
| CVSS v4.0 | 취약점 심각도 정량 지표 |
| VEX | Vulnerability Exploitability eXchange — 취약점이 자사 제품에 실제로 미치는 영향 표명 |
| Embargo | 패치 배포 전까지 외부 비공개 유지 합의 기간 |
| Patch SLA | 심각도별 패치 제공 약속 기한 |

## 4. 책임·권한
| 역할 | 책임 |
|------|------|
| Security Officer (PSIRT Lead) | CVD 운영 총괄, 외부 커뮤니케이션, 공시 결정 |
| 제품 책임자(PM) | 영향 범위 판정, 패치 우선순위 결정 |
| SW Engineer | 재현·근본원인 분석, 패치 개발 |
| QA/RA | 패치 검증, 규제기관 보고(MDR/MIR), DHF 기록 |
| Legal | 공시문 검토, 신고자 면책 합의 |
| Customer Service | 사용자 통지(Field Safety Notice 협조) |

PSIRT(Product Security Incident Response Team)는 본 정책 발효 후 60일 이내 정식 발족한다.

## 5. 신고 접수 채널
| 채널 | 주소(예시) | 용도 |
|------|-----------|------|
| 공식 메일 | psirt@<company>.com | 모든 신고 1차 접수 |
| security.txt | https://<company>.com/.well-known/security.txt | 채널 안내, PGP 키 |
| 웹 폼 | https://<company>.com/security/report | 비기술 신고자 편의 |
| HackerOne / Bugcrowd | (운영 검토) | 옵션 — 2026 H2 평가 |

PGP 키는 매 12개월 갱신, 채널은 24/7 모니터링.

## 6. 처리 SLA
| 단계 | 기한 | 비고 |
|------|------|------|
| 접수 확인 | 2 영업일 | 자동 응답 + 담당자 배정 |
| 1차 Triage | 5 영업일 | 진위·심각도 잠정 결정 |
| 영향 분석 | 14 영업일 | SBOM·VEX 갱신 |
| 패치 개발 | Critical 30일 / High 60일 / Med 90일 / Low 180일 | CVSS v4.0 기준 |
| 공시 | 패치 배포 동시 또는 ±7일 | 신고자 합의 |
| MFDS·FDA·EU 보고 | 사고 인지 후 법정기한(§10) | |

## 7. 처리 흐름
```
[신고 접수] → [Acknowledge ≤2d] → [Triage ≤5d] → [영향분석/SBOM·VEX]
   → [패치 개발(SLA)] → [내부 검증/회귀시험] → [공시·배포]
   → [Reporter 사후 통지/사례공유] → [Lessons Learned → 차기 SOP 반영]
```
각 단계 산출물은 PSIRT 티켓 시스템(JIRA-Sec)에 기록되며, DHF/DMR에 편입된다.

## 8. 공시 원칙
- 기본 90일 Embargo, 신고자 합의 시 연장/단축
- 동시 공시(synchronized release) 우선, 부득이한 경우 단계 공시
- 공시문 필수 포함: 영향 받는 모델/버전, CVE ID, CVSS 점수, 공격 시나리오 요약, 완화책, 패치 절차
- Reporter 공개/비공개·Hall of Fame 등재 여부는 신고자 의사 우선

## 9. 면책 / Safe Harbor
- 정직한 보안 연구를 위해 본 정책에 따라 신고된 행위는 법적 조치 대상 아님
- 단, ① 환자 데이터 접근/유출 ② 임상 운영 중인 기기 가용성 침해 ③ 사회공학·물리적 침해는 제외
- 미국·EU·한국 관할 모두 동일 기준 적용

## 10. 규제기관 보고 의무
| 관할 | 트리거 | 기한 | 양식 |
|------|--------|------|------|
| FDA(미) | 환자에게 위해 가능한 사이버 사고 | 즉시(unforeseeable adverse event) + MDR 30일 | MedWatch 3500A |
| EU MDR | 사망/중대 위해 가능 | 인지 후 즉시(serious 2d/15d) | EUDAMED Vigilance |
| MFDS(국내) | 사용 중 부작용·결함 | 사망 7일/위해 15일/기타 30일 | 의료기기전자민원창구 |
| KISA(국내) | 침해사고 인지 시 | 24시간 이내 | 정보통신망법 §48의3 |

본 매트릭스는 `01_법규_규제/`의 각 규제 문서와 교차참조한다.

## 11. 외부 컴포넌트(OSS·상용) 처리
1. SBOM(SOP-SBOM-001 §6) 기준으로 영향 범위 즉시 판정
2. Upstream 패치 가용성 확인 → 없으면 자체 패치/완화제어 결정
3. VEX 갱신·고객 배포(SBOM과 동봉)
4. EoS·EoL 컴포넌트는 SOP-CC-001 변경관리로 대체·제거 추진

## 12. 측정 지표(KPI)
- MTTA(접수→Acknowledge): ≤2 영업일
- MTTR(접수→패치 배포): Critical 30d / High 60d 준수율 ≥ 95%
- 미공시 잔여 취약점 수(>SLA 초과): 0 유지
- 외부 신고자 만족도(post-disclosure 설문): ≥ 4.0/5.0

## 13. 기록 및 보관
- 모든 신고·처리 이력은 제품 EoS 후 15년 보관(사내 자율정책 — EU MDR Annex IX Ch.III §7 비이식형 법적 최소 10년 초과 보존; ISO 13485 §4.2.5)
- DHF/DMR 편입: VEX, 패치 검증 결과, 공시문, 규제기관 보고 사본
- 연 1회 경영검토에 KPI·미해결 건 보고


---

## 15A. FDA 사이버보안 지침 2026-02 개정 대응 (v0.3 추가)

> **배경**: FDA가 2026-02-03 사이버보안 지침을 재발행하여 QSR → QMSR 참조를 전면 교체했다. CVD 계획은 FD&C Act §524B(b)(1)에 따라 "cyber device"의 시판 전 제출 의무 문서이며, QMSR 하에서 QMS 문서로 명시적으로 편입된다.

### 15A.1 QMSR 하 CVD 계획의 QMS 편입

| 항목 | 변경 사항 |
|------|----------|
| 문서 위상 | 독립 정책문서 → QMS 필수 문서(ISO 13485 §4.2.4 문서관리 대상) |
| 실사 열람 | FDA 실사 시 CVD 계획·실행 기록 직접 열람 대상 (QMSR 하 보호 조항 없음) |
| 설계관리 연계 | CVD 계획을 설계관리(§7.3) 출력물로 명시 — 설계 검토 시 사이버보안 리스크 평가와 CVD 대응 역량 확인 |
| SPDF 연계 | Secure Product Development Framework 내 CVD를 사후 보안 유지(post-market security maintenance) 핵심 프로세스로 배치 |

### 15A.2 CP 7382.850 실사 — 사이버보안 CVD 점검 항목

FDA CP 7382.850(2026-01-30)은 "cyber device" 실사 시 다음 CVD 관련 항목을 확인한다:

1. **CVD 계획 존재 및 최신성**: §524B 요구 CVD 계획이 QMS에 편입되어 관리되는지
2. **취약점 모니터링 체계**: SBOM 기반 지속적 모니터링(CISA KEV, NVD, vendor advisory) 운영 증적
3. **신고 접수·처리 이력**: 외부 신고 접수 후 SLA 준수 기록, 패치 배포 기록
4. **규제 보고 연계**: Critical/High 취약점의 MDR 보고 여부 판정 기록
5. **SBOM 갱신 기록**: 패치 적용 시 SBOM 갱신·VEX 발행 기록

### 15A.3 CVSS v4.0 전면 적용

기존 CVSS v3.1 기반 심각도 평가를 CVSS v4.0으로 전면 전환한다:

| 항목 | CVSS v3.1 (기존) | CVSS v4.0 (변경) |
|------|-----------------|-----------------|
| 심각도 계산 | Base Score 단독 | Base + Threat + Environmental + Supplemental 4중 평가 |
| 의료기기 반영 | 환자안전 별도 평가 필요 | Supplemental 메트릭에 Safety 포함 가능 |
| 점수 체계 | 0.0~10.0 | 0.0~10.0 (동일 범위, 세분화된 산출) |
| 적용 시점 | 즉시 (신규 신고부터) | |

F-CVD-001 양식의 'CVSS 점수' 항목을 'CVSS v4.0 점수'로 변경하고, Base/Threat/Environmental 각 점수를 별도 기록한다.

### 15A.4 X-ray 시스템 사이버보안 CVD 특수사항

X-ray 시스템은 "cyber device"로서 다음 취약점 유형에 대한 CVD 대응 역량을 유지한다:

| 취약점 유형 | 환자안전 영향 | CVD 대응 우선순위 |
|------------|-------------|-----------------|
| 선량 제어 SW 취약점 | 과선량·저선량 위험 | Critical — 30일 이내 패치 |
| 영상 무결성 취약점 | 진단 오류 위험 | Critical — 30일 이내 패치 |
| 환자 데이터 유출 취약점 | 개인정보 침해 | High — 60일 이내 패치 |
| 원격 접근 취약점 | 장비 무단 제어 위험 | Critical — 30일 이내 패치 |
| OSS 구성요소 취약점 | 간접적 | SBOM 기반 영향도 평가 후 등급 결정 |
## 14. 개정 이력
| 버전 | 날짜 | 변경 내용 | 작성 |
|------|------|-----------|------|
| v0.3.1 | 2026-07-10 | **audit #954/#948 정정** — §524B(b)(2)→(b)(1) 인용부정확 정정(2개소, CVD 계획 근거), FDA Cyber Guidance 판본 '2023-09-26'→2026-02 Final(Docket FDA-2021-D-1158) 정정 | md-process-auditor |
| v0.3 | 2026-06-05 | v0.3 보강 — FDA 사이버보안 지침 2026-02 개정 반영, QMSR CVD 계획 QMS 편입, CVSS v4.0 전면 적용 |
| v0.2 | 2026-05-21 | v0.2 보강 — forms·related-docs 추가, applicable 규격 보강, frontmatter 정규화, 양식 템플릿(F-CVD-001) 추가 |
| v0.1 | 2026-04-25 | 초안 작성 | 자동화 세션 |

## 15. 미확정·후속 과제
- HackerOne/Bugcrowd 도입 여부 — 2026 H2 결정
- PSIRT 인력 충원 계획(최소 2 FTE) — HR 협의 필요
- security.txt·PGP 키 인프라 구성 — IT 협조 요청
- Sigstore/in-toto 활용 패치 아티팩트 서명 자동화 — SOP-SBOM-001 v0.2와 병행 검토


---

## 부록: 양식 템플릿

### F-CVD-001 — 취약점 신고 접수·처리 기록

| 항목 | 내용 |
|------|------|
| CVD No. | CVD-YYYY-NNN |
| 접수일 | |
| 신고 채널 | ☐이메일 ☐웹폼 ☐CERT 통보 ☐내부 발견 |
| 신고자 정보 | (익명 허용, 연락처) |
| **취약점 상세** | |
| 영향 제품/SW 버전 | (X-ray 시스템 모델, Detector FW, SW 버전) |
| 취약점 유형 | (CWE 분류) |
| CVSS 점수 (v3.1) | |
| 심각도 | ☐Critical(≥9.0) ☐High(7.0~8.9) ☐Medium(4.0~6.9) ☐Low(<4.0) |
| 환자안전 영향 | ☐선량 제어 영향 ☐영상 무결성 영향 ☐데이터 유출 ☐없음 |
| **처리 SLA** | |
| 확인 응답 기한 | 접수 후 5영업일 |
| 패치 배포 목표 | Critical: 30일 / High: 60일 / Medium: 90일 |
| 공시 예정일 | (신고자 협의) |
| **조치 내역** | |
| 근본 원인 | |
| 패치/완화 조치 | |
| SBOM 갱신 | ☐필요 ☐불필요 |
| 변경통제 연계 | ☐SOP-CC-001(CR No:    ) |
| CAPA 연계 | ☐SOP-CAPA-001(CAPA No:    ) ☐불필요 |
| 규제 보고 | ☐FDA(MDR) ☐MFDS ☐NB ☐해당없음 |
| **종결** | |
| 공시 완료일 | |
| 신고자 확인 | ☐완료 ☐불필요 |
| 종결 승인자 | |

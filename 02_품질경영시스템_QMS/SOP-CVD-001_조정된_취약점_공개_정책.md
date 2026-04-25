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
- FDA FD&C Act §524B(b)(2): "have a plan to monitor, identify, and address ... vulnerabilities and exploits"
- FDA Premarket Cybersecurity Guidance(2023-09-26): SBOM·VEX·CVD plan 제출 의무
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
- 모든 신고·처리 이력은 제품 EoS 후 15년 보관(ISO 13485 §4.2.5, MDR Annex IX)
- DHF/DMR 편입: VEX, 패치 검증 결과, 공시문, 규제기관 보고 사본
- 연 1회 경영검토에 KPI·미해결 건 보고

## 14. 개정 이력
| 버전 | 날짜 | 변경 내용 | 작성 |
|------|------|-----------|------|
| v0.1 | 2026-04-25 | 초안 작성 | 자동화 세션 |

## 15. 미확정·후속 과제
- HackerOne/Bugcrowd 도입 여부 — 2026 H2 결정
- PSIRT 인력 충원 계획(최소 2 FTE) — HR 협의 필요
- security.txt·PGP 키 인프라 구성 — IT 협조 요청
- Sigstore/in-toto 활용 패치 아티팩트 서명 자동화 — SOP-SBOM-001 v0.2와 병행 검토

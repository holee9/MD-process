---
title: "audit(factuality): IEC 81001-5-1:2021 'Clause 5' 보안위험관리/요구사항분석/위협모델링/시험 오귀속 — 정답 §4.2·§7(보안위험관리 PROCESS)·§5.2(요구사항)·§5.7(시험)"
labels: "audit:factuality,prio:P0,risk:high"
state: closed
---

## 대상 (C1×07_위험관리_ISO14971 전수 스윕)

1. `07_위험관리_ISO14971/위험관리_개요.md` L27
   > 사이버보안: IEC 81001-5-1:2021 §5 (보안 위험관리)
2. `07_위험관리_ISO14971/SOP-RM-001_위험관리_절차.md` L225, L264-272 (§5.9.5 매핑표 전체)
   > IEC 81001-5-1:2021 §5.3~5.5를 준수하여... / 5.9.1 범위→§5.3 보안 요구사항 분석 / 5.9.2 STRIDE→§5.4 위협 모델링 / 5.9.3 CVSS 등급화→§5.4 위협 모델링—위험 산정 / 5.9.4 통제 수단→§5.5 보안 설계·구현
3. `07_위험관리_ISO14971/F-RM-002_위험분석_워크시트_FMEA.md` L765
   > IEC 81001-5-1 §5.5 보안 시험 결과 반영

## 결함

IEC 81001-5-1:2021 공식 목차(Contents, Tier1 — ANSI 무료 미리보기 PDF 직접 확보) 확인 결과, 조항 구조는 다음과 같다.

- **Clause 4.2 "SECURITY RISK MANAGEMENT"** — 일반 요구사항 내 보안위험관리 규정
- **Clause 5 "Software development PROCESS"** — SW개발 전주기 프로세스(보안위험관리 전담 조항이 아님)
  - 5.1 Software development planning
  - **5.2 HEALTH SOFTWARE requirements analysis** (5.2.1 SW SECURITY requirements, 5.2.2 SECURITY requirements review, 5.2.3 SECURITY risks for REQUIRED SOFTWARE)
  - **5.3 Software architectural design** (5.3.1 DEFENSE-IN-DEPTH architecture/design, 5.3.2 secure design best practices, 5.3.3 SECURITY architectural design review)
  - **5.4 Software design** (secure design, interfaces, detailed design VERIFICATION for SECURITY)
  - **5.5 Software unit implementation and VERIFICATION** (secure coding standards, SECURITY implementation review)
  - 5.6 Software integration testing
  - **5.7 Software system testing** (5.7.1 SECURITY requirements testing, 5.7.2 THREAT mitigation testing, 5.7.3 VULNERABILITY testing, 5.7.4 Penetration testing)
  - 5.8 Software release
- **Clause 7 "SECURITY RISK MANAGEMENT PROCESS"** — 보안위험관리 전담 조항(7.1 RM context, 7.2 식별, 7.3 추정·평가, 7.4 통제, 7.5 효과성 모니터링)

즉 저장소 3개 문서가 "§5"를 "보안 위험관리" 자체로 지칭하거나(①), §5.9.5 매핑표에서 "§5.3=보안요구사항분석/§5.4=위협모델링/§5.5=보안설계·구현"으로 배정(②), "§5.5=보안 시험 결과"로 인용(③)한 것은 모두 사실과 다르다.

- 보안위험관리(Security Risk Management) 자체 = Clause 4.2(일반) 또는 Clause 7(전담 프로세스), **Clause 5 전체 아님**.
- 보안 요구사항 분석 = §5.2 (§5.3 아님). §5.3은 아키텍처 설계 단계.
- "위협 모델링"에 명확히 대응하는 서브조항은 목차상 없음(§5.3.1 DEFENSE-IN-DEPTH architecture 또는 Clause 7 위험식별과 관련) — §5.4(Software design)에 배정한 것은 오귀속.
- 보안 구현 검토 = §5.5 (설계 아님, "구현" 검증 단계). "설계·구현"으로 §5.4/§5.5를 뭉뚱그려 §5.5에만 배정한 것도 부정확.
- 보안 **시험** 결과 = §5.7(Software system testing, 특히 5.7.1 SECURITY requirements testing/5.7.2 THREAT mitigation testing) — §5.5(구현·검증)이 아님.

## Tier1 근거

ANSI 무료 미리보기 PDF(IEC 81001-5-1:2021 공식 CONTENTS 전문, 저작권자 IEC, 실제 조항 제목 전체 확보) — `https://webstore.ansi.org/preview-pages/ISO/preview_IEC+81001-5-1-2021.pdf` 직접 열람. 목차 전체 확보(paywalled 본문 아님, 공식 목차는 무료 공개) — 기존 사이클(01~06)에서 "IEC 81001-5-1 조항 구조 미확보(paywalled)"로 미확인 처리했던 항목들도 본 목차로 재검증 가능(향후 사이클 권고 — 아래 참고).

## 판정

P0 — 3개 문서, 최소 4개소. 감사관 본문 미수정(이슈 등록만). 실운영 문서 미참고.

## 향후 사이클 참고

본 사이클에서 확보한 IEC 81001-5-1:2021 공식 목차(무료 미리보기)는 02_QMS, 03_설계_개발관리 등 타 카테고리에서 "IEC 81001-5-1 조항 — paywalled 미확인"으로 남겨둔 기존 항목(예: SOP-SBOM-001 '§7.SR' 표기, 03_설계 IEC_81001-5-1 문서 등) 재검증에 활용 가능. 다음 C1 사이클 또는 별도 재확인 스프린트 대상으로 원장에 기록.

## 정정 완료 (2026-07-19, 드레인 스프린트)
- `07_위험관리_ISO14971/위험관리_개요.md` §1: "IEC 81001-5-1:2021 §5(보안 위험관리)" → "§4.2·Clause 7(보안 위험관리 프로세스)" 정정 (v0.2.1→v0.2.2)
- `07_위험관리_ISO14971/SOP-RM-001_위험관리_절차.md` §5.9 도입부·§5.9.5 매핑표: §5.3~5.5 오귀속 5개소 → §4.2/§7.1~7.4/§5.2~5.5/§5.7로 재배정 (v0.3→v0.3.1)
- `07_위험관리_ISO14971/F-RM-002_위험분석_워크시트_FMEA.md` §12.2: "§5.5 보안 시험 결과" → "§5.7(5.7.1 SECURITY requirements testing)" 정정 (v0.2.1→v0.2.2)
- **동일 오류클래스 일괄교정(proactive sweep)**: 저장소 전체 `IEC 81001-5-1` 조항 인용 grep 전수 검토 후 추가 3문서 4개소 정정
  - `05_검사_시험_밸리데이션/IEC60601-2-54_형식시험_체크리스트.md` 항목52/53: §5.3/§5.4(설계단계) → §5.7(시스템시험단계) (v0.2→v0.2.1)
  - `05_검사_시험_밸리데이션/외부_Pen-test_계획서_v0.1.md` frontmatter+§2표: §7.4(위험통제) → §5.7(5.7.4 Penetration testing) (v0.2.1→v0.2.2)
  - `05_검사_시험_밸리데이션/X-ray_장비_안전성능_표준_매핑.md` §6표 No.8: §7.4 → §5.7(5.7.4) (v0.4.1→v0.4.2)
  - `06_문서_기록관리/SOP-DOC-001_문서_기록관리_절차.md` §9.3: §5.7(AI/ML) 오귀속 2개소 — Tier1 미확인 세부조항이므로 "세부조항 미확인"으로 완화 표기(추정배제, v0.3→v0.3.1)
- Clause 6·Clause 8 인용(§6.1, §6.2, §6.5, §8, §8.3 등)은 본 사이클에서 확보한 Tier1 목차(§4.2/§5.1~5.8/§7.1~7.5)에 포함되지 않아 판정 보류(미확인 유지, 임의 수정하지 않음 — 추정배제).
- 실운영 문서 미참고. web_verification: yes(ANSI 무료 미리보기 IEC 81001-5-1:2021 공식 CONTENTS, 기존 확보 Tier1 재사용 — 신규 web 조회 없음, 문서 간 정합 교정).


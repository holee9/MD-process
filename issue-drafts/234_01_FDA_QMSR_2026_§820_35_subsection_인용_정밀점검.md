---
title: "[PLAN] FDA_QMSR_2026 §820.35 하위항목 (a)(b)(c)(d) 인용 정밀점검"
labels: "source:plan,type:audit-followup,prio:P2,risk:med,규제"
state: closed
created: 2026-06-25
created-by: holee9-builder
related-issues: [915]
target-doc: 01_법규_규제/03_미국_FDA/FDA_QMSR_2026.md
---

## 배경
audit #915로 `FDA_QMSR_820.35_vs_ISO13485_4.2.5` v0.3 §820.35 (a)(b)(c)(d) 하위항목 주제를 eCFR 본문대로 정정했으나, 또 다른 FDA 가이드 `FDA_QMSR_2026.md`에서도 동일 오류 잔존 여부를 정밀 점검해야 한다.

## DoD
- [ ] `01_법규_규제/03_미국_FDA/FDA_QMSR_2026.md` 본문에서 §820.35 인용 모든 라인 추출
- [ ] 각 라인 (a)(b)(c)(d) 주제가 eCFR 본문((a)불만 / (b)서비스 / (c)UDI / (d)Confidentiality)과 일치하는지 검증
- [ ] 불일치 라인 정정, v+1 개정이력 등록
- [ ] Part 11을 §820.35 하위항목으로 잘못 결합한 표현 제거

## Tier 1 출처
- 21 CFR 820.35 (eCFR 현행, Source: 89 FR 7523, 2024-02-02; 시행 2026-02-02)

## 우선순위
P2 — 적용 시점은 이미 시행됐고 다른 FDA 가이드와의 사내 정합성 확보 필요.

## 종결 처리 (2026-07-09, md-process-auditor)
재확인 결과 `FDA_QMSR_2026.md`는 이미 v0.3(2026-06-26, audit #917 close 커밋)에서 §3.3 및 §6 F-QMSR-READINESS-001 표의 §820.35(a)(b)(c)(d) 하위항목을 eCFR 원문(complaints/servicing/UDI/confidentiality)대로 정정 완료한 상태였음을 확인. Part 11도 §3.6으로 독립 분리되어 있어 DoD 4개 항목 모두 충족. 추가 조치 불요 — closed.

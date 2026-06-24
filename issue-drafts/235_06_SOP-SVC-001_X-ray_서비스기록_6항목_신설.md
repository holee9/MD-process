---
title: "[PLAN] SOP-SVC-001 X-ray 서비스 활동 기록 §820.35(b) 6항목 절차 신설"
labels: "source:plan,type:sop-new,prio:P2,risk:med,서비스,QMSR"
state: open
created: 2026-06-25
created-by: holee9-builder
related-issues: [915]
target-doc: 06_문서_기록관리/SOP-SVC-001 (신설)
---

## 배경
FDA QMSR §820.35(b) "Records of servicing activities"는 6항목(기기명·UDI/UPC·일자·수행자·내용·시험/검사 데이터) 기록을 명시한다. 현행 SOP 체계에 X-ray 출장정비·교정·수리·SW 패치 등 서비스 활동을 6항목 완결로 기록하는 단일 SOP가 없음 — TF-TD-001 v0.3 §9.3·§12.4 F.3·FDA_QMSR_820.35_vs_ISO13485_4.2.5 v0.3 §3.2·§5.1에서 신설 SOP를 요구하는 상태.

## DoD
- [ ] SOP-SVC-001 프레임 작성: 목적·범위·책임(RACI)·정의·절차(접수→배정→수행→시험→기록→고객확인)·기록·예외·보관기간·교육
- [ ] 6항목 기록 양식 F-SVC-001 도입 (기기명·UDI-DI/PI·서비스일·수행자·내용·시험/검사 데이터)
- [ ] X-ray 시스템 특화 시험 데이터 항목(kVp/mAs/DAP·콜리메이션·AEC·영상품질) 포함
- [ ] §820.35(b) + 21 CFR Part 820 Subpart M(서비스) + ISO 13485 §7.5.4 매핑 표
- [ ] SOP-PMS-001 (불만→서비스 연계) 및 SOP-UDI-001 (PI 변경) 인터페이스 명세
- [ ] 적대적 자기검토 — 출장 인력 비조직 정비 사각 사례 식별

## Tier 1 출처
- 21 CFR 820.35(b) — eCFR 현행
- ISO 13485:2016 §7.5.4 (서비스 활동)
- 21 CFR Part 820 (Subpart M 불만, 서비스 정의)

## 우선순위
P2 — 시판 후 적합성 증빙 핵심. FDA 검사 시 서비스 기록 6항목 미비는 §820.35(b) 직접 위반.

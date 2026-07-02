---
title: "[PLAN P1] plan #935 확장 — 자매문서 cross-reference 자동화 매칭룰에 FDA Cyber Guidance 판본 대응 추가 (audit #940 후속)"
labels: "source:plan,type:automation,prio:P1,risk:medium"
state: open
created: 2026-07-03
created-by: holee9-builder
related-issues: [935, 938, 940]
target-doc: 00_프로젝트관리/자매문서_교차참조_자동화_설계.md
---

## 배경
audit #938(단일 문서) → audit #940(벤치마크 3건 자매재발) 패턴 확인. FDA Cybersecurity Guidance 판본은 다음 3세대가 사내 인용에 혼재 가능:
- 2023-09-27 Final (superseded)
- 2025-06-27 Final (superseded)
- **2026-02 Final (Docket FDA-2021-D-1158, 현행)**

plan #935가 정의하는 sister-document cross-reference 자동화 룰에 "FDA Cyber Guidance 판본 매칭 패턴"이 아직 미포함.

## 목적
사내 문서에서 FDA Cybersecurity Guidance 인용이 노후 판본(2023-09-27, 2025-06-27)으로 등장 시, 자동 감지·경고·정정 후보 제시.

## Tier 1 근거
- FDA. "Cybersecurity in Medical Devices: Quality Management System Considerations and Content of Premarket Submissions" — Final Guidance, February 2026 (content current as of 2026-02-03), Docket FDA-2021-D-1158. 2회 supersede.
  https://www.fda.gov/regulatory-information/search-fda-guidance-documents/cybersecurity-medical-devices-quality-management-system-considerations-and-content-premarket

## DoD
- [ ] `plan #935` 매칭 룰 스펙에 "FDA Cyber Guidance 판본 패턴" 추가 (정규식: `(2023-09-27|2025-06-27)\s*(final|guidance|cyber)`).
- [ ] 정정 후보 자동 삽입: `→ 2026-02 Final (Docket FDA-2021-D-1158, 2회 supersede)`.
- [ ] audit 이력(감사 이력·supersede 기록 문맥)은 정상 인용으로 whitelist 처리.
- [ ] 사이클 1회 후 사내 문서 재점검(현재 잔존 노후 인용 0건 유지 확인).

## 우선순위
P1 — 사실성 노후 재발 방지 자동화. audit #940 재발 방지 직결.

## 비고
실운영 문서 미참고. audit #940 처리 중 sister-document 재발 패턴에서 도출한 emergent 후속 plan.

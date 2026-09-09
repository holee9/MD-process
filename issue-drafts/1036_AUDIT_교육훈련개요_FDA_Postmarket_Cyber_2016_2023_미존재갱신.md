---
title: "audit(currency): 교육_훈련_개요 L130 — FDA Postmarket Cybersecurity Guidance '(2016/2023)' 미존재 갱신 판본 (#1026 자매재발)"
labels: "audit:currency,prio:P1,risk:medium,training,compliance"
opened: 2026-09-09
---

## 대상 (C3×10_교육_훈련 전수 스윕 — C3 최종 카테고리)

`10_교육_훈련/교육_훈련_개요.md` L130 (§9 조직 학습·피드백):

> - FDA Postmarket Cybersecurity Guidance **(2016/2023)** — 사이버 취약점 발견 시 조직 학습 반영

## 결함

FDA "Postmarket Management of Cybersecurity in Medical Devices" Final Guidance는 **2016-12-28 발행 이후 개정된 바 없다.** "2023" 판본은 미존재이며, 2023-09-27자 문헌은 **별개의 Premarket 가이던스** "Cybersecurity in Medical Devices: Quality System Considerations and Content of Premarket Submissions"로서, 이마저 **2026-02 Final(Docket FDA-2021-D-1158)로 supersede** 되었다. 따라서 본 표기는 (a) 미존재 판본 창작, (b) Postmarket/Premarket 두 별개 가이던스의 혼동, (c) 이미 대체된 2023-09 판본 참조 — 3중 결함.

**동일 클래스 자매재발**: audit #1026(GH#1704, `08_시판후_감시_PMS/PMS_개요.md` L141 "(2016, 2023 갱신)")과 **동일한 오류 패턴**. C3×08 사이클(2026-08-09)에서 PMS_개요만 등록되고 10 카테고리 잔존분이 확산 grep에서 누락됨(#935 자매문서 교차참조 자동화 미적용 구간).

## Tier1 근거

- Federal Register 2016-31406 — "Postmarket Management of Cybersecurity in Medical Devices; Guidance … Availability", 2016-12-28. 이후 개정 고시 부재.
- FDA Docket FDA-2021-D-1158 — Premarket Cybersecurity Guidance 2026-02 Final(2023-09-27 Final을 supersede). 기 audit #938/#940/#947/#948/#954/#1026 확정 사실 재사용.

## 판정

**P1 / risk:medium** — 사이버보안 교육·조직학습의 규제 근거 문서를 잘못 지목. 정정 권고:
`FDA Postmarket Cybersecurity Guidance (2016-12-28 Final)` 로 단독 표기하고, Premarket 계열 병기 시 `FDA Premarket Cybersecurity Guidance (2026-02 Final, Docket FDA-2021-D-1158)` 로 **별행 분리**.

## 확산 점검

저장소 전수 grep 결과 본 패턴 잔존은 1개소(PMS_개요는 #1026으로 기등록). 추가 자매 0건.

## 참고

- 원장: `00_프로젝트관리/_audit_sweep_ledger.md` (C3×10)
- 실운영 문서 미참고: 확인. web: ok.

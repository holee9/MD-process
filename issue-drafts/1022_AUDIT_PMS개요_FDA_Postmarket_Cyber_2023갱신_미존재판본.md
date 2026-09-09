---
title: "audit #1026 (citation/C3): PMS_개요.md §8.1 — FDA Postmarket Cybersecurity Guidance '(2016, 2023 갱신)' 미존재 갱신판 표기"
labels: "audit:citation,prio:P1,risk:medium"
state: closed
gh-issue: 1704
---

## 결함 (C3×08_시판후_감시_PMS 전수 스윕, 2026-08-09 등록 — GH#1704)

`08_시판후_감시_PMS/PMS_개요.md` L141: "FDA Postmarket Cybersecurity Guidance (2016, 2023 갱신)".

## Tier1 (2026-09-09 드레인 사이클 직접 재확인)

- FDA *Postmarket Management of Cybersecurity in Medical Devices* — **Final, 2016-12-28 발행**, Docket **FDA-2015-D-5105**, Federal Register 게재 2016-31406(2016-12-28). CDRH 발행 이후 **개정판·갱신판 없음**(FDA guidance 검색 페이지·HHS Guidance Portal·FR 원문 교차확인).
- "2023" 판은 **별개의 Premarket** 사이버보안 가이던스(2023-09 Final) 계열이며, 저장소가 이미 확정한 현행판은 2026-02 Final(Docket FDA-2021-D-1158). 즉 Postmarket 문서에 Premarket 판본 연도를 혼입한 표기.

## 수정 (2026-09-09, 드레인 스프린트)

- `PMS_개요.md` §8.1 → "FDA *Postmarket Management of Cybersecurity in Medical Devices* (Final, 2016-12-28 발행, Docket FDA-2015-D-5105 / FR 2016-31406) — 발행 이후 개정판 없음" (v0.3.3, 상단 정정주석 부기).
- **동일 오류클래스 전 저장소 일괄교정**: grep(`Postmarket Cybersecurity Guidance`) 결과 자매재발 1개소 신규 발견 — `10_교육_훈련/교육_훈련_개요.md` L130 "(2016/2023)" → 정식 표제 + "이후 개정 없음"으로 동반 정정(v0.2.1, 인라인 정정주석). 정정 후 잔존 0건.

실운영 문서 미참고. web_verification: yes(FDA guidance 페이지·Federal Register 2016-31406·HHS Guidance Portal 교차확인).

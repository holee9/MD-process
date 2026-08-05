---
title: "audit #1018 (citation/C3): SOP-PKG-001 §9 — ESD 경고 라벨 기호 'IEC 60417-5734' 오기재 (정답 5134)"
labels: "audit:citation,prio:P2,risk:low"
state: closed
gh-issue: 1695
---

## 결함 (C3×04 전수 스윕, 2026-08-05 등록 — GH#1695)

`04_제조공정_관리/SOP-PKG-001_라벨링_포장관리_절차.md` L283: "ESD 경고 라벨 부착: IEC 60417-5734 기호 사용".

## Tier1

ESD(정전기 민감 소자) 경고 기호의 정답 번호는 **IEC 60417-5134** "Electrostatic sensitive devices" (ISO Online Browsing Platform Tier1, 2026-08-05 사이클 확인). 5734는 IEC 60417 DB(유료)에서 실존 미확인 — 최소 오귀속 확정.

## 수정 (2026-08-06, 드레인 스프린트)

- SOP-PKG-001 L283: `IEC 60417-5734` → `IEC 60417-5134` + 기호 표제 병기 (v0.2.4).
- 동일 클래스 일괄 점검: 저장소 전수 grep(`60417`) — 타 출현은 `IEC_62366-1_사용적합성_엔지니어링_계획서_v0.1.md` L49의 표준 시리즈 일반 인용(기호 번호 미기재)뿐, 오기재 잔존 0건.

실운영 문서 미참고. web_verification: 기확보 Tier1(ISO OBP, 2026-08-05) 재사용.

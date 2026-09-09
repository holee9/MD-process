---
title: "audit #1027 (citation/C3): SOP-PSUR-001 §DQE — 'IEC 62220-1'(2003 구판) 인용, 정답 IEC 62220-1-1:2015"
labels: "audit:currency,prio:P2,risk:low"
state: closed
gh-issue: 1705
---

## 결함 (C3×08 전수 스윕, 2026-08-09 등록 — GH#1705)

`08_시판후_감시_PMS/SOP-PSUR-001_정기안전성보고_PMCF_절차.md` L181: "영상 화질 — DQE | ... | IEC 62220-1에 따른 측정".

## Tier1 (2026-09-09 재확인)

**IEC 62220-1-1:2015**(Ed.1.0, IEC Webstore pub.21937) — *Medical electrical equipment — Characteristics of digital X-ray imaging devices — Part 1-1: Determination of the detective quantum efficiency — Detectors used in radiographic imaging*. 원문 Foreword: **IEC 62220-1:2003을 cancel & replace**하는 technical revision(IEC 61267:2005 반영). 따라서 무접미 "IEC 62220-1"은 폐지된 2003 구판 지칭.

## 수정 (2026-09-09, 드레인 스프린트)

- `SOP-PSUR-001` L181 → "IEC 62220-1-1:2015에 따른 측정" (v0.3.2, 개정이력 부기).
- 동일클래스 일괄교정은 audit #1029 항목에서 전 저장소 단위로 통합 수행(자매재발 4개소).

실운영 문서 미참고. web_verification: yes(IEC Webstore pub.21937, ANSI webstore, iTeh 원문 샘플 Foreword 교차확인).

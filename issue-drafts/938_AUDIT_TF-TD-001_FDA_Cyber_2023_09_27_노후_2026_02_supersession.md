---
title: "[AUDIT P0] TF-TD-001 v0.4 §18.5 — FDA Premarket Cybersecurity Guidance '2023-09-27' 노후 (정답: 2026-02 Final, 2023-09-27/2025-06-27 2회 supersede)"
labels: "audit:currency,prio:P0,risk:high"
state: closed
closed-date: 2026-07-02
closed-by: holee9-builder
closed-summary: |
  06_문서_기록관리/TF-TD-001 v0.5 §18.5 및 자매 03_설계/IEC_81001-5-1_FDA_Cybersecurity_SW보안.md frontmatter: FDA Cyber Final Guidance February 2026 (Docket FDA-2021-D-1158, 2회 supersede) 반영
---

## 대상 문서
- `06_문서_기록관리/TF-TD-001_의료기기파일_기술문서_관리.md` v0.4 (2026-06-29)
- 위치: §18.5 §SE-3 적합성 표준 일괄 매핑 양식 — "SW 사이버보안" 행

## 주장 (기재값)
> | SW 사이버보안 | IEC 81001-5-1:2021 + **FDA Premarket Cybersecurity Guidance 2023-09-27** | SW 사이버보안 | IEC_81001-5-1_FDA_Cybersecurity_SW보안, SBOM |

즉, FDA 사이버보안 premarket 가이던스의 **현행 적용 판본을 2023-09-27 final** 로 인용.

## Tier 1 정답
FDA Guidance 페이지 — "Cybersecurity in Medical Devices: Quality Management System Considerations and Content of Premarket Submissions" (Docket FDA-2021-D-1158):

- **Current Final Guidance**: **February 2026** (Content current as of: **02/03/2026**)
- 페이지 본문 직접 인용:
  > "This document supersedes the final guidance 'Cybersecurity in Medical Devices: Quality System Considerations and Content of Premarket Submissions,' **issued June 27, 2025**."
- Supersession 이력:
  1. **2023-09-27 Final** (1st final) — superseded by 2025-06-27
  2. **2025-06-27 Final** (2nd final) — superseded by 2026-02-03
  3. **2026-02-03 Final** (현행, 3rd final)

본 문서 v0.4(2026-06-29) 시점 현행 final = **2026-02-03** (직전 final 2025-06-27 supersede). 본 문서가 인용한 **2023-09-27**은 2회 supersede 된 노후 판본.

## 판정
**노후 (P0, audit:currency)** — SE 매트릭스 §18.5 표준 일괄 매핑은 510(k) §VII Performance Data 적합성 일괄 매핑 양식 — 외부 dossier 직접 영향. 노후 판본 인용은:

1. **두 번의 supersession 미반영**: 단순 1회 노후가 아니라 2026-06-29 시점 기준 2회 supersede 된 판본 인용.
2. **자매문서 잠재 영향 (sister-doc risk)**: §18.5 "관련 자사 산출물" 셀의 `IEC_81001-5-1_FDA_Cybersecurity_SW보안` 문서 본문이 어느 판본을 기준 삼는지 별도 점검 필요. 직전 audit #913 (IEC_81001-5-1 frontmatter '§524B FDARA' P0 사실오류) 정정 시 frontmatter는 갱신됐으나 본문 cyber guidance 판본 인용은 본 감사 표본 외 — 후속 점검 권고.
3. **2026-02-03 = QMSR 시행일 다음날**: FDA QMSR §820.35 (a)(b)(c)(d) Tier 1 정정(audit #917)이 2026-02-02 QMSR 시행일을 정확히 반영한 반면, 같은 시점(2026-02-03) FDA cyber 가이던스 supersession 은 미반영. 사내 "2026-02 Tier 1 일제 갱신" 이 분야별로 불균등.

## Tier 1 출처
- FDA 현행 Final Guidance 페이지 (2026-02): https://www.fda.gov/regulatory-information/search-fda-guidance-documents/cybersecurity-medical-devices-quality-management-system-considerations-and-content-premarket
  - Title: "Cybersecurity in Medical Devices: Quality Management System Considerations and Content of Premarket Submissions"
  - Issued: February 2026
  - Docket: FDA-2021-D-1158
  - Supersession statement (인용 above)

## 권고
1. §18.5 "SW 사이버보안" 행 → "FDA Final Guidance 'Cybersecurity in Medical Devices: Quality Management System Considerations and Content of Premarket Submissions' (**February 2026**, Docket FDA-2021-D-1158; supersedes 2025-06-27 및 2023-09-27 final)" 로 정정.
2. 자매문서 `03_설계_개발관리/IEC_81001-5-1_FDA_Cybersecurity_SW보안.md` 본문 (frontmatter 외) 일괄 grep — "2023-09-27" / "premarket cybersecurity" 본문 인용 위치 일괄 갱신.
3. plan #935(Sister-document cross-reference 자동화) 범위에 "FDA cyber guidance 판본 인용" 자동 매칭 룰 추가.
4. 사내 표준 갱신 카덴스 — 분기 종합(2026-Q2) 시 "2026-02 Tier 1 일제 갱신" 누락 분야 (cyber, software, SaMD AI) 일제 점검.

## 추가 PASS 별기록 (같은 §18.5)
- "AAMI/ANSI ES60601-1 (판본은 X-ray 표준매핑 v0.4 참조)" — 판본 위임 양식 (감사 PASS, 위임처 별도 점검 대상).
- "IEC 62304:2006+AMD1:2015 (Ed.1.1)" — audit #908/#925 권고 표기 일치 (PASS).
- "IEC 60601-2-54 Ed.2 (2022-09-26)" — Tier 1 (IEC Webstore 69988) 일치 (PASS).
- "FDA 'Content of Premarket Submissions for Device Software Functions' (2023-06-14)" — Tier 1 (Federal Register 2023-12723) 일치 (PASS).
- "FDA 'Solid State X-ray Imaging Devices 510(k) Guidance' (2016-09-01)" — 직전 사내 BMK 다수 일치 (PASS, 단 final/draft 표시 확인 권고).

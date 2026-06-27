---
title: "[AUDIT P0] PMS_개요 v0.2 §3 — IEC 62304:2006+A1 §9 = 'SW 유지보수' 사실오류 (정답: §6 = Maintenance Process / §9 = Problem Resolution Process)"
labels: "audit:factuality,prio:P0,risk:high"
---

## 대상 문서
- `08_시판후_감시_PMS/PMS_개요.md` (doc-id: PMS_개요, type: Overview, version: v0.2, last-review: 2026-05-02)
- 위치: §3 "관련 규제·표준" 표 마지막에서 두 번째 행

## 주장 (기재값)
> | IEC 62304:2006+A1 | §9 | SW 유지보수 |

즉 IEC 62304:2006+AMD1:2015 Edition 1.1의 **§9** 조항을 **"SW 유지보수"** 주제로 매핑.

## Tier 1 정답 (조항-주제 매핑)
IEC 62304:2006+AMD1:2015 Edition 1.1 본문 구조:
- **Clause 5** — Software development PROCESS
- **Clause 6** — Software MAINTENANCE Process  ← "SW 유지보수"의 정확한 조항
- **Clause 7** — Software RISK MANAGEMENT Process
- **Clause 8** — Software CONFIGURATION MANAGEMENT Process
- **Clause 9** — Software **PROBLEM RESOLUTION** Process  ← 문제 해결/시정·환류 절차 (Maintenance와 별도)

즉 본 문서가 PMS 맥락에서 "SW 유지보수"로 인용한 조항 **§9**는 실제로는 **"Problem Resolution Process"**이며, "Software Maintenance Process"는 **§6**이다.

## 판정
**사실오류 (P0, audit:factuality)** — 표준 본문 조항 번호-주제 매핑이 1차 출처와 불일치. PMS 맥락에서 §9 Problem Resolution과 §6 Maintenance는 별개 프로세스이며, §9는 NCR/CAPA·시정조치와 직결되는 반면 §6은 출시 후 유지보수 계획 자체를 다룬다.

## Tier 1 출처
- ISO Online Browsing Platform — IEC 62304:2006(en): https://www.iso.org/obp/ui/#iso:std:iec:62304:ed-1:v1:en
- ISO catalogue — IEC 62304:2006/Amd 1:2015: https://www.iso.org/standard/64686.html

## 권고
1. §3 표의 IEC 62304 행을 **두 줄**로 분리하여 `§6 — Software Maintenance Process(시판후 변경·결함 처리 절차)` 및 `§9 — Software Problem Resolution Process(문제 해결·시정 환류)`를 각각 명시할 것. PMS 맥락에서는 두 조항 모두 필수 인용 대상.
2. 자매 문서(SOP-PMS-001, GUIDE-VIG-001, IEC_62304_SW_수명주기 등)에 동일 패턴 인용이 있는지 사내 전수 확인(audit #908/#925/#926 패턴과 동일한 자매문서 재발 위험).

## 비고
실운영 문서 미참고. 빌더의 자체 ✅ 신뢰 배제, 1차 출처(IEC OBP) 기반 독립 재확인.

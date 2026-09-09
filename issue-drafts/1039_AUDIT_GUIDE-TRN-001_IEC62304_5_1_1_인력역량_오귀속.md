---
title: "audit(factuality): GUIDE-TRN-001 L13 — IEC 62304 §5.1.1을 'SW 개발 인력 역량' 근거로 오귀속 (원문 §5.1 = 소프트웨어 개발 계획)"
labels: "audit:factuality,prio:P2,risk:low,training"
opened: 2026-09-09
---

## 대상 (C3×10_교육_훈련 전수 스윕)

`10_교육_훈련/GUIDE-TRN-001_역량평가_교육니즈_매트릭스.md` L13 (frontmatter `applicable`):

> - IEC 62304 **§5.1.1 (SW 개발 인력 역량)**

## 결함

IEC 62304:2006+AMD1:2015(Ed.1.1) **원문 목차(Tier1)** 기준 Clause 5는 다음과 같다.

| 조항 | 정식 표제 |
|---|---|
| **5.1** | **Software development planning** (→ 5.1.1 Software development plan) |
| 5.2 | Software requirements analysis |
| 5.3 | Software ARCHITECTURAL design |
| 5.4 | Software detailed design |
| 5.5 | SOFTWARE UNIT implementation and verification |
| 5.6 | Software integration and integration testing |
| 5.7 | SOFTWARE SYSTEM testing |
| 5.8 | Software release |

즉 **§5.1.1은 소프트웨어 개발 계획서 수립 요구**이며, 인력 역량(competence) 요구가 아니다.

IEC 62304는 **인력 역량에 관한 독립 요구조항을 두지 않는다.** 역량은 §4.1(Quality management system)이 QMS로 위임하며, 실제 요구 원천은 **ISO 13485:2016 §6.2(Human resources)** — QMSR 체제에서는 21 CFR 820.10(c)/820.7 참조편입 경로 — 이다. 동일 문서 L10~L11이 이미 `ISO 13485:2016 §6.2` 및 `FDA QMSR (21 CFR 820.25 → ISO 13485 §6.2)`를 정확히 인용하고 있어 **문서 내 근거 체계와도 중복·불일치**.

(참고: IEC 62366-1:2015 §4.1.1은 "USABILITY ENGINEERING 활동은 적절한 교육·훈련·기술 또는 경험을 갖춘 인원이 수행"을 명시하므로, SW 인력 역량의 표준 근거로 62304 §5.1.1보다 적절한 대안이 존재.)

## Tier1 근거

- IEC 62304 Edition 1.1 2015-06 CONSOLIDATED VERSION, **CONTENTS(pp.2~3) 및 Figure 1 원문** — 5.1 "Software development planning" ~ 5.8 "Software release"(공인 유통채널 공개 프리뷰, IEC 저작 원문).
- 동 원문 §4.1 Quality management system(QMS 위임 구조).
- 기 audit #908/#925/#1016 확정 판본 사실 재사용.

## 판정

**P2 / risk:low** — frontmatter 근거 목록 결함(본문 요구 자체는 §6.2로 정합). 정정 권고:
`IEC 62304:2006+AMD1:2015 §5.1(소프트웨어 개발 계획 — 역량 요구는 §4.1 QMS 위임, 원천은 ISO 13485 §6.2)`

## 확산 점검

저장소 내 "62304 §5.1.1 = 인력 역량" 표기 잔존 0건(본 1개소). `03_설계_개발관리/SOP-DT-001` L9의 `IEC 62304 …§5.8`은 설계이관 맥락으로 §5.8(Software release) 귀속이 정합 — PASS.

## 참고

- 실운영 문서 미참고: 확인. web: ok(IEC 원문 프리뷰 직접 대조).

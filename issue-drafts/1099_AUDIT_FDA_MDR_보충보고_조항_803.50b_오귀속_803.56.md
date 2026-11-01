---
title: "[audit:citation] 21 CFR 803.50(b) → 803.56 — MDR 후속(Supplemental) 보고 조항 오귀속 (2문서 2개소)"
labels: "audit:citation,prio:P2,risk:medium"
state: closed
---

## 배경 (C1 조항번호 · 표본 19차-b, 2026-10-31)
FDA MDR 제조업자 후속(supplemental/followup) 보고의 근거 조항은 **21 CFR §803.56**이며 기한은 "30 calendar days of the day that you receive this information"이다. 저장소는 이를 §803.50(b)로 인용 중 (기한 30일 수치는 정확, 조항번호만 오류).

## Tier1 근거
- 21 CFR 803.56 (govinfo, CFR-2024-title21-vol8 sec803-56): 후속 정보 30 calendar days 이내 제출.
- eCFR/FDA accessdata: robots 차단·본문 미회수 (govinfo로 충족).

## 결함 위치
| 문서 | 위치 | 현 인용 | 정정 |
|---|---|---|---|
| 01_법규_규제/03_미국_FDA/FDA_QMSR_820.35_vs_ISO13485_4.2.5.md | L90 | §803.50(b) Supplemental | §803.56 |
| 08_시판후_감시_PMS/SOP-PMS-001_불만처리_부작용보고_절차.md | L143 | 21 CFR 803.50(b) | 21 CFR 803.56 |

## 체크리스트
- [ ] 두 문서 인용 정정 (감사자는 수정하지 않음)
- [ ] 확산 grep: `803.50(b)` 잔여 0
- [ ] 검증

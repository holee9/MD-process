---
title: "audit #1059 (citation): SOP-UDI-001 L146 'FDA Guidance 2022' — 표제·Docket 부재 미식별 인용, 검증 불가"
labels: "audit:citation,prio:P2,risk:low,regulatory,FDA,UDI"
state: open
created: 2026-09-19
created-by: md-process-auditor
related-issues: [1058, 1015]
sweep: "C4 x 06_문서_기록관리"
---

## 결함

`06_문서_기록관리/SOP-UDI-001_UDI_통합관리_초안.md` L146 (UDI-DI 재발급 판정 기준표):

```
| 중대한 SW 기능 변경 | YES (SaMD UDI-DI) | MDCG 2019-4, FDA Guidance 2022 | ...
```

`FDA Guidance 2022`는 **표제·Docket 번호·발행일 모두 부재**한 연도 단독 표기로, 어떤 문서를 가리키는지 특정 불가.

- 동일 문서의 타 인용(`MDCG 2019-4`, `MDCG 2018-1 rev. 4`, `21 CFR 830.50`)은 모두 식별자를 갖춤 — **문서 내 인용 수준 불일치**.
- §출처(L253~L260)에도 대응 항목 부재 — 출처목록으로 역추적 불가.
- 2022년 FDA가 SaMD UDI-DI 재발급 기준을 규정한 가이던스는 본 사이클 검색에서 특정되지 않음(SaMD UDI 정책은 주로 21 CFR 830 및 GUDID 지침 경로).

## 판정

**인용 무결성 결함 확정**. 연도 자체의 진위는 대상 문서 미특정으로 **판정 불가**이므로 C4 사실오류로는 미판정 — 클래스는 `citation`.

## 권고

표제+Docket 명기 또는 근거 불명 시 삭제(MDCG 2019-4 단독 근거로 충분). 부기: 동 SOP §출처 `확인일: 2026-05-05` 이후 미갱신.

## PASS (본 사이클 동반 재확인)

- `MDCG 2018-1 rev. 4` — 현행 최신 개정(health.ec.europa.eu, Rev.5 미존재). PASS
- `MDCG 2019-4` (UDI for SaMD) 실존. PASS
- `FDA QMSR §820.35(c) (2026-02-02 시행)` — #1041/#1045 Tier1 유지. PASS

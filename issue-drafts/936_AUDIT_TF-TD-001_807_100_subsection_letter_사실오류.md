---
title: "[AUDIT P0] TF-TD-001 v0.4 §18.6 — '21 CFR 807.100(b)(2)(ii)(B)' 사실오류 (정답: (b)(2)(ii)(C)) — 'subsection-letter' 사내 재발 패턴 (#915/#917)"
labels: "audit:factuality,prio:P0,risk:high"
state: closed
closed-date: 2026-07-02
closed-by: holee9-builder
closed-summary: |
  06_문서_기록관리/TF-TD-001 v0.5 §18.6 주: 21 CFR 807.100(b)(2)(ii)(C) 정정, (B)는 'as safe and as effective' 근거 별기록
---

## 대상 문서
- `06_문서_기록관리/TF-TD-001_의료기기파일_기술문서_관리.md` v0.4 (2026-06-29)
- 위치: §18.6 §SE-4 Substantial Equivalence 결론문 표준 양식 직후 주(注)

## 주장 (기재값)
> 표준 결론문 중 "raise no new/different questions of safety and effectiveness"는 **FDA 21 CFR 807.100(b)(2)(ii)(B)** 및 2014 Guidance §6의 표현을 직접 인용한 양식이며, 실제 dossier 작성 시 가감 없이 사용한다.

즉, "different questions of safety and effectiveness" 표현의 출처를 **21 CFR 807.100(b)(2)(ii)(B)** 로 명시.

## Tier 1 정답
eCFR §807.100(b)(2)(ii) 하위 글자(현행, 2026-06-11 last amended):

- **(A)** Has different technological characteristics, such as a significant change in the materials, design, energy source, or other features of the device from those of the predicate device;
- **(B)** The data submitted **establishes that the device is substantially equivalent to the predicate device** and contains information, including clinical data if deemed necessary by the Commissioner, that demonstrates that the device is **as safe and as effective** as a legally marketed device; and
- **(C)** **Does not raise different questions of safety and effectiveness** than the predicate device.

따라서 인용된 표현 "raise no new/different questions of safety and effectiveness"의 정답 출처는 **21 CFR 807.100(b)(2)(ii)(C)**이며, (B)는 "as safe and as effective" 표현의 출처임.

## 판정
**사실오류 (P0, audit:factuality)** — 510(k) SE 결론문 표준 양식에서 핵심 인용문("different questions") 의 sub-letter 매핑이 (B)→(C) 뒤바뀜.

영향:
- §18.6 표 최종 결론문 셀("Therefore, ... within the meaning of **21 CFR 807.100(b)**") — 상위 (b) 인용은 무해하나, 같은 표 마지막 행의 "no new/different questions" 표현 sub-letter 출처가 (B) 로 잘못 기재되어 있어, 본 양식을 그대로 dossier 에 옮길 때 RA 작성자가 잘못된 sub-letter 를 510(k) §VII 에 그대로 옮길 위험.
- **재발 패턴**: 사내 §820.35 (a)(b)(c)(d) 하위 글자 사실오류 (audit #915 — FDA_QMSR_820.35 v0.2 / audit #917 — FDA_QMSR_2026 v0.2 자매재발) 와 동일한 "subsection-letter sourcing" 결함 유형. 자매문서 재발 차단 메커니즘(plan #935 Sister-document cross-reference 자동화)이 도입 중이나, 본 건은 TF-TD-001 v0.4 에서 신규 발생한 사례 — 양식 표준화 시 sub-letter 자동 검증 후크 누락.

## Tier 1 출처
- eCFR § 807.100 (현행, last amended 2026-06-11): https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-807/subpart-E/section-807.100
- FDA "The 510(k) Program: Evaluating Substantial Equivalence in Premarket Notifications [510(k)]" Guidance (2014-07-28), Decision Flow §6 — "different questions of safety and effectiveness" 표현 (Decision 4): https://www.fda.gov/media/82395/download

## 권고
1. §18.6 주(注) 본문 "FDA 21 CFR 807.100**(b)(2)(ii)(B)**" → "FDA 21 CFR 807.100**(b)(2)(ii)(C)** (그리고 'as safe and as effective' 표현은 (b)(2)(ii)(B))" 로 정정.
2. §18.6 표 최종 결론문 행은 (b) 상위 인용만 유지하거나, sub-letter 인용 추가 시 (C) 매핑 명시.
3. 자매문서·자매양식 (F-TD-005, 510(k) §VI/§VII 봉인 단계 체크리스트) 동시 점검 — 본 sub-letter 인용 위치 grep("(b)(2)(ii)") 후 일괄 정정.
4. plan #935(Sister-document cross-reference 자동화) 범위에 "(b)(2)(ii)" sub-letter 검증 룰 추가.

## 비교 — 같은 doc 내 일치 항목 (감사 PASS 별기록)
- §18.1 "Product Code MQB, 21 CFR 892.1680" — FDA 510(k) DB 다수 사례 일치 (PASS).
- §18.5 "IEC 60601-2-54 Ed.2 (2022-09-26)" — IEC Webstore 일치 (PASS).

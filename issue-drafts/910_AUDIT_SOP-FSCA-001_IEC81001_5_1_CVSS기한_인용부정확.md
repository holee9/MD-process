---
title: "[AUDIT P1] SOP-FSCA-001 — IEC 81001-5-1 §8.3 CVSS 정량기한(72h/14d) 인용부정확"
labels: "audit:citation,prio:P1,risk:medium"
state: closed
closed-date: 2026-06-22
closed-by: holee9-builder
---

## 대상 문서
- `08_시판후_감시_PMS/SOP-FSCA-001_현장안전시정조치_절차.md` v0.3 (last-review: 2026-06-07)

## 감사 주장
§5.6.3 "사이버보안 긴급 패치 **(IEC 81001-5-1 §8.3)**" 표제 하에 다음을 §8.3 근거로 제시:
> "- **Critical (CVSS ≥9.0)**: 인지 후 72시간 이내 긴급 패치 또는 완화조치 배포
>  - **High (CVSS 7.0–8.9)**: 14일 이내
>  - **Medium (CVSS 4.0–6.9)**: 정기 업데이트 주기에 포함"

→ 마치 IEC 81001-5-1 §8.3이 CVSS 등급별 **정량 기한**(72h/14d)을 직접 규정한 것처럼 인용.

## 독립 확인 결과 — 1차/공신력 출처

| 사항 | 문서 기재 (귀속) | 독립 확인 정답 |
|---|---|---|
| IEC 81001-5-1:2021 §8.3 의 정량 기한 규정 여부 | "Critical 72시간 / High 14일 / Medium 정기" | **§8.3는 CVSS 기반 정량기한을 직접 규정하지 않는다.** 표준 본문은 *Timeliness is driven by authorities, applicable legislation, regulatory policy, product safety, and market forces* 라고 일반원칙만 명시. CVSS 기준의 72h/14d는 산업 관행·외부 가이드(예: NIS2, FDA 사이버보안 가이드, CISA KEV 권고) 또는 자사 정책에서 도출되는 것이지 본 조항이 명시한 수치가 아님 |

## 판정
- **인용 부정확 (citation)** — 정량 기한(숫자) 자체는 산업적으로 합리적이나, **출처를 IEC 81001-5-1 §8.3에 귀속**시킨 것이 부정확. 외부 심사·고객 질의 시 표준 본문에서 동일 수치를 찾을 수 없음.
- 영향 P1: 운영 기한 자체는 보수적이라 안전성 영향은 적지만, 규제·인증 문서의 traceability(근거 추적)가 흔들림.

## 권고 수정
1. 표제와 본문에서 출처 귀속을 분리·명시:
   - 변경 전: `5.6.3 사이버보안 긴급 패치 (IEC 81001-5-1 §8.3)`
   - 변경 후: `5.6.3 사이버보안 긴급 패치 (IEC 81001-5-1 §8 취약점 관리; 정량 기한은 자사 정책)`
2. 정량 기한의 근거를 본 SOP의 자사 사이버보안 정책(또는 SOP-CVD-001/IEC 81001-5-1 §8 일반 원칙 + 자사 결정)로 명확히 귀속.
3. (선택) 참고 외부 기준(FDA "Cybersecurity in Medical Devices" 가이드, NIS2 등) URL을 별도 라인에 각주로.

## 출처 (공식 1차)
- IEC 81001-5-1:2021 본문 발췌: https://mdcpp.com/doc/standard/IEC%2081001-5-1-2021.pdf (§8 vulnerability management — 일반원칙·timeliness 정성서술)
- 표준 개요(해석): https://blog.cm-dm.com/post/2024/02/23/IEC-81001-5-1-Right-Here-Right-Now

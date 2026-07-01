---
title: "[AUDIT P0] PMS_개요 v0.2 §6 표 — 'EU 사망·심각한 건강 위협 2일 이내' 사실오류 (정답: 사망/심각한 건강 악화 = 10일, 공중보건 심각한 위협 = 2일)"
labels: "audit:factuality,prio:P0,risk:high"
state: closed
closed-date: 2026-07-02
closed-by: holee9-builder
closed-summary: |
  08_시판후_감시_PMS/PMS_개요.md v0.3 §6·§6.1: EU MDR Art.87(2)공중보건위협 2일 / 87(3)사망 10일 / 87(4)기타 15일 3버킷 분리
---

## 대상 문서
- `08_시판후_감시_PMS/PMS_개요.md` (doc-id: PMS_개요, type: Overview, version: v0.2, last-review: 2026-05-02)
- 위치: §6 "보고 기한 (주요국 비교)" 표 EU 행 "중대 부작용" 열

## 주장 (기재값)
> | **EU** | 15일 (사망·심각한 건강 위협은 **2일 이내**) | 경향 보고 | PSUR — Class IIa: 최소 2년마다 갱신 |

즉 EU MDR 2017/745의 사망/중대 사건 보고기한을 **2일 이내**로 인용. ("사망"과 "심각한 건강 위협"을 동일 2일 버킷에 묶음.)

## Tier 1 정답
Regulation (EU) 2017/745 Article 87 — Reporting of serious incidents and field safety corrective actions:
- **Art. 87(2)** — *Serious public health threat*(공중보건에 대한 심각한 위협): **즉시, 늦어도 인지 후 2일 이내**
- **Art. 87(3)** — *Death or an unanticipated serious deterioration in a person's state of health*(사망 또는 사람의 건강상태의 예상되지 않는 심각한 악화): **즉시, 늦어도 인지 후 10일 이내**
- **Art. 87(4)** — *Other serious incidents*(그 외 심각한 사건): **늦어도 인지 후 15일 이내**

즉 "사망"은 **10일 버킷**(Art. 87(3))이며, **공중보건에 대한 심각한 위협**만이 **2일 버킷**(Art. 87(2))이다. 본 문서는 두 버킷을 하나로 묶고 "사망"을 2일로 처리하여 사실관계를 왜곡.

## 판정
**사실오류 (P0, audit:factuality)** — 보고기한 수치 사실오류. 본 문서대로 운영하면 법정 기한(10일)을 잘못 단축 적용(2일)하는 결과 — 운영 보수성은 높으나 인용 사실 자체는 불일치. audit #903/#904(SOP-PMS-001 EU/FDA 보고기한 사실오류)와 동일 패턴의 자매문서 재발.

## Tier 1 출처
- EUR-Lex — Regulation (EU) 2017/745: https://eur-lex.europa.eu/eli/reg/2017/745/oj/eng
- (보조) Medical Device HQ — MDR Article 87 요약: https://medicaldevicehq.com/documentation/mdr-article-87-reporting-of-serious-incidents/

## 권고
EU 행을 3개 버킷으로 분리:
```
| **EU** | 사망/예기치 않은 심각한 건강 악화: 10일(Art.87(3))
          공중보건 심각한 위협: 2일(Art.87(2))
          기타 심각 사건: 15일(Art.87(4)) | 경향 보고 | PSUR — IIa: 최소 2년 / IIb·III: 연 1회 |
```
또한 §6.1 표 "X-ray 튜브 파열" 행 "EU 2일 / KR 7일" 인용도 Art. 87(2)에 해당하는지 시나리오 재판정 필요(과피폭이 단일 환자 위해라면 87(3) 10일, 광범위 공중보건 위협 수준일 때만 87(2) 2일).

## 비고
실운영 문서 미참고. 빌더의 자체 ✅ 신뢰 배제, EUR-Lex 1차 본문 기반 독립 재확인. 자매 SOP-PMS-001(v0.3) §6 보고기한 표도 audit #903 정정 이후 본 문서와 일치 확인 권고.

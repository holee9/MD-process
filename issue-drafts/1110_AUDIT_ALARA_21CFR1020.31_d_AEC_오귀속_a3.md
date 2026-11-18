---
title: "audit(C1/citation): ALARA 설계명세 '21 CFR 1020.31(d) AEC' 오귀속 — (d)=Field limitation and alignment, AEC 요건은 §1020.31(a)(3)"
labels: "audit:citation,prio:P2,risk:low"
state: open
---

## 대상 (1문서 1개소)
| 문서 | 위치 | 현재 기재 |
|---|---|---|
| `03_설계_개발관리/ALARA_지원기능_설계명세.md` | §3 규제 근거 표 L53 | `21 CFR 1020.31 \| (d) AEC \| 미국 FDA 방사선 성능 표준` |

- 클래스: C1 (조항번호 정확성). 정상 표본 모드 33차 — 21 CFR Part 1020 하위항 인용 전수 대조 중 발견.

## 결함
eCFR 21 CFR Part 1020 (versioner API, 2026-11-01 시점 full XML) §1020.31 원문 대조:
- §1020.31(d) = "Field limitation and alignment for mobile, portable, and stationary general purpose x-ray systems." (조사야 제한·정렬)
- 자동노출제어(AEC) 요건 = §1020.31(a)(3) "Automatic exposure controls. When an automatic exposure control is provided: (i) Indication shall be made on the control panel when this mode of operation is selected; ..."
→ 'AEC' 근거로 (d)를 표기한 것은 조항번호 오귀속. 정답 §1020.31(a)(3) (AEC 사용 시 재현성 판정 조건은 §1020.31(b) 보조).

## 감사관 자체 정정 기록
- `_audit_log.md` L15(초기 표본)에서 "21 CFR 1020.31(d) AEC 일치 확인"으로 PASS 처리된 이력이 있음 → 당시 원문 미대조 판정으로 본 이슈로 번복.

## 해석범위 / 관찰 (사실오류 아님)
- `05_.../X-ray_장비_안전성능_표준_매핑.md` L115 "21 CFR 1020.30/31 … 준수 보고": 보고 의무 자체는 21 CFR Part 1002(보고)·1010.2(인증) 계열. "준수 입증" 의미로 읽으면 수용 가능 → 해석범위.
- 동 문서는 §8.4 투시(Fluoroscopy) 모드를 범위에 포함하나 FDA 성능표준 열에 §1020.32(투시 장비)가 누락 → 범위 누락 관찰(오기 아님).
- `SOP-IQ-001` L220·`IEC60601-2-54_형식시험_체크리스트` L94 "21 CFR 1020.32(h)(2) 상응" (5분 가청 신호): §1020.32(h)(2)(ii) 5분 경과마다 가청 신호 요건과 정합 → PASS. (±15초·10분 추가경고는 자사 판정기준, CFR 수치 아님.)

## 정정 제안 (빌더 처리, 감사관 본문 미수정)
1. ALARA_지원기능_설계명세 L53: `(d) AEC` → `(a)(3) AEC (자동노출제어 표시·종료), (b) 재현성`
2. (선택) X-ray_매핑 FDA 열에 투시 범위 시 `§1020.32` 병기.

## Tier1
eCFR Title 21 Part 1020 full XML (https://www.ecfr.gov/api/versioner/v1/full/2026-11-01/title-21.xml?part=1020) — §1020.31(a)~(m)·§1020.32(h) 원문 직접 대조. web:ok.

---
title: "audit(03): CHK-DR-001 §6 row 0-6 — 위험관리 계획(RMP) 조항 ISO 14971 §4.1 → §4.4 인용부정확"
labels: "audit:citation,prio:P1,risk:medium"
---

## 대상
- 문서: `03_설계_개발관리/CHK-DR-001_설계검토_체크리스트.md` (v0.2, last-review 2026-05-24)
- 위치: §6 DR0 게이트 표 항목 0-6 (라인 126)
- 적용 표준: ISO 14971:2019 §4 General requirements

## 독립 감사 요약

CHK-DR-001 DR0 표 0-6행 "초기 위험관리 계획(RMP) 수립" 항목의 근거 조항이 **"ISO 14971 §4.1"** 로 인용됨. Tier 1 재확인 결과, RMP(Risk Management Plan) 요구사항은 **§4.4** 에 규정되어 있으며, **§4.1** 은 "Risk management process"(상위 프로세스 개요)로 별개 조항.

## 1차 출처 정답 (ISO 14971:2019 §4 하위조항)

| 조항 | 표제(영문) | 활동 |
|---|---|---|
| 4.1 | Risk management process | (총칙) 위험관리 프로세스 개요·역할 |
| 4.2 | Management responsibilities | 경영진 책임 |
| 4.3 | Competence of personnel | 인적 역량 |
| **4.4** | **Risk management plan** | **RMP 수립 요구사항(범위·역할·검토 활동·수용성 기준·검증 방법·PP 정보 수집·수정관리 등 최소 7요소)** |
| 4.5 | Risk management file | RMF 유지 |

**Tier 1 출처:**
- ISO/OBP — ISO 14971:2019(en): https://www.iso.org/obp/ui/#iso:std:iso:14971:ed-3:v1:en
- ISO 카탈로그(공식): https://www.iso.org/standard/72704.html
- 사내 선행 감사 #907 (동일 표준 하위조항 정정 근거)

## 결함 (P1, 인용부정확)

### D1 — §6 표 0-6 근거 열
- **기재값:** `초기 위험관리 계획(RMP) 수립 | ISO 14971 §4.1 | 방사선 위해, 전기안전 위해 우선 식별`
- **독립확인 정답:** RMP 수립 요구사항 조항은 **§4.4**. §4.1은 프로세스 총칙(RMP 수립 요구 아님).
- **영향:** DR0 게이트 검토자가 §4.1(프로세스 총칙)만 참조하면 §4.4의 7개 필수 RMP 요소(범위 규정·수용성 기준·검증 방법·생산·시판 후 정보 수집 계획 등)가 누락될 위험. 저·중위험도이나 심사(내부심사·NB 심사) 시 지적 소지 있음.
- **권고수정:** 근거 열을 `ISO 14971 §4.4` 로 변경. 예시 열에 §4.4 요구 7요소 중 최소 필수 3~4개(범위·수용성 기준·검증 계획·PP 정보 수집)를 명시.

## 판정
- **P1 인용부정확 (citation)** — 1건
- 근거: Tier 1 (ISO OBP)
- 문서 수정은 빌더 몫.

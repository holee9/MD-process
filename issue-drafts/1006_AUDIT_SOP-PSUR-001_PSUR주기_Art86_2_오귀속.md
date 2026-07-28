---
title: "audit(factuality): SOP-PSUR-001 §5.1 — Class IIb/III PSUR 연 1회 근거 Art.86(2) 오귀속 (정답: Art.86(1))"
labels: "audit:factuality,prio:P1,risk:medium"
state: closed
---

## 요약 (audit #1006, C2×08 전수 스윕)
`08_시판후_감시_PMS/SOP-PSUR-001_정기안전성보고_PMCF_절차.md` §4 빈도 표(L67~68)가 Class IIb·III PSUR "최소 연 1회"의 근거를 **EU MDR Art.86(2)**로 오귀속.

## Tier1 근거
EU MDR 2017/745 Art.86 원문:
- **Art.86(1)**: PSUR 갱신주기 규정 — Class IIb·III **연 1회 이상**, Class IIa **최소 2년마다** (전부 (1)항 소속)
- **Art.86(2)**: Class III·이식형 기기의 **NB 전자시스템(Art.92) 제출 의무** — 갱신주기 조항 아님
- Art.86(3): 그 외 기기는 NB 열람 제공·당국 요청 시 제출

## 지적 사항
- L67: `Class IIb (진단용 X-ray) | 최소 연 1회 | EU MDR Art.86(2)` → 정답 **Art.86(1)**
- L68: `Class III (해당 시) | 최소 연 1회 | EU MDR Art.86(2)` → 정답 **Art.86(1)** (제출경로는 Art.86(2) 별도)
- L69 IIa=Art.86(1)은 정확. 주기 수치 자체(연1회/2년)는 전부 정확 — 조항 오귀속만 결함.

## 계보
audit #1004(TF-TD-001 PSUR 주기)에서 Art.86(1)=주기 조항 Tier1 기확정. C1×08(2026-07-19) 사이클은 "Art.86(1)(2) PASS"로 기록했으나 본 표의 (2) 귀속을 놓침(재발·감사 누락 정정).

## 조치 제안 (빌더)
L67~68 근거를 Art.86(1)로 정정, 필요 시 Class III 행에 "NB 제출: Art.86(2)" 별도 주석.

*독립 감사: 문서 수정 없음, 이슈 등록만. 실운영 문서 미참고.*

## 해소 (2026-07-29, 드레인 스프린트)
- SOP-PSUR-001 §5.1: Class IIb·III 연 1회 근거 'Art.86(2)' → 'Art.86(1)' 정정(2행), 'Art.86(1)(2) 공통' → 갱신의무(86(1))/NB 전자제출(86(2)) 분리 표기, #912 정정 노트의 조항 귀속도 동반 정정(v0.3.1).
- 전 저장소 grep: 본문 내 Art.86(2) 오귀속 잔존 0건(감사원장 기록 제외). Tier1: Art.86(1)(#1004 재사용). 실운영 문서 미참고.

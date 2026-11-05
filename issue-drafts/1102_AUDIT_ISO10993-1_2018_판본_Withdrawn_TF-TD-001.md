---
title: "[audit:currency] ISO 10993-1:2018 — iso.org 상 Withdrawn(Edition 5) 판본을 현행 기준으로 인용 (TF-TD-001 L687, 1문서 1개소)"
labels: "audit:currency,prio:P2,risk:medium"
state: open
---

## 배경 (C3 표준 판본 · 표본 24차, 2026-11-05)
`06_문서_기록관리/TF-TD-001_의료기기파일_기술문서_관리.md` L687 표: `생체적합성 | ISO 10993-1:2018 + 시리즈`.

## Tier1 근거
iso.org 표준 페이지 https://www.iso.org/standard/68936.html (ISO 10993-1:2018, Edition 5, 2018-08): 상태 표기 **"Withdrawn"** / "Withdrawn (Edition 5, 2018)" (web:ok 직접 열람). 동 페이지 FAQ는 제6판이 ISO 14971에 맞춰 전면 개편되었다고 기술하나, 대체 판본의 발행일·정확한 표기는 본 실행에서 Tier1 미회수 → **대체 판본 표기(예: :2025)는 미확인**.

## 결함
저장소가 withdrawn 판본(2018)을 현행 정합 표준으로 단정 인용. 판본 연도 고정 표기는 노후(currency) 결함.
정정 방향(문서 수정은 빌더 몫): 판본 연도 삭제 또는 iso.org Tier1 확인 후 현행 판본으로 갱신, 그리고 EU 조화표준(EN ISO 10993-1) 및 FDA 인정 판본 여부는 별도 Tier1 확인.

## 비결함(확인)
`GSPR_정합표준_매핑표.md` L78, `GSPR_체크리스트_v0.2` L41, `T-FDA510K-C2` L27/65는 연도 없는 'ISO 10993-1' 표기 → 판본 결함 없음.

## 판정
P2/risk:medium. 실운영 문서 미참고.

---
title: "audit(currency): GSPR_정합표준_매핑표 §23.1 — 철회 표준 EN 1041:2008+A1:2013을 MDR 정합표준 'H'로 인용"
labels: "audit:currency,prio:P2,risk:low"
state: open
opened: 2026-07-30
---

## 대상 (C3×01_법규_규제 전수 스윕)

`01_법규_규제/04_유럽_MDR/GSPR_정합표준_매핑표.md` L98 (GSPR §23.1):

> | §23.1 | 라벨·사용설명서 일반 | EN ISO 15223-1:2021; EN 1041:2008+A1:2013 | H | ...

## 결함

EN 1041:2008+A1:2013은 **MDD 시대 표준으로, EN ISO 20417:2021이 대체(supersede)하여 철회(withdrawn)** 상태. MDR 정합표준 목록(Decision (EU) 2021/1182 및 개정)에 등재된 적 없음 — 'H' 표기 오류. 동일 문서 §23.2/§23.3은 이미 EN ISO 20417:2021을 올바르게 인용하고 있어 §23.1 행만 구표준 잔존(내부 불일치).

## 근거

- EN ISO 20417:2021 유럽 서문: "This document supersedes EN 1041:2008+A1:2013" (CEN 발행 기록, BSI/genorma 공개 서문 대조). 대체·철회 사실은 표준 자체 서문 기재 사항.
- 보조(Tier2): Emergo, Greenlight Guru, Johner Institute — EN 1041 철회·ISO 20417 대체 일치 서술.

## 판정

P2/risk:low — 철회 표준 인용 + 'H' 상태 오표기. 1문서 1개소. 정정 방향: EN 1041 삭제, EN ISO 20417:2021로 통일.

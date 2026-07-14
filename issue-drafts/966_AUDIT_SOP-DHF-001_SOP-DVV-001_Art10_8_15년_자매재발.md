---
title: "audit(C1): SOP-DHF-001·SOP-DVV-001 'EU MDR Art.10(8) 단종 후 15년' 사실오류 — 비이식형 정답 10년, audit #914/#963 자매재발 잔존 3개소"
labels: "audit:factuality,prio:P0,risk:high"
state: closed
closed: 2026-07-15
---

## 대상
- `03_설계_개발관리/SOP-DHF-001_설계개발파일_관리.md` L170("제품 단종 후 최소 15년 보존 (EU MDR Art.10 §8)"), L307(보존기간 표 "단종 후 15년 이상 | EU MDR Art.10 §8")
- `03_설계_개발관리/SOP-DVV-001_설계개발_검증_및_유효성확인_절차.md` L152("단종 후 15년(EU MDR Article 10(8))")
- 클래스: C1 (조항 부속 수치) — C1×04 사이클 중 03 잔존분 확인

## 결함
MDR 2017/745 Art.10(8): 기술문서 보관 "최소 10년", **이식형에 한해 15년**. 자사 X-ray(비이식형) 정답 **10년**. audit #914(SOP-PSUR-001)·#963(F-DVV-001)과 동일 조항·동일 오류 — grep 전수 재검색으로 잔존 3개소 확인(#963 권고사항 이행 결과).

## Tier1
EUR-Lex CELEX 02017R0745(consolidated) Art.10(8) 원문 직접 열람(Chrome).

## 판정
P0, 3개소. 해석범위 아님. 감사관은 본문 미수정(정정은 빌더 몫). 실운영 문서 미참고. web_verification: yes.

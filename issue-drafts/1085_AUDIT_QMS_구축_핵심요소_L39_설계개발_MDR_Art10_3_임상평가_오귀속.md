---
title: "audit(citation): QMS_구축_핵심요소 §3.1 L39 '설계 개발 ↔ EU MDR Art.10(3)' 오귀속 — Art.10(3)=임상평가, 기술문서(Annex II)=Art.10(4)"
labels: "audit:citation,prio:P2,risk:low,qms"
opened: 2026-09-30
state: closed
---

## 대상 (표본 모드 3차 — 이월 리드 (d) Tier1 대조 결과)

| # | 파일 | 라인 | 표기 |
|---|---|---|---|
| 1 | `02_품질경영시스템_QMS/QMS_구축_핵심요소.md` | L39 | 설계 개발 행 — EU MDR 열 `Art.10(3), Annex II` |

저장소 전수 grep(01~10·11·12·00): `Art.10(3)` 인용은 위 1개소뿐 — 확산 0건.

## 결함

Regulation (EU) 2017/745 Art.10 원문 대조(medical-device-regulation.eu 전문 + EUR-Lex 통합본 2025-01-10 요약 일치):

- Art.10(2) = 위험관리시스템(Annex I §3)
- **Art.10(3) = 임상평가(Art.61, Annex XIV, PMCF)** ← 문서가 '설계 개발'에 귀속
- **Art.10(4) = 기술문서 작성·갱신(Annex II·III)**
- Art.10(9) = QMS(설계·개발은 (a)~(m) 요소 내 포함)

'설계 개발' 행의 정답 후보: `Art.10(4), Annex II`(및 Art.10(9)). Annex II 병기는 정확하나 Art.10(3)은 임상평가 조항으로 설계개발과 무관 → C1 조항번호 오귀속(P2).

## 증거 등급

- Tier1: EUR-Lex CELEX 02017R0745-20250110 — Art.10 본문은 fetch 도구 요약 수준 교차확인(Art.10 전문 verbatim 미회수).
- 보조(Tier2, 범위만): medical-device-regulation.eu 전문 열람 — 문단 구조 일치.
- 판정 신뢰도: 문단 구성(2=위험관리, 3=임상평가, 4=기술문서)은 두 소스 일치. EUR-Lex verbatim 재확인은 차기 사이클 권고.

## 권고 (감사관은 문서 수정 안 함)

L39 EU MDR 열을 `Art.10(4), Annex II (+Art.10(9))`로 정정 검토.

---

## 종결 (2026-10-01, audit-drain 스프린트)

- `QMS_구축_핵심요소.md` L39 EU MDR 열 `Art.10(3), Annex II` → `Art.10(4), Annex II (+Art.10(9))` 정정 (Art.10(3)=임상평가, (4)=기술문서, (9)=QMS).
- 동일 클래스 전수 grep(`Art.10(3)` 등, 이슈드래프트·시점기록 제외): 잔여 0건.
- 증거: Reg.(EU) 2017/745 Art.10 문단 구조(2=위험관리, 3=임상평가, 4=기술문서, 9=QMS). EUR-Lex verbatim 미회수분은 범위 표기 유지.

실운영 문서 미참고.

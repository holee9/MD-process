---
title: "audit(citation): GSPR_정합표준_매핑표 §16 방사선 방호 — IEC 62667(광이온빔 치료장비 표준) 무관 인용"
labels: "audit:citation,prio:P1,risk:med"
state: open
opened: 2026-07-30
---

## 대상 (C3×01_법규_규제 전수 스윕)

`01_법규_규제/04_유럽_MDR/GSPR_정합표준_매핑표.md` L85 (Chapter II 표, GSPR §16 방사선 방호):

> | **§16** | **방사선 방호** | **EN 60601-1-3:2008/A1:2013/A2:2021; IEC 62667** | **H** | ...

## 결함

IEC 62667:2017의 실제 표제는 **"Medical electrical equipment — Medical light ion beam equipment — Performance characteristics"** — 10~500 MeV/n **광이온빔(양성자/탄소이온) 치료장비**의 성능 특성 표준으로, 진단용 X-ray 방사선 방호와 무관. 자사 제품군(X-ray FPD/System/SaMD)에 적용 불가한 표준을 GSPR §16 정합표준(그것도 'H')으로 인용.

추정 원인: 방사선 방호 관련 다른 표준(예: IEC 60601-1-3 계열로 충분)과의 번호 혼동 또는 임의 삽입. Tier1 기준 §16에 IEC 62667을 매핑할 근거 전무.

## Tier1/근거

- IEC 62667:2017 표제·적용범위 — IEC 발행 기록(ANSI webstore·AFNOR·SIS 등 공식 유통채널 기재 표제 일치, In Compliance Mag 발행 공지 교차).

## 판정

P1/risk:med — 무관(사실상 미존재급) 인용, NB 심사 시 신뢰도 훼손 소지. 1문서 1개소.

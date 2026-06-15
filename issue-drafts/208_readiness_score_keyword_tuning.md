---
title: "[P2][consistency] build_readiness.py — ISO 13485 점수 과대평가 보정 (키워드 세분화)"
labels: "source:emergent,prio:P2,type:consistency,risk:med"
log-ref: CRV-2026-06-15-ISO13485-CHK
---

## 배경

`build_readiness.py`가 `applicable_keywords: [ISO 13485]`를 전체 문서 applicable과 매칭하여
ISO 13485 준비도를 100%로 과대평가. 실제 미충족 9개 must 항목이 "충족"으로 계산됨.

## 원인

키워드가 표준명(ISO 13485) 수준이어서 조항 수준 추적 불가.
unmet 항목에 `related_docs: []`로 문서 ID가 없어 evidence 없는 항목도 매칭.

## Definition of Done

- [ ] 체크리스트 항목에 `related_docs` 필드 추가(미충족 항목은 `[]`)
- [ ] 스크립트에서 `status: unmet` 항목은 score=0으로 우선 처리하는 로직 추가
  또는 `applicable_keywords`에 `ISO 13485 §4.2.2` 수준 세분화
- [ ] 재실행 후 ISO 13485 점수 60~75% 범위로 현실 반영

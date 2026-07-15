---
title: "audit(C1): SOP-VAL-001 — '밸리데이션 = IEC 62304 §5.8' 오귀속(§5.8=Software release, SW 밸리데이션은 62304 적용범위 밖) 2개소"
labels: "audit:factuality,prio:P0,risk:medium"
state: closed
---

## 대상
- `05_검사_시험_밸리데이션/SOP-VAL-001_SW_검증_밸리데이션_절차.md`
  - L66(§3 용어정의 표 "밸리데이션(Validation) | 의도된 용도에 대한 적합성 확인 (IEC 62304 §5.8)")
  - L231(§5.5 헤더 "### 5.5 SW 밸리데이션 (IEC 62304 §5.8)")
- 클래스: C1 (조항번호/주제 귀속)

## 결함
IEC 62304:2006+AMD1:2015 §5.8 = **Software release**(계획활동 완료·버전 정합·잔여 이상 평가 후 릴리스). '의도된 용도 적합성 확인(validation)'은 **IEC 62304의 적용범위에 포함되지 않음** — 시스템/기기 레벨 밸리데이션은 ISO 13485 §7.3.7 및 FDA 소프트웨어 밸리데이션 원칙 영역. §5.5(단위 구현·검증)/§5.6(통합·통합시험)/§5.7(시스템시험) 인용은 정확(PASS)하나, validation을 §5.8에 귀속한 2개소는 오귀속.

## Tier1
IEC 62304 Ed.1.1(2015-06 consolidated) 조항 구조 — §5.8 'SOFTWARE RELEASE' 제목 및 표준 적용범위(validation 미포함) 확인. (표준 전문 유료 — 조항 제목·범위는 공개 TOC·통합본으로 확인, 조항 제목 수준의 확정)

## 판정
P0(절차서 용어정의의 규격 근거 오귀속), 2개소. 해석범위 아님. 감사관 본문 미수정. 실운영 문서 미참고. web_verification: yes.


## 처리 결과 (2026-07-16)
- `05_검사_시험_밸리데이션/SOP-VAL-001_SW_검증_밸리데이션_절차.md` L66/L231 2개소 정정 완료.
  - L66 용어정의: "밸리데이션(Validation) | 의도된 용도에 대한 적합성 확인 (IEC 62304 §5.8)" → "(ISO 13485:2016 §7.3.7 / IEC 62304 적용범위 밖 — §5.8은 Software release)"로 정정.
  - L231 헤더: "### 5.5 SW 밸리데이션 (IEC 62304 §5.8)" → "### 5.5 SW 밸리데이션 (ISO 13485:2016 §7.3.7 — IEC 62304 적용범위 밖, §5.8은 Software release와 별개)"로 정정.
- Tier1 재확인: IEC 62304:2006+AMD1:2015 Clause 5 구조 — §5.5 Unit Implementation/Verification, §5.6 Integration/Integration Testing, §5.7 System Testing, §5.8 Software Release. Validation(의도된 용도 적합성 확인)은 62304 범위 밖(WebSearch: jamasoftware.com, openregulatory.com 조항 제목 교차확인).
- 동일 클래스 일괄 점검: 전 저장소 §5.8 인용 전수 검토 — SOP-DT-001·SOP-DVV-001·SOP-MFG-001 등의 §5.8 인용은 모두 "SW 릴리스/빌드" 맥락으로 정확(PASS), validation 오귀속 추가 잔존 없음.
- 실운영 문서 미참고.

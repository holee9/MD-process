---
title: "audit(01): GSPR_정합표준_매핑표 v0.3 §5 매핑 표 — MDR Annex I §19 주제 오인 (기재: '무선·전자기기(EMC)' / 정답: 'Particular requirements for active implantable devices')"
labels: "audit:citation,prio:P1,risk:high"
state: closed
---

## 대상
- 문서: `01_법규_규제/04_유럽_MDR/GSPR_정합표준_매핑표.md` v0.3 (last-review 2026-06-28)
- 위치: §5 "매핑표" — 라인 89 부근 `| §19 | 무선·전자기기 | EN 60601-1-2:2014/A1:2020 (EMC); RED 2014/53/EU | H | EMC 시험: X-ray 발생 시 전자기 간섭, WiFi/BT 모듈 |`

## 독립 감사 요약

GSPR_정합표준_매핑표는 EU MDR 2017/745 Annex I(GSPR)의 각 조항에 정합표준을 매핑하는 핵심 참조문서. **§19의 주제를 "무선·전자기기(EMC)"로 표기**하고 있으나, Tier 1 재확인 결과 **Annex I §19의 정확한 주제는 "Particular requirements for active implantable devices"** (활성 이식형 의료기기 특수요구사항). 자사 취급 품목(디지털 X-ray FPD, X-ray System, 영상처리 SaMD)은 **모두 비이식형(non-implantable)** 이므로 실무적으로 §19는 **applicable=Not Applicable** 처리되어야 하며, 대신 별도 §17(전자프로그래머블 시스템) 또는 §14(환경·상호작용) 항목이 EMC/무선 대응처가 됨.

## 1차 출처 정답 (Tier 1)

- **EUR-Lex — Regulation (EU) 2017/745, Annex I Chapter II**:
  - §14 Construction of devices and interaction with their environment (EMC/환경 대응)
  - §16 Protection against radiation (방사선 방호 — 이미 §16 행이 doc 본문에 정합 매핑됨)
  - §17 Electronic programmable systems / devices that incorporate electronic programmable systems and software that are devices in themselves — **§17.1 EMC/신뢰성 요구, §17.2 SW 개발수명주기·정보보안, §17.4 IT security minimum requirements**
  - **§19 Particular requirements for active implantable devices** — 19.1 에너지원·유지보수·상호작용 위험 최소화 / 19.3 부품 식별성 / 19.4 수술 없이 판독 가능한 코드
  - §20 Protection against mechanical and thermal risks
- MDR Annex I 텍스트 재확인: https://eur-lex.europa.eu/eli/reg/2017/745/oj/eng
- 참고 인용: medical-device-regulation.eu Annex I 요약 (Tier 2 보조 확인용): https://www.medical-device-regulation.eu/2019/07/23/annex-i-general-safety-and-performance-requirements/

## 결함 (P1, 인용부정확 / 부분 사실오류)

### D1 — §5 매핑표 §19 행 (라인 89)
- **기재값:**
  > `| §19 | 무선·전자기기 | EN 60601-1-2:2014/A1:2020 (EMC); RED 2014/53/EU | H | EMC 시험: X-ray 발생 시 전자기 간섭, WiFi/BT 모듈 |`
- **오류 유형:** §19 조항 주제 오인 → **인용부정확 (citation)** + 부분적 **사실오류** (Annex I §19는 이식형 특수요구, EMC가 아님).
- **정답:**
  - **§19 행:** `| §19 | Particular requirements for active implantable devices | Not Applicable (자사 취급 품목 비이식형) | — | 자사 X-ray FPD·System·SaMD는 이식형 아님. §19 미적용 사유 서면화(GSPR 체크리스트 N/A 근거). |`
  - **EMC/무선 관련 매핑은 §17(및 필요시 §14) 하위로 이동:** `| §17.1/17.2 | 전자프로그래머블 시스템 — EMC·SW 수명주기 | IEC 60601-1-2:2014/A1:2020, IEC 62304:2006+AMD1:2015 | H | EMC 시험(전자기 간섭), SW SDLC |` — 이미 §17이 별도 행에 있는지 확인 후 통합/신설.
- **영향:**
  - **감사·인증 리스크**: NB(Notified Body)/BSI 등이 GSPR 체크리스트 확인 시 §19 대응근거로 IEC 60601-1-2 (EMC 표준)이 매핑되면 근거불일치로 관찰사항(observation) 가능. 반면 §19가 실제로 Not Applicable로 처리되지 않으면 이식형 요구사항을 놓친 것으로 오인될 수 있음.
  - **GSPR 체크리스트 (F-GSPR-MAP-001) 파생 오류**: 이 매핑표를 근거로 체크리스트가 생성될 시 §19 항목이 EMC 항목으로 오분류되어 실제 §19의 N/A 근거 서면화가 누락될 수 있음.

## 참고 (Cross-Ref) — 동일 문서 §5 매핑표 부수 검토
- **§16 "방사선 방호" ↔ EN 60601-1-3:2008/A1:2013/A2:2021** — Annex I §16(방사선 방호) 정합 (PASS 별기록, Tier 1 EUR-Lex Annex I).
- **§17.1 "전자프로그래머블 시스템"** — 상단 매핑에 존재 여부 재확인 필요(§19에 오배치되었다면 §17에서 미커버 소지).
- **§21 "방사선 발생 기기 ↔ EN 60601-2-54:2022"** — Annex I §21 실제 주제는 "Protection against the risks posed to the patient or user by devices that supply energy or substances"(에너지·물질 공급 기기 위험 방호)로, X-ray 에너지 공급은 §21에 논리적 포함되나 방사선 특수요구는 §16이 주 조항. **§21에 X-ray 전용 매핑을 두는 것은 §16과의 중복·경쟁 가능**하므로 별도 감사 검토 필요(본 이슈에서는 미확인, 1차 원문 세밀검토 필요).

## 재발 방지

- **Plan #935 확장 매칭룰**에 EU MDR Annex I 조항 표제(§19=Active implantable 등) 대응표 등록. §5·§6 GSPR 매핑 표의 "조항 → 주제" 대조검증 자동화.
- **F-GSPR-MAP-001 체크리스트** 재생성 시 §19 N/A 근거 서면 슬롯 신설.

## 판정
- **P1 인용부정확 + 부분 사실오류 (§19 주제 오인)**
- 근거: EUR-Lex Regulation (EU) 2017/745 Annex I §19 원문 (Tier 1)
- 문서 수정은 빌더 몫.

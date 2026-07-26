---
title: "audit(citation): IEC 60601-2-54 kVp/AEC/투시경보 조항번호 문서 간 3중 모순(§203.6 vs §201.12.1 vs §201.6 등) + IEC 60601-1-3 '§29.201' 판본 혼재 의심 — 원문 유료로 정답 미확인"
labels: "audit:citation,prio:P1,risk:medium"
state: closed
---

## 대상 (C1×05 전수 스윕 중 발견한 상호모순 클러스터)
**관전압(kVp) 정확도 — 동일 파라미터에 3개 조항번호·3개 역치:**
- `검사_시험_밸리데이션_개요.md` L107: "IEC 60601-2-54 §203.6, ±5%"
- `IEC60601-2-54_형식시험_체크리스트.md` L77: "§201.12.1, ±10%"
- `X-ray_장비_안전성능_표준_매핑.md` L168: "§201.12.1, ±10%"
- `SOP-IQ-001` L180: "§201.6, ±5%" / L196(AT-R01): "§201.6, ±2%"
- `SOP-CAL-001` L177: "§201.6, ±2%"

**AEC — 3개 조항번호:** 체크리스트 L81-82 "§203.7.8" vs SOP-IQ L199 "§201.12" vs 검사개요 L110 "§203.7"
**투시 시간 경보(5분):** 체크리스트 L92 "§203.8.102" vs SOP-IQ L218(AT-F06) "§203.4"
**IEC 60601-1-3 누설선량:** 체크리스트 L65 "§29.201" — Ed.1(1994) 계열 조항번호로 추정되며, 동일 문서군의 Ed.2 구조 인용("§7" HVL, L66·L169·L202)과 판본 혼재 의심(C3 연계).

## 결함
표준 원문(IEC Webstore 유료) 미확보로 **어느 표기가 정답인지는 미확인**. 그러나 동일 파라미터에 대해 서로 다른 조항번호가 병존하므로 **최소 일부는 필연적으로 오류**(논리적 모순) — 인용 무결성 결함으로 등록. 역치 차이(±2/±5/±10%)는 시험 단계별(형식시험 vs 수용시험 vs 계측기 교정) 상이 기준일 가능성이 있어 C2에서 별도 판단.

## Tier1
미확보(web:attempted-paywalled). 모순 판정은 저장소 내 교차대조에 근거(우아한 저하).

## 판정
P1. 정답 확정은 표준 원문 확보 후 후속(빌더: IEC 60601-2-54:2022 원문 대조로 단일화 권고). 감사관 본문 미수정. 실운영 문서 미참고.

## 재확인 시도 (2026-07-16)
- WebSearch로 IEC 60601-2-54 §201.12.1/§203.6/§201.6 clause 특정 재시도 — 검색 결과에 표준 원문 발췌 없음(반환된 링크는 IEC 60601-2-25/-2-60/-2-24/-2-34 등 무관 표준). 신뢰 가능한 Tier1/Tier2 1차 인용 미확보.
- **판정 유지: 미확인.** 추정 배제 원칙에 따라 5개 문서(검사_시험_밸리데이션_개요·IEC60601-2-54_형식시험_체크리스트·X-ray_장비_안전성능_표준_매핑·SOP-IQ-001·SOP-CAL-001)의 조항번호는 임의 수정하지 않음(수정 시 미확인 값 기재 위험이 실제 오류보다 큼).
- **상태: open 유지.** 해소 조건 — IEC 60601-2-54:2022 원문(유료) 구매·직접 대조 후 단일 조항번호로 일원화. 회사 QA/RA에 표준 원문 구매 권고.
- 실운영 문서 미참고. web_verification: attempted-paywalled(재확인).

## 재확인 시도 (2026-07-17, 드레인 스프린트)
- WebSearch 재시도("IEC 60601-2-54" clause 201.12.1.101 kVp / 203.6 / 203.7 AEC) — IEC Webstore·iTeh 카탈로그 페이지만 반환, 조항 본문 발췌 없음. 표준 원문(유료) 미확보 상태 불변.
- **판정 유지: 미확인. 상태: open 유지.** 5개 문서(검사_시험_밸리데이션_개요·IEC60601-2-54_형식시험_체크리스트·X-ray_장비_안전성능_표준_매핑·SOP-IQ-001·SOP-CAL-001)의 조항번호는 임의 수정하지 않음. 해소 조건 불변 — IEC 60601-2-54:2022 원문 구매 후 대조.
- 실운영 문서 미참고. web_verification: attempted-paywalled(재확인 2026-07-17).

## 재확인 시도 (2026-07-18, 드레인 스프린트 3차)
- WebSearch 재시도(clause 201.12.1.101/203.6/203.7 kVp·AEC 특정 조항) — IEC Webstore/iTeh 카탈로그·무관 표준(60601-2-25/-27/-7 등)만 반환, 조항 본문 미확보.
- MITA "21 CFR Subchapter J to IEC Comparison Table" PDF(medicalimaging.org) — 링크 만료(NEMA 홈페이지로 리다이렉트), 접근 불가.
- FDA Guidance "Medical X-Ray Imaging Devices: Conformance with IEC Standards"(fda.gov/media/99466, 2023-02-21) 직접 열람 — IEC 60601-2-54가 21 CFR 1020.31 등에 상응함은 확인되나, kVp/AEC 세부 조항번호(§203.6/§201.12.1/§201.6 등) 본문 발췌는 미포함. 해소에 불충분.
- **판정 유지: 미확인. 상태: open 유지.** 대상 5개 문서 조항번호 임의 수정하지 않음. 해소 조건 불변 — IEC 60601-2-54:2022 원문 구매 후 대조.
- 실운영 문서 미참고. web_verification: attempted-paywalled(3차 재확인 2026-07-18).

## 재확인 시도 (2026-07-19, 드레인 스프린트 4차)
- WebSearch 재시도(clause 201.12.1.101 kVp / 203.7 AEC 특정 조항) — 표준 원문 발췌 미확보(동일 카탈로그 페이지만 반환), 4차 시도에도 paywalled 상태 불변.
- 부분적 정황 증거(Tier1 아님, 참고용): IEC 60601-2-54 조항번호 체계는 IEC 60601-1:2005 기반 particular standard 관례상 "201.x"는 모(母)표준 Clause x에 대응(예: Clause 12 = "Accuracy of controls and instruments and protection against hazardous output") — 이 구조적 관례에 따르면 "§201.12.1"(kVp 정확도)은 Clause 12 계열과 구조적으로 부합하나, "§201.6"(Clause 6 = Classification 계열)은 부합하지 않음. 단, 이는 일반 넘버링 관례 추론이며 IEC 60601-2-54:2022 본문 직접 확인이 아니므로 **정답 확정 근거로 사용하지 않음**(추정 배제 원칙).
- **판정 유지: 미확인. 상태: open 유지.** 대상 5개 문서 조항번호 임의 수정하지 않음. 해소 조건 불변 — IEC 60601-2-54:2022 원문 구매 후 대조.
- 실운영 문서 미참고. web_verification: attempted-paywalled(4차 재확인 2026-07-19).

## 재확인 시도 (2026-07-24, 드레인 스프린트 6차)

**신규 확보(Tier1급, Ed.1.1/2009+AMD1:2015 CSV 한정)**: iTeh Standards 무료 미리보기 PDF(`https://cdn.standards.iteh.ai/samples/15163/5a770dc1ca1e43aebecc0c9e4880a364/IEC-60601-2-54-2009.pdf`, IEC 공식 배포 미리보기 — Foreword+목차 전문)를 web_fetch로 확보. Foreword에 조항번호 체계 규칙이 명시됨: "the numbering of clauses ... corresponds to that of the general standard with the prefix '201' ... or applicable collateral standard with the prefix '20x' where x is the final digit(s) of the collateral standard document number (e.g. 203.4 ... addresses ... Clause 4 of the IEC 60601-1-3 collateral standard)". 목차상 `201.6 Classification`(분류, kVp정확도와 무관), `201.12 Accuracy of controls and instruments and protection against hazardous outputs`(제어기·계기 정확도 — kVp정확도 후보), `Table 203.102 – Loadings for testing AUTOMATIC EXPOSURE CONTROLS`(AEC시험, Clause 203=IEC 60601-1-3 산하 확인)를 확인 — 5차(2026-07-19)에서 이미 확보한 근거와 동일선상.

**신규 발견 1(Tier1급 — IEC 자체 배포 채널, Ed.2:2022 대상)**: IECEE(IEC 산하 적합성평가 공식기구, iecee.org) 및 AFNOR EDITIONS(프랑스 국가표준기관 공식 판매채널, boutique.afnor.org) 두 독립 공식 채널에서 **동일한 IEC 60601-2-54:2022 Foreword "Significant technical changes" 원문 a)~f)**을 확보(web_fetch 직접 열람, 두 소스 완전 일치 — 상호검증). 핵심: "d) the subclause 201.11.101 'Protection against excessive temperatures of X-ray tube assemblies' has been removed from this document" — Ed.2:2022에서도 `201.x.10x` particular-standard 서브조항 넘버링 관행이 실제로 유지됨을 **2022년판 원문 자체로 최초 확인**(5차까지는 Ed.1.1 추론에 불과했음). 단, kVp/AEC/투시경보 조항번호 자체는 이 Foreword 발췌에 포함되지 않아 직접 확정 불가.

**신규 발견 2(Tier2, 참고용 — 실무자 인용, Ed.1:2009 대상)**: elsmar.com(품질규격 전문 포럼) 2022-10-16 게시물에서 실제 표준 소지자가 "IEC 60601-2-54:2009 → **203.6.4.3.104.6** Accuracy of CURRENT TIME PRODUCT(mAs 정확도), 판정기준 ±(10% + 0.2 mAs)"를 직접 인용. 이는 `203.6.x`가 "부하계수(loading factor: kV·mA·시간·mAs) 정확도" 패밀리 조항군임을 시사하며, 5개 문서 중 `검사_시험_밸리데이션_개요.md`의 "§203.6, kVp ±5%" 표기와 **구조적으로 상당히 부합**(동일 상위조항 산하 형제 서브조항 존재 확인). 그러나 (a) Tier2(포럼 게시물, 1차 출처 직접 열람 아님) (b) Ed.1:2009 기준이며 Ed.2:2022는 "technical revision"으로 서브조항 재번호 가능성 있음 — 정답 확정 근거로 사용하지 않음.

**iTeh 2022년판 미리보기 PDF 직접 열람 재시도(4차)**: 카탈로그 페이지에서 확보한 두 링크(`.../a4ed6bfb.../IEC-60601-2-54-2022.pdf`, `.../d6093f55.../IEC-60601-2-54-2022.pdf`[RLV=redline판])를 Chrome으로 열람 — 두 URL 모두 `document.contentType == application/pdf` 확인(유효한 PDF 로드)되나, `get_page_text`는 "No text content found"(캔버스 렌더링), `screenshot`은 대기시간 연장(6~8초) 및 재로드·클릭 시도에도 **3개 사이클 연속 동일하게 완전 회색 빈 화면**만 캡처됨(PDFium 별도 프로세스 렌더링 추정, CDP 캡처 범위 밖 가능성). `read_network_requests`·`read_page` 접근도 콘텐츠 미확보. web_fetch는 두 URL 모두 "URL not in provenance set"(WebSearch 결과에 정확한 URL 미포함)으로 거부 — WebSearch 쿼리 재구성(수 회) 시도했으나 정확한 sample-PDF 직접링크는 검색결과에 노출되지 않음(카탈로그 페이지·webstore.iec.ch 개요 페이지만 반환, 두 페이지 모두 JS-렌더링 SPA로 본문 텍스트 미확보).

**mdcpp.com 전문 PDF 링크 발견(미사용)**: WebSearch 결과에 `mdcpp.com`(비공식 3자 사이트)의 IEC 60601-2-54-2022 전문 PDF 직접다운로드 링크가 노출되었으나, **IEC/공식 재판매채널이 아닌 출처 미상 사이트이므로 Tier1 원칙 및 신뢰할 수 없는 출처 다운로드 금지 원칙에 따라 접근하지 않음**(의도적 미사용, 저작권/출처신뢰성 문제).

**판정 유지: 미확인. 상태: open 유지.** 대상 5개 문서(검사_시험_밸리데이션_개요·IEC60601-2-54_형식시험_체크리스트·X-ray_장비_안전성능_표준_매핑·SOP-IQ-001·SOP-CAL-001)의 조항번호는 이번 사이클도 임의 수정하지 않음. 구조적 정황(2건)이 "§203.6"(검사_시험_밸리데이션_개요) 표기에 유리하게 축적되고 있으나 — (1) Ed.2:2022 원문 직접 대조 실패 지속, (2) Ed.1→Ed.2 technical revision에 따른 서브조항 재번호 리스크 미배제, (3) "§201.12.1"(형식시험_체크리스트·X-ray_매핑, Clause 12=Accuracy of controls, 일반표준측) 역시 여전히 구조적으로 배제 불가 — **추정 배제 원칙에 따라 정답 확정 보류**. 해소 조건 불변: IEC 60601-2-54:2022 원문(유료, 정식 채널) 구매·직접 대조 후 단일화.

실운영 문서 미참고. web_verification: yes(IECEE·AFNOR EDITIONS 공식 Foreword 원문 직접열람 — 상호검증 2소스 일치, 신규 확보) + attempted-blocked(iTeh 2022 PDF 캔버스 렌더링 6차 연속 실패) + Tier2 보조(elsmar.com 실무자 인용).

**클러스터 확장 발견(C2×03_설계_개발관리 스윕 중 grep 확산 — 신규 자매문서 4건 추가 확인, 정정 없이 기록만)**: 기존 5개 문서(05 카테고리) 외에 `03_설계_개발관리` 폴더에서도 동일 파라미터가 재차 인용됨을 확인:
- `설계개발_프로세스.md` L117-119: kVp정확도 "§203.6.4"(±5%), mAs재현성 "§203.6.5"(CV≤5%), HVL "§203.6.3" — **§203.6 계열 서브조항**으로, `검사_시험_밸리데이션_개요.md`의 "§203.6"(상위조항)과 **정합**(자매 상위/하위 관계로 해석 가능, 상호모순 아님).
- `CHK-DR-001_설계검토_체크리스트.md` L180, `ALARA_지원기능_설계명세.md` L11/L51: AEC "§203.7.8" — `IEC60601-2-54_형식시험_체크리스트.md`의 기존 "§203.7.8"과 **정합**(3개 문서 일치), `검사_시험_밸리데이션_개요.md`의 "§203.7"(상위조항 표기)과도 정합 가능성. SOP-IQ-001의 "§201.12"만 이 그룹과 불일치.
- `SOP-DT-001_설계이관_절차.md` L116: kVp±5%/mAs±10%(구체 조항번호 미기재, "IEC 60601-2-54"만 인용) — 결함 아님(조항번호 주장 없음).

**해석**: "§203.6.x"(kVp) / "§203.7.8"(AEC) 계열이 저장소 내 독립 작성된 4개 이상 문서에서 수렴하는 반면, "§201.12.1"(형식시험_체크리스트·X-ray_매핑)·"§201.6"(SOP-IQ-001·SOP-CAL-001)·"§201.12"(SOP-IQ AEC)는 소수 문서에 국한됨 — **정황상 "§203.6.x/§203.7.8" 계열의 확률적 개연성이 다수결로는 더 높으나, 이는 Tier1 근거가 아니라 저장소 내부 합의(consensus) 관찰에 불과**하며 추정 배제 원칙상 정답 확정 근거로 사용하지 않음. 5개 문서(원 클러스터) 임의 수정은 이번 사이클도 보류. 신규 확인된 4개 문서(설계개발_프로세스·CHK-DR-001·ALARA_지원기능_설계명세·SOP-DT-001)는 서로 정합적이므로 별도 정정 불필요(PASS, 클러스터 확장 기록만).

## 해소 및 종결 (2026-07-27, 드레인 스프린트 7차 — Tier1 신규 확보)
- **신규 Tier1**: VDE(IEC 공식 리셀러, vde-verlag.de) 배포 IEC 60601-2-54:2022 **RLV 미리보기 PDF 직접 열람**(WebSearch 경유, EN 목차 전문 + FR 목차). 확정 사실: ① Clause **203.6 = RADIATION management**(pp.33–48), 산하에 Table 203.101(Tests for verifying reproducibility and linearity, p.37)·Table 203.102(LOADINGS for testing AUTOMATIC EXPOSURE CONTROLS, p.38) 소속 — kVp/부하계수 정확도·재현성·AEC 시험은 §203.6 계열. ② **§201.6 = Classification**(kVp와 무관), ③ §201.12 = Accuracy of controls…(p.27, 1쪽 — 세부 방사선 출력 요구는 §203.6에 위치), ④ **§203.7 = RADIATION QUALITY**(pp.48–49, 1쪽 — AEC 소속 불가), ⑤ §203.8 = X-RAY BEAM 제한(투시 경보 소속 근거 없음).
- **일원화 정정(클러스터 전체, 동일 클래스 일괄)**: kVp 정확도 → §203.6 (Table 203.101)로 통일: 형식시험_체크리스트(§201.12.1→)·X-ray_매핑(§201.12.1→)·SOP-IQ-001 2개소(§201.6→)·SOP-CAL-001(§201.6→)·SOP-CC-001 2개소(§201.12.1→)·SOP-SVC-001(§201.12.1→)·공정_밸리데이션(§201.12.1→). AEC → §203.6 (Table 203.102)로 통일: 개요(§203.7→)·체크리스트 2개소(§203.7.8→)·SOP-IQ(§201.12→)·SOP-CAL(§201.12→)·X-ray_매핑·SOP-SVC·공정_밸리데이션 2개소·CHK-DR-001·ALARA_설계명세 2개소(§203.7.8→). 검사_개요 §203.6 기존 표기·설계개발_프로세스 §203.6.x는 정합(무수정). 투시 5분 경보: 체크리스트(§203.8.102)·SOP-IQ(§203.4) → "세부조항 미확인(21 CFR 1020.32(h)(2) 상응)"로 표기(경보값 자체는 eCFR 1020.32(h) Tier1 기확정).
- **잔존(별건 이관)**: 세부 서브조항 번호(203.6.x.x)·역치값(±5/±10/±2%, CV 5/10%)은 원문 본문 미확보로 미확정 — 역치 모순은 **audit #1002(open)**가 승계. IEC 60601-1-3 "§29.201" 판본 혼재 의심(체크리스트 L65)은 무수정 유지(60601-1-3 원문 미확보), 필요 시 별도 audit.
- **state: closed** (조항번호 모순 — 본 audit의 대상 결함 — 은 Tier1 목차 기준으로 단일화 완료).
- 실운영 문서 미참고. web_verification: yes(VDE 2022 RLV 목차 Tier1).

---
title: "audit #1002 (factuality/C2): 05 카테고리 AEC 재현성 CV 임계 문서 간 모순 — 검사_시험_밸리데이션_개요 'CV≤5%' vs SOP-IQ-001·영상품질_QC·SOP-CAL-001 'CV≤10%' (동일 파라미터·동일 표준 인용, 최소 한쪽 필연 오류)"
labels: "audit:factuality,prio:P1,risk:medium"
state: open
---

## 대상 (C2×05_검사_시험_밸리데이션 전수 스윕, 2026-07-26)

동일 파라미터 **AEC(자동노출제어) 재현성 변동계수(CV)** 임계값이 카테고리 내 4개 문서에서 두 값으로 갈림:

- `검사_시험_밸리데이션_개요.md` L110: "AEC 재현성 | CV ≤5% | IEC 60601-2-54 §203.7" (L195 체크리스트 동일 "CV ≤5%")
- `SOP-IQ-001_설치검증_수용시험_절차.md` L199 (AT-R04): "AEC 재현성 | CV ≤ 10% | IEC 60601-2-54 §201.12" (L351 양식 동일)
- `영상품질_QC_프로토콜.md` L133 (R8): "CoV ≤ 10%" (L237 양식 동일)
- `SOP-CAL-001_교정관리_절차.md` L180: "AEC 센서 검증용 장비 | CV ≤10% | IEC 60601-2-54 §201.12"

## 결함

수용시험·정기 QC·출하검사 등 시험 단계가 달라도 네 문서 모두 **같은 표준(IEC 60601-2-54)을 근거로 같은 파라미터**에 서로 다른 역치(5% vs 10%)를 부여 — 단계별 의도적 차등이라는 설명이 문서 어디에도 없어, 최소 한쪽은 필연적으로 표준 값과 불일치(논리적 모순). audit #976(조항번호 3중 모순 클러스터)이 "역치 차이는 C2에서 별도 판단"으로 이관한 사안의 C2 정식 등록 건.

참고(혼동 주의): 진단용방사선 안전관리규칙 별표1의 CV≤0.05(5%)는 **조사선량 재현성**(장치 출력) 기준으로 AEC 재현성과 별개 항목(audit #991 Tier1 확정 사실 재사용) — 이를 AEC에 전용했을 가능성이 개요.md 5% 값의 유력 기원.

## Tier1

IEC 60601-2-54:2022 원문 유료 — 정답 값 미확인(web:attempted-paywalled, #976과 동일 상태). 모순 판정은 저장소 내 교차대조에 근거(우아한 저하). 별표1 CV≤0.05는 #991에서 law.go.kr PDF 원문 확보로 확정.

## 판정

P1. 정답 확정은 표준 원문 확보 후 후속. 빌더: 표준 원문 대조로 단일화 + 시험 단계별 차등이라면 근거 명기 권고. 감사관 문서 미수정. 실운영 문서 미참고.

## 재확인 시도 및 부분 해소 (2026-07-27, 드레인 스프린트 7차)
- **신규 Tier1 확보**: VDE(IEC 공식 리셀러) 배포 IEC 60601-2-54:2022 RLV 미리보기 PDF(vde-verlag.de, WebSearch 경유 직접 열람 — EN/FR 목차 전문). Clause **203.6 RADIATION management**(pp.33–48)에 Table 203.101(reproducibility and linearity)·Table 203.102(LOADINGS for testing AUTOMATIC EXPOSURE CONTROLS) 소속 확인. §201.6=Classification, §201.12=Accuracy of controls(1쪽 분량), §203.7=RADIATION QUALITY.
- **조항 귀속 정정 완료**(#976과 동일 클래스 일괄): AEC 인용 조항을 4개 문서 모두 §203.6 (Table 203.102)로 단일화(개요 §203.7→, SOP-IQ·SOP-CAL §201.12→). 조항 모순은 해소.
- **CV 역치(5% vs 10%)는 미해소**: Table 203.102의 판정값 본문은 미리보기에 미포함(paywalled). 참고 정황(Tier1, 타법역): 21 CFR 1020.31(b) 재현성 CV≤0.05 — 단 IEC 요구값과 동일하다는 근거 없음. 추정 배제 원칙에 따라 역치 임의 통일하지 않음.
- **상태: open 유지.** 해소 조건: IEC 60601-2-54:2022 원문(유료) 구매 후 Table 203.102 판정값 대조·역치 단일화(또는 시험 단계별 차등 근거 명기).
- 실운영 문서 미참고. web_verification: yes(VDE RLV 목차 Tier1 신규).

## 재확인 시도 3차 (2026-07-28, 드레인 스프린트 — 가속)
- 추가 무료 Tier1 미리보기 2종 열람: (1) iTeh 배포 IEC 60601-2-54:2009+AMD1:2015 CSV 미리보기 PDF — p.10(§201.3 정의부)에서 절단, Table 203.101(p.31)·203.102(p.33) 본문 미포함. (2) elstandard.se 배포 SS-EN IEC 60601-2-54:2025(=IEC 2022 Ed.2) 미리보기 — 목차·서문까지만 포함, Table 203.101(p.37)·203.102(p.38) 본문 미포함.
- 보조 검색: AAPM Report(비규범, Tier2) 계열에서 AEC 재현성 CV<5% 관행 언급 확인되나, IEC 60601-2-54 규범값과 동일하다는 Tier1 근거 없음 — 추정 배제 원칙 유지, 역치 단일화 보류.
- **상태: open 유지(blocked: paywalled).** 해소 조건 불변 — 표준 원문 구매 후 Table 203.101/203.102 판정값 대조. 실운영 문서 미참고. web_verification: yes(무료 미리보기 2종 신규 열람, 판정값 미포함 확인).

## 재확인 시도 4차 (2026-07-29, 드레인 스프린트)
- WebSearch 재시도(IEC 60601-2-54:2022 §203.6.4 loading factors accuracy) — 카탈로그(iTeh·IEC Webstore·IECEE)·elsmar 포럼 결과만 반환, Table 203.101/203.102 판정값 본문 미확보. elsmar 스레드(#68968) 직접 열람 시도 — 본문 미반환.
- **상태: open 유지(blocked: paywalled).** 해소 조건 불변 — IEC 60601-2-54:2022 원문 구매 후 Table 203.101/203.102 대조. 역치 임의 통일하지 않음(추정 배제). 실운영 문서 미참고. web_verification: attempted-paywalled(4차).
## 재확인 시도 5차 (2026-07-30, 드레인 스프린트 — 가속 2차)
- iTeh 배포 IEC 60601-2-54 Ed1.1(2009+AMD1:2015 CSV) 미리보기 PDF 재열람(cdn.standards.iteh.ai) — 목차에서 §201.6=Classification, §201.12=Accuracy of controls and instruments, Table 203.101(재현성·직선성 시험)·Table 203.102(AEC 시험 LOADINGS) 소속 재확인. 판정값 본문(p.31/33)은 미리보기 미포함.
- WebSearch 재시도(§203.6.3 loading factors accuracy) — 카탈로그·포럼 결과만, 판정값 미확보.
- **상태: open 유지(blocked: paywalled).** 해소 조건 불변 — IEC 60601-2-54:2022 원문 구매 후 Table 203.101/203.102 판정값 대조·CV 역치(5% vs 10%) 단일화. 역치 임의 통일하지 않음(추정 배제). 실운영 문서 미참고. web_verification: attempted-paywalled(5차).
## 재확인 시도 6차 (2026-07-31, 드레인 스프린트)
- WebSearch 재시도(Table 203.102 / §203.6.4 AEC reproducibility CV) — 카탈로그·미리보기·포럼 결과만, 판정값 본문 미확보.
- **상태: open 유지(blocked: paywalled).** 해소 조건 불변 — IEC 60601-2-54:2022 원문 구매 후 Table 203.101/203.102 판정값 대조·CV 역치(5% vs 10%) 단일화. 역치 임의 통일하지 않음(추정 배제). 실운영 문서 미참고. web_verification: attempted-paywalled(6차).
## 재확인 시도 7차 (2026-08-04, 드레인 스프린트)
- WebSearch 재시도(§201.12.1/§203.6.4 loading factors accuracy) — 카탈로그(iTeh 2022/2024)·elsmar 포럼(Tier2)만 반환. mdcpp.com 게시 IEC 60601-2-54:2022 전문 PDF 링크 발견했으나 fetch 본문 미반환(빈 응답). elsmar 스레드에서 Ed.1(2009) §203.6.4.3.104.6 CURRENT TIME PRODUCT 정확도 ±(10%+0.2mAs) 확인(Tier2, AEC 재현성 CV값 아님 — 판정 불사용).
- **상태: open 유지(blocked: paywalled).** 해소 조건 불변 — IEC 60601-2-54:2022 원문 구매 후 Table 203.101/203.102 판정값 대조·CV 역치(5% vs 10%) 단일화. 추정 배제 유지. 실운영 문서 미참고. web_verification: attempted-paywalled(7차).
## 재확인 8차 (2026-08-05, 드레인 스프린트)
- 간단 재확인만 수행(원장 권고: 반복 WebSearch/미리보기 재시도 한계효용 낮음). 상태 변화 없음 — Table 203.101/203.102 판정값 paywalled 유지.
- 처리 방침은 plan #1018(GH#1690, 목표 2026-08-11)에서 확정 예정: 원문 확보 경로(구매/도서관/제조사) 결정 또는 보수적 잠정값+주석.
- **상태: open 유지(blocked: paywalled).** 추정 배제 유지. 실운영 문서 미참고. web_verification: no(신규 시도 없음, 8차 간단 재확인).
## 재확인 9차 (2026-08-06, 드레인 스프린트)
- WebSearch 1회 재시도(Table 203.102 AEC reproducibility CV limit) — 기존 확인된 카탈로그·미리보기(VDE RLV, iTeh, elstandard.se) 및 Tier2 교육자료만 반환, 판정값 본문 미확보(신규 소스 없음).
- **상태: open 유지(blocked: paywalled).** 처리 방침은 plan #1018(GH#1690, 목표 2026-08-11)에서 확정 예정 — 원문 확보 경로 결정 또는 보수적 잠정값+주석. 추정 배제 유지. 실운영 문서 미참고. web_verification: attempted-paywalled(9차).
## 재확인 10차 (2026-08-07, 드레인 스프린트)
- WebSearch 1회 재시도(Table 203.102 AEC reproducibility CV limit) — 기존 카탈로그(iTeh, IEC Webstore)·Tier2 학술자료(맘모그래피 AEC, 비해당)만 반환. 판정값 본문 미확보(신규 소스 없음).
- **상태: open 유지(blocked: paywalled).** 처리 방침은 plan #1018(GH#1690, 목표 2026-08-11)에서 확정 예정 — 원문 확보 경로 결정 또는 보수적 잠정값+주석. 추정 배제 유지. 실운영 문서 미참고. web_verification: attempted-paywalled(10차).

---
doc-id: GUIDE-PHASE2-FRAMEWORK
title: Phase 2 — 규제 준비도 평가 프레임
type: Guide
version: v0.1
status: draft
category: 00_프로젝트관리
purpose: 1차 구축 자료의 인허가 충분성을 자체 평가하기 위한 체크리스트·갭분석·점수화 표준
applicable: [FDA QMSR, FDA SBOM, EU MDR 2017/745, ISO13485:2016, ISO14971:2019, IEC62304, IEC60601-1, IEC60601-2-54, IEC81001-5-1, MFDS]
owner: RA/QA Lead
last-review: 2026-05-28
review-due: 2026-08-28
---

# Phase 2 — 규제 준비도 평가 프레임

## 1. 평가 원칙

1. **자체 평가** — 규제기관 API 접속 없이 공개된 공식 체크리스트·가이드만으로 평가
2. **데이터 기반** — 각 문서의 frontmatter `applicable` 필드를 단일 진실원으로 사용. 사람 판단 최소화
3. **정량+정성 병행** — 자동 점수(정량) + 모의 감사 시나리오(정성)
4. **지속 사이클** — 일/주/월/분기 4단계 주기로 점검·보완

## 2. 체크리스트 항목 표준 형식

`13_규제평가_체크리스트/<표준코드>.md` 1개 파일 = 1개 표준. 본문은 다음 형식 항목들:

```yaml
- id: FDA-510K-RTA-A1
  source: FDA 510(k) RTA Checklist (2024)
  clause: Section A.1
  requirement: 510(k) Cover Letter — applicant name, address, contact
  severity: must
  evidence_type: cover_letter
  applicable_keywords: [FDA QMSR, FDA 510]
  related_docs: [JD-RA-001]
```

| 필드 | 설명 |
|------|------|
| `id` | `<표준>-<섹션>-<번호>` 형식 고유 ID |
| `source` | 출처 (공식 문서명·버전·발행일) |
| `clause` | 원문 조항 번호 |
| `requirement` | 요구사항 한 줄 요약 (영문 가능) |
| `severity` | `must` (의무) / `should` (권장) / `may` (선택) |
| `evidence_type` | 충족 증거 유형 (SOP / Form / Report / Test 등) |
| `applicable_keywords` | 충족 매핑 키워드 (문서 frontmatter `applicable`과 매칭) |
| `related_docs` | (자동 채워짐) 충족 후보 문서 doc-id 목록 |

## 3. 자동 갭 분석 알고리즘

```
for 항목 in 모든_체크리스트_항목:
    매칭_문서 = [d for d in 모든_문서
                if any(k in d.frontmatter.applicable for k in 항목.applicable_keywords)]

    if not 매칭_문서:
        status = '미충족 (없음)'
        score = 0
    elif len(매칭_문서) == 1 and not 양식·SOP_타입:
        status = '부분 충족 (참조만 있음)'
        score = 50
    elif evidence_type == 'Form' and not '관련 양식 존재':
        status = '부분 충족 (SOP만, 양식 없음)'
        score = 70
    else:
        status = '충족'
        score = 100

표준_점수 = mean(항목별 score, weight by severity)
```

severity 가중치:
- `must`: 가중치 1.0
- `should`: 가중치 0.5
- `may`: 가중치 0.2

표준별 점수 = Σ(항목 점수 × 가중치) / Σ(가중치) × 100

## 4. 4단계 보완 사이클

### 4.1 데일리 (process-project, 03:18 KST)
**Trigger:** 매일 자동
**산출:**
- 신규 문서 작성/보강 (현재 활동 유지)
- 갭 발견 시 issue-draft 자동 등록 (severity가 must인 경우)
- 매트릭스·readiness·대시보드 자동 갱신

### 4.2 위클리 (weekly-review, 매주 금요일 17:00 KST)
**Trigger:** 신규 스케줄
**작업:**
1. 주간 갭 변동 분석 (지난주 vs 이번주 readiness 점수 비교)
2. closed/open 이슈 효율 지표 (평균 처리일, 재오픈율)
3. 다음 주 보강 우선순위 Top 3 선정 (severity × business_risk × time-to-target)
**산출:** `13_규제평가_체크리스트/주간_갭분석_YYYY-MM-DD.md`

### 4.3 월간 (monthly-readiness, 매월 1일 09:00 KST)
**Trigger:** 신규 스케줄
**작업:**
1. 표준별 종합 점수 산출 (8종 표준)
2. 모의 감사 시나리오 10건 실행 (LLM 셀프 리뷰)
3. 외부 변경사항 점검 (규제 개정·새 표준 발효)
4. review-due 60일 이내 만료 문서 알림 → issue-draft 자동 생성
5. 월간 Executive Summary 작성
**산출:** `12_교차검증_보고서/월간_종합_YYYY-MM.md`

### 4.4 분기 (quarterly-audit, 분기말 금요일 16:00 KST)
**Trigger:** 신규 스케줄
**작업:**
1. 분기 종합 보고서 (이해관계자용)
2. 공개 510(k) Summary 벤치마크 3건 분석
3. Tier 마일스톤 점검
4. 다음 분기 우선순위 결정
5. 외부 컨설팅 필요 여부 판단
**산출:** `12_교차검증_보고서/분기_종합_YYYY-Qx.md`

## 5. 종합 점수 → 대시보드 표시

`scripts/build_readiness.py` 가 다음 산출:

```json
{
  "FDA 510(k)": {"score": 72, "must_unmet": 5, "total_items": 80},
  "FDA QMSR":   {"score": 68, "must_unmet": 8, "total_items": 120},
  "EU MDR":     {"score": 58, "must_unmet": 12, "total_items": 75},
  "ISO13485":   {"score": 91, "must_unmet": 1,  "total_items": 95},
  ...
}
```

`build_dashboard_html.py`가 이 JSON을 읽어 "규제 준비도" 카드 렌더링.

## 6. 모의 감사 시나리오

`13_규제평가_체크리스트/모의감사_시나리오.md`에 50~100건의 가상 감사관 질문 작성. 형식:

```yaml
- id: SCEN-FDA-001
  question: "변경 통제 절차서를 보여달라. 최근 1년 변경 이력을 확인하고 싶다."
  expected_docs: [SOP-CC-001, F-CC-001~005]
  category: change_control
  source: FDA QMSR 820.30 inspection style
```

자동 평가:
- 자동 응답 가능 (해당 doc-id 존재 + 매트릭스에서 즉시 식별 가능) → 충족
- 응답 불가 → 갭

## 7. 종료 조건 (Definition of Done)

| 항목 | 목표 |
|------|------|
| 8개 표준 체크리스트 항목화 | 100% |
| 자동 갭 분석 가동 | push마다 |
| 4단계 스케줄 정상 가동 | 1주 이상 |
| 7개 표준 readiness | ≥ 70% |
| 모의 감사 응답률 | ≥ 80% |
| Critical(must) 미충족 | 0건 |

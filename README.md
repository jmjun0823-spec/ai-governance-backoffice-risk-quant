# Quant & LegalTech Risk Framework (AI Governance & Back-Office Analysis)

본 리포지토리는 네이버 경제/금융 데이터 분석 블로그 **혜안**의 게시글 **"[집중 탐구 분석]: 증권업계 AI 거버넌스 법제화와 백오피스 혁신, 정량적 리스크 평가 및 리걸테크 파이프라인 구축 전략"**에 언급된 정량적 실증 모델 및 시뮬레이션을 구현한 코드베이스입니다.

---

## 📅 실증 분석 기간 (Empirical Analysis Period)
- **분석 기간**: **2026년 10월 2일 ~ 2026년 11월 2일 (최근 1개월, 22거래일)**
- **분석 목적**: 최근 1개월간의 시장 변동성($VKOSPI > 25\%$) 및 일일 거래량 폭증 국면(+150%)에서 백오피스 수작업 지연 시간($12.4\text{분} \to 48.7\text{분}$)과 리스크 마모(Operational Drag)를 통계적으로 검정.

---

## 📌 주요 특징 및 기능 (Key Features)

1. **AI 거버넌스 규제 충격 정량화 모델 ($ETC$ 계산기)**
   - 금융 AI 도입 시 직면하는 총 기대 비용(Expected Total Cost, $ETC$) 산출
   - $ETC = C_{dev}(A) + P_{fail}(\theta) \times L_{reg} + \lambda \cdot VaR_{operational}$ 공식 구현
   - SHAP Score, XAI(설명가능성) 미준수 시의 법적 과징금 정량화

2. **백오피스 수작업 처리 및 과태료 시뮬레이터 (가설 $H_0, S$ 검정)**
   - 건당 처리 시간, 야간 근무 비용, 결제 지연 과태료 계산
   - 최근 1개월(22거래일) 시뮬레이션 기반 $H_0$ 가설 통계적 기각 검정 ($p < 0.05$)

3. **추적오차 & 테일 리스크 (Tail Risk) 측정 모듈**
   - 장 마감 임박 시점(End-of-Day Settlement) 결제 오류, 슬리피지(Slippage), 유동성 박약 위험 수치 분석

---

## 📁 프로젝트 구조 (Repository Structure)

```text
ai-governance-backoffice-risk-quant/
├── README.md
├── requirements.txt
├── config.py
├── main.py
└── src/
    ├── governance_etc.py
    ├── backoffice_sim.py
    ├── tail_risk.py
    └── pipeline.py

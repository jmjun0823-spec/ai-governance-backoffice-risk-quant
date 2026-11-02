# config.py

ANALYSIS_PERIOD = {
    'start_date': '2026-10-02',
    'end_date': '2026-11-02',
    'trading_days': 22  # 최근 1개월 거래일수
}

PARAM_ETC = {
    'C_dev': 500000,          # 개발 및 자율화 기본 비용 (USD)
    'L_reg': 2000000,         # 규제 위반 시 기본 법적 과징금 (USD)
    'lambda_var': 1.5,        # 운용 리스크 VaR 가중치
    'shap_threshold': 0.85    # XAI 설명가능성 기준 점수
}

PARAM_BACKOFFICE = {
    'normal_proc_time_min': 12.4,   # 정상 국면 건당 처리 시간 (분)
    'high_vol_proc_time_min': 48.7,  # 고변동성/거래량 폭증 국면 건당 처리 시간 (분)
    'vix_threshold': 25.0,          # VKOSPI / VIX 기준치 (%)
    'volume_surge_pct': 1.50        # 거래량 증가율 (+150%)
}

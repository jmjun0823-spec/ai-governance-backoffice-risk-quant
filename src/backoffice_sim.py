# src/backoffice_sim.py
import numpy as np
import pandas as pd
from scipy import stats

class BackOfficeDragSimulator:
    """
    백오피스 수작업 처리 지연 및 H0 가설 검정 모듈
    - 분석 기간: 2026-10-02 ~ 2026-11-02 (22거래일 시뮬레이션 데이터)
    - H0: 시장 변동성 폭증 시에도 백오피스의 건당 처리 리스크 및 오류율은 일정하다.
    """
    def __init__(self, trading_days: int = 22):
        self.n_sims = trading_days

    def run_hypothesis_test(self):
        np.random.seed(42)
        # 2026-10-02 ~ 2026-11-02 거래일 날짜 생성 및 지연시간 시뮬레이션
        dates = pd.date_range(start="2026-10-02", end="2026-11-02", freq="B")
        normal_days = np.random.normal(loc=12.4, scale=1.5, size=len(dates))
        surge_days = np.random.normal(loc=48.7, scale=5.2, size=len(dates))
        
        # 웰치 t-검정 (Welch's t-test)
        t_stat, p_val = stats.ttest_ind(surge_days, normal_days, equal_var=False)
        
        df_result = pd.DataFrame({
            'Date': dates,
            'Normal_Proc_Time_Min': normal_days,
            'Surge_Proc_Time_Min': surge_days,
            'Delay_Delta_Min': surge_days - normal_days
        })
        
        return {
            't_statistic': t_stat,
            'p_value': p_val,
            'h0_rejected': p_val < 0.05,
            'data_summary': df_result
        }

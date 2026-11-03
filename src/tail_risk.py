# src/tail_risk.py
import numpy as np

class TailRiskAnalyzer:
    """
    장 마감 임박 시점(End-of-Day Settlement) 결제 오류 및 테일 리스크(Tail Risk) 평가 모듈
    """
    def __init__(self, portfolio_value: float = 10_000_000):
        self.portfolio_value = portfolio_value

    def estimate_slippage_and_var(self, delay_minutes: float, market_volatility: float = 0.25):
        """
        결제 지연 시간(분) 및 시장 변동성에 따른 Tail Risk (99% VaR 및 Slippage) 산출
        """
        time_factor = np.sqrt(delay_minutes / (6.5 * 60))
        slippage_pct = 0.0005 * (delay_minutes / 10.0) ** 1.5
        
        var_99 = self.portfolio_value * 2.33 * market_volatility * time_factor
        expected_slippage_loss = self.portfolio_value * slippage_pct
        
        return {
            "Delay_Minutes": delay_minutes,
            "Slippage_Loss_USD": expected_slippage_loss,
            "Tail_VaR_99_USD": var_99,
            "Total_Tail_Exposure": expected_slippage_loss + var_99
        }

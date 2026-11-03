# src/governance_etc.py
import numpy as np

class AIGovernanceCostModel:
    """
    AI 거버넌스 규제 충격 모델링 (ETC: Expected Total Cost)
    ETC = C_dev(A) + P_fail(theta) * L_reg + lambda * VaR_operational
    """
    def __init__(self, c_dev: float, l_reg: float, lambda_var: float = 1.5):
        self.c_dev = c_dev
        self.l_reg = l_reg
        self.lambda_var = lambda_var

    def calculate_p_fail(self, shap_score: float) -> float:
        """
        XAI 설명가능성(SHAP Score)에 따른 규제 위반/오류 발생 확률 P_fail(theta)
        SHAP 점수가 기준치(0.85) 미만일 경우 위반 확률이 지수적으로 상승
        """
        p_fail = np.exp(-4.5 * (shap_score - 0.5)) if shap_score < 0.85 else 0.02
        return float(np.clip(p_fail, 0.01, 0.95))

    def calculate_etc(self, shap_score: float, var_op: float) -> dict:
        p_fail = self.calculate_p_fail(shap_score)
        expected_penalty = p_fail * self.l_reg
        op_risk_cost = self.lambda_var * var_op
        
        total_etc = self.c_dev + expected_penalty + op_risk_cost
        
        return {
            "Total_ETC": total_etc,
            "C_dev": self.c_dev,
            "P_fail": p_fail,
            "Expected_Penalty": expected_penalty,
            "OpRisk_Cost": op_risk_cost
        }

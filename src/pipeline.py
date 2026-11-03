# src/pipeline.py
from src.governance_etc import AIGovernanceCostModel
from src.backoffice_sim import BackOfficeDragSimulator
from src.tail_risk import TailRiskAnalyzer

class LegalTechRiskPipeline:
    """
    증권업계 AI 거버넌스 및 백오피스 혁신 파이프라인 통합 클래스
    """
    def __init__(self, etc_model: AIGovernanceCostModel, bo_sim: BackOfficeDragSimulator, tail_analyzer: TailRiskAnalyzer):
        self.etc_model = etc_model
        self.bo_sim = bo_sim
        self.tail_analyzer = tail_analyzer

    def execute_full_diagnostic(self, shap_score: float = 0.80):
        print("=== [1] AI 거버넌스 규제 충격(ETC) 평가 ===")
        etc_res = self.etc_model.calculate_etc(shap_score=shap_score, var_op=150000)
        print(f"SHAP Score: {shap_score} -> Total ETC: ${etc_res['Total_ETC']:,.2f} (Penalty: ${etc_res['Expected_Penalty']:,.2f})")

        print("\n=== [2] 백오피스 수작업 drag 및 가설 검정 (H0_S) [기간: 2026.10.02 ~ 2026.11.02] ===")
        bo_res = self.bo_sim.run_hypothesis_test()
        print(f"t-stat: {bo_res['t_statistic']:.4f}, p-value: {bo_res['p_value']:.2e}")
        print(f"H0 기각 여부 (p < 0.05): {bo_res['h0_rejected']}")

        print("\n=== [3] 결제 지연에 따른 Tail Risk 및 Slippage 산출 ===")
        mean_delay = bo_res['data_summary']['Delay_Delta_Min'].mean()
        tail_res = self.tail_analyzer.estimate_slippage_and_var(delay_minutes=mean_delay)
        print(f"평균 지연시간: {mean_delay:.2f}분 -> Total Tail Risk Exposure: ${tail_res['Total_Tail_Exposure']:,.2f}")
        
        return {
            'etc': etc_res,
            'bo': bo_res,
            'tail': tail_res
        }

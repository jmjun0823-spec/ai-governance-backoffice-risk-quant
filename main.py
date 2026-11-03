# main.py
from config import PARAM_ETC, ANALYSIS_PERIOD
from src.governance_etc import AIGovernanceCostModel
from src.backoffice_sim import BackOfficeDragSimulator
from src.tail_risk import TailRiskAnalyzer
from src.pipeline import LegalTechRiskPipeline

def main():
    print("==========================================================================")
    print(" 혜안 블로그: [집중 탐구 분석] AI 거버넌스 & 리걸테크 리스크 파이프라인 검정")
    print(f" 분석 기간: {ANALYSIS_PERIOD['start_date']} ~ {ANALYSIS_PERIOD['end_date']} (총 {ANALYSIS_PERIOD['trading_days']}거래일)")
    print("==========================================================================\n")

    etc_model = AIGovernanceCostModel(c_dev=PARAM_ETC['C_dev'], l_reg=PARAM_ETC['L_reg'], lambda_var=PARAM_ETC['lambda_var'])
    bo_sim = BackOfficeDragSimulator(trading_days=ANALYSIS_PERIOD['trading_days'])
    tail_analyzer = TailRiskAnalyzer(portfolio_value=10_000_000)

    pipeline = LegalTechRiskPipeline(etc_model, bo_sim, tail_analyzer)
    pipeline.execute_full_diagnostic(shap_score=0.72)  # SHAP 미달 시나리오 진단

if __name__ == "__main__":
    main()

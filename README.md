securities-ai-governance-legaltech-pipeline/
├── README.md                  # 리포지토리 설명서 (분석 기간 2026.10.02~11.02 명시)
├── requirements.txt           # 필요 라이브러리 목록
├── config.py                  # 1개월 분석 기간 설정 및 파라미터 정의
├── main.py                    # 전체 시뮬레이션 파이프라인 실행 파일
└── src/
    ├── governance_etc.py      # AI 거버넌스 규제 충격(ETC) 계산 모듈
    ├── backoffice_sim.py      # 최근 1개월 일별 백오피스 지연 Monte Carlo 시뮬레이터
    ├── tail_risk.py           # 장 마감 임박 결제 지연 및 Tail Risk 분석 모듈
    └── pipeline.py            # 리갈테크 통합 진단 파이프라인

"""行业到 ETF 的研究型表达质量评估。"""
from __future__ import annotations

import pandas as pd


def evaluate_etf_expression(candidates: pd.DataFrame) -> pd.DataFrame:
    """评估候选 ETF 是否足以表达行业信号；不构成交易指令。"""
    result = candidates.copy()
    required = (
        (result["return_correlation_60d"] >= 0.80)
        & (result["tracking_error_60d"] <= 0.08)
        & (result["average_turnover_20d"] >= 5_000_000)
        & (result["spread_bps"] <= 10)
    )
    result["expression_status"] = required.map({True: "expressible", False: "not_recommended"})
    result["expression_quality_score"] = (
        result["return_correlation_60d"] - result["tracking_error_60d"]
        + (result["average_turnover_20d"] / 100_000_000).clip(upper=0.2)
        - (result["spread_bps"] / 100).clip(upper=0.2)
    )
    result["expression_rank"] = result.groupby("sector_name")["expression_quality_score"].rank(ascending=False, method="min")
    return result

"""行业到 ETF 的研究型表达质量评估。"""
from __future__ import annotations

from itertools import combinations

import pandas as pd


def calculate_etf_expression_metrics(
    sector_returns: pd.DataFrame,
    etf_returns: pd.DataFrame,
    candidates: pd.DataFrame,
    as_of_date: str | pd.Timestamp,
) -> pd.DataFrame:
    """Calculate point-in-time sector-to-ETF return expression metrics."""
    cutoff = pd.Timestamp(as_of_date)
    sector = sector_returns.copy()
    etf = etf_returns.copy()
    sector["as_of_date"] = pd.to_datetime(sector["as_of_date"])
    etf["as_of_date"] = pd.to_datetime(etf["as_of_date"])
    sector = sector.loc[sector["as_of_date"] <= cutoff]
    etf = etf.loc[etf["as_of_date"] <= cutoff]
    rows = []
    for candidate in candidates.to_dict("records"):
        matched = sector.loc[sector["sector_name"] == candidate["sector_name"], ["as_of_date", "return"]].merge(
            etf.loc[etf["etf_code"] == candidate["etf_code"], ["as_of_date", "return"]],
            on="as_of_date",
            suffixes=("_sector", "_etf"),
        ).dropna()
        result = dict(candidate)
        for window in (60, 120):
            sample = matched.tail(window)
            if len(sample) < window:
                result[f"return_correlation_{window}d"] = float("nan")
                result[f"beta_{window}d"] = float("nan")
                result[f"tracking_error_{window}d"] = float("nan")
                continue
            result[f"return_correlation_{window}d"] = sample["return_sector"].corr(sample["return_etf"])
            variance = sample["return_sector"].var(ddof=0)
            result[f"beta_{window}d"] = sample["return_sector"].cov(sample["return_etf"], ddof=0) / variance if variance else float("nan")
            result[f"tracking_error_{window}d"] = (sample["return_etf"] - sample["return_sector"]).std(ddof=0)
        result["metrics_as_of_date"] = cutoff
        rows.append(result)
    return pd.DataFrame(rows)


def evaluate_etf_expression(candidates: pd.DataFrame) -> pd.DataFrame:
    """评估候选 ETF 是否足以表达行业信号；不构成交易指令。"""
    result = candidates.copy()
    required_columns = ["return_correlation_60d", "tracking_error_60d", "average_turnover_20d", "spread_bps"]
    for column in required_columns:
        if column not in result:
            result[column] = float("nan")
    required = (
        (result["return_correlation_60d"] >= 0.80)
        & (result["tracking_error_60d"] <= 0.08)
        & (result["average_turnover_20d"] >= 5_000_000)
        & (result["spread_bps"] <= 10)
    )
    complete = result[required_columns].notna().all(axis=1)
    result["expression_status"] = "insufficient_data"
    result.loc[complete & ~required, "expression_status"] = "not_recommended"
    result.loc[complete & required, "expression_status"] = "expressible"
    result["expression_quality_score"] = (
        result["return_correlation_60d"] - result["tracking_error_60d"]
        + (result["average_turnover_20d"] / 100_000_000).clip(upper=0.2)
        - (result["spread_bps"] / 100).clip(upper=0.2)
    )
    result["expression_rank"] = result.groupby("sector_name")["expression_quality_score"].rank(ascending=False, method="min")
    return result


def select_etf_mapping(metrics: pd.DataFrame, mapping_as_of_date: str | pd.Timestamp) -> pd.DataFrame:
    """Create a dated mapping snapshot and disclose sectors without an expression."""
    result = []
    for sector_name, group in metrics.groupby("sector_name", sort=True):
        qualified = group.loc[group["expression_status"] == "expressible"].copy()
        if qualified.empty:
            result.append({
                "sector_name": sector_name,
                "etf_code": None,
                "mapping_status": "no_qualified_etf",
                "mapping_as_of_date": pd.Timestamp(mapping_as_of_date),
            })
            continue
        qualified["mapping_status"] = "expressible"
        qualified["mapping_as_of_date"] = pd.Timestamp(mapping_as_of_date)
        result.extend(qualified.to_dict("records"))
    return pd.DataFrame(result)


def calculate_etf_overlap(etf_returns: pd.DataFrame) -> pd.DataFrame:
    """Return pairwise 60-day correlations for ETF return clusters."""
    frame = etf_returns.copy()
    frame["as_of_date"] = pd.to_datetime(frame["as_of_date"])
    pivot = frame.sort_values("as_of_date").pivot(index="as_of_date", columns="etf_code", values="return")
    rows = []
    for left, right in combinations(pivot.columns, 2):
        matched = pivot[[left, right]].dropna().tail(60)
        rows.append({
            "left_etf_code": left,
            "right_etf_code": right,
            "return_correlation_60d": matched[left].corr(matched[right]) if len(matched) == 60 else float("nan"),
            "sample_count": len(matched),
        })
    return pd.DataFrame(rows)

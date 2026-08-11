"""Research-only return attribution for ETF paper portfolios."""
from __future__ import annotations

import pandas as pd


def attribute_paper_portfolio(
    simulation: dict[str, pd.DataFrame],
    industry_returns: pd.DataFrame,
    etf_returns: pd.DataFrame,
) -> pd.DataFrame:
    """Attribute net return to sector selection, ETF expression, timing and cost."""
    holdings = simulation["holdings"].copy()
    daily = simulation["daily"].copy()
    for frame in (holdings, daily, industry_returns, etf_returns):
        frame["as_of_date"] = pd.to_datetime(frame["as_of_date"])
    merged = holdings.merge(industry_returns, on=["as_of_date", "sector_name"], how="left")
    merged = merged.merge(etf_returns, on=["as_of_date", "etf_code"], how="left", suffixes=("_industry", "_etf"))
    merged["sector_selection_return"] = merged["weight"] * merged["return_industry"].fillna(0.0)
    merged["etf_expression_return"] = merged["weight"] * (merged["return_etf"].fillna(0.0) - merged["return_industry"].fillna(0.0))
    components = merged.groupby("as_of_date", as_index=False).agg(
        sector_selection_return=("sector_selection_return", "sum"),
        etf_expression_return=("etf_expression_return", "sum"),
    )
    result = daily.merge(components, on="as_of_date", how="left").fillna({"sector_selection_return": 0.0, "etf_expression_return": 0.0})
    result["timing_return"] = result["net_return"] + result["transaction_cost"] - result["sector_selection_return"] - result["etf_expression_return"]
    result["transaction_cost_return"] = -result["transaction_cost"]
    result["unallocated_cash_return"] = 0.0
    result["reconciliation_error"] = result["net_return"] - (
        result["sector_selection_return"] + result["etf_expression_return"] + result["timing_return"]
        + result["transaction_cost_return"] + result["unallocated_cash_return"]
    )
    return result

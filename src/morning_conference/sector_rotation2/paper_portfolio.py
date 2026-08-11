"""Research-only ETF paper portfolio construction; contains no execution integration."""
from __future__ import annotations

from dataclasses import dataclass

import pandas as pd


RESEARCH_MODE_ONLY = True


@dataclass(frozen=True)
class ResearchPolicy:
    max_single_etf_weight: float
    max_sector_weight: float
    max_cluster_weight: float
    max_turnover: float
    min_average_turnover: float
    cost_bps: float
    rebalance_frequency: int


def build_etf_targets(
    intent: pd.DataFrame,
    mapping: pd.DataFrame,
    policy: ResearchPolicy,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Turn permitted manual/validated industry intent into rank-one ETF targets."""
    target_rows: list[dict[str, object]] = []
    issue_rows: list[dict[str, object]] = []
    for row in intent.to_dict("records"):
        weight = float(row["target_weight"])
        if row["source_label"] not in {"manual_scenario", "validated_signal"}:
            issue_rows.append({**row, "reason": "unvalidated_signal_source", "unallocated_cash_weight": weight})
            continue
        candidates = mapping.loc[
            (mapping["sector_name"] == row["sector_name"])
            & (mapping["mapping_status"] == "expressible")
        ].sort_values("expression_rank")
        if candidates.empty:
            issue_rows.append({**row, "reason": "no_qualified_etf", "unallocated_cash_weight": weight})
            continue
        selected = candidates.iloc[0]
        if weight > policy.max_sector_weight or weight > policy.max_single_etf_weight:
            issue_rows.append({**row, "reason": "weight_limit_exceeded", "unallocated_cash_weight": weight})
            continue
        if float(selected["average_turnover_20d"]) < policy.min_average_turnover:
            issue_rows.append({**row, "reason": "insufficient_liquidity", "unallocated_cash_weight": weight})
            continue
        target_rows.append({
            "as_of_date": row["as_of_date"], "sector_name": row["sector_name"],
            "etf_code": selected["etf_code"], "target_weight": weight,
        })
    return pd.DataFrame(target_rows), pd.DataFrame(issue_rows)


def simulate_paper_portfolio(
    targets: pd.DataFrame,
    etf_prices: pd.DataFrame,
    policy: ResearchPolicy,
    initial_nav: float = 1.0,
) -> dict[str, pd.DataFrame]:
    """Simulate research holdings, unallocated cash and turnover costs only."""
    prices = etf_prices.copy()
    prices["as_of_date"] = pd.to_datetime(prices["as_of_date"])
    prices["asset_return"] = prices.sort_values("as_of_date").groupby("etf_code")["close"].pct_change()
    daily_rows: list[dict[str, object]] = []
    holding_rows: list[dict[str, object]] = []
    prior_weights: dict[str, float] = {}
    nav = initial_nav
    for as_of_date, group in targets.assign(as_of_date=pd.to_datetime(targets["as_of_date"])).groupby("as_of_date", sort=True):
        today_returns = prices.loc[prices["as_of_date"] == as_of_date].set_index("etf_code")["asset_return"]
        gross_return = sum(weight * float(today_returns.get(code, 0.0) if pd.notna(today_returns.get(code, 0.0)) else 0.0) for code, weight in prior_weights.items())
        weights = dict(zip(group["etf_code"], group["target_weight"], strict=True))
        turnover = sum(abs(weights.get(code, 0.0) - prior_weights.get(code, 0.0)) for code in set(weights) | set(prior_weights))
        cost = turnover * policy.cost_bps / 10_000
        net_return = gross_return - cost
        nav *= 1.0 + net_return
        cash_weight = 1.0 - sum(weights.values())
        daily_rows.append({"as_of_date": as_of_date, "gross_return": gross_return, "turnover": turnover, "transaction_cost": cost, "net_return": net_return, "nav": nav})
        for etf_code, weight in weights.items():
            holding_rows.append({"as_of_date": as_of_date, "etf_code": etf_code, "weight": weight, "cash_weight": cash_weight})
        prior_weights = weights
    return {"daily": pd.DataFrame(daily_rows), "holdings": pd.DataFrame(holding_rows)}

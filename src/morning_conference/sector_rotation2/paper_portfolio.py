"""Research-only ETF paper portfolio construction; contains no execution integration."""
from __future__ import annotations

from dataclasses import dataclass

import pandas as pd


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

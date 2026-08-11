"""Research-mode-only paper portfolio runner; contains no broker or order APIs."""
from __future__ import annotations

from pathlib import Path

import pandas as pd

from .attribution import attribute_paper_portfolio
from .paper_portfolio import ResearchPolicy, build_etf_targets, simulate_paper_portfolio


def run_paper_portfolio(intent: pd.DataFrame, mapping: pd.DataFrame, prices: pd.DataFrame, industry_returns: pd.DataFrame, etf_returns: pd.DataFrame, policy: ResearchPolicy, output_dir: str | Path) -> dict[str, pd.DataFrame]:
    """Run a deterministic research scenario and write inspectable CSV outputs."""
    targets, issues = build_etf_targets(intent, mapping, policy)
    simulation = simulate_paper_portfolio(targets, prices, policy)
    if not simulation["holdings"].empty:
        target_sector = targets[["as_of_date", "etf_code", "sector_name"]].copy()
        target_sector["as_of_date"] = pd.to_datetime(target_sector["as_of_date"])
        simulation["holdings"] = simulation["holdings"].merge(target_sector, on=["as_of_date", "etf_code"], how="left")
    attribution = attribute_paper_portfolio(simulation, industry_returns, etf_returns)
    destination = Path(output_dir)
    destination.mkdir(parents=True, exist_ok=True)
    simulation["daily"].to_csv(destination / "paper_portfolio_daily.csv", index=False, encoding="utf-8-sig")
    simulation["holdings"].to_csv(destination / "paper_portfolio_holdings.csv", index=False, encoding="utf-8-sig")
    issues.to_csv(destination / "paper_portfolio_issues.csv", index=False, encoding="utf-8-sig")
    attribution.to_csv(destination / "paper_portfolio_attribution.csv", index=False, encoding="utf-8-sig")
    return {"targets": targets, "issues": issues, **simulation, "attribution": attribution}

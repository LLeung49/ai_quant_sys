"""Write reproducible, research-only sector-to-ETF mapping artifacts."""
from __future__ import annotations

from pathlib import Path
from collections.abc import Callable

import pandas as pd

from .etf_mapping import calculate_etf_expression_metrics, calculate_etf_overlap, evaluate_etf_expression, shortlist_market_candidates, verify_etf_mapping
from .etf_research_data import calculate_holdings_industry_exposure
from .etf_research_data import load_current_stock_industries, load_qfq_etf_panel
from .etf_sources import fetch_etf_holdings, fetch_etf_universe


def run_etf_mapping_research(candidates: pd.DataFrame, sector_returns: pd.DataFrame, etf_returns: pd.DataFrame, mapping_as_of_date: str | pd.Timestamp, output_dir: str | Path, holdings: pd.DataFrame | None = None, industries: pd.DataFrame | None = None) -> dict[str, pd.DataFrame]:
    """Create a dated metrics, mapping and overlap research bundle from supplied inputs."""
    metrics = calculate_etf_expression_metrics(sector_returns, etf_returns, candidates, mapping_as_of_date)
    for column in ("average_turnover_20d", "spread_bps"):
        if column in candidates:
            metrics[column] = candidates.set_index(["sector_name", "etf_code"])[column].reindex(pd.MultiIndex.from_frame(metrics[["sector_name", "etf_code"]])).to_numpy()
    evaluated = evaluate_etf_expression(metrics)
    shortlist = shortlist_market_candidates(evaluated)
    evidence = pd.DataFrame()
    mapping = shortlist
    if holdings is not None and industries is not None:
        evidence = calculate_holdings_industry_exposure(holdings, industries, level=2)
        mapping = verify_etf_mapping(shortlist, evidence)
    overlap = calculate_etf_overlap(etf_returns.loc[pd.to_datetime(etf_returns["as_of_date"]) <= pd.Timestamp(mapping_as_of_date)])
    destination = Path(output_dir)
    destination.mkdir(parents=True, exist_ok=True)
    candidates.to_csv(destination / "etf_universe_snapshot.csv", index=False, encoding="utf-8-sig")
    metrics.to_csv(destination / "etf_mapping_metrics.csv", index=False, encoding="utf-8-sig")
    metrics.to_csv(destination / "etf_market_metrics.csv", index=False, encoding="utf-8-sig")
    evidence.to_csv(destination / "etf_holdings_evidence.csv", index=False, encoding="utf-8-sig")
    mapping.to_csv(destination / "etf_mapping_snapshot.csv", index=False, encoding="utf-8-sig")
    overlap.to_csv(destination / "etf_mapping_overlap.csv", index=False, encoding="utf-8-sig")
    (destination / "etf_mapping_report.md").write_text(f"# ETF Mapping Research\n\n- mapping_as_of_date: `{pd.Timestamp(mapping_as_of_date).date()}`\n- candidates: `{len(candidates)}`\n- expressible: `{int((evaluated['expression_status'] == 'expressible').sum())}`\n- verified: `{int((mapping['mapping_status'] == 'verified').sum())}`\n- RESEARCH_MODE_ONLY: `true`\n", encoding="utf-8")
    return {"universe": candidates, "metrics": metrics, "holdings_evidence": evidence, "mapping": mapping, "overlap": overlap}


def run_qfq_two_stage_etf_mapping_research(
    sector_returns: pd.DataFrame,
    start_date: str,
    mapping_as_of_date: str,
    output_dir: str | Path,
    universe_fetcher: Callable[[], pd.DataFrame],
    holdings_fetcher: Callable[[str], pd.DataFrame],
    level: int = 2,
    max_universe: int = 300,
) -> dict[str, pd.DataFrame]:
    """Run source-backed two-stage ETF research with a bounded liquid universe."""
    cutoff = pd.Timestamp(mapping_as_of_date)
    universe = fetch_etf_universe(universe_fetcher, cutoff)
    qfq = load_qfq_etf_panel(universe["etf_code"].tolist(), start_date, mapping_as_of_date)
    qfq["return"] = qfq.groupby("stock_code")["close_price"].pct_change()
    liquidity = qfq.sort_values("trade_date").groupby("stock_code")["amount"].tail(20).groupby(qfq.sort_values("trade_date").groupby("stock_code").tail(20)["stock_code"]).mean()
    selected_codes = liquidity.sort_values(ascending=False).head(max_universe).index.tolist()
    universe = universe.loc[universe["etf_code"].isin(selected_codes)].copy()
    etf_returns = qfq.loc[qfq["stock_code"].isin(selected_codes), ["trade_date", "stock_code", "return"]].rename(columns={"trade_date": "as_of_date", "stock_code": "etf_code"})
    candidates = pd.MultiIndex.from_product([sector_returns["sector_name"].unique(), selected_codes], names=["sector_name", "etf_code"]).to_frame(index=False)
    candidates["average_turnover_20d"] = candidates["etf_code"].map(liquidity)
    candidates["spread_bps"] = 0.0
    result = run_etf_mapping_research(candidates, sector_returns, etf_returns, cutoff, output_dir)
    finalist_codes = result["mapping"]["etf_code"].dropna().unique().tolist()
    holdings, failures = fetch_etf_holdings(finalist_codes, holdings_fetcher, cutoff)
    if not holdings.empty and "股票代码" in holdings:
        industries = load_current_stock_industries(holdings["股票代码"].astype(str).str.zfill(6).unique().tolist(), level)
        result = run_etf_mapping_research(candidates, sector_returns, etf_returns, cutoff, output_dir, holdings, industries)
    if not failures.empty:
        failures.to_csv(Path(output_dir) / "etf_holdings_failures.csv", index=False, encoding="utf-8-sig")
    result["universe"] = universe
    universe.to_csv(Path(output_dir) / "etf_universe_snapshot.csv", index=False, encoding="utf-8-sig")
    return result

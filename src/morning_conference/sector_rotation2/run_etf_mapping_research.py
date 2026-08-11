"""Write reproducible, research-only sector-to-ETF mapping artifacts."""
from __future__ import annotations

from pathlib import Path

import pandas as pd

from .etf_mapping import calculate_etf_expression_metrics, calculate_etf_overlap, evaluate_etf_expression, shortlist_market_candidates, verify_etf_mapping
from .etf_research_data import calculate_holdings_industry_exposure


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

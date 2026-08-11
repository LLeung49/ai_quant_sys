"""Write reproducible, research-only sector-to-ETF mapping artifacts."""
from __future__ import annotations

from pathlib import Path

import pandas as pd

from .etf_mapping import calculate_etf_expression_metrics, calculate_etf_overlap, evaluate_etf_expression, select_etf_mapping


def run_etf_mapping_research(candidates: pd.DataFrame, sector_returns: pd.DataFrame, etf_returns: pd.DataFrame, mapping_as_of_date: str | pd.Timestamp, output_dir: str | Path) -> dict[str, pd.DataFrame]:
    """Create a dated metrics, mapping and overlap research bundle from supplied inputs."""
    metrics = calculate_etf_expression_metrics(sector_returns, etf_returns, candidates, mapping_as_of_date)
    for column in ("average_turnover_20d", "spread_bps"):
        if column in candidates:
            metrics[column] = candidates.set_index(["sector_name", "etf_code"])[column].reindex(pd.MultiIndex.from_frame(metrics[["sector_name", "etf_code"]])).to_numpy()
    evaluated = evaluate_etf_expression(metrics)
    mapping = select_etf_mapping(evaluated, mapping_as_of_date)
    overlap = calculate_etf_overlap(etf_returns.loc[pd.to_datetime(etf_returns["as_of_date"]) <= pd.Timestamp(mapping_as_of_date)])
    destination = Path(output_dir)
    destination.mkdir(parents=True, exist_ok=True)
    metrics.to_csv(destination / "etf_mapping_metrics.csv", index=False, encoding="utf-8-sig")
    mapping.to_csv(destination / "etf_mapping_snapshot.csv", index=False, encoding="utf-8-sig")
    overlap.to_csv(destination / "etf_mapping_overlap.csv", index=False, encoding="utf-8-sig")
    (destination / "etf_mapping_report.md").write_text(f"# ETF Mapping Research\n\n- mapping_as_of_date: `{pd.Timestamp(mapping_as_of_date).date()}`\n- candidates: `{len(candidates)}`\n- expressible: `{int((evaluated['expression_status'] == 'expressible').sum())}`\n", encoding="utf-8")
    return {"metrics": metrics, "mapping": mapping, "overlap": overlap}

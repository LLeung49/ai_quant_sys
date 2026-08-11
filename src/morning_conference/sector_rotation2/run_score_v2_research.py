"""Run frozen P1 Score V2 nested historical research without changing production scores."""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from data_ingestion.db_config import execute_query

from .backtest import (
    DEFAULT_ALPHA_DECAY_HORIZONS,
    evaluate_nested_candidates,
    expanding_outer_windows,
    rolling_oos_windows,
)
from .backtest import build_forward_return_labels
from .score_candidates import CANDIDATE_NAMES, build_candidate_scores


SNAPSHOT_COMPONENT_COLUMNS = (
    "as_of_date, sector_name, trend_level_score, velocity_score, "
    "acceleration_score, participation_score"
)


def run_nested_research(
    level: int,
    start_date: str,
    end_date: str,
    model_version: str,
    output_dir: str | Path,
    horizons: tuple[int, ...] = DEFAULT_ALPHA_DECAY_HORIZONS,
    outer_windows: list[dict[str, pd.Timestamp]] | None = None,
    inner_window_factory=rolling_oos_windows,
) -> dict[str, pd.DataFrame]:
    """Evaluate fixed score candidates with nested historical validation only."""
    labels = build_forward_return_labels(level, start_date, end_date, horizons=horizons).copy()
    labels["as_of_date"] = pd.to_datetime(labels["as_of_date"])
    labels["target_date"] = pd.to_datetime(labels["target_date"])
    snapshots = pd.DataFrame(execute_query(
        "SELECT " + SNAPSHOT_COMPONENT_COLUMNS + " FROM sector_rotation_sector_daily_snapshot "
        "WHERE sector_level = %s AND model_version = %s AND as_of_date BETWEEN %s AND %s",
        (level, model_version, start_date, end_date),
    ))
    snapshots["as_of_date"] = pd.to_datetime(snapshots["as_of_date"])
    candidates = build_candidate_scores(snapshots)
    dates = pd.DatetimeIndex(candidates["as_of_date"].unique())
    windows = outer_windows if outer_windows is not None else expanding_outer_windows(dates)
    selection, outer = evaluate_nested_candidates(
        candidates,
        labels,
        CANDIDATE_NAMES,
        horizons,
        windows,
        inner_window_factory=inner_window_factory,
    )
    destination = Path(output_dir)
    destination.mkdir(parents=True, exist_ok=True)
    selection.to_csv(destination / f"sector_rotation2_v2_nested_selection_{end_date}.csv", index=False, encoding="utf-8-sig")
    outer.to_csv(destination / f"sector_rotation2_v2_nested_outer_{end_date}.csv", index=False, encoding="utf-8-sig")
    _write_nested_report(selection, outer, level, start_date, end_date, model_version, destination)
    return {"selection": selection, "outer": outer}


def _write_nested_report(
    selection: pd.DataFrame,
    outer: pd.DataFrame,
    level: int,
    start_date: str,
    end_date: str,
    model_version: str,
    output_dir: Path,
) -> None:
    selected = selection.loc[selection.get("selected", pd.Series(dtype=bool))] if not selection.empty else selection
    outer_rank_ic = pd.to_numeric(outer.get("rank_ic_mean", pd.Series(dtype=float)), errors="coerce")
    outer_net_return = pd.to_numeric(outer.get("outer_net_return", pd.Series(dtype=float)), errors="coerce")
    lines = [
        "# P1 Score V2 Nested Research",
        "",
        "## Scope",
        "",
        "- research_type: `nested_historical_validation`",
        f"- model_version: `{model_version}`",
        f"- sector_level: `{level}`",
        f"- discovery_sample: `{start_date}` to `{end_date}`",
        "- This is not a final OOS result. Locked OOS starts on `2026-06-12`.",
        "- Candidate matrix: `h1_acceleration`, `h2_trend_pruned`, `h3_trend_reversed`.",
        "",
        "## Summary",
        "",
        f"- outer_folds: `{len(selection)}`",
        f"- selected_folds: `{len(selected)}`",
        f"- evaluated_outer_folds: `{len(outer)}`",
        f"- outer_mean_rank_ic: `{outer_rank_ic.mean():.6f}`",
        f"- outer_median_rank_ic: `{outer_rank_ic.median():.6f}`",
        f"- outer_positive_rank_ic_share: `{(outer_rank_ic > 0).mean():.6f}`",
        f"- outer_mean_cost_adjusted_return: `{outer_net_return.mean():.6f}`",
    ]
    (output_dir / f"sector_rotation2_v2_nested_report_{end_date}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """Parse CLI arguments and run frozen nested historical research."""
    parser = argparse.ArgumentParser(description="Run P1 Score V2 nested historical research")
    parser.add_argument("--level", type=int, required=True)
    parser.add_argument("--start-date", required=True)
    parser.add_argument("--end-date", required=True)
    parser.add_argument("--model-version", default="v1")
    parser.add_argument("--output", default="outputs")
    args = parser.parse_args()
    run_nested_research(args.level, args.start_date, args.end_date, args.model_version, args.output)


if __name__ == "__main__":
    main()

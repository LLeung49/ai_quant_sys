"""Run frozen P1 Score V2 nested historical research without changing production scores."""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from data_ingestion.db_config import execute_query

from .backtest import (
    DEFAULT_ALPHA_DECAY_HORIZONS,
    evaluate_factor,
    evaluate_nested_candidates,
    expanding_outer_windows,
    rolling_oos_windows,
    select_inner_candidate,
    simulate_top_group_strategy,
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
    frozen = pd.DataFrame([
        select_inner_candidate(
            candidates,
            labels,
            CANDIDATE_NAMES,
            horizons,
            inner_window_factory(dates),
        )
    ])
    destination = Path(output_dir)
    destination.mkdir(parents=True, exist_ok=True)
    selection.to_csv(destination / f"sector_rotation2_v2_nested_selection_{end_date}.csv", index=False, encoding="utf-8-sig")
    outer.to_csv(destination / f"sector_rotation2_v2_nested_outer_{end_date}.csv", index=False, encoding="utf-8-sig")
    frozen.to_csv(destination / f"sector_rotation2_v2_frozen_selection_{end_date}.csv", index=False, encoding="utf-8-sig")
    _write_nested_report(selection, outer, level, start_date, end_date, model_version, destination)
    return {"selection": selection, "outer": outer, "frozen": frozen}


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


def evaluate_locked_oos(
    snapshots: pd.DataFrame,
    labels: pd.DataFrame,
    frozen_selection: pd.DataFrame,
    locked_start: str,
    minimum_evaluation_days: int = 63,
    cost_bps: float = 10,
) -> pd.DataFrame:
    """Report only mature results for a pre-frozen candidate after the Locked OOS boundary."""
    dated_snapshots = snapshots.copy()
    dated_snapshots["as_of_date"] = pd.to_datetime(dated_snapshots["as_of_date"])
    dated_labels = labels.copy()
    dated_labels["as_of_date"] = pd.to_datetime(dated_labels["as_of_date"])
    locked_boundary = pd.Timestamp(locked_start)
    rows: list[dict[str, object]] = []
    for frozen in frozen_selection.itertuples(index=False):
        candidate = str(frozen.candidate)
        horizon = int(frozen.horizon)
        locked_snapshots = dated_snapshots.loc[dated_snapshots["as_of_date"] >= locked_boundary]
        locked_labels = dated_labels.loc[
            (dated_labels["as_of_date"] >= locked_boundary) & (dated_labels["horizon"] == horizon)
        ]
        mature_days = int(len(set(locked_snapshots["as_of_date"]) & set(locked_labels["as_of_date"])))
        row: dict[str, object] = {
            "candidate": candidate,
            "horizon": horizon,
            "locked_start": locked_boundary.date().isoformat(),
            "mature_evaluation_days": mature_days,
            "minimum_evaluation_days": minimum_evaluation_days,
        }
        if mature_days < minimum_evaluation_days:
            row["status"] = "insufficient_locked_oos"
            rows.append(row)
            continue
        metrics = evaluate_factor(locked_snapshots, locked_labels, candidate, horizon)
        strategy = simulate_top_group_strategy(
            dated_snapshots,
            locked_labels,
            candidate,
            rebalance_every=1,
            cost_bps=cost_bps,
        )
        mean_rank_ic = float(metrics["rank_ic_mean"])
        top_group_return = float(metrics["top_group_return"])
        net_return = float(strategy["net_return"])
        row.update({
            "status": "evaluated_locked_oos",
            **metrics,
            "cost_bps": cost_bps,
            "net_return": net_return,
            "candidate_valid": bool(mean_rank_ic > 0 and top_group_return > 0 and net_return > 0),
        })
        rows.append(row)
    return pd.DataFrame(rows)


def run_locked_oos_monitor(
    level: int,
    end_date: str,
    model_version: str,
    frozen_selection_path: str | Path,
    locked_start: str,
    output_dir: str | Path,
    minimum_evaluation_days: int = 63,
) -> pd.DataFrame:
    """Evaluate a supplied frozen candidate only after the Locked OOS boundary."""
    selection_path = Path(frozen_selection_path)
    frozen_selection = pd.read_json(selection_path) if selection_path.suffix.lower() == ".json" else pd.read_csv(selection_path)
    required_columns = {"candidate", "horizon"}
    if not required_columns.issubset(frozen_selection.columns):
        raise ValueError("frozen selection must contain candidate and horizon columns")
    labels = build_forward_return_labels(level, locked_start, end_date).copy()
    labels["as_of_date"] = pd.to_datetime(labels["as_of_date"])
    labels["target_date"] = pd.to_datetime(labels["target_date"])
    snapshots = pd.DataFrame(execute_query(
        "SELECT " + SNAPSHOT_COMPONENT_COLUMNS + " FROM sector_rotation_sector_daily_snapshot "
        "WHERE sector_level = %s AND model_version = %s AND as_of_date BETWEEN %s AND %s",
        (level, model_version, locked_start, end_date),
    ))
    snapshots["as_of_date"] = pd.to_datetime(snapshots["as_of_date"])
    candidates = build_candidate_scores(snapshots)
    result = evaluate_locked_oos(
        candidates,
        labels,
        frozen_selection.loc[:, ["candidate", "horizon"]],
        locked_start,
        minimum_evaluation_days=minimum_evaluation_days,
    )
    destination = Path(output_dir)
    destination.mkdir(parents=True, exist_ok=True)
    result.to_csv(destination / f"sector_rotation2_v2_locked_oos_{end_date}.csv", index=False, encoding="utf-8-sig")
    return result


def main() -> None:
    """Parse CLI arguments and run frozen nested historical research."""
    parser = argparse.ArgumentParser(description="Run P1 Score V2 nested historical research")
    parser.add_argument("--level", type=int, required=True)
    parser.add_argument("--start-date")
    parser.add_argument("--end-date", required=True)
    parser.add_argument("--model-version", default="v1")
    parser.add_argument("--output", default="outputs")
    parser.add_argument("--frozen-selection")
    parser.add_argument("--locked-start", default="2026-06-12")
    args = parser.parse_args()
    if args.frozen_selection:
        run_locked_oos_monitor(
            args.level,
            args.end_date,
            args.model_version,
            args.frozen_selection,
            args.locked_start,
            args.output,
        )
    elif args.start_date:
        run_nested_research(args.level, args.start_date, args.end_date, args.model_version, args.output)
    else:
        parser.error("--start-date is required unless --frozen-selection is supplied")


if __name__ == "__main__":
    main()

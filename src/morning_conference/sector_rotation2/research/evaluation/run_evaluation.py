"""Materialize coverage-aware evaluation metrics from persisted forward labels."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import date
from uuid import uuid4

import pandas as pd

from data_ingestion.db_config import execute_query, get_connection

from .config import DEFAULT_EVALUATION_CONFIG
from .metrics import evaluate_condition
from .bootstrap import moving_block_bootstrap_ci
from .store import ensure_evaluation_tables, persist_evaluation_header, persist_evaluation_metrics
from .oos import build_purged_oos_windows, signal_scope
from .prices import load_authoritative_market_calendar


def run(
    *, snapshot_mode: str, start_date: date, end_date: date, oos: bool = False,
    strategy_type: str | None = None,
) -> dict[str, object]:
    query = """SELECT f.*, s.strategy_type, s.model_version AS upstream_model_version
             FROM sector_rotation_research_forward_label f
             JOIN research_candidate_snapshot s ON s.id=f.source_snapshot_id AND s.snapshot_mode=f.snapshot_mode
            WHERE f.snapshot_mode=%s AND f.signal_date BETWEEN %s AND %s
              AND NOT (s.strategy_type='stock_repair' AND s.validation_status='rejected')
        """
    params: tuple[object, ...] = (snapshot_mode, start_date, end_date)
    if strategy_type is not None:
        query += "AND s.strategy_type=%s "
        params += (strategy_type,)
    rows = execute_query(query + "ORDER BY f.signal_date, f.id", params)
    if not rows:
        return {"snapshot_mode": snapshot_mode, "groups": 0, "metrics": 0}
    frame = pd.DataFrame(rows)
    run_id = f"evaluation-{snapshot_mode}-{uuid4().hex[:12]}"
    connection = get_connection()
    groups = metrics_count = 0
    windows = ()
    if oos:
        market_dates = load_authoritative_market_calendar(start_date, end_date, execute_query, sector_level=2)
        # Windows are built per horizon below; no window is a valid result when
        # the authoritative calendar lacks the configured train/validation/test coverage.
    try:
        ensure_evaluation_tables(connection)
        grouped = frame.groupby(["strategy_type", "horizon", "label_type"], dropna=False)
        work_items = []
        for (strategy_key, horizon_key, label_key), group in grouped:
            if not oos:
                work_items.append(((strategy_key, horizon_key, label_key), group, "full", None))
                continue
            group_windows = build_purged_oos_windows(market_dates, int(horizon_key), DEFAULT_EVALUATION_CONFIG)
            windows = group_windows or windows
            for window in group_windows:
                for scope in ("train", "validation", "test"):
                    selected = group[group["signal_date"].map(lambda value: signal_scope(window, value) == scope)]
                    if not selected.empty:
                        work_items.append(((strategy_key, horizon_key, label_key), selected, scope, window))
        for (strategy, horizon, label_type), group, sample_scope, window in work_items:
            group = group.copy()
            group["signal_event_id"] = group["source_snapshot_id"].astype(str)
            header_counts, metrics = evaluate_condition(
                group,
                # Candidate score is not persisted in the label table; rank metrics
                # therefore remain unavailable until a score adapter is supplied.
                _macd_spec(str(strategy)),
                min_cross_section_pairs=DEFAULT_EVALUATION_CONFIG.min_cross_section_pairs,
                round_trip_cost_bps=DEFAULT_EVALUATION_CONFIG.round_trip_cost_bps,
            )
            model_version = str(group["upstream_model_version"].iloc[0])
            header_id = persist_evaluation_header(connection, {
                "signal_family": str(strategy), "signal_model_version": model_version,
                "condition_key": "forward_return", "horizon": int(horizon), "label_type": str(label_type),
                "event_sampling_mode": "snapshot", "sample_scope": sample_scope, "snapshot_mode": snapshot_mode,
                "candidate_count": header_counts["candidate_count"], "unique_event_count": header_counts["unique_event_count"],
                "return_complete_count": header_counts["return_complete_count"], "excess_complete_count": header_counts["excess_complete_count"],
                "path_complete_count": header_counts["path_complete_count"], "model_version": "evaluation_metrics_v1",
                "config_hash": "evaluation-metrics-v1", "run_id": run_id,
            })
            metrics_count += persist_evaluation_metrics(connection, header_id, metrics)
            complete = group[group["forward_return"].notna()].copy()
            if not complete.empty:
                ci_low, ci_high = moving_block_bootstrap_ci(
                    complete.rename(columns={"signal_date": "bootstrap_date"}),
                    lambda sample: float(sample["forward_return"].mean()),
                    date_col="bootstrap_date", horizon=int(horizon), config=DEFAULT_EVALUATION_CONFIG,
                    seed=int.from_bytes(hashlib.sha256(f"{snapshot_mode}|{strategy}|{horizon}|{label_type}".encode()).digest()[:4], "big"),
                )
                persist_evaluation_metrics(connection, header_id, [{
                    "metric_name": "mean_return", "metric_value": float(complete["forward_return"].mean()),
                    "sample_count": len(complete), "ci_low": ci_low, "ci_high": ci_high,
                }])
            groups += 1
    finally:
        connection.close()
    result = {"snapshot_mode": snapshot_mode, "groups": groups, "metrics": metrics_count, "oos_windows": len(windows) if oos else 0, "run_id": run_id}
    if oos and not windows:
        result["reason"] = "insufficient_market_calendar_coverage"
    return result


def _macd_spec(strategy: str):
    from ..contracts import SignalFrameSpec
    return SignalFrameSpec(strategy, None, (), "signal_event_id", False)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--snapshot-mode", choices=("backfill", "live_shadow", "delayed_shadow"), required=True)
    parser.add_argument("--start-date", required=True, type=date.fromisoformat)
    parser.add_argument("--end-date", required=True, type=date.fromisoformat)
    parser.add_argument("--oos", action="store_true", help="materialize purged train/validation/test scopes")
    parser.add_argument("--strategy-type")
    args = parser.parse_args()
    print(json.dumps(run(
        snapshot_mode=args.snapshot_mode, start_date=args.start_date,
        end_date=args.end_date, oos=args.oos, strategy_type=args.strategy_type,
    ), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

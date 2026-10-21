"""Rebuild Repair Alpha backfill aggregates from corrected forward labels."""

from __future__ import annotations

from datetime import date
import hashlib
import json

import numpy as np
import pandas as pd

from data_ingestion.db_config import execute_query, get_connection
from morning_conference.sector_rotation2.research.contracts import SignalFrameSpec
from morning_conference.sector_rotation2.research.evaluation.config import DEFAULT_EVALUATION_CONFIG, EvaluationConfig
from morning_conference.sector_rotation2.research.evaluation.metrics import evaluate_condition
from morning_conference.sector_rotation2.research.evaluation.store import (
    ensure_evaluation_tables, persist_evaluation_header, persist_evaluation_metrics,
)


def daily_mean_bootstrap_ci(
    frame: pd.DataFrame, *, horizon: int, config: EvaluationConfig, seed: int,
) -> tuple[float | None, float | None]:
    complete = frame.loc[frame["forward_return"].notna(), ["signal_date", "forward_return"]]
    if complete.empty:
        return None, None
    daily = complete.groupby("signal_date")["forward_return"].agg(["sum", "count"])
    sums = daily["sum"].to_numpy(dtype=float)
    counts = daily["count"].to_numpy(dtype=int)
    dates_count = len(daily)
    block_size = max(horizon, config.min_block_size)
    rng = np.random.default_rng(seed)
    means = []
    for _ in range(config.bootstrap_repetitions):
        sampled_indices = []
        while len(sampled_indices) < dates_count:
            start = int(rng.integers(dates_count))
            sampled_indices.extend((start + offset) % dates_count for offset in range(block_size))
        indices = sampled_indices[:dates_count]
        means.append(float(sums[indices].sum() / counts[indices].sum()))
    return float(np.quantile(means, 0.025)), float(np.quantile(means, 0.975))


def rebuild(start_date: date = date(2024, 1, 2), end_date: date = date(2026, 10, 19)) -> dict:
    connection = get_connection()
    try:
        ensure_evaluation_tables(connection)
        result = {}
        for horizon in DEFAULT_EVALUATION_CONFIG.horizons["stock_repair"]:
            rows = execute_query(
                "SELECT f.signal_date,f.source_snapshot_id,f.label_type,f.forward_return,"
                "f.excess_return,f.mae,f.mfe,f.entry_gap,s.model_version "
                "FROM sector_rotation_research_forward_label f "
                "JOIN research_candidate_snapshot s ON s.id=f.source_snapshot_id "
                "WHERE s.strategy_type='stock_repair' AND s.validation_status<>'rejected' "
                "AND s.snapshot_mode='backfill' AND f.snapshot_mode='backfill' "
                "AND f.horizon=%s AND f.signal_date BETWEEN %s AND %s "
                "ORDER BY f.signal_date,f.id",
                (horizon, start_date, end_date),
            )
            if not rows:
                raise ValueError(f"missing Repair Alpha labels for horizon {horizon}")
            frame = pd.DataFrame(rows)
            if frame["label_type"].nunique() != 1 or frame["model_version"].nunique() != 1:
                raise ValueError(f"mixed Repair Alpha label/model groups for horizon {horizon}")
            frame["signal_event_id"] = frame["source_snapshot_id"].astype(str)
            counts, metrics = evaluate_condition(
                frame, SignalFrameSpec("stock_repair", None, (), "signal_event_id", False),
                min_cross_section_pairs=DEFAULT_EVALUATION_CONFIG.min_cross_section_pairs,
                round_trip_cost_bps=DEFAULT_EVALUATION_CONFIG.round_trip_cost_bps,
            )
            seed = int.from_bytes(hashlib.sha256(
                f"backfill|stock_repair|{horizon}|{frame['label_type'].iloc[0]}".encode()
            ).digest()[:4], "big")
            ci_low, ci_high = daily_mean_bootstrap_ci(
                frame, horizon=horizon, config=DEFAULT_EVALUATION_CONFIG, seed=seed,
            )
            for metric in metrics:
                if metric["metric_name"] == "mean_return":
                    metric["ci_low"], metric["ci_high"] = ci_low, ci_high
            header_id = persist_evaluation_header(connection, {
                "signal_family": "stock_repair", "signal_model_version": str(frame["model_version"].iloc[0]),
                "condition_key": "forward_return", "horizon": horizon,
                "label_type": str(frame["label_type"].iloc[0]), "event_sampling_mode": "snapshot",
                "sample_scope": "full", "snapshot_mode": "backfill", **counts,
                "model_version": "evaluation_metrics_v1", "config_hash": "evaluation-metrics-v1",
                "run_id": f"repair-evaluation-20261020-{horizon}",
            })
            persist_evaluation_metrics(connection, header_id, metrics)
            result[str(horizon)] = {"labels": len(frame), "header_id": header_id,
                                    "complete": counts["return_complete_count"]}
        return result
    finally:
        connection.close()


if __name__ == "__main__":
    print(json.dumps(rebuild(), ensure_ascii=False))

"""Persistence functions for forward labels and later aggregate evaluation."""

from collections.abc import Iterable, Mapping
from typing import Any

from ..contracts import ForwardLabel, ResearchContext
from ..status import SnapshotMode
from .schema import EVALUATION_DDL, EVALUATION_METRIC_DDL, FORWARD_LABEL_DDL


def ensure_evaluation_tables(connection: Any) -> None:
    cursor = connection.cursor()
    try:
        for statement in (FORWARD_LABEL_DDL, EVALUATION_DDL, EVALUATION_METRIC_DDL):
            cursor.execute(statement)
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()


def persist_forward_labels(connection: Any, labels: Iterable[ForwardLabel], context: ResearchContext) -> int:
    """Persist matured outcomes idempotently without allowing completed rows to regress."""
    rows = [_label_values(label, context) for label in labels]
    if not rows:
        return 0
    cursor = connection.cursor()
    try:
        snapshot_ids = sorted({row[0] for row in rows})
        placeholders = ",".join(["%s"] * len(snapshot_ids))
        cursor.execute(
            "SELECT id,snapshot_mode FROM research_candidate_snapshot "
            "WHERE id IN (" + placeholders + ") "
            "AND NOT (strategy_type='stock_repair' AND validation_status='rejected') FOR SHARE",
            snapshot_ids,
        )
        eligible = {(int(row[0]), str(row[1])) for row in cursor.fetchall()}
        rows = [row for row in rows if (int(row[0]), str(row[1])) in eligible]
        if not rows:
            connection.commit()
            return 0
        cursor.executemany(_FORWARD_LABEL_UPSERT, rows)
        connection.commit()
        return cursor.rowcount
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()


def persist_evaluation_header(connection: Any, header: Mapping[str, Any]) -> int:
    """Insert/update a homogeneous evaluation header and return its database ID."""
    required = {
        "signal_family", "signal_model_version", "condition_key", "horizon", "label_type", "event_sampling_mode",
        "sample_scope", "snapshot_mode", "model_version", "config_hash", "run_id",
    }
    missing = sorted(required.difference(header))
    if missing:
        raise ValueError(f"evaluation header missing fields: {', '.join(missing)}")
    columns = (
        "signal_family", "signal_model_version", "condition_key", "horizon", "label_type", "event_sampling_mode",
        "sample_scope", "snapshot_mode", "oos_window_id", "train_start", "train_end", "validation_start",
        "validation_end", "test_start", "test_end", "candidate_count", "unique_event_count", "return_complete_count",
        "excess_complete_count", "path_complete_count", "model_version", "config_hash", "run_id",
    )
    values = tuple(header.get(column, _HEADER_DEFAULTS.get(column)) for column in columns)
    cursor = connection.cursor()
    try:
        cursor.execute(_EVALUATION_HEADER_UPSERT, values)
        connection.commit()
        return int(cursor.lastrowid)
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()


def persist_evaluation_metrics(connection: Any, evaluation_id: int, metrics: Iterable[Mapping[str, Any]]) -> int:
    rows = [(
        evaluation_id, metric["metric_name"], metric.get("metric_value"), metric.get("sample_count", 0),
        metric.get("ci_low"), metric.get("ci_high"),
    ) for metric in metrics]
    if not rows:
        return 0
    cursor = connection.cursor()
    try:
        cursor.executemany(_EVALUATION_METRIC_UPSERT, rows)
        connection.commit()
        return cursor.rowcount
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()


def _label_values(label: ForwardLabel, context: ResearchContext) -> tuple[Any, ...]:
    if label.source_snapshot_id is None or label.snapshot_mode is None:
        raise ValueError("forward labels require immutable source_snapshot_id and snapshot_mode")
    snapshot_mode = label.snapshot_mode.value if isinstance(label.snapshot_mode, SnapshotMode) else str(label.snapshot_mode)
    return (
        label.source_snapshot_id, snapshot_mode, label.signal_date, label.entity_type, label.entity_code,
        label.benchmark_type or "none", label.benchmark_code or "", label.horizon, label.label_type, label.price_basis,
        label.entry_date, label.exit_date, label.signal_close, label.entry_price, label.exit_price, label.entry_gap,
        label.forward_return, label.benchmark_return, label.excess_return, label.mae, label.mfe,
        label.return_status.value, label.path_status.value, label.benchmark_status.value,
        int(label.is_complete), int(label.excess_is_complete), context.model_version, context.config_hash, context.run_id,
    )


_FORWARD_LABEL_UPSERT = """
INSERT INTO sector_rotation_research_forward_label (
    source_snapshot_id, snapshot_mode, signal_date, entity_type, entity_code, benchmark_type, benchmark_code,
    horizon, label_type, price_basis, entry_date, exit_date, signal_close, entry_price, exit_price, entry_gap,
    forward_return, benchmark_return, excess_return, mae, mfe, return_status, path_status, benchmark_status,
    is_complete, excess_is_complete, label_model_version, label_config_hash, run_id
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
ON DUPLICATE KEY UPDATE
    signal_date=VALUES(signal_date), entity_type=VALUES(entity_type), entity_code=VALUES(entity_code),
    entry_date=CASE WHEN is_complete=1 AND VALUES(is_complete)=0 THEN entry_date ELSE VALUES(entry_date) END,
    exit_date=CASE WHEN is_complete=1 AND VALUES(is_complete)=0 THEN exit_date ELSE VALUES(exit_date) END,
    signal_close=CASE WHEN is_complete=1 AND VALUES(is_complete)=0 THEN signal_close ELSE VALUES(signal_close) END,
    entry_price=CASE WHEN is_complete=1 AND VALUES(is_complete)=0 THEN entry_price ELSE VALUES(entry_price) END,
    exit_price=CASE WHEN is_complete=1 AND VALUES(is_complete)=0 THEN exit_price ELSE VALUES(exit_price) END,
    entry_gap=CASE WHEN is_complete=1 AND VALUES(is_complete)=0 THEN entry_gap ELSE VALUES(entry_gap) END,
    forward_return=CASE WHEN is_complete=1 AND VALUES(is_complete)=0 THEN forward_return ELSE VALUES(forward_return) END,
    benchmark_return=CASE WHEN is_complete=1 AND VALUES(is_complete)=0 THEN benchmark_return ELSE VALUES(benchmark_return) END,
    excess_return=CASE WHEN is_complete=1 AND VALUES(is_complete)=0 THEN excess_return ELSE VALUES(excess_return) END,
    mae=CASE WHEN is_complete=1 AND VALUES(is_complete)=0 THEN mae ELSE VALUES(mae) END,
    mfe=CASE WHEN is_complete=1 AND VALUES(is_complete)=0 THEN mfe ELSE VALUES(mfe) END,
    return_status=CASE WHEN is_complete=1 AND VALUES(is_complete)=0 THEN return_status ELSE VALUES(return_status) END,
    path_status=CASE WHEN is_complete=1 AND VALUES(is_complete)=0 THEN path_status ELSE VALUES(path_status) END,
    benchmark_status=CASE WHEN is_complete=1 AND VALUES(is_complete)=0 THEN benchmark_status ELSE VALUES(benchmark_status) END,
    is_complete=CASE WHEN is_complete=1 AND VALUES(is_complete)=0 THEN is_complete ELSE VALUES(is_complete) END,
    excess_is_complete=CASE WHEN is_complete=1 AND VALUES(is_complete)=0 THEN excess_is_complete ELSE VALUES(excess_is_complete) END,
    run_id=VALUES(run_id)
"""

_HEADER_DEFAULTS = {
    "oos_window_id": "full", "train_start": None, "train_end": None, "validation_start": None,
    "validation_end": None, "test_start": None, "test_end": None, "candidate_count": 0,
    "unique_event_count": 0, "return_complete_count": 0, "excess_complete_count": 0, "path_complete_count": 0,
}

_EVALUATION_HEADER_UPSERT = """
INSERT INTO sector_rotation_research_evaluation (
    signal_family, signal_model_version, condition_key, horizon, label_type, event_sampling_mode, sample_scope,
    snapshot_mode, oos_window_id, train_start, train_end, validation_start, validation_end, test_start, test_end,
    candidate_count, unique_event_count, return_complete_count, excess_complete_count, path_complete_count,
    model_version, config_hash, run_id
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
ON DUPLICATE KEY UPDATE
    candidate_count=VALUES(candidate_count), unique_event_count=VALUES(unique_event_count),
    return_complete_count=VALUES(return_complete_count), excess_complete_count=VALUES(excess_complete_count),
    path_complete_count=VALUES(path_complete_count), run_id=VALUES(run_id), id=LAST_INSERT_ID(id)
"""

_EVALUATION_METRIC_UPSERT = """
INSERT INTO sector_rotation_research_evaluation_metric
    (evaluation_id, metric_name, metric_value, sample_count, ci_low, ci_high)
VALUES (%s, %s, %s, %s, %s, %s)
ON DUPLICATE KEY UPDATE metric_value=VALUES(metric_value), sample_count=VALUES(sample_count),
    ci_low=VALUES(ci_low), ci_high=VALUES(ci_high)
"""

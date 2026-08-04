"""Transactional persistence for versioned sector-rotation daily snapshots."""
from __future__ import annotations

from typing import Any
from datetime import datetime

import pandas as pd

from data_ingestion.db_config import get_connection


SNAPSHOT_COLUMNS = (
    "as_of_date", "sector_level", "sector_name", "model_version", "run_id",
    "membership_asof_mode", "coverage_ratio", "score_eligible", "base_score",
    "composite_score", "composite_rank", "phase_raw", "phase_confirmed",
    "phase_confidence", "market_regime",
)


def _execute_update(sql: str, params: tuple[Any, ...]) -> int:
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(sql, params)
        connection.commit()
        return cursor.rowcount
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()
        connection.close()


def create_run(
    run_id: str,
    as_of_date: str,
    sector_level: int,
    model_version: str,
    config_hash: str,
    source_max_trade_date: str,
) -> int:
    """Create a durable running audit record before any daily persistence."""
    return _execute_update(
        """
        INSERT INTO sector_rotation_run_log
            (run_id, as_of_date, sector_level, model_version, config_hash,
             source_max_trade_date, status, started_at)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (run_id, as_of_date, sector_level, model_version, config_hash,
         source_max_trade_date, "running", datetime.now()),
    )


def mark_run_failed(run_id: str, error_summary: str) -> int:
    """Mark an existing audit record failed after the data transaction rolls back."""
    return _execute_update(
        """
        UPDATE sector_rotation_run_log
        SET status = %s, error_summary = %s, finished_at = NOW()
        WHERE run_id = %s
        """,
        ("failed", error_summary, run_id),
    )


def persist_daily_snapshot(
    frame: pd.DataFrame,
    as_of_date: str,
    sector_level: int,
    model_version: str,
    run_id: str,
) -> int:
    """Upsert one day's sector rows in one database transaction."""
    rows: list[tuple[Any, ...]] = []
    for sector_name, row in frame.iterrows():
        name = row.get("sector_name", sector_name)
        rows.append((
            as_of_date, sector_level, name, model_version, run_id,
            row.get("membership_asof_mode", "current_mapping"), row.get("coverage_ratio"),
            bool(row.get("score_eligible", False)), row.get("base_score"),
            row.get("composite_score"), row.get("composite_rank"), row.get("phase_raw"),
            row.get("phase_confirmed"), row.get("phase_confidence"), row.get("market_regime"),
        ))
    if not rows:
        return 0

    placeholders = ", ".join(["%s"] * len(SNAPSHOT_COLUMNS))
    sql = f"""
        INSERT INTO sector_rotation_sector_daily_snapshot ({", ".join(SNAPSHOT_COLUMNS)})
        VALUES ({placeholders})
        ON DUPLICATE KEY UPDATE
            run_id = VALUES(run_id), membership_asof_mode = VALUES(membership_asof_mode),
            coverage_ratio = VALUES(coverage_ratio), score_eligible = VALUES(score_eligible),
            base_score = VALUES(base_score), composite_score = VALUES(composite_score),
            composite_rank = VALUES(composite_rank), phase_raw = VALUES(phase_raw),
            phase_confirmed = VALUES(phase_confirmed), phase_confidence = VALUES(phase_confidence),
            market_regime = VALUES(market_regime)
    """
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.executemany(sql, rows)
        connection.commit()
        return cursor.rowcount
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()
        connection.close()

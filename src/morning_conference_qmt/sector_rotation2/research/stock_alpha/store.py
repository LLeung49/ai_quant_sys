"""Persistence boundary for SHADOW Trend Alpha stock candidates.

Trend Alpha does re does not own its own snapshot table.  It reuses the unified
``research_candidate_snapshot`` table introduced in Phase 0, with
``entity_type='stock'`` and ``strategy_type='stock_trend'``.  The only
domain-specific persistence concerns are:

- ``rank_in_sector INT NULL`` column on the snapshot table (added by
  :func:`ensure_research_candidate_snapshot_extensions`).
- Eligibility columns (``listing_date`` / ``is_suspended`` / ``is_tradable``)
  on ``trade_stock_status`` so :mod:`common` can gate the universe without
  silently dropping rows with missing metadata.

All migrations are idempotent: every column is checked against
``information_schema.columns`` before being added, so re-running the
helpers on already-migrated databases is a safe no-op.
"""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

import pymysql

from data_ingestion_qmt.db_config import get_connection


RESEARCH_CANDIDATE_SNAPSHOT_RANK_DDL = """
ALTER TABLE research_candidate_snapshot
    ADD COLUMN rank_in_sector INT NULL
"""

RESEARCH_CANDIDATE_SNAPSHOT_RANK_INDEX_DDL = """
ALTER TABLE research_candidate_snapshot
    ADD INDEX idx_research_rank (
        as_of_date, sector_level, sector_name, strategy_type, rank_in_sector
    )
"""

_TRADE_STOCK_STATUS_ELIGIBILITY_COLUMNS = {
    "listing_date": "DATE NULL COMMENT 'Stock listing date; null means unknown (eligibility_unknown)'",
    "is_suspended": "TINYINT(1) NULL COMMENT 'Latest suspension flag; null means unknown'",
    "is_tradable": "TINYINT(1) NULL COMMENT 'Latest tradable flag; null means unknown'",
}


def _ensure_rank_column(cursor: pymysql.cursors.Cursor) -> None:
    cursor.execute(
        """SELECT 1 FROM information_schema.columns
            WHERE table_schema = DATABASE()
              AND table_name = 'research_candidate_snapshot'
              AND column_name = 'rank_in_sector'"""
    )
    if cursor.fetchone() is None:
        cursor.execute(RESEARCH_CANDIDATE_SNAPSHOT_RANK_DDL)


def _ensure_rank_index(cursor: pymysql.cursors.Cursor) -> None:
    cursor.execute(
        """SELECT 1 FROM information_schema.statistics
            WHERE table_schema = DATABASE()
              AND table_name = 'research_candidate_snapshot'
              AND index_name = 'idx_research_rank'"""
    )
    if cursor.fetchone() is None:
        cursor.execute(RESEARCH_CANDIDATE_SNAPSHOT_RANK_INDEX_DDL)


def _ensure_trade_stock_status_column(
    cursor: pymysql.cursors.Cursor, column_name: str, column_ddl: str,
) -> None:
    cursor.execute(
        """SELECT 1 FROM information_schema.columns
            WHERE table_schema = DATABASE()
              AND table_name = 'trade_stock_status'
              AND column_name = %s""",
        (column_name,),
    )
    if cursor.fetchone() is None:
        cursor.execute(
            f"ALTER TABLE trade_stock_status ADD COLUMN {column_name} {column_ddl}"
        )


def ensure_research_candidate_snapshot_extensions(
    connection_factory: Callable[[], Any] = get_connection,
) -> None:
    """Ensure Trend Alpha's ``rank_in_sector`` column and index exist."""

    connection = connection_factory()
    cursor = connection.cursor()
    try:
        _ensure_rank_column(cursor)
        _ensure_rank_index(cursor)
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()
        connection.close()


def ensure_trade_stock_status_eligibility(
    connection_factory: Callable[[], Any] = get_connection,
) -> None:
    """Ensure Trend Alpha eligibility columns exist on ``trade_stock_status``.

    Adds ``listing_date`` / ``is_suspended`` / ``is_tradable`` as nullable
    columns.  Idempotent: re-running is a no-op.
    """

    connection = connection_factory()
    cursor = connection.cursor()
    try:
        for column_name, column_ddl in _TRADE_STOCK_STATUS_ELIGIBILITY_COLUMNS.items():
            _ensure_trade_stock_status_column(cursor, column_name, column_ddl)
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()
        connection.close()


def ensure_research_schema(
    connection_factory: Callable[[], Any] = get_connection,
) -> None:
    """Run every Phase 3 idempotent migration in one call.

    This is invoked by :mod:`run_trend_daily` so the CLI is self-bootstrapping
    against a fresh deployment.
    """

    ensure_research_candidate_snapshot_extensions(connection_factory)
    ensure_trade_stock_status_eligibility(connection_factory)


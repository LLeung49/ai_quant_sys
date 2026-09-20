"""Read-only adapter for the existing MACD entity-daily calculation."""

from collections.abc import Callable
from datetime import date
from typing import Any

from data_ingestion_qmt.db_config import execute_query


def load_etf_macd_evidence(
    etf_code: str, as_of_date: date,
    query: Callable[[str, tuple[object, ...]], list[dict[str, Any]]] = execute_query,
) -> dict[str, Any] | None:
    rows = query(
        """SELECT is_triggered AS macd_triggered, gc_offset, adx_14 AS adx, rsi_14 AS rsi,
                  kama_efficiency AS trend_quality, above_ma60
             FROM sector_rotation_macd_entity_daily
             WHERE as_of_date=%s AND entity_type='etf' AND stock_code=%s
             ORDER BY model_version DESC LIMIT 1""",
        (as_of_date, etf_code),
    )
    return rows[0] if rows else None


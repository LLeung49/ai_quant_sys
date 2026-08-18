"""Read-only ETF liquidity and price-extension evidence."""

from collections.abc import Callable
from datetime import date
import math
from typing import Any

from data_ingestion.db_config import execute_query


EXECUTION_WINDOW = 20
MIN_AVG_AMOUNT_20 = 10_000_000.0
MAX_EXTENSION_FROM_MA20 = 0.10


def load_etf_execution_evidence(
    etf_code: str,
    as_of_date: date,
    query: Callable[[str, tuple[object, ...]], list[dict[str, Any]]] = execute_query,
    *,
    min_avg_amount_20: float = MIN_AVG_AMOUNT_20,
    max_extension_from_ma20: float = MAX_EXTENSION_FROM_MA20,
) -> dict[str, Any] | None:
    """Derive same-date execution evidence from the read-only QFQ price table.

    Incomplete, stale, or invalid windows return ``None`` so candidate
    selection fails closed instead of inventing liquidity or extension flags.
    """

    if min_avg_amount_20 < 0:
        raise ValueError("min_avg_amount_20 must be non-negative")
    if max_extension_from_ma20 < 0:
        raise ValueError("max_extension_from_ma20 must be non-negative")
    rows = query(
        """SELECT trade_date, close_price, amount
             FROM trade_stock_daily_qfq
             WHERE stock_code=%s AND trade_date <= %s
             ORDER BY trade_date DESC
             LIMIT 20""",
        (etf_code, as_of_date),
    )
    if len(rows) < EXECUTION_WINDOW or _as_date(rows[0].get("trade_date")) != as_of_date:
        return None

    closes: list[float] = []
    amounts: list[float] = []
    for row in rows[:EXECUTION_WINDOW]:
        close = _finite_number(row.get("close_price"))
        amount = _finite_number(row.get("amount"))
        if close is None or close <= 0 or amount is None or amount < 0:
            return None
        closes.append(close)
        amounts.append(amount)
    ma20 = sum(closes) / EXECUTION_WINDOW
    avg_amount_20 = sum(amounts) / EXECUTION_WINDOW
    distance_ma20 = closes[0] / ma20 - 1.0
    return {
        "liquid": avg_amount_20 >= min_avg_amount_20,
        "extended": distance_ma20 >= max_extension_from_ma20,
        "avg_amount_20": avg_amount_20,
        "min_avg_amount_20": min_avg_amount_20,
        "distance_ma20": distance_ma20,
        "max_extension_from_ma20": max_extension_from_ma20,
        "execution_evidence_as_of_date": as_of_date.isoformat(),
        "execution_evidence_source": "trade_stock_daily_qfq",
    }


def _as_date(value: object) -> date | None:
    if type(value) is date:
        return value
    try:
        return date.fromisoformat(str(value))
    except (TypeError, ValueError):
        return None


def _finite_number(value: object) -> float | None:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    return number if math.isfinite(number) else None

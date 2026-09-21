"""Fail-closed integrity checks for independent raw and QFQ price projections."""

from dataclasses import dataclass
from decimal import Decimal, InvalidOperation

try:
    from .db_config import execute_query
except ImportError:  # Direct collector execution from src/data_ingestion_qmt.
    from db_config import execute_query


PRICE_COLUMNS = ("open_price", "high_price", "low_price", "close_price")
PRICE_TOLERANCE = Decimal("0.000001")

SELECT_RAW_ROWS_SQL = """
SELECT stock_code, trade_date, open_price, high_price, low_price, close_price
FROM trade_stock_daily_raw
WHERE stock_code = %s
ORDER BY trade_date
"""

SELECT_QFQ_ROWS_SQL = """
SELECT stock_code, trade_date, open_price, high_price, low_price, close_price,
       adjustment_asof
FROM trade_stock_daily_qfq
WHERE stock_code = %s
ORDER BY trade_date
"""


@dataclass(frozen=True)
class RawQfqIssue:
    stock_code: str
    trade_date: str
    reason: str


def _decimal(value) -> Decimal:
    try:
        return Decimal(str(value))
    except (InvalidOperation, ValueError, TypeError) as exc:
        raise ValueError(f"invalid price value: {value!r}") from exc


def find_raw_qfq_issues(
    raw_rows: list[dict], qfq_rows: list[dict], *, tolerance: Decimal = PRICE_TOLERANCE,
) -> list[RawQfqIssue]:
    """Return missing-date and non-uniform-adjustment issues for one instrument.

    A legitimate per-day front-adjustment factor must multiply all four OHLC
    raw prices equally.  The function is side-effect free so a collector can
    validate a provider candidate before persisting it.
    """
    raw_by_date = {str(row["trade_date"]): row for row in raw_rows}
    qfq_by_date = {str(row["trade_date"]): row for row in qfq_rows}
    stock_code = next(
        iter(raw_by_date.values() or qfq_by_date.values()), {}
    ).get("stock_code", "")
    issues: list[RawQfqIssue] = []
    for trade_date in sorted(set(raw_by_date) | set(qfq_by_date)):
        raw = raw_by_date.get(trade_date)
        qfq = qfq_by_date.get(trade_date)
        if raw is None:
            issues.append(RawQfqIssue(stock_code, trade_date, "raw_missing"))
            continue
        if qfq is None:
            issues.append(RawQfqIssue(stock_code, trade_date, "qfq_missing"))
            continue
        points = [
            (_decimal(raw[column]), _decimal(qfq[column]))
            for column in PRICE_COLUMNS
        ]
        first_raw, first_qfq = points[0]
        second = next(
            ((raw_price, qfq_price) for raw_price, qfq_price in points[1:]
             if raw_price != first_raw),
            None,
        )
        if second is None:
            if any(qfq_price != first_qfq for _, qfq_price in points[1:]):
                issues.append(
                    RawQfqIssue(stock_code, trade_date, "qfq_ohlc_affine_mismatch")
                )
            continue
        second_raw, second_qfq = second
        slope = (second_qfq - first_qfq) / (second_raw - first_raw)
        intercept = first_qfq - slope * first_raw
        if slope <= 0 or any(
            abs(qfq_price - (slope * raw_price + intercept))
            > tolerance * max(Decimal("1"), abs(qfq_price))
            for raw_price, qfq_price in points
        ):
            issues.append(
                RawQfqIssue(stock_code, trade_date, "qfq_ohlc_affine_mismatch")
            )
    return issues


def audit_raw_qfq_projection(stock_code: str) -> list[RawQfqIssue]:
    """Read and validate one complete independent raw/QFQ projection pair."""
    raw_rows = execute_query(SELECT_RAW_ROWS_SQL, (stock_code,))
    qfq_rows = execute_query(SELECT_QFQ_ROWS_SQL, (stock_code,))
    return find_raw_qfq_issues(raw_rows, qfq_rows)


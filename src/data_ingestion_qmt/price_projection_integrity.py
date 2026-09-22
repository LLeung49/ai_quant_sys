"""Fail-closed integrity checks for independent raw and QFQ price projections."""

from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
import math

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


@dataclass(frozen=True)
class VerifiedProjectionException:
    stock_code: str
    trade_date: str
    check_code: str
    status: str = "qmt_verified_exception"


@dataclass(frozen=True)
class ProjectionDecision:
    """Separate QMT-originated non-affine exceptions from repair cases."""

    hard_issues: list[RawQfqIssue]
    verified_exceptions: list[VerifiedProjectionException]


def _decimal(value) -> Decimal:
    try:
        return Decimal(str(value))
    except (InvalidOperation, ValueError, TypeError) as exc:
        raise ValueError(f"invalid price value: {value!r}") from exc


def _row_is_valid(row: dict | None) -> bool:
    if row is None:
        return False
    try:
        prices = {column: float(row[column]) for column in PRICE_COLUMNS}
        if not all(math.isfinite(value) for value in prices.values()):
            return False
        if not (
            prices["low_price"] <= min(prices["open_price"], prices["close_price"])
            <= max(prices["open_price"], prices["close_price"])
            <= prices["high_price"]
        ):
            return False
        for column in ("volume", "amount"):
            if column in row and row[column] is not None:
                if not math.isfinite(float(row[column])) or float(row[column]) < 0:
                    return False
    except (KeyError, TypeError, ValueError, OverflowError):
        return False
    return True


def _same_stored_prices(stored: dict | None, qmt: dict | None) -> bool:
    """Compare QMT and MySQL price values at the table's six-decimal precision."""
    if stored is None or qmt is None:
        return False
    try:
        return all(
            _decimal(stored[column]).quantize(PRICE_TOLERANCE)
            == _decimal(qmt[column]).quantize(PRICE_TOLERANCE)
            for column in PRICE_COLUMNS
        )
    except (InvalidOperation, ValueError):
        return False


def classify_projection_issues(
    issues: list[RawQfqIssue],
    stored_raw_rows: list[dict],
    stored_qfq_rows: list[dict],
    qmt_raw_rows: list[dict],
    qmt_qfq_rows: list[dict],
) -> ProjectionDecision:
    """Classify audited rows after querying QMT only for non-affine dates.

    A non-affine raw/QFQ relation is a warning only when the current QMT raw
    and front rows exactly match what is stored and both pairs remain valid.
    Every other problem stays fail-closed and is eligible for rebuild.
    """
    stored_raw = {str(row["trade_date"]): row for row in stored_raw_rows}
    stored_qfq = {str(row["trade_date"]): row for row in stored_qfq_rows}
    qmt_raw = {str(row["trade_date"]): row for row in qmt_raw_rows}
    qmt_qfq = {str(row["trade_date"]): row for row in qmt_qfq_rows}
    hard_issues: list[RawQfqIssue] = []
    verified: list[VerifiedProjectionException] = []

    for issue in issues:
        if issue.reason != "qfq_ohlc_affine_mismatch":
            hard_issues.append(issue)
            continue
        trade_date = str(issue.trade_date)
        stored_pair = (stored_raw.get(trade_date), stored_qfq.get(trade_date))
        qmt_pair = (qmt_raw.get(trade_date), qmt_qfq.get(trade_date))
        if (
            all(_row_is_valid(row) for row in (*stored_pair, *qmt_pair))
            and _same_stored_prices(stored_pair[0], qmt_pair[0])
            and _same_stored_prices(stored_pair[1], qmt_pair[1])
        ):
            verified.append(
                VerifiedProjectionException(
                    issue.stock_code, trade_date, "qfq_ohlc_non_affine"
                )
            )
        else:
            hard_issues.append(
                RawQfqIssue(issue.stock_code, trade_date, "qmt_storage_mismatch")
            )
    return ProjectionDecision(hard_issues, verified)


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
    raw_rows, qfq_rows = load_raw_qfq_rows(stock_code)
    return find_raw_qfq_issues(raw_rows, qfq_rows)


def load_raw_qfq_rows(stock_code: str) -> tuple[list[dict], list[dict]]:
    """Load stored raw and QFQ projections for source verification."""
    return (
        execute_query(SELECT_RAW_ROWS_SQL, (stock_code,)),
        execute_query(SELECT_QFQ_ROWS_SQL, (stock_code,)),
    )


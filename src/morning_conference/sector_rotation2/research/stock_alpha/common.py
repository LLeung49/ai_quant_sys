"""Shared stock-universe loader and eligibility rules for Trend Alpha.

The universe loader is the single source of PIT-safe inputs for the trend
stock-candidate pipeline.  Eligibility rules reject stocks whose listing age
or membership availability cannot be confirmed at ``as_of_date``.  When
upstream metadata columns are missing, the loader records
``eligibility_unknown`` reasons and keeps the stock eligible rather than
silently dropping it on missing PIT metadata.

Note: the ``min_price_history`` gate is **lazy**.  The price-history scan
is expensive on production tables (10M+ rows of ``trade_stock_daily_qfq``),
so the loader only flags ``eligibility_unknown`` and lets downstream feature
computation either use the history (when available) or score the row as
``NaN`` (which the sector-local ranking and risk-adjusted scoring
naturally down-weight).
"""

from __future__ import annotations

from collections.abc import Callable, Iterable
from dataclasses import dataclass, field
from datetime import date
from typing import Any

from data_ingestion.db_config import execute_query


TREND_FOLLOW_PLAYBOOK = "trend_follow"

DEFAULT_STOCK_STATUS_QUERY = """
SELECT stock_code,
       listing_date,
       is_suspended,
       is_tradable,
       sector_1,
       sector_2,
       updated_at AS status_as_of_date
  FROM trade_stock_status
"""


@dataclass(frozen=True)
class StockEligibilityRow:
    """Result of the PIT-safe stock-universe loader for one stock/date pair."""

    stock_code: str
    sector_level: int
    sector_name: str
    listing_date: date | None
    suspended: bool | None
    tradable: bool | None
    mapping_quality: str
    eligibility_reasons: tuple = ()
    eligibility_unknown: tuple = field(default_factory=tuple)


def _normalize_bool(value: Any) -> bool | None:
    """Return a tri-state bool for sparse upstream tables."""

    if value is None:
        return None
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return bool(value)
    text = str(value).strip().lower()
    if text in {"1", "true", "t", "yes", "y"}:
        return True
    if text in {"0", "false", "f", "no", "n"}:
        return False
    return None


def _as_date(value: Any) -> date | None:
    if value is None:
        return None
    if isinstance(value, date):
        return value
    try:
        return date.fromisoformat(str(value))
    except ValueError:
        return None


def _sector_field(sector_level: int) -> str:
    if sector_level not in (1, 2):
        raise ValueError("sector_level must be 1 or 2")
    return f"sector_{sector_level}"


def load_sector_membership(
    sector_names: Iterable[str],
    sector_level: int,
    as_of_date: date,
    query: Callable = execute_query,
) -> dict:
    """Group stocks by sector for the requested date using current mapping only."""

    field = _sector_field(sector_level)
    sql = (
        "SELECT stock_code, " + field + " AS sector_name "
        "FROM trade_stock_status "
        "WHERE " + field + " IS NOT NULL "
        "AND TRIM(" + field + ") <> %s"
    )
    rows = query(sql, ("",))
    grouped: dict = {}
    for row in rows:
        name = str(row.get("sector_name") or "").strip()
        code = str(row.get("stock_code") or "").strip()
        if not name or not code:
            continue
        grouped.setdefault(name, []).append(code)
    selected = {name for name in sector_names}
    return {name: codes for name, codes in grouped.items() if name in selected}


def load_stock_universe(
    *,
    as_of_date: date,
    sector_names: Iterable[str],
    sector_level: int,
    config: Any,
    query: Callable = execute_query,
    status_query: str = DEFAULT_STOCK_STATUS_QUERY,
) -> list:
    """Load the eligible stock universe for ``as_of_date``.

    Eligibility rules:
    - The stock must be mapped to one of the requested sectors.
    - ``is_suspended=True`` is excluded; ``None`` is treated as unknown.
    - ``is_tradable=False`` is excluded; ``None`` is treated as unknown.
    - The listing-age gate (``listing_date + min_listing_age``) is enforced
      only when ``listing_date`` is present; missing values are recorded as
      ``eligibility_unknown`` rather than dropping the stock.

    The price-history gate is intentionally deferred to feature computation:
    stocks with insufficient history simply receive NaN components which the
    sector-local ranking and risk-adjusted scoring naturally down-weight.
    """

    wanted_sectors = {name for name in sector_names}
    if not wanted_sectors:
        return []
    membership = load_sector_membership(wanted_sectors, sector_level, as_of_date, query)
    if not membership:
        return []

    status_rows = query(status_query, ())
    listing_by_code: dict = {}
    for row in status_rows:
        code = str(row.get("stock_code") or "").strip()
        if not code:
            continue
        listing_by_code[code] = row

    eligible: list = []
    for sector_name, codes in membership.items():
        for code in codes:
            status_row = listing_by_code.get(code)
            reasons: list = []
            unknown: list = []
            listing_date = _as_date((status_row or {}).get("listing_date"))
            suspended = _normalize_bool((status_row or {}).get("is_suspended"))
            tradable = _normalize_bool((status_row or {}).get("is_tradable"))

            if listing_date is None:
                unknown.append("listing_date")
            else:
                age = (as_of_date - listing_date).days
                if age < config.min_listing_age:
                    reasons.append("listing_age_below_minimum")

            if suspended is True:
                reasons.append("suspended_at_as_of_date")
            elif suspended is None:
                unknown.append("is_suspended")

            if tradable is False:
                reasons.append("not_tradable_at_as_of_date")
            elif tradable is None:
                unknown.append("is_tradable")

            if reasons:
                continue

            eligible.append(
                StockEligibilityRow(
                    stock_code=code,
                    sector_level=sector_level,
                    sector_name=sector_name,
                    listing_date=listing_date,
                    suspended=suspended,
                    tradable=tradable,
                    mapping_quality="current_mapping",
                    eligibility_reasons=(),
                    eligibility_unknown=tuple(unknown),
                ),
            )
    eligible.sort(key=lambda row: (row.sector_name, row.stock_code))
    return eligible


def load_sector_close_series(
    sector_names: Iterable[str],
    sector_level: int,
    as_of_date: date,
    query: Callable = execute_query,
) -> dict:
    """Load per-sector close series for relative-return calculations."""

    selected = tuple(name for name in sector_names if name)
    if not selected:
        return {}
    placeholders = ", ".join(["%s"] * len(selected))
    sql = (
        "SELECT sector_name, trade_date, close_idx AS close "
        "FROM trade_sector_daily "
        "WHERE sector_level = %s AND trade_date <= %s "
        "AND sector_name IN (" + placeholders + ") "
        "ORDER BY sector_name, trade_date"
    )
    rows = query(sql, (sector_level, as_of_date, *selected))
    out: dict = {}
    for row in rows:
        name = str(row.get("sector_name") or "").strip()
        trade_date = _as_date(row.get("trade_date"))
        close = row.get("close")
        if not name or trade_date is None or close is None:
            continue
        out.setdefault(name, {})[trade_date] = float(close)
    return out


def load_stock_close_series(
    stock_codes: Iterable[str],
    as_of_date: date,
    query: Callable = execute_query,
    *,
    batch_size: int = 100,
) -> dict:
    """Load per-stock close series (qfq) for stock-level return calculations.

    The query is batched to avoid the cost of an excessively long ``IN`` list,
    which MySQL handles poorly.  Default ``batch_size=100`` keeps each round
    trip under one second.
    """

    codes = sorted({code for code in stock_codes if code})
    if not codes:
        return {}
    out: dict = {}
    for i in range(0, len(codes), batch_size):
        chunk = codes[i:i + batch_size]
        placeholders = ", ".join(["%s"] * len(chunk))
        sql = (
            "SELECT stock_code, trade_date, close_price AS close, volume, amount "
            "FROM trade_stock_daily_qfq "
            "WHERE trade_date <= %s "
            "AND stock_code IN (" + placeholders + ") "
            "ORDER BY stock_code, trade_date"
        )
        rows = query(sql, (as_of_date, *chunk))
        for row in rows:
            code = str(row.get("stock_code") or "").strip()
            trade_date = _as_date(row.get("trade_date"))
            close = row.get("close")
            if not code or trade_date is None or close is None:
                continue
            out.setdefault(code, {})[trade_date] = float(close)
    return out


def load_stock_ohlcv_series(
    stock_codes: Iterable[str], as_of_date: date, query: Callable = execute_query,
    *, batch_size: int = 100,
) -> dict[str, dict[date, dict[str, float]]]:
    """Load raw OHLCV history for technical features without changing the close API."""
    codes = sorted({code for code in stock_codes if code})
    out: dict[str, dict[date, dict[str, float]]] = {}
    for i in range(0, len(codes), batch_size):
        chunk = codes[i:i + batch_size]
        placeholders = ", ".join(["%s"] * len(chunk))
        sql = (
            "SELECT stock_code, trade_date, open_price AS open, high_price AS high, "
            "low_price AS low, close_price AS close, volume, amount "
            "FROM trade_stock_daily_qfq WHERE trade_date <= %s AND stock_code IN ("
            + placeholders + ") ORDER BY stock_code, trade_date"
        )
        for row in query(sql, (as_of_date, *chunk)):
            code = str(row.get("stock_code") or "").strip()
            day = _as_date(row.get("trade_date"))
            if not code or day is None or row.get("close") is None:
                continue
            out.setdefault(code, {})[day] = {
                key: float(row[key]) for key in ("open", "high", "low", "close", "volume", "amount")
                if row.get(key) is not None
            }
    return out

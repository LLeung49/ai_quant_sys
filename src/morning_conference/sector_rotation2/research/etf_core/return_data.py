"""Local SW2 and ETF close-price input for return-based mappings."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from datetime import date, datetime
import math
from typing import Any

import pandas as pd

from data_ingestion.db_config import execute_query

from ...macd_pool import ETF_PREFIXES, is_excluded_bond_etf
from .exposure import normalize_stock_code


_NON_DOMESTIC_NAME_KEYWORDS = (
    "货币", "黄金", "商品", "原油", "豆粕", "纳指", "标普", "日经", "恒生", "港股", "跨境",
    "bond", "treasury", "money market", "cash management", "certificate of deposit",
    "commodity", "gold", "crude", "oil", "soybean meal", "nasdaq", "s&p", "nikkei",
    "hang seng", "hong kong", "cross-border", "cross border", "overseas", "global",
)
_ETF_EXCHANGE_BY_PREFIX = {
    "15": "SZ",
    "16": "SZ",
    "50": "SH",
    "51": "SH",
    "56": "SH",
    "58": "SH",
}


@dataclass(frozen=True)
class ReturnMappingInput:
    as_of_date: date
    sector_closes: dict[str, pd.Series]
    etf_closes: dict[str, pd.Series]
    universe_codes: tuple[str, ...]
    price_source: str = "local_trade_daily"


def is_domestic_equity_etf(code: str, name: str | None) -> bool:
    """Return whether a recognized ETF is a domestic-equity product."""

    try:
        normalized_code = normalize_etf_code(code)
    except ValueError:
        return False
    normalized_name = str(name or "").strip().lower()
    if not normalized_name:
        return False
    if not normalized_code.startswith(ETF_PREFIXES) or is_excluded_bond_etf(normalized_code, name):
        return False
    return not any(keyword in normalized_name for keyword in _NON_DOMESTIC_NAME_KEYWORDS)


def normalize_etf_code(code: str) -> str:
    """Return the canonical exchange-suffixed identifier used by price consumers."""

    digits = normalize_stock_code(code)
    exchange = next(
        (market for prefix, market in _ETF_EXCHANGE_BY_PREFIX.items() if digits.startswith(prefix)),
        None,
    )
    if exchange is None:
        raise ValueError(f"unrecognized ETF code: {code!r}")

    raw = str(code).strip().upper().replace(" ", "")
    explicit_exchange = None
    for market in ("SH", "SZ", "BJ"):
        if raw.startswith((market, f"{market}.")) or raw.endswith(f".{market}"):
            explicit_exchange = market
            break
    if explicit_exchange is not None and explicit_exchange != exchange:
        raise ValueError(f"ETF code exchange does not match its prefix: {code!r}")
    return f"{digits}.{exchange}"


def load_return_mapping_input(
    as_of_date: date,
    sector_level: int,
    window: int = 60,
    query: Callable[[str, tuple[object, ...]], list[dict[str, Any]]] = execute_query,
) -> ReturnMappingInput:
    """Load up to ``window`` daily returns from only local trade tables."""

    if sector_level != 2:
        raise ValueError("return mapping requires sector_level=2")
    if window < 1:
        raise ValueError("window must be positive")

    target_date = _coerce_date(as_of_date)
    selected_dates = _load_trade_dates(target_date, window, query)
    if not selected_dates:
        return ReturnMappingInput(target_date, {}, {}, ())

    sector_rows = query(
        "SELECT sector_name, trade_date, close_idx "
        "FROM trade_sector_daily "
        "WHERE sector_level=%s AND trade_date IN (" + _placeholders(selected_dates) + ") "
        "ORDER BY sector_name ASC, trade_date ASC",
        (sector_level, *selected_dates),
    )
    stock_rows = query(
        "SELECT daily.stock_code, status.stock_name, daily.trade_date, daily.close_price "
        "FROM trade_stock_daily_qfq AS daily "
        "LEFT JOIN trade_stock_status AS status ON status.stock_code=daily.stock_code "
        "WHERE daily.trade_date IN (" + _placeholders(selected_dates) + ") "
        "ORDER BY daily.stock_code ASC, daily.trade_date ASC",
        tuple(selected_dates),
    )

    sector_closes = _close_series_by_code(
        sector_rows, code_key="sector_name", close_key="close_idx", selected_dates=set(selected_dates),
    )
    etf_rows = _eligible_etf_rows(stock_rows, set(selected_dates))
    etf_closes = {
        code: series
        for code, series in _close_series_by_code(
            etf_rows, code_key="normalized_code", close_key="close_price", selected_dates=set(selected_dates),
        ).items()
        if len(series) >= 51
    }
    universe_codes = tuple(sorted(etf_closes))
    return ReturnMappingInput(
        as_of_date=target_date,
        sector_closes=sector_closes,
        etf_closes={code: etf_closes[code] for code in universe_codes},
        universe_codes=universe_codes,
    )


def _load_trade_dates(
    as_of_date: date,
    window: int,
    query: Callable[[str, tuple[object, ...]], list[dict[str, Any]]],
) -> tuple[date, ...]:
    rows = query(
        "SELECT DISTINCT trade_date FROM trade_sector_daily "
        "WHERE sector_level=%s AND trade_date<=%s "
        "ORDER BY trade_date DESC LIMIT %s",
        (2, as_of_date, window + 1),
    )
    dates = sorted(
        {
            trade_date
            for row in rows
            if (trade_date := _coerce_date(row.get("trade_date"))) <= as_of_date
        },
        reverse=True,
    )
    return tuple(sorted(dates[: window + 1]))


def _eligible_etf_rows(rows: list[dict[str, Any]], selected_dates: set[date]) -> list[dict[str, Any]]:
    eligible: list[dict[str, Any]] = []
    for row in rows:
        raw_code = row.get("stock_code")
        if not is_domestic_equity_etf(str(raw_code or ""), row.get("stock_name")):
            continue
        try:
            trade_date = _coerce_date(row.get("trade_date"))
            code = normalize_etf_code(str(raw_code))
        except ValueError:
            continue
        if trade_date in selected_dates:
            eligible.append({**row, "normalized_code": code, "trade_date": trade_date})
    return eligible


def _close_series_by_code(
    rows: list[dict[str, Any]],
    *,
    code_key: str,
    close_key: str,
    selected_dates: set[date],
) -> dict[str, pd.Series]:
    values: dict[str, dict[date, float]] = {}
    for row in rows:
        raw_code = row.get(code_key)
        if raw_code is None or not str(raw_code).strip():
            continue
        try:
            trade_date = _coerce_date(row.get("trade_date"))
            close = float(row.get(close_key))
        except (TypeError, ValueError):
            continue
        if trade_date not in selected_dates or not math.isfinite(close) or close <= 0:
            continue
        values.setdefault(str(raw_code), {})[trade_date] = close
    return {
        code: pd.Series(series, dtype=float).sort_index()
        for code, series in sorted(values.items())
    }


def _coerce_date(value: object) -> date:
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if value is None:
        raise ValueError("trade date is required")
    return pd.Timestamp(value).date()


def _placeholders(values: tuple[date, ...]) -> str:
    return ",".join("%s" for _ in values)

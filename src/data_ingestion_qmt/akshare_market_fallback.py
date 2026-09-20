# -*- coding: utf-8 -*-
"""Validated, exact-date AkShare daily-market fallback rows."""

import math

import akshare as ak


MODE_ADJUST = {"none": "", "front": "qfq", "back": "hfq"}
REQUIRED_FIELDS = ("open", "high", "low", "close", "volume", "amount")
EASTMONEY_COLUMNS = {
    "日期": "trade_date",
    "开盘": "open",
    "最高": "high",
    "最低": "low",
    "收盘": "close",
    "成交量": "volume",
    "成交额": "amount",
}
SINA_COLUMNS = {
    "date": "trade_date",
    "open": "open",
    "high": "high",
    "low": "low",
    "close": "close",
    "volume": "volume",
    "amount": "amount",
}
ETF_CODE_PREFIXES = ("15", "16", "50", "51", "56", "58")


def _is_etf_code(stock_code: str) -> bool:
    return stock_code.split(".")[0].startswith(ETF_CODE_PREFIXES)


def _normalize_market_columns(frame):
    """Normalize provider column names without assuming one response schema."""
    if frame is None:
        return frame
    aliases = {
        "trade_date": ("trade_date", "date", "日期", "鏃ユ湡"),
        "open": ("open", "开盘", "寮€鐩?"),
        "high": ("high", "最高", "鏈€楂?"),
        "low": ("low", "最低", "鏈€浣?"),
        "close": ("close", "收盘", "鏀剁洏"),
        "volume": ("volume", "成交量", "鎴愪氦閲?"),
        "amount": ("amount", "成交额", "鎴愪氦棰?"),
    }
    rename = {}
    columns = set(frame.columns)
    for canonical, names in aliases.items():
        source = next((name for name in names if name in columns), None)
        if source is not None and source != canonical:
            rename[source] = canonical
    return frame.rename(columns=rename)


def _date_text(value) -> str:
    return str(value)[:10]


def _valid_number(value) -> float | None:
    try:
        number = float(value)
    except (TypeError, ValueError, OverflowError):
        return None
    return number if math.isfinite(number) else None


def _select_target_rows(frame, target_dates: set[str]) -> tuple[dict[str, dict], dict[str, str]]:
    rows = {}
    invalid_dates = set()
    if frame is not None:
        for _, row in frame.iterrows():
            trade_date = _date_text(row.get("trade_date"))
            if trade_date not in target_dates:
                continue
            values = {field: _valid_number(row.get(field)) for field in REQUIRED_FIELDS}
            if any(value is None for value in values.values()):
                invalid_dates.add(trade_date)
                continue
            values["volume"] = int(values["volume"])
            rows[trade_date] = values
    failures = {
        trade_date: (
            "AkShare returned invalid market values"
            if trade_date in invalid_dates
            else "AkShare response missing target date"
        )
        for trade_date in target_dates - set(rows)
    }
    return rows, failures


def _sina_symbol(stock_code: str) -> str:
    return ("sh" if stock_code.endswith(".SH") else "sz") + stock_code.split(".")[0]


def _fetch_eastmoney(stock_code: str, start_date: str, end_date: str, adjust: str):
    if _is_etf_code(stock_code):
        return ak.fund_etf_hist_em(
            symbol=stock_code.split(".")[0], period="daily",
            start_date=start_date, end_date=end_date, adjust=adjust,
        )
    return ak.stock_zh_a_hist(
        symbol=stock_code.split(".")[0], period="daily",
        start_date=start_date, end_date=end_date, adjust=adjust,
    )


def _fetch_sina(stock_code: str, start_date: str, end_date: str, adjust: str):
    if _is_etf_code(stock_code):
        if adjust:
            raise ValueError("Sina ETF fallback does not provide adjusted prices")
        return ak.fund_etf_hist_sina(symbol=_sina_symbol(stock_code))
    return ak.stock_zh_a_daily(
        symbol=_sina_symbol(stock_code), start_date=start_date,
        end_date=end_date, adjust=adjust,
    )


def _merge_provider_rows(rows, failures, frame, target_dates):
    provider_rows, provider_failures = _select_target_rows(frame, target_dates)
    rows.update(provider_rows)
    return rows, {
        trade_date: provider_failures[trade_date]
        for trade_date in target_dates - set(rows)
    }


def fetch_valid_rows(
    stock_code: str,
    dividend_type: str,
    target_dates: set[str],
) -> tuple[dict[str, dict], dict[str, str]]:
    """Return valid Eastmoney rows for exactly the requested daily dates."""
    if dividend_type not in MODE_ADJUST:
        raise ValueError(f"Unsupported dividend type: {dividend_type}")
    if not target_dates:
        return {}, {}
    start_date = min(target_dates).replace("-", "")
    end_date = max(target_dates).replace("-", "")
    rows = {}
    try:
        frame = _fetch_eastmoney(
            stock_code, start_date, end_date, MODE_ADJUST[dividend_type]
        )
        rows, failures = _merge_provider_rows(
            rows, {}, _normalize_market_columns(frame), target_dates
        )
    except Exception as exc:
        failures = {trade_date: f"Eastmoney failed: {type(exc).__name__}: {exc}" for trade_date in target_dates}
    if not failures:
        return rows, {}
    try:
        frame = _fetch_sina(
            stock_code, start_date, end_date, MODE_ADJUST[dividend_type]
        )
        return _merge_provider_rows(
            rows, failures, _normalize_market_columns(frame), target_dates
        )
    except Exception as exc:
        return rows, {
            trade_date: f"Sina failed: {type(exc).__name__}: {exc}"
            for trade_date in target_dates - set(rows)
        }


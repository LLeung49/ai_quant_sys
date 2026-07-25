# -*- coding: utf-8 -*-
"""Independent QMT collector for raw, front-adjusted, and back-adjusted prices.

This script does not import or write through the legacy market-data collector.
It writes only ``trade_stock_daily_raw``, ``trade_stock_daily_qfq``, and
``trade_stock_daily_bfq`` so the two daily pipelines can be compared safely.
"""

import sys
from datetime import date

from xtquant import xtdata

from price_projection_store import get_existing_latest_dates, write_daily_rows


DATA_START = "20150101"
SECTORS = ("沪深A股", "沪深ETF")
DIVIDEND_TYPES = ("none", "front", "back")
MARKET_FIELDS = (
    "open", "high", "low", "close", "volume", "amount", "preClose", "suspendFlag",
)


def _as_trade_date(index_value) -> str:
    value = str(index_value)
    if len(value) < 8:
        raise ValueError(f"Unexpected QMT trading-date index: {index_value!r}")
    return f"{value[:4]}-{value[4:6]}-{value[6:8]}"


def _optional_number(row, key):
    value = row.get(key) if hasattr(row, "get") else row[key]
    if value is None:
        return None
    try:
        if value != value:  # NaN without adding a pandas dependency.
            return None
    except TypeError:
        pass
    return float(value)


def _rows_from_dataframe(stock_code: str, dataframe, dividend_type: str) -> list[dict]:
    """Normalize QMT rows while retaining unadjusted pre-close and suspension data."""
    rows = []
    for index_value, row in dataframe.iterrows():
        item = {
            "stock_code": stock_code,
            "trade_date": _as_trade_date(index_value),
            "open_price": float(row["open"]),
            "high_price": float(row["high"]),
            "low_price": float(row["low"]),
            "close_price": float(row["close"]),
            "volume": int(row["volume"]),
            "amount": float(row["amount"]),
        }
        if dividend_type == "none":
            item["pre_close"] = _optional_number(row, "preClose")
            suspend = _optional_number(row, "suspendFlag")
            item["suspend_flag"] = int(suspend) if suspend is not None else None
        else:
            item["turnover_rate"] = None
        rows.append(item)
    return rows


def download_and_save_all_modes(
    stock_code: str, start_date: str, adjustment_asof: date | None = None,
) -> dict[str, int]:
    """Fetch QMT daily data for all three modes and store them independently."""
    xtdata.download_history_data(stock_code, "1d", start_time=start_date)
    adjustment_asof = adjustment_asof or date.today()
    counts = {}
    for dividend_type in DIVIDEND_TYPES:
        data = xtdata.get_market_data_ex(
            field_list=list(MARKET_FIELDS),
            stock_list=[stock_code],
            period="1d",
            start_time=start_date,
            dividend_type=dividend_type,
        )
        dataframe = data.get(stock_code) if data else None
        rows = [] if dataframe is None or len(dataframe) == 0 else _rows_from_dataframe(
            stock_code, dataframe, dividend_type
        )
        write_daily_rows(dividend_type, rows, adjustment_asof)
        counts[dividend_type] = len(rows)
    return counts


def get_all_codes() -> list[str]:
    """Return distinct stock and ETF codes from the configured QMT sectors."""
    codes = []
    seen = set()
    for sector in SECTORS:
        for stock_code in xtdata.get_stock_list_in_sector(sector) or []:
            if "." in str(stock_code) and stock_code not in seen:
                seen.add(stock_code)
                codes.append(stock_code)
    return codes


def _earliest_start(latest_dates: dict[str, dict[str, str]], stock_code: str) -> str:
    """Use the earliest mode cursor so all three independent tables stay aligned."""
    starts = [latest_dates[mode].get(stock_code) for mode in DIVIDEND_TYPES]
    if any(value is None for value in starts):
        return DATA_START
    return min(starts)


def main() -> int:
    """Run a simple sequential daily collection for all independently stored modes."""
    xtdata.connect()
    latest_dates = {mode: get_existing_latest_dates(mode) for mode in DIVIDEND_TYPES}
    total_rows = {mode: 0 for mode in DIVIDEND_TYPES}
    failures = []
    codes = get_all_codes()
    for number, stock_code in enumerate(codes, start=1):
        start_date = _earliest_start(latest_dates, stock_code)
        try:
            counts = download_and_save_all_modes(stock_code, start_date)
            for mode, count in counts.items():
                total_rows[mode] += count
            print(f"[{number}/{len(codes)}] {stock_code}: {counts}")
        except Exception as exc:
            failures.append(stock_code)
            print(f"[{number}/{len(codes)}] {stock_code}: failed - {type(exc).__name__}: {exc}")
    print(f"[行情] raw={total_rows['none']} qfq={total_rows['front']} bfq={total_rows['back']}")
    print(f"[结果] 成功={len(codes) - len(failures)} 失败={len(failures)}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())

# -*- coding: utf-8 -*-
"""Independent QMT collector for raw, front-adjusted, and back-adjusted prices.

This script does not import or write through the legacy market-data collector.
It writes only ``trade_stock_daily_raw``, ``trade_stock_daily_qfq``, and
``trade_stock_daily_bfq`` so the two daily pipelines can be compared safely.
"""

import sys
from datetime import date, timedelta

from xtquant import xtdata

from db_config import execute_query
from price_corporate_actions import run_due_refresh_tasks, sync_qmt_factor_snapshot
from price_projection_store import get_existing_latest_dates, write_daily_rows


DATA_START = "20150101"
DATA_START_DATE = date(2015, 1, 1)
A_SHARE_SECTOR = "沪深A股"
ETF_SECTOR = "沪深ETF"
SECTORS = (A_SHARE_SECTOR, ETF_SECTOR)
DIVIDEND_TYPES = ("none", "front", "back")
ACTION_LOOKBACK_DAYS = 10
MARKET_FIELDS = (
    "open", "high", "low", "close", "volume", "amount", "preClose", "suspendFlag",
)

SELECT_ADJUSTMENT_ASOF_SQL = """
SELECT MAX(ex_date) AS adjustment_asof
FROM trade_corporate_action
WHERE stock_code = %s
  AND data_source = 'xtquant'
  AND event_status = 'effective'
"""

MODE_LABELS = {
    "none": "raw",
    "front": "front-adjusted",
    "back": "back-adjusted",
}


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


def download_and_save_mode(
    stock_code: str,
    dividend_type: str,
    start_date: str,
    adjustment_asof: date | None,
) -> int:
    """Fetch and persist one mode; an empty provider response is a failure."""
    if dividend_type not in DIVIDEND_TYPES:
        raise ValueError(f"Unsupported dividend type: {dividend_type}")
    xtdata.download_history_data(stock_code, "1d", start_time=start_date)
    data = xtdata.get_market_data_ex(
        field_list=list(MARKET_FIELDS),
        stock_list=[stock_code],
        period="1d",
        start_time=start_date,
        dividend_type=dividend_type,
    )
    dataframe = data.get(stock_code) if data else None
    if dataframe is None or len(dataframe) == 0:
        raise RuntimeError(
            f"empty QMT {MODE_LABELS[dividend_type]} market response for {stock_code}"
        )
    rows = _rows_from_dataframe(stock_code, dataframe, dividend_type)
    if not rows:
        raise RuntimeError(
            f"QMT returned no valid {MODE_LABELS[dividend_type]} rows for {stock_code}"
        )
    write_daily_rows(dividend_type, rows, adjustment_asof)
    return len(rows)


def download_and_save_all_modes(
    stock_code: str, start_date: str, adjustment_asof: date | None = None,
) -> dict[str, int]:
    """Fetch QMT daily data for all three modes and store them independently."""
    counts = {}
    for dividend_type in DIVIDEND_TYPES:
        counts[dividend_type] = download_and_save_mode(
            stock_code,
            dividend_type,
            start_date,
            adjustment_asof,
        )
    return counts


def get_adjustment_asof(stock_code: str) -> date | None:
    """Return the newest effective event represented by adjusted projections."""
    rows = execute_query(SELECT_ADJUSTMENT_ASOF_SQL, (stock_code,))
    return rows[0]["adjustment_asof"] if rows and rows[0]["adjustment_asof"] else None


def sync_stock_actions(stock_code: str, today: date):
    """Snapshot the recent complete QMT factor window and enqueue durable work."""
    snapshot_start = today - timedelta(days=ACTION_LOOKBACK_DAYS)
    factor_frame = xtdata.get_divid_factors(
        stock_code,
        start_time=snapshot_start.strftime("%Y%m%d"),
        end_time=today.strftime("%Y%m%d"),
    )
    if factor_frame is None:
        raise RuntimeError(f"empty QMT corporate-action response for {stock_code}")
    return sync_qmt_factor_snapshot(
        stock_code,
        factor_frame,
        snapshot_start,
        today,
        DATA_START_DATE,
    )


def get_code_universe() -> tuple[list[str], set[str]]:
    """Return ordered stock/ETF codes and the A-share subset."""
    codes = []
    seen = set()
    a_share_codes = set()
    for sector in SECTORS:
        for stock_code in xtdata.get_stock_list_in_sector(sector) or []:
            if "." in str(stock_code) and stock_code not in seen:
                seen.add(stock_code)
                codes.append(stock_code)
            if sector == A_SHARE_SECTOR and "." in str(stock_code):
                a_share_codes.add(stock_code)
    return codes, a_share_codes


def get_all_codes() -> list[str]:
    return get_code_universe()[0]


def _earliest_start(latest_dates: dict[str, dict[str, str]], stock_code: str) -> str:
    """Use the earliest mode cursor so all three independent tables stay aligned."""
    starts = [latest_dates[mode].get(stock_code) for mode in DIVIDEND_TYPES]
    if any(value is None for value in starts):
        return DATA_START
    return min(starts)


def main() -> int:
    """Run facts, projections, action planning, and durable projection refreshes."""
    xtdata.connect()
    latest_dates = {mode: get_existing_latest_dates(mode) for mode in DIVIDEND_TYPES}
    total_rows = {mode: 0 for mode in DIVIDEND_TYPES}
    failures = []
    action_counts = {"new": 0, "corrected": 0, "cancelled": 0, "tasks": 0}
    codes, a_share_codes = get_code_universe()
    today = date.today()
    for number, stock_code in enumerate(codes, start=1):
        start_date = _earliest_start(latest_dates, stock_code)
        try:
            if stock_code in a_share_codes:
                plan = sync_stock_actions(stock_code, today)
                for change in plan.changes:
                    action_counts[change.kind] += 1
                action_counts["tasks"] += len(plan.refresh_tasks)
            counts = download_and_save_all_modes(
                stock_code,
                start_date,
                adjustment_asof=get_adjustment_asof(stock_code),
            )
            for mode, count in counts.items():
                total_rows[mode] += count
            print(f"[{number}/{len(codes)}] {stock_code}: {counts}")
        except Exception as exc:
            failures.append(stock_code)
            print(f"[{number}/{len(codes)}] {stock_code}: failed - {type(exc).__name__}: {exc}")
    def refresh_projection(stock_code: str, price_mode: str, refresh_from: date) -> int:
        return download_and_save_mode(
            stock_code,
            price_mode,
            refresh_from.strftime("%Y%m%d"),
            get_adjustment_asof(stock_code),
        )

    refresh = run_due_refresh_tasks(refresh_projection)
    print("[行情] raw=%(none)s qfq=%(front)s bfq=%(back)s" % total_rows)
    print(
        "[权益] 新增=%(new)s 修订=%(corrected)s 撤回=%(cancelled)s 刷新任务=%(tasks)s"
        % action_counts
    )
    print(
        "[刷新] 成功=%(done)s 失败=%(failed)s 重试=%(retried)s 回收=%(reclaimed)s"
        % refresh
    )
    print(f"[结果] 股票成功={len(codes) - len(failures)} 股票失败={len(failures)}")
    return 1 if failures or refresh["failed"] else 0


if __name__ == "__main__":
    sys.exit(main())

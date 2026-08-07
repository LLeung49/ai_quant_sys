"""板块日 K 线 API 的纯数据边界校验。"""
from __future__ import annotations

from datetime import date, datetime, time
from math import isfinite
from typing import Any
from zoneinfo import ZoneInfo

SHANGHAI_TIMEZONE = ZoneInfo("Asia/Shanghai")
_PRICE_FIELDS = ("open", "high", "low", "close")
_NONNEGATIVE_FIELDS = ("volume", "amount")


def trade_date_to_shanghai_timestamp(trade_date: date) -> int:
    """将交易日转换为上海时区零点的 Unix 毫秒时间戳。

    参数:
        trade_date: 已解析且不含时间部分的交易日期。

    返回:
        对应 ``00:00:00 Asia/Shanghai`` 的 Unix 毫秒数。
    """
    return int(datetime.combine(trade_date, time.min, SHANGHAI_TIMEZONE).timestamp() * 1000)


def normalize_sector_kline_rows(
    rows: list[dict[str, Any]], requested_end_date: date
) -> tuple[list[dict[str, Any]], int]:
    """清洗仓储返回的板块行情行。

    参数:
        rows: 可含 date/string、Decimal、None 或非法浮点数的数据库字典行。
        requested_end_date: 用户请求的截止日期，任何未来行都必须排除。

    返回:
        第一项为日期唯一且严格升序的有效行情；第二项为被排除的原始行数。
    """
    candidates: list[dict[str, Any]] = []
    skipped = 0

    for row in rows:
        trade_date = _parse_trade_date(row.get("trade_date"))
        if trade_date is None or trade_date > requested_end_date:
            skipped += 1
            continue

        values = _parse_numeric_values(row)
        if values is None or not _has_valid_ohlc(values):
            skipped += 1
            continue

        candidates.append({
            "trade_date": trade_date,
            "timestamp": trade_date_to_shanghai_timestamp(trade_date),
            **values,
        })

    bars: list[dict[str, Any]] = []
    seen_dates: set[date] = set()
    for candidate in sorted(candidates, key=lambda item: item["trade_date"]):
        trade_date = candidate["trade_date"]
        if trade_date in seen_dates:
            skipped += 1
            continue
        seen_dates.add(trade_date)
        bars.append({"trade_date": trade_date.isoformat(), **{
            key: value for key, value in candidate.items() if key != "trade_date"
        }})

    return bars, skipped


def _parse_trade_date(value: Any) -> date | None:
    """解析交易日期；仅接受日期对象或 ISO 日期字符串。"""
    if isinstance(value, datetime):
        return None
    if isinstance(value, date):
        return value
    if not isinstance(value, str):
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        return None


def _parse_numeric_values(row: dict[str, Any]) -> dict[str, float] | None:
    """转换并校验数值字段的有限性、正负约束。"""
    values: dict[str, float] = {}
    for field in _PRICE_FIELDS + _NONNEGATIVE_FIELDS:
        value = row.get(field)
        if isinstance(value, bool):
            return None
        try:
            numeric_value = float(value)
        except (TypeError, ValueError, OverflowError):
            return None
        if not isfinite(numeric_value):
            return None
        if field in _PRICE_FIELDS and numeric_value <= 0:
            return None
        if field in _NONNEGATIVE_FIELDS and numeric_value < 0:
            return None
        values[field] = numeric_value
    return values


def _has_valid_ohlc(values: dict[str, float]) -> bool:
    """确认最高价与最低价包住开盘价和收盘价。"""
    return values["high"] >= max(values["open"], values["close"]) and values["low"] <= min(
        values["open"], values["close"]
    )

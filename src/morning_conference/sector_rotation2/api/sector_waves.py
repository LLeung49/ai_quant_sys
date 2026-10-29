"""申万合成指数上涨波段与成分股区间涨幅的只读计算。"""

from __future__ import annotations

from math import isfinite
from typing import Any

RISE_THRESHOLD = 0.08
REVERSAL_THRESHOLD = 0.05


def detect_rising_waves(bars: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """按收盘价检测上涨 8% 且回撤 5% 确认的波段，保留末尾进行中波段。"""
    if len(bars) < 3:
        return []
    trough = 1  # 起点必须有前一根指数日线作为收益率基准。
    peak = trough
    rising = False
    waves: list[dict[str, Any]] = []

    def append_wave(confirmed: bool) -> None:
        base_close = bars[trough - 1]["close"]
        waves.append({
            "base_date": bars[trough - 1]["trade_date"],
            "start_date": bars[trough]["trade_date"],
            "end_date": bars[peak]["trade_date"],
            "start_timestamp": bars[trough]["timestamp"],
            "end_timestamp": bars[peak]["timestamp"],
            "start_low": min(bar["low"] for bar in bars[trough:peak + 1]),
            "end_high": max(bar["high"] for bar in bars[trough:peak + 1]),
            "trading_days": peak - trough + 1,
            "sector_change_pct": round((bars[peak]["close"] / base_close - 1) * 100, 2),
            "is_confirmed": confirmed,
            "leaders": [],
        })

    for index in range(2, len(bars)):
        close = bars[index]["close"]
        if not rising:
            if close < bars[trough]["close"]:
                trough = index
                peak = index
            elif close / bars[trough]["close"] - 1 >= RISE_THRESHOLD:
                rising = True
                peak = index
        elif close > bars[peak]["close"]:
            peak = index
        elif close / bars[peak]["close"] - 1 <= -REVERSAL_THRESHOLD:
            append_wave(True)
            trough = index
            peak = index
            rising = False
    if rising:
        append_wave(False)
    return waves


def rank_wave_leaders(wave: dict[str, Any], rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """按起点前日与终点前复权收盘价排序，缺任一端价格的个股不参与。"""
    prices: dict[str, dict[str, float]] = {}
    names: dict[str, str] = {}
    for row in rows:
        trade_date = str(row.get("trade_date"))
        if trade_date not in (wave["base_date"], wave["end_date"]):
            continue
        code = str(row.get("stock_code") or "")
        try:
            close = float(row.get("close"))
        except (TypeError, ValueError, OverflowError):
            continue
        if not code or not isfinite(close) or close <= 0:
            continue
        prices.setdefault(code, {})[trade_date] = close
        names[code] = str(row.get("stock_name") or code)

    ranked = []
    for code, pair in prices.items():
        base, end = pair.get(wave["base_date"]), pair.get(wave["end_date"])
        if base is None or end is None:
            continue
        ranked.append((round((end / base - 1) * 100, 2), code, names[code]))
    ranked.sort(key=lambda item: (-item[0], item[1]))
    return [
        {"rank": rank, "stock_code": code, "stock_name": name, "change_pct": change}
        for rank, (change, code, name) in enumerate(ranked[:3], 1)
    ]

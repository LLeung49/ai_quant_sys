"""Signal-coordinate daily-bar indicator snapshots."""

from dataclasses import dataclass
from datetime import date
from math import log, sqrt
from typing import Sequence

from .contracts import DualPriceBar


@dataclass(frozen=True)
class IndicatorSnapshot:
    close: float
    prior_high_20: float
    prior_low_10: float
    ma20: float
    std20: float
    atr20: float | None
    adx: float | None = None
    dif: float | None = None
    dea: float | None = None
    amount_ratio: float | None = None
    price_percentile_252: float | None = None
    hurst: float | None = None
    signal_date: date | None = None
    prior_dif: float | None = None
    prior_dea: float | None = None


def _population_std(values: Sequence[float]) -> float:
    mean = sum(values) / len(values)
    return sqrt(sum((value - mean) ** 2 for value in values) / len(values))


def _ema(values: Sequence[float], period: int) -> list[float]:
    alpha = 2.0 / (period + 1)
    result: list[float] = []
    prior = values[0]
    for value in values:
        prior = alpha * value + (1.0 - alpha) * prior
        result.append(prior)
    return result


def _adx(bars: Sequence[DualPriceBar], period: int = 14) -> list[float | None]:
    values: list[float | None] = [None] * len(bars)
    raw: list[tuple[float, float, float]] = []
    for index in range(1, len(bars)):
        current, previous = bars[index], bars[index - 1]
        up = current.signal_high - previous.signal_high
        down = previous.signal_low - current.signal_low
        plus_dm, minus_dm = max(up, 0.0) if up > down else 0.0, max(down, 0.0) if down > up else 0.0
        tr = max(current.signal_high - current.signal_low, abs(current.signal_high - previous.signal_close), abs(current.signal_low - previous.signal_close))
        raw.append((tr, plus_dm, minus_dm))
    if len(raw) < period:
        return values
    tr_s, plus_s, minus_s = (sum(row[column] for row in raw[:period]) for column in range(3))
    dxs: list[float] = []
    for offset in range(period - 1, len(raw)):
        if offset >= period:
            tr, plus_dm, minus_dm = raw[offset]
            tr_s = tr_s - tr_s / period + tr
            plus_s = plus_s - plus_s / period + plus_dm
            minus_s = minus_s - minus_s / period + minus_dm
        plus_di = 100.0 * plus_s / tr_s if tr_s else 0.0
        minus_di = 100.0 * minus_s / tr_s if tr_s else 0.0
        denominator = plus_di + minus_di
        dx = 100.0 * abs(plus_di - minus_di) / denominator if denominator else 0.0
        dxs.append(dx)
        if len(dxs) == period:
            values[offset + 1] = sum(dxs) / period
        elif len(dxs) > period:
            prior = values[offset]
            assert prior is not None
            values[offset + 1] = (prior * (period - 1) + dx) / period
    return values


def _atr(bars: Sequence[DualPriceBar], period: int = 20) -> list[float | None]:
    values: list[float | None] = [None] * len(bars)
    if len(bars) <= period:
        return values
    ranges = [
        max(
            bars[index].signal_high - bars[index].signal_low,
            abs(bars[index].signal_high - bars[index - 1].signal_close),
            abs(bars[index].signal_low - bars[index - 1].signal_close),
        )
        for index in range(1, len(bars))
    ]
    atr = sum(ranges[:period]) / period
    values[period] = atr
    for offset in range(period, len(ranges)):
        atr = (atr * (period - 1) + ranges[offset]) / period
        values[offset + 1] = atr
    return values


def _hurst(closes: Sequence[float]) -> float:
    returns = [log(current / previous) for previous, current in zip(closes, closes[1:])]
    if len(returns) < 2:
        return 0.5
    mean = sum(returns) / len(returns)
    deviations = [value - mean for value in returns]
    cumulative: list[float] = []
    total = 0.0
    for value in deviations:
        total += value
        cumulative.append(total)
    spread = max(cumulative) - min(cumulative)
    scale = sqrt(sum(value * value for value in deviations) / len(deviations))
    if spread == 0.0 or scale == 0.0:
        return 0.5
    return min(1.0, max(0.0, log(spread / scale) / log(len(returns))))


def compute_indicators(bars: Sequence[DualPriceBar]) -> tuple[IndicatorSnapshot | None, ...]:
    if not bars:
        return ()
    closes = [bar.signal_close for bar in bars]
    fast, slow = _ema(closes, 12), _ema(closes, 26)
    difs = [left - right for left, right in zip(fast, slow)]
    deas = _ema(difs, 9)
    adxs = _adx(bars)
    atrs = _atr(bars)
    snapshots: list[IndicatorSnapshot | None] = []
    for index, bar in enumerate(bars):
        if index < 252:
            snapshots.append(None)
            continue
        prior20 = bars[index - 20:index]
        prior10 = bars[index - 10:index]
        closes20 = [item.signal_close for item in prior20]
        prior252 = [item.signal_close for item in bars[index - 252:index]]
        snapshots.append(IndicatorSnapshot(
            close=bar.signal_close,
            prior_high_20=max(item.signal_high for item in prior20),
            prior_low_10=min(item.signal_low for item in prior10),
            ma20=sum(closes20) / 20,
            std20=_population_std(closes20),
            atr20=atrs[index],
            adx=adxs[index],
            dif=difs[index],
            dea=deas[index],
            amount_ratio=(bar.amount / (sum(item.amount for item in prior20) / 20)),
            price_percentile_252=(
                sum(value <= bar.signal_close for value in prior252) / len(prior252)
            ),
            hurst=_hurst(prior252),
            signal_date=bar.trade_date,
            prior_dif=difs[index - 1],
            prior_dea=deas[index - 1],
        ))
    return tuple(snapshots)

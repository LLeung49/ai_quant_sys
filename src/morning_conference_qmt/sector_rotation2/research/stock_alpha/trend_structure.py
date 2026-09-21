"""Trend-structure evidence: MA stack, breakout, strong pullback.

All evidence here must use ``shift(1)`` to ensure no current-day data leaks
into the prior history used as the breakout/breakdown reference level.  The
module returns boolean components and a sector-local normalized score in
``[0, 1]`` for downstream weighting.
"""

from __future__ import annotations

from typing import Mapping

import numpy as np
import pandas as pd


def calc_ma_stack(close: pd.Series, ma20: pd.Series, ma60: pd.Series, ma20_slope: pd.Series) -> bool:
    """Return True iff ``close > ma20 > ma60`` and MA20 slope is positive."""

    if close is None or ma20 is None or ma60 is None or ma20_slope is None:
        return False
    if len(close) == 0 or len(ma20) == 0 or len(ma60) == 0 or len(ma20_slope) == 0:
        return False
    try:
        c = float(close.iloc[-1])
        m20 = float(ma20.iloc[-1])
        m60 = float(ma60.iloc[-1])
        slope = float(ma20_slope.iloc[-1])
    except (TypeError, ValueError):
        return False
    if any(np.isnan(value) for value in (c, m20, m60, slope)):
        return False
    return c > m20 > m60 and slope > 0


def calc_breakout_flags(high: pd.Series, prev_high_20: pd.Series, prev_high_60: pd.Series) -> tuple:
    """Return ``(breakout20, breakout60)`` using only prior-day history.

    ``prev_high_20`` and ``prev_high_60`` must already be shifted by the
    caller using ``high.shift(1).rolling(...).max()`` so that no current-day
    high can leak into the comparison.
    """

    if high is None or prev_high_20 is None or prev_high_60 is None:
        return False, False
    if len(high) == 0 or len(prev_high_20) == 0 or len(prev_high_60) == 0:
        return False, False
    try:
        h = float(high.iloc[-1])
        p20 = float(prev_high_20.iloc[-1])
        p60 = float(prev_high_60.iloc[-1])
    except (TypeError, ValueError):
        return False, False
    if any(np.isnan(value) for value in (h, p20, p60)):
        return False, False
    return h > p20, h > p60


def calc_strong_pullback(
    close: pd.Series,
    high: pd.Series,
    ma20: pd.Series,
    volume_3d_mean: pd.Series,
    volume_20d_mean: pd.Series,
    *,
    drawdown_low: float = 0.02,
    drawdown_high: float = 0.08,
    volume_ratio_cap: float = 0.80,
) -> bool:
    """Return True iff the stock is in a healthy MA20>MA60 pullback."""

    if close is None or len(close) < 10:
        return False
    if ma20 is None:
        return False
    try:
        c0 = float(close.iloc[-1])
        m20 = float(ma20.iloc[-1])
        high_10 = float(high.iloc[-10:].max())
        vol_3 = float(volume_3d_mean.iloc[-1]) if volume_3d_mean is not None else float("nan")
        vol_20 = float(volume_20d_mean.iloc[-1]) if volume_20d_mean is not None else float("nan")
    except (TypeError, ValueError, IndexError):
        return False
    if any(np.isnan(value) for value in (c0, m20, high_10, vol_3, vol_20)):
        return False
    if not (c0 > m20):
        return False
    drawdown = (high_10 - c0) / high_10
    if not (drawdown_low <= drawdown <= drawdown_high):
        return False
    if vol_20 <= 0 or vol_3 / vol_20 > volume_ratio_cap:
        return False
    # Each of last 3 closes >= its corresponding MA20.
    for i in range(1, 4):
        idx = -i
        if idx < -len(close):
            return False
        c_i = float(close.iloc[idx])
        m_i = float(ma20.iloc[idx])
        if np.isnan(c_i) or np.isnan(m_i):
            return False
        if c_i < m_i:
            return False
    return True


DEFAULT_STRUCTURE_WEIGHTS: dict = {
    "ma_stack": 0.35,
    "breakout20": 0.25,
    "breakout60": 0.20,
    "strong_pullback": 0.20,
}


def _is_missing(value: object) -> bool:
    if value is None:
        return True
    if isinstance(value, float) and np.isnan(value):
        return True
    try:
        return bool(np.isnan(value))
    except (TypeError, ValueError):
        return False


def score_trend_structure(
    frame: pd.DataFrame,
    *,
    weights: Mapping = None,
) -> pd.DataFrame:
    """Combine MA stack, breakout20/60, strong_pullback into a 0-1 score.

    Each component is a boolean column on the input frame.  The output
    ``trend_structure`` is the weighted average of valid components; missing
    components (``NaN``) are excluded from the normalization and the average is
    only emitted when at least one valid component exists.
    """

    if weights is None:
        weights = DEFAULT_STRUCTURE_WEIGHTS
    weights = dict(weights)
    if abs(sum(weights.values()) - 1.0) > 1e-9:
        raise ValueError("structure_weights must sum to 1.0")
    out = frame.copy()
    scores = np.full(len(out), np.nan, dtype="float64")
    for idx in range(len(out)):
        row = out.iloc[idx]
        total_weight = 0.0
        weighted = 0.0
        for name, weight in weights.items():
            value = row[name]
            if _is_missing(value):
                continue
            total_weight += weight
            weighted += float(value) * weight
        if total_weight <= 0:
            scores[idx] = np.nan
        else:
            scores[idx] = weighted / total_weight
    out["trend_structure"] = scores
    return out


def calc_prev_high(series: pd.Series, window: int) -> pd.Series:
    """Return ``series.shift(1).rolling(window).max()`` for breakout usage."""

    if window <= 0:
        raise ValueError("window must be positive")
    return series.shift(1).rolling(window, min_periods=window).max()


def calc_ma(series: pd.Series, window: int) -> pd.Series:
    """Return a simple moving average of ``series`` over ``window`` days."""

    if window <= 0:
        raise ValueError("window must be positive")
    return series.rolling(window, min_periods=window).mean()


def calc_ma_slope(series: pd.Series, window: int = 5) -> pd.Series:
    """Return the slope of the trailing ``window``-day mean as a ratio."""

    if window <= 0:
        raise ValueError("window must be positive")
    shifted = series.shift(1)
    return (shifted - shifted.shift(window)) / shifted.shift(window)


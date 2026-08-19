"""Sector-relative returns, persistence, alpha-strength and trend-quality scoring.

This module contains the *pure* feature work for the Trend Alpha pipeline.
Inputs are pre-aligned close-price series and the loader-produced metadata
bundle; outputs are auditable floats that feed into the scoring module.

All ranks are sector-local: every cross-sectional percentile is computed only
inside the ``(as_of_date, sector_name)`` group.  All breakout/breakdown windows
must be computed by the caller using ``shift(1)`` so that no current-day data
leaks into the prior history used as the reference level.
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from math import sqrt

import numpy as np
import pandas as pd


def calc_relative_return(stock_ret: float, sector_ret: float) -> float:
    """Return the simple sector-relative return for a single window."""

    return float(stock_ret) - float(sector_ret)


def calc_relative_returns(
    stock_close: pd.Series,
    sector_close: pd.Series,
    windows: tuple = (5, 10, 20),
) -> dict:
    """Compute per-window sector-relative simple returns.

    Both series must share an index aligned on the same trading dates.  The
    function returns ``{f"rr_{n}": rr_n, ...}`` where ``rr_n = stock_ret_n -
    sector_ret_n``.  Missing or misaligned inputs yield ``None`` for that
    window only.
    """

    if stock_close is None or sector_close is None:
        return {f"rr_{window}": None for window in windows}
    aligned = pd.concat(
        [stock_close.rename("stock"), sector_close.rename("sector")], axis=1,
    ).dropna()
    out: dict = {}
    for window in windows:
        if len(aligned) < window + 1:
            out[f"rr_{window}"] = None
            continue
        head = aligned.tail(window + 1)
        stock_ret = float(head["stock"].iloc[-1] / head["stock"].iloc[0] - 1.0)
        sector_ret = float(head["sector"].iloc[-1] / head["sector"].iloc[0] - 1.0)
        out[f"rr_{window}"] = stock_ret - sector_ret
    return out


def _signed_percentile(values: pd.Series) -> pd.Series:
    """Return signed-percentile rank ``[-0.5, +0.5]`` for a numeric series.

    NaNs stay NaN.  Single non-NaN values map to ``0.0``.  Two or more values
    are evenly spaced between ``-0.5`` (lowest rank) and ``+0.5`` (highest).
    """

    ranks = values.rank(method="average", na_option="keep")
    size = int(ranks.notna().sum())
    if size == 0:
        return pd.Series(np.nan, index=values.index)
    if size == 1:
        # Single valid value: assign 0.0 only to that row, leave NaN at NaN.
        return ranks.apply(lambda r: 0.0 if pd.notna(r) else np.nan)
    return (ranks - 0.5 * (size + 1)) / (size - 1)


def sector_local_percentile(
    frame: pd.DataFrame,
    value_column: str,
    group_keys: tuple = ("as_of_date", "sector_name"),
) -> pd.Series:
    """Return a signed percentile rank of ``value_column`` within each group."""

    if value_column not in frame.columns:
        raise ValueError(f"missing column: {value_column}")
    if not all(key in frame.columns for key in group_keys):
        raise ValueError(f"missing group keys: {group_keys}")
    return frame.groupby(list(group_keys))[value_column].transform(_signed_percentile)


def _renormalize_weights(
    values: Mapping,
    weights: Mapping,
) -> tuple:
    """Return ``(weighted_sum, total_weight)`` ignoring ``None`` entries."""

    total_weight = 0.0
    weighted_sum = 0.0
    for name, weight in weights.items():
        value = values.get(name)
        if value is None or pd.isna(value):
            continue
        total_weight += weight
        weighted_sum += float(value) * weight
    return weighted_sum, total_weight


def score_alpha_strength(
    frame: pd.DataFrame,
    *,
    windows: tuple = (5, 10, 20),
    alpha_weights: tuple = (0.50, 0.30, 0.20),
    min_alpha_weight: float = 0.60,
    group_keys: tuple = ("as_of_date", "sector_name"),
) -> pd.DataFrame:
    """Compute ``rr_<n>_pct`` columns and ``alpha_strength`` for the frame.

    The frame must already contain ``rr_<n>`` columns.  Percentiles are
    computed sector-locally; ``alpha_strength`` is the weighted sum of the
    sector-local signed percentiles, renormalized to weights of valid
    windows only when the total valid weight is at least
    ``min_alpha_weight``.  Otherwise ``alpha_strength`` is ``NaN`` and the
    caller is expected to down-rank the row.
    """

    if len(alpha_weights) != len(windows):
        raise ValueError("windows and alpha_weights must have the same length")
    out = frame.copy()
    weight_by_window = {f"rr_{window}_pct": weight for window, weight in zip(windows, alpha_weights)}
    for window in windows:
        col = f"rr_{window}"
        pct_col = f"{col}_pct"
        out[pct_col] = sector_local_percentile(out, col, group_keys=group_keys)
    strength = np.full(len(out), np.nan, dtype="float64")
    for idx in range(len(out)):
        per_window = {name: out.iloc[idx][name] for name in weight_by_window}
        weighted_sum, total_weight = _renormalize_weights(per_window, weight_by_window)
        if total_weight >= min_alpha_weight:
            strength[idx] = weighted_sum / total_weight
    out["alpha_strength"] = strength
    return out


def calc_alpha_persistence(
    relative_rank_history: Mapping,
    *,
    lookback: int = 10,
    top_threshold: float = 0.70,
    min_dates: int = 6,
) -> float:
    """Return persistence score in ``[-1, 1]`` for the given history.

    Each iterable must yield signed percentiles (already sector-local).  A
    history shorter than ``min_dates`` returns ``None``.  The persistence is
    computed as ``2 * top_ratio - 1`` where ``top_ratio`` is the fraction of
    dates where the stock ranked in the top ``top_threshold`` percentile.
    The top threshold accepts signed percentiles >= ``0.0`` by default,
    which corresponds to "ranked at or above the group median".
    """

    del lookback  # Lookback is enforced by the caller through slicing.

    valid: list = []
    for values in relative_rank_history.values():
        for value in values:
            if value is None or pd.isna(value):
                continue
            valid.append(float(value))
    if len(valid) < min_dates:
        return None
    top = sum(1 for value in valid if value >= top_threshold)
    return 2 * top / len(valid) - 1


def calc_kama_er(close: pd.Series, window: int = 10) -> float:
    """Return the Kaufman Efficiency Ratio for the trailing window."""

    if close is None or len(close) < window + 1:
        return None
    values = pd.Series(close).tail(window + 1).astype("float64").to_numpy()
    diffs = np.diff(values)
    direction = abs(values[-1] - values[0])
    path = float(np.sum(np.abs(diffs)))
    if path <= 0:
        return 0.0
    return float(direction / path)


def calc_adx14(high: pd.Series, low: pd.Series, close: pd.Series) -> float:
    """Return the latest 14-period ADX value, or ``None`` when too short.

    The Wilder True Range / +/-DM / ADX formula is reproduced here so callers
    can feed a pure-Python pipeline.  It avoids duplicating the MACD-pool
    implementation because Phase 2's ``step2_filter_trap_avoidance`` is
    optimized for daily-row vectors, not stock-only analytic use.
    """

    if high is None or low is None or close is None or len(close) < 28:
        return None
    h = pd.Series(high).astype("float64").to_numpy()
    l = pd.Series(low).astype("float64").to_numpy()
    c = pd.Series(close).astype("float64").to_numpy()
    tr = np.maximum(h[1:] - l[1:], np.maximum(np.abs(h[1:] - c[:-1]), np.abs(l[1:] - c[:-1])))
    up = np.diff(h)
    down = -np.diff(l)
    plus = np.where((up > down) & (up > 0), up, 0.0)
    minus = np.where((down > up) & (down > 0), down, 0.0)
    atr = pd.Series(tr).rolling(14, min_periods=14).mean()
    pdi = 100 * pd.Series(plus).rolling(14, min_periods=14).mean() / atr
    mdi = 100 * pd.Series(minus).rolling(14, min_periods=14).mean() / atr
    dx = (100 * (pdi - mdi).abs() / (pdi + mdi)).replace([np.inf, -np.inf], np.nan)
    adx = dx.rolling(14, min_periods=14).mean().iloc[-1]
    if pd.isna(adx):
        return None
    return float(adx)


def score_trend_quality(
    frame: pd.DataFrame,
    *,
    weights: tuple = (0.50, 0.50),
    group_keys: tuple = ("as_of_date", "sector_name"),
) -> pd.DataFrame:
    """Combine ER and ADX into a sector-local signed-percentile score."""

    if abs(sum(weights) - 1.0) > 1e-9:
        raise ValueError("trend_quality weights must sum to 1.0")
    out = frame.copy()
    out["er_pct"] = sector_local_percentile(out, "er", group_keys=group_keys)
    out["adx_pct"] = sector_local_percentile(out, "adx", group_keys=group_keys)
    er_w, adx_w = weights
    quality = np.full(len(out), np.nan, dtype="float64")
    for idx in range(len(out)):
        er_pct = out.iloc[idx]["er_pct"]
        adx_pct = out.iloc[idx]["adx_pct"]
        if pd.isna(er_pct) and pd.isna(adx_pct):
            continue
        num = (0.0 if pd.isna(er_pct) else float(er_pct) * er_w) + (
            0.0 if pd.isna(adx_pct) else float(adx_pct) * adx_w
        )
        denom = (0.0 if pd.isna(er_pct) else er_w) + (0.0 if pd.isna(adx_pct) else adx_w)
        if denom <= 0:
            continue
        quality[idx] = num / denom
    out["trend_quality"] = quality
    return out


def calc_volatility(ret_1d: pd.Series, window: int = 20) -> float:
    """Return annualized 20-day volatility from a daily return series."""

    if ret_1d is None or len(ret_1d) < window:
        return None
    series = pd.Series(ret_1d).tail(window).astype("float64")
    if series.isna().any():
        return None
    return float(series.std(ddof=0) * sqrt(252))

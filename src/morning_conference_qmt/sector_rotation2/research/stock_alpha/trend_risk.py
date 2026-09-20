"""Trend risk controls: liquidity, extension, volatility, and hot-leader evidence.

Liquidity and volatility are computed as sector-local signed percentiles.
Extension is a deterministic linear penalty based on the absolute distance
from MA20.  Hot-leader evidence is gated on PIT-safe limit-up metadata; if
that metadata is not available, the contribution is forced to zero and the
``hot_leader_unavailable`` flag is surfaced for the audit log.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from .trend_features import sector_local_percentile


def calc_stock_liquidity(
    frame: pd.DataFrame,
    *,
    amount_column: str = "amount_20d_median",
    group_keys: tuple = ("as_of_date", "sector_name"),
) -> pd.Series:
    """Return sector-local signed-percentile of trailing 20-day median amount."""

    if amount_column not in frame.columns:
        raise ValueError(f"missing column: {amount_column}")
    return sector_local_percentile(frame, amount_column, group_keys=group_keys)


def calc_extension_penalty(
    distance_ma20: float | None,
    *,
    start: float = 0.20,
    end: float = 1.00,
    max_penalty: float = 0.40,
) -> float | None:
    """Return a linear penalty in ``[0, max_penalty]`` for over-extension."""

    if distance_ma20 is None:
        return None
    try:
        distance = float(distance_ma20)
    except (TypeError, ValueError):
        return None
    if np.isnan(distance):
        return None
    if start >= end:
        raise ValueError("extension_start must be < extension_end")
    if distance <= start:
        return 0.0
    if distance >= end:
        return float(max_penalty)
    return float(max_penalty * (distance - start) / (end - start))


def calc_volatility_penalty(
    frame: pd.DataFrame,
    *,
    column: str = "volatility_20d",
    group_keys: tuple = ("as_of_date", "sector_name"),
) -> pd.Series:
    """Return sector-local signed-percentile of 20-day annualized volatility."""

    if column not in frame.columns:
        raise ValueError(f"missing column: {column}")
    return sector_local_percentile(frame, column, group_keys=group_keys)


def calc_hot_leader_bonus(
    *,
    streak: int | None,
    source: str,
    cap: float = 0.05,
    streak_threshold: int = 2,
) -> tuple:
    """Return ``(bonus, unavailable_flag)`` for hot-leader evidence."""

    if cap < 0 or cap > 1:
        raise ValueError("cap must be in [0, 1]")
    if streak_threshold <= 0:
        raise ValueError("streak_threshold must be positive")
    if source == "unavailable":
        return 0.0, True
    if streak is None:
        return 0.0, False
    try:
        streak_value = int(streak)
    except (TypeError, ValueError):
        return 0.0, False
    if streak_value < streak_threshold:
        return 0.0, False
    return float(cap), False


def total_risk_penalty(
    extension: float | None,
    volatility_pct: float | None,
    *,
    extension_weight: float = 0.50,
    volatility_weight: float = 0.50,
) -> float:
    """Combine extension and volatility contributions into a single penalty.

    Weighted average: missing components renormalize over remaining weights.
    Returns 0.0 when both components are missing.
    """

    num = 0.0
    denom = 0.0
    if extension is not None and not np.isnan(extension):
        num += float(extension) * extension_weight
        denom += extension_weight
    if volatility_pct is not None and not np.isnan(volatility_pct):
        penalty = max(0.0, float(volatility_pct))
        num += penalty * volatility_weight
        denom += volatility_weight
    if denom <= 0:
        return 0.0
    return float(num / denom)


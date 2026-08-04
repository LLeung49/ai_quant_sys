"""Pure cross-sectional normalization helpers for sector_rotation2."""
from __future__ import annotations

from collections.abc import Mapping

import pandas as pd


def signed_percentile(series: pd.Series, minimum_count: int = 20) -> pd.Series:
    """Map a valid cross section to [-1, 1] using average percentile ranks."""
    result = pd.Series(float("nan"), index=series.index, dtype="float64")
    valid = series.dropna()
    if len(valid) < minimum_count or valid.nunique() < 2:
        return result

    ranks = valid.rank(method="average")
    result.loc[valid.index] = 2.0 * (ranks - 1.0) / (len(valid) - 1.0) - 1.0
    return result


def weighted_available_mean(
    frame: pd.DataFrame,
    weights: Mapping[str, float],
    minimum_weight: float,
) -> pd.Series:
    """Return an available-column weighted mean, subject to a weight threshold."""
    columns = list(weights)
    missing = set(columns).difference(frame.columns)
    if missing:
        raise KeyError(f"Missing weighted columns: {sorted(missing)}")

    weight_series = pd.Series(weights, dtype="float64")
    available = frame[columns].notna()
    available_weight = available.mul(weight_series, axis=1).sum(axis=1)
    numerator = frame[columns].mul(weight_series, axis=1).sum(axis=1, min_count=1)
    result = numerator.div(available_weight.where(available_weight >= minimum_weight))
    return result.astype("float64")

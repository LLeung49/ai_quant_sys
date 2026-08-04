from __future__ import annotations

import pandas as pd

from morning_conference.sector_rotation2.config import DEFAULT_CONFIG, config_hash
from morning_conference.sector_rotation2.normalizers import (
    signed_percentile,
    weighted_available_mean,
)


def test_signed_percentile_maps_three_distinct_values_to_minus_one_zero_one():
    result = signed_percentile(pd.Series([1.0, 2.0, 3.0]), minimum_count=3)

    assert result.tolist() == [-1.0, 0.0, 1.0]


def test_signed_percentile_returns_nan_for_small_cross_section():
    result = signed_percentile(pd.Series([1.0, 2.0]), minimum_count=3)

    assert result.isna().all()


def test_signed_percentile_returns_nan_for_constant_cross_section():
    result = signed_percentile(pd.Series([1.0, 1.0, 1.0]), minimum_count=3)

    assert result.isna().all()


def test_weighted_available_mean_renormalizes_available_columns():
    frame = pd.DataFrame({"trend": [1.0], "velocity": [float("nan")]})

    result = weighted_available_mean(
        frame,
        {"trend": 0.45, "velocity": 0.55},
        minimum_weight=0.40,
    )

    assert result.iloc[0] == 1.0


def test_weighted_available_mean_returns_nan_below_minimum_weight():
    frame = pd.DataFrame({"trend": [1.0], "velocity": [float("nan")]})

    result = weighted_available_mean(
        frame,
        {"trend": 0.45, "velocity": 0.55},
        minimum_weight=0.50,
    )

    assert pd.isna(result.iloc[0])


def test_config_hash_is_stable_for_same_configuration():
    assert config_hash(DEFAULT_CONFIG) == config_hash(DEFAULT_CONFIG)

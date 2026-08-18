import pandas as pd

from morning_conference.sector_rotation2.research.etf_core.features import calc_tracking_corr, calc_tracking_error


def test_perfect_tracker_has_correlation_one_and_zero_error() -> None:
    prices = pd.Series([100, 101, 103, 102, 105])
    assert calc_tracking_corr(prices, prices, window=4) == 1.0
    assert calc_tracking_error(prices, prices, window=4) == 0.0

import warnings

import pandas as pd
import pytest

from morning_conference.sector_rotation.sector_loader import build_market_benchmark


def test_build_market_benchmark_avoids_fragmentation_for_many_sectors():
    dates = pd.date_range("2024-01-01", periods=2)
    sector_panel = {
        f"sector_{index}": pd.DataFrame(
            {
                "close": [100 + index, 110 + index],
                "amount": [index + 1, (index + 1) * 2],
            },
            index=dates,
        )
        for index in range(125)
    }

    with warnings.catch_warnings():
        warnings.simplefilter("error", pd.errors.PerformanceWarning)
        benchmark = build_market_benchmark(sector_panel)

    expected_second_close = (
        sum((110 + index) / (100 + index) for index in range(125)) / 125 * 1000
    )
    assert benchmark["close"].tolist() == pytest.approx(
        [1000.0, expected_second_close]
    )
    assert benchmark["amount"].tolist() == [7875, 15750]

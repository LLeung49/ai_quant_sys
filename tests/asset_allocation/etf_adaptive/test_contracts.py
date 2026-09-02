from datetime import date

import pytest

from asset_allocation.etf_adaptive.contracts import DualPriceBar


def test_dual_price_bar_rejects_non_positive_prices() -> None:
    with pytest.raises(ValueError, match="prices must be positive"):
        DualPriceBar(
            stock_code="510300.SH", trade_date=date(2026, 9, 1),
            signal_open=0.0, signal_high=1.0, signal_low=0.9, signal_close=1.0,
            raw_open=4.0, raw_high=4.1, raw_low=3.9, raw_close=4.0,
            amount=20_000_000.0, suspended=False, adjustment_ratio=0.25,
        )

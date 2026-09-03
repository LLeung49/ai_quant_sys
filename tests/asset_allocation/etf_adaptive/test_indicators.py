from datetime import date, timedelta

from asset_allocation.etf_adaptive.contracts import DualPriceBar
from asset_allocation.etf_adaptive.indicators import compute_indicators


def _bar(day: date, close: float) -> DualPriceBar:
    return DualPriceBar(
        stock_code="510300.SH", trade_date=day, signal_open=close - 0.1,
        signal_high=close + 0.2, signal_low=close - 0.2, signal_close=close,
        raw_open=close - 0.1, raw_high=close + 0.2, raw_low=close - 0.2,
        raw_close=close, amount=20_000_000.0, suspended=False,
        adjustment_ratio=1.0,
    )


def test_donchian_channels_exclude_current_bar() -> None:
    start = date(2026, 1, 1)
    bars = tuple(_bar(start + timedelta(days=index), float(index + 1)) for index in range(253))

    snapshot = compute_indicators(bars)[-1]

    assert snapshot is not None
    assert snapshot.close == 253.0
    assert snapshot.prior_high_20 == 252.2
    assert snapshot.close > snapshot.prior_high_20


def test_indicator_snapshot_waits_for_252_prior_sessions() -> None:
    start = date(2026, 1, 1)
    bars = tuple(_bar(start + timedelta(days=index), float(index + 1)) for index in range(252))

    snapshots = compute_indicators(bars)

    assert all(snapshot is None for snapshot in snapshots)


def test_rising_signal_prices_produce_bullish_macd_and_finite_adx() -> None:
    start = date(2026, 1, 1)
    bars = tuple(_bar(start + timedelta(days=index), float(index + 1)) for index in range(253))

    snapshot = compute_indicators(bars)[-1]

    assert snapshot is not None
    assert snapshot.dif is not None and snapshot.dea is not None
    assert snapshot.dif > snapshot.dea
    assert snapshot.adx is not None and 0.0 <= snapshot.adx <= 100.0


def test_atr20_uses_wilder_smoothing_after_its_initial_window() -> None:
    start = date(2026, 1, 1)
    closes = [100.0] + [101.0] * 250 + [111.0] * 2
    bars = tuple(_bar(start + timedelta(days=index), close) for index, close in enumerate(closes))

    snapshot = compute_indicators(bars)[-1]

    assert snapshot is not None
    # A 10-point gap one session ago is attenuated by Wilder smoothing; a
    # simple 20-session average remains 0.89 here.
    assert snapshot.atr20 is not None and 0.4 < snapshot.atr20 < 0.89


def test_hurst_is_research_feature_on_warmed_snapshot() -> None:
    start = date(2026, 1, 1)
    bars = tuple(_bar(start + timedelta(days=index), float(index + 1)) for index in range(253))

    snapshot = compute_indicators(bars)[-1]

    assert snapshot is not None
    assert snapshot.hurst is not None
    assert 0.0 <= snapshot.hurst <= 1.0

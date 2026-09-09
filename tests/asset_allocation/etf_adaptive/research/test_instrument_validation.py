"""Contracts for independent fixed-ETF strategy validation."""

from datetime import date
from decimal import Decimal

from asset_allocation.etf_adaptive.contracts import DualPriceBar, ExecutionAvailability
from asset_allocation.etf_adaptive.contracts import DataQualityError
from asset_allocation.etf_adaptive.research.instrument_validation import (
    CachedValidationProvider,
    FIXED_VALIDATION_TARGETS,
    ValidationStatus,
    evaluate_validation_gate,
    run_instrument_validation,
    resolve_validation_start,
)
from asset_allocation.etf_adaptive.research.walk_forward import build_windows


def test_fixed_targets_are_the_confirmed_ten_exposures() -> None:
    assert {(target.exposure_id, target.stock_code) for target in FIXED_VALIDATION_TARGETS} == {
        ("sp_china_low_vol_dividend", "515450.SH"),
        ("csi_dividend", "515080.SH"),
        ("csi_300", "510300.SH"),
        ("csi_a500", "563360.SH"),
        ("chinext", "159915.SZ"),
        ("star_50", "588000.SH"),
        ("nasdaq_100", "513100.SH"),
        ("sp_500", "513500.SH"),
        ("hang_seng_tech", "513130.SH"),
        ("hang_seng_internet_technology", "513330.SH"),
    }


def test_gate_needs_excess_return_drawdown_and_window_majority() -> None:
    assert evaluate_validation_gate(
        annual_excess=0.001,
        drawdown_excess=0.02,
        non_lagging_windows=2,
        total_windows=3,
    ) is ValidationStatus.PASSED
    assert evaluate_validation_gate(
        annual_excess=0.0,
        drawdown_excess=0.02,
        non_lagging_windows=3,
        total_windows=3,
    ) is ValidationStatus.FAILED


def test_validation_rejects_provider_with_missing_history() -> None:
    class Provider:
        def load_bars(self, stock_code, start_date, end_date):
            return ()

    result = run_instrument_validation(
        FIXED_VALIDATION_TARGETS[0],
        Provider(),
        date(2020, 1, 1),
        date(2026, 9, 8),
        Decimal("100000"),
    )

    assert result.status is ValidationStatus.DATA_REJECTED
    assert result.rejection_reason == "no market bars in requested range"


def test_validation_converts_initial_market_data_error_to_data_rejected() -> None:
    class Provider:
        def load_bars(self, stock_code, start_date, end_date):
            raise DataQualityError("expected market session is missing")

    result = run_instrument_validation(FIXED_VALIDATION_TARGETS[0], Provider(), date(2020, 1, 1), date(2026, 9, 8), Decimal("100000"))

    assert result.status is ValidationStatus.DATA_REJECTED
    assert result.rejection_reason == "expected market session is missing"


def test_validation_rejects_history_shorter_than_first_walk_forward_window() -> None:
    class Provider:
        def load_bars(self, stock_code, start_date, end_date):
            return (
                DualPriceBar(
                    stock_code=stock_code, trade_date=start_date,
                    signal_open=1.0, signal_high=1.0, signal_low=1.0, signal_close=1.0,
                    raw_open=1.0, raw_high=1.0, raw_low=1.0, raw_close=1.0,
                    amount=20_000_000.0, suspended=False, adjustment_ratio=1.0,
                    execution_availability=ExecutionAvailability(False, False, "test"),
                ),
            )

    result = run_instrument_validation(
        FIXED_VALIDATION_TARGETS[0], Provider(), date(2020, 1, 1), date(2026, 9, 8), Decimal("100000"),
    )

    assert result.status is ValidationStatus.DATA_REJECTED
    assert result.rejection_reason == "insufficient history for walk-forward validation"


def test_short_sample_reference_uses_252_train_and_126_validation_sessions() -> None:
    dates = tuple(date(2024, 1, 1) + __import__("datetime").timedelta(days=index) for index in range(504))
    windows = build_windows(dates, train_sessions=252, validation_sessions=126, step_sessions=126)
    assert len(windows[0].train_dates) == 252
    assert len(windows[0].validation_dates) == 126


def test_validation_provider_cache_reuses_identical_market_requests() -> None:
    class Provider:
        def __init__(self) -> None:
            self.calls = 0

        def load_bars(self, stock_code, start_date, end_date):
            self.calls += 1
            return (stock_code, start_date, end_date)

    provider = Provider()
    cached = CachedValidationProvider(provider)

    assert cached.load_bars("159915.SZ", date(2025, 1, 1), date(2025, 6, 1)) == ("159915.SZ", date(2025, 1, 1), date(2025, 6, 1))
    assert cached.load_bars("159915.SZ", date(2025, 1, 1), date(2025, 6, 1)) == ("159915.SZ", date(2025, 1, 1), date(2025, 6, 1))
    assert provider.calls == 1


def test_validation_start_advances_to_first_aligned_session_from_provider() -> None:
    class Provider:
        def first_aligned_session(self, stock_code, start_date, end_date):
            assert stock_code == "588000.SH"
            return date(2020, 11, 16)

    assert resolve_validation_start(Provider(), "588000.SH", date(2020, 1, 1), date(2026, 9, 8)) == date(2020, 11, 16)

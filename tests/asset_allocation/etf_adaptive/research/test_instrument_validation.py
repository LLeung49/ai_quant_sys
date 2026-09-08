"""Contracts for independent fixed-ETF strategy validation."""

from asset_allocation.etf_adaptive.research.instrument_validation import (
    FIXED_VALIDATION_TARGETS,
    ValidationStatus,
    evaluate_validation_gate,
)


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

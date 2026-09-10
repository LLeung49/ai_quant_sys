"""Contracts for independent fixed-ETF strategy validation."""

from datetime import date
from decimal import Decimal

import pytest

from asset_allocation.etf_adaptive.contracts import DualPriceBar, ExecutionAvailability
from asset_allocation.etf_adaptive.contracts import DataQualityError
from asset_allocation.etf_adaptive.config import AdaptiveConfig
from asset_allocation.etf_adaptive.research.instrument_validation import (
    CachedValidationProvider,
    FIXED_VALIDATION_TARGETS,
    ValidationScope,
    ValidationStatus,
    evaluate_validation_gate,
    run_instrument_validation,
    resolve_validation_start,
)
from asset_allocation.etf_adaptive.research.decision import DecisionSummary, ResearchConclusion
from asset_allocation.etf_adaptive.research.parameters import ParameterCandidate
from asset_allocation.etf_adaptive.state import BacktestEvent, DailyNav
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
    assert result.decision is not None
    assert result.decision.conclusion is ResearchConclusion.DO_NOT_TRADE


def test_formal_validation_never_activates_a_non_passing_research_decision() -> None:
    """The legacy gate must not override the stricter recorded-evidence decision."""
    from asset_allocation.etf_adaptive.research.instrument_validation import _activation_eligible

    decision = DecisionSummary(ResearchConclusion.CONTINUE_PARAMETER_OPTIMIZATION, ("annual_excess",))

    assert _activation_eligible(ValidationScope.FORMAL, decision) is False
    assert _activation_eligible(ValidationScope.REFERENCE_ONLY, DecisionSummary(ResearchConclusion.PASSED, ())) is False


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


def test_recorded_metrics_and_exposure_use_only_persisted_nav_and_events() -> None:
    from asset_allocation.etf_adaptive.research.instrument_validation import _recorded_exposure, _recorded_performance

    nav = (
        DailyNav(date(2026, 9, 1), Decimal("100"), Decimal("0")),
        DailyNav(date(2026, 9, 2), Decimal("20"), Decimal("90")),
        DailyNav(date(2026, 9, 3), Decimal("120"), Decimal("0")),
    )
    events = (BacktestEvent(date(2026, 9, 2), "fill", (
        ("side", "buy"), ("shares", "9"), ("raw_price", "10"), ("commission", "2.5"),
    )),)

    metrics = _recorded_performance(nav, events)

    assert metrics.total_cost == 2.5
    assert _recorded_exposure(nav) == (1, 2)


def test_staged_training_expands_each_exit_axis_without_cartesian_candidates(monkeypatch: pytest.MonkeyPatch) -> None:
    from asset_allocation.etf_adaptive.research import instrument_validation as module

    base = ParameterCandidate(AdaptiveConfig.default(), family="grid_only")
    observed_sizes: list[int] = []

    def screen(*args):
        candidates = args[4]
        observed_sizes.append(len(candidates))
        return candidates[len(candidates) // 2], ()

    monkeypatch.setattr(module, "_screen_training_candidates", screen)
    selection = module._select_training_candidate(
        "510300.SH", object(), (date(2026, 1, 1),), Decimal("100"), (base,),
        ("step_pct",), 1, ("atr_stop_multiple", "cooldown_sessions"),
    )

    assert selection is not None
    assert observed_sizes == [1, 3, 4]

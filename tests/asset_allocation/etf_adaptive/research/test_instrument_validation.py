"""Contracts for independent fixed-ETF strategy validation."""

from datetime import date, timedelta
from decimal import Decimal

import pytest

from asset_allocation.etf_adaptive.contracts import DualPriceBar, ExecutionAvailability
from asset_allocation.etf_adaptive.contracts import DataQualityError
from asset_allocation.etf_adaptive.config import AdaptiveConfig, CostConfig
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
from asset_allocation.etf_adaptive.state import BacktestEvent, BacktestResult, DailyNav
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
    assert result.evidence is None
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
        ("side", "buy"), ("shares", "1"), ("raw_price", "101"), ("commission", "2.5"),
    )),)

    metrics = _recorded_performance(
        nav, events,
        CostConfig(commission_rate=0.01, minimum_commission=5.0, slippage_bps=100.0),
    )

    assert metrics.total_cost == 6.0
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


def test_oos_only_prices_do_not_change_training_hashes_or_activate_nonpassing_decision(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Training replays never read validation prices, and decision remains the activation gate."""
    from asset_allocation.etf_adaptive.research import instrument_validation as module
    from asset_allocation.etf_adaptive.research.baselines import BaselineKind, BaselineRun
    from asset_allocation.etf_adaptive.research.decision import DecisionSummary
    from asset_allocation.etf_adaptive.research.walk_forward import WalkForwardWindow

    dates = tuple(date(2026, 1, 1) + timedelta(days=index) for index in range(18))
    windows = tuple(
        WalkForwardWindow(
            f"wf_{index:03d}", dates[index * 6:index * 6 + 4], dates[index * 6 + 4:index * 6 + 6],
        )
        for index in range(3)
    )
    monkeypatch.setattr(module, "build_windows", lambda *args, **kwargs: windows)
    monkeypatch.setattr(module, "compute_indicators", lambda bars: tuple(None for _ in bars))
    monkeypatch.setattr(module, "evaluate_research_decision", lambda evidence: DecisionSummary(
        ResearchConclusion.CONTINUE_PARAMETER_OPTIMIZATION, ("annual_excess",),
    ))
    training_requests: list[tuple[date, date]] = []

    def run_baseline(kind, request, provider, config):
        training_requests.append((request.start_date, request.end_date))
        terminal = Decimal("101") if kind is not BaselineKind.BUY_AND_HOLD else Decimal("100")
        return BaselineRun(kind, config, BacktestResult(request, (), (
            DailyNav(request.start_date, Decimal("100"), Decimal("0")),
            DailyNav(request.end_date, terminal, Decimal("0")),
        )))

    def run_baselines(request, provider, config):
        bars = provider.load_bars(request.stock_code, request.trade_start_date, request.end_date)
        nav = tuple(DailyNav(bar.trade_date, Decimal("0"), Decimal(str(bar.raw_close))) for bar in bars)
        strategy_result = BacktestResult(request, (BacktestEvent(request.trade_start_date, "fill", (
            ("side", "buy"), ("shares", "1"), ("raw_price", "100"), ("commission", "0"),
        )),), nav)
        benchmark_result = BacktestResult(request, (), nav)
        return {
            BaselineKind.FULL_ADAPTIVE: BaselineRun(BaselineKind.FULL_ADAPTIVE, config, strategy_result),
            BaselineKind.BUY_AND_HOLD: BaselineRun(BaselineKind.BUY_AND_HOLD, config, benchmark_result),
        }

    monkeypatch.setattr(module, "run_baseline", run_baseline)
    monkeypatch.setattr(module, "run_baselines", run_baselines)

    def validate(oos_multiplier: float):
        oos_dates = {day for window in windows for day in window.validation_dates}
        bars = tuple(DualPriceBar(
            stock_code="515450.SH", trade_date=day,
            signal_open=100.0, signal_high=100.0, signal_low=100.0, signal_close=100.0,
            raw_open=100.0, raw_high=100.0, raw_low=100.0,
            raw_close=100.0 * (oos_multiplier if day in oos_dates else 1.0),
            amount=20_000_000.0, suspended=False, adjustment_ratio=1.0,
            execution_availability=ExecutionAvailability(False, False, "test"),
        ) for day in dates)

        class Provider:
            def load_bars(self, stock_code, start_date, end_date):
                return tuple(bar for bar in bars if start_date <= bar.trade_date <= end_date)

        return run_instrument_validation(
            FIXED_VALIDATION_TARGETS[0], Provider(), dates[0], dates[-1], Decimal("100"),
        )

    baseline = validate(1.0)
    changed_oos = validate(10.0)

    assert tuple(window.config_hash for window in baseline.windows) == tuple(window.config_hash for window in changed_oos.windows)
    assert baseline.decision is not None
    assert baseline.decision.conclusion is not ResearchConclusion.PASSED
    assert baseline.activation_eligible is False
    assert baseline.strategy_metrics is not None
    assert baseline.strategy_metrics.turnover == 3.0
    assert all(end in {day for window in windows for day in window.train_dates} for _, end in training_requests)

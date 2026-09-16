"""Contracts for independent fixed-ETF strategy validation."""

from dataclasses import asdict, replace
from datetime import date, timedelta
from decimal import Decimal
from math import sqrt

import pytest

from asset_allocation.etf_adaptive.contracts import DualPriceBar, ExecutionAvailability
from asset_allocation.etf_adaptive.contracts import DataQualityError
from asset_allocation.etf_adaptive.config import AdaptiveConfig, CostConfig, GridConfig
from asset_allocation.etf_adaptive.research.instrument_validation import (
    CachedValidationProvider,
    FIXED_VALIDATION_TARGETS,
    ValidationScope,
    ValidationStatus,
    evaluate_validation_gate,
    legacy_unprofiled as run_instrument_validation,
    resolve_validation_start,
)
from asset_allocation.etf_adaptive.research.decision import DecisionSummary, ResearchConclusion
from asset_allocation.etf_adaptive.research.parameters import ParameterCandidate
from asset_allocation.etf_adaptive.state import (
    BacktestEvent,
    BacktestResult,
    DailyNav,
    DailyStrategyObservation,
    Regime,
)
from asset_allocation.etf_adaptive.research.walk_forward import build_windows
from asset_allocation.etf_adaptive.research.strategy_profiles import (
    GRID_CORE_PROFILE,
    GRID_PLUS_OPTIONAL_TREND_PROFILE,
    CORE_HOLD_REBALANCE_PROFILE,
)


@pytest.fixture
def profile_validation(monkeypatch):
    """Real OOS execution; deterministic train replays isolate the family gate."""
    from asset_allocation.etf_adaptive.contracts import ETFEligibility
    from asset_allocation.etf_adaptive.research import instrument_validation as module
    from asset_allocation.etf_adaptive.research.baselines import BaselineKind, BaselineRun
    from asset_allocation.etf_adaptive.research.walk_forward import WalkForwardWindow

    dates = tuple(date(2025, 1, 1) + timedelta(days=index) for index in range(335))
    windows = tuple(WalkForwardWindow(
        f"wf_{index:03d}", dates[251 + index * 28:271 + index * 28],
        dates[271 + index * 28:279 + index * 28],
    ) for index in range(3))
    bars = tuple(DualPriceBar(
        stock_code="515450.SH", trade_date=day,
        signal_open=price, signal_high=price * 1.01, signal_low=price * .99, signal_close=price,
        raw_open=price, raw_high=price * 1.01, raw_low=price * .99, raw_close=price,
        amount=20_000_000.0, suspended=False, adjustment_ratio=1.0,
        execution_availability=ExecutionAvailability(False, False, "test"),
    ) for index, day in enumerate(dates) for price in (10 + (index % 5) * .02,))

    class Provider:
        def load_bars(self, stock_code, start_date, end_date):
            return tuple(bar for bar in bars if start_date <= bar.trade_date <= end_date)

        def load_actions(self, stock_code, start_date, end_date):
            return ()

        def load_eligibility(self, stock_code, bars):
            return {bar.trade_date: ETFEligibility(True, (), "core_broad", 252, 20_000_000.0)
                    for bar in bars}

    training_kinds = []

    def replay(kind, request, provider, config):
        training_kinds.append(kind.value)
        values = ((100, 99, 103, 102.5, 110) if kind is BaselineKind.GRID_ONLY else
                  (100, 99, 101, 100.5, 98) if kind is BaselineKind.BUY_AND_HOLD else
                  (100, 100, 100, 100, 100))
        segment = tuple(day for day in dates if request.trade_start_date <= day <= request.end_date)
        nav = tuple(DailyNav(day, Decimal(str(total)), Decimal("0")) for day, total in zip(segment, values))
        return BaselineRun(kind, config, BacktestResult(request, (), nav))

    monkeypatch.setattr(module, "build_windows", lambda *args, **kwargs: windows)
    monkeypatch.setattr(module, "run_baseline", replay)
    candidates = tuple(ParameterCandidate(
        AdaptiveConfig(grid=GridConfig(step_pct=step)), "grid_only",
    ) for step in (.01, .015, .02))

    def validate(profile, *, plan=None, omit_plan=False):
        return module.run_instrument_validation(
            FIXED_VALIDATION_TARGETS[0], Provider(), dates[0], dates[-1], Decimal("100000"),
            profile=profile,
            **({} if omit_plan else {"training_plan": plan if plan is not None else
                                   ({"grid_only": (candidates, ("step_pct",), ())}
                                    if profile.strategy is not None else {})}),
        )

    return validate, training_kinds, candidates


@pytest.mark.parametrize("profile", (GRID_CORE_PROFILE, GRID_PLUS_OPTIONAL_TREND_PROFILE))
def test_profile_accepts_stable_grid_when_standalone_trend_metrics_are_undefined(profile_validation, profile):
    validate, training_kinds, _ = profile_validation

    result = validate(profile)

    assert result.rejection_reason is None
    assert len(result.windows) == 3
    assert result.evidence.stable_parameter_region is True
    assert set(training_kinds) == {"grid_only", "buy_and_hold"}
    for window in result.windows:
        assert window.profile_id == profile.profile_id
        assert set(window.selected_scores) == {"grid_only"}
        assert window.trend_training_surface == ()
        assert window.selected_config["trend"] == asdict(profile.strategy.config.trend)
        assert window.excess_attribution is not None
        assert window.strategy_observations
        assert set(window.benchmark_runs) == {"buy_and_hold", "fixed_half_hold"}
        assert all(run.request.trade_start_date == window.validation_start
                   and run.nav[0].nav_date == window.validation_start
                   for run in window.benchmark_runs.values())
    if profile is GRID_CORE_PROFILE:
        assert all(point.regime is Regime.GRID for window in result.windows
                   for point in window.strategy_observations)


def test_core_hold_rebalance_runs_both_ledgers_without_adaptive_selection(profile_validation, monkeypatch):
    from asset_allocation.etf_adaptive.research import instrument_validation as module

    def adaptive_forbidden(*args, **kwargs):
        pytest.fail("core hold must not execute adaptive selection or strategy")

    monkeypatch.setattr(module, "_select_training_candidate", adaptive_forbidden)
    monkeypatch.setattr(module, "run_strategy_spec", adaptive_forbidden, raising=False)
    validate, training_kinds, _ = profile_validation

    result = validate(CORE_HOLD_REBALANCE_PROFILE, omit_plan=True)

    assert result.rejection_reason is None
    assert len(result.windows) == 3
    assert training_kinds == []
    for window in result.windows:
        assert window.selected_config is None
        assert window.profile_id == "core_hold_rebalance"
        assert not window.candidate_scores and not window.selected_scores
        assert set(window.benchmark_runs) == {"buy_and_hold", "fixed_half_hold"}
        assert window.benchmark_daily_nav == window.benchmark_runs["buy_and_hold"].nav
        assert window.strategy_daily_nav == window.benchmark_runs["fixed_half_hold"].nav
        assert window.strategy_daily_nav != window.benchmark_daily_nav
        assert window.strategy_metrics.total_cost > 0
        assert all(event.kind != "strategy_signal" for event in window.strategy_events)


@pytest.mark.parametrize("profile", (GRID_CORE_PROFILE, GRID_PLUS_OPTIONAL_TREND_PROFILE))
def test_profile_rejects_unstable_grid_without_executing_default_config(profile_validation, profile):
    validate, _, candidates = profile_validation

    result = validate(profile, plan={"grid_only": (candidates[:1], ("step_pct",), ())})

    assert result.rejection_reason == "no_stable_grid_training_parameters"
    assert result.decision.conclusion is ResearchConclusion.DO_NOT_TRADE
    assert result.activation_eligible is False
    assert result.windows[0].profile_id == profile.profile_id
    assert result.windows[0].selected_config is None
    assert not result.windows[0].strategy_events


def test_new_validation_requires_an_explicit_profile():
    from asset_allocation.etf_adaptive.research.instrument_validation import run_instrument_validation

    with pytest.raises(TypeError, match="profile"):
        run_instrument_validation(FIXED_VALIDATION_TARGETS[0], object(),
                                  date(2025, 1, 1), date(2026, 1, 1), Decimal("100000"))


@pytest.mark.parametrize("profile", (GRID_CORE_PROFILE, GRID_PLUS_OPTIONAL_TREND_PROFILE,
                                     CORE_HOLD_REBALANCE_PROFILE))
def test_profile_records_executed_benchmark_provenance_and_cost_evidence(profile_validation, profile):
    validate, _, _ = profile_validation

    result = validate(profile)

    assert result.run_manifest["profile_id"] == profile.profile_id
    assert result.run_manifest["profile_hash"] == profile.profile_hash()
    for window, recorded in zip(result.windows, result.run_manifest["execution_windows"]):
        assert recorded["window_id"] == window.window_id
        assert recorded["profile_id"] == profile.profile_id
        assert recorded["execution_config"] == asdict(window.execution_config)
        assert recorded["reference_benchmark_id"] == "buy_and_hold"
        assert recorded["strategy_spec"] is None if profile.strategy is None else (
            recorded["strategy_spec"]["policy_id"] == profile.strategy.policy_id)
        assert {item["benchmark_id"] for item in recorded["benchmarks"]} == {"buy_and_hold", "fixed_half_hold"}
        for benchmark in recorded["benchmarks"]:
            run = window.benchmark_runs[benchmark["benchmark_id"]]
            assert benchmark["validation_start"] == window.validation_start.isoformat()
            assert benchmark["validation_end"] == run.nav[-1].nav_date.isoformat()
            assert benchmark["nav_sessions"] == len(run.nav)
            assert benchmark["metrics"]["total_cost"] > 0
            assert benchmark["spec_hash"]
            assert benchmark["provenance_hash"]
            assert run.nav[0].total == Decimal("100000")
            assert run.events[0].event_date > window.validation_start


@pytest.mark.parametrize("mutation", ("wrong_family", "trend_axis", "trend_config", "cost_config", "empty"))
def test_profile_rejects_plan_that_cannot_reproduce_frozen_execution(profile_validation, mutation):
    validate, training_kinds, candidates = profile_validation
    axes = ("step_pct",)
    if mutation == "wrong_family":
        candidates = tuple(replace(candidate, family="trend_only") for candidate in candidates)
    elif mutation == "trend_axis":
        axes = ("risk_per_unit",)
    elif mutation == "trend_config":
        candidates = tuple(replace(candidate, config=replace(
            candidate.config, trend=replace(candidate.config.trend, max_units=2),
        )) for candidate in candidates)
    elif mutation == "cost_config":
        candidates = tuple(replace(candidate, config=replace(
            candidate.config, cost=CostConfig(minimum_commission=1),
        )) for candidate in candidates)
    else:
        candidates = ()

    result = validate(GRID_PLUS_OPTIONAL_TREND_PROFILE,
                      plan={"grid_only": (candidates, axes, ())})

    assert result.status is ValidationStatus.DATA_REJECTED
    assert result.decision.conclusion is ResearchConclusion.DO_NOT_TRADE
    assert not result.windows
    assert training_kinds == []


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
    from asset_allocation.etf_adaptive.research.candidate_scoring import TrainingCandidateScore

    base = ParameterCandidate(AdaptiveConfig.default(), family="grid_only")
    observed_sizes: list[int] = []

    def screen(*args):
        candidates = args[4]
        observed_sizes.append(len(candidates))
        selected = candidates[len(candidates) // 2]
        score = TrainingCandidateScore(
            selected.config_hash, asdict(selected.config), 1.0, 0.2, 0.1,
            0.01, 0.001, 0.002, 0.5, True, None,
        )
        return selected, (), (score,)

    monkeypatch.setattr(module, "_screen_training_candidates", screen)
    selection = module._select_training_candidate(
        "510300.SH", object(), (date(2026, 1, 1),), Decimal("100"), (base,),
        ("step_pct",), 1, ("atr_stop_multiple", "cooldown_sessions"),
    )

    assert selection is not None
    assert observed_sizes == [1, 3, 4]


@pytest.fixture
def oos_validation_pair(
    monkeypatch: pytest.MonkeyPatch,
):
    """Replay recorded training paths and price-sensitive OOS paths separately."""
    from asset_allocation.etf_adaptive.research import instrument_validation as module
    from asset_allocation.etf_adaptive.research.baselines import BaselineKind, BaselineRun
    from asset_allocation.etf_adaptive.research.decision import DecisionSummary
    from asset_allocation.etf_adaptive.research.walk_forward import WalkForwardWindow

    dates = tuple(date(2026, 1, 1) + timedelta(days=index) for index in range(66))
    windows = tuple(
        WalkForwardWindow(
            f"wf_{index:03d}", dates[index * 22:index * 22 + 20], dates[index * 22 + 20:index * 22 + 22],
        )
        for index in range(3)
    )
    monkeypatch.setattr(module, "build_windows", lambda *args, **kwargs: windows)
    monkeypatch.setattr(module, "compute_indicators", lambda bars: tuple(None for _ in bars))
    monkeypatch.setattr(module, "evaluate_research_decision", lambda evidence: DecisionSummary(
        ResearchConclusion.CONTINUE_PARAMETER_OPTIMIZATION, ("annual_excess",),
    ))
    training_requests = []

    def run_baseline(kind, request, provider, config):
        training_requests.append(request)
        training_bars = provider.load_bars(request.stock_code, request.start_date, request.end_date)
        totals = (100, 99, 103, 102.5, 104) if kind is not BaselineKind.BUY_AND_HOLD else (100, 98, 101, 100, 102)
        terminal = Decimal(str(totals[-1]))
        terminal *= Decimal(str(sum(bar.raw_close for bar in training_bars) / (100 * len(training_bars))))
        segment = tuple(bar for bar in training_bars if bar.trade_date >= request.trade_start_date)
        assert len(segment) == 5
        nav = tuple(DailyNav(
            bar.trade_date, Decimal(str(total)) if index < 4 else terminal, Decimal("0"),
        ) for index, (bar, total) in enumerate(zip(segment, totals)))
        return BaselineRun(kind, config, BacktestResult(request, (), nav))

    def run_baselines(request, provider, config):
        bars = provider.load_bars(request.stock_code, request.trade_start_date, request.end_date)
        nav = tuple(DailyNav(bar.trade_date, Decimal("0"), Decimal(str(bar.raw_close))) for bar in bars)
        observations = tuple(DailyStrategyObservation(
            point.nav_date, Regime.GRID, 1.0, 1.0, 0, 0, "grid",
        ) for point in nav)
        strategy_result = BacktestResult(request, (BacktestEvent(request.trade_start_date, "fill", (
            ("side", "buy"), ("shares", "1"), ("raw_price", "100"), ("commission", "0"),
        )),), nav, observations)
        benchmark_result = BacktestResult(request, (), nav)
        return {
            BaselineKind.FULL_ADAPTIVE: BaselineRun(BaselineKind.FULL_ADAPTIVE, config, strategy_result),
            BaselineKind.BUY_AND_HOLD: BaselineRun(BaselineKind.BUY_AND_HOLD, config, benchmark_result),
        }

    monkeypatch.setattr(module, "run_baseline", run_baseline)
    monkeypatch.setattr(module, "run_baselines", run_baselines)

    def validate(oos_multiplier: float):
        oos_dates = {day for window in windows for day in window.validation_dates}
        oos_ends = {window.validation_dates[-1] for window in windows}
        bars = tuple(DualPriceBar(
            stock_code="515450.SH", trade_date=day,
            signal_open=100.0, signal_high=100.0, signal_low=100.0, signal_close=100.0,
            raw_open=100.0, raw_high=100.0, raw_low=100.0,
            raw_close=100.0 * (oos_multiplier ** (2 if day in oos_ends else 1) if day in oos_dates else 1.0),
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
    return baseline, changed_oos, training_requests, windows, validate


def test_oos_only_prices_do_not_change_training_hashes_or_activate_nonpassing_decision(
    oos_validation_pair,
) -> None:
    """Training replays never read validation prices, and decision remains the activation gate."""
    baseline, changed_oos, training_requests, windows, _ = oos_validation_pair

    assert tuple(window.config_hash for window in baseline.windows) == tuple(window.config_hash for window in changed_oos.windows)
    assert baseline.decision is not None
    assert baseline.decision.conclusion is not ResearchConclusion.PASSED
    assert baseline.activation_eligible is False
    assert baseline.strategy_metrics is not None
    assert baseline.strategy_metrics.turnover == 3.0
    training_dates = {day for window in windows for day in window.train_dates}
    assert all(request.end_date in training_dates for request in training_requests)
    assert all(request.trade_start_date in training_dates for request in training_requests)
    assert all(request.start_date <= request.trade_start_date for request in training_requests)
    # Reproducibility evidence records actual selected parameters and the exact
    # data snapshot; changing only OOS bars must change the latter, not the former.
    assert baseline.run_manifest is not None and changed_oos.run_manifest is not None
    assert baseline.run_manifest["data_fingerprint"] != changed_oos.run_manifest["data_fingerprint"]
    assert baseline.run_manifest["selected_configs"] == changed_oos.run_manifest["selected_configs"]
    assert all(window.selected_config is not None for window in baseline.windows)


def test_oos_mutation_cannot_change_recorded_training_scores(oos_validation_pair) -> None:
    baseline, changed_oos, _, _, _ = oos_validation_pair

    assert len(baseline.windows) == len(changed_oos.windows) == 3
    assert baseline.windows[0].strategy_return != changed_oos.windows[0].strategy_return
    for before, after in zip(baseline.windows, changed_oos.windows):
        assert before.candidate_scores
        assert before.candidate_scores == after.candidate_scores
        assert before.selected_scores == after.selected_scores
        assert before.screened_axes == after.screened_axes == {
            "grid_only": (("step_pct", "unit_pct", "fixed_initial_pct"),
                          ("atr_stop_multiple",), ("cooldown_sessions",)),
            "trend_only": (("risk_per_unit", "add_n", "max_units", "amount_ratio_min"),
                           ("stop_n",), ("require_macd_bullish",)),
        }
        assert len(before.candidate_scores) == 220 + 3 + 4 + 144 + 4 + 2
        for family, selected in before.selected_scores.items():
            assert selected in before.candidate_scores
            assert selected.stable is True
            assert selected.rejection_reason is None
            section = "grid" if family == "grid_only" else "trend"
            assert selected.config[section] == before.selected_config[section]


def test_formal_validation_rejects_missing_strategy_observations(
    oos_validation_pair, monkeypatch: pytest.MonkeyPatch,
) -> None:
    # Break caught: formal validation cannot publish a decision or manifest
    # when the recorded state required for causal attribution is absent.
    from asset_allocation.etf_adaptive.research import instrument_validation as module
    from asset_allocation.etf_adaptive.research.baselines import BaselineKind, BaselineRun

    _, _, _, _, validate = oos_validation_pair
    recorded_runs = module.run_baselines

    def missing_observations(request, provider, config):
        runs = recorded_runs(request, provider, config)
        strategy = runs[BaselineKind.FULL_ADAPTIVE]
        return {
            **runs,
            BaselineKind.FULL_ADAPTIVE: BaselineRun(
                strategy.kind,
                strategy.config,
                replace(strategy.result, observations=()),
                strategy.notes,
                strategy.strategy_spec_hash,
                strategy.benchmark_spec_hash,
            ),
        }

    monkeypatch.setattr(module, "run_baselines", missing_observations)

    result = validate(1.0)

    assert result.status is ValidationStatus.DATA_REJECTED
    assert result.evidence is None
    assert result.run_manifest is None
    assert result.rejection_reason == "strategy observations are required for formal validation"


@pytest.mark.parametrize("lower_neighbor", ("present", "missing", "unrelated_axis"))
def test_training_ranks_all_plateau_members_and_rejects_inexact_neighbors(
    monkeypatch: pytest.MonkeyPatch, lower_neighbor: str,
) -> None:
    from asset_allocation.etf_adaptive.research import instrument_validation as module
    from asset_allocation.etf_adaptive.research.baselines import BaselineKind, BaselineRun

    dates = tuple(date(2026, 1, 1) + timedelta(days=index) for index in range(10))
    candidates = tuple(ParameterCandidate(
        AdaptiveConfig(grid=GridConfig(step_pct=step)), family="grid_only",
    ) for step in (0.01, 0.015, 0.02, 0.025, 0.03))
    if lower_neighbor == "missing":
        candidates = candidates[1:]
    elif lower_neighbor == "unrelated_axis":
        candidates = (replace(candidates[0], config=replace(
            candidates[0].config, grid=replace(candidates[0].config.grid, unit_pct=0.15),
        )), *candidates[1:])

    def replay(kind, request, provider, config):
        if kind is BaselineKind.BUY_AND_HOLD:
            totals = (100, 98, 101, 100, 102)
        elif config.grid.step_pct == 0.01:
            totals = (100, 99, 150, 149.5, 200)
        elif config.grid.step_pct == 0.015:
            totals = (100, 99, 102, 101.5, 103)
        else:
            totals = (100, 90, 105, 97, 103)
        segment = tuple(day for day in dates if request.trade_start_date <= day <= request.end_date)
        assert len(segment) == 5
        nav = tuple(DailyNav(day, Decimal("0"), Decimal(str(total))) for day, total in zip(segment, totals))
        return BaselineRun(kind, config, BacktestResult(request, (), nav))

    monkeypatch.setattr(module, "run_baseline", replay)
    selection = module._select_training_candidate(
        "510300.SH", object(), dates, Decimal("100"), candidates, ("step_pct",), 5,
    )

    assert selection is not None
    expected_step = 0.015 if lower_neighbor == "present" else 0.02
    assert selection.candidate.config.grid.step_pct == expected_step
    scores = {row.config["grid"]["step_pct"]: row for row in selection.candidate_scores}
    assert len(scores) == len(candidates)
    assert scores[0.015].stable is (lower_neighbor == "present")
    assert scores[0.015].rejection_reason == (None if lower_neighbor == "present" else "outside_stable_plateau")
    assert scores[0.03].rejection_reason == "outside_stable_plateau"
    if lower_neighbor == "present":
        assert scores[0.01].sortino_excess > scores[0.015].sortino_excess
        assert scores[0.01].rejection_reason == "outside_stable_plateau"
    assert selection.selected_score == scores[expected_step]
    assert all(row.family == "grid_only" and row.screened_axes == ("step_pct",)
               for row in selection.candidate_scores)


def test_training_scores_aggregate_recorded_subperiod_risk_cost_and_exposure(monkeypatch) -> None:
    from asset_allocation.etf_adaptive.research import instrument_validation as module
    from asset_allocation.etf_adaptive.research.baselines import BaselineKind, BaselineRun

    dates = tuple(date(2026, 1, 1) + timedelta(days=index) for index in range(20))
    candidates = tuple(ParameterCandidate(AdaptiveConfig(
        grid=GridConfig(step_pct=step),
        cost=CostConfig(commission_rate=0.01, minimum_commission=5, slippage_bps=100),
    ), family="grid_only") for step in (0.01, 0.015, 0.02))

    def replay(kind, request, provider, config):
        final_segment = request.trade_start_date == dates[15]
        strategy = kind is BaselineKind.GRID_ONLY
        # Returns: good = (+10%, -10%, +10%, -5%);
        # bad = (+5%, -15%, +5%, -10%). Swap in the fourth segment.
        good = (100, 110, 99, 108.9, 103.455)
        bad = (100, 105, 89.25, 93.7125, 84.34125)
        totals = tuple(value * 100 for value in (good if strategy != final_segment else bad))
        segment = tuple(day for day in dates if request.trade_start_date <= day <= request.end_date)
        invested_indexes = {1, 2, 3, 4} if final_segment else {1, 2}
        nav = tuple(DailyNav(
            day,
            Decimal("0") if index in invested_indexes else Decimal(str(total)),
            Decimal(str(total)) if index in invested_indexes else Decimal("0"),
        ) for index, (day, total) in enumerate(zip(segment, totals)))
        shares = "2" if final_segment else "1"
        fee = ("10" if final_segment else "5") if strategy else "100"
        events = (BacktestEvent(segment[1], "fill", (
            ("side", "buy"), ("shares", shares), ("raw_price", "101"), ("commission", fee),
        )),)
        return BaselineRun(kind, config, BacktestResult(request, events, nav))

    monkeypatch.setattr(module, "run_baseline", replay)
    selection = module._select_training_candidate(
        "510300.SH", object(), dates, Decimal("10000"), candidates, ("step_pct",), 5,
    )

    assert selection is not None
    score = selection.selected_score
    # Hand-derived: equal subperiod weights give half the good-minus-bad
    # excess; both return paths have population variance 0.00796875 and
    # downside deviation 0.025. NAVs already include costs.
    annual_excess = 1.03455 ** 63 - 0.8434125 ** 63
    assert score.positive_subperiod_share == 0.75
    assert score.sortino_excess == pytest.approx(annual_excess / (0.05 * sqrt(252)))
    assert score.sharpe_excess == pytest.approx(annual_excess / (2 * sqrt(0.00796875 * 252)))
    assert score.drawdown_improvement == pytest.approx(0.048375)
    assert score.cvar5_improvement == pytest.approx(0.025)
    assert score.cost_drag == pytest.approx(0.00075)  # (6 + 6 + 6 + 12) / 40000
    assert score.exposure_ratio == 0.5  # (2 + 2 + 2 + 4) / 20
    assert score.stable is True


@pytest.mark.parametrize("unavailable_kind,totals,only_final_segment", (
    ("grid_only", (100, 100, 100, 100, 100), False),
    ("grid_only", (100, 101, 103, 105, 110), False),
    ("grid_only", (100, 105, 104, 108, 110), False),
    ("grid_only", (100, 50, 100, 50, 110), False),
    ("buy_and_hold", (100, 100, 100, 100, 100), False),
    ("buy_and_hold", (100, 101, 103, 105, 109), False),
    ("grid_only", (100, 100, 100, 100, 100), True),
))
def test_undefined_training_ratios_reject_the_score_without_changing_legacy_metrics(
    monkeypatch, unavailable_kind, totals, only_final_segment,
) -> None:
    from asset_allocation.etf_adaptive.research import instrument_validation as module
    from asset_allocation.etf_adaptive.research.baselines import BaselineKind, BaselineRun

    dates = tuple(date(2026, 1, 1) + timedelta(days=index) for index in range(20))
    candidates = tuple(ParameterCandidate(
        AdaptiveConfig(grid=GridConfig(step_pct=step)), family="grid_only",
    ) for step in (0.01, 0.015, 0.02))
    legacy_fallbacks = []

    def replay(kind, request, provider, config):
        values = (100, 99, 103, 102.5, 110) if kind is BaselineKind.GRID_ONLY else (100, 99, 101, 100.5, 98)
        unavailable = kind.value == unavailable_kind and (not only_final_segment or request.trade_start_date == dates[15])
        if unavailable:
            values = totals
        segment = tuple(day for day in dates if request.trade_start_date <= day <= request.end_date)
        nav = tuple(DailyNav(day, Decimal(str(total)), Decimal("0")) for day, total in zip(segment, values))
        if unavailable:
            legacy_fallbacks.append(module._recorded_performance(nav, (), config.cost).sortino)
        return BaselineRun(kind, config, BacktestResult(request, (), nav))

    monkeypatch.setattr(module, "run_baseline", replay)
    selected, _, scores = module._screen_training_candidates(
        "510300.SH", object(), dates, Decimal("100"), candidates, ("step_pct",), 5,
    )

    assert legacy_fallbacks and all(value == 0.0 for value in legacy_fallbacks)
    assert selected is None
    assert len(scores) == 3
    for score in scores:
        assert score.stable is False
        assert score.sortino_excess is None
        assert "unavailable_training_metrics" in score.rejection_reason
        if len(set(totals)) == 1:
            assert score.sharpe_excess is None


def test_recorded_training_cost_above_two_percent_cannot_be_promoted_by_stability(monkeypatch) -> None:
    from asset_allocation.etf_adaptive.research import instrument_validation as module
    from asset_allocation.etf_adaptive.research.baselines import BaselineKind, BaselineRun

    dates = tuple(date(2026, 1, 1) + timedelta(days=index) for index in range(5))
    candidates = tuple(ParameterCandidate(AdaptiveConfig(
        grid=GridConfig(step_pct=step), cost=CostConfig(slippage_bps=0),
    ), family="grid_only") for step in (0.01, 0.015, 0.02))

    def replay(kind, request, provider, config):
        values = (100, 99, 103, 102.5, 110) if kind is BaselineKind.GRID_ONLY else (100, 99, 101, 100.5, 98)
        nav = tuple(DailyNav(day, Decimal(str(total)), Decimal("0")) for day, total in zip(dates, values))
        events = (BacktestEvent(dates[1], "fill", (
            ("side", "buy"), ("shares", "1"), ("raw_price", "100"), ("commission", "5"),
        )),)
        return BaselineRun(kind, config, BacktestResult(request, events, nav))

    monkeypatch.setattr(module, "run_baseline", replay)
    selected, _, scores = module._screen_training_candidates(
        "510300.SH", object(), dates, Decimal("100"), candidates, ("step_pct",), 5,
    )

    assert selected is None
    assert all(score.cost_drag == 0.05 for score in scores)
    assert all(score.stable is False and score.rejection_reason == "cost_drag_out_of_bounds" for score in scores)


def test_training_segments_keep_prior_history_for_eligibility_without_booking_warmup(monkeypatch) -> None:
    """Each train replay warms eligibility from prior data but books only its own segment."""
    from asset_allocation.etf_adaptive.research import instrument_validation as module
    from asset_allocation.etf_adaptive.research.baselines import BaselineKind, BaselineRun

    history_start = date(2025, 1, 1)
    dates = tuple(date(2026, 1, 1) + timedelta(days=index) for index in range(20))
    candidates = tuple(ParameterCandidate(
        AdaptiveConfig(grid=GridConfig(step_pct=step)), family="grid_only",
    ) for step in (0.01, 0.015, 0.02))
    requests = []

    def replay(kind, request, provider, config):
        requests.append(request)
        segment = tuple(day for day in dates if request.trade_start_date <= day <= request.end_date)
        values = (100, 99, 103, 100, 110) if kind is BaselineKind.GRID_ONLY else (100, 98, 101, 99, 102)
        nav = tuple(DailyNav(day, Decimal(str(total)), Decimal("0")) for day, total in zip(segment, values))
        return BaselineRun(kind, config, BacktestResult(request, (), nav))

    monkeypatch.setattr(module, "run_baseline", replay)
    module._screen_training_candidates(
        "510300.SH", object(), dates, Decimal("100"), candidates, ("step_pct",), 5,
        history_start=history_start,
    )

    assert requests
    assert {request.start_date for request in requests} == {history_start}
    assert {request.trade_start_date for request in requests} == {dates[index] for index in range(0, len(dates), 5)}
    assert all(request.end_date in dates and request.end_date < dates[-1] or request.end_date == dates[-1]
               for request in requests)


def test_second_training_segment_keeps_prior_training_indicator_history(monkeypatch) -> None:
    # Dropping 126 prior TRAINING days removes the first day's usable MA20.
    from asset_allocation.etf_adaptive.indicators import compute_indicators
    from asset_allocation.etf_adaptive.research import instrument_validation as module
    from asset_allocation.etf_adaptive.research.baselines import BaselineRun

    days = tuple(date(2024, 1, 1) + timedelta(days=index) for index in range(503))
    bars = tuple(DualPriceBar(
        "510300.SH", day, price, price, price, price, price, price, price, price,
        20_000_000.0, False, 1.0,
    ) for index, day in enumerate(days) for price in (10.0 if index < 251 else 20.0,))

    class Provider:
        def load_bars(self, stock_code, start_date, end_date):
            return tuple(bar for bar in bars if start_date <= bar.trade_date <= end_date)

    observed = []

    def replay(kind, request, provider, config):
        history = provider.load_bars(request.stock_code, request.start_date, request.trade_start_date)
        if request.trade_start_date == days[377]:
            snapshot = compute_indicators(history)[-1]
            observed.append((len(history), snapshot.ma20 if snapshot is not None else None))
        nav = tuple(DailyNav(day, Decimal(str(total)), Decimal("0"))
                    for day, total in zip(days[days.index(request.trade_start_date):], (100, 99, 103, 101, 105)))
        return BaselineRun(kind, config, BacktestResult(request, (), nav))

    monkeypatch.setattr(module, "run_baseline", replay)
    module._screen_training_candidates(
        "510300.SH", Provider(), days[251:], Decimal("100"),
        (ParameterCandidate(AdaptiveConfig.default(), family="grid_only"),),
        ("step_pct",), 126, history_start=days[0], evaluation_start=days[251],
    )

    assert observed == [(378, 20.0), (378, 20.0)]

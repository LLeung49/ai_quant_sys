import json
from collections.abc import Mapping
from copy import deepcopy
from dataclasses import asdict, replace
from datetime import date
from decimal import Decimal
from hashlib import sha256
from pathlib import Path

import pytest

from asset_allocation.etf_adaptive.contracts import DualPriceBar, SubLayer
from asset_allocation.etf_adaptive.config import AdaptiveConfig
from asset_allocation.etf_adaptive.research.attribution import build_excess_attribution
from asset_allocation.etf_adaptive.research.candidate_scoring import TrainingCandidateScore
from asset_allocation.etf_adaptive.research.experiment import ExperimentSpec, bind_experiment, APPROVED_EXPERIMENT_AXES
from asset_allocation.etf_adaptive.research.strategy_profiles import (
    CORE_HOLD_REBALANCE_PROFILE,
    GRID_CORE_PROFILE,
    GRID_PLUS_OPTIONAL_TREND_PROFILE,
)
from asset_allocation.etf_adaptive.research.strategy_specs import (
    BUY_AND_HOLD_SPEC,
    FULL_ADAPTIVE_SPEC,
    benchmark_provenance_hash,
)
from asset_allocation.etf_adaptive.research.decision import DecisionSummary, ResearchConclusion, ResearchEvidence
from asset_allocation.etf_adaptive.research.instrument_validation import (
    InstrumentValidationResult, TrainingSurfaceSummary, ValidationScope,
    ValidationStatus, ValidationTarget, ValidationWindowResult,
)
from asset_allocation.etf_adaptive.research.metrics import PerformanceMetrics
from asset_allocation.etf_adaptive.research.validation_report import (
    validation_publication_decision,
    write_validation_artifacts,
)
from asset_allocation.etf_adaptive.state import (
    BacktestEvent,
    BacktestRequest,
    BacktestResult,
    DailyNav,
    DailyStrategyObservation,
    Regime,
)


def _metrics(*, annual_return: float, sortino: float, total_cost: float) -> PerformanceMetrics:
    return PerformanceMetrics(
        annual_return=annual_return, annual_volatility=0.20, sharpe=0.50,
        sortino=sortino, calmar=0.40, worst_126_session_return=-0.08,
        cvar5=-0.03, win_rate=0.55, payoff_ratio=1.20, profit_factor=1.30,
        turnover=0.90, minimum_commission_share=0.25, unfilled_share=0.0,
        slippage_degradation=0.10, max_drawdown=-0.12, recovery_sessions=20,
        total_cost=total_cost,
    )


def _recorded_result() -> InstrumentValidationResult:
    target = ValidationTarget("test", "159915.SZ", SubLayer.DOMESTIC_GROWTH)
    strategy_metrics = _metrics(annual_return=0.10, sortino=0.70, total_cost=1.0)
    benchmark_metrics = _metrics(annual_return=0.08, sortino=0.40, total_cost=0.2)
    days = (date(2025, 7, 1), date(2025, 7, 2), date(2025, 7, 3))
    bars = tuple(
        DualPriceBar("159915.SZ", day, 1.0 + index / 100, 1.1 + index / 100,
                     0.9 + index / 100, 1.0 + index / 100, 1.0 + index / 100,
                     1.1 + index / 100, 0.9 + index / 100, 1.0 + index / 100,
                     100_000.0, False, 1.0)
        for index, day in enumerate(days)
    )
    strategy_nav = (
        DailyNav(days[0], Decimal("100"), Decimal("0")),
        DailyNav(days[1], Decimal("20"), Decimal("82")),
        DailyNav(days[2], Decimal("10"), Decimal("100")),
    )
    benchmark_nav = tuple(DailyNav(day, Decimal("0"), Decimal("100") + index) for index, day in enumerate(days))
    window = ValidationWindowResult(
        "wf_000", date(2025, 1, 2), days[0], "abc123", 0.10, 0.08,
        (1.0, 1.02, 1.10), (1.0, 1.01, 1.08),
        (BacktestEvent(days[1], "fill", (("side", "buy"), ("shares", "80"),
                                            ("raw_price", "1.02"), ("reason", "trend_entry"),
                                            ("commission", "5"))),),
        (), strategy_nav, benchmark_nav, bars, (), strategy_metrics, benchmark_metrics,
        2, 1, 3, 0,
        (TrainingSurfaceSummary("grid-hash", (True, True), (0.01, 0.02), 1.0),),
        (TrainingSurfaceSummary("trend-hash", (True, True), (0.01, 0.02), 1.0),),
        None,
        {"grid": {"step_pct": 0.02}, "trend": {"stop_n": 2.0}, "cost": {"slippage_bps": 3.0}},
    )
    evidence = ResearchEvidence(
        data_valid=True, oos_window_count=3, oos_non_lagging_share=1.0,
        stable_parameter_region=True, annual_excess=0.02, drawdown_improvement=0.04,
        sharpe_excess=0.20, sortino_excess=0.30, calmar_excess=0.10,
        cvar5_improvement=0.01, exposure_ratio=2 / 3, turnover=0.90,
        total_cost=1.0, initial_oos_nav=100.0, cost_drag=0.01,
    )
    config = AdaptiveConfig.default()
    observations = tuple(DailyStrategyObservation(day, Regime.TREND, 1.0,
                         float(point.market_value / point.total), 0, 0, "hold")
                         for day, point in zip(days, strategy_nav))
    scores = (TrainingCandidateScore(config.config_hash(), asdict(config),
              1.0, 0.3, 0.2, 0.04, 0.01, 0.01, 0.7, True, None,
              family="grid_only", screened_axes=("step_pct",)),)
    window = replace(window, config_hash=config.config_hash(), selected_config=asdict(config),
                     cost_config=config.cost,
                     screened_axes={"grid_only": (("step_pct",),)},
                     candidate_scores=scores, selected_scores={score.family: score for score in scores},
                     strategy_observations=observations,
                     excess_attribution=build_excess_attribution(strategy_nav, benchmark_nav, observations,
                                                                window.strategy_events, execution_cost=1.0))
    result = InstrumentValidationResult(
        target=target, status=ValidationStatus.PASSED, as_of_date=date(2026, 9, 8),
        windows=(window, replace(window, window_id="wf_001"), replace(window, window_id="wf_002")),
        strategy_annual_return=0.10, benchmark_annual_return=0.08,
        strategy_max_drawdown=0.12, benchmark_max_drawdown=0.16,
        scope=ValidationScope.FORMAL, activation_eligible=True, evidence=evidence,
        decision=DecisionSummary(ResearchConclusion.PASSED, ()),
        strategy_metrics=strategy_metrics, benchmark_metrics=benchmark_metrics,
        strategy_invested_sessions=6, strategy_cash_sessions=3,
        benchmark_invested_sessions=9, benchmark_cash_sessions=0,
        run_manifest={
            "schema_version": 1, "runner": "test", "source_provider": "test",
            "data_cutoff": "2026-09-08", "requested_start": "2025-01-02",
            "data_fingerprint": "test", "target": {"stock_code": "159915.SZ"},
            "selected_configs": [
                {"window_id": item.window_id, "config_hash": item.config_hash, "config": item.selected_config}
                for item in (window, replace(window, window_id="wf_001"), replace(window, window_id="wf_002"))
            ],
            "screened_axes": {"grid": ["step_pct"]},
        },
    )
    spec = ExperimentSpec(
        "recorded-test", ("159915.SZ",), GRID_PLUS_OPTIONAL_TREND_PROFILE,
        {"step_pct": (0.02,), "unit_pct": (0.1, 0.15)},
        date(2025, 1, 2), result.as_of_date,
    )
    return bind_experiment(result, spec)


def _legacy_recorded_result() -> InstrumentValidationResult:
    result = _recorded_result()
    legacy_payload = {
        "experiment_id": "recorded-test",
        "target_codes": ["159915.SZ"],
        "strategy": asdict(FULL_ADAPTIVE_SPEC),
        "benchmarks": [asdict(BUY_AND_HOLD_SPEC)],
        "allowed_axes": {axis: list(values) for axis, values in APPROVED_EXPERIMENT_AXES.items()},
        "start_date": "2025-01-02",
        "as_of_date": result.as_of_date.isoformat(),
    }
    rebound = bind_experiment(result, ExperimentSpec.from_dict(legacy_payload))
    manifest = dict(rebound.run_manifest)
    legacy_hash = sha256(json.dumps(
        legacy_payload, sort_keys=True, separators=(",", ":"), allow_nan=False,
    ).encode("utf-8")).hexdigest()
    manifest.update(experiment=legacy_payload, experiment_hash=legacy_hash)
    return replace(rebound, run_manifest=manifest)


def _optional_trend_manifest(result: InstrumentValidationResult) -> Mapping[str, object]:
    spec = ExperimentSpec(
        "optional-trend-report", (result.target.stock_code,),
        GRID_PLUS_OPTIONAL_TREND_PROFILE, {"step_pct": (0.02,)},
        date(2025, 1, 2), result.as_of_date,
    )
    return bind_experiment(result, spec).run_manifest


def _profiled_recorded_result(profile=GRID_PLUS_OPTIONAL_TREND_PROFILE) -> InstrumentValidationResult:
    from asset_allocation.etf_adaptive.research.instrument_validation import (
        _recorded_performance,
        _run_manifest,
        _stitch_paths,
    )
    from asset_allocation.etf_adaptive.research.metrics import calculate_performance

    result = _recorded_result()
    config = AdaptiveConfig.default()
    windows = []
    for window in result.windows:
        request = BacktestRequest(
            result.target.stock_code,
            window.strategy_daily_nav[0].total,
            window.validation_start,
            window.strategy_daily_nav[-1].nav_date,
            window.validation_start,
        )
        benchmark_runs = {
            "buy_and_hold": BacktestResult(
                request, window.benchmark_events, window.benchmark_daily_nav,
            ),
            "fixed_half_hold": BacktestResult(
                request, window.strategy_events, window.strategy_daily_nav,
            ),
        }
        updates = {
            "profile_id": profile.profile_id,
            "benchmark_runs": benchmark_runs,
            "execution_config": config,
            "strategy_metrics": _recorded_performance(
                window.strategy_daily_nav, window.strategy_events, config.cost,
            ),
            "benchmark_metrics": _recorded_performance(
                window.benchmark_daily_nav, window.benchmark_events, config.cost,
            ),
        }
        updates["excess_attribution"] = build_excess_attribution(
            window.strategy_daily_nav,
            window.benchmark_daily_nav,
            window.strategy_observations,
            window.strategy_events,
            execution_cost=updates["strategy_metrics"].total_cost,
        )
        if profile is CORE_HOLD_REBALANCE_PROFILE:
            updates.update(
                selected_config=None,
                candidate_scores=(),
                selected_scores={},
                screened_axes={},
                strategy_observations=(),
                excess_attribution=None,
                grid_training_surface=(),
                trend_training_surface=(),
            )
        windows.append(replace(window, **updates))
    strategy_path = _stitch_paths(tuple(window.strategy_nav for window in windows))
    benchmark_path = _stitch_paths(tuple(window.benchmark_nav for window in windows))
    strategy_metrics = replace(
        calculate_performance(strategy_path, ()),
        total_cost=sum(window.strategy_metrics.total_cost for window in windows),
    )
    benchmark_metrics = replace(
        calculate_performance(benchmark_path, ()),
        total_cost=sum(window.benchmark_metrics.total_cost for window in windows),
    )
    evidence = replace(
        result.evidence,
        drawdown_improvement=(
            abs(benchmark_metrics.max_drawdown) - abs(strategy_metrics.max_drawdown)
        ),
        cvar5_improvement=benchmark_metrics.cvar5 - strategy_metrics.cvar5,
        total_cost=strategy_metrics.total_cost,
        cost_drag=strategy_metrics.total_cost / result.evidence.initial_oos_nav,
    )
    result = replace(
        result,
        windows=tuple(windows),
        strategy_metrics=strategy_metrics,
        benchmark_metrics=benchmark_metrics,
        strategy_max_drawdown=abs(strategy_metrics.max_drawdown),
        benchmark_max_drawdown=abs(benchmark_metrics.max_drawdown),
        evidence=evidence,
    )
    manifest = _run_manifest(
        result.target,
        date(2025, 1, 2),
        result.as_of_date,
        object(),
        result.windows[0].market_bars,
        result.windows,
        profile=profile,
    )
    result = replace(result, run_manifest=manifest)
    spec = ExperimentSpec(
        f"{profile.profile_id}-report", (result.target.stock_code,), profile,
        {"step_pct": (0.02,)} if profile.selection_families else {},
        date(2025, 1, 2), result.as_of_date,
    )
    if profile.strategy is None:
        manifest = dict(result.run_manifest)
        manifest.update(
            experiment=spec.to_dict(),
            experiment_hash=spec.experiment_hash(),
            strategy_spec=None,
            benchmark_specs=[asdict(item) for item in spec.benchmarks],
            experiment_windows=[
                {
                    "window_id": window.window_id,
                    "execution_cost_config": asdict(window.cost_config),
                    "screened_axes": window.screened_axes,
                    "strategy_spec": None,
                    "benchmark_specs": [
                        {
                            **asdict(item),
                            "spec_hash": item.spec_hash(),
                            "config": asdict(window.execution_config),
                            "provenance_hash": benchmark_provenance_hash(
                                item, window.execution_config,
                            ),
                        }
                        for item in spec.benchmarks
                    ],
                    "selected_scores": {},
                    "candidate_scores": [],
                    "excess_attribution": None,
                }
                for window in result.windows
            ],
        )
        return replace(result, run_manifest=manifest)
    return bind_experiment(result, spec)


def test_optional_trend_report_publishes_required_integrated_diagnostics(tmp_path) -> None:
    # Break caught: an optional-TREND report can omit its profile identity and observed mode diagnostics.
    recorded = _profiled_recorded_result()
    result = replace(recorded, run_manifest=_optional_trend_manifest(recorded))

    summary = json.loads(
        write_validation_artifacts(result, tmp_path / "report").summary_json.read_text()
    )

    assert summary["strategy_profile"]["profile_id"] == "grid_plus_optional_trend"
    assert summary["trend_diagnostics"]["active_sessions"] >= 0
    assert "incremental_execution_cost" in summary["trend_diagnostics"]


def test_optional_trend_report_is_do_not_trade_when_attribution_is_missing(tmp_path) -> None:
    # Break caught: missing optional-TREND attribution can fall through to a generic or publishable decision.
    recorded = _profiled_recorded_result()
    result = replace(recorded, run_manifest=_optional_trend_manifest(recorded))
    result = replace(
        result,
        windows=(replace(result.windows[0], excess_attribution=None), *result.windows[1:]),
    )

    summary = json.loads(
        write_validation_artifacts(result, tmp_path / "report").summary_json.read_text()
    )

    assert summary["decision"]["conclusion"] == "do_not_trade"
    assert "profile_mode_attribution" in summary["decision"]["blockers"]


def test_complete_recorded_profile_execution_removes_unexecuted_benchmark_blocker(tmp_path) -> None:
    # Break caught: declarations alone or a legacy one-benchmark assumption can reject actual OOS ledgers.
    result = _profiled_recorded_result()

    summary = json.loads(
        write_validation_artifacts(result, tmp_path / "report").summary_json.read_text()
    )

    assert "unexecuted_benchmark_evidence" not in summary["decision"]["blockers"]
    assert summary["decision"]["conclusion"] == "passed"
    assert summary["strategy_profile"] == {
        "profile_id": "grid_plus_optional_trend",
        "version": "1",
        "profile_hash": "f4f9eb95055b94fd1694c9f43501573cd2e7eb3f2e5590104fa2a83fd6ebf8b1",
        "executable_strategy_id": "full_adaptive",
        "benchmark_hashes": {
            "buy_and_hold": "3958c38c790b7737f3af03d4a690f2509833bfa7f847fbd3e06c6a8e5cafd0c3",
            "fixed_half_hold": "ac073b13dfd8fc5232bf30851ba89adea309c68abd84a01a15249842c1d2e597",
        },
    }
    assert summary["trend_diagnostics"]["active_sessions"] == 6
    assert summary["trend_diagnostics"]["execution_cost"] == pytest.approx(15.073417974607617)
    assert summary["trend_diagnostics"]["incremental_execution_cost"] == pytest.approx(15.073417974607617)


def test_missing_recorded_profile_benchmark_run_remains_fail_closed() -> None:
    # Break caught: manifest declarations can be mistaken for proof that every benchmark executed.
    result = _profiled_recorded_result()
    window = result.windows[0]
    result = replace(
        result,
        windows=(
            replace(window, benchmark_runs={"buy_and_hold": window.benchmark_runs["buy_and_hold"]}),
            *result.windows[1:],
        ),
    )

    decision = validation_publication_decision(result)

    assert decision["conclusion"] == "do_not_trade"
    assert "unexecuted_benchmark_evidence" in decision["blockers"]


@pytest.mark.parametrize("forgery", ("profile_hash", "benchmark_provenance"))
def test_forged_recorded_profile_execution_remains_fail_closed(forgery) -> None:
    # Break caught: self-declared profile or benchmark metadata can be accepted without ledger reconciliation.
    result = _profiled_recorded_result()
    manifest = deepcopy(result.run_manifest)
    if forgery == "profile_hash":
        manifest["profile_hash"] = "forged"
    else:
        manifest["execution_windows"][0]["benchmarks"][0]["provenance_hash"] = "forged"

    decision = validation_publication_decision(replace(result, run_manifest=manifest))

    assert decision["conclusion"] == "do_not_trade"
    assert "unexecuted_benchmark_evidence" in decision["blockers"]


def test_unreconciled_optional_trend_attribution_uses_profile_blocker() -> None:
    # Break caught: finite but forged mode returns can bypass the optional-TREND evidence gate.
    result = _profiled_recorded_result()
    attribution = replace(
        result.windows[0].excess_attribution,
        trend_return=result.windows[0].excess_attribution.trend_return + 0.1,
    )
    result = replace(
        result,
        windows=(replace(result.windows[0], excess_attribution=attribution), *result.windows[1:]),
    )

    decision = validation_publication_decision(result)

    assert decision["conclusion"] == "do_not_trade"
    assert "profile_mode_attribution" in decision["blockers"]


def test_optional_trend_report_rejects_cost_not_reconciled_to_recorded_events(tmp_path) -> None:
    # Break caught: matching forged metric/attribution cost fields can bypass the recorded-event ledger.
    result = _profiled_recorded_result()
    window = result.windows[0]
    forged_cost = window.strategy_metrics.total_cost + 7.0
    forged_window = replace(
        window,
        strategy_metrics=replace(window.strategy_metrics, total_cost=forged_cost),
        excess_attribution=replace(window.excess_attribution, execution_cost=forged_cost),
    )
    result = replace(result, windows=(forged_window, *result.windows[1:]))
    result = bind_experiment(result, ExperimentSpec.from_dict(result.run_manifest["experiment"]))

    summary = json.loads(
        write_validation_artifacts(result, tmp_path / "forged-cost").summary_json.read_text()
    )

    assert summary["decision"]["conclusion"] == "do_not_trade"
    assert "profile_mode_attribution" in summary["decision"]["blockers"]
    assert summary["trend_diagnostics"] is None


def test_optional_trend_report_rejects_cost_config_not_bound_to_execution_manifest(
    tmp_path,
) -> None:
    # Break caught: forged cost config plus matching metrics/attribution can still emit diagnostics.
    from asset_allocation.etf_adaptive.research.instrument_validation import _recorded_performance

    result = _profiled_recorded_result()
    window = result.windows[0]
    forged_cost_config = replace(window.cost_config, slippage_bps=9.0)
    strategy_metrics = _recorded_performance(
        window.strategy_daily_nav, window.strategy_events, forged_cost_config,
    )
    benchmark_metrics = _recorded_performance(
        window.benchmark_daily_nav, window.benchmark_events, forged_cost_config,
    )
    forged_window = replace(
        window,
        cost_config=forged_cost_config,
        strategy_metrics=strategy_metrics,
        benchmark_metrics=benchmark_metrics,
        excess_attribution=build_excess_attribution(
            window.strategy_daily_nav,
            window.benchmark_daily_nav,
            window.strategy_observations,
            window.strategy_events,
            execution_cost=strategy_metrics.total_cost,
        ),
    )
    result = replace(result, windows=(forged_window, *result.windows[1:]))
    result = bind_experiment(result, ExperimentSpec.from_dict(result.run_manifest["experiment"]))

    summary = json.loads(
        write_validation_artifacts(result, tmp_path / "forged-cost-config").summary_json.read_text()
    )

    assert summary["decision"]["conclusion"] == "do_not_trade"
    assert "profile_mode_attribution" in summary["decision"]["blockers"]
    assert summary["trend_diagnostics"] is None


@pytest.mark.parametrize("metric_name, forged_value", (
    ("max_drawdown", -0.75),
    ("cvar5", -0.50),
))
def test_optional_trend_report_rejects_aggregate_risk_not_reconciled_to_nav(
    tmp_path, metric_name, forged_value,
) -> None:
    # Break caught: mutable aggregate MDD/CVaR fields can publish unsupported diagnostic deltas.
    result = _profiled_recorded_result()
    result = replace(
        result,
        strategy_metrics=replace(result.strategy_metrics, **{metric_name: forged_value}),
    )

    summary = json.loads(
        write_validation_artifacts(result, tmp_path / metric_name).summary_json.read_text()
    )

    assert summary["decision"]["conclusion"] == "do_not_trade"
    assert "profile_mode_attribution" in summary["decision"]["blockers"]
    assert summary["trend_diagnostics"] is None


def test_low_optional_trend_activity_is_diagnostic_only(tmp_path) -> None:
    # Break caught: a zero active-session diagnostic can be promoted into an unstated trading gate.
    result = _profiled_recorded_result()
    windows = []
    for window in result.windows:
        observations = tuple(replace(item, regime=Regime.GRID) for item in window.strategy_observations)
        windows.append(replace(
            window,
            strategy_observations=observations,
            excess_attribution=build_excess_attribution(
                window.strategy_daily_nav,
                window.benchmark_daily_nav,
                observations,
                window.strategy_events,
                execution_cost=window.strategy_metrics.total_cost,
            ),
        ))
    result = replace(result, windows=tuple(windows))
    result = bind_experiment(result, ExperimentSpec.from_dict(result.run_manifest["experiment"]))

    summary = json.loads(
        write_validation_artifacts(result, tmp_path / "low-trend").summary_json.read_text()
    )

    assert summary["trend_diagnostics"]["active_sessions"] == 0
    assert summary["decision"]["conclusion"] == "passed"
    assert "profile_mode_attribution" not in summary["decision"]["blockers"]


def test_shortened_non_reference_benchmark_ledger_is_unexecuted_evidence() -> None:
    # Break caught: a benchmark manifest can faithfully describe a ledger that omits the OOS tail.
    from asset_allocation.etf_adaptive.research.instrument_validation import _run_manifest

    result = _profiled_recorded_result()
    window = result.windows[0]
    shortened = replace(
        window.benchmark_runs["fixed_half_hold"],
        nav=window.benchmark_runs["fixed_half_hold"].nav[:-1],
    )
    shortened_window = replace(
        window,
        benchmark_runs={**window.benchmark_runs, "fixed_half_hold": shortened},
    )
    result = replace(result, windows=(shortened_window, *result.windows[1:]))
    execution_manifest = _run_manifest(
        result.target,
        date(2025, 1, 2),
        result.as_of_date,
        object(),
        result.windows[0].market_bars,
        result.windows,
        profile=GRID_PLUS_OPTIONAL_TREND_PROFILE,
    )
    manifest = deepcopy(result.run_manifest)
    manifest["execution_windows"] = execution_manifest["execution_windows"]

    decision = validation_publication_decision(replace(result, run_manifest=manifest))

    assert decision["conclusion"] == "do_not_trade"
    assert "unexecuted_benchmark_evidence" in decision["blockers"]


def test_all_shortened_benchmark_ledgers_remain_unexecuted_against_market_window() -> None:
    # Break caught: peers can agree on a shortened request while omitting recorded OOS market sessions.
    from asset_allocation.etf_adaptive.research.instrument_validation import _run_manifest

    result = _profiled_recorded_result()
    window = result.windows[0]
    shortened_runs = {
        benchmark_id: replace(
            run,
            request=replace(run.request, end_date=run.nav[-2].nav_date),
            nav=run.nav[:-1],
        )
        for benchmark_id, run in window.benchmark_runs.items()
    }
    shortened_window = replace(
        window,
        benchmark_runs=shortened_runs,
        benchmark_daily_nav=shortened_runs["buy_and_hold"].nav,
    )
    result = replace(result, windows=(shortened_window, *result.windows[1:]))
    execution_manifest = _run_manifest(
        result.target,
        date(2025, 1, 2),
        result.as_of_date,
        object(),
        result.windows[0].market_bars,
        result.windows,
        profile=GRID_PLUS_OPTIONAL_TREND_PROFILE,
    )
    manifest = deepcopy(result.run_manifest)
    manifest["execution_windows"] = execution_manifest["execution_windows"]

    decision = validation_publication_decision(replace(result, run_manifest=manifest))

    assert decision["conclusion"] == "do_not_trade"
    assert "unexecuted_benchmark_evidence" in decision["blockers"]


@pytest.mark.parametrize("profile", (GRID_CORE_PROFILE, CORE_HOLD_REBALANCE_PROFILE))
def test_non_optional_profiles_publish_null_trend_diagnostics(tmp_path, profile) -> None:
    result = _profiled_recorded_result(profile)

    summary = json.loads(
        write_validation_artifacts(result, tmp_path / profile.profile_id).summary_json.read_text()
    )

    assert summary["trend_diagnostics"] is None


def test_core_hold_report_keeps_candidate_surface_empty(tmp_path) -> None:
    import csv

    result = _profiled_recorded_result(CORE_HOLD_REBALANCE_PROFILE)
    forged_candidate = _recorded_result().windows[0].candidate_scores[0]
    result = replace(
        result,
        windows=(
            replace(result.windows[0], candidate_scores=(forged_candidate,)),
            *result.windows[1:],
        ),
    )

    artifacts = write_validation_artifacts(result, tmp_path / "core")

    assert list(csv.DictReader(artifacts.candidate_scores_csv.open(encoding="utf-8"))) == []
    summary = json.loads(artifacts.summary_json.read_text())
    assert summary["strategy_profile"]["executable_strategy_id"] is None
    assert summary["decision"]["conclusion"] == "do_not_trade"


@pytest.mark.parametrize("experiment_metadata", ("missing", "conflicting"))
def test_core_candidate_csv_stays_empty_when_experiment_metadata_is_invalid(
    tmp_path, experiment_metadata,
) -> None:
    # Break caught: a broken experiment payload can disable deterministic-core candidate suppression.
    import csv

    result = _profiled_recorded_result(CORE_HOLD_REBALANCE_PROFILE)
    forged_candidate = _recorded_result().windows[0].candidate_scores[0]
    result = replace(
        result,
        windows=(
            replace(result.windows[0], candidate_scores=(forged_candidate,)),
            *result.windows[1:],
        ),
    )
    manifest = deepcopy(result.run_manifest)
    if experiment_metadata == "missing":
        manifest.pop("experiment")
    else:
        grid = _profiled_recorded_result(GRID_CORE_PROFILE)
        manifest["experiment"] = deepcopy(grid.run_manifest["experiment"])

    artifacts = write_validation_artifacts(
        replace(result, run_manifest=manifest), tmp_path / experiment_metadata,
    )
    summary = json.loads(artifacts.summary_json.read_text())

    assert summary["decision"]["conclusion"] == "do_not_trade"
    assert list(csv.DictReader(artifacts.candidate_scores_csv.open(encoding="utf-8"))) == []


def test_core_candidate_csv_uses_execution_window_profile_signal(tmp_path) -> None:
    # Break caught: forged root/window identities can hide a recorded core execution profile.
    import csv

    result = _profiled_recorded_result(CORE_HOLD_REBALANCE_PROFILE)
    grid = _profiled_recorded_result(GRID_CORE_PROFILE)
    forged_candidate = _recorded_result().windows[0].candidate_scores[0]
    windows = tuple(replace(
        window,
        profile_id=GRID_CORE_PROFILE.profile_id,
        candidate_scores=(forged_candidate,) if index == 0 else (),
    ) for index, window in enumerate(result.windows))
    manifest = deepcopy(result.run_manifest)
    manifest["profile_id"] = GRID_CORE_PROFILE.profile_id
    manifest["profile_hash"] = GRID_CORE_PROFILE.profile_hash()
    manifest["experiment"] = deepcopy(grid.run_manifest["experiment"])

    artifacts = write_validation_artifacts(
        replace(result, windows=windows, run_manifest=manifest), tmp_path / "execution-core",
    )
    summary = json.loads(artifacts.summary_json.read_text())

    assert summary["decision"]["conclusion"] == "do_not_trade"
    assert list(csv.DictReader(artifacts.candidate_scores_csv.open(encoding="utf-8"))) == []


def test_validation_artifacts_fail_closed_without_all_profile_benchmarks(tmp_path: Path) -> None:
    manifest = write_validation_artifacts(_recorded_result(), tmp_path / "159915.SZ")

    summary = json.loads(manifest.summary_json.read_text(encoding="utf-8"))
    report = manifest.report_markdown.read_text(encoding="utf-8")

    assert summary["decision"] == {
        "conclusion": "do_not_trade", "blockers": ["unexecuted_benchmark_evidence"],
    }
    assert summary["comparison"] is None
    assert summary["execution"] is None
    assert summary["data_provenance"]["data_cutoff"] == "2026-09-08"
    assert "experiment evidence" in report
    assert manifest.chart_png.exists() and manifest.chart_png.stat().st_size > 1_000
    assert (tmp_path / "159915.SZ" / "charts" / "wf_000.png").exists()
    assert manifest.daily_nav_csv.exists()


def test_optional_trend_profile_cannot_publish_without_all_benchmark_oos_evidence() -> None:
    result = _recorded_result()

    decision = validation_publication_decision(result)

    assert decision["conclusion"] == "do_not_trade"
    assert "unexecuted_benchmark_evidence" in decision["blockers"]


def test_legacy_validation_artifacts_preserve_provenance_but_fail_closed(tmp_path: Path) -> None:
    # Break caught: historical strategy/baseline metadata must not authorize a new formal publication.
    manifest = write_validation_artifacts(_legacy_recorded_result(), tmp_path / "159915.SZ")

    summary = json.loads(manifest.summary_json.read_text(encoding="utf-8"))
    report = manifest.report_markdown.read_text(encoding="utf-8")

    assert summary["decision"] == {
        "conclusion": "do_not_trade", "blockers": ["experiment_metadata"],
    }
    assert summary["comparison"] is None
    assert summary["execution"] is None
    assert summary["data_provenance"]["data_cutoff"] == "2026-09-08"
    assert "风险调整后 ETF 样本外验证决策报告" in report
    assert "experiment evidence" in report
    assert "事件归因" in report
    assert manifest.chart_png.exists() and manifest.chart_png.stat().st_size > 1_000
    assert (tmp_path / "159915.SZ" / "charts" / "wf_000.png").exists()
    assert manifest.daily_nav_csv.exists()


def test_write_validation_artifacts_fails_closed_when_recorded_evidence_is_absent(tmp_path: Path) -> None:
    # Break caught: defaulting missing recorded evidence to zero can fabricate a tradable-looking comparison.
    target = ValidationTarget("test", "159915.SZ", SubLayer.DOMESTIC_GROWTH)
    result = InstrumentValidationResult(
        target=target, status=ValidationStatus.DATA_REJECTED, as_of_date=date(2026, 9, 8),
        rejection_reason="insufficient history", scope=ValidationScope.FORMAL,
    )

    manifest = write_validation_artifacts(result, tmp_path / "159915.SZ")
    summary = json.loads(manifest.summary_json.read_text(encoding="utf-8"))

    assert summary["comparison"] is None
    assert summary["decision"]["conclusion"] == "do_not_trade"
    assert "insufficient history" in summary["decision"]["blockers"]
    assert summary["execution"] is None
    assert "0.0" not in manifest.summary_json.read_text(encoding="utf-8")


def test_write_validation_artifacts_marks_missing_recorded_exposure_as_a_blocker(tmp_path: Path) -> None:
    # Break caught: a missing exposure series must not leave a passed decision alongside a null execution block.
    result = replace(_recorded_result(), strategy_invested_sessions=0, strategy_cash_sessions=0)

    manifest = write_validation_artifacts(result, tmp_path / "159915.SZ")
    summary = json.loads(manifest.summary_json.read_text(encoding="utf-8"))

    assert summary["decision"]["conclusion"] == "do_not_trade"
    assert "strategy_exposure" in summary["decision"]["blockers"]
    assert summary["execution"] is None


def test_write_validation_artifacts_marks_inconsistent_oos_window_evidence_as_invalid(tmp_path: Path) -> None:
    # Break caught: a decision cannot rely on an OOS count that disagrees with its recorded windows.
    result = _recorded_result()
    result = replace(result, evidence=replace(result.evidence, oos_window_count=2))

    manifest = write_validation_artifacts(result, tmp_path / "159915.SZ")
    summary = json.loads(manifest.summary_json.read_text(encoding="utf-8"))

    assert summary["decision"]["conclusion"] == "do_not_trade"
    assert "oos_window_count" in summary["decision"]["blockers"]
    assert summary["comparison"] is None


def test_report_without_reproducibility_evidence_cannot_approve(tmp_path: Path) -> None:
    result = replace(_recorded_result(), run_manifest=None)
    manifest = write_validation_artifacts(result, tmp_path / "missing-provenance")
    summary = json.loads(manifest.summary_json.read_text(encoding="utf-8"))
    assert summary["decision"]["conclusion"] == "do_not_trade"
    assert summary["activation_eligible"] is False
    assert "run_manifest" in summary["decision"]["blockers"]


def test_report_exports_candidate_scores_and_reconciled_attribution(tmp_path):
    manifest = write_validation_artifacts(_recorded_result(), tmp_path / "report")
    assert manifest.candidate_scores_csv.exists()
    assert manifest.excess_attribution_json.exists()
    assert manifest.daily_state_csv.exists()
    import csv
    scores = list(csv.DictReader(manifest.candidate_scores_csv.open(encoding="utf-8")))
    assert len(scores) == 3
    assert json.loads(scores[0]["config"])["cost"]["slippage_bps"] == 3.0
    assert {row["family"] for row in scores} == {"grid_only"}
    attribution = json.loads(manifest.excess_attribution_json.read_text(encoding="utf-8"))
    assert len(attribution) == 3
    assert attribution[0]["reconciliation_error"] == pytest.approx(0.0)
    report = manifest.report_markdown.read_text(encoding="utf-8")
    assert "experiment evidence" in report
    states = list(csv.DictReader(manifest.daily_state_csv.open(encoding="utf-8")))
    assert len(states) == 9
    assert states[0]["actual_exposure"] == "0.0"
    persisted = json.loads(manifest.summary_json.read_text(encoding="utf-8"))["data_provenance"]["run_manifest"]
    assert persisted["experiment_hash"] == _recorded_result().run_manifest["experiment_hash"]
    assert persisted["experiment_windows"][0]["selected_scores"]["grid_only"]["config"] == json.loads(scores[0]["config"])


@pytest.mark.parametrize("missing", ["experiment_hash", "strategy_spec", "benchmark_specs", "experiment_windows"])
def test_report_rejects_missing_experiment_fields(tmp_path, monkeypatch, missing):
    monkeypatch.setattr("asset_allocation.etf_adaptive.research.validation_report._plot", lambda *args: None)
    result = _recorded_result()
    metadata = dict(result.run_manifest)
    metadata.pop(missing)
    manifest = write_validation_artifacts(replace(result, run_manifest=metadata), tmp_path / "report")
    summary = json.loads(manifest.summary_json.read_text(encoding="utf-8"))
    assert summary["decision"]["conclusion"] == "do_not_trade"
    assert summary["activation_eligible"] is False


@pytest.mark.parametrize("missing", ["candidate_scores", "selected_scores", "strategy_observations", "excess_attribution"])
def test_report_rejects_missing_window_diagnostics(tmp_path, monkeypatch, missing):
    monkeypatch.setattr("asset_allocation.etf_adaptive.research.validation_report._plot", lambda *args: None)
    result = _recorded_result()
    window = replace(result.windows[0], **{missing: None if missing in {"selected_scores", "excess_attribution"} else ()})
    manifest = write_validation_artifacts(replace(result, windows=(window, *result.windows[1:])), tmp_path / "report")
    summary = json.loads(manifest.summary_json.read_text(encoding="utf-8"))
    assert summary["decision"]["conclusion"] == "do_not_trade"
    assert summary["activation_eligible"] is False


def test_diagnostic_write_failure_preserves_previous_published_report(tmp_path, monkeypatch):
    import asset_allocation.etf_adaptive.research.validation_report as module
    destination = tmp_path / "report"
    destination.mkdir()
    (destination / "summary.json").write_text("previous", encoding="utf-8")
    original = module._write_csv
    def fail_diagnostics(path, rows, fields):
        if path.name == "daily_state.csv":
            raise OSError("diagnostic write failed")
        return original(path, rows, fields)
    monkeypatch.setattr(module, "_write_csv", fail_diagnostics)
    with pytest.raises(OSError, match="diagnostic write failed"):
        write_validation_artifacts(_recorded_result(), destination)
    assert (destination / "summary.json").read_text(encoding="utf-8") == "previous"


def test_formal_report_without_experiment_metadata_is_do_not_trade(tmp_path):
    result = _recorded_result()
    metadata = dict(result.run_manifest)
    metadata.pop("experiment", None)
    result = replace(result, run_manifest=metadata)
    manifest = write_validation_artifacts(result, tmp_path / "report")
    summary = json.loads(manifest.summary_json.read_text(encoding="utf-8"))
    assert summary["decision"]["conclusion"] == "do_not_trade"
    assert "experiment_metadata" in summary["decision"]["blockers"]
    assert summary["activation_eligible"] is False


@pytest.mark.parametrize("forgery", ["version", "profile_hash", "unexpected_field"])
def test_current_profile_forgery_is_rejected_and_cannot_publish(
    tmp_path, monkeypatch, forgery,
):
    monkeypatch.setattr("asset_allocation.etf_adaptive.research.validation_report._plot", lambda *args: None)
    result = _recorded_result()
    experiment_payload = deepcopy(result.run_manifest["experiment"])
    if forgery == "version":
        experiment_payload["profile"]["version"] = "forged"
    elif forgery == "profile_hash":
        experiment_payload["profile_hash"] = "forged"
    else:
        experiment_payload["profile"]["unexpected"] = True

    with pytest.raises(ValueError):
        ExperimentSpec.from_dict(experiment_payload)

    metadata = dict(result.run_manifest)
    metadata["experiment"] = experiment_payload
    manifest = write_validation_artifacts(
        replace(result, run_manifest=metadata), tmp_path / forgery,
    )
    summary = json.loads(manifest.summary_json.read_text(encoding="utf-8"))
    assert summary["decision"]["conclusion"] == "do_not_trade"
    assert "experiment_metadata" in summary["decision"]["blockers"]
    assert summary["activation_eligible"] is False


def test_legacy_experiment_manifest_deserializes_but_cannot_publish_formally(tmp_path):
    result = _legacy_recorded_result()
    legacy_payload = result.run_manifest["experiment"]

    spec = ExperimentSpec.from_dict(legacy_payload)
    manifest = write_validation_artifacts(result, tmp_path / "report")
    summary = json.loads(manifest.summary_json.read_text(encoding="utf-8"))

    assert spec.profile.profile_id == "legacy_unprofiled"
    assert summary["decision"]["conclusion"] == "do_not_trade"
    assert "experiment_metadata" in summary["decision"]["blockers"]
    assert summary["activation_eligible"] is False


@pytest.mark.parametrize("change", ["window_hash", "attribution", "target", "selected_config"])
def test_report_rejects_inconsistent_recorded_provenance(tmp_path, monkeypatch, change):
    monkeypatch.setattr("asset_allocation.etf_adaptive.research.validation_report._plot", lambda *args: None)
    result = _recorded_result()
    spec = ExperimentSpec.from_dict(result.run_manifest["experiment"])
    if change == "window_hash":
        result = replace(result, windows=(replace(result.windows[0], config_hash="forged"), *result.windows[1:]))
    elif change == "attribution":
        attribution = replace(result.windows[0].excess_attribution, trend_return=0.9)
        result = replace(result, windows=(replace(result.windows[0], excess_attribution=attribution), *result.windows[1:]))
    elif change == "target":
        result.run_manifest["target"]["stock_code"] = "513330.SH"
    elif change == "selected_config":
        result.run_manifest["selected_configs"][0]["config_hash"] = "forged"
    result = bind_experiment(result, spec)
    manifest = write_validation_artifacts(result, tmp_path / "report")
    summary = json.loads(manifest.summary_json.read_text(encoding="utf-8"))
    assert summary["decision"]["conclusion"] == "do_not_trade"
    assert summary["activation_eligible"] is False


def test_experiment_allows_provider_to_advance_to_first_aligned_session(tmp_path, monkeypatch):
    monkeypatch.setattr("asset_allocation.etf_adaptive.research.validation_report._plot", lambda *args: None)
    result = _recorded_result()
    spec = replace(ExperimentSpec.from_dict(result.run_manifest["experiment"]), start_date=date(2025, 1, 1))
    result = bind_experiment(result, spec)
    manifest = write_validation_artifacts(result, tmp_path / "report")
    summary = json.loads(manifest.summary_json.read_text(encoding="utf-8"))
    assert summary["decision"]["conclusion"] == "do_not_trade"
    assert "unexecuted_benchmark_evidence" in summary["decision"]["blockers"]


@pytest.mark.parametrize("change", [
    "window_cost", "candidate_cost", "recorded_cost", "missing_cost",
    "unapproved_cooldown", "undeclared_cooldown", "undeclared_field",
    "empty_score_axes", "missing_window_axes", "empty_window_axes",
    "missing_manifest_axes", "wrong_family_axes", "empty_allowed_axes",
])
def test_formal_gate_rejects_rebound_cost_and_axis_bypasses(change):
    # Rebinding hashes must not turn altered execution settings into approved evidence.
    result = _recorded_result()
    baseline = validation_publication_decision(result)
    assert baseline == {
        "conclusion": "do_not_trade", "blockers": ["unexecuted_benchmark_evidence"],
    }
    spec = ExperimentSpec.from_dict(result.run_manifest["experiment"])
    window = result.windows[0]
    config = AdaptiveConfig.default()
    if change in {"window_cost", "candidate_cost"}:
        config = replace(config, cost=replace(config.cost, slippage_bps=9.0))
    elif change in {"unapproved_cooldown", "undeclared_cooldown"}:
        config = replace(config, grid=replace(config.grid, cooldown_sessions=99 if change == "unapproved_cooldown" else 10))
        if change == "undeclared_cooldown":
            spec = replace(spec, allowed_axes={"step_pct": (0.02,)})
    elif change == "undeclared_field":
        config = replace(config, grid=replace(config.grid, initial_model="atr"))
    if config != AdaptiveConfig.default():
        scores = tuple(replace(score, config=asdict(config), config_hash=config.config_hash())
                       for score in window.candidate_scores)
        if change == "candidate_cost":
            window = replace(window, candidate_scores=(*window.candidate_scores, scores[0]))
        else:
            window = replace(window, selected_config=asdict(config), config_hash=config.config_hash(),
                             candidate_scores=scores, selected_scores={score.family: score for score in scores})
    elif change in {"recorded_cost", "missing_cost"}:
        window = replace(window, cost_config=None if change == "missing_cost" else replace(config.cost, slippage_bps=9.0))
    elif change in {"empty_score_axes", "wrong_family_axes", "empty_allowed_axes"}:
        scores = tuple(replace(score, screened_axes=("stop_n",) if change == "wrong_family_axes" else ())
                       for score in window.candidate_scores)
        window = replace(window, candidate_scores=scores, selected_scores={score.family: score for score in scores})
        if change == "empty_allowed_axes":
            spec = replace(spec, allowed_axes={})
    elif change in {"missing_window_axes", "empty_window_axes"}:
        window = replace(window, screened_axes=None if change == "missing_window_axes" else {})
    elif change == "missing_manifest_axes":
        result.run_manifest["screened_axes"] = {}
    result = replace(result, windows=(window, *result.windows[1:]))
    result.run_manifest["selected_configs"] = [
        {"window_id": item.window_id, "config_hash": item.config_hash, "config": item.selected_config}
        for item in result.windows
    ]
    result = bind_experiment(result, spec)
    decision = validation_publication_decision(result)
    assert decision["conclusion"] == "do_not_trade"
    assert "experiment_metadata" in decision["blockers"]


def test_formal_gate_binds_candidate_deviations_to_its_own_screened_axes():
    # Break caught: an axis declared by a different screening stage cannot approve
    # an undeclared deviation in this candidate after its evidence is rebound.
    result = _recorded_result()
    baseline = validation_publication_decision(result)
    assert baseline == {
        "conclusion": "do_not_trade", "blockers": ["unexecuted_benchmark_evidence"],
    }
    spec = ExperimentSpec.from_dict(result.run_manifest["experiment"])
    default = AdaptiveConfig.default()
    altered = replace(default, grid=replace(default.grid, unit_pct=0.15))
    windows = []
    for index, existing in enumerate(result.windows):
        config = altered if index == 0 else default
        grid_score = existing.candidate_scores[0]
        candidate_with_hidden_deviation = replace(
            grid_score, config=asdict(config), config_hash=config.config_hash(), screened_axes=("step_pct",),
        )
        unit_screened_candidate = replace(
            grid_score, config=asdict(config), config_hash=config.config_hash(), screened_axes=("unit_pct",),
        )
        windows.append(replace(
            existing,
            selected_config=asdict(config), config_hash=config.config_hash(),
            screened_axes={"grid_only": (("step_pct",), ("unit_pct",))},
            candidate_scores=(candidate_with_hidden_deviation, unit_screened_candidate),
            selected_scores={"grid_only": candidate_with_hidden_deviation},
        ))
    result = replace(result, windows=tuple(windows))
    result.run_manifest["screened_axes"] = {"grid": ["step_pct", "unit_pct"]}
    result.run_manifest["selected_configs"] = [
        {"window_id": item.window_id, "config_hash": item.config_hash, "config": item.selected_config}
        for item in result.windows
    ]

    rebound = bind_experiment(result, spec)

    decision = validation_publication_decision(rebound)
    assert decision["conclusion"] == "do_not_trade"
    assert "experiment_metadata" in decision["blockers"]


def test_final_rename_failure_preserves_complete_previous_report(tmp_path, monkeypatch):
    import os
    import asset_allocation.etf_adaptive.research.validation_report as module
    destination = tmp_path / "report"
    destination.mkdir()
    for name in ("summary.json", "candidate_scores.csv", "daily_state.csv", "report.md"):
        (destination / name).write_text("previous " + name, encoding="utf-8")
    original = os.replace
    def fail_publication(source, target):
        if Path(target) == destination and str(source).endswith(".staging"):
            raise OSError("final rename failed")
        return original(source, target)
    monkeypatch.setattr(os, "replace", fail_publication)
    monkeypatch.setattr(module, "_plot", lambda *args: None)
    with pytest.raises(OSError, match="final rename failed"):
        write_validation_artifacts(_recorded_result(), destination)
    for name in ("summary.json", "candidate_scores.csv", "daily_state.csv", "report.md"):
        assert (destination / name).read_text(encoding="utf-8") == "previous " + name

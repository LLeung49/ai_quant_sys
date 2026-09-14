import json
from dataclasses import asdict, replace
from datetime import date
from decimal import Decimal
from pathlib import Path

import pytest

from asset_allocation.etf_adaptive.contracts import DualPriceBar, SubLayer
from asset_allocation.etf_adaptive.config import AdaptiveConfig
from asset_allocation.etf_adaptive.research.attribution import build_excess_attribution
from asset_allocation.etf_adaptive.research.candidate_scoring import TrainingCandidateScore
from asset_allocation.etf_adaptive.research.experiment import ExperimentSpec, bind_experiment, APPROVED_EXPERIMENT_AXES
from asset_allocation.etf_adaptive.research.strategy_specs import FULL_ADAPTIVE_SPEC, BUY_AND_HOLD_SPEC
from asset_allocation.etf_adaptive.research.decision import DecisionSummary, ResearchConclusion, ResearchEvidence
from asset_allocation.etf_adaptive.research.instrument_validation import (
    InstrumentValidationResult, TrainingSurfaceSummary, ValidationScope,
    ValidationStatus, ValidationTarget, ValidationWindowResult,
)
from asset_allocation.etf_adaptive.research.metrics import PerformanceMetrics
from asset_allocation.etf_adaptive.research.validation_report import write_validation_artifacts
from asset_allocation.etf_adaptive.state import BacktestEvent, DailyNav, DailyStrategyObservation, Regime


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
    scores = tuple(TrainingCandidateScore(config.config_hash(), asdict(config),
                   1.0, 0.3, 0.2, 0.04, 0.01, 0.01, 0.7, True, None,
                   family=family, screened_axes=axes)
                   for family, axes in (("grid_only", ("step_pct",)), ("trend_only", ("stop_n",))))
    window = replace(window, config_hash=config.config_hash(), selected_config=asdict(config),
                     cost_config=config.cost,
                     screened_axes={"grid_only": (("step_pct",),), "trend_only": (("stop_n",),)},
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
            "screened_axes": {"grid": ["step_pct"], "trend": ["stop_n"]},
        },
    )
    spec = ExperimentSpec("recorded-test", ("159915.SZ",), FULL_ADAPTIVE_SPEC,
                          (BUY_AND_HOLD_SPEC,), APPROVED_EXPERIMENT_AXES,
                          date(2025, 1, 2), result.as_of_date)
    return bind_experiment(result, spec)


def test_write_validation_artifacts_publishes_recorded_risk_adjusted_decision_report(tmp_path: Path) -> None:
    # Break caught: omitting persisted decision/Sortino/exposure evidence makes a report look actionable without support.
    manifest = write_validation_artifacts(_recorded_result(), tmp_path / "159915.SZ")

    summary = json.loads(manifest.summary_json.read_text(encoding="utf-8"))
    report = manifest.report_markdown.read_text(encoding="utf-8")

    assert summary["decision"] == {"conclusion": "passed", "blockers": []}
    assert summary["comparison"]["strategy"]["sortino"] == 0.70
    assert summary["comparison"]["differences"]["sortino"] == pytest.approx(0.30)
    assert summary["execution"]["strategy"]["exposure_ratio"] == 2 / 3
    assert summary["data_provenance"]["data_cutoff"] == "2026-09-08"
    assert "风险调整后 ETF 样本外验证决策报告" in report
    assert "Sortino" in report
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
    assert len(scores) == 6
    assert json.loads(scores[0]["config"])["cost"]["slippage_bps"] == 3.0
    assert {row["family"] for row in scores} == {"grid_only", "trend_only"}
    attribution = json.loads(manifest.excess_attribution_json.read_text(encoding="utf-8"))
    assert len(attribution) == 3
    assert attribution[0]["reconciliation_error"] == pytest.approx(0.0)
    report = manifest.report_markdown.read_text(encoding="utf-8")
    assert "Largest absolute contributor: trend_return" in report
    assert "trend entry/exit" in report
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


@pytest.mark.parametrize("change", ["window_hash", "attribution", "target", "selected_config", "unrun_policy", "unrun_benchmark", "undeclared_cost"])
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
    elif change == "unrun_policy":
        from asset_allocation.etf_adaptive.research.strategy_specs import GRID_ONLY_SPEC
        spec = replace(spec, strategy=GRID_ONLY_SPEC)
    elif change == "unrun_benchmark":
        from asset_allocation.etf_adaptive.research.strategy_specs import FIXED_HALF_SPEC
        spec = replace(spec, benchmarks=(FIXED_HALF_SPEC,))
    elif change == "undeclared_cost":
        config = replace(spec.strategy.config, cost=replace(spec.strategy.config.cost, slippage_bps=9.0))
        spec = replace(spec, strategy=replace(spec.strategy, config=config))
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
    assert summary["decision"]["conclusion"] == "passed"


@pytest.mark.parametrize("change", [
    "window_cost", "candidate_cost", "recorded_cost", "missing_cost",
    "unapproved_cooldown", "undeclared_cooldown", "undeclared_field",
    "empty_score_axes", "missing_window_axes", "empty_window_axes",
    "missing_manifest_axes", "wrong_family_axes", "empty_allowed_axes",
])
def test_formal_gate_rejects_rebound_cost_and_axis_bypasses(change):
    # Rebinding hashes must not turn altered execution settings into approved evidence.
    from asset_allocation.etf_adaptive.research.validation_report import validation_publication_decision
    result = _recorded_result()
    spec = ExperimentSpec.from_dict(result.run_manifest["experiment"])
    window = result.windows[0]
    config = AdaptiveConfig.default()
    if change in {"window_cost", "candidate_cost"}:
        config = replace(config, cost=replace(config.cost, slippage_bps=9.0))
    elif change in {"unapproved_cooldown", "undeclared_cooldown"}:
        config = replace(config, grid=replace(config.grid, cooldown_sessions=99 if change == "unapproved_cooldown" else 10))
        if change == "undeclared_cooldown":
            spec = replace(spec, allowed_axes={"step_pct": (0.02,), "stop_n": (2.0,)})
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
    assert decision["blockers"]


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

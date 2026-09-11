import json
from dataclasses import replace
from datetime import date
from decimal import Decimal
from pathlib import Path

import pytest

from asset_allocation.etf_adaptive.contracts import DualPriceBar, SubLayer
from asset_allocation.etf_adaptive.research.decision import DecisionSummary, ResearchConclusion, ResearchEvidence
from asset_allocation.etf_adaptive.research.instrument_validation import (
    InstrumentValidationResult, TrainingSurfaceSummary, ValidationScope,
    ValidationStatus, ValidationTarget, ValidationWindowResult,
)
from asset_allocation.etf_adaptive.research.metrics import PerformanceMetrics
from asset_allocation.etf_adaptive.research.validation_report import write_validation_artifacts
from asset_allocation.etf_adaptive.state import BacktestEvent, DailyNav


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
    return InstrumentValidationResult(
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

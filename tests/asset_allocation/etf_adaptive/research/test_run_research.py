"""CLI entry point: argument parsing and provider dispatch."""

from __future__ import annotations

import json
import math
import shutil
import uuid
from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from pathlib import Path

import pytest

from asset_allocation.etf_adaptive.research.run_research import (
    ResearchArtifact,
    ResearchRunConfig,
    build_parser,
    run_research,
    _explicit_evidence,
    _validated_layer_benchmarks,
)
from asset_allocation.etf_adaptive.contracts import (
    DualPriceBar,
    ExecutionAvailability,
    InstrumentType,
    LayeredInstrument,
    SubLayer,
    SubLayerBudget,
)
from asset_allocation.etf_adaptive.frozen_selection import FrozenSelection
from asset_allocation.etf_adaptive.research.selection import CandidateMetrics, ProductMetrics, SubLayerSelectionEvidence


REPORTS_ROOT = Path("D:/aiQuant/ai_quant_sys/reports/pytest-run-research-tmp")


@pytest.fixture
def reports_dir() -> Path:
    REPORTS_ROOT.mkdir(parents=True, exist_ok=True)
    target = REPORTS_ROOT / f"run-{uuid.uuid4().hex}"
    target.mkdir(parents=True, exist_ok=True)
    try:
        yield target
    finally:
        shutil.rmtree(target, ignore_errors=True)


def _artifact_factory(config: ResearchRunConfig) -> ResearchArtifact:
    return ResearchArtifact(
        attempted_config_count=3,
        failed_config_count=1,
        data_cutoff=config.as_of_date.isoformat(),
        config_hash="abc123",
        artifacts={"executive_report": "# 测试\n"},
    )


def test_build_parser_requires_as_of_date_and_output_dir() -> None:
    parser = build_parser()
    args = parser.parse_args(["--as-of-date", "2026-09-01", "--output-dir", "reports/run"])

    assert args.as_of_date == "2026-09-01"
    assert args.output_dir == "reports/run"


def test_run_research_publishes_manifest_and_files(reports_dir: Path) -> None:
    config = ResearchRunConfig(
        as_of_date=date(2026, 9, 1),
        output_dir=reports_dir / "out",
        initial_cash=Decimal("250000"),
    )

    run_research(config, provider=None, artifact_factory=_artifact_factory)

    manifest = json.loads((reports_dir / "out" / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["data_cutoff"] == "2026-09-01"
    assert manifest["attempted_config_count"] == 3
    assert manifest["failed_config_count"] == 1
    assert manifest["config_hash"] == "abc123"
    assert (reports_dir / "out" / "executive_report.md").exists()


def test_run_research_propagates_as_of_date_into_executive_report(reports_dir: Path) -> None:
    config = ResearchRunConfig(
        as_of_date=date(2026, 9, 1),
        output_dir=reports_dir / "out",
    )

    def _factory(config: ResearchRunConfig) -> ResearchArtifact:
        return ResearchArtifact(
            attempted_config_count=1,
            failed_config_count=0,
            data_cutoff=config.as_of_date.isoformat(),
            config_hash="hash",
            artifacts={
                "executive_report": f"# run\n\n as-of {config.as_of_date.isoformat()}\n",
            },
        )

    run_research(config, provider=None, artifact_factory=_factory)

    report = (reports_dir / "out" / "executive_report.md").read_text(encoding="utf-8")
    assert "as-of 2026-09-01" in report


def test_run_research_raises_when_no_provider_or_factory() -> None:
    config = ResearchRunConfig(
        as_of_date=date(2026, 9, 1),
        output_dir=Path("."),
    )

    with pytest.raises(NotImplementedError):
        run_research(config)


def test_research_freeze_requires_two_complete_passing_layer_benchmarks() -> None:
    assert _validated_layer_benchmarks({
        "defensive": {"passed": True},
        "broad_beta": {"passed": True},
    }) == {
        "defensive": {"passed": True},
        "broad_beta": {"passed": True},
    }
    assert _validated_layer_benchmarks({
        "defensive": {"passed": False},
        "broad_beta": {"passed": True},
    }) is None
    assert _validated_layer_benchmarks({"defensive": {"passed": True}}) is None
    assert _validated_layer_benchmarks(None) is None


def test_run_research_freezes_only_evidence_supported_layered_targets(
    reports_dir: Path,
) -> None:
    """A missing OOS pass or a rejected layer must never enter the freeze."""

    as_of = date(2026, 9, 1)

    class LayeredProvider:
        def load_instruments(self, requested_as_of: date):
            assert requested_as_of == as_of
            return (
                LayeredInstrument(
                    stock_code="513500.SH", as_of_date=as_of,
                    instrument_type=InstrumentType.ETF, style="broad",
                    exposure="nasdaq_or_sp500", is_qdii=True,
                ),
                LayeredInstrument(
                    stock_code="510300.SH", as_of_date=as_of,
                    instrument_type=InstrumentType.ETF, style="broad",
                    exposure="domestic_core", is_qdii=False,
                ),
            )

        def load_bars(self, stock_code: str, start_date: date, end_date: date):
            assert end_date == as_of
            if stock_code == "513500.SH":
                return (
                    _research_bar(stock_code, date(2026, 8, 30), 1.0),
                    _research_bar(stock_code, date(2026, 8, 31), 0.9),
                    _research_bar(stock_code, as_of, 1.1),
                )
            return (
                _research_bar(stock_code, date(2026, 8, 31), 1.0),
                _research_bar(stock_code, as_of, 0.9),
            )

        def load_research_evidence(self, requested_as_of: date, stock_code: str):
            if stock_code == "510300.SH":
                return None
            return {
                "product": ProductMetrics(
                    product_id=stock_code, tracking_index_code="NDX",
                    history_confidence=0.9, average_amount=20_000_000.0,
                    data_quality_score=0.98, cost_sensitivity=0.02,
                    oos_evidence=0.1, sub_layer=SubLayer.OVERSEAS_MATURE,
                ),
                "candidate": CandidateMetrics(stock_code, 0.1, 0.1, 0.5, 0.02),
                "oos_returns": (-0.1, 0.2222222222),
            }

        def load_selection_evidence(self, requested_as_of: date, sub_layer: SubLayer, budget: SubLayerBudget):
            return SubLayerSelectionEvidence(
                budget=budget, pareto_product_ids=frozenset(), maximum_cost_sensitivity=0.05,
                minimum_tradable_budget=Decimal("1000"), per_product_cap=1.0,
                minimum_diversification_gain=0.3,
            )

    config = ResearchRunConfig(
        as_of_date=as_of,
        output_dir=reports_dir / "layered-out",
        extra={
            "sub_layer_budgets": {"broad_overseas_mature": "48000", "broad_domestic_core": "12000"},
            "layer_benchmarks": {
                "defensive": {"passed": True},
                "broad_beta": {"passed": True},
            },
        },
    )

    run_research(config, provider=LayeredProvider())

    manifest = json.loads((config.output_dir / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["sub_layers"]["broad_overseas_mature"]["budget"] == "48000"
    assert set(manifest["sub_layers"]) == {"broad_overseas_mature"}
    assert manifest["frozen_selection"]["targets"] == [{
        "stock_code": "513500.SH",
        "tracking_index_code": "NDX",
        "layer": "broad_beta",
        "sub_layer": "broad_overseas_mature",
        "sub_layer_budget": "48000",
        "instrument_type": "etf",
        "weight": "1",
        "config_hash": manifest["config_hash"],
    }]
    assert (config.output_dir / "sub_layers" / "broad_overseas_mature" / "oos.json").exists()
    oos = json.loads((config.output_dir / "sub_layers" / "broad_overseas_mature" / "oos.json").read_text(encoding="utf-8"))
    pareto = json.loads((config.output_dir / "sub_layers" / "broad_overseas_mature" / "pareto.json").read_text(encoding="utf-8"))
    portfolio = json.loads((config.output_dir / "sub_layers" / "broad_overseas_mature" / "portfolio.json").read_text(encoding="utf-8"))
    assert oos == [{"annual_return": pytest.approx(0.1), "max_drawdown_abs": pytest.approx(0.1), "positive_window_share": pytest.approx(0.5), "stock_code": "513500.SH"}]
    assert pareto == ["513500.SH"]
    assert portfolio["equal_weight"]["weights"] == {"513500.SH": pytest.approx(1.0)}
    selection = FrozenSelection.from_research_manifest(config.output_dir / "manifest.json")
    assert selection.targets[0].config_hash == selection.config_hash


def test_run_research_rejects_positive_two_price_candidate_without_return_evidence(
    reports_dir: Path,
) -> None:
    """A two-price gain is not a stitched-OOS return series or a portfolio."""

    as_of = date(2026, 9, 1)

    class LayeredProvider:
        def load_instruments(self, requested_as_of: date):
            return (
                LayeredInstrument(
                    stock_code="513500.SH", as_of_date=requested_as_of,
                    instrument_type=InstrumentType.ETF, style="broad",
                    exposure="nasdaq_or_sp500", is_qdii=True,
                ),
            )

        def load_bars(self, stock_code: str, start_date: date, end_date: date):
            return (
                _research_bar(stock_code, date(2026, 8, 31), 1.0),
                _research_bar(stock_code, as_of, 1.2),
            )

    config = ResearchRunConfig(
        as_of_date=as_of,
        output_dir=reports_dir / "insufficient-oos",
        extra={"sub_layer_budgets": {"broad_overseas_mature": "48000"}},
    )

    run_research(config, provider=LayeredProvider())

    manifest = json.loads((config.output_dir / "manifest.json").read_text(encoding="utf-8"))
    audit = json.loads((config.output_dir / "universe_audit.json").read_text(encoding="utf-8"))
    assert "sub_layers" not in manifest
    assert manifest["frozen_selection"]["targets"] == []
    assert audit["rows"] == [{
        "accepted": False,
            "reason": "missing_walk_forward_evidence",
        "stock_code": "513500.SH",
        "sub_layer": "broad_overseas_mature",
    }]


def test_run_research_rejects_price_only_provider_without_walk_forward_evidence(reports_dir: Path) -> None:
    """Prices alone cannot manufacture cost-adjusted OOS selection evidence."""

    as_of = date(2026, 9, 1)

    class PriceOnlyProvider:
        def load_instruments(self, requested_as_of: date):
            return (LayeredInstrument(
                stock_code="513500.SH", as_of_date=requested_as_of,
                instrument_type=InstrumentType.ETF, style="broad",
                exposure="nasdaq_or_sp500", is_qdii=True,
            ),)

        def load_bars(self, stock_code: str, start_date: date, end_date: date):
            return (
                _research_bar(stock_code, date(2026, 8, 30), 1.0),
                _research_bar(stock_code, date(2026, 8, 31), 0.9),
                _research_bar(stock_code, as_of, 1.1),
            )

    config = ResearchRunConfig(
        as_of_date=as_of, output_dir=reports_dir / "price-only",
        extra={"sub_layer_budgets": {"broad_overseas_mature": "48000"}},
    )
    run_research(config, provider=PriceOnlyProvider())

    manifest = json.loads((config.output_dir / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["frozen_selection"]["targets"] == []


def test_run_research_rejects_walk_forward_product_without_selection_policy(reports_dir: Path) -> None:
    as_of = date(2026, 9, 1)

    class EvidenceOnlyProvider:
        def load_instruments(self, requested_as_of: date):
            return (LayeredInstrument("513500.SH", requested_as_of, InstrumentType.ETF, "broad", "nasdaq_or_sp500", True),)

        def load_research_evidence(self, requested_as_of: date, stock_code: str):
            return {
                "product": ProductMetrics(stock_code, "NDX", 0.9, 20_000_000.0, 0.98, 0.02, 0.1, SubLayer.OVERSEAS_MATURE),
                "candidate": CandidateMetrics(stock_code, 0.1, 0.1, 0.5, 0.02),
                "oos_returns": (-0.1, 0.2222222222),
            }

    config = ResearchRunConfig(as_of, reports_dir / "no-policy", extra={"sub_layer_budgets": {"broad_overseas_mature": "48000"}})
    run_research(config, provider=EvidenceOnlyProvider())
    manifest = json.loads((config.output_dir / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["frozen_selection"]["targets"] == []


@pytest.mark.parametrize("bad_return", (True, math.nan, math.inf, -math.inf))
def test_explicit_evidence_rejects_non_finite_or_boolean_oos_returns(bad_return: float) -> None:
    as_of = date(2026, 9, 1)
    instrument = LayeredInstrument("513500.SH", as_of, InstrumentType.ETF, "broad", "nasdaq_or_sp500", True)
    raw = {
        "product": ProductMetrics("513500.SH", "NDX", 0.9, 20_000_000.0, 0.98, 0.02, 0.1, SubLayer.OVERSEAS_MATURE),
        "candidate": CandidateMetrics("513500.SH", 0.1, 0.1, 0.5, 0.02),
        "oos_returns": (0.01, bad_return),
    }

    with pytest.raises(ValueError, match="invalid_walk_forward_evidence"):
        _explicit_evidence(raw, instrument, SubLayer.OVERSEAS_MATURE)


def _research_bar(stock_code: str, trade_date: date, close: float) -> DualPriceBar:
    return DualPriceBar(
        stock_code=stock_code, trade_date=trade_date,
        signal_open=close, signal_high=close, signal_low=close, signal_close=close,
        raw_open=close, raw_high=close, raw_low=close, raw_close=close,
        amount=20_000_000.0, suspended=False, adjustment_ratio=1.0,
        execution_availability=ExecutionAvailability(False, False, "test"),
    )

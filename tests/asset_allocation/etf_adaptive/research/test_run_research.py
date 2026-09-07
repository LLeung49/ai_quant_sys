"""CLI entry point: argument parsing and provider dispatch."""

from __future__ import annotations

import json
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
)
from asset_allocation.etf_adaptive.contracts import (
    DualPriceBar,
    ExecutionAvailability,
    InstrumentType,
    LayeredInstrument,
)


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
            close = 1.1 if stock_code == "513500.SH" else 0.9
            return (
                _research_bar(stock_code, date(2026, 8, 31), 1.0),
                _research_bar(stock_code, as_of, close),
            )

    config = ResearchRunConfig(
        as_of_date=as_of,
        output_dir=reports_dir / "layered-out",
        extra={"sub_layer_budgets": {"broad_overseas_mature": "48000", "broad_domestic_core": "12000"}},
    )

    run_research(config, provider=LayeredProvider())

    manifest = json.loads((config.output_dir / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["sub_layers"]["broad_overseas_mature"]["budget"] == "48000"
    assert set(manifest["sub_layers"]) == {"broad_overseas_mature"}
    assert manifest["frozen_selection"]["targets"] == [{
        "stock_code": "513500.SH",
        "tracking_index_code": "513500.SH",
        "layer": "broad_beta",
        "sub_layer": "broad_overseas_mature",
        "sub_layer_budget": "48000",
        "instrument_type": "etf",
        "weight": "1",
        "config_hash": manifest["config_hash"],
    }]
    assert (config.output_dir / "sub_layers" / "broad_overseas_mature" / "oos.json").exists()


def _research_bar(stock_code: str, trade_date: date, close: float) -> DualPriceBar:
    return DualPriceBar(
        stock_code=stock_code, trade_date=trade_date,
        signal_open=close, signal_high=close, signal_low=close, signal_close=close,
        raw_open=close, raw_high=close, raw_low=close, raw_close=close,
        amount=20_000_000.0, suspended=False, adjustment_ratio=1.0,
        execution_availability=ExecutionAvailability(False, False, "test"),
    )

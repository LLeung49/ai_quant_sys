"""Report generation: manifest, artifact atomicity, and CSV/JSON shape."""

from __future__ import annotations

import json
import shutil
import uuid
from decimal import Decimal
from pathlib import Path

import pytest

from asset_allocation.etf_adaptive.config import AdaptiveConfig
from asset_allocation.etf_adaptive.research.baselines import BaselineKind, BaselineRun
from asset_allocation.etf_adaptive.research.report import (
    ResearchArtifact,
    write_research_report,
)
import asset_allocation.etf_adaptive.research.report as report_module
from asset_allocation.etf_adaptive.frozen_selection import FrozenSelection, _canonical_hash
from asset_allocation.etf_adaptive.state import BacktestRequest, BacktestResult


REPORTS_ROOT = Path("D:/aiQuant/ai_quant_sys/reports/pytest-report-tmp")


@pytest.fixture
def output_dir() -> Path:
    REPORTS_ROOT.mkdir(parents=True, exist_ok=True)
    target = REPORTS_ROOT / f"run-{uuid.uuid4().hex}"
    target.mkdir(parents=True, exist_ok=True)
    try:
        yield target
    finally:
        shutil.rmtree(target, ignore_errors=True)


def _research_result() -> ResearchArtifact:
    return ResearchArtifact(
        attempted_config_count=12,
        failed_config_count=2,
        data_cutoff="2026-09-01",
        config_hash="abcdef0123456789",
        artifacts={
            "stitched_oos_nav": [
                {"window_id": "wf_000", "trade_date": "2026-08-01", "nav_total": 1.02},
                {"window_id": "wf_000", "trade_date": "2026-08-02", "nav_total": 1.04},
            ],
            "trades": [
                {
                    "trade_date": "2026-08-01",
                    "side": "BUY",
                    "shares": 100,
                    "raw_price": 1.02,
                    "reason": "grid_buy",
                    "config_hash": "abcdef0123456789",
                },
            ],
            "executive_report": (
                "# 报告\n\n"
                "本报告为测试用例输出，覆盖 staged walk-forward 与 Pareto 选择。\n"
            ),
        },
    )


def test_report_manifest_records_all_attempts_and_data_cutoff(output_dir: Path) -> None:
    manifest = write_research_report(_research_result(), output_dir)

    payload = json.loads((output_dir / "manifest.json").read_text(encoding="utf-8"))
    assert payload["data_cutoff"] == "2026-09-01"
    assert payload["attempted_config_count"] == 12
    assert payload["failed_config_count"] == 2
    assert payload["config_hash"] == manifest.config_hash


def test_report_writes_every_required_artifact(output_dir: Path) -> None:
    write_research_report(_research_result(), output_dir)

    expected_files = (
        "manifest.json",
        "universe_audit.json",
        "attempted_configs.json",
        "failed_configs.json",
        "window_selections.json",
        "stitched_oos_nav.csv",
        "trades.csv",
        "mode_attribution.json",
        "cost_scenarios.json",
        "exposure_ranking.json",
        "product_ranking.json",
        "pareto_set.json",
        "portfolio_comparisons.json",
        "executive_report.md",
    )
    for name in expected_files:
        assert (output_dir / name).exists(), f"missing artifact {name}"


def test_report_clears_staging_directory_on_overwrite(output_dir: Path) -> None:
    write_research_report(_research_result(), output_dir)
    staging = output_dir.with_suffix(output_dir.suffix + ".staging")

    write_research_report(_research_result(), output_dir)

    assert not staging.exists()


def test_report_republishes_nested_sub_layer_artifacts(output_dir: Path) -> None:
    from dataclasses import replace
    layered = replace(_research_result(), sub_layers={
        "broad_overseas_mature": {"budget": "48000", "oos": [{"return": 0.1}]},
    })

    write_research_report(layered, output_dir)
    write_research_report(layered, output_dir)

    assert (output_dir / "sub_layers" / "broad_overseas_mature" / "oos.json").exists()


def test_publish_directory_retries_transient_windows_permission_error(tmp_path, monkeypatch) -> None:
    staging = tmp_path / "staging"
    destination = tmp_path / "destination"
    staging.mkdir()
    (staging / "artifact.txt").write_text("ready", encoding="utf-8")
    real_replace = report_module.os.replace
    attempts = 0

    def flaky_replace(source, target):
        nonlocal attempts
        attempts += 1
        if attempts == 1:
            raise PermissionError(5, "access denied")
        return real_replace(source, target)

    monkeypatch.setattr(report_module.os, "replace", flaky_replace)

    report_module.publish_directory(staging, destination)

    assert attempts == 2
    assert (destination / "artifact.txt").read_text(encoding="utf-8") == "ready"


def test_report_rejects_unsafe_sub_layer_path(output_dir: Path) -> None:
    from dataclasses import replace
    layered = replace(_research_result(), sub_layers={"../escape": {"budget": "1"}})

    with pytest.raises(ValueError, match="sub-layer"):
        write_research_report(layered, output_dir)


def test_report_manifest_round_trips_frozen_selection(output_dir: Path) -> None:
    payload = {
        "selection_id": "selection-2026-09", "data_cutoff": "2026-09-01",
        "activation_date": "2026-09-02", "review_date": "2027-03-04",
        "targets": [{
            "stock_code": "510300.SH", "tracking_index_code": "000300.SH",
            "layer": "broad_beta", "sub_layer": "broad_domestic_core",
            "sub_layer_budget": "12000", "instrument_type": "etf", "weight": "1",
        }],
        "sub_layer_budgets": {"broad_domestic_core": "12000"},
    }
    payload["config_hash"] = _canonical_hash(payload)
    artifact = _research_result()
    from dataclasses import replace
    write_research_report(replace(artifact, frozen_selection=payload), output_dir)
    assert FrozenSelection.from_research_manifest(output_dir / "manifest.json").selection_id == "selection-2026-09"
    assert (output_dir / "manifest.json").exists()


def test_report_stitched_nav_csv_serializes_provided_rows(output_dir: Path) -> None:
    write_research_report(_research_result(), output_dir)

    csv_text = (output_dir / "stitched_oos_nav.csv").read_text(encoding="utf-8")
    assert "window_id,trade_date,nav_total" in csv_text
    assert "wf_000,2026-08-01,1.02" in csv_text


def test_report_trades_csv_serializes_provided_rows(output_dir: Path) -> None:
    write_research_report(_research_result(), output_dir)

    csv_text = (output_dir / "trades.csv").read_text(encoding="utf-8")
    assert "trade_date,side,shares,raw_price,reason,config_hash" in csv_text
    assert "grid_buy" in csv_text


def test_report_executive_markdown_preserves_chinese_payload(output_dir: Path) -> None:
    write_research_report(_research_result(), output_dir)

    text = (output_dir / "executive_report.md").read_text(encoding="utf-8")
    assert "本报告为测试用例输出" in text
    assert text.startswith("# ")


def test_report_manifest_payload_serializes_data_cutoff_iso(output_dir: Path) -> None:
    write_research_report(_research_result(), output_dir)
    payload = json.loads((output_dir / "manifest.json").read_text(encoding="utf-8"))

    assert payload["data_cutoff"] == "2026-09-01"
    assert len(payload["data_cutoff"]) == 10


def test_report_publishes_mutually_exclusive_baseline_provenance(output_dir: Path) -> None:
    from dataclasses import replace

    request = BacktestRequest("510300.SH", Decimal("100000"))
    empty_result = BacktestResult(request, (), ())
    strategy_run = BaselineRun(
        BaselineKind.FULL_ADAPTIVE, AdaptiveConfig.default(), empty_result,
        notes=("strategy_spec=full_adaptive@1", "strategy_spec_hash=strategy-hash"),
        strategy_spec_hash="strategy-hash",
    )
    benchmark_run = BaselineRun(
        BaselineKind.FIXED_HALF_HOLD, AdaptiveConfig.default(), empty_result,
        notes=("benchmark_spec=fixed_half_hold@1", "benchmark_spec_hash=benchmark-hash"),
        benchmark_spec_hash="benchmark-hash",
    )
    artifact = replace(_research_result(), baseline_provenance={
        strategy_run.kind.value: strategy_run.provenance,
        benchmark_run.kind.value: benchmark_run.provenance,
    })

    write_research_report(artifact, output_dir)

    manifest = json.loads((output_dir / "manifest.json").read_text(encoding="utf-8"))
    report = (output_dir / "executive_report.md").read_text(encoding="utf-8")
    assert manifest["baseline_provenance"]["full_adaptive"]["strategy_spec_hash"] == "strategy-hash"
    assert manifest["baseline_provenance"]["fixed_half_hold"]["benchmark_spec_hash"] == "benchmark-hash"
    assert "strategy_spec_hash=strategy-hash" in report
    assert "benchmark_spec_hash=benchmark-hash" in report

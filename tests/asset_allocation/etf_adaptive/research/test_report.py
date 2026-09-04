"""Report generation: manifest, artifact atomicity, and CSV/JSON shape."""

from __future__ import annotations

import json
import shutil
import uuid
from pathlib import Path

import pytest

from asset_allocation.etf_adaptive.research.report import (
    ResearchArtifact,
    write_research_report,
)


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

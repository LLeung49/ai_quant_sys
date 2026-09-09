from datetime import date
from pathlib import Path

from asset_allocation.etf_adaptive.contracts import SubLayer
from asset_allocation.etf_adaptive.research.instrument_validation import (
    InstrumentValidationResult,
    ValidationScope,
    ValidationStatus,
    ValidationTarget,
    ValidationWindowResult,
)
from asset_allocation.etf_adaptive.research.validation_report import write_validation_artifacts


def test_write_validation_artifacts_emits_metrics_csv_markdown_and_three_panel_chart(tmp_path: Path) -> None:
    target = ValidationTarget("test", "159915.SZ", SubLayer.DOMESTIC_GROWTH)
    result = InstrumentValidationResult(
        target=target,
        status=ValidationStatus.FAILED,
        as_of_date=date(2026, 9, 8),
        windows=(ValidationWindowResult(
            "wf_000", date(2025, 1, 2), date(2025, 7, 1), "abc123",
            0.10, 0.08, (1.0, 1.02, 1.10), (1.0, 1.01, 1.08),
        ),),
        strategy_annual_return=0.10,
        benchmark_annual_return=0.08,
        strategy_max_drawdown=0.03,
        benchmark_max_drawdown=0.04,
        scope=ValidationScope.FORMAL,
    )

    manifest = write_validation_artifacts(result, tmp_path / "159915.SZ")

    assert manifest.summary_json.exists()
    assert manifest.windows_csv.exists()
    assert manifest.trades_csv.exists()
    assert manifest.report_markdown.exists()
    assert manifest.chart_png.exists()
    assert (tmp_path / "159915.SZ" / "charts" / "wf_000.png").exists()
    assert manifest.chart_png.stat().st_size > 1_000
    assert "sharpe" in manifest.summary_json.read_text(encoding="utf-8")
    assert "三联图" in manifest.report_markdown.read_text(encoding="utf-8")

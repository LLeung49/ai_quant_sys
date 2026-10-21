"""Tests for the Phase 4.5 collector + Repair Alpha pipeline integration."""

import importlib
import sys
from unittest import mock

import pytest

def test_run_daily_pipeline_module_exists() -> None:
    """The pipeline entry point module is importable."""

    mod = importlib.import_module("data_ingestion.run_daily_pipeline")
    assert hasattr(mod, "main")
    assert hasattr(mod, "build_parser")


def test_run_daily_pipeline_help_works() -> None:
    """--help is a clean way for the operator to verify the pipeline is wired."""

    from data_ingestion import run_daily_pipeline

    saved_argv = sys.argv
    sys.argv = ["run_daily_pipeline", "--help"]
    try:
        with pytest.raises(SystemExit):
            run_daily_pipeline.main()
    finally:
        sys.argv = saved_argv


def test_run_daily_pipeline_parser_accepts_typical_args() -> None:
    from data_ingestion import run_daily_pipeline

    args = run_daily_pipeline.build_parser().parse_args([
        "--as-of-date", "2026-08-17", "--mode", "backfill",
        "--allow-estimated-pit", "--sector", "专业服务", "--dry-run",
    ])
    assert args.as_of_date == "2026-08-17"
    assert args.mode == "backfill"
    assert args.allow_estimated_pit is True
    assert args.sector == "专业服务"
    assert args.dry_run is True
    assert args.skip_collector is False


def test_run_daily_pipeline_forwards_date_and_dry_run_to_akshare_collector() -> None:
    from data_ingestion import run_daily_pipeline

    captured = []

    class Collector:
        @staticmethod
        def main(argv):
            captured.extend(argv)
            return 0

    args = run_daily_pipeline.build_parser().parse_args([
        "--as-of-date", "2026-08-17", "--dry-run", "--skip-repair",
    ])
    with mock.patch.object(
        run_daily_pipeline.importlib, "import_module", return_value=Collector
    ):
        assert run_daily_pipeline.run_collector(args) == 0

    assert captured == [
        "--as-of-date", "2026-08-17", "--workers", "4", "--dry-run",
    ]


def test_run_daily_pipeline_skips_collector_when_flagged() -> None:
    """The pipeline respects --skip-collector for tests that exercise only the repair stage."""

    from data_ingestion import run_daily_pipeline

    # Stub both stages so the test doesn't touch QMT or MySQL.
    with mock.patch.object(
        run_daily_pipeline, "run_collector", return_value=0,
    ) as collector_mock:
        with mock.patch.object(
            run_daily_pipeline, "run_repair_runner", return_value=0,
        ) as repair_mock:
            rc = run_daily_pipeline.main([
                "--as-of-date", "2026-08-17", "--mode", "backfill",
                "--skip-collector", "--allow-estimated-pit",
            ])
    assert collector_mock.call_count == 0
    assert repair_mock.call_count == 1
    assert rc == 0


def test_run_daily_pipeline_collector_failure_skips_repair() -> None:
    """Do not publish repair candidates from a partially failed financial run."""

    from data_ingestion import run_daily_pipeline

    with mock.patch.object(
        run_daily_pipeline, "run_collector",
        side_effect=RuntimeError("collector down"),
    ):
        with mock.patch.object(
            run_daily_pipeline, "run_repair_runner", return_value=0,
        ) as repair_mock:
            rc = run_daily_pipeline.main([
                "--as-of-date", "2026-08-17", "--mode", "backfill",
                "--allow-estimated-pit",
            ])
    assert repair_mock.call_count == 0
    assert rc == 1


def test_run_daily_pipeline_propagates_collector_nonzero_return() -> None:
    """A clean collector return must still preserve its failure status."""

    from data_ingestion import run_daily_pipeline

    with mock.patch.object(
        run_daily_pipeline, "run_collector", return_value=7,
    ):
        with mock.patch.object(
            run_daily_pipeline, "run_repair_runner", return_value=0,
        ) as repair_mock:
            rc = run_daily_pipeline.main([
                "--as-of-date", "2026-08-17", "--mode", "backfill",
                "--allow-estimated-pit",
            ])
    assert repair_mock.call_count == 0
    assert rc == 1


def test_migration_sql_dedupe_via_source_hash() -> None:
    """The migration's NOT EXISTS clause keys on source_hash, so re-runs are idempotent.

    The SQL itself is exercised by the MySQL operator; this unit test
    only documents the dedupe contract by inspecting the SQL string.
    """

    import os
    path = os.path.join("sql", "20260821_migrate_trade_stock_financial_to_pit.sql")
    with open(path, "r", encoding="utf-8") as f:
        sql = f.read()
    assert "INSERT INTO trade_stock_financial_raw_pit" in sql
    assert "NOT EXISTS" in sql
    assert "SHA2(" in sql
    assert "source_table" in sql
    assert "stock_code" in sql
    assert "report_date" in sql
    assert "pit_estimated" in sql

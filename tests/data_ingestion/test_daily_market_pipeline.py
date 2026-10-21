from __future__ import annotations

import json
import os
from datetime import date, timedelta
from pathlib import Path
import subprocess
import sys

import pytest

from data_ingestion import db_config, run_daily_market_pipeline
from data_ingestion.run_daily_market_pipeline import DailyStep, run_steps


ROOT = Path(__file__).resolve().parents[2]


def test_plan_runs_the_complete_non_financial_daily_pipeline() -> None:
    env = os.environ.copy()
    env["PYTHONPATH"] = str(ROOT / "src")
    env["PYTHONUTF8"] = "1"

    completed = subprocess.run(
        [
            sys.executable,
            "-m",
            "data_ingestion.run_daily_market_pipeline",
            "--as-of-date",
            "2026-10-13",
            "--plan",
        ],
        cwd=ROOT,
        env=env,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )

    assert completed.returncode == 0, completed.stderr
    plan = json.loads(completed.stdout)
    assert plan[0]["name"] == "AKShare 原始行情与复权行情采集"
    assert plan[-1]["name"] == "趋势个股候选"
    assert len(plan) == 13
    assert all(step["as_of_date"] == "2026-10-13" for step in plan[1:])

    rendered = json.dumps(plan, ensure_ascii=False)
    assert "8-原始行情与复权数据采集.py" in rendered
    assert "1-行情数据采集.py" not in rendered
    assert "run_daily_pipeline" not in rendered
    assert "run_repair_daily" not in rendered
    research_steps = plan[-3:]
    assert all(
        step["command"][-2:] == ["--mode", "backfill"]
        for step in research_steps
    )


def test_financial_daily_stage_is_opt_in_and_runs_after_market_research(
) -> None:
    target = date.today()
    plan = run_daily_market_pipeline.build_downstream_steps(target, include_financial=True)
    assert plan[-1].name == "AKShare 财务与 Repair Alpha"
    assert plan[-1].argv[-4:] == (
        "--as-of-date", target.isoformat(), "--mode", "live_shadow",
    )
    assert plan[-2].name == "趋势个股候选"


def test_financial_daily_stage_rejects_historical_target_before_any_step(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    calls = []
    monkeypatch.setattr(run_daily_market_pipeline, "run_steps", lambda steps: calls.append(steps))
    assert run_daily_market_pipeline.main([
        "--as-of-date", (date.today() - timedelta(days=1)).isoformat(),
        "--include-financial", "--plan",
    ]) == 2
    assert calls == []


def test_run_steps_stops_after_the_first_failed_process(tmp_path: Path) -> None:
    log_path = tmp_path / "steps.log"
    failed = tmp_path / "failed.py"
    failed.write_text(
        f"from pathlib import Path\nPath({str(log_path)!r}).write_text('failed', encoding='utf-8')\nraise SystemExit(7)\n",
        encoding="utf-8",
    )
    must_not_run = tmp_path / "must_not_run.py"
    must_not_run.write_text(
        f"from pathlib import Path\nPath({str(log_path)!r}).write_text('ran-after-failure', encoding='utf-8')\n",
        encoding="utf-8",
    )
    target = date(2026, 10, 13)

    result = run_steps(
        [
            DailyStep("失败步骤", (sys.executable, str(failed)), target),
            DailyStep("不应执行", (sys.executable, str(must_not_run)), target),
        ]
    )

    assert result == 7
    assert log_path.read_text(encoding="utf-8") == "failed"


@pytest.mark.parametrize("bad_projection", ["missing", "zero_price", "code_mismatch"])
def test_daily_entry_rejects_invalid_target_market_before_downstream(
    monkeypatch: pytest.MonkeyPatch, bad_projection: str,
) -> None:
    valid = {
        "stock_code": "600519.SH", "open_price": 10, "high_price": 11,
        "low_price": 9, "close_price": 10,
    }

    def market_rows(sql: str, params: tuple[str]) -> list[dict]:
        assert params == ("2026-10-19",)
        if bad_projection == "missing" and "trade_stock_daily_bfq" in sql:
            return []
        row = dict(valid)
        if bad_projection == "zero_price" and "trade_stock_daily_qfq" in sql:
            row["close_price"] = 0
        if bad_projection == "code_mismatch" and "trade_stock_daily_bfq" in sql:
            row["stock_code"] = "000001.SZ"
        return [row]

    monkeypatch.setattr(db_config, "execute_query", market_rows)
    monkeypatch.setattr(
        run_daily_market_pipeline, "run_steps",
        lambda steps: (_ for _ in ()).throw(AssertionError("downstream must not run")),
    )

    assert run_daily_market_pipeline.main([
        "--as-of-date", "2026-10-19", "--skip-market-collection",
    ]) == 1


def test_daily_gap_is_reported_without_blocking_downstream(monkeypatch, tmp_path):
    calls = []
    monkeypatch.setattr(run_daily_market_pipeline, "market_date_issue", lambda target: None)
    monkeypatch.setattr(run_daily_market_pipeline, "find_missing_market_codes", lambda target: (
        date(2026, 10, 19), ["159318.SZ"],
    ))
    monkeypatch.setattr(run_daily_market_pipeline, "write_gap_report", lambda *args: tmp_path / "gap.json")
    monkeypatch.setattr(run_daily_market_pipeline, "run_steps", lambda steps: (calls.append(steps), 0)[1])

    assert run_daily_market_pipeline.main([
        "--as-of-date", "2026-10-20", "--skip-market-collection",
    ]) == 0
    assert len(calls) == 1
    assert len(calls[0]) == 12


def test_failed_collection_still_records_gap(monkeypatch, tmp_path):
    reports = []
    monkeypatch.setattr(run_daily_market_pipeline, "run_steps", lambda steps: 1)
    monkeypatch.setattr(run_daily_market_pipeline, "find_missing_market_codes", lambda target: (
        date(2026, 10, 19), ["159318.SZ"],
    ))
    monkeypatch.setattr(run_daily_market_pipeline, "write_gap_report", lambda *args: reports.append(args[2]))

    assert run_daily_market_pipeline.main(["--as-of-date", "2026-10-20"]) == 1
    assert reports == [["159318.SZ"]]


def test_retry_missing_collects_only_gap_then_refreshes_downstream(monkeypatch, tmp_path):
    calls = []
    reports = []
    gaps = iter([
        (date(2026, 10, 19), ["159318.SZ"]),
        (date(2026, 10, 19), []),
    ])
    monkeypatch.setattr(run_daily_market_pipeline, "market_date_issue", lambda target: None)
    monkeypatch.setattr(run_daily_market_pipeline, "find_missing_market_codes", lambda target: next(gaps))
    monkeypatch.setattr(run_daily_market_pipeline, "write_gap_report", lambda *args: (reports.append(args[2]), tmp_path / "gap.json")[1])
    monkeypatch.setattr(run_daily_market_pipeline, "run_steps", lambda steps: (calls.append(steps), 0)[1])
    monkeypatch.setattr(run_daily_market_pipeline, "refresh_research_backfill", lambda target: None)

    assert run_daily_market_pipeline.main([
        "--as-of-date", "2026-10-20", "--retry-missing-market",
    ]) == 0
    assert len(calls) == 3
    assert "--missing-only" in calls[0][0].argv
    assert len(calls[1]) == 9
    assert len(calls[2]) == 3
    assert calls[2][0].argv[-2:] == ("--mode", "backfill")
    assert reports == [["159318.SZ"], []]


def test_retry_missing_without_new_rows_skips_downstream(monkeypatch, tmp_path):
    calls = []
    monkeypatch.setattr(run_daily_market_pipeline, "find_missing_market_codes", lambda target: (
        date(2026, 10, 19), ["159318.SZ"],
    ))
    monkeypatch.setattr(run_daily_market_pipeline, "write_gap_report", lambda *args: tmp_path / "gap.json")
    monkeypatch.setattr(run_daily_market_pipeline, "run_steps", lambda steps: (calls.append(steps), 0)[1])

    assert run_daily_market_pipeline.main([
        "--as-of-date", "2026-10-20", "--retry-missing-market",
    ]) == 0
    assert len(calls) == 1


def test_retry_without_gap_can_finish_interrupted_downstream(monkeypatch, tmp_path):
    calls = []
    refreshed = []
    monkeypatch.setattr(run_daily_market_pipeline, "find_missing_market_codes", lambda target: (
        date(2026, 10, 19), [],
    ))
    monkeypatch.setattr(run_daily_market_pipeline, "write_gap_report", lambda *args: tmp_path / "gap.json")
    monkeypatch.setattr(run_daily_market_pipeline, "market_date_issue", lambda target: None)
    monkeypatch.setattr(run_daily_market_pipeline, "run_steps", lambda steps: (calls.append(steps), 0)[1])
    monkeypatch.setattr(run_daily_market_pipeline, "refresh_research_backfill", lambda target: refreshed.append(target))

    assert run_daily_market_pipeline.main([
        "--as-of-date", "2026-10-20", "--retry-missing-market",
    ]) == 0
    assert [len(steps) for steps in calls] == [9, 3]
    assert refreshed == [date(2026, 10, 20)]


def test_research_refresh_deletes_only_target_backfill_price_candidates(monkeypatch):
    calls = []

    class Cursor:
        rowcount = 12

        def __enter__(self):
            return self

        def __exit__(self, *args):
            return None

        def execute(self, sql, params):
            calls.append((sql, params))

    class Connection:
        def cursor(self):
            return Cursor()

        def commit(self):
            calls.append("commit")

        def rollback(self):
            calls.append("rollback")

        def close(self):
            calls.append("close")

    monkeypatch.setattr(db_config, "get_connection", Connection)
    assert run_daily_market_pipeline.refresh_research_backfill(date(2026, 10, 20)) == 12
    sql, params = calls[0]
    assert params == ("2026-10-20",)
    assert "snapshot_mode='backfill'" in sql
    assert "stock_repair" not in sql
    assert "sector_opportunity" in sql and "etf_core" in sql and "stock_trend" in sql
    assert calls[1:] == ["commit", "close"]

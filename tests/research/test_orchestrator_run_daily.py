import pytest

from morning_conference.sector_rotation2.research.orchestrator import run_daily
from morning_conference.sector_rotation2.research.orchestrator.run_daily import build_parser


def test_runner_accepts_live_and_backfill_modes() -> None:
    parser = build_parser()
    live = parser.parse_args(["--as-of-date", "2026-08-18", "--level", "1"])
    backfill = parser.parse_args(["--backfill-start", "2026-08-10", "--backfill-end", "2026-08-18", "--level", "2"])
    assert live.as_of_date == "2026-08-18"
    assert backfill.backfill_end == "2026-08-18"


def test_run_one_date_records_existing_run_log_lifecycle(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[tuple[object, ...]] = []
    monkeypatch.setattr(run_daily, "MySQLSnapshotStore", lambda: type("Store", (), {"ensure_schema": lambda self: None})())
    monkeypatch.setattr(run_daily, "load_v1_rows", lambda *_: [{"sector_name": "半导体"}])
    monkeypatch.setattr(run_daily, "load_v2_rows", lambda *_: [])
    monkeypatch.setattr(run_daily, "build_sector_opportunity_snapshots", lambda *_args, **_kwargs: [object()])
    monkeypatch.setattr(run_daily, "create_run", lambda *args: calls.append(("create", *args)))
    monkeypatch.setattr(run_daily, "mark_run_succeeded", lambda *args: calls.append(("succeeded", *args)))

    assert run_daily.run_one_date("2026-08-18", 1, run_daily.SnapshotMode.LIVE_SHADOW) == 1
    assert calls[0][0] == "create"
    assert calls[1][0] == "succeeded"
    assert calls[1][-2:] == (1, 0)


def test_run_one_date_marks_run_failed_before_reraising(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[tuple[object, ...]] = []
    monkeypatch.setattr(run_daily, "MySQLSnapshotStore", lambda: type("Store", (), {"ensure_schema": lambda self: None})())
    monkeypatch.setattr(run_daily, "load_v1_rows", lambda *_: [])
    monkeypatch.setattr(run_daily, "load_v2_rows", lambda *_: [])
    monkeypatch.setattr(run_daily, "create_run", lambda *args: calls.append(("create", *args)))
    monkeypatch.setattr(run_daily, "mark_run_failed", lambda *args: calls.append(("failed", *args)))
    monkeypatch.setattr(run_daily, "build_sector_opportunity_snapshots", lambda *_args, **_kwargs: (_ for _ in ()).throw(RuntimeError("broken source")))

    with pytest.raises(RuntimeError, match="broken source"):
        run_daily.run_one_date("2026-08-18", 1, run_daily.SnapshotMode.LIVE_SHADOW)
    assert calls[1][0] == "failed"
    assert "broken source" in calls[1][-1]


def test_main_reports_snapshot_count(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    monkeypatch.setattr(run_daily, "run_one_date", lambda *_: 3)

    assert run_daily.main(["--as-of-date", "2026-08-18", "--level", "1"]) == 0
    output = capsys.readouterr().out
    assert "2026-08-18" in output
    assert "3" in output

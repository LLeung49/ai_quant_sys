import pytest
from datetime import date, datetime

from morning_conference.sector_rotation2.research.orchestrator import run_daily
from morning_conference.sector_rotation2.research.orchestrator.run_daily import build_parser
from morning_conference.sector_rotation2.research.availability import AvailabilityBasis, AvailabilityMetadata
from morning_conference.sector_rotation2.research.contracts import CandidateSnapshot
from morning_conference.sector_rotation2.research.status import SnapshotMode


def test_runner_accepts_live_and_backfill_modes() -> None:
    parser = build_parser()
    live = parser.parse_args(["--as-of-date", "2026-08-18", "--level", "1"])
    backfill = parser.parse_args(["--backfill-start", "2026-08-10", "--backfill-end", "2026-08-18", "--level", "2"])
    assert live.as_of_date == "2026-08-18"
    assert backfill.backfill_end == "2026-08-18"


def test_live_shadow_rejects_historical_date_unless_today_override_matches() -> None:
    with pytest.raises(ValueError, match="non-today"):
        run_daily.validate_mode_for_date(
            date(2026, 8, 18), SnapshotMode.LIVE_SHADOW, today=date(2026, 8, 19),
        )

    run_daily.validate_mode_for_date(
        date(2026, 8, 18), SnapshotMode.LIVE_SHADOW, today=date(2026, 8, 18),
    )


def test_main_wires_today_override_to_each_single_date_run(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[tuple[object, ...]] = []
    monkeypatch.setattr(run_daily, "run_one_date", lambda *args, **kwargs: calls.append((*args, kwargs)) or 1)

    assert run_daily.main([
        "--as-of-date", "2026-08-18", "--level", "1", "--today", "2026-08-18",
    ]) == 0

    assert calls == [("2026-08-18", 1, SnapshotMode.LIVE_SHADOW, {"today": date(2026, 8, 18)})]


def test_run_one_date_records_existing_run_log_lifecycle(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[tuple[object, ...]] = []
    monkeypatch.setattr(run_daily, "MySQLSnapshotStore", lambda: type("Store", (), {"ensure_schema": lambda self: None})())
    monkeypatch.setattr(run_daily, "load_v1_rows", lambda *_: [{"sector_name": "半导体"}])
    monkeypatch.setattr(run_daily, "load_v2_rows", lambda *_: [])
    monkeypatch.setattr(run_daily, "build_sector_opportunity_snapshots", lambda *_args, **_kwargs: [object()])
    monkeypatch.setattr(run_daily, "persist_sector_opportunity", lambda _store, snapshot: snapshot)
    monkeypatch.setattr(run_daily, "create_run", lambda *args: calls.append(("create", *args)))
    monkeypatch.setattr(run_daily, "mark_run_succeeded", lambda *args: calls.append(("succeeded", *args)))

    assert run_daily.run_one_date(
        "2026-08-18", 1, run_daily.SnapshotMode.LIVE_SHADOW, today=date(2026, 8, 18),
    ) == 1
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
        run_daily.run_one_date(
            "2026-08-18", 1, run_daily.SnapshotMode.LIVE_SHADOW, today=date(2026, 8, 18),
        )
    assert calls[1][0] == "failed"
    assert "broken source" in calls[1][-1]


def test_delayed_root_resolves_one_run_time_after_candidate_computation(monkeypatch: pytest.MonkeyPatch) -> None:
    events: list[str] = []
    snapshot = CandidateSnapshot(
        as_of_date=date(2026, 8, 24), entity_type='sector', entity_code='Bank', sector_level=2,
        sector_name='Bank', strategy_type='sector_opportunity', candidate_status='trend_continue',
        candidate_score=0.8, model_version='v1', config_hash='hash', run_id='run',
        snapshot_mode=SnapshotMode.DELAYED_SHADOW,
    )
    monkeypatch.setattr(run_daily, 'MySQLSnapshotStore', lambda: type('Store', (), {'ensure_schema': lambda self: None})())
    monkeypatch.setattr(run_daily, 'create_run', lambda *_args: None)
    monkeypatch.setattr(run_daily, 'mark_run_succeeded', lambda *_args: None)
    monkeypatch.setattr(run_daily, 'load_v1_rows', lambda *_args: [{'sector_name': 'Bank'}])
    monkeypatch.setattr(run_daily, 'load_v2_rows', lambda *_args: [])
    monkeypatch.setattr(
        run_daily, 'build_sector_opportunity_snapshots',
        lambda *_args, **kwargs: (events.append('build'), [snapshot])[1] if kwargs['persist'] is False else pytest.fail('root persisted before timing'),
    )
    metadata = AvailabilityMetadata(
        data_available_at=datetime(2026, 8, 24, 18), run_at=datetime(2026, 8, 25, 9, 10),
        execution_eligible_at=datetime(2026, 8, 25, 9, 30), daily_bar_entry_date=date(2026, 8, 25),
        availability_basis=AvailabilityBasis.MARKET_CLOSE_1800,
    )
    monkeypatch.setattr(run_daily, '_delayed_availability', lambda *_args: (events.append('availability'), metadata)[1])
    persisted = []
    monkeypatch.setattr(run_daily, 'persist_sector_opportunity', lambda _store, item: persisted.append(item))

    assert run_daily.run_one_date('2026-08-24', 2, SnapshotMode.DELAYED_SHADOW, now=datetime(2026, 8, 25, 9, 10)) == 1
    assert events == ['build', 'availability']
    assert persisted[0].run_at == metadata.run_at


def test_main_reports_snapshot_count(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    monkeypatch.setattr(run_daily, "run_one_date", lambda *_, **__: 3)

    assert run_daily.main(["--as-of-date", "2026-08-18", "--level", "1"]) == 0
    output = capsys.readouterr().out
    assert "2026-08-18" in output
    assert "3" in output

from datetime import date

import pytest

from morning_conference.sector_rotation2.research.etf_core import run_daily
from morning_conference.sector_rotation2.research.status import SnapshotMode


def test_etf_runner_accepts_live_and_backfill_arguments() -> None:
    parser = run_daily.build_parser()
    live = parser.parse_args(["--as-of-date", "2026-08-18", "--level", "1"])
    backfill = parser.parse_args([
        "--backfill-start", "2026-08-10", "--backfill-end", "2026-08-18", "--level", "2",
    ])

    assert live.as_of_date == "2026-08-18"
    assert backfill.backfill_end == "2026-08-18"


def test_live_runner_rejects_historical_as_of_date() -> None:
    with pytest.raises(ValueError, match="BACKFILL"):
        run_daily.validate_mode_for_date(
            date(2026, 8, 17), SnapshotMode.LIVE_SHADOW, today=date(2026, 8, 18),
        )


def test_live_runner_rejects_future_as_of_date() -> None:
    with pytest.raises(ValueError, match="BACKFILL"):
        run_daily.validate_mode_for_date(
            date(2026, 8, 19), SnapshotMode.LIVE_SHADOW, today=date(2026, 8, 18),
        )


def test_runner_loads_one_deterministic_sector_snapshot_with_identity() -> None:
    assert hasattr(run_daily, "load_sector_rows")
    captured: dict[str, object] = {}

    def query(sql: str, params: tuple[object, ...]) -> list[dict[str, object]]:
        captured.update(sql=sql, params=params)
        return [{"sector_name": "半导体", "candidate_status": "ready", "model_version": "sector_opportunity_v1", "config_hash": "cfg", "snapshot_mode": "live_shadow"}]

    assert run_daily.load_sector_rows("2026-08-18", 2, SnapshotMode.LIVE_SHADOW, query) == [
        {"sector_name": "半导体", "candidate_status": "ready", "model_version": "sector_opportunity_v1", "config_hash": "cfg", "snapshot_mode": "live_shadow"},
    ]
    assert "ROW_NUMBER() OVER" in str(captured["sql"])
    assert "entity_type='sector'" in str(captured["sql"])


def test_runner_does_not_migrate_mapping_schema_on_every_execution(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(run_daily, "ensure_mapping_schema", lambda: (_ for _ in ()).throw(AssertionError("DDL")), raising=False)
    monkeypatch.setattr(run_daily, "MySQLSnapshotStore", lambda: type("Store", (), {"ensure_schema": lambda self: None})())
    monkeypatch.setattr(run_daily, "load_sector_rows", lambda *_: [])

    assert run_daily.run_one_date(date.today().isoformat(), 2) == 0

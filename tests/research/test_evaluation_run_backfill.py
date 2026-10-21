from datetime import date, datetime

from morning_conference.sector_rotation2.research.availability import AvailabilityBasis
from morning_conference.sector_rotation2.research.contracts import CandidateSnapshot, ReturnStatus
from morning_conference.sector_rotation2.research.evaluation.run_backfill import CachingProvider, main, run
from morning_conference.sector_rotation2.research.evaluation.prices import PriceBar
from morning_conference.sector_rotation2.research.status import SnapshotMode


def test_caching_provider_queries_each_entity_once() -> None:
    calls = []

    def query(sql, params):
        calls.append(params)
        return [{"trade_date": date(2026, 1, 5), "close": 10, "open": 9, "high": 11, "low": 8}]

    provider = CachingProvider(query, date(2026, 1, 1), date(2026, 1, 10))
    provider.load_bars("stock", "000001.SZ", date(2026, 1, 5), date(2026, 1, 5))
    provider.load_bars("stock", "000001.SZ", date(2026, 1, 5), date(2026, 1, 6))
    assert len(calls) == 1


def test_forward_label_cli_accepts_delayed_shadow(monkeypatch) -> None:
    monkeypatch.setattr("sys.argv", ["run_backfill", "--snapshot-mode", "delayed_shadow", "--start-date", "2026-01-05", "--end-date", "2026-01-06"])
    monkeypatch.setattr("morning_conference.sector_rotation2.research.evaluation.run_backfill.run", lambda **kwargs: {"snapshot_mode": kwargs["snapshot_mode"].value})

    main()


def test_delayed_run_extends_calendar_past_cli_end_date(monkeypatch) -> None:
    signal_date = date(2026, 1, 5)
    snapshot = CandidateSnapshot(
        snapshot_id=1, as_of_date=signal_date, entity_type="stock", entity_code="000001.SZ", sector_level=2,
        sector_name="test", strategy_type="short_term", candidate_status="candidate", candidate_score=1.0,
        model_version="v1", config_hash="c1", run_id="run", snapshot_mode=SnapshotMode.DELAYED_SHADOW,
        data_available_at=datetime(2026, 1, 5, 18), run_at=datetime(2026, 1, 6, 10),
        execution_eligible_at=datetime(2026, 1, 6, 10), availability_basis=AvailabilityBasis.MARKET_CLOSE_1800,
    )
    captured = {}
    monkeypatch.setattr("morning_conference.sector_rotation2.research.evaluation.run_backfill.execute_query", lambda *_: [{}])
    monkeypatch.setattr("morning_conference.sector_rotation2.research.evaluation.run_backfill._snapshot_from_row", lambda _: snapshot)

    def calendar_loader(start, end, *_args, **_kwargs):
        captured["end"] = end
        return (signal_date, date(2026, 1, 6), date(2026, 1, 7))

    monkeypatch.setattr("morning_conference.sector_rotation2.research.evaluation.run_backfill.load_authoritative_market_calendar", calendar_loader)
    monkeypatch.setattr("morning_conference.sector_rotation2.research.evaluation.run_backfill.backfill_forward_labels", lambda **kwargs: [])
    class Connection:
        def close(self):
            pass
    monkeypatch.setattr("morning_conference.sector_rotation2.research.evaluation.run_backfill.get_connection", Connection)
    monkeypatch.setattr("morning_conference.sector_rotation2.research.evaluation.run_backfill.ensure_evaluation_tables", lambda _: None)
    monkeypatch.setattr("morning_conference.sector_rotation2.research.evaluation.run_backfill.persist_forward_labels", lambda *_: 0)

    result = run(snapshot_mode=SnapshotMode.DELAYED_SHADOW, start_date=signal_date, end_date=signal_date, sector_level=2)

    assert captured["end"] > signal_date
    assert result["label_count"] == 0


def test_delayed_backfill_persists_not_matured_when_calendar_coverage_is_exhausted(monkeypatch) -> None:
    signal_date = date(2026, 1, 6)
    snapshot = CandidateSnapshot(
        snapshot_id=9, as_of_date=signal_date, entity_type="stock", entity_code="000001.SZ", sector_level=2,
        sector_name="test", strategy_type="short_term", candidate_status="candidate", candidate_score=1.0,
        model_version="v1", config_hash="c1", run_id="run", snapshot_mode=SnapshotMode.DELAYED_SHADOW,
        data_available_at=datetime(2026, 1, 6, 18), run_at=datetime(2026, 1, 6, 20),
        execution_eligible_at=datetime(2026, 1, 7, 9, 30), availability_basis=AvailabilityBasis.MARKET_CLOSE_1800,
    )
    persisted = []
    monkeypatch.setattr("morning_conference.sector_rotation2.research.evaluation.run_backfill.execute_query", lambda *_: [{}])
    monkeypatch.setattr("morning_conference.sector_rotation2.research.evaluation.run_backfill._snapshot_from_row", lambda _: snapshot)
    monkeypatch.setattr(
        "morning_conference.sector_rotation2.research.evaluation.run_backfill.load_authoritative_market_calendar",
        lambda *_args, **_kwargs: (signal_date,),
    )

    class Connection:
        def close(self):
            pass

    monkeypatch.setattr("morning_conference.sector_rotation2.research.evaluation.run_backfill.get_connection", Connection)
    monkeypatch.setattr("morning_conference.sector_rotation2.research.evaluation.run_backfill.ensure_evaluation_tables", lambda _: None)

    def persist(_connection, labels, _context):
        persisted.extend(labels)
        return len(labels)

    monkeypatch.setattr("morning_conference.sector_rotation2.research.evaluation.run_backfill.persist_forward_labels", persist)

    result = run(
        snapshot_mode=SnapshotMode.DELAYED_SHADOW,
        start_date=signal_date,
        end_date=signal_date,
        sector_level=2,
    )

    assert result["status_counts"] == {ReturnStatus.NOT_MATURED.value: 3}
    assert len(persisted) == 3
    assert all(label.source_snapshot_id == 9 for label in persisted)


def test_backfill_accepts_bounded_calendar_end(monkeypatch) -> None:
    signal_date = date(2024, 1, 2)
    snapshot = CandidateSnapshot(
        snapshot_id=10, as_of_date=signal_date, entity_type="stock", entity_code="000001.SZ", sector_level=2,
        sector_name="test", strategy_type="stock_repair", candidate_status="candidate", candidate_score=1.0,
        model_version="v1", config_hash="c1", run_id="run", snapshot_mode=SnapshotMode.BACKFILL,
    )
    captured = {}
    monkeypatch.setattr("morning_conference.sector_rotation2.research.evaluation.run_backfill.execute_query", lambda *_: [{}])
    monkeypatch.setattr("morning_conference.sector_rotation2.research.evaluation.run_backfill._snapshot_from_row", lambda _: snapshot)
    monkeypatch.setattr(
        "morning_conference.sector_rotation2.research.evaluation.run_backfill.load_authoritative_market_calendar",
        lambda start, end, *_args, **_kwargs: (captured.setdefault("end", end), (signal_date,))[1],
    )
    monkeypatch.setattr("morning_conference.sector_rotation2.research.evaluation.run_backfill.backfill_forward_labels", lambda **kwargs: [])

    class Connection:
        def close(self):
            pass

    monkeypatch.setattr("morning_conference.sector_rotation2.research.evaluation.run_backfill.get_connection", Connection)
    monkeypatch.setattr("morning_conference.sector_rotation2.research.evaluation.run_backfill.ensure_evaluation_tables", lambda _: None)
    monkeypatch.setattr("morning_conference.sector_rotation2.research.evaluation.run_backfill.persist_forward_labels", lambda *_: 0)
    bounded_end = date(2026, 10, 19)

    run(
        snapshot_mode=SnapshotMode.BACKFILL, start_date=signal_date, end_date=signal_date,
        sector_level=2, calendar_end_date=bounded_end,
    )

    assert captured["end"] == bounded_end

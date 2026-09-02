"""Operational-time semantics shared by the three delayed candidate runners."""

from datetime import date, datetime

from morning_conference.sector_rotation2.research.availability import AvailabilityBasis
from morning_conference.sector_rotation2.research.calendar import TradingCalendar
from morning_conference.sector_rotation2.research.contracts import CandidateSnapshot
from morning_conference.sector_rotation2.research.snapshot import InMemorySnapshotStore
from morning_conference.sector_rotation2.research.status import SnapshotMode
from morning_conference.sector_rotation2.research.etf_core import run_daily as etf_runner
from morning_conference.sector_rotation2.research.orchestrator import run_daily as sector_runner
from morning_conference.sector_rotation2.research.stock_alpha import run_repair_daily, run_trend_daily
from morning_conference.sector_rotation2.research.evaluation import prices


_AS_OF = date(2026, 8, 24)
_RUN_AT = datetime(2026, 8, 25, 9, 10)
_CALENDAR = TradingCalendar([_AS_OF, date(2026, 8, 25), date(2026, 8, 26)])
_CALENDAR_DATES = (_AS_OF, date(2026, 8, 25), date(2026, 8, 26))


def _candidate(strategy_type: str) -> CandidateSnapshot:
    return CandidateSnapshot(
        as_of_date=_AS_OF, entity_type="stock", entity_code="600000", sector_level=2,
        sector_name="Bank", strategy_type=strategy_type, candidate_status="ready", candidate_score=0.8,
        model_version="v1", config_hash="hash", run_id="run",
        snapshot_mode=SnapshotMode.DELAYED_SHADOW,
    )


def test_etf_delayed_shadow_persists_market_availability(monkeypatch) -> None:
    persisted = []
    monkeypatch.setattr(etf_runner, "load_trading_calendar", lambda *_args, **_kwargs: _CALENDAR_DATES, raising=False)
    monkeypatch.setattr(etf_runner, "MySQLSnapshotStore", lambda: type("Store", (), {"ensure_schema": lambda self: None})())
    monkeypatch.setattr(etf_runner, "load_sector_rows", lambda *_args: [{
        "sector_name": "Bank", "candidate_status": "ready", "model_version": "sector-v1",
        "config_hash": "sector-hash", "snapshot_mode": "delayed_shadow",
    }])
    monkeypatch.setattr(etf_runner, "load_effective_return_etfs", lambda *_args: [{"etf_code": "510300"}])
    monkeypatch.setattr(etf_runner, "load_etf_execution_evidence", lambda *_args: {"liquid": True, "extended": False})
    monkeypatch.setattr(etf_runner, "load_etf_macd_evidence", lambda *_args: {"macd_triggered": True})
    monkeypatch.setattr(etf_runner, "persist_etf_candidate", lambda _store, snapshot: persisted.append(snapshot))

    assert etf_runner.run_one_date(_AS_OF.isoformat(), 2, SnapshotMode.DELAYED_SHADOW, now=_RUN_AT) == 1
    assert persisted[0].availability_basis is AvailabilityBasis.MARKET_CLOSE_1800
    assert persisted[0].data_available_at == datetime(2026, 8, 24, 18, 0)
    assert persisted[0].run_at == _RUN_AT
    assert persisted[0].execution_eligible_at == datetime(2026, 8, 25, 9, 30)


def test_delayed_sector_root_then_etf_child_uses_same_mode_only(monkeypatch) -> None:
    class RootStore:
        def __init__(self) -> None:
            self.inner = InMemorySnapshotStore()
            self.inserted = []

        def ensure_schema(self) -> None:
            return None

        def get(self, identity):
            return self.inner.get(identity)

        def insert(self, snapshot) -> None:
            self.inserted.append(snapshot)
            self.inner.insert(snapshot)

    root_store = RootStore()
    monkeypatch.setattr(sector_runner, "load_trading_calendar", lambda *_args, **_kwargs: _CALENDAR_DATES, raising=False)
    monkeypatch.setattr(sector_runner, "MySQLSnapshotStore", lambda: root_store)
    monkeypatch.setattr(sector_runner, "create_run", lambda *_args: None)
    monkeypatch.setattr(sector_runner, "mark_run_succeeded", lambda *_args: None)
    monkeypatch.setattr(sector_runner, "load_v1_rows", lambda *_args: [{
        "sector_name": "Bank", "score_eligible": True, "lifecycle_state": "trending",
        "phase_confirmed": "accel_up", "phase_confidence": 0.8, "participation_score": 0.2,
        "rank_change_5d": 2, "composite_score": 0.75,
    }])
    monkeypatch.setattr(sector_runner, "load_v2_rows", lambda *_args: [])
    assert sector_runner.run_one_date(_AS_OF.isoformat(), 2, SnapshotMode.DELAYED_SHADOW, now=_RUN_AT) == 1
    root = root_store.inserted[0]
    assert root.snapshot_mode is SnapshotMode.DELAYED_SHADOW
    assert root.availability_basis is AvailabilityBasis.MARKET_CLOSE_1800

    persisted = []
    monkeypatch.setattr(etf_runner, "load_trading_calendar", lambda *_args, **_kwargs: _CALENDAR_DATES, raising=False)
    monkeypatch.setattr(etf_runner, "MySQLSnapshotStore", lambda: type("Store", (), {"ensure_schema": lambda self: None})())

    def delayed_roots(_as_of, _level, mode):
        assert mode is SnapshotMode.DELAYED_SHADOW
        return [{"sector_name": root.sector_name, "candidate_status": root.candidate_status, "model_version": root.model_version, "config_hash": root.config_hash, "snapshot_mode": root.snapshot_mode.value}]

    monkeypatch.setattr(etf_runner, "load_sector_rows", delayed_roots)
    monkeypatch.setattr(etf_runner, "load_effective_return_etfs", lambda *_args: [{"etf_code": "510300"}])
    monkeypatch.setattr(etf_runner, "load_etf_execution_evidence", lambda *_args: {"liquid": True, "extended": False})
    monkeypatch.setattr(etf_runner, "load_etf_macd_evidence", lambda *_args: {"macd_triggered": True})
    monkeypatch.setattr(etf_runner, "persist_etf_candidate", lambda _store, snapshot: persisted.append(snapshot))
    assert etf_runner.run_one_date(_AS_OF.isoformat(), 2, SnapshotMode.DELAYED_SHADOW, now=_RUN_AT) == 1
    assert len(persisted) == 1
    assert persisted[0].snapshot_mode is SnapshotMode.DELAYED_SHADOW


def test_trend_delayed_shadow_passes_one_batch_availability_to_each_sector(monkeypatch) -> None:
    captured = []
    monkeypatch.setattr(run_trend_daily, "load_trading_calendar", lambda *_args, **_kwargs: _CALENDAR_DATES, raising=False)
    monkeypatch.setattr(run_trend_daily, "ensure_research_schema", lambda: None)
    monkeypatch.setattr(run_trend_daily, "MySQLSnapshotStore", lambda: type("Store", (), {"ensure_schema": lambda self: None})())
    monkeypatch.setattr(run_trend_daily, "create_run", lambda *_args: None)
    monkeypatch.setattr(run_trend_daily, "mark_run_succeeded", lambda *_args: None)
    monkeypatch.setattr(run_trend_daily, "load_trend_follow_sectors", lambda *_args: [{"sector_name": "Bank"}])

    monkeypatch.setattr(run_trend_daily, "persist_trend_candidates", lambda _store, snapshots: captured.extend(snapshots))

    def process(_sector, **_kwargs):
        return [_candidate("stock_trend")]

    monkeypatch.setattr(run_trend_daily, "_process_sector", process)
    assert run_trend_daily.run_one_date(_AS_OF.isoformat(), 2, SnapshotMode.DELAYED_SHADOW, now=_RUN_AT) == 1
    assert captured[0].availability_basis is AvailabilityBasis.MARKET_CLOSE_1800


def test_repair_delayed_shadow_passes_one_batch_availability_to_each_sector(monkeypatch) -> None:
    captured = []
    monkeypatch.setattr(run_repair_daily, "load_trading_calendar", lambda *_args, **_kwargs: _CALENDAR_DATES, raising=False)
    monkeypatch.setattr(run_repair_daily, "MySQLSnapshotStore", lambda: type("Store", (), {"ensure_schema": lambda self: None})())
    monkeypatch.setattr(run_repair_daily, "create_run", lambda *_args: None)
    monkeypatch.setattr(run_repair_daily, "mark_run_succeeded", lambda *_args: None)
    monkeypatch.setattr(run_repair_daily, "load_repair_sectors", lambda *_args: [{"sector_name": "Bank"}])

    monkeypatch.setattr(run_repair_daily, "persist_repair_candidates", lambda _store, snapshots: captured.extend(snapshots))

    def score(_sector, **_kwargs):
        return [_candidate("stock_repair")]

    monkeypatch.setattr(run_repair_daily, "score_repair_sector", score)
    assert run_repair_daily.run_one_date(_AS_OF.isoformat(), 2, SnapshotMode.DELAYED_SHADOW, now=_RUN_AT) == 1
    assert captured[0].execution_eligible_at == datetime(2026, 8, 25, 9, 30)


def test_delayed_runners_resolve_next_morning_from_future_exchange_schedule(monkeypatch) -> None:
    """Every runner uses the future-capable schedule boundary, even when DB bars stop at T."""
    future_sessions = (_AS_OF, date(2026, 8, 25), date(2026, 8, 26))
    monkeypatch.setattr(prices, "load_exchange_schedule", lambda *_args: future_sessions, raising=False)

    def completed_bars_only(_sql, _params):
        return [{"trade_date": _AS_OF}]

    monkeypatch.setattr(sector_runner, "execute_query", completed_bars_only)
    resolvers = (
        lambda run_at: sector_runner._delayed_availability(_AS_OF, 2, run_at),
        lambda run_at: etf_runner._delayed_availability(_AS_OF, 2, run_at, completed_bars_only),
        lambda run_at: run_trend_daily._delayed_availability(_AS_OF, 2, run_at, completed_bars_only),
        lambda run_at: run_repair_daily._delayed_availability(_AS_OF, 2, run_at, completed_bars_only),
    )

    for resolve in resolvers:
        availability = resolve(datetime(2026, 8, 25, 9, 10))
        assert availability.daily_bar_entry_date == date(2026, 8, 25)


def test_delayed_runners_resolve_post_open_entry_at_t_plus_two(monkeypatch) -> None:
    future_sessions = (_AS_OF, date(2026, 8, 25), date(2026, 8, 26))
    monkeypatch.setattr(prices, "load_exchange_schedule", lambda *_args: future_sessions, raising=False)

    def completed_bars_only(_sql, _params):
        return [{"trade_date": _AS_OF}]

    monkeypatch.setattr(sector_runner, "execute_query", completed_bars_only)
    resolvers = (
        lambda: sector_runner._delayed_availability(_AS_OF, 2, datetime(2026, 8, 25, 10)),
        lambda: etf_runner._delayed_availability(_AS_OF, 2, datetime(2026, 8, 25, 10), completed_bars_only),
        lambda: run_trend_daily._delayed_availability(_AS_OF, 2, datetime(2026, 8, 25, 10), completed_bars_only),
        lambda: run_repair_daily._delayed_availability(_AS_OF, 2, datetime(2026, 8, 25, 10), completed_bars_only),
    )

    for resolve in resolvers:
        assert resolve().daily_bar_entry_date == date(2026, 8, 26)

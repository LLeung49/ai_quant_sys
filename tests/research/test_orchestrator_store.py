import json
from datetime import date, datetime
from decimal import Decimal
from pathlib import Path

from morning_conference.sector_rotation2.research.availability import AvailabilityBasis
from morning_conference.sector_rotation2.research.contracts import CandidateSnapshot, SnapshotIdentity
from morning_conference.sector_rotation2.research.orchestrator.store import RESEARCH_SNAPSHOT_DDL, MySQLSnapshotStore, _identity_values, _snapshot_from_row
from morning_conference.sector_rotation2.research.status import SnapshotMode


def test_research_snapshot_schema_keeps_live_identity_immutable() -> None:
    normalized = ' '.join(RESEARCH_SNAPSHOT_DDL.lower().split())
    assert 'create table if not exists research_candidate_snapshot' in normalized
    assert 'snapshot_mode varchar(16) not null' in normalized
    assert 'unique key uk_research_snapshot_identity' in normalized
    assert 'as_of_date, entity_type, entity_code, strategy_type, model_version, config_hash, snapshot_mode' in normalized
    assert 'rank_in_sector int null' in normalized
    assert 'on duplicate key update' not in normalized


def test_identity_values_are_bindable_for_mysql_lookup() -> None:
    identity = SnapshotIdentity(
        date(2026, 8, 17), 'sector', '\u534a\u5bfc\u4f53', 'sector_opportunity', 'v1', 'hash', SnapshotMode.BACKFILL,
    )
    assert _identity_values(identity) == (
        date(2026, 8, 17), 'sector', '\u534a\u5bfc\u4f53', 'sector_opportunity', 'v1', 'hash', 'backfill',
    )

def test_snapshot_store_serializes_mysql_decimal_and_dates_in_feature_json(monkeypatch) -> None:
    captured = {}
    store = MySQLSnapshotStore()
    monkeypatch.setattr(store, '_execute', lambda sql, params: captured.update(params=params))
    snapshot = CandidateSnapshot(
        as_of_date=date(2026, 8, 18), entity_type='etf', entity_code='510300.SH',
        sector_level=2, sector_name='semiconductor', strategy_type='etf_core', candidate_status='blocked',
        candidate_score=None, model_version='v1', config_hash='hash', run_id='run',
        snapshot_mode=SnapshotMode.BACKFILL,
        feature_json={'mapping': {'beta': Decimal('1.10'), 'price_as_of_date': date(2026, 8, 18)}},
    )

    store.insert(snapshot)

    assert captured['params'][15] is None
    assert json.loads(captured['params'][16]) == {
        'mapping': {'beta': '1.10', 'price_as_of_date': '2026-08-18'}
    }


def test_snapshot_store_persists_rank_in_sector(monkeypatch) -> None:
    captured = {}
    store = MySQLSnapshotStore()
    monkeypatch.setattr(store, '_execute', lambda sql, params: captured.update(params=params))
    snapshot = CandidateSnapshot(
        as_of_date=date(2026, 8, 18), entity_type='stock', entity_code='600000',
        sector_level=1, sector_name='Bank', strategy_type='stock_trend',
        candidate_status='trend_leader', candidate_score=0.5, model_version='stock_trend_v1',
        config_hash='hash', run_id='run', snapshot_mode=SnapshotMode.LIVE_SHADOW,
        rank_in_sector=3,
    )

    store.insert(snapshot)
    assert captured['params'][15] == 3


def test_snapshot_insert_includes_availability_columns(monkeypatch) -> None:
    captured = {}
    store = MySQLSnapshotStore()
    monkeypatch.setattr(store, '_execute', lambda sql, params: captured.update(sql=sql, params=params))
    ready_at = datetime(2026, 8, 24, 18, 0)
    run_at = datetime(2026, 8, 25, 9, 10)
    eligible_at = datetime(2026, 8, 25, 9, 30)
    snapshot = CandidateSnapshot(
        as_of_date=date(2026, 8, 24), entity_type='etf', entity_code='510300.SH',
        sector_level=2, sector_name='semiconductor', strategy_type='etf_core', candidate_status='candidate',
        candidate_score=0.5, model_version='v1', config_hash='hash', run_id='run',
        snapshot_mode=SnapshotMode.DELAYED_SHADOW, data_available_at=ready_at, run_at=run_at,
        execution_eligible_at=eligible_at, availability_basis=AvailabilityBasis.MARKET_CLOSE_1800,
    )

    store.insert(snapshot)

    assert 'data_available_at' in captured['sql']
    assert captured['params'][-4:] == (ready_at, run_at, eligible_at, 'market_close_1800')


def test_availability_migration_adds_nullable_columns_only() -> None:
    ddl = Path('sql/20260825_add_research_snapshot_availability.sql').read_text(encoding='utf-8')

    assert 'ADD COLUMN data_available_at DATETIME NULL' in ddl
    assert 'ADD COLUMN run_at DATETIME NULL' in ddl
    assert 'ADD COLUMN execution_eligible_at DATETIME NULL' in ddl
    assert 'ADD COLUMN availability_basis VARCHAR(32) NULL' in ddl
    assert 'UPDATE research_candidate_snapshot' not in ddl


def test_store_schema_ensure_applies_availability_migration(monkeypatch) -> None:
    calls: list[str] = []
    store = MySQLSnapshotStore()
    monkeypatch.setattr(store, '_execute', lambda sql, _params: calls.append(sql))
    monkeypatch.setattr(store, '_ensure_availability_schema', lambda: calls.append('availability'), raising=False)

    store.ensure_schema()

    assert calls == [RESEARCH_SNAPSHOT_DDL, 'availability']


def test_snapshot_read_converts_availability_metadata_from_mysql_values() -> None:
    snapshot = _snapshot_from_row({
        'id': 1, 'as_of_date': '2026-08-24', 'entity_type': 'etf', 'entity_code': '510300.SH',
        'sector_level': 2, 'sector_name': 'semiconductor', 'strategy_type': 'etf_core',
        'candidate_status': 'candidate', 'candidate_score': 0.5, 'research_status': 'shadow',
        'validation_status': 'not_evaluated', 'execution_status': 'manual_only', 'model_version': 'v1',
        'config_hash': 'hash', 'run_id': 'run', 'snapshot_mode': 'delayed_shadow', 'rank_in_sector': 1,
        'feature_json': '{}', 'reasons_json': '[]', 'risk_flags_json': '[]',
        'data_available_at': '2026-08-24 18:00:00', 'run_at': '2026-08-25 09:10:00',
        'execution_eligible_at': '2026-08-25 09:30:00', 'availability_basis': 'market_close_1800',
    })

    assert snapshot.data_available_at == datetime(2026, 8, 24, 18, 0)
    assert snapshot.run_at == datetime(2026, 8, 25, 9, 10)
    assert snapshot.execution_eligible_at == datetime(2026, 8, 25, 9, 30)
    assert snapshot.availability_basis is AvailabilityBasis.MARKET_CLOSE_1800

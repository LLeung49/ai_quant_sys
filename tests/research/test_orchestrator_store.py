import json
from datetime import date
from decimal import Decimal

from morning_conference.sector_rotation2.research.contracts import CandidateSnapshot, SnapshotIdentity
from morning_conference.sector_rotation2.research.orchestrator.store import RESEARCH_SNAPSHOT_DDL, MySQLSnapshotStore, _identity_values
from morning_conference.sector_rotation2.research.status import SnapshotMode


def test_research_snapshot_schema_keeps_live_identity_immutable() -> None:
    normalized = " ".join(RESEARCH_SNAPSHOT_DDL.lower().split())
    assert "create table if not exists research_candidate_snapshot" in normalized
    assert "snapshot_mode varchar(16) not null" in normalized
    assert "unique key uk_research_snapshot_identity" in normalized
    assert "as_of_date, entity_type, entity_code, strategy_type, model_version, config_hash, snapshot_mode" in normalized
    assert "on duplicate key update" not in normalized


def test_identity_values_are_bindable_for_mysql_lookup() -> None:
    identity = SnapshotIdentity(
        date(2026, 8, 17), "sector", "半导体", "sector_opportunity", "v1", "hash", SnapshotMode.BACKFILL,
    )
    assert _identity_values(identity) == (
        date(2026, 8, 17), "sector", "半导体", "sector_opportunity", "v1", "hash", "backfill",
    )

def test_snapshot_store_serializes_mysql_decimal_and_dates_in_feature_json(monkeypatch) -> None:
    captured = {}
    store = MySQLSnapshotStore()
    monkeypatch.setattr(store, "_execute", lambda sql, params: captured.update(params=params))
    snapshot = CandidateSnapshot(
        as_of_date=date(2026, 8, 18), entity_type="etf", entity_code="510300.SH",
        sector_level=2, sector_name="semiconductor", strategy_type="etf_core", candidate_status="blocked",
        candidate_score=None, model_version="v1", config_hash="hash", run_id="run",
        snapshot_mode=SnapshotMode.BACKFILL,
        feature_json={"mapping": {"beta": Decimal("1.10"), "price_as_of_date": date(2026, 8, 18)}},
    )

    store.insert(snapshot)

    assert json.loads(captured["params"][15]) == {
        "mapping": {"beta": "1.10", "price_as_of_date": "2026-08-18"}
    }

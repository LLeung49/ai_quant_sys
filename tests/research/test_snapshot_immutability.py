from dataclasses import replace
from datetime import date

import pytest

from morning_conference.sector_rotation2.research.contracts import CandidateSnapshot
from morning_conference.sector_rotation2.research.snapshot import (
    InMemorySnapshotStore,
    SnapshotConflictError,
    persist_backfill_snapshot,
    persist_live_shadow_snapshot,
)
from morning_conference.sector_rotation2.research.status import SnapshotMode


def make_snapshot(**changes: object) -> CandidateSnapshot:
    values = dict(as_of_date=date(2026, 8, 17), entity_type="etf", entity_code="512480.SH", sector_level=1,
        sector_name="半导体", strategy_type="etf_core", candidate_status="ready", candidate_score=0.8,
        model_version="v1", config_hash="abc", run_id="run-1")
    values.update(changes)
    return CandidateSnapshot(**values)


def test_same_live_shadow_payload_is_idempotent() -> None:
    store, snapshot = InMemorySnapshotStore(), make_snapshot()
    persist_live_shadow_snapshot(store, snapshot)
    persist_live_shadow_snapshot(store, snapshot)
    assert store.count(snapshot.identity) == 1


def test_changed_payload_cannot_overwrite_same_live_shadow_identity() -> None:
    store, snapshot = InMemorySnapshotStore(), make_snapshot()
    persist_live_shadow_snapshot(store, snapshot)
    with pytest.raises(SnapshotConflictError):
        persist_live_shadow_snapshot(store, replace(snapshot, candidate_score=0.99))


def test_same_snapshot_with_a_new_run_id_is_idempotent() -> None:
    store, snapshot = InMemorySnapshotStore(), make_snapshot()
    persist_live_shadow_snapshot(store, snapshot)
    persist_live_shadow_snapshot(store, replace(snapshot, run_id="run-2"))
    assert store.count(snapshot.identity) == 1

    backfill_store = InMemorySnapshotStore()
    persist_backfill_snapshot(backfill_store, snapshot)
    persist_backfill_snapshot(backfill_store, replace(snapshot, run_id="run-2"))
    assert backfill_store.count() == 1


def test_backfill_can_coexist_with_live_shadow() -> None:
    store, snapshot = InMemorySnapshotStore(), make_snapshot()
    persist_live_shadow_snapshot(store, snapshot)
    backfill = persist_backfill_snapshot(store, snapshot)
    assert backfill.snapshot_mode is SnapshotMode.BACKFILL
    assert store.count() == 2

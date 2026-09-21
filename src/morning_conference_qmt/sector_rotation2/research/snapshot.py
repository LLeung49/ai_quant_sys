"""Immutable persistence semantics for research candidate snapshots."""

from dataclasses import replace
from typing import Protocol

from .contracts import CandidateSnapshot, SnapshotIdentity
from .status import SnapshotMode


class SnapshotConflictError(ValueError):
    """Raised when a LIVE_SHADOW identity is reused with different content."""


class SnapshotStore(Protocol):
    def get(self, identity: SnapshotIdentity) -> CandidateSnapshot | None: ...

    def insert(self, snapshot: CandidateSnapshot) -> None: ...


class InMemorySnapshotStore:
    """Small deterministic adapter used by unit tests and local dry-runs."""

    def __init__(self) -> None:
        self._snapshots: dict[SnapshotIdentity, CandidateSnapshot] = {}

    def get(self, identity: SnapshotIdentity) -> CandidateSnapshot | None:
        return self._snapshots.get(identity)

    def insert(self, snapshot: CandidateSnapshot) -> None:
        self._snapshots[snapshot.identity] = snapshot

    def count(self, identity: SnapshotIdentity | None = None) -> int:
        return int(identity in self._snapshots) if identity is not None else len(self._snapshots)


def assert_snapshot_compatible(existing: CandidateSnapshot, incoming: CandidateSnapshot) -> None:
    # ``run_id`` and ``snapshot_id`` identify persistence/audit records, not
    # immutable model output.  A re-run constructs a snapshot before MySQL has
    # assigned its surrogate id, so comparing a stored id against ``None``
    # would incorrectly turn an idempotent retry into a semantic conflict.
    # Re-running identical inputs must remain an idempotent no-op.
    if replace(existing, run_id=incoming.run_id, snapshot_id=incoming.snapshot_id) != incoming:
        raise SnapshotConflictError(f"immutable snapshot conflict for {incoming.identity}")


def persist_live_shadow_snapshot(store: SnapshotStore, snapshot: CandidateSnapshot) -> CandidateSnapshot:
    if snapshot.snapshot_mode is not SnapshotMode.LIVE_SHADOW:
        raise ValueError("persist_live_shadow_snapshot requires LIVE_SHADOW mode")
    existing = store.get(snapshot.identity)
    if existing is None:
        store.insert(snapshot)
    else:
        assert_snapshot_compatible(existing, snapshot)
    return snapshot


def persist_backfill_snapshot(store: SnapshotStore, snapshot: CandidateSnapshot) -> CandidateSnapshot:
    backfill = replace(snapshot, snapshot_mode=SnapshotMode.BACKFILL)
    existing = store.get(backfill.identity)
    if existing is None:
        store.insert(backfill)
    else:
        assert_snapshot_compatible(existing, backfill)
    return backfill


def persist_delayed_shadow_snapshot(store: SnapshotStore, snapshot: CandidateSnapshot) -> CandidateSnapshot:
    """Persist an immutable operational delayed-shadow snapshot."""
    if snapshot.snapshot_mode is not SnapshotMode.DELAYED_SHADOW:
        raise ValueError("persist_delayed_shadow_snapshot requires DELAYED_SHADOW mode")
    existing = store.get(snapshot.identity)
    if existing is None:
        store.insert(snapshot)
    else:
        assert_snapshot_compatible(existing, snapshot)
    return snapshot


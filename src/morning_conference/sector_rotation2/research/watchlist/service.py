from __future__ import annotations

from typing import Any

from data_ingestion.db_config import execute_query, execute_update

from .schema import WATCHLIST_DDL

WATCH_STATUSES = frozenset({"watch", "paused", "done"})


def ensure_schema() -> None:
    execute_update(WATCHLIST_DDL)


def _snapshot(snapshot_id: int) -> dict[str, Any] | None:
    rows = execute_query(
        "SELECT id,entity_type,entity_code,strategy_type,as_of_date,model_version,config_hash,snapshot_mode "
        "FROM research_candidate_snapshot WHERE id=%s", (snapshot_id,),
    )
    return dict(rows[0]) if rows else None


def add(*, user_id: str, snapshot_id: int, note: str | None = None, watch_status: str = "watch") -> dict[str, Any]:
    if watch_status not in WATCH_STATUSES:
        raise ValueError("invalid watch_status")
    source = _snapshot(snapshot_id)
    if source is None:
        raise LookupError("snapshot not found")
    ensure_schema()
    execute_update(
        "INSERT INTO research_watchlist (user_id,snapshot_id,entity_type,entity_code,strategy_type,as_of_date,model_version,config_hash,snapshot_mode,watch_status,note) "
        "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE watch_status=VALUES(watch_status),note=VALUES(note)",
        (user_id, snapshot_id, source["entity_type"], source["entity_code"], source["strategy_type"], source["as_of_date"], source["model_version"], source["config_hash"], source["snapshot_mode"], watch_status, note),
    )
    return get(user_id=user_id, snapshot_id=snapshot_id) or {}


def update(*, user_id: str, snapshot_id: int, note: str | None = None, watch_status: str | None = None) -> dict[str, Any]:
    changes: list[str] = []
    params: list[Any] = []
    if note is not None: changes.append("note=%s"); params.append(note)
    if watch_status is not None:
        if watch_status not in WATCH_STATUSES: raise ValueError("invalid watch_status")
        changes.append("watch_status=%s"); params.append(watch_status)
    if not changes: return get(user_id=user_id, snapshot_id=snapshot_id) or {}
    params.extend([user_id, snapshot_id])
    execute_update(f"UPDATE research_watchlist SET {', '.join(changes)} WHERE user_id=%s AND snapshot_id=%s", tuple(params))
    return get(user_id=user_id, snapshot_id=snapshot_id) or {}


def remove(*, user_id: str, snapshot_id: int) -> None:
    execute_update("DELETE FROM research_watchlist WHERE user_id=%s AND snapshot_id=%s", (user_id, snapshot_id))


def get(*, user_id: str, snapshot_id: int) -> dict[str, Any] | None:
    rows = execute_query("SELECT * FROM research_watchlist WHERE user_id=%s AND snapshot_id=%s", (user_id, snapshot_id))
    return dict(rows[0]) if rows else None


def list_items(*, user_id: str) -> list[dict[str, Any]]:
    return [dict(row) for row in execute_query("SELECT * FROM research_watchlist WHERE user_id=%s ORDER BY updated_at DESC,id DESC", (user_id,))]

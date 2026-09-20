from __future__ import annotations

from typing import Any

from data_ingestion_qmt.db_config import execute_query, execute_update

from .schema import DECISION_DDL

DECISIONS = frozenset({"WATCH", "ENTER", "SKIP", "EXIT"})


def ensure_schema() -> None:
    execute_update(DECISION_DDL)


def append(*, user_id: str, snapshot_id: int, decision: str, note: str | None = None) -> dict[str, Any]:
    decision = decision.upper()
    if decision not in DECISIONS: raise ValueError("invalid decision")
    rows = execute_query("SELECT id,entity_type,entity_code,strategy_type,as_of_date,model_version,config_hash,snapshot_mode FROM research_candidate_snapshot WHERE id=%s", (snapshot_id,))
    if not rows: raise LookupError("snapshot not found")
    source = dict(rows[0])
    ensure_schema()
    execute_update(
        "INSERT INTO research_human_decision (user_id,snapshot_id,entity_type,entity_code,strategy_type,as_of_date,model_version,config_hash,snapshot_mode,decision,note) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        (user_id, snapshot_id, source["entity_type"], source["entity_code"], source["strategy_type"], source["as_of_date"], source["model_version"], source["config_hash"], source["snapshot_mode"], decision, note),
    )
    return dict(execute_query("SELECT * FROM research_human_decision WHERE user_id=%s AND snapshot_id=%s ORDER BY id DESC LIMIT 1", (user_id, snapshot_id))[0])


def list_items(*, user_id: str, snapshot_id: int | None = None) -> list[dict[str, Any]]:
    if snapshot_id is None:
        rows = execute_query("SELECT * FROM research_human_decision WHERE user_id=%s ORDER BY created_at DESC,id DESC", (user_id,))
    else:
        rows = execute_query("SELECT * FROM research_human_decision WHERE user_id=%s AND snapshot_id=%s ORDER BY created_at DESC,id DESC", (user_id, snapshot_id))
    return [dict(row) for row in rows]


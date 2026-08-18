"""Persistence boundary for immutable Research Cockpit snapshots."""

import json
from datetime import date
from typing import Any, Callable

import pymysql

from data_ingestion.db_config import get_connection

from ..contracts import CandidateSnapshot, SnapshotIdentity
from ..snapshot import SnapshotStore, persist_backfill_snapshot, persist_live_shadow_snapshot
from ..status import SnapshotMode


RESEARCH_SNAPSHOT_DDL = """
CREATE TABLE IF NOT EXISTS research_candidate_snapshot (
    id BIGINT NOT NULL AUTO_INCREMENT,
    as_of_date DATE NOT NULL,
    entity_type VARCHAR(32) NOT NULL,
    entity_code VARCHAR(128) NOT NULL,
    sector_level TINYINT NULL,
    sector_name VARCHAR(128) NULL,
    strategy_type VARCHAR(64) NOT NULL,
    candidate_status VARCHAR(32) NOT NULL,
    candidate_score DOUBLE NULL,
    research_status VARCHAR(32) NOT NULL,
    validation_status VARCHAR(32) NOT NULL,
    execution_status VARCHAR(32) NOT NULL,
    model_version VARCHAR(64) NOT NULL,
    config_hash VARCHAR(64) NOT NULL,
    run_id VARCHAR(64) NOT NULL,
    snapshot_mode VARCHAR(16) NOT NULL,
    feature_json JSON NOT NULL,
    reasons_json JSON NOT NULL,
    risk_flags_json JSON NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY uk_research_snapshot_identity (
        as_of_date, entity_type, entity_code, strategy_type, model_version, config_hash, snapshot_mode
    )
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
"""


class MySQLSnapshotStore:
    """MySQL adapter that deliberately never performs an upsert."""

    def __init__(self, connection_factory: Callable[[], Any] = get_connection) -> None:
        self._connection_factory = connection_factory

    def ensure_schema(self) -> None:
        self._execute(RESEARCH_SNAPSHOT_DDL, ())

    def get(self, identity: SnapshotIdentity) -> CandidateSnapshot | None:
        connection = self._connection_factory()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        try:
            cursor.execute(
                """SELECT * FROM research_candidate_snapshot
                   WHERE as_of_date=%s AND entity_type=%s AND entity_code=%s AND strategy_type=%s
                     AND model_version=%s AND config_hash=%s AND snapshot_mode=%s""",
                (*_identity_values(identity),),
            )
            row = cursor.fetchone()
            return _snapshot_from_row(row) if row else None
        finally:
            cursor.close()
            connection.close()

    def insert(self, snapshot: CandidateSnapshot) -> None:
        values = (
            snapshot.as_of_date, snapshot.entity_type, snapshot.entity_code, snapshot.sector_level, snapshot.sector_name,
            snapshot.strategy_type, snapshot.candidate_status, snapshot.candidate_score, snapshot.research_status.value,
            snapshot.validation_status.value, snapshot.execution_status.value, snapshot.model_version, snapshot.config_hash,
            snapshot.run_id, snapshot.snapshot_mode.value, json.dumps(dict(snapshot.feature_json), ensure_ascii=False),
            json.dumps(snapshot.reasons_json, ensure_ascii=False), json.dumps(snapshot.risk_flags_json, ensure_ascii=False),
        )
        self._execute(
            """INSERT INTO research_candidate_snapshot
               (as_of_date, entity_type, entity_code, sector_level, sector_name, strategy_type, candidate_status,
                candidate_score, research_status, validation_status, execution_status, model_version, config_hash,
                run_id, snapshot_mode, feature_json, reasons_json, risk_flags_json)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
            values,
        )

    def _execute(self, sql: str, params: tuple[Any, ...]) -> None:
        connection = self._connection_factory()
        cursor = connection.cursor()
        try:
            cursor.execute(sql, params)
            connection.commit()
        except Exception:
            connection.rollback()
            raise
        finally:
            cursor.close()
            connection.close()


def _identity_values(identity: SnapshotIdentity) -> tuple[object, ...]:
    return (*identity.__dict__.values()[:-1], identity.snapshot_mode.value)


def _snapshot_from_row(row: dict[str, Any]) -> CandidateSnapshot:
    from ..status import ExecutionStatus, ResearchStatus, ValidationStatus

    return CandidateSnapshot(
        as_of_date=row["as_of_date"] if isinstance(row["as_of_date"], date) else date.fromisoformat(str(row["as_of_date"])),
        entity_type=row["entity_type"], entity_code=row["entity_code"], sector_level=row["sector_level"],
        sector_name=row["sector_name"], strategy_type=row["strategy_type"], candidate_status=row["candidate_status"],
        candidate_score=row["candidate_score"], research_status=ResearchStatus(row["research_status"]),
        validation_status=ValidationStatus(row["validation_status"]), execution_status=ExecutionStatus(row["execution_status"]),
        model_version=row["model_version"], config_hash=row["config_hash"], run_id=row["run_id"],
        snapshot_mode=SnapshotMode(row["snapshot_mode"]), feature_json=json.loads(row["feature_json"]),
        reasons_json=tuple(json.loads(row["reasons_json"])), risk_flags_json=tuple(json.loads(row["risk_flags_json"])),
    )


def persist_sector_opportunity(store: SnapshotStore, snapshot: CandidateSnapshot) -> CandidateSnapshot:
    if snapshot.snapshot_mode is SnapshotMode.LIVE_SHADOW:
        return persist_live_shadow_snapshot(store, snapshot)
    if snapshot.snapshot_mode is SnapshotMode.BACKFILL:
        return persist_backfill_snapshot(store, snapshot)
    raise ValueError("Sector Opportunity only supports LIVE_SHADOW or BACKFILL snapshots")

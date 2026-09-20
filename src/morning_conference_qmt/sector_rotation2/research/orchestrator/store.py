"""Persistence boundary for immutable Research Cockpit snapshots."""

import json
from datetime import date, datetime
from decimal import Decimal
from typing import Any, Callable

import numpy as np
import pymysql

from data_ingestion_qmt.db_config import get_connection

from ..availability import AvailabilityBasis
from ..contracts import CandidateSnapshot, SnapshotIdentity
from ..snapshot import (
    SnapshotStore, persist_backfill_snapshot, persist_delayed_shadow_snapshot,
    persist_live_shadow_snapshot,
)
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
    data_available_at DATETIME NULL,
    run_at DATETIME NULL,
    execution_eligible_at DATETIME NULL,
    availability_basis VARCHAR(32) NULL,
    rank_in_sector INT NULL,
    feature_json JSON NOT NULL,
    reasons_json JSON NOT NULL,
    risk_flags_json JSON NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY uk_research_snapshot_identity (
        as_of_date, entity_type, entity_code, strategy_type, model_version, config_hash, snapshot_mode
    ),
    KEY idx_research_rank (
        as_of_date, sector_level, sector_name, strategy_type, rank_in_sector
    ),
    KEY idx_research_snapshot_execution (snapshot_mode, execution_eligible_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
"""


def _coerce_jsonable(value: object) -> object:
    """Recursively convert pandas/numpy scalars and NaN to JSON-safe values.

    - ``np.True_`` / ``np.False_`` -> ``True`` / ``False``
    - ``np.integer`` -> ``int``
    - ``np.floating`` -> ``float`` (``NaN`` / ``+inf`` / ``-inf`` -> ``None``)
    - ``np.ndarray`` -> ``list(value)``
    - ``pandas.Timestamp`` -> ``datetime``
    - ``pandas.NaT`` / ``NaTType`` -> ``None``  (must precede the date/datetime
      branch because ``NaTType`` inherits from ``datetime``)
    - ``pandas Series`` -> ``list(...)``
    - ``dict`` / ``list`` / ``tuple`` -> recursively coerced
    - ``None`` and other primitives pass through.
    """

    if value is None:
        return None
    if isinstance(value, (str, bool, int, Decimal)):
        return value
    if isinstance(value, float):
        return value if np.isfinite(value) else None
    # NaTType must be checked before ``isinstance(value, (date, datetime))``
    # because it inherits from ``datetime``.  The type-name check below also
    # catches subclasses in older pandas versions.
    if type(value).__name__ == "NaTType":
        return None
    if isinstance(value, (date, datetime)):
        return value
    if isinstance(value, np.bool_):
        return bool(value)
    if isinstance(value, np.integer):
        return int(value)
    if isinstance(value, np.floating):
        f = float(value)
        return f if np.isfinite(f) else None
    if isinstance(value, np.ndarray):
        return [_coerce_jsonable(item) for item in value.tolist()]
    if isinstance(value, dict):
        return {str(key): _coerce_jsonable(item) for key, item in value.items()}
    if isinstance(value, (list, tuple, set, frozenset)):
        return [_coerce_jsonable(item) for item in value]
    type_name = type(value).__name__
    if type_name == "Timestamp":
        try:
            ts = value.to_pydatetime()
            return ts if ts is not pd_NaT else None
        except (TypeError, ValueError):
            return None
    if type_name == "Series":
        try:
            return [_coerce_jsonable(item) for item in value.tolist()]
        except (TypeError, ValueError):
            return None
    return value


pd_NaT = object()  # sentinel used by the Timestamp branch above


def _json_default(value: object) -> Any:
    """JSON default hook: safely stringify exotic scalars that survived coercion."""

    if isinstance(value, Decimal):
        return str(value)
    if isinstance(value, (datetime, date)):
        return value.isoformat()
    coerced = _coerce_jsonable(value)
    if isinstance(coerced, float) and not np.isfinite(coerced):
        return None
    return coerced


class MySQLSnapshotStore:
    """MySQL adapter that deliberately never performs an upsert."""

    def __init__(self, connection_factory: Callable[[], Any] = get_connection) -> None:
        self._connection_factory = connection_factory

    def ensure_schema(self) -> None:
        self._execute(RESEARCH_SNAPSHOT_DDL, ())
        self._ensure_availability_schema()

    def _ensure_availability_schema(self) -> None:
        """Add availability metadata to existing snapshot tables, idempotently."""
        connection = self._connection_factory()
        cursor = connection.cursor()
        try:
            cursor.execute(
                "SELECT column_name FROM information_schema.columns "
                "WHERE table_schema=DATABASE() AND table_name='research_candidate_snapshot'"
            )
            columns = {row[0] for row in cursor.fetchall()}
            additions = (
                ("data_available_at", "DATETIME NULL"),
                ("run_at", "DATETIME NULL"),
                ("execution_eligible_at", "DATETIME NULL"),
                ("availability_basis", "VARCHAR(32) NULL"),
            )
            for name, definition in additions:
                if name not in columns:
                    cursor.execute(f"ALTER TABLE research_candidate_snapshot ADD COLUMN {name} {definition}")
            cursor.execute(
                "SELECT 1 FROM information_schema.statistics WHERE table_schema=DATABASE() "
                "AND table_name='research_candidate_snapshot' AND index_name='idx_research_snapshot_execution'"
            )
            if cursor.fetchone() is None:
                cursor.execute(
                    "ALTER TABLE research_candidate_snapshot ADD KEY "
                    "idx_research_snapshot_execution (snapshot_mode, execution_eligible_at)"
                )
            connection.commit()
        except Exception:
            connection.rollback()
            raise
        finally:
            cursor.close()
            connection.close()

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
            snapshot.run_id, snapshot.snapshot_mode.value, snapshot.rank_in_sector,
            _json_dump(snapshot.feature_json),
            _json_dump(snapshot.reasons_json), _json_dump(snapshot.risk_flags_json),
            snapshot.data_available_at, snapshot.run_at, snapshot.execution_eligible_at,
            snapshot.availability_basis.value if snapshot.availability_basis is not None else None,
        )
        self._execute(
            """INSERT INTO research_candidate_snapshot
               (as_of_date, entity_type, entity_code, sector_level, sector_name, strategy_type, candidate_status,
                candidate_score, research_status, validation_status, execution_status, model_version, config_hash,
                run_id, snapshot_mode, rank_in_sector, feature_json, reasons_json, risk_flags_json,
                data_available_at, run_at, execution_eligible_at, availability_basis)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                       %s, %s, %s, %s)""",
            values,
        )

    def _execute(self, sql: str, params: tuple) -> None:
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
    return (
        identity.as_of_date,
        identity.entity_type,
        identity.entity_code,
        identity.strategy_type,
        identity.model_version,
        identity.config_hash,
        identity.snapshot_mode.value,
    )


def _json_dump(value: object) -> str:
    """Serialize snapshot provenance to a JSON string MySQL accepts.

    Runs ``_coerce_jsonable`` once to handle pandas/numpy scalars and
    NaN/Inf values that ``json.dumps`` would otherwise emit as the invalid
    tokens ``NaN``/``Infinity`` (rejected by MySQL strict mode).  Falls
    back to ``_json_default`` for any value type that survived coercion but
    is still unknown to the encoder (e.g. ``Decimal``).
    """

    return json.dumps(
        _coerce_jsonable(value),
        ensure_ascii=False,
        allow_nan=False,
        default=_json_default,
    )


def _snapshot_from_row(row: dict[str, Any]) -> CandidateSnapshot:
    from ..status import ExecutionStatus, ResearchStatus, ValidationStatus

    return CandidateSnapshot(
        snapshot_id=row.get("id"),
        as_of_date=row["as_of_date"] if isinstance(row["as_of_date"], date) else date.fromisoformat(str(row["as_of_date"])),
        entity_type=row["entity_type"], entity_code=row["entity_code"], sector_level=row["sector_level"],
        sector_name=row["sector_name"], strategy_type=row["strategy_type"], candidate_status=row["candidate_status"],
        candidate_score=row["candidate_score"], research_status=ResearchStatus(row["research_status"]),
        validation_status=ValidationStatus(row["validation_status"]), execution_status=ExecutionStatus(row["execution_status"]),
        model_version=row["model_version"], config_hash=row["config_hash"], run_id=row["run_id"],
        snapshot_mode=SnapshotMode(row["snapshot_mode"]), feature_json=_json_load(row["feature_json"]),
        reasons_json=tuple(_json_load(row["reasons_json"])), risk_flags_json=tuple(_json_load(row["risk_flags_json"])),
        rank_in_sector=row.get("rank_in_sector"),
        data_available_at=_datetime_from_row(row.get("data_available_at")),
        run_at=_datetime_from_row(row.get("run_at")),
        execution_eligible_at=_datetime_from_row(row.get("execution_eligible_at")),
        availability_basis=(AvailabilityBasis(row["availability_basis"]) if row.get("availability_basis") else None),
    )


def _json_load(value: Any) -> Any:
    """Accept both pymysql JSON strings and drivers returning decoded values."""
    return json.loads(value) if isinstance(value, (str, bytes, bytearray)) else value


def _datetime_from_row(value: Any) -> datetime | None:
    if value is None or isinstance(value, datetime):
        return value
    return datetime.fromisoformat(str(value))


def persist_sector_opportunity(store: SnapshotStore, snapshot: CandidateSnapshot) -> CandidateSnapshot:
    if snapshot.snapshot_mode is SnapshotMode.LIVE_SHADOW:
        return persist_live_shadow_snapshot(store, snapshot)
    if snapshot.snapshot_mode is SnapshotMode.BACKFILL:
        return persist_backfill_snapshot(store, snapshot)
    if snapshot.snapshot_mode is SnapshotMode.DELAYED_SHADOW:
        return persist_delayed_shadow_snapshot(store, snapshot)
    raise ValueError("Sector Opportunity only supports LIVE_SHADOW or BACKFILL (or DELAYED_SHADOW) snapshots")


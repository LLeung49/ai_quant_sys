"""Atomic, effective-dated mappings derived from ETF constituent exposure."""

from __future__ import annotations

from collections.abc import Callable, Iterable
from contextlib import AbstractContextManager, contextmanager
from datetime import date
from typing import Any, Literal, Protocol

from data_ingestion.db_config import execute_query, execute_update, get_connection

from .exposure import ExposureAssessment, ExposureResult, RejectedExposure


CURRENT_MAPPING_MODE = "current_mapping"
MAPPING_TYPE_EXPOSURE_DERIVED = "exposure_derived"
MAPPING_TYPE_QUALITY_FAILURE = "exposure_quality_failure"
QUALITY_STATUS_QUALIFIED = "qualified"
QUALITY_STATUS_FAILED = "failed"
_FAILURE_ETF_CODE = "__NO_QUALIFIED_ETF__"

SECTOR_ETF_MAP_DDL = """
CREATE TABLE IF NOT EXISTS trade_sector_etf_map (
    id BIGINT NOT NULL AUTO_INCREMENT,
    sector_level TINYINT NOT NULL,
    sector_name VARCHAR(128) NOT NULL,
    etf_code VARCHAR(32) NOT NULL,
    mapping_type VARCHAR(32) NOT NULL,
    is_primary TINYINT NOT NULL DEFAULT 0,
    effective_from DATE NOT NULL,
    effective_to DATE DEFAULT NULL,
    source_as_of_date DATE NOT NULL,
    source_provider VARCHAR(64) NOT NULL,
    exposure_weight DECIMAL(18,8) NOT NULL,
    coverage_ratio DECIMAL(18,8) NOT NULL,
    mapping_version VARCHAR(64) NOT NULL,
    config_hash VARCHAR(128) NOT NULL,
    rank_no TINYINT NOT NULL,
    weight_unit ENUM('decimal', 'percent') NOT NULL,
    membership_asof_mode VARCHAR(32) NOT NULL,
    membership_as_of_date DATE NOT NULL,
    constituent_as_of_date DATE NOT NULL,
    quality_status ENUM('qualified', 'failed') NOT NULL,
    failure_reason VARCHAR(255) DEFAULT NULL,
    mapping_note VARCHAR(255) DEFAULT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY uk_sector_etf_map (sector_level, sector_name, etf_code, mapping_type, effective_from),
    KEY idx_sector_etf_effective (sector_level, sector_name, effective_from, effective_to)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
"""

# Existing deployments can contain manually curated rows.  Added fields stay
# nullable during migration so those legacy rows remain readable/auditable;
# all newly derived rows use the NOT NULL contract from the create DDL above.
_MIGRATION_COLUMNS = {
    "source_as_of_date": "DATE NULL",
    "source_provider": "VARCHAR(64) NULL",
    "exposure_weight": "DECIMAL(18,8) NULL",
    "coverage_ratio": "DECIMAL(18,8) NULL",
    "mapping_version": "VARCHAR(64) NULL",
    "config_hash": "VARCHAR(128) NULL",
    "rank_no": "TINYINT NULL",
    "weight_unit": "VARCHAR(16) NULL",
    "membership_asof_mode": "VARCHAR(32) NULL",
    "membership_as_of_date": "DATE NULL",
    "constituent_as_of_date": "DATE NULL",
    "quality_status": "VARCHAR(16) NULL",
    "failure_reason": "VARCHAR(255) NULL",
    "mapping_note": "VARCHAR(255) NULL",
    "updated_at": "DATETIME NULL",
}

_INSERT_EXPOSURE_MAPPING_SQL = """
INSERT INTO trade_sector_etf_map (
    sector_level, sector_name, etf_code, mapping_type, is_primary,
    effective_from, effective_to, source_as_of_date, source_provider,
    exposure_weight, coverage_ratio, mapping_version, rank_no, config_hash,
    weight_unit, membership_asof_mode, membership_as_of_date,
    constituent_as_of_date, quality_status, failure_reason, mapping_note
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

_LOCK_SECTOR_SQL = """
SELECT id FROM trade_sector_etf_map
WHERE sector_level=%s AND sector_name=%s
  AND mapping_type IN ('exposure_derived', 'exposure_quality_failure')
FOR UPDATE
"""

_DELETE_SAME_DAY_SQL = """
DELETE FROM trade_sector_etf_map
WHERE sector_level=%s AND sector_name=%s AND effective_from=%s
  AND mapping_type IN ('exposure_derived', 'exposure_quality_failure')
"""

# The canonical event rows are the derived mapping/failure records by date.
# Rebuilding end dates after every replacement makes a same-day rerun
# idempotent and also closes the correct interval when a historical date is
# backfilled out of order.
_REBUILD_EFFECTIVE_INTERVALS_SQL = """
UPDATE trade_sector_etf_map AS target
LEFT JOIN (
    SELECT current_event.effective_from,
           MIN(next_event.effective_from) AS next_effective_from
    FROM (
        SELECT DISTINCT effective_from
        FROM trade_sector_etf_map
        WHERE sector_level=%s AND sector_name=%s
          AND mapping_type IN ('exposure_derived', 'exposure_quality_failure')
    ) AS current_event
    LEFT JOIN trade_sector_etf_map AS next_event
      ON next_event.sector_level=%s AND next_event.sector_name=%s
     AND next_event.effective_from > current_event.effective_from
     AND next_event.mapping_type IN ('exposure_derived', 'exposure_quality_failure')
    GROUP BY current_event.effective_from
) AS intervals ON intervals.effective_from=target.effective_from
SET target.effective_to=CASE
    WHEN intervals.next_effective_from IS NULL THEN NULL
    ELSE DATE_SUB(intervals.next_effective_from, INTERVAL 1 DAY)
END
WHERE target.sector_level=%s AND target.sector_name=%s
  AND target.mapping_type IN ('exposure_derived', 'exposure_quality_failure')
"""


class MappingTransaction(Protocol):
    """Minimal transaction boundary required by mapping persistence."""

    def execute(self, sql: str, params: tuple[object, ...] = ()) -> int: ...

    def execute_many(self, sql: str, rows: list[tuple[object, ...]]) -> int: ...


class _CursorTransaction:
    def __init__(self, cursor: Any) -> None:
        self._cursor = cursor

    def execute(self, sql: str, params: tuple[object, ...] = ()) -> int:
        self._cursor.execute(sql, params)
        return int(self._cursor.rowcount)

    def execute_many(self, sql: str, rows: list[tuple[object, ...]]) -> int:
        self._cursor.executemany(sql, rows)
        return int(self._cursor.rowcount)


@contextmanager
def open_mapping_transaction() -> Iterable[MappingTransaction]:
    """Yield one connection and commit or roll back all mapping mutations."""

    connection = get_connection()
    cursor = connection.cursor()
    try:
        yield _CursorTransaction(cursor)
    except Exception:
        connection.rollback()
        raise
    else:
        connection.commit()
    finally:
        cursor.close()
        connection.close()


def ensure_mapping_schema(
    *,
    query: Callable[[str, tuple[object, ...]], list[dict[str, Any]]] = execute_query,
    execute_update: Callable[[str, tuple[object, ...]], int] = execute_update,
) -> None:
    """Explicit writer/startup migration; readers never invoke this function."""

    execute_update(SECTOR_ETF_MAP_DDL, ())
    rows = query(
        """SELECT column_name FROM information_schema.columns
             WHERE table_schema=DATABASE() AND table_name=%s""",
        ("trade_sector_etf_map",),
    )
    existing = {str(row["column_name"]) for row in rows}
    for name, definition in _MIGRATION_COLUMNS.items():
        if name not in existing:
            execute_update(f"ALTER TABLE trade_sector_etf_map ADD COLUMN {name} {definition}", ())
    index_rows = query(
        """SELECT index_name, column_name FROM information_schema.statistics
             WHERE table_schema=DATABASE() AND table_name=%s
             ORDER BY index_name, seq_in_index""",
        ("trade_sector_etf_map",),
    )
    index_columns: dict[str, list[str]] = {}
    for row in index_rows:
        index_columns.setdefault(str(row["index_name"]), []).append(str(row["column_name"]))
    desired_unique_columns = ["sector_level", "sector_name", "etf_code", "mapping_type", "effective_from"]
    old_unique_columns = index_columns.get("uk_sector_etf_map")
    if old_unique_columns != desired_unique_columns:
        if old_unique_columns is not None:
            execute_update(
                """ALTER TABLE trade_sector_etf_map
                   DROP INDEX uk_sector_etf_map,
                   ADD UNIQUE KEY uk_sector_etf_map
                   (sector_level, sector_name, etf_code, mapping_type, effective_from)""",
                (),
            )
        else:
            execute_update(
                """ALTER TABLE trade_sector_etf_map ADD UNIQUE KEY uk_sector_etf_map
                   (sector_level, sector_name, etf_code, mapping_type, effective_from)""",
                (),
            )


def load_sector_member_codes(
    sector_name: str,
    sector_level: int,
    query: Callable[[str, tuple[object, ...]], list[dict[str, Any]]] = execute_query,
) -> list[str]:
    """Return member codes from ``trade_stock_status`` using current_mapping."""

    field = _sector_field(sector_level)
    rows = query(
        f"""SELECT DISTINCT status.stock_code FROM trade_stock_status AS status
              WHERE status.{field} = %s ORDER BY status.stock_code ASC""",
        (sector_name,),
    )
    return [str(row["stock_code"]) for row in rows if row.get("stock_code") is not None]


def persist_exposure_mapping(
    *,
    sector_name: str,
    sector_level: int,
    as_of_date: date,
    ranked: Iterable[ExposureResult],
    source_as_of_date: date,
    source_provider: str,
    membership_as_of_date: date,
    constituent_as_of_date: date,
    mapping_version: str,
    config_hash: str,
    weight_unit: Literal["decimal", "percent"],
    min_coverage: float = 0.80,
    rejected: Iterable[RejectedExposure] = (),
    transaction: Callable[[], AbstractContextManager[MappingTransaction]] = open_mapping_transaction,
    ensure_schema: Callable[[], None] | None = None,
) -> int:
    """Atomically replace one canonical mapping event and rebuild intervals.

    A mapping event represents the whole sector/date, not individual ETF rows.
    Replacing it deletes stale same-day derived rows, inserts either ranked
    qualified ETFs or one explicit failure event, then derives all effective
    end dates for that sector within the same transaction.
    """

    _sector_field(sector_level)
    if not 0 <= min_coverage <= 1:
        raise ValueError("min_coverage must be between zero and one")
    if weight_unit not in {"decimal", "percent"}:
        raise ValueError(f"invalid weight unit: {weight_unit!r}")
    _validate_as_of_dates(source_as_of_date, membership_as_of_date, constituent_as_of_date)

    if ensure_schema is not None:
        ensure_schema()
    ranked_items = list(ranked)
    rejected_items = list(rejected)
    qualified = sorted(
        (
            item for item in ranked_items
            if item.coverage_ratio >= min_coverage and item.exposure_weight > 0
        ),
        key=lambda item: (-item.exposure_weight, -item.coverage_ratio, item.etf_code),
    )[:3]
    rows = _mapping_rows(
        sector_name=sector_name, sector_level=sector_level, as_of_date=as_of_date,
        ranked=qualified, observed=[*ranked_items, *rejected_items], source_as_of_date=source_as_of_date, source_provider=source_provider,
        membership_as_of_date=membership_as_of_date,
        constituent_as_of_date=constituent_as_of_date, mapping_version=mapping_version,
        config_hash=config_hash, weight_unit=weight_unit, min_coverage=min_coverage,
    )
    with transaction() as db:
        db.execute(_LOCK_SECTOR_SQL, (sector_level, sector_name))
        db.execute(_DELETE_SAME_DAY_SQL, (sector_level, sector_name, as_of_date))
        count = db.execute_many(_INSERT_EXPOSURE_MAPPING_SQL, rows)
        db.execute(
            _REBUILD_EFFECTIVE_INTERVALS_SQL,
            (sector_level, sector_name, sector_level, sector_name, sector_level, sector_name),
        )
    return count


def persist_exposure_assessment(
    *,
    assessment: ExposureAssessment,
    **kwargs: Any,
) -> int:
    """Persist an assessment while preserving rejected observations on failure."""

    return persist_exposure_mapping(
        ranked=assessment.eligible,
        rejected=assessment.rejected,
        **kwargs,
    )


def load_effective_etfs(
    sector_name: str,
    sector_level: int,
    as_of_date: date,
    query: Callable[[str, tuple[object, ...]], list[dict[str, Any]]] = execute_query,
    *,
    min_coverage: float = 0.80,
) -> list[dict[str, Any]]:
    """Load at most three qualified, exposure-derived ETFs effective on a date."""

    _sector_field(sector_level)
    if not 0 <= min_coverage <= 1:
        raise ValueError("min_coverage must be between zero and one")
    rows = query(
        """SELECT etf_code, mapping_type, is_primary, effective_from, effective_to,
                  source_as_of_date, source_provider, exposure_weight, coverage_ratio,
                  mapping_version, config_hash, rank_no, weight_unit,
                  membership_asof_mode, membership_as_of_date, constituent_as_of_date,
                  quality_status, failure_reason, mapping_note
             FROM trade_sector_etf_map
             WHERE sector_name=%s AND sector_level=%s AND effective_from <= %s
               AND (effective_to IS NULL OR effective_to >= %s)
               AND mapping_type='exposure_derived' AND quality_status='qualified'
               AND exposure_weight > 0 AND coverage_ratio >= %s
             ORDER BY rank_no ASC, etf_code ASC
             LIMIT 3""",
        (sector_name, sector_level, as_of_date, as_of_date, min_coverage),
    )
    qualified = [
        row for row in rows
        if row.get("mapping_type") == MAPPING_TYPE_EXPOSURE_DERIVED
        and row.get("quality_status") == QUALITY_STATUS_QUALIFIED
        and float(row.get("exposure_weight") or 0) > 0
        and float(row.get("coverage_ratio") or 0) >= min_coverage
    ]
    return sorted(qualified, key=_effective_mapping_sort_key)[:3]


def _mapping_rows(
    *, sector_name: str, sector_level: int, as_of_date: date,
    ranked: list[ExposureResult], observed: list[ExposureResult | RejectedExposure], source_as_of_date: date, source_provider: str,
    membership_as_of_date: date, constituent_as_of_date: date, mapping_version: str,
    config_hash: str, weight_unit: str, min_coverage: float,
) -> list[tuple[object, ...]]:
    if not ranked:
        observed_item = max(observed, key=lambda item: (item.coverage_ratio, item.exposure_weight, item.etf_code), default=None)
        observed_code = observed_item.etf_code if observed_item else _FAILURE_ETF_CODE
        observed_exposure = observed_item.exposure_weight if observed_item else 0.0
        observed_coverage = observed_item.coverage_ratio if observed_item else 0.0
        return [(
            sector_level, sector_name, observed_code, MAPPING_TYPE_QUALITY_FAILURE, 0,
            as_of_date, None, source_as_of_date, source_provider, observed_exposure, observed_coverage,
            mapping_version, 0, config_hash, weight_unit, CURRENT_MAPPING_MODE,
            membership_as_of_date, constituent_as_of_date, QUALITY_STATUS_FAILED,
            _failure_reason(min_coverage, observed_item, observed_code, observed_coverage), None,
        )]
    return [
        (
            sector_level, sector_name, item.etf_code, MAPPING_TYPE_EXPOSURE_DERIVED,
            int(rank_no == 1), as_of_date, None, source_as_of_date, source_provider,
            item.exposure_weight, item.coverage_ratio, mapping_version, rank_no, config_hash,
            weight_unit, CURRENT_MAPPING_MODE, membership_as_of_date, constituent_as_of_date,
            QUALITY_STATUS_QUALIFIED, None, None,
        )
        for rank_no, item in enumerate(ranked, start=1)
    ]


def _sector_field(sector_level: int) -> str:
    if sector_level not in (1, 2):
        raise ValueError("sector_level must be 1 or 2")
    return f"sector_{sector_level}"


def _effective_mapping_sort_key(row: dict[str, Any]) -> tuple[int, str]:
    return (int(row.get("rank_no") or 99), str(row["etf_code"]))


def _validate_as_of_dates(
    source_as_of_date: date | None,
    membership_as_of_date: date | None,
    constituent_as_of_date: date | None,
) -> None:
    dates = (source_as_of_date, membership_as_of_date, constituent_as_of_date)
    if any(type(value) is not date for value in dates) or len(set(dates)) != 1:
        raise ValueError(
            "source_as_of_date, membership_as_of_date, and constituent_as_of_date must be non-null dates and must match"
        )


def _failure_reason(
    min_coverage: float,
    observed: ExposureResult | RejectedExposure | None,
    observed_code: str,
    observed_coverage: float,
) -> str:
    reason = observed.failure_reason if isinstance(observed, RejectedExposure) else "not_qualified"
    return (
        f"no qualified exposure result at min_coverage={min_coverage:.4f}; "
        f"observed_etf={observed_code}; observed_coverage={observed_coverage}; reason={reason}"
    )

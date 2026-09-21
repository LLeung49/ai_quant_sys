"""Atomic, effective-dated mappings derived from ETF constituent exposure."""

from __future__ import annotations

from collections.abc import Callable, Iterable
from contextlib import AbstractContextManager, contextmanager
from datetime import date
from math import isclose, isfinite
from typing import Any, Literal, Protocol

from data_ingestion_qmt.db_config import execute_query, execute_update, get_connection

from .exposure import ExposureAssessment, ExposureResult, RejectedExposure
from .freshness import HoldingsFreshness, assess_holdings_freshness
from .return_exposure import ReturnExposureResult


CURRENT_MAPPING_MODE = "current_mapping"
MAPPING_TYPE_EXPOSURE_DERIVED = "exposure_derived"
MAPPING_TYPE_QUALITY_FAILURE = "exposure_quality_failure"
MAPPING_TYPE_RETURN_EXPOSURE_DERIVED = "return_exposure_derived"
MAPPING_TYPE_RETURN_QUALITY_FAILURE = "return_mapping_quality_failure"
RETURN_MAPPING_METHOD = "sw2_return_regression_v1"
QUALITY_STATUS_QUALIFIED = "qualified"
QUALITY_STATUS_FAILED = "failed"
_FAILURE_ETF_CODE = "__NO_QUALIFIED_ETF__"
_RETURN_FAILURE_REASON = "no_return_exposure_with_sufficient_observations"

SECTOR_ETF_MAP_DDL = """
CREATE TABLE IF NOT EXISTS trade_sector_etf_map (
    id BIGINT NOT NULL AUTO_INCREMENT,
    sector_level TINYINT NOT NULL,
    sector_name VARCHAR(128) NOT NULL,
    etf_code VARCHAR(32) NOT NULL,
    mapping_type VARCHAR(32) NOT NULL,
    mapping_method VARCHAR(64) DEFAULT NULL,
    is_primary TINYINT NOT NULL DEFAULT 0,
    effective_from DATE NOT NULL,
    effective_to DATE DEFAULT NULL,
    source_as_of_date DATE DEFAULT NULL,
    source_provider VARCHAR(64) NOT NULL,
    exposure_weight DECIMAL(18,8) NOT NULL,
    coverage_ratio DECIMAL(18,8) NOT NULL,
    mapping_version VARCHAR(64) NOT NULL,
    config_hash VARCHAR(128) NOT NULL,
    rank_no TINYINT NOT NULL,
    weight_unit ENUM('decimal', 'percent') DEFAULT NULL,
    membership_asof_mode VARCHAR(32) NOT NULL,
    membership_as_of_date DATE DEFAULT NULL,
    constituent_as_of_date DATE DEFAULT NULL,
    quality_status ENUM('qualified', 'failed') NOT NULL,
    failure_reason VARCHAR(255) DEFAULT NULL,
    mapping_note VARCHAR(255) DEFAULT NULL,
    source_reference VARCHAR(255) DEFAULT NULL,
    constituent_reported_date DATE DEFAULT NULL,
    holdings_age_days SMALLINT DEFAULT NULL,
    freshness_status ENUM('fresh', 'aging', 'stale') DEFAULT NULL,
    freshness_confidence DECIMAL(18,8) DEFAULT NULL,
    basket_source_priority VARCHAR(64) DEFAULT NULL,
    cross_check_status VARCHAR(32) DEFAULT NULL,
    cross_check_detail VARCHAR(1024) DEFAULT NULL,
    lookback_trading_days SMALLINT DEFAULT NULL,
    window_start_date DATE DEFAULT NULL,
    window_end_date DATE DEFAULT NULL,
    sample_count SMALLINT DEFAULT NULL,
    corr DECIMAL(24,12) DEFAULT NULL,
    beta DECIMAL(24,12) DEFAULT NULL,
    r_squared DECIMAL(24,12) DEFAULT NULL,
    residual_vol DECIMAL(24,12) DEFAULT NULL,
    sector_fit_score DECIMAL(24,12) DEFAULT NULL,
    confidence_status VARCHAR(32) DEFAULT NULL,
    price_source VARCHAR(64) DEFAULT NULL,
    price_as_of_date DATE DEFAULT NULL,
    universe_source VARCHAR(64) DEFAULT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY uk_sector_etf_map (sector_level, sector_name, etf_code, mapping_type, effective_from),
    KEY idx_sector_etf_effective (sector_level, sector_name, effective_from, effective_to)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
"""

# Existing deployments can contain manually curated rows.  Added fields stay
# nullable during migration so those legacy rows remain readable/auditable;
# qualified rows enforce complete provenance in Python; failure rows may keep
# unavailable provenance fields null so the quality event remains auditable.
_MIGRATION_COLUMNS = {
    "mapping_method": "VARCHAR(64) NULL",
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
    "source_reference": "VARCHAR(255) NULL",
    "constituent_reported_date": "DATE NULL",
    "holdings_age_days": "SMALLINT NULL",
    "freshness_status": "VARCHAR(16) NULL",
    "freshness_confidence": "DECIMAL(18,8) NULL",
    "basket_source_priority": "VARCHAR(64) NULL",
    "cross_check_status": "VARCHAR(32) NULL",
    "cross_check_detail": "VARCHAR(1024) NULL",
    "lookback_trading_days": "SMALLINT NULL",
    "window_start_date": "DATE NULL",
    "window_end_date": "DATE NULL",
    "sample_count": "SMALLINT NULL",
    "corr": "DECIMAL(24,12) NULL",
    "beta": "DECIMAL(24,12) NULL",
    "r_squared": "DECIMAL(24,12) NULL",
    "residual_vol": "DECIMAL(24,12) NULL",
    "sector_fit_score": "DECIMAL(24,12) NULL",
    "confidence_status": "VARCHAR(32) NULL",
    "price_source": "VARCHAR(64) NULL",
    "price_as_of_date": "DATE NULL",
    "universe_source": "VARCHAR(64) NULL",
    "updated_at": "DATETIME NULL",
}

_NULLABLE_FAILURE_PROVENANCE = {
    "source_as_of_date": "DATE NULL",
    "weight_unit": "ENUM('decimal', 'percent') NULL",
    "membership_as_of_date": "DATE NULL",
    "constituent_as_of_date": "DATE NULL",
}

_INSERT_EXPOSURE_MAPPING_SQL = """
INSERT INTO trade_sector_etf_map (
    sector_level, sector_name, etf_code, mapping_type, is_primary,
    effective_from, effective_to, source_as_of_date, source_provider,
    exposure_weight, coverage_ratio, mapping_version, rank_no, config_hash,
    weight_unit, membership_asof_mode, membership_as_of_date,
    constituent_as_of_date, quality_status, failure_reason, mapping_note,
    source_reference, constituent_reported_date, holdings_age_days,
    freshness_status, freshness_confidence, basket_source_priority,
    cross_check_status, cross_check_detail
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
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

_INSERT_RETURN_MAPPING_SQL = """
INSERT INTO trade_sector_etf_map (
    sector_level, sector_name, etf_code, mapping_type, mapping_method,
    is_primary, effective_from, effective_to, source_as_of_date,
    source_provider, exposure_weight, coverage_ratio, mapping_version,
    config_hash, rank_no, membership_asof_mode, quality_status,
    failure_reason, lookback_trading_days, window_start_date,
    window_end_date, sample_count, corr, beta, r_squared, residual_vol,
    sector_fit_score, confidence_status, price_source, price_as_of_date,
    universe_source
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
ON DUPLICATE KEY UPDATE
    mapping_method=VALUES(mapping_method), is_primary=VALUES(is_primary),
    effective_to=VALUES(effective_to), source_as_of_date=VALUES(source_as_of_date),
    source_provider=VALUES(source_provider), mapping_version=VALUES(mapping_version),
    config_hash=VALUES(config_hash), rank_no=VALUES(rank_no),
    quality_status=VALUES(quality_status), failure_reason=VALUES(failure_reason),
    lookback_trading_days=VALUES(lookback_trading_days),
    window_start_date=VALUES(window_start_date), window_end_date=VALUES(window_end_date),
    sample_count=VALUES(sample_count), corr=VALUES(corr), beta=VALUES(beta),
    r_squared=VALUES(r_squared), residual_vol=VALUES(residual_vol),
    sector_fit_score=VALUES(sector_fit_score), confidence_status=VALUES(confidence_status),
    price_source=VALUES(price_source), price_as_of_date=VALUES(price_as_of_date),
    universe_source=VALUES(universe_source)
"""

_LOCK_RETURN_SECTOR_SQL = """
SELECT id FROM trade_sector_etf_map
WHERE sector_level=%s AND sector_name=%s
  AND mapping_type IN ('return_exposure_derived', 'return_mapping_quality_failure')
FOR UPDATE
"""

_DELETE_SAME_DAY_RETURN_SQL = """
DELETE FROM trade_sector_etf_map
WHERE sector_level=%s AND sector_name=%s AND effective_from=%s
  AND mapping_type='return_exposure_derived'
"""

_DELETE_SAME_DAY_RETURN_FAILURE_SQL = """
DELETE FROM trade_sector_etf_map
WHERE sector_level=%s AND sector_name=%s AND effective_from=%s
  AND mapping_type='return_mapping_quality_failure'
"""

_REBUILD_RETURN_EFFECTIVE_INTERVALS_SQL = """
UPDATE trade_sector_etf_map AS target
LEFT JOIN (
    SELECT current_event.effective_from,
           MIN(next_event.effective_from) AS next_effective_from
    FROM (
        SELECT DISTINCT effective_from
        FROM trade_sector_etf_map
        WHERE sector_level=%s AND sector_name=%s
          AND mapping_type IN ('return_exposure_derived', 'return_mapping_quality_failure')
    ) AS current_event
    LEFT JOIN trade_sector_etf_map AS next_event
      ON next_event.sector_level=%s AND next_event.sector_name=%s
     AND next_event.effective_from > current_event.effective_from
     AND next_event.mapping_type IN ('return_exposure_derived', 'return_mapping_quality_failure')
    GROUP BY current_event.effective_from
) AS intervals ON intervals.effective_from=target.effective_from
SET target.effective_to=CASE
    WHEN intervals.next_effective_from IS NULL THEN NULL
    ELSE DATE_SUB(intervals.next_effective_from, INTERVAL 1 DAY)
END
WHERE target.sector_level=%s AND target.sector_name=%s
  AND target.mapping_type IN ('return_exposure_derived', 'return_mapping_quality_failure')
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
        """SELECT column_name, is_nullable FROM information_schema.columns
             WHERE table_schema=DATABASE() AND table_name=%s""",
        ("trade_sector_etf_map",),
    )
    existing = {str(_metadata_value(row, "column_name")) for row in rows}
    nullability = {
        str(_metadata_value(row, "column_name")): str(_metadata_value(row, "is_nullable"))
        for row in rows if _metadata_value(row, "is_nullable") is not None
    }
    for name, definition in _MIGRATION_COLUMNS.items():
        if name not in existing:
            execute_update(f"ALTER TABLE trade_sector_etf_map ADD COLUMN {name} {definition}", ())
    for name, definition in _NULLABLE_FAILURE_PROVENANCE.items():
        if nullability.get(name) == "NO":
            execute_update(f"ALTER TABLE trade_sector_etf_map MODIFY COLUMN {name} {definition}", ())
    index_rows = query(
        """SELECT index_name, column_name FROM information_schema.statistics
             WHERE table_schema=DATABASE() AND table_name=%s
             ORDER BY index_name, seq_in_index""",
        ("trade_sector_etf_map",),
    )
    index_columns: dict[str, list[str]] = {}
    for row in index_rows:
        index_columns.setdefault(str(_metadata_value(row, "index_name")), []).append(
            str(_metadata_value(row, "column_name")),
        )
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


def _metadata_value(row: dict[str, Any], name: str) -> object | None:
    """Read MySQL information_schema fields regardless of driver key casing."""

    for key, value in row.items():
        if key.casefold() == name:
            return value
    return None


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
    source_as_of_date: date | None,
    source_provider: str,
    membership_as_of_date: date | None,
    constituent_as_of_date: date | None,
    mapping_version: str,
    config_hash: str,
    weight_unit: Literal["decimal", "percent"] | None,
    min_coverage: float = 0.80,
    rejected: Iterable[RejectedExposure] = (),
    membership_asof_mode: str = CURRENT_MAPPING_MODE,
    quality_failure_reason: str | None = None,
    source_reference: str | None = None,
    constituent_reported_date: date | None = None,
    basket_source_priority: str | None = None,
    cross_check_status: str | None = "not_run",
    cross_check_detail: str | None = None,
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
    ranked_items = list(ranked)
    rejected_items = list(rejected)
    if quality_failure_reason is None:
        if weight_unit not in {"decimal", "percent"}:
            raise ValueError(f"invalid weight unit: {weight_unit!r}")
        _validate_as_of_dates(
            as_of_date,
            source_as_of_date,
            membership_as_of_date,
            constituent_as_of_date,
        )
    elif ranked_items:
        raise ValueError("quality_failure_reason cannot accompany ranked mappings")
    if not membership_asof_mode:
        raise ValueError("membership_asof_mode is required")

    if ensure_schema is not None:
        ensure_schema()
    qualified = sorted(
        (
            item for item in ranked_items
            if item.coverage_ratio >= min_coverage and item.exposure_weight > 0
        ),
        key=lambda item: (-item.exposure_weight, -item.coverage_ratio, item.etf_code),
    )[:3]
    if qualified and not str(source_reference or "").strip():
        raise ValueError("source_reference is required for qualified exposure mappings")
    if qualified and not str(source_provider or "").strip():
        raise ValueError("source_provider is required for qualified exposure mappings")
    if qualified and type(constituent_reported_date) is not date:
        raise ValueError("constituent_reported_date is required for qualified exposure mappings")
    if qualified and not str(basket_source_priority or "").strip():
        raise ValueError("basket_source_priority is required for qualified exposure mappings")
    freshness = (
        assess_holdings_freshness(constituent_reported_date, as_of_date)
        if type(constituent_reported_date) is date
        else None
    )
    rows = _mapping_rows(
        sector_name=sector_name, sector_level=sector_level, as_of_date=as_of_date,
        ranked=qualified, observed=[*ranked_items, *rejected_items], source_as_of_date=source_as_of_date, source_provider=source_provider,
        membership_as_of_date=membership_as_of_date,
        constituent_as_of_date=constituent_as_of_date, mapping_version=mapping_version,
        config_hash=config_hash, weight_unit=weight_unit, min_coverage=min_coverage,
        membership_asof_mode=membership_asof_mode,
        quality_failure_reason=quality_failure_reason,
        source_reference=source_reference,
        freshness=freshness,
        basket_source_priority=basket_source_priority,
        cross_check_status=cross_check_status,
        cross_check_detail=cross_check_detail,
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


def persist_return_exposure_mapping(
    sector_name: str,
    sector_level: int,
    as_of_date: date,
    ranked: Iterable[ReturnExposureResult],
    *,
    window_start_date: date,
    window_end_date: date,
    lookback_trading_days: int,
    price_as_of_date: date,
    price_source: str,
    universe_source: str,
    mapping_version: str,
    config_hash: str,
    transaction: Callable[[], AbstractContextManager[MappingTransaction]] = open_mapping_transaction,
    ensure_schema: Callable[[], None] | None = None,
) -> int:
    """Atomically persist one SW2 return-regression mapping event.

    This is deliberately separate from holdings-derived persistence: return
    rows have price-window provenance and never pass through constituent or
    holdings-freshness validation.
    """

    if sector_level != 2:
        raise ValueError("return exposure mapping requires sector_level=2")
    _validate_return_mapping_provenance(
        as_of_date=as_of_date,
        window_start_date=window_start_date,
        window_end_date=window_end_date,
        lookback_trading_days=lookback_trading_days,
        price_as_of_date=price_as_of_date,
        price_source=price_source,
        universe_source=universe_source,
        mapping_version=mapping_version,
        config_hash=config_hash,
    )
    if ensure_schema is not None:
        ensure_schema()

    qualified = sorted(
        (item for item in ranked if item.sample_count >= 50),
        key=lambda item: (-item.sector_fit_score, -item.r_squared, item.etf_code),
    )[:3]
    rows = _return_mapping_rows(
        sector_name=sector_name,
        sector_level=sector_level,
        as_of_date=as_of_date,
        ranked=qualified,
        window_start_date=window_start_date,
        window_end_date=window_end_date,
        lookback_trading_days=lookback_trading_days,
        price_as_of_date=price_as_of_date,
        price_source=price_source,
        universe_source=universe_source,
        mapping_version=mapping_version,
        config_hash=config_hash,
    )
    with transaction() as db:
        db.execute(_LOCK_RETURN_SECTOR_SQL, (sector_level, sector_name))
        db.execute(_DELETE_SAME_DAY_RETURN_SQL, (sector_level, sector_name, as_of_date))
        db.execute(_DELETE_SAME_DAY_RETURN_FAILURE_SQL, (sector_level, sector_name, as_of_date))
        db.execute_many(_INSERT_RETURN_MAPPING_SQL, rows)
        db.execute(
            _REBUILD_RETURN_EFFECTIVE_INTERVALS_SQL,
            (sector_level, sector_name, sector_level, sector_name, sector_level, sector_name),
        )
    return len(rows)


def load_effective_return_etfs(
    sector_name: str,
    sector_level: int,
    as_of_date: date,
    query: Callable[[str, tuple[object, ...]], list[dict[str, Any]]] = execute_query,
) -> list[dict[str, Any]]:
    """Load return-regression Top3 effective on a date, including low confidence."""

    if sector_level != 2:
        raise ValueError("return exposure mapping requires sector_level=2")
    rows = query(
        """SELECT etf_code, mapping_type, mapping_method, is_primary,
                  effective_from, effective_to, source_as_of_date,
                  source_provider, mapping_version, config_hash, rank_no,
                  quality_status, failure_reason, lookback_trading_days,
                  window_start_date, window_end_date, sample_count, corr, beta,
                  r_squared, residual_vol, sector_fit_score, confidence_status,
                  price_source, price_as_of_date, universe_source
             FROM trade_sector_etf_map AS mapping_event
             WHERE sector_name=%s AND sector_level=%s AND effective_from <= %s
               AND (effective_to IS NULL OR effective_to >= %s)
               AND mapping_type='return_exposure_derived'
               AND mapping_method='sw2_return_regression_v1'
               AND quality_status='qualified'
               AND NOT EXISTS (
                   SELECT 1 FROM trade_sector_etf_map AS failure_event
                    WHERE failure_event.sector_name=mapping_event.sector_name
                      AND failure_event.sector_level=mapping_event.sector_level
                      AND failure_event.mapping_type='return_mapping_quality_failure'
                      AND failure_event.effective_from > mapping_event.effective_from
                      AND failure_event.effective_from <= %s
               )
             ORDER BY rank_no ASC, etf_code ASC
             LIMIT 3""",
        (sector_name, sector_level, as_of_date, as_of_date, as_of_date),
    )
    return sorted(
        (
            row for row in rows
            if row.get("mapping_type") == MAPPING_TYPE_RETURN_EXPOSURE_DERIVED
            and row.get("mapping_method") == RETURN_MAPPING_METHOD
            and row.get("quality_status") == QUALITY_STATUS_QUALIFIED
            and _has_return_mapping_provenance(row, as_of_date)
        ),
        key=_effective_mapping_sort_key,
    )[:3]


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
                  quality_status, failure_reason, mapping_note, source_reference,
                  constituent_reported_date, holdings_age_days, freshness_status,
                  freshness_confidence, basket_source_priority,
                  cross_check_status, cross_check_detail
             FROM trade_sector_etf_map
             WHERE sector_name=%s AND sector_level=%s AND effective_from <= %s
               AND (effective_to IS NULL OR effective_to >= %s)
               AND mapping_type='exposure_derived' AND quality_status='qualified'
               AND exposure_weight > 0 AND coverage_ratio >= %s
               AND source_as_of_date=%s AND membership_as_of_date=%s
               AND constituent_as_of_date=%s
               AND source_provider IS NOT NULL AND TRIM(source_provider) <> ''
               AND source_reference IS NOT NULL AND TRIM(source_reference) <> ''
               AND constituent_reported_date IS NOT NULL
               AND holdings_age_days IS NOT NULL
               AND freshness_status IS NOT NULL
               AND freshness_confidence IS NOT NULL
               AND basket_source_priority IS NOT NULL AND TRIM(basket_source_priority) <> ''
             ORDER BY rank_no ASC, etf_code ASC
             LIMIT 3""",
        (
            sector_name, sector_level, as_of_date, as_of_date, min_coverage,
            as_of_date, as_of_date, as_of_date,
        ),
    )
    qualified = [
        row for row in rows
        if row.get("mapping_type") == MAPPING_TYPE_EXPOSURE_DERIVED
        and row.get("quality_status") == QUALITY_STATUS_QUALIFIED
        and float(row.get("exposure_weight") or 0) > 0
        and float(row.get("coverage_ratio") or 0) >= min_coverage
        and row.get("source_as_of_date") == as_of_date
        and row.get("membership_as_of_date") == as_of_date
        and row.get("constituent_as_of_date") == as_of_date
        and bool(str(row.get("source_provider") or "").strip())
        and bool(str(row.get("source_reference") or "").strip())
        and _has_consistent_holdings_freshness(row, as_of_date)
    ]
    return sorted(qualified, key=_effective_mapping_sort_key)[:3]


def _mapping_rows(
    *, sector_name: str, sector_level: int, as_of_date: date,
    ranked: list[ExposureResult], observed: list[ExposureResult | RejectedExposure], source_as_of_date: date | None, source_provider: str,
    membership_as_of_date: date | None, constituent_as_of_date: date | None, mapping_version: str,
    config_hash: str, weight_unit: str | None, min_coverage: float,
    membership_asof_mode: str, quality_failure_reason: str | None,
    source_reference: str | None, freshness: HoldingsFreshness | None,
    basket_source_priority: str | None,
    cross_check_status: str | None, cross_check_detail: str | None,
) -> list[tuple[object, ...]]:
    if not ranked:
        observed_item = max(observed, key=lambda item: (item.coverage_ratio, item.exposure_weight, item.etf_code), default=None)
        observed_code = observed_item.etf_code if observed_item else _FAILURE_ETF_CODE
        observed_exposure = observed_item.exposure_weight if observed_item else 0.0
        observed_coverage = observed_item.coverage_ratio if observed_item else 0.0
        return [(
            sector_level, sector_name, observed_code, MAPPING_TYPE_QUALITY_FAILURE, 0,
            as_of_date, None, source_as_of_date, source_provider, observed_exposure, observed_coverage,
            mapping_version, 0, config_hash, weight_unit, membership_asof_mode,
            membership_as_of_date, constituent_as_of_date, QUALITY_STATUS_FAILED,
            quality_failure_reason or _failure_reason(min_coverage, observed_item, observed_code, observed_coverage), None,
            source_reference, *_freshness_row_values(freshness), basket_source_priority,
            cross_check_status, cross_check_detail,
        )]
    return [
        (
            sector_level, sector_name, item.etf_code, MAPPING_TYPE_EXPOSURE_DERIVED,
            int(rank_no == 1), as_of_date, None, source_as_of_date, source_provider,
            item.exposure_weight, item.coverage_ratio, mapping_version, rank_no, config_hash,
            weight_unit, membership_asof_mode, membership_as_of_date, constituent_as_of_date,
            QUALITY_STATUS_QUALIFIED, None, None,
            source_reference, *_freshness_row_values(freshness), basket_source_priority,
            cross_check_status, cross_check_detail,
        )
        for rank_no, item in enumerate(ranked, start=1)
    ]


def _return_mapping_rows(
    *,
    sector_name: str,
    sector_level: int,
    as_of_date: date,
    ranked: list[ReturnExposureResult],
    window_start_date: date,
    window_end_date: date,
    lookback_trading_days: int,
    price_as_of_date: date,
    price_source: str,
    universe_source: str,
    mapping_version: str,
    config_hash: str,
) -> list[tuple[object, ...]]:
    common = (
        sector_level,
        sector_name,
        RETURN_MAPPING_METHOD,
        as_of_date,
        None,
        price_as_of_date,
        price_source,
        0.0,
        0.0,
        mapping_version,
        config_hash,
        CURRENT_MAPPING_MODE,
        lookback_trading_days,
        window_start_date,
        window_end_date,
        price_source,
        price_as_of_date,
        universe_source,
    )
    if not ranked:
        return [(
            common[0], common[1], _FAILURE_ETF_CODE,
            MAPPING_TYPE_RETURN_QUALITY_FAILURE, common[2], 0,
            common[3], common[4], common[5], common[6], common[7], common[8],
            common[9], common[10], 0, common[11], QUALITY_STATUS_FAILED,
            _RETURN_FAILURE_REASON, common[12], common[13], common[14],
            None, None, None, None, None, None, None,
            common[15], common[16], common[17],
        )]
    rows: list[tuple[object, ...]] = []
    for rank_no, item in enumerate(ranked, start=1):
        item_window_start, item_window_end, item_price_as_of = _return_result_price_window(
            item,
            fallback_start=window_start_date,
            fallback_end=window_end_date,
            fallback_price_as_of=price_as_of_date,
            event_date=as_of_date,
        )
        rows.append((
            common[0], common[1], item.etf_code,
            MAPPING_TYPE_RETURN_EXPOSURE_DERIVED, common[2], int(rank_no == 1),
            common[3], common[4], item_price_as_of, common[6], common[7], common[8],
            common[9], common[10], rank_no, common[11], QUALITY_STATUS_QUALIFIED,
            None, common[12], item_window_start, item_window_end, item.sample_count,
            item.corr, item.beta, item.r_squared, item.residual_vol,
            item.sector_fit_score, item.confidence_status,
            common[15], item_price_as_of, common[17],
        ))
    return rows


def _return_result_price_window(
    item: ReturnExposureResult,
    *,
    fallback_start: date,
    fallback_end: date,
    fallback_price_as_of: date,
    event_date: date,
) -> tuple[date, date, date]:
    provided = (item.window_start_date, item.window_end_date, item.price_as_of_date)
    if all(value is None for value in provided):
        return fallback_start, fallback_end, fallback_price_as_of
    if any(type(value) is not date for value in provided):
        raise ValueError("return result price-window dates must be all present dates")
    start, end, price_as_of = provided
    if not (start <= end == price_as_of <= event_date):
        raise ValueError("return result price-window provenance is incoherent")
    return start, end, price_as_of


def _validate_return_mapping_provenance(
    *,
    as_of_date: date,
    window_start_date: date,
    window_end_date: date,
    lookback_trading_days: int,
    price_as_of_date: date,
    price_source: str,
    universe_source: str,
    mapping_version: str,
    config_hash: str,
) -> None:
    if any(
        type(value) is not date
        for value in (as_of_date, window_start_date, window_end_date, price_as_of_date)
    ):
        raise ValueError("return mapping dates must be dates")
    if window_start_date > window_end_date:
        raise ValueError("window_start_date must not be after window_end_date")
    if window_end_date != price_as_of_date:
        raise ValueError("window_end_date and price_as_of_date must match")
    if price_as_of_date > as_of_date:
        raise ValueError("price_as_of_date must not be later than as_of_date")
    if isinstance(lookback_trading_days, bool) or lookback_trading_days < 1:
        raise ValueError("lookback_trading_days must be positive")
    for field, value in (
        ("price_source", price_source),
        ("universe_source", universe_source),
        ("mapping_version", mapping_version),
        ("config_hash", config_hash),
    ):
        if not str(value or "").strip():
            raise ValueError(f"{field} is required")


def _has_return_mapping_provenance(row: dict[str, Any], as_of_date: date) -> bool:
    effective_from = row.get("effective_from")
    effective_to = row.get("effective_to")
    source_as_of_date = row.get("source_as_of_date")
    window_start_date = row.get("window_start_date")
    window_end_date = row.get("window_end_date")
    price_as_of_date = row.get("price_as_of_date")
    if any(
        type(value) is not date
        for value in (
            effective_from,
            source_as_of_date,
            window_start_date,
            window_end_date,
            price_as_of_date,
        )
    ):
        return False
    if effective_to is not None and type(effective_to) is not date:
        return False
    if not (
        window_start_date <= window_end_date
        and window_end_date == price_as_of_date == source_as_of_date
        and price_as_of_date <= effective_from <= as_of_date
    ):
        return False
    if effective_to is not None and not (effective_from <= effective_to and as_of_date <= effective_to):
        return False
    price_source = str(row.get("price_source") or "").strip()
    if not price_source or str(row.get("source_provider") or "").strip() != price_source:
        return False
    if not str(row.get("universe_source") or "").strip():
        return False
    if not str(row.get("mapping_version") or "").strip() or not str(row.get("config_hash") or "").strip():
        return False
    if row.get("confidence_status") not in {"qualified", "low_confidence"}:
        return False
    try:
        lookback = int(row.get("lookback_trading_days"))
        sample_count = int(row.get("sample_count"))
        metrics = tuple(
            float(row.get(field))
            for field in ("corr", "beta", "r_squared", "residual_vol", "sector_fit_score")
        )
    except (TypeError, ValueError):
        return False
    return lookback > 0 and sample_count >= 50 and all(isfinite(value) for value in metrics)


def _sector_field(sector_level: int) -> str:
    if sector_level not in (1, 2):
        raise ValueError("sector_level must be 1 or 2")
    return f"sector_{sector_level}"


def _effective_mapping_sort_key(row: dict[str, Any]) -> tuple[int, str]:
    return (int(row.get("rank_no") or 99), str(row["etf_code"]))


def _freshness_row_values(freshness: HoldingsFreshness | None) -> tuple[object, object, object, object]:
    if freshness is None:
        return (None, None, None, None)
    return (
        freshness.reported_date,
        freshness.age_days,
        freshness.status,
        freshness.confidence,
    )


def _has_consistent_holdings_freshness(row: dict[str, Any], as_of_date: date) -> bool:
    reported_date = row.get("constituent_reported_date")
    if type(reported_date) is not date:
        return False
    if not str(row.get("basket_source_priority") or "").strip():
        return False
    try:
        freshness = assess_holdings_freshness(reported_date, as_of_date)
        confidence = float(row.get("freshness_confidence"))
    except (TypeError, ValueError):
        return False
    return (
        row.get("holdings_age_days") == freshness.age_days
        and row.get("freshness_status") == freshness.status
        and isclose(confidence, freshness.confidence, rel_tol=0.0, abs_tol=5e-9)
    )


def _validate_as_of_dates(
    as_of_date: date,
    source_as_of_date: date | None,
    membership_as_of_date: date | None,
    constituent_as_of_date: date | None,
) -> None:
    dates = (source_as_of_date, membership_as_of_date, constituent_as_of_date)
    if any(type(value) is not date for value in dates) or len(set(dates)) != 1:
        raise ValueError(
            "source_as_of_date, membership_as_of_date, and constituent_as_of_date must be non-null dates and must match"
        )
    if dates[0] != as_of_date:
        raise ValueError(
            "source_as_of_date, membership_as_of_date, and constituent_as_of_date must equal as_of_date"
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


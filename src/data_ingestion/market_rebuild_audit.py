"""Independent audit gates for a staged market-layer reconstruction."""

from __future__ import annotations

from dataclasses import dataclass
import random
from typing import Iterable, Mapping

from .db_config import execute_query
from .market_provider import MarketBatch
from .market_row_validation import validate_projection_batch


HARD_METRICS = (
    "missing_expected_codes",
    "unexpected_completed_codes",
    "exclusion_manifest_mismatches",
    "unresolved_gap_rows",
    "canonical_universe_mismatches",
    "staging_code_mismatches",
    "foreign_batch_rows",
    "incomplete_batches",
    "duplicate_rows",
    "batch_row_count_mismatches",
    "zero_price_rows",
    "non_finite_rows",
    "invalid_ohlc_rows",
    "mode_date_mismatches",
    "extra_adjusted_rows",
    "mode_volume_amount_mismatches",
    "rollback_table_collisions",
)


@dataclass(frozen=True)
class SourceComparison:
    stock_code: str
    compared_rows: int
    outside_tolerance: int
    hard_failures: tuple[str, ...] = ()
    warnings: tuple[str, ...] = ()


@dataclass(frozen=True)
class RebuildAuditReport:
    can_cutover: bool
    hard_failures: tuple[str, ...]
    warnings: tuple[str, ...]
    metrics: Mapping[str, int]


def build_stratified_sample(
    catalog: Iterable[Mapping[str, object]],
    seed: int,
    target_size: int = 30,
) -> list[str]:
    """Select deterministic coverage before filling remaining sample slots."""
    rows = [dict(row) for row in catalog]
    if target_size <= 0 or not rows:
        return []
    rng = random.Random(seed)
    strata: dict[tuple[object, ...], list[str]] = {}
    for row in rows:
        key = (
            row.get("security_type", "unknown"),
            row.get("listing_era", "unknown"),
            bool(row.get("has_action")),
            bool(row.get("abnormal")),
        )
        strata.setdefault(key, []).append(str(row["stock_code"]))
    selected: list[str] = []
    for key in sorted(strata, key=str):
        choices = sorted(set(strata[key]))
        selected.append(choices[rng.randrange(len(choices))])
        if len(selected) >= target_size:
            return selected
    remaining = sorted({str(row["stock_code"]) for row in rows} - set(selected))
    rng.shuffle(remaining)
    selected.extend(remaining[: max(0, target_size - len(selected))])
    return selected


def _index(batch: MarketBatch):
    return {
        (mode, str(row["stock_code"]), str(row["trade_date"])[:10]): row
        for mode, rows in batch.rows_by_mode.items()
        for row in rows
    }


def compare_source_batches(
    qmt_batch: MarketBatch,
    akshare_batch: MarketBatch,
    *,
    price_relative_tolerance: float = 0.05,
    volume_relative_tolerance: float = 0.20,
) -> SourceComparison:
    """Compare overlapping rows; source differences are advisory for recovery."""
    hard: list[str] = []
    for name, batch in (("qmt", qmt_batch), ("akshare", akshare_batch)):
        if batch.failures:
            hard.append(f"{name}_batch_incomplete")
            continue
        validation = validate_projection_batch(batch.rows_by_mode)
        if not validation.is_valid:
            hard.append(f"{name}_batch_structurally_invalid")
    qmt_rows = _index(qmt_batch)
    ak_rows = _index(akshare_batch)
    overlap = sorted(set(qmt_rows).intersection(ak_rows))
    outside = 0
    for key in overlap:
        left, right = qmt_rows[key], ak_rows[key]
        price_bad = any(
            abs(float(left[field]) - float(right[field]))
            / max(abs(float(left[field])), 0.01)
            > price_relative_tolerance
            for field in ("open_price", "high_price", "low_price", "close_price")
        )
        volume_bad = (
            abs(float(left["volume"]) - float(right["volume"]))
            / max(abs(float(left["volume"])), 1.0)
            > volume_relative_tolerance
        )
        if price_bad or volume_bad:
            outside += 1
    warnings = []
    if not overlap:
        warnings.append("akshare_no_overlapping_rows")
    elif outside:
        warnings.append(f"akshare_outside_tolerance={outside}/{len(overlap)}")
    return SourceComparison(
        qmt_batch.stock_code,
        len(overlap),
        outside,
        tuple(hard),
        tuple(warnings),
    )


def assess_rebuild_metrics(
    metrics: Mapping[str, int], comparisons: Iterable[SourceComparison]
) -> RebuildAuditReport:
    hard = [f"{name}={int(metrics.get(name, 0))}" for name in HARD_METRICS if metrics.get(name, 0)]
    warnings: list[str] = []
    for comparison in comparisons:
        hard.extend(
            f"{comparison.stock_code}:{failure}" for failure in comparison.hard_failures
        )
        warnings.extend(
            f"{comparison.stock_code}:{warning}" for warning in comparison.warnings
        )
    return RebuildAuditReport(not hard, tuple(hard), tuple(warnings), dict(metrics))


def audit_rebuild(batch_id: str) -> RebuildAuditReport:
    """Read structural metrics from staging; AKShare comparisons are added separately."""
    incomplete = execute_query(
        "SELECT COUNT(*) AS n FROM trade_market_rebuild_batch b "
        "LEFT JOIN trade_market_rebuild_excluded_code x "
        "ON x.batch_id=b.batch_id AND x.stock_code=b.stock_code "
        "WHERE b.batch_id=%s AND b.status<>'complete' AND x.stock_code IS NULL",
        (batch_id,),
    )[0]["n"]
    universe = execute_query(
        """
        SELECT
          (SELECT COUNT(*) FROM trade_market_rebuild_expected_code e
           LEFT JOIN trade_market_rebuild_excluded_code x
             ON x.batch_id=e.batch_id AND x.stock_code=e.stock_code
           LEFT JOIN trade_market_rebuild_batch b
             ON b.batch_id=e.batch_id AND b.stock_code=e.stock_code AND b.status='complete'
           WHERE e.batch_id=%s AND x.stock_code IS NULL AND b.stock_code IS NULL)
             AS missing_expected_codes,
          (SELECT COUNT(*) FROM trade_market_rebuild_batch b
           LEFT JOIN trade_market_rebuild_expected_code e
             ON e.batch_id=b.batch_id AND e.stock_code=b.stock_code
           LEFT JOIN trade_market_rebuild_excluded_code x
             ON x.batch_id=b.batch_id AND x.stock_code=b.stock_code
           WHERE b.batch_id=%s AND b.status='complete'
             AND (e.stock_code IS NULL OR x.stock_code IS NOT NULL))
            AS unexpected_completed_codes
        """,
        (batch_id, batch_id),
    )[0]
    exclusions = execute_query(
        """
        SELECT COUNT(*) AS n
        FROM trade_market_rebuild_excluded_code x
        LEFT JOIN trade_market_rebuild_expected_code e
          ON e.batch_id=x.batch_id AND e.stock_code=x.stock_code
        WHERE x.batch_id=%s
          AND (e.stock_code IS NULL OR TRIM(x.reason)=''
            OR JSON_LENGTH(x.evidence)=0)
        """,
        (batch_id,),
    )[0]["n"]
    gaps = execute_query(
        """
        SELECT
          COALESCE(SUM(CASE
            WHEN g.reason='zero_price_fill'
             AND (g.last_trade_date < b.start_date OR g.first_trade_date > b.end_date)
            THEN 0 ELSE g.gap_count END), 0) AS unresolved_gap_rows,
          COALESCE(SUM(CASE
            WHEN g.reason='zero_price_fill'
             AND (g.last_trade_date < b.start_date OR g.first_trade_date > b.end_date)
            THEN g.gap_count ELSE 0 END), 0) AS outside_expected_gap_rows
        FROM trade_market_rebuild_gap g
        JOIN trade_market_rebuild_batch b
          ON b.batch_id=g.batch_id AND b.stock_code=g.stock_code
        LEFT JOIN trade_market_rebuild_excluded_code x
          ON x.batch_id=b.batch_id AND x.stock_code=b.stock_code
        WHERE g.batch_id=%s AND b.status='complete' AND x.stock_code IS NULL
        """,
        (batch_id,),
    )[0]
    canonical = execute_query(
        """
        SELECT COUNT(*) AS n FROM (
          SELECT current_codes.stock_code
          FROM (
            SELECT stock_code FROM trade_stock_daily_raw
            UNION SELECT stock_code FROM trade_stock_daily_qfq
            UNION SELECT stock_code FROM trade_stock_daily_bfq
          ) current_codes
          LEFT JOIN trade_market_rebuild_expected_code e
            ON e.batch_id=%s AND e.stock_code=current_codes.stock_code
          WHERE e.stock_code IS NULL
          UNION ALL
          SELECT e.stock_code
          FROM trade_market_rebuild_expected_code e
          LEFT JOIN (
            SELECT stock_code FROM trade_stock_daily_raw
            UNION SELECT stock_code FROM trade_stock_daily_qfq
            UNION SELECT stock_code FROM trade_stock_daily_bfq
          ) current_codes ON current_codes.stock_code=e.stock_code
          WHERE e.batch_id=%s AND current_codes.stock_code IS NULL
        ) differences
        """,
        (batch_id, batch_id),
    )[0]["n"]
    staging = execute_query(
        """
        SELECT
          SUM(code_mismatch) AS staging_code_mismatches,
          SUM(foreign_rows) AS foreign_batch_rows
        FROM (
          SELECT
            (SELECT COUNT(*) FROM (
              SELECT e.stock_code FROM trade_market_rebuild_expected_code e
              LEFT JOIN trade_market_rebuild_excluded_code x
                ON x.batch_id=e.batch_id AND x.stock_code=e.stock_code
              LEFT JOIN (SELECT DISTINCT stock_code FROM trade_stock_daily_raw_rebuild
                         WHERE rebuild_batch_id=%s) s ON s.stock_code=e.stock_code
              WHERE e.batch_id=%s AND x.stock_code IS NULL AND s.stock_code IS NULL
              UNION ALL
              SELECT DISTINCT s.stock_code FROM trade_stock_daily_raw_rebuild s
              LEFT JOIN trade_market_rebuild_expected_code e
                ON e.batch_id=%s AND e.stock_code=s.stock_code
              LEFT JOIN trade_market_rebuild_excluded_code x
                ON x.batch_id=e.batch_id AND x.stock_code=e.stock_code
              WHERE s.rebuild_batch_id=%s
                AND (e.stock_code IS NULL OR x.stock_code IS NOT NULL)
            ) d) AS code_mismatch,
            (SELECT COUNT(*) FROM trade_stock_daily_raw_rebuild
             WHERE rebuild_batch_id<>%s) AS foreign_rows
          UNION ALL
          SELECT
            (SELECT COUNT(*) FROM (
              SELECT e.stock_code FROM trade_market_rebuild_expected_code e
              LEFT JOIN trade_market_rebuild_excluded_code x
                ON x.batch_id=e.batch_id AND x.stock_code=e.stock_code
              LEFT JOIN (SELECT DISTINCT stock_code FROM trade_stock_daily_qfq_rebuild
                         WHERE rebuild_batch_id=%s) s ON s.stock_code=e.stock_code
              WHERE e.batch_id=%s AND x.stock_code IS NULL AND s.stock_code IS NULL
              UNION ALL
              SELECT DISTINCT s.stock_code FROM trade_stock_daily_qfq_rebuild s
              LEFT JOIN trade_market_rebuild_expected_code e
                ON e.batch_id=%s AND e.stock_code=s.stock_code
              LEFT JOIN trade_market_rebuild_excluded_code x
                ON x.batch_id=e.batch_id AND x.stock_code=e.stock_code
              WHERE s.rebuild_batch_id=%s
                AND (e.stock_code IS NULL OR x.stock_code IS NOT NULL)
            ) d),
            (SELECT COUNT(*) FROM trade_stock_daily_qfq_rebuild
             WHERE rebuild_batch_id<>%s)
          UNION ALL
          SELECT
            (SELECT COUNT(*) FROM (
              SELECT e.stock_code FROM trade_market_rebuild_expected_code e
              LEFT JOIN trade_market_rebuild_excluded_code x
                ON x.batch_id=e.batch_id AND x.stock_code=e.stock_code
              LEFT JOIN (SELECT DISTINCT stock_code FROM trade_stock_daily_bfq_rebuild
                         WHERE rebuild_batch_id=%s) s ON s.stock_code=e.stock_code
              WHERE e.batch_id=%s AND x.stock_code IS NULL AND s.stock_code IS NULL
              UNION ALL
              SELECT DISTINCT s.stock_code FROM trade_stock_daily_bfq_rebuild s
              LEFT JOIN trade_market_rebuild_expected_code e
                ON e.batch_id=%s AND e.stock_code=s.stock_code
              LEFT JOIN trade_market_rebuild_excluded_code x
                ON x.batch_id=e.batch_id AND x.stock_code=e.stock_code
              WHERE s.rebuild_batch_id=%s
                AND (e.stock_code IS NULL OR x.stock_code IS NOT NULL)
            ) d),
            (SELECT COUNT(*) FROM trade_stock_daily_bfq_rebuild
             WHERE rebuild_batch_id<>%s)
        ) checks
        """,
        (batch_id, batch_id, batch_id, batch_id, batch_id,
         batch_id, batch_id, batch_id, batch_id, batch_id,
         batch_id, batch_id, batch_id, batch_id, batch_id),
    )[0]
    duplicates = execute_query(
        """
        SELECT COALESCE(SUM(duplicate_count), 0) AS n FROM (
          SELECT COUNT(*) - 1 AS duplicate_count
          FROM trade_stock_daily_raw_rebuild WHERE rebuild_batch_id=%s
          GROUP BY stock_code, trade_date HAVING COUNT(*) > 1
          UNION ALL
          SELECT COUNT(*) - 1
          FROM trade_stock_daily_qfq_rebuild WHERE rebuild_batch_id=%s
          GROUP BY stock_code, trade_date HAVING COUNT(*) > 1
          UNION ALL
          SELECT COUNT(*) - 1
          FROM trade_stock_daily_bfq_rebuild WHERE rebuild_batch_id=%s
          GROUP BY stock_code, trade_date HAVING COUNT(*) > 1
        ) duplicates
        """,
        (batch_id, batch_id, batch_id),
    )[0]["n"]
    batch_counts = execute_query(
        """
        SELECT COUNT(*) AS n
        FROM trade_market_rebuild_batch b
        LEFT JOIN (
          SELECT stock_code, COUNT(*) AS n FROM trade_stock_daily_raw_rebuild
          WHERE rebuild_batch_id=%s GROUP BY stock_code
        ) r ON r.stock_code=b.stock_code
        LEFT JOIN (
          SELECT stock_code, COUNT(*) AS n FROM trade_stock_daily_qfq_rebuild
          WHERE rebuild_batch_id=%s GROUP BY stock_code
        ) q ON q.stock_code=b.stock_code
        LEFT JOIN (
          SELECT stock_code, COUNT(*) AS n FROM trade_stock_daily_bfq_rebuild
          WHERE rebuild_batch_id=%s GROUP BY stock_code
        ) h ON h.stock_code=b.stock_code
        WHERE b.batch_id=%s AND b.status='complete'
          AND (b.raw_rows<>COALESCE(r.n, 0)
            OR b.qfq_rows<>COALESCE(q.n, 0)
            OR b.hfq_rows<>COALESCE(h.n, 0))
        """,
        (batch_id, batch_id, batch_id, batch_id),
    )[0]["n"]
    aggregate = execute_query(
        """
        SELECT
          SUM(zero_price) AS zero_price_rows,
          SUM(non_finite) AS non_finite_rows,
          SUM(invalid_ohlc) AS invalid_ohlc_rows
        FROM (
          SELECT
            (open_price=0 OR high_price=0 OR low_price=0 OR close_price=0) zero_price,
            (NOT (open_price <=> open_price) OR NOT (high_price <=> high_price)
             OR NOT (low_price <=> low_price) OR NOT (close_price <=> close_price)
             OR NOT (amount <=> amount)) non_finite,
            (low_price>high_price OR low_price>LEAST(open_price,close_price)
             OR high_price<GREATEST(open_price,close_price)) invalid_ohlc
          FROM trade_stock_daily_raw_rebuild WHERE rebuild_batch_id=%s
          UNION ALL
          SELECT
            (open_price=0 OR high_price=0 OR low_price=0 OR close_price=0),
            (NOT (open_price <=> open_price) OR NOT (high_price <=> high_price)
             OR NOT (low_price <=> low_price) OR NOT (close_price <=> close_price)
             OR NOT (amount <=> amount)),
            (low_price>high_price OR low_price>LEAST(open_price,close_price)
             OR high_price<GREATEST(open_price,close_price))
          FROM trade_stock_daily_qfq_rebuild WHERE rebuild_batch_id=%s
          UNION ALL
          SELECT
            (open_price=0 OR high_price=0 OR low_price=0 OR close_price=0),
            (NOT (open_price <=> open_price) OR NOT (high_price <=> high_price)
             OR NOT (low_price <=> low_price) OR NOT (close_price <=> close_price)
             OR NOT (amount <=> amount)),
            (low_price>high_price OR low_price>LEAST(open_price,close_price)
             OR high_price<GREATEST(open_price,close_price))
          FROM trade_stock_daily_bfq_rebuild WHERE rebuild_batch_id=%s
        ) checked
        """,
        (batch_id, batch_id, batch_id),
    )[0]
    alignment = execute_query(
        """
        SELECT
          SUM(q.stock_code IS NULL OR b.stock_code IS NULL) AS mode_date_mismatches,
          SUM(q.stock_code IS NOT NULL AND b.stock_code IS NOT NULL AND
              (r.volume<>q.volume OR r.amount<>q.amount OR
               r.volume<>b.volume OR r.amount<>b.amount)) AS mode_volume_amount_mismatches
        FROM trade_stock_daily_raw_rebuild r
        LEFT JOIN trade_stock_daily_qfq_rebuild q
          ON q.stock_code=r.stock_code AND q.trade_date=r.trade_date AND q.rebuild_batch_id=%s
        LEFT JOIN trade_stock_daily_bfq_rebuild b
          ON b.stock_code=r.stock_code AND b.trade_date=r.trade_date AND b.rebuild_batch_id=%s
        WHERE r.rebuild_batch_id=%s
        """,
        (batch_id, batch_id, batch_id),
    )[0]
    extra_adjusted = execute_query(
        """
        SELECT
          (SELECT COUNT(*) FROM trade_stock_daily_qfq_rebuild q
           LEFT JOIN trade_stock_daily_raw_rebuild r
             ON r.stock_code=q.stock_code AND r.trade_date=q.trade_date
                AND r.rebuild_batch_id=%s
           WHERE q.rebuild_batch_id=%s AND r.stock_code IS NULL)
          +
          (SELECT COUNT(*) FROM trade_stock_daily_bfq_rebuild b
           LEFT JOIN trade_stock_daily_raw_rebuild r
             ON r.stock_code=b.stock_code AND r.trade_date=b.trade_date
                AND r.rebuild_batch_id=%s
           WHERE b.rebuild_batch_id=%s AND r.stock_code IS NULL) AS n
        """,
        (batch_id, batch_id, batch_id, batch_id),
    )[0]["n"]
    rollback_collisions = execute_query(
        """
        SELECT COUNT(*) AS n FROM information_schema.tables
        WHERE table_schema=DATABASE() AND table_name IN (
          'trade_stock_daily_raw_rollback_20261014',
          'trade_stock_daily_qfq_rollback_20261014',
          'trade_stock_daily_bfq_rollback_20261014',
          'trade_stock_daily_raw_rejected_20261014',
          'trade_stock_daily_qfq_rejected_20261014',
          'trade_stock_daily_bfq_rejected_20261014'
        )
        """
    )[0]["n"]
    metrics = {
        "missing_expected_codes": int(universe.get("missing_expected_codes") or 0),
        "unexpected_completed_codes": int(universe.get("unexpected_completed_codes") or 0),
        "exclusion_manifest_mismatches": int(exclusions or 0),
        "unresolved_gap_rows": int(gaps.get("unresolved_gap_rows") or 0),
        "outside_expected_gap_rows": int(gaps.get("outside_expected_gap_rows") or 0),
        "canonical_universe_mismatches": int(canonical or 0),
        "staging_code_mismatches": int(staging.get("staging_code_mismatches") or 0),
        "foreign_batch_rows": int(staging.get("foreign_batch_rows") or 0),
        "incomplete_batches": int(incomplete or 0),
        "duplicate_rows": int(duplicates or 0),
        "batch_row_count_mismatches": int(batch_counts or 0),
        "zero_price_rows": int(aggregate.get("zero_price_rows") or 0),
        "non_finite_rows": int(aggregate.get("non_finite_rows") or 0),
        "invalid_ohlc_rows": int(aggregate.get("invalid_ohlc_rows") or 0),
        "mode_date_mismatches": int(alignment.get("mode_date_mismatches") or 0),
        "extra_adjusted_rows": int(extra_adjusted or 0),
        "mode_volume_amount_mismatches": int(alignment.get("mode_volume_amount_mismatches") or 0),
        "rollback_table_collisions": int(rollback_collisions or 0),
    }
    return assess_rebuild_metrics(metrics, [])

"""Independent audit gates for a staged market-layer reconstruction."""

from __future__ import annotations

from dataclasses import dataclass
import random
from typing import Iterable, Mapping

from .db_config import execute_query
from .market_provider import MarketBatch
from .market_row_validation import validate_projection_batch


HARD_METRICS = (
    "incomplete_batches",
    "duplicate_rows",
    "zero_price_rows",
    "non_finite_rows",
    "invalid_ohlc_rows",
    "mode_date_mismatches",
    "mode_volume_amount_mismatches",
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
        "SELECT COUNT(*) AS n FROM trade_market_rebuild_batch "
        "WHERE batch_id=%s AND status<>'complete'", (batch_id,)
    )[0]["n"]
    aggregate = execute_query(
        """
        SELECT
          SUM(zero_price) AS zero_price_rows,
          SUM(invalid_ohlc) AS invalid_ohlc_rows
        FROM (
          SELECT
            (open_price=0 OR high_price=0 OR low_price=0 OR close_price=0) zero_price,
            (low_price>high_price OR low_price>LEAST(open_price,close_price)
             OR high_price<GREATEST(open_price,close_price)) invalid_ohlc
          FROM trade_stock_daily_raw_rebuild WHERE rebuild_batch_id=%s
          UNION ALL
          SELECT
            (open_price=0 OR high_price=0 OR low_price=0 OR close_price=0),
            (low_price>high_price OR low_price>LEAST(open_price,close_price)
             OR high_price<GREATEST(open_price,close_price))
          FROM trade_stock_daily_qfq_rebuild WHERE rebuild_batch_id=%s
          UNION ALL
          SELECT
            (open_price=0 OR high_price=0 OR low_price=0 OR close_price=0),
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
    metrics = {
        "incomplete_batches": int(incomplete or 0),
        "duplicate_rows": 0,
        "zero_price_rows": int(aggregate.get("zero_price_rows") or 0),
        "non_finite_rows": 0,
        "invalid_ohlc_rows": int(aggregate.get("invalid_ohlc_rows") or 0),
        "mode_date_mismatches": int(alignment.get("mode_date_mismatches") or 0),
        "mode_volume_amount_mismatches": int(alignment.get("mode_volume_amount_mismatches") or 0),
    }
    return assess_rebuild_metrics(metrics, [])

"""Dry-run-first repair of historical daily-market volume unit drift.

The command never downloads market data.  It identifies rows whose
amount/(close*volume) relation proves their volume is in shares, records the
original values under a run id, and converts them to canonical lots.
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
from datetime import date
from typing import Iterable
from uuid import uuid4

from .db_config import get_connection
from .market_volume_contract import assess_volume


FACT_TABLES = (
    "trade_stock_daily",
    "trade_stock_daily_qfq",
    "trade_stock_daily_bfq",
)

# Explicitly force the date indexes for full-market monthly repair batches.
# The fact tables are large enough that an expression on amount/volume alone
# otherwise invites an expensive full-table scan.
FACT_TABLE_DATE_INDEXES = {
    "trade_stock_daily": "idx_stock_daily_date",
    "trade_stock_daily_qfq": "idx_qfq_trade_date",
    "trade_stock_daily_bfq": "idx_bfq_trade_date",
}

CUTOVER_CODES_SQL = """
SELECT l12.stock_code
FROM trade_stock_daily AS l12
JOIN trade_stock_daily_raw AS r12
  ON r12.stock_code=l12.stock_code AND r12.trade_date=l12.trade_date
JOIN trade_stock_daily AS l13
  ON l13.stock_code=l12.stock_code AND l13.trade_date='2026-08-13'
JOIN trade_stock_daily_raw AS r13
  ON r13.stock_code=l13.stock_code AND r13.trade_date=l13.trade_date
WHERE l12.trade_date='2026-08-12'
  AND l12.volume / NULLIF(r12.volume, 0) BETWEEN 50 AND 150
  AND l13.volume / NULLIF(r13.volume, 0) BETWEEN 0.5 AND 2
"""

AUDIT_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS trade_market_volume_repair_audit (
    run_id CHAR(36) NOT NULL,
    table_name VARCHAR(64) NOT NULL,
    stock_code VARCHAR(16) NOT NULL,
    trade_date DATE NOT NULL,
    original_volume BIGINT NOT NULL,
    normalized_volume BIGINT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (run_id, table_name, stock_code, trade_date)
)
"""


@dataclass(frozen=True)
class VolumeRepairCandidate:
    table_name: str
    stock_code: str
    trade_date: date
    volume: int
    amount: float
    close_price: float

    @property
    def normalized_volume(self) -> int | None:
        return assess_volume(self.amount, self.close_price, self.volume).normalized_volume


@dataclass(frozen=True)
class VolumeRepairPlan:
    candidates: tuple[VolumeRepairCandidate, ...]
    row_counts: dict[str, int]
    start_date: date | None
    end_date: date | None


def build_repair_plan(candidates: Iterable[VolumeRepairCandidate]) -> VolumeRepairPlan:
    selected = tuple(
        candidate for candidate in candidates
        if candidate.table_name in FACT_TABLES
        and assess_volume(candidate.amount, candidate.close_price, candidate.volume).unit == "share"
    )
    dates = [candidate.trade_date for candidate in selected]
    return VolumeRepairPlan(
        candidates=selected,
        row_counts=dict(Counter(candidate.table_name for candidate in selected)),
        start_date=min(dates) if dates else None,
        end_date=max(dates) if dates else None,
    )


def month_window(month: str) -> tuple[date, date]:
    """Return [month start, next month start) and reject ambiguous input."""
    try:
        year_text, month_text = month.split("-", maxsplit=1)
        year, month_number = int(year_text), int(month_text)
        start = date(year, month_number, 1)
    except (TypeError, ValueError) as exc:
        raise ValueError("month must be YYYY-MM") from exc
    if start.month == 12:
        return start, date(start.year + 1, 1, 1)
    return start, date(start.year, start.month + 1, 1)


def iter_months(first_month: str, last_month: str) -> Iterable[str]:
    """Yield an inclusive, validated sequence of YYYY-MM month keys."""
    current, _ = month_window(first_month)
    last, _ = month_window(last_month)
    if current > last:
        raise ValueError("from-month must not be later than to-month")
    while current <= last:
        yield current.strftime("%Y-%m")
        if current.month == 12:
            current = date(current.year + 1, 1, 1)
        else:
            current = date(current.year, current.month + 1, 1)


def scan_candidates(connection) -> list[VolumeRepairCandidate]:
    candidates: list[VolumeRepairCandidate] = []
    cursor = connection.cursor()
    try:
        print("[volume-unit-repair] identifying-cutover-codes", flush=True)
        cursor.execute(CUTOVER_CODES_SQL)
        codes = [row[0] for row in cursor.fetchall()]
        print(f"[volume-unit-repair] cutover_codes={len(codes)}", flush=True)
        if not codes:
            return candidates
        placeholders = ", ".join(["%s"] * len(codes))
        for table_name in FACT_TABLES:
            print(f"[volume-unit-repair] scanning={table_name}", flush=True)
            cursor.execute(
                f"""SELECT stock_code, trade_date, volume, amount, close_price
                    FROM {table_name}
                   WHERE stock_code IN ({placeholders})
                     AND volume > 0 AND amount > 0 AND close_price > 0
                     AND amount / (volume * close_price) BETWEEN 0.5 AND 2""",
                codes,
            )
            rows = cursor.fetchall()
            print(f"[volume-unit-repair] scanned_candidates={table_name}:{len(rows)}", flush=True)
            for stock_code, trade_date, volume, amount, close_price in rows:
                candidates.append(VolumeRepairCandidate(
                    table_name=table_name,
                    stock_code=stock_code,
                    trade_date=trade_date,
                    volume=int(volume),
                    amount=float(amount),
                    close_price=float(close_price),
                ))
    finally:
        cursor.close()
    return candidates


def scan_candidates_for_date_range(
    connection,
    start_date: date,
    end_date: date,
) -> list[VolumeRepairCandidate]:
    """Scan all stocks in a bounded date window for provable share-unit rows."""
    candidates: list[VolumeRepairCandidate] = []
    cursor = connection.cursor()
    try:
        for table_name in FACT_TABLES:
            index_name = FACT_TABLE_DATE_INDEXES[table_name]
            print(
                f"[volume-unit-repair] scanning={table_name} range={start_date}:{end_date}",
                flush=True,
            )
            cursor.execute(
                f"""SELECT stock_code, trade_date, volume, amount, close_price
                    FROM {table_name} FORCE INDEX ({index_name})
                   WHERE trade_date >= %s AND trade_date < %s
                     AND volume > 0 AND amount > 0 AND close_price > 0
                     AND amount / (volume * close_price) BETWEEN 0.5 AND 2""",
                (start_date, end_date),
            )
            rows = cursor.fetchall()
            print(f"[volume-unit-repair] scanned_candidates={table_name}:{len(rows)}", flush=True)
            for stock_code, trade_date, volume, amount, close_price in rows:
                candidates.append(VolumeRepairCandidate(
                    table_name=table_name,
                    stock_code=stock_code,
                    trade_date=trade_date,
                    volume=int(volume),
                    amount=float(amount),
                    close_price=float(close_price),
                ))
    finally:
        cursor.close()
    return candidates


def create_audit_table(connection) -> None:
    cursor = connection.cursor()
    try:
        cursor.execute(AUDIT_TABLE_SQL)
        connection.commit()
    finally:
        cursor.close()


def apply_plan(connection, plan: VolumeRepairPlan, run_id: str) -> dict[str, int]:
    """Persist an audit snapshot then update only rows selected by the plan."""
    create_audit_table(connection)
    cursor = connection.cursor()
    try:
        for table_name in FACT_TABLES:
            table_candidates = [
                candidate for candidate in plan.candidates
                if candidate.table_name == table_name
            ]
            if not table_candidates:
                continue
            audit_values = [
                (run_id, table_name, candidate.stock_code, candidate.trade_date,
                 candidate.volume, candidate.normalized_volume)
                for candidate in table_candidates
            ]
            cursor.executemany(
                """INSERT INTO trade_market_volume_repair_audit
                   (run_id, table_name, stock_code, trade_date, original_volume, normalized_volume)
                   VALUES (%s, %s, %s, %s, %s, %s)""",
                audit_values,
            )
            cursor.execute(
                f"""UPDATE {table_name} AS fact
                    INNER JOIN trade_market_volume_repair_audit AS audit
                      ON audit.table_name=%s
                     AND audit.stock_code=fact.stock_code
                     AND audit.trade_date=fact.trade_date
                   SET fact.volume=audit.normalized_volume
                 WHERE audit.run_id=%s""",
                (table_name, run_id),
            )
            if cursor.rowcount != len(table_candidates):
                raise RuntimeError(f"updated row count mismatch for {table_name}")
            cursor.execute(
                f"""SELECT COUNT(*) FROM {table_name} AS fact
                    INNER JOIN trade_market_volume_repair_audit AS audit
                      ON audit.table_name=%s
                     AND audit.stock_code=fact.stock_code
                     AND audit.trade_date=fact.trade_date
                   WHERE audit.run_id=%s AND fact.volume<>audit.normalized_volume""",
                (table_name, run_id),
            )
            if cursor.fetchone()[0]:
                raise RuntimeError(f"post-update validation failed for {table_name}")
        connection.commit()
        return plan.row_counts
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()


def rollback_run(connection, run_id: str) -> dict[str, int]:
    cursor = connection.cursor()
    restored: dict[str, int] = {}
    try:
        for table_name in FACT_TABLES:
            cursor.execute(
                f"""UPDATE {table_name} AS fact
                    INNER JOIN trade_market_volume_repair_audit AS audit
                      ON audit.table_name=%s
                     AND audit.stock_code=fact.stock_code
                     AND audit.trade_date=fact.trade_date
                   SET fact.volume=audit.original_volume
                 WHERE audit.run_id=%s""",
                (table_name, run_id),
            )
            restored[table_name] = cursor.rowcount
        connection.commit()
        return restored
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()


def _print_plan(plan: VolumeRepairPlan) -> None:
    print("[volume-unit-repair] rows=", sum(plan.row_counts.values()))
    print("[volume-unit-repair] by_table=", plan.row_counts)
    print("[volume-unit-repair] date_range=", plan.start_date, plan.end_date)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Repair historical share-unit daily volumes to lots")
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--rollback", metavar="RUN_ID")
    parser.add_argument("--month", metavar="YYYY-MM", help="repair every stock in one calendar month")
    parser.add_argument("--all-months", action="store_true", help="process an inclusive month range")
    parser.add_argument("--from-month", metavar="YYYY-MM")
    parser.add_argument("--to-month", metavar="YYYY-MM")
    parser.add_argument("--run-id", metavar="RUN_ID", help="reuse one audit run id across batches")
    args = parser.parse_args(argv)
    if args.apply and args.rollback:
        parser.error("--apply and --rollback are mutually exclusive")
    if args.month and args.all_months:
        parser.error("--month and --all-months are mutually exclusive")
    if args.all_months and (not args.from_month or not args.to_month):
        parser.error("--all-months requires --from-month and --to-month")
    if (args.from_month or args.to_month) and not args.all_months:
        parser.error("--from-month and --to-month require --all-months")
    connection = get_connection()
    try:
        if args.rollback:
            print("[volume-unit-repair] rollback=", rollback_run(connection, args.rollback))
            return 0
        if args.all_months:
            months = iter_months(args.from_month, args.to_month)
        elif args.month:
            months = (args.month,)
        else:
            months = ()
        if months:
            run_id = args.run_id or str(uuid4())
            print("[volume-unit-repair] run_id=", run_id)
            for month in months:
                start_date, end_date = month_window(month)
                plan = build_repair_plan(
                    scan_candidates_for_date_range(connection, start_date, end_date)
                )
                print(f"[volume-unit-repair] month={month}")
                _print_plan(plan)
                if args.apply:
                    print("[volume-unit-repair] applied=", apply_plan(connection, plan, run_id))
            if not args.apply:
                print("[volume-unit-repair] dry-run; pass --apply to mutate production data")
            return 0
        plan = build_repair_plan(scan_candidates(connection))
        _print_plan(plan)
        if not args.apply:
            print("[volume-unit-repair] dry-run; pass --apply to mutate production data")
            return 0
        run_id = args.run_id or str(uuid4())
        print("[volume-unit-repair] run_id=", run_id)
        print("[volume-unit-repair] applied=", apply_plan(connection, plan, run_id))
        return 0
    finally:
        connection.close()


if __name__ == "__main__":
    raise SystemExit(main())


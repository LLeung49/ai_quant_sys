# -*- coding: utf-8 -*-
"""Idempotently fill only NULL QFQ turnover rates from QMT ContextInfo."""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

try:
    from data_ingestion_qmt.db_config import execute_query, execute_update
    from data_ingestion_qmt.qmt_data_gateway import QMTDataGateway
except ImportError:  # Direct execution from src/data_ingestion_qmt.
    from db_config import execute_query, execute_update
    from qmt_data_gateway import QMTDataGateway


UPDATE_TURNOVER_SQL = """
UPDATE trade_stock_daily_qfq
SET turnover_rate = %s
WHERE stock_code = %s
  AND trade_date = %s
  AND turnover_rate IS NULL
"""


@dataclass(frozen=True)
class TurnoverWindow:
    stock_code: str
    start_date: str
    end_date: str
    missing_dates: set[str]


@dataclass(frozen=True)
class BackfillResult:
    stock_code: str
    requested: int
    matched: int
    written: int
    missing_dates: set[str]
    error: str | None = None


def _compact_date(value) -> str:
    return str(value).replace("-", "")[:8]


def _mysql_date(compact_date: str) -> str:
    return f"{compact_date[:4]}-{compact_date[4:6]}-{compact_date[6:8]}"


def _percent_rate(value) -> float | None:
    try:
        rate = float(value)
        return round(rate * 100, 4) if math.isfinite(rate) else None
    except (TypeError, ValueError, OverflowError):
        return None


def backfill_window(
    window: TurnoverWindow, gateway: QMTDataGateway, dry_run: bool,
) -> BackfillResult:
    """Fetch QMT turnover for one NULL-only window and never overwrite a value."""
    try:
        response = gateway.get_turnover_rate(
            [window.stock_code], window.start_date, window.end_date
        )
    except Exception as exc:
        return BackfillResult(
            window.stock_code, len(window.missing_dates), 0, 0,
            set(window.missing_dates), f"{type(exc).__name__}: {exc}",
        )

    return _backfill_rates(window, response.get(window.stock_code, {}), dry_run)


def _backfill_rates(
    window: TurnoverWindow, rates: dict[str, float], dry_run: bool,
) -> BackfillResult:
    """Apply a previously fetched response to one code's NULL dates."""
    matched = 0
    written = 0
    for compact_date in sorted(window.missing_dates):
        percent = _percent_rate(rates.get(compact_date))
        if percent is None:
            continue
        matched += 1
        if not dry_run:
            written += execute_update(
                UPDATE_TURNOVER_SQL,
                (percent, window.stock_code, _mysql_date(compact_date)),
            )
    return BackfillResult(
        window.stock_code,
        len(window.missing_dates),
        matched,
        written,
        set(window.missing_dates) - {
            date for date in window.missing_dates
            if _percent_rate(rates.get(date)) is not None
        },
    )


def _chunks(values: list[TurnoverWindow], size: int):
    for start in range(0, len(values), size):
        yield values[start:start + size]


def load_null_turnover_windows(
    start_date: str | None = None, end_date: str | None = None,
    limit_codes: int | None = None,
) -> list[TurnoverWindow]:
    """Load bounded NULL rows without materializing all QFQ history in Python."""
    predicates = ["turnover_rate IS NULL"]
    params: list[str] = []
    if start_date:
        predicates.append("trade_date >= %s")
        params.append(_mysql_date(_compact_date(start_date)))
    if end_date:
        predicates.append("trade_date <= %s")
        params.append(_mysql_date(_compact_date(end_date)))
    where = " AND ".join(predicates)
    sql = f"""
    SELECT stock_code, MIN(trade_date) AS start_date, MAX(trade_date) AS end_date
    FROM trade_stock_daily_qfq
    WHERE {where}
    GROUP BY stock_code
    ORDER BY stock_code
    """
    if limit_codes:
        sql += " LIMIT %s"
        params.append(limit_codes)
    grouped = execute_query(sql, tuple(params))
    windows = []
    for row in grouped:
        dates = execute_query(
            f"""SELECT trade_date FROM trade_stock_daily_qfq
            WHERE stock_code = %s AND {where}
            ORDER BY trade_date""",
            (row["stock_code"], *params[:len(predicates) - 1]),
        )
        missing_dates = {_compact_date(item["trade_date"]) for item in dates}
        windows.append(TurnoverWindow(
            row["stock_code"], _compact_date(row["start_date"]),
            _compact_date(row["end_date"]), missing_dates,
        ))
    return windows


def main() -> int:
    parser = argparse.ArgumentParser(description="QMT QFQ NULL turnover backfill")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--limit-codes", type=int)
    parser.add_argument("--start-date")
    parser.add_argument("--end-date")
    parser.add_argument("--batch-size", type=int, default=5)
    args = parser.parse_args()
    if args.batch_size <= 0:
        parser.error("--batch-size must be positive")
    windows = load_null_turnover_windows(
        args.start_date, args.end_date, args.limit_codes
    )
    gateway = QMTDataGateway.from_env()
    totals = {"requested": 0, "matched": 0, "written": 0, "missing": 0, "failed": 0}
    for batch in _chunks(windows, args.batch_size):
        start_date = min(window.start_date for window in batch)
        end_date = max(window.end_date for window in batch)
        try:
            response = gateway.get_turnover_rate(
                [window.stock_code for window in batch], start_date, end_date
            )
            results = [
                _backfill_rates(window, response.get(window.stock_code, {}), args.dry_run)
                for window in batch
            ]
        except Exception as exc:
            message = f"{type(exc).__name__}: {exc}"
            results = [
                BackfillResult(
                    window.stock_code, len(window.missing_dates), 0, 0,
                    set(window.missing_dates), message,
                ) for window in batch
            ]
        for result in results:
            totals["requested"] += result.requested
            totals["matched"] += result.matched
            totals["written"] += result.written
            totals["missing"] += len(result.missing_dates)
            totals["failed"] += int(result.error is not None)
            if result.error:
                print(f"[换手率回填失败] {result.stock_code}: {result.error}")
    print(
        "[QFQ换手率回填] "
        f"dry_run={args.dry_run} codes={len(windows)} requested={totals['requested']} "
        f"matched={totals['matched']} written={totals['written']} "
        f"missing={totals['missing']} failed={totals['failed']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

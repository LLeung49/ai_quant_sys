"""Canonical AKShare financial collector with PIT-safe persistence."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import date, timedelta
import json
import math
from pathlib import Path
import re
from typing import Callable, Sequence

import akshare as ak
import pandas as pd

from .akshare_financial_provider import AKShareFinancialProvider
from .db_config import execute_query, get_connection
from .financial_recovery.akshare_archive import archive_snapshot


PIT_INSERT_SQL = """
INSERT IGNORE INTO trade_stock_financial_raw_pit
(stock_code, source_table, report_date, announcement_date, period_type,
 revenue, net_profit, total_assets, total_equity, operating_cash_flow,
 eps, roe, gross_margin, metric_available_at, metric_lineage_json, date_evidence,
 pit_status, source_updated_at, source_hash, is_restated,
 source_verified, data_source)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

CAPITAL_INSERT_SQL = """
INSERT IGNORE INTO trade_stock_capital_pit
(stock_code, report_date, announcement_date, total_shares, circulating_shares,
 pit_status, source_hash, data_source)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""


@dataclass(frozen=True)
class FinancialCollectionResult:
    succeeded: int
    failed: int
    written_rows: int
    failures: tuple[dict[str, str], ...]
    quarantined_rows: int = 0
    quarantine: tuple[dict[str, str], ...] = ()


_A_SHARE_PATTERNS = (
    re.compile(r"^(?:000|001|002|003|300|301)[0-9]{3}\.SZ$"),
    re.compile(r"^(?:600|601|603|605|688|689)[0-9]{3}\.SH$"),
)


def is_a_share_stock_code(stock_code: str) -> bool:
    """Return whether a code is a Shanghai/Shenzhen A-share company."""

    return any(pattern.fullmatch(stock_code) for pattern in _A_SHARE_PATTERNS)


def _normalize_disclosure_code(value: object) -> str | None:
    digits = str(value or "").strip().zfill(6)
    if not re.fullmatch(r"[0-9]{6}", digits):
        return None
    exchange = "SH" if digits.startswith(("5", "6", "9")) else "SZ"
    stock_code = f"{digits}.{exchange}"
    return stock_code if is_a_share_stock_code(stock_code) else None


def _disclosure_periods(as_of_date: date) -> tuple[str, ...]:
    year = as_of_date.year
    return (
        f"{year - 1}年报",
        f"{year}一季",
        f"{year}半年报",
        f"{year}三季",
    )


def get_disclosed_stock_codes(
    *,
    as_of_date: date,
    lookback_days: int = 7,
    fetch_disclosure: Callable[..., pd.DataFrame] = ak.stock_report_disclosure,
) -> list[str]:
    """Return A-share companies with actual disclosures in a recent window."""

    if lookback_days < 1:
        raise ValueError("lookback_days must be positive")
    start_date = as_of_date - timedelta(days=lookback_days)
    codes: set[str] = set()
    received_valid_frame = False
    for period in _disclosure_periods(as_of_date):
        frame = fetch_disclosure(market="沪深京", period=period)
        if frame.empty or len(frame.columns) < 2:
            continue
        received_valid_frame = True
        code_column = "股票代码" if "股票代码" in frame.columns else frame.columns[0]
        actual_column = "实际披露" if "实际披露" in frame.columns else frame.columns[-1]
        actual_dates = pd.to_datetime(frame[actual_column], errors="coerce").dt.date
        for raw_code, actual_date in zip(frame[code_column], actual_dates):
            if pd.isna(actual_date) or not start_date <= actual_date <= as_of_date:
                continue
            stock_code = _normalize_disclosure_code(raw_code)
            if stock_code:
                codes.add(stock_code)
    if not received_valid_frame:
        raise ValueError("disclosure_provider_empty: all reporting periods returned no usable rows")
    return sorted(codes)


def get_stock_universe() -> list[str]:
    rows = execute_query(
        "SELECT DISTINCT stock_code FROM trade_stock_daily_raw "
        "WHERE stock_code REGEXP '^[0-9]{6}\\.(SH|SZ)$' ORDER BY stock_code"
    )
    return [
        stock_code
        for row in rows
        if is_a_share_stock_code(stock_code := str(row["stock_code"]))
    ]


def _validated_financial_row(row: dict) -> dict:
    """Reject incomplete source responses before opening a write transaction."""
    report = row["report_date"]
    announced = row["announcement_date"]
    if not isinstance(report, date) or not isinstance(announced, date) or announced <= report:
        raise ValueError("invalid financial announcement date")
    metric_date = row.get("metric_available_at", announced)
    if metric_date is not None and (not isinstance(metric_date, date) or
                                    metric_date > announced or metric_date <= report):
        raise ValueError("invalid financial metric date")
    if not re.fullmatch(r"[0-9a-f]{64}", str(row.get("source_hash") or "")):
        raise ValueError("invalid financial source hash")
    for field in ("revenue", "net_profit", "total_assets", "total_equity",
                  "operating_cash_flow"):
        value = row.get(field)
        try:
            valid = value is not None and not isinstance(value, bool) and math.isfinite(float(value))
        except (TypeError, ValueError, OverflowError):
            valid = False
        if not valid:
            raise ValueError(f"invalid financial core: {field}")
    if float(row["total_assets"]) <= 0:
        raise ValueError("invalid financial core: total_assets")
    normalized = dict(row)
    flags = []
    for field, limit in (("eps", 100), ("roe", 1000), ("gross_margin", 1000)):
        value = normalized.get(field)
        if value is None:
            continue
        try:
            valid = math.isfinite(float(value)) and abs(float(value)) <= limit
        except (TypeError, ValueError, OverflowError):
            valid = False
        if not valid:
            normalized[field] = None
            flags.append(field + "_outlier")
    normalized["metric_quality_flags"] = flags
    return normalized


def persist_financial_rows(
    rows: Sequence[dict], *, connection_factory: Callable = get_connection
) -> int:
    if not rows:
        return 0
    rows = [_validated_financial_row(row) for row in rows]
    connection = connection_factory()
    cursor = connection.cursor()
    written = 0
    try:
        for row in rows:
            cursor.execute(PIT_INSERT_SQL, (
                row["stock_code"], row["source_table"], row["report_date"],
                row["announcement_date"], row["period_type"], row.get("revenue"),
                row.get("net_profit"), row.get("total_assets"),
                row.get("total_equity"), row.get("operating_cash_flow"),
                row.get("eps"), row.get("roe"), row.get("gross_margin"),
                row.get("metric_available_at", row.get("announcement_date")),
                json.dumps({"original_announcement_date": str(row.get("original_announcement_date") or ""),
                            "metric_source": "akshare_eastmoney_current_snapshot",
                            "metric_quality_flags": row["metric_quality_flags"]}, ensure_ascii=False),
                "akshare_notice_or_update_date",
                row["pit_status"], row["source_updated_at"], row["source_hash"],
                1 if row.get("is_restated") else 0,
                1 if row.get("source_verified") else 0,
                row.get("data_source", "akshare"),
            ))
            written += max(0, cursor.rowcount)
        connection.commit()
        return written
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()
        connection.close()


def persist_capital_rows(
    rows: Sequence[dict], *, connection_factory: Callable = get_connection
) -> int:
    if not rows:
        return 0
    connection = connection_factory()
    cursor = connection.cursor()
    written = 0
    try:
        for row in rows:
            cursor.execute(CAPITAL_INSERT_SQL, (
                row["stock_code"], row["report_date"], row["announcement_date"],
                row.get("total_shares"), row.get("circulating_shares"),
                row["pit_status"], row["source_hash"], row.get("data_source", "akshare"),
            ))
            written += max(0, cursor.rowcount)
        connection.commit()
        return written
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()
        connection.close()


def run_collection(
    provider: AKShareFinancialProvider,
    stock_codes: Sequence[str],
    *,
    as_of_date: date,
    dry_run: bool,
    workers: int = 4,
    persist: Callable[[Sequence[dict]], int] = persist_financial_rows,
    persist_capital: Callable[[Sequence[dict]], int] = persist_capital_rows,
    archive_root: Path | None = None,
    recent_announcement_days: int | None = None,
) -> FinancialCollectionResult:
    if workers < 1:
        raise ValueError("workers must be positive")
    if recent_announcement_days is not None and recent_announcement_days < 1:
        raise ValueError("recent_announcement_days must be positive")
    succeeded = 0
    written_rows = 0
    failures: list[dict[str, str]] = []
    quarantine: list[dict[str, str]] = []

    def collect_one(stock_code: str) -> tuple[int, str | None, list[dict[str, str]]]:
        source_rows = provider.fetch(stock_code, as_of_date=as_of_date)
        if not dry_run and archive_root is not None:
            archive_snapshot(source_rows, stock_code=stock_code, as_of_date=as_of_date,
                             kind="financial", root=archive_root)
        recent_start = (as_of_date - timedelta(days=recent_announcement_days)
                        if recent_announcement_days is not None else None)
        rejected: list[dict[str, str]] = []
        rows = []
        for source_row in source_rows:
            try:
                rows.append(_validated_financial_row(source_row))
            except (ValueError, KeyError) as exc:
                announced = source_row.get("announcement_date")
                if not (isinstance(announced, date) and recent_start is not None
                        and announced < recent_start):
                    raise
                rejected.append({
                    "stock_code": stock_code,
                    "report_date": str(source_row.get("report_date")),
                    "announcement_date": announced.isoformat(),
                    "reason": str(exc),
                })
        if not rows:
            raise ValueError(f"financial_provider_empty: {stock_code}")
        if any(row["announcement_date"] > as_of_date for row in rows):
            raise ValueError(f"future_financial_announcement: {stock_code}")
        if recent_announcement_days is not None:
            start = as_of_date - timedelta(days=recent_announcement_days)
            if not any(start <= row["announcement_date"] <= as_of_date for row in rows):
                raise ValueError(f"recent_disclosure_missing: {stock_code}")
        written = 0 if dry_run else persist(rows)
        capital_fetcher = getattr(provider, "fetch_capital", None)
        if not callable(capital_fetcher):
            return written, None, rejected
        try:
            capital_rows = capital_fetcher(stock_code, as_of_date=as_of_date)
            if not dry_run:
                if archive_root is not None:
                    archive_snapshot(capital_rows, stock_code=stock_code,
                                     as_of_date=as_of_date, kind="capital",
                                     root=archive_root)
                written += persist_capital(capital_rows)
            return written, None, rejected
        except Exception as exc:
            return written, f"capital: {type(exc).__name__}: {exc}", rejected

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(collect_one, stock_code): stock_code
            for stock_code in stock_codes
        }
        for index, future in enumerate(as_completed(futures), start=1):
            stock_code = futures[future]
            try:
                rows_written, capital_error, rejected = future.result()
                written_rows += rows_written
                quarantine.extend(rejected)
                if capital_error:
                    failures.append({"stock_code": stock_code, "error": capital_error})
                else:
                    succeeded += 1
            except Exception as exc:
                failures.append({
                    "stock_code": stock_code,
                    "error": f"{type(exc).__name__}: {exc}",
                })
            if index % 100 == 0 or index == len(stock_codes):
                print(
                    f"[financial progress] completed={index}/{len(stock_codes)} "
                    f"succeeded={succeeded} failed={len(failures)}",
                    flush=True,
                )
    return FinancialCollectionResult(
        succeeded=succeeded,
        failed=len(failures),
        written_rows=written_rows,
        failures=tuple(sorted(failures, key=lambda item: item["stock_code"])),
        quarantined_rows=len(quarantine),
        quarantine=tuple(sorted(quarantine, key=lambda item: (
            item["stock_code"], item["report_date"]))),
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Collect PIT-safe financial data from AKShare")
    parser.add_argument("--as-of-date", type=date.fromisoformat, default=date.today())
    scope = parser.add_mutually_exclusive_group()
    scope.add_argument("--stock-code", action="append", dest="stock_codes")
    scope.add_argument(
        "--all-stocks",
        action="store_true",
        help="scan the full Shanghai/Shenzhen A-share universe (manual recovery only)",
    )
    parser.add_argument("--disclosure-lookback-days", type=int, default=7)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--archive-dir", type=Path,
                        default=Path("reports/financial-audit/akshare-daily"))
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.stock_codes:
        selection_mode = "explicit"
        stock_codes = sorted(set(args.stock_codes))
    elif args.all_stocks:
        selection_mode = "all_stocks"
        stock_codes = get_stock_universe()
    else:
        selection_mode = "recent_disclosures"
        try:
            stock_codes = get_disclosed_stock_codes(
                as_of_date=args.as_of_date,
                lookback_days=args.disclosure_lookback_days,
            )
        except ValueError as exc:
            print(f"[financial failed] {exc}", flush=True)
            return 2
    if args.limit is not None:
        if args.limit < 1:
            print("[financial failed] --limit must be positive", flush=True)
            return 2
        stock_codes = stock_codes[:args.limit]
    if not stock_codes:
        print(json.dumps({
            "provider": "akshare",
            "selection_mode": selection_mode,
            "as_of_date": args.as_of_date.isoformat(),
            "codes": 0,
            "succeeded": 0,
            "failed": 0,
            "written_rows": 0,
            "dry_run": args.dry_run,
            "failures": [],
        }, ensure_ascii=False, indent=2))
        return 0
    result = run_collection(
        AKShareFinancialProvider(), stock_codes,
        as_of_date=args.as_of_date, dry_run=args.dry_run, workers=args.workers,
        archive_root=args.archive_dir,
        recent_announcement_days=(args.disclosure_lookback_days
                                  if selection_mode == "recent_disclosures" else None),
    )
    print(json.dumps({
        "provider": "akshare",
        "selection_mode": selection_mode,
        "as_of_date": args.as_of_date.isoformat(),
        "codes": len(stock_codes),
        "succeeded": result.succeeded,
        "failed": result.failed,
        "written_rows": result.written_rows,
        "dry_run": args.dry_run,
        "failures": result.failures,
        "quarantined_rows": result.quarantined_rows,
        "quarantine": result.quarantine,
    }, ensure_ascii=False, indent=2))
    return 1 if result.failed else 0


if __name__ == "__main__":
    raise SystemExit(main())

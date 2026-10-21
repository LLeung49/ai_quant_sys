# -*- coding: utf-8 -*-
"""AKShare raw, QFQ, and HFQ daily-market collector.

The one-time recovery path lives in run_market_rebuild.py and may use the
temporary bridge.  This operator-facing collector is the long-term AKShare
path and only persists complete, validated three-projection batches.
"""

import argparse
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path
import sys
from typing import Sequence

if __package__:
    from .akshare_market_provider import AKShareMarketProvider
    from .db_config import execute_query
    from .market_provider import MarketProvider
    from .market_gap import find_missing_market_codes
    from .market_row_validation import validate_projection_batch
    from .price_projection_store import write_projection_batch
else:  # Direct script execution or importlib file loading.
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from data_ingestion.akshare_market_provider import AKShareMarketProvider
    from data_ingestion.db_config import execute_query
    from data_ingestion.market_provider import MarketProvider
    from data_ingestion.market_gap import find_missing_market_codes
    from data_ingestion.market_row_validation import validate_projection_batch
    from data_ingestion.price_projection_store import write_projection_batch


MODES = ("none", "front", "back")
DEFAULT_LOOKBACK_DAYS = 10

SELECT_CODE_UNIVERSE_SQL = """
SELECT stock_code FROM trade_stock_daily_raw
UNION
SELECT stock_code FROM trade_stock_daily_qfq
UNION
SELECT stock_code FROM trade_stock_daily_bfq
ORDER BY stock_code
"""


@dataclass(frozen=True)
class CollectionResult:
    succeeded: int
    failed: int
    written_rows: int
    failures: tuple[dict[str, object], ...]
    pending: tuple[dict[str, object], ...] = ()


def _parse_date(value: str) -> date:
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("date must use YYYY-MM-DD") from exc


def get_code_universe() -> list[str]:
    return [str(row["stock_code"]) for row in execute_query(SELECT_CODE_UNIVERSE_SQL)]


def get_latest_suspended_codes(stock_codes: Sequence[str]) -> set[str]:
    """Return codes whose latest persisted raw bar is explicitly suspended."""
    if not stock_codes:
        return set()
    placeholders = ",".join(["%s"] * len(stock_codes))
    rows = execute_query(
        "SELECT latest.stock_code FROM ("
        "SELECT stock_code, MAX(trade_date) AS latest_date "
        "FROM trade_stock_daily_raw GROUP BY stock_code"
        ") AS latest JOIN trade_stock_daily_raw AS raw "
        "ON raw.stock_code=latest.stock_code AND raw.trade_date=latest.latest_date "
        f"WHERE raw.suspend_flag=1 AND latest.stock_code IN ({placeholders})",
        tuple(stock_codes),
    )
    return {str(row["stock_code"]) for row in rows}


def _is_expected_suspended_empty(
    stock_code: str,
    failures: dict[str, object],
    accepted_suspended_codes: set[str],
) -> bool:
    return (
        stock_code in accepted_suspended_codes
        and bool(failures)
        and all("empty_response" in str(detail).lower() for detail in failures.values())
    )


def run_collection(
    provider: MarketProvider,
    stock_codes: Sequence[str],
    start_date: date,
    end_date: date,
    *,
    dry_run: bool,
    workers: int = 1,
    accepted_suspended_codes: set[str] | None = None,
) -> CollectionResult:
    """Fetch complete batches and write no mode unless all modes validate."""
    if workers < 1:
        raise ValueError("workers must be positive")
    accepted_suspended_codes = accepted_suspended_codes or set()

    def collect_one(stock_code: str) -> tuple[bool, int, dict[str, object] | None]:
        try:
            batch = provider.fetch_batch(stock_code, start_date, end_date)
        except BaseException as exc:
            return False, 0, {
                "stock_code": stock_code,
                "reason": "provider_failed",
                "details": f"{type(exc).__name__}: {exc}",
            }
        if not batch.is_complete:
            if _is_expected_suspended_empty(
                stock_code, dict(batch.failures), accepted_suspended_codes
            ):
                return True, 0, None
            return False, 0, {
                "stock_code": stock_code,
                "reason": "provider_batch_incomplete",
                "details": dict(batch.failures),
            }
        missing_modes = [
            mode for mode in MODES
            if end_date.isoformat() not in {
                str(row["trade_date"])[:10]
                for row in batch.rows_by_mode.get(mode, ())
            }
        ]
        if missing_modes:
            return False, 0, {
                "stock_code": stock_code,
                "reason": "missing_target_date",
                "details": {"target_date": end_date.isoformat(), "modes": missing_modes},
            }
        validation = validate_projection_batch(batch.rows_by_mode)
        if not validation.is_valid:
            return False, 0, {
                "stock_code": stock_code,
                "reason": "batch_validation_failed",
                "details": [
                    {
                        "code": issue.code,
                        "date": issue.trade_date,
                        "mode": issue.mode,
                        "field": issue.field,
                    }
                    for issue in validation.issues
                    if issue.severity == "error"
                ],
            }

        if not dry_run:
            try:
                written = write_projection_batch(batch.rows_by_mode, end_date)
            except Exception as exc:
                return False, 0, {
                    "stock_code": stock_code,
                    "reason": "persistence_failed",
                    "details": f"{type(exc).__name__}: {exc}",
                }
        else:
            written = 0
        return True, written, None

    succeeded = 0
    written_rows = 0
    failures: list[dict[str, object]] = []
    pending: list[dict[str, object]] = []
    with ThreadPoolExecutor(max_workers=workers) as executor:
        results = executor.map(collect_one, stock_codes)
        for completed, (ok, written, failure) in enumerate(results, start=1):
            if ok:
                succeeded += 1
                written_rows += written
            elif failure is not None and failure["reason"] == "missing_target_date":
                pending.append(failure)
            elif failure is not None:
                failures.append(failure)
            if completed % 100 == 0 or completed == len(stock_codes):
                print(
                    f"[行情进度] completed={completed}/{len(stock_codes)} "
                    f"succeeded={succeeded} failed={len(failures)} pending={len(pending)}",
                    flush=True,
                )

    if workers > 1 and failures:
        retry_failures: list[dict[str, object]] = []
        initial_failures = failures
        print(
            f"[行情重试] retrying={len(initial_failures)} workers=1",
            flush=True,
        )
        for failure in initial_failures:
            stock_code = str(failure["stock_code"])
            ok, written, retry_failure = collect_one(stock_code)
            if ok:
                succeeded += 1
                written_rows += written
            elif retry_failure is not None and retry_failure["reason"] == "missing_target_date":
                pending.append(retry_failure)
            elif retry_failure is not None:
                retry_failures.append(retry_failure)
        failures = retry_failures

    return CollectionResult(
        succeeded=succeeded,
        failed=len(failures),
        written_rows=written_rows,
        failures=tuple(failures),
        pending=tuple(pending),
    )


def build_parser() -> argparse.ArgumentParser:
    today = date.today()
    parser = argparse.ArgumentParser(
        description="Collect validated raw/QFQ/HFQ daily prices from AKShare"
    )
    parser.add_argument("--provider", choices=("akshare",), default="akshare")
    parser.add_argument("--stock-code", action="append", dest="stock_codes")
    parser.add_argument("--missing-only", action="store_true", help="Only retry symbols present on the prior session but missing on the target date")
    parser.add_argument(
        "--start-date",
        type=_parse_date,
        default=today - timedelta(days=DEFAULT_LOOKBACK_DAYS),
    )
    parser.add_argument("--end-date", type=_parse_date, default=today)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--max-attempts", type=int, default=3)
    parser.add_argument("--request-timeout", type=float, default=30.0)
    parser.add_argument("--workers", type=int, default=8)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.start_date > args.end_date:
        print("[行情失败] start-date must not exceed end-date", flush=True)
        return 2
    if args.missing_only and args.stock_codes:
        print("[行情失败] --missing-only cannot be combined with --stock-code", flush=True)
        return 2
    if args.missing_only:
        prior, missing = find_missing_market_codes(args.end_date)
        stock_codes = missing
        print(f"[行情补采] prior={prior} target={args.end_date} codes={len(stock_codes)}", flush=True)
        if not stock_codes:
            print("[行情补采] 无待补代码", flush=True)
            return 0
    else:
        stock_codes = sorted(set(args.stock_codes or get_code_universe()))
    if not stock_codes:
        print("[行情失败] no stock codes available", flush=True)
        return 2

    provider = AKShareMarketProvider(
        max_attempts=args.max_attempts,
        request_timeout=args.request_timeout,
    )
    result = run_collection(
        provider,
        stock_codes,
        args.start_date,
        args.end_date,
        dry_run=args.dry_run,
        workers=args.workers,
        accepted_suspended_codes=get_latest_suspended_codes(stock_codes),
    )
    print(
        f"[行情完成] provider=akshare codes={len(stock_codes)} "
        f"succeeded={result.succeeded} failed={result.failed} "
        f"pending={len(result.pending)} written_rows={result.written_rows} dry_run={args.dry_run}",
        flush=True,
    )
    for failure in result.failures[:20]:
        print(f"[行情失败] {failure}", flush=True)
    if len(result.failures) > 20:
        print(f"[行情失败] 还有 {len(result.failures) - 20} 只未逐条显示；请使用每日入口的补采模式", flush=True)
    if result.pending:
        print(
            f"[行情待补] {len(result.pending)} 只未返回 {args.end_date.isoformat()} 行情；"
            "下游会跳过缺日标的，请稍后用每日入口 -RetryMissingMarket 补采",
            flush=True,
        )
    return 1 if result.failed else 0


if __name__ == "__main__":
    raise SystemExit(main())

# -*- coding: utf-8 -*-
"""AKShare raw, QFQ, and HFQ daily-market collector.

The one-time recovery path lives in run_market_rebuild.py and may use the
temporary bridge.  This operator-facing collector is the long-term AKShare
path and only persists complete, validated three-projection batches.
"""

import argparse
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path
import sys
from typing import Sequence

if __package__:
    from .akshare_market_provider import AKShareMarketProvider
    from .db_config import execute_query
    from .market_provider import MarketProvider
    from .market_row_validation import validate_projection_batch
    from .price_projection_store import write_daily_rows
else:  # Direct script execution or importlib file loading.
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from data_ingestion.akshare_market_provider import AKShareMarketProvider
    from data_ingestion.db_config import execute_query
    from data_ingestion.market_provider import MarketProvider
    from data_ingestion.market_row_validation import validate_projection_batch
    from data_ingestion.price_projection_store import write_daily_rows


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


def _parse_date(value: str) -> date:
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("date must use YYYY-MM-DD") from exc


def get_code_universe() -> list[str]:
    return [str(row["stock_code"]) for row in execute_query(SELECT_CODE_UNIVERSE_SQL)]


def run_collection(
    provider: MarketProvider,
    stock_codes: Sequence[str],
    start_date: date,
    end_date: date,
    *,
    dry_run: bool,
) -> CollectionResult:
    """Fetch complete batches and write no mode unless all modes validate."""
    succeeded = 0
    written_rows = 0
    failures: list[dict[str, object]] = []

    for stock_code in stock_codes:
        batch = provider.fetch_batch(stock_code, start_date, end_date)
        if not batch.is_complete:
            failures.append({
                "stock_code": stock_code,
                "reason": "provider_batch_incomplete",
                "details": dict(batch.failures),
            })
            continue
        validation = validate_projection_batch(batch.rows_by_mode)
        if not validation.is_valid:
            failures.append({
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
            })
            continue

        if not dry_run:
            try:
                for mode in MODES:
                    written_rows += write_daily_rows(
                        mode,
                        batch.rows_by_mode[mode],
                        adjustment_asof=end_date if mode != "none" else None,
                    )
            except Exception as exc:
                failures.append({
                    "stock_code": stock_code,
                    "reason": "persistence_failed",
                    "details": f"{type(exc).__name__}: {exc}",
                })
                continue
        succeeded += 1

    return CollectionResult(
        succeeded=succeeded,
        failed=len(failures),
        written_rows=written_rows,
        failures=tuple(failures),
    )


def build_parser() -> argparse.ArgumentParser:
    today = date.today()
    parser = argparse.ArgumentParser(
        description="Collect validated raw/QFQ/HFQ daily prices from AKShare"
    )
    parser.add_argument("--provider", choices=("akshare",), default="akshare")
    parser.add_argument("--stock-code", action="append", dest="stock_codes")
    parser.add_argument(
        "--start-date",
        type=_parse_date,
        default=today - timedelta(days=DEFAULT_LOOKBACK_DAYS),
    )
    parser.add_argument("--end-date", type=_parse_date, default=today)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--max-attempts", type=int, default=3)
    parser.add_argument("--request-timeout", type=float, default=30.0)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.start_date > args.end_date:
        print("[行情失败] start-date must not exceed end-date", flush=True)
        return 2
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
    )
    print(
        f"[行情完成] provider=akshare codes={len(stock_codes)} "
        f"succeeded={result.succeeded} failed={result.failed} "
        f"written_rows={result.written_rows} dry_run={args.dry_run}",
        flush=True,
    )
    for failure in result.failures:
        print(f"[行情失败] {failure}", flush=True)
    return 1 if result.failed else 0


if __name__ == "__main__":
    raise SystemExit(main())

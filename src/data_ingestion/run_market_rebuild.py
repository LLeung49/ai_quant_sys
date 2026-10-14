"""Resumable staging-only market reconstruction runner."""

from __future__ import annotations

import argparse
from datetime import date, datetime
import json
from pathlib import Path

from .db_config import execute_query
from .market_rebuild_store import RebuildStore
from .qmt_bootstrap_provider import QMTBootstrapProvider


CODE_UNIVERSE_SQL = """
SELECT stock_code FROM trade_stock_daily_raw
UNION SELECT stock_code FROM trade_stock_daily_qfq
UNION SELECT stock_code FROM trade_stock_daily_bfq
ORDER BY stock_code
"""


def _parse_date(value: str) -> date:
    return date.fromisoformat(value)


def _chunks(values: list[str], size: int):
    for offset in range(0, len(values), size):
        yield values[offset:offset + size]


def _load_codes(explicit: list[str] | None, codes_file: Path | None) -> list[str]:
    codes = list(explicit or [])
    if codes_file:
        codes.extend(
            line.strip() for line in codes_file.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.lstrip().startswith("#")
        )
    if not codes:
        codes = [str(row["stock_code"]) for row in execute_query(CODE_UNIVERSE_SQL)]
    return sorted(set(codes))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Rebuild market prices into staging tables")
    parser.add_argument("--provider", choices=("qmt-bootstrap",), default="qmt-bootstrap")
    parser.add_argument("--batch-id", default=datetime.now().strftime("market-%Y%m%d-%H%M%S"))
    parser.add_argument("--start-date", type=_parse_date, default=date(2015, 1, 1))
    parser.add_argument("--end-date", type=_parse_date, required=True)
    parser.add_argument("--stock-code", action="append", dest="stock_codes")
    parser.add_argument("--codes-file", type=Path)
    parser.add_argument("--batch-size", type=int, default=20)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--no-resume", action="store_true")
    parser.add_argument("--report", type=Path)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.batch_size <= 0 or args.start_date > args.end_date:
        return 2
    codes = _load_codes(args.stock_codes, args.codes_file)
    if args.limit is not None:
        codes = codes[:args.limit]
    provider = QMTBootstrapProvider()
    store = RebuildStore(batch_id=args.batch_id)
    if not args.dry_run and not args.no_resume:
        codes = [code for code in codes if code not in store.completed_codes()]

    report = {
        "batch_id": args.batch_id,
        "provider": "qmt_bridge",
        "start_date": args.start_date.isoformat(),
        "end_date": args.end_date.isoformat(),
        "dry_run": args.dry_run,
        "requested_codes": len(codes),
        "complete": [],
        "failed": [],
        "rows": 0,
        "gaps": 0,
    }
    for code_batch in _chunks(codes, args.batch_size):
        batches = provider.fetch_batches(code_batch, args.start_date, args.end_date)
        for code in code_batch:
            batch = batches[code]
            if not batch.is_complete:
                detail = json.dumps(batch.failures, ensure_ascii=False)
                report["failed"].append({"stock_code": code, "detail": detail})
                if not args.dry_run:
                    store.record_failure(
                        code, args.start_date, args.end_date, "qmt_bridge", detail
                    )
                continue
            if args.dry_run:
                report["complete"].append(code)
                report["rows"] += sum(len(rows) for rows in batch.rows_by_mode.values())
                report["gaps"] += len(batch.gaps)
                continue
            try:
                result = store.persist_validated_batch(batch)
            except Exception as exc:
                detail = f"{type(exc).__name__}: {exc}"
                report["failed"].append({"stock_code": code, "detail": detail})
                store.record_failure(
                    code, args.start_date, args.end_date, "qmt_bridge", detail
                )
            else:
                report["complete"].append(code)
                report["rows"] += result.rows_written
                report["gaps"] += result.gaps_recorded
        print(
            f"[重建进度] complete={len(report['complete'])} "
            f"failed={len(report['failed'])} rows={report['rows']} gaps={report['gaps']}",
            flush=True,
        )
    report_path = args.report or Path("reports/market-rebuild") / args.batch_id / "run.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    return 1 if report["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())

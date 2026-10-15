"""Resumable staging-only market reconstruction runner."""

from __future__ import annotations

import argparse
from datetime import date, datetime
import hashlib
import json
from pathlib import Path
import shutil
import time

from .akshare_market_provider import AKShareMarketProvider
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


def has_minimum_free_space(path: Path | str, minimum_gib: float) -> bool:
    return shutil.disk_usage(path).free >= minimum_gib * 1024**3


def remaining_codes(codes: list[str], store: RebuildStore) -> list[str]:
    finished = store.completed_codes() | store.excluded_codes()
    return [code for code in codes if code not in finished]


def initialize_session_codes(
    codes: list[str],
    store: RebuildStore,
    *,
    dry_run: bool,
    no_resume: bool,
    limit: int | None,
) -> tuple[list[str], str]:
    """Persist/hash the full universe before limiting one session's work."""

    universe_sha256 = hashlib.sha256(
        "".join(f"{code}\n" for code in codes).encode("utf-8")
    ).hexdigest()
    session_codes = list(codes)
    if not dry_run:
        universe_sha256 = store.prepare_universe(codes)
        if not no_resume:
            session_codes = remaining_codes(codes, store)
    if limit is not None:
        session_codes = session_codes[:limit]
    return session_codes, universe_sha256


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
    parser.add_argument("--max-batches", type=int)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--no-resume", action="store_true")
    parser.add_argument("--report", type=Path)
    parser.add_argument("--disk-path", type=Path, default=Path.cwd().anchor or Path("."))
    parser.add_argument("--min-free-gib", type=float, default=5.0)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.batch_size <= 0 or args.start_date > args.end_date:
        return 2
    codes = _load_codes(args.stock_codes, args.codes_file)
    provider = QMTBootstrapProvider()
    fallback_provider = AKShareMarketProvider(max_attempts=1, request_timeout=15.0)
    store = RebuildStore(batch_id=args.batch_id)
    codes, universe_sha256 = initialize_session_codes(
        codes,
        store,
        dry_run=args.dry_run,
        no_resume=args.no_resume,
        limit=args.limit,
    )

    report_path = args.report or Path("reports/market-rebuild") / args.batch_id / "run.json"
    progress_path = report_path.with_suffix(".progress.jsonl")
    progress_path.parent.mkdir(parents=True, exist_ok=True)

    def emit_progress(event: str, **detail) -> None:
        record = {
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "event": event,
            **detail,
        }
        with progress_path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")

    emit_progress("session_start", remaining_codes=len(codes))
    report = {
        "batch_id": args.batch_id,
        "provider": "qmt_bridge",
        "start_date": args.start_date.isoformat(),
        "end_date": args.end_date.isoformat(),
        "dry_run": args.dry_run,
        "requested_codes": len(codes),
        "universe_sha256": universe_sha256,
        "complete": [],
        "failed": [],
        "akshare_replacements": [],
        "rows": 0,
        "gaps": 0,
        "batch_timings": [],
    }
    for batch_number, code_batch in enumerate(_chunks(codes, args.batch_size), start=1):
        if args.max_batches is not None and batch_number > args.max_batches:
            emit_progress("session_limit_reached", max_batches=args.max_batches)
            break
        if not has_minimum_free_space(args.disk_path, args.min_free_gib):
            report["failed"].append({
                "stock_code": "__disk_guard__",
                "detail": (
                    f"free space below {args.min_free_gib:.2f} GiB "
                    f"on {args.disk_path}"
                ),
            })
            break
        batch_started = time.perf_counter()
        print(
            f"[重建阶段] fetch_start first={code_batch[0]} "
            f"last={code_batch[-1]} codes={len(code_batch)}",
            flush=True,
        )
        emit_progress(
            "fetch_start", first_code=code_batch[0], last_code=code_batch[-1],
            codes=len(code_batch),
        )
        batches = provider.fetch_batches(code_batch, args.start_date, args.end_date)
        fetch_seconds = time.perf_counter() - batch_started
        print(f"[重建阶段] qmt_fetch_done seconds={fetch_seconds:.2f}", flush=True)
        emit_progress("qmt_fetch_done", seconds=round(fetch_seconds, 3))
        ready = []
        for code in code_batch:
            batch = batches[code]
            if not batch.is_complete:
                qmt_failures = dict(batch.failures)
                replacement = fallback_provider.fetch_batch(
                    code, batch.start_date, batch.end_date
                )
                if replacement.is_complete:
                    batch = replacement
                    report["akshare_replacements"].append({
                        "stock_code": code,
                        "qmt_failures": qmt_failures,
                        "interfaces": replacement.provenance.get("interfaces", {}),
                    })
                else:
                    detail = json.dumps({
                        "qmt": qmt_failures,
                        "akshare": replacement.failures,
                    }, ensure_ascii=False)
                    report["failed"].append({
                        "stock_code": code, "detail": detail,
                    })
                    if not args.dry_run:
                        store.record_failure(
                            code, batch.start_date, batch.end_date,
                            "qmt_bridge+akshare", detail,
                        )
                    continue
            if args.dry_run:
                report["complete"].append(code)
                report["rows"] += sum(len(rows) for rows in batch.rows_by_mode.values())
                report["gaps"] += len(batch.gaps)
                continue
            ready.append(batch)
        fallback_seconds = time.perf_counter() - batch_started - fetch_seconds
        if ready and not args.dry_run:
            persist_started = time.perf_counter()
            print(f"[重建阶段] persist_start codes={len(ready)}", flush=True)
            emit_progress("persist_start", codes=len(ready))
            try:
                results = store.persist_validated_batches(ready)
            except Exception as exc:
                # Preserve per-code visibility if a bulk transaction fails.
                for batch in ready:
                    try:
                        result = store.persist_validated_batch(batch)
                    except Exception as isolated_exc:
                        detail = f"{type(isolated_exc).__name__}: {isolated_exc}"
                        report["failed"].append({
                            "stock_code": batch.stock_code, "detail": detail,
                        })
                        store.record_failure(
                            batch.stock_code, args.start_date, args.end_date,
                            "qmt_bridge", detail,
                        )
                    else:
                        report["complete"].append(batch.stock_code)
                        report["rows"] += result.rows_written
                        report["gaps"] += result.gaps_recorded
            else:
                for result in results:
                    report["complete"].append(result.stock_code)
                    report["rows"] += result.rows_written
                    report["gaps"] += result.gaps_recorded
            persist_seconds = time.perf_counter() - persist_started
        else:
            persist_seconds = 0.0
        report["batch_timings"].append({
            "first_code": code_batch[0],
            "last_code": code_batch[-1],
            "codes": len(code_batch),
            "qmt_fetch_seconds": round(fetch_seconds, 3),
            "fallback_seconds": round(fallback_seconds, 3),
            "persist_seconds": round(persist_seconds, 3),
            "total_seconds": round(time.perf_counter() - batch_started, 3),
        })
        emit_progress(
            "batch_done", complete=len(report["complete"]),
            failed=len(report["failed"]), rows=report["rows"],
            gaps=report["gaps"], timing=report["batch_timings"][-1],
        )
        print(
            f"[重建进度] complete={len(report['complete'])} "
            f"failed={len(report['failed'])} rows={report['rows']} gaps={report['gaps']}",
            flush=True,
        )
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    return 1 if report["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())

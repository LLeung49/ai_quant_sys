"""Daily pipeline: financial data collection + Repair Alpha scoring.

This script is the operator-facing entry point for the Phase 4 / Repair
Alpha pipeline.  It runs two stages in order:

1. :mod:`data_ingestion_qmt.2-财务数据采集` -- the legacy financial data
   collector.  This script writes to ``trade_stock_financial`` AND, after
   the Phase 4.5 dual-write patch, to ``trade_stock_financial_raw_pit``.
2. :mod:`morning_conference_qmt.sector_rotation2.research.stock_alpha.run_repair_daily`
   -- the Repair Alpha runner.  By default the runner uses
   ``PIT_ESTIMATED`` rows (the legacy collector does not have
   announcement_date).  Pass ``--allow-estimated-pit`` to consume them.

Usage
-----

::

    # Default: today, latest live snapshot, no estimated
    python -m data_ingestion_qmt.run_daily_pipeline

    # Backfill a historical date with estimated PIT (legacy data)
    python -m data_ingestion_qmt.run_daily_pipeline \\
        --as-of-date 2026-08-17 --mode backfill --allow-estimated-pit

    # Single sector smoke test
    python -m data_ingestion_qmt.run_daily_pipeline \\
        --as-of-date 2026-08-17 --mode backfill --sector "专业服务"

The pipeline is best-effort: a failure in the collector does not abort
the Repair Alpha run, and vice versa.  Operator can scan the printed
counters to confirm both stages emitted the expected row counts.
"""

from __future__ import annotations

import argparse
import importlib
import sys
import time
from datetime import date, datetime
from typing import Any


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Daily Phase 4 / Repair Alpha pipeline: collector + Repair Alpha",
    )
    parser.add_argument("--as-of-date", help="Target date (ISO YYYY-MM-DD)")
    parser.add_argument(
        "--mode",
        choices=("live_shadow", "backfill"),
        help="Snapshot mode for the Repair Alpha runner (default: live_shadow)",
    )
    parser.add_argument("--today", help="Override the LIVE_SHADOW today gate")
    parser.add_argument(
        "--level",
        type=int,
        choices=(1, 2),
        default=2,
        help="SW sector level (default: 2)",
    )
    parser.add_argument(
        "--sector",
        help="Limit the Repair Alpha runner to one upstream sector name",
    )
    parser.add_argument(
        "--workers", type=int, default=4, help="Repair Alpha worker pool size",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Pass --dry-run to the Repair Alpha runner (no PIT persist)",
    )
    parser.add_argument(
        "--allow-estimated-pit",
        action="store_true",
        help="Pass --allow-estimated-pit to the Repair Alpha runner (consume legacy rows)",
    )
    parser.add_argument(
        "--skip-collector",
        action="store_true",
        help="Skip the financial data collector (debug only)",
    )
    parser.add_argument(
        "--skip-repair",
        action="store_true",
        help="Skip the Repair Alpha runner (debug only)",
    )
    return parser


def run_collector(args: argparse.Namespace) -> int:
    """Invoke the legacy financial collector as ``2-财务数据采集.main``.

    The collector is a module under :mod:`data_ingestion`.  We import it
    dynamically so the pipeline can run before the legacy script has
    been invoked manually.
    """

    print("=" * 60)
    print(f"[1/2] Financial data collection start: {datetime.now().isoformat()}")
    print("=" * 60)
    t0 = time.time()
    module = importlib.import_module("data_ingestion_qmt.2-财务数据采集")
    # The collector's main() ignores CLI args; it always runs in full
    # (or test-mode) mode.  We call it directly so the entry point
    # propagates sys.argv cleanly.
    saved_argv = sys.argv
    sys.argv = ["2-财务数据采集"]
    try:
        module.main()
    finally:
        sys.argv = saved_argv
    elapsed = time.time() - t0
    print(f"[1/2] Collector done in {elapsed:.1f}s")
    return 0


def run_repair_runner(args: argparse.Namespace) -> int:
    """Invoke the Repair Alpha runner with the CLI flags forwarded."""

    print("=" * 60)
    print(f"[2/2] Repair Alpha runner start: {datetime.now().isoformat()}")
    print("=" * 60)
    t0 = time.time()
    module = importlib.import_module(
        "morning_conference_qmt.sector_rotation2.research.stock_alpha.run_repair_daily"
    )
    runner_args: list[str] = []
    if args.as_of_date:
        runner_args += ["--as-of-date", args.as_of_date]
    else:
        runner_args += ["--as-of-date", date.today().isoformat()]
    if args.mode:
        runner_args += ["--mode", args.mode]
    if args.today:
        runner_args += ["--today", args.today]
    runner_args += ["--level", str(args.level)]
    if args.sector:
        runner_args += ["--sector", args.sector]
    runner_args += ["--workers", str(args.workers)]
    if args.dry_run:
        runner_args += ["--dry-run"]
    if args.allow_estimated_pit:
        runner_args += ["--allow-estimated-pit"]
    saved_argv = sys.argv
    sys.argv = ["run_repair_daily"] + runner_args
    try:
        rc = module.main()
    finally:
        sys.argv = saved_argv
    elapsed = time.time() - t0
    print(f"[2/2] Repair runner done in {elapsed:.1f}s (rc={rc})")
    return rc


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    rc_collector = 0 if args.skip_collector else 1
    rc_repair = 0 if args.skip_repair else 1
    if not args.skip_collector:
        try:
            rc_collector = run_collector(args)
        except Exception as exc:
            print(f"[1/2] Collector failed: {exc!r}")
    if not args.skip_repair:
        try:
            rc_repair = run_repair_runner(args)
        except Exception as exc:
            print(f"[2/2] Repair runner failed: {exc!r}")
    return 0 if (args.skip_repair or rc_repair == 0) else 1


if __name__ == "__main__":
    raise SystemExit(main())


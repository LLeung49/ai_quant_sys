"""Transactionally rebuild historical Repair Alpha snapshots after the YTD TTM fix.

The old snapshots must be archived before this command can write.  Each day is
fully scored in memory, then the old backfill rows are deleted and replacement
rows inserted in one MySQL transaction.  A failed day rolls back to its old
rows; a JSONL ledger supports an idempotent long-running resume.
"""

from __future__ import annotations

import argparse
from collections import deque
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
from datetime import date, datetime
import hashlib
import gzip
import json
import os
from functools import lru_cache
from pathlib import Path
from threading import Lock
from uuid import uuid4

from data_ingestion.db_config import execute_query, get_connection
from .archive_repair_dependencies import DEFAULT_ROOT as DEFAULT_DEPENDENCY_ROOT, archived_bounds
from morning_conference.sector_rotation2.research.config_hash import build_config_hash
from morning_conference.sector_rotation2.research.contracts import CandidateSnapshot
from morning_conference.sector_rotation2.research.financial.service import (
    load_repair_sectors, score_repair_sector,
)
from morning_conference.sector_rotation2.research.orchestrator.store import _json_dump
from morning_conference.sector_rotation2.research.status import SnapshotMode
from morning_conference.sector_rotation2.research.stock_alpha.config import TrendAlphaConfig
from morning_conference.sector_rotation2.snapshot_store import (
    create_run, mark_run_failed, mark_run_succeeded,
)
from morning_conference.sector_rotation2.research.financial.providers.database import (
    DEFAULT_RAW_QUERY, DEFAULT_CAPITAL_QUERY,
)


class RecoveryQueryCache:
    def __init__(self, query, end_date):
        self.query = query
        self.end_date = end_date
        self.rows = {}
        self.lock = Lock()

    def __call__(self, sql, params=()):
        table = next((name for name in (
            "trade_stock_financial_raw_pit", "trade_stock_capital_pit",
        ) if f"FROM {name}" in sql), None)
        if table is None or len(params) < 2:
            return self.query(sql, params)
        target, *codes = params
        with self.lock:
            missing = [code for code in codes if (table, code) not in self.rows]
            if missing:
                template = DEFAULT_RAW_QUERY if table == "trade_stock_financial_raw_pit" else DEFAULT_CAPITAL_QUERY
                rows = self.query(template.format(placeholders=", ".join(["%s"] * len(missing))),
                                  (self.end_date, *missing))
                for code in missing:
                    self.rows[table, code] = []
                for row in rows:
                    self.rows[table, row["stock_code"]].append(row)
            return [row for code in codes for row in self.rows[table, code]
                    if row["report_date"] <= target]


_worker_query = execute_query


def initialize_worker(end_date):
    global _worker_query
    _worker_query = RecoveryQueryCache(execute_query, date.fromisoformat(end_date))


INSERT_SQL = """
INSERT INTO research_candidate_snapshot
    (as_of_date, entity_type, entity_code, sector_level, sector_name, strategy_type,
     candidate_status, candidate_score, research_status, validation_status,
     execution_status, model_version, config_hash, run_id, snapshot_mode,
     rank_in_sector, feature_json, reasons_json, risk_flags_json,
     data_available_at, run_at, execution_eligible_at, availability_basis)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s, %s, %s)
"""

DEFAULT_MANIFEST = Path(
    "reports/financial-audit/repair-all-pre-full-rebuild-20261020.manifest.json"
)
DEFAULT_LEDGER = Path("reports/financial-audit/repair-historical-rebuild-20261020.jsonl")


def ensure_completion_table():
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""CREATE TABLE IF NOT EXISTS financial_repair_recovery_day (
            as_of_date DATE PRIMARY KEY, run_id VARCHAR(64) NOT NULL,
            old_count INT NOT NULL, new_count INT NOT NULL,
            completed_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
        ) ENGINE=InnoDB""")
        connection.commit()
    finally:
        cursor.close()
        connection.close()


def verify_backup(manifest_path: Path) -> dict:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    archive_path = Path(manifest["path"])
    if not archive_path.is_file():
        raise FileNotFoundError(f"missing historical snapshot backup: {archive_path}")
    digest = hashlib.sha256(archive_path.read_bytes()).hexdigest()
    if digest != manifest["sha256"] or int(manifest["rows"]) < 600_000:
        raise ValueError("historical snapshot backup failed SHA/count verification")
    return manifest


def _insert_values(snapshot: CandidateSnapshot) -> tuple:
    return (
        snapshot.as_of_date, snapshot.entity_type, snapshot.entity_code,
        snapshot.sector_level, snapshot.sector_name, snapshot.strategy_type,
        snapshot.candidate_status, snapshot.candidate_score,
        snapshot.research_status.value, snapshot.validation_status.value,
        snapshot.execution_status.value, snapshot.model_version,
        snapshot.config_hash, snapshot.run_id, snapshot.snapshot_mode.value,
        snapshot.rank_in_sector, _json_dump(snapshot.feature_json),
        _json_dump(snapshot.reasons_json), _json_dump(snapshot.risk_flags_json),
        snapshot.data_available_at, snapshot.run_at,
        snapshot.execution_eligible_at,
        snapshot.availability_basis.value if snapshot.availability_basis else None,
    )


def replace_backfill_day(
    as_of_date: str, snapshots: list[CandidateSnapshot], *,
    connection_factory=get_connection, archive_limits: dict | None = None,
) -> int:
    """Delete old and insert new Repair Alpha rows in one transaction."""

    if not snapshots:
        raise ValueError("empty replacement is not allowed")
    if len({snapshot.entity_code for snapshot in snapshots}) != len(snapshots):
        raise ValueError("duplicate stock in replacement")
    if any(snapshot.as_of_date != date.fromisoformat(as_of_date)
           or snapshot.strategy_type != "stock_repair"
           or snapshot.snapshot_mode is not SnapshotMode.BACKFILL
           or snapshot.sector_level != 2 for snapshot in snapshots):
        raise ValueError("replacement contains wrong date, level, strategy or mode")

    connection = connection_factory()
    cursor = connection.cursor()
    try:
        if archive_limits is not None:
            cursor.execute(
                "SELECT MAX(s.id),MAX(f.id),MAX(f.updated_at) "
                "FROM research_candidate_snapshot s LEFT JOIN "
                "sector_rotation_research_forward_label f ON f.source_snapshot_id=s.id "
                "WHERE s.as_of_date=%s AND s.sector_level=2 "
                "AND s.strategy_type='stock_repair' AND s.snapshot_mode='backfill'",
                (as_of_date,),
            )
            snapshot_id, label_id, updated = cursor.fetchone()
            if ((snapshot_id or 0) > archive_limits["snapshot_max_id"]
                    or (label_id or 0) > archive_limits["forward_labels"]["max_id"]
                    or str(updated or "") > archive_limits["forward_labels"]["max_updated"]):
                raise ValueError("replacement would remove data outside verified archives")
        cursor.execute(
            "DELETE f FROM sector_rotation_research_forward_label f "
            "JOIN research_candidate_snapshot s ON s.id=f.source_snapshot_id "
            "WHERE s.as_of_date=%s AND s.sector_level=2 "
            "AND s.strategy_type='stock_repair' "
            "AND s.snapshot_mode='backfill'",
            (as_of_date,),
        )
        cursor.execute(
            "DELETE FROM research_candidate_snapshot WHERE as_of_date=%s "
            "AND sector_level=2 AND strategy_type='stock_repair' "
            "AND snapshot_mode='backfill'",
            (as_of_date,),
        )
        old_count = cursor.rowcount
        for offset in range(0, len(snapshots), 500):
            cursor.executemany(
                INSERT_SQL,
                [_insert_values(snapshot) for snapshot in snapshots[offset:offset + 500]],
            )
        cursor.execute(
            "SELECT COUNT(*) FROM research_candidate_snapshot WHERE as_of_date=%s "
            "AND sector_level=2 AND strategy_type='stock_repair' "
            "AND snapshot_mode='backfill'",
            (as_of_date,),
        )
        actual = int(cursor.fetchone()[0])
        if actual != len(snapshots):
            raise ValueError(f"replacement count mismatch: {actual} != {len(snapshots)}")
        if archive_limits is not None:
            cursor.execute(
                "INSERT INTO financial_repair_recovery_day "
                "(as_of_date,run_id,old_count,new_count) VALUES (%s,%s,%s,%s)",
                (as_of_date, snapshots[0].run_id, old_count, actual),
            )
        connection.commit()
        return old_count
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()
        connection.close()


def score_day(as_of_date: str, *, run_id: str, workers: int) -> tuple[int, list[CandidateSnapshot]]:
    config = TrendAlphaConfig()
    sectors = load_repair_sectors(as_of_date, 2, SnapshotMode.BACKFILL, execute_query)
    snapshots: list[CandidateSnapshot] = []
    query = lru_cache(maxsize=128)(_worker_query)
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = [pool.submit(
            score_repair_sector, sector,
            as_of_date=as_of_date, level=2, mode=SnapshotMode.BACKFILL,
            config=config, run_id=run_id, store=None, query=query,
            allow_estimated_pit=False,
        ) for sector in sectors]
        for future in as_completed(futures):
            snapshots.extend(future.result())
    return len(sectors), snapshots


def candidate_dates(start: str, end: str) -> list[str]:
    rows = execute_query(
        "SELECT DISTINCT as_of_date FROM research_candidate_snapshot "
        "WHERE strategy_type='stock_repair' AND snapshot_mode='backfill' "
        "AND sector_level=2 AND as_of_date BETWEEN %s AND %s ORDER BY as_of_date",
        (start, end),
    )
    return [str(row["as_of_date"]) for row in rows]


def completed_dates(ledger_path: Path) -> set[str]:
    if not ledger_path.exists():
        return set()
    return {
        row["date"] for line in ledger_path.read_text(encoding="utf-8").splitlines()
        if line.strip() and (row := json.loads(line))["status"] == "succeeded"
    }


def append_ledger(ledger_path: Path, row: dict) -> None:
    ledger_path.parent.mkdir(parents=True, exist_ok=True)
    with ledger_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row, ensure_ascii=False, default=str) + "\n")
        handle.flush()
        os.fsync(handle.fileno())


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start", default="2024-01-02")
    parser.add_argument("--end", default="2026-09-17")
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--date-workers", type=int, default=1)
    parser.add_argument("--max-dates", type=int)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--dependency-archive", type=Path, default=DEFAULT_DEPENDENCY_ROOT)
    parser.add_argument("--ledger", type=Path, default=DEFAULT_LEDGER)
    return parser


def scored_dates(dates: list[str], *, workers: int, date_workers: int):
    remaining = iter(dates)
    with ProcessPoolExecutor(max_workers=date_workers, initializer=initialize_worker,
                             initargs=(max(dates) if dates else "2026-09-17",)) as pool:
        pending = deque()

        def submit_next():
            day = next(remaining, None)
            if day is not None:
                run_id = str(uuid4())
                pending.append((day, run_id, pool.submit(
                    score_day, day, run_id=run_id, workers=workers,
                )))

        for _ in range(date_workers):
            submit_next()
        while pending:
            day, run_id, future = pending.popleft()
            yield day, run_id, future
            submit_next()


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.workers < 1 or args.date_workers < 1 or (args.max_dates is not None and args.max_dates < 1):
        raise ValueError("workers and max-dates must be positive")
    backup = verify_backup(args.manifest)
    archive_limits = None
    database_completed = set()
    if not args.dry_run:
        archive_limits = archived_bounds(args.dependency_archive)
        with gzip.open(backup["path"], "rt", encoding="utf-8") as handle:
            archive_limits["snapshot_max_id"] = max(int(json.loads(line)["id"]) for line in handle)
        ensure_completion_table()
        database_completed = {str(row["as_of_date"]) for row in execute_query(
            "SELECT as_of_date FROM financial_repair_recovery_day"
        )}
    dates = [day for day in candidate_dates(args.start, args.end)
             if day not in completed_dates(args.ledger) | database_completed]
    if args.max_dates:
        dates = dates[:args.max_dates]
    print(f"historical repair dates queued: {len(dates)}", flush=True)
    for index, (day, run_id, future) in enumerate(scored_dates(
        dates, workers=args.workers, date_workers=args.date_workers,
    ), 1):
        committed = False
        if not args.dry_run:
            config = TrendAlphaConfig()
            create_run(run_id, day, 2, config.model_version,
                       build_config_hash({"model_version": config.model_version,
                                          "sector_level": 2}), day)
        try:
            sectors, snapshots = future.result()
            if sectors and not snapshots:
                raise ValueError("no valid PIT candidates for populated repair sectors")
            if not snapshots:
                raise ValueError("empty historical repair replacement")
            old_count = 0 if args.dry_run else replace_backfill_day(
                day, snapshots, archive_limits=archive_limits,
            )
            committed = not args.dry_run
            if not args.dry_run:
                mark_run_succeeded(run_id, len(snapshots), 0)
                append_ledger(args.ledger, {
                    "date": day, "status": "succeeded", "old_count": old_count,
                    "new_count": len(snapshots), "sectors": sectors, "run_id": run_id,
                    "completed_at": datetime.now().isoformat(),
                })
            print(f"[{index}/{len(dates)}] {day}: old={old_count} new={len(snapshots)} "
                  f"sectors={sectors} {'DRY RUN' if args.dry_run else 'COMMITTED'}", flush=True)
        except Exception as exc:
            if committed:
                raise RuntimeError(
                    f"{day} committed; bookkeeping failed; resume uses database completion marker"
                ) from exc
            if not args.dry_run:
                mark_run_failed(run_id, str(exc))
                append_ledger(args.ledger, {
                    "date": day, "status": "failed", "run_id": run_id,
                    "error": f"{type(exc).__name__}: {exc}",
                    "failed_at": datetime.now().isoformat(),
                })
            raise
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Publish verified QMT native share counts with separate effective dates."""

from __future__ import annotations

from collections import Counter
from datetime import date
import gzip
import hashlib
import json
import math
from pathlib import Path
import re
from typing import Any


_INSERT = """INSERT IGNORE INTO trade_stock_capital_pit
 (stock_code,report_date,announcement_date,total_shares,circulating_shares,
  pit_status,source_hash,data_source)
 VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""


def prepare_capital(row: dict[str, Any], *, as_of_date: date) -> dict[str, Any]:
    effective = date.fromisoformat(row["report_date"])
    announced = date.fromisoformat(row["announcement_date"])
    usable = date.fromisoformat(row["first_usable_date"])
    if usable != max(effective, announced) or usable > as_of_date:
        raise ValueError("invalid capital availability date")
    total, circulating = row.get("total_shares"), row.get("circulating_shares")
    if not all(isinstance(value, (int, float)) and math.isfinite(value)
               for value in (total, circulating)) or total <= 0 or circulating < 0:
        raise ValueError("invalid shares")
    if circulating > total:
        raise ValueError("circulating shares exceed total")
    if not re.fullmatch(r"[0-9a-f]{64}", row["source_hash"]):
        raise ValueError("invalid capital source hash")
    return {**row, "circulating_shares": None if circulating == 0 else circulating}


def publish_capital(archive_dir: Path, output: Path, *, as_of_date: date,
                    apply: bool = False, stock_code: str | None = None) -> dict[str, Any]:
    archive_dir, output = Path(archive_dir), Path(output)
    summary = json.loads((archive_dir / "archive-summary.json").read_text(encoding="utf-8"))
    groups = [g for g in summary["groups"] if str(g["kind"]) == "7004"]
    if len(groups) != 2:
        raise ValueError("capital archives for both exchanges required")
    counts: Counter[str] = Counter()
    failed_stocks = []
    connection = cursor = None
    if apply:
        from data_ingestion.db_config import get_connection
        connection = get_connection()
        cursor = connection.cursor()
    current_code = None
    pending = []

    def flush() -> None:
        if not pending or cursor is None or connection is None:
            pending.clear()
            return
        try:
            cursor.executemany(_INSERT, pending)
            connection.commit()
            counts["inserted"] += cursor.rowcount
        except Exception as error:
            connection.rollback()
            failed_stocks.append({"stock_code": current_code, "rows": len(pending),
                                  "error": type(error).__name__})
            counts["db_failed_rows"] += len(pending)
        pending.clear()

    try:
        for group in groups:
            path = archive_dir / f"{group['market']}-7004.jsonl.gz"
            if hashlib.sha256(path.read_bytes()).hexdigest() != group["archive_sha256"]:
                raise ValueError(f"capital archive checksum mismatch: {path}")
            found = 0
            with gzip.open(path, "rt", encoding="utf-8") as source:
                for line in source:
                    found += 1
                    row = json.loads(line)
                    code = row["stock_code"]
                    if code != current_code:
                        flush()
                        current_code = code
                    if stock_code and code != stock_code:
                        continue
                    counts["selected_rows"] += 1
                    try:
                        prepared = prepare_capital(row, as_of_date=as_of_date)
                    except (ValueError, TypeError, KeyError):
                        counts["invalid_rows"] += 1
                        continue
                    counts["publishable_rows"] += 1
                    if prepared["circulating_shares"] is None:
                        counts["circulating_missing_rows"] += 1
                    pending.append((code, prepared["report_date"], prepared["announcement_date"],
                                    prepared["total_shares"], prepared["circulating_shares"],
                                    "EXACT", prepared["source_hash"], "qmt"))
            if found != group["records"]:
                raise ValueError(f"capital archive count mismatch: {path}")
        flush()
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
    result = {"status": "applied" if apply and not failed_stocks else
              "partial_failure" if failed_stocks else "dry_run",
              "as_of_date": as_of_date.isoformat(), "stock_code": stock_code,
              "counts": dict(counts), "failed_stocks": failed_stocks}
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    return result


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive_dir", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--as-of-date", type=date.fromisoformat, required=True)
    parser.add_argument("--stock-code")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    print(json.dumps(publish_capital(args.archive_dir, args.output,
                                     as_of_date=args.as_of_date,
                                     apply=args.apply, stock_code=args.stock_code), indent=2))

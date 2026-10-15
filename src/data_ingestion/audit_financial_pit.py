"""Audit and safely quarantine invalid financial PIT rows.

The command is read-only unless ``--apply`` is supplied.  Apply mode copies
each exact source row to a JSON quarantine table before deleting the same IDs
inside one transaction.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import date, datetime
from decimal import Decimal
from pathlib import Path
from typing import Any, Iterable

import pymysql

from data_ingestion.db_config import get_connection


VALID_STOCK_CODE = re.compile(r"^[0-9]{6}\.(SH|SZ|BJ)$")
MIN_REPORT_DATE = date(1990, 1, 1)


def _coerce_date(value: Any) -> date | None:
    if value is None:
        return None
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    text = str(value).strip()
    if not text or text.startswith("0000-00-00"):
        return None
    try:
        return date.fromisoformat(text[:10])
    except ValueError:
        return None


def classify_row(row: dict[str, Any], *, as_of_date: date) -> tuple[str, ...]:
    """Return deterministic evidence codes for one suspicious PIT row."""

    reasons: list[str] = []
    if not VALID_STOCK_CODE.fullmatch(str(row.get("stock_code") or "")):
        reasons.append("invalid_stock_code")

    report_date = _coerce_date(row.get("report_date"))
    if report_date is None or report_date < MIN_REPORT_DATE:
        reasons.append("invalid_report_date")
    elif report_date > as_of_date:
        reasons.append("future_report_date")

    announcement_value = row.get("announcement_date")
    announcement_date = _coerce_date(announcement_value)
    if announcement_value is not None and announcement_date is None:
        reasons.append("invalid_announcement_date")
    elif announcement_date is not None and announcement_date > as_of_date:
        reasons.append("future_announcement_date")

    return tuple(reasons)


def audit_rows(
    rows: Iterable[dict[str, Any]], *, as_of_date: date
) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    for row in rows:
        reasons = classify_row(row, as_of_date=as_of_date)
        if reasons:
            findings.append(
                {
                    "id": int(row["id"]),
                    "stock_code": str(row.get("stock_code") or ""),
                    "reasons": list(reasons),
                }
            )
    return findings


def fetch_candidates(connection, *, as_of_date: date) -> list[dict[str, Any]]:
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    try:
        cursor.execute(
            """SELECT *
               FROM trade_stock_financial_raw_pit
               WHERE stock_code NOT REGEXP '^[0-9]{6}\\.(SH|SZ|BJ)$'
                  OR report_date < '1990-01-01'
                  OR report_date > %s
                  OR announcement_date > %s
               ORDER BY id""",
            (as_of_date, as_of_date),
        )
        return list(cursor.fetchall())
    finally:
        cursor.close()


def _json_default(value: Any) -> str:
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, Decimal):
        return str(value)
    if isinstance(value, bytes):
        return value.hex()
    return str(value)


def ensure_quarantine_table(connection) -> None:
    cursor = connection.cursor()
    try:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS trade_stock_financial_raw_pit_quarantine (
                   quarantine_id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                   source_id BIGINT NOT NULL,
                   stock_code VARCHAR(32) NOT NULL,
                   reason_codes VARCHAR(255) NOT NULL,
                   batch_id VARCHAR(96) NOT NULL,
                   quarantined_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                   row_payload JSON NOT NULL,
                   UNIQUE KEY uq_financial_pit_quarantine_batch (source_id, batch_id),
                   KEY idx_financial_pit_quarantine_code (stock_code)
               ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4"""
        )
        connection.commit()
    finally:
        cursor.close()


def quarantine_rows(
    connection,
    findings: list[dict[str, Any]],
    *,
    batch_id: str,
) -> int:
    """Copy findings to quarantine, then delete only their exact source IDs."""

    if not findings:
        return 0
    if len({item["id"] for item in findings}) != len(findings):
        raise ValueError("duplicate source IDs in quarantine request")

    ensure_quarantine_table(connection)
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    ids = tuple(int(item["id"]) for item in findings)
    try:
        connection.begin()
        for finding in findings:
            source_id = int(finding["id"])
            cursor.execute(
                "SELECT * FROM trade_stock_financial_raw_pit WHERE id = %s FOR UPDATE",
                (source_id,),
            )
            source_row = cursor.fetchone()
            if source_row is None:
                raise RuntimeError(f"source row disappeared before quarantine: id={source_id}")
            if str(source_row.get("stock_code") or "") != finding["stock_code"]:
                raise RuntimeError(f"source row changed before quarantine: id={source_id}")
            cursor.execute(
                """INSERT INTO trade_stock_financial_raw_pit_quarantine
                       (source_id, stock_code, reason_codes, batch_id, row_payload)
                   VALUES (%s, %s, %s, %s, %s)""",
                (
                    source_id,
                    finding["stock_code"],
                    ",".join(finding["reasons"]),
                    batch_id,
                    json.dumps(source_row, ensure_ascii=False, default=_json_default),
                ),
            )
            if cursor.rowcount != 1:
                raise RuntimeError(f"failed to preserve source row: id={source_id}")

        placeholders = ",".join(["%s"] * len(ids))
        cursor.execute(
            f"DELETE FROM trade_stock_financial_raw_pit WHERE id IN ({placeholders})",
            ids,
        )
        if cursor.rowcount != len(ids):
            raise RuntimeError(
                f"delete count mismatch: expected={len(ids)} actual={cursor.rowcount}"
            )
        connection.commit()
        return len(ids)
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--as-of-date", default=date.today().isoformat())
    parser.add_argument("--output", type=Path)
    parser.add_argument("--batch-id")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="copy findings to quarantine and delete the exact source IDs",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    as_of_date = date.fromisoformat(args.as_of_date)
    batch_id = args.batch_id or f"financial-pit-audit-{as_of_date:%Y%m%d}"
    output = args.output or Path("reports/financial-audit") / f"{batch_id}.json"

    connection = get_connection()
    try:
        rows = fetch_candidates(connection, as_of_date=as_of_date)
        findings = audit_rows(rows, as_of_date=as_of_date)
        moved = quarantine_rows(connection, findings, batch_id=batch_id) if args.apply else 0
    finally:
        connection.close()

    counts: dict[str, int] = {}
    for finding in findings:
        for reason in finding["reasons"]:
            counts[reason] = counts.get(reason, 0) + 1
    report = {
        "batch_id": batch_id,
        "as_of_date": as_of_date.isoformat(),
        "mode": "apply" if args.apply else "dry-run",
        "candidate_count": len(rows),
        "finding_count": len(findings),
        "reason_counts": counts,
        "quarantined_count": moved,
        "findings": findings,
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({**report, "findings": f"{len(findings)} rows"}, ensure_ascii=False))
    print(f"report={output.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

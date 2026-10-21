"""Gate and optionally publish QMT native PIT candidates, preserving lineage."""

from __future__ import annotations

from collections import Counter
from datetime import date, datetime
import gzip
import hashlib
import json
import math
from pathlib import Path
import re
from typing import Any


_INSERT = """INSERT IGNORE INTO trade_stock_financial_raw_pit
 (stock_code,source_table,report_date,announcement_date,period_type,
  revenue,net_profit,total_assets,total_equity,operating_cash_flow,
  eps,roe,gross_margin,metric_available_at,metric_lineage_json,date_evidence,
  pit_status,source_updated_at,source_hash,is_restated,source_verified,data_source)
 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""


def _finite(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def prepare_candidate(row: dict[str, Any], *, as_of_date: date) -> dict[str, Any]:
    report_date = date.fromisoformat(row["report_date"])
    announced = date.fromisoformat(row["announcement_date"])
    if not report_date < announced <= as_of_date:
        raise ValueError("invalid announcement date")
    if not re.fullmatch(r"[0-9a-f]{64}", row["source_hash"]):
        raise ValueError("invalid source hash")
    core = {"revenue": row.get("revenue"), "net_profit": row.get("net_profit"),
            "total_assets": row.get("total_assets"), "total_equity": row.get("total_equity"),
            "operating_cash_flow": row.get("operating_cashflow")}
    if not all(_finite(value) for value in core.values()) or core["total_assets"] <= 0:
        raise ValueError("invalid financial core")
    metric_date = (date.fromisoformat(row["metric_available_at"])
                   if row.get("metric_available_at") else None)
    metrics = {"eps": row.get("eps"), "roe": row.get("roe"),
               "gross_margin": row.get("gross_margin")}
    if any(value is not None for value in metrics.values()) and (
        metric_date is None or metric_date > announced or metric_date > as_of_date
    ):
        raise ValueError("unverified metric date")
    flags = []
    for name, limit in (("eps", 100), ("roe", 1000), ("gross_margin", 1000)):
        value = metrics[name]
        if value is not None and (not _finite(value) or abs(value) > limit):
            metrics[name] = None
            flags.append(name + "_outlier")
    return {**row, **core, **metrics, "metric_quality_flags": flags,
            "metric_available_at": metric_date.isoformat() if metric_date else None}


def _hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _blocked_keys(exceptions: Path, conflicts: Path) -> set[tuple[str, str]]:
    blocked = set()
    for path in (exceptions, conflicts):
        with gzip.open(path, "rt", encoding="utf-8") as source:
            for line in source:
                row = json.loads(line)
                if path == exceptions and row.get("status") == "no_candidate":
                    continue
                blocked.add((row["stock_code"], row["report_date"]))
    return blocked


def publish_native_pit(stage: Path, exceptions: Path, conflicts: Path,
                       output: Path, *, as_of_date: date, apply: bool = False,
                       stock_code: str | None = None) -> dict[str, Any]:
    """Dry-run by default; apply inserts one stock at a time in transactions."""
    stage, exceptions, conflicts, output = map(Path, (stage, exceptions, conflicts, output))
    blocked = _blocked_keys(exceptions, conflicts)
    counts: Counter[str] = Counter()
    conn = None
    cursor = None
    if apply:
        from data_ingestion.db_config import get_connection
        conn = get_connection()
        cursor = conn.cursor()
    current_code = None
    current_period = None
    period_version = 0
    pending: list[tuple[Any, ...]] = []
    failed_stocks = []

    def flush() -> None:
        if not pending or cursor is None or conn is None:
            pending.clear()
            return
        try:
            cursor.executemany(_INSERT, pending)
            conn.commit()
            counts["inserted"] += cursor.rowcount
        except Exception as error:
            conn.rollback()
            failed_stocks.append({"stock_code": current_code, "error": type(error).__name__,
                                  "rows": len(pending)})
            counts["db_failed_rows"] += len(pending)
        pending.clear()

    try:
        with gzip.open(stage, "rt", encoding="utf-8") as source:
            for line in source:
                row = json.loads(line)
                code = row["stock_code"]
                if current_code != code:
                    flush()
                    current_code = code
                if current_period != (code, row["report_date"]):
                    current_period = (code, row["report_date"])
                    period_version = 0
                if stock_code and code != stock_code:
                    continue
                counts["selected_rows"] += 1
                if (code, row["report_date"]) in blocked:
                    counts["blocked_rows"] += 1
                    continue
                try:
                    prepared = prepare_candidate(row, as_of_date=as_of_date)
                except (ValueError, KeyError, TypeError):
                    counts["invalid_rows"] += 1
                    continue
                counts["publishable_rows"] += 1
                counts["metric_outliers"] += len(prepared["metric_quality_flags"])
                lineage = json.dumps({"components": prepared["lineage"],
                                      "metric_quality_flags": prepared["metric_quality_flags"]},
                                     ensure_ascii=False, sort_keys=True)
                pending.append((
                    code, "qmt_native_composite", row["report_date"], row["announcement_date"],
                    "quarterly", prepared["revenue"], prepared["net_profit"],
                    prepared["total_assets"], prepared["total_equity"],
                    prepared["operating_cash_flow"], prepared["eps"], prepared["roe"],
                    prepared["gross_margin"], prepared["metric_available_at"], lineage,
                    "qmt_native_m_anntime_crosschecked", "EXACT", datetime.now(),
                    row["source_hash"], 1 if period_version else 0, 1, "qmt",
                ))
                period_version += 1
        flush()
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()
    result = {"status": "applied" if apply and not failed_stocks else
              "partial_failure" if failed_stocks else "dry_run",
              "as_of_date": as_of_date.isoformat(), "stock_code": stock_code,
              "inputs_sha256": {"stage": _hash(stage), "exceptions": _hash(exceptions),
                                "conflicts": _hash(conflicts)},
              "blocked_keys": len(blocked), "counts": dict(counts),
              "failed_stocks": failed_stocks}
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    return result


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", type=Path)
    parser.add_argument("exceptions", type=Path)
    parser.add_argument("conflicts", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--as-of-date", type=date.fromisoformat, required=True)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--stock-code")
    args = parser.parse_args()
    print(json.dumps(publish_native_pit(args.stage, args.exceptions, args.conflicts,
                                        args.output, as_of_date=args.as_of_date,
                                        apply=args.apply, stock_code=args.stock_code), indent=2))

"""Read-only reconciliation of dated native candidates with legacy QMT PIT."""

from __future__ import annotations

from collections import Counter, defaultdict
from decimal import Decimal, ROUND_HALF_UP
import gzip
import json
from pathlib import Path
from typing import Any, Mapping, Sequence


_KEYS = ("revenue", "net_profit", "total_assets", "total_equity", "operating_cashflow")


def _fingerprint(row: Mapping[str, Any], *, old: bool = False) -> tuple[Decimal | None, ...]:
    values = []
    for name in _KEYS:
        value = row.get("operating_cash_flow" if old and name == "operating_cashflow" else name)
        values.append(None if value is None else Decimal(str(value)).quantize(
            Decimal("0.0001"), rounding=ROUND_HALF_UP))
    return tuple(values)


def compare_old_row(old: Mapping[str, Any], versions: Sequence[Mapping[str, Any]]) -> str:
    if not versions:
        return "no_candidate"
    fingerprint = _fingerprint(old, old=True)
    if fingerprint == _fingerprint(versions[-1]):
        return "latest_match"
    if any(fingerprint == _fingerprint(row) for row in versions[:-1]):
        return "historical_match"
    return "no_value_match"


def reconcile_native_stage(stage: Path, output_dir: Path) -> dict[str, Any]:
    from data_ingestion.db_config import execute_query

    by_key: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    with gzip.open(stage, "rt", encoding="utf-8") as source:
        for line in source:
            row = json.loads(line)
            by_key[(row["stock_code"], row["report_date"])].append(row)
    old_rows = execute_query("""SELECT stock_code,report_date,revenue,net_profit,
        total_assets,total_equity,operating_cash_flow
        FROM trade_stock_financial_raw_pit
        WHERE data_source='qmt' AND source_table='trade_stock_financial'""")
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    counts: Counter[str] = Counter()
    old_keys = set()
    with gzip.open(output_dir / "exceptions.jsonl.gz", "wt", encoding="utf-8") as exceptions:
        for old in old_rows:
            key = (old["stock_code"], str(old["report_date"]))
            old_keys.add(key)
            status = compare_old_row(old, by_key.get(key, []))
            counts[status] += 1
            if status in {"no_candidate", "no_value_match"}:
                exceptions.write(json.dumps({"stock_code": key[0], "report_date": key[1],
                                             "status": status}, ensure_ascii=False) + "\n")
    counts["candidate_keys_without_old_qmt"] = len(by_key.keys() - old_keys)
    summary = {"old_rows": len(old_rows), "candidate_keys": len(by_key),
               "statuses": dict(counts), "status": "read_only_audit"}
    (output_dir / "reconciliation-summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    return summary


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", type=Path)
    parser.add_argument("output_dir", type=Path)
    args = parser.parse_args()
    print(json.dumps(reconcile_native_stage(args.stage, args.output_dir), indent=2))

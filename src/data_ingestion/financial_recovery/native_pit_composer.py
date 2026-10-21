"""Compose dated QMT statement records without borrowing future revisions."""

from __future__ import annotations

import hashlib
import json
import math
from collections import defaultdict
from typing import Any, Iterable


_TABLES = ("ASHAREBALANCESHEET", "ASHAREINCOME", "ASHARECASHFLOW", "PERSHAREINDEX")
_CORE = ("ASHAREBALANCESHEET", "ASHAREINCOME", "ASHARECASHFLOW")
_FIELDS = {
    "ASHAREBALANCESHEET": ("tot_assets", "total_equity"),
    "ASHAREINCOME": ("revenue", "net_profit_incl_min_int_inc"),
    "ASHARECASHFLOW": ("net_cash_flows_oper_act",),
    "PERSHAREINDEX": ("s_fa_eps_basic", "du_return_on_equity", "sales_gross_profit"),
}


def _fingerprint(row: dict[str, Any]) -> tuple[Any, ...]:
    fields = row["raw_fields"]
    return tuple(fields.get(field) for field in _FIELDS[row["source_table"]])


def _usable(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def compose_native_pit_versions(records: Iterable[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    """Return candidate snapshots and quarantined same-day source conflicts.

    A revision is visible from its own announcement date. Three core statements
    must all exist before a snapshot can be emitted; per-share metrics have their
    own first-visible date. The caller groups records for one stock and period.
    """
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in records:
        if row.get("source_table") not in _TABLES:
            continue
        if not row.get("stock_code") or not row.get("report_date") or not row.get("announcement_date"):
            continue
        grouped[(row["stock_code"], row["report_date"])].append(row)

    candidates: list[dict[str, Any]] = []
    conflicts: list[dict[str, Any]] = []
    for (code, period), rows in sorted(grouped.items()):
        events: dict[str, dict[str, list[dict[str, Any]]]] = defaultdict(lambda: defaultdict(list))
        for row in rows:
            if row["announcement_date"] < period:
                conflicts.append({"stock_code": code, "report_date": period,
                                  "announcement_date": row["announcement_date"],
                                  "source_table": row["source_table"], "reason": "announcement_before_report"})
                continue
            events[row["announcement_date"]][row["source_table"]].append(row)
        latest: dict[str, dict[str, Any]] = {}
        for event_date in sorted(events):
            blocked = False
            for table, variants in sorted(events[event_date].items()):
                fingerprints = {_fingerprint(row) for row in variants}
                if len(fingerprints) > 1:
                    latest.pop(table, None)
                    conflicts.append({"stock_code": code, "report_date": period,
                                      "announcement_date": event_date,
                                      "source_table": table, "reason": "same_day_value_conflict",
                                      "source_hashes": sorted({str(row["source_hash"]) for row in variants})})
                    blocked = True
                    continue
                latest[table] = min(variants, key=lambda row: str(row["source_hash"]))
            if blocked or not all(table in latest for table in _CORE):
                continue
            balance = latest["ASHAREBALANCESHEET"]["raw_fields"]
            income = latest["ASHAREINCOME"]["raw_fields"]
            cash = latest["ASHARECASHFLOW"]["raw_fields"]
            core = {
                "total_assets": balance.get("tot_assets"),
                "total_equity": balance.get("total_equity"),
                "revenue": income.get("revenue"),
                "net_profit": income.get("net_profit_incl_min_int_inc"),
                "operating_cashflow": cash.get("net_cash_flows_oper_act"),
            }
            if not all(_usable(value) for value in core.values()):
                conflicts.append({"stock_code": code, "report_date": period,
                                  "announcement_date": event_date, "reason": "incomplete_core"})
                continue
            per_share = latest.get("PERSHAREINDEX")
            metrics = per_share["raw_fields"] if per_share else {}
            lineage = {table: {"source_hash": row["source_hash"],
                               "announcement_date": row["announcement_date"]}
                       for table, row in sorted(latest.items())}
            payload = json.dumps({"stock_code": code, "report_date": period,
                                  "lineage": lineage}, sort_keys=True, ensure_ascii=False)
            candidates.append({
                "stock_code": code, "report_date": period,
                "announcement_date": event_date, "source_table": "qmt_native_composite",
                "data_source": "qmt", "pit_status": "EXACT",
                **core,
                "eps": metrics.get("s_fa_eps_basic"),
                "roe": metrics.get("du_return_on_equity"),
                "gross_margin": metrics.get("sales_gross_profit"),
                "metric_available_at": per_share["announcement_date"] if per_share else None,
                "lineage": lineage,
                "source_hash": hashlib.sha256(payload.encode("utf-8")).hexdigest(),
            })
    return {"candidates": candidates, "conflicts": conflicts}

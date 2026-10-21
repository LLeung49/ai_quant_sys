"""Match PIT core values to dated QMT native statement records."""

from __future__ import annotations

from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from typing import Any, Iterable, Mapping


_SCALE = Decimal("0.0001")
_COMPONENTS = {
    "balance": "ASHAREBALANCESHEET",
    "income": "ASHAREINCOME",
    "cashflow": "ASHARECASHFLOW",
}


def _amount(value: object) -> Decimal | None:
    if value is None:
        return None
    try:
        number = Decimal(str(value))
        if not number.is_finite():
            return None
        return number.quantize(_SCALE, rounding=ROUND_HALF_UP)
    except (InvalidOperation, ValueError, TypeError):
        return None


def _matches(component: str, pit: Mapping[str, Any], raw: Mapping[str, Any]) -> bool:
    if component == "balance":
        return (
            _amount(pit["total_assets"]) == _amount(raw.get("tot_assets"))
            and _amount(pit["total_equity"]) == _amount(raw.get("total_equity"))
        )
    if component == "income":
        profit = raw.get("net_profit_incl_min_int_inc")
        if profit is None:
            profit = raw.get("net_profit_excl_min_int_inc")
        return (
            _amount(pit["revenue"]) == _amount(raw.get("revenue"))
            and _amount(pit["net_profit"]) == _amount(profit)
        )
    return _amount(pit["operating_cash_flow"]) == _amount(
        raw.get("net_cash_flows_oper_act")
    )


def match_pit_to_native(
    pit_row: Mapping[str, Any], native_rows: Iterable[Mapping[str, Any]]
) -> dict[str, Any]:
    """Return earliest evidence for all five core values, or a failure code.

    The matched dates are per statement. The complete PIT row only becomes
    visible after the latest of those three statement dates.
    """

    result: dict[str, Any] = {
        "status": "incomplete_core",
        "first_visible_date": None,
        "component_dates": {},
        "component_hashes": {},
    }
    if any(
        _amount(pit_row.get(name)) is None
        for name in (
            "revenue", "net_profit", "total_assets", "total_equity",
            "operating_cash_flow",
        )
    ):
        return result

    report_date = str(pit_row["report_date"])
    by_component: dict[str, list[Mapping[str, Any]]] = {
        name: [] for name in _COMPONENTS
    }
    table_to_component = {table: name for name, table in _COMPONENTS.items()}
    for row in native_rows:
        if (
            row.get("stock_code") != pit_row["stock_code"]
            or str(row.get("report_date")) != report_date
        ):
            continue
        component = table_to_component.get(str(row.get("source_table")))
        if component:
            by_component[component].append(row)

    if any(not rows for rows in by_component.values()):
        result["status"] = "missing_statement"
        return result

    for component, rows in by_component.items():
        matches = [
            row for row in rows
            if row.get("announcement_date")
            and _matches(component, pit_row, row.get("raw_fields") or {})
        ]
        if not matches:
            result["status"] = "numeric_mismatch"
            return result
        selected = min(
            matches,
            key=lambda row: (
                str(row["announcement_date"]), str(row.get("source_hash") or "")
            ),
        )
        result["component_dates"][component] = str(selected["announcement_date"])
        result["component_hashes"][component] = selected.get("source_hash")

    result["status"] = "matched"
    result["first_visible_date"] = max(result["component_dates"].values())
    return result

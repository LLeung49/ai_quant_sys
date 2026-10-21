"""Preserve QMT's raw financial timestamps without xtdata's date fallback.

This module only produces files. It has no database connection or publisher.
"""

from __future__ import annotations

from datetime import date, datetime, timedelta, timezone
from decimal import Decimal
from hashlib import sha256
import json
import math
import os
from pathlib import Path
from typing import Any, Mapping


SHANGHAI = timezone(timedelta(hours=8))


def _date_from_ms(value: object) -> date | None:
    if value is None:
        return None
    try:
        number = float(value)
    except (TypeError, ValueError, OverflowError):
        return None
    if not math.isfinite(number) or not 631152000000 <= number <= 2051222400000:
        return None
    return datetime.fromtimestamp(number / 1000, SHANGHAI).date()


def _json_safe(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {str(key): _json_safe(part) for key, part in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_safe(part) for part in value]
    if isinstance(value, float) and not math.isfinite(value):
        return None
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, Decimal):
        return str(value)
    if hasattr(value, "item"):
        return _json_safe(value.item())
    return value


def archive_raw_financial_response(
    response: Mapping[str, Mapping[str, list[Mapping[str, Any]]]],
    *,
    captured_at: datetime,
) -> list[dict[str, Any]]:
    """Normalize raw xtdata rows while retaining distinct report versions."""

    if captured_at.tzinfo is None:
        raise ValueError("captured_at must be timezone-aware")
    output: list[dict[str, Any]] = []
    for stock_code, tables in response.items():
        for source_table, raw_rows in tables.items():
            for raw_row in raw_rows:
                report_date = _date_from_ms(raw_row.get("m_timetag"))
                if report_date is None:
                    raise ValueError(
                        f"invalid m_timetag: {stock_code}/{source_table}"
                    )
                announcement_date = _date_from_ms(raw_row.get("m_anntime"))
                fields = _json_safe(raw_row)
                payload = {
                    "stock_code": stock_code,
                    "source_table": source_table,
                    "report_date": report_date.isoformat(),
                    "announcement_date": (
                        announcement_date.isoformat() if announcement_date else None
                    ),
                    "date_evidence": (
                        "qmt_raw_m_anntime" if announcement_date else "missing"
                    ),
                    "captured_at": captured_at.isoformat(),
                    "raw_fields": fields,
                }
                source = {key: value for key, value in payload.items() if key != "captured_at"}
                payload["source_hash"] = sha256(
                    json.dumps(source, sort_keys=True, ensure_ascii=False).encode("utf-8")
                ).hexdigest()
                output.append(payload)
    return output


def write_archive_jsonl(rows: list[dict[str, Any]], output: Path) -> None:
    """Write a new immutable archive file through a same-directory temp file."""

    output = Path(output)
    if output.exists():
        raise FileExistsError(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_name(output.name + ".tmp")
    if temporary.exists():
        raise FileExistsError(temporary)
    try:
        with temporary.open("w", encoding="utf-8", newline="\n") as stream:
            for row in rows:
                stream.write(json.dumps(row, sort_keys=True, ensure_ascii=False) + "\n")
        os.replace(temporary, output)
    finally:
        temporary.unlink(missing_ok=True)

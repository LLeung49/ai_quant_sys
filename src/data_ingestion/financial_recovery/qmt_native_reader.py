"""Read cross-checked fields from QMT's cached statement record versions.

The offsets below were checked against 3,602 bridge values from six stocks.
Unknown native fields remain in the original checksummed DAT file; they are
not guessed or published by this reader.
"""

from __future__ import annotations

from hashlib import sha256
import math
from pathlib import Path
import re
import struct
from typing import Any

from .qmt_raw_archive import _date_from_ms


# kind -> (official table, record width, disclosure timestamp offset, fields)
_LAYOUTS: dict[str, tuple[str, int, int, dict[str, int]]] = {
    "7001": (
        "ASHAREBALANCESHEET", 1264, 8,
        {
            "tot_assets": 600,
            "tot_liab": 800,
            "total_equity": 880,
            "total_current_assets": 472,
            "total_current_liability": 736,
        },
    ),
    "7002": (
        "ASHAREINCOME", 664, 16,
        {
            "revenue": 248,
            "net_profit_incl_min_int_inc": 352,
            "net_profit_excl_min_int_inc": 224,
            "total_operating_cost": 48,
        },
    ),
    "7003": (
        "ASHARECASHFLOW", 920, 16,
        {"net_cash_flows_oper_act": 336},
    ),
    "7008": (
        "PERSHAREINDEX", 344, 8,
        {
            "s_fa_eps_basic": 32,
            "du_return_on_equity": 72,
            "sales_gross_profit": 80,
        },
    ),
}


def _numeric(record: bytes, offset: int) -> float | None:
    value = struct.unpack_from("<d", record, offset)[0]
    if not math.isfinite(value) or abs(value) >= 1e300:
        return None
    return value


def read_native_financial_file(
    path: Path, *, market: str, expected_sha256: str
) -> list[dict[str, Any]]:
    """Parse only verified fields, retaining every version and byte offset."""

    path = Path(path)
    match = re.fullmatch(r"([0-9]{6})_(700[1238])\.DAT", path.name)
    if match is None or market not in {"SH", "SZ"}:
        raise ValueError(f"unsupported native financial file: {path.name}/{market}")
    stock, kind = match.groups()
    table, width, announcement_offset, fields = _LAYOUTS[kind]
    payload = path.read_bytes()
    digest = sha256(payload).hexdigest()
    if digest != expected_sha256:
        raise ValueError(f"native file checksum mismatch: {path.name}")
    if len(payload) % width:
        raise ValueError(f"invalid native record length: {path.name}")

    rows: list[dict[str, Any]] = []
    for offset in range(0, len(payload), width):
        record = payload[offset : offset + width]
        report_ms = struct.unpack_from("<Q", record, 0)[0]
        announcement_ms = struct.unpack_from("<Q", record, announcement_offset)[0]
        report_date = _date_from_ms(report_ms)
        announcement_date = _date_from_ms(announcement_ms)
        if report_date is None or announcement_date is None:
            raise ValueError(f"invalid native timestamp: {path.name}:{offset}")
        if announcement_date <= report_date:
            raise ValueError(f"invalid announcement date: {path.name}:{offset}")
        rows.append(
            {
                "stock_code": f"{stock}.{market}",
                "source_table": table,
                "report_date": report_date.isoformat(),
                "announcement_date": announcement_date.isoformat(),
                "date_evidence": "qmt_native_m_anntime_candidate",
                "native_file": path.name,
                "native_file_sha256": digest,
                "native_offset": offset,
                "source_hash": sha256(record).hexdigest(),
                "raw_fields": {
                    "m_timetag": report_ms,
                    "m_anntime": announcement_ms,
                    **{name: _numeric(record, field_offset) for name, field_offset in fields.items()},
                },
            }
        )
    return rows

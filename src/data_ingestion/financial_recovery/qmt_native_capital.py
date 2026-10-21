"""Read QMT capital changes without conflating announcement and effect."""

from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import re
import struct
from typing import Any

from .qmt_native_reader import _numeric
from .qmt_raw_archive import _date_from_ms


_WIDTH = 56


def read_native_capital_file(
    path: Path, *, market: str, expected_sha256: str
) -> list[dict[str, Any]]:
    path = Path(path)
    match = re.fullmatch(r"([0-9]{6})_7004\.DAT", path.name)
    if match is None or market not in {"SH", "SZ"}:
        raise ValueError(f"unsupported native capital file: {path.name}/{market}")
    stock = match.group(1)
    payload = path.read_bytes()
    digest = sha256(payload).hexdigest()
    if digest != expected_sha256:
        raise ValueError(f"native capital checksum mismatch: {path.name}")
    if len(payload) % _WIDTH:
        raise ValueError(f"invalid native capital record length: {path.name}")

    rows: list[dict[str, Any]] = []
    for offset in range(0, len(payload), _WIDTH):
        record = payload[offset : offset + _WIDTH]
        change_ms, announcement_ms = struct.unpack_from("<QQ", record, 0)
        change_date = _date_from_ms(change_ms)
        announcement_date = _date_from_ms(announcement_ms)
        if change_date is None or announcement_date is None:
            raise ValueError(f"invalid capital date: {path.name}:{offset}")
        total_shares = _numeric(record, 16)
        circulating_shares = _numeric(record, 24)
        if total_shares is None or total_shares <= 0:
            raise ValueError(f"invalid total shares: {path.name}:{offset}")
        if (
            circulating_shares is None or circulating_shares < 0
            or circulating_shares > total_shares
        ):
            raise ValueError(f"invalid circulating shares: {path.name}:{offset}")
        rows.append(
            {
                "stock_code": f"{stock}.{market}",
                "source_table": "CAPITALSTRUCTURE",
                "report_date": change_date.isoformat(),
                "announcement_date": announcement_date.isoformat(),
                "first_usable_date": max(change_date, announcement_date).isoformat(),
                "date_evidence": "qmt_native_m_anntime_candidate",
                "total_shares": total_shares,
                "circulating_shares": circulating_shares,
                "restricted_shares": _numeric(record, 32),
                "free_float_shares": _numeric(record, 40),
                "native_file": path.name,
                "native_file_sha256": digest,
                "native_offset": offset,
                "source_hash": sha256(record).hexdigest(),
                "raw_fields": {
                    "m_timetag": change_ms,
                    "m_anntime": announcement_ms,
                },
            }
        )
    return rows

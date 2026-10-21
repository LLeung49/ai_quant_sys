"""Offline QMT financial records retain each disclosure version."""

from datetime import date
from hashlib import sha256
from pathlib import Path
import struct

import pytest

from data_ingestion.financial_recovery.qmt_native_reader import read_native_financial_file


def _record(*, report_ms: int, announcement_ms: int, revenue: float) -> bytes:
    raw = bytearray(664)
    struct.pack_into("<Q", raw, 0, report_ms)
    struct.pack_into("<Q", raw, 8, report_ms)
    struct.pack_into("<Q", raw, 16, announcement_ms)
    struct.pack_into("<d", raw, 248, revenue)
    struct.pack_into("<d", raw, 224, revenue / 10)
    struct.pack_into("<d", raw, 352, revenue / 8)
    return bytes(raw)


def test_income_reader_keeps_two_versions_of_same_period(tmp_path: Path) -> None:
    first = _record(
        report_ms=1427731200000,
        announcement_ms=1430323200000,
        revenue=100.0,
    )
    revised = _record(
        report_ms=1427731200000,
        announcement_ms=1461964800000,
        revenue=110.0,
    )
    file = tmp_path / "600000_7002.DAT"
    payload = first + revised
    file.write_bytes(payload)

    rows = read_native_financial_file(
        file, market="SH", expected_sha256=sha256(payload).hexdigest()
    )

    assert len(rows) == 2
    assert [r["report_date"] for r in rows] == ["2015-03-31"] * 2
    assert [r["announcement_date"] for r in rows] == [
        "2015-04-30", "2016-04-30"
    ]
    assert [r["raw_fields"]["revenue"] for r in rows] == [100.0, 110.0]
    assert [r["raw_fields"]["net_profit_incl_min_int_inc"] for r in rows] == [
        12.5, 13.75
    ]
    assert [r["native_offset"] for r in rows] == [0, 664]
    assert rows[0]["source_hash"] != rows[1]["source_hash"]
    assert rows[0]["source_table"] == "ASHAREINCOME"


def test_native_reader_rejects_checksum_or_record_length_change(tmp_path: Path) -> None:
    file = tmp_path / "600000_7002.DAT"
    file.write_bytes(_record(
        report_ms=1427731200000,
        announcement_ms=1430323200000,
        revenue=100.0,
    ))
    with pytest.raises(ValueError, match="checksum"):
        read_native_financial_file(file, market="SH", expected_sha256="0" * 64)

    file.write_bytes(file.read_bytes() + b"\x00")
    with pytest.raises(ValueError, match="record length"):
        read_native_financial_file(
            file, market="SH", expected_sha256=sha256(file.read_bytes()).hexdigest()
        )


def test_native_reader_rejects_report_period_used_as_announcement(tmp_path: Path) -> None:
    payload = _record(
        report_ms=1427731200000,
        announcement_ms=1427731200000,
        revenue=100.0,
    )
    file = tmp_path / "600000_7002.DAT"
    file.write_bytes(payload)
    with pytest.raises(ValueError, match="announcement"):
        read_native_financial_file(
            file, market="SH", expected_sha256=sha256(payload).hexdigest()
        )

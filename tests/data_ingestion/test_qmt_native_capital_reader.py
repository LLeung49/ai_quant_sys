"""QMT native capital dates separate disclosure from share-change effect."""

from hashlib import sha256
import struct

import pytest

from data_ingestion.financial_recovery.qmt_native_capital import read_native_capital_file


def test_native_capital_reader_retains_early_announcement_and_effective_date(tmp_path):
    record = bytearray(56)
    struct.pack_into("<Q", record, 0, 1792886400000)  # 2026-10-25
    struct.pack_into("<Q", record, 8, 1791590400000)  # 2026-10-10
    struct.pack_into("<d", record, 16, 1_000_000_000.0)
    struct.pack_into("<d", record, 24, 800_000_000.0)
    path = tmp_path / "600000_7004.DAT"
    path.write_bytes(record)

    rows = read_native_capital_file(
        path, market="SH", expected_sha256=sha256(record).hexdigest()
    )

    assert len(rows) == 1
    assert rows[0]["report_date"] == "2026-10-25"
    assert rows[0]["announcement_date"] == "2026-10-10"
    assert rows[0]["first_usable_date"] == "2026-10-25"
    assert rows[0]["total_shares"] == 1_000_000_000.0
    assert rows[0]["circulating_shares"] == 800_000_000.0


def test_native_capital_reader_rejects_bad_share_count(tmp_path):
    record = bytearray(56)
    struct.pack_into("<Q", record, 0, 1792886400000)
    struct.pack_into("<Q", record, 8, 1791590400000)
    struct.pack_into("<d", record, 16, 100.0)
    struct.pack_into("<d", record, 24, 200.0)
    path = tmp_path / "600000_7004.DAT"
    path.write_bytes(record)
    with pytest.raises(ValueError, match="circulating"):
        read_native_capital_file(
            path, market="SH", expected_sha256=sha256(record).hexdigest()
        )

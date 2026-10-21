"""AKShare daily observations are durable before PIT publication."""

from datetime import date
import gzip
import json

import pandas as pd

from data_ingestion.financial_recovery.akshare_archive import archive_snapshot, read_snapshot


def test_archive_preserves_source_payload_and_first_capture(tmp_path) -> None:
    row = {"stock_code": "600519.SH", "report_date": date(2026, 6, 30),
           "source_hash": "a" * 64,
           "source_payload": {"income": {"NOTICE_DATE": pd.Timestamp("2026-08-15"),
                                         "OPTIONAL": pd.NaT, "EPS": float("nan")}}}
    first = archive_snapshot([row], stock_code="600519.SH", as_of_date=date(2026, 10, 20),
                             kind="financial", root=tmp_path)
    second = archive_snapshot([row], stock_code="600519.SH", as_of_date=date(2026, 10, 20),
                              kind="financial", root=tmp_path)
    assert first == second
    with gzip.open(first, "rt", encoding="utf-8") as source:
        payload = json.load(source)
    assert payload["rows"][0]["source_payload"]["income"]["NOTICE_DATE"] == "2026-08-15T00:00:00"
    assert payload["rows"][0]["source_payload"]["income"]["OPTIONAL"] is None
    assert payload["rows"][0]["source_payload"]["income"]["EPS"] is None
    assert payload["captured_at"]
    recovered = read_snapshot(first)
    assert recovered["kind"] == "financial"
    assert recovered["rows"][0]["report_date"] == date(2026, 6, 30)


def test_archive_replay_detects_changed_file_content(tmp_path) -> None:
    row = {"stock_code": "600519.SH", "report_date": date(2026, 6, 30),
           "source_hash": "a" * 64}
    path = archive_snapshot([row], stock_code="600519.SH", as_of_date=date(2026, 10, 20),
                            kind="financial", root=tmp_path)
    import pytest
    with gzip.open(path, "rt", encoding="utf-8") as source:
        payload = json.load(source)
    payload["rows"][0]["stock_code"] = "000001.SZ"
    with gzip.open(path, "wt", encoding="utf-8") as output:
        json.dump(payload, output)
    with pytest.raises(ValueError, match="checksum"):
        read_snapshot(path)

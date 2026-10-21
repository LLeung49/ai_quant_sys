"""The QMT raw archive must preserve disclosure evidence without fallback."""

from datetime import datetime, timezone
import json
import math

from data_ingestion.financial_recovery.qmt_raw_archive import (
    archive_raw_financial_response,
    write_archive_jsonl,
)


def test_raw_archive_preserves_real_announcement_and_revision_versions(tmp_path) -> None:
    response = {
        "600000.SH": {
            "ASHAREINCOME": [
                {"m_timetag": 1427731200000, "m_anntime": 1430323200000,
                 "revenue": 100.0},
                {"m_timetag": 1427731200000, "m_anntime": 1461964800000,
                 "revenue": 105.0},
            ]
        }
    }
    captured = datetime(2026, 10, 20, 10, 0, tzinfo=timezone.utc)
    rows = archive_raw_financial_response(response, captured_at=captured)

    assert len(rows) == 2
    assert [row["report_date"] for row in rows] == ["2015-03-31"] * 2
    assert [row["announcement_date"] for row in rows] == [
        "2015-04-30", "2016-04-30"
    ]
    assert [row["raw_fields"]["revenue"] for row in rows] == [100.0, 105.0]
    assert rows[0]["source_hash"] != rows[1]["source_hash"]
    assert all(row["date_evidence"] == "qmt_raw_m_anntime" for row in rows)

    output = tmp_path / "qmt.jsonl"
    write_archive_jsonl(rows, output)
    assert [json.loads(line)["source_hash"] for line in output.read_text().splitlines()] == [
        row["source_hash"] for row in rows
    ]


def test_missing_announcement_never_falls_back_to_report_date() -> None:
    response = {
        "000001.SZ": {
            "ASHAREBALANCESHEET": [
                {"m_timetag": 1427731200000, "m_anntime": math.nan,
                 "tot_assets": 50.0},
            ]
        }
    }
    rows = archive_raw_financial_response(
        response, captured_at=datetime(2026, 10, 20, tzinfo=timezone.utc)
    )
    assert rows[0]["report_date"] == "2015-03-31"
    assert rows[0]["announcement_date"] is None
    assert rows[0]["raw_fields"]["m_anntime"] is None
    assert rows[0]["date_evidence"] == "missing"


def test_invalid_report_time_is_rejected() -> None:
    response = {"600000.SH": {"ASHAREINCOME": [{"m_timetag": 0}]}}
    try:
        archive_raw_financial_response(
            response, captured_at=datetime(2026, 10, 20, tzinfo=timezone.utc)
        )
    except ValueError as exc:
        assert "m_timetag" in str(exc)
    else:
        raise AssertionError("invalid report time was accepted")

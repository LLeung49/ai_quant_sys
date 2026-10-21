"""The offline staging pass must preserve revisions and reject bad archives."""

import gzip
import hashlib
import json

import pytest

from data_ingestion.financial_recovery.native_pit_stage import stage_native_pit


def _row(table, value):
    fields = {
        "ASHAREBALANCESHEET": {"tot_assets": 200., "total_equity": 80.},
        "ASHAREINCOME": {"revenue": 100., "net_profit_incl_min_int_inc": 10.},
        "ASHARECASHFLOW": {"net_cash_flows_oper_act": 5.},
        "PERSHAREINDEX": {"s_fa_eps_basic": 1.},
    }
    return {"stock_code": "600000.SH", "report_date": "2015-03-31",
            "announcement_date": "2015-04-30", "source_table": table,
            "source_hash": value, "raw_fields": fields[table]}


def test_stage_validates_archive_and_emits_one_candidate(tmp_path):
    folder = tmp_path / "archive"
    folder.mkdir()
    groups = []
    for kind, table in [("7001", "ASHAREBALANCESHEET"),
                        ("7002", "ASHAREINCOME"),
                        ("7003", "ASHARECASHFLOW"),
                        ("7008", "PERSHAREINDEX")]:
        path = folder / f"SH-{kind}.jsonl.gz"
        with gzip.open(path, "wt", encoding="utf-8") as out:
            out.write(json.dumps(_row(table, kind)) + "\n")
        groups.append({"market": "SH", "kind": kind, "records": 1,
                       "archive": str(path),
                       "archive_sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
    manifest = folder / "archive-summary.json"
    manifest.write_text(json.dumps({"groups": groups}), encoding="utf-8")
    output = tmp_path / "staged"
    result = stage_native_pit(manifest, output)
    assert result["input_records"] == 4
    assert result["candidate_rows"] == 1
    with gzip.open(output / "candidates.jsonl.gz", "rt", encoding="utf-8") as rows:
        assert json.loads(rows.readline())["announcement_date"] == "2015-04-30"
    groups[0]["archive_sha256"] = "wrong"
    manifest.write_text(json.dumps({"groups": groups}), encoding="utf-8")
    with pytest.raises(ValueError, match="checksum"):
        stage_native_pit(manifest, tmp_path / "bad")

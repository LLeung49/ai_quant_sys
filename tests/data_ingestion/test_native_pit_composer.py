"""QMT statement timelines must become dated, versioned PIT candidates."""

from data_ingestion.financial_recovery.native_pit_composer import compose_native_pit_versions


def _row(table, date, fields, *, hash_value):
    return {
        "stock_code": "600000.SH", "report_date": "2015-03-31",
        "source_table": table, "announcement_date": date,
        "source_hash": hash_value, "raw_fields": fields,
    }


def test_composer_waits_for_all_statements_and_keeps_later_revision() -> None:
    records = [
        _row("ASHAREBALANCESHEET", "2015-04-30",
             {"tot_assets": 200.0, "total_equity": 80.0}, hash_value="b1"),
        _row("ASHAREINCOME", "2015-04-30",
             {"revenue": 100.0, "net_profit_incl_min_int_inc": 10.0},
             hash_value="i1"),
        _row("ASHARECASHFLOW", "2015-05-01",
             {"net_cash_flows_oper_act": 5.0}, hash_value="c1"),
        _row("ASHAREINCOME", "2016-04-30",
             {"revenue": 110.0, "net_profit_incl_min_int_inc": 11.0},
             hash_value="i2"),
    ]
    result = compose_native_pit_versions(records)
    rows = result["candidates"]
    assert [r["announcement_date"] for r in rows] == [
        "2015-05-01", "2016-04-30"
    ]
    assert [r["revenue"] for r in rows] == [100.0, 110.0]
    assert [r["net_profit"] for r in rows] == [10.0, 11.0]
    assert rows[0]["source_hash"] != rows[1]["source_hash"]
    assert result["conflicts"] == []


def test_composer_adds_pershare_metrics_only_when_visible() -> None:
    records = [
        _row("ASHAREBALANCESHEET", "2015-04-30",
             {"tot_assets": 200.0, "total_equity": 80.0}, hash_value="b1"),
        _row("ASHAREINCOME", "2015-04-30",
             {"revenue": 100.0, "net_profit_incl_min_int_inc": 10.0},
             hash_value="i1"),
        _row("ASHARECASHFLOW", "2015-04-30",
             {"net_cash_flows_oper_act": 5.0}, hash_value="c1"),
        _row("PERSHAREINDEX", "2015-05-01",
             {"s_fa_eps_basic": 1.2, "du_return_on_equity": 10.5},
             hash_value="p1"),
    ]
    rows = compose_native_pit_versions(records)["candidates"]
    assert len(rows) == 2
    assert rows[0]["eps"] is None
    assert rows[1]["eps"] == 1.2
    assert rows[1]["roe"] == 10.5
    assert rows[1]["metric_available_at"] == "2015-05-01"


def test_composer_quarantines_conflicting_same_day_versions() -> None:
    records = [
        _row("ASHAREBALANCESHEET", "2015-04-30",
             {"tot_assets": 200.0, "total_equity": 80.0}, hash_value="b1"),
        _row("ASHAREINCOME", "2015-04-30",
             {"revenue": 100.0, "net_profit_incl_min_int_inc": 10.0},
             hash_value="i1"),
        _row("ASHAREINCOME", "2015-04-30",
             {"revenue": 110.0, "net_profit_incl_min_int_inc": 11.0},
             hash_value="i2"),
        _row("ASHARECASHFLOW", "2015-04-30",
             {"net_cash_flows_oper_act": 5.0}, hash_value="c1"),
    ]
    result = compose_native_pit_versions(records)
    assert result["candidates"] == []
    assert len(result["conflicts"]) == 1


def test_conflict_does_not_reappear_on_unrelated_later_event() -> None:
    records = [
        _row("ASHAREBALANCESHEET", "2015-04-29",
             {"tot_assets": 200., "total_equity": 80.}, hash_value="b1"),
        _row("ASHAREINCOME", "2015-04-29",
             {"revenue": 100., "net_profit_incl_min_int_inc": 10.}, hash_value="i1"),
        _row("ASHARECASHFLOW", "2015-04-29",
             {"net_cash_flows_oper_act": 5.}, hash_value="c1"),
        _row("ASHAREINCOME", "2015-04-30",
             {"revenue": 110., "net_profit_incl_min_int_inc": 11.}, hash_value="i2"),
        _row("ASHAREINCOME", "2015-04-30",
             {"revenue": 120., "net_profit_incl_min_int_inc": 12.}, hash_value="i3"),
        _row("PERSHAREINDEX", "2015-05-01",
             {"s_fa_eps_basic": 1.}, hash_value="p1"),
    ]
    assert [row["announcement_date"] for row in compose_native_pit_versions(records)["candidates"]] == ["2015-04-29"]

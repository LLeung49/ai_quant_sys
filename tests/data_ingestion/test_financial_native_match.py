"""PIT core values need statement-version evidence before assigning dates."""

from datetime import date
from decimal import Decimal

from data_ingestion.financial_recovery.native_match import match_pit_to_native


def _row(table: str, announcement: str, **fields):
    return {
        "stock_code": "600000.SH",
        "source_table": table,
        "report_date": "2015-03-31",
        "announcement_date": announcement,
        "raw_fields": fields,
    }


def test_match_uses_first_date_when_every_core_value_was_visible() -> None:
    pit = {
        "stock_code": "600000.SH",
        "report_date": date(2015, 3, 31),
        "revenue": Decimal("110.0000"),
        "net_profit": Decimal("11.0000"),
        "total_assets": Decimal("200.0000"),
        "total_equity": Decimal("80.0000"),
        "operating_cash_flow": Decimal("5.0000"),
    }
    rows = [
        _row("ASHAREBALANCESHEET", "2015-04-30",
             tot_assets=200.0, total_equity=80.0),
        _row("ASHAREINCOME", "2015-04-30",
             revenue=100.0, net_profit_incl_min_int_inc=10.0),
        _row("ASHAREINCOME", "2016-04-30",
             revenue=110.0, net_profit_incl_min_int_inc=11.0),
        _row("ASHARECASHFLOW", "2015-05-01",
             net_cash_flows_oper_act=5.0),
    ]
    result = match_pit_to_native(pit, rows)
    assert result["status"] == "matched"
    assert result["first_visible_date"] == "2016-04-30"
    assert result["component_dates"]["income"] == "2016-04-30"


def test_missing_or_different_values_never_gain_exact_date() -> None:
    pit = {
        "stock_code": "600000.SH", "report_date": date(2015, 3, 31),
        "revenue": Decimal("110.0000"), "net_profit": Decimal("11.0000"),
        "total_assets": Decimal("200.0000"), "total_equity": Decimal("80.0000"),
        "operating_cash_flow": Decimal("5.0000"),
    }
    balance = _row("ASHAREBALANCESHEET", "2015-04-30",
                   tot_assets=200.0, total_equity=80.0)
    income = _row("ASHAREINCOME", "2015-04-30",
                  revenue=100.0, net_profit_incl_min_int_inc=10.0)
    assert match_pit_to_native(pit, [balance, income])["status"] == "missing_statement"
    cash = _row("ASHARECASHFLOW", "2015-05-01",
                net_cash_flows_oper_act=5.0)
    result = match_pit_to_native(pit, [balance, income, cash])
    assert result["status"] == "numeric_mismatch"
    assert result["first_visible_date"] is None

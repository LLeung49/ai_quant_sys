from datetime import date

import pandas as pd
import pytest

from data_ingestion.akshare_financial_provider import AKShareFinancialProvider, _date


def _frame(**columns):
    return pd.DataFrame(columns)


def test_provider_merges_statements_and_uses_latest_notice_date() -> None:
    provider = AKShareFinancialProvider(
        fetch_balance=lambda _symbol: _frame(
            REPORT_DATE=["2026-06-30"], NOTICE_DATE=["2026-08-14"],
            UPDATE_DATE=["2026-08-14"], TOTAL_ASSETS=[1000],
            TOTAL_LIABILITIES=[600], TOTAL_EQUITY=[400],
            TOTAL_CURRENT_ASSETS=[300], TOTAL_CURRENT_LIAB=[200],
        ),
        fetch_income=lambda _symbol: _frame(
            REPORT_DATE=["2026-06-30"], NOTICE_DATE=["2026-08-15"],
            UPDATE_DATE=["2026-08-15"], TOTAL_OPERATE_INCOME=[100],
            PARENT_NETPROFIT=[10], TOTAL_OPERATE_COST=[70], BASIC_EPS=[0.5],
        ),
        fetch_cash=lambda _symbol: _frame(
            REPORT_DATE=["2026-06-30"], NOTICE_DATE=["2026-08-13"],
            UPDATE_DATE=["2026-08-13"], NETCASH_OPERATE=[20],
        ),
    )

    rows = provider.fetch("600519.SH", as_of_date=date(2026, 10, 15))

    assert len(rows) == 1
    row = rows[0]
    assert row["report_date"] == date(2026, 6, 30)
    assert row["announcement_date"] == date(2026, 8, 15)
    assert row["revenue"] == 100.0
    assert row["net_profit"] == 10.0
    assert row["operating_cash_flow"] == 20.0
    assert row["data_source"] == "akshare"
    assert row["pit_status"] == "pit_exact"
    assert row["original_announcement_date"] == date(2026, 8, 15)
    assert row["metric_available_at"] == date(2026, 8, 15)
    assert row["gross_margin"] is None  # total operating costs include more than COGS
    assert row["source_payload"]["income"]["PARENT_NETPROFIT"] == 10
    assert row["source_payload"]["balance"]["NOTICE_DATE"] == "2026-08-14"


def test_gross_margin_uses_operating_cost_not_total_operating_cost() -> None:
    base = {"REPORT_DATE": ["2026-06-30"], "NOTICE_DATE": ["2026-08-15"]}
    provider = AKShareFinancialProvider(
        fetch_balance=lambda _symbol: _frame(**base, TOTAL_ASSETS=[1000], TOTAL_EQUITY=[400]),
        fetch_income=lambda _symbol: _frame(**base, TOTAL_OPERATE_INCOME=[100],
                                            OPERATE_COST=[60], TOTAL_OPERATE_COST=[90],
                                            NETPROFIT=[10]),
        fetch_cash=lambda _symbol: _frame(**base, NETCASH_OPERATE=[20]),
    )
    row = provider.fetch("600519.SH", as_of_date=date(2026, 10, 15))[0]
    assert row["gross_margin"] == 40.0


def test_provider_excludes_rows_not_available_by_as_of_date() -> None:
    base = {
        "REPORT_DATE": ["2026-09-30"],
        "NOTICE_DATE": ["2026-10-31"],
        "UPDATE_DATE": ["2026-10-31"],
    }
    provider = AKShareFinancialProvider(
        fetch_balance=lambda _symbol: _frame(**base),
        fetch_income=lambda _symbol: _frame(**base),
        fetch_cash=lambda _symbol: _frame(**base),
    )

    assert provider.fetch("600519.SH", as_of_date=date(2026, 10, 15)) == []


def test_provider_rejects_zero_report_date() -> None:
    bad = {
        "REPORT_DATE": ["0000-00-00"],
        "NOTICE_DATE": ["2026-08-15"],
        "UPDATE_DATE": ["2026-08-15"],
    }
    provider = AKShareFinancialProvider(
        fetch_balance=lambda _symbol: _frame(**bad),
        fetch_income=lambda _symbol: _frame(**bad),
        fetch_cash=lambda _symbol: _frame(**bad),
    )

    with pytest.raises(ValueError, match="invalid report date"):
        provider.fetch("600519.SH", as_of_date=date(2026, 10, 15))


def test_provider_uses_later_update_date_as_pit_availability_date() -> None:
    base = {
        "REPORT_DATE": ["2026-06-30"],
        "NOTICE_DATE": ["2026-08-15"],
        "UPDATE_DATE": ["2026-10-20"],
    }
    provider = AKShareFinancialProvider(
        fetch_balance=lambda _symbol: _frame(**base, TOTAL_ASSETS=[1000]),
        fetch_income=lambda _symbol: _frame(**base, TOTAL_OPERATE_INCOME=[100]),
        fetch_cash=lambda _symbol: _frame(**base, NETCASH_OPERATE=[20]),
    )

    assert provider.fetch("600519.SH", as_of_date=date(2026, 10, 15)) == []
    rows = provider.fetch("600519.SH", as_of_date=date(2026, 10, 20))
    assert rows[0]["announcement_date"] == date(2026, 10, 20)
    assert rows[0]["is_restated"] == 1


def test_nat_is_rejected_as_a_date_and_skipped_in_capital_response() -> None:
    with pytest.raises(ValueError, match="invalid"):
        _date(pd.NaT, field="announcement date")
    frame = pd.DataFrame([
        {"变动日期": pd.Timestamp("2026-06-30"), "公告日期": pd.NaT,
         "总股本": 100, "已流通股份": 80},
        {"变动日期": pd.Timestamp("2026-07-01"),
         "公告日期": pd.Timestamp("2026-07-02"),
         "总股本": 100, "已流通股份": 80},
    ])
    provider = AKShareFinancialProvider(fetch_capital=lambda **_kwargs: frame)
    rows = provider.fetch_capital("600519.SH", as_of_date=date(2026, 10, 20))
    assert len(rows) == 1
    assert rows[0]["announcement_date"] == date(2026, 7, 2)


def test_financial_fetch_ignores_pre_2015_partial_history() -> None:
    provider = AKShareFinancialProvider(
        fetch_balance=lambda _symbol: _frame(
            REPORT_DATE=["2002-03-31", "2015-03-31"],
            NOTICE_DATE=["2002-04-15", "2015-04-15"],
            TOTAL_ASSETS=[100., 200.], TOTAL_EQUITY=[40., 80.]),
        fetch_income=lambda _symbol: _frame(
            REPORT_DATE=["2002-03-31", "2015-03-31"],
            NOTICE_DATE=["2002-04-15", "2015-04-15"],
            OPERATE_INCOME=[20., 30.], NETPROFIT=[2., 3.]),
        fetch_cash=lambda _symbol: _frame(
            REPORT_DATE=["2015-03-31"], NOTICE_DATE=["2015-04-15"],
            NETCASH_OPERATE=[5.]),
    )
    rows = provider.fetch("600519.SH", as_of_date=date(2026, 10, 20))
    assert [row["report_date"] for row in rows] == [date(2015, 3, 31)]

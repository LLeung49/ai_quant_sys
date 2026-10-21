from datetime import date
import importlib
from pathlib import Path

import pandas as pd
import pytest

from data_ingestion import akshare_financial_collection as collection
from data_ingestion.akshare_financial_collection import (
    get_disclosed_stock_codes,
    get_stock_universe,
    is_a_share_stock_code,
    persist_financial_rows,
    run_collection,
)


class Cursor:
    def __init__(self):
        self.calls = []
        self.rowcount = 1

    def execute(self, sql, params):
        self.calls.append((" ".join(sql.split()), params))

    def close(self):
        pass


class Connection:
    def __init__(self):
        self.cursor_value = Cursor()
        self.commits = 0
        self.rollbacks = 0

    def cursor(self):
        return self.cursor_value

    def commit(self):
        self.commits += 1

    def rollback(self):
        self.rollbacks += 1

    def close(self):
        pass


def financial_row(stock_code="600519.SH"):
    return {
        "stock_code": stock_code,
        "source_table": "akshare_eastmoney_financial",
        "report_date": date(2026, 6, 30),
        "announcement_date": date(2026, 8, 15),
        "period_type": "quarterly",
        "revenue": 100.0,
        "net_profit": 10.0,
        "eps": 0.5,
        "roe": 2.5,
        "roa": 1.0,
        "gross_margin": 30.0,
        "net_margin": 10.0,
        "debt_ratio": 60.0,
        "current_ratio": 1.5,
        "operating_cash_flow": 20.0,
        "total_assets": 1000.0,
        "total_equity": 400.0,
        "pit_status": "pit_exact",
        "source_updated_at": date(2026, 8, 15),
        "source_hash": "a" * 64,
        "is_restated": 0,
        "source_verified": 1,
        "data_source": "akshare",
        "metric_available_at": date(2026, 8, 15),
        "original_announcement_date": date(2026, 8, 15),
    }


def test_persist_financial_rows_preserves_legacy_wide_table_and_writes_pit_metrics():
    connection = Connection()

    written = persist_financial_rows(
        [financial_row()], connection_factory=lambda: connection
    )

    assert written == 1
    assert connection.commits == 1
    assert connection.rollbacks == 0
    sql = "\n".join(call[0] for call in connection.cursor_value.calls)
    assert "INSERT INTO trade_stock_financial " not in sql
    assert "INSERT IGNORE INTO trade_stock_financial_raw_pit" in sql
    assert "metric_available_at" in sql
    assert "eps" in sql and "roe" in sql
    assert len(connection.cursor_value.calls) == 1
    assert all(call[1][-1] == "akshare" for call in connection.cursor_value.calls)


@pytest.mark.parametrize("change", [
    {"total_assets": 0.0},
    {"net_profit": None},
    {"announcement_date": date(2026, 6, 1)},
    {"metric_available_at": date(2026, 8, 16)},
])
def test_persist_rejects_incomplete_or_future_akshare_versions(change):
    connection = Connection()
    with pytest.raises(ValueError):
        persist_financial_rows([dict(financial_row(), **change)],
                               connection_factory=lambda: connection)
    assert connection.commits == 0
    assert connection.cursor_value.calls == []


def test_collection_reports_provider_failure_without_writing():
    class Provider:
        def fetch(self, stock_code, *, as_of_date):
            if stock_code == "000001.SZ":
                raise RuntimeError("network")
            return [financial_row(stock_code)]

    writes = []
    result = run_collection(
        Provider(),
        ["000001.SZ", "600519.SH"],
        as_of_date=date(2026, 10, 16),
        dry_run=False,
        persist=lambda rows: writes.append(rows) or len(rows) * 2,
    )

    assert result.succeeded == 1
    assert result.failed == 1
    assert result.written_rows == 2
    assert len(writes) == 1


def test_collection_uses_requested_bounded_worker_pool(monkeypatch):
    real_pool = collection.ThreadPoolExecutor
    observed = []

    class RecordingPool(real_pool):
        def __init__(self, max_workers):
            observed.append(max_workers)
            super().__init__(max_workers=max_workers)

    class Provider:
        def fetch(self, stock_code, *, as_of_date):
            return [financial_row(stock_code)]

    monkeypatch.setattr(collection, "ThreadPoolExecutor", RecordingPool)
    result = run_collection(
        Provider(),
        ["000001.SZ", "600519.SH"],
        as_of_date=date(2026, 10, 16),
        dry_run=True,
        workers=3,
    )

    assert observed == [3]
    assert result.succeeded == 2


def test_collection_dry_run_checks_financial_core_before_reporting_success():
    class Provider:
        def fetch(self, stock_code, *, as_of_date):
            return [dict(financial_row(stock_code), net_profit=None)]

    result = run_collection(Provider(), ["600519.SH"],
                            as_of_date=date(2026, 10, 20), dry_run=True)
    assert result.failed == 1
    assert result.succeeded == 0
    assert "net_profit" in result.failures[0]["error"]


def test_collection_rejects_empty_financial_response_for_selected_stock():
    class Provider:
        def fetch(self, stock_code, *, as_of_date):
            return []

    result = run_collection(Provider(), ["600519.SH"],
                            as_of_date=date(2026, 10, 20), dry_run=True)
    assert result.failed == 1
    assert "financial_provider_empty" in result.failures[0]["error"]


def test_recent_disclosure_does_not_pass_on_only_stale_financial_reports():
    class Provider:
        def fetch(self, stock_code, *, as_of_date):
            return [financial_row(stock_code)]  # last announced 2026-08-15

    result = run_collection(
        Provider(), ["600519.SH"], as_of_date=date(2026, 10, 20),
        dry_run=True, recent_announcement_days=7,
    )
    assert result.failed == 1
    assert "recent_disclosure_missing" in result.failures[0]["error"]


def test_collection_rejects_financial_version_after_requested_date():
    class Provider:
        def fetch(self, stock_code, *, as_of_date):
            return [dict(financial_row(stock_code), announcement_date=date(2026, 10, 21))]

    result = run_collection(Provider(), ["600519.SH"],
                            as_of_date=date(2026, 10, 20), dry_run=True)
    assert result.failed == 1
    assert "future_financial_announcement" in result.failures[0]["error"]


def test_recent_collection_quarantines_old_bad_row_but_keeps_valid_new_report():
    class Provider:
        def fetch(self, stock_code, *, as_of_date):
            return [
                dict(financial_row(stock_code), report_date=date(2020, 3, 31),
                     announcement_date=date(2021, 6, 1),
                     metric_available_at=date(2021, 6, 1), total_assets=None),
                dict(financial_row(stock_code), report_date=date(2026, 9, 30),
                     announcement_date=date(2026, 10, 15),
                     metric_available_at=date(2026, 10, 15)),
            ]

    result = run_collection(
        Provider(), ["001207.SZ"], as_of_date=date(2026, 10, 20),
        dry_run=True, recent_announcement_days=7,
    )
    assert result.succeeded == 1
    assert result.failed == 0
    assert result.quarantined_rows == 1


def test_recent_collection_rejects_bad_new_report_even_with_valid_old_row():
    class Provider:
        def fetch(self, stock_code, *, as_of_date):
            return [
                financial_row(stock_code),
                dict(financial_row(stock_code), report_date=date(2026, 9, 30),
                     announcement_date=date(2026, 10, 15),
                     metric_available_at=date(2026, 10, 15), total_assets=None),
            ]

    result = run_collection(
        Provider(), ["001207.SZ"], as_of_date=date(2026, 10, 20),
        dry_run=True, recent_announcement_days=7,
    )
    assert result.failed == 1
    assert "total_assets" in result.failures[0]["error"]


def test_collection_archives_financial_response_before_pit_write(tmp_path):
    class Provider:
        def fetch(self, stock_code, *, as_of_date):
            return [financial_row(stock_code)]

    observed = []
    def persist(rows):
        files = list(tmp_path.rglob("*.json.gz"))
        observed.append(len(files))
        return len(rows)

    result = run_collection(Provider(), ["600519.SH"],
                            as_of_date=date(2026, 10, 20), dry_run=False,
                            persist=persist, archive_root=tmp_path)
    assert result.failed == 0
    assert observed == [1]


def test_canonical_financial_script_has_no_xtquant_runtime_dependency():
    module = importlib.import_module("data_ingestion.2-财务数据采集")
    source = Path(module.__file__).read_text(encoding="utf-8")

    assert "xtquant" not in source.lower()
    assert callable(module.main)


def test_a_share_filter_rejects_etfs_and_non_shenzhen_shanghai_codes():
    assert is_a_share_stock_code("000001.SZ")
    assert is_a_share_stock_code("301001.SZ")
    assert is_a_share_stock_code("600519.SH")
    assert is_a_share_stock_code("688795.SH")
    assert not is_a_share_stock_code("510300.SH")
    assert not is_a_share_stock_code("159915.SZ")
    assert not is_a_share_stock_code("430047.BJ")


def test_stock_universe_filters_out_etfs(monkeypatch):
    monkeypatch.setattr(
        collection,
        "execute_query",
        lambda _sql: [
            {"stock_code": "000001.SZ"},
            {"stock_code": "510300.SH"},
            {"stock_code": "600519.SH"},
        ],
    )

    assert get_stock_universe() == ["000001.SZ", "600519.SH"]


def test_disclosure_selector_uses_actual_date_window_and_a_share_codes():
    calls = []

    def fetch_disclosure(*, market, period):
        calls.append((market, period))
        return pd.DataFrame(
            [
                ["000001", "平安银行", None, None, None, None, date(2026, 10, 16)],
                ["510300", "沪深300ETF", None, None, None, None, date(2026, 10, 16)],
                ["600519", "贵州茅台", None, None, None, None, date(2026, 10, 8)],
                ["300750", "宁德时代", None, None, None, None, date(2026, 10, 9)],
            ],
            columns=[
                "股票代码", "股票简称", "首次预约", "初次变更",
                "二次变更", "三次变更", "实际披露",
            ],
        )

    codes = get_disclosed_stock_codes(
        as_of_date=date(2026, 10, 16),
        lookback_days=7,
        fetch_disclosure=fetch_disclosure,
    )

    assert codes == ["000001.SZ", "300750.SZ"]
    assert calls == [
        ("沪深京", "2025年报"),
        ("沪深京", "2026一季"),
        ("沪深京", "2026半年报"),
        ("沪深京", "2026三季"),
    ]


def test_main_treats_no_recent_disclosures_as_success(monkeypatch, capsys):
    monkeypatch.setattr(collection, "get_disclosed_stock_codes", lambda **_kwargs: [])

    assert collection.main(["--as-of-date", "2026-10-16"]) == 0
    assert '"codes": 0' in capsys.readouterr().out


def test_disclosure_selector_rejects_all_empty_provider_responses():
    with pytest.raises(ValueError, match="disclosure_provider_empty"):
        get_disclosed_stock_codes(
            as_of_date=date(2026, 10, 20),
            fetch_disclosure=lambda **_: pd.DataFrame(),
        )

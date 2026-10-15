from datetime import date
from pathlib import Path
import sys

import pytest


SRC_DIR = Path(__file__).parents[1] / "src"
INGESTION_DIR = SRC_DIR / "data_ingestion"
sys.path.insert(0, str(SRC_DIR))

from data_ingestion import price_projection_store as store  # noqa: E402
from data_ingestion import price_projection_integrity as integrity  # noqa: E402


def test_raw_qfq_validator_accepts_cash_adjusted_affine_projection():
    raw_rows = [{
        "stock_code": "515450.SH", "trade_date": "2020-02-26",
        "open_price": 0.970, "high_price": 0.999,
        "low_price": 0.970, "close_price": 0.994,
    }]
    qfq_rows = [{
        "stock_code": "515450.SH", "trade_date": "2020-02-26",
        "open_price": 0.530, "high_price": 0.559,
        "low_price": 0.530, "close_price": 0.554,
        "adjustment_asof": None,
    }]

    issues = integrity.find_raw_qfq_issues(raw_rows, qfq_rows)

    assert issues == []


def test_projection_audit_loads_raw_and_qfq_for_the_same_stock(monkeypatch):
    raw_rows = [{
        "stock_code": "515450.SH", "trade_date": "2020-02-26",
        "open_price": 0.970, "high_price": 0.999,
        "low_price": 0.970, "close_price": 0.994,
    }]
    qfq_rows = [{
        "stock_code": "515450.SH", "trade_date": "2020-02-26",
        "open_price": 0.530, "high_price": 0.559,
        "low_price": 0.530, "close_price": 0.554,
    }]
    calls = []

    def fake_query(sql, params):
        calls.append(params)
        return raw_rows if "trade_stock_daily_raw" in sql else qfq_rows

    monkeypatch.setattr(integrity, "execute_query", fake_query)

    issues = integrity.audit_raw_qfq_projection("515450.SH")

    assert issues == []
    assert calls == [("515450.SH",), ("515450.SH",)]


def test_mode_to_table_mapping_is_explicit_and_fixed():
    assert store.table_for_mode("none") == "trade_stock_daily_raw"
    assert store.table_for_mode("front") == "trade_stock_daily_qfq"
    assert store.table_for_mode("back") == "trade_stock_daily_bfq"

    with pytest.raises(ValueError, match="Unsupported dividend type"):
        store.table_for_mode("invalid")

    source = (INGESTION_DIR / "price_projection_store.py").read_text(encoding="utf-8")
    assert 'f"SELECT' not in source


def test_raw_rows_preserve_pre_close_and_suspend_flag(monkeypatch):
    written = []
    monkeypatch.setattr(store, "execute_many", lambda sql, rows: written.append((sql, rows)))

    store.write_daily_rows(
        "none",
        [
            {
                "stock_code": "600519.SH",
                "trade_date": "2025-01-02",
                "open_price": 10.0,
                "high_price": 11.0,
                "low_price": 9.0,
                "close_price": 10.5,
                "volume": 100,
                "amount": 1000.0,
                "pre_close": 9.8,
                "suspend_flag": 0,
            }
        ],
        adjustment_asof=date(2025, 1, 3),
    )

    sql, rows = written[0]
    assert "INSERT INTO trade_stock_daily_raw" in sql
    assert rows == [
        ("600519.SH", "2025-01-02", 10.0, 11.0, 9.0, 10.5, 100, 1000.0, 9.8, 0, "akshare")
    ]


def test_raw_rows_persist_the_actual_fallback_source(monkeypatch):
    written = []
    monkeypatch.setattr(store, "execute_many", lambda sql, rows: written.append((sql, rows)))

    store.write_daily_rows("none", [{
        "stock_code": "600519.SH", "trade_date": "2025-01-02",
        "open_price": 10.0, "high_price": 11.0, "low_price": 9.0,
        "close_price": 10.5, "volume": 100, "amount": 1000.0,
        "pre_close": 9.8, "suspend_flag": 0, "data_source": "akshare",
    }], adjustment_asof=None)

    sql, rows = written[0]
    assert "data_source" in sql
    assert rows[0][-1] == "akshare"


@pytest.mark.parametrize(
    ("mode", "table_name"),
    [("front", "trade_stock_daily_qfq"), ("back", "trade_stock_daily_bfq")],
)
def test_adjusted_rows_write_adjustment_asof_to_its_own_table(monkeypatch, mode, table_name):
    written = []
    monkeypatch.setattr(store, "execute_many", lambda sql, rows: written.append((sql, rows)))

    store.write_daily_rows(
        mode,
        [
            {
                "stock_code": "600519.SH",
                "trade_date": "2025-01-02",
                "open_price": 10.0,
                "high_price": 11.0,
                "low_price": 9.0,
                "close_price": 10.5,
                "volume": 100,
                "amount": 1000.0,
                "turnover_rate": None,
            }
        ],
        adjustment_asof=date(2025, 1, 3),
    )

    sql, rows = written[0]
    assert f"INSERT INTO {table_name}" in sql
    assert rows[-1][-1] == date(2025, 1, 3)


def test_batch_adjusted_rows_keep_each_stock_own_adjustment_asof(monkeypatch):
    """Batching must not assign one stock's corporate-action version to another stock."""
    written = []
    monkeypatch.setattr(store, "execute_many", lambda sql, rows: written.append((sql, rows)))

    store.write_daily_rows_batch(
        "front",
        [
            {
                "stock_code": "000001.SZ", "trade_date": "2025-01-02",
                "open_price": 10, "high_price": 11, "low_price": 9,
                "close_price": 10.5, "volume": 100, "amount": 1000,
            },
            {
                "stock_code": "600519.SH", "trade_date": "2025-01-02",
                "open_price": 20, "high_price": 21, "low_price": 19,
                "close_price": 20.5, "volume": 200, "amount": 2000,
            },
        ],
        {
            "000001.SZ": date(2025, 1, 1),
            "600519.SH": date(2025, 1, 2),
        },
    )

    sql, values = written[0]
    assert "INSERT INTO trade_stock_daily_qfq" in sql
    assert [row[-1] for row in values] == [date(2025, 1, 1), date(2025, 1, 2)]


def test_batch_write_splits_large_row_sets_into_database_chunks(monkeypatch):
    calls = []
    monkeypatch.setattr(
        store,
        "execute_many",
        lambda sql, rows: calls.append(list(rows)) or len(rows),
    )
    rows = [
        {
            "stock_code": "600519.SH", "trade_date": f"2025-01-{index:02d}",
            "open_price": 10, "high_price": 11, "low_price": 9,
            "close_price": 10.5, "volume": 100, "amount": 1000,
        }
        for index in range(1, 6)
    ]

    assert store.write_daily_rows_batch(
        "front", rows, {"600519.SH": date(2025, 1, 1)}, chunk_size=2
    ) == 5
    assert [len(chunk) for chunk in calls] == [2, 2, 1]

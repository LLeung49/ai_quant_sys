from datetime import date
import importlib.util
from pathlib import Path
import sys
import types

import pytest


SRC_DIR = Path(__file__).parents[1] / "src"
INGESTION_DIR = SRC_DIR / "data_ingestion"
sys.path.insert(0, str(SRC_DIR))

from data_ingestion import price_projection_store as store  # noqa: E402
from data_ingestion import price_projection_integrity as integrity  # noqa: E402


SCRIPT_PATH = INGESTION_DIR / "8-原始行情与复权数据采集.py"


def load_collector(fake_xtdata):
    fake_xtquant = types.ModuleType("xtquant")
    fake_xtquant.xtdata = fake_xtdata
    prior = sys.modules.get("xtquant")
    sys.modules["xtquant"] = fake_xtquant
    sys.path.insert(0, str(INGESTION_DIR))
    try:
        spec = importlib.util.spec_from_file_location("price_projection_collector", SCRIPT_PATH)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    finally:
        sys.path.remove(str(INGESTION_DIR))
        if prior is None:
            sys.modules.pop("xtquant", None)
        else:
            sys.modules["xtquant"] = prior


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
        ("600519.SH", "2025-01-02", 10.0, 11.0, 9.0, 10.5, 100, 1000.0, 9.8, 0, "xtquant")
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



def test_collector_fetches_none_front_and_back_without_importing_legacy_collector(monkeypatch):
    calls = []

    class OneRowDataFrame:
        def __len__(self):
            return 1

        def iterrows(self):
            yield "20250102", {
                "open": 10.0,
                "high": 11.0,
                "low": 9.0,
                "close": 10.5,
                "volume": 100,
                "amount": 1000.0,
                "preClose": 9.8,
                "suspendFlag": 0,
            }

    fake_xtdata = types.SimpleNamespace(
        download_history_data=lambda *args, **kwargs: None,
        get_market_data_ex=lambda **kwargs: calls.append(kwargs) or {"600519.SH": OneRowDataFrame()},
    )
    collector = load_collector(fake_xtdata)
    written = []
    monkeypatch.setattr(collector, "write_daily_rows", lambda mode, rows, adjustment_asof: written.append((mode, rows, adjustment_asof)))

    result = collector.download_and_save_all_modes("600519.SH", "20250101", date(2025, 1, 3))

    assert result == {"none": 1, "front": 1, "back": 1}
    assert [call["dividend_type"] for call in calls] == ["none", "front", "back"]
    assert [mode for mode, _, _ in written] == ["none", "front", "back"]
    assert written[0][1][0]["pre_close"] == 9.8
    assert written[0][1][0]["suspend_flag"] == 0
    source = SCRIPT_PATH.read_text(encoding="utf-8")
    assert "1-行情数据采集" not in source
    assert "download_and_save(" not in source


def test_all_mode_rebuild_rejects_invalid_raw_qfq_candidate_before_writing(monkeypatch):
    class OneRowDataFrame:
        def __init__(self, open_price, close_price):
            self.open_price = open_price
            self.close_price = close_price

        def __len__(self):
            return 1

        def iterrows(self):
            yield "20250102", {
                "open": self.open_price, "high": self.open_price,
                "low": self.open_price, "close": self.close_price,
                "volume": 100, "amount": 1000.0,
                "preClose": self.close_price, "suspendFlag": 0,
            }

    fake_xtdata = types.SimpleNamespace(
        download_history_data=lambda *args, **kwargs: None,
        get_market_data_ex=lambda **kwargs: {
            "515450.SH": OneRowDataFrame(
                1.0 if kwargs["dividend_type"] == "none" else 0.5,
                1.0 if kwargs["dividend_type"] == "none" else 0.55,
            )
        },
    )
    collector = load_collector(fake_xtdata)
    writes = []
    monkeypatch.setattr(
        collector, "write_daily_rows",
        lambda *args: writes.append(args),
    )

    with pytest.raises(RuntimeError, match="raw/qfq candidate integrity failed"):
        collector.download_and_save_all_modes("515450.SH", "20250101")

    assert writes == []


def test_batch_rejects_invalid_raw_qfq_candidate_before_any_mode_is_written(monkeypatch):
    class OneRowDataFrame:
        def __init__(self, mode):
            self.mode = mode

        def __len__(self):
            return 1

        def iterrows(self):
            qfq = self.mode == "front"
            yield "20250102", {
                "open": 0.5 if qfq else 1.0,
                "high": 0.5 if qfq else 1.0,
                "low": 0.5 if qfq else 1.0,
                "close": 0.55 if qfq else 1.0,
                "volume": 100, "amount": 1000.0,
                "preClose": 1.0, "suspendFlag": 0,
            }

    fake_xtdata = types.SimpleNamespace(
        download_history_data=lambda *args, **kwargs: None,
        get_market_data_ex=lambda **kwargs: {
            "515450.SH": OneRowDataFrame(kwargs["dividend_type"])
        },
    )
    collector = load_collector(fake_xtdata)
    writes = []
    monkeypatch.setattr(
        collector, "write_daily_rows_batch",
        lambda *args: writes.append(args),
    )

    counts, failed_codes = collector.download_and_save_batch(
        ["515450.SH"], "20250101", {"515450.SH": None}
    )

    assert counts == {"none": 0, "front": 0, "back": 0}
    assert failed_codes == ["515450.SH"]
    assert writes == []


def test_daily_integrity_repair_rebuilds_from_full_history_and_reverifies(monkeypatch):
    collector = load_collector(types.SimpleNamespace())
    issue = integrity.RawQfqIssue(
        "515450.SH", "2020-02-26", "qfq_ohlc_factor_mismatch"
    )
    audits = iter([[issue], []])
    calls = []
    monkeypatch.setattr(collector, "audit_raw_qfq_projection", lambda code: next(audits))
    monkeypatch.setattr(
        collector, "download_and_save_all_modes",
        lambda code, start, asof: calls.append((code, start, asof))
        or {"none": 100, "front": 100, "back": 100},
    )

    result = collector.audit_and_repair_projection(
        "515450.SH", date(2026, 9, 9)
    )

    assert result == {"detected": 1, "repaired": 1, "failed": 0}
    assert calls == [("515450.SH", collector.DATA_START, date(2026, 9, 9))]


def test_daily_integrity_repair_fails_closed_when_audit_is_unavailable(monkeypatch):
    collector = load_collector(types.SimpleNamespace())
    monkeypatch.setattr(
        collector, "audit_raw_qfq_projection",
        lambda code: (_ for _ in ()).throw(RuntimeError("database unavailable")),
    )

    result = collector.audit_and_repair_projection("515450.SH", None)

    assert result == {"detected": 0, "repaired": 0, "failed": 1}


def test_single_code_history_download_uses_single_code_qmt_api():
    calls = []
    fake_xtdata = types.SimpleNamespace(
        download_history_data=lambda *args, **kwargs: calls.append(("single", args, kwargs)),
        download_history_data2=lambda *args, **kwargs: calls.append(("batch", args, kwargs)),
    )
    collector = load_collector(fake_xtdata)

    collector._download_history_batch(["600519.SH"], "20260715")

    assert calls == [("single", ("600519.SH", "1d", "20260715", ""), {})]


def test_collector_backfills_all_modes_when_one_projection_table_is_empty():
    collector = load_collector(types.SimpleNamespace())

    assert collector._earliest_start(
        {
            "none": {"600519.SH": "20250724"},
            "front": {},
            "back": {"600519.SH": "20250724"},
        },
        "600519.SH",
    ) == collector.DATA_START


def test_collector_retries_unresolved_current_date_from_last_successful_date():
    collector = load_collector(types.SimpleNamespace())

    assert collector._earliest_start(
        {
            "none": {"515443.SH": "20260819"},
            "front": {"515443.SH": "20260819"},
            "back": {"515443.SH": "20260819"},
        },
        "515443.SH",
    ) == "20260819"


def test_collector_classifies_current_date_fallback_failure_as_pending():
    collector = load_collector(types.SimpleNamespace())

    pending, failed = collector._classify_fallback_failures(
        {
            "2026-08-20": "AkShare response missing target date",
            "2026-08-19": "provider unavailable",
        },
        asof="2026-08-20",
    )

    assert pending == {"2026-08-20": "AkShare response missing target date"}
    assert failed == {"2026-08-19": "provider unavailable"}


def test_collector_normalizes_share_volume_from_fallback_to_lot():
    collector = load_collector(types.SimpleNamespace())

    rows = collector._rows_from_fallback(
        "600000.SH",
        {
            "2026-08-28": {
                "open": 10,
                "high": 10,
                "low": 10,
                "close": 10,
                "volume": 100_000,
                "amount": 1_000_000,
            }
        },
        "none",
    )

    assert rows[0]["volume"] == 1_000


def test_collector_treats_each_mode_empty_response_as_failure(monkeypatch):
    fake_xtdata = types.SimpleNamespace(
        download_history_data=lambda *args, **kwargs: None,
        get_market_data_ex=lambda **kwargs: {},
    )
    collector = load_collector(fake_xtdata)
    monkeypatch.setattr(
        collector,
        "write_daily_rows",
        lambda *args, **kwargs: pytest.fail("empty market data must not be written"),
    )

    with pytest.raises(RuntimeError, match="empty QMT front-adjusted market response"):
        collector.download_and_save_mode(
            "600519.SH",
            "front",
            "20250101",
            adjustment_asof=None,
        )


def test_collector_skips_nan_core_field_and_logs_full_context(capsys):
    """A NaN amount must not reach MySQL, but other daily rows remain usable."""
    class TwoRowDataFrame:
        def iterrows(self):
            yield "20260728", {
                "open": 10.0,
                "high": 11.0,
                "low": 9.0,
                "close": 10.5,
                "volume": 100,
                "amount": float("nan"),
            }
            yield "20260729", {
                "open": 11.0,
                "high": 12.0,
                "low": 10.0,
                "close": 11.5,
                "volume": 200,
                "amount": 2000.0,
            }

    collector = load_collector(types.SimpleNamespace())

    rows = collector._rows_from_dataframe("600519.SH", TwoRowDataFrame(), "none")

    assert [row["trade_date"] for row in rows] == ["2026-07-29"]
    output = capsys.readouterr().out
    assert "stock=600519.SH" in output
    assert "trade_date=2026-07-28" in output
    assert "mode=none" in output
    assert "field=amount" in output
    assert "value=nan" in output


def test_batch_writes_valid_rows_when_another_row_has_nan(monkeypatch):
    """A valid fallback keeps both the stock and its normal QMT row writable."""
    class TwoRowDataFrame:
        def __len__(self):
            return 2

        def iterrows(self):
            yield "20260728", {
                "open": 10.0,
                "high": 11.0,
                "low": 9.0,
                "close": 10.5,
                "volume": 100,
                "amount": float("nan"),
            }
            yield "20260729", {
                "open": 11.0,
                "high": 12.0,
                "low": 10.0,
                "close": 11.5,
                "volume": 200,
                "amount": 2000.0,
            }

    fake_xtdata = types.SimpleNamespace(
        download_history_data=lambda *args, **kwargs: None,
        get_market_data_ex=lambda **kwargs: {"600519.SH": TwoRowDataFrame()},
    )
    collector = load_collector(fake_xtdata)
    monkeypatch.setattr(
        collector,
        "fetch_valid_rows",
        lambda code, mode, dates: (
            {
                "2026-07-28": {
                    "open": 10.0, "high": 11.0, "low": 9.0, "close": 10.5,
                    "volume": 100, "amount": 1000.0,
                }
            },
            {},
        ),
        raising=False,
    )
    writes = []
    monkeypatch.setattr(
        collector,
        "write_daily_rows_batch",
        lambda mode, rows, adjustment_asofs: writes.append((mode, rows)),
    )

    counts, failures = collector.download_and_save_batch(
        ["600519.SH"], "20260728", {"600519.SH": None}
    )

    assert failures == []
    assert counts == {"none": 2, "front": 2, "back": 2}
    assert all(
        {row["trade_date"] for row in rows} == {"2026-07-28", "2026-07-29"}
        for _, rows in writes
    )


def test_batch_replaces_only_qmt_invalid_row_with_akshare_row(monkeypatch):
    """Removing the merge must leave the dirty date absent instead of repaired."""
    class TwoRowDataFrame:
        def __len__(self):
            return 2

        def iterrows(self):
            yield "20260728", {
                "open": 10.0, "high": 11.0, "low": 9.0, "close": 10.5,
                "volume": 100, "amount": 1000.0,
            }
            yield "20260729", {
                "open": 20.0, "high": 21.0, "low": 19.0, "close": 20.5,
                "volume": 200, "amount": float("nan"),
            }

    fake_xtdata = types.SimpleNamespace(
        download_history_data=lambda *args, **kwargs: None,
        get_market_data_ex=lambda **kwargs: {"600519.SH": TwoRowDataFrame()},
    )
    collector = load_collector(fake_xtdata)
    monkeypatch.setattr(
        collector,
        "fetch_valid_rows",
        lambda code, mode, dates: (
            {
                "2026-07-29": {
                    "open": 30.0, "high": 31.0, "low": 29.0, "close": 30.5,
                    # AkShare volume is in shares; keep amount/price/volume
                    # economically coherent so the unit-contract guard admits it.
                    "volume": 300, "amount": 9150.0,
                }
            },
            {},
        ),
        raising=False,
    )
    writes = []
    monkeypatch.setattr(
        collector,
        "write_daily_rows_batch",
        lambda mode, rows, adjustment_asofs: writes.append((mode, rows)),
    )

    counts, failures = collector.download_and_save_batch(
        ["600519.SH"], "20260728", {"600519.SH": None}
    )

    assert failures == []
    assert counts == {"none": 2, "front": 2, "back": 2}
    for _, rows in writes:
        by_date = {row["trade_date"]: row for row in rows}
        assert by_date["2026-07-28"]["close_price"] == 10.5
        assert by_date["2026-07-29"]["close_price"] == 30.5


def test_batch_marks_stock_failed_when_akshare_cannot_fill_qmt_dirty_date(monkeypatch):
    """Removing incomplete-fallback handling must not silently report the stock healthy."""
    class TwoRowDataFrame:
        def __len__(self):
            return 2

        def iterrows(self):
            yield "20260728", {
                "open": 10.0, "high": 11.0, "low": 9.0, "close": 10.5,
                "volume": 100, "amount": 1000.0,
            }
            yield "20260729", {
                "open": 20.0, "high": 21.0, "low": 19.0, "close": 20.5,
                "volume": 200, "amount": float("nan"),
            }

    collector = load_collector(types.SimpleNamespace(
        download_history_data=lambda *args, **kwargs: None,
        get_market_data_ex=lambda **kwargs: {"600519.SH": TwoRowDataFrame()},
    ))
    monkeypatch.setattr(
        collector,
        "fetch_valid_rows",
        lambda *args: ({}, {"2026-07-29": "Sina response missing target date"}),
        raising=False,
    )
    writes = []
    monkeypatch.setattr(
        collector,
        "write_daily_rows_batch",
        lambda mode, rows, adjustment_asofs: writes.append(rows),
    )

    counts, failures = collector.download_and_save_batch(
        ["600519.SH"], "20260728", {"600519.SH": None}
    )

    assert failures == ["600519.SH"]
    assert counts == {"none": 0, "front": 0, "back": 0}
    assert writes == []


def test_batch_marks_stock_failed_when_all_rows_have_nan(monkeypatch):
    """A stock remains failed when NaN filtering leaves no usable row in a mode."""
    class NanOnlyDataFrame:
        def __len__(self):
            return 1

        def iterrows(self):
            yield "20260728", {
                "open": 10.0,
                "high": 11.0,
                "low": 9.0,
                "close": 10.5,
                "volume": 100,
                "amount": float("nan"),
            }

    fake_xtdata = types.SimpleNamespace(
        download_history_data=lambda *args, **kwargs: None,
        get_market_data_ex=lambda **kwargs: {"600519.SH": NanOnlyDataFrame()},
    )
    collector = load_collector(fake_xtdata)
    monkeypatch.setattr(
        collector,
        "fetch_valid_rows",
        lambda *args: ({}, {"2026-07-28": "test fallback unavailable"}),
        raising=False,
    )
    monkeypatch.setattr(
        collector,
        "write_daily_rows_batch",
        lambda *args, **kwargs: pytest.fail("all-invalid rows must not be written"),
    )

    counts, failures = collector.download_and_save_batch(
        ["600519.SH"], "20260728", {"600519.SH": None}
    )

    assert counts == {"none": 0, "front": 0, "back": 0}
    assert failures == ["600519.SH"]


def test_collector_fetches_three_modes_for_a_code_batch_and_isolates_missing_codes(monkeypatch):
    """A batch response must preserve per-code failure visibility instead of failing silently."""
    download_calls = []
    market_calls = []

    class OneRowDataFrame:
        def __len__(self):
            return 1

        def iterrows(self):
            yield "20250102", {
                "open": 10.0,
                "high": 11.0,
                "low": 9.0,
                "close": 10.5,
                "volume": 100,
                "amount": 1000.0,
                "preClose": 9.8,
                "suspendFlag": 0,
            }

    def get_market_data_ex(**kwargs):
        market_calls.append(kwargs)
        codes = kwargs["stock_list"]
        # One code is absent only from qfq: no partial raw/bfq projection may
        # be persisted for it, while the healthy code remains writable.
        if kwargs["dividend_type"] == "front":
            codes = [code for code in codes if code != "000002.SZ"]
        return {code: OneRowDataFrame() for code in codes}

    fake_xtdata = types.SimpleNamespace(
        download_history_data=lambda *args, **kwargs: download_calls.append((args, kwargs)),
        get_market_data_ex=get_market_data_ex,
    )
    collector = load_collector(fake_xtdata)
    writes = []
    monkeypatch.setattr(
        collector,
        "write_daily_rows_batch",
        lambda mode, rows, adjustment_asofs: writes.append((mode, rows, adjustment_asofs)),
        raising=False,
    )

    counts, failed_codes = collector.download_and_save_batch(
        ["000001.SZ", "000002.SZ"],
        "20250101",
        {
            "000001.SZ": date(2025, 1, 3),
            "000002.SZ": None,
        },
    )

    assert download_calls == [
        (("000001.SZ", "1d", "20250101", ""), {}),
        (("000002.SZ", "1d", "20250101", ""), {}),
    ]
    assert [call["dividend_type"] for call in market_calls] == ["none", "front", "back"]
    assert all(call["stock_list"] == ["000001.SZ", "000002.SZ"] for call in market_calls)
    assert counts == {"none": 1, "front": 1, "back": 1}
    assert failed_codes == ["000002.SZ"]
    assert [(mode, len(rows)) for mode, rows, _ in writes] == [
        ("none", 1), ("front", 1), ("back", 1),
    ]


def test_collector_logs_each_qmt_batch_stage_immediately(monkeypatch, capsys):
    class OneRowDataFrame:
        def __len__(self):
            return 1

        def iterrows(self):
            yield "20250102", {
                "open": 10.0, "high": 11.0, "low": 9.0, "close": 10.5,
                "volume": 100, "amount": 1000.0,
            }

    fake_xtdata = types.SimpleNamespace(
        download_history_data=lambda *args, **kwargs: None,
        download_history_data2=lambda *args, **kwargs: None,
        get_market_data_ex=lambda **kwargs: {"600519.SH": OneRowDataFrame()},
    )
    collector = load_collector(fake_xtdata)
    monkeypatch.setattr(collector, "write_daily_rows_batch", lambda *args, **kwargs: None)

    collector.download_and_save_batch(["600519.SH"], "20150101", {"600519.SH": None})

    output = capsys.readouterr().out
    assert "阶段=开始下载历史缓存" in output
    assert "阶段=历史缓存下载完成" in output
    assert "阶段=开始读取raw (none)" in output
    assert "阶段=开始读取front-adjusted (front)" in output
    assert "阶段=开始读取back-adjusted (back)" in output
    assert "阶段=back-adjusted读取完成 rows=1" in output


def test_adjustment_asof_comes_from_latest_effective_action_not_wall_clock(monkeypatch):
    collector = load_collector(types.SimpleNamespace())
    monkeypatch.setattr(
        collector,
        "execute_query",
        lambda sql, params=None: [{"adjustment_asof": date(2025, 6, 20)}],
    )

    assert collector.get_adjustment_asof("600519.SH") == date(2025, 6, 20)


def test_adjustment_asofs_are_loaded_with_one_grouped_query(monkeypatch):
    collector = load_collector(types.SimpleNamespace())
    calls = []
    monkeypatch.setattr(
        collector,
        "execute_query",
        lambda sql, params=None: calls.append((sql, params)) or [
            {"stock_code": "600519.SH", "adjustment_asof": date(2025, 6, 20)},
        ],
    )

    assert collector.get_adjustment_asofs(["600519.SH", "000001.SZ"]) == {
        "600519.SH": date(2025, 6, 20),
        "000001.SZ": None,
    }
    assert len(calls) == 1
    assert "GROUP BY stock_code" in calls[0][0]
    assert calls[0][1] == ("600519.SH", "000001.SZ")


def test_batch_missing_count_does_not_use_dataframe_truth_value(monkeypatch):
    class AmbiguousDataFrame:
        def __len__(self):
            return 1

        def __bool__(self):
            raise ValueError("ambiguous dataframe truth value")

        def iterrows(self):
            yield "20250102", {
                "open": 10.0, "high": 11.0, "low": 9.0, "close": 10.5,
                "volume": 100, "amount": 1000.0,
            }

    fake_xtdata = types.SimpleNamespace(
        download_history_data=lambda *args, **kwargs: None,
        download_history_data2=lambda *args, **kwargs: None,
        get_market_data_ex=lambda **kwargs: {"600519.SH": AmbiguousDataFrame()},
    )
    collector = load_collector(fake_xtdata)
    monkeypatch.setattr(collector, "write_daily_rows_batch", lambda *args, **kwargs: None)

    counts, failed_codes = collector.download_and_save_batch(
        ["600519.SH"], "20150101", {"600519.SH": None}
    )

    assert counts == {"none": 1, "front": 1, "back": 1}
    assert failed_codes == []


def test_executable_flow_syncs_actions_before_prices_then_runs_durable_refresh(
    monkeypatch,
    capsys,
):
    collector = load_collector(types.SimpleNamespace(connect=lambda: None))
    calls = []
    plan = types.SimpleNamespace(
        changes=[
            types.SimpleNamespace(kind="corrected"),
            types.SimpleNamespace(kind="cancelled"),
        ],
        refresh_tasks=[{}, {}],
    )
    monkeypatch.setattr(
        collector,
        "get_existing_latest_dates",
        lambda mode: {},
    )
    monkeypatch.setattr(
        collector,
        "get_code_universe",
        lambda: (["600519.SH"], {"600519.SH"}),
    )
    monkeypatch.setattr(collector, "_new_code_start", lambda code, today: collector.DATA_START)
    monkeypatch.setattr(
        collector,
        "sync_stock_actions",
        lambda code, today: calls.append(("actions", code)) or plan,
    )
    monkeypatch.setattr(
        collector,
        "get_adjustment_asof",
        lambda code: date(2026, 6, 20),
    )
    monkeypatch.setattr(
        collector,
        "get_adjustment_asofs",
        lambda codes: {code: date(2026, 6, 20) for code in codes},
    )
    monkeypatch.setattr(
        collector,
        "audit_and_repair_projection",
        lambda code, adjustment_asof: {"detected": 0, "repaired": 0, "failed": 0},
    )
    monkeypatch.setattr(
        collector,
        "download_and_save_batch",
        lambda codes, start, adjustment_asofs: calls.append(
            ("daily_batch", codes, start, adjustment_asofs)
        )
        or ({"none": 1, "front": 1, "back": 1}, []),
    )
    monkeypatch.setattr(
        collector,
        "download_and_save_mode",
        lambda code, mode, start, adjustment_asof: calls.append(
            ("refresh", code, mode, start, adjustment_asof)
        )
        or 8,
    )

    def run_tasks(callback):
        callback("600519.SH", "front", date(2015, 1, 1))
        return {
            "done": 1,
            "failed": 0,
            "retried": 1,
            "reclaimed": 1,
            "superseded": 0,
        }

    monkeypatch.setattr(collector, "run_due_refresh_tasks", run_tasks)

    assert collector.main() == 0
    assert calls == [
        ("actions", "600519.SH"),
        (
            "daily_batch",
            ["600519.SH"],
            collector.DATA_START,
            {"600519.SH": date(2026, 6, 20)},
        ),
        ("refresh", "600519.SH", "front", "20150101", date(2026, 6, 20)),
    ]
    output = capsys.readouterr().out
    assert "[权益] 新增=0 修订=1 撤回=1 刷新任务=2" in output
    assert "[刷新] 成功=1 失败=0 重试=1 回收=1 已被新任务取代=0" in output


def test_main_can_skip_equity_snapshot(monkeypatch):
    collector = load_collector(types.SimpleNamespace(connect=lambda: None))
    calls = []
    monkeypatch.setattr(collector, "get_existing_latest_dates", lambda mode: {})
    monkeypatch.setattr(
        collector, "get_code_universe", lambda: (["600519.SH"], {"600519.SH"})
    )
    monkeypatch.setattr(collector, "_new_code_start", lambda code, today: collector.DATA_START)
    monkeypatch.setattr(
        collector,
        "sync_stock_actions",
        lambda *args: pytest.fail("equity snapshot should be skipped"),
    )
    monkeypatch.setattr(
        collector,
        "get_adjustment_asofs",
        lambda codes: {code: None for code in codes},
    )
    monkeypatch.setattr(
        collector,
        "audit_and_repair_projection",
        lambda code, adjustment_asof: {"detected": 0, "repaired": 0, "failed": 0},
    )
    monkeypatch.setattr(
        collector,
        "download_and_save_batch",
        lambda codes, start, adjustment_asofs: calls.append(
            (codes, start, adjustment_asofs)
        ) or ({"none": 1, "front": 1, "back": 1}, []),
    )
    monkeypatch.setattr(
        collector,
        "run_due_refresh_tasks",
        lambda callback: {
            "done": 0, "failed": 0, "retried": 0,
            "reclaimed": 0, "superseded": 0,
        },
    )

    assert collector.main(skip_equity_snapshot=True) == 0
    assert calls == [(["600519.SH"], collector.DATA_START, {"600519.SH": None})]

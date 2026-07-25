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
        ("600519.SH", "2025-01-02", 10.0, 11.0, 9.0, 10.5, 100, 1000.0, 9.8, 0)
    ]


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


def test_adjustment_asof_comes_from_latest_effective_action_not_wall_clock(monkeypatch):
    collector = load_collector(types.SimpleNamespace())
    monkeypatch.setattr(
        collector,
        "execute_query",
        lambda sql, params=None: [{"adjustment_asof": date(2025, 6, 20)}],
    )

    assert collector.get_adjustment_asof("600519.SH") == date(2025, 6, 20)


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
        "download_and_save_all_modes",
        lambda code, start, adjustment_asof: calls.append(("daily", code, adjustment_asof))
        or {"none": 1, "front": 1, "back": 1},
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
        ("daily", "600519.SH", date(2026, 6, 20)),
        ("refresh", "600519.SH", "front", "20150101", date(2026, 6, 20)),
    ]
    output = capsys.readouterr().out
    assert "[权益] 新增=0 修订=1 撤回=1 刷新任务=2" in output
    assert "[刷新] 成功=1 失败=0 重试=1 回收=1 已被新任务取代=0" in output

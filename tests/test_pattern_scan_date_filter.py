import importlib.util
from pathlib import Path

import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize("filename", ["9-形态选股雷达.py", "10-MACD全市场扫描选股.py"])
def test_scan_loader_excludes_symbol_without_target_day(monkeypatch, filename):
    path = ROOT / "src" / "pattern_detection" / filename
    spec = importlib.util.spec_from_file_location("scanner_date_test", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    dates = pd.bdate_range(end="2026-10-20", periods=65)
    rows = []
    for code, used_dates in (("000001.SZ", dates), ("159318.SZ", dates[:-1])):
        rows.extend({
            "stock_code": code, "trade_date": day.date(),
            "open_price": 10, "high_price": 11, "low_price": 9,
            "close_price": 10, "volume": 100,
        } for day in used_dates)
    monkeypatch.setattr(module, "execute_query", lambda sql, params: rows)

    loaded = module.batch_load_recent(days_back=65, end_date="2026-10-20")

    assert set(loaded) == {"000001.SZ"}

import importlib.util
import json
from pathlib import Path

import pandas as pd
import pytest

from data_ingestion import utils
from pattern_detection import instrument_names


ROOT = Path(__file__).resolve().parents[1]


def load_scanner(filename):
    path = ROOT / "src" / "pattern_detection" / filename
    spec = importlib.util.spec_from_file_location("scanner_output_test", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_missing_etf_names_are_fetched_and_merged_into_fresh_cache(tmp_path, monkeypatch):
    cache_file = tmp_path / "instrument_name_map.json"
    cache_file.write_text(json.dumps({"mapping": {"000001.SZ": "平安银行"}}), encoding="utf-8")
    monkeypatch.setattr(utils, "_NAME_MAP_FILE", cache_file)
    monkeypatch.setattr(utils, "_NAME_MAP_CACHE", None)
    calls = []

    def fetch_etfs():
        calls.append(1)
        return {"510300.SH": "沪深300ETF"}

    monkeypatch.setattr(utils, "_fetch_etf_name_map_from_akshare", fetch_etfs)

    assert utils.get_instrument_names(["000001.SZ", "510300.SH"]) == {
        "000001.SZ": "平安银行", "510300.SH": "沪深300ETF"
    }
    assert utils.get_instrument_names(["510300.SH"]) == {"510300.SH": "沪深300ETF"}
    assert len(calls) == 1
    assert json.loads(cache_file.read_text(encoding="utf-8"))["mapping"]["510300.SH"] == "沪深300ETF"


def test_scan_names_prefer_local_database_and_fallback_for_missing(monkeypatch):
    queries = []

    def query(sql, params):
        queries.append((sql, params))
        return [{"stock_code": "510300.SH", "stock_name": "沪深300ETF泰康基金"}]

    monkeypatch.setattr(instrument_names, "execute_query", query)
    monkeypatch.setattr(instrument_names, "get_instrument_names", lambda codes: {
        "000001.SZ": "平安银行", "510300.SH": "过期名称"
    })
    names = instrument_names.get_scan_names(["000001.SZ", "510300.SH"])
    assert names == {"000001.SZ": "平安银行", "510300.SH": "沪深300ETF泰康基金"}
    assert queries[0][1] == ["000001.SZ", "510300.SH"]


def test_scan_names_fallback_when_metadata_table_unavailable(monkeypatch):
    def unavailable(sql, params):
        raise RuntimeError("table missing")

    monkeypatch.setattr(instrument_names, "execute_query", unavailable)
    monkeypatch.setattr(instrument_names, "get_instrument_names", lambda codes: {
        "510300.SH": "沪深300ETF"
    })
    assert instrument_names.get_scan_names(["510300.SH"]) == {"510300.SH": "沪深300ETF"}


@pytest.mark.parametrize("filename", ["9-形态选股雷达.py", "10-MACD全市场扫描选股.py"])
def test_fund_code_classification_includes_18_prefix(filename):
    scanner = load_scanner(filename)
    assert scanner._is_stock("000001.SZ")
    assert not scanner._is_stock("510300.SH")
    assert not scanner._is_stock("159915.SZ")
    assert not scanner._is_stock("180101.SZ")


def test_radar_prints_and_exports_stock_and_fund_sections(tmp_path, monkeypatch, capsys):
    scanner = load_scanner("9-形态选股雷达.py")
    monkeypatch.chdir(tmp_path)
    bars = pd.DataFrame(index=pd.to_datetime(["2026-10-20"]))
    monkeypatch.setattr(scanner, "batch_load_recent", lambda **kwargs: {"000001.SZ": bars, "510300.SH": bars})
    monkeypatch.setattr(scanner, "get_scan_names", lambda codes: {"000001.SZ": "平安银行", "510300.SH": "沪深300ETF"})
    monkeypatch.setattr(scanner, "scan_one", lambda df, lookback: {
        "has_divergence": True, "divergence_info": {"prev_price": 10, "recent_price": 9,
        "prev_macd": -1, "recent_macd": -0.5, "days_apart": 12},
        "bullish_patterns": [("锤子线", "CDLHAMMER", 100)], "combined": True,
        "close": 10, "change_pct": 1, "vol_ratio": 2, "macd": -0.5,
    })

    result = scanner.run_radar()
    scanner.export_candidate_pool(result)
    output = capsys.readouterr().out
    assert "股票 - 双重共振" in output
    assert "ETF/基金 - 双重共振" in output
    for label, expected in (("股票", "000001.SZ"), ("ETF基金", "510300.SH")):
        path = tmp_path / "outputs" / f"候选池_{label}_2026-10-20.csv"
        assert path.exists()
        frame = pd.read_csv(path, dtype={"代码": str})
        assert frame["代码"].tolist() == [expected]
        assert frame["名称"].iloc[0] != expected


def test_macd_prints_and_exports_stock_and_fund_sections(tmp_path, monkeypatch, capsys):
    scanner = load_scanner("10-MACD全市场扫描选股.py")
    monkeypatch.chdir(tmp_path)
    bars = pd.DataFrame(index=pd.to_datetime(["2026-10-20"]))
    monkeypatch.setattr(scanner, "batch_load_recent", lambda **kwargs: {"000001.SZ": bars, "510300.SH": bars})
    monkeypatch.setattr(scanner, "get_scan_names", lambda codes: {"000001.SZ": "平安银行", "510300.SH": "沪深300ETF"})
    monkeypatch.setattr(scanner, "step1_filter_macd_momentum_trend", lambda df: (True, {
        "close": 10, "change_pct": 1, "dif": 1, "dea": 0.5, "macd_hist": 1,
        "vol_ratio": 2, "vol_ratio_gc": 2, "gc_label": "T-0", "gc_dif": 1, "gc_dea": 0.5,
    }))

    scanner.run_macd_pool_scanner()
    output = capsys.readouterr().out
    assert "股票明细" in output
    assert "ETF/基金明细" in output
    for label, expected in (("股票", "000001.SZ"), ("ETF基金", "510300.SH")):
        path = tmp_path / "outputs" / f"MACD动能趋势股票池_{label}_2026-10-20.csv"
        assert path.exists()
        frame = pd.read_csv(path, dtype={"代码": str})
        assert frame["代码"].tolist() == [expected]
        assert frame["名称"].iloc[0] != expected

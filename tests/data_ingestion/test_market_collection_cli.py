from datetime import date
import importlib.util
from pathlib import Path

from data_ingestion.market_provider import MarketBatch


SCRIPT = Path(__file__).parents[2] / "src" / "data_ingestion" / "8-原始行情与复权数据采集.py"


def load_script():
    spec = importlib.util.spec_from_file_location("canonical_market_collector", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def rows(code="600519.SH"):
    base = {
        "stock_code": code,
        "trade_date": "2026-09-18",
        "open_price": 10.0,
        "high_price": 11.0,
        "low_price": 9.0,
        "close_price": 10.5,
        "volume": 100,
        "amount": 1000.0,
    }
    return {mode: [dict(base)] for mode in ("none", "front", "back")}


def test_script_has_no_xtquant_runtime_dependency():
    assert "xtquant" not in SCRIPT.read_text(encoding="utf-8").lower()


def test_dry_run_fetches_and_validates_without_writing(monkeypatch):
    module = load_script()
    batch = MarketBatch(
        "600519.SH", date(2026, 9, 18), date(2026, 9, 18),
        rows_by_mode=rows(), provenance={"provider": "akshare"},
    )

    class Provider:
        def fetch_batch(self, *args):
            return batch

    monkeypatch.setattr(module, "write_daily_rows", lambda *args: (_ for _ in ()).throw(
        AssertionError("dry-run must not write")
    ))

    result = module.run_collection(
        Provider(), ["600519.SH"], date(2026, 9, 18), date(2026, 9, 18),
        dry_run=True,
    )

    assert result.succeeded == 1
    assert result.failed == 0
    assert result.written_rows == 0


def test_partial_provider_response_fails_without_any_write(monkeypatch):
    module = load_script()
    batch = MarketBatch(
        "600519.SH", date(2026, 9, 18), date(2026, 9, 18),
        rows_by_mode={"none": rows()["none"]}, failures={"front": "timeout"},
    )

    class Provider:
        def fetch_batch(self, *args):
            return batch

    writes = []
    monkeypatch.setattr(module, "write_daily_rows", lambda *args: writes.append(args))

    result = module.run_collection(
        Provider(), ["600519.SH"], date(2026, 9, 18), date(2026, 9, 18),
        dry_run=False,
    )

    assert result.failed == 1
    assert writes == []


def test_main_returns_nonzero_when_any_code_fails(monkeypatch):
    module = load_script()

    class Provider:
        def __init__(self, **kwargs):
            pass

        def fetch_batch(self, stock_code, start_date, end_date):
            return MarketBatch(
                stock_code, start_date, end_date, failures={"none": "network"}
            )

    monkeypatch.setattr(module, "AKShareMarketProvider", Provider)

    assert module.main([
        "--provider", "akshare",
        "--stock-code", "600519.SH",
        "--start-date", "2026-09-18",
        "--end-date", "2026-09-18",
        "--dry-run",
    ]) == 1

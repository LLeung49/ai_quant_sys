from datetime import date
import importlib.util
from pathlib import Path
import threading

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

    monkeypatch.setattr(module, "write_projection_batch", lambda *args: (_ for _ in ()).throw(
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
    monkeypatch.setattr(module, "write_projection_batch", lambda *args: writes.append(args))

    result = module.run_collection(
        Provider(), ["600519.SH"], date(2026, 9, 18), date(2026, 9, 18),
        dry_run=False,
    )

    assert result.failed == 1
    assert writes == []


def test_complete_batch_without_target_day_is_pending_and_not_written(monkeypatch):
    module = load_script()
    batch = MarketBatch(
        "159318.SZ", date(2026, 10, 10), date(2026, 10, 20),
        rows_by_mode=rows("159318.SZ"), provenance={"provider": "akshare"},
    )

    class Provider:
        def fetch_batch(self, *args):
            return batch

    writes = []
    monkeypatch.setattr(module, "write_projection_batch", lambda *args: (writes.append(args), 0)[1])
    result = module.run_collection(
        Provider(), ["159318.SZ"], date(2026, 10, 10), date(2026, 10, 20),
        dry_run=False, workers=2,
    )
    assert result.failed == 0
    assert len(result.pending) == 1
    assert result.pending[0]["reason"] == "missing_target_date"
    assert writes == []


def test_known_suspended_code_with_empty_provider_response_is_an_accepted_noop(monkeypatch):
    module = load_script()
    batch = MarketBatch(
        "600293.SH",
        date(2026, 10, 14),
        date(2026, 10, 16),
        failures={
            mode: "primary=network; fallback=ValueError: empty_response"
            for mode in ("none", "front", "back")
        },
    )

    class Provider:
        def fetch_batch(self, *args):
            return batch

    writes = []
    monkeypatch.setattr(module, "write_projection_batch", lambda *args: writes.append(args))

    result = module.run_collection(
        Provider(),
        ["600293.SH"],
        date(2026, 10, 14),
        date(2026, 10, 16),
        dry_run=False,
        accepted_suspended_codes={"600293.SH"},
    )

    assert result.succeeded == 1
    assert result.failed == 0
    assert result.written_rows == 0
    assert writes == []


def test_known_suspended_code_still_fails_for_nonempty_provider_error():
    module = load_script()
    batch = MarketBatch(
        "600293.SH",
        date(2026, 10, 14),
        date(2026, 10, 16),
        failures={"none": "timeout"},
    )

    class Provider:
        def fetch_batch(self, *args):
            return batch

    result = module.run_collection(
        Provider(),
        ["600293.SH"],
        date(2026, 10, 14),
        date(2026, 10, 16),
        dry_run=True,
        accepted_suspended_codes={"600293.SH"},
    )

    assert result.failed == 1


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
    monkeypatch.setattr(module, "get_latest_suspended_codes", lambda stock_codes: set())

    assert module.main([
        "--provider", "akshare",
        "--stock-code", "600519.SH",
        "--start-date", "2026-09-18",
        "--end-date", "2026-09-18",
        "--dry-run",
    ]) == 1


def test_missing_only_collects_prior_day_gap_instead_of_whole_universe(monkeypatch):
    module = load_script()
    calls = []

    class Provider:
        def __init__(self, **kwargs):
            pass

    monkeypatch.setattr(module, "AKShareMarketProvider", Provider)
    monkeypatch.setattr(module, "find_missing_market_codes", lambda target: (date(2026, 10, 19), ["159318.SZ"]))
    monkeypatch.setattr(module, "get_code_universe", lambda: (_ for _ in ()).throw(AssertionError("full universe queried")))
    monkeypatch.setattr(module, "get_latest_suspended_codes", lambda codes: set())
    monkeypatch.setattr(module, "run_collection", lambda provider, codes, start, end, **kwargs: (
        calls.append(list(codes)), module.CollectionResult(1, 0, 3, ())
    )[1])

    assert module.main(["--missing-only", "--start-date", "2026-10-10", "--end-date", "2026-10-20"]) == 0
    assert calls == [["159318.SZ"]]


def test_collection_uses_a_bounded_worker_pool_for_independent_stocks():
    module = load_script()
    barrier = threading.Barrier(2)

    class Provider:
        def fetch_batch(self, stock_code, start_date, end_date):
            barrier.wait(timeout=1)
            return MarketBatch(
                stock_code,
                start_date,
                end_date,
                rows_by_mode=rows(stock_code),
                provenance={"provider": "akshare"},
            )

    result = module.run_collection(
        Provider(),
        ["000001.SZ", "600519.SH"],
        date(2026, 9, 18),
        date(2026, 9, 18),
        dry_run=True,
        workers=2,
    )

    assert result.succeeded == 2
    assert result.failed == 0


def test_parallel_collection_retries_failed_code_once_serially():
    module = load_script()
    calls = 0

    class Provider:
        def fetch_batch(self, stock_code, start_date, end_date):
            nonlocal calls
            calls += 1
            if calls == 1:
                return MarketBatch(
                    stock_code,
                    start_date,
                    end_date,
                    failures={"batch": "projection_volume_amount_mismatch"},
                )
            return MarketBatch(
                stock_code,
                start_date,
                end_date,
                rows_by_mode=rows(stock_code),
            )

    result = module.run_collection(
        Provider(),
        ["600519.SH"],
        date(2026, 9, 18),
        date(2026, 9, 18),
        dry_run=True,
        workers=2,
    )

    assert calls == 2
    assert result.succeeded == 1
    assert result.failed == 0

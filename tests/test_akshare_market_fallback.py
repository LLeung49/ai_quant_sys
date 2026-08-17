from pathlib import Path
import importlib.util
import sys

import pandas as pd


INGESTION_DIR = Path(__file__).parents[1] / "src" / "data_ingestion"
MODULE_PATH = INGESTION_DIR / "akshare_market_fallback.py"


def load_fallback_module():
    sys.path.insert(0, str(INGESTION_DIR))
    try:
        spec = importlib.util.spec_from_file_location("akshare_market_fallback", MODULE_PATH)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    finally:
        sys.path.remove(str(INGESTION_DIR))


def eastmoney_frame(rows):
    return pd.DataFrame(
        rows,
        columns=["日期", "开盘", "最高", "最低", "收盘", "成交量", "成交额"],
    )


def sina_frame(rows):
    return pd.DataFrame(
        rows,
        columns=["date", "open", "high", "low", "close", "volume", "amount"],
    )


def test_fetch_valid_rows_uses_eastmoney_qfq_and_returns_only_requested_valid_dates(
    monkeypatch,
):
    """Breaking finite-value validation must never allow a dirty fallback row to storage."""
    fallback = load_fallback_module()
    calls = []
    monkeypatch.setattr(
        fallback.ak,
        "stock_zh_a_hist",
        lambda **kwargs: calls.append(kwargs)
        or eastmoney_frame(
            [
                ("2026-08-14", 10, 11, 9, 10.5, 100, 1000),
                ("2026-08-15", float("nan"), 11, 9, 10.5, 100, 1000),
                ("2026-08-16", 30, 31, 29, 30.5, 300, 3000),
            ]
        ),
    )
    monkeypatch.setattr(fallback.ak, "stock_zh_a_daily", lambda **kwargs: sina_frame([]))

    rows, failures = fallback.fetch_valid_rows(
        "600519.SH", "front", {"2026-08-14", "2026-08-15"}
    )

    assert calls[0]["symbol"] == "600519"
    assert calls[0]["adjust"] == "qfq"
    assert rows == {
        "2026-08-14": {
            "open": 10.0,
            "high": 11.0,
            "low": 9.0,
            "close": 10.5,
            "volume": 100,
            "amount": 1000.0,
        }
    }
    assert failures == {"2026-08-15": "AkShare response missing target date"}


def test_fetch_valid_rows_falls_back_to_sina_when_eastmoney_cannot_supply_every_target(
    monkeypatch,
):
    """Dropping Sina fallback must leave an otherwise available dirty date unresolved."""
    fallback = load_fallback_module()
    monkeypatch.setattr(
        fallback.ak,
        "stock_zh_a_hist",
        lambda **kwargs: eastmoney_frame([("2026-08-14", 10, 11, 9, 10.5, 100, 1000)]),
    )
    sina_calls = []
    monkeypatch.setattr(
        fallback.ak,
        "stock_zh_a_daily",
        lambda **kwargs: sina_calls.append(kwargs)
        or sina_frame([("2026-08-15", 20, 21, 19, 20.5, 200, 2000)]),
    )

    rows, failures = fallback.fetch_valid_rows(
        "000001.SZ", "back", {"2026-08-14", "2026-08-15"}
    )

    assert sina_calls[0]["symbol"] == "sz000001"
    assert sina_calls[0]["adjust"] == "hfq"
    assert set(rows) == {"2026-08-14", "2026-08-15"}
    assert failures == {}

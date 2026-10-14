from datetime import date

import pandas as pd

from data_ingestion.akshare_market_provider import AKShareMarketProvider


def stock_frame():
    return pd.DataFrame(
        [{
            "日期": "2026-09-18",
            "开盘": 10.0,
            "最高": 11.0,
            "最低": 9.0,
            "收盘": 10.5,
            "成交量": 123,
            "成交额": 4567.0,
            "换手率": 1.25,
        }]
    )


def test_stock_fetch_returns_complete_normalized_market_batch(monkeypatch):
    calls = []

    def fetch(**kwargs):
        calls.append(kwargs)
        return stock_frame()

    provider = AKShareMarketProvider(
        stock_fetcher=fetch, etf_fetcher=lambda **kwargs: None,
        max_attempts=1,
    )

    batch = provider.fetch_batch(
        "600519.SH", date(2026, 9, 18), date(2026, 9, 18)
    )

    assert batch.is_complete
    assert batch.failures == {}
    assert set(batch.rows_by_mode) == {"none", "front", "back"}
    assert [call["adjust"] for call in calls] == ["", "qfq", "hfq"]
    assert all(call["symbol"] == "600519" for call in calls)
    assert batch.rows_by_mode["none"][0] == {
        "stock_code": "600519.SH",
        "trade_date": "2026-09-18",
        "open_price": 10.0,
        "high_price": 11.0,
        "low_price": 9.0,
        "close_price": 10.5,
        "volume": 123,
        "amount": 4567.0,
        "turnover_rate": 1.25,
        "pre_close": None,
        "suspend_flag": None,
        "data_source": "akshare",
    }
    assert batch.provenance["volume_unit"] == "lot"


def test_etf_uses_etf_interface_for_all_adjustments():
    calls = []

    def fetch(**kwargs):
        calls.append(kwargs)
        return stock_frame()

    batch = AKShareMarketProvider(
        stock_fetcher=lambda **kwargs: None,
        etf_fetcher=fetch,
        max_attempts=1,
    ).fetch_batch("510300.SH", date(2026, 9, 18), date(2026, 9, 18))

    assert batch.is_complete
    assert len(calls) == 3
    assert batch.provenance["interface"] == "fund_etf_hist_em"


def test_empty_response_is_a_visible_incomplete_batch():
    batch = AKShareMarketProvider(
        stock_fetcher=lambda **kwargs: pd.DataFrame(),
        etf_fetcher=lambda **kwargs: pd.DataFrame(),
        max_attempts=1,
    ).fetch_batch("000001.SZ", date(2026, 9, 18), date(2026, 9, 18))

    assert not batch.is_complete
    assert set(batch.failures) == {"none", "front", "back"}
    assert all("empty_response" in reason for reason in batch.failures.values())


def test_schema_drift_is_reported_and_never_manufactures_zero_rows():
    frame = stock_frame().drop(columns=["收盘"])
    batch = AKShareMarketProvider(
        stock_fetcher=lambda **kwargs: frame,
        etf_fetcher=lambda **kwargs: frame,
        max_attempts=1,
    ).fetch_batch("000001.SZ", date(2026, 9, 18), date(2026, 9, 18))

    assert not batch.is_complete
    assert batch.rows_by_mode == {}
    assert all("schema_drift" in reason for reason in batch.failures.values())


def test_zero_price_response_is_rejected_for_every_mode():
    frame = stock_frame()
    for column in ("开盘", "最高", "最低", "收盘"):
        frame[column] = 0
    batch = AKShareMarketProvider(
        stock_fetcher=lambda **kwargs: frame,
        etf_fetcher=lambda **kwargs: frame,
        max_attempts=1,
    ).fetch_batch("000001.SZ", date(2026, 9, 18), date(2026, 9, 18))

    assert not batch.is_complete
    assert batch.rows_by_mode == {}
    assert all("zero_price" in reason for reason in batch.failures.values())


def test_timeout_retries_are_bounded_and_exhaustion_is_visible():
    attempts = []

    def timeout(**kwargs):
        attempts.append(kwargs)
        raise TimeoutError("provider timed out")

    batch = AKShareMarketProvider(
        stock_fetcher=timeout,
        etf_fetcher=timeout,
        max_attempts=2,
        sleeper=lambda _: None,
        jitter=lambda: 0.0,
    ).fetch_batch("000001.SZ", date(2026, 9, 18), date(2026, 9, 18))

    assert len(attempts) == 6
    assert not batch.is_complete
    assert all("retry_exhausted" in reason for reason in batch.failures.values())


def test_partial_mode_failure_keeps_batch_incomplete():
    def fetch(**kwargs):
        if kwargs["adjust"] == "qfq":
            raise ConnectionError("temporary failure")
        return stock_frame()

    batch = AKShareMarketProvider(
        stock_fetcher=fetch,
        etf_fetcher=fetch,
        max_attempts=1,
    ).fetch_batch("000001.SZ", date(2026, 9, 18), date(2026, 9, 18))

    assert not batch.is_complete
    assert set(batch.rows_by_mode) == {"none", "back"}
    assert set(batch.failures) == {"front"}


def test_stock_primary_failure_uses_sina_fallback_and_normalizes_share_volume():
    fallback_calls = []

    def primary(**kwargs):
        raise ConnectionError("eastmoney unavailable")

    def sina(**kwargs):
        fallback_calls.append(kwargs)
        frame = stock_frame().rename(columns={
            "日期": "date", "开盘": "open", "最高": "high", "最低": "low",
            "收盘": "close", "成交量": "volume", "成交额": "amount",
        })
        frame["volume"] = 12300  # Sina stock volume is shares.
        return frame

    batch = AKShareMarketProvider(
        stock_fetcher=primary,
        etf_fetcher=primary,
        stock_fallback_fetcher=sina,
        max_attempts=1,
    ).fetch_batch("600519.SH", date(2026, 9, 18), date(2026, 9, 18))

    assert batch.is_complete
    assert [call["adjust"] for call in fallback_calls] == ["", "qfq", "hfq"]
    assert all(call["symbol"] == "sh600519" for call in fallback_calls)
    assert batch.rows_by_mode["none"][0]["volume"] == 123
    assert batch.provenance["interfaces"] == {
        "none": "stock_zh_a_daily",
        "front": "stock_zh_a_daily",
        "back": "stock_zh_a_daily",
    }

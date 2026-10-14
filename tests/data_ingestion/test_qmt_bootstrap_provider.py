from datetime import date

import pandas as pd

from data_ingestion.qmt_bootstrap_provider import QMTBootstrapProvider


def frame(include_zero=True):
    rows = []
    index = []
    if include_zero:
        rows.append({
            "open": 0, "high": 0, "low": 0, "close": 0,
            "volume": 0, "amount": 0, "preClose": 0, "suspendFlag": 1,
        })
        index.append("20260917")
    rows.append({
        "open": 10.0, "high": 11.0, "low": 9.0, "close": 10.5,
        "volume": 100, "amount": 100000.0, "preClose": 9.8,
        "suspendFlag": 0,
    })
    index.append("20260918")
    return pd.DataFrame(rows, index=index)


class Gateway:
    def __init__(self, missing_mode=None):
        self.missing_mode = missing_mode
        self.calls = []

    def get_market_data_ex(self, **kwargs):
        self.calls.append(kwargs)
        if kwargs["dividend_type"] == self.missing_mode:
            return {}
        return {code: frame() for code in kwargs["stock_list"]}

    def get_instrument_detail(self, stock_list, iscomplete=False):
        return {
            code: {"OpenDate": 20260917, "ExpireDate": 99999999}
            for code in stock_list
        }


def test_zero_fill_rows_are_recorded_as_gaps_and_never_returned_as_prices():
    gateway = Gateway()
    provider = QMTBootstrapProvider(gateway=gateway)

    batch = provider.fetch_batch(
        "000001.SZ", date(2026, 9, 17), date(2026, 9, 18)
    )

    assert batch.is_complete
    assert all(len(rows) == 1 for rows in batch.rows_by_mode.values())
    assert all(rows[0]["trade_date"] == "2026-09-18" for rows in batch.rows_by_mode.values())
    assert len(batch.gaps) == 3
    assert {gap["reason"] for gap in batch.gaps} == {"zero_price_fill"}
    assert all(call["fill_data"] is False for call in gateway.calls)


def test_provider_fetches_multiple_codes_in_three_bridge_calls():
    gateway = Gateway()
    provider = QMTBootstrapProvider(gateway=gateway)

    batches = provider.fetch_batches(
        ["000001.SZ", "600519.SH"], date(2026, 9, 17), date(2026, 9, 18)
    )

    assert set(batches) == {"000001.SZ", "600519.SH"}
    assert len(gateway.calls) == 3
    assert all(call["stock_list"] == ["000001.SZ", "600519.SH"] for call in gateway.calls)


def test_missing_projection_keeps_batch_incomplete():
    batch = QMTBootstrapProvider(gateway=Gateway(missing_mode="front")).fetch_batch(
        "000001.SZ", date(2026, 9, 17), date(2026, 9, 18)
    )

    assert not batch.is_complete
    assert "front" in batch.failures
    assert set(batch.rows_by_mode) == {"none", "back"}


def test_old_listing_with_only_recent_cache_is_rejected_as_incomplete():
    gateway = Gateway()
    gateway.get_instrument_detail = lambda stock_list, iscomplete=False: {
        stock_list[0]: {"OpenDate": 19910403, "ExpireDate": 99999999}
    }

    batch = QMTBootstrapProvider(gateway=gateway).fetch_batch(
        "000001.SZ", date(2015, 1, 1), date(2026, 9, 18)
    )

    assert not batch.is_complete
    assert "coverage" in batch.failures
    assert "expected_start=2015-01-01" in batch.failures["coverage"]


def test_volume_normalization_indexes_each_projection_once():
    class CountingList(list):
        def __init__(self, values):
            super().__init__(values)
            self.iterations = 0

        def __iter__(self):
            self.iterations += 1
            return super().__iter__()

    rows = {
        mode: CountingList([
            {
                "trade_date": f"2026-01-{day:02d}",
                "volume": 100,
                "amount": 100000.0,
                "close_price": 10.0,
            }
            for day in range(1, 29)
        ])
        for mode in ("none", "front", "back")
    }

    QMTBootstrapProvider._normalize_batch_volumes(rows)

    assert all(projection.iterations <= 2 for projection in rows.values())

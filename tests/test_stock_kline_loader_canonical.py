from __future__ import annotations

import pytest

from morning_conference.sector_rotation import stock_kline_loader


def test_load_stock_kline_reads_canonical_qfq(monkeypatch) -> None:
    captured = {}

    def fake_query(sql, params):
        captured["sql"] = sql
        captured["params"] = params
        return []

    monkeypatch.setattr(stock_kline_loader, "execute_query", fake_query)
    frame = stock_kline_loader.load_stock_kline(
        "600519.SH", start_date="2026-01-01", end_date="2026-02-01"
    )

    assert frame.empty
    assert "FROM trade_stock_daily_qfq" in captured["sql"]
    assert "FROM trade_stock_daily " not in captured["sql"]
    assert captured["params"] == ["600519.SH", "2026-01-01", "2026-02-01"]


def test_retired_kline_writer_cannot_run() -> None:
    with pytest.raises(RuntimeError, match="已废弃"):
        stock_kline_loader.sync_all_kline()


def test_stock_kline_loader_has_no_qmt_runtime_import() -> None:
    source = stock_kline_loader.Path(stock_kline_loader.__file__).read_text(encoding="utf-8")
    assert "from xtquant" not in source
    assert "import xtquant" not in source

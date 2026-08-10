from __future__ import annotations

import importlib.util
import sys
from datetime import date
from pathlib import Path

from morning_conference.sector_rotation import sector_index_builder as builder


def load_init_module():
    path = Path(__file__).parents[1] / "src" / "morning_conference" / "sector_rotation" / "1-run_init.py"
    spec = importlib.util.spec_from_file_location("sector_rotation_init", path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


def test_rebuild_all_sectors_limits_full_rebuild_to_start_date(monkeypatch):
    all_dates = [date(2025, 12, 31), date(2026, 1, 2), date(2026, 1, 5)]
    monkeypatch.setattr(builder, "get_all_trade_dates", lambda: all_dates)
    monkeypatch.setattr(builder, "list_sectors_from_db", lambda level: ["sector-a"])
    calls = []
    monkeypatch.setattr(builder, "rebuild_one_sector", lambda *args: calls.append(args) or 3)

    assert builder.rebuild_all_sectors(full=True, start_date="20260102") == 3
    assert calls[0][2] == [date(2026, 1, 2), date(2026, 1, 5)]
    assert calls[0][3] == all_dates


def test_rebuild_all_sectors_returns_zero_when_start_date_has_no_trade_dates(monkeypatch):
    monkeypatch.setattr(builder, "get_all_trade_dates", lambda: [date(2026, 1, 2)])

    assert builder.rebuild_all_sectors(full=True, start_date="20270101") == 0


def test_rebuild_all_sectors_uses_all_dates_without_start_date(monkeypatch):
    all_dates = [date(2026, 1, 2), date(2026, 1, 5)]
    monkeypatch.setattr(builder, "get_all_trade_dates", lambda: all_dates)
    monkeypatch.setattr(builder, "list_sectors_from_db", lambda level: ["sector-a"])
    calls = []
    monkeypatch.setattr(builder, "rebuild_one_sector", lambda *args: calls.append(args) or 0)

    builder.rebuild_all_sectors(full=True)

    assert calls[0][2] == all_dates


def test_init_forwards_start_to_index_rebuild_when_kline_is_skipped(monkeypatch):
    init = load_init_module()
    monkeypatch.setattr(
        sys,
        "argv",
        ["1-run_init.py", "--start", "20260101", "--skip-schema", "--skip-meta", "--skip-kline"],
    )
    received = []
    monkeypatch.setattr(init, "rebuild_all_sectors", lambda **kwargs: received.append(kwargs))

    init.main()

    assert received == [{"level": 2, "full": True, "start_date": "20260101"}]

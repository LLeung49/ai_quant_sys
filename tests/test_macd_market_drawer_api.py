from datetime import date
from decimal import Decimal

from fastapi.testclient import TestClient


def test_etf_kline_returns_bounded_historical_bars(monkeypatch):
    from morning_conference.sector_rotation2.api.app import create_app
    from morning_conference.sector_rotation2.api.repository import SectorRotationRepository

    calls = []

    def load(self, code, end_date):
        calls.append((code, end_date))
        return [{"trade_date": date(2026, 8, 13), "open": Decimal("4"),
                 "high": Decimal("4.2"), "low": Decimal("3.9"),
                 "close": Decimal("4.1"), "volume": 1000, "amount": Decimal("4100")}]

    monkeypatch.setattr(SectorRotationRepository, "load_etf_kline", load, raising=False)
    response = TestClient(create_app()).get("/api/v1/sector-rotation/etf-kline", params={
        "stock_code": "510300.SH", "end_date": "2026-08-13",
    })
    assert response.status_code == 200
    assert calls == [("510300.SH", "2026-08-13")]
    assert response.json()["bars"][0]["close"] == 4.1
    assert response.json()["meta"]["source"] == "trade_stock_daily_qfq"


def test_etf_kline_rejects_non_etf_code(monkeypatch):
    from morning_conference.sector_rotation2.api.app import create_app
    from morning_conference.sector_rotation2.api.repository import SectorRotationRepository

    monkeypatch.setattr(SectorRotationRepository, "load_etf_kline", lambda *_: 1 / 0, raising=False)
    response = TestClient(create_app()).get("/api/v1/sector-rotation/etf-kline", params={
        "stock_code": "600519.SH", "end_date": "2026-08-13",
    })
    assert response.status_code == 422


def test_etf_kline_repository_uses_code_cutoff_and_limit(monkeypatch):
    from morning_conference.sector_rotation2.api import repository

    observed = []
    monkeypatch.setattr(repository, "execute_query", lambda sql, params: observed.append((sql, params)) or [])
    assert repository.SectorRotationRepository().load_etf_kline("510300.SH", "2026-08-13") == []
    sql, params = observed[0]
    assert "trade_stock_daily_qfq" in sql
    assert "stock_code = %s AND trade_date <= %s" in sql
    assert "LIMIT %s" in sql
    assert params == ("510300.SH", "2026-08-13", repository.KLINE_BAR_LIMIT)

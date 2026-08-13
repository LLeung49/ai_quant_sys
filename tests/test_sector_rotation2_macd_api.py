from fastapi.testclient import TestClient
from morning_conference.sector_rotation2.api.macd_router import macd_router
from fastapi import FastAPI
import morning_conference.sector_rotation2.api.macd_router as module

app=FastAPI(); app.include_router(macd_router)

def test_invalid_date():
    response=TestClient(app).get('/api/v1/sector-rotation/macd-pool', params={'as_of_date':'bad'})
    assert response.status_code == 422

def test_not_found(monkeypatch):
    monkeypatch.setattr(module, 'load_macd_pool', lambda *args: [])
    response=TestClient(app).get('/api/v1/sector-rotation/macd-pool', params={'as_of_date':'2026-08-12'})
    assert response.status_code == 404

def test_grouped_success(monkeypatch):
    monkeypatch.setattr(module, 'load_macd_pool', lambda *args: [{'entity_type':'etf','stock_code':'510300.SH'}])
    response=TestClient(app).get('/api/v1/sector-rotation/macd-pool', params={'as_of_date':'2026-08-12'})
    assert response.status_code == 200
    assert response.json()['groups']['etf'][0]['stock_code'] == '510300.SH'

def test_trajectory_reads_full_daily_metrics(monkeypatch):
    calls = []
    def query(sql, params):
        calls.append(sql)
        if "DISTINCT" in sql:
            return [{"as_of_date": "2026-08-11"}, {"as_of_date": "2026-08-10"}]
        return [{"as_of_date": "2026-08-10", "entity_type": "etf", "stock_code": "510300.SH", "stock_name": "沪深300ETF", "kama_efficiency": 0.61, "adx_14": 28.2}]
    monkeypatch.setattr(module, "execute_query", query)
    response = TestClient(app).get('/api/v1/sector-rotation/macd-pool-trajectory', params={'as_of_date':'2026-08-11', 'entity_type':'etf', 'stock_code':'510300.SH'})
    assert response.status_code == 200
    assert "sector_rotation_macd_entity_daily" in calls[0]
    assert response.json()["trajectory"]["points"][0]["er"] == 0.61

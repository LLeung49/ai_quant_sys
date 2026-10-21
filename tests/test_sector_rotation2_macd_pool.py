import numpy as np
import pandas as pd
import pytest
from morning_conference.sector_rotation2.macd_pool import evaluate_macd_entity, is_excluded_bond_etf, step1_filter_macd_momentum_trend, step2_filter_trap_avoidance

def _frame(values, volumes=None):
    n=len(values); return pd.DataFrame({'close':values,'volume':volumes or [100]*n})

def test_step1_rejects_short_series():
    ok, details=step1_filter_macd_momentum_trend(_frame(np.arange(20)+1))
    assert not ok and details == {}

def test_step2_returns_null_warmup_fields():
    result=step2_filter_trap_avoidance(_frame([1,2,3]))
    assert result['above_ma60'] is None

def test_step2_uses_zero_efficiency_for_flat_prices():
    result = step2_filter_trap_avoidance(_frame([10.0] * 30))
    assert result["kama_efficiency"] == 0.0
    assert result["hurst_60"] is None

def test_bond_etf_filter_uses_code_and_name_rules():
    assert is_excluded_bond_etf("511010.SH")
    assert is_excluded_bond_etf("159999.SZ", "国债ETF")
    assert not is_excluded_bond_etf("159999.SZ", "科技ETF")

def test_step1_accepts_recent_cross_with_volume():
    values=np.concatenate([np.linspace(10,8,50), np.linspace(8,14,15)])
    volumes=[100]*64+[200]
    ok, details=step1_filter_macd_momentum_trend(_frame(values, volumes), gc_lookback=10, vol_ratio_threshold=1.2, require_zero_above=False)
    assert isinstance(ok,bool)

def test_daily_pool_excludes_stocks(monkeypatch):
    import morning_conference.sector_rotation2.macd_pool as module
    monkeypatch.setattr(module, "run_macd_daily_metrics", lambda *args, **kwargs: pd.DataFrame([
        {"entity_type":"etf", "stock_code":"E", "is_triggered":1},
        {"entity_type":"sector_l1", "stock_code":"1", "is_triggered":1},
        {"entity_type":"sector_l2", "stock_code":"2", "is_triggered":1},
    ]))
    result = module.run_macd_daily_pool("2026-08-12")
    assert set(result["entity_type"]) == {"etf", "sector_l1", "sector_l2"}

def test_daily_entity_metrics_are_retained_when_not_triggered():
    frame = _frame(np.linspace(10, 11, 70))
    frame["trade_date"] = pd.date_range("2026-06-01", periods=70)
    result = evaluate_macd_entity(frame, entity_type="etf", volume_threshold=9.9)
    assert result["entity_type"] == "etf"
    assert result["is_triggered"] == 0
    assert result["kama_efficiency"] is not None

def test_daily_job_rejects_non_trading_date(monkeypatch):
    import morning_conference.sector_rotation2.run_macd_daily as module
    monkeypatch.setattr(module, "execute_query", lambda *args, **kwargs: [])
    with pytest.raises(ValueError, match="not a trading date"):
        module.ensure_trade_date("2026-08-08")

def test_sync_etf_status_names_skips_unresolved_codes(monkeypatch):
    import morning_conference.sector_rotation2.macd_pool_store as module
    monkeypatch.setattr(module, 'execute_query', lambda *_args: [])
    monkeypatch.setattr("data_ingestion.utils.get_instrument_names", lambda codes: {"510300.SH": "沪深300ETF", "159011.SZ": "159011.SZ"})
    captured = {}
    class Cursor:
        rowcount = 1
        def executemany(self, sql, rows): captured["rows"] = rows
        def close(self): pass
    class Connection:
        def cursor(self): return Cursor()
        def commit(self): pass
        def rollback(self): pass
        def close(self): pass
    monkeypatch.setattr(module, "get_connection", lambda: Connection())
    assert module.sync_etf_status_names(["510300.SH", "159011.SZ"]) == 1
    assert captured["rows"] == [("510300.SH", "沪深300ETF")]


def test_sync_etf_status_names_uses_existing_database_names(monkeypatch):
    import morning_conference.sector_rotation2.macd_pool_store as module
    monkeypatch.setattr(module, 'execute_query', lambda *_args: [{'stock_code': '510300.SH'}])
    monkeypatch.setattr('data_ingestion.utils.get_instrument_names', lambda *_args: pytest.fail('network called'))
    assert module.sync_etf_status_names(['510300.SH']) == 0


def test_replace_macd_daily_rejects_zero_before_database_write(monkeypatch):
    import morning_conference.sector_rotation2.macd_pool_store as module
    monkeypatch.setattr(module, 'get_connection', lambda: pytest.fail('database touched'))
    frame = pd.DataFrame([{'close': 0, 'is_triggered': 1}])
    with pytest.raises(ValueError, match='Invalid MACD close'):
        module.replace_macd_daily(frame, '2026-09-18', 2, 'v1', 'run')


def test_replace_macd_daily_rolls_back_both_tables_on_failure(monkeypatch):
    import morning_conference.sector_rotation2.macd_pool_store as module
    events = []

    class Cursor:
        def execute(self, sql, params): events.append(('execute', sql))
        def executemany(self, sql, rows):
            events.append(('executemany', sql))
            if 'sector_rotation_macd_pool' in sql:
                raise RuntimeError('pool insert failed')
        def close(self): events.append(('cursor_close',))

    class Connection:
        def cursor(self): return Cursor()
        def commit(self): events.append(('commit',))
        def rollback(self): events.append(('rollback',))
        def close(self): events.append(('connection_close',))

    monkeypatch.setattr(module, 'get_connection', lambda: Connection())
    frame = pd.DataFrame([{'close': 10, 'is_triggered': 1, 'entity_type': 'etf', 'stock_code': '510300.SH'}])
    with pytest.raises(RuntimeError, match='pool insert failed'):
        module.replace_macd_daily(frame, '2026-09-18', 2, 'v1', 'run')
    assert ('rollback',) in events
    assert ('commit',) not in events
    assert sum(event[0] == 'execute' for event in events) == 2


def test_daily_metrics_exclude_nonpositive_sector_index(monkeypatch):
    import morning_conference.sector_rotation2.macd_pool as module
    def query(sql, _params):
        if 'trade_stock_daily_qfq' in sql:
            return []
        return [
            {'sector_name': 'bad', 'trade_date': '2026-09-17', 'close': -1, 'volume': 100},
            {'sector_name': 'bad', 'trade_date': '2026-09-18', 'close': -2, 'volume': 100},
        ]
    monkeypatch.setattr('data_ingestion.db_config.execute_query', query)
    assert module.run_macd_daily_metrics('2026-09-18').empty

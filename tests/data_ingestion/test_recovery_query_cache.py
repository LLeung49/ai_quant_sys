from datetime import date

from data_ingestion.financial_recovery import rebuild_repair_history as rebuild


def test_cache_reuses_source_rows_but_filters_report_dates(monkeypatch):
    calls = []
    def query(sql, params):
        calls.append(params)
        return [
            {"stock_code": "000001.SZ", "report_date": date(2025, 12, 31)},
            {"stock_code": "000001.SZ", "report_date": date(2024, 12, 31)},
        ]
    cache = rebuild.RecoveryQueryCache(query, date(2026, 9, 17))
    sql = "SELECT * FROM trade_stock_financial_raw_pit WHERE report_date<=%s AND stock_code IN (%s)"
    early = cache(sql, (date(2025, 1, 1), "000001.SZ"))
    later = cache(sql, (date(2026, 1, 1), "000001.SZ"))
    assert len(early) == 1
    assert len(later) == 2
    assert len(calls) == 1
    assert calls[0][0] == date(2026, 9, 17)

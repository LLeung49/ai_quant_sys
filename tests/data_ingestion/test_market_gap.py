from datetime import date
import json

from data_ingestion import market_gap


def test_missing_codes_compare_prior_session_with_all_three_projections(monkeypatch):
    def query(sql, params):
        if "AS prior_date" in sql:
            return [{"prior_date": date(2026, 10, 19)}]
        if "UNION" in sql:
            assert params[0] == "2026-08-21"
            assert params[1:] == ("2026-10-20", "2026-10-20", "2026-10-20")
            return [{"stock_code": "159318.SZ"}, {"stock_code": "510300.SH"}]
        if "suspend_flag=1" in sql:
            return []
        if "trade_stock_daily_bfq" in sql:
            return [{"stock_code": "510300.SH"}]
        return [{"stock_code": "159318.SZ"}, {"stock_code": "510300.SH"}]

    monkeypatch.setattr(market_gap, "execute_query", query)
    prior, codes = market_gap.find_missing_market_codes(date(2026, 10, 20))
    assert prior == date(2026, 10, 19)
    assert codes == ["159318.SZ"]


def test_stale_active_code_is_retryable_but_last_suspended_code_is_not(monkeypatch):
    def query(sql, params):
        if "AS prior_date" in sql:
            return [{"prior_date": date(2026, 10, 19)}]
        if "UNION" in sql:
            return [{"stock_code": "159291.SZ"}, {"stock_code": "000016.SZ"}]
        if "suspend_flag=1" in sql:
            return [{"stock_code": "000016.SZ"}]
        return []

    monkeypatch.setattr(market_gap, "execute_query", query)
    prior, codes = market_gap.find_missing_market_codes(date(2026, 10, 20))
    assert prior == date(2026, 10, 19)
    assert codes == ["159291.SZ"]


def test_gap_report_records_missing_codes_and_clears_after_recovery(tmp_path):
    target = date(2026, 10, 20)
    path = market_gap.write_gap_report(target, date(2026, 10, 19), ["159318.SZ"], tmp_path)
    assert json.loads(path.read_text(encoding="utf-8"))["missing_codes"] == ["159318.SZ"]
    market_gap.write_gap_report(target, date(2026, 10, 19), [], tmp_path)
    report = json.loads(path.read_text(encoding="utf-8"))
    assert report["status"] == "complete"
    assert report["missing_codes"] == []
    assert report["observed_missing_codes"] == ["159318.SZ"]
    assert report["recovered_codes"] == ["159318.SZ"]

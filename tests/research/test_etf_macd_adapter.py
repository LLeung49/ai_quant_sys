from datetime import date

from morning_conference.sector_rotation2.research.etf_core.macd_adapter import load_etf_macd_evidence


def test_adapter_reads_existing_entity_daily_metrics_without_recalculation() -> None:
    captured = {}
    def query(sql, params):
        captured.update(sql=sql, params=params)
        return [{"gc_offset": 2, "adx": 30}]
    assert load_etf_macd_evidence("512480.SH", date(2026, 8, 17), query) == {"gc_offset": 2, "adx": 30}
    assert "sector_rotation_macd_entity_daily" in captured["sql"]

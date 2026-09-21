from pathlib import Path


ROOT = Path(__file__).parents[1]
QMT_CONSUMERS = [
    ROOT / "src/data_ingestion_qmt/4-新闻事件采集.py",
    ROOT / "src/data_ingestion_qmt/5-研报数据采集.py",
    ROOT / "src/morning_conference_qmt/sector_rotation2/macd_pool.py",
    ROOT / "src/morning_conference_qmt/sector_rotation2/run_macd_daily.py",
    ROOT / "src/morning_conference_qmt/sector_rotation2/research/etf_core/return_data.py",
    ROOT / "src/morning_conference_qmt/sector_rotation2/research/financial/service.py",
]


def test_qmt_business_consumers_read_qfq_not_legacy_daily():
    for path in QMT_CONSUMERS:
        source = path.read_text(encoding="utf-8")
        assert "trade_stock_daily_qfq" in source, path
        assert "FROM trade_stock_daily " not in source, path
        assert "FROM trade_stock_daily\n" not in source, path
        assert "FROM trade_stock_daily AS" not in source, path

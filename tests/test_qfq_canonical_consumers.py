from pathlib import Path


ROOT = Path(__file__).parents[1]
BUSINESS_READER_PATHS = [
    ROOT / "src/pattern_detection/data_loader.py",
    ROOT / "src/pattern_detection/9-形态选股雷达.py",
    ROOT / "src/pattern_detection/10-MACD全市场扫描选股.py",
    ROOT / "src/data_ingestion/4-新闻事件采集.py",
    ROOT / "src/data_ingestion/5-研报数据采集.py",
    ROOT / "src/morning_conference/sector_rotation2/macd_pool.py",
    ROOT / "src/morning_conference/sector_rotation2/run_macd_daily.py",
    ROOT / "src/morning_conference/sector_rotation2/research/etf_core/return_data.py",
    ROOT / "src/morning_conference/sector_rotation2/research/financial/service.py",
]
ASSET_MARKET_DATA = ROOT / "src/asset_allocation/etf_adaptive/market_data.py"
QMT_OLD_WRITER = ROOT / "src/data_ingestion_qmt/1-行情数据采集_qmt_bridge.py"
RUN_GUIDE = ROOT / "docs/run_daily_once_qmt.txt"
LEGACY_WRITER_PATHS = [
    ROOT / "src/data_ingestion/1-行情数据采集.py",
    ROOT / "src/data_ingestion/9-前复权对账与定向重刷.py",
    ROOT / "src/morning_conference/sector_rotation/stock_kline_loader.py",
]
VOLUME_REPAIR_PATHS = [
    ROOT / "src/data_ingestion/repair_market_volume_units.py",
    ROOT / "src/data_ingestion_qmt/repair_market_volume_units.py",
]


def test_business_readers_use_qfq_not_legacy_daily():
    for path in BUSINESS_READER_PATHS:
        source = path.read_text(encoding="utf-8")
        assert "trade_stock_daily_qfq" in source, path
        assert "FROM trade_stock_daily " not in source, path
        assert "FROM trade_stock_daily\n" not in source, path
        assert "FROM trade_stock_daily AS" not in source, path


def test_asset_allocation_keeps_raw_and_qfq_contracts():
    source = ASSET_MARKET_DATA.read_text(encoding="utf-8")
    assert "FROM trade_stock_daily_raw" in source
    assert "FROM trade_stock_daily_qfq" in source


def test_executable_legacy_writers_fail_before_old_table_write():
    for path in LEGACY_WRITER_PATHS:
        source = path.read_text(encoding="utf-8")
        assert "已废弃" in source, path
        assert "trade_stock_daily_qfq" in source, path


def test_volume_repair_targets_raw_qfq_bfq_not_legacy_daily():
    for path in VOLUME_REPAIR_PATHS:
        source = path.read_text(encoding="utf-8")
        assert '"trade_stock_daily",' not in source, path
        assert "FROM trade_stock_daily AS" not in source, path
        assert '"trade_stock_daily_qfq",' in source, path


def test_qfq_preflight_has_no_qmt_old_writer_or_guide_reference():
    assert not QMT_OLD_WRITER.exists()
    assert "1-行情数据采集_qmt_bridge.py" not in RUN_GUIDE.read_text(encoding="utf-8")

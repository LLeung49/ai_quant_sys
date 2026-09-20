from pathlib import Path


ROOT = Path(__file__).parents[1]
KLINE = ROOT / "src/morning_conference/sector_rotation/stock_kline_loader_qmt_bridge.py"
INDUSTRY = ROOT / "src/morning_conference/sector_rotation/industry_meta_qmt_bridge.py"


def test_morning_copies_exist_without_direct_xtquant_imports():
    for path in (KLINE, INDUSTRY):
        assert path.exists()
        assert "from xtquant import xtdata" not in path.read_text(encoding="utf-8")
        assert "QMTDataGateway" in path.read_text(encoding="utf-8")

from pathlib import Path


ROOT = Path(__file__).parents[1]
INDUSTRY = ROOT / "src/morning_conference_qmt/sector_rotation/industry_meta_qmt_bridge.py"


def test_qmt_sector_rotation_keeps_industry_bridge_and_retires_kline_loader():
    assert INDUSTRY.exists()
    source = INDUSTRY.read_text(encoding="utf-8")
    assert "from xtquant import xtdata" not in source
    assert "QMTDataGateway" in source
    assert not (
        ROOT / "src/morning_conference_qmt/sector_rotation/stock_kline_loader_qmt_bridge.py"
    ).exists()

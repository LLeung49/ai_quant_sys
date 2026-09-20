import importlib.util
from pathlib import Path


MODULE_PATH = next(
    Path("src/morning_conference_qmt/sector_rotation").glob("industry_meta_qmt_bridge.py")
)


def _load_module():
    spec = importlib.util.spec_from_file_location("industry_meta_qmt_bridge_test", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_qmt_industry_sync_uses_akshare_catalog_and_qmt_memberships():
    module = _load_module()

    class Gateway:
        def connect(self):
            return None

        def get_industry(self, name):
            return {
                "SW1食品饮料": ["600519.SH", "000568.SZ"],
                "SW2白酒": ["600519.SH"],
            }[name]

        def get_instrument_detail(self, code):
            return {"InstrumentName": {"600519.SH": "贵州茅台", "000568.SZ": "泸州老窖"}[code]}

    module.set_gateway_for_test(Gateway())

    result = module.fetch_sw_classification_from_qmt(
        catalog_loader=lambda: (["SW1食品饮料"], ["SW2白酒"])
    )

    assert result == {
        "600519.SH": {"sector_1": "食品饮料", "sector_2": "白酒", "stock_name": "贵州茅台"},
        "000568.SZ": {"sector_1": "食品饮料", "stock_name": "泸州老窖"},
    }

from pathlib import Path
from datetime import date

from morning_conference.sector_rotation2.research.etf_core.providers_qmt_bridge import (
    QMTBridgeETFProvider,
)


PATH = Path(__file__).parents[2] / "src/morning_conference/sector_rotation2/research/etf_core/providers_qmt_bridge.py"


def test_etf_provider_copy_exists_without_direct_xtquant_import():
    assert PATH.exists()
    source = PATH.read_text(encoding="utf-8")
    assert "from xtquant import xtdata" not in source
    assert "QMTDataGateway" in source


def test_etf_bridge_rejects_code_only_components():
    class Client:
        def download_etf_info(self):
            return None

        def get_etf_info(self):
            return {"510300.SH": {
                "source_as_of_date": "2026-08-18",
                "weight_unit": "percent",
                "source_reference": "fixture",
                "成份股信息": [{"成份股代码": "600519.SH"}],
            }}

    result = QMTBridgeETFProvider(client=Client()).load(date(2026, 8, 18))
    assert result.quality_issue.code == "missing_constituent_weight"

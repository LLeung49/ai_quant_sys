from __future__ import annotations

import pandas as pd
import pytest

from morning_conference.sector_rotation import industry_meta


class FakeAKShare:
    def sw_index_second_info(self) -> pd.DataFrame:
        return pd.DataFrame([
            {"行业代码": "801016.SI", "行业名称": "种植业", "上级行业": "农林牧渔"},
            {"行业代码": "801783.SI", "行业名称": "医疗服务", "上级行业": "医药生物"},
        ])

    def index_component_sw(self, symbol: str) -> pd.DataFrame:
        rows = {
            "801016": [
                {"证券代码": "000998", "证券名称": "隆平高科"},
                {"证券代码": "600598", "证券名称": "北大荒"},
            ],
            "801783": [
                {"证券代码": "300015", "证券名称": "爱尔眼科"},
                {"证券代码": "830946", "证券名称": "森萱医药"},
            ],
        }
        return pd.DataFrame(rows[symbol])


def test_fetch_sw_classification_uses_akshare_membership() -> None:
    result = industry_meta.fetch_sw_classification_from_akshare(FakeAKShare())

    assert result == {
        "000998.SZ": {"stock_name": "隆平高科", "sector_1": "农林牧渔", "sector_2": "种植业"},
        "600598.SH": {"stock_name": "北大荒", "sector_1": "农林牧渔", "sector_2": "种植业"},
        "300015.SZ": {"stock_name": "爱尔眼科", "sector_1": "医药生物", "sector_2": "医疗服务"},
        "830946.BJ": {"stock_name": "森萱医药", "sector_1": "医药生物", "sector_2": "医疗服务"},
    }


def test_fetch_sw_classification_rejects_malformed_catalog() -> None:
    class BadAKShare(FakeAKShare):
        def sw_index_second_info(self) -> pd.DataFrame:
            return pd.DataFrame([{"行业代码": "801016.SI", "行业名称": "种植业"}])

    with pytest.raises(ValueError, match="上级行业"):
        industry_meta.fetch_sw_classification_from_akshare(BadAKShare())


def test_runtime_industry_source_has_no_xtquant_import() -> None:
    source = industry_meta.Path(industry_meta.__file__).read_text(encoding="utf-8")
    assert "from xtquant" not in source
    assert "import xtquant" not in source

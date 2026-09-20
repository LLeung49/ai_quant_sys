import pandas as pd

from data_ingestion.qmt_data_gateway import QMTBridgeError
from data_ingestion.qmt_gateway_probe import GatewayProbe, ProbeConfig, summarize


class _Gateway:
    def get_sector_list(self):
        return ["沪深A股"]

    def get_stock_list_in_sector(self, sector):
        return ["600519.SH"]

    def get_instrument_detail(self, stock):
        return {"OpenDate": "20010827"}

    def get_market_data_ex(self, *args, **kwargs):
        return {"600519.SH": pd.DataFrame({"close": [1.0]}, index=["20250102"])}

    def get_divid_factors(self, *args):
        return pd.DataFrame({"factor": [1.0]}, index=["20250102"])

    def get_financial_data(self, *args, **kwargs):
        return {"600519.SH": {"Balance": pd.DataFrame({"asset": [1.0]})}}

    def get_etf_info(self):
        return {"510300.SH": {"components": []}}


def test_probe_reports_shapes_and_keeps_read_only_default():
    probe = GatewayProbe(_Gateway(), ProbeConfig(stock="600519.SH", sector="沪深A股"))

    results = probe.run()

    assert {item["name"] for item in results} >= {"sector_list", "market_none", "etf_info"}
    assert all(item["status"] == "ok" for item in results)
    assert all("download" not in item["name"] for item in results)
    market = next(item for item in results if item["name"] == "market_none")
    assert market["result"]["kind"] == "mapping"
    assert market["result"]["sample"]["600519.SH"]["kind"] == "dataframe"


def test_probe_keeps_going_after_gateway_error():
    class _BrokenGateway(_Gateway):
        def get_sector_list(self):
            raise QMTBridgeError("QMT unavailable")

    results = GatewayProbe(_BrokenGateway(), ProbeConfig()).run()

    sector = next(item for item in results if item["name"] == "sector_list")
    assert sector == {"name": "sector_list", "status": "error", "error": "QMT unavailable"}


def test_summarize_dataframe_exposes_columns_and_sample_rows():
    result = summarize(pd.DataFrame({"close": [1.2]}, index=["20250102"]))

    assert result["kind"] == "dataframe"
    assert result["rows"] == 1
    assert result["columns"] == ["close"]


def test_probe_can_run_one_named_api_only():
    results = GatewayProbe(_Gateway(), ProbeConfig()).run(only={"market_front"})

    assert [result["name"] for result in results] == ["market_front"]

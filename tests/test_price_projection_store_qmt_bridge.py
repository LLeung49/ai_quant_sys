import importlib.util
from pathlib import Path


PATH = Path(__file__).parents[1] / "src/data_ingestion_qmt/8-原始行情与复权数据采集_qmt_bridge.py"


def test_projection_copy_is_separate_and_preserves_public_functions():
    assert PATH.exists()
    source = PATH.read_text(encoding="utf-8")
    assert "from xtquant import xtdata" not in source
    spec = importlib.util.spec_from_file_location("projection_bridge", PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assert callable(module.download_and_save_all_modes)


def test_projection_rows_use_qmt_turnover_rate_in_legacy_percent_units():
    import pandas as pd

    spec = importlib.util.spec_from_file_location("projection_bridge", PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    dataframe = pd.DataFrame(
        [{"open": 1, "high": 2, "low": 1, "close": 2, "volume": 3, "amount": 600}],
        index=["20250102"],
    )

    rows, _ = module._split_qmt_rows("600519.SH", dataframe, "front")
    module._apply_turnover_rates(
        rows,
        {"600519.SH": {"20250102": 0.001100888133141958}},
    )

    assert rows[0]["turnover_rate"] == 0.1101


def test_projection_rows_keep_turnover_null_when_qmt_does_not_return_a_date():
    import pandas as pd

    spec = importlib.util.spec_from_file_location("projection_bridge", PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    dataframe = pd.DataFrame(
        [{"open": 1, "high": 2, "low": 1, "close": 2, "volume": 3, "amount": 600}],
        index=["20250102"],
    )

    rows, _ = module._split_qmt_rows("600519.SH", dataframe, "front")
    module._apply_turnover_rates(rows, {"600519.SH": {}})

    assert rows[0]["turnover_rate"] is None


def test_projection_turnover_fetch_failure_keeps_projection_rows_writable():
    spec = importlib.util.spec_from_file_location("projection_bridge", PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    class FailingGateway:
        def get_turnover_rate(self, *args, **kwargs):
            raise RuntimeError("ContextInfo turnover unavailable")

    assert module._load_turnover_rates(
        FailingGateway(), ["600519.SH"], "20250101", "20250131"
    ) == {}

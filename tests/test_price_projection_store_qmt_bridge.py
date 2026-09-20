import importlib.util
from pathlib import Path


PATH = Path(__file__).parents[1] / "src/data_ingestion/8-原始行情与复权数据采集_qmt_bridge.py"
ORIGINAL = Path(__file__).parents[1] / "src/data_ingestion/8-原始行情与复权数据采集.py"


def test_projection_copy_is_separate_and_preserves_public_functions():
    assert PATH.exists()
    assert PATH.read_text(encoding="utf-8") != ORIGINAL.read_text(encoding="utf-8")
    source = PATH.read_text(encoding="utf-8")
    assert "from xtquant import xtdata" not in source
    spec = importlib.util.spec_from_file_location("projection_bridge", PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assert callable(module.download_and_save_all_modes)

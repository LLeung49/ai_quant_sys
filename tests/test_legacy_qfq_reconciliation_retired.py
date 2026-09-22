import importlib.util
from pathlib import Path
import sys

import pytest


ROOT = Path(__file__).parents[1]
INGESTION_DIR = ROOT / "src/data_ingestion"
SCRIPT_PATH = INGESTION_DIR / "9-前复权对账与定向重刷.py"


def test_legacy_reconciliation_cli_is_retired():
    sys.path.insert(0, str(INGESTION_DIR))
    try:
        spec = importlib.util.spec_from_file_location("legacy_qfq_reconciliation", SCRIPT_PATH)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    finally:
        sys.path.remove(str(INGESTION_DIR))

    with pytest.raises(RuntimeError):
        module.main(["--run-repairs"])

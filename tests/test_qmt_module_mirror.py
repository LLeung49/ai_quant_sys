from pathlib import Path


ROOT = Path(__file__).parents[1]
QMT_ROOTS = [ROOT / "src/data_ingestion_qmt", ROOT / "src/morning_conference_qmt"]
QMT_ENTRYPOINTS = [
    ROOT / "src/data_ingestion_qmt/1-行情数据采集_qmt_bridge.py",
    ROOT / "src/data_ingestion_qmt/2-财务数据采集_qmt_bridge.py",
    ROOT / "src/data_ingestion_qmt/8-原始行情与复权数据采集_qmt_bridge.py",
    ROOT / "src/morning_conference_qmt/sector_rotation/1-run_init_qmt_bridge.py",
    ROOT / "src/morning_conference_qmt/sector_rotation/2-run_data_daily_qmt_bridge.py",
]


def test_qmt_roots_and_entrypoints_exist_without_runtime_artifacts():
    for root in QMT_ROOTS:
        assert root.is_dir()
        assert not list(root.rglob("*.log"))
        assert not list(root.rglob("*.py[co]"))
        assert not list(root.rglob("__pycache__"))
    assert all(path.is_file() for path in QMT_ENTRYPOINTS)


def test_qmt_entrypoints_never_use_xtquant_or_legacy_xtdata_endpoint():
    for path in QMT_ENTRYPOINTS:
        source = path.read_text(encoding="utf-8")
        assert "from xtquant" not in source
        assert "import xtquant" not in source
        assert "xtdata." not in source
        assert "/api/xtdata/" not in source

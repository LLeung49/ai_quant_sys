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
MOVED_FROM_ORIGINAL = [
    ROOT / "src/data_ingestion/qmt_data_gateway.py",
    ROOT / "src/data_ingestion/qmt_gateway_probe.py",
    ROOT / "src/data_ingestion/qmt_client.py",
    ROOT / "src/data_ingestion/1-行情数据采集_qmt_bridge.py",
    ROOT / "src/data_ingestion/2-财务数据采集_qmt_bridge.py",
    ROOT / "src/data_ingestion/8-原始行情与复权数据采集_qmt_bridge.py",
    ROOT / "src/morning_conference/sector_rotation/industry_meta_qmt_bridge.py",
    ROOT / "src/morning_conference/sector_rotation/stock_kline_loader_qmt_bridge.py",
    ROOT / "src/morning_conference/sector_rotation2/research/etf_core/providers_qmt_bridge.py",
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


def test_qmt_specific_files_are_migrated_out_of_original_modules():
    assert not any(path.exists() for path in MOVED_FROM_ORIGINAL)
    assert (ROOT / "src/data_ingestion_qmt/qmt_data_gateway.py").is_file()
    assert (
        ROOT
        / "src/morning_conference_qmt/sector_rotation/industry_meta_qmt_bridge.py"
    ).is_file()


def test_qmt_sources_do_not_reference_original_project_packages():
    for root in QMT_ROOTS:
        for path in root.rglob("*.py"):
            source = path.read_text(encoding="utf-8")
            assert "from data_ingestion." not in source
            assert "import data_ingestion." not in source
            assert "from morning_conference." not in source
            assert "import morning_conference." not in source


def test_qmt_tree_contains_no_legacy_xtdata_transport():
    for root in QMT_ROOTS:
        for path in root.rglob("*.py"):
            source = path.read_text(encoding="utf-8")
            assert "from xtquant" not in source
            assert "import xtquant" not in source
            assert "xtdata." not in source
            assert "/api/xtdata/" not in source


def test_qmt_morning_entrypoints_select_bridge_loaders_and_keep_cli_options():
    root = ROOT / "src/morning_conference_qmt/sector_rotation"
    init_source = (root / "1-run_init_qmt_bridge.py").read_text(encoding="utf-8")
    daily_source = (root / "2-run_data_daily_qmt_bridge.py").read_text(encoding="utf-8")
    assert "from industry_meta_qmt_bridge import sync_sw_classification" in init_source
    assert "from stock_kline_loader_qmt_bridge import sync_all_kline" in init_source
    assert "--skip-schema" in init_source and "--skip-meta" in init_source
    assert "from industry_meta_qmt_bridge import sync_sw_classification" in daily_source
    assert "--refresh-meta" in daily_source and "--days" in daily_source

from types import SimpleNamespace

from data_ingestion import run_market_rebuild


def test_disk_guard_uses_free_bytes(monkeypatch):
    monkeypatch.setattr(
        run_market_rebuild.shutil,
        "disk_usage",
        lambda _path: SimpleNamespace(free=6 * 1024**3),
    )

    assert run_market_rebuild.has_minimum_free_space("D:/", 5.0)
    assert not run_market_rebuild.has_minimum_free_space("D:/", 7.0)


def test_rebuild_parser_defaults_to_five_gib_disk_guard():
    args = run_market_rebuild.build_parser().parse_args(["--end-date", "2026-10-13"])

    assert args.min_free_gib == 5.0
    assert args.max_batches is None


def test_resume_reads_completed_codes_once():
    class Store:
        calls = 0

        def completed_codes(self):
            self.calls += 1
            return {"000002.SZ"}

    store = Store()

    remaining = run_market_rebuild.remaining_codes(
        ["000001.SZ", "000002.SZ", "600519.SH"], store
    )

    assert remaining == ["000001.SZ", "600519.SH"]
    assert store.calls == 1

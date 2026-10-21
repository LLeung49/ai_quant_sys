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
        completed_calls = 0
        excluded_calls = 0

        def completed_codes(self):
            self.completed_calls += 1
            return {"000002.SZ"}

        def excluded_codes(self):
            self.excluded_calls += 1
            return {"000003.SZ"}

    store = Store()

    remaining = run_market_rebuild.remaining_codes(
        ["000001.SZ", "000002.SZ", "000003.SZ", "600519.SH"], store
    )

    assert remaining == ["000001.SZ", "600519.SH"]
    assert store.completed_calls == 1
    assert store.excluded_calls == 1


def test_limit_applies_after_full_universe_is_persisted_and_resumed():
    class Store:
        prepared = None

        def prepare_universe(self, codes):
            self.prepared = list(codes)
            return "full-universe-hash"

        def completed_codes(self):
            return {"000001.SZ"}

        def excluded_codes(self):
            return set()

    store = Store()
    codes, digest = run_market_rebuild.initialize_session_codes(
        ["000001.SZ", "000002.SZ", "000003.SZ"],
        store,
        dry_run=False,
        no_resume=False,
        limit=1,
    )

    assert store.prepared == ["000001.SZ", "000002.SZ", "000003.SZ"]
    assert codes == ["000002.SZ"]
    assert digest == "full-universe-hash"


def test_forced_codes_must_belong_to_full_universe():
    assert run_market_rebuild.select_forced_codes(
        ["000001.SZ", "600519.SH"], ["600519.SH"]
    ) == ["600519.SH"]

    try:
        run_market_rebuild.select_forced_codes(
            ["000001.SZ", "600519.SH"], ["999999.SH"]
        )
    except ValueError as exc:
        assert "outside immutable universe" in str(exc)
    else:
        raise AssertionError("foreign forced code must be rejected")

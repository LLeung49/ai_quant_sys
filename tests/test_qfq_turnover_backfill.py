import importlib.util
from pathlib import Path
import sys


PATH = Path(__file__).parents[1] / "src/data_ingestion_qmt/10-QFQ换手率全量回填_qmt.py"


def load_module():
    spec = importlib.util.spec_from_file_location("qfq_turnover_backfill", PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class FakeGateway:
    def __init__(self, response):
        self.response = response

    def get_turnover_rate(self, stock_codes, start_date, end_date):
        return self.response


def test_backfill_updates_only_null_rows(monkeypatch):
    module = load_module()
    captured = []

    def capture_update(sql, params):
        captured.append((sql, params))
        return 1

    monkeypatch.setattr(module, "execute_update", capture_update)
    window = module.TurnoverWindow(
        "600519.SH", "20260915", "20260918", {"20260915", "20260918"}
    )

    result = module.backfill_window(
        window,
        FakeGateway({"600519.SH": {"20260915": 0.0011, "20260918": 0.002}}),
        dry_run=False,
    )

    assert result.matched == 2
    assert result.written == 2
    assert [item[1] for item in captured] == [
        (0.11, "600519.SH", "2026-09-15"),
        (0.2, "600519.SH", "2026-09-18"),
    ]
    assert "AND turnover_rate IS NULL" in captured[0][0]


def test_dry_run_and_missing_qmt_date_do_not_write(monkeypatch):
    module = load_module()
    monkeypatch.setattr(module, "execute_update", lambda *_: (_ for _ in ()).throw(AssertionError()))
    window = module.TurnoverWindow(
        "600519.SH", "20260915", "20260918", {"20260915", "20260918"}
    )

    result = module.backfill_window(
        window, FakeGateway({"600519.SH": {"20260915": 0.0011}}), dry_run=True
    )

    assert result.written == 0
    assert result.missing_dates == {"20260918"}


def test_null_window_limit_is_bound_as_integer(monkeypatch):
    module = load_module()
    captured = []

    def capture_query(sql, params):
        captured.append((sql, params))
        return []

    monkeypatch.setattr(module, "execute_query", capture_query)

    assert module.load_null_turnover_windows(limit_codes=5) == []
    assert captured[0][1] == (5,)

from datetime import date
from decimal import Decimal
import json
from pathlib import Path

import pytest

from asset_allocation.etf_adaptive.research.instrument_validation import InstrumentValidationResult, ValidationStatus
from asset_allocation.etf_adaptive.research.instrument_validation import FIXED_VALIDATION_TARGETS


def test_cli_writes_one_status_per_fixed_target(tmp_path, monkeypatch) -> None:
    import asset_allocation.etf_adaptive.run_instrument_validation as module

    monkeypatch.setattr(module, "default_validation_provider", lambda: object())
    monkeypatch.setattr(module, "legacy_unprofiled", lambda target, provider, start, cutoff, cash: InstrumentValidationResult(target, ValidationStatus.PASSED, cutoff))

    assert module.main(["--start-date", "2020-01-01", "--as-of-date", "2026-09-08", "--output-dir", str(tmp_path)]) == 0
    payload = json.loads((tmp_path / "instrument_validation.json").read_text(encoding="utf-8"))
    assert len(payload["results"]) == len(FIXED_VALIDATION_TARGETS)
    assert {row["status"] for row in payload["results"]} == {"passed"}
    assert all(row["decision"]["conclusion"] == "do_not_trade" for row in payload["results"])
    assert all(row["activation_eligible"] is False for row in payload["results"])
    assert all(row["profile_id"] == "legacy_unprofiled" for row in payload["results"])
    assert "\n- " not in (tmp_path / "instrument_validation.md").read_text(encoding="utf-8")


def test_cli_publishes_per_instrument_validation_manifest(tmp_path, monkeypatch) -> None:
    import asset_allocation.etf_adaptive.run_instrument_validation as module

    target = FIXED_VALIDATION_TARGETS[0]
    result = InstrumentValidationResult(target, ValidationStatus.FAILED, date(2026, 9, 8))
    monkeypatch.setattr(module, "default_validation_provider", lambda: object())
    monkeypatch.setattr(module, "legacy_unprofiled", lambda *args: result)
    monkeypatch.setattr(module, "write_validation_artifacts", lambda value, destination: destination.mkdir(parents=True) or None)

    assert module.main(["--stock-code", target.stock_code, "--start-date", "2020-01-01", "--as-of-date", "2026-09-08", "--output-dir", str(tmp_path)]) == 0
    assert (tmp_path / target.stock_code).exists()


def test_cli_binds_declared_experiment_before_publication(tmp_path, monkeypatch):
    import asset_allocation.etf_adaptive.run_instrument_validation as module
    target = FIXED_VALIDATION_TARGETS[0]
    result = InstrumentValidationResult(target, ValidationStatus.FAILED, date(2026, 9, 8))
    captured = []
    monkeypatch.setattr(module, "default_validation_provider", lambda: object())
    monkeypatch.setattr(module, "legacy_unprofiled", lambda *args: result)
    monkeypatch.setattr(module, "write_validation_artifacts", lambda value, destination: captured.append(value))
    module.main(["--stock-code", target.stock_code, "--start-date", "2020-01-01",
                 "--as-of-date", "2026-09-08", "--output-dir", str(tmp_path)])
    metadata = captured[0].run_manifest
    assert metadata["experiment"]["target_codes"] == [target.stock_code]
    assert metadata["experiment"]["as_of_date"] == "2026-09-08"
    assert metadata["experiment"]["profile"]["profile_id"] == "legacy_unprofiled"
    assert metadata["experiment_hash"]
    assert metadata["strategy_spec"]["policy_id"] == "full_adaptive"


@pytest.mark.parametrize("filename", ["instrument_validation_513330_SH.json", "instrument_validation.json", "instrument_validation.md"])
def test_cli_final_replace_failure_preserves_previous_status(tmp_path, monkeypatch, filename):
    import os
    import asset_allocation.etf_adaptive.run_instrument_validation as module
    target = next(item for item in FIXED_VALIDATION_TARGETS if item.stock_code == "513330.SH")
    result = InstrumentValidationResult(target, ValidationStatus.FAILED, date(2026, 9, 8))
    destination = tmp_path / filename
    destination.write_text("previous status", encoding="utf-8")
    monkeypatch.setattr(module, "default_validation_provider", lambda: object())
    monkeypatch.setattr(module, "legacy_unprofiled", lambda *args: result)
    monkeypatch.setattr(module, "write_validation_artifacts", lambda *args: None)
    original = os.replace
    def fail_status(source, output):
        if Path(output) == destination:
            raise OSError("status replace failed")
        return original(source, output)
    monkeypatch.setattr(os, "replace", fail_status)
    with pytest.raises(OSError, match="status replace failed"):
        module.main(["--stock-code", target.stock_code, "--start-date", "2020-01-01",
                     "--as-of-date", "2026-09-08", "--output-dir", str(tmp_path)])
    assert destination.read_text(encoding="utf-8") == "previous status"


def _cli_args(output):
    return ["--start-date", "2020-01-01", "--as-of-date", "2026-09-08",
            "--output-dir", str(output)]


@pytest.mark.parametrize("name", ["industry-demo", "hk_internet", "chinext_reentry", "star50_extreme_window"])
def test_cli_rejects_named_experiment_without_profile(tmp_path, monkeypatch, capsys, name):
    import asset_allocation.etf_adaptive.run_instrument_validation as module

    def unexpected_provider():
        pytest.fail("invalid declaration must fail before provider construction")

    monkeypatch.setattr(module, "default_validation_provider", unexpected_provider)
    output = tmp_path / "output"
    with pytest.raises(SystemExit) as exc:
        module.main(_cli_args(output) + ["--experiment", name])
    assert exc.value.code == 2
    assert "--experiment requires --profile" in capsys.readouterr().err
    assert not output.exists()


@pytest.mark.parametrize("arguments,reason", [
    (["--profile", "grid_core"], "--profile requires --experiment"),
    (["--experiment", "industry-demo", "--profile", "grid_core"], "requires --stock-code"),
    (["--experiment", "industry-demo", "--profile", "unknown", "--stock-code", "515450.SH"], "invalid choice"),
    (["--experiment", "industry-demo", "--profile", "grid_core", "--stock-code", "999999.SH"], "fixed validation"),
    (["--experiment", "hk_internet", "--profile", "grid_core", "--stock-code", "515450.SH"], "target code"),
])
def test_cli_rejects_invalid_profile_assignment_before_provider(tmp_path, monkeypatch, capsys, arguments, reason):
    import asset_allocation.etf_adaptive.run_instrument_validation as module

    def unexpected_provider():
        pytest.fail("invalid declaration must fail before provider construction")

    monkeypatch.setattr(module, "default_validation_provider", unexpected_provider)
    output = tmp_path / "output"
    with pytest.raises(SystemExit) as exc:
        module.main(_cli_args(output) + arguments)
    assert exc.value.code == 2
    assert reason in capsys.readouterr().err
    assert not output.exists()


@pytest.mark.parametrize("profile_id", ["grid_core", "grid_plus_optional_trend", "core_hold_rebalance"])
@pytest.mark.parametrize("experiment,code", [("industry-demo", "515450.SH"), ("hk_internet", "513330.SH")])
def test_cli_persists_explicit_profile_and_fail_closed_decision(tmp_path, monkeypatch, profile_id, experiment, code):
    import asset_allocation.etf_adaptive.run_instrument_validation as module
    from asset_allocation.etf_adaptive.research.strategy_profiles import profile_for_id

    class EmptyProvider:
        def load_bars(self, stock_code, start_date, end_date):
            return ()

    monkeypatch.setattr(module, "default_validation_provider", EmptyProvider)
    assert module.main(_cli_args(tmp_path) + ["--experiment", experiment,
                       "--profile", profile_id, "--stock-code", code]) == 3
    payload = json.loads((tmp_path / "instrument_validation.json").read_text(encoding="utf-8"))
    row, = payload["results"]
    assert row["stock_code"] == code
    assert row["profile_id"] == profile_id
    assert row["profile_version"] == "1"
    assert row["profile_hash"] == profile_for_id(profile_id).profile_hash()
    assert row["status"] == "data_rejected"
    assert row["decision"]["conclusion"] == "do_not_trade"
    assert row["activation_eligible"] is False
    markdown = (tmp_path / "instrument_validation.md").read_text(encoding="utf-8")
    assert all(value in markdown for value in (profile_id, row["profile_hash"], "do_not_trade"))
    assert "profile_version" in markdown and "| 1 |" in markdown
    manifest = json.loads((tmp_path / "experiment.json").read_text(encoding="utf-8"))
    assert manifest["experiment"]["profile"]["profile_id"] == profile_id
    assert manifest["experiment"]["target_codes"] == [code]
    assert manifest["research_only"] is True
    assert manifest["trading_authorized"] is False


def test_cli_legacy_route_runs_without_an_implicit_profile(tmp_path, monkeypatch):
    import asset_allocation.etf_adaptive.run_instrument_validation as module

    class EmptyProvider:
        def load_bars(self, stock_code, start_date, end_date):
            return ()

    monkeypatch.setattr(module, "default_validation_provider", EmptyProvider)
    assert module.main(_cli_args(tmp_path) + ["--stock-code", "515450.SH"]) == 3
    row, = json.loads((tmp_path / "instrument_validation.json").read_text(encoding="utf-8"))["results"]
    assert row["profile_id"] == "legacy_unprofiled"
    assert row["profile_version"] == "0"
    assert row["decision"]["conclusion"] == "do_not_trade"
    assert row["activation_eligible"] is False

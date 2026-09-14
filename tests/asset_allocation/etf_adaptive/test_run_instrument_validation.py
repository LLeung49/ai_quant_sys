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
    monkeypatch.setattr(module, "run_instrument_validation", lambda target, provider, start, cutoff, cash: InstrumentValidationResult(target, ValidationStatus.PASSED, cutoff))

    assert module.main(["--start-date", "2020-01-01", "--as-of-date", "2026-09-08", "--output-dir", str(tmp_path)]) == 0
    payload = json.loads((tmp_path / "instrument_validation.json").read_text(encoding="utf-8"))
    assert len(payload["results"]) == len(FIXED_VALIDATION_TARGETS)
    assert {row["status"] for row in payload["results"]} == {"passed"}
    assert all(row["decision"]["conclusion"] == "do_not_trade" for row in payload["results"])
    assert all(row["activation_eligible"] is False for row in payload["results"])
    assert "\n- " not in (tmp_path / "instrument_validation.md").read_text(encoding="utf-8")


def test_cli_publishes_per_instrument_validation_manifest(tmp_path, monkeypatch) -> None:
    import asset_allocation.etf_adaptive.run_instrument_validation as module

    target = FIXED_VALIDATION_TARGETS[0]
    result = InstrumentValidationResult(target, ValidationStatus.FAILED, date(2026, 9, 8))
    monkeypatch.setattr(module, "default_validation_provider", lambda: object())
    monkeypatch.setattr(module, "run_instrument_validation", lambda *args: result)
    monkeypatch.setattr(module, "write_validation_artifacts", lambda value, destination: destination.mkdir(parents=True) or None)

    assert module.main(["--stock-code", target.stock_code, "--start-date", "2020-01-01", "--as-of-date", "2026-09-08", "--output-dir", str(tmp_path)]) == 0
    assert (tmp_path / target.stock_code).exists()


def test_cli_binds_declared_experiment_before_publication(tmp_path, monkeypatch):
    import asset_allocation.etf_adaptive.run_instrument_validation as module
    target = FIXED_VALIDATION_TARGETS[0]
    result = InstrumentValidationResult(target, ValidationStatus.FAILED, date(2026, 9, 8))
    captured = []
    monkeypatch.setattr(module, "default_validation_provider", lambda: object())
    monkeypatch.setattr(module, "run_instrument_validation", lambda *args: result)
    monkeypatch.setattr(module, "write_validation_artifacts", lambda value, destination: captured.append(value))
    module.main(["--stock-code", target.stock_code, "--start-date", "2020-01-01",
                 "--as-of-date", "2026-09-08", "--output-dir", str(tmp_path)])
    metadata = captured[0].run_manifest
    assert metadata["experiment"]["target_codes"] == [target.stock_code]
    assert metadata["experiment"]["as_of_date"] == "2026-09-08"
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
    monkeypatch.setattr(module, "run_instrument_validation", lambda *args: result)
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

"""Frozen research selection validation, activation window, and store wiring."""

from __future__ import annotations

import json
import shutil
import uuid
from datetime import date, datetime, timedelta
from pathlib import Path

import pytest

from asset_allocation.etf_adaptive.frozen_selection import (
    FrozenSelection,
    FrozenSelectionError,
    MAX_SINGLE_TARGET_WEIGHT,
    SIX_MONTH_REVIEW_DAYS,
    _canonical_hash,
    activate_selection,
)
from asset_allocation.etf_adaptive.shadow_store import InMemoryShadowStore


REPORTS_ROOT = Path("D:/aiQuant/ai_quant_sys/reports/pytest-frozen-selection-tmp")


@pytest.fixture
def manifest_dir() -> Path:
    REPORTS_ROOT.mkdir(parents=True, exist_ok=True)
    target = REPORTS_ROOT / f"manifest-{uuid.uuid4().hex}"
    target.mkdir(parents=True, exist_ok=True)
    try:
        yield target
    finally:
        shutil.rmtree(target, ignore_errors=True)


def _payload(
    *,
    config_hash: str,
    targets: tuple[dict, ...] = (
        {"stock_code": "510300.SH", "layer": "core_broad", "weight": 0.5,
         "tracking_index_code": "000300.SH"},
        {"stock_code": "510500.SH", "layer": "core_broad", "weight": 0.5,
         "tracking_index_code": "000905.SH"},
    ),
    layer_weights: dict | None = None,
    activation_date: str = "2026-09-01",
    review_date: str | None = None,
    data_cutoff: str = "2026-09-01",
) -> dict:
    review_date = review_date or (
        date.fromisoformat(activation_date) + timedelta(days=SIX_MONTH_REVIEW_DAYS)
    ).isoformat()
    payload = {
        "selection_id": "selection-2026-09",
        "data_cutoff": data_cutoff,
        "activation_date": activation_date,
        "review_date": review_date,
        "targets": list(targets),
        "layer_weights": layer_weights or {"core_broad": 1.0},
    }
    canonical = _canonical_hash(payload)
    payload["config_hash"] = canonical if config_hash == "irrelevant" else config_hash
    return payload


def _selection(config_hash: str | None = None, **overrides) -> FrozenSelection:
    return FrozenSelection.from_payload(_payload(config_hash=config_hash or "irrelevant", **overrides))


def test_frozen_selection_rejects_manifest_hash_mismatch() -> None:
    try:
        _selection(config_hash="wrong-hash")
    except FrozenSelectionError as exc:
        assert "manifest config hash mismatch" in str(exc)
    else:
        raise AssertionError("expected FrozenSelectionError on hash mismatch")


def test_frozen_selection_round_trips_valid_payload() -> None:
    payload = _payload(config_hash="irrelevant")
    selection = FrozenSelection.from_payload(payload)

    assert selection.config_hash == payload["config_hash"]
    assert selection.activation_date == date(2026, 9, 1)
    assert selection.review_date == date(2026, 9, 1) + timedelta(days=SIX_MONTH_REVIEW_DAYS)
    assert selection.review_window_days == SIX_MONTH_REVIEW_DAYS
    assert {target.stock_code for target in selection.targets} == {"510300.SH", "510500.SH"}


def test_frozen_selection_rejects_duplicate_stock_codes() -> None:
    payload = _payload(
        config_hash="irrelevant",
        targets=(
            {"stock_code": "510300.SH", "layer": "core_broad", "weight": 0.5,
             "tracking_index_code": "000300.SH"},
            {"stock_code": "510300.SH", "layer": "core_broad", "weight": 0.5,
             "tracking_index_code": "000300.SH"},
        ),
    )

    try:
        FrozenSelection.from_payload(payload)
    except FrozenSelectionError as exc:
        assert "duplicate stock_code" in str(exc)
    else:
        raise AssertionError("expected FrozenSelectionError for duplicate stock codes")


def test_frozen_selection_rejects_layer_weight_not_summing_to_one() -> None:
    payload = _payload(
        config_hash="irrelevant",
        targets=(
            {"stock_code": "510300.SH", "layer": "core_broad", "weight": 0.4,
             "tracking_index_code": "000300.SH"},
            {"stock_code": "510500.SH", "layer": "core_broad", "weight": 0.4,
             "tracking_index_code": "000905.SH"},
        ),
        layer_weights={"core_broad": 0.8},
    )

    try:
        FrozenSelection.from_payload(payload)
    except FrozenSelectionError as exc:
        assert "weights sum to" in str(exc)
    else:
        raise AssertionError("expected FrozenSelectionError for layer weight sum")


def test_frozen_selection_rejects_single_target_above_cap() -> None:
    payload = _payload(
        config_hash="irrelevant",
        targets=(
            {"stock_code": "510300.SH", "layer": "core_broad",
             "weight": MAX_SINGLE_TARGET_WEIGHT + 0.05, "tracking_index_code": "000300.SH"},
            {"stock_code": "510500.SH", "layer": "core_broad", "weight": 0.3,
             "tracking_index_code": "000905.SH"},
        ),
    )

    try:
        FrozenSelection.from_payload(payload)
    except FrozenSelectionError as exc:
        assert "exceeds the" in str(exc)
    else:
        raise AssertionError("expected FrozenSelectionError for over-weight target")


def test_frozen_selection_rejects_six_month_window_violation() -> None:
    payload = _payload(config_hash="irrelevant", review_date="2027-04-01")

    try:
        FrozenSelection.from_payload(payload)
    except FrozenSelectionError as exc:
        assert "review window" in str(exc)
    else:
        raise AssertionError("expected FrozenSelectionError for wrong review window")


def test_validate_activation_rejects_future_and_expired_dates() -> None:
    selection = _selection()

    try:
        selection.validate_activation(date(2026, 8, 31))
    except FrozenSelectionError as exc:
        assert "future" in str(exc)
    else:
        raise AssertionError("expected FrozenSelectionError for early activation")

    try:
        selection.validate_activation(date(2027, 4, 1))
    except FrozenSelectionError as exc:
        assert "review date" in str(exc)
    else:
        raise AssertionError("expected FrozenSelectionError for expired selection")


def test_activate_selection_persists_to_store_and_enforces_window() -> None:
    store = InMemoryShadowStore()
    selection = _selection()

    record = activate_selection(store, selection, now=datetime(2026, 10, 1, 17, 0))

    assert store.frozen_config_count == 1
    assert record.config_hash == selection.config_hash
    assert store.load_active_frozen_config(date(2026, 12, 1)) is record


def test_activate_selection_refuses_to_activate_before_window() -> None:
    store = InMemoryShadowStore()
    selection = _selection()

    try:
        activate_selection(store, selection, now=datetime(2026, 7, 1, 17, 0))
    except FrozenSelectionError as exc:
        assert "future" in str(exc)
    else:
        raise AssertionError("expected FrozenSelectionError when activating before window")


def test_from_research_manifest_round_trips_via_disk(manifest_dir: Path) -> None:
    payload = _payload(config_hash="irrelevant")
    manifest_path = manifest_dir / "manifest.json"
    manifest_path.write_text(
        json.dumps(payload, ensure_ascii=False, sort_keys=True),
        encoding="utf-8",
    )

    selection = FrozenSelection.from_research_manifest(manifest_path)

    assert selection.config_hash == payload["config_hash"]
    assert selection.data_cutoff == date(2026, 9, 1)

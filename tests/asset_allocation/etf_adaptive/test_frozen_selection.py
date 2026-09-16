"""Frozen research selection validation, activation window, and store wiring."""

from __future__ import annotations

import json
import shutil
import uuid
from dataclasses import asdict
from datetime import date, datetime, timedelta
from decimal import Decimal
from pathlib import Path

import pytest

from asset_allocation.etf_adaptive.frozen_selection import (
    FrozenSelection,
    FrozenSelectionError,
    SIX_MONTH_REVIEW_DAYS,
    _canonical_hash,
    activate_selection,
)
from asset_allocation.etf_adaptive.shadow_store import InMemoryShadowStore
from asset_allocation.etf_adaptive.config import AdaptiveConfig, CostConfig, GridConfig, TrendConfig


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
        {"stock_code": "510300.SH", "layer": "broad_beta", "weight": "0.5",
         "tracking_index_code": "000300.SH", "sub_layer": "broad_domestic_core",
         "sub_layer_budget": "42000", "instrument_type": "etf"},
        {"stock_code": "510500.SH", "layer": "broad_beta", "weight": "0.5",
         "tracking_index_code": "000905.SH", "sub_layer": "broad_domestic_core",
         "sub_layer_budget": "42000", "instrument_type": "etf"},
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
        "layer_weights": layer_weights or {"broad_beta": 1.0},
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


def test_frozen_selection_restores_declared_custom_configuration() -> None:
    config = AdaptiveConfig(
        grid=GridConfig(step_pct=0.035, unit_pct=0.15),
        trend=TrendConfig(stop_n=2.5, require_macd_bullish=False),
        cost=CostConfig(slippage_bps=4.0, sell_tax_rate=0.001, transfer_fee_rate=0.0001),
    )
    payload = _payload(config_hash="irrelevant")
    payload.update(config=asdict(config), declared_config_hash=config.config_hash())
    payload["config_hash"] = _canonical_hash(payload)

    assert FrozenSelection.from_payload(payload).base_config == config


@pytest.mark.parametrize("mutation", ("missing_config", "wrong_hash", "missing_hash"))
def test_frozen_selection_rejects_incomplete_or_mismatched_declared_config(mutation) -> None:
    config = AdaptiveConfig(grid=GridConfig(step_pct=0.035))
    payload = _payload(config_hash="irrelevant")
    payload.update(config=asdict(config), declared_config_hash=config.config_hash())
    if mutation == "missing_config":
        del payload["config"]
    elif mutation == "wrong_hash":
        payload["declared_config_hash"] = AdaptiveConfig.default().config_hash()
    else:
        del payload["declared_config_hash"]
    payload["config_hash"] = _canonical_hash(payload)

    with pytest.raises(FrozenSelectionError, match="config"):
        FrozenSelection.from_payload(payload)


@pytest.mark.parametrize("target_count", (1, 3))
def test_layered_selection_accepts_any_nonempty_evidence_supported_target_count(
    target_count: int,
) -> None:
    targets = tuple(
        {
            "stock_code": f"510{300 + index}.SH",
            "tracking_index_code": "000300.SH",
            "layer": "broad_beta",
            "sub_layer": "broad_domestic_core",
            "sub_layer_budget": "42000",
            "instrument_type": "etf",
            "weight": (
                "1" if target_count == 1 else ("0.2", "0.3", "0.5")[index]
            ),
        }
        for index in range(target_count)
    )
    payload = _payload(
        config_hash="irrelevant",
        targets=targets,
        layer_weights={"broad_beta": 1.0},
    )
    payload["config_hash"] = _canonical_hash(payload)

    selection = FrozenSelection.from_payload(payload)

    assert len(selection.targets) == target_count
    assert selection.targets[0].sub_layer.value == "broad_domestic_core"
    assert selection.targets[0].sub_layer_budget == Decimal("42000")
    assert selection.targets[0].instrument_type.value == "etf"


def test_layered_selection_rejects_empty_configured_sub_layer() -> None:
    payload = _payload(
        config_hash="irrelevant",
        targets=(
            {"stock_code": "510300.SH", "layer": "defensive", "weight": "1",
             "tracking_index_code": "000922.SH", "sub_layer": "defensive_dividend_etf",
             "sub_layer_budget": "42000", "instrument_type": "etf"},
        ),
        layer_weights={"defensive": 1.0},
    )
    payload["sub_layer_budgets"] = {
        "defensive_dividend_etf": "42000",
        "defensive_blue_chip": "18000",
    }
    payload["config_hash"] = _canonical_hash(payload)

    with pytest.raises(FrozenSelectionError, match="no selected targets"):
        FrozenSelection.from_payload(payload)


def test_frozen_selection_rejects_duplicate_stock_codes() -> None:
    payload = _payload(
        config_hash="irrelevant",
        targets=(
            {"stock_code": "510300.SH", "layer": "broad_beta", "weight": "0.5",
             "tracking_index_code": "000300.SH", "sub_layer": "broad_domestic_core",
             "sub_layer_budget": "42000", "instrument_type": "etf"},
            {"stock_code": "510300.SH", "layer": "broad_beta", "weight": "0.5",
             "tracking_index_code": "000300.SH", "sub_layer": "broad_domestic_core",
             "sub_layer_budget": "42000", "instrument_type": "etf"},
        ),
    )

    try:
        FrozenSelection.from_payload(payload)
    except FrozenSelectionError as exc:
        assert "duplicate stock_code" in str(exc)
    else:
        raise AssertionError("expected FrozenSelectionError for duplicate stock codes")


def test_frozen_selection_rejects_sub_layer_weight_not_summing_to_one() -> None:
    payload = _payload(
        config_hash="irrelevant",
        targets=(
            {"stock_code": "510300.SH", "layer": "broad_beta", "weight": "0.4",
             "tracking_index_code": "000300.SH", "sub_layer": "broad_domestic_core",
             "sub_layer_budget": "42000", "instrument_type": "etf"},
            {"stock_code": "510500.SH", "layer": "broad_beta", "weight": "0.4",
             "tracking_index_code": "000905.SH", "sub_layer": "broad_domestic_core",
             "sub_layer_budget": "42000", "instrument_type": "etf"},
        ),
        layer_weights={"core_broad": 0.8},
    )

    try:
        FrozenSelection.from_payload(payload)
    except FrozenSelectionError as exc:
        assert "sub-layer" in str(exc)
    else:
        raise AssertionError("expected FrozenSelectionError for layer weight sum")


def test_frozen_selection_allows_single_target_with_full_evidence_configured_weight() -> None:
    payload = _payload(
        config_hash="irrelevant",
        targets=(
            {"stock_code": "510300.SH", "layer": "broad_beta",
             "weight": "1", "tracking_index_code": "000300.SH",
             "sub_layer": "broad_domestic_core", "sub_layer_budget": "42000",
             "instrument_type": "etf"},
        ),
    )

    payload["config_hash"] = _canonical_hash(payload)

    assert FrozenSelection.from_payload(payload).targets[0].weight == Decimal("1")


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
    assert record.selection_payload["targets"][0] == {
        "stock_code": "510300.SH",
        "tracking_index_code": "000300.SH",
        "layer": "broad_beta",
        "sub_layer": "broad_domestic_core",
        "sub_layer_budget": "42000",
        "instrument_type": "etf",
        "weight": "0.5",
        "config_hash": selection.config_hash,
    }
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

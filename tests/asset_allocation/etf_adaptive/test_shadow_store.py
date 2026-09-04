"""Shadow store contract: idempotent persistence and config-conflict safety."""

from __future__ import annotations

from dataclasses import replace
from datetime import date, datetime
from decimal import Decimal

import pytest

from asset_allocation.etf_adaptive.config import AdaptiveConfig
from asset_allocation.etf_adaptive.shadow_store import (
    ConfigConflictError,
    DuplicateRunError,
    FillObservation,
    FrozenConfigRecord,
    InMemoryShadowStore,
    ShadowRunIdentity,
    build_run_record,
)
from asset_allocation.etf_adaptive.state import (
    OrderIntent,
    OrderReason,
    Side,
    StrategyState,
)


def _shadow_run(*, config_hash: str = "cfg-a", run_id: str = "run-1") -> "ShadowRunRecord":
    identity = ShadowRunIdentity(
        as_of_date=date(2026, 9, 1),
        model_version="v1",
        stock_code="510300.SH",
    )
    return build_run_record(
        run_id=run_id,
        identity=identity,
        config_hash=config_hash,
        execution_eligible_date=date(2026, 9, 2),
        state=StrategyState(cash=Decimal("100000"), position_shares=0),
        orders=(
            OrderIntent(
                signal_date=date(2026, 9, 1),
                side=Side.BUY,
                reason=OrderReason.GRID_INITIALIZE,
                signal_atr20=None,
                signal_thresholds=(("grid_anchor", 1.0),),
                target_budget=0.0,
                risk_per_unit=0.0,
                quantity_rationale="test",
            ),
        ),
    )


def test_persist_run_is_idempotent_and_never_replaces_different_config() -> None:
    store = InMemoryShadowStore()
    run = _shadow_run(config_hash="cfg-a")

    store.persist_run(run)
    store.persist_run(run)

    assert store.run_count == 1
    with pytest.raises(ConfigConflictError):
        store.persist_run(replace(run, config_hash="cfg-b"))


def test_persist_run_rejects_run_id_mismatch_on_same_identity() -> None:
    store = InMemoryShadowStore()
    run_a = _shadow_run(config_hash="cfg-a", run_id="run-1")

    store.persist_run(run_a)

    with pytest.raises(DuplicateRunError):
        store.persist_run(_shadow_run(config_hash="cfg-a", run_id="run-2"))


def test_load_latest_state_returns_most_recent_for_stock_and_config() -> None:
    store = InMemoryShadowStore()
    first = _shadow_run(config_hash="cfg-a", run_id="run-1")
    store.persist_run(first)

    later_identity = replace(first.identity, as_of_date=date(2026, 9, 2))
    later = build_run_record(
        run_id="run-1",
        identity=later_identity,
        config_hash="cfg-a",
        execution_eligible_date=date(2026, 9, 3),
        state=StrategyState(cash=Decimal("90000"), position_shares=100),
        orders=(),
    )
    store.persist_run(later)

    found = store.load_latest_state("510300.SH", "cfg-a")

    assert found is not None
    run, state = found
    assert run.identity.as_of_date == date(2026, 9, 2)
    assert state.cash == Decimal("90000")


def test_load_latest_state_isolates_by_config_hash() -> None:
    store = InMemoryShadowStore()
    store.persist_run(_shadow_run(config_hash="cfg-a", run_id="run-1"))
    later_identity = ShadowRunIdentity(
        as_of_date=date(2026, 9, 2),
        model_version="v1",
        stock_code="510300.SH",
    )
    store.persist_run(
        build_run_record(
            run_id="run-1",
            identity=later_identity,
            config_hash="cfg-b",
            execution_eligible_date=date(2026, 9, 3),
            state=StrategyState(cash=Decimal("50000")),
            orders=(),
        ),
    )

    assert store.load_latest_state("510300.SH", "cfg-a") is not None
    assert store.load_latest_state("510300.SH", "cfg-b") is not None
    assert store.load_latest_state("510300.SH", "cfg-c") is None


def test_activate_frozen_config_round_trips_through_store() -> None:
    store = InMemoryShadowStore()
    record = FrozenConfigRecord(
        config_hash="cfg-a",
        config=AdaptiveConfig.default(),
        selection_payload={"targets": [{"stock_code": "510300.SH"}]},
        data_cutoff=date(2026, 9, 1),
        activation_date=date(2026, 9, 1),
        review_date=date(2027, 3, 1),
        activated_at=datetime(2026, 9, 1, 17, 0),
    )

    store.activate_frozen_config(record)

    assert store.load_frozen_config("cfg-a") is record
    assert store.load_active_frozen_config(date(2026, 10, 15)) is record
    assert store.load_active_frozen_config(date(2028, 1, 1)) is None


def test_load_active_frozen_config_picks_most_recent_activation() -> None:
    store = InMemoryShadowStore()
    earlier = FrozenConfigRecord(
        config_hash="cfg-a",
        config=AdaptiveConfig.default(),
        selection_payload={},
        data_cutoff=date(2026, 1, 1),
        activation_date=date(2026, 1, 1),
        review_date=date(2026, 6, 30),
        activated_at=datetime(2026, 1, 1, 17, 0),
    )
    later = FrozenConfigRecord(
        config_hash="cfg-b",
        config=AdaptiveConfig.default(),
        selection_payload={},
        data_cutoff=date(2026, 6, 1),
        activation_date=date(2026, 6, 1),
        review_date=date(2026, 12, 31),
        activated_at=datetime(2026, 6, 1, 17, 0),
    )
    store.activate_frozen_config(earlier)
    store.activate_frozen_config(later)

    assert store.load_active_frozen_config(date(2026, 8, 1)) is later


def test_record_fill_observation_appends_to_history() -> None:
    store = InMemoryShadowStore()
    observation = FillObservation(
        execution_eligible_date=date(2026, 9, 2),
        stock_code="510300.SH",
        config_hash="cfg-a",
        raw_open=1.02,
        raw_close=1.03,
        slippage_bps=2.0,
        fill_complete=True,
        notes="clean open",
    )

    store.record_fill_observation(observation)

    assert store.fill_observations[-1] is observation


def test_activate_frozen_config_rejects_empty_hash() -> None:
    store = InMemoryShadowStore()
    record = FrozenConfigRecord(
        config_hash="",
        config=AdaptiveConfig.default(),
        selection_payload={},
        data_cutoff=date(2026, 9, 1),
        activation_date=date(2026, 9, 1),
        review_date=date(2027, 3, 1),
        activated_at=datetime(2026, 9, 1, 17, 0),
    )

    try:
        store.activate_frozen_config(record)
    except ValueError as exc:
        assert "config_hash" in str(exc)
    else:
        raise AssertionError("expected ValueError for empty config_hash")

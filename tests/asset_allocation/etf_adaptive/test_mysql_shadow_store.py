"""MySQL shadow store behaviour: SQL emission, transaction, idempotency."""

from __future__ import annotations

from dataclasses import asdict
from datetime import date, datetime, timedelta
from decimal import Decimal
from typing import Any
import json

import pytest

from asset_allocation.etf_adaptive.config import AdaptiveConfig, CostConfig, GridConfig, TrendConfig
from asset_allocation.etf_adaptive.frozen_selection import FrozenSelection, _canonical_hash, activate_selection
from asset_allocation.etf_adaptive.mysql_shadow_store import (
    MySQLShadowStore,
    _deserialize_strategy_state,
    _serialize_strategy_state,
    _split_sql_statements,
)
from asset_allocation.etf_adaptive.shadow_store import (
    ConfigConflictError,
    DuplicateRunError,
    FillObservation,
    FrozenConfigRecord,
    ShadowRunIdentity,
    build_run_record,
)
from asset_allocation.etf_adaptive.state import (
    OrderIntent,
    OrderReason,
    Regime,
    Side,
    StrategyState,
    TrendUnit,
)


class _RecordingCursor:
    def __init__(self) -> None:
        self.statements: list[tuple[str, tuple | None]] = []
        self.results: list[list[tuple]] = [()]
        self.executed = 0
        self._index = 0

    def execute(self, sql: str, params: tuple | None = None) -> None:
        self.statements.append((sql.strip(), params))
        self.executed += 1
        self._index = self.executed - 1
        if self._raise_with is not None:
            message, marker = self._raise_with
            if marker is None or marker in sql:
                self._raise_with = None
                raise RuntimeError(message)

    def fetchone(self) -> tuple | None:
        if not self.results:
            return None
        bucket = self.results[min(self._index, len(self.results) - 1)]
        return bucket[0] if bucket else None

    def fetchall(self) -> list[tuple]:
        if not self.results:
            return []
        return self.results[min(self._index, len(self.results) - 1)]

    def close(self) -> None:
        return None

    def set_results(self, *result_buckets: list[tuple]) -> None:
        self.results = [bucket for bucket in result_buckets] or [()]

    def program_failure(self, message: str, marker: str | None = None) -> None:
        self._raise_with = (message, marker)

    _raise_with: tuple[str, str | None] | None = None


class _RecordingConnection:
    def __init__(self) -> None:
        self.cursor_obj = _RecordingCursor()
        self.commits = 0
        self.rollbacks = 0
        self.closed = False

    def cursor(self) -> _RecordingCursor:
        return self.cursor_obj

    def commit(self) -> None:
        self.commits += 1

    def rollback(self) -> None:
        self.rollbacks += 1

    def close(self) -> None:
        self.closed = True

    def executed_statements(self) -> list[str]:
        return [sql for sql, _ in self.cursor_obj.statements]


def _connection_factory(connection: _RecordingConnection):
    def factory() -> _RecordingConnection:
        return connection
    return factory


def _selection_payload(config=None):
    payload = {
        "selection_id": "round-trip", "data_cutoff": "2026-09-01",
        "activation_date": "2026-09-01",
        "review_date": (date(2026, 9, 1) + timedelta(days=183)).isoformat(),
        "targets": [{"stock_code": "510300.SH", "sub_layer": "broad_domestic_core",
                     "sub_layer_budget": "42000", "instrument_type": "etf", "weight": "1"}],
    }
    if config is not None:
        payload.update(config=asdict(config), declared_config_hash=config.config_hash())
    payload["config_hash"] = _canonical_hash(payload)
    return payload


class _FrozenRowCursor(_RecordingCursor):
    """Persist the actual INSERT tuple at the external SQL boundary."""
    frozen_row = None

    def execute(self, sql, params=None):
        super().execute(sql, params)
        if "INSERT INTO asset_allocation_etf_adaptive_frozen_config" in sql:
            self.frozen_row = params

    def fetchone(self):
        return self.frozen_row


@pytest.mark.parametrize("custom", (False, True))
@pytest.mark.parametrize("active", (False, True))
def test_normal_selection_activation_round_trips_through_mysql(custom, active):
    config = AdaptiveConfig(grid=GridConfig(step_pct=0.035), cost=CostConfig(slippage_bps=4.0)) if custom else AdaptiveConfig.default()
    selection = FrozenSelection.from_payload(_selection_payload(config if custom else None))
    conn = _RecordingConnection()
    conn.cursor_obj = _FrozenRowCursor()
    store = MySQLShadowStore(connection_factory=_connection_factory(conn))
    activated = activate_selection(store, selection, now=datetime(2026, 9, 1, 17, 0))

    loaded = store.load_active_frozen_config(date(2026, 9, 2)) if active else store.load_frozen_config(selection.config_hash)

    assert loaded == activated
    assert loaded.config == config
    assert loaded.config_hash == selection.config_hash != config.config_hash()
    assert loaded.selection_payload["selection_hash"] == selection.config_hash
    assert loaded.selection_payload["declared_config_hash"] == config.config_hash()


@pytest.mark.parametrize("field", ("config", "selection"))
def test_mysql_selection_load_rejects_tampering_of_either_identity(field):
    selection = FrozenSelection.from_payload(_selection_payload())
    conn = _RecordingConnection()
    conn.cursor_obj = _FrozenRowCursor()
    store = MySQLShadowStore(connection_factory=_connection_factory(conn))
    activate_selection(store, selection, now=datetime(2026, 9, 1, 17, 0))
    row = list(conn.cursor_obj.frozen_row)
    if field == "config":
        payload = json.loads(row[1])
        payload["grid"]["step_pct"] = 0.035
        row[1] = json.dumps(payload)
    else:
        payload = json.loads(row[2])
        payload["targets"][0]["sub_layer_budget"] = "99999"
        row[2] = json.dumps(payload)
    conn.cursor_obj.frozen_row = tuple(row)

    with pytest.raises(ValueError):
        store.load_active_frozen_config(date(2026, 9, 2))


def _frozen_record() -> FrozenConfigRecord:
    return FrozenConfigRecord(
        config_hash="cfg-a" * 16,
        config=AdaptiveConfig.default(),
        selection_payload={"targets": [{"stock_code": "510300.SH", "weight": 1.0}]},
        data_cutoff=date(2026, 9, 1),
        activation_date=date(2026, 9, 1),
        review_date=date(2027, 3, 2),
        activated_at=datetime(2026, 9, 1, 17, 0),
    )


def _run_record(*, config_hash: str = "cfg-a" * 16, run_id: str = "run-1") -> Any:
    state = StrategyState(
        regime=Regime.GRID,
        position_shares=100,
        cash=Decimal("99000"),
        grid_anchor=1.0,
        cycle_entry_price=1.0,
        grid_stop_price=0.95,
        units=(TrendUnit(
            raw_fill_price=1.0,
            signal_fill_price=1.0,
            signal_atr20=0.05,
            shares=100,
            next_add_signal_price=1.05,
        ),),
        applied_action_ids=("510300.SH:2026-09-01:cash_dividend",),
        cooldown_remaining=5,
    )
    identity = ShadowRunIdentity(
        as_of_date=date(2026, 9, 1),
        model_version="shadow-v1",
        stock_code="510300.SH",
    )
    return build_run_record(
        run_id=run_id,
        identity=identity,
        config_hash=config_hash,
        execution_eligible_date=date(2026, 9, 2),
        state=state,
        orders=(
            OrderIntent(
                signal_date=date(2026, 9, 1),
                side=Side.BUY,
                reason=OrderReason.GRID_BUY,
                signal_atr20=0.05,
                signal_thresholds=(("grid_anchor", 1.0),),
                target_budget=0.10,
                risk_per_unit=0.005,
                quantity_rationale="GRID unit",
            ),
        ),
    )


def test_split_sql_statements_ignores_comments_and_keeps_create_blocks() -> None:
    sql = """
    -- header comment
    CREATE TABLE foo (id INT);
    CREATE TABLE bar (id INT);
    """

    statements = _split_sql_statements(sql)

    assert len(statements) == 2
    assert all(stmt.startswith("CREATE TABLE") for stmt in statements)


def test_split_sql_statements_drops_empty_fragments() -> None:
    sql = "CREATE TABLE foo (id INT);;;   "

    statements = _split_sql_statements(sql)

    assert len(statements) == 1
    assert statements[0].startswith("CREATE TABLE")


def test_serialize_strategy_state_round_trips_via_json() -> None:
    state = StrategyState(
        regime=Regime.TREND,
        position_shares=200,
        cash=Decimal("100000.50"),
        grid_anchor=1.02,
        cycle_entry_price=1.00,
        grid_stop_price=0.95,
        trend_stop_price=0.92,
        highest_close=1.10,
        cooldown_remaining=3,
        units=(TrendUnit(1.0, 1.0, 0.05, 200, 1.06),),
        applied_action_ids=("510300.SH:2026-09-01:cash_dividend",),
    )

    encoded = _serialize_strategy_state(state)
    decoded = _deserialize_strategy_state(encoded)

    assert decoded == state


def test_ensure_schema_executes_create_table_statements_once() -> None:
    conn = _RecordingConnection()
    store = MySQLShadowStore(connection_factory=_connection_factory(conn))

    store.ensure_schema()

    create_statements = [
        sql for sql in conn.executed_statements() if sql.startswith("CREATE TABLE")
    ]
    assert len(create_statements) == 6
    first_commit_total = conn.commits
    assert first_commit_total >= 1

    store.ensure_schema()
    assert conn.commits == first_commit_total
    assert conn.closed is True


def test_activate_frozen_config_uses_insert_on_duplicate_key() -> None:
    conn = _RecordingConnection()
    store = MySQLShadowStore(connection_factory=_connection_factory(conn))

    store.activate_frozen_config(_frozen_record())

    upsert = next(
        sql for sql in conn.executed_statements()
        if sql.startswith("INSERT INTO asset_allocation_etf_adaptive_frozen_config")
    )
    assert "ON DUPLICATE KEY UPDATE" in upsert
    assert conn.commits >= 1


def test_activate_frozen_config_rejects_empty_hash() -> None:
    store = MySQLShadowStore(connection_factory=_connection_factory(_RecordingConnection()))
    record = FrozenConfigRecord(
        config_hash="",
        config=AdaptiveConfig.default(),
        selection_payload={},
        data_cutoff=date(2026, 9, 1),
        activation_date=date(2026, 9, 1),
        review_date=date(2027, 3, 2),
        activated_at=datetime(2026, 9, 1, 17, 0),
    )

    try:
        store.activate_frozen_config(record)
    except ValueError as exc:
        assert "config_hash" in str(exc)
    else:
        raise AssertionError("expected ValueError for empty config_hash")


def test_persist_run_writes_run_state_and_advice_tables() -> None:
    conn = _RecordingConnection()
    store = MySQLShadowStore(connection_factory=_connection_factory(conn))

    store.persist_run(_run_record())

    inserts = [sql for sql in conn.executed_statements() if sql.startswith("INSERT INTO")]
    table_names = [
        sql.split("INTO ", 1)[1].split(chr(10), 1)[0].split(chr(40), 1)[0].strip().rstrip(",")
        for sql in inserts
    ]
    assert "asset_allocation_etf_adaptive_run" in table_names
    assert "asset_allocation_etf_adaptive_state" in table_names
    assert "asset_allocation_etf_adaptive_order_advice" in table_names
    assert conn.commits >= 1
    assert conn.rollbacks == 0


def test_persist_run_rolls_back_on_state_insert_failure() -> None:
    conn = _RecordingConnection()
    store = MySQLShadowStore(connection_factory=_connection_factory(conn))
    store.ensure_schema()
    conn.cursor_obj.program_failure(
        "simulated state insert failure", marker="asset_allocation_etf_adaptive_state",
    )

    try:
        store.persist_run(_run_record())
    except RuntimeError as exc:
        assert "simulated" in str(exc)
    else:
        raise AssertionError("expected RuntimeError from broken cursor")

    assert conn.rollbacks >= 1


def test_persist_run_rejects_different_config_hash_under_same_identity() -> None:
    conn = _RecordingConnection()
    conn.cursor_obj.set_results([("run-1", "cfg-other")])
    store = MySQLShadowStore(connection_factory=_connection_factory(conn))

    try:
        store.persist_run(_run_record())
    except ConfigConflictError as exc:
        assert "refusing to overwrite" in str(exc)
    else:
        raise AssertionError("expected ConfigConflictError")


def test_persist_run_rejects_run_id_mismatch_on_same_identity() -> None:
    conn = _RecordingConnection()
    conn.cursor_obj.set_results([("run-original", "cfg-a" * 16)])
    store = MySQLShadowStore(connection_factory=_connection_factory(conn))

    try:
        store.persist_run(_run_record(run_id="run-different"))
    except DuplicateRunError as exc:
        assert "byte-equivalent replay" in str(exc)
    else:
        raise AssertionError("expected DuplicateRunError")


def test_persist_run_is_idempotent_when_existing_matches() -> None:
    conn = _RecordingConnection()
    conn.cursor_obj.set_results([("run-1", "cfg-a" * 16)])
    store = MySQLShadowStore(connection_factory=_connection_factory(conn))

    result = store.persist_run(_run_record())

    assert result.run_id == "run-1"
    inserts = [sql for sql in conn.executed_statements() if sql.startswith("INSERT INTO")]
    assert not inserts


def test_record_fill_observation_inserts_into_observation_table() -> None:
    conn = _RecordingConnection()
    store = MySQLShadowStore(connection_factory=_connection_factory(conn))

    store.record_fill_observation(FillObservation(
        execution_eligible_date=date(2026, 9, 2),
        stock_code="510300.SH",
        config_hash="cfg-a" * 16,
        raw_open=1.0, raw_close=1.02,
        slippage_bps=2.0,
        fill_complete=True,
        notes="clean open",
    ))

    inserts = [sql for sql in conn.executed_statements() if sql.startswith("INSERT INTO")]
    assert any(
        "asset_allocation_etf_adaptive_fill_observation" in sql for sql in inserts
    )


def test_load_frozen_config_returns_none_when_missing() -> None:
    conn = _RecordingConnection()
    store = MySQLShadowStore(connection_factory=_connection_factory(conn))

    assert store.load_frozen_config("absent") is None
    creates = [sql for sql in conn.executed_statements() if sql.startswith("CREATE TABLE")]
    assert creates


def test_load_active_frozen_config_filters_by_window() -> None:
    conn = _RecordingConnection()
    conn.cursor_obj.set_results(
        [(AdaptiveConfig.default().config_hash(),
          """{"cost":{"commission_rate":0.0001,"minimum_commission":5.0,"slippage_bps":3.0},"grid":{"atr_stop_multiple":3.0,"cooldown_sessions":5,"fixed_initial_pct":0.5,"initial_model":"fixed","max_grid_per_day":1,"step_pct":0.02,"unit_pct":0.1},"trend":{"add_n":0.5,"amount_ratio_min":null,"max_units":4,"require_macd_bullish":true,"risk_per_unit":0.005,"stop_n":2.0}}""",
          "{}", date(2026, 6, 1), date(2026, 6, 1),
          date(2026, 12, 1), datetime(2026, 6, 1, 17, 0))],
    )
    store = MySQLShadowStore(connection_factory=_connection_factory(conn))

    record = store.load_active_frozen_config(date(2026, 8, 1))

    assert record is not None
    assert record.config_hash == AdaptiveConfig.default().config_hash()
    selects = [sql for sql in conn.executed_statements() if sql.startswith("SELECT")]
    assert any("activation_date" in sql and "review_date" in sql for sql in selects)


def test_load_active_frozen_config_restores_the_approved_nondefault_parameters() -> None:
    """Break caught: loading the default config silently changes approved shadow behavior."""
    config = AdaptiveConfig(
        grid=GridConfig(step_pct=0.035, unit_pct=0.15, atr_stop_multiple=2.0, cooldown_sessions=3),
        trend=TrendConfig(stop_n=2.5, risk_per_unit=0.0075, add_n=0.75, max_units=3,
                          require_macd_bullish=False, amount_ratio_min=1.2),
        cost=CostConfig(commission_rate=0.0002, minimum_commission=8.0, slippage_bps=4.0),
    )
    config_json = """{"cost":{"commission_rate":0.0002,"minimum_commission":8.0,"slippage_bps":4.0},"grid":{"atr_stop_multiple":2.0,"cooldown_sessions":3,"fixed_initial_pct":0.5,"initial_model":"fixed","max_grid_per_day":1,"step_pct":0.035,"unit_pct":0.15},"trend":{"add_n":0.75,"amount_ratio_min":1.2,"max_units":3,"require_macd_bullish":false,"risk_per_unit":0.0075,"stop_n":2.5}}"""
    conn = _RecordingConnection()
    conn.cursor_obj.set_results(
        [(config.config_hash(), config_json, "{}", date(2026, 6, 1), date(2026, 6, 1),
          date(2026, 12, 1), datetime(2026, 6, 1, 17, 0))],
    )
    store = MySQLShadowStore(connection_factory=_connection_factory(conn))

    record = store.load_active_frozen_config(date(2026, 8, 1))

    assert record is not None
    assert record.config == config


def test_iter_runs_yields_shadow_run_records_for_each_row() -> None:
    conn = _RecordingConnection()
    store = MySQLShadowStore(connection_factory=_connection_factory(conn))
    store.ensure_schema()
    conn.cursor_obj = _RecordingCursor()
    state_json = _serialize_strategy_state(_run_record().state.state)
    conn.cursor_obj.set_results(
        [
            ("run-1", date(2026, 9, 1), "510300.SH", "shadow-v1", "cfg-x", date(2026, 9, 2),
             state_json, Decimal("99000"), 100, "grid"),
            ("run-2", date(2026, 9, 1), "510500.SH", "shadow-v1", "cfg-x", date(2026, 9, 2),
             state_json, Decimal("99000"), 100, "grid"),
        ], [], [],
    )

    runs = list(store.iter_runs())

    assert [run.identity.stock_code for run in runs] == ["510300.SH", "510500.SH"]
    assert runs[0].run_id == "run-1"
    assert runs[0].state.state.position_shares == 100
    assert runs[0].state.cash == Decimal("99000")


def test_iter_runs_restores_advice_and_observations_for_continuity_verification() -> None:
    conn = _RecordingConnection()
    store = MySQLShadowStore(connection_factory=_connection_factory(conn))
    store.ensure_schema()
    conn.cursor_obj = _RecordingCursor()
    record = _run_record()
    conn.cursor_obj.set_results(
        [(record.run_id, record.identity.as_of_date, "510300.SH", "shadow-v1", record.config_hash,
          date(2026, 9, 2), _serialize_strategy_state(record.state.state), Decimal("99000"), 100, "grid")],
        [(record.run_id, "510300.SH", date(2026, 9, 1), date(2026, 9, 2), date(2026, 9, 1),
          "buy", "grid_buy", record.config_hash, Decimal("0.1"), Decimal("0.005"), "GRID unit", '[["grid_anchor", 1.0]]')],
        [(date(2026, 9, 2), "510300.SH", record.config_hash, Decimal("1.0"), Decimal("1.02"),
          Decimal("3.0"), 1, "observed")],
    )

    restored = tuple(store.iter_runs())[0]

    assert len(restored.advices) == len(restored.observations) == 1
    assert restored.advices[0].order.reason is OrderReason.GRID_BUY
    assert restored.advices[0].order.target_budget == 0.1
    assert restored.advices[0].execution_eligible_date == date(2026, 9, 2)
    assert restored.observations[0].raw_open == 1.0
    assert restored.observations[0].fill_complete is True




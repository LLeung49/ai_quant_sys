"""Transactional MySQL ``ShadowStore`` for production deployment.

This module bridges the ``ShadowStore`` protocol to the existing
``data_ingestion.db_config`` connection pool. The daily runner
persists all four tables (run / state / order_advice / health_check)
inside a single transaction so partial state is never observable.

The companion SQL schema lives in
``sql/20260902_create_etf_adaptive_shadow_tables.sql`` and is loaded
by :meth:`MySQLShadowStore.ensure_schema` on first use.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal
from pathlib import Path
from typing import Any, Iterable, Mapping, Optional, Sequence

from .config import AdaptiveConfig, CostConfig, GridConfig, TrendConfig
from .shadow_store import (
    AdviceRecord,
    ConfigConflictError,
    DuplicateRunError,
    FillObservation,
    FrozenConfigRecord,
    HealthCheck,
    ShadowRunIdentity,
    ShadowRunRecord,
    ShadowStore,
    StateRecord,
)
from .state import Decision, OrderIntent, OrderReason, Regime, Side, StrategyState, TrendUnit


SCHEMA_SQL_PATH: Path = Path(
    "D:/aiQuant/ai_quant_sys/sql/20260902_create_etf_adaptive_shadow_tables.sql",
)


@dataclass(frozen=True)
class _ConnectionFactory:
    """Wrapper that defers ``get_connection`` import to call time."""

    @staticmethod
    def build():
        from data_ingestion.db_config import get_connection
        return get_connection()


def _get_connection_factory() -> Any:
    return _ConnectionFactory.build()


def _serialize_strategy_state(state: StrategyState) -> str:
    payload = {
        "regime": state.regime.value if state.regime is not None else None,
        "pending_grid": state.pending_grid,
        "grid_anchor": state.grid_anchor,
        "cycle_entry_price": state.cycle_entry_price,
        "grid_stop_price": state.grid_stop_price,
        "trend_stop_price": state.trend_stop_price,
        "highest_close": state.highest_close,
        "cooldown_remaining": state.cooldown_remaining,
        "position_shares": state.position_shares,
        "cash": str(state.cash),
        "applied_action_ids": list(state.applied_action_ids),
        "units": [
            {
                "raw_fill_price": unit.raw_fill_price,
                "signal_fill_price": unit.signal_fill_price,
                "signal_atr20": unit.signal_atr20,
                "shares": unit.shares,
                "next_add_signal_price": unit.next_add_signal_price,
            }
            for unit in state.units
        ],
    }
    return json.dumps(payload, ensure_ascii=False, sort_keys=True)


def _deserialize_strategy_state(payload: str) -> StrategyState:
    data = json.loads(payload)
    units = tuple(
        TrendUnit(
            raw_fill_price=float(unit["raw_fill_price"]),
            signal_fill_price=float(unit["signal_fill_price"]),
            signal_atr20=(
                float(unit["signal_atr20"])
                if unit.get("signal_atr20") is not None
                else None
            ),
            shares=int(unit["shares"]),
            next_add_signal_price=float(unit["next_add_signal_price"]),
        )
        for unit in data.get("units", [])
    )
    return StrategyState(
        regime=Regime(data["regime"]) if data.get("regime") else None,
        pending_grid=bool(data.get("pending_grid", False)),
        grid_anchor=data.get("grid_anchor"),
        cycle_entry_price=data.get("cycle_entry_price"),
        grid_stop_price=data.get("grid_stop_price"),
        trend_stop_price=data.get("trend_stop_price"),
        highest_close=data.get("highest_close"),
        cooldown_remaining=int(data.get("cooldown_remaining", 0)),
        position_shares=int(data.get("position_shares", 0)),
        cash=Decimal(data["cash"]),
        applied_action_ids=tuple(data.get("applied_action_ids", ())),
        units=units,
    )


def _serialize_adaptive_config(config: AdaptiveConfig) -> str:
    return json.dumps(
        {
            "grid": {
                "step_pct": config.grid.step_pct,
                "unit_pct": config.grid.unit_pct,
                "initial_model": config.grid.initial_model,
                "fixed_initial_pct": config.grid.fixed_initial_pct,
                "max_grid_per_day": config.grid.max_grid_per_day,
                "atr_stop_multiple": config.grid.atr_stop_multiple,
                "cooldown_sessions": config.grid.cooldown_sessions,
            },
            "trend": {
                "stop_n": config.trend.stop_n,
                "risk_per_unit": config.trend.risk_per_unit,
                "add_n": config.trend.add_n,
                "max_units": config.trend.max_units,
                "require_macd_bullish": config.trend.require_macd_bullish,
                "amount_ratio_min": config.trend.amount_ratio_min,
            },
            "cost": {
                "commission_rate": config.cost.commission_rate,
                "minimum_commission": config.cost.minimum_commission,
                "slippage_bps": config.cost.slippage_bps,
                "sell_tax_rate": config.cost.sell_tax_rate,
                "transfer_fee_rate": config.cost.transfer_fee_rate,
            },
        },
        ensure_ascii=False,
        sort_keys=True,
    )


def _deserialize_adaptive_config(payload: str) -> AdaptiveConfig:
    """Restore the immutable approval snapshot and reject a mismatched identity."""
    try:
        data = json.loads(payload)
        config = AdaptiveConfig(
            grid=GridConfig(**data["grid"]),
            trend=TrendConfig(**data["trend"]),
            cost=CostConfig(**data["cost"]),
        )
    except (TypeError, KeyError, ValueError, json.JSONDecodeError) as exc:
        raise ValueError("invalid frozen adaptive configuration") from exc
    return config


def _serialize_mapping(mapping: Mapping[str, Any]) -> str:
    return json.dumps(dict(mapping), ensure_ascii=False, sort_keys=True, default=str)


def _deserialize_frozen_record(row) -> FrozenConfigRecord:
    config = _deserialize_adaptive_config(row[1])
    payload = json.loads(row[2]) if row[2] else {}
    if not isinstance(payload, dict):
        raise ValueError("invalid frozen selection payload")
    if "selection_hash" in payload or "selection_manifest" in payload:
        from .frozen_selection import FrozenSelection, _activation_payload

        selection = FrozenSelection.from_payload(payload.get("selection_manifest"))
        if (
            row[0] != selection.config_hash
            or payload.get("selection_hash") != selection.config_hash
            or payload.get("declared_config_hash") != config.config_hash()
            or selection.base_config != config
            or payload != _activation_payload(selection)
            or (row[3], row[4], row[5]) != (
                selection.data_cutoff, selection.activation_date, selection.review_date,
            )
        ):
            raise ValueError("frozen selection or config identity does not match recorded evidence")
    elif config.config_hash() != row[0]:
        # Historical parameter-only records used the column as a parameter hash.
        raise ValueError("frozen config hash does not match config_json")
    return FrozenConfigRecord(
        config_hash=row[0], config=config, selection_payload=payload,
        data_cutoff=row[3], activation_date=row[4], review_date=row[5], activated_at=row[6],
    )


class MySQLShadowStore:
    """Transactional MySQL implementation of the ``ShadowStore`` protocol.

    All write operations on the daily run path use a single connection
    with a single transaction. Read operations open their own
    short-lived connection via ``data_ingestion.db_config.get_connection``.
    """

    def __init__(
        self,
        *,
        schema_path: Path | None = None,
        connection_factory: Any | None = None,
    ) -> None:
        self._schema_path = Path(schema_path) if schema_path else SCHEMA_SQL_PATH
        self._connection_factory = connection_factory or _get_connection_factory
        self._schema_ensured = False

    def ensure_schema(self) -> None:
        if self._schema_ensured:
            return
        sql_text = self._schema_path.read_text(encoding="utf-8")
        statements = _split_sql_statements(sql_text)
        conn = self._connection_factory()
        try:
            cursor = conn.cursor()
            try:
                for statement in statements:
                    if statement.strip():
                        cursor.execute(statement)
                conn.commit()
            finally:
                cursor.close()
        finally:
            self._close_connection(conn)
        self._schema_ensured = True

    def activate_frozen_config(self, record: FrozenConfigRecord) -> None:
        if not record.config_hash:
            raise ValueError("config_hash must be a non-empty SHA-256 hex string")
        self.ensure_schema()
        conn = self._connection_factory()
        try:
            cursor = conn.cursor()
            try:
                cursor.execute(
                    """
                    INSERT INTO asset_allocation_etf_adaptive_frozen_config
                        (config_hash, config_json, selection_json, data_cutoff,
                         activation_date, review_date, activated_at)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    ON DUPLICATE KEY UPDATE
                        config_json = VALUES(config_json),
                        selection_json = VALUES(selection_json),
                        data_cutoff = VALUES(data_cutoff),
                        activation_date = VALUES(activation_date),
                        review_date = VALUES(review_date),
                        activated_at = VALUES(activated_at)
                    """,
                    (
                        record.config_hash,
                        _serialize_adaptive_config(record.config),
                        _serialize_mapping(record.selection_payload),
                        record.data_cutoff,
                        record.activation_date,
                        record.review_date,
                        record.activated_at,
                    ),
                )
                conn.commit()
            finally:
                cursor.close()
        finally:
            self._close_connection(conn)

    def load_frozen_config(self, config_hash: str) -> FrozenConfigRecord | None:
        self.ensure_schema()
        conn = self._connection_factory()
        try:
            cursor = conn.cursor()
            try:
                cursor.execute(
                    """
                    SELECT config_hash, config_json, selection_json, data_cutoff,
                           activation_date, review_date, activated_at
                    FROM asset_allocation_etf_adaptive_frozen_config
                    WHERE config_hash = %s
                    """,
                    (config_hash,),
                )
                row = cursor.fetchone()
                if not row:
                    return None
                return _deserialize_frozen_record(row)
            finally:
                cursor.close()
        finally:
            self._close_connection(conn)

    def load_active_frozen_config(self, on_date: date) -> FrozenConfigRecord | None:
        self.ensure_schema()
        conn = self._connection_factory()
        try:
            cursor = conn.cursor()
            try:
                cursor.execute(
                    """
                    SELECT config_hash, config_json, selection_json, data_cutoff,
                           activation_date, review_date, activated_at
                    FROM asset_allocation_etf_adaptive_frozen_config
                    WHERE activation_date <= %s AND review_date >= %s
                    ORDER BY activated_at DESC
                    LIMIT 1
                    """,
                    (on_date, on_date),
                )
                row = cursor.fetchone()
                if not row:
                    return None
                return _deserialize_frozen_record(row)
            finally:
                cursor.close()
        finally:
            self._close_connection(conn)

    def load_latest_state(
        self, stock_code: str, config_hash: str,
    ) -> tuple[ShadowRunRecord, StateRecord] | None:
        self.ensure_schema()
        conn = self._connection_factory()
        try:
            cursor = conn.cursor()
            try:
                cursor.execute(
                    """
                    SELECT s.run_id, s.as_of_date, s.stock_code, s.config_hash,
                           s.state_json, s.cash, s.position_shares, s.regime,
                           r.model_version, r.execution_eligible_date
                    FROM asset_allocation_etf_adaptive_state s
                    JOIN asset_allocation_etf_adaptive_run r
                      ON r.run_id = s.run_id
                    WHERE s.stock_code = %s AND s.config_hash = %s
                    ORDER BY s.as_of_date DESC
                    LIMIT 1
                    """,
                    (stock_code, config_hash),
                )
                row = cursor.fetchone()
                if not row:
                    return None
                state = _deserialize_strategy_state(row[4])
                record = StateRecord(
                    run_id=row[0],
                    as_of_date=row[1],
                    stock_code=row[2],
                    config_hash=row[3],
                    state=state,
                    cash=row[5],
                    position_shares=row[6],
                    regime=row[7],
                )
                run_record = ShadowRunRecord(
                    run_id=row[0],
                    identity=ShadowRunIdentity(
                        as_of_date=row[1],
                        model_version=row[8],
                        stock_code=row[2],
                    ),
                    config_hash=row[3],
                    execution_eligible_date=row[9],
                    state=record,
                    advices=(),
                )
                return run_record, record
            finally:
                cursor.close()
        finally:
            self._close_connection(conn)

    def persist_run(self, run: ShadowRunRecord) -> ShadowRunRecord:
        self.ensure_schema()
        conn = self._connection_factory()
        try:
            cursor = conn.cursor()
            try:
                cursor.execute(
                    """
                    SELECT run_id, config_hash FROM asset_allocation_etf_adaptive_run
                    WHERE as_of_date = %s AND model_version = %s AND stock_code = %s
                    """,
                    (
                        run.identity.as_of_date,
                        run.identity.model_version,
                        run.identity.stock_code,
                    ),
                )
                existing = cursor.fetchone()
                if existing is not None:
                    existing_run_id, existing_config_hash = existing
                    if existing_config_hash != run.config_hash:
                        raise ConfigConflictError(
                            f"identity {run.identity} already stored under "
                            f"config_hash={existing_config_hash!r}; refusing to overwrite "
                            f"with config_hash={run.config_hash!r}"
                        )
                    if existing_run_id != run.run_id:
                        raise DuplicateRunError(
                            f"identity {run.identity} already completed as run_id="
                            f"{existing_run_id!r}; re-running requires the same run_id "
                            f"for byte-equivalent replay"
                        )
                    conn.commit()
                    return run

                cursor.execute(
                    """
                    INSERT INTO asset_allocation_etf_adaptive_run
                        (as_of_date, stock_code, model_version, config_hash,
                         run_id, execution_eligible_date, status)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """,
                    (
                        run.identity.as_of_date,
                        run.identity.stock_code,
                        run.identity.model_version,
                        run.config_hash,
                        run.run_id,
                        run.execution_eligible_date,
                        "succeeded",
                    ),
                )
                cursor.execute(
                    """
                    INSERT INTO asset_allocation_etf_adaptive_state
                        (run_id, stock_code, as_of_date, config_hash,
                         state_json, cash, position_shares, regime)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    ON DUPLICATE KEY UPDATE
                        state_json = VALUES(state_json),
                        cash = VALUES(cash),
                        position_shares = VALUES(position_shares),
                        regime = VALUES(regime)
                    """,
                    (
                        run.run_id,
                        run.identity.stock_code,
                        run.identity.as_of_date,
                        run.config_hash,
                        _serialize_strategy_state(run.state.state),
                        run.state.cash,
                        run.state.position_shares,
                        run.state.regime,
                    ),
                )
                for advice in run.advices:
                    cursor.execute(
                        """
                        INSERT INTO asset_allocation_etf_adaptive_order_advice
                            (run_id, stock_code, as_of_date, execution_eligible_date,
                             signal_date, side, reason, config_hash, target_budget,
                             risk_per_unit, quantity_rationale, signal_thresholds_json)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        """,
                        (
                            advice.run_id,
                            advice.stock_code,
                            advice.as_of_date,
                            advice.execution_eligible_date,
                            advice.signal_date,
                            advice.order.side.value,
                            advice.order.reason.value,
                            advice.config_hash,
                            advice.order.target_budget,
                            advice.order.risk_per_unit,
                            advice.order.quantity_rationale,
                            json.dumps(
                                [list(item) for item in advice.order.signal_thresholds],
                                ensure_ascii=False,
                            ),
                        ),
                    )
                for health in run.health_checks:
                    cursor.execute(
                        """
                        INSERT INTO asset_allocation_etf_adaptive_health_check
                            (run_id, check_name, passed, detail_json)
                        VALUES (%s, %s, %s, %s)
                        """,
                        (
                            health.run_id,
                            health.check_name,
                            1 if health.passed else 0,
                            json.dumps(dict(health.detail), ensure_ascii=False, default=str),
                        ),
                    )
                conn.commit()
            except Exception:
                conn.rollback()
                raise
            finally:
                cursor.close()
        finally:
            self._close_connection(conn)
        return run

    def record_fill_observation(self, observation: FillObservation) -> None:
        self.ensure_schema()
        conn = self._connection_factory()
        try:
            cursor = conn.cursor()
            try:
                cursor.execute(
                    """
                    INSERT INTO asset_allocation_etf_adaptive_fill_observation
                        (execution_eligible_date, stock_code, config_hash,
                         raw_open, raw_close, slippage_bps, fill_complete, notes)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    """,
                    (
                        observation.execution_eligible_date,
                        observation.stock_code,
                        observation.config_hash,
                        observation.raw_open,
                        observation.raw_close,
                        observation.slippage_bps,
                        1 if observation.fill_complete else 0,
                        observation.notes,
                    ),
                )
                conn.commit()
            finally:
                cursor.close()
        finally:
            self._close_connection(conn)

    def iter_runs(self) -> Iterable[ShadowRunRecord]:
        self.ensure_schema()
        conn = self._connection_factory()
        try:
            cursor = conn.cursor()
            try:
                cursor.execute(
                    """
                    SELECT r.run_id, r.as_of_date, r.stock_code, r.model_version,
                           r.config_hash, r.execution_eligible_date,
                           s.state_json, s.cash, s.position_shares, s.regime
                    FROM asset_allocation_etf_adaptive_run r
                    JOIN asset_allocation_etf_adaptive_state s ON s.run_id = r.run_id
                    ORDER BY r.as_of_date, r.stock_code
                    """
                )
                rows = cursor.fetchall()
                cursor.execute(
                    """
                    SELECT run_id, stock_code, as_of_date, execution_eligible_date,
                           signal_date, side, reason, config_hash, target_budget,
                           risk_per_unit, quantity_rationale, signal_thresholds_json
                    FROM asset_allocation_etf_adaptive_order_advice
                    ORDER BY as_of_date, id
                    """
                )
                advice_rows = cursor.fetchall()
                cursor.execute(
                    """
                    SELECT execution_eligible_date, stock_code, config_hash,
                           raw_open, raw_close, slippage_bps, fill_complete, notes
                    FROM asset_allocation_etf_adaptive_fill_observation
                    ORDER BY execution_eligible_date, id
                    """
                )
                observation_rows = cursor.fetchall()
            finally:
                cursor.close()
        finally:
            self._close_connection(conn)
        advices_by_run: dict[str, list[AdviceRecord]] = {}
        for row in advice_rows:
            (run_id, stock_code, as_of_date, eligible_date, signal_date, side, reason,
             config_hash, budget, risk, rationale, thresholds) = row
            advice = AdviceRecord(
                run_id=run_id, stock_code=stock_code, as_of_date=as_of_date,
                execution_eligible_date=eligible_date, signal_date=signal_date,
                config_hash=config_hash,
                order=OrderIntent(
                    signal_date=signal_date, side=Side(side), reason=OrderReason(reason),
                    # The existing SQL model does not persist ATR. Continuity
                    # must not reconstruct ATR-dependent quantities from defaults.
                    signal_atr20=None,
                    signal_thresholds=tuple((name, float(value)) for name, value in json.loads(thresholds)),
                    target_budget=float(budget), risk_per_unit=float(risk), quantity_rationale=rationale,
                ),
            )
            advices_by_run.setdefault(run_id, []).append(advice)
        observations_by_key: dict[tuple, list[FillObservation]] = {}
        for row in observation_rows:
            observation = FillObservation(
                execution_eligible_date=row[0], stock_code=row[1], config_hash=row[2],
                raw_open=float(row[3]) if row[3] is not None else None,
                raw_close=float(row[4]) if row[4] is not None else None,
                slippage_bps=float(row[5]) if row[5] is not None else None,
                fill_complete=bool(row[6]), notes=row[7],
            )
            observations_by_key.setdefault((row[0], row[1], row[2]), []).append(observation)
        for row in rows:
            (run_id, as_of_date, stock_code, model_version, config_hash, execution_eligible_date,
             state_json, cash, position_shares, regime) = row
            state = _deserialize_strategy_state(state_json)
            yield ShadowRunRecord(
                run_id=run_id,
                identity=ShadowRunIdentity(
                    as_of_date=as_of_date,
                    model_version=model_version,
                    stock_code=stock_code,
                ),
                config_hash=config_hash,
                execution_eligible_date=execution_eligible_date,
                state=StateRecord(
                    run_id=run_id,
                    as_of_date=as_of_date,
                    stock_code=stock_code,
                    config_hash=config_hash,
                    state=state,
                    cash=cash,
                    position_shares=position_shares,
                    regime=regime,
                ),
                advices=tuple(advices_by_run.get(run_id, ())),
                observations=tuple(observations_by_key.get(
                    (execution_eligible_date, stock_code, config_hash), (),
                )),
            )

    @staticmethod
    def _close_connection(conn: Any) -> None:
        close = getattr(conn, "close", None)
        if callable(close):
            close()


def _split_sql_statements(text: str) -> list[str]:
    """Split a SQL script on top-level ``;`` boundaries while preserving comments."""

    cleaned_lines: list[str] = []
    for line in text.splitlines():
        stripped = line.lstrip("\ufeff").strip()
        if stripped.startswith("--") or not stripped:
            continue
        cleaned_lines.append(line)
    statements: list[str] = []
    buffer: list[str] = []
    cleaned = chr(10).join(cleaned_lines)
    for char in cleaned:
        buffer.append(char)
        if char == ";":
            statements.append("".join(buffer).strip().rstrip(";"))
            buffer = []
    if buffer and any(part.strip() for part in buffer):
        statements.append("".join(buffer).strip())
    return [stmt for stmt in statements if stmt.strip()]


__all__ = [
    "MySQLShadowStore",
    "SCHEMA_SQL_PATH",
    "_deserialize_adaptive_config",
    "_deserialize_strategy_state",
    "_serialize_adaptive_config",
    "_serialize_strategy_state",
    "_split_sql_statements",
]


# Silence unused import warning while keeping the dependency obvious for tests.
_ = (Decision, OrderIntent, OrderReason, Side)





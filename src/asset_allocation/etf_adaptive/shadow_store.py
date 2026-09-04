"""Append-only shadow store for the adaptive ETF daily runner.

The shadow runner never imports a broker or order API. Its only
side-effect is writing immutable records to a transactional repository:

* one ``frozen_config`` row per accepted research activation
* one ``run`` row per ``(as_of_date, model_version, config_hash, stock_code)``
* one ``state`` row that reflects the post-close ``StrategyState``
* one ``order_advice`` row per emitted T+1 advisory intent
* zero or more ``fill_observation`` rows recording next-open reality
* zero or more ``health_check`` rows recording the daily preflight

The identity tuple ``(as_of_date, model_version, stock_code)`` is unique
within the store. Re-running the same identity with the same
``config_hash`` and ``run_id`` is idempotent; a different ``config_hash``
under the same identity raises ``ConfigConflictError`` so an accidental
config drift can never overwrite an archived run.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from decimal import Decimal
from typing import Iterable, Mapping, Protocol, Sequence

from .config import AdaptiveConfig
from .state import OrderIntent, StrategyState


class ShadowStoreError(Exception):
    """Base class for shadow-store contract violations."""


class ConfigConflictError(ShadowStoreError):
    """Raised when a run attempts to overwrite a stored run with a different config_hash."""


class DuplicateRunError(ShadowStoreError):
    """Raised when a run is already completed and cannot be re-persisted as a new run."""


@dataclass(frozen=True)
class ShadowRunIdentity:
    """Composite identity used for idempotent persistence (no config_hash)."""

    as_of_date: date
    model_version: str
    stock_code: str


@dataclass(frozen=True)
class FrozenConfigRecord:
    config_hash: str
    config: AdaptiveConfig
    selection_payload: Mapping[str, object]
    data_cutoff: date
    activation_date: date
    review_date: date
    activated_at: datetime


@dataclass(frozen=True)
class StateRecord:
    run_id: str
    as_of_date: date
    stock_code: str
    config_hash: str
    state: StrategyState
    cash: Decimal
    position_shares: int
    regime: str | None


@dataclass(frozen=True)
class AdviceRecord:
    run_id: str
    stock_code: str
    as_of_date: date
    execution_eligible_date: date
    signal_date: date
    order: OrderIntent
    config_hash: str


@dataclass(frozen=True)
class FillObservation:
    execution_eligible_date: date
    stock_code: str
    config_hash: str
    raw_open: float | None
    raw_close: float | None
    slippage_bps: float | None
    fill_complete: bool
    notes: str | None


@dataclass(frozen=True)
class HealthCheck:
    run_id: str
    check_name: str
    passed: bool
    detail: Mapping[str, object] = field(default_factory=dict)


@dataclass(frozen=True)
class ShadowRunRecord:
    """All artifacts associated with one shadow run for one stock."""

    run_id: str
    identity: ShadowRunIdentity
    config_hash: str
    execution_eligible_date: date
    state: StateRecord
    advices: tuple[AdviceRecord, ...]
    observations: tuple[FillObservation, ...] = ()
    health_checks: tuple[HealthCheck, ...] = ()


class ShadowStore(Protocol):
    """Persistence contract implemented by every shadow store backend."""

    def ensure_schema(self) -> None: ...

    def activate_frozen_config(self, record: FrozenConfigRecord) -> None: ...

    def load_frozen_config(self, config_hash: str) -> FrozenConfigRecord | None: ...

    def load_active_frozen_config(self, on_date: date) -> FrozenConfigRecord | None: ...

    def load_latest_state(
        self, stock_code: str, config_hash: str,
    ) -> tuple[ShadowRunRecord, StateRecord] | None: ...

    def persist_run(self, run: ShadowRunRecord) -> ShadowRunRecord: ...

    def record_fill_observation(self, observation: FillObservation) -> None: ...

    def iter_runs(self) -> Iterable[ShadowRunRecord]: ...


def build_run_record(
    *,
    run_id: str,
    identity: ShadowRunIdentity,
    config_hash: str,
    execution_eligible_date: date,
    state: StrategyState,
    orders: Sequence[OrderIntent],
) -> ShadowRunRecord:
    """Construct a fully populated ``ShadowRunRecord`` from inputs."""

    state_record = StateRecord(
        run_id=run_id,
        as_of_date=identity.as_of_date,
        stock_code=identity.stock_code,
        config_hash=config_hash,
        state=state,
        cash=state.cash,
        position_shares=state.position_shares,
        regime=state.regime.value if state.regime is not None else None,
    )
    advices = tuple(
        AdviceRecord(
            run_id=run_id,
            stock_code=identity.stock_code,
            as_of_date=identity.as_of_date,
            execution_eligible_date=execution_eligible_date,
            signal_date=order.signal_date,
            order=order,
            config_hash=config_hash,
        )
        for order in orders
    )
    return ShadowRunRecord(
        run_id=run_id,
        identity=identity,
        config_hash=config_hash,
        execution_eligible_date=execution_eligible_date,
        state=state_record,
        advices=advices,
    )


class InMemoryShadowStore:
    """In-memory ``ShadowStore`` used for unit tests and dry-runs."""

    def __init__(self) -> None:
        self._frozen: dict[str, FrozenConfigRecord] = {}
        self._runs: dict[ShadowRunIdentity, ShadowRunRecord] = {}
        self._fills: list[FillObservation] = []

    @property
    def run_count(self) -> int:
        return len(self._runs)

    @property
    def frozen_config_count(self) -> int:
        return len(self._frozen)

    def ensure_schema(self) -> None:
        return None

    def activate_frozen_config(self, record: FrozenConfigRecord) -> None:
        if not record.config_hash:
            raise ValueError("config_hash must be a non-empty SHA-256 hex string")
        self._frozen[record.config_hash] = record

    def load_frozen_config(self, config_hash: str) -> FrozenConfigRecord | None:
        return self._frozen.get(config_hash)

    def load_active_frozen_config(self, on_date: date) -> FrozenConfigRecord | None:
        candidates = [
            record for record in self._frozen.values()
            if record.activation_date <= on_date <= record.review_date
        ]
        if not candidates:
            return None
        candidates.sort(key=lambda record: record.activated_at, reverse=True)
        return candidates[0]

    def load_latest_state(
        self, stock_code: str, config_hash: str,
    ) -> tuple[ShadowRunRecord, StateRecord] | None:
        candidates = sorted(
            (
                run for run in self._runs.values()
                if run.identity.stock_code == stock_code
                and run.config_hash == config_hash
            ),
            key=lambda run: run.identity.as_of_date,
        )
        if not candidates:
            return None
        latest = candidates[-1]
        return latest, latest.state

    def persist_run(self, run: ShadowRunRecord) -> ShadowRunRecord:
        existing = self._runs.get(run.identity)
        if existing is not None:
            if existing.config_hash != run.config_hash:
                raise ConfigConflictError(
                    f"identity {run.identity} already stored under "
                    f"config_hash={existing.config_hash!r}; refusing to overwrite "
                    f"with config_hash={run.config_hash!r}"
                )
            if existing.run_id != run.run_id:
                raise DuplicateRunError(
                    f"identity {run.identity} already completed as run_id="
                    f"{existing.run_id!r}; re-running requires the same run_id "
                    f"for byte-equivalent replay"
                )
            return existing
        self._runs[run.identity] = run
        return run

    def record_fill_observation(self, observation: FillObservation) -> None:
        self._fills.append(observation)

    def iter_runs(self) -> Iterable[ShadowRunRecord]:
        return tuple(self._runs.values())

    @property
    def fill_observations(self) -> tuple[FillObservation, ...]:
        return tuple(self._fills)


__all__ = [
    "AdviceRecord",
    "ConfigConflictError",
    "DuplicateRunError",
    "FillObservation",
    "FrozenConfigRecord",
    "HealthCheck",
    "InMemoryShadowStore",
    "ShadowRunIdentity",
    "ShadowRunRecord",
    "ShadowStore",
    "ShadowStoreError",
    "StateRecord",
    "build_run_record",
]

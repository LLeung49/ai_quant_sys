"""Frozen research selections bound to a six-month review cycle.

A ``FrozenSelection`` is the operator-approved slice of a research run
that the daily shadow runner consumes. It captures the exact
``config_hash`` and target weights, the research data cutoff, and the
activation/review dates that govern the six-month production cycle.

The selection is immutable and self-validating: loading it from a
research ``manifest.json`` recomputes the canonical hash from the
payload and refuses to materialise when the recomputed hash disagrees
with the manifest's declared ``config_hash``.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import date, datetime
from decimal import Decimal
from hashlib import sha256
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from .config import AdaptiveConfig
from .contracts import InstrumentType, SubLayer, asset_layer_for
from .shadow_store import FrozenConfigRecord, ShadowStore


SIX_MONTH_REVIEW_DAYS: int = 183


class FrozenSelectionError(ValueError):
    """Base class for frozen-selection validation failures."""


@dataclass(frozen=True)
class FrozenTarget:
    """One immutable, fully funded target in an approved sub-layer."""

    stock_code: str
    tracking_index_code: str
    layer: str
    sub_layer: SubLayer
    sub_layer_budget: Decimal
    instrument_type: InstrumentType
    weight: Decimal
    config_hash: str

    def __post_init__(self) -> None:
        if not self.stock_code:
            raise FrozenSelectionError("target stock_code must be non-empty")
        if not isinstance(self.sub_layer, SubLayer):
            raise FrozenSelectionError("target sub_layer must be an approved SubLayer")
        if self.layer != asset_layer_for(self.sub_layer).value:
            raise FrozenSelectionError(
                f"target {self.stock_code} layer does not match sub_layer {self.sub_layer.value}"
            )
        if not isinstance(self.sub_layer_budget, Decimal) or not self.sub_layer_budget.is_finite() or self.sub_layer_budget <= 0:
            raise FrozenSelectionError("target sub_layer_budget must be a positive finite Decimal")
        if not isinstance(self.instrument_type, InstrumentType):
            raise FrozenSelectionError("target instrument_type must be an InstrumentType")
        if not isinstance(self.weight, Decimal) or not self.weight.is_finite() or self.weight <= 0:
            raise FrozenSelectionError("target weight must be a positive finite Decimal")
        if not self.config_hash:
            raise FrozenSelectionError("target config_hash must be non-empty")


@dataclass(frozen=True)
class FrozenSelection:
    """Operator-approved research slice consumed by the daily shadow runner."""

    selection_id: str
    config_hash: str
    targets: tuple[FrozenTarget, ...]
    layer_weights: Mapping[str, float]
    data_cutoff: date
    activation_date: date
    review_date: date
    base_config: AdaptiveConfig
    selection_payload: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        _validate_targets(self.targets)
        _validate_review_window(self.activation_date, self.review_date)
        _validate_sub_layer_portfolio(self.targets)
        if not self.config_hash:
            raise FrozenSelectionError("config_hash must be a non-empty SHA-256 hex string")
        if not self.selection_id:
            raise FrozenSelectionError("selection_id must be a non-empty string")

    @property
    def review_window_days(self) -> int:
        return (self.review_date - self.activation_date).days

    def validate_activation(self, on_date: date) -> None:
        """Raise when ``on_date`` is outside the active review window."""

        if on_date < self.activation_date:
            raise FrozenSelectionError(
                f"activation date {self.activation_date.isoformat()} is in the future "
                f"relative to {on_date.isoformat()}"
            )
        if on_date > self.review_date:
            raise FrozenSelectionError(
                f"review date {self.review_date.isoformat()} has passed; "
                f"on {on_date.isoformat()} a new selection is required"
            )

    @classmethod
    def from_payload(cls, payload: Mapping[str, Any]) -> "FrozenSelection":
        """Build a ``FrozenSelection`` from a JSON-safe research manifest payload."""

        if not isinstance(payload, Mapping):
            raise FrozenSelectionError("manifest payload must be a mapping")
        manifest_hash = payload.get("config_hash")
        if not isinstance(manifest_hash, str) or not manifest_hash:
            raise FrozenSelectionError("manifest payload missing config_hash")
        expected_hash = _canonical_hash(payload)
        if expected_hash != manifest_hash:
            raise FrozenSelectionError(
                "manifest config hash mismatch: declared "
                f"{manifest_hash!r}, recomputed {expected_hash!r}"
            )
        targets = _parse_targets(payload, manifest_hash)
        layer_weights = {
            str(layer): float(weight)
            for layer, weight in payload.get("layer_weights", {}).items()
        }
        base_config = AdaptiveConfig.default()
        try:
            declared_hash = str(payload.get("declared_config_hash") or "")
        except (KeyError, TypeError):
            declared_hash = ""
        if declared_hash:
            base_config = _rebuild_config(payload)
        _validate_configured_sub_layer_budgets(payload, targets)
        return cls(
            selection_id=str(payload["selection_id"]),
            config_hash=manifest_hash,
            targets=targets,
            layer_weights=layer_weights,
            data_cutoff=_parse_date(payload["data_cutoff"]),
            activation_date=_parse_date(payload["activation_date"]),
            review_date=_parse_date(payload["review_date"]),
            base_config=base_config,
            selection_payload=dict(payload),
        )

    @classmethod
    def from_research_manifest(cls, path: Path) -> "FrozenSelection":
        """Load a frozen selection from a research run's ``manifest.json``."""

        manifest = json.loads(Path(path).read_text(encoding="utf-8"))
        payload = manifest.get("frozen_selection", manifest)
        if not isinstance(payload, Mapping):
            raise FrozenSelectionError("research manifest missing frozen_selection payload")
        return cls.from_payload(payload)


def _rebuild_config(payload: Mapping[str, Any]) -> AdaptiveConfig:
    declared_hash = payload.get("declared_config_hash")
    if not declared_hash:
        return AdaptiveConfig.default()
    return AdaptiveConfig.default()


def _validate_targets(targets: Sequence[FrozenTarget]) -> None:
    seen: set[str] = set()
    for target in targets:
        if target.stock_code in seen:
            raise FrozenSelectionError(f"duplicate stock_code in frozen selection: {target.stock_code}")
        seen.add(target.stock_code)


def _validate_review_window(activation_date: date, review_date: date) -> None:
    window = (review_date - activation_date).days
    if window <= 0:
        raise FrozenSelectionError(
            f"review_date {review_date.isoformat()} must be after activation_date "
            f"{activation_date.isoformat()}"
        )
    if window != SIX_MONTH_REVIEW_DAYS:
        raise FrozenSelectionError(
            f"review window is {window} days, expected exactly "
            f"{SIX_MONTH_REVIEW_DAYS} for the six-month review cycle"
        )


def _parse_targets(payload: Mapping[str, Any], config_hash: str) -> tuple[FrozenTarget, ...]:
    """Parse only unambiguous target records with explicit sub-layer funding."""

    raw_targets = payload.get("targets", ())
    if not isinstance(raw_targets, Sequence) or isinstance(raw_targets, (str, bytes)):
        raise FrozenSelectionError("targets must be a sequence")
    parsed: list[FrozenTarget] = []
    for raw in raw_targets:
        if not isinstance(raw, Mapping):
            raise FrozenSelectionError("target entries must be mappings")
        missing = {
            "sub_layer", "sub_layer_budget", "instrument_type", "weight", "stock_code"
        }.difference(raw)
        if missing:
            raise FrozenSelectionError(
                "legacy target payload is ambiguous; missing " + ", ".join(sorted(missing))
            )
        try:
            sub_layer = SubLayer(str(raw["sub_layer"]))
            instrument_type = InstrumentType(str(raw["instrument_type"]))
            budget = _as_decimal(raw["sub_layer_budget"], "sub_layer_budget")
            weight = _as_decimal(raw["weight"], "weight")
        except (ValueError, TypeError, ArithmeticError) as exc:
            raise FrozenSelectionError(f"invalid frozen target: {exc}") from exc
        target_hash = str(raw.get("config_hash", config_hash))
        if target_hash != config_hash:
            raise FrozenSelectionError("target config_hash must equal manifest config_hash")
        expected_layer = asset_layer_for(sub_layer).value
        declared_layer = str(raw.get("layer", expected_layer))
        parsed.append(FrozenTarget(
            stock_code=str(raw["stock_code"]),
            tracking_index_code=str(raw.get("tracking_index_code", "")),
            layer=declared_layer,
            sub_layer=sub_layer,
            sub_layer_budget=budget,
            instrument_type=instrument_type,
            weight=weight,
            config_hash=config_hash,
        ))
    return tuple(parsed)


def _as_decimal(value: Any, field_name: str) -> Decimal:
    if isinstance(value, bool):
        raise ValueError(f"{field_name} must be a decimal number")
    decimal = Decimal(str(value))
    if not decimal.is_finite():
        raise ValueError(f"{field_name} must be finite")
    return decimal


def _validate_sub_layer_portfolio(targets: Sequence[FrozenTarget]) -> None:
    grouped: dict[SubLayer, list[FrozenTarget]] = {}
    for target in targets:
        grouped.setdefault(target.sub_layer, []).append(target)
    if not grouped:
        raise FrozenSelectionError("frozen selection requires at least one funded sub-layer")
    for sub_layer, members in grouped.items():
        budgets = {member.sub_layer_budget for member in members}
        if len(budgets) != 1:
            raise FrozenSelectionError(
                f"sub-layer {sub_layer.value!r} targets must share one account-currency budget"
            )
        # Decimal values are parsed directly from the manifest; exact equality avoids
        # binary-float drift and deliberately leaves no generic target-count or cap rule.
        if sum((member.weight for member in members), Decimal("0")) != Decimal("1"):
            raise FrozenSelectionError(
                f"sub-layer {sub_layer.value!r} target weights must sum exactly to 1"
            )


def _validate_configured_sub_layer_budgets(
    payload: Mapping[str, Any], targets: Sequence[FrozenTarget],
) -> None:
    raw_budgets = payload.get("sub_layer_budgets")
    if raw_budgets is None:
        return
    if not isinstance(raw_budgets, Mapping):
        raise FrozenSelectionError("sub_layer_budgets must be a mapping")
    configured: dict[SubLayer, Decimal] = {}
    for raw_layer, raw_budget in raw_budgets.items():
        try:
            configured[SubLayer(str(raw_layer))] = _as_decimal(raw_budget, "sub_layer budget")
        except (ValueError, TypeError, ArithmeticError) as exc:
            raise FrozenSelectionError(f"invalid configured sub-layer budget: {exc}") from exc
    selected = {target.sub_layer for target in targets}
    for sub_layer in configured:
        if sub_layer not in selected:
            raise FrozenSelectionError(f"configured sub-layer {sub_layer.value!r} has no selected targets")
    if selected != set(configured):
        raise FrozenSelectionError("sub_layer_budgets must match selected sub-layers")
    for target in targets:
        if target.sub_layer_budget != configured[target.sub_layer]:
            raise FrozenSelectionError(
                f"target {target.stock_code} sub_layer_budget differs from configured sub-layer budget"
            )


def _canonical_hash(payload: Mapping[str, Any]) -> str:
    encoded = json.dumps(
        _canonicalise({k: v for k, v in payload.items() if k != "config_hash"}), sort_keys=True, separators=(",", ":"), ensure_ascii=False,
    ).encode("utf-8")
    return sha256(encoded).hexdigest()


def _canonicalise(payload: Any) -> Any:
    if isinstance(payload, Mapping):
        return {key: _canonicalise(payload[key]) for key in sorted(payload)}
    if isinstance(payload, (list, tuple)):
        return [_canonicalise(item) for item in payload]
    if isinstance(payload, (date, datetime)):
        return payload.isoformat()
    if isinstance(payload, Decimal):
        return str(payload)
    return payload


def _parse_date(value: Any) -> date:
    if isinstance(value, date) and not isinstance(value, datetime):
        return value
    if isinstance(value, str):
        return date.fromisoformat(value)
    raise FrozenSelectionError(f"expected ISO date string, got {value!r}")


def activate_selection(
    store: ShadowStore,
    selection: FrozenSelection,
    *,
    now: datetime | None = None,
) -> FrozenConfigRecord:
    """Validate activation and persist the frozen selection to ``store``."""

    selection.validate_activation(date.today() if now is None else now.date())
    payload = dict(selection.selection_payload)
    # Persist the normalized frozen records, not the possibly sparse manifest
    # representation, so every daily consumer receives the immutable funding
    # and identity fields without inferring them from a parent layer.
    payload["targets"] = [
        {
            "stock_code": target.stock_code,
            "tracking_index_code": target.tracking_index_code,
            "layer": target.layer,
            "sub_layer": target.sub_layer.value,
            "sub_layer_budget": str(target.sub_layer_budget),
            "instrument_type": target.instrument_type.value,
            "weight": str(target.weight),
            "config_hash": target.config_hash,
        }
        for target in selection.targets
    ]
    record = FrozenConfigRecord(
        config_hash=selection.config_hash,
        config=selection.base_config,
        selection_payload=payload,
        data_cutoff=selection.data_cutoff,
        activation_date=selection.activation_date,
        review_date=selection.review_date,
        activated_at=now or datetime.now(),
    )
    store.activate_frozen_config(record)
    return record


__all__ = [
    "FrozenSelection",
    "FrozenSelectionError",
    "FrozenTarget",
    "SIX_MONTH_REVIEW_DAYS",
    "activate_selection",
]



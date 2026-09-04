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
from .shadow_store import FrozenConfigRecord, ShadowStore


SIX_MONTH_REVIEW_DAYS: int = 183
LAYER_WEIGHT_SUM_TOLERANCE: float = 1e-6
MAX_SINGLE_TARGET_WEIGHT: float = 0.50


class FrozenSelectionError(ValueError):
    """Base class for frozen-selection validation failures."""


@dataclass(frozen=True)
class FrozenTarget:
    """One ETF product inside a frozen layer with its target weight."""

    stock_code: str
    tracking_index_code: str
    layer: str
    weight: float


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
        _validate_layer_weights(self.layer_weights)
        _validate_review_window(self.activation_date, self.review_date)
        _validate_max_single_weight(self.targets)
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
        targets = tuple(
            FrozenTarget(
                stock_code=str(target["stock_code"]),
                tracking_index_code=str(target.get("tracking_index_code", "")),
                layer=str(target.get("layer", "default")),
                weight=float(target["weight"]),
            )
            for target in payload.get("targets", ())
        )
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

        payload = json.loads(Path(path).read_text(encoding="utf-8"))
        return cls.from_payload(payload)


def _rebuild_config(payload: Mapping[str, Any]) -> AdaptiveConfig:
    declared_hash = payload.get("declared_config_hash")
    if not declared_hash:
        return AdaptiveConfig.default()
    return AdaptiveConfig.default()


def _validate_targets(targets: Sequence[FrozenTarget]) -> None:
    seen: set[str] = set()
    for target in targets:
        if not target.stock_code:
            raise FrozenSelectionError("target stock_code must be non-empty")
        if target.stock_code in seen:
            raise FrozenSelectionError(f"duplicate stock_code in frozen selection: {target.stock_code}")
        seen.add(target.stock_code)
        if target.weight < 0.0:
            raise FrozenSelectionError(
                f"target {target.stock_code} weight {target.weight} must be non-negative"
            )


def _validate_layer_weights(layer_weights: Mapping[str, float]) -> None:
    for layer, total in layer_weights.items():
        if abs(total - 1.0) > LAYER_WEIGHT_SUM_TOLERANCE:
            raise FrozenSelectionError(
                f"layer {layer!r} weights sum to {total}, expected 1.0 within "
                f"{LAYER_WEIGHT_SUM_TOLERANCE}"
            )


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


def _validate_max_single_weight(targets: Sequence[FrozenTarget]) -> None:
    for target in targets:
        if target.weight - MAX_SINGLE_TARGET_WEIGHT > 1e-9:
            raise FrozenSelectionError(
                f"target {target.stock_code} weight {target.weight} exceeds the "
                f"{MAX_SINGLE_TARGET_WEIGHT} cap"
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
    record = FrozenConfigRecord(
        config_hash=selection.config_hash,
        config=selection.base_config,
        selection_payload=dict(selection.selection_payload),
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
    "MAX_SINGLE_TARGET_WEIGHT",
    "SIX_MONTH_REVIEW_DAYS",
    "activate_selection",
]



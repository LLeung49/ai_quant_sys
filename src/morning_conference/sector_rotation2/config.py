"""Versioned configuration for the independent sector-rotation pipeline."""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from hashlib import sha256
import json
from typing import Mapping


@dataclass(frozen=True)
class ModelConfig:
    model_version: str = "v1"
    min_cross_section: int = 20
    min_coverage_ratio: float = 0.80
    phase_enter_threshold: float = 0.25
    phase_hold_threshold: float = 0.10
    score_minimum_weight: float = 0.60
    score_weights: Mapping[str, float] = field(
        default_factory=lambda: {
            "trend_level_score": 0.45,
            "velocity_score": 0.25,
            "acceleration_score": 0.15,
            "participation_score": 0.15,
        }
    )


DEFAULT_CONFIG = ModelConfig()


def config_hash(config: ModelConfig) -> str:
    """Return a deterministic hash that identifies the complete model setup."""
    payload = json.dumps(asdict(config), ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return sha256(payload.encode("utf-8")).hexdigest()

"""Explicit configuration for deterministic Sector Opportunity rules."""

from dataclasses import dataclass


@dataclass(frozen=True)
class OrchestratorConfig:
    model_version: str = "sector_opportunity_v1"

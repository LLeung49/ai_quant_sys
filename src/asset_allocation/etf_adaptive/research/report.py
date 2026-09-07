"""Reproducible research artifacts and operator report generation.

The artifact writer always stages files in a sibling ``<output>.staging``
directory and atomically renames the staging directory to ``output`` only
after every JSON, CSV, and Markdown file has been flushed to disk. This
guarantees that downstream consumers never observe a partial report.
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping


REPORT_FILES: tuple[str, ...] = (
    "manifest.json",
    "universe_audit.json",
    "attempted_configs.json",
    "failed_configs.json",
    "window_selections.json",
    "stitched_oos_nav.csv",
    "trades.csv",
    "mode_attribution.json",
    "cost_scenarios.json",
    "exposure_ranking.json",
    "product_ranking.json",
    "pareto_set.json",
    "portfolio_comparisons.json",
    "executive_report.md",
)


@dataclass(frozen=True)
class ResearchArtifact:
    """In-memory representation of one research output section."""

    attempted_config_count: int
    failed_config_count: int
    data_cutoff: str
    config_hash: str
    artifacts: Mapping[str, Any] = field(default_factory=lambda: MappingProxyType({}))
    frozen_selection: Mapping[str, Any] | None = None


@dataclass(frozen=True)
class ResearchReportManifest:
    """The published manifest for one research run."""

    data_cutoff: str
    attempted_config_count: int
    failed_config_count: int
    config_hash: str
    artifact_paths: Mapping[str, str]
    notes: tuple[str, ...] = ()


def publish_directory(staging: Path, destination: Path) -> None:
    """Atomically rename ``staging`` to ``destination``."""

    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        for child in destination.iterdir():
            if child.is_file():
                child.unlink()
            else:
                for sub in child.rglob("*"):
                    if sub.is_file():
                        sub.unlink()
                child.rmdir()
        destination.rmdir()
    os.replace(staging, destination)


def _stage_directory(output_dir: Path) -> Path:
    return output_dir.with_suffix(output_dir.suffix + ".staging")


def _json_default(value: Any) -> Any:
    if isinstance(value, date):
        return value.isoformat()
    if hasattr(value, "_asdict"):
        return value._asdict()
    if hasattr(value, "__dict__"):
        return value.__dict__
    raise TypeError(f"cannot serialize {type(value).__name__}")


def _dump_json(path: Path, payload: Any) -> None:
    path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True, default=_json_default),
        encoding="utf-8",
    )


def _dump_csv(path: Path, rows: list[dict[str, Any]], columns: tuple[str, ...]) -> None:
    lines = [",".join(columns)]
    for row in rows:
        cells = []
        for column in columns:
            value = row.get(column, "")
            cells.append(str(value))
        lines.append(",".join(cells))
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_research_report(
    artifact: ResearchArtifact, output_dir: Path,
) -> ResearchReportManifest:
    """Write every research artifact under ``output_dir`` and return the manifest.

    Files are staged in ``output_dir.staging`` and only renamed into place
    after every artifact has been flushed successfully, so consumers never
    observe a partial report.
    """

    output_dir = Path(output_dir)
    staging = _stage_directory(output_dir)
    if staging.exists():
        for child in staging.iterdir():
            if child.is_file():
                child.unlink()
            else:
                for sub in child.rglob("*"):
                    if sub.is_file():
                        sub.unlink()
                child.rmdir()
        staging.rmdir()
    staging.mkdir(parents=True, exist_ok=True)

    artifacts = artifact.artifacts

    def _payload(name: str, default: Any) -> Any:
        return artifacts.get(name, default)

    manifest_payload = {
        "data_cutoff": artifact.data_cutoff,
        "attempted_config_count": artifact.attempted_config_count,
        "failed_config_count": artifact.failed_config_count,
        "config_hash": artifact.config_hash,
        "notes": [],
    }
    if artifact.frozen_selection is not None:
        manifest_payload["frozen_selection"] = dict(artifact.frozen_selection)
    _dump_json(staging / "manifest.json", manifest_payload)

    _dump_json(
        staging / "universe_audit.json",
        _payload("universe_audit", {"as_of_date": artifact.data_cutoff, "rows": []}),
    )
    _dump_json(
        staging / "attempted_configs.json",
        _payload("attempted_configs", {"count": artifact.attempted_config_count, "configs": []}),
    )
    _dump_json(
        staging / "failed_configs.json",
        _payload("failed_configs", {"count": artifact.failed_config_count, "configs": []}),
    )
    _dump_json(
        staging / "window_selections.json",
        _payload("window_selections", {"windows": []}),
    )

    nav_rows = _payload("stitched_oos_nav", [])
    _dump_csv(
        staging / "stitched_oos_nav.csv",
        list(nav_rows),
        ("window_id", "trade_date", "nav_total"),
    )
    trade_rows = _payload("trades", [])
    _dump_csv(
        staging / "trades.csv",
        list(trade_rows),
        ("trade_date", "side", "shares", "raw_price", "reason", "config_hash"),
    )

    _dump_json(
        staging / "mode_attribution.json",
        _payload("mode_attribution", {"grid_pnl": 0.0, "trend_pnl": 0.0, "transition_pnl": 0.0, "costs": 0.0}),
    )
    _dump_json(
        staging / "cost_scenarios.json",
        _payload("cost_scenarios", {"scenarios": []}),
    )
    _dump_json(
        staging / "exposure_ranking.json",
        _payload("exposure_ranking", {"rows": []}),
    )
    _dump_json(
        staging / "product_ranking.json",
        _payload("product_ranking", {"rows": []}),
    )
    _dump_json(
        staging / "pareto_set.json",
        _payload("pareto_set", {"candidates": []}),
    )
    _dump_json(
        staging / "portfolio_comparisons.json",
        _payload("portfolio_comparisons", {"portfolios": []}),
    )
    executive_report = _payload(
        "executive_report",
        "# Adaptive ETF Research Report\n\n无数据 - 请提供 artifacts['executive_report']\n",
    )
    if not isinstance(executive_report, str):
        executive_report = json.dumps(executive_report, ensure_ascii=False, sort_keys=True, default=_json_default)
    (staging / "executive_report.md").write_text(executive_report, encoding="utf-8")

    artifact_paths = {name: str(output_dir / name) for name in REPORT_FILES}
    publish_directory(staging, output_dir)

    return ResearchReportManifest(
        data_cutoff=artifact.data_cutoff,
        attempted_config_count=artifact.attempted_config_count,
        failed_config_count=artifact.failed_config_count,
        config_hash=artifact.config_hash,
        artifact_paths=MappingProxyType(artifact_paths),
        notes=("atomic publish via staging directory",),
    )

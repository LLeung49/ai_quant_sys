"""Auditable artifacts for recorded ETF out-of-sample validation results.

This module only serializes the evidence persisted by instrument validation.
It deliberately never runs a strategy, broker, or data provider while writing
an operator report.
"""

from __future__ import annotations

import csv
import json
import os
import shutil
import tempfile
from collections.abc import Mapping
from dataclasses import asdict, dataclass, fields, replace
from datetime import date
from math import isclose, isfinite
from pathlib import Path
from typing import Iterable
from uuid import uuid4

from .attribution import build_excess_attribution, build_result_attribution
from .decision import ResearchConclusion
from .experiment import ExperimentSpec, experiment_evidence
from .instrument_validation import InstrumentValidationResult, ValidationWindowResult
from .metrics import PerformanceMetrics
from .strategy_specs import BUY_AND_HOLD_SPEC, FULL_ADAPTIVE_SPEC


@dataclass(frozen=True)
class ValidationArtifactManifest:
    summary_json: Path
    windows_csv: Path
    trades_csv: Path
    daily_nav_csv: Path
    report_markdown: Path
    chart_png: Path
    candidate_scores_csv: Path
    excess_attribution_json: Path
    daily_state_csv: Path


_METRIC_NAMES = tuple(field.name for field in fields(PerformanceMetrics))
_EVIDENCE_NUMBERS = (
    "oos_window_count", "oos_non_lagging_share", "annual_excess",
    "drawdown_improvement", "sharpe_excess", "sortino_excess",
    "calmar_excess", "cvar5_improvement", "exposure_ratio", "turnover",
    "total_cost", "initial_oos_nav", "cost_drag",
)


def _payload(event) -> dict[str, str]:
    return dict(event.payload)


def _finite(value: object) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and isfinite(value)


def _metrics_payload(metrics: PerformanceMetrics | None) -> dict[str, float] | None:
    if metrics is None or any(not _finite(getattr(metrics, name)) for name in _METRIC_NAMES):
        return None
    return {name: getattr(metrics, name) for name in _METRIC_NAMES}


def _evidence_blockers(result: InstrumentValidationResult) -> list[str]:
    blockers: list[str] = []
    evidence = result.evidence
    if evidence is None:
        blockers.append("missing_research_evidence")
    else:
        if evidence.data_valid is not True:
            blockers.append("data_valid")
        if not isinstance(evidence.stable_parameter_region, bool):
            blockers.append("stable_parameter_region")
        for name in _EVIDENCE_NUMBERS:
            if not _finite(getattr(evidence, name)):
                blockers.append(name)
        if not isinstance(evidence.oos_window_count, int) or evidence.oos_window_count <= 0:
            blockers.append("oos_window_count")
        if evidence.oos_window_count != len(result.windows):
            blockers.append("oos_window_count")
        if _finite(evidence.oos_non_lagging_share) and not 0.0 <= evidence.oos_non_lagging_share <= 1.0:
            blockers.append("oos_non_lagging_share")
        if _finite(evidence.exposure_ratio) and not 0.0 <= evidence.exposure_ratio <= 1.0:
            blockers.append("exposure_ratio")
        if _finite(evidence.turnover) and evidence.turnover < 0.0:
            blockers.append("turnover")
        if _finite(evidence.total_cost) and evidence.total_cost < 0.0:
            blockers.append("total_cost")
        if _finite(evidence.initial_oos_nav) and evidence.initial_oos_nav <= 0.0:
            blockers.append("initial_oos_nav")
        if _finite(evidence.cost_drag) and evidence.cost_drag < 0.0:
            blockers.append("cost_drag")
        if (
            _finite(evidence.total_cost) and _finite(evidence.initial_oos_nav)
            and evidence.initial_oos_nav > 0.0 and _finite(evidence.cost_drag)
            and not isclose(evidence.cost_drag, evidence.total_cost / evidence.initial_oos_nav,
                            rel_tol=1e-9, abs_tol=1e-12)
        ):
            blockers.append("cost_drag")
    if result.decision is None:
        blockers.append("missing_decision")
    if _metrics_payload(result.strategy_metrics) is None:
        blockers.append("strategy_metrics")
    if _metrics_payload(result.benchmark_metrics) is None:
        blockers.append("benchmark_metrics")
    if result.strategy_invested_sessions + result.strategy_cash_sessions <= 0:
        blockers.append("strategy_exposure")
    if result.benchmark_invested_sessions + result.benchmark_cash_sessions <= 0:
        blockers.append("benchmark_exposure")
    if result.rejection_reason:
        blockers.append(result.rejection_reason)
    manifest = result.run_manifest
    required_manifest_fields = {
        "schema_version", "runner", "source_provider", "data_cutoff", "requested_start",
        "data_fingerprint", "target", "selected_configs", "screened_axes",
    }
    if not isinstance(manifest, dict) or not required_manifest_fields.issubset(manifest):
        blockers.append("run_manifest")
    elif (
        manifest["data_cutoff"] != result.as_of_date.isoformat()
        or not isinstance(manifest["selected_configs"], list)
        or len(manifest["selected_configs"]) != len(result.windows)
        or not isinstance(manifest["screened_axes"], dict)
    ):
        blockers.append("run_manifest")
    if any(not isinstance(window.selected_config, dict) for window in result.windows):
        blockers.append("selected_config")
    blockers.extend(_experiment_blockers(result))
    return list(dict.fromkeys(blockers))


def _experiment_blockers(result: InstrumentValidationResult) -> list[str]:
    """Bind declared experiments to stored train-only scores and daily evidence."""
    manifest = result.run_manifest
    try:
        spec = ExperimentSpec.from_dict(manifest["experiment"])
        if (result.target.stock_code not in spec.target_codes
                or result.as_of_date != spec.as_of_date
                or not spec.start_date <= date.fromisoformat(manifest["requested_start"]) <= spec.as_of_date
                or manifest["target"]["stock_code"] != result.target.stock_code
                or manifest["selected_configs"] != [
                    {"window_id": window.window_id, "config_hash": window.config_hash,
                     "config": window.selected_config} for window in result.windows
                ]):
            return ["experiment_metadata"]
        # This recorded-result interface currently runs FULL_ADAPTIVE against B&H.
        # A declaration cannot relabel those runs as another policy/benchmark.
        if (spec.strategy != FULL_ADAPTIVE_SPEC
                or spec.benchmarks != (BUY_AND_HOLD_SPEC,)):
            return ["experiment_metadata"]
        expected = experiment_evidence(result, spec)
        if any(manifest.get(key) != value for key, value in expected.items()):
            return ["experiment_metadata"]
        for window, recorded in zip(result.windows, expected["experiment_windows"]):
            strategy = recorded["strategy_spec"]
            if (strategy is None or strategy["config"] != window.selected_config
                    or strategy["config_hash"] != window.config_hash):
                return ["experiment_metadata"]
            _validate_execution_boundaries(window, manifest["screened_axes"], spec)
    except (KeyError, TypeError, ValueError, AttributeError):
        return ["experiment_metadata"]
    blockers = []
    for window in result.windows:
        if not window.candidate_scores or not window.selected_scores:
            blockers.append("candidate_scores")
        else:
            candidates = [item.to_dict() for item in window.candidate_scores]
            if set(window.selected_scores) != {"grid_only", "trend_only"}:
                blockers.append("selected_scores")
            for family, score in window.selected_scores.items():
                section = {"grid_only": "grid", "trend_only": "trend"}.get(family)
                if (section is None or score.family != family or not score.stable
                        or score.rejection_reason is not None or score.to_dict() not in candidates
                        or dict(score.config[section]) != window.selected_config[section]
                        or dict(score.config["cost"]) != window.selected_config["cost"]):
                    blockers.append("selected_scores")
            for score in window.candidate_scores:
                for axis in score.screened_axes:
                    section = "grid" if axis in score.config["grid"] else "trend"
                    if (axis not in spec.allowed_axes
                            or score.config[section].get(axis) not in spec.allowed_axes[axis]):
                        blockers.append("allowed_axes")
        if (not window.strategy_observations or window.excess_attribution is None
                or window.training_end >= window.validation_start):
            blockers.append("daily_state_attribution")
            continue
        try:
            if any(point.nav_date > spec.as_of_date or point.nav_date < spec.start_date
                   for point in window.strategy_daily_nav):
                raise ValueError("daily evidence outside experiment dates")
            actual = build_excess_attribution(
                window.strategy_daily_nav, window.benchmark_daily_nav,
                window.strategy_observations, window.strategy_events,
                execution_cost=window.strategy_metrics.total_cost,
            )
            if any(not _finite(value) or not isclose(value, asdict(actual)[name], abs_tol=1e-9)
                   for name, value in asdict(window.excess_attribution).items()):
                raise ValueError("recorded attribution does not reconcile")
        except (TypeError, ValueError, AttributeError, ArithmeticError):
            blockers.append("daily_state_attribution")
    return blockers


def _validate_execution_boundaries(window, manifest_axes, spec) -> None:
    """Check all configuration fields, including those omitted from score axes."""
    base = asdict(spec.strategy.config)
    if window.cost_config is None or asdict(window.cost_config) != base["cost"]:
        raise ValueError("recorded execution cost differs from declaration")
    if not isinstance(manifest_axes, Mapping) or set(manifest_axes) != {"grid", "trend"}:
        raise ValueError("missing screening metadata")
    if not isinstance(window.screened_axes, Mapping) or set(window.screened_axes) != {"grid_only", "trend_only"}:
        raise ValueError("missing window screening metadata")

    def axes_set(axes, section):
        if not isinstance(axes, (tuple, list)) or not axes or any(not isinstance(axis, str) for axis in axes):
            raise ValueError("missing screened axes")
        if len(set(axes)) != len(axes) or any(axis not in base[section] or axis not in spec.allowed_axes for axis in axes):
            raise ValueError("undeclared or wrong-family screened axis")
        return set(axes)

    approved = {section: axes_set(manifest_axes[section], section) for section in ("grid", "trend")}
    for family, section in (("grid_only", "grid"), ("trend_only", "trend")):
        stages = window.screened_axes[family]
        if not isinstance(stages, (tuple, list)) or not stages:
            raise ValueError("missing screening stages")
        stage_axes = [axes_set(stage, section) for stage in stages]
        if set().union(*stage_axes) != approved[section]:
            raise ValueError("window and manifest screening differ")
        recorded_stages = {tuple(stage) for stage in stages}
        scores = [score for score in window.candidate_scores if score.family == family]
        if {tuple(score.screened_axes) for score in scores} != recorded_stages:
            raise ValueError("candidate and window screening differ")

    def check_config(config, permitted):
        if not isinstance(config, Mapping) or set(config) != set(base):
            raise ValueError("incomplete configuration")
        for section, defaults in base.items():
            values = config[section]
            if not isinstance(values, Mapping) or set(values) != set(defaults):
                raise ValueError("incomplete configuration section")
            for name, value in values.items():
                unchanged = type(value) is type(defaults[name]) and value == defaults[name]
                if unchanged:
                    continue
                if (name not in permitted.get(section, ())
                        or not any(type(value) is type(item) and value == item for item in spec.allowed_axes[name])):
                    raise ValueError("undeclared configuration deviation")

    check_config(window.selected_config, approved)
    for score in window.candidate_scores:
        section = {"grid_only": "grid", "trend_only": "trend"}.get(score.family)
        if section is None:
            raise ValueError("unrun candidate family")
        axes = axes_set(score.screened_axes, section)
        check_config(score.config, {section: axes})
        for axis in axes:
            if not any(type(score.config[section][axis]) is type(item) and score.config[section][axis] == item
                       for item in spec.allowed_axes[axis]):
                raise ValueError("unapproved screened value")


def validation_publication_decision(result: InstrumentValidationResult) -> dict[str, object]:
    """Use the same fail-closed decision in detailed and CLI summary artifacts."""
    return _decision_payload(result, _evidence_blockers(result))


def _decision_payload(result: InstrumentValidationResult, blockers: list[str]) -> dict[str, object]:
    if not blockers and result.decision is not None:
        return {
            "conclusion": result.decision.conclusion.value,
            "blockers": list(result.decision.blockers),
        }
    recorded_blockers = list(result.decision.blockers) if result.decision is not None else []
    return {
        "conclusion": ResearchConclusion.DO_NOT_TRADE.value,
        "blockers": list(dict.fromkeys(recorded_blockers + blockers)),
    }


def _comparison(result: InstrumentValidationResult, blockers: list[str]) -> dict[str, object] | None:
    if blockers:
        return None
    strategy = _metrics_payload(result.strategy_metrics)
    benchmark = _metrics_payload(result.benchmark_metrics)
    if strategy is None or benchmark is None:
        return None
    return {
        "strategy": strategy,
        "buy_and_hold": benchmark,
        "differences": {name: strategy[name] - benchmark[name] for name in _METRIC_NAMES},
    }


def _execution(result: InstrumentValidationResult, blockers: list[str]) -> dict[str, object] | None:
    if blockers or result.evidence is None or result.strategy_metrics is None or result.benchmark_metrics is None:
        return None
    strategy_sessions = result.strategy_invested_sessions + result.strategy_cash_sessions
    benchmark_sessions = result.benchmark_invested_sessions + result.benchmark_cash_sessions
    if strategy_sessions <= 0 or benchmark_sessions <= 0 or result.evidence.initial_oos_nav <= 0:
        return None
    initial_nav = result.evidence.initial_oos_nav
    return {
        "strategy": {
            "invested_sessions": result.strategy_invested_sessions,
            "cash_sessions": result.strategy_cash_sessions,
            "exposure_ratio": result.strategy_invested_sessions / strategy_sessions,
            "turnover": result.strategy_metrics.turnover,
            "total_cost": result.strategy_metrics.total_cost,
            "cost_drag": result.strategy_metrics.total_cost / initial_nav,
        },
        "buy_and_hold": {
            "invested_sessions": result.benchmark_invested_sessions,
            "cash_sessions": result.benchmark_cash_sessions,
            "exposure_ratio": result.benchmark_invested_sessions / benchmark_sessions,
            "turnover": result.benchmark_metrics.turnover,
            "total_cost": result.benchmark_metrics.total_cost,
            "cost_drag": result.benchmark_metrics.total_cost / initial_nav,
        },
    }


def _window_row(window: ValidationWindowResult) -> dict[str, object]:
    strategy = _metrics_payload(window.strategy_metrics)
    benchmark = _metrics_payload(window.benchmark_metrics)
    return {
        "window_id": window.window_id, "training_end": window.training_end.isoformat(),
        "validation_start": window.validation_start.isoformat(), "config_hash": window.config_hash,
        "strategy_return": window.strategy_return, "benchmark_return": window.benchmark_return,
        "selected_config": json.dumps(window.selected_config, ensure_ascii=False, sort_keys=True),
        "excess_return": window.strategy_return - window.benchmark_return,
        **{f"strategy_{name}": strategy[name] if strategy else None for name in _METRIC_NAMES},
        **{f"benchmark_{name}": benchmark[name] if benchmark else None for name in _METRIC_NAMES},
    }


def _distribution(rows: list[dict[str, object]]) -> dict[str, object] | None:
    if not rows:
        return None
    excesses = sorted(float(row["excess_return"]) for row in rows)
    return {
        "window_count": len(excesses),
        "win_rate": sum(value >= 0.0 for value in excesses) / len(excesses),
        "median_excess_return": excesses[len(excesses) // 2],
        "best_excess_return": excesses[-1],
        "worst_excess_return": excesses[0],
    }


def _training_surface(result: InstrumentValidationResult) -> list[dict[str, object]]:
    def records(items) -> list[dict[str, object]]:
        return [
            {
                "config_hash": item.config_hash,
                "positive_windows": list(item.positive_windows),
                "oos_returns": list(item.oos_returns),
                "positive_window_share": item.positive_window_share,
            }
            for item in items
        ]

    return [
        {"window_id": window.window_id, "grid": records(window.grid_training_surface),
         "trend": records(window.trend_training_surface)}
        for window in result.windows
    ]


def _trade_rows(result: InstrumentValidationResult) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for window in result.windows:
        for role, events in (("strategy", window.strategy_events), ("buy_and_hold", window.benchmark_events)):
            for event in events:
                if event.kind not in {"fill", "rejected_order"}:
                    continue
                payload = _payload(event)
                rows.append({
                    "window_id": window.window_id, "role": role,
                    "trade_date": event.event_date.isoformat(), "kind": event.kind,
                    "side": payload.get("side", ""), "shares": payload.get("shares", ""),
                    "raw_price": payload.get("raw_price", ""), "reason": payload.get("reason", ""),
                    "commission": payload.get("commission", ""), "config_hash": window.config_hash,
                })
    return rows


def _daily_nav_rows(result: InstrumentValidationResult) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for window in result.windows:
        for role, nav in (("strategy", window.strategy_daily_nav), ("buy_and_hold", window.benchmark_daily_nav)):
            for point in nav:
                rows.append({
                    "window_id": window.window_id,
                    "role": role,
                    "nav_date": point.nav_date.isoformat(),
                    "cash": str(point.cash),
                    "market_value": str(point.market_value),
                    "total_nav": str(point.total),
                    "exposure": int(point.market_value > 0),
                })
    return rows


def _candidate_score_rows(result: InstrumentValidationResult) -> list[dict[str, object]]:
    rows = []
    for window in result.windows:
        selected = [score.to_dict() for score in (window.selected_scores or {}).values()]
        for score in window.candidate_scores:
            payload = score.to_dict()
            rows.append({"window_id": window.window_id, "training_end": window.training_end.isoformat(),
                         "selected": payload in selected, **payload,
                         "config": json.dumps(payload["config"], sort_keys=True, allow_nan=False),
                         "screened_axes": json.dumps(payload["screened_axes"])})
    return rows


def _daily_state_rows(result: InstrumentValidationResult) -> list[dict[str, object]]:
    return [{"window_id": window.window_id, **asdict(item),
             "nav_date": item.nav_date.isoformat(),
             "regime": item.regime.value if item.regime is not None else None}
            for window in result.windows for item in window.strategy_observations]


def _excess_payload(result: InstrumentValidationResult) -> list[dict[str, object]]:
    return [{"window_id": window.window_id, **asdict(window.excess_attribution)}
            for window in result.windows if window.excess_attribution is not None]


_NEXT_RESEARCH_ACTION = {
    "grid_return": "Study grid spacing, sizing and stop/cooldown behavior on training windows.",
    "trend_return": "Study trend entry/exit filters and stop distances on training windows.",
    "transition_return": "Study recorded regime transitions and handoff timing on training windows.",
    "cash_opportunity_cost": "Study cash exposure and re-entry timing on training windows.",
}


def _excess_markdown(rows: list[dict[str, object]], valid: bool) -> list[str]:
    lines = ["## Excess return diagnostics", "",
             "Contributions sum daily net excess returns; execution_cost is a separate currency diagnostic already embedded in NAV.", ""]
    if not valid or not rows:
        return lines + ["Missing or invalid experiment evidence; no research action can be inferred.", ""]
    for row in rows:
        largest = max(_NEXT_RESEARCH_ACTION, key=lambda name: abs(row[name]))
        lines += [f"### {row['window_id']}", "",
                  f"Largest absolute contributor: {largest} ({row[largest]:.8f}).",
                  f"Next research action: {_NEXT_RESEARCH_ACTION[largest]}", ""]
    return lines + ["Research evidence only; no broker action is authorized.", ""]


def _attribution_payload(window: ValidationWindowResult) -> dict[str, object]:
    attribution = build_result_attribution(
        window.window_id,
        type("RecordedResult", (), {"events": window.strategy_events, "nav": window.strategy_daily_nav})(),
    )
    return {
        "window_id": attribution.window_id,
        "trade_points": [
            {"event_date": point.event_date.isoformat(), "kind": point.kind, "reason": point.reason,
             "shares": point.shares, "raw_price": point.raw_price}
            for point in attribution.trade_points
        ],
        "by_reason": {
            reason: {"reason": value.reason, "fill_count": value.fill_count,
                     "shares": value.shares, "traded_value": str(value.traded_value)}
            for reason, value in attribution.by_reason.items()
        },
        "invested_sessions": attribution.invested_sessions,
        "cash_sessions": attribution.cash_sessions,
        "rejected_order_count": attribution.rejected_order_count,
    }


def _drawdowns(nav: tuple[float, ...]) -> list[float]:
    if not nav:
        return []
    peak = nav[0]
    values = []
    for value in nav:
        peak = max(peak, value)
        values.append(value / peak - 1.0)
    return values


def _plot(result: InstrumentValidationResult, destination: Path) -> None:
    import matplotlib
    matplotlib.use("Agg")
    from matplotlib import pyplot as plt

    fig, (price_ax, equity_ax, drawdown_ax, exposure_ax) = plt.subplots(4, 1, figsize=(16, 15), sharex=True)
    for window in result.windows:
        x = list(range(len(window.strategy_nav)))
        if window.market_bars:
            bar_dates = {bar.trade_date: index for index, bar in enumerate(window.market_bars)}
            price_ax.plot(x, [bar.signal_close for bar in window.market_bars], label=f"{window.window_id} close")
            for event in window.strategy_events:
                if event.kind != "fill" or event.event_date not in bar_dates:
                    continue
                payload = _payload(event)
                price_ax.scatter(bar_dates[event.event_date], float(payload.get("raw_price", "nan")),
                                 marker="^" if payload.get("side") == "buy" else "v", s=50, color="tab:red")
        equity_ax.plot(x, window.strategy_nav, label=f"{window.window_id} strategy")
        equity_ax.plot(x, window.benchmark_nav, linestyle="--", label=f"{window.window_id} buy-and-hold")
        drawdown_ax.plot(x, _drawdowns(window.strategy_nav), label=f"{window.window_id} strategy drawdown")
        drawdown_ax.plot(x, _drawdowns(window.benchmark_nav), linestyle="--", label=f"{window.window_id} buy-and-hold drawdown")
        exposure_by_date = {point.nav_date: float(point.market_value > 0) for point in window.strategy_daily_nav}
        exposure = [exposure_by_date[bar.trade_date] for bar in window.market_bars if bar.trade_date in exposure_by_date]
        if len(exposure) == len(x):
            exposure_ax.step(x, exposure, where="post", label=f"{window.window_id} strategy exposure")
    price_ax.set_title(f"{result.target.stock_code}: recorded OOS price, fills, equity, drawdown and exposure")
    price_ax.set_ylabel("Price")
    equity_ax.set_ylabel("Normalised NAV")
    drawdown_ax.set_ylabel("Drawdown")
    exposure_ax.set_ylabel("Exposure")
    exposure_ax.set_xlabel("OOS session index (resets per window)")
    for axis in (price_ax, equity_ax, drawdown_ax, exposure_ax):
        axis.grid(alpha=.25)
        if axis.lines or axis.collections:
            axis.legend(loc="best", fontsize=8)
    fig.tight_layout()
    fig.savefig(destination, dpi=140)
    plt.close(fig)


def _write_csv(path: Path, rows: Iterable[dict[str, object]], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def _recommendation(conclusion: str) -> str:
    return {
        ResearchConclusion.PASSED.value: "仅可进入人工复核；研究结论不构成实盘交易授权。",
        ResearchConclusion.CONTINUE_PARAMETER_OPTIMIZATION.value: "继续参数优化，不执行交易。",
        ResearchConclusion.EVALUATE_STRUCTURAL_CHANGE.value: "评估策略结构调整，不执行交易。",
        ResearchConclusion.DO_NOT_TRADE.value: "不交易，直至补齐并复核缺失或无效证据。",
    }[conclusion]


def _markdown(summary: dict[str, object], attribution: list[dict[str, object]]) -> str:
    decision = summary["decision"]
    comparison = summary["comparison"]
    distribution = summary["oos_distribution"]
    execution = summary["execution"]
    provenance = summary["data_provenance"]
    lines = [
        "# 风险调整后 ETF 样本外验证决策报告", "",
        "## 决策", "",
        f"- 结论：`{decision['conclusion']}`",
        f"- 建议：{_recommendation(decision['conclusion'])}",
        f"- 阻断项：{', '.join(decision['blockers']) if decision['blockers'] else '无'}", "",
        "## 策略与买入持有比较", "",
    ]
    if comparison is None:
        lines.extend(["证据缺失或无效，不能生成策略与买入持有比较。", ""])
    else:
        lines.extend([
            "| 指标 | 策略 | 买入持有 | 差异（策略－买入持有） |",
            "| --- | ---: | ---: | ---: |",
        ])
        labels = {"sortino": "Sortino"}
        for name in ("annual_return", "sharpe", "sortino", "calmar", "cvar5", "max_drawdown", "turnover", "total_cost"):
            lines.append(f"| {labels.get(name, name)} | {comparison['strategy'][name]:.6f} | {comparison['buy_and_hold'][name]:.6f} | {comparison['differences'][name]:.6f} |")
        lines.append("")
    lines.extend(["## OOS 分布", "", json.dumps(distribution, ensure_ascii=False, indent=2) if distribution else "无可用 OOS 窗口证据。", ""])
    lines.extend(["## 执行、换手与成本", "", json.dumps(execution, ensure_ascii=False, indent=2) if execution else "执行证据缺失或无效。", ""])
    lines.extend(["## 数据边界、配置与训练曲面", "", json.dumps(provenance, ensure_ascii=False, indent=2), ""])
    lines.extend(["## 事件归因", "", json.dumps(attribution, ensure_ascii=False, indent=2), ""])
    return "\n".join(lines)


def write_atomic_text(destination: Path, text: str) -> None:
    """Replace one complete UTF-8 file without truncating a prior publication."""
    destination = Path(destination)
    descriptor, temporary = tempfile.mkstemp(prefix=f".{destination.name}.", suffix=".staging", dir=destination.parent)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, destination)
    finally:
        Path(temporary).unlink(missing_ok=True)


def _publish_validation_directory(staging: Path, destination: Path) -> None:
    """Publish a complete directory and restore the previous one on rename failure.

    Existing nonempty directories cannot be atomically overwritten on Windows.
    Retain the old generation until the staged rename succeeds. Readers may see
    a brief missing path between renames, but never a partially written report.
    """
    backup = destination.with_name(f".{destination.name}.{uuid4().hex}.backup")
    had_previous = destination.exists()
    if had_previous:
        os.replace(destination, backup)
    try:
        os.replace(staging, destination)
    except BaseException:
        if had_previous:
            os.replace(backup, destination)
        raise
    if had_previous:
        shutil.rmtree(backup)


def write_validation_artifacts(result: InstrumentValidationResult, output_dir: Path) -> ValidationArtifactManifest:
    """Publish complete recorded reports with rollback if final replacement fails."""
    output_dir = Path(output_dir)
    output_dir.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=f".{output_dir.name}.", suffix=".staging", dir=output_dir.parent))
    blockers = _evidence_blockers(result)
    window_rows = [_window_row(window) for window in result.windows]
    attribution = [_attribution_payload(window) for window in result.windows]
    excess_attribution = _excess_payload(result)
    summary = {
        "stock_code": result.target.stock_code,
        "exposure_id": result.target.exposure_id,
        "sub_layer": result.target.sub_layer.value,
        "scope": result.scope.value,
        "status": result.status.value,
        "activation_eligible": bool(
            result.activation_eligible
            and not blockers
            and result.decision is not None
            and result.decision.conclusion is ResearchConclusion.PASSED
        ),
        "decision": _decision_payload(result, blockers),
        "comparison": _comparison(result, blockers),
        "oos_distribution": _distribution(window_rows) if not blockers else None,
        "execution": _execution(result, blockers),
        "data_provenance": {
            "data_cutoff": result.as_of_date.isoformat(),
            "config_hashes": sorted({window.config_hash for window in result.windows}),
            "training_surface": _training_surface(result),
            "run_manifest": result.run_manifest,
        },
        "windows": window_rows if not blockers else None,
    }
    (staging / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8",
    )
    _write_csv(staging / "windows.csv", window_rows, list(window_rows[0]) if window_rows else ["window_id"])
    trades = _trade_rows(result)
    _write_csv(staging / "trades.csv", trades, ["window_id", "role", "trade_date", "kind", "side", "shares", "raw_price", "reason", "commission", "config_hash"])
    daily_nav = _daily_nav_rows(result)
    _write_csv(staging / "daily_nav.csv", daily_nav, ["window_id", "role", "nav_date", "cash", "market_value", "total_nav", "exposure"])
    scores = _candidate_score_rows(result)
    _write_csv(staging / "candidate_scores.csv", scores, list(scores[0]) if scores else [
        "window_id", "training_end", "selected", "config_hash", "config", "family", "screened_axes",
        "positive_subperiod_share", "sortino_excess", "sharpe_excess", "drawdown_improvement",
        "cvar5_improvement", "cost_drag", "exposure_ratio", "stable", "rejection_reason",
    ])
    _write_csv(staging / "daily_state.csv", _daily_state_rows(result), [
        "window_id", "nav_date", "regime", "target_exposure", "actual_exposure",
        "cooldown_remaining", "pending_order_count", "state_reason",
    ])
    (staging / "excess_attribution.json").write_text(
        json.dumps(excess_attribution, ensure_ascii=False, indent=2), encoding="utf-8",
    )
    (staging / "attribution.json").write_text(json.dumps(attribution, ensure_ascii=False, indent=2), encoding="utf-8")
    (staging / "report.md").write_text(
        _markdown(summary, attribution) + "\n".join(_excess_markdown(excess_attribution, not blockers)),
        encoding="utf-8",
    )
    _plot(result, staging / "validation_chart.png")
    charts_dir = staging / "charts"
    charts_dir.mkdir()
    for window in result.windows:
        _plot(replace(result, windows=(window,)), charts_dir / f"{window.window_id}.png")
    _publish_validation_directory(staging, output_dir)
    return ValidationArtifactManifest(output_dir / "summary.json", output_dir / "windows.csv", output_dir / "trades.csv", output_dir / "daily_nav.csv", output_dir / "report.md", output_dir / "validation_chart.png", output_dir / "candidate_scores.csv", output_dir / "excess_attribution.json", output_dir / "daily_state.csv")

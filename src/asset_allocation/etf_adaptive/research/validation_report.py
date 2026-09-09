"""Auditable, per-instrument OOS validation artifacts.

The report never replays a strategy: it consumes the validation result's
already-recorded NAV, fill events, bars and indicator snapshots.  This keeps
the visualisation and attribution aligned with the actual backtest run.
"""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass, replace
from datetime import date
from decimal import Decimal
from pathlib import Path
from typing import Iterable

from .attribution import build_result_attribution
from .instrument_validation import InstrumentValidationResult, ValidationWindowResult
from .metrics import PerformanceMetrics, Trade, calculate_performance
from .report import publish_directory


@dataclass(frozen=True)
class ValidationArtifactManifest:
    summary_json: Path
    windows_csv: Path
    trades_csv: Path
    report_markdown: Path
    chart_png: Path


def _metrics(path: tuple[float, ...], events: tuple[object, ...]) -> PerformanceMetrics:
    trades: list[Trade] = []
    for event in events:
        payload = _payload(event)
        if event.kind == "fill":
            trades.append(Trade(
                signal_date=event.event_date, fill_date=event.event_date,
                side=payload.get("side", ""), shares=int(payload.get("shares", "0")),
                raw_price=float(payload.get("raw_price", "0")),
                commission=Decimal(payload.get("commission", "0")), slippage_cost=Decimal("0"),
                minimum_commission_applied=Decimal(payload.get("commission", "0")) >= Decimal("5"),
                is_unfilled=False,
            ))
        elif event.kind == "rejected_order":
            trades.append(Trade(
                signal_date=event.event_date, fill_date=event.event_date, side=payload.get("side", ""),
                shares=0, raw_price=0.0, commission=Decimal("0"), slippage_cost=Decimal("0"),
                minimum_commission_applied=False, is_unfilled=True,
            ))
    return calculate_performance(path, tuple(trades))


def _payload(event) -> dict[str, str]:
    return dict(event.payload)


def _trade_rows(result: InstrumentValidationResult) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for window in result.windows:
        for role, events in (("strategy", window.strategy_events), ("benchmark", window.benchmark_events)):
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


def _window_row(window: ValidationWindowResult) -> dict[str, object]:
    strategy = _metrics(window.strategy_nav, window.strategy_events)
    benchmark = _metrics(window.benchmark_nav, window.benchmark_events)
    return {
        "window_id": window.window_id, "training_end": window.training_end.isoformat(),
        "validation_start": window.validation_start.isoformat(), "config_hash": window.config_hash,
        "strategy_return": window.strategy_return, "benchmark_return": window.benchmark_return,
        "excess_return": window.strategy_return - window.benchmark_return,
        "strategy_sharpe": strategy.sharpe, "benchmark_sharpe": benchmark.sharpe,
        "strategy_sortino": strategy.sortino, "benchmark_sortino": benchmark.sortino,
        "strategy_calmar": strategy.calmar, "benchmark_calmar": benchmark.calmar,
        "strategy_max_drawdown": strategy.max_drawdown, "benchmark_max_drawdown": benchmark.max_drawdown,
        "strategy_cvar5": strategy.cvar5, "benchmark_cvar5": benchmark.cvar5,
        "strategy_worst_126_session_return": strategy.worst_126_session_return,
        "benchmark_worst_126_session_return": benchmark.worst_126_session_return,
        "strategy_recovery_sessions": strategy.recovery_sessions,
        "benchmark_recovery_sessions": benchmark.recovery_sessions,
        "strategy_total_cost": strategy.total_cost, "benchmark_total_cost": benchmark.total_cost,
        "strategy_turnover": strategy.turnover, "benchmark_turnover": benchmark.turnover,
    }


def _distribution(rows: list[dict[str, object]]) -> dict[str, object]:
    excesses = [float(row["excess_return"]) for row in rows]
    if not excesses:
        return {"window_count": 0, "win_rate": 0.0}
    ordered = sorted(excesses)
    return {
        "window_count": len(excesses), "win_rate": sum(value >= 0.0 for value in excesses) / len(excesses),
        "median_excess_return": ordered[len(ordered) // 2], "best_excess_return": ordered[-1],
        "worst_excess_return": ordered[0],
    }


def _write_csv(path: Path, rows: Iterable[dict[str, object]], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def _plot(result: InstrumentValidationResult, destination: Path) -> None:
    import matplotlib
    matplotlib.use("Agg")
    from matplotlib import pyplot as plt

    fig, (price_ax, indicator_ax, nav_ax) = plt.subplots(3, 1, figsize=(16, 12), sharex=True)
    for window in result.windows:
        x = list(range(len(window.strategy_nav)))
        if window.market_bars:
            price_ax.plot(x, [bar.signal_close for bar in window.market_bars], label=f"{window.window_id} close")
            snapshots = window.indicator_snapshots
            ma20 = [item.ma20 if item is not None else float("nan") for item in snapshots]
            adx = [item.adx if item is not None and item.adx is not None else float("nan") for item in snapshots]
            price_ax.plot(x, ma20, linestyle="--", label="MA20")
            indicator_ax.plot(x, adx, label="ADX")
        for event in window.strategy_events:
            if event.kind == "fill" and event.event_date in [bar.trade_date for bar in window.market_bars]:
                index = [bar.trade_date for bar in window.market_bars].index(event.event_date)
                payload = _payload(event)
                marker = "^" if payload.get("side") == "buy" else "v"
                price_ax.scatter(index, float(payload.get("raw_price", "nan")), marker=marker, s=50, color="tab:red")
        nav_ax.plot(x, window.strategy_nav, label=f"{window.window_id} strategy")
        nav_ax.plot(x, window.benchmark_nav, linestyle="--", label=f"{window.window_id} B&H")
    price_ax.set_title(f"{result.target.stock_code}: OOS price, fills, indicators and NAV")
    price_ax.set_ylabel("Price")
    indicator_ax.set_ylabel("ADX")
    nav_ax.set_ylabel("Normalised NAV")
    nav_ax.set_xlabel("OOS session index (resets per window)")
    for axis in (price_ax, indicator_ax, nav_ax):
        axis.grid(alpha=.25)
        if axis.lines or axis.collections:
            axis.legend(loc="best", fontsize=8)
    fig.tight_layout()
    fig.savefig(destination, dpi=140)
    plt.close(fig)


def _attribution_payload(window: ValidationWindowResult) -> dict[str, object]:
    """Serialize immutable attribution without deepcopying MappingProxyType."""
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


def write_validation_artifacts(result: InstrumentValidationResult, output_dir: Path) -> ValidationArtifactManifest:
    """Publish JSON/CSV/Markdown/PNG atomically for one fixed instrument."""
    output_dir = Path(output_dir)
    staging = output_dir.with_suffix(output_dir.suffix + ".staging")
    if staging.exists():
        import shutil
        shutil.rmtree(staging)
    staging.mkdir(parents=True, exist_ok=True)
    window_rows = [_window_row(window) for window in result.windows]
    summary = {
        "stock_code": result.target.stock_code, "exposure_id": result.target.exposure_id,
        "sub_layer": result.target.sub_layer.value, "scope": result.scope.value,
        "as_of_date": result.as_of_date.isoformat(), "status": result.status.value,
        "activation_eligible": result.activation_eligible, "rejection_reason": result.rejection_reason,
        "strategy_annual_return": result.strategy_annual_return,
        "benchmark_annual_return": result.benchmark_annual_return,
        "strategy_max_drawdown": result.strategy_max_drawdown,
        "benchmark_max_drawdown": result.benchmark_max_drawdown,
        "window_distribution": _distribution(window_rows), "windows": window_rows,
    }
    (staging / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    _write_csv(staging / "windows.csv", window_rows, list(window_rows[0]) if window_rows else ["window_id"])
    trades = _trade_rows(result)
    _write_csv(staging / "trades.csv", trades, ["window_id", "role", "trade_date", "kind", "side", "shares", "raw_price", "reason", "commission", "config_hash"])
    attribution = [_attribution_payload(window) for window in result.windows]
    (staging / "attribution.json").write_text(json.dumps(attribution, ensure_ascii=False, indent=2), encoding="utf-8")
    (staging / "report.md").write_text(
        f"# {result.target.stock_code} OOS 验证报告\n\n"
        f"- 截止日：{result.as_of_date.isoformat()}\n- 状态：{result.status.value}\n"
        f"- 年化收益：策略 {result.strategy_annual_return!r}；B&H {result.benchmark_annual_return!r}\n"
        f"- 最大回撤：策略 {result.strategy_max_drawdown!r}；B&H {result.benchmark_max_drawdown!r}\n\n"
        "## 三联图\n\n图中仅使用本次 OOS 已记录的价格、指标快照、成交事件与净值；不重算交易。\n\n"
        "## 窗口分布\n\n```json\n" + json.dumps(summary["window_distribution"], ensure_ascii=False, indent=2) + "\n```\n",
        encoding="utf-8",
    )
    _plot(result, staging / "validation_chart.png")
    charts_dir = staging / "charts"
    charts_dir.mkdir()
    for window in result.windows:
        _plot(replace(result, windows=(window,)), charts_dir / f"{window.window_id}.png")
    publish_directory(staging, output_dir)
    return ValidationArtifactManifest(output_dir / "summary.json", output_dir / "windows.csv", output_dir / "trades.csv", output_dir / "report.md", output_dir / "validation_chart.png")

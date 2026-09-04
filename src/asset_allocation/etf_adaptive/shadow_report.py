"""Chinese-language daily shadow report renderer.

The shadow runner emits a deterministic ``ShadowRunSummary``. This module
renders a Chinese Markdown report that includes:

* run summary (date, execution eligible date, model version, config hash)
* per-target state (regime, grid anchor, cycle entry, stops, position, cash)
* indicators, anchor, stops, blocked reasons
* T+1 order advice with quantity rationale
* health check results

The renderer never modifies the underlying summary and never imports a
broker or order API.
"""

from __future__ import annotations

from datetime import date
from decimal import Decimal
from typing import Iterable

from .run_shadow_daily import ShadowRunSummary, TargetSpec
from .shadow_store import AdviceRecord, HealthCheck, StateRecord


def _format_money(value: Decimal | float) -> str:
    if isinstance(value, Decimal):
        return f"¥{value.quantize(Decimal('0.01'))}"
    return f"¥{value:.2f}"


def _render_state(target: TargetSpec, state: StateRecord) -> str:
    regime = state.regime or "无"
    return (
        f"- 标的: `{target.stock_code}` (跟踪指数 `{target.tracking_index_code or 'n/a'}`, "
        f"层级 `{target.layer}`, 权重 `{target.weight:.2%}`)\n"
        f"- 当前状态: regime=`{regime}`, 持仓 `{state.position_shares}`, "
        f"现金 {_format_money(state.cash)}\n"
        f"- 关键价位: "
        f"grid_anchor=`{state.state.grid_anchor}`, "
        f"cycle_entry_price=`{state.state.cycle_entry_price}`, "
        f"grid_stop_price=`{state.state.grid_stop_price}`, "
        f"trend_stop_price=`{state.state.trend_stop_price}`, "
        f"highest_close=`{state.state.highest_close}`\n"
        f"- 持久化身份: stock_code=`{state.stock_code}` "
        f"config_hash=`{state.config_hash}` as_of_date=`{state.as_of_date.isoformat()}`\n"
    )


def _render_advice(advice: AdviceRecord) -> str:
    order = advice.order
    return (
        f"- `{advice.stock_code}` @ signal_date={advice.signal_date.isoformat()}, "
        f"execution_eligible_date={advice.execution_eligible_date.isoformat()}, "
        f"side=`{order.side.value}`, reason=`{order.reason.value}`, "
        f"target_budget=`{order.target_budget}`, risk_per_unit=`{order.risk_per_unit}`\n"
        f"  - quantity_rationale: {order.quantity_rationale}\n"
        f"  - thresholds: {dict(order.signal_thresholds)}\n"
    )


def _render_health(health: HealthCheck) -> str:
    status = "✅" if health.passed else "❌"
    return f"- {status} `{health.check_name}` detail={dict(health.detail)}\n"


def render_daily_report(summary: ShadowRunSummary) -> str:
    """Render one Chinese Markdown report describing the shadow run."""

    lines: list[str] = []
    lines.append(f"# 自适应 ETF 影子运行日报 · {summary.as_of_date.isoformat()}\n")
    lines.append("## 运行概要\n")
    lines.append(
        f"- 信号交易日 (as_of_date): `{summary.as_of_date.isoformat()}`\n"
        f"- 可执行交易日 (execution_eligible_date): "
        f"`{summary.execution_eligible_date.isoformat()}`\n"
        f"- 模型版本: `{summary.model_version}`\n"
        f"- config_hash: `{summary.config_hash}`\n"
        f"- run_id: `{summary.run_id}`\n"
    )
    lines.append("\n## 标的当前状态\n")
    if not summary.target_states:
        lines.append("- （无活跃标的）\n")
    else:
        for target, state in summary.target_states:
            lines.append(_render_state(target, state))
    lines.append("\n## T+1 订单建议（仅供人工审阅，绝不下单）\n")
    if not summary.advices:
        lines.append("- （本交易日无新订单建议）\n")
    else:
        for advice in summary.advices:
            lines.append(_render_advice(advice))
    lines.append("\n## 健康检查\n")
    if not summary.health_checks:
        lines.append("- （本交易日无健康检查）\n")
    else:
        for health in summary.health_checks:
            lines.append(_render_health(health))
    lines.append("\n---\n")
    lines.append(
        "本报告由影子运行流水线自动产出；任何字段均不允许直接触发下单，"
        "仅供研究与运营复核使用。\n"
    )
    return "".join(lines)


__all__ = ["render_daily_report"]

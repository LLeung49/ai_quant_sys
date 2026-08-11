/** 基于已成功快照的市场环境与行业数量摘要。 */
import { Activity, BadgeCheck, TrendingUp, TriangleAlert } from "lucide-react";
import type { LifecycleSummaryCounts } from "../lifecycle/derive";
import type { LifecycleFilter } from "../lifecycle/meta";

interface MarketSummaryProps {
  /** 市场状态字段，来自当日快照。 */
  marketRegime: string;
  /** 完整快照的 Lifecycle 观察计数。 */
  counts: LifecycleSummaryCounts;
  /** 当前选中的 Lifecycle 状态组。 */
  activeLifecycle: LifecycleFilter;
  /** 是否仅查看当日状态变化的行业。 */
  changedOnly: boolean;
  /** 旧快照无 Lifecycle 字段时禁用四张交互卡。 */
  lifecycleDisabled?: boolean;
  /** 输出：点击状态组卡后更新页面筛选。 */
  onLifecycleFilterChange: (filter: LifecycleFilter) => void;
  /** 输出：点击今日变化卡后切换页面筛选。 */
  onChangedOnlyChange: (changedOnly: boolean) => void;
}

const regimeCopy: Record<string, { label: string; hint: string }> = {
  risk_off: { label: "风险偏好偏弱", hint: "市场环境偏弱，行业强弱变化需结合风险承受能力审慎观察。" },
  high_volatility: { label: "高波动", hint: "高波动环境下，强势信号存在更高不确定性。" },
  risk_on: { label: "风险偏好改善", hint: "市场参与度较活跃，仍需关注行业内部覆盖与持续性。" },
  range: { label: "区间震荡", hint: "市场方向尚不明确，行业信号可能出现更快切换。" },
};

/**
 * 渲染市场环境与当日行业观察计数。
 *
 * 输入：市场状态和从同日快照统计的行业数量。
 * 输出：不含交易指令的五张研究摘要卡片。
 */
export function MarketSummary({ marketRegime, counts, activeLifecycle, changedOnly, lifecycleDisabled = false, onLifecycleFilterChange, onChangedOnlyChange }: MarketSummaryProps) {
  const regime = regimeCopy[marketRegime] ?? { label: "状态待确认", hint: "市场状态字段缺失，建议结合原始数据检查。" };
  return (
    <section className="market-summary" aria-label="当日市场摘要">
      <article className="summary-card summary-card--regime"><div className="summary-icon"><Activity aria-hidden="true" /></div><div><span>市场环境</span><strong>{regime.label}</strong><p>{regime.hint}</p></div></article>
      <button className="summary-card summary-card--positive" type="button" disabled={lifecycleDisabled} aria-pressed={activeLifecycle === "trending"} onClick={() => onLifecycleFilterChange("trending")}><div className="summary-icon"><TrendingUp aria-hidden="true" /></div><div><span>趋势运行</span><strong>{counts.trending}</strong><p>点击仅显示趋势运行行业</p></div></button>
      <button className="summary-card" type="button" disabled={lifecycleDisabled} aria-pressed={activeLifecycle === "repair_or_emerging"} onClick={() => onLifecycleFilterChange("repair_or_emerging")}><div className="summary-icon"><BadgeCheck aria-hidden="true" /></div><div><span>修复/初启</span><strong>{counts.repairOrEmerging}</strong><p>点击仅显示修复或初启行业</p></div></button>
      <button className="summary-card summary-card--risk" type="button" disabled={lifecycleDisabled} aria-pressed={activeLifecycle === "risk"} onClick={() => onLifecycleFilterChange("risk")}><div className="summary-icon"><TriangleAlert aria-hidden="true" /></div><div><span>拥挤/背离/退出</span><strong>{counts.risk}</strong><p>点击仅显示风险提示行业</p></div></button>
      <button className="summary-card" type="button" disabled={lifecycleDisabled} aria-pressed={changedOnly} onClick={() => onChangedOnlyChange(!changedOnly)}><div className="summary-icon"><Activity aria-hidden="true" /></div><div><span>今日变化</span><strong>{counts.changed}</strong><p>点击切换仅看当日发生变化的行业</p></div></button>
    </section>
  );
}

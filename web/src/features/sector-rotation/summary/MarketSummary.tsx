/** 基于已成功快照的市场环境与行业数量摘要。 */
import { Activity, BadgeCheck, TrendingUp, TriangleAlert } from "lucide-react";

interface MarketSummaryProps {
  /** 市场状态字段，来自当日快照。 */
  marketRegime: string;
  /** 当日具备综合评分资格的行业数量。 */
  eligibleCount: number;
  /** 当日确认处于加速走强阶段的行业数量。 */
  acceleratingCount: number;
  /** 当日处于走弱或降温观察状态的行业数量。 */
  riskCount: number;
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
 * 输出：不含交易指令的四项研究摘要卡片。
 */
export function MarketSummary({ marketRegime, eligibleCount, acceleratingCount, riskCount }: MarketSummaryProps) {
  const regime = regimeCopy[marketRegime] ?? { label: "状态待确认", hint: "市场状态字段缺失，建议结合原始数据检查。" };
  return (
    <section className="market-summary" aria-label="当日市场摘要">
      <article className="summary-card summary-card--regime"><div className="summary-icon"><Activity aria-hidden="true" /></div><div><span>市场环境</span><strong>{regime.label}</strong><p>{regime.hint}</p></div></article>
      <article className="summary-card"><div className="summary-icon"><BadgeCheck aria-hidden="true" /></div><div><span>可评分行业</span><strong>{eligibleCount}</strong><p>{eligibleCount} 个行业具备完整评分证据</p></div></article>
      <article className="summary-card summary-card--positive"><div className="summary-icon"><TrendingUp aria-hidden="true" /></div><div><span>加速走强</span><strong>{acceleratingCount}</strong><p>{acceleratingCount} 个行业处于加速走强阶段</p></div></article>
      <article className="summary-card summary-card--risk"><div className="summary-icon"><TriangleAlert aria-hidden="true" /></div><div><span>风险观察</span><strong>{riskCount}</strong><p>{riskCount} 个行业出现趋势降温或走弱迹象</p></div></article>
    </section>
  );
}

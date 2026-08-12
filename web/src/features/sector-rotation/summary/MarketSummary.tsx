/** Renders the snapshot-level market environment summary. */
import { Activity } from "lucide-react";

interface MarketSummaryProps {
  /** Market-regime field from the displayed snapshot. */
  marketRegime: string;
}

const regimeCopy: Record<string, { label: string; hint: string }> = {
  risk_off: { label: "风险偏好偏弱", hint: "市场环境偏弱，行业强弱变化需结合风险承受能力审慎观察。" },
  high_volatility: { label: "高波动", hint: "高波动环境下，强势信号存在更高不确定性。" },
  risk_on: { label: "风险偏好改善", hint: "市场参与度较活跃，仍需关注行业内部覆盖与持续性。" },
  range: { label: "区间震荡", hint: "市场方向尚不明确，行业信号可能出现更快切换。" },
};

/** Keeps market-level context separate from industry Lifecycle observations. */
export function MarketSummary({ marketRegime }: MarketSummaryProps) {
  const regime = regimeCopy[marketRegime] ?? { label: "状态待确认", hint: "市场状态字段缺失，建议结合原始数据检查。" };

  return (
    <section className="market-summary" aria-label="当日市场摘要">
      <article className="summary-card summary-card--regime">
        <div className="summary-icon"><Activity aria-hidden="true" /></div>
        <div><span>市场环境</span><strong>{regime.label}</strong><p>{regime.hint}</p></div>
      </article>
    </section>
  );
}

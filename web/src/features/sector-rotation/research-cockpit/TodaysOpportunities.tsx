import { Activity, AlertTriangle, BarChart3, TrendingUp } from "lucide-react";
import { useQuery } from "@tanstack/react-query";
import { fetchResearchSummary } from "./api";
import { ResearchStatusBadge } from "./ResearchStatusBadge";

export function TodaysOpportunities({ asOfDate, level = 2, snapshotMode = "delayed_shadow" }: { asOfDate: string; level?: number; snapshotMode?: "live_shadow" | "delayed_shadow" | "backfill" }) {
  const query = useQuery({ queryKey: ["research-summary", asOfDate, level, snapshotMode], queryFn: () => fetchResearchSummary(asOfDate, level, snapshotMode), enabled: Boolean(asOfDate) });
  if (query.isLoading) return <section className="research-cockpit-panel">研究汇总加载中…</section>;
  if (query.isError || !query.data) return <section className="research-cockpit-panel" role="status">研究汇总暂不可用</section>;
  const values = query.data.summary;
  const items = [
    ["核心 ETF 候选", values.core_etf_ready ?? 0, BarChart3],
    ["趋势个股", values.trend_candidates ?? 0, TrendingUp],
    ["修复个股", values.repair_candidates ?? 0, Activity],
    ["减仓 / 避免", values.reduce_or_avoid ?? 0, AlertTriangle],
  ] as const;
  return <section className="research-cockpit-panel"><header><div><p className="eyebrow">RESEARCH COCKPIT</p><h2>研究机会摘要</h2></div><ResearchStatusBadge status={query.data.research_status} /></header><div className="research-summary-grid">{items.map(([label, value, Icon]) => <div className="research-summary-item" key={label}><Icon size={16} aria-hidden="true" /><span>{label}</span><strong>{value}</strong></div>)}</div>{(values.data_quality_blocked ?? 0) > 0 && <p className="research-warning">存在 {values.data_quality_blocked} 条数据质量阻断记录，未视为可用候选。</p>}<p className="research-source-note">来源版本：{query.data.source_versions.length} 组，按模型版本与配置哈希隔离。</p></section>;
}

import { useMutation, useQueries, useQueryClient } from "@tanstack/react-query";
import { addToWatchlist, fetchResearchCandidates, recordDecision } from "./api";
import { ResearchStatusBadge } from "./ResearchStatusBadge";

type SnapshotMode = "live_shadow" | "delayed_shadow" | "backfill";
type AvailabilityRow = { snapshot_mode: string; availability_basis?: string | null; data_available_at?: string | null; run_at?: string | null; execution_eligible_at?: string | null; daily_bar_entry_date?: string | null; daily_bar_entry_reason?: string | null };
const formatTimestamp = (value: string) => value.replace("T", " ").slice(0, 16);
const availabilityLabel = (basis: string) => basis === "market_close_1800" ? "行情收盘后 18:00" : "下一交易日 00:00";

function AvailabilityContract({ row }: { row: AvailabilityRow }) {
  const isLegacy = row.snapshot_mode === "backfill" || row.availability_basis === "legacy_inferred";
  if (isLegacy) return <small className="research-availability legacy">历史研究快照：时间未完整记录</small>;
  if (!row.data_available_at || !row.run_at || !row.execution_eligible_at || !row.availability_basis) return <small className="research-availability invalid">时间契约不完整：该快照不可作为可执行信号</small>;
  return <div className="research-availability"><small>模式：{row.snapshot_mode}</small><small>{availabilityLabel(row.availability_basis)}</small><small>数据就绪：{formatTimestamp(row.data_available_at)}</small><small>运行完成：{formatTimestamp(row.run_at)}</small><small>可执行时间：{formatTimestamp(row.execution_eligible_at)}</small>{row.daily_bar_entry_date ? <small>最早日线入场：{row.daily_bar_entry_date} 开盘</small> : <small>{row.daily_bar_entry_reason === "trading_calendar_unavailable" ? "日线入场日待交易日历确认" : "日线入场日暂不可用"}</small>}</div>;
}

export function SectorResearchCockpit({ asOfDate, level = 2, sectorName, snapshotMode = "live_shadow" }: { asOfDate: string; level?: number; sectorName?: string; snapshotMode?: SnapshotMode }) {
  const client = useQueryClient();
  const refreshRecords = () => void client.invalidateQueries({ queryKey: ["research-watchlist"] }).then(() => client.invalidateQueries({ queryKey: ["research-decisions"] }));
  const watch = useMutation({ mutationFn: (snapshotId: number) => addToWatchlist(snapshotId), onSuccess: refreshRecords });
  const decision = useMutation({ mutationFn: ({ snapshotId, value }: { snapshotId: number; value: "WATCH" | "ENTER" | "SKIP" | "EXIT" }) => recordDecision(snapshotId, value), onSuccess: refreshRecords });
  const queries = useQueries({ queries: ["sector_opportunity", "etf_core", "stock_trend", "stock_repair"].map((strategyType) => ({ queryKey: ["research-candidates", strategyType, asOfDate, level, snapshotMode, sectorName], queryFn: () => fetchResearchCandidates(asOfDate, level, snapshotMode, strategyType, sectorName), enabled: Boolean(asOfDate) })) });
  if (queries.some((query) => query.isLoading)) return <section className="research-cockpit-panel">候选数据加载中…</section>;
  if (queries.some((query) => query.isError || !query.data)) return <section className="research-cockpit-panel" role="status">部分候选数据暂不可用</section>;
  const sections = queries.map((query, index) => ({ label: ["板块机会", "ETF 候选", "趋势个股", "修复个股"][index], rows: query.data!.candidates.slice(0, index < 2 ? 12 : 20) }));
  return <section className="research-cockpit-panel"><header><div><p className="eyebrow">CANDIDATE SNAPSHOTS</p><h2>{sectorName ?? "研究候选"}</h2></div><ResearchStatusBadge /></header><div className="research-candidate-sections">{sections.map((section) => <div key={section.label}><h3>{section.label}<small>{section.rows.length}</small></h3><div className="research-candidate-list">{section.rows.map((row) => <article className="research-candidate-row" key={`${row.strategy_type}-${row.entity_code}`}><div className="research-security"><strong>{row.entity_name || row.entity_code}</strong><small>{row.entity_code}</small><span>{row.candidate_status}</span></div><div className="research-candidate-meta"><span>{row.is_data_quality_blocked ? "数据质量阻断" : row.candidate_score == null ? "未评分" : `score ${row.candidate_score.toFixed(3)}`}</span><small>{row.model_version}</small><AvailabilityContract row={row} /><div className="research-row-actions"><button type="button" title="加入研究观察清单" disabled={watch.isPending} onClick={() => watch.mutate(row.id)}>观察</button>{(["WATCH", "ENTER", "SKIP", "EXIT"] as const).map((value) => <button key={value} type="button" title={`记录 ${value} 人工研究决定`} disabled={decision.isPending} onClick={() => decision.mutate({ snapshotId: row.id, value })}>{value}</button>)}</div></div></article>)}</div></div>)}</div></section>;
}

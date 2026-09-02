/** 板块轮动页面的顶层布局：标签页切换避免引入额外 router 依赖。 */
import { QueryClient, QueryClientProvider, useQuery } from "@tanstack/react-query";
import { Activity, DatabaseZap } from "lucide-react";
import { useState } from "react";
import { SectorRotationPage } from "../features/sector-rotation/SectorRotationPage";
import { MacdPoolPage } from "../features/sector-rotation/MacdPoolPage";
import { TodaysOpportunities } from "../features/sector-rotation/research-cockpit/TodaysOpportunities";
import { SectorResearchCockpit } from "../features/sector-rotation/research-cockpit/SectorResearchCockpit";
import { ResearchRecords } from "../features/sector-rotation/research-cockpit/ResearchRecords";
import { fetchLatestResearchDate } from "../features/sector-rotation/research-cockpit/api";

type WorkspaceTab = "rotation" | "macd" | "research";

const TAB_META: Record<WorkspaceTab, { label: string; caption: string; Icon: typeof Activity }> = {
  macd: { label: "MACD 标的池", caption: "MACD POOL · 动能与趋势筛选", Icon: DatabaseZap },
  rotation: { label: "板块轮动", caption: "SECTOR ROTATION · 申万行业研究", Icon: Activity },
  research: { label: "研究驾驶舱", caption: "RESEARCH COCKPIT · SHADOW 候选", Icon: Activity },
};

/**
 * 渲染研究终端的应用壳。
 *
 * 输入：无；标签页状态由 useState 维护。
 * 输出：包含顶部标签栏、当前选中页面与免责声明的 React 元素。
 */
export function App() {
  const [queryClient] = useState(() => new QueryClient({ defaultOptions: { queries: { retry: 1 } } }));
  const [tab, setTab] = useState<WorkspaceTab>("rotation");
  const meta = TAB_META[tab];
  return (
    <QueryClientProvider client={queryClient}>
      <main className="app-shell" aria-busy="false">
        <header className="app-header">
          <div className="brand-mark"><Activity aria-hidden="true" size={20} /><span>AI QUANT</span><small>RESEARCH TERMINAL</small></div>
          <div className="header-copy">
            <p className="eyebrow">{meta.caption}</p>
            <h1>{meta.label}</h1>
            <p className="subtitle">从相对强弱、趋势加速度与市场参与度，观察行业轮动所处的位置与变化。</p>
          </div>
          <div className="header-status"><DatabaseZap aria-hidden="true" size={16} /><span>快照数据</span><strong>只读</strong></div>
        </header>
        <nav className="workspace-tabs" role="tablist" aria-label="工作区切换">
          {(Object.entries(TAB_META) as Array<[WorkspaceTab, typeof TAB_META[WorkspaceTab]]>).map(([key, item]) => (
            <button
              key={key}
              type="button"
              role="tab"
              aria-selected={tab === key}
              className={`workspace-tab ${tab === key ? "is-active" : ""}`}
              onClick={() => setTab(key)}
            >
              <item.Icon aria-hidden="true" size={14} /> {item.label}
            </button>
          ))}
        </nav>
        {tab === "rotation" ? <SectorRotationPage /> : tab === "macd" ? <MacdPoolPage /> : <ResearchCockpitPage />}
        <footer className="disclaimer">
          <span>AI Quant Research · Sector Rotation V1</span>
          <span>本页面仅供量化研究参考，不构成投资建议。</span>
        </footer>
      </main>
    </QueryClientProvider>
  );
}

function ResearchCockpitPage() {
  const [snapshotMode, setSnapshotMode] = useState<"live_shadow" | "delayed_shadow" | "backfill">("delayed_shadow");
  const snapshotModeLabel = { delayed_shadow: "延迟运行", live_shadow: "当日运行", backfill: "历史回填" }[snapshotMode];
  const latest = useQuery({ queryKey: ["research-latest-date", snapshotMode], queryFn: () => fetchLatestResearchDate(2, snapshotMode) });
  const [selectedDate, setSelectedDate] = useState<string>("");
  const activeDate = selectedDate || latest.data?.as_of_date || "";

  if (latest.isLoading) return <div className="research-cockpit-page"><section className="research-cockpit-panel">快照信息加载中…</section></div>;
  if (!activeDate) return <div className="research-cockpit-page"><section className="research-cockpit-panel">暂无可用研究快照</section></div>;

  return (
    <div className="research-cockpit-page">
      <div className="research-date-bar">
        <div className="research-date-controls">
          <span>观测交易日:</span>
          <input
            type="date"
            value={activeDate}
            onChange={(e) => setSelectedDate(e.target.value)}
          />
          <label>
            快照模式
            <select value={snapshotMode} onChange={(event) => { setSnapshotMode(event.target.value as "live_shadow" | "delayed_shadow" | "backfill"); setSelectedDate(""); }}>
              <option value="delayed_shadow">延迟运行</option>
              <option value="live_shadow">当日运行</option>
              <option value="backfill">历史回填</option>
            </select>
          </label>
          {selectedDate && selectedDate !== latest.data?.as_of_date && (
            <button
              type="button"
              onClick={() => setSelectedDate("")}
            >
              返回最新 ({latest.data?.as_of_date})
            </button>
          )}
        </div>
        <span className="research-date-note">
          {`当前查询：${snapshotModeLabel}；仅显示该模式快照，不跨模式回退。`}
        </span>
      </div>
      <TodaysOpportunities asOfDate={activeDate} snapshotMode={snapshotMode} />
      <SectorResearchCockpit asOfDate={activeDate} snapshotMode={snapshotMode} />
      <ResearchRecords />
    </div>
  );
}

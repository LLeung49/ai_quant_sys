/** 板块轮动页面的顶层布局：标签页切换避免引入额外 router 依赖。 */
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { Activity, DatabaseZap } from "lucide-react";
import { useState } from "react";
import { SectorRotationPage } from "../features/sector-rotation/SectorRotationPage";

type WorkspaceTab = "rotation";

const TAB_META: Record<WorkspaceTab, { label: string; caption: string; Icon: typeof Activity }> = {
  rotation: { label: "板块轮动", caption: "SECTOR ROTATION · 申万行业研究", Icon: Activity },
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
        <SectorRotationPage />
        <footer className="disclaimer">
          <span>AI Quant Research · Sector Rotation V1</span>
          <span>本页面仅供量化研究参考，不构成投资建议。</span>
        </footer>
      </main>
    </QueryClientProvider>
  );
}

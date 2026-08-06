/** 板块轮动页面的顶层布局组件。 */
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { Activity, DatabaseZap } from "lucide-react";
import { useState } from "react";
import { SectorRotationPage } from "../features/sector-rotation/SectorRotationPage";

/**
 * 渲染板块轮动产品的初始应用壳。
 *
 * 输入：无；后续将由查询状态驱动内部内容。
 * 输出：包含语义主区域、初始加载态与研究风险提示的 React 元素。
 */
export function App() {
  const [queryClient] = useState(() => new QueryClient({ defaultOptions: { queries: { retry: 1 } } }));
  return (
    <QueryClientProvider client={queryClient}><main className="app-shell" aria-busy="false">
      <header className="app-header">
        <div className="brand-mark"><Activity aria-hidden="true" size={20} /><span>AI QUANT</span><small>RESEARCH TERMINAL</small></div>
        <div className="header-copy">
          <p className="eyebrow">SECTOR ROTATION · 申万行业研究</p>
          <h1>板块轮动</h1>
          <p className="subtitle">从相对强弱、趋势加速度与市场参与度，观察行业轮动所处的位置与变化。</p>
        </div>
        <div className="header-status"><DatabaseZap aria-hidden="true" size={16} /><span>快照数据</span><strong>只读</strong></div>
      </header>
      <SectorRotationPage />
      <footer className="disclaimer"><span>AI Quant Research · Sector Rotation V1</span><span>本页面仅供量化研究参考，不构成投资建议。</span></footer>
    </main></QueryClientProvider>
  );
}

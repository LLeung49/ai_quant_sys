/** 按需加载主象限图，避免 ECharts 进入应用初始 JavaScript 包。 */
import { lazy, Suspense } from "react";
import type { QuadrantSector } from "./quadrantOption";
import type { QuadrantTrailPoint } from "./quadrantOption";
import type { LabelDensity } from "../workbench/urlState";

const QuadrantChart = lazy(() => import("./QuadrantChart").then((module) => ({ default: module.QuadrantChart })));

/**
 * 延迟加载板块轮动象限图。
 *
 * 输入：同日行业连续得分。
 * 输出：图表模块加载前显示可理解的占位，加载完成后渲染实际 ECharts 图表。
 */
export function LazyQuadrantChart({ sectors, selectedSectorName, onSelect, labelDensity = "focus", trail = [] }: { sectors: QuadrantSector[]; selectedSectorName?: string | null; onSelect?: (sectorName: string) => void; labelDensity?: LabelDensity; trail?: Array<QuadrantTrailPoint | null> }) {
  return <Suspense fallback={<div className="loading-panel">正在加载轮动图表…</div>}><QuadrantChart sectors={sectors} selectedSectorName={selectedSectorName} onSelect={onSelect} labelDensity={labelDensity} trail={trail} /></Suspense>;
}

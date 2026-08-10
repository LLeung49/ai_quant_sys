/** 板块 K 线图表的按需加载边界，避免首屏下载 KLineChart 图表内核。 */
import { Suspense, lazy } from "react";
import type { SectorKlineChartProps } from "./SectorKlineChart";

const SectorKlineChart = lazy(() => import("./SectorKlineChart"));

/**
 * 延迟加载板块 K 线组件，并在模块下载期间维持抽屉布局稳定。
 *
 * 输入：与 ``SectorKlineChart`` 相同的日 K 线、模式、窗口和无障碍属性。
 * 输出：加载完成后的三窗格图表，或具有固定高度的加载占位。
 * 异常：动态导入的渲染异常由上层 ``KlineErrorBoundary`` 接管。
 */
export function LazySectorKlineChart(props: SectorKlineChartProps) {
  return <Suspense fallback={<div className="sector-kline-chart__skeleton" aria-label="正在加载行情图" />}>
    <SectorKlineChart {...props} />
  </Suspense>;
}

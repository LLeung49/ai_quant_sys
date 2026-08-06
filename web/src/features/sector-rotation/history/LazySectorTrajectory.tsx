/** 按需加载行业历史轨迹图，避免非首屏图表进入初始包。 */
import { lazy, Suspense } from "react";
import type { SectorTrajectoryProps } from "./SectorTrajectory";

const SectorTrajectory = lazy(() => import("./SectorTrajectory").then((module) => ({ default: module.SectorTrajectory })));

/** 输入：行业名称与坐标序列；输出：延迟加载的历史轨迹图或加载提示。 */
export function LazySectorTrajectory({ trajectories }: SectorTrajectoryProps) {
  return <Suspense fallback={<p>正在加载历史轨迹…</p>}><SectorTrajectory trajectories={trajectories} /></Suspense>;
}

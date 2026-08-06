/** 行业历史轮动轨迹的 ECharts 展示组件。 */
import { useEffect, useMemo, useRef } from "react";
import { echarts } from "../chart/echarts";
import { buildTrajectoryOption } from "./trajectoryOption";

export interface TrajectoryPoint { as_of_date: string; velocity_score: number | null; acceleration_score: number | null; }
export interface SectorTrajectoryProps { trajectories: { sector_name: string; points: TrajectoryPoint[] }[]; }

/**
 * 挂载最多五行业的历史象限轨迹。
 *
 * 输入：按交易日排序的行业坐标序列。
 * 输出：自适应尺寸 ECharts 容器；坐标缺失由配置层绘制为断线。
 */
export function SectorTrajectory({ trajectories }: SectorTrajectoryProps) {
  const ref = useRef<HTMLDivElement>(null);
  const chartRef = useRef<ReturnType<typeof echarts.init> | null>(null);
  const option = useMemo(() => buildTrajectoryOption(trajectories), [trajectories]);
  const optionRef = useRef(option);
  const renderedOptionRef = useRef<typeof option | null>(null);
  optionRef.current = option;
  useEffect(() => {
    if (!ref.current) return undefined;
    const container = ref.current;
    const initializeOrResize = () => {
      if (container.clientWidth <= 0 || container.clientHeight <= 0) return;
      if (!chartRef.current) {
        chartRef.current = echarts.init(container);
        chartRef.current.setOption(optionRef.current);
        renderedOptionRef.current = optionRef.current;
      }
      chartRef.current.resize();
    };
    const resizeObserver = new ResizeObserver(initializeOrResize);
    resizeObserver.observe(container);
    initializeOrResize();
    return () => { resizeObserver.disconnect(); chartRef.current?.dispose(); chartRef.current = null; };
  }, []);
  useEffect(() => {
    if (chartRef.current && renderedOptionRef.current !== option) {
      chartRef.current.setOption(option, { notMerge: true });
      renderedOptionRef.current = option;
    }
  }, [option]);
  return <div className="trajectory-chart" role="img" aria-label="行业历史轮动轨迹" ref={ref} />;
}

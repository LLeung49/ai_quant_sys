/** ECharts 板块轮动象限气泡图组件。 */
import { useEffect, useMemo, useRef } from "react";
import { echarts } from "./echarts";
import { buildQuadrantOption, type QuadrantSector } from "./quadrantOption";
import type { QuadrantTrailPoint } from "./quadrantOption";
import type { LabelDensity } from "../workbench/urlState";
export type { QuadrantSector } from "./quadrantOption";

interface QuadrantChartProps {
  /** 同日快照中可用于象限展示的行业集合。 */
  sectors: QuadrantSector[];
  /** 当前高亮行业；为空时所有气泡使用正常透明度。 */
  selectedSectorName?: string | null;
  /** 输入：用户点击的行业名称；输出：通知页面同步列表和详情选择。 */
  onSelect?: (sectorName: string) => void;
  /** 智能标签显示密度。 */
  labelDensity?: LabelDensity;
  /** 回放时当前选中行业截至当前帧的最近历史尾迹。 */
  trail?: Array<QuadrantTrailPoint | null>;
}

/**
 * 在 DOM 容器中挂载板块轮动象限气泡图。
 *
 * 输入：行业连续得分与阶段字段。
 * 输出：一个自适应尺寸的 ECharts 图表容器；卸载时释放图表资源。
 */
export function QuadrantChart({ sectors, selectedSectorName, onSelect, labelDensity = "focus", trail = [] }: QuadrantChartProps) {
  const containerRef = useRef<HTMLDivElement>(null);
  const chartRef = useRef<ReturnType<typeof echarts.init> | null>(null);
  const option = useMemo(() => buildQuadrantOption(sectors, selectedSectorName, labelDensity, trail), [sectors, selectedSectorName, labelDensity, trail]);
  const optionRef = useRef(option);
  const renderedOptionRef = useRef<typeof option | null>(null);
  const selectRef = useRef(onSelect);
  optionRef.current = option;
  selectRef.current = onSelect;

  useEffect(() => {
    if (!containerRef.current) return undefined;
    const container = containerRef.current;
    const initializeOrResize = () => {
      if (container.clientWidth <= 0 || container.clientHeight <= 0) return;
      if (!chartRef.current) {
        const chart = echarts.init(container);
        chart.on("click", (params: { name?: string }) => {
          if (params.name) selectRef.current?.(params.name);
        });
        chartRef.current = chart;
        chart.setOption(optionRef.current);
        renderedOptionRef.current = optionRef.current;
      }
      chartRef.current.resize();
    };
    const resizeObserver = new ResizeObserver(initializeOrResize);
    resizeObserver.observe(container);
    initializeOrResize();
    return () => {
      resizeObserver.disconnect();
      chartRef.current?.dispose();
      chartRef.current = null;
    };
  }, []);

  useEffect(() => {
    if (chartRef.current && renderedOptionRef.current !== option) {
      chartRef.current.setOption(option, { notMerge: true });
      renderedOptionRef.current = option;
    }
  }, [option]);

  return <div className="quadrant-chart-shell">
    <div ref={containerRef} className="quadrant-chart" aria-label="板块轮动象限气泡图" role="img" />
    <span className="quadrant-caption quadrant-caption--repair">修复 / 弱转强观察</span>
    <span className="quadrant-caption quadrant-caption--strong">加速走强</span>
    <span className="quadrant-caption quadrant-caption--weak">加速走弱</span>
    <span className="quadrant-caption quadrant-caption--cooling">强势降温</span>
  </div>;
}

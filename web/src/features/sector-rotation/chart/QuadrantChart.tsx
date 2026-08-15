/** ECharts 板块轮动象限图组件。 */
import { useEffect, useMemo, useRef } from "react";
import { echarts } from "./echarts";
import { buildQuadrantOption, type QuadrantSector } from "./quadrantOption";
import type { QuadrantTrailPoint } from "./quadrantOption";
import type { LabelDensity } from "../workbench/urlState";
import type { ShortTermHaloInfo } from "./shortTermHalo";
export type { QuadrantSector } from "./quadrantOption";
export type { ShortTermHaloInfo } from "./shortTermHalo";

interface QuadrantChartProps {
  /** 同日快照中可用于象限展示的行业集合。 */
  sectors: QuadrantSector[];
  /** 当前高亮行业;为空时所有气泡使用正常透明度。 */
  selectedSectorName?: string | null;
  /** 输入:用户点击的行业名称;输出:通知页面同步到列表和详情选择。 */
  onSelect?: (sectorName: string) => void;
  /** 智能标签显示密度。 */
  labelDensity?: LabelDensity;
  /** 回放时当前选中行业截止当前帧的最近10日尾迹。 */
  trail?: Array<QuadrantTrailPoint | null>;
  /** 短期异动光晕与 Chip 的索引;不传则不渲染光晕装饰层。 */
  shortTermHaloByName?: ReadonlyMap<string, ShortTermHaloInfo>;
}

/**
 * 在 DOM 容器中挂载板块轮动象限图。
 *
 * 输入:行业连续得分与阶段字段;可选的短期光晕映射、回放尾迹。
 * 输出:一个自适应尺寸的 ECharts 图表容器;卸载时释放图表资源。
 *
 * 该组件不直接读取任何短期面板或回放数据;所有外部协调由父组件 SectorRotationPage 完成,
 * 以保证象限图本身可以在未来被独立复用(例如其它页面对 v1 截面的快照)。
 */
export function QuadrantChart({ sectors, selectedSectorName, onSelect, labelDensity = "focus", trail = [], shortTermHaloByName }: QuadrantChartProps) {
  const containerRef = useRef<HTMLDivElement>(null);
  const chartRef = useRef<ReturnType<typeof echarts.init> | null>(null);
  const option = useMemo(() => buildQuadrantOption(sectors, selectedSectorName, labelDensity, trail, shortTermHaloByName), [sectors, selectedSectorName, labelDensity, trail, shortTermHaloByName]);
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

  return <div className="quadrant-chart-shell sector-quadrant-shell">
    <div ref={containerRef} className="quadrant-chart" aria-label="板块轮动象限图" role="img" />
    <span className="quadrant-caption quadrant-caption--repair">修复 / 反弹观察</span>
    <span className="quadrant-caption quadrant-caption--strong">加速走强</span>
    <div className="quadrant-caption-row"><span>加速走强</span><span>强势降温</span></div>
  </div>;
}
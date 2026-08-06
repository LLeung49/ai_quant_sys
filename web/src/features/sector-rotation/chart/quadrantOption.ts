/** 板块轮动象限气泡图的 ECharts 纯配置生成器。 */

import { getPhaseMeta } from "../labels";
import type { LabelDensity } from "../workbench/urlState";
import { rankAttention } from "./attentionPriority";

export interface QuadrantSector {
  sector_name: string;
  velocity_score: number | null;
  acceleration_score: number | null;
  volume_score: number | null;
  participation_score: number | null;
  phase_confirmed: string | null;
  phase_confidence: number | null;
  composite_rank: number | null;
  composite_score?: number | null;
  rank_change_1d?: number | null;
  rank_change_5d?: number | null;
  coverage_ratio?: number | null;
  phase_changed?: number | boolean | null;
}

export interface QuadrantTrailPoint { as_of_date: string; velocity_score: number; acceleration_score: number; }

/**
 * 将当日行业截面转换为象限气泡图配置。
 *
 * 输入：行业的连续得分与确认阶段；缺失速度或加速度的行业不会进入图表。
 * 输出：固定 ``[-1, 1]`` 坐标、阶段颜色和可解释 tooltip 的 ECharts 配置对象。
 */
export function buildQuadrantOption(sectors: QuadrantSector[], selectedSectorName?: string | null, labelDensity: LabelDensity = "focus", trail: Array<QuadrantTrailPoint | null> = []) {
  const attention = rankAttention(sectors, selectedSectorName, labelDensity);
  const attentionByName = new Map(attention.map((decision) => [decision.sector.sector_name, decision]));
  const data = sectors
    .filter((sector) => sector.velocity_score !== null && sector.acceleration_score !== null)
    .map((sector) => {
      const phase = getPhaseMeta(sector.phase_confirmed);
      const selected = sector.sector_name === selectedSectorName;
      const attentionDecision = attentionByName.get(sector.sector_name);
      return {
        name: sector.sector_name,
        value: [sector.velocity_score!, sector.acceleration_score!, sector.volume_score ?? 0],
        itemStyle: {
          color: phase.color,
          opacity: selectedSectorName && !selected ? 0.2 : Math.max(0.48, sector.phase_confidence ?? 0.58),
          borderColor: selected ? "#ffffff" : (sector.participation_score ?? 0) > 0 ? "#d7e7ff" : "#64748b",
          borderWidth: selected ? 3 : (sector.participation_score ?? 0) > 0 ? 1.5 : 1,
          shadowBlur: selected ? 24 : 8,
          shadowColor: selected ? phase.color : "rgba(0, 0, 0, 0.2)",
        },
        label: { show: attentionDecision?.visible ?? false },
        attentionReasons: attentionDecision?.reasons ?? [],
        sector,
      };
    });
  return {
    animationDuration: 420,
    animationEasing: "cubicOut" as const,
    grid: { left: 64, right: 28, top: 42, bottom: 58, containLabel: false },
    tooltip: {
      trigger: "item",
      // ECharts 的 HTML tooltip 默认允许超出画布，但象限容器为了保持圆角边界会裁剪溢出内容。
      // 开启 confine 后，ECharts 会同时校正上、下、左、右四个方向的位置，确保完整悬浮框
      // 始终留在主图可视区域内，不会伸入回放控制条或排行榜后再被相邻组件遮挡。
      renderMode: "html" as const,
      confine: true,
      backgroundColor: "rgba(9, 18, 32, 0.96)",
      borderColor: "#30445f",
      borderWidth: 1,
      padding: 14,
      textStyle: { color: "#dce8f8", fontSize: 12 },
      formatter: (params: { data: { sector?: QuadrantSector; attentionReasons?: string[]; as_of_date?: string } }) => {
        if (!params.data.sector) return params.data.as_of_date ?? "历史轨迹";
        const sector = params.data.sector;
        const phase = getPhaseMeta(sector.phase_confirmed);
        const number = (value: number | null | undefined) => value == null ? "数据不足" : value.toFixed(2);
        const percent = (value: number | null | undefined) => value == null ? "数据不足" : `${(value * 100).toFixed(0)}%`;
        return [
          `<div class="chart-tooltip-title">${sector.sector_name}<span>${phase.label}</span></div>`,
          `<div class="chart-tooltip-reasons"><span>关注原因</span><strong>${params.data.attentionReasons?.length ? params.data.attentionReasons.join(" · ") : "当前截面常规观察"}</strong></div>`,
          `<div class="chart-tooltip-grid"><span>综合排名</span><b>${sector.composite_rank ?? "—"}</b><span>综合得分</span><b>${number(sector.composite_score)}</b>`,
          `<span>趋势速度</span><b>${number(sector.velocity_score)}</b><span>趋势加速度</span><b>${number(sector.acceleration_score)}</b>`,
          `<span>量能活跃度</span><b>${number(sector.volume_score)}</b><span>内部参与度</span><b>${number(sector.participation_score)}</b>`,
          `<span>阶段置信度</span><b>${percent(sector.phase_confidence)}</b><span>数据覆盖率</span><b>${percent(sector.coverage_ratio)}</b></div>`,
          `<div class="chart-tooltip-note">以上均为当日行业截面相对得分，不代表收益率</div>`,
        ].join("");
      },
    },
    xAxis: {
      type: "value", min: -1, max: 1, interval: 0.5, name: "趋势速度 / 相对强弱 →",
      nameLocation: "middle", nameGap: 38,
      axisLine: { lineStyle: { color: "#62728a" } },
      axisLabel: { color: "#7f8da3", fontSize: 11 },
      nameTextStyle: { color: "#aab8cc", fontSize: 12 },
      splitLine: { lineStyle: { color: "rgba(92, 112, 140, 0.16)" } },
    },
    yAxis: {
      type: "value", min: -1, max: 1, interval: 0.5, name: "趋势加速度 ↑",
      nameLocation: "middle", nameGap: 46,
      axisLine: { lineStyle: { color: "#62728a" } },
      axisLabel: { color: "#7f8da3", fontSize: 11 },
      nameTextStyle: { color: "#aab8cc", fontSize: 12 },
      splitLine: { lineStyle: { color: "rgba(92, 112, 140, 0.16)" } },
    },
    series: [{
      type: "scatter",
      data,
      symbolSize: (value: number[]) => Math.max(12, Math.min(46, 24 + value[2] * 18)),
      label: { position: "top", color: "#dce8f8", fontSize: 10, formatter: "{b}" },
      labelLayout: { hideOverlap: labelDensity !== "all", moveOverlap: "shiftY" },
      emphasis: { focus: "self", scale: 1.18 },
      markArea: {
        silent: true,
        itemStyle: { opacity: 1 },
        data: [
          [{ xAxis: 0, yAxis: 1, itemStyle: { color: "rgba(55, 214, 176, 0.035)" } }, { xAxis: 1, yAxis: 0 }],
          [{ xAxis: 0, yAxis: 0, itemStyle: { color: "rgba(240, 182, 90, 0.03)" } }, { xAxis: 1, yAxis: -1 }],
          [{ xAxis: -1, yAxis: 0, itemStyle: { color: "rgba(255, 114, 133, 0.03)" } }, { xAxis: 0, yAxis: -1 }],
          [{ xAxis: -1, yAxis: 1, itemStyle: { color: "rgba(145, 133, 255, 0.03)" } }, { xAxis: 0, yAxis: 0 }],
        ],
      },
    }, ...(trail.length ? [{
      type: "line" as const,
      name: `${selectedSectorName ?? "选中行业"}近10日尾迹`,
      data: trail.map((point) => point ? { value: [point.velocity_score, point.acceleration_score], as_of_date: point.as_of_date } : null),
      connectNulls: false,
      symbol: "circle",
      symbolSize: 6,
      lineStyle: { color: "#dce8f8", width: 2, opacity: .52, type: "dashed" as const },
      itemStyle: { color: "#dce8f8", opacity: .62 },
      z: 2,
    }] : [])],
  };
}

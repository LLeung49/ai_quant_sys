/** 板块轮动象限图的 ECharts 配置生成器。 */

import { getPhaseMeta } from "../labels";
import { getLifecycleMeta, getLifecycleReasonLabel, type LifecycleSectorFields } from "../lifecycle/meta";
import type { LabelDensity } from "../workbench/urlState";
import { rankAttention } from "./attentionPriority";
import {
  getShortTermChipText,
  getShortTermGlyphColor,
  getShortTermGlyphOffset,
  getShortTermGlyphPath,
  getShortTermGlyphShadowBlur,
  getShortTermGlyphSize,
  SHORT_TERM_GLYPH_BORDER,
  SHORT_TERM_GLYPH_BORDER_WIDTH,
  type ShortTermHaloInfo,
} from "./shortTermHalo";

export interface QuadrantSector extends LifecycleSectorFields {
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

const PHASE_BORDER_DEFAULT = "#64748b";

/**
 * 将当日短期横截面装配为带短期强度形状的 v1 象限配置。
 *
 * 输入:行业截面(v1),可选的回放尾迹与短期形状索引。
 * 输出:ECharts 配置对象,坐标固定 [-1, 1] 区间。
 *
 * P2.2 设计变更:
 * - 短期强度仅通过 Layer C (corner shape) 单通道编码;
 * - 主气泡本身的描边 / 阴影 / 透明度不再被覆盖,完整保留 v1 的
 *   参与度(描边色 / 描边宽)、阶段置信度(opacity)、综合分(phase 阴影)三套编码;
 * - Layer B 外圈光环已删除,避免与 Layer C 重复表达 intensity;
 * - Layer C 形状 size + shadow + path + color 同时表达强度档位与主标签类别。
 */
export function buildQuadrantOption(
  sectors: QuadrantSector[],
  selectedSectorName?: string | null,
  labelDensity: LabelDensity = "focus",
  trail: Array<QuadrantTrailPoint | null> = [],
  shortTermHaloByName?: ReadonlyMap<string, ShortTermHaloInfo>,
) {
  const attention = rankAttention(sectors, selectedSectorName, labelDensity);
  const attentionByName = new Map(attention.map((decision) => [decision.sector.sector_name, decision]));
  const haloByName = (() => {
    const local = new Map<string, ShortTermHaloInfo>();
    shortTermHaloByName?.forEach((value, key) => local.set(key, value));
    return local;
  })();

  // 主气泡区域:无论是否存在 halo,都使用同一份基于 v1 的描边 / 透明度 / 阴影规则。
  // 这是 P2.2 的关键决策:不再因为短期命中覆盖 v1 的可视编码。
  const data = sectors
    .filter((sector) => sector.velocity_score !== null && sector.acceleration_score !== null)
    .map((sector) => {
      const phase = getPhaseMeta(sector.phase_confirmed);
      const selected = sector.sector_name === selectedSectorName;
      const attentionDecision = attentionByName.get(sector.sector_name);
      const baseBorder = selected ? "#ffffff" : (sector.participation_score ?? 0) > 0 ? "#d7e7ff" : PHASE_BORDER_DEFAULT;
      const baseBorderWidth = selected ? 3 : (sector.participation_score ?? 0) > 0 ? 1.5 : 1;
      const baseShadowBlur = selected ? 24 : 8;
      const baseShadowColor = selected ? phase.color : "rgba(0, 0, 0, 0.2)";
      return {
        name: sector.sector_name,
        value: [sector.velocity_score!, sector.acceleration_score!, sector.volume_score ?? 0],
        itemStyle: {
          color: phase.color,
          opacity: selectedSectorName && !selected ? 0.2 : Math.max(0.48, sector.phase_confidence ?? 0.58),
          borderColor: baseBorder,
          borderWidth: baseBorderWidth,
          shadowBlur: baseShadowBlur,
          shadowColor: baseShadowColor,
        },
        label: { show: attentionDecision?.visible ?? false },
        attentionReasons: attentionDecision?.reasons ?? [],
        sector,
        halo: haloByName.get(sector.sector_name) ?? null,
      };
    });

  // Layer C:短期异动主标签形状。P2.2 后只剩这一层,size + shadow + color 三通道编码强度。
  // 仅保留存在 halo 且 primaryLabel + intensity 都有效的 sector;其他 sector 直接跳过,
  // 不会进入 chipSeriesData,也不会触发 Layer C 散点系列生成。
  const chipSeriesData = sectors
    .filter((sector) => sector.velocity_score !== null && sector.acceleration_score !== null)
    .map((sector) => {
      const halo = haloByName.get(sector.sector_name);
      const primaryLabel = halo?.primaryLabel ?? null;
      const intensity = halo?.intensity ?? null;
      if (!halo || !primaryLabel || !intensity) {
        return null;
      }
      // 用主气泡的实际半径决定 Layer C 形状的偏移距离,避免小型气泡与大型气泡上的形状错位。
      const bubbleRadius = Math.max(6, Math.min(23, (24 + (sector.volume_score ?? 0) * 18) / 2));
      const [glyphW, glyphH] = getShortTermGlyphSize(primaryLabel, intensity);
      return {
        name: `${sector.sector_name}-chip`,
        value: [sector.velocity_score, sector.acceleration_score, sector.volume_score ?? 0, primaryLabel],
        itemStyle: {
          color: getShortTermGlyphColor(primaryLabel, intensity),
          borderColor: SHORT_TERM_GLYPH_BORDER,
          borderWidth: SHORT_TERM_GLYPH_BORDER_WIDTH,
          shadowBlur: getShortTermGlyphShadowBlur(intensity),
          shadowColor: getShortTermGlyphColor(primaryLabel, intensity),
        },
        emphasis: { disabled: true },
        silent: false,
        symbol: `path://${getShortTermGlyphPath(primaryLabel, intensity)}` as const,
        symbolSize: [glyphW, glyphH] as [number, number],
        symbolOffset: [...getShortTermGlyphOffset(primaryLabel, bubbleRadius)] as [number, number],
        label: { show: false },
        sector,
        halo,
        z: 3,
      };
    })
    .filter((entry): entry is NonNullable<typeof entry> => entry !== null);

  const tooltipFormatter = (params: { data: { sector?: QuadrantSector; attentionReasons?: string[]; as_of_date?: string; halo?: ShortTermHaloInfo | null } }) => {
    if (!params.data.sector) return params.data.as_of_date ?? "历史尾迹";
    const sector = params.data.sector;
    const phase = getPhaseMeta(sector.phase_confirmed);
    const lifecycle = getLifecycleMeta(sector.lifecycle_state);
    const number = (value: number | null | undefined) => value == null ? "数据不足" : value.toFixed(2);
    const percent = (value: number | null | undefined) => value == null ? "数据不足" : (value * 100).toFixed(0) + "%";
    const ageText = sector.lifecycle_age == null ? "持续时间不足" : `${sector.lifecycle_age} 日`;
    const changedSuffix = sector.lifecycle_changed === true ? "<em>今日变化</em>" : "";
    const reasonText = getLifecycleReasonLabel(sector.lifecycle_reason);
    const reasonsText = params.data.attentionReasons?.length ? params.data.attentionReasons.join(" · ") : "当前截面常规观察";
    const halo = params.data.halo ?? null;
    const haloSuffix = halo && halo.isAnomaly
      ? `<div class="chart-tooltip-halo"><span>短期命中</span><b>${(halo.allLabels ?? []).map((label) => getShortTermChipText(label) ?? label).join(" / ") || "—"}</b><span>强度</span><b>${halo.intensity ? halo.intensity : "未标注"}</b></div>`
      : "";
    const lines = [
      `<div class="chart-tooltip-title">${sector.sector_name}<span>${phase.label}</span></div>`,
      `<div class="chart-tooltip-lifecycle"><span>${lifecycle.label}</span><b>${ageText}</b>${changedSuffix}<strong>${reasonText}</strong></div>`,
      `<div class="chart-tooltip-reasons"><span>关注原因</span><strong>${reasonsText}</strong></div>`,
      `<div class="chart-tooltip-grid"><span>综合排名</span><b>${sector.composite_rank ?? "—"}</b><span>综合得分</span><b>${number(sector.composite_score)}</b>`,
      `<span>趋势速度</span><b>${number(sector.velocity_score)}</b><span>趋势加速度</span><b>${number(sector.acceleration_score)}</b>`,
      `<span>量能活跃度</span><b>${number(sector.volume_score)}</b><span>内部参与度</span><b>${number(sector.participation_score)}</b>`,
      `<span>阶段置信度</span><b>${percent(sector.phase_confidence)}</b><span>数据覆盖比例</span><b>${percent(sector.coverage_ratio)}</b></div>`,
      haloSuffix,
      `<div class="chart-tooltip-note">以上均为当日行业截面相对得分,不代表收益口径</div>`,
    ];
    return lines.join("");
  };

  const baseSeries = {
    type: "scatter" as const,
    data,
    symbolSize: (value: number[]) => Math.max(12, Math.min(46, 24 + value[2] * 18)),
    label: { position: "top", color: "#dce8f8", fontSize: 10, formatter: "{b}" },
    labelLayout: { hideOverlap: labelDensity !== "all", moveOverlap: "shiftY" },
    emphasis: { focus: "self", scale: 1.18 },
    markArea: {
      silent: true,
      itemStyle: { opacity: 1 },
      data: [
        [{ xAxis: 0, yAxis: 1, itemStyle: { color: "rgba(240, 79, 95, 0.035)" } }, { xAxis: 1, yAxis: 0 }],
        [{ xAxis: 0, yAxis: 0, itemStyle: { color: "rgba(240, 182, 90, 0.03)" } }, { xAxis: 1, yAxis: -1 }],
        [{ xAxis: -1, yAxis: 0, itemStyle: { color: "rgba(38, 166, 154, 0.03)" } }, { xAxis: 0, yAxis: -1 }],
        [{ xAxis: -1, yAxis: 1, itemStyle: { color: "rgba(145, 133, 255, 0.03)" } }, { xAxis: 0, yAxis: 0 }],
      ],
    },
  };

  return {
    animationDuration: 420,
    animationEasing: "cubicOut" as const,
    grid: { left: 64, right: 28, top: 42, bottom: 58, containLabel: false },
    tooltip: {
      trigger: "item" as const,
      renderMode: "html" as const,
      confine: true,
      backgroundColor: "rgba(9, 18, 32, 0.96)",
      borderColor: "#30445f",
      borderWidth: 1,
      padding: 14,
      textStyle: { color: "#dce8f8", fontSize: 12 },
      formatter: tooltipFormatter,
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
    series: [
      baseSeries,
      ...(chipSeriesData.length ? [{
        type: "scatter" as const,
        name: "短期异动形状",
        data: chipSeriesData,
        animation: false,
        emphasis: { disabled: true },
        legendHoverLink: false,
        z: 3,
      }] : []),
      ...(trail.length ? [{
        type: "line" as const,
        name: `${selectedSectorName ?? "选中行业"}近10日尾迹`,
        data: trail.map((point) => point ? { value: [point.velocity_score, point.acceleration_score], as_of_date: point.as_of_date } : null),
        connectNulls: false,
        symbol: "circle",
        symbolSize: 6,
        lineStyle: { color: "#dce8f8", width: 2, opacity: .52, type: "dashed" as const },
        itemStyle: { color: "#dce8f8", opacity: .62 },
        z: 2,
      }] : []),
    ],
  };
}
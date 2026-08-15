/** v1 主象限图叠加短期异动光晕与形状标记的纯函数辅助。 */

import type { ShortTermSector } from "../short_term/api";
import { getIntensityMeta, parseLabelsCsv } from "../short_term/labels";

export type ShortTermIntensity = "intense" | "moderate" | "mild";

/** 短期光晕的归一化信息,与 sector 一对一;不同强度档位的纯函数映射表均以此结构为输入。 */
export interface ShortTermHaloInfo {
  intensity: ShortTermIntensity | null;
  primaryLabel: string | null;
  allLabels: string[];
  isAnomaly: boolean;
}

/**
 * 形状边框与填充色。
 *
 * 设计取舍:P2.1 + P2.2 之后,Layer B 外圈光环已删除,intensity 只通过 Layer C 形状
 * (color + size + shadow + shape-path)单通道编码,所以 SHORT_TERM_HALO_STYLE 缩减为单字段
 * (borderColor)。原有 shadow / border / halo 字段只为 Layer B 服务,一并删除。
 */
export interface ShortTermHaloStyle {
  /** 形状填充与短码颜色(与 INTENSITY_META[i].color 对齐)。 */
  color: string;
}

/**
 * 短期信号强度档位对应的颜色。
 *
 * 与 SHORT_TERM_LABEL_WHITELIST 的语义保持一致,intense=intense / moderate=moderate / mild=mild;
 * 颜色直接采用 INTENSITY_META 同档位的色,确保 Layer C 形状与 tooltip、图例的视觉一致。
 */
export const SHORT_TERM_HALO_STYLE: Record<ShortTermIntensity, ShortTermHaloStyle> = {
  intense: { color: "#ff6b35" },
  moderate: { color: "#f0b65a" },
  mild: { color: "#67c3a2" },
};

/** 主标签 Chip 的简短显示文本映射(只用于 tooltip 内文展示,不再渲染在主气泡上)。 */
export const SHORT_TERM_CHIP_TEXT: Record<string, string> = {
  pulse_up: "脉冲↑",
  pulse_down: "脉冲↓",
  extreme_up: "极端↑",
  extreme_down: "极端↓",
  volume_spike: "量异",
  limit_cluster: "涨停",
  limit_panic: "跌停",
  short_rebound_candidate: "反弹",
  short_breakdown_candidate: "破位",
};

/**
 * Chip 主标签的优先级排序,与 SHORT_TERM_LABEL_PRIORITY 区分:
 * - SHORT_TERM_LABEL_PRIORITY 用于异动榜的纵向排序与折叠优先级;
 * - 本表用于"哪个标签最该被形状显示",更看重信号主导性:脉冲上涨 > 涨停集群 > 脉冲下跌 > ...
 */
const PRIMARY_LABEL_ORDER: readonly string[] = [
  "pulse_up",
  "limit_cluster",
  "pulse_down",
  "limit_panic",
  "extreme_up",
  "extreme_down",
  "volume_spike",
  "short_rebound_candidate",
  "short_breakdown_candidate",
];

/** 给定一组标签 id,按 PRIMARY_LABEL_ORDER 顺序选择第一个出现的标签。 */
export function pickPrimaryShortTermLabel(labels: readonly string[]): string | null {
  for (const candidate of PRIMARY_LABEL_ORDER) {
    if (labels.includes(candidate)) return candidate;
  }
  return null;
}

/** 校验短期 intensity 字段是否属于已知三档之一。 */
export function normalizeShortTermIntensity(value: string | null | undefined): ShortTermIntensity | null {
  if (value === "intense" || value === "moderate" || value === "mild") return value;
  return null;
}

/** 解析单个 sector 的短期异动光晕信息(纯函数,无 IO)。 */
export function buildShortTermHaloInfo(sector: {
  score_eligible?: boolean | null | number;
  short_term_intensity?: string | null;
  short_term_labels?: string | null;
}): ShortTermHaloInfo {
  if (!sector || sector.score_eligible === false || sector.score_eligible === 0) {
    return { intensity: null, primaryLabel: null, allLabels: [], isAnomaly: false };
  }
  const allLabels = parseLabelsCsv(sector.short_term_labels ?? null);
  const intensity = normalizeShortTermIntensity(sector.short_term_intensity ?? null);
  const isAnomaly = intensity !== null || allLabels.length > 0;
  const primaryLabel = isAnomaly ? pickPrimaryShortTermLabel(allLabels) : null;
  return { intensity, primaryLabel, allLabels, isAnomaly };
}

/**
 * 给定 sectors 列表,按 sector_name 索引出所有光晕信息。
 */
export function buildShortTermHaloIndex<T extends { sector_name: string }>(
  sectors: readonly T[],
): Map<string, ShortTermHaloInfo> {
  const out = new Map<string, ShortTermHaloInfo>();
  for (const sector of sectors) {
    out.set(sector.sector_name, buildShortTermHaloInfo(sector as unknown as ShortTermSector));
  }
  return out;
}

/** 取标签 Chip 的文本;无匹配则安全回退到 id 原文。仅供 tooltip 使用。 */
export function getShortTermChipText(label: string | null | undefined): string | null {
  if (!label) return null;
  return SHORT_TERM_CHIP_TEXT[label] ?? label;
}

/** 取某一 intensity 对应的填充色;无匹配返回 null(不展示形状)。 */
export function getShortTermHaloStyle(intensity: ShortTermIntensity | null | undefined): ShortTermHaloStyle | null {
  if (!intensity) return null;
  return SHORT_TERM_HALO_STYLE[intensity] ?? null;
}

/** 取强度档位的中文标签,本质是 getIntensityMeta 的便捷封装。 */
export function getShortTermIntensityLabel(intensity: ShortTermIntensity | null | undefined): string {
  return getIntensityMeta(intensity ?? "none").label;
}

/* ====================================================================
 * 形状 (glyph) 编码:用 SVG path 替换原本的矩形文字 chip
 * ====================================================================
 *
 * P2.2 之后的设计:
 * - 不再渲染矩形文字 chip,改为 SVG path:// 形状;
 * - pulse_up / pulse_down 通过 path 尖锐度编码 intensity;
 * - 其它标签的形状固定,但通过 size (在 getShortTermGlyphSize 中按 intensity 缩放) 表达 intensity;
 * - 主气泡本身的描边 / 阴影 / 透明度不再被覆盖,保留 v1 的参与度 / 阶段置信度 / 综合分编码;
 * - Layer B 外圈光环已删除,Layer C 形状就是唯一的 intensity 通道。
 */

/**
 * 形状路径字典。键 = 主标签 id;值 = 14×14 viewBox 的 SVG path data。
 *
 * rebound / breakdown 重新设计为"三角 + 同侧小方块":
 * - rebound:上三角 + 下方小方块 → "先低位后上涨";
 * - breakdown:下三角 + 上方小方块 → "先高位后下跌";
 * 该形状比 hook 更直观,在 12px 下仍可识别。
 *
 * 高宽比编码策略:
 * - pulse_up / pulse_down:形状 path 内嵌 sharp / medium / flat 三档;
 * - 其余标签的形状固定,intensity 由 getShortTermGlyphSize 的 size 缩放承载。
 */
export const SHORT_TERM_GLYPH_PATHS: Record<string, string> = {
  // pulse_up —— 上三角形,顶点越尖代表强度越高
  pulse_up_intense: "M7,0 L10,12 L4,12 Z",
  pulse_up_moderate: "M7,2 L11,12 L3,12 Z",
  pulse_up_mild: "M7,5 L13,12 L1,12 Z",

  // pulse_down —— 下三角形,顶点越尖代表强度越高
  pulse_down_intense: "M7,14 L10,2 L4,2 Z",
  pulse_down_moderate: "M7,12 L11,2 L3,2 Z",
  pulse_down_mild: "M7,9 L13,2 L1,2 Z",

  // extreme_up —— 比 pulse_up_intense 更窄的"针尖"形
  extreme_up: "M7,0 L9,13 L5,13 Z",

  // extreme_down —— 同上的下指版本
  extreme_down: "M7,14 L9,1 L5,1 Z",

  // volume_spike —— 垂直矩形,模拟成交量的"立柱"
  volume_spike: "M5,2 H10 V12 H5 Z",

  // limit_cluster —— 双上峰(W 形),直观表达"涨停集群"
  limit_cluster: "M0,14 L4,3 L7,8 L10,3 L14,14 Z",

  // limit_panic —— 双下峰(M 形倒置)
  limit_panic: "M0,0 L4,11 L7,6 L10,11 L14,0 Z",

  // short_rebound_candidate —— 上三角 + 下方小方块("先低位后上涨")
  short_rebound_candidate: "M7,1 L12,9 L2,9 Z M5,11 L9,11 L9,13 L5,13 Z",

  // short_breakdown_candidate —— 下三角 + 上方小方块("先高位后下跌")
  short_breakdown_candidate: "M7,13 L12,5 L2,5 Z M5,1 L9,1 L9,3 L5,3 Z",
};

/**
 * 形状基础尺寸(不含 intensity 缩放)。
 *
 * - pulse_up / pulse_down / rebound / breakdown: 12×13;
 * - extreme_up / extreme_down:10×14 更窄;
 * - volume_spike:6×13 垂直立柱;
 * - limit_cluster / limit_panic:14×12 多峰宽度;
 *
 * 这些尺寸会在 getShortTermGlyphSize 中按 intensity 缩放。
 */
export function getShortTermGlyphBaseSize(primaryLabel: string): readonly [number, number] {
  switch (primaryLabel) {
    case "volume_spike":
      return [6, 13];
    case "limit_cluster":
    case "limit_panic":
      return [14, 12];
    case "extreme_up":
    case "extreme_down":
      return [10, 14];
    case "pulse_up":
    case "pulse_down":
    case "short_rebound_candidate":
    case "short_breakdown_candidate":
    default:
      return [12, 13];
  }
}

/**
 * 形状在不同 intensity 下的 size 缩放系数。
 *
 * - pulse_up / pulse_down:intensity 已由 path 尖锐度承载,size 不再缩放;
 * - 其余标签 (extreme_*, volume_spike, limit_*, rebound, breakdown):intense=1.10×
 *   moderate=0.95× mild=0.80×,使 Layer C 形状成为唯一的 intensity 通道。
 */
export const SHORT_TERM_GLYPH_INTENSITY_SCALE: Record<ShortTermIntensity, number> = {
  intense: 1.10,
  moderate: 0.95,
  mild: 0.80,
};

const PULSE_LABELS = new Set(["pulse_up", "pulse_down"]);

/**
 * 取主标签对应的 SVG path。pulse_up / pulse_down 需要根据 intensity 选择不同的尖锐度档。
 */
export function getShortTermGlyphPath(primaryLabel: string, intensity: ShortTermIntensity): string {
  if (PULSE_LABELS.has(primaryLabel)) {
    const key = `${primaryLabel}_${intensity}`;
    return SHORT_TERM_GLYPH_PATHS[key] ?? SHORT_TERM_GLYPH_PATHS[`${primaryLabel}_mild`];
  }
  return SHORT_TERM_GLYPH_PATHS[primaryLabel] ?? SHORT_TERM_GLYPH_PATHS.pulse_up_mild;
}

/**
 * 取形状在 (主标签, intensity) 下的最终尺寸。
 *
 * - pulse_up / pulse_down:固定尺寸,size 不承载 intensity (由 path 尖锐度承载);
 * - 其它标签:基础尺寸 × intensity 缩放系数;
 * - 未知 label 安全回退到 pulse 家族基础尺寸 × mild 缩放,不抛出。
 */
export function getShortTermGlyphSize(
  primaryLabel: string,
  intensity: ShortTermIntensity,
): readonly [number, number] {
  const base = getShortTermGlyphBaseSize(primaryLabel);
  if (PULSE_LABELS.has(primaryLabel)) return base;
  const scale = SHORT_TERM_GLYPH_INTENSITY_SCALE[intensity] ?? 0.8;
  return [Math.max(6, Math.round(base[0] * scale)), Math.max(6, Math.round(base[1] * scale))];
}

/**
 * 形状阴影强度,与 intensity 同步;避免 Layer B 删除后强度信息完全丢失。
 *
 * intense=8 / moderate=6 / mild=4,在 14px 形状上呈现细微但可辨的发光差异。
 */
export function getShortTermGlyphShadowBlur(intensity: ShortTermIntensity): number {
  if (intensity === "intense") return 8;
  if (intensity === "moderate") return 6;
  return 4;
}

/** 取形状填充色,默认与 halo style color 保持一致。 */
export function getShortTermGlyphColor(intensity: ShortTermIntensity): string {
  return SHORT_TERM_HALO_STYLE[intensity].color;
}

/**
 * 形状描边色:相对于 phase 色面提供衬底色,确保在浅色与深色 phase 背景上均可辨识。
 */
export const SHORT_TERM_GLYPH_BORDER: string = "rgba(12, 25, 43, 0.85)";

/** 形状描边宽度。1.2 像素足以与所有 phase 色面分隔,又不喧宾夺主。 */
export const SHORT_TERM_GLYPH_BORDER_WIDTH: number = 1.2;

/**
 * 形状在主气泡上的相对位置。[dx, dy] = 在气泡中心的基础上,向外偏移。
 *
 * Layer B 外圈光环删除后,Layer C 形状成为唯一异动标记,因此需要稳定在右上角附近,
 * 与主气泡轮廓保持一致间距。dx 与 dy 都跟随 bubbleRadius 调整,
 * 避免小型气泡与大型气泡上的形状位置错位。
 */
export function getShortTermGlyphOffset(primaryLabel: string, bubbleRadius: number): readonly [number, number] {
  return [bubbleRadius + 2, -(bubbleRadius * 0.4 + 5)];
}
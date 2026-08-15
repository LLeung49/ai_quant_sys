/**
 * 5 日连续性 strip 的纯函数:把 fetchShortTermHistory 的响应转换成 strip 表格所需的行数据。
 *
 * 设计取舍:
 * - history.points 用 `.passthrough()` 通过 Zod 校验,实际返回可能附带 `as_of_date` 字段;
 * - 但 schema 本身不显式声明 as_of_date,所以这里通过类型断言读取 raw 字段;
 * - 主标签按 SHORT_TERM_LABEL_PRIORITY 顺序选择,与 Layer C chip 保持一致;
 * - intensity 归一化:仅识别 intense / moderate / mild,其它一律 null;
 * - 当 history 为 null 或行业不存在时返回空数组,strip UI 自适应空态。
 *
 * 字段语义:
 * - as_of_date:YYYY-MM-DD;
 * - primaryLabel:strip 主标签对应的 id,可空(行业当日无短期信号);
 * - intensity:三档之一或 null;
 * - composite:短期综合分绝对值,可空;
 * - labels:命中标签的去重保序数组;
 * - ret_1 / rs_1 / rvol_1_20:tooltip 用 raw 字段。
 */

import type { ShortTermHistoryResponse } from "../short_term/api";
import { orderLabelsByPriority, parseLabelsCsv } from "../short_term/labels";

export type StripIntensity = "intense" | "moderate" | "mild";

export interface StripCell {
  as_of_date: string;
  primaryLabel: string | null;
  intensity: StripIntensity | null;
  composite: number | null;
  labels: string[];
  ret_1: number | null;
  rs_1: number | null;
  rvol_1_20: number | null;
}

/** 默认窗口天数:5 个交易日。 */
export const STRIP_WINDOW_DAYS = 5;

/** 把原始 intensity 字段归一化为已知三档之一;未知 / 空 / none 一律 null。 */
export function normalizeStripIntensity(value: unknown): StripIntensity | null {
  if (value === "intense" || value === "moderate" || value === "mild") return value;
  return null;
}

/**
 * 读取 history 中某行业的 strip 序列(按 as_of_date desc 取前 days 个交易日)。
 *
 * 行为:
 * - history 为 null → [];
 * - 行业不在 history.points → [];
 * - 按 as_of_date 倒序排序后取前 days 条;
 * - 每行 emit StripCell:as_of_date / primaryLabel / intensity / composite / labels / ret_1 / rs_1 / rvol_1_20;
 * - primaryLabel:parseLabelsCsv → orderLabelsByPriority → [0] / null;
 * - intensity:normalizeStripIntensity;
 * - labels:parseLabelsCsv(去重保序);
 *
 * as_of_date 字段兼容性:短期 history API 的 schema 未显式声明 as_of_date(依赖 passthrough),
 * 故通过 raw 字段读取;若不存在则使用 ""。
 */
export function buildShortTermStripRow(
  history: ShortTermHistoryResponse | null,
  sectorName: string,
  asOfDate: string,
  days: number = STRIP_WINDOW_DAYS,
): StripCell[] {
  if (!history || !sectorName) return [];
  const points = history.points ?? [];
  const filtered = points.filter((point) => {
    const rawName = (point as { sector_name?: string }).sector_name;
    return rawName === sectorName;
  });
  if (filtered.length === 0) return [];

  // 排序:as_of_date desc;asOfDate 仅作为 "保留到哪天" 的语义锚点,即使晚于历史最新日也按 desc 取前 days。
  const sorted = [...filtered].sort((a, b) => {
    const ad = String((a as { as_of_date?: string }).as_of_date ?? "");
    const bd = String((b as { as_of_date?: string }).as_of_date ?? "");
    if (ad === bd) return 0;
    return ad < bd ? 1 : -1;
  });
  const take = sorted.slice(0, Math.max(0, days));

  return take.map((point): StripCell => {
    const asOfDateRaw = String((point as { as_of_date?: string }).as_of_date ?? "");
    const labelsRaw = (point as { short_term_labels?: string | null }).short_term_labels ?? null;
    const labels = parseLabelsCsv(labelsRaw);
    const ordered = orderLabelsByPriority(labels);
    const intensityRaw = (point as { short_term_intensity?: string | null }).short_term_intensity ?? null;
    const compositeRaw = (point as { short_term_composite?: number | null }).short_term_composite ?? null;
    const retRaw = (point as { ret_1?: number | null }).ret_1 ?? null;
    const rsRaw = (point as { rs_1?: number | null }).rs_1 ?? null;
    const rvolRaw = (point as { rvol_1_20?: number | null }).rvol_1_20 ?? null;
    return {
      as_of_date: asOfDateRaw,
      primaryLabel: ordered[0] ?? null,
      intensity: normalizeStripIntensity(intensityRaw),
      composite: compositeRaw,
      labels,
      ret_1: retRaw,
      rs_1: rsRaw,
      rvol_1_20: rvolRaw,
    };
  });
}

/** 取出 strip cell 的 tooltip 详情。供悬停态展示用。 */
export function describeStripCell(cell: StripCell): {
  ret_1: number | null;
  rs_1: number | null;
  rvol_1_20: number | null;
  labels: string[];
} {
  return {
    ret_1: cell.ret_1,
    rs_1: cell.rs_1,
    rvol_1_20: cell.rvol_1_20,
    labels: [...cell.labels],
  };
}
import type { ShortTermSector } from "./api";
import { parseLabelsCsv } from "./labels";

export const NEXT_DAY_WATCH_GROUP_ORDER = [
  "strength_follow_through",
  "panic_reversal_watch",
  "short_rebound_watch",
  "short_breakdown_watch",
] as const;

export type NextDayWatchGroupId = (typeof NEXT_DAY_WATCH_GROUP_ORDER)[number];

export interface NextDayWatchGroup {
  id: NextDayWatchGroupId;
  sectors: ShortTermSector[];
}

function isEligible(sector: ShortTermSector): boolean {
  return Boolean(sector.score_eligible);
}

function hasAll(labels: Set<string>, required: readonly string[]): boolean {
  return required.every((label) => labels.has(label));
}

function matchesGroup(sector: ShortTermSector, groupId: NextDayWatchGroupId): boolean {
  if (!isEligible(sector)) return false;
  const labels = new Set(parseLabelsCsv(sector.short_term_labels));
  switch (groupId) {
    case "strength_follow_through":
      return hasAll(labels, ["pulse_up", "volume_spike"]);
    case "panic_reversal_watch":
      return hasAll(labels, ["pulse_down", "volume_spike"]) || labels.has("limit_panic");
    case "short_rebound_watch":
      return labels.has("short_rebound_candidate");
    case "short_breakdown_watch":
      return labels.has("short_breakdown_candidate");
  }
}

function comparableScore(value: number | null | undefined): number {
  return typeof value === "number" && Number.isFinite(value) ? value : Number.NEGATIVE_INFINITY;
}

function comparableRank(value: number | null | undefined): number {
  return typeof value === "number" && Number.isFinite(value) ? value : Number.POSITIVE_INFINITY;
}

function compareSectors(left: ShortTermSector, right: ShortTermSector): number {
  const scoreDelta = comparableScore(right.short_term_composite) - comparableScore(left.short_term_composite);
  if (scoreDelta !== 0) return scoreDelta;
  const rankDelta = comparableRank(left.short_term_composite_rank) - comparableRank(right.short_term_composite_rank);
  if (rankDelta !== 0) return rankDelta;
  return left.sector_name.localeCompare(right.sector_name, "zh-CN");
}

/**
 * 将同日的有效短期异动快照映射为非排他的研究观察情景。
 * 该函数只复用既有标签，不输出投资建议或改变原始板块对象。
 */
export function buildNextDayWatchGroups(sectors: ShortTermSector[]): NextDayWatchGroup[] {
  return NEXT_DAY_WATCH_GROUP_ORDER.map((id) => ({
    id,
    sectors: sectors.filter((sector) => matchesGroup(sector, id)).sort(compareSectors),
  }));
}

/** 气泡标签的稳定关注优先级与用户可见解释。 */
import type { LabelDensity } from "../workbench/urlState";

export interface AttentionSector {
  sector_name: string;
  composite_rank?: number | null;
  acceleration_score?: number | null;
  phase_confirmed?: string | null;
  phase_changed?: number | boolean | null;
  rank_change_1d?: number | null;
  rank_change_5d?: number | null;
}

export interface AttentionDecision<T extends AttentionSector> {
  sector: T;
  priority: number;
  reasons: string[];
  visible: boolean;
}

const densityLimit: Record<LabelDensity, number> = { compact: 14, focus: 30, all: Number.POSITIVE_INFINITY };

/**
 * 计算行业标签的显示优先级和解释原因。
 *
 * 输入：同日行业列表、当前跟踪行业和标签密度。
 * 输出：保持输入顺序的决策列表；``visible`` 由稳定分数排序决定，选中行业强制保留。
 */
export function rankAttention<T extends AttentionSector>(sectors: T[], selectedSectorName: string | null | undefined, density: LabelDensity): AttentionDecision<T>[] {
  const scored = sectors.map((sector, inputIndex) => {
    let priority = Math.max(0, 120 - (sector.composite_rank ?? 120));
    const reasons: string[] = [];
    if (sector.sector_name === selectedSectorName) { priority += 10_000; reasons.push("正在跟踪"); }
    if ((sector.composite_rank ?? 999) <= 10) { priority += 320 - (sector.composite_rank ?? 10) * 5; reasons.push("综合排名前10"); }
    else if ((sector.composite_rank ?? 999) <= 30) { priority += 120; reasons.push("综合排名靠前"); }
    if (Boolean(sector.phase_changed)) { priority += 260; reasons.push("阶段刚切换"); }
    const change1d = sector.rank_change_1d ?? 0;
    if (Math.abs(change1d) >= 8) { priority += 210 + Math.min(80, Math.abs(change1d)); reasons.push(`1日排名${change1d > 0 ? "上升" : "下降"}${Math.abs(change1d)}位`); }
    const change5d = sector.rank_change_5d ?? 0;
    if (Math.abs(change5d) >= 20) { priority += 120 + Math.min(60, Math.abs(change5d) / 2); reasons.push(`5日排名${change5d > 0 ? "上升" : "下降"}${Math.abs(change5d)}位`); }
    if (Math.abs(sector.acceleration_score ?? 0) >= 0.75) { priority += 190; reasons.push("加速度处于极值区"); }
    if (sector.phase_confirmed === "accel_down") { priority += 170; reasons.push("加速走弱"); }
    if (sector.phase_confirmed === "reversal_confirmed") { priority += 160; reasons.push("修复确认"); }
    return { sector, priority, reasons, inputIndex, visible: false };
  });
  const visibleIndexes = new Set(scored.slice().sort((left, right) => right.priority - left.priority || left.inputIndex - right.inputIndex).slice(0, densityLimit[density]).map((item) => item.inputIndex));
  return scored.map(({ inputIndex, ...item }) => ({ ...item, visible: visibleIndexes.has(inputIndex) }));
}

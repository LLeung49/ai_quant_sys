/** 短期异动标签与强度的视觉语义（与方案文档 §10.3 一致）。 */

export const SHORT_TERM_LABEL_META: Record<string, { label: string; color: string; softColor: string; description: string }> = {
  pulse_up: {
    label: "单日脉冲上涨",
    color: "#ff8547",
    softColor: "rgba(255, 133, 71, 0.18)",
    description: "板块当日相对市场跑赢且上涨广度显著高于中性，关注量能延续。",
  },
  pulse_down: {
    label: "单日脉冲下跌",
    color: "#ff5470",
    softColor: "rgba(255, 84, 112, 0.18)",
    description: "板块当日相对市场跑输且上涨广度显著低于中性，关注风险扩散。",
  },
  extreme_up: {
    label: "单日极端上涨",
    color: "#ffa040",
    softColor: "rgba(255, 160, 64, 0.18)",
    description: "板块当日绝对涨幅超过 ±3% 阈值。",
  },
  extreme_down: {
    label: "单日极端下跌",
    color: "#ff3d62",
    softColor: "rgba(255, 61, 98, 0.18)",
    description: "板块当日绝对跌幅超过 ±3% 阈值。",
  },
  volume_spike: {
    label: "量能异动",
    color: "#f5b342",
    softColor: "rgba(245, 179, 66, 0.18)",
    description: "板块当日成交额相对 20 日均值显著放大。",
  },
  limit_cluster: {
    label: "涨停集群",
    color: "#ff6b35",
    softColor: "rgba(255, 107, 53, 0.18)",
    description: "板块当日涨停家数 ≥ 阈值，且跌停极少。",
  },
  limit_panic: {
    label: "跌停集群",
    color: "#e0224d",
    softColor: "rgba(224, 34, 77, 0.18)",
    description: "板块当日跌停家数 ≥ 阈值，且涨停极少。",
  },
  short_rebound_candidate: {
    label: "短期反弹候选",
    color: "#67c3a2",
    softColor: "rgba(103, 195, 162, 0.18)",
    description: "5 日相对弱势中当日突然转强，V 形反弹观察期。",
  },
  short_breakdown_candidate: {
    label: "短期走弱候选",
    color: "#c47ac0",
    softColor: "rgba(196, 122, 192, 0.18)",
    description: "5 日相对强势中当日突然转弱，关注是否破位。",
  },
};

/** 标签展示顺序：靠前的标签在前端异动榜中优先展示。 */
export const SHORT_TERM_LABEL_PRIORITY: readonly string[] = [
  "pulse_up",
  "pulse_down",
  "extreme_up",
  "extreme_down",
  "limit_cluster",
  "limit_panic",
  "volume_spike",
  "short_rebound_candidate",
  "short_breakdown_candidate",
];

/** 获取任一标签的展示元信息；未知值安全回退到原值。 */
export function getShortTermLabelMeta(label: string | null | undefined) {
  if (!label) return null;
  return SHORT_TERM_LABEL_META[label] ?? null;
}

/** 解析逗号分隔的标签字符串为去重、保序的数组。 */
export function parseLabelsCsv(raw: string | null | undefined): string[] {
  if (!raw) return [];
  const seen = new Set<string>();
  const ordered: string[] = [];
  for (const part of raw.split(",")) {
    const trimmed = part.trim();
    if (!trimmed || seen.has(trimmed)) continue;
    seen.add(trimmed);
    ordered.push(trimmed);
  }
  return ordered;
}

export const INTENSITY_META: Record<string, { label: string; color: string; softColor: string }> = {
  intense: { label: "强异动", color: "#ff6b35", softColor: "rgba(255, 107, 53, 0.16)" },
  moderate: { label: "中等异动", color: "#f0b65a", softColor: "rgba(240, 182, 90, 0.16)" },
  mild: { label: "轻度异动", color: "#67c3a2", softColor: "rgba(103, 195, 162, 0.16)" },
  none: { label: "无异动", color: "#8795ab", softColor: "rgba(135, 149, 171, 0.14)" },
};

/** 获取任一强度档位的展示元数据；未知值安全回退到 none。 */
export function getIntensityMeta(intensity: string | null | undefined) {
  const key = intensity ?? "none";
  return INTENSITY_META[key] ?? INTENSITY_META.none;
}

/** 把 CSV 标签按优先级排序，供前端展示使用。 */
export function orderLabelsByPriority(labels: string[]): string[] {
  const rank = new Map(SHORT_TERM_LABEL_PRIORITY.map((label, index) => [label, index] as const));
  return [...labels].sort((left, right) => (rank.get(left) ?? 99) - (rank.get(right) ?? 99));
}

/**
 * 次日研究观察候选情景的展示元信息（仅用于研究与提示，不构成交易信号等级）。
 *
 * 关键字段：
 * - `title`：情景的中文展示名；
 * - `tone`：配色基调，与短期强度配色保持区分；
 * - `iconName`：Lucide 图标名，由 `NextDayWatchPanel` 解析为组件；
 * - `description`：卡片头部的一句话研究说明；
 * - `hint`：悬停展开的细则。
 */
export interface NextDayWatchGroupMeta {
  title: string;
  tone: "warm" | "rose" | "teal" | "violet";
  iconName: "trending-up" | "siren" | "corner-down-left" | "corner-down-right";
  description: string;
  hint: string;
}

export const NEXT_DAY_WATCH_GROUP_META: Record<string, NextDayWatchGroupMeta> = {
  strength_follow_through: {
    title: "强势跟进观察",
    tone: "warm",
    iconName: "trending-up",
    description: "相对强势与量能同步出现，次日重点复核延续性与广度。",
    hint: "同时命中 pulse_up + volume_spike 的板块；用于辅助判断次日是否仍具备动量与资金配合。",
  },
  panic_reversal_watch: {
    title: "恐慌修复观察",
    tone: "rose",
    iconName: "siren",
    description: "下行压力或跌停集群已显化，次日重点复核恐慌是否扩散或收敛。",
    hint: "同时含 pulse_down + volume_spike，或独立命中 limit_panic 的板块；用于辅助判断次日情绪是否缓解。",
  },
  short_rebound_watch: {
    title: "V 形反弹观察",
    tone: "teal",
    iconName: "corner-down-left",
    description: "前 5 日相对弱势后出现当日转强，次日重点复核反弹质量。",
    hint: "命中 short_rebound_candidate 的板块；用于辅助判断弱势板块是否完成反转。",
  },
  short_breakdown_watch: {
    title: "破位警惕观察",
    tone: "violet",
    iconName: "corner-down-right",
    description: "前 5 日相对强势后出现当日转弱，次日重点复核风险是否延续。",
    hint: "命中 short_breakdown_candidate 的板块；用于辅助判断强势板块是否开始走弱。",
  },
};

/** 获取候选情景的展示元信息；未知 id 安全回退到原 id 的空对象。 */
export function getNextDayWatchGroupMeta(id: string): NextDayWatchGroupMeta {
  return (
    NEXT_DAY_WATCH_GROUP_META[id] ?? {
      title: id,
      tone: "warm",
      iconName: "trending-up",
      description: "",
      hint: "",
    }
  );
}

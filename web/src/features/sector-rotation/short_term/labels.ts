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

/** 获取任一标签的展示元数据；未知值安全回退到原值。 */
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

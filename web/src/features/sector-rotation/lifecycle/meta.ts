export const LIFECYCLE_STATES = ["repair", "emerging", "trending", "crowded", "divergence", "exit", "neutral"] as const;
export type LifecycleState = typeof LIFECYCLE_STATES[number];
export type LifecycleFilter = "all" | LifecycleState | "repair_or_emerging" | "risk";

export interface LifecycleSectorFields {
  lifecycle_state?: string | null;
  lifecycle_reason?: string | null;
  lifecycle_changed?: boolean | null;
  lifecycle_age?: number | null;
}

export interface LifecycleMeta {
  state: LifecycleState | "unknown";
  label: string;
  description: string;
  color: string;
  softColor: string;
}

export const LIFECYCLE_META: Record<LifecycleState, LifecycleMeta> = {
  repair: { state: "repair", label: "修复观察", description: "弱势阶段出现初步修复迹象，仍需观察确认。", color: "#8b9cff", softColor: "rgba(139,156,255,.12)" },
  emerging: { state: "emerging", label: "初步启动", description: "修复已经确认或强势尚未出现风险警告。", color: "#56c7d9", softColor: "rgba(86,199,217,.12)" },
  trending: { state: "trending", label: "趋势运行", description: "相对强势与趋势加速同时存在。", color: "#37d6b0", softColor: "rgba(55,214,176,.12)" },
  crowded: { state: "crowded", label: "强势拥挤", description: "强势持续时间较长，进入拥挤观察区。", color: "#f0b65a", softColor: "rgba(240,182,90,.12)" },
  divergence: { state: "divergence", label: "强弱背离", description: "强势降温且参与度或排名同步转弱。", color: "#ff8a78", softColor: "rgba(255,138,120,.12)" },
  exit: { state: "exit", label: "加速转弱", description: "趋势已经进入加速走弱状态。", color: "#ff7285", softColor: "rgba(255,114,133,.12)" },
  neutral: { state: "neutral", label: "方向未明", description: "当前证据不足以归入其他观察状态。", color: "#7f8da3", softColor: "rgba(127,141,163,.12)" },
};

export const LIFECYCLE_REASON_LABELS: Record<string, string> = {
  score_ineligible: "评分证据不足",
  phase_accel_down: "确认阶段为加速走弱",
  decel_up_with_fading_breadth_or_rank: "强势降温且参与度或排名转弱",
  decel_up_with_extended_top10_duration: "强势降温且近 20 日排名前十时长较长",
  phase_accel_up: "确认阶段为加速走强",
  reversal_confirmed: "确认阶段为修复确认",
  repair_phase: "原始阶段为弱势修复观察",
  decel_up_without_warning: "强势降温但暂未出现风险警告",
  no_lifecycle_signal: "暂无明确 Lifecycle 信号",
};

export const UNKNOWN_LIFECYCLE_META: LifecycleMeta = {
  state: "unknown", label: "未知状态", description: "Lifecycle 状态字段暂未识别。", color: "#7f8da3", softColor: "rgba(127,141,163,.12)",
};

export const LIFECYCLE_FILTER_VALUES: readonly LifecycleFilter[] = ["all", ...LIFECYCLE_STATES, "repair_or_emerging", "risk"];

export function getLifecycleMeta(value: string | null | undefined): LifecycleMeta {
  return LIFECYCLE_META[value as LifecycleState] ?? UNKNOWN_LIFECYCLE_META;
}

export function getLifecycleReasonLabel(value: string | null | undefined): string {
  if (!value) return "状态原因暂不可用";
  return LIFECYCLE_REASON_LABELS[value] ?? "原因字段暂未识别";
}

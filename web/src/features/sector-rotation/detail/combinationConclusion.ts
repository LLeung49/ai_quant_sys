import { getPhaseMeta, PHASE_META } from "../labels";
import { getLifecycleMeta } from "../lifecycle/meta";

export type CombinationConclusionTone = "positive" | "watch" | "risk" | "neutral";

export interface CombinationConclusion {
  title: string;
  guidance: string;
  tone: CombinationConclusionTone;
}

const FALLBACK_GUIDANCE = "当前证据不足，建议继续观察后续连续变化。";

/**
 * Combines the existing phase and lifecycle labels into a display-only insight.
 * This deliberately contains no trading instruction or data fetching.
 */
export function getCombinationConclusion(
  phase: string | null | undefined,
  lifecycle: string | null | undefined,
): CombinationConclusion {
  const phaseMeta = getPhaseMeta(phase);
  const lifecycleMeta = getLifecycleMeta(lifecycle);
  const normalizedPhase = phase ?? "neutral";

  if (!(normalizedPhase in PHASE_META) || lifecycleMeta.state === "unknown") {
    return {
      title: `${phaseMeta.label} · ${lifecycleMeta.label}`,
      guidance: FALLBACK_GUIDANCE,
      tone: "neutral",
    };
  }

  const key = `${normalizedPhase}:${lifecycleMeta.state}`;

  if (key === "reversal_confirmed:emerging") {
    return {
      title: `${phaseMeta.label} · ${lifecycleMeta.label}`,
      guidance: "可进入重点跟踪，等待排名与市场环境共同确认。",
      tone: "positive",
    };
  }

  if (key === "decel_up:divergence") {
    return {
      title: `${phaseMeta.label} · ${lifecycleMeta.label}`,
      guidance: "强势降温且强弱背离，避免追涨，等待排名与市场环境重新确认。",
      tone: "risk",
    };
  }

  const { guidance, tone } = getLifecycleGuidance(lifecycleMeta.state, normalizedPhase);
  return {
    title: `${phaseMeta.label} · ${lifecycleMeta.label}`,
    guidance,
    tone,
  };
}

function getLifecycleGuidance(
  lifecycle: string,
  phase: string,
): { guidance: string; tone: CombinationConclusionTone } {
  switch (lifecycle) {
    case "repair":
      return phase === "bottoming_candidate"
        ? { guidance: "修复迹象仍需连续性验证，重点观察排名与参与度。", tone: "positive" }
        : { guidance: "修复信号初步出现，重点观察排名与市场环境是否同步改善。", tone: "watch" };
    case "emerging":
      return { guidance: "关注趋势能否延续，等待排名与市场环境共同确认。", tone: "positive" };
    case "trending":
      return phase === "accel_down"
        ? { guidance: "趋势运行与阶段走弱出现分歧，留意后续扩散与持续性。", tone: "watch" }
        : { guidance: "趋势运行相对顺畅，继续观察参与度与排名持续性。", tone: "positive" };
    case "crowded":
      return { guidance: "强势拥挤，关注参与度变化与排名降温信号。", tone: "watch" };
    case "divergence":
      return { guidance: "强弱背离加大不确定性，等待排名与市场环境重新确认。", tone: "risk" };
    case "exit":
      return { guidance: "趋势转弱迹象明确，关注风险扩散与后续阶段变化。", tone: "risk" };
    case "neutral":
      return phase === "neutral"
        ? { guidance: FALLBACK_GUIDANCE, tone: "neutral" }
        : { guidance: "Lifecycle 信号暂不明确，结合阶段变化继续观察。", tone: "neutral" };
    default:
      return { guidance: FALLBACK_GUIDANCE, tone: "neutral" };
  }
}

/** 板块轮动各视图共用的阶段文案与视觉语义。 */

export const PHASE_META: Record<string, { label: string; color: string; softColor: string; description: string }> = {
  accel_up: {
    label: "加速走强",
    color: "#37d6b0",
    softColor: "rgba(55, 214, 176, 0.16)",
    description: "相对强势与趋势加速同时出现，关注量能和行业内部参与度能否保持。",
  },
  decel_up: {
    label: "强势降温",
    color: "#f0b65a",
    softColor: "rgba(240, 182, 90, 0.16)",
    description: "相对强势仍在，但趋势加速放缓，需观察后续是否继续降温。",
  },
  bottoming_candidate: {
    label: "弱势修复观察",
    color: "#9185ff",
    softColor: "rgba(145, 133, 255, 0.16)",
    description: "弱势方向出现修复迹象，但尚不能视为趋势反转确认。",
  },
  reversal_confirmed: {
    label: "修复确认",
    color: "#67a9ff",
    softColor: "rgba(103, 169, 255, 0.16)",
    description: "弱势阶段后的修复得到模型确认，仍需观察持续性和覆盖质量。",
  },
  accel_down: {
    label: "加速走弱",
    color: "#ff7285",
    softColor: "rgba(255, 114, 133, 0.16)",
    description: "相对弱势与趋势走弱同时出现，应关注风险信号是否进一步扩散。",
  },
  neutral: {
    label: "方向未明",
    color: "#8795ab",
    softColor: "rgba(135, 149, 171, 0.14)",
    description: "当前阶段方向未明，适合结合后续交易日的连续变化观察。",
  },
};

/**
 * 获取任意阶段值对应的稳定展示元数据。
 *
 * 输入：数据库保存的确认阶段，可为空或为尚未识别的新值。
 * 输出：已知阶段元数据；未知值安全回退为“方向未明”。
 */
export function getPhaseMeta(phase: string | null | undefined) {
  return PHASE_META[phase ?? "neutral"] ?? PHASE_META.neutral;
}

/** 行业轨迹对比允许同时展示的最大行业数量。 */
export const MAX_TRAJECTORY_SECTORS = 5;

/**
 * 行业轨迹按选择顺序使用的固定色板。
 *
 * 输入：数组下标，即行业加入轨迹对比的先后顺序。
 * 输出：与该行业绑定的十六进制颜色；最多覆盖五条轨迹。
 */
export const TRAJECTORY_COLORS = ["#37d6b0", "#67a9ff", "#f0b65a", "#ff7189", "#a98bff"] as const;

/**
 * 在保持原有选择顺序的前提下追加一个行业。
 *
 * 输入：当前已选行业数组和准备加入的行业名称。
 * 输出：未重复且未达到五个时返回追加后的新数组；否则返回原数组，避免无效状态更新。
 */
export function addTrajectorySector(current: string[], candidate: string): string[] {
  if (current.includes(candidate) || current.length >= MAX_TRAJECTORY_SECTORS) return current;
  return [...current, candidate];
}

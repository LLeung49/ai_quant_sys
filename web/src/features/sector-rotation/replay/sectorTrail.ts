/** 统一象限图中单个关注行业的短期移动尾迹。 */
import type { QuadrantTrailPoint } from "../chart/quadrantOption";

export interface ReplayTrailSource {
  as_of_date: string;
  sector_name: string;
  velocity_score: number | null;
  acceleration_score: number | null;
}

/**
 * 构建截至当前回放帧的行业尾迹。
 *
 * 输入：全市场预加载点、行业名称、当前日期和最多保留的成功交易日数。
 * 输出：日期升序坐标；行业缺失或坐标缺失时输出 ``null`` 断点，不进行插值。
 */
export function buildSectorTrail(points: ReplayTrailSource[], sectorName: string | null, currentDate: string, limit = 10): Array<QuadrantTrailPoint | null> {
  if (!sectorName || !currentDate) return [];
  const dates = [...new Set(points.map((point) => point.as_of_date).filter((date) => date <= currentDate))].sort().slice(-limit);
  return dates.map((date) => {
    const point = points.find((item) => item.as_of_date === date && item.sector_name === sectorName);
    if (!point || point.velocity_score === null || point.acceleration_score === null) return null;
    return { as_of_date: date, velocity_score: point.velocity_score, acceleration_score: point.acceleration_score };
  });
}

/** 多行业轨迹中不可插值的数据缺口识别。 */

export interface HistoryGapPoint { as_of_date: string; sector_name: string; velocity_score: number | null; acceleration_score: number | null; }
export interface SectorGapSummary { sector_name: string; dates: string[]; }

/**
 * 查找指定成功交易日窗口内的行业轨迹缺口。
 *
 * 输入：预期交易日、对比行业和服务端返回的历史点。
 * 输出：仅包含有缺口行业的日期列表；行业行缺失或任一坐标为空都视为断点。
 */
export function findHistoryGaps(expectedDates: string[], sectorNames: string[], points: HistoryGapPoint[]): SectorGapSummary[] {
  return sectorNames.map((sectorName) => ({
    sector_name: sectorName,
    dates: expectedDates.filter((date) => {
      const point = points.find((item) => item.sector_name === sectorName && item.as_of_date === date);
      return !point || point.velocity_score === null || point.acceleration_score === null;
    }),
  })).filter((summary) => summary.dates.length > 0);
}

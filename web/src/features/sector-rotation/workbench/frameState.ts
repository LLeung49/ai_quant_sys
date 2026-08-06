/** 将一次性预加载的市场历史点组织成可即时切换的日期帧。 */

export interface DatedSectorPoint { as_of_date: string; sector_name: string; }

export interface ReplayFrames<T extends DatedSectorPoint> {
  dates: string[];
  byDate: Record<string, T[]>;
}

/**
 * 按成功交易日构建本地回放帧索引。
 *
 * 输入：服务端按任意稳定顺序返回的全市场历史点。
 * 输出：日期升序数组和日期到行业点列表的索引；不修改输入数组。
 */
export function buildReplayFrames<T extends DatedSectorPoint>(points: T[]): ReplayFrames<T> {
  const byDate: Record<string, T[]> = {};
  for (const point of points) (byDate[point.as_of_date] ??= []).push(point);
  return { dates: Object.keys(byDate).sort(), byDate };
}

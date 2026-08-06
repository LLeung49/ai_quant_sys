/** 选中行业历史轨迹的受限查询封装。 */
import { useQuery } from "@tanstack/react-query";
import { fetchSectorHistory } from "./api";
import { MAX_TRAJECTORY_SECTORS } from "./history/constants";

/**
 * 读取一个行业在当前成功日期集合内的历史坐标。
 *
 * 输入：行业名称、成功快照日期、行业层级和模型版本。
 * 输出：仅在日期边界完整时启用的 TanStack Query 状态。
 */
export function useHistoryData(sectorNames: string[], dates: string[], level: 1 | 2, modelVersion: string) {
  const ordered = [...dates].sort(); const startDate = ordered[0]; const endDate = ordered.at(-1);
  return useQuery({ queryKey: ["sector-rotation", "history", sectorNames, startDate, endDate, level, modelVersion], queryFn: () => fetchSectorHistory(sectorNames, startDate!, endDate!, level, modelVersion), enabled: Boolean(sectorNames.length > 0 && sectorNames.length <= MAX_TRAJECTORY_SECTORS && startDate && endDate && startDate !== endDate), staleTime: 60_000 });
}

/** 全市场回放数据的受限 TanStack Query 封装。 */
import { useQuery } from "@tanstack/react-query";
import { fetchReplay } from "./api";

/**
 * 读取当前成功日期集合的全市场回放点。
 *
 * 输入：倒序或乱序成功日期、行业层级和模型版本。
 * 输出：仅在至少两个日期存在时启用的查询状态，日期范围由集合边界严格限定。
 */
export function useReplayData(dates: string[], level: 1 | 2, modelVersion: string) {
  const ordered = [...dates].sort(); const startDate = ordered[0]; const endDate = ordered.at(-1);
  return useQuery({ queryKey: ["sector-rotation", "replay", startDate, endDate, level, modelVersion], queryFn: () => fetchReplay(startDate!, endDate!, level, modelVersion), enabled: Boolean(startDate && endDate && startDate !== endDate), staleTime: 60_000 });
}

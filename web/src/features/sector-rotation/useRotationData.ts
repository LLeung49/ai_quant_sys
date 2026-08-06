/** 使用 TanStack Query 串联板块轮动日期与快照请求。 */
import { useQuery } from "@tanstack/react-query";
import { fetchAvailableDates, fetchSnapshot } from "./api";

/**
 * 获取某行业层级下的最新成功快照。
 *
 * 输入：行业层级和模型版本。
 * 输出：日期查询与快照查询状态；快照仅在取得最新日期后发起，二者共享稳定查询键。
 */
export function useRotationData(level: 1 | 2, modelVersion: string, selectedDate?: string) {
  const dates = useQuery({
    queryKey: ["sector-rotation", "available-dates", level, modelVersion],
    queryFn: () => fetchAvailableDates(level, modelVersion),
    staleTime: 60_000,
  });
  const latestDate = selectedDate ?? dates.data?.[0];
  const snapshot = useQuery({
    queryKey: ["sector-rotation", "snapshot", latestDate, level, modelVersion],
    queryFn: () => fetchSnapshot(latestDate!, level, modelVersion),
    enabled: Boolean(latestDate),
    staleTime: 60_000,
  });
  return { dates, snapshot, latestDate };
}

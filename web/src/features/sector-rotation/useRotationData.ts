/** 使用 TanStack Query 串联板块轮动日期与快照请求。 */
import { useQuery } from "@tanstack/react-query";
import { fetchAvailableDates, fetchSnapshot } from "./api";

/**
 * 获取某行业层级下不晚于用户所选日的最近成功快照。
 *
 * 输入：行业层级和模型版本。
 * 输出：成功快照日期查询与快照查询状态；快照仅在解析出加载日期后发起，二者共享稳定查询键。
 */
export function useRotationData(level: 1 | 2, modelVersion: string, selectedDate?: string) {
  const dates = useQuery({
    queryKey: ["sector-rotation", "available-dates", level, modelVersion],
    queryFn: () => fetchAvailableDates(level, modelVersion),
    staleTime: 60_000,
  });
  const loadedSnapshotDate = dates.data
    ?.filter((date) => !selectedDate || date <= selectedDate)
    .sort()
    .at(-1);
  const snapshot = useQuery({
    queryKey: ["sector-rotation", "snapshot", loadedSnapshotDate, level, modelVersion],
    queryFn: () => fetchSnapshot(loadedSnapshotDate!, level, modelVersion),
    enabled: Boolean(loadedSnapshotDate),
    staleTime: 60_000,
  });
  return { dates, snapshot, loadedSnapshotDate };
}

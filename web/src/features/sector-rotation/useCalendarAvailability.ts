import { useQuery } from "@tanstack/react-query";
import { fetchCalendarAvailability } from "./api";

/** 用显示月的起止日缓存日历可用性，避免不同月份共享无效缓存。 */
export function useCalendarAvailability(
  level: 1 | 2,
  modelVersion: string,
  startDate: string,
  endDate: string,
) {
  return useQuery({
    queryKey: ["sector-rotation", "calendar-availability", level, modelVersion, startDate, endDate],
    queryFn: () => fetchCalendarAvailability(level, modelVersion, startDate, endDate),
    staleTime: 60_000,
  });
}

import { useQuery, type UseQueryResult } from "@tanstack/react-query";
import {
  fetchShortTermHistory,
  type ShortTermHistoryResponse,
} from "../short_term/api";

/**
 * 详情抽屉使用的短期历史 hook。
 *
 * 复用现有 `fetchShortTermHistory` 接口,queryKey 直接命中,
 * 二次打开同一行业详情时,TanStack Query 缓存,零额外请求。
 *
 * 输入:
 * - level: 1|2 行业层级;
 * - asOfDate: 工作台截止日期(YYYY-MM-DD);
 * - sectorName: 目标行业名;
 * - days: 历史窗口天数,默认 5。
 *
 * 输出: 仅暴露 response / isLoading / isError / queryRef 四个字段。
 *
 * 边界: 任意参数为空时查询不发出,避免在抽屉未打开时空跑请求。
 *
 * 关键: 短期历史 API 是区间查询,后端只返回成功运行的交易日。
 * 为了保证能拿到 days 个工作日,start_date 取 asOfDate 之前 LOOKBACK_DAYS 个日历日
 * (LOOKBACK_DAYS = max(days*6, 30),足以覆盖一个月的交易日 ~21 天)。
 */
export interface ShortTermHistoryQueryResult {
  /** 已加载的响应;未发出查询或加载失败时为 null。 */
  response: ShortTermHistoryResponse | null;
  isLoading: boolean;
  isError: boolean;
  queryRef: UseQueryResult<ShortTermHistoryResponse>;
}

/** 计算历史窗口的起始日;空日期时安全回退返回原值,避免 Date 解析失败。 */
function computeHistoryStart(asOfDate: string, windowDays: number): string {
  if (!asOfDate) return asOfDate;
  const lookbackDays = Math.max(windowDays * 6, 30);
  const end = new Date(`${asOfDate}T00:00:00Z`);
  if (Number.isNaN(end.getTime())) return asOfDate;
  end.setUTCDate(end.getUTCDate() - lookbackDays);
  return end.toISOString().slice(0, 10);
}

export function useShortTermHistory(
  level: 1 | 2,
  asOfDate: string,
  sectorName: string,
  days: number = 5,
): ShortTermHistoryQueryResult {
  const startDate = computeHistoryStart(asOfDate, days);
  const query = useQuery({
    queryKey: ["short-term-history", level, asOfDate, sectorName, days],
    queryFn: () => fetchShortTermHistory([sectorName], startDate, asOfDate, level),
    enabled: Boolean(asOfDate && sectorName),
    staleTime: 60_000,
  });
  return {
    response: query.data ?? null,
    isLoading: query.isLoading,
    isError: query.isError,
    queryRef: query,
  };
}
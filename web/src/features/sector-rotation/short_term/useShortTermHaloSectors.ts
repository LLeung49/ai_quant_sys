/**
 * 共享给 ShortTermAnomalyModule 与 SectorRotationPage 的短期快照 hook。
 *
 * 该 hook 与 ShortTermAnomalyModule 内的 queryKey 完全一致,使得两边使用相同 level + asOfDate 时,
 * TanStack Query 自动 dedupe 同一条请求并共享缓存。
 *
 * 输入:level(1|2) 与 asOfDate(YYYY-MM-DD),可选 availableDates 用于提前触发 availableDates 查询。
 * 输出:仅暴露 sectors 数组 + query 状态,避免泄漏完整的 snapshot 字段。
 */

import { useQuery, type UseQueryResult } from "@tanstack/react-query";
import { fetchShortTermSnapshot, type ShortTermSector, type ShortTermSnapshotResponse } from "./api";

export interface ShortTermHaloQueryResult {
  /** 归一化的 sectors(可能为空数组);永远不会为 undefined,避免消费方到处判空。 */
  sectors: ShortTermSector[];
  /** 是否仍在加载(包含 retry)。 */
  isLoading: boolean;
  /** 是否遇到错误(包含 5xx、解析失败)。 */
  isError: boolean;
  /** 原始 snapshot 缓存(用于进一步读取 meta 等字段);加载未完成时为 null。 */
  snapshot: ShortTermSnapshotResponse | null;
  /** 透传给消费方的 query ref,便于 test 触发 refetch / invalidate。 */
  queryRef: UseQueryResult<ShortTermSnapshotResponse>;
}

/**
 * 拉取当日短期异动快照并选择 sectors 字段,供 SectorRotationPage 等非 UI 形态使用。
 *
 * 设计要点:
 * - queryKey 与 ShortTermAnomalyModule 内部完全一致,确保两边调用时 TanStack Query 只发起一次请求;
 * - 不提供 onSuccess / onError 之类的副作用钩子,留给消费方自行处理;
 * - 不缓存 sectors 引用,每次渲染都返回新数组以避免下游误判;
 * - 失败时不抛错,只通过 isError 暴露给消费方。
 */
export function useShortTermHaloSectors(level: 1 | 2, asOfDate: string | null | undefined): ShortTermHaloQueryResult {
  const query = useQuery({
    queryKey: ["short-term-snapshot", level, asOfDate],
    queryFn: () => fetchShortTermSnapshot(asOfDate as string, level),
    enabled: Boolean(asOfDate),
    staleTime: 5 * 60 * 1000,
  });
  const data = query.data;
  return {
    sectors: (data?.sectors ?? []) as ShortTermSector[],
    isLoading: query.isLoading,
    isError: query.isError,
    snapshot: data ?? null,
    queryRef: query,
  };
}

/** 板块 K 线的 TanStack Query 缓存键和请求生命周期封装。 */
import { useQuery } from "@tanstack/react-query";
import { fetchSectorKline } from "./sectorKlineApi";

/** 触发板块 K 线查询所需的工作台上下文。 */
export interface UseSectorKlineParams {
  /** 当前抽屉选中的板块名称；为空时不请求。 */
  sectorName: string | undefined;
  /** 申万行业层级。 */
  level: 1 | 2;
  /** 工作台当前显示的行情截止日；为空时不请求。 */
  endDate: string | undefined;
  /** 仅当详情抽屉已打开时为真。 */
  enabled: boolean;
  /** 当前工作台日期是否为数据集最新日，用于选择短期或永久缓存。 */
  isLatestDate: boolean;
}

/**
 * 构建板块 K 线的确定性缓存键。
 *
 * 输入：板块名称、行业层级、行情截止日。
 * 输出：区分不同板块、层级和日期的只读 Query Key。
 */
export function buildSectorKlineQueryKey(sectorName: string | undefined, level: 1 | 2, endDate: string | undefined) {
  return ["sector-rotation", "sector-kline", sectorName, level, endDate] as const;
}

/**
 * 在抽屉打开且请求上下文完整时读取板块 K 线，并复用同一缓存供缩略图和放大弹窗使用。
 *
 * 输入：抽屉选择状态、行业层级、工作台截止日、启用标志和最新日标志。
 * 输出：TanStack Query 结果；最新日缓存 60 秒，历史日缓存永久有效。
 * 异常：请求层 API/网络/取消/数据契约异常均记录在 Query 的 error 字段，不影响页面其他区域。
 */
export function useSectorKline(params: UseSectorKlineParams) {
  return useQuery({
    queryKey: buildSectorKlineQueryKey(params.sectorName, params.level, params.endDate),
    queryFn: ({ signal }) => fetchSectorKline(params.sectorName!, params.level, params.endDate!, signal),
    enabled: params.enabled && Boolean(params.sectorName && params.endDate),
    staleTime: params.isLatestDate ? 60_000 : Infinity,
  });
}

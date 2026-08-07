/** 板块 K 线 TanStack Query 封装测试。 */
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { renderHook, waitFor } from "@testing-library/react";
import type { ReactNode } from "react";
import { describe, expect, it, vi } from "vitest";
import { buildSectorKlineQueryKey, useSectorKline } from "./useSectorKline";

const response = {
  sector_name: "半导体",
  sector_level: 2,
  requested_end_date: "2026-08-06",
  actual_end_date: "2026-08-06",
  price_basis: "equal_weight_composite_index",
  bars: [{ trade_date: "2026-08-06", timestamp: 1785945600000, open: 10, high: 12, low: 9, close: 11, volume: 100, amount: 1_000 }],
  meta: { field_version: "v1", source: "trade_sector_daily", bar_count: 1, skipped_bar_count: 0, warmup_target: 100 },
};

/** 输入：是否以最新日期查询；输出：隔离缓存与禁用重试的 Hook 测试包装器。 */
function createWrapper() {
  const client = new QueryClient({ defaultOptions: { queries: { retry: false } } });
  const wrapper = ({ children }: { children: ReactNode }) => <QueryClientProvider client={client}>{children}</QueryClientProvider>;
  return { client, wrapper };
}

describe("useSectorKline", () => {
  it("使用包含行业、层级和截止日的稳定缓存键", () => {
    expect(buildSectorKlineQueryKey("半导体", 2, "2026-08-06"))
      .toEqual(["sector-rotation", "sector-kline", "半导体", 2, "2026-08-06"]);
  });

  it("抽屉未打开时不发起请求", async () => {
    const fetchMock = vi.fn();
    vi.stubGlobal("fetch", fetchMock);
    const { wrapper } = createWrapper();

    renderHook(() => useSectorKline({ sectorName: "半导体", level: 2, endDate: "2026-08-06", enabled: false, isLatestDate: true }), { wrapper });

    await Promise.resolve();
    expect(fetchMock).not.toHaveBeenCalled();
  });

  it("最新日期短缓存、历史日期永久缓存，并把 Query signal 传递到请求层", async () => {
    const fetchMock = vi.fn().mockResolvedValue(new Response(JSON.stringify(response)));
    vi.stubGlobal("fetch", fetchMock);
    const { client, wrapper } = createWrapper();
    const latestKey = buildSectorKlineQueryKey("半导体", 2, "2026-08-06");
    const { result, rerender } = renderHook(
      ({ isLatestDate }) => useSectorKline({ sectorName: "半导体", level: 2, endDate: "2026-08-06", enabled: true, isLatestDate }),
      { initialProps: { isLatestDate: true }, wrapper },
    );

    await waitFor(() => expect(result.current.isSuccess).toBe(true));
    // QueryCache 对查询选项使用宽泛泛型；测试只读取运行时注册的 staleTime 配置。
    const latestOptions = client.getQueryCache().find({ queryKey: latestKey })?.options as { staleTime?: number } | undefined;
    expect(latestOptions?.staleTime).toBe(60_000);
    expect((fetchMock.mock.calls[0][1] as RequestInit).signal).toBeInstanceOf(AbortSignal);

    rerender({ isLatestDate: false });
    const historicalOptions = client.getQueryCache().find({ queryKey: latestKey })?.options as { staleTime?: number } | undefined;
    expect(historicalOptions?.staleTime).toBe(Infinity);
    expect(fetchMock).toHaveBeenCalledTimes(1);
  });
});

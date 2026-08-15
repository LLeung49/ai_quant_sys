/** useShortTermHistory 的 queryKey、enabled、参数传递测试。 */

import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { renderHook, waitFor } from "@testing-library/react";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { useShortTermHistory } from "./useShortTermHistory";

const fakeHistory = {
  sector_level: 2,
  model_version: "v2_short_term",
  meta: {
    run_status: "succeeded" as const,
    field_version: "v2_short_term" as const,
    source_max_trade_date: "2026-08-11",
    eligible_sector_count: 30,
    skipped_sector_count: 5,
    pulse_up_count: 3,
    volume_spike_count: 2,
    limit_cluster_count: 1,
    limit_panic_count: 0,
  },
  points: [
    { sector_name: "半导体", as_of_date: "2026-08-11", score_eligible: true, short_term_intensity: "intense", short_term_labels: "pulse_up" },
    { sector_name: "半导体", as_of_date: "2026-08-10", score_eligible: true, short_term_intensity: "mild" },
    { sector_name: "半导体", as_of_date: "2026-08-09", score_eligible: true, short_term_intensity: "moderate", short_term_labels: "volume_spike" },
  ],
};

const fetchMock = vi.fn().mockResolvedValue(fakeHistory);

vi.mock("../short_term/api", async () => {
  const actual = await vi.importActual("../short_term/api");
  return {
    ...actual,
    fetchShortTermHistory: (...args: unknown[]) => fetchMock(...args),
  };
});

function createWrapper() {
  const client = new QueryClient({ defaultOptions: { queries: { retry: false } } });
  return function Wrapper({ children }: { children: React.ReactNode }) {
    return <QueryClientProvider client={client}>{children}</QueryClientProvider>;
  };
}

describe("useShortTermHistory", () => {
  beforeEach(() => {
    fetchMock.mockClear();
  });

  afterEach(() => {
    vi.clearAllMocks();
  });

  it("缺少 asOfDate 或 sectorName 时不发请求,response 为 null", () => {
    const { result: r1 } = renderHook(() => useShortTermHistory(2, "", "半导体"), { wrapper: createWrapper() });
    expect(r1.current.response).toBeNull();
    expect(r1.current.isLoading).toBe(false);
    expect(fetchMock).not.toHaveBeenCalled();

    const { result: r2 } = renderHook(() => useShortTermHistory(2, "2026-08-11", ""), { wrapper: createWrapper() });
    expect(r2.current.response).toBeNull();
    expect(fetchMock).not.toHaveBeenCalled();
  });

  it("成功加载后 response 返回数据,isLoading 变 false", async () => {
    const { result } = renderHook(() => useShortTermHistory(2, "2026-08-11", "半导体"), { wrapper: createWrapper() });
    await waitFor(() => {
      expect(result.current.response).toBe(fakeHistory);
    });
    expect(result.current.isLoading).toBe(false);
    expect(result.current.isError).toBe(false);
  });

  it("请求参数为 [sectorName], endDate 等于 asOfDate,startDate 早于 asOfDate", async () => {
    const { result } = renderHook(() => useShortTermHistory(2, "2026-08-11", "半导体", 5), { wrapper: createWrapper() });
    await waitFor(() => expect(result.current.response).not.toBeNull());
    expect(fetchMock).toHaveBeenCalledTimes(1);
    const callArgs = fetchMock.mock.calls[0];
    expect(callArgs[0]).toEqual(["半导体"]);
    const startDate = callArgs[1] as string;
    const endDate = callArgs[2] as string;
    expect(endDate).toBe("2026-08-11");
    expect(startDate < endDate).toBe(true);
  });

  it("同 (level, asOfDate, sectorName, days) 多次调用只发一次请求(缓存 dedupe)", async () => {
    const wrapper = createWrapper();
    const h1 = renderHook(() => useShortTermHistory(2, "2026-08-11", "半导体"), { wrapper });
    const h2 = renderHook(() => useShortTermHistory(2, "2026-08-11", "半导体"), { wrapper });
    await waitFor(() => expect(h1.result.current.response).not.toBeNull());
    expect(h2.result.current.response).not.toBeNull();
    expect(fetchMock).toHaveBeenCalledTimes(1);
  });

  it("days 不同时 queryKey 不同,触发新请求", async () => {
    const wrapper = createWrapper();
    const h1 = renderHook(() => useShortTermHistory(2, "2026-08-11", "半导体", 5), { wrapper });
    await waitFor(() => expect(h1.result.current.response).not.toBeNull());
    const h2 = renderHook(() => useShortTermHistory(2, "2026-08-11", "半导体", 10), { wrapper });
    await waitFor(() => expect(h2.result.current.response).not.toBeNull());
    expect(fetchMock).toHaveBeenCalledTimes(2);
  });

  it("请求失败时 response 为 null,isError 为 true", async () => {
    fetchMock.mockRejectedValueOnce(new Error("network"));
    const { result } = renderHook(() => useShortTermHistory(2, "2026-08-11", "半导体"), { wrapper: createWrapper() });
    await waitFor(() => expect(result.current.isError).toBe(true));
    expect(result.current.response).toBeNull();
  });
});
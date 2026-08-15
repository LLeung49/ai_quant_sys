/** useShortTermHaloSectors 的查询键与 TanStack Query 行为测试。 */

import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { renderHook, waitFor } from "@testing-library/react";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { useShortTermHaloSectors } from "./useShortTermHaloSectors";

const fakeSnapshot = {
  as_of_date: "2026-08-11",
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
  sectors: [
    { sector_name: "半导体", score_eligible: true, short_term_intensity: "intense", short_term_labels: "pulse_up,volume_spike" },
  ],
};

const fetchMock = vi.fn().mockResolvedValue(fakeSnapshot);

vi.mock("./api", async () => {
  const actual = await vi.importActual("./api");
  return {
    ...actual,
    fetchShortTermSnapshot: (...args: unknown[]) => fetchMock(...args),
  };
});

function createWrapper() {
  const client = new QueryClient({ defaultOptions: { queries: { retry: false } } });
  return function Wrapper({ children }: { children: React.ReactNode }) {
    return <QueryClientProvider client={client}>{children}</QueryClientProvider>;
  };
}

describe("useShortTermHaloSectors", () => {
  beforeEach(() => {
    fetchMock.mockClear();
  });

  afterEach(() => {
    vi.clearAllMocks();
  });

  it("缺少 asOfDate 时不发请求,sectors 为空数组", () => {
    const { result } = renderHook(() => useShortTermHaloSectors(2, null), { wrapper: createWrapper() });
    expect(result.current.sectors).toEqual([]);
    expect(result.current.isLoading).toBe(false);
    expect(fetchMock).not.toHaveBeenCalled();
  });

  it("同 level+asOfDate 多次调用只发起一次请求(TanStack Query dedupe)", async () => {
    const wrapper = createWrapper();
    const hook1 = renderHook(() => useShortTermHaloSectors(2, "2026-08-11"), { wrapper });
    const hook2 = renderHook(() => useShortTermHaloSectors(2, "2026-08-11"), { wrapper });
    await waitFor(() => {
      expect(hook1.result.current.sectors.length).toBe(1);
      expect(hook2.result.current.sectors.length).toBe(1);
    });
    expect(fetchMock).toHaveBeenCalledTimes(1);
    expect(fetchMock).toHaveBeenCalledWith("2026-08-11", 2);
  });
});

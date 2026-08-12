/** 板块轮动页面数据查询状态测试。 */
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { renderHook, waitFor } from "@testing-library/react";
import { type ReactNode } from "react";
import { vi } from "vitest";
import * as api from "./api";
import { useRotationData } from "./useRotationData";

describe("useRotationData", () => {
  it("先读取可用日期，再以最新日期读取同一层级的快照", async () => {
    vi.spyOn(api, "fetchAvailableDates").mockResolvedValue(["2026-08-04"]);
    vi.spyOn(api, "fetchSnapshot").mockResolvedValue({
      as_of_date: "2026-08-04", sector_level: 2, model_version: "v1", sectors: [],
      meta: { run_status: "succeeded", field_version: "v1", source_max_trade_date: "2026-08-04", eligible_sector_count: 113, skipped_sector_count: 0, market_regime: "high_volatility", regime_multiplier: 0.85 },
    });
    const client = new QueryClient({ defaultOptions: { queries: { retry: false } } });
    const wrapper = ({ children }: { children: ReactNode }) => <QueryClientProvider client={client}>{children}</QueryClientProvider>;

    const { result } = renderHook(() => useRotationData(2, "v1"), { wrapper });
    await waitFor(() => expect(result.current.snapshot.data?.as_of_date).toBe("2026-08-04"));

    expect(api.fetchAvailableDates).toHaveBeenCalledWith(2, "v1");
    expect(api.fetchSnapshot).toHaveBeenCalledWith("2026-08-04", 2, "v1");
  });

  it("uses the latest successful snapshot not later than a pending selected date", async () => {
    vi.spyOn(api, "fetchAvailableDates").mockResolvedValue(["2026-08-10"]);
    vi.spyOn(api, "fetchSnapshot").mockResolvedValue({
      as_of_date: "2026-08-10", sector_level: 2, model_version: "v1", sectors: [],
      meta: { run_status: "succeeded", field_version: "v1", source_max_trade_date: "2026-08-10", eligible_sector_count: 113, skipped_sector_count: 0, market_regime: "high_volatility", regime_multiplier: 0.85 },
    });
    const client = new QueryClient({ defaultOptions: { queries: { retry: false } } });
    const wrapper = ({ children }: { children: ReactNode }) => <QueryClientProvider client={client}>{children}</QueryClientProvider>;

    const { result } = renderHook(() => useRotationData(2, "v1", "2026-08-11"), { wrapper });
    await waitFor(() => expect(result.current.snapshot.data?.as_of_date).toBe("2026-08-10"));

    expect(result.current.loadedSnapshotDate).toBe("2026-08-10");
    expect(api.fetchSnapshot).toHaveBeenCalledWith("2026-08-10", 2, "v1");
    expect(api.fetchSnapshot).not.toHaveBeenCalledWith("2026-08-11", 2, "v1");
  });

  it("does not load a snapshot later than the selected date", async () => {
    vi.spyOn(api, "fetchAvailableDates").mockResolvedValue(["2026-08-10", "2026-08-08"]);
    vi.spyOn(api, "fetchSnapshot").mockResolvedValue({
      as_of_date: "2026-08-08", sector_level: 2, model_version: "v1", sectors: [],
      meta: { run_status: "succeeded", field_version: "v1", source_max_trade_date: "2026-08-08", eligible_sector_count: 113, skipped_sector_count: 0, market_regime: "high_volatility", regime_multiplier: 0.85 },
    });
    const client = new QueryClient({ defaultOptions: { queries: { retry: false } } });
    const wrapper = ({ children }: { children: ReactNode }) => <QueryClientProvider client={client}>{children}</QueryClientProvider>;

    const { result } = renderHook(() => useRotationData(2, "v1", "2026-08-09"), { wrapper });
    await waitFor(() => expect(result.current.snapshot.data?.as_of_date).toBe("2026-08-08"));

    expect(result.current.loadedSnapshotDate).toBe("2026-08-08");
    expect(api.fetchSnapshot).toHaveBeenCalledWith("2026-08-08", 2, "v1");
    expect(api.fetchSnapshot).not.toHaveBeenCalledWith("2026-08-10", 2, "v1");
  });

  it("does not request a snapshot when no successful snapshot is available on or before the selected date", async () => {
    vi.spyOn(api, "fetchAvailableDates").mockResolvedValue(["2026-08-10"]);
    const fetchSnapshot = vi.spyOn(api, "fetchSnapshot");
    const client = new QueryClient({ defaultOptions: { queries: { retry: false } } });
    const wrapper = ({ children }: { children: ReactNode }) => <QueryClientProvider client={client}>{children}</QueryClientProvider>;

    const { result } = renderHook(() => useRotationData(2, "v1", "2026-08-09"), { wrapper });
    await waitFor(() => expect(result.current.dates.data).toEqual(["2026-08-10"]));

    expect(result.current.loadedSnapshotDate).toBeUndefined();
    expect(fetchSnapshot).not.toHaveBeenCalled();
  });
});

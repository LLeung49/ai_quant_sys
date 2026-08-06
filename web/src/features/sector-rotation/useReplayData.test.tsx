/** 全市场回放查询范围与缓存键测试。 */
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { renderHook, waitFor } from "@testing-library/react";
import { type ReactNode } from "react";
import { vi } from "vitest";
import * as api from "./api";
import { useReplayData } from "./useReplayData";

describe("useReplayData", () => {
  it("使用已成功运行日期中的最早和最新日期请求回放", async () => {
    vi.spyOn(api, "fetchReplay").mockResolvedValue([]);
    const client = new QueryClient({ defaultOptions: { queries: { retry: false } } });
    const wrapper = ({ children }: { children: ReactNode }) => <QueryClientProvider client={client}>{children}</QueryClientProvider>;
    const { result } = renderHook(() => useReplayData(["2026-08-04", "2026-08-01"], 2, "v1"), { wrapper });
    await waitFor(() => expect(result.current.isSuccess).toBe(true));
    expect(api.fetchReplay).toHaveBeenCalledWith("2026-08-01", "2026-08-04", 2, "v1");
  });
});

/** 单板块历史轨迹查询范围测试。 */
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { renderHook, waitFor } from "@testing-library/react";
import { type ReactNode } from "react";
import { vi } from "vitest";
import * as api from "./api";
import { useHistoryData } from "./useHistoryData";

describe("useHistoryData", () => {
  it("只请求选中行业与指定成功日期边界内的历史", async () => {
    vi.spyOn(api, "fetchSectorHistory").mockResolvedValue([]);
    const client = new QueryClient({ defaultOptions: { queries: { retry: false } } });
    const wrapper = ({ children }: { children: ReactNode }) => <QueryClientProvider client={client}>{children}</QueryClientProvider>;
    const sectors = ["半导体", "教育", "软件开发", "贵金属", "证券"];
    const { result } = renderHook(() => useHistoryData(sectors, ["2026-08-04", "2026-08-01"], 2, "v1"), { wrapper });
    await waitFor(() => expect(result.current.isSuccess).toBe(true));
    expect(api.fetchSectorHistory).toHaveBeenCalledWith(sectors, "2026-08-01", "2026-08-04", 2, "v1");
  });
});

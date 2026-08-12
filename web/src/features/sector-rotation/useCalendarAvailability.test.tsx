import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { renderHook, waitFor } from "@testing-library/react";
import { type ReactNode } from "react";
import { expect, it, vi } from "vitest";
import * as api from "./api";
import { useCalendarAvailability } from "./useCalendarAvailability";

it("以显示月的起止日作为查询键和请求参数", async () => {
  const availability = {
    sector_level: 2,
    model_version: "v1",
    trade_dates: ["2026-08-10"],
    snapshot_dates: ["2026-08-10"],
    latest_snapshot_date: "2026-08-10",
  };
  const fetchAvailability = vi.spyOn(api, "fetchCalendarAvailability").mockResolvedValue(availability);
  const client = new QueryClient({ defaultOptions: { queries: { retry: false } } });
  const wrapper = ({ children }: { children: ReactNode }) => <QueryClientProvider client={client}>{children}</QueryClientProvider>;

  const { result } = renderHook(
    () => useCalendarAvailability(2, "v1", "2026-08-01", "2026-08-31"),
    { wrapper },
  );

  await waitFor(() => expect(result.current.data).toEqual(availability));
  expect(fetchAvailability).toHaveBeenCalledWith(2, "v1", "2026-08-01", "2026-08-31");
  expect(client.getQueryState(["sector-rotation", "calendar-availability", 2, "v1", "2026-08-01", "2026-08-31"]))
    .toMatchObject({ status: "success" });
});

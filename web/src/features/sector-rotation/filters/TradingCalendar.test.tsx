import { fireEvent, render, screen } from "@testing-library/react";
import { expect, it, vi } from "vitest";
import { TradingCalendar } from "./TradingCalendar";

it("把快照日、待生成交易日和非交易日呈现为不同的可访问状态", () => {
  const onDateChange = vi.fn();
  render(
    <TradingCalendar
      displayedMonth="2026-08"
      onDisplayedMonthChange={vi.fn()}
      tradeDates={["2026-08-10", "2026-08-11"]}
      snapshotDates={["2026-08-10"]}
      selectedDate="2026-08-10"
      onDateChange={onDateChange}
    />,
  );

  const snapshotDay = screen.getByRole("button", { name: /2026-08-10.*已生成快照/ });
  const pendingDay = screen.getByRole("button", { name: /2026-08-11.*尚未生成快照/ });
  const closedDay = screen.getByRole("button", { name: /2026-08-09.*非交易日/ });

  expect(snapshotDay).toHaveAttribute("data-date-status", "snapshot");
  expect(pendingDay).toHaveAttribute("data-date-status", "pending");
  expect(closedDay).toBeDisabled();
  fireEvent.click(pendingDay);
  expect(onDateChange).toHaveBeenCalledWith("2026-08-11");
});

it("使用上一个和下一个月控件更新受控的显示月", () => {
  const onDisplayedMonthChange = vi.fn();
  render(<TradingCalendar displayedMonth="2026-08" onDisplayedMonthChange={onDisplayedMonthChange} tradeDates={[]} snapshotDates={[]} selectedDate="" onDateChange={vi.fn()} />);

  fireEvent.click(screen.getByRole("button", { name: "上个月" }));
  fireEvent.click(screen.getByRole("button", { name: "下个月" }));

  expect(onDisplayedMonthChange).toHaveBeenNthCalledWith(1, "2026-07");
  expect(onDisplayedMonthChange).toHaveBeenNthCalledWith(2, "2026-09");
  expect(screen.getByRole("grid")).toHaveStyle({ gridTemplateColumns: "repeat(7, minmax(0, 1fr))" });
});

/** 板块轮动筛选器的用户交互测试。 */
import { fireEvent, render, screen } from "@testing-library/react";
import { RotationFilters } from "./RotationFilters";

describe("RotationFilters", () => {
  it("默认显示二级行业，并将用户选择回传给页面状态", () => {
    const onLevelChange = vi.fn();
    render(<RotationFilters dates={["2026-08-04", "2026-08-03"]} selectedDate="2026-08-04" level={2} modelVersion="v1" onDateChange={vi.fn()} onLevelChange={onLevelChange} />);

    expect(screen.getByLabelText("行业层级")).toHaveValue("2");
    fireEvent.change(screen.getByLabelText("行业层级"), { target: { value: "1" } });
    expect(onLevelChange).toHaveBeenCalledWith(1);
  });
});

/** ShortTermKpi 卡片在数字上悬停时展示当日命中板块的单元测试。 */
import { fireEvent, render, screen, within } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import { ShortTermKpi } from "./ShortTermKpi";
import type { ShortTermResponseMeta } from "./api";

function makeMeta(overrides: Partial<ShortTermResponseMeta> = {}): ShortTermResponseMeta {
  return {
    run_status: "succeeded",
    field_version: "v2_short_term",
    source_max_trade_date: "2026-08-11",
    eligible_sector_count: 30,
    skipped_sector_count: 5,
    pulse_up_count: 0,
    volume_spike_count: 0,
    limit_cluster_count: 0,
    limit_panic_count: 0,
    pulse_up_sectors: [],
    volume_spike_sectors: [],
    limit_cluster_sectors: [],
    limit_panic_sectors: [],
    ...overrides,
  };
}

describe("ShortTermKpi", () => {
  it("默认以 1×4 排列并展示四个 KPI", () => {
    render(<ShortTermKpi meta={makeMeta({ pulse_up_count: 3 })} />);
    const section = screen.getByLabelText("短期异动 KPI");
    expect(section).toBeInTheDocument();
    expect(section).not.toHaveAttribute("data-layout", "grid");
    expect(within(section).getByText("3")).toBeInTheDocument();
  });

  it("layout=grid 时产出 data-layout=grid", () => {
    render(<ShortTermKpi meta={makeMeta()} layout="grid" />);
    expect(screen.getByLabelText("短期异动 KPI")).toHaveAttribute("data-layout", "grid");
  });

  it("鼠标悬停数字时弹出当日命中的板块名称清单", () => {
    const meta = makeMeta({
      pulse_up_count: 2,
      pulse_up_sectors: ["半导体", "新能源"],
    });
    render(<ShortTermKpi meta={meta} />);
    const card = screen.getByText("单日脉冲上涨").closest("[data-key]") as HTMLElement;
    expect(card).not.toBeNull();
    const value = within(card).getByText("2");
    fireEvent.mouseEnter(card);
    const popover = card.querySelector(".kpi-sector-popover") as HTMLElement;
    expect(popover).not.toBeNull();
    expect(within(popover).getByText("半导体")).toBeInTheDocument();
    expect(within(popover).getByText("新能源")).toBeInTheDocument();
    expect(within(popover).getByText("命中板块")).toBeInTheDocument();
    expect(popover.querySelector(".kpi-sector-popover__count")).toBeInTheDocument();
    expect(value).toBeInTheDocument();
  });

  it("悬停空列表时显示当日无符合阈值的板块", () => {
    const meta = makeMeta({ limit_cluster_count: 0, limit_cluster_sectors: [] });
    render(<ShortTermKpi meta={meta} />);
    const card = screen.getByText("涨停集群").closest("[data-key]") as HTMLElement;
    fireEvent.mouseEnter(card);
    const popover = card.querySelector(".kpi-sector-popover") as HTMLElement;
    expect(popover).not.toBeNull();
    expect(within(popover).getByText("当日无符合阈值的板块")).toBeInTheDocument();
  });

  it("超过一页时仍全部渲染且可在列表内滚动", () => {
    const names = Array.from({ length: 12 }, (_, index) => "x_" + (index + 1));
    const meta = makeMeta({ pulse_up_count: 12, pulse_up_sectors: names });
    render(<ShortTermKpi meta={meta} />);
    const card = screen.getByText("单日脉冲上涨").closest("[data-key]") as HTMLElement;
    fireEvent.mouseEnter(card);
    const popover = card.querySelector(".kpi-sector-popover") as HTMLElement;
    expect(popover).not.toBeNull();
    // 12 项都在列表里，不截断；保留滚动能力供用户查看全部
    for (const name of names) {
      expect(within(popover).getByText(name)).toBeInTheDocument();
    }
    // jsdom 不计算 overflowY，但列表有 scroll 容器类、能正常渲染所有条目
    expect(popover.querySelector(".kpi-sector-popover__list")).not.toBeNull();
  });

  it("点击列表项触发 onSectorSelect 回调", () => {
    const handler = vi.fn();
    const meta = makeMeta({
      pulse_up_count: 2,
      pulse_up_sectors: ["半导体", "新能源"],
    });
    render(<ShortTermKpi meta={meta} onSectorSelect={handler} />);
    const card = screen.getByText("单日脉冲上涨").closest("[data-key]") as HTMLElement;
    fireEvent.mouseEnter(card);
    const popover = card.querySelector(".kpi-sector-popover") as HTMLElement;
    const button = within(popover).getByRole("button", { name: "查看半导体的短期异动详情" });
    fireEvent.click(button);
    expect(handler).toHaveBeenCalledWith("半导体");
  });

  it("鼠标离开后悬停浮层关闭", () => {
    const meta = makeMeta({ volume_spike_count: 1, volume_spike_sectors: ["金属"] });
    render(<ShortTermKpi meta={meta} />);
    const card = screen.getByText("量能异动").closest("[data-key]") as HTMLElement;
    fireEvent.mouseEnter(card);
    expect(within(card).getByText("金属")).toBeInTheDocument();
    fireEvent.mouseLeave(card);
    expect(within(card).queryByText("金属")).toBeNull();
  });

  it("value 为 null 时不会弹出悬停浮层", () => {
    const meta = makeMeta({ pulse_up_count: null, pulse_up_sectors: ["半导体"] });
    render(<ShortTermKpi meta={meta} />);
    const card = screen.getByText("单日脉冲上涨").closest("[data-key]") as HTMLElement;
    fireEvent.mouseEnter(card);
    expect(card.querySelector(".kpi-sector-popover")).toBeNull();
  });
});

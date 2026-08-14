/** NextDayWatchPanel 组件的单元测试：覆盖渲染、排序、展开/收起、点击回调、空态与快照切换重置。 */
import { describe, expect, it, vi } from "vitest";
import { fireEvent, render, screen, within } from "@testing-library/react";
import type { ShortTermSector } from "./api";
import { NextDayWatchPanel } from "./NextDayWatchPanel";

function sector(
  sector_name: string,
  short_term_labels: string,
  short_term_composite: number | null,
  short_term_composite_rank: number | null,
  score_eligible = true,
): ShortTermSector {
  return {
    sector_name,
    short_term_labels,
    short_term_composite,
    short_term_composite_rank,
    score_eligible,
  };
}

const SAMPLE_SECTORS: ShortTermSector[] = [
  sector("半导体", "pulse_up,volume_spike", 0.91, 1),
  sector("新能源", "pulse_up,volume_spike", 0.74, 2),
  sector("医药", "pulse_up,volume_spike", 0.62, 3),
  sector("消费", "pulse_up,volume_spike", 0.55, 4),
  sector("银行", "pulse_up,volume_spike", 0.48, 5),
  sector("钢铁", "pulse_up,volume_spike", 0.32, 6),
  sector("地产", "pulse_down,volume_spike", -0.41, 9),
  sector("煤炭", "limit_panic", -0.7, 8),
  sector("软件", "short_rebound_candidate", 0.12, 12),
  sector("建材", "short_breakdown_candidate", -0.18, 15),
  sector("无资格", "pulse_up,volume_spike", 0.95, 1, false),
];

describe("NextDayWatchPanel", () => {
  it("渲染 4 张候选情景卡并展示组名、命中数与板块名", () => {
    render(<NextDayWatchPanel sectors={SAMPLE_SECTORS} onSelect={() => {}} />);

    expect(screen.getByRole("region", { name: "次日研究观察候选" })).toBeInTheDocument();
    expect(screen.getByText("强势跟进观察")).toBeInTheDocument();
    expect(screen.getByText("恐慌修复观察")).toBeInTheDocument();
    expect(screen.getByText("V 形反弹观察")).toBeInTheDocument();
    expect(screen.getByText("破位警惕观察")).toBeInTheDocument();

    const strengthCard = screen.getByRole("article", { name: "强势跟进观察研究观察候选" });
    // 命中总数 = 半导体 + 新能源 + 医药 + 消费 + 银行 + 钢铁 = 6
    expect(within(strengthCard).getByText("6")).toBeInTheDocument();
    // 默认仅展示前 5 条，按综合分降序：半导体 / 新能源 / 医药 / 消费 / 银行。
    expect(within(strengthCard).getByRole("button", { name: "查看 半导体 短期异动详情" })).toBeInTheDocument();
    expect(within(strengthCard).getByRole("button", { name: "查看 银行 短期异动详情" })).toBeInTheDocument();
    expect(within(strengthCard).queryByRole("button", { name: "查看 钢铁 短期异动详情" })).not.toBeInTheDocument();
  });

  it("显示恐慌组与反弹/走弱组各自的命中板块", () => {
    render(<NextDayWatchPanel sectors={SAMPLE_SECTORS} onSelect={() => {}} />);

    const panicCard = screen.getByRole("article", { name: "恐慌修复观察研究观察候选" });
    expect(within(panicCard).getByRole("button", { name: "查看 地产 短期异动详情" })).toBeInTheDocument();
    expect(within(panicCard).getByRole("button", { name: "查看 煤炭 短期异动详情" })).toBeInTheDocument();

    const reboundCard = screen.getByRole("article", { name: "V 形反弹观察研究观察候选" });
    expect(within(reboundCard).getByRole("button", { name: "查看 软件 短期异动详情" })).toBeInTheDocument();

    const breakdownCard = screen.getByRole("article", { name: "破位警惕观察研究观察候选" });
    expect(within(breakdownCard).getByRole("button", { name: "查看 建材 短期异动详情" })).toBeInTheDocument();
  });

  it("未命中时显示空态文案", () => {
    render(<NextDayWatchPanel sectors={[sector("仅有一个 V 形", "short_rebound_candidate", 0.1, 1)]} onSelect={() => {}} />);

    const emptyMessages = screen.getAllByText("今日无此类信号");
    expect(emptyMessages).toHaveLength(3);
  });

  it("默认仅显示前 5 条候选，展开后可看到全部且可收起", () => {
    render(<NextDayWatchPanel sectors={SAMPLE_SECTORS} onSelect={() => {}} />);

    const strengthCard = screen.getByRole("article", { name: "强势跟进观察研究观察候选" });
    const toggle = within(strengthCard).getByRole("button", { name: /展开全部/ });
    expect(toggle).toHaveTextContent("展开全部 6 个");
    fireEvent.click(toggle);

    expect(within(strengthCard).getByRole("button", { name: "查看 钢铁 短期异动详情" })).toBeInTheDocument();
    const collapse = within(strengthCard).getByRole("button", { name: "收起" });
    fireEvent.click(collapse);
    expect(within(strengthCard).queryByRole("button", { name: "查看 钢铁 短期异动详情" })).not.toBeInTheDocument();
  });

  it("点击候选板块按钮调用 onSelect 且 aria-label 包含板块名", () => {
    const onSelect = vi.fn();
    render(<NextDayWatchPanel sectors={SAMPLE_SECTORS} onSelect={onSelect} />);

    fireEvent.click(screen.getByRole("button", { name: "查看 半导体 短期异动详情" }));
    expect(onSelect).toHaveBeenCalledWith("半导体");
  });

  it("综合分为空时显示“综合分数据不足”，并稳定排在末尾", () => {
    const sectors: ShortTermSector[] = [
      sector("A 行业", "pulse_up,volume_spike", 0.5, 1),
      sector("B 行业", "pulse_up,volume_spike", null, 2),
    ];
    render(<NextDayWatchPanel sectors={sectors} onSelect={() => {}} />);
    const card = screen.getByRole("article", { name: "强势跟进观察研究观察候选" });

    const buttons = within(card).getAllByRole("button", { name: /查看 .* 短期异动详情/ });
    expect(buttons[0]).toHaveAccessibleName("查看 A 行业 短期异动详情");
    // B 行业应稳定排在末尾，并展示“数据不足”文本。
    expect(buttons[1]).toHaveAccessibleName("查看 B 行业 短期异动详情");
    expect(within(buttons[1] as HTMLElement).getByText("数据不足")).toBeInTheDocument();
  });

  it("切换 sectors 后展开状态被重置", () => {
    const { rerender } = render(<NextDayWatchPanel sectors={SAMPLE_SECTORS} onSelect={() => {}} />);
    const card = screen.getByRole("article", { name: "强势跟进观察研究观察候选" });
    fireEvent.click(within(card).getByRole("button", { name: /展开全部/ }));
    expect(within(card).getByRole("button", { name: "查看 钢铁 短期异动详情" })).toBeInTheDocument();

    rerender(<NextDayWatchPanel sectors={[sector("唯一", "pulse_up,volume_spike", 0.1, 1)]} onSelect={() => {}} />);
    const nextCard = screen.getByRole("article", { name: "强势跟进观察研究观察候选" });
    expect(within(nextCard).queryByRole("button", { name: "收起" })).not.toBeInTheDocument();
    // 新快照中没有可展开的额外条目，只剩 1 个候选。
    expect(within(nextCard).getByRole("button", { name: "查看 唯一 短期异动详情" })).toBeInTheDocument();
  });

  it("未提供 sectors 时仍渲染 4 张卡并全部为空态", () => {
    render(<NextDayWatchPanel sectors={[]} onSelect={() => {}} />);

    const articles = screen.getAllByRole("article");
    expect(articles).toHaveLength(4);
    expect(screen.getAllByText("今日无此类信号")).toHaveLength(4);
  });
});

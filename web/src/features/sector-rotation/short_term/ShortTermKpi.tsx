/** v2_short_term 顶部 KPI 卡片：当日各类异动命中数。 */
import { Flame, Gauge, Layers, Zap } from "lucide-react";
import { HintIcon } from "../HintIcon";
import type { ShortTermResponseMeta } from "./api";

interface ShortTermKpiProps {
  meta: ShortTermResponseMeta | undefined;
  /** 卡片排版：默认 "row" 横向 1×4；"grid" 切换为 2×2 排版（用于嵌入工作台模块）。 */
  layout?: "row" | "grid";
}

interface KpiItem {
  key: string;
  label: string;
  hint: string;
  value: number | null;
  Icon: typeof Zap;
}

function buildItems(meta: ShortTermResponseMeta | undefined): KpiItem[] {
  return [
    { key: "pulse_up", label: "单日脉冲上涨", hint: "rs_1 与 breadth_up 双证据命中", value: meta?.pulse_up_count ?? null, Icon: Zap },
    { key: "volume_spike", label: "量能异动", hint: "rvol_1_20 或 share_impulse_1d 突破阈值", value: meta?.volume_spike_count ?? null, Icon: Gauge },
    { key: "limit_cluster", label: "涨停集群", hint: "涨停家数 >= 阈值且跌停极少", value: meta?.limit_cluster_count ?? null, Icon: Flame },
    { key: "limit_panic", label: "跌停集群", hint: "跌停家数 >= 阈值且涨停极少", value: meta?.limit_panic_count ?? null, Icon: Layers },
  ];
}

/**
 * 渲染 KPI 行：四个核心异动计数。
 *
 * 输入：API 响应的 meta 字段（可为空表示尚未加载）、排版方式。
 * 输出：4 个图标卡；卡片右上角的 HintIcon 提供对应口径的说明。
 * 默认 row 与既有 CSS 一致；grid 模式输出 data-layout="grid"，由配套 CSS 切换为 2×2。
 */
export function ShortTermKpi({ meta, layout = "row" }: ShortTermKpiProps) {
  const items = buildItems(meta);
  const isGrid = layout === "grid";
  return (
    <section
      className="short-term-kpi"
      aria-label="短期异动 KPI"
      data-layout={isGrid ? "grid" : undefined}
    >
      {items.map((item) => (
        <article key={item.key} className="short-term-kpi__card" data-key={item.key}>
          <div className="short-term-kpi__icon"><item.Icon aria-hidden="true" size={18} /></div>
          <div className="short-term-kpi__body">
            <span className="short-term-kpi__label">{item.label}</span>
            <strong className="short-term-kpi__value">{item.value ?? "—"}</strong>
          </div>
          <HintIcon text={item.hint} tone="warm" placement="left" />
        </article>
      ))}
    </section>
  );
}


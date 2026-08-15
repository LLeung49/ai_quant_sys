
/** v2_short_term 顶部 KPI 卡片：当日各类异动命中数。 */
import { useState } from "react";
import { Flame, Gauge, Layers, Zap } from "lucide-react";
import { HintIcon } from "../HintIcon";
import type { ShortTermResponseMeta } from "./api";

interface ShortTermKpiProps {
  meta: ShortTermResponseMeta | undefined;
  /** 卡片排版：默认 "row"横向 1×4；"grid"切换为 2×2 排版。 */
  layout?: "row" | "grid";
  /** 点击悬停浮层中的板块名称时触发，用于打开短期异动板块抽屉。 */
  onSectorSelect?: (sectorName: string) => void;
}

interface KpiItem {
  key: string;
  label: string;
  hint: string;
  value: number | null;
  sectors: string[];
  Icon: typeof Zap;
}

/** 挂在卡片上的悬停浮层。 */
function KpiSectorPopover({ sectors, onSelect }: { sectors: string[]; onSelect?: (name: string) => void }) {
  return (
    <div className="kpi-sector-popover" role="tooltip">
      <header className="kpi-sector-popover__header">
        <span className="kpi-sector-popover__title">
          <span className="kpi-sector-popover__dot" aria-hidden="true" />
          命中板块
        </span>
        <span className="kpi-sector-popover__count">〈{sectors.length}〉</span>
      </header>
      {sectors.length === 0 ? (
        <p className="kpi-sector-popover__empty">当日无符合阈值的板块</p>
      ) : (
        <ul className="kpi-sector-popover__list">
          {sectors.map((name, index) => (
            <li key={name}>
              <button
                type="button"
                className="kpi-sector-popover__item"
                disabled={!onSelect}
                onClick={onSelect ? () => onSelect(name) : undefined}
                aria-label={onSelect ? "查看" + name + "的短期异动详情" : undefined}
              >
                <span className="kpi-sector-popover__index" aria-hidden="true">{String(index + 1).padStart(2, "0")}</span>
                <span className="kpi-sector-popover__name">{name}</span>
                {onSelect && <span className="kpi-sector-popover__chevron" aria-hidden="true">›</span>}
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

function buildItems(meta: ShortTermResponseMeta | undefined): KpiItem[] {
  return [
    {
      key: "pulse_up",
      label: "单日脉冲上涨",
      hint: "rs_1 与 breadth_up 双证据命中",
      value: meta?.pulse_up_count ?? null,
      sectors: meta?.pulse_up_sectors ?? [],
      Icon: Zap,
    },
    {
      key: "volume_spike",
      label: "量能异动",
      hint: "rvol_1_20 或 share_impulse_1d 突破阈值",
      value: meta?.volume_spike_count ?? null,
      sectors: meta?.volume_spike_sectors ?? [],
      Icon: Gauge,
    },
    {
      key: "limit_cluster",
      label: "涨停集群",
      hint: "涨停占比 ≥ 5% 且跌停占比 ≤ 1%",
      value: meta?.limit_cluster_count ?? null,
      sectors: meta?.limit_cluster_sectors ?? [],
      Icon: Flame,
    },
    {
      key: "limit_panic",
      label: "跌停集群",
      hint: "跌停占比 ≥ 5% 且涨停占比 ≤ 1%",
      value: meta?.limit_panic_count ?? null,
      sectors: meta?.limit_panic_sectors ?? [],
      Icon: Layers,
    },
  ];
}

/**
 * 渲染 KPI 行：四个核心异动计数。 */
export function ShortTermKpi({ meta, layout = "row", onSectorSelect }: ShortTermKpiProps) {
  const items = buildItems(meta);
  const isGrid = layout === "grid";
  const [hoverKey, setHoverKey] = useState<string | null>(null);
  return (
    <section
      className="short-term-kpi"
      aria-label="短期异动 KPI"
      data-layout={isGrid ? "grid" : undefined}
    >
      {items.map((item) => {
        const isHover = hoverKey === item.key;
        const showPopover = isHover && item.value != null;
        return (
          <article
            key={item.key}
            className="short-term-kpi__card"
            data-key={item.key}
            onMouseEnter={() => setHoverKey(item.key)}
            onMouseLeave={() => setHoverKey(null)}
            onFocus={() => setHoverKey(item.key)}
            onBlur={() => setHoverKey(null)}
          >
            <div className="short-term-kpi__icon"><item.Icon aria-hidden="true" size={18} /></div>
            <div className="short-term-kpi__body">
              <span className="short-term-kpi__label">{item.label}</span>
              <strong
                className="short-term-kpi__value"
                tabIndex={0}
                aria-describedby={showPopover ? "kpi-sector-" + item.key : undefined}
              >
                {item.value ?? "—"}
              </strong>
            </div>
            <HintIcon text={item.hint} tone="warm" placement="left" />
            {showPopover && (
              <div id={"kpi-sector-" + item.key} className="kpi-sector-popover-wrapper">
                <KpiSectorPopover sectors={item.sectors} onSelect={onSectorSelect} />
              </div>
            )}
          </article>
        );
      })}
    </section>
  );
}

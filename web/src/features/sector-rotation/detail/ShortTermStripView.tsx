/**
 * 5 日连续性 strip 组件。
 *
 * 渲染单行业近 N 个交易日的短期命中轨迹,与 Layer C chip 形状完全一致。
 * 设计要点:
 * - 内部调用 buildShortTermStripRow 把 history 转换为 cell 序列;
 * - 每个 cell 背景色 = INTENSITY_META[intensity].softColor;
 * - 图标 = SHORT_TERM_GLYPH_PATHS 主标签 SVG path,与 Layer C 形状复用;
 * - "当日"(asOfDate 匹配)cell 加 .is-now class;
 * - "无命中"cell 灰底 + 短横线;
 * - 加载/错误态分别显示进度提示,不抛错;
 * - aria-label="5 日连续性时间轴" 提供语义。
 */

import { getShortTermGlyphColor, getShortTermGlyphPath, getShortTermGlyphSize } from "../chart/shortTermHalo";
import { getShortTermChipText } from "../chart/shortTermHalo";
import { INTENSITY_META, getShortTermLabelMeta } from "../short_term/labels";
import type { ShortTermHistoryResponse } from "../short_term/api";
import { STRIP_WINDOW_DAYS, buildShortTermStripRow, describeStripCell, type StripCell } from "./shortTermStrip";

export interface ShortTermStripViewProps {
  history: ShortTermHistoryResponse | null;
  sectorName: string;
  asOfDate: string;
  days?: number;
  isLoading?: boolean;
  isError?: boolean;
}

interface CellVisualProps {
  cell: StripCell;
  isNow: boolean;
}

/** 单个 strip cell 的视觉渲染:背景色 + SVG 形状 + 短码文本。 */
function StripCellView({ cell, isNow }: CellVisualProps) {
  const intensityMeta = cell.intensity ? INTENSITY_META[cell.intensity] : null;
  const bg = intensityMeta?.softColor ?? "rgba(127,141,163,0.10)";
  const border = intensityMeta?.color ?? "rgba(127,141,163,0.4)";
  const primaryLabel = cell.primaryLabel;

  if (!primaryLabel || !cell.intensity) {
    return (
      <td
        className="short-term-strip__cell is-empty"
        style={{ background: bg }}
        aria-label={`${cell.as_of_date} 无命中`}
      >
        <span aria-hidden="true">—</span>
      </td>
    );
  }

  const [w, h] = getShortTermGlyphSize(primaryLabel, cell.intensity);
  const path = getShortTermGlyphPath(primaryLabel, cell.intensity);
  const color = getShortTermGlyphColor(primaryLabel, cell.intensity);
  const meta = getShortTermLabelMeta(primaryLabel);
  const shortText = getShortTermChipText(primaryLabel) ?? primaryLabel;
  const desc = describeStripCell(cell);
  const tooltip = [
    cell.as_of_date,
    meta?.label ?? primaryLabel,
    desc.ret_1 != null ? `1日收益 ${(desc.ret_1 * 100).toFixed(2)}%` : null,
    desc.rs_1 != null ? `1日强度 ${(desc.rs_1 * 100).toFixed(2)}%` : null,
    desc.rvol_1_20 != null ? `量比 ${desc.rvol_1_20.toFixed(2)}` : null,
    desc.labels.length > 1 ? `标签 ${desc.labels.join("/")}` : null,
  ]
    .filter(Boolean)
    .join("\n");

  return (
    <td
      className={`short-term-strip__cell is-${cell.intensity}${isNow ? " is-now" : ""}`}
      style={{ background: bg, borderLeft: `4px solid ${border}` }}
      title={tooltip}
      aria-label={tooltip.replace(/\n/g, ", ")}
    >
      <svg width={w} height={h} viewBox="0 0 14 14" aria-hidden="true" focusable="false">
        <path d={path} fill={color} />
      </svg>
      <span className="short-term-strip__cell-text">{shortText}</span>
    </td>
  );
}

/** 当日(T)列的视觉差异:边框高亮 + 单元格右上角小圆点。 */
function NowIndicator() {
  return <span className="short-term-strip__now-dot" aria-hidden="true" />;
}

export function ShortTermStripView({ history, sectorName, asOfDate, days = STRIP_WINDOW_DAYS, isLoading = false, isError = false }: ShortTermStripViewProps) {
  // buildShortTermStripRow 按 as_of_date desc 返回(最新在前),这里反转成 asc(最旧在前),
  // 与下方 K 线图 X 轴方向对齐,方便用户左右对照。
  const cells = buildShortTermStripRow(history, sectorName, asOfDate, days).reverse();
  const isNow = (cell: StripCell) => cell.as_of_date === asOfDate;

  // 历史不足 N 天时,在右侧补空 cell,使 strip 仍对齐 N 列且保持左旧右新。
  const paddedCells: (StripCell | null)[] = [...cells];
  while (paddedCells.length < days) {
    paddedCells.push(null);
  }
  const visibleCells = paddedCells.slice(0, days);

  return (
    <section className="short-term-strip" aria-label="5 日连续性时间轴">
      <header className="short-term-strip__header">
        <div>
          <p className="short-term-strip__eyebrow">短期连续性</p>
          <h3 className="short-term-strip__title">{days} 日连续性</h3>
        </div>
        <p className="short-term-strip__hint">橙=强异动 · 琥珀=中等异动 · 蓝绿=轻度异动 · 灰=无命中 · 加边框=当日</p>
      </header>
      {isError ? (
        <p className="short-term-strip__error" role="status">历史数据暂不可用</p>
      ) : isLoading ? (
        <p className="short-term-strip__loading" role="status">加载中…</p>
      ) : (
        <table className="short-term-strip__table">
          <thead>
            <tr>
              {visibleCells.map((cell, index) => (
                <th key={`hdr-${index}`} className="short-term-strip__th" scope="col">
                  {cell ? cell.as_of_date.slice(5) : "—"}
                  {cell && isNow(cell) ? <NowIndicator /> : null}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            <tr>
              {visibleCells.map((cell, index) =>
                cell ? (
                  <StripCellView key={`cell-${cell.as_of_date}-${index}`} cell={cell} isNow={isNow(cell)} />
                ) : (
                  <td
                    key={`empty-${index}`}
                    className="short-term-strip__cell is-empty"
                    style={{ background: "rgba(127,141,163,0.10)" }}
                    aria-label="数据不足"
                  >
                    <span aria-hidden="true">—</span>
                  </td>
                ),
              )}
            </tr>
          </tbody>
        </table>
      )}
    </section>
  );
}
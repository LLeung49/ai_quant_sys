/** 板块 K 线放大行情窗口：使用原生 dialog 置于顶层，并复用抽屉已加载的行情数据。 */
import { useEffect, useMemo, useRef, type RefObject } from "react";
import { createPortal } from "react-dom";
import { X } from "lucide-react";
import { LazySectorKlineChart } from "./LazySectorKlineChart";
import type { SectorKlineResponse } from "./sectorKlineApi";
import { KLINE_WINDOWS, type KlineWindow } from "./sectorKlineConfig";

/** 放大行情窗口的输入属性。 */
export interface SectorKlineModalProps {
  /** 已由抽屉缩略卡加载并完成 Zod 校验的同一份行情响应，不在弹窗内重新请求。 */
  data: SectorKlineResponse;
  /** 与缩略图共享的离散可见交易日窗口。 */
  visibleCount: KlineWindow;
  /** 用户切换 60/120/250 日窗口时的受控状态回调。 */
  onVisibleCountChange: (visibleCount: KlineWindow) => void;
  /** 打开弹窗的按钮引用，关闭后恢复键盘焦点。 */
  openerRef: RefObject<HTMLButtonElement | null>;
  /** 关闭弹窗的唯一状态回调，由抽屉负责卸载本组件。 */
  onClose: () => void;
  /** 当前板块阶段标签，仅用于行情摘要，不参与买卖判断。 */
  phaseLabel?: string;
}

/**
 * 格式化数值，避免行情摘要在缺失或无穷数值时渲染异常。
 *
 * 参数：value 为 API 返回的数值；fractionDigits 为小数展示位数。
 * 返回：有限数值的本地化文本，或“--”占位。
 * 异常：无；非法数值会安全降级为占位文本。
 */
function formatNumber(value: number | undefined, fractionDigits = 2): string {
  return typeof value === "number" && Number.isFinite(value)
    ? value.toLocaleString("zh-CN", { maximumFractionDigits: fractionDigits })
    : "--";
}

/**
 * 映射滑块离散索引到受限的交易日窗口，杜绝产生任意中间日数。
 *
 * 参数：index 为 range 控件的 0/1/2 索引。
 * 返回：60、120 或 250 中的一个合法窗口值。
 * 异常：无；越界索引按最近有效档位处理。
 */
function windowFromRangeIndex(index: number): KlineWindow {
  return KLINE_WINDOWS[Math.max(0, Math.min(KLINE_WINDOWS.length - 1, index))] ?? KLINE_WINDOWS[0];
}

/**
 * 渲染可放大的板块三联图弹窗。
 *
 * 参数：已加载行情、共享窗口状态、焦点来源及关闭回调。
 * 返回：通过 Portal 挂载到 document.body 的原生 modal dialog。
 * 异常：浏览器原生 dialog 初始化异常不会向外抛出；组件会保持可卸载状态，避免影响抽屉其他内容。
 */
export function SectorKlineModal({ data, visibleCount, onVisibleCountChange, openerRef, onClose, phaseLabel = "研究观察" }: SectorKlineModalProps) {
  const dialogRef = useRef<HTMLDialogElement>(null);
  const latestBar = data.bars.at(-1);
  const previousBar = data.bars.at(-2);
  const closeChange = useMemo(() => {
    if (!latestBar || !previousBar || previousBar.close === 0) return undefined;
    return ((latestBar.close - previousBar.close) / previousBar.close) * 100;
  }, [latestBar, previousBar]);

  /** 请求父级卸载弹窗并同步恢复到明确的打开控件。 */
  const requestClose = () => {
    openerRef.current?.focus();
    onClose();
  };

  useEffect(() => {
    const dialog = dialogRef.current;
    if (!dialog) return undefined;
    const previousOverflow = document.body.style.overflow;
    document.body.style.overflow = "hidden";
    // showModal 使 dialog 进入浏览器 top layer，天然避免被抽屉及其工具栏裁剪。
    if (!dialog.open) dialog.showModal();
    return () => {
      document.body.style.overflow = previousOverflow;
      if (dialog.open) dialog.close();
      // 日期/行业切换导致的被动关闭同样应回到触发按钮，方便连续键盘操作。
      if (openerRef.current?.isConnected) openerRef.current.focus();
    };
  }, [openerRef]);

  const selectedIndex = KLINE_WINDOWS.indexOf(visibleCount);
  const chartLabel = `${data.sector_name} 截至 ${data.actual_end_date} 的日 K 线、成交量和 MACD 放大图`;

  return createPortal(
    <dialog ref={dialogRef} className="sector-kline-dialog" aria-label={`${data.sector_name}放大行情图`}
      onCancel={(event) => { event.preventDefault(); requestClose(); }}
      onClick={(event) => { if (event.target === event.currentTarget) requestClose(); }}>
      <section className="sector-kline-modal" aria-label={`${data.sector_name} 行情详情`}>
        <header className="sector-kline-modal__header">
          <div><p>SECTOR MARKET</p><h2>{data.sector_name}</h2><span>申万 {data.sector_level} 级 · 截至 {data.actual_end_date}</span></div>
          <button type="button" className="icon-button" aria-label={`关闭${data.sector_name}放大行情`} onClick={requestClose}><X aria-hidden="true" /></button>
        </header>
        <dl className="sector-kline-modal__summary">
          <div><dt>收盘指数</dt><dd>{formatNumber(latestBar?.close)}</dd></div>
          <div><dt>涨跌幅</dt><dd className={closeChange == null ? "" : closeChange >= 0 ? "is-up" : "is-down"}>{closeChange == null ? "--" : `${closeChange >= 0 ? "+" : ""}${closeChange.toFixed(2)}%`}</dd></div>
          <div><dt>阶段</dt><dd>{phaseLabel}</dd></div>
          <div><dt>成交额</dt><dd>{formatNumber(latestBar?.amount, 0)}</dd></div>
        </dl>
        <div className="sector-kline-modal__toolbar" aria-label="放大行情观察窗口">
          <div className="sector-kline-window-buttons">{KLINE_WINDOWS.map((windowValue) => <button key={windowValue} type="button" className={visibleCount === windowValue ? "is-active" : ""} aria-label={`显示最近 ${windowValue} 个交易日`} aria-pressed={visibleCount === windowValue} onClick={() => onVisibleCountChange(windowValue)}>{windowValue} 日</button>)}</div>
          <label className="sector-kline-range-label">可见窗口<input type="range" min="0" max="2" step="1" value={selectedIndex < 0 ? 1 : selectedIndex} aria-label="选择放大行情可见窗口" onChange={(event) => onVisibleCountChange(windowFromRangeIndex(Number(event.target.value)))} /></label>
        </div>
        <div className="sector-kline-modal__chart-wrap"><LazySectorKlineChart bars={data.bars} mode="expanded" visibleCount={visibleCount} ariaLabel={chartLabel} /></div>
      </section>
    </dialog>, document.body,
  );
}

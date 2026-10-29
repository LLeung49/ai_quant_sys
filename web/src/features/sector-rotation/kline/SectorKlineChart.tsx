/** 板块 K 线 React 容器：仅管理可见尺寸、运行时创建和局部错误降级。 */
import { useEffect, useRef, useState } from "react";
import type { SectorKlineResponse } from "./sectorKlineApi";
import {
  createSectorKlineRuntime,
  type SectorKlineChartMode,
  type SectorKlineRuntime,
} from "./klinechartRuntime";

/** 板块 K 线图表组件的输入属性。 */
export interface SectorKlineChartProps {
  /** 已通过 API 契约校验且按交易日升序的 K 线。 */
  bars: SectorKlineResponse["bars"];
  waves?: SectorKlineResponse["waves"];
  /** 缩略图或弹窗放大图模式。 */
  mode: SectorKlineChartMode;
  /** 当前希望显示的最近交易日根数。 */
  visibleCount: number;
  /** 将板块、截止日和图表组成传达给读屏软件的中文说明。 */
  ariaLabel: string;
}

/**
 * 在有效 DOM 尺寸下挂载板块 K 线运行时。
 *
 * 输入：已校验日 K 线、展示模式、可见根数和无障碍说明。
 * 输出：图表容器；初始化失败仅显示本组件 ``role=alert``，不会影响详情抽屉其余内容。
 * 异常：第三方图表的异步异常被本地捕获并降级，渲染期异常交由 ``KlineErrorBoundary`` 处理。
 */
export function SectorKlineChart({ bars, waves, mode, visibleCount, ariaLabel }: SectorKlineChartProps) {
  const containerRef = useRef<HTMLDivElement>(null);
  const runtimeRef = useRef<SectorKlineRuntime | null>(null);
  const visibleCountRef = useRef(visibleCount);
  const [error, setError] = useState(false);
  visibleCountRef.current = visibleCount;

  useEffect(() => {
    runtimeRef.current?.setVisibleCount(visibleCount);
  }, [visibleCount]);

  useEffect(() => {
    const container = containerRef.current;
    if (!container) return undefined;
    let cancelled = false;
    // 每次 bars/mode effect 都拥有独立的初始化状态，StrictMode 或快速切换不会被旧 Promise 卡住。
    let initializing = false;
    let initializationFailed = false;
    setError(false);

    const initializeOrResize = () => {
      if (cancelled || container.clientWidth <= 0 || container.clientHeight <= 0) return;
      if (runtimeRef.current) {
        runtimeRef.current.resize();
        return;
      }
      // 同一份 bars/mode 的失败只展示局部提示，不因连续 ResizeObserver 回调无休止重试。
      if (initializing || initializationFailed) return;
      initializing = true;
      void createSectorKlineRuntime({ container, bars, waves, mode, visibleCount: visibleCountRef.current })
        .then((runtime) => {
          // 异步加载期间若已切换板块/模式或卸载，立即释放迟到实例，禁止旧图闪现。
          if (cancelled) {
            runtime.dispose();
            return;
          }
          runtimeRef.current = runtime;
          runtime.setVisibleCount(visibleCountRef.current);
        })
        .catch(() => {
          if (!cancelled) {
            initializationFailed = true;
            setError(true);
          }
        })
        .finally(() => {
          initializing = false;
        });
    };

    const resizeObserver = new ResizeObserver(initializeOrResize);
    resizeObserver.observe(container);
    initializeOrResize();
    return () => {
      cancelled = true;
      resizeObserver.disconnect();
      runtimeRef.current?.dispose();
      runtimeRef.current = null;
    };
  }, [bars, waves, mode]);

  return <div className={`sector-kline-chart-shell sector-kline-chart-shell--${mode}`}>
    {/* 容器在失败时仍须保留，后续切换板块、日期或模式才能重新获得 ref 并初始化。 */}
    <div ref={containerRef} className={`sector-kline-chart sector-kline-chart--${mode}`} role="img" aria-label={ariaLabel} />
    {error && <div className="sector-kline-chart__fallback" role="alert">行情图初始化失败，请重试</div>}
  </div>;
}

export default SectorKlineChart;

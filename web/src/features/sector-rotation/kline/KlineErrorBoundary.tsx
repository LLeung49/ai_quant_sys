/** 板块 K 线局部渲染错误边界，防止图表异常导致详情抽屉或整页白屏。 */
import { Component, type ErrorInfo, type ReactNode } from "react";

/** 错误边界的输入属性。 */
interface KlineErrorBoundaryProps {
  /** 可能抛出渲染异常的 K 线卡片或图表节点。 */
  children: ReactNode;
}

/** 错误边界的内部渲染状态。 */
interface KlineErrorBoundaryState {
  /** 是否已捕获子树渲染异常。 */
  hasError: boolean;
}

/**
 * 捕获 K 线子树渲染异常，局部替换为可理解的失败提示。
 *
 * 输入：子树 React 节点。
 * 输出：正常时原样渲染子树，异常时输出 ``role=alert`` 降级提示。
 * 异常：不重新抛出子树异常；日志保留给浏览器开发工具定位。
 */
export class KlineErrorBoundary extends Component<KlineErrorBoundaryProps, KlineErrorBoundaryState> {
  state: KlineErrorBoundaryState = { hasError: false };

  /**
   * 将子树错误转换为本地降级状态。
   *
   * 输入：React 捕获的原始错误。
   * 输出：使下一次渲染展示局部失败提示的状态对象。
   * 异常：无；错误细节由 ``componentDidCatch`` 记录。
   */
  static getDerivedStateFromError(_error: Error): KlineErrorBoundaryState {
    return { hasError: true };
  }

  /**
   * 在错误边界捕获子树异常后记录调试上下文。
   *
   * 输入：原始错误和 React 组件栈信息。
   * 输出：无；仅向控制台输出便于开发环境定位。
   * 异常：无；避免日志失败反向影响错误边界。
   */
  componentDidCatch(error: Error, info: ErrorInfo): void {
    console.error("板块 K 线图渲染异常", error, info);
  }

  /**
   * 渲染 K 线子树或局部失败提示。
   *
   * 输入：无；使用当前错误边界状态和 children。
   * 输出：子树节点或 ``role=alert`` 降级提示。
   * 异常：子树异常由本错误边界捕获并改为提示。
   */
  render(): ReactNode {
    if (this.state.hasError) {
      return <div className="sector-kline-chart__fallback" role="alert">行情图初始化失败，请重试</div>;
    }
    return this.props.children;
  }
}

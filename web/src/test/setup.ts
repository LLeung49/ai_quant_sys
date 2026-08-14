/** 前端测试运行前加载 DOM 断言扩展。 */
import "@testing-library/jest-dom";

/** 为 jsdom 补齐原生 dialog 的最小可观察行为；生产代码仍直接使用浏览器实现。 */
if (typeof HTMLDialogElement !== "undefined" && !HTMLDialogElement.prototype.showModal) {
  HTMLDialogElement.prototype.showModal = function showModal(): void { this.setAttribute("open", ""); };
}
if (typeof HTMLDialogElement !== "undefined" && !HTMLDialogElement.prototype.close) {
  HTMLDialogElement.prototype.close = function close(): void { this.removeAttribute("open"); };
}

/**
 * ECharts / zrender 依赖 HTMLCanvasElement 的 getContext。
 * jsdom 默认未实现 canvas，此处提供最小桩实现，避免抛错导致组件被卸载。
 */
if (typeof HTMLCanvasElement !== "undefined") {
  const canvasProto = HTMLCanvasElement.prototype as unknown as {
    getContext?: (...args: unknown[]) => unknown;
    __patchedForEcharts?: boolean;
  };
  if (!canvasProto.__patchedForEcharts) {
    const stubContext = new Proxy(
      {},
      {
        get(_target, prop) {
          if (prop === "measureText") {
            return () => ({ width: 0 });
          }
          if (prop === "getImageData") {
            return () => ({ data: new Uint8ClampedArray(4) });
          }
          return typeof prop === "string" ? () => undefined : undefined;
        },
      },
    );
    canvasProto.getContext = () => stubContext;
    canvasProto.__patchedForEcharts = true;
  }
}

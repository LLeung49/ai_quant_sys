/** 前端测试运行前加载 DOM 断言扩展。 */
import "@testing-library/jest-dom";

/** 为 jsdom 补齐原生 dialog 的最小可观察行为；生产代码仍直接使用浏览器实现。 */
if (typeof HTMLDialogElement !== "undefined" && !HTMLDialogElement.prototype.showModal) {
  HTMLDialogElement.prototype.showModal = function showModal(): void { this.setAttribute("open", ""); };
}
if (typeof HTMLDialogElement !== "undefined" && !HTMLDialogElement.prototype.close) {
  HTMLDialogElement.prototype.close = function close(): void { this.removeAttribute("open"); };
}

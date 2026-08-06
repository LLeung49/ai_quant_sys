/** 板块轮动页面骨架的用户可见行为测试。 */
import { render, screen } from "@testing-library/react";
import { App } from "./App";

describe("App", () => {
  it("展示板块轮动标题、加载态与研究风险提示", () => {
    render(<App />);

    expect(screen.getByRole("heading", { name: "板块轮动" })).toBeInTheDocument();
    expect(screen.getByText("正在加载最新板块快照…")).toBeInTheDocument();
    expect(screen.getByText("本页面仅供量化研究参考，不构成投资建议。")).toBeInTheDocument();
  });
});

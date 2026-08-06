/** 板块轮动仅注册实际使用的 ECharts 模块，避免打包完整图表库。 */
import * as echarts from "echarts/core";
import { LineChart, ScatterChart } from "echarts/charts";
import { GridComponent, MarkAreaComponent, TooltipComponent } from "echarts/components";
import { CanvasRenderer } from "echarts/renderers";

echarts.use([LineChart, ScatterChart, GridComponent, MarkAreaComponent, TooltipComponent, CanvasRenderer]);

export { echarts };

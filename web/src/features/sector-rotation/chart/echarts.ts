/** 鏉垮潡杞姩浠呮敞鍐屽疄闄呬娇鐢ㄧ殑 ECharts 妯″潡锛岄伩鍏嶆墦鍖呭畬鏁村浘琛ㄥ簱銆?*/
import * as echarts from "echarts/core";
import { LineChart, ScatterChart, TreemapChart } from "echarts/charts";
import { GridComponent, MarkAreaComponent, TooltipComponent, VisualMapComponent } from "echarts/components";
import { CanvasRenderer } from "echarts/renderers";

echarts.use([LineChart, ScatterChart, TreemapChart, GridComponent, MarkAreaComponent, TooltipComponent, VisualMapComponent, CanvasRenderer]);

export { echarts };


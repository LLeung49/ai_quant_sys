# 风险调整后 ETF 样本外验证决策报告

## 决策

- 结论：`do_not_trade`
- 建议：不交易，直至补齐并复核缺失或无效证据。
- 阻断项：stable_parameter_region

## 策略与买入持有比较

| 指标 | 策略 | 买入持有 | 差异（策略－买入持有） |
| --- | ---: | ---: | ---: |
| annual_return | -0.038397 | 0.214438 | -0.252835 |
| sharpe | -0.695633 | 1.257780 | -1.953413 |
| Sortino | -0.715945 | 1.979345 | -2.695290 |
| calmar | -0.964577 | 2.541680 | -3.506257 |
| cvar5 | -0.009667 | -0.023791 | 0.014124 |
| max_drawdown | -0.039807 | -0.084369 | 0.044562 |
| turnover | 3.883007 | 0.978856 | 2.904151 |
| total_cost | 191.191080 | 39.945600 | 151.245480 |

## OOS 分布

{
  "window_count": 1,
  "win_rate": 0.0,
  "median_excess_return": -0.12040017663456226,
  "best_excess_return": -0.12040017663456226,
  "worst_excess_return": -0.12040017663456226
}

## 执行、换手与成本

{
  "strategy": {
    "invested_sessions": 71,
    "cash_sessions": 55,
    "exposure_ratio": 0.5634920634920635,
    "turnover": 3.883006960708855,
    "total_cost": 191.19108,
    "cost_drag": 0.0019119108
  },
  "buy_and_hold": {
    "invested_sessions": 126,
    "cash_sessions": 0,
    "exposure_ratio": 1.0,
    "turnover": 0.9788556971868236,
    "total_cost": 39.9456,
    "cost_drag": 0.00039945599999999996
  }
}

## 数据边界、配置与训练曲面

{
  "data_cutoff": "2026-09-10",
  "config_hashes": [
    "928ff9246144538cdea5af2f6efde5b0355c71d0abf4f11f954532e7de8195ce"
  ],
  "training_surface": [
    {
      "window_id": "wf_000",
      "grid": [],
      "trend": []
    }
  ],
  "run_manifest": {
    "schema_version": 1,
    "runner": "run_instrument_validation",
    "source_provider": "ValidationMarketDataProvider",
    "data_cutoff": "2026-09-10",
    "requested_start": "2024-10-15",
    "data_fingerprint": "6138cb6ff0e35f14c9aeba928b3d22798bfa3b5e5b3477492e4c226ee8581392",
    "target": {
      "exposure_id": "csi_a500",
      "stock_code": "563360.SH",
      "sub_layer": "broad_domestic_core",
      "scope": "reference_only"
    },
    "selected_configs": [
      {
        "window_id": "wf_000",
        "config_hash": "928ff9246144538cdea5af2f6efde5b0355c71d0abf4f11f954532e7de8195ce",
        "config": {
          "grid": {
            "step_pct": 0.02,
            "unit_pct": 0.1,
            "initial_model": "fixed",
            "fixed_initial_pct": 0.5,
            "max_grid_per_day": 1,
            "atr_stop_multiple": 3.0,
            "cooldown_sessions": 5
          },
          "trend": {
            "stop_n": 2.0,
            "risk_per_unit": 0.005,
            "add_n": 0.5,
            "max_units": 4,
            "require_macd_bullish": true,
            "amount_ratio_min": null
          },
          "cost": {
            "commission_rate": 0.0001,
            "minimum_commission": 5.0,
            "slippage_bps": 3.0,
            "sell_tax_rate": 0.0,
            "transfer_fee_rate": 0.0
          }
        }
      }
    ],
    "screened_axes": {
      "grid": [
        "step_pct",
        "unit_pct",
        "fixed_initial_pct",
        "atr_stop_multiple",
        "cooldown_sessions"
      ],
      "trend": [
        "risk_per_unit",
        "add_n",
        "max_units",
        "amount_ratio_min",
        "stop_n",
        "require_macd_bullish"
      ]
    }
  }
}

## 事件归因

[
  {
    "window_id": "wf_000",
    "trade_points": [
      {
        "event_date": "2025-10-30",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 39400,
        "raw_price": 1.2663798
      },
      {
        "event_date": "2025-11-05",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 8000,
        "raw_price": 1.2203659999999998
      },
      {
        "event_date": "2025-11-07",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 7900,
        "raw_price": 1.2486253
      },
      {
        "event_date": "2025-11-21",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 8100,
        "raw_price": 1.2073621
      },
      {
        "event_date": "2025-11-24",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 47600,
        "raw_price": 1.1886433
      },
      {
        "event_date": "2025-12-08",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 39200,
        "raw_price": 1.2353705000000001
      },
      {
        "event_date": "2025-12-29",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 7700,
        "raw_price": 1.2646205
      },
      {
        "event_date": "2026-01-07",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 7500,
        "raw_price": 1.3096070000000002
      },
      {
        "event_date": "2026-01-13",
        "kind": "fill",
        "reason": "grid_to_trend_rebalance",
        "shares": 13900,
        "raw_price": 1.329601
      },
      {
        "event_date": "2026-01-22",
        "kind": "fill",
        "reason": "trend_stop",
        "shares": 10100,
        "raw_price": 1.3236028000000002
      },
      {
        "event_date": "2026-02-27",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 37700,
        "raw_price": 1.3253975
      },
      {
        "event_date": "2026-03-05",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 7500,
        "raw_price": 1.3063918
      },
      {
        "event_date": "2026-03-20",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 45200,
        "raw_price": 1.2716184000000001
      },
      {
        "event_date": "2026-04-23",
        "kind": "fill",
        "reason": "trend_entry",
        "shares": 11700,
        "raw_price": 1.3454035
      },
      {
        "event_date": "2026-05-07",
        "kind": "fill",
        "reason": "trend_add",
        "shares": 10100,
        "raw_price": 1.3774131
      }
    ],
    "by_reason": {
      "grid_initialize": {
        "reason": "grid_initialize",
        "fill_count": 3,
        "shares": 116300,
        "traded_value": "148289.3734700000039200"
      },
      "grid_buy": {
        "reason": "grid_buy",
        "fill_count": 3,
        "shares": 23600,
        "traded_value": "29340.4995099999984000"
      },
      "grid_sell": {
        "reason": "grid_sell",
        "fill_count": 3,
        "shares": 23100,
        "traded_value": "29423.7702200000015000"
      },
      "grid_stop": {
        "reason": "grid_stop",
        "fill_count": 2,
        "shares": 92800,
        "traded_value": "114056.5727600000045200"
      },
      "grid_to_trend_rebalance": {
        "reason": "grid_to_trend_rebalance",
        "fill_count": 1,
        "shares": 13900,
        "traded_value": "18481.453900"
      },
      "trend_stop": {
        "reason": "trend_stop",
        "fill_count": 1,
        "shares": 10100,
        "traded_value": "13368.3882800000020200"
      },
      "trend_entry": {
        "reason": "trend_entry",
        "fill_count": 1,
        "shares": 11700,
        "traded_value": "15741.2209500"
      },
      "trend_add": {
        "reason": "trend_add",
        "fill_count": 1,
        "shares": 10100,
        "traded_value": "13911.8723100"
      }
    },
    "invested_sessions": 71,
    "cash_sessions": 55,
    "rejected_order_count": 0
  }
]

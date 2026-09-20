# 风险调整后 ETF 样本外验证决策报告

## 决策

- 结论：`do_not_trade`
- 建议：不交易，直至补齐并复核缺失或无效证据。
- 阻断项：data_valid, missing_research_evidence, strategy_metrics, benchmark_metrics, strategy_exposure, benchmark_exposure, bar coverage must include the requested start and end dates, run_manifest, experiment_metadata

## 策略与买入持有比较

证据缺失或无效，不能生成策略与买入持有比较。

## OOS 分布

无可用 OOS 窗口证据。

## 执行、换手与成本

执行证据缺失或无效。

## 数据边界、配置与训练曲面

{
  "data_cutoff": "2026-09-11",
  "config_hashes": [],
  "training_surface": [],
  "run_manifest": {
    "benchmark_specs": [
      {
        "benchmark_id": "buy_and_hold",
        "rebalance_sessions": null,
        "target_weight": 1.0,
        "version": "1"
      }
    ],
    "experiment": {
      "allowed_axes": {
        "atr_stop_multiple": [
          2.0,
          3.0,
          4.0
        ],
        "cooldown_sessions": [
          0,
          3,
          5,
          10
        ],
        "require_macd_bullish": [
          false,
          true
        ],
        "step_pct": [
          0.01,
          0.015,
          0.02,
          0.025,
          0.03,
          0.035,
          0.04,
          0.045,
          0.05,
          0.055,
          0.06
        ],
        "stop_n": [
          1.5,
          2.0,
          2.5,
          3.0
        ],
        "unit_pct": [
          0.05,
          0.1,
          0.15,
          0.2
        ]
      },
      "as_of_date": "2026-09-11",
      "benchmarks": [
        {
          "benchmark_id": "buy_and_hold",
          "rebalance_sessions": null,
          "target_weight": 1.0,
          "version": "1"
        }
      ],
      "experiment_id": "hk_internet",
      "start_date": "2021-01-01",
      "strategy": {
        "config": {
          "cost": {
            "commission_rate": 0.0001,
            "minimum_commission": 5.0,
            "sell_tax_rate": 0.0,
            "slippage_bps": 3.0,
            "transfer_fee_rate": 0.0
          },
          "grid": {
            "atr_stop_multiple": 3.0,
            "cooldown_sessions": 5,
            "fixed_initial_pct": 0.5,
            "initial_model": "fixed",
            "max_grid_per_day": 1,
            "step_pct": 0.02,
            "unit_pct": 0.1
          },
          "trend": {
            "add_n": 0.5,
            "amount_ratio_min": null,
            "max_units": 4,
            "require_macd_bullish": true,
            "risk_per_unit": 0.005,
            "stop_n": 2.0
          }
        },
        "policy_id": "full_adaptive",
        "strategy_id": "full_adaptive",
        "version": "1"
      },
      "target_codes": [
        "513330.SH"
      ]
    },
    "experiment_hash": "d940e723f1ba1fa36fa356dd983d34b956357817819bf390b49e14c96d30ec02",
    "experiment_windows": [],
    "strategy_spec": {
      "config": {
        "cost": {
          "commission_rate": 0.0001,
          "minimum_commission": 5.0,
          "sell_tax_rate": 0.0,
          "slippage_bps": 3.0,
          "transfer_fee_rate": 0.0
        },
        "grid": {
          "atr_stop_multiple": 3.0,
          "cooldown_sessions": 5,
          "fixed_initial_pct": 0.5,
          "initial_model": "fixed",
          "max_grid_per_day": 1,
          "step_pct": 0.02,
          "unit_pct": 0.1
        },
        "trend": {
          "add_n": 0.5,
          "amount_ratio_min": null,
          "max_units": 4,
          "require_macd_bullish": true,
          "risk_per_unit": 0.005,
          "stop_n": 2.0
        }
      },
      "policy_id": "full_adaptive",
      "strategy_id": "full_adaptive",
      "version": "1"
    }
  }
}

## 事件归因

[]
## Excess return diagnostics

Contributions sum daily net excess returns; execution_cost is a separate currency diagnostic already embedded in NAV.

Missing or invalid experiment evidence; no research action can be inferred.

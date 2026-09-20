# 风险调整后 ETF 样本外验证决策报告

## 决策

- 结论：`do_not_trade`
- 建议：不交易，直至补齐并复核缺失或无效证据。
- 阻断项：data_valid, missing_research_evidence, strategy_metrics, benchmark_metrics, strategy_exposure, benchmark_exposure, insufficient history for walk-forward validation, run_manifest, unexecuted_benchmark_evidence, experiment_metadata

## 策略与买入持有比较

证据缺失或无效，不能生成策略与买入持有比较。

## OOS 分布

无可用 OOS 窗口证据。

## 执行、换手与成本

执行证据缺失或无效。

## 数据边界、配置与训练曲面

{
  "data_cutoff": "2026-09-17",
  "config_hashes": [],
  "training_surface": [],
  "run_manifest": {
    "activation_eligible": false,
    "benchmark_specs": [
      {
        "benchmark_id": "buy_and_hold",
        "rebalance_sessions": null,
        "target_weight": 1.0,
        "version": "1"
      },
      {
        "benchmark_id": "fixed_half_hold",
        "rebalance_sessions": 1,
        "target_weight": 0.5,
        "version": "1"
      }
    ],
    "experiment": {
      "allowed_axes": {
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
        "unit_pct": [
          0.05,
          0.1,
          0.15,
          0.2
        ]
      },
      "as_of_date": "2026-09-17",
      "experiment_id": "round2-a500-20260917",
      "profile": {
        "benchmarks": [
          {
            "benchmark_id": "buy_and_hold",
            "rebalance_sessions": null,
            "target_weight": 1.0,
            "version": "1"
          },
          {
            "benchmark_id": "fixed_half_hold",
            "rebalance_sessions": 1,
            "target_weight": 0.5,
            "version": "1"
          }
        ],
        "profile_id": "grid_core",
        "required_evidence": [
          "execution",
          "integrated_oos",
          "provenance"
        ],
        "selection_families": [
          "grid_only"
        ],
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
          "policy_id": "grid_only",
          "strategy_id": "grid_only",
          "version": "1"
        },
        "version": "1"
      },
      "profile_hash": "53e04e2ebcde6b11cecadf28bd776455bbc733ecf2d4f5a2eececcacc0d3ff45",
      "start_date": "2021-01-01",
      "target_codes": [
        "563360.SH"
      ]
    },
    "experiment_hash": "33b351e6645256a1c4e828b323d2361fe6ccf172be31c66304f6b15a7b92d7c8",
    "experiment_windows": [],
    "research_only": true,
    "run_mode": "formal_validation",
    "shadow_run_eligible": null,
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
      "policy_id": "grid_only",
      "strategy_id": "grid_only",
      "version": "1"
    },
    "trading_authorized": false
  }
}

## 事件归因

[]
## Excess return diagnostics

Contributions sum daily net excess returns; execution_cost is a separate currency diagnostic already embedded in NAV.

Missing or invalid experiment evidence; no research action can be inferred.

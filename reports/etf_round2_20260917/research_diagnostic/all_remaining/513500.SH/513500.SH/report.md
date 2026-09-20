# 风险调整后 ETF 样本外验证决策报告

## 决策

- 结论：`diagnostic_complete`
- 建议：Diagnostic research only; no authorization.
- 阻断项：无

## 策略与买入持有比较

| 指标 | 策略 | 买入持有 | 差异（策略－买入持有） |
| --- | ---: | ---: | ---: |
| annual_return | 0.085335 | 0.179859 | -0.094524 |
| sharpe | 0.877440 | 0.922975 | -0.045535 |
| Sortino | 1.106242 | 1.162027 | -0.055785 |
| calmar | 0.645961 | 0.720775 | -0.074815 |
| cvar5 | -0.014519 | -0.028952 | 0.014433 |
| max_drawdown | -0.132105 | -0.249535 | 0.117430 |
| turnover | 3.011365 | 4.038392 | -1.027027 |
| total_cost | 1395.186980 | 199.793440 | 1195.393540 |

## OOS 分布

{
  "window_count": 5,
  "win_rate": 0.0,
  "median_excess_return": -0.036804335900000096,
  "best_excess_return": -0.01343283999999989,
  "worst_excess_return": -0.09195207569999986
}

## 执行、换手与成本

{
  "strategy": {
    "invested_sessions": 625,
    "cash_sessions": 5,
    "exposure_ratio": 0.9920634920634921,
    "turnover": 3.0113646443646256,
    "total_cost": 1395.18698,
    "cost_drag": 0.013951869799999999
  },
  "buy_and_hold": {
    "invested_sessions": 625,
    "cash_sessions": 5,
    "exposure_ratio": 0.9920634920634921,
    "turnover": 4.038391591905623,
    "total_cost": 199.79344,
    "cost_drag": 0.0019979344
  }
}

## 数据边界、配置与训练曲面

{
  "data_cutoff": "2026-09-17",
  "config_hashes": [
    "928ff9246144538cdea5af2f6efde5b0355c71d0abf4f11f954532e7de8195ce"
  ],
  "training_surface": [
    {
      "window_id": "wf_000",
      "grid": [],
      "trend": []
    },
    {
      "window_id": "wf_001",
      "grid": [],
      "trend": []
    },
    {
      "window_id": "wf_002",
      "grid": [],
      "trend": []
    },
    {
      "window_id": "wf_003",
      "grid": [],
      "trend": []
    },
    {
      "window_id": "wf_004",
      "grid": [],
      "trend": []
    }
  ],
  "run_manifest": {
    "schema_version": 1,
    "runner": "run_instrument_validation",
    "source_provider": "ValidationMarketDataProvider",
    "data_cutoff": "2026-09-17",
    "requested_start": "2021-01-04",
    "data_fingerprint": "4bc7731b63e1d7d244a6bc9df0da17ef1830efe11cb5c391643f9c709a42df8c",
    "run_mode": "research_diagnostic",
    "research_only": true,
    "activation_eligible": false,
    "shadow_run_eligible": false,
    "trading_authorized": false,
    "target": {
      "exposure_id": "sp_500",
      "stock_code": "513500.SH",
      "sub_layer": "broad_overseas_mature",
      "scope": "formal"
    },
    "selected_configs": [
      {
        "window_id": "wf_000",
        "config_hash": "928ff9246144538cdea5af2f6efde5b0355c71d0abf4f11f954532e7de8195ce",
        "config": null
      },
      {
        "window_id": "wf_001",
        "config_hash": "928ff9246144538cdea5af2f6efde5b0355c71d0abf4f11f954532e7de8195ce",
        "config": null
      },
      {
        "window_id": "wf_002",
        "config_hash": "928ff9246144538cdea5af2f6efde5b0355c71d0abf4f11f954532e7de8195ce",
        "config": null
      },
      {
        "window_id": "wf_003",
        "config_hash": "928ff9246144538cdea5af2f6efde5b0355c71d0abf4f11f954532e7de8195ce",
        "config": null
      },
      {
        "window_id": "wf_004",
        "config_hash": "928ff9246144538cdea5af2f6efde5b0355c71d0abf4f11f954532e7de8195ce",
        "config": null
      }
    ],
    "screened_axes": {
      "grid": [],
      "trend": []
    },
    "profile_id": "core_hold_rebalance",
    "profile_hash": "3d23b18c8a3614be7b56c821bcbd22b50743036b6473fa2520a5bd6e0acbeff9",
    "execution_windows": [
      {
        "window_id": "wf_000",
        "profile_id": "core_hold_rebalance",
        "execution_config": {
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
        },
        "reference_benchmark_id": "buy_and_hold",
        "strategy_spec": null,
        "benchmarks": [
          {
            "benchmark_id": "buy_and_hold",
            "version": "1",
            "rebalance_sessions": null,
            "target_weight": 1.0,
            "spec_hash": "3958c38c790b7737f3af03d4a690f2509833bfa7f847fbd3e06c6a8e5cafd0c3",
            "provenance_hash": "ad96060e0acdbd7d60fb870e3232884fa580658da2888cfebb9f99956bf8f0e6",
            "validation_start": "2024-02-19",
            "validation_end": "2024-08-20",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": 0.2809981236454435,
              "annual_volatility": 0.19202229368047935,
              "sharpe": 1.4633619787555392,
              "sortino": 1.6646078137393887,
              "calmar": 2.153027672523689,
              "worst_126_session_return": 0.13070019499999974,
              "cvar5": -0.03245323910536785,
              "win_rate": 0.576,
              "payoff_ratio": 0.9168035775278506,
              "profit_factor": 1.2694203381154852,
              "turnover": 0.9380008222763166,
              "minimum_commission_share": 0.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 2.99805,
              "max_drawdown": -0.1305130106925515,
              "recovery_sessions": 3,
              "total_cost": 39.9805
            }
          },
          {
            "benchmark_id": "fixed_half_hold",
            "version": "1",
            "rebalance_sessions": 1,
            "target_weight": 0.5,
            "spec_hash": "ac073b13dfd8fc5232bf30851ba89adea309c68abd84a01a15249842c1d2e597",
            "provenance_hash": "8b2bac349c450898c8323f53d9294ff1bca46a32b24858cf044f59f48f6c9c43",
            "validation_start": "2024-02-19",
            "validation_end": "2024-08-20",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": 0.13049725117398991,
              "annual_volatility": 0.09582800530770288,
              "sharpe": 1.3617861579708812,
              "sortino": 1.5578384747126552,
              "calmar": 1.9545236804829282,
              "worst_126_session_return": 0.06273104699999998,
              "cvar5": -0.016197406675612758,
              "win_rate": 0.576,
              "payoff_ratio": 0.9247498339937865,
              "profit_factor": 1.256263925425521,
              "turnover": 0.6753905377517477,
              "minimum_commission_share": 1.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 0.0652978125,
              "max_drawdown": -0.06676677928084573,
              "recovery_sessions": 3,
              "total_cost": 340.8953
            }
          }
        ]
      },
      {
        "window_id": "wf_001",
        "profile_id": "core_hold_rebalance",
        "execution_config": {
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
        },
        "reference_benchmark_id": "buy_and_hold",
        "strategy_spec": null,
        "benchmarks": [
          {
            "benchmark_id": "buy_and_hold",
            "version": "1",
            "rebalance_sessions": null,
            "target_weight": 1.0,
            "spec_hash": "3958c38c790b7737f3af03d4a690f2509833bfa7f847fbd3e06c6a8e5cafd0c3",
            "provenance_hash": "ad96060e0acdbd7d60fb870e3232884fa580658da2888cfebb9f99956bf8f0e6",
            "validation_start": "2024-08-21",
            "validation_end": "2025-03-04",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": 0.05386472069094195,
              "annual_volatility": 0.16951689205605283,
              "sharpe": 0.31775429597382493,
              "sortino": 0.47519167818254776,
              "calmar": 0.5043792248296594,
              "worst_126_session_return": 0.026365433000000715,
              "cvar5": -0.024534041074854684,
              "win_rate": 0.432,
              "payoff_ratio": 1.3475752736849105,
              "profit_factor": 1.0701333055733113,
              "turnover": 0.9458117017459999,
              "minimum_commission_share": 0.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 2.9996696696696694,
              "max_drawdown": -0.10679409071444868,
              "recovery_sessions": 5,
              "total_cost": 39.9567
            }
          },
          {
            "benchmark_id": "fixed_half_hold",
            "version": "1",
            "rebalance_sessions": 1,
            "target_weight": 0.5,
            "spec_hash": "ac073b13dfd8fc5232bf30851ba89adea309c68abd84a01a15249842c1d2e597",
            "provenance_hash": "8b2bac349c450898c8323f53d9294ff1bca46a32b24858cf044f59f48f6c9c43",
            "validation_start": "2024-08-21",
            "validation_end": "2025-03-04",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": 0.026243406681990322,
              "annual_volatility": 0.08475380637466319,
              "sharpe": 0.30964280903182756,
              "sortino": 0.4631845104941116,
              "calmar": 0.4793298208952229,
              "worst_126_session_return": 0.012932592999999715,
              "cvar5": -0.012300960632305976,
              "win_rate": 0.432,
              "payoff_ratio": 1.3565234238019284,
              "profit_factor": 1.0616270273232482,
              "turnover": 0.6470950320834982,
              "minimum_commission_share": 1.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 0.07121678571428572,
              "max_drawdown": -0.05475020651328699,
              "recovery_sessions": 5,
              "total_cost": 299.9407
            }
          }
        ]
      },
      {
        "window_id": "wf_002",
        "profile_id": "core_hold_rebalance",
        "execution_config": {
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
        },
        "reference_benchmark_id": "buy_and_hold",
        "strategy_spec": null,
        "benchmarks": [
          {
            "benchmark_id": "buy_and_hold",
            "version": "1",
            "rebalance_sessions": null,
            "target_weight": 1.0,
            "spec_hash": "3958c38c790b7737f3af03d4a690f2509833bfa7f847fbd3e06c6a8e5cafd0c3",
            "provenance_hash": "ad96060e0acdbd7d60fb870e3232884fa580658da2888cfebb9f99956bf8f0e6",
            "validation_start": "2025-03-05",
            "validation_end": "2025-09-03",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": 0.14923499851567468,
              "annual_volatility": 0.2547421836917758,
              "sharpe": 0.5858275859652711,
              "sortino": 0.6918300894192071,
              "calmar": 0.9338406592255618,
              "worst_126_session_return": 0.07143222440000141,
              "cvar5": -0.03808820585561198,
              "win_rate": 0.464,
              "payoff_ratio": 1.2492559263952399,
              "profit_factor": 1.1686587698536115,
              "turnover": 0.9974507955126857,
              "minimum_commission_share": 0.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 2.997756,
              "max_drawdown": -0.15980777560000003,
              "recovery_sessions": 57,
              "total_cost": 39.97756
            }
          },
          {
            "benchmark_id": "fixed_half_hold",
            "version": "1",
            "rebalance_sessions": 1,
            "target_weight": 0.5,
            "spec_hash": "ac073b13dfd8fc5232bf30851ba89adea309c68abd84a01a15249842c1d2e597",
            "provenance_hash": "8b2bac349c450898c8323f53d9294ff1bca46a32b24858cf044f59f48f6c9c43",
            "validation_start": "2025-03-05",
            "validation_end": "2025-09-03",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": 0.07103807042533106,
              "annual_volatility": 0.12678806978051835,
              "sharpe": 0.5602898644036809,
              "sortino": 0.66241663338898,
              "calmar": 0.8680609189456596,
              "worst_126_session_return": 0.03462788849999998,
              "cvar5": -0.019228561992182314,
              "win_rate": 0.464,
              "payoff_ratio": 1.2481615393880925,
              "profit_factor": 1.149101099754117,
              "turnover": 0.6733747508516514,
              "minimum_commission_share": 1.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 0.08249448979591836,
              "max_drawdown": -0.08183535149999999,
              "recovery_sessions": 57,
              "total_cost": 265.21115
            }
          }
        ]
      },
      {
        "window_id": "wf_003",
        "profile_id": "core_hold_rebalance",
        "execution_config": {
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
        },
        "reference_benchmark_id": "buy_and_hold",
        "strategy_spec": null,
        "benchmarks": [
          {
            "benchmark_id": "buy_and_hold",
            "version": "1",
            "rebalance_sessions": null,
            "target_weight": 1.0,
            "spec_hash": "3958c38c790b7737f3af03d4a690f2509833bfa7f847fbd3e06c6a8e5cafd0c3",
            "provenance_hash": "ad96060e0acdbd7d60fb870e3232884fa580658da2888cfebb9f99956bf8f0e6",
            "validation_start": "2025-09-04",
            "validation_end": "2026-03-18",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": 0.0677443692458346,
              "annual_volatility": 0.155942229659213,
              "sharpe": 0.4344196526744498,
              "sortino": 0.5948688292120271,
              "calmar": 0.8069376580821375,
              "worst_126_session_return": 0.03304842400000019,
              "cvar5": -0.024082069252291727,
              "win_rate": 0.536,
              "payoff_ratio": 0.9119423103827866,
              "profit_factor": 1.0910738356365484,
              "turnover": 0.9291488107175612,
              "minimum_commission_share": 0.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 2.9997597597597596,
              "max_drawdown": -0.08395242007523085,
              "recovery_sessions": 6,
              "total_cost": 39.9576
            }
          },
          {
            "benchmark_id": "fixed_half_hold",
            "version": "1",
            "rebalance_sessions": 1,
            "target_weight": 0.5,
            "spec_hash": "ac073b13dfd8fc5232bf30851ba89adea309c68abd84a01a15249842c1d2e597",
            "provenance_hash": "8b2bac349c450898c8323f53d9294ff1bca46a32b24858cf044f59f48f6c9c43",
            "validation_start": "2025-09-04",
            "validation_end": "2026-03-18",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": 0.03193005565397811,
              "annual_volatility": 0.07793259708361198,
              "sharpe": 0.4097137378819947,
              "sortino": 0.559496675997702,
              "calmar": 0.7327344006601165,
              "worst_126_session_return": 0.015712888199999497,
              "cvar5": -0.012072342813940614,
              "win_rate": 0.536,
              "payoff_ratio": 0.9030481343176952,
              "profit_factor": 1.0804325892729567,
              "turnover": 0.6018093336597307,
              "minimum_commission_share": 0.975,
              "unfilled_share": 0.025,
              "slippage_degradation": 0.09595476923076922,
              "max_drawdown": -0.0435765751208248,
              "recovery_sessions": 6,
              "total_cost": 213.71118
            }
          }
        ]
      },
      {
        "window_id": "wf_004",
        "profile_id": "core_hold_rebalance",
        "execution_config": {
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
        },
        "reference_benchmark_id": "buy_and_hold",
        "strategy_spec": null,
        "benchmarks": [
          {
            "benchmark_id": "buy_and_hold",
            "version": "1",
            "rebalance_sessions": null,
            "target_weight": 1.0,
            "spec_hash": "3958c38c790b7737f3af03d4a690f2509833bfa7f847fbd3e06c6a8e5cafd0c3",
            "provenance_hash": "ad96060e0acdbd7d60fb870e3232884fa580658da2888cfebb9f99956bf8f0e6",
            "validation_start": "2026-03-19",
            "validation_end": "2026-09-17",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": 0.38752079053059063,
              "annual_volatility": 0.18981344931959251,
              "sharpe": 2.0415876320655997,
              "sortino": 2.891143930731528,
              "calmar": 6.929346901236119,
              "worst_126_session_return": 0.17640078920000013,
              "cvar5": -0.02719923605297081,
              "win_rate": 0.544,
              "payoff_ratio": 1.0743745260581834,
              "profit_factor": 1.378442788150122,
              "turnover": 0.8997833498433292,
              "minimum_commission_share": 0.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 3.0001082164328654,
              "max_drawdown": -0.055924576450554264,
              "recovery_sessions": 13,
              "total_cost": 39.92108
            }
          },
          {
            "benchmark_id": "fixed_half_hold",
            "version": "1",
            "rebalance_sessions": 1,
            "target_weight": 0.5,
            "spec_hash": "ac073b13dfd8fc5232bf30851ba89adea309c68abd84a01a15249842c1d2e597",
            "provenance_hash": "8b2bac349c450898c8323f53d9294ff1bca46a32b24858cf044f59f48f6c9c43",
            "validation_start": "2026-03-19",
            "validation_end": "2026-09-17",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": 0.17755548589287162,
              "annual_volatility": 0.0949822102257347,
              "sharpe": 1.869355171572585,
              "sortino": 2.648489294452116,
              "calmar": 6.23769940654819,
              "worst_126_session_return": 0.08444871350000183,
              "cvar5": -0.013616704826708848,
              "win_rate": 0.544,
              "payoff_ratio": 1.0844362271461583,
              "profit_factor": 1.3655863601099771,
              "turnover": 0.6469240571168747,
              "minimum_commission_share": 1.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 0.08011235294117648,
              "max_drawdown": -0.02846489936762231,
              "recovery_sessions": 13,
              "total_cost": 275.42865
            }
          }
        ]
      }
    ],
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
      "allowed_axes": {},
      "as_of_date": "2026-09-17",
      "experiment_id": "round2-sp500-20260917",
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
        "profile_id": "core_hold_rebalance",
        "required_evidence": [
          "execution",
          "integrated_oos",
          "provenance"
        ],
        "selection_families": [],
        "strategy": null,
        "version": "1"
      },
      "profile_hash": "3d23b18c8a3614be7b56c821bcbd22b50743036b6473fa2520a5bd6e0acbeff9",
      "start_date": "2021-01-01",
      "target_codes": [
        "513500.SH"
      ]
    },
    "experiment_hash": "6c2ac2648f72af0af938608ca5ba2aca2c9857fef999b33b3c8d1ad15079687d",
    "experiment_windows": [
      {
        "benchmark_specs": [
          {
            "benchmark_id": "buy_and_hold",
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
            "provenance_hash": "ad96060e0acdbd7d60fb870e3232884fa580658da2888cfebb9f99956bf8f0e6",
            "rebalance_sessions": null,
            "spec_hash": "3958c38c790b7737f3af03d4a690f2509833bfa7f847fbd3e06c6a8e5cafd0c3",
            "target_weight": 1.0,
            "version": "1"
          },
          {
            "benchmark_id": "fixed_half_hold",
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
            "provenance_hash": "8b2bac349c450898c8323f53d9294ff1bca46a32b24858cf044f59f48f6c9c43",
            "rebalance_sessions": 1,
            "spec_hash": "ac073b13dfd8fc5232bf30851ba89adea309c68abd84a01a15249842c1d2e597",
            "target_weight": 0.5,
            "version": "1"
          }
        ],
        "candidate_scores": [],
        "excess_attribution": null,
        "execution_cost_config": {
          "commission_rate": 0.0001,
          "minimum_commission": 5.0,
          "sell_tax_rate": 0.0,
          "slippage_bps": 3.0,
          "transfer_fee_rate": 0.0
        },
        "screened_axes": {},
        "selected_scores": {},
        "strategy_spec": null,
        "window_id": "wf_000"
      },
      {
        "benchmark_specs": [
          {
            "benchmark_id": "buy_and_hold",
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
            "provenance_hash": "ad96060e0acdbd7d60fb870e3232884fa580658da2888cfebb9f99956bf8f0e6",
            "rebalance_sessions": null,
            "spec_hash": "3958c38c790b7737f3af03d4a690f2509833bfa7f847fbd3e06c6a8e5cafd0c3",
            "target_weight": 1.0,
            "version": "1"
          },
          {
            "benchmark_id": "fixed_half_hold",
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
            "provenance_hash": "8b2bac349c450898c8323f53d9294ff1bca46a32b24858cf044f59f48f6c9c43",
            "rebalance_sessions": 1,
            "spec_hash": "ac073b13dfd8fc5232bf30851ba89adea309c68abd84a01a15249842c1d2e597",
            "target_weight": 0.5,
            "version": "1"
          }
        ],
        "candidate_scores": [],
        "excess_attribution": null,
        "execution_cost_config": {
          "commission_rate": 0.0001,
          "minimum_commission": 5.0,
          "sell_tax_rate": 0.0,
          "slippage_bps": 3.0,
          "transfer_fee_rate": 0.0
        },
        "screened_axes": {},
        "selected_scores": {},
        "strategy_spec": null,
        "window_id": "wf_001"
      },
      {
        "benchmark_specs": [
          {
            "benchmark_id": "buy_and_hold",
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
            "provenance_hash": "ad96060e0acdbd7d60fb870e3232884fa580658da2888cfebb9f99956bf8f0e6",
            "rebalance_sessions": null,
            "spec_hash": "3958c38c790b7737f3af03d4a690f2509833bfa7f847fbd3e06c6a8e5cafd0c3",
            "target_weight": 1.0,
            "version": "1"
          },
          {
            "benchmark_id": "fixed_half_hold",
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
            "provenance_hash": "8b2bac349c450898c8323f53d9294ff1bca46a32b24858cf044f59f48f6c9c43",
            "rebalance_sessions": 1,
            "spec_hash": "ac073b13dfd8fc5232bf30851ba89adea309c68abd84a01a15249842c1d2e597",
            "target_weight": 0.5,
            "version": "1"
          }
        ],
        "candidate_scores": [],
        "excess_attribution": null,
        "execution_cost_config": {
          "commission_rate": 0.0001,
          "minimum_commission": 5.0,
          "sell_tax_rate": 0.0,
          "slippage_bps": 3.0,
          "transfer_fee_rate": 0.0
        },
        "screened_axes": {},
        "selected_scores": {},
        "strategy_spec": null,
        "window_id": "wf_002"
      },
      {
        "benchmark_specs": [
          {
            "benchmark_id": "buy_and_hold",
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
            "provenance_hash": "ad96060e0acdbd7d60fb870e3232884fa580658da2888cfebb9f99956bf8f0e6",
            "rebalance_sessions": null,
            "spec_hash": "3958c38c790b7737f3af03d4a690f2509833bfa7f847fbd3e06c6a8e5cafd0c3",
            "target_weight": 1.0,
            "version": "1"
          },
          {
            "benchmark_id": "fixed_half_hold",
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
            "provenance_hash": "8b2bac349c450898c8323f53d9294ff1bca46a32b24858cf044f59f48f6c9c43",
            "rebalance_sessions": 1,
            "spec_hash": "ac073b13dfd8fc5232bf30851ba89adea309c68abd84a01a15249842c1d2e597",
            "target_weight": 0.5,
            "version": "1"
          }
        ],
        "candidate_scores": [],
        "excess_attribution": null,
        "execution_cost_config": {
          "commission_rate": 0.0001,
          "minimum_commission": 5.0,
          "sell_tax_rate": 0.0,
          "slippage_bps": 3.0,
          "transfer_fee_rate": 0.0
        },
        "screened_axes": {},
        "selected_scores": {},
        "strategy_spec": null,
        "window_id": "wf_003"
      },
      {
        "benchmark_specs": [
          {
            "benchmark_id": "buy_and_hold",
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
            "provenance_hash": "ad96060e0acdbd7d60fb870e3232884fa580658da2888cfebb9f99956bf8f0e6",
            "rebalance_sessions": null,
            "spec_hash": "3958c38c790b7737f3af03d4a690f2509833bfa7f847fbd3e06c6a8e5cafd0c3",
            "target_weight": 1.0,
            "version": "1"
          },
          {
            "benchmark_id": "fixed_half_hold",
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
            "provenance_hash": "8b2bac349c450898c8323f53d9294ff1bca46a32b24858cf044f59f48f6c9c43",
            "rebalance_sessions": 1,
            "spec_hash": "ac073b13dfd8fc5232bf30851ba89adea309c68abd84a01a15249842c1d2e597",
            "target_weight": 0.5,
            "version": "1"
          }
        ],
        "candidate_scores": [],
        "excess_attribution": null,
        "execution_cost_config": {
          "commission_rate": 0.0001,
          "minimum_commission": 5.0,
          "sell_tax_rate": 0.0,
          "slippage_bps": 3.0,
          "transfer_fee_rate": 0.0
        },
        "screened_axes": {},
        "selected_scores": {},
        "strategy_spec": null,
        "window_id": "wf_004"
      }
    ],
    "strategy_spec": null
  }
}

## 事件归因

[
  {
    "window_id": "wf_000",
    "trade_points": [
      {
        "event_date": "2024-02-20",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 28700,
        "raw_price": 1.7385214
      },
      {
        "event_date": "2024-02-21",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.720516
      },
      {
        "event_date": "2024-02-22",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.7295187
      },
      {
        "event_date": "2024-02-23",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.7614714
      },
      {
        "event_date": "2024-02-26",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.7634708000000001
      },
      {
        "event_date": "2024-02-29",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.7764669
      },
      {
        "event_date": "2024-03-11",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.789463
      },
      {
        "event_date": "2024-03-18",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.7735318999999998
      },
      {
        "event_date": "2024-03-22",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 300,
        "raw_price": 1.8264519000000001
      },
      {
        "event_date": "2024-03-25",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.8374486
      },
      {
        "event_date": "2024-03-29",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.8674396000000002
      },
      {
        "event_date": "2024-04-03",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.830549
      },
      {
        "event_date": "2024-04-08",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 300,
        "raw_price": 1.8075420999999998
      },
      {
        "event_date": "2024-04-12",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.8015402999999999
      },
      {
        "event_date": "2024-04-17",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 400,
        "raw_price": 1.7425226
      },
      {
        "event_date": "2024-04-19",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.710513
      },
      {
        "event_date": "2024-04-22",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.7025105999999999
      },
      {
        "event_date": "2024-04-25",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 300,
        "raw_price": 1.7484753000000002
      },
      {
        "event_date": "2024-04-26",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.7545262
      },
      {
        "event_date": "2024-05-06",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.7574726
      },
      {
        "event_date": "2024-05-08",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.7784663
      },
      {
        "event_date": "2024-05-09",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.7854642
      },
      {
        "event_date": "2024-05-13",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.8004597
      },
      {
        "event_date": "2024-05-14",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.8004597
      },
      {
        "event_date": "2024-05-16",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.8484453
      },
      {
        "event_date": "2024-05-17",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.8434468000000002
      },
      {
        "event_date": "2024-05-27",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 1.8295487
      },
      {
        "event_date": "2024-05-28",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.8354492000000002
      },
      {
        "event_date": "2024-05-31",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.7935378999999998
      },
      {
        "event_date": "2024-06-04",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.8344495
      },
      {
        "event_date": "2024-06-06",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.8734378000000003
      },
      {
        "event_date": "2024-06-07",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.869439
      },
      {
        "event_date": "2024-06-12",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.8954312
      },
      {
        "event_date": "2024-06-14",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.9064279000000002
      },
      {
        "event_date": "2024-06-21",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.9064279000000002
      },
      {
        "event_date": "2024-06-27",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.9324201
      },
      {
        "event_date": "2024-06-28",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.9544135
      },
      {
        "event_date": "2024-07-01",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.9644105
      },
      {
        "event_date": "2024-07-04",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 2.0173946
      },
      {
        "event_date": "2024-07-05",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.9745922
      },
      {
        "event_date": "2024-07-09",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.0003997
      },
      {
        "event_date": "2024-07-15",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.9835949
      },
      {
        "event_date": "2024-07-16",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 2.0283913
      },
      {
        "event_date": "2024-07-17",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.0383883000000003
      },
      {
        "event_date": "2024-07-18",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.0013994
      },
      {
        "event_date": "2024-07-19",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 2.0106029999999997
      },
      {
        "event_date": "2024-07-22",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 300,
        "raw_price": 1.9555865000000001
      },
      {
        "event_date": "2024-07-23",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.9795937000000001
      },
      {
        "event_date": "2024-07-24",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.9744075
      },
      {
        "event_date": "2024-07-26",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 500,
        "raw_price": 1.9015703
      },
      {
        "event_date": "2024-07-29",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.9474156
      },
      {
        "event_date": "2024-07-30",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 300,
        "raw_price": 1.9624111000000002
      },
      {
        "event_date": "2024-08-01",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.9795937000000001
      },
      {
        "event_date": "2024-08-02",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.9274216
      },
      {
        "event_date": "2024-08-05",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 300,
        "raw_price": 1.840552
      },
      {
        "event_date": "2024-08-06",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 1000,
        "raw_price": 1.8135439
      },
      {
        "event_date": "2024-08-08",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.7924621
      },
      {
        "event_date": "2024-08-12",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.8414474
      },
      {
        "event_date": "2024-08-13",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.8614414000000001
      },
      {
        "event_date": "2024-08-14",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.9134258
      },
      {
        "event_date": "2024-08-15",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.9354192000000001
      },
      {
        "event_date": "2024-08-16",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.9934018
      },
      {
        "event_date": "2024-08-19",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.9774066000000001
      },
      {
        "event_date": "2024-08-20",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.9685903999999999
      }
    ],
    "by_reason": {
      "grid_initialize": {
        "reason": "grid_initialize",
        "fill_count": 1,
        "shares": 28700,
        "traded_value": "49895.5641800"
      },
      "grid_buy": {
        "reason": "grid_buy",
        "fill_count": 22,
        "shares": 4500,
        "traded_value": "8279.6831599999998900"
      },
      "grid_sell": {
        "reason": "grid_sell",
        "fill_count": 41,
        "shares": 6100,
        "traded_value": "11489.7520400000004300"
      }
    },
    "invested_sessions": 125,
    "cash_sessions": 1,
    "rejected_order_count": 0
  },
  {
    "window_id": "wf_001",
    "trade_points": [
      {
        "event_date": "2024-08-22",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 25200,
        "raw_price": 1.9785933999999998
      },
      {
        "event_date": "2024-08-23",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.9505849999999998
      },
      {
        "event_date": "2024-08-29",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.9704087000000001
      },
      {
        "event_date": "2024-09-05",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 400,
        "raw_price": 1.9335799
      },
      {
        "event_date": "2024-09-10",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.9205759999999998
      },
      {
        "event_date": "2024-09-11",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.9085724
      },
      {
        "event_date": "2024-09-13",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.9434168
      },
      {
        "event_date": "2024-09-20",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.9854042
      },
      {
        "event_date": "2024-09-24",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.9764069000000002
      },
      {
        "event_date": "2024-09-26",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.9495847
      },
      {
        "event_date": "2024-09-30",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 1.8935678999999999
      },
      {
        "event_date": "2024-10-08",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.8865657999999998
      },
      {
        "event_date": "2024-10-09",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.9145742
      },
      {
        "event_date": "2024-10-10",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.9424171000000001
      },
      {
        "event_date": "2024-10-11",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.9544135
      },
      {
        "event_date": "2024-10-14",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.9834048
      },
      {
        "event_date": "2024-10-15",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.0043984999999997
      },
      {
        "event_date": "2024-10-16",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 400,
        "raw_price": 2.0243925
      },
      {
        "event_date": "2024-10-22",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 2.0156045000000002
      },
      {
        "event_date": "2024-10-24",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.9865958
      },
      {
        "event_date": "2024-11-04",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 1.9665898
      },
      {
        "event_date": "2024-11-07",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 300,
        "raw_price": 2.0643805
      },
      {
        "event_date": "2024-11-08",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.0463859
      },
      {
        "event_date": "2024-11-11",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.0643805
      },
      {
        "event_date": "2024-11-12",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 2.0913724
      },
      {
        "event_date": "2024-11-13",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.1083673000000003
      },
      {
        "event_date": "2024-11-15",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.1033688
      },
      {
        "event_date": "2024-11-18",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 2.0676201
      },
      {
        "event_date": "2024-11-25",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.1403577
      },
      {
        "event_date": "2024-11-26",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 300,
        "raw_price": 2.1803457
      },
      {
        "event_date": "2024-12-03",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.209337
      },
      {
        "event_date": "2024-12-04",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.2193340000000004
      },
      {
        "event_date": "2024-12-06",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.2273316000000003
      },
      {
        "event_date": "2024-12-11",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 2.20066
      },
      {
        "event_date": "2024-12-13",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.2253322
      },
      {
        "event_date": "2024-12-17",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 2.5002497
      },
      {
        "event_date": "2024-12-19",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 2.1496447
      },
      {
        "event_date": "2024-12-20",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 400,
        "raw_price": 2.1556464999999996
      },
      {
        "event_date": "2024-12-24",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.2123361000000004
      },
      {
        "event_date": "2024-12-26",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.1983403
      },
      {
        "event_date": "2024-12-31",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 2.1516452999999998
      },
      {
        "event_date": "2025-01-07",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.2193340000000004
      },
      {
        "event_date": "2025-01-13",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 2.1526456
      },
      {
        "event_date": "2025-01-14",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 2.1526456
      },
      {
        "event_date": "2025-01-15",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.1603517
      },
      {
        "event_date": "2025-01-17",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.1883433
      },
      {
        "event_date": "2025-01-21",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.2013394
      },
      {
        "event_date": "2025-01-23",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.2243325
      },
      {
        "event_date": "2025-02-06",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 2.20066
      },
      {
        "event_date": "2025-02-13",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 2.1796537
      },
      {
        "event_date": "2025-02-24",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 2.1186353999999996
      },
      {
        "event_date": "2025-02-25",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 2.110633
      },
      {
        "event_date": "2025-02-26",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 2.0926276
      },
      {
        "event_date": "2025-02-28",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 2.0506149999999996
      },
      {
        "event_date": "2025-03-03",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 300,
        "raw_price": 2.0526155999999998
      },
      {
        "event_date": "2025-03-04",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.0333897999999997
      }
    ],
    "by_reason": {
      "grid_initialize": {
        "reason": "grid_initialize",
        "fill_count": 1,
        "shares": 25200,
        "traded_value": "49860.5536799999949600"
      },
      "grid_buy": {
        "reason": "grid_buy",
        "fill_count": 25,
        "shares": 3800,
        "traded_value": "7779.0330099999996200"
      },
      "grid_sell": {
        "reason": "grid_sell",
        "fill_count": 30,
        "shares": 4200,
        "traded_value": "8844.0459900000001600"
      }
    },
    "invested_sessions": 125,
    "cash_sessions": 1,
    "rejected_order_count": 0
  },
  {
    "window_id": "wf_002",
    "trade_points": [
      {
        "event_date": "2025-03-06",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 24600,
        "raw_price": 2.0316093
      },
      {
        "event_date": "2025-03-10",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.9985994
      },
      {
        "event_date": "2025-03-11",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.9375811
      },
      {
        "event_date": "2025-03-12",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 300,
        "raw_price": 1.9385814
      },
      {
        "event_date": "2025-03-14",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.9205759999999998
      },
      {
        "event_date": "2025-03-21",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.9784063
      },
      {
        "event_date": "2025-03-25",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.0243925
      },
      {
        "event_date": "2025-03-26",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.0273916
      },
      {
        "event_date": "2025-03-28",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.9745922
      },
      {
        "event_date": "2025-03-31",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.9105729999999999
      },
      {
        "event_date": "2025-04-01",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 400,
        "raw_price": 1.9175750999999999
      },
      {
        "event_date": "2025-04-02",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.939418
      },
      {
        "event_date": "2025-04-07",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.7075121
      },
      {
        "event_date": "2025-04-08",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 1400,
        "raw_price": 1.7375211000000002
      },
      {
        "event_date": "2025-04-09",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 400,
        "raw_price": 1.7064879000000002
      },
      {
        "event_date": "2025-04-10",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 300,
        "raw_price": 1.8815643
      },
      {
        "event_date": "2025-04-11",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 1100,
        "raw_price": 1.8064579
      },
      {
        "event_date": "2025-04-14",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 1.8645592
      },
      {
        "event_date": "2025-04-15",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.8674396000000002
      },
      {
        "event_date": "2025-04-17",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.8315492999999998
      },
      {
        "event_date": "2025-04-18",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.8265478
      },
      {
        "event_date": "2025-04-22",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 1.7925376
      },
      {
        "event_date": "2025-04-24",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 300,
        "raw_price": 1.8544435000000001
      },
      {
        "event_date": "2025-04-28",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 300,
        "raw_price": 1.8914324
      },
      {
        "event_date": "2025-05-07",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.919424
      },
      {
        "event_date": "2025-05-09",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.939418
      },
      {
        "event_date": "2025-05-13",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.9864039000000002
      },
      {
        "event_date": "2025-05-14",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.9974006
      },
      {
        "event_date": "2025-05-15",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 2.0063979
      },
      {
        "event_date": "2025-05-21",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.0183943
      },
      {
        "event_date": "2025-05-23",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.9875961
      },
      {
        "event_date": "2025-05-30",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.0003997
      },
      {
        "event_date": "2025-06-10",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.0413874
      },
      {
        "event_date": "2025-06-25",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.0613813999999997
      },
      {
        "event_date": "2025-06-27",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.0793760000000003
      },
      {
        "event_date": "2025-06-30",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.1013694
      },
      {
        "event_date": "2025-07-01",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.1013694
      },
      {
        "event_date": "2025-07-07",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.1203637
      },
      {
        "event_date": "2025-07-21",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.1413574
      },
      {
        "event_date": "2025-07-28",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.1753472
      },
      {
        "event_date": "2025-07-29",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.1823451
      },
      {
        "event_date": "2025-08-01",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.169349
      },
      {
        "event_date": "2025-08-05",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 2.1716512999999997
      },
      {
        "event_date": "2025-08-06",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.1663498999999997
      },
      {
        "event_date": "2025-08-12",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.1873436
      },
      {
        "event_date": "2025-08-18",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.2083373
      },
      {
        "event_date": "2025-08-21",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 2.1776531
      },
      {
        "event_date": "2025-08-25",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 2.1976591
      },
      {
        "event_date": "2025-08-26",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.189343
      }
    ],
    "by_reason": {
      "grid_initialize": {
        "reason": "grid_initialize",
        "fill_count": 1,
        "shares": 24600,
        "traded_value": "49977.5887800"
      },
      "grid_buy": {
        "reason": "grid_buy",
        "fill_count": 18,
        "shares": 4100,
        "traded_value": "7658.3968300000001300"
      },
      "grid_sell": {
        "reason": "grid_sell",
        "fill_count": 30,
        "shares": 5000,
        "traded_value": "9748.8744600000001200"
      }
    },
    "invested_sessions": 125,
    "cash_sessions": 1,
    "rejected_order_count": 0
  },
  {
    "window_id": "wf_003",
    "trade_points": [
      {
        "event_date": "2025-09-05",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 22600,
        "raw_price": 2.210663
      },
      {
        "event_date": "2025-09-17",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.2343295
      },
      {
        "event_date": "2025-09-23",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.2823151
      },
      {
        "event_date": "2025-09-24",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.2743175
      },
      {
        "event_date": "2025-10-10",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 2.3203037
      },
      {
        "event_date": "2025-10-14",
        "kind": "rejected_order",
        "reason": "insufficient lot size",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-10-15",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 2.2786834
      },
      {
        "event_date": "2025-10-21",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 2.3412974
      },
      {
        "event_date": "2025-10-23",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.3472956
      },
      {
        "event_date": "2025-10-27",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.3822851000000003
      },
      {
        "event_date": "2025-10-28",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 2.4322700999999998
      },
      {
        "event_date": "2025-10-30",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 2.4682593
      },
      {
        "event_date": "2025-10-31",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.469259
      },
      {
        "event_date": "2025-11-05",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 2.3767128
      },
      {
        "event_date": "2025-11-06",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 2.4007199999999997
      },
      {
        "event_date": "2025-11-11",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.4502647
      },
      {
        "event_date": "2025-11-13",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.4672596
      },
      {
        "event_date": "2025-11-14",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.4462659
      },
      {
        "event_date": "2025-11-19",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 300,
        "raw_price": 2.3887164
      },
      {
        "event_date": "2025-11-20",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 2.3997197
      },
      {
        "event_date": "2025-11-21",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.3652902
      },
      {
        "event_date": "2025-11-24",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 2.3827146
      },
      {
        "event_date": "2025-11-25",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.4342695
      },
      {
        "event_date": "2025-11-26",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.4232728
      },
      {
        "event_date": "2025-11-27",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 2.459262
      },
      {
        "event_date": "2025-12-04",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.4732578000000003
      },
      {
        "event_date": "2025-12-09",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 2.4407319999999997
      },
      {
        "event_date": "2025-12-10",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 2.4207259999999997
      },
      {
        "event_date": "2025-12-15",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.4362689
      },
      {
        "event_date": "2025-12-17",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 2.4217262999999996
      },
      {
        "event_date": "2025-12-22",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.469259
      },
      {
        "event_date": "2026-01-06",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.469259
      },
      {
        "event_date": "2026-01-20",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 2.4407319999999997
      },
      {
        "event_date": "2026-01-27",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 2.4227266000000003
      },
      {
        "event_date": "2026-02-03",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 2.3997197
      },
      {
        "event_date": "2026-02-09",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 2.3717113
      },
      {
        "event_date": "2026-02-10",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 2.3832847999999998
      },
      {
        "event_date": "2026-03-05",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 2.350705
      },
      {
        "event_date": "2026-03-10",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 2.320696
      },
      {
        "event_date": "2026-03-16",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 2.2846851999999997
      }
    ],
    "by_reason": {
      "grid_initialize": {
        "reason": "grid_initialize",
        "fill_count": 1,
        "shares": 22600,
        "traded_value": "49960.983800"
      },
      "grid_sell": {
        "reason": "grid_sell",
        "fill_count": 22,
        "shares": 2800,
        "traded_value": "6723.3823799999999800"
      },
      "grid_buy": {
        "reason": "grid_buy",
        "fill_count": 16,
        "shares": 2400,
        "traded_value": "5700.9097599999998400"
      }
    },
    "invested_sessions": 125,
    "cash_sessions": 1,
    "rejected_order_count": 1
  },
  {
    "window_id": "wf_004",
    "trade_points": [
      {
        "event_date": "2026-03-20",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 22100,
        "raw_price": 2.2586774
      },
      {
        "event_date": "2026-03-23",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 2.2256675
      },
      {
        "event_date": "2026-03-24",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 400,
        "raw_price": 2.1716512999999997
      },
      {
        "event_date": "2026-03-25",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.1983403
      },
      {
        "event_date": "2026-03-26",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.2213334000000002
      },
      {
        "event_date": "2026-03-31",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 2.1686504
      },
      {
        "event_date": "2026-04-01",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 2.2176651
      },
      {
        "event_date": "2026-04-02",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 300,
        "raw_price": 2.2403277000000004
      },
      {
        "event_date": "2026-04-09",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 300,
        "raw_price": 2.2633208
      },
      {
        "event_date": "2026-04-15",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.3332998000000003
      },
      {
        "event_date": "2026-04-16",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.3612914000000003
      },
      {
        "event_date": "2026-04-17",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.3642905
      },
      {
        "event_date": "2026-04-23",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.3772866
      },
      {
        "event_date": "2026-04-29",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.39928
      },
      {
        "event_date": "2026-05-06",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.4542635
      },
      {
        "event_date": "2026-05-07",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.4682593
      },
      {
        "event_date": "2026-05-08",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.4782563
      },
      {
        "event_date": "2026-05-12",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.4902527
      },
      {
        "event_date": "2026-05-19",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 2.4417323
      },
      {
        "event_date": "2026-05-21",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 2.4547362
      },
      {
        "event_date": "2026-05-25",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.5302407000000002
      },
      {
        "event_date": "2026-05-26",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 300,
        "raw_price": 2.5452361999999997
      },
      {
        "event_date": "2026-06-02",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 300,
        "raw_price": 2.6352092000000003
      },
      {
        "event_date": "2026-06-05",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 2.5697707
      },
      {
        "event_date": "2026-06-09",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 2.5227565999999997
      },
      {
        "event_date": "2026-06-12",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 2.5507649999999997
      },
      {
        "event_date": "2026-06-16",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 2.5802257
      },
      {
        "event_date": "2026-06-17",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.5802257
      },
      {
        "event_date": "2026-06-24",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 300,
        "raw_price": 2.5017503
      },
      {
        "event_date": "2026-06-29",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 2.4927476
      },
      {
        "event_date": "2026-07-07",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.519244
      },
      {
        "event_date": "2026-07-15",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.5422371000000004
      },
      {
        "event_date": "2026-07-16",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.5632308
      },
      {
        "event_date": "2026-07-20",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 2.5037509
      },
      {
        "event_date": "2026-07-29",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 2.4957485
      },
      {
        "event_date": "2026-07-30",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.489253
      },
      {
        "event_date": "2026-07-31",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 2.5227565999999997
      },
      {
        "event_date": "2026-08-03",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.5212434
      },
      {
        "event_date": "2026-08-04",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.5622311000000004
      },
      {
        "event_date": "2026-08-05",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 2.6312104
      },
      {
        "event_date": "2026-08-06",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 300,
        "raw_price": 2.6572026
      },
      {
        "event_date": "2026-08-07",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.6811954
      },
      {
        "event_date": "2026-08-12",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.7041885000000003
      },
      {
        "event_date": "2026-08-17",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 2.7771666
      },
      {
        "event_date": "2026-08-19",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 2.6547962
      },
      {
        "event_date": "2026-08-20",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 2.6657995
      },
      {
        "event_date": "2026-08-26",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.6941915
      },
      {
        "event_date": "2026-08-31",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.7021891
      },
      {
        "event_date": "2026-09-03",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 2.6547962
      },
      {
        "event_date": "2026-09-07",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.6921921
      },
      {
        "event_date": "2026-09-15",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 2.6587973999999996
      }
    ],
    "by_reason": {
      "grid_initialize": {
        "reason": "grid_initialize",
        "fill_count": 1,
        "shares": 22100,
        "traded_value": "49916.7705400"
      },
      "grid_buy": {
        "reason": "grid_buy",
        "fill_count": 18,
        "shares": 2800,
        "traded_value": "6899.4692199999997200"
      },
      "grid_sell": {
        "reason": "grid_sell",
        "fill_count": 32,
        "shares": 4500,
        "traded_value": "11292.9111100000003300"
      }
    },
    "invested_sessions": 125,
    "cash_sessions": 1,
    "rejected_order_count": 0
  }
]
## Excess return diagnostics

Contributions sum daily net excess returns; execution_cost is a separate currency diagnostic already embedded in NAV.

Missing or invalid experiment evidence; no research action can be inferred.

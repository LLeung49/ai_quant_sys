# 风险调整后 ETF 样本外验证决策报告

## 决策

- 结论：`diagnostic_complete`
- 建议：Diagnostic research only; no authorization.
- 阻断项：无

## 策略与买入持有比较

| 指标 | 策略 | 买入持有 | 差异（策略－买入持有） |
| --- | ---: | ---: | ---: |
| annual_return | 0.107009 | 0.227443 | -0.120434 |
| sharpe | 0.901333 | 0.956695 | -0.055362 |
| Sortino | 1.208314 | 1.277593 | -0.069279 |
| calmar | 0.804420 | 0.907720 | -0.103300 |
| cvar5 | -0.017153 | -0.034257 | 0.017104 |
| max_drawdown | -0.133027 | -0.250565 | 0.117538 |
| turnover | 3.348996 | 3.920570 | -0.571574 |
| total_cost | 1922.833450 | 199.767400 | 1723.066050 |

## OOS 分布

{
  "window_count": 5,
  "win_rate": 0.0,
  "median_excess_return": -0.046538857500000086,
  "best_excess_return": -0.013867076799999767,
  "worst_excess_return": -0.13179077159999997
}

## 执行、换手与成本

{
  "strategy": {
    "invested_sessions": 625,
    "cash_sessions": 5,
    "exposure_ratio": 0.9920634920634921,
    "turnover": 3.3489955704887624,
    "total_cost": 1922.83345,
    "cost_drag": 0.0192283345
  },
  "buy_and_hold": {
    "invested_sessions": 625,
    "cash_sessions": 5,
    "exposure_ratio": 0.9920634920634921,
    "turnover": 3.920569583142156,
    "total_cost": 199.7674,
    "cost_drag": 0.001997674
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
    "data_fingerprint": "6d3bec467d9953d0fcecfb19b5f33b7f305ec092eb0217e353f0bc82573bcb99",
    "run_mode": "research_diagnostic",
    "research_only": true,
    "activation_eligible": false,
    "shadow_run_eligible": false,
    "trading_authorized": false,
    "target": {
      "exposure_id": "nasdaq_100",
      "stock_code": "513100.SH",
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
              "annual_return": 0.28054129411422535,
              "annual_volatility": 0.23847071926160063,
              "sharpe": 1.17641819919398,
              "sortino": 1.3288881891726243,
              "calmar": 1.5656221199362974,
              "worst_126_session_return": 0.1305001619999997,
              "cvar5": -0.03989967459374527,
              "win_rate": 0.568,
              "payoff_ratio": 0.9033452031885624,
              "profit_factor": 1.2334136428151523,
              "turnover": 0.9433061098099356,
              "minimum_commission_share": 0.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 2.99838,
              "max_drawdown": -0.1791883817569211,
              "recovery_sessions": 1,
              "total_cost": 39.9838
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
              "annual_return": 0.12959561083592352,
              "annual_volatility": 0.11876397795798202,
              "sharpe": 1.0912030151244485,
              "sortino": 1.2413012157769026,
              "calmar": 1.3981566156970486,
              "worst_126_session_return": 0.06231052960000083,
              "cvar5": -0.019932880340624442,
              "win_rate": 0.568,
              "payoff_ratio": 0.9254553538309598,
              "profit_factor": 1.2168024096666321,
              "turnover": 0.7506559938878898,
              "minimum_commission_share": 1.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 0.055776,
              "max_drawdown": -0.09269033910862257,
              "recovery_sessions": 1,
              "total_cost": 438.14704
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
              "annual_return": 0.051636775242464905,
              "annual_volatility": 0.1994688787803615,
              "sharpe": 0.2588713365122136,
              "sortino": 0.35299619537087323,
              "calmar": 0.5308447590368589,
              "worst_126_session_return": 0.02528856439999916,
              "cvar5": -0.030952899575204435,
              "win_rate": 0.544,
              "payoff_ratio": 0.8590665739711896,
              "profit_factor": 1.0621186732734706,
              "turnover": 0.9617544115804972,
              "minimum_commission_share": 0.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 2.9983543543543547,
              "max_drawdown": -0.09727283610400972,
              "recovery_sessions": 43,
              "total_cost": 39.943560000000005
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
              "annual_return": 0.02315932500264095,
              "annual_volatility": 0.09986741816070245,
              "sharpe": 0.2319007082507524,
              "sortino": 0.31492586586032767,
              "calmar": 0.46170861207681274,
              "worst_126_session_return": 0.01142148759999917,
              "cvar5": -0.015531004478493371,
              "win_rate": 0.544,
              "payoff_ratio": 0.8792293995791676,
              "profit_factor": 1.0489052486207613,
              "turnover": 0.6991993819097332,
              "minimum_commission_share": 1.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 0.059309,
              "max_drawdown": -0.050160045528429564,
              "recovery_sessions": 43,
              "total_cost": 381.35124
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
              "annual_return": 0.19106126285931313,
              "annual_volatility": 0.2763239574279447,
              "sharpe": 0.6914393693465215,
              "sortino": 0.8057356207134866,
              "calmar": 1.1108250414990541,
              "worst_126_session_return": 0.0906005799999996,
              "cvar5": -0.041892998484214815,
              "win_rate": 0.512,
              "payoff_ratio": 1.0366018575778642,
              "profit_factor": 1.1846878372318448,
              "turnover": 0.983672959199517,
              "minimum_commission_share": 0.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 2.998198198198198,
              "max_drawdown": -0.1719994199999999,
              "recovery_sessions": 46,
              "total_cost": 39.942
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
              "annual_return": 0.0908171731620977,
              "annual_volatility": 0.13769026452101107,
              "sharpe": 0.6595758493022525,
              "sortino": 0.7774200342195258,
              "calmar": 1.0292630201271353,
              "worst_126_session_return": 0.04406172249999951,
              "cvar5": -0.020922097487300968,
              "win_rate": 0.512,
              "payoff_ratio": 1.0560694096028527,
              "profit_factor": 1.1653179692169409,
              "turnover": 0.7256565805766703,
              "minimum_commission_share": 1.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 0.06545597014925374,
              "max_drawdown": -0.08823514630000007,
              "recovery_sessions": 46,
              "total_cost": 356.92775
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
              "annual_return": 0.10995626449487728,
              "annual_volatility": 0.19036393704745092,
              "sharpe": 0.577610792255621,
              "sortino": 0.9382344067806202,
              "calmar": 0.9021825763631227,
              "worst_126_session_return": 0.05310857279999959,
              "cvar5": -0.02664534635712884,
              "win_rate": 0.464,
              "payoff_ratio": 1.247486037290931,
              "profit_factor": 1.1131413871211384,
              "turnover": 0.9105359285608794,
              "minimum_commission_share": 0.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 2.99827027027027,
              "max_drawdown": -0.12187806257368972,
              "recovery_sessions": 1,
              "total_cost": 39.942719999999994
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
              "annual_return": 0.05077609586955045,
              "annual_volatility": 0.09524694313963929,
              "sharpe": 0.5330994801072915,
              "sortino": 0.8589046485635766,
              "calmar": 0.795492212450013,
              "worst_126_session_return": 0.024872250599999646,
              "cvar5": -0.013402536042377086,
              "win_rate": 0.464,
              "payoff_ratio": 1.2697436830158098,
              "profit_factor": 1.099181098730104,
              "turnover": 0.6809173505367874,
              "minimum_commission_share": 1.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 0.0667966875,
              "max_drawdown": -0.06382978371738757,
              "recovery_sessions": 1,
              "total_cost": 341.37494
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
              "annual_return": 0.5752702398536544,
              "annual_volatility": 0.2733508027904482,
              "sharpe": 2.104512713996523,
              "sortino": 3.7787690836318144,
              "calmar": 4.201499012035221,
              "worst_126_session_return": 0.25283644680000195,
              "cvar5": -0.032272648232508395,
              "win_rate": 0.552,
              "payoff_ratio": 1.0641873213082966,
              "profit_factor": 1.3597949105606013,
              "turnover": 0.8454821117265742,
              "minimum_commission_share": 0.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 2.9995315315315314,
              "max_drawdown": -0.13692023685017873,
              "recovery_sessions": 13,
              "total_cost": 39.95532
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
              "annual_return": 0.2590430733537137,
              "annual_volatility": 0.13677911584363953,
              "sharpe": 1.893878840756958,
              "sortino": 3.3866997685501232,
              "calmar": 3.669402617078923,
              "worst_126_session_return": 0.12104567519999954,
              "cvar5": -0.016158533004346626,
              "win_rate": 0.552,
              "payoff_ratio": 1.0752679176236386,
              "profit_factor": 1.348972478473292,
              "turnover": 0.7674204884354618,
              "minimum_commission_share": 1.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 0.06587494736842105,
              "max_drawdown": -0.07059543483945308,
              "recovery_sessions": 13,
              "total_cost": 405.03248
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
      "experiment_id": "round2-nasdaq-20260917",
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
        "513100.SH"
      ]
    },
    "experiment_hash": "94df218c02d64add06e34ac71513377475bb942381f10440a3d296a64b4ac04a",
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
        "shares": 38500,
        "raw_price": 1.2983894
      },
      {
        "event_date": "2024-02-22",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 1.3013903
      },
      {
        "event_date": "2024-02-23",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.3216034
      },
      {
        "event_date": "2024-02-26",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 300,
        "raw_price": 1.3106067
      },
      {
        "event_date": "2024-02-27",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.3083924
      },
      {
        "event_date": "2024-03-01",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.3143942
      },
      {
        "event_date": "2024-03-04",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.3365989
      },
      {
        "event_date": "2024-03-05",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.3256022
      },
      {
        "event_date": "2024-03-07",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.3213963
      },
      {
        "event_date": "2024-03-08",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.3374011
      },
      {
        "event_date": "2024-03-11",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.3166049
      },
      {
        "event_date": "2024-03-12",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 1.3183954
      },
      {
        "event_date": "2024-03-14",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.3226031
      },
      {
        "event_date": "2024-03-18",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.3073921
      },
      {
        "event_date": "2024-03-20",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.3153944999999998
      },
      {
        "event_date": "2024-03-22",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 300,
        "raw_price": 1.3345995
      },
      {
        "event_date": "2024-03-27",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.3345995
      },
      {
        "event_date": "2024-04-08",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.3273981
      },
      {
        "event_date": "2024-04-12",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.3424026
      },
      {
        "event_date": "2024-04-15",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.3226031
      },
      {
        "event_date": "2024-04-16",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.2993896999999999
      },
      {
        "event_date": "2024-04-17",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 500,
        "raw_price": 1.2973891
      },
      {
        "event_date": "2024-04-19",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.2643792
      },
      {
        "event_date": "2024-04-22",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 300,
        "raw_price": 1.250375
      },
      {
        "event_date": "2024-04-23",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 1.260378
      },
      {
        "event_date": "2024-04-25",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 400,
        "raw_price": 1.2736178
      },
      {
        "event_date": "2024-04-26",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 1.2883864
      },
      {
        "event_date": "2024-04-29",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 300,
        "raw_price": 1.3006096999999999
      },
      {
        "event_date": "2024-04-30",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.2966109
      },
      {
        "event_date": "2024-05-08",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.3186043
      },
      {
        "event_date": "2024-05-09",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.3146055
      },
      {
        "event_date": "2024-05-14",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.3246025
      },
      {
        "event_date": "2024-05-16",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.3555932000000002
      },
      {
        "event_date": "2024-05-17",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 300,
        "raw_price": 1.3545935
      },
      {
        "event_date": "2024-05-22",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.3685893
      },
      {
        "event_date": "2024-05-23",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.3745875
      },
      {
        "event_date": "2024-05-24",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.3635908
      },
      {
        "event_date": "2024-05-27",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 300,
        "raw_price": 1.3714112999999999
      },
      {
        "event_date": "2024-05-28",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.3765869
      },
      {
        "event_date": "2024-05-31",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.3484044
      },
      {
        "event_date": "2024-06-03",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.3594077
      },
      {
        "event_date": "2024-06-06",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.3925821
      },
      {
        "event_date": "2024-06-07",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 300,
        "raw_price": 1.3915823999999999
      },
      {
        "event_date": "2024-06-12",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.4075776
      },
      {
        "event_date": "2024-06-13",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.4335698
      },
      {
        "event_date": "2024-06-14",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 400,
        "raw_price": 1.4335698
      },
      {
        "event_date": "2024-06-18",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.4565629000000002
      },
      {
        "event_date": "2024-06-19",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.4605617000000002
      },
      {
        "event_date": "2024-06-21",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.4525641
      },
      {
        "event_date": "2024-06-24",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.4434329
      },
      {
        "event_date": "2024-06-25",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.4264278
      },
      {
        "event_date": "2024-06-26",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 1.4474341
      },
      {
        "event_date": "2024-06-27",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.449565
      },
      {
        "event_date": "2024-07-01",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 300,
        "raw_price": 1.4665599
      },
      {
        "event_date": "2024-07-04",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 300,
        "raw_price": 1.519544
      },
      {
        "event_date": "2024-07-05",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.5115464
      },
      {
        "event_date": "2024-07-08",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.5465359
      },
      {
        "event_date": "2024-07-09",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 300,
        "raw_price": 1.5585323
      },
      {
        "event_date": "2024-07-10",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.5695290000000002
      },
      {
        "event_date": "2024-07-11",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 1.5684704
      },
      {
        "event_date": "2024-07-15",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 600,
        "raw_price": 1.5054515
      },
      {
        "event_date": "2024-07-16",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 400,
        "raw_price": 1.5435368
      },
      {
        "event_date": "2024-07-18",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.4664397999999998
      },
      {
        "event_date": "2024-07-19",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 300,
        "raw_price": 1.4774431000000001
      },
      {
        "event_date": "2024-07-22",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 300,
        "raw_price": 1.460438
      },
      {
        "event_date": "2024-07-23",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.4834449
      },
      {
        "event_date": "2024-07-24",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.4645605000000002
      },
      {
        "event_date": "2024-07-25",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 300,
        "raw_price": 1.410423
      },
      {
        "event_date": "2024-07-26",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 500,
        "raw_price": 1.3964188
      },
      {
        "event_date": "2024-07-30",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 300,
        "raw_price": 1.4215734
      },
      {
        "event_date": "2024-07-31",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.4124236
      },
      {
        "event_date": "2024-08-02",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 400,
        "raw_price": 1.4105767
      },
      {
        "event_date": "2024-08-05",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 700,
        "raw_price": 1.330399
      },
      {
        "event_date": "2024-08-06",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 1600,
        "raw_price": 1.3354005
      },
      {
        "event_date": "2024-08-07",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 600,
        "raw_price": 1.3316004000000001
      },
      {
        "event_date": "2024-08-09",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 1.3554065
      },
      {
        "event_date": "2024-08-12",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 400,
        "raw_price": 1.3545935
      },
      {
        "event_date": "2024-08-13",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.3675896
      },
      {
        "event_date": "2024-08-14",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.4115764
      },
      {
        "event_date": "2024-08-15",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 500,
        "raw_price": 1.4165749
      },
      {
        "event_date": "2024-08-16",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.4615614000000001
      },
      {
        "event_date": "2024-08-19",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 600,
        "raw_price": 1.469559
      },
      {
        "event_date": "2024-08-20",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 300,
        "raw_price": 1.4684404
      }
    ],
    "by_reason": {
      "grid_initialize": {
        "reason": "grid_initialize",
        "fill_count": 1,
        "shares": 38500,
        "traded_value": "49987.9919000"
      },
      "grid_buy": {
        "reason": "grid_buy",
        "fill_count": 35,
        "shares": 8800,
        "traded_value": "12065.4185399999999500"
      },
      "grid_sell": {
        "reason": "grid_sell",
        "fill_count": 47,
        "shares": 10800,
        "traded_value": "15117.4634000000001500"
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
        "shares": 33800,
        "raw_price": 1.4774431000000001
      },
      {
        "event_date": "2024-08-23",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.4494347
      },
      {
        "event_date": "2024-08-26",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.4704409999999999
      },
      {
        "event_date": "2024-08-28",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 1.4414323
      },
      {
        "event_date": "2024-08-30",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 400,
        "raw_price": 1.4134239
      },
      {
        "event_date": "2024-09-03",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.4305707
      },
      {
        "event_date": "2024-09-04",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.3735878000000001
      },
      {
        "event_date": "2024-09-05",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 900,
        "raw_price": 1.3664098
      },
      {
        "event_date": "2024-09-09",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.3485953
      },
      {
        "event_date": "2024-09-12",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.4135758
      },
      {
        "event_date": "2024-09-13",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 500,
        "raw_price": 1.4315704
      },
      {
        "event_date": "2024-09-18",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.4325701000000002
      },
      {
        "event_date": "2024-09-20",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.4555632
      },
      {
        "event_date": "2024-09-24",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.449565
      },
      {
        "event_date": "2024-09-26",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.4454335
      },
      {
        "event_date": "2024-09-30",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 1.4014203
      },
      {
        "event_date": "2024-10-08",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.3904169999999998
      },
      {
        "event_date": "2024-10-09",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.430429
      },
      {
        "event_date": "2024-10-10",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.4385683
      },
      {
        "event_date": "2024-10-11",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.4445665
      },
      {
        "event_date": "2024-10-15",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.459562
      },
      {
        "event_date": "2024-10-16",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 300,
        "raw_price": 1.4545635000000001
      },
      {
        "event_date": "2024-10-17",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.4574371
      },
      {
        "event_date": "2024-10-25",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.4564367999999999
      },
      {
        "event_date": "2024-10-29",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.4655602
      },
      {
        "event_date": "2024-10-31",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.4625611
      },
      {
        "event_date": "2024-11-01",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 1.4334299
      },
      {
        "event_date": "2024-11-04",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 1.4414323
      },
      {
        "event_date": "2024-11-07",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 500,
        "raw_price": 1.5145454999999999
      },
      {
        "event_date": "2024-11-08",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.5245425
      },
      {
        "event_date": "2024-11-11",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.529541
      },
      {
        "event_date": "2024-11-12",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.5345395
      },
      {
        "event_date": "2024-11-18",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 1.4914473000000001
      },
      {
        "event_date": "2024-11-19",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.4964488
      },
      {
        "event_date": "2024-11-21",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.509547
      },
      {
        "event_date": "2024-11-26",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.5285412999999999
      },
      {
        "event_date": "2024-12-04",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 300,
        "raw_price": 1.5755272
      },
      {
        "event_date": "2024-12-05",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.5895230000000002
      },
      {
        "event_date": "2024-12-06",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.5805257
      },
      {
        "event_date": "2024-12-10",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 300,
        "raw_price": 1.5855242
      },
      {
        "event_date": "2024-12-11",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.5934779
      },
      {
        "event_date": "2024-12-13",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.6155152000000002
      },
      {
        "event_date": "2024-12-16",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.6305107
      },
      {
        "event_date": "2024-12-17",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.6754972
      },
      {
        "event_date": "2024-12-18",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.6575026
      },
      {
        "event_date": "2024-12-19",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.6165149
      },
      {
        "event_date": "2024-12-20",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 300,
        "raw_price": 1.620486
      },
      {
        "event_date": "2024-12-23",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 400,
        "raw_price": 1.6264877999999998
      },
      {
        "event_date": "2024-12-24",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 500,
        "raw_price": 1.6724981
      },
      {
        "event_date": "2024-12-26",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.6684993000000001
      },
      {
        "event_date": "2024-12-27",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.6635008
      },
      {
        "event_date": "2024-12-31",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 300,
        "raw_price": 1.6254875
      },
      {
        "event_date": "2025-01-02",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.6254875
      },
      {
        "event_date": "2025-01-03",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.6385083
      },
      {
        "event_date": "2025-01-07",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.6864939
      },
      {
        "event_date": "2025-01-09",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.6404919999999998
      },
      {
        "event_date": "2025-01-10",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.6284884
      },
      {
        "event_date": "2025-01-14",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 400,
        "raw_price": 1.6094826999999998
      },
      {
        "event_date": "2025-01-15",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.6025191
      },
      {
        "event_date": "2025-01-17",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.6215134000000002
      },
      {
        "event_date": "2025-01-21",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.6405077000000001
      },
      {
        "event_date": "2025-01-23",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.6625011
      },
      {
        "event_date": "2025-02-05",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 300,
        "raw_price": 1.6174851
      },
      {
        "event_date": "2025-02-11",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.6124836
      },
      {
        "event_date": "2025-02-17",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.6285113
      },
      {
        "event_date": "2025-02-19",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.6385083
      },
      {
        "event_date": "2025-02-21",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.6164848
      },
      {
        "event_date": "2025-02-24",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.5814743
      },
      {
        "event_date": "2025-02-25",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 1.5684704
      },
      {
        "event_date": "2025-02-26",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 300,
        "raw_price": 1.5554664999999999
      },
      {
        "event_date": "2025-03-03",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 600,
        "raw_price": 1.5284583999999999
      },
      {
        "event_date": "2025-03-04",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 300,
        "raw_price": 1.5045484999999998
      }
    ],
    "by_reason": {
      "grid_initialize": {
        "reason": "grid_initialize",
        "fill_count": 1,
        "shares": 33800,
        "traded_value": "49937.5767800000033800"
      },
      "grid_buy": {
        "reason": "grid_buy",
        "fill_count": 30,
        "shares": 6600,
        "traded_value": "9977.2922899999997100"
      },
      "grid_sell": {
        "reason": "grid_sell",
        "fill_count": 41,
        "shares": 7300,
        "traded_value": "11270.5178300000000500"
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
        "shares": 32500,
        "raw_price": 1.5364608
      },
      {
        "event_date": "2025-03-10",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 400,
        "raw_price": 1.4984494
      },
      {
        "event_date": "2025-03-12",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 800,
        "raw_price": 1.4254275
      },
      {
        "event_date": "2025-03-14",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.4194257
      },
      {
        "event_date": "2025-03-17",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.4515644
      },
      {
        "event_date": "2025-03-18",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.4505647000000002
      },
      {
        "event_date": "2025-03-19",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.4415674
      },
      {
        "event_date": "2025-03-21",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.469559
      },
      {
        "event_date": "2025-03-25",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 300,
        "raw_price": 1.5235428
      },
      {
        "event_date": "2025-03-26",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.5215434
      },
      {
        "event_date": "2025-03-28",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 1.4774431000000001
      },
      {
        "event_date": "2025-03-31",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.4284283999999998
      },
      {
        "event_date": "2025-04-01",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 700,
        "raw_price": 1.420426
      },
      {
        "event_date": "2025-04-02",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.4415674
      },
      {
        "event_date": "2025-04-03",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.4085773000000001
      },
      {
        "event_date": "2025-04-07",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 300,
        "raw_price": 1.2723816
      },
      {
        "event_date": "2025-04-08",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 1900,
        "raw_price": 1.3063918
      },
      {
        "event_date": "2025-04-09",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 600,
        "raw_price": 1.2706187
      },
      {
        "event_date": "2025-04-10",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 1.430429
      },
      {
        "event_date": "2025-04-11",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 1600,
        "raw_price": 1.3715884000000003
      },
      {
        "event_date": "2025-04-14",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.4354305
      },
      {
        "event_date": "2025-04-15",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.4245725
      },
      {
        "event_date": "2025-04-16",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.4004199999999998
      },
      {
        "event_date": "2025-04-17",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 300,
        "raw_price": 1.3794137
      },
      {
        "event_date": "2025-04-21",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.3744122
      },
      {
        "event_date": "2025-04-22",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 1.3614083
      },
      {
        "event_date": "2025-04-24",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 500,
        "raw_price": 1.419574
      },
      {
        "event_date": "2025-04-25",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.4364308
      },
      {
        "event_date": "2025-04-28",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 500,
        "raw_price": 1.439568
      },
      {
        "event_date": "2025-05-07",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.4625611
      },
      {
        "event_date": "2025-05-08",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.4765569
      },
      {
        "event_date": "2025-05-09",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.4845545000000002
      },
      {
        "event_date": "2025-05-13",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 400,
        "raw_price": 1.5375386
      },
      {
        "event_date": "2025-05-15",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 500,
        "raw_price": 1.5635308
      },
      {
        "event_date": "2025-05-20",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.5654694999999998
      },
      {
        "event_date": "2025-05-21",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.5625311
      },
      {
        "event_date": "2025-05-22",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.540462
      },
      {
        "event_date": "2025-05-23",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.540462
      },
      {
        "event_date": "2025-05-29",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.5895230000000002
      },
      {
        "event_date": "2025-05-30",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.5535338
      },
      {
        "event_date": "2025-06-03",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 1.5674701
      },
      {
        "event_date": "2025-06-05",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.5745275
      },
      {
        "event_date": "2025-06-16",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.5614682999999998
      },
      {
        "event_date": "2025-06-18",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.5675296
      },
      {
        "event_date": "2025-06-20",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.5594677
      },
      {
        "event_date": "2025-06-25",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 300,
        "raw_price": 1.5955212
      },
      {
        "event_date": "2025-06-27",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.6115164000000002
      },
      {
        "event_date": "2025-06-30",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.6245125
      },
      {
        "event_date": "2025-07-01",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.6305107
      },
      {
        "event_date": "2025-07-07",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.6325101
      },
      {
        "event_date": "2025-07-16",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.639508
      },
      {
        "event_date": "2025-07-21",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.6625011
      },
      {
        "event_date": "2025-07-29",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.6824951000000001
      },
      {
        "event_date": "2025-08-01",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.6734978
      },
      {
        "event_date": "2025-08-04",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 1.6434929
      },
      {
        "event_date": "2025-08-05",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 1.6725016
      },
      {
        "event_date": "2025-08-06",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.6575026
      },
      {
        "event_date": "2025-08-08",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.6904927
      },
      {
        "event_date": "2025-08-12",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.7014894
      },
      {
        "event_date": "2025-08-14",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.7174846000000001
      },
      {
        "event_date": "2025-08-20",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.6785033999999999
      },
      {
        "event_date": "2025-08-21",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.6765028
      },
      {
        "event_date": "2025-08-25",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.70051
      },
      {
        "event_date": "2025-08-26",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.6904927
      },
      {
        "event_date": "2025-08-28",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.6934918
      },
      {
        "event_date": "2025-09-01",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.6795037
      },
      {
        "event_date": "2025-09-02",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.6765028
      }
    ],
    "by_reason": {
      "grid_initialize": {
        "reason": "grid_initialize",
        "fill_count": 1,
        "shares": 32500,
        "traded_value": "49934.9760000"
      },
      "grid_buy": {
        "reason": "grid_buy",
        "fill_count": 28,
        "shares": 7200,
        "traded_value": "10309.5919499999999300"
      },
      "grid_sell": {
        "reason": "grid_sell",
        "fill_count": 38,
        "shares": 8600,
        "traded_value": "12862.1402000000006400"
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
        "shares": 29400,
        "raw_price": 1.6985093999999998
      },
      {
        "event_date": "2025-09-16",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.7354792
      },
      {
        "event_date": "2025-09-19",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.7504747
      },
      {
        "event_date": "2025-09-22",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.7614714
      },
      {
        "event_date": "2025-09-23",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.7874636000000002
      },
      {
        "event_date": "2025-09-24",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 300,
        "raw_price": 1.7834648000000002
      },
      {
        "event_date": "2025-09-25",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.7795336999999998
      },
      {
        "event_date": "2025-09-30",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.8014594000000002
      },
      {
        "event_date": "2025-10-09",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.8414474
      },
      {
        "event_date": "2025-10-10",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 300,
        "raw_price": 1.8514444
      },
      {
        "event_date": "2025-10-14",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.8555564999999998
      },
      {
        "event_date": "2025-10-15",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 1.8235469
      },
      {
        "event_date": "2025-10-16",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.8224531
      },
      {
        "event_date": "2025-10-17",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.8244525
      },
      {
        "event_date": "2025-10-20",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 1.8355504999999999
      },
      {
        "event_date": "2025-10-21",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 300,
        "raw_price": 1.8874336
      },
      {
        "event_date": "2025-10-22",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.8704387
      },
      {
        "event_date": "2025-10-23",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.8674396000000002
      },
      {
        "event_date": "2025-10-27",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.9224231
      },
      {
        "event_date": "2025-10-28",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 400,
        "raw_price": 1.9754072
      },
      {
        "event_date": "2025-10-29",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.9834048
      },
      {
        "event_date": "2025-10-30",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.9964009000000003
      },
      {
        "event_date": "2025-11-05",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 300,
        "raw_price": 1.8905669999999999
      },
      {
        "event_date": "2025-11-06",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 1.9235769
      },
      {
        "event_date": "2025-11-07",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.9174246
      },
      {
        "event_date": "2025-11-10",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.9465838
      },
      {
        "event_date": "2025-11-11",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.9744075
      },
      {
        "event_date": "2025-11-13",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.969409
      },
      {
        "event_date": "2025-11-17",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 300,
        "raw_price": 1.9415823
      },
      {
        "event_date": "2025-11-18",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.8815643
      },
      {
        "event_date": "2025-11-19",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 500,
        "raw_price": 1.8355504999999999
      },
      {
        "event_date": "2025-11-20",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.8795636999999998
      },
      {
        "event_date": "2025-11-21",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 500,
        "raw_price": 1.8334498000000001
      },
      {
        "event_date": "2025-11-24",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 400,
        "raw_price": 1.8685604
      },
      {
        "event_date": "2025-11-26",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 300,
        "raw_price": 1.9104267000000001
      },
      {
        "event_date": "2025-11-27",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.9404177
      },
      {
        "event_date": "2025-12-01",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.929421
      },
      {
        "event_date": "2025-12-04",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.9644105
      },
      {
        "event_date": "2025-12-10",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 1.9285784
      },
      {
        "event_date": "2025-12-16",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 1.8905669999999999
      },
      {
        "event_date": "2025-12-17",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 1.8865657999999998
      },
      {
        "event_date": "2025-12-18",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.8724381
      },
      {
        "event_date": "2025-12-22",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.939418
      },
      {
        "event_date": "2025-12-23",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 300,
        "raw_price": 1.9454162
      },
      {
        "event_date": "2025-12-29",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.9255775
      },
      {
        "event_date": "2025-12-31",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.9055715
      },
      {
        "event_date": "2026-01-06",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.9314204
      },
      {
        "event_date": "2026-01-09",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 1.8965687999999998
      },
      {
        "event_date": "2026-01-20",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.8875661
      },
      {
        "event_date": "2026-01-29",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.8944315
      },
      {
        "event_date": "2026-02-02",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.8585574
      },
      {
        "event_date": "2026-02-03",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 400,
        "raw_price": 1.8705610000000001
      },
      {
        "event_date": "2026-02-04",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.8484453
      },
      {
        "event_date": "2026-02-06",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.8095427
      },
      {
        "event_date": "2026-02-09",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 1.8465538000000001
      },
      {
        "event_date": "2026-02-10",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.8504447
      },
      {
        "event_date": "2026-03-02",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.8045412
      },
      {
        "event_date": "2026-03-03",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.810543
      },
      {
        "event_date": "2026-03-04",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.7795336999999998
      },
      {
        "event_date": "2026-03-05",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 1.790537
      },
      {
        "event_date": "2026-03-06",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.7934618
      },
      {
        "event_date": "2026-03-10",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 300,
        "raw_price": 1.7925376
      },
      {
        "event_date": "2026-03-11",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.7914624000000001
      },
      {
        "event_date": "2026-03-16",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.7635288999999998
      }
    ],
    "by_reason": {
      "grid_initialize": {
        "reason": "grid_initialize",
        "fill_count": 1,
        "shares": 29400,
        "traded_value": "49936.1763599999941200"
      },
      "grid_sell": {
        "reason": "grid_sell",
        "fill_count": 34,
        "shares": 6000,
        "traded_value": "11274.2167200000002800"
      },
      "grid_buy": {
        "reason": "grid_buy",
        "fill_count": 29,
        "shares": 5400,
        "traded_value": "10054.0152999999997600"
      }
    },
    "invested_sessions": 125,
    "cash_sessions": 1,
    "rejected_order_count": 0
  },
  {
    "window_id": "wf_004",
    "trade_points": [
      {
        "event_date": "2026-03-20",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 28200,
        "raw_price": 1.7715313
      },
      {
        "event_date": "2026-03-23",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 1.7255175
      },
      {
        "event_date": "2026-03-24",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 500,
        "raw_price": 1.6995097
      },
      {
        "event_date": "2026-03-25",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 1.729481
      },
      {
        "event_date": "2026-03-26",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.729481
      },
      {
        "event_date": "2026-03-30",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.6725016
      },
      {
        "event_date": "2026-03-31",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 1.6805039999999998
      },
      {
        "event_date": "2026-04-01",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.7245172
      },
      {
        "event_date": "2026-04-02",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 600,
        "raw_price": 1.7444765000000002
      },
      {
        "event_date": "2026-04-03",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 1.7375211000000002
      },
      {
        "event_date": "2026-04-09",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 800,
        "raw_price": 1.8324501
      },
      {
        "event_date": "2026-04-10",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.8245472
      },
      {
        "event_date": "2026-04-14",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 1.8335499
      },
      {
        "event_date": "2026-04-15",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.8554432
      },
      {
        "event_date": "2026-04-16",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 300,
        "raw_price": 1.89943
      },
      {
        "event_date": "2026-04-17",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 300,
        "raw_price": 1.9014294
      },
      {
        "event_date": "2026-04-28",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 300,
        "raw_price": 1.9444165000000002
      },
      {
        "event_date": "2026-04-29",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 1.9504147
      },
      {
        "event_date": "2026-05-07",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 300,
        "raw_price": 2.029391
      },
      {
        "event_date": "2026-05-08",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 300,
        "raw_price": 2.0483853
      },
      {
        "event_date": "2026-05-11",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.1033688
      },
      {
        "event_date": "2026-05-12",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 300,
        "raw_price": 2.0973706
      },
      {
        "event_date": "2026-05-13",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 2.0766228
      },
      {
        "event_date": "2026-05-19",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 2.0586173999999997
      },
      {
        "event_date": "2026-05-20",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 2.0366108
      },
      {
        "event_date": "2026-05-22",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 200,
        "raw_price": 2.119364
      },
      {
        "event_date": "2026-05-25",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 300,
        "raw_price": 2.2103367
      },
      {
        "event_date": "2026-05-26",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 500,
        "raw_price": 2.2303307
      },
      {
        "event_date": "2026-05-27",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 2.2156645
      },
      {
        "event_date": "2026-05-28",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.2253322
      },
      {
        "event_date": "2026-06-01",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 300,
        "raw_price": 2.2723181
      },
      {
        "event_date": "2026-06-02",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 500,
        "raw_price": 2.3542935000000003
      },
      {
        "event_date": "2026-06-04",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 300,
        "raw_price": 2.310693
      },
      {
        "event_date": "2026-06-05",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 300,
        "raw_price": 2.2026605999999997
      },
      {
        "event_date": "2026-06-08",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 2.1166348
      },
      {
        "event_date": "2026-06-09",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 500,
        "raw_price": 2.150645
      },
      {
        "event_date": "2026-06-10",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 400,
        "raw_price": 2.1553532000000004
      },
      {
        "event_date": "2026-06-11",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 2.1236369
      },
      {
        "event_date": "2026-06-12",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 2.210663
      },
      {
        "event_date": "2026-06-15",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.2303307
      },
      {
        "event_date": "2026-06-16",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 500,
        "raw_price": 2.2633208
      },
      {
        "event_date": "2026-06-17",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.2503247
      },
      {
        "event_date": "2026-06-24",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 500,
        "raw_price": 2.1546461999999997
      },
      {
        "event_date": "2026-06-26",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.2053382
      },
      {
        "event_date": "2026-06-29",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 2.1616483
      },
      {
        "event_date": "2026-06-30",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.2103367
      },
      {
        "event_date": "2026-07-01",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.2263319
      },
      {
        "event_date": "2026-07-03",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 2.150645
      },
      {
        "event_date": "2026-07-09",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 2.1576471
      },
      {
        "event_date": "2026-07-10",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.1803457
      },
      {
        "event_date": "2026-07-16",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.1673496
      },
      {
        "event_date": "2026-07-20",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 400,
        "raw_price": 2.1076321
      },
      {
        "event_date": "2026-07-22",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.1383582999999997
      },
      {
        "event_date": "2026-07-27",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 2.1056315
      },
      {
        "event_date": "2026-07-29",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 2.0766228
      },
      {
        "event_date": "2026-07-31",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 2.1116333000000003
      },
      {
        "event_date": "2026-08-03",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 400,
        "raw_price": 2.1143655000000003
      },
      {
        "event_date": "2026-08-04",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.169349
      },
      {
        "event_date": "2026-08-05",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 300,
        "raw_price": 2.2583223
      },
      {
        "event_date": "2026-08-06",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 500,
        "raw_price": 2.2423271
      },
      {
        "event_date": "2026-08-07",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 2.2446732000000003
      },
      {
        "event_date": "2026-08-10",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.2793159999999997
      },
      {
        "event_date": "2026-08-12",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 2.2116632999999997
      },
      {
        "event_date": "2026-08-17",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.2633208
      },
      {
        "event_date": "2026-08-18",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.2423271
      },
      {
        "event_date": "2026-08-19",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 2.1976591
      },
      {
        "event_date": "2026-08-20",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 2.2176651
      },
      {
        "event_date": "2026-08-25",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 200,
        "raw_price": 2.1596477
      },
      {
        "event_date": "2026-08-26",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.1953412
      },
      {
        "event_date": "2026-08-28",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.2433268
      },
      {
        "event_date": "2026-08-31",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.2063379
      },
      {
        "event_date": "2026-09-03",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 2.2016603
      },
      {
        "event_date": "2026-09-08",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.2383283
      },
      {
        "event_date": "2026-09-14",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 2.1956585
      },
      {
        "event_date": "2026-09-15",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 100,
        "raw_price": 2.1956585
      },
      {
        "event_date": "2026-09-17",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 100,
        "raw_price": 2.2173346
      }
    ],
    "by_reason": {
      "grid_initialize": {
        "reason": "grid_initialize",
        "fill_count": 1,
        "shares": 28200,
        "traded_value": "49957.1826600"
      },
      "grid_buy": {
        "reason": "grid_buy",
        "fill_count": 34,
        "shares": 6600,
        "traded_value": "13610.8820399999997600"
      },
      "grid_sell": {
        "reason": "grid_sell",
        "fill_count": 41,
        "shares": 9500,
        "traded_value": "19886.6322200000005500"
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

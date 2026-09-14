"""Run fixed-universe ETF validation and publish local research artifacts."""

import argparse
from datetime import date
from decimal import Decimal
import json
from pathlib import Path

from .research.instrument_validation import FIXED_VALIDATION_TARGETS, run_instrument_validation
from .research.experiment import APPROVED_EXPERIMENT_AXES, ExperimentSpec, bind_experiment
from .research.strategy_specs import FULL_ADAPTIVE_SPEC, BUY_AND_HOLD_SPEC
from .research.validation_provider import default_validation_provider
from .research.validation_report import validation_publication_decision, write_validation_artifacts


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start-date", required=True)
    parser.add_argument("--as-of-date", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--initial-cash", default="100000")
    parser.add_argument("--stock-code")
    args = parser.parse_args(argv)
    start, cutoff = date.fromisoformat(args.start_date), date.fromisoformat(args.as_of_date)
    if start > cutoff:
        raise ValueError("start date must not be after as-of date")
    output = Path(args.output_dir)
    output.mkdir(parents=True, exist_ok=True)
    targets = tuple(
        target for target in FIXED_VALIDATION_TARGETS
        if args.stock_code is None or target.stock_code == args.stock_code.upper()
    )
    if not targets:
        raise ValueError("stock-code is not part of the fixed validation manifest")
    provider = default_validation_provider()
    results = []
    for target in targets:
        effective_start = max(start, target.available_from) if target.available_from else start
        print(f"validating {target.stock_code} from {effective_start}", flush=True)
        result = run_instrument_validation(target, provider, effective_start, cutoff, Decimal(args.initial_cash))
        experiment = ExperimentSpec(
            "fixed-etf-adaptive-validation-v1", (target.stock_code,), FULL_ADAPTIVE_SPEC,
            (BUY_AND_HOLD_SPEC,), APPROVED_EXPERIMENT_AXES, effective_start, cutoff,
        )
        result = bind_experiment(result, experiment)
        write_validation_artifacts(result, output / target.stock_code)
        print(f"completed {target.stock_code}: {result.status.value}", flush=True)
        results.append(result)
        (output / f"instrument_validation_{target.stock_code.replace('.', '_')}.json").write_text(
            json.dumps({"as_of_date": cutoff.isoformat(), "stock_code": target.stock_code,
                        "status": result.status.value, "rejection_reason": result.rejection_reason,
                        "decision": validation_publication_decision(result),
                        "experiment_hash": result.run_manifest["experiment_hash"]}, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
    rows = [{"exposure_id": result.target.exposure_id, "stock_code": result.target.stock_code,
             "status": result.status.value, "rejection_reason": result.rejection_reason,
             "strategy_annual_return": result.strategy_annual_return,
             "benchmark_annual_return": result.benchmark_annual_return,
             "strategy_max_drawdown": result.strategy_max_drawdown,
             "benchmark_max_drawdown": result.benchmark_max_drawdown,
             "decision": validation_publication_decision(result),
             "activation_eligible": bool(result.activation_eligible and validation_publication_decision(result)["conclusion"] == "passed"),
             "scope": result.target.scope.value,
             "available_from": result.target.available_from.isoformat() if result.target.available_from else None} for result in results]
    (output / "instrument_validation.json").write_text(json.dumps({"as_of_date": cutoff.isoformat(), "results": rows}, ensure_ascii=False, indent=2), encoding="utf-8")
    passed = [row["stock_code"] for row in rows if row["activation_eligible"]]
    markdown = "# ETF 验证报告\n\n| 标的 | 状态 | 原因 |\n|---|---|---|\n" + "\n".join(f"| {row['stock_code']} | {row['status']} | {row['rejection_reason'] or ''} |" for row in rows) + "\n\n## 影子运行候选\n\n" + ("\n".join(f"- {code}" for code in passed) if passed else "无") + "\n"
    (output / "instrument_validation.md").write_text(markdown, encoding="utf-8")
    return 3 if all(row["status"] == "data_rejected" for row in rows) else 0


if __name__ == "__main__":
    raise SystemExit(main())

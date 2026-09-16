"""Run fixed-universe ETF validation and publish local research artifacts."""

import argparse
from dataclasses import asdict
from datetime import date
from decimal import Decimal
import json
from pathlib import Path

from .research.instrument_validation import FIXED_VALIDATION_TARGETS, legacy_unprofiled, run_instrument_validation
from .research.experiment import (APPROVED_EXPERIMENT_AXES, ExperimentSpec, bind_experiment,
                                  targeted_study, star50_diagnostic)
from .research.strategy_profiles import profile_for_id, profile_training_plan
from .research.strategy_specs import FULL_ADAPTIVE_SPEC, BUY_AND_HOLD_SPEC
from .research.validation_provider import default_validation_provider
from .research.validation_report import validation_publication_decision, write_atomic_text, write_validation_artifacts


def _legacy_fixed_experiment(stock_code: str, start_date: date, as_of_date: date) -> ExperimentSpec:
    """Keep the historical fixed-universe CLI readable and non-actionable."""
    return ExperimentSpec.from_dict({
        "experiment_id": "fixed-etf-adaptive-validation-v1",
        "target_codes": [stock_code],
        "strategy": asdict(FULL_ADAPTIVE_SPEC),
        "benchmarks": [asdict(BUY_AND_HOLD_SPEC)],
        "allowed_axes": {axis: list(values) for axis, values in APPROVED_EXPERIMENT_AXES.items()},
        "start_date": start_date.isoformat(),
        "as_of_date": as_of_date.isoformat(),
    })


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start-date", required=True)
    parser.add_argument("--as-of-date", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--initial-cash", default="100000")
    parser.add_argument("--stock-code")
    parser.add_argument("--experiment", help="Named research experiment; new names require --stock-code")
    parser.add_argument("--profile", choices=("grid_core", "grid_plus_optional_trend", "core_hold_rebalance"))
    args = parser.parse_args(argv)
    if args.experiment is not None and args.profile is None:
        parser.error("--experiment requires --profile")
    if args.profile is not None and args.experiment is None:
        parser.error("--profile requires --experiment")
    start, cutoff = date.fromisoformat(args.start_date), date.fromisoformat(args.as_of_date)
    if start > cutoff:
        raise ValueError("start date must not be after as-of date")
    output = Path(args.output_dir)
    study = None
    training_plan = None
    if args.experiment is not None:
        try:
            profile = profile_for_id(args.profile)
            if args.experiment in ("hk_internet", "chinext_reentry", "star50_extreme_window"):
                declaration = targeted_study(args.experiment, start_date=start, as_of_date=cutoff,
                    target_codes=(args.stock_code.upper(),) if args.stock_code else None)
                codes, axes = declaration.target_codes, declaration.allowed_axes
            else:
                if not args.stock_code:
                    parser.error("a new --experiment requires --stock-code from the fixed validation manifest")
                codes = (args.stock_code.upper(),)
                axes = {axis: APPROVED_EXPERIMENT_AXES[axis] for axis in ("step_pct", "unit_pct")}
            study = ExperimentSpec(args.experiment, codes, profile,
                                   axes if profile.strategy is not None else {}, start, cutoff)
            training_plan = (profile_training_plan(profile, profile.strategy.config, study.allowed_axes)
                             if profile.strategy is not None else {})
        except ValueError as exc:
            parser.error(str(exc))
    targets = tuple(
        target for target in FIXED_VALIDATION_TARGETS
        if args.stock_code is None or target.stock_code == args.stock_code.upper()
        if study is None or target.stock_code in study.target_codes
    )
    if not targets:
        parser.error("stock-code is not part of the fixed validation manifest")
    output.mkdir(parents=True, exist_ok=True)
    if study:
        write_atomic_text(output / "experiment.json", json.dumps(
            {"experiment": study.to_dict(), "experiment_hash": study.experiment_hash(),
             "research_only": True, "trading_authorized": False}, indent=2))
    if args.experiment == "star50_extreme_window":
        diagnostic = star50_diagnostic(study, Path("reports/etf_validation_risk_adjusted_2026-09-11-evidence-gated/588000.SH"))
        write_atomic_text(output / "diagnostic.json", json.dumps(diagnostic, indent=2))
        if not diagnostic["parameter_execution_allowed"]:
            print("STAR50 diagnostic blocked: missing largest contributor evidence", flush=True)
            return 4
    provider = default_validation_provider()
    results = []
    for target in targets:
        effective_start = max(start, target.available_from) if target.available_from else start
        print(f"validating {target.stock_code} from {effective_start}", flush=True)
        if study is not None:
            result = run_instrument_validation(target, provider, effective_start, cutoff, Decimal(args.initial_cash),
                                               profile=study.profile, training_plan=training_plan)
        else:
            result = legacy_unprofiled(target, provider, effective_start, cutoff, Decimal(args.initial_cash))
        experiment = study or _legacy_fixed_experiment(target.stock_code, effective_start, cutoff)
        result = bind_experiment(result, experiment)
        write_validation_artifacts(result, output / target.stock_code)
        print(f"completed {target.stock_code}: {result.status.value}", flush=True)
        results.append(result)
        write_atomic_text(output / f"instrument_validation_{target.stock_code.replace('.', '_')}.json",
            json.dumps({"as_of_date": cutoff.isoformat(), "stock_code": target.stock_code,
                        "status": result.status.value, "rejection_reason": result.rejection_reason,
                        "decision": validation_publication_decision(result),
                        "experiment_hash": result.run_manifest["experiment_hash"]}, ensure_ascii=False, indent=2),
        )
    rows = [{"exposure_id": result.target.exposure_id, "stock_code": result.target.stock_code,
             "status": result.status.value, "rejection_reason": result.rejection_reason,
             "strategy_annual_return": result.strategy_annual_return,
             "benchmark_annual_return": result.benchmark_annual_return,
             "strategy_max_drawdown": result.strategy_max_drawdown,
             "benchmark_max_drawdown": result.benchmark_max_drawdown,
             "profile_id": result.run_manifest["experiment"]["profile"]["profile_id"],
             "profile_version": result.run_manifest["experiment"]["profile"]["version"],
             "profile_hash": result.run_manifest["experiment"]["profile_hash"],
             "decision": validation_publication_decision(result),
             "activation_eligible": bool(result.activation_eligible and validation_publication_decision(result)["conclusion"] == "passed"),
             "scope": result.target.scope.value,
             "available_from": result.target.available_from.isoformat() if result.target.available_from else None} for result in results]
    write_atomic_text(output / "instrument_validation.json", json.dumps({"as_of_date": cutoff.isoformat(), "results": rows}, ensure_ascii=False, indent=2))
    passed = [row["stock_code"] for row in rows if row["activation_eligible"]]
    markdown = (
        "# ETF 验证报告\n\n"
        "| 标的 | 状态 | profile_id | profile_version | profile_hash | decision | 原因 / 阻断项 |\n"
        "|---|---|---|---|---|---|---|\n"
        + "\n".join(
            f"| {row['stock_code']} | {row['status']} | {row['profile_id']} | {row['profile_version']} | "
            f"{row['profile_hash']} | {row['decision']['conclusion']} | "
            f"{row['rejection_reason'] or ''} {'; '.join(row['decision']['blockers'])} |"
            for row in rows
        )
        + "\n\n## 影子运行候选\n\n"
        + ("\n".join(f"- {code}" for code in passed) if passed else "无") + "\n"
    )
    write_atomic_text(output / "instrument_validation.md", markdown)
    return 3 if all(row["status"] == "data_rejected" for row in rows) else 0


if __name__ == "__main__":
    raise SystemExit(main())

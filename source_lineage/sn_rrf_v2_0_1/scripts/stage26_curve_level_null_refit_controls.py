#!/usr/bin/env python3
"""Stage 26 curve-level null-refit controls for SN-RRF/A10-TVC-RRF.

This script performs an auditable curve-level squared-velocity residual refit:

    Vobs^2 - Vbar^2 ~= A K(r/rc)

It is an adversarial diagnostic control, not a physical model fit and not a
replacement for the earlier nonlinear velocity-space audit.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Dict, Iterable, List, Optional, Tuple

import numpy as np
import pandas as pd

CLAIM_BOUNDARY = [
    "No dark-matter exclusion claim.",
    "No Lambda-CDM replacement claim.",
    "No MOND/RAR defeat claim.",
    "No Bullet-Cluster explanation claim.",
    "No physical proof of a TVC mechanism.",
    "No Hubble-tension solution claim.",
    "Curve-level null-refit diagnostic only.",
    "No universal fixed-exponent law claim.",
]

DESTRUCTIVE_NULLS = {
    "constant_floor",
    "reversed_rrf_nfixed",
    "shuffled_radius_rrf_nfixed",
    "outer_step_median",
}

NEIGHBOR_NULLS = {
    "saturating_n1",
    "saturating_n2",
    "saturating_n4",
    "saturating_n6",
    "saturating_n8",
    "exp_saturating",
    "arctan_saturating",
}

LOCKED_KERNEL = "locked_rrf_nfixed"


@dataclass
class Curve:
    galaxy: str
    r: np.ndarray
    vobs: np.ndarray
    evobs: np.ndarray
    vgas: np.ndarray
    vdisk: np.ndarray
    vbul: np.ndarray
    path: str


def sanitize_name(name: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "", str(name)).lower()


def load_rotmod(path: Path, galaxy: str) -> Optional[Curve]:
    try:
        arr = np.loadtxt(path, comments="#")
    except Exception:
        return None
    if arr.ndim == 1:
        arr = arr.reshape(1, -1)
    if arr.shape[0] < 5 or arr.shape[1] < 5:
        return None
    r = arr[:, 0].astype(float)
    vobs = arr[:, 1].astype(float)
    evobs = arr[:, 2].astype(float)
    vgas = arr[:, 3].astype(float)
    vdisk = arr[:, 4].astype(float)
    vbul = arr[:, 5].astype(float) if arr.shape[1] >= 6 else np.zeros_like(r)
    m = np.isfinite(r) & np.isfinite(vobs) & np.isfinite(evobs) & np.isfinite(vgas) & np.isfinite(vdisk) & np.isfinite(vbul)
    m &= (r > 0) & (vobs > 0)
    r, vobs, evobs, vgas, vdisk, vbul = r[m], vobs[m], evobs[m], vgas[m], vdisk[m], vbul[m]
    if len(r) < 5:
        return None
    # Conservative error floor to avoid overweighting tiny tabulated errors.
    finite_err = evobs[np.isfinite(evobs) & (evobs > 0)]
    floor = max(1.0, float(np.nanmedian(finite_err)) * 0.25) if len(finite_err) else 1.0
    evobs = np.where(np.isfinite(evobs) & (evobs > 0), evobs, floor)
    evobs = np.maximum(evobs, floor)
    order = np.argsort(r)
    return Curve(galaxy, r[order], vobs[order], evobs[order], vgas[order], vdisk[order], vbul[order], str(path))


def find_rotmod_file(row: pd.Series, rotmod_dir: Path) -> Optional[Path]:
    galaxy = str(row.get("galaxy", "")).strip()
    # Prefer exact resolved path from prior Stage 13R if still valid.
    for col in ["resolved_rotmod_file", "source_file"]:
        val = row.get(col, None)
        if isinstance(val, str) and val and val.lower() != "nan":
            p = Path(val)
            if p.exists():
                return p
            # If absolute WSL path changed, try basename under current rotmod_dir.
            q = rotmod_dir / p.name
            if q.exists():
                return q
    if not rotmod_dir.exists():
        return None
    sg = sanitize_name(galaxy)
    candidates = []
    for p in rotmod_dir.glob("*"):
        if not p.is_file():
            continue
        sp = sanitize_name(p.stem)
        if sg and (sg == sp or sg in sp or sp in sg):
            candidates.append(p)
    if candidates:
        # Prefer files with rotmod in name, then shortest stem.
        candidates.sort(key=lambda p: ("rotmod" not in p.name.lower(), len(p.name)))
        return candidates[0]
    return None


def kernel_values(kind: str, r: np.ndarray, rc: float, n_fixed: float, rng: np.random.Generator, galaxy_key: str) -> np.ndarray:
    x = np.maximum(r / max(rc, 1e-12), 1e-12)
    if kind == LOCKED_KERNEL:
        k = x ** n_fixed / (1.0 + x ** n_fixed)
    elif kind.startswith("saturating_n"):
        n = float(kind.replace("saturating_n", ""))
        k = x ** n / (1.0 + x ** n)
    elif kind == "exp_saturating":
        k = 1.0 - np.exp(-x)
    elif kind == "arctan_saturating":
        k = (2.0 / np.pi) * np.arctan(x)
    elif kind == "constant_floor":
        k = np.ones_like(r)
    elif kind == "reversed_rrf_nfixed":
        base = x ** n_fixed / (1.0 + x ** n_fixed)
        k = 1.0 - base
    elif kind == "outer_step_median":
        k = (r >= np.median(r)).astype(float)
    elif kind == "shuffled_radius_rrf_nfixed":
        base = x ** n_fixed / (1.0 + x ** n_fixed)
        # Deterministic per galaxy and rc bucket. This preserves values but breaks radius ordering.
        local_seed = abs(hash((galaxy_key, int(round(math.log10(max(rc, 1e-9)) * 1000))))) % (2**32)
        lrng = np.random.default_rng(local_seed)
        idx = np.arange(len(base))
        lrng.shuffle(idx)
        k = base[idx]
    else:
        raise ValueError(f"unknown kernel kind: {kind}")
    return np.asarray(k, dtype=float)


def fit_kernel(curve: Curve, kind: str, n_fixed: float, ups_d: float, ups_b: float, rc_grid_size: int, seed: int) -> Dict[str, float | str | int]:
    r, vobs, ev = curve.r, curve.vobs, curve.evobs
    # SPARC convention: gas contribution may be signed; use Vgas*abs(Vgas) for squared contribution.
    vbar2 = curve.vgas * np.abs(curve.vgas) + ups_d * curve.vdisk**2 + ups_b * curve.vbul**2
    y = vobs**2 - vbar2
    sigma_y = np.maximum(2.0 * np.maximum(vobs, 1.0) * ev, 1.0)
    w = 1.0 / np.maximum(sigma_y**2, 1e-12)
    valid = np.isfinite(y) & np.isfinite(w) & (w > 0)
    y, w, r = y[valid], w[valid], r[valid]
    if len(y) < 5:
        return {"kernel": kind, "fit_ok": 0, "aic_v2": np.nan, "chi2_v2": np.nan, "A_kms2": np.nan, "rc_kpc": np.nan, "k_params": np.nan}
    rng = np.random.default_rng(seed)
    if kind in {"constant_floor", "outer_step_median"}:
        rc_grid = np.array([np.nan])
    else:
        rmin = max(float(np.nanmin(r)) / 3.0, 1e-4)
        rmax = max(float(np.nanmax(r)) * 3.0, rmin * 10.0)
        rc_grid = np.geomspace(rmin, rmax, int(rc_grid_size))
    best = None
    for rc in rc_grid:
        rc_eff = float(np.nanmedian(r)) if not np.isfinite(rc) else float(rc)
        k = kernel_values(kind, r, rc_eff, n_fixed, rng, curve.galaxy)
        denom = float(np.sum(w * k * k))
        if not np.isfinite(denom) or denom <= 0:
            continue
        A = float(np.sum(w * k * y) / denom)
        # Restrict to non-negative residual-response amplitude for all families.
        A = max(0.0, A)
        resid = y - A * k
        chi2 = float(np.sum(w * resid * resid))
        if kind in {"constant_floor", "outer_step_median"}:
            k_params = 1
        else:
            k_params = 2
        aic = chi2 + 2.0 * k_params
        rec = (aic, chi2, A, rc_eff, k_params)
        if best is None or aic < best[0]:
            best = rec
    if best is None:
        return {"kernel": kind, "fit_ok": 0, "aic_v2": np.nan, "chi2_v2": np.nan, "A_kms2": np.nan, "rc_kpc": np.nan, "k_params": np.nan}
    aic, chi2, A, rc, k_params = best
    return {"kernel": kind, "fit_ok": 1, "aic_v2": aic, "chi2_v2": chi2, "A_kms2": A, "rc_kpc": rc, "k_params": k_params}


def frac(series: pd.Series, condition) -> float:
    if len(series) == 0:
        return float("nan")
    return float(np.mean(condition(series)))


def summarize_group(df: pd.DataFrame, label: str) -> Dict[str, object]:
    if len(df) == 0:
        return {"class": label, "count": 0}
    return {
        "class": label,
        "count": int(len(df)),
        "median_delta_aic_rrf_minus_best_destructive_null": float(np.nanmedian(df["delta_aic_rrf_minus_best_destructive_null"])),
        "rrf_beats_best_destructive_null_fraction": float(np.nanmean(df["delta_aic_rrf_minus_best_destructive_null"] < 0)),
        "rrf_strongly_beats_best_destructive_null_fraction": float(np.nanmean(df["delta_aic_rrf_minus_best_destructive_null"] <= -10)),
        "median_delta_aic_rrf_minus_best_neighbor_null": float(np.nanmedian(df["delta_aic_rrf_minus_best_neighbor_null"])),
        "rrf_beats_best_neighbor_null_fraction": float(np.nanmean(df["delta_aic_rrf_minus_best_neighbor_null"] < 0)),
        "median_curve_level_rrf_A_kms2": float(np.nanmedian(df["curve_level_rrf_A_kms2"])),
        "median_curve_level_rrf_rc_kpc": float(np.nanmedian(df["curve_level_rrf_rc_kpc"])),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--population-table", required=True)
    ap.add_argument("--rotmod-dir", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--seed", type=int, default=20260516)
    ap.add_argument("--n-fixed", type=float, default=3.258993)
    ap.add_argument("--ups-d", type=float, default=0.5)
    ap.add_argument("--ups-b", type=float, default=0.7)
    ap.add_argument("--rc-grid-size", type=int, default=140)
    ap.add_argument("--max-galaxies", type=int, default=0)
    args = ap.parse_args()

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    pop_path = Path(args.population_table)
    rotmod_dir = Path(args.rotmod_dir)
    if not pop_path.exists():
        raise FileNotFoundError(f"population table not found: {pop_path}")
    pop = pd.read_csv(pop_path)
    if "galaxy" not in pop.columns:
        raise ValueError("population table must contain a 'galaxy' column")
    if args.max_galaxies and args.max_galaxies > 0:
        pop = pop.head(args.max_galaxies).copy()

    kernels = [
        LOCKED_KERNEL,
        "constant_floor",
        "reversed_rrf_nfixed",
        "shuffled_radius_rrf_nfixed",
        "outer_step_median",
        "saturating_n1",
        "saturating_n2",
        "saturating_n4",
        "saturating_n6",
        "saturating_n8",
        "exp_saturating",
        "arctan_saturating",
    ]

    by_kernel_rows: List[Dict[str, object]] = []
    by_galaxy_rows: List[Dict[str, object]] = []
    missing: List[str] = []

    for _, row in pop.iterrows():
        galaxy = str(row["galaxy"])
        p = find_rotmod_file(row, rotmod_dir)
        if p is None:
            missing.append(galaxy)
            continue
        curve = load_rotmod(p, galaxy)
        if curve is None:
            missing.append(galaxy)
            continue
        fit_recs: Dict[str, Dict[str, object]] = {}
        for kind in kernels:
            rec = fit_kernel(curve, kind, args.n_fixed, args.ups_d, args.ups_b, args.rc_grid_size, args.seed)
            rec.update({
                "galaxy": galaxy,
                "stage8_class": row.get("stage8_class", "UNKNOWN"),
                "rotmod_file": curve.path,
                "n_points": int(len(curve.r)),
            })
            fit_recs[kind] = rec
            by_kernel_rows.append(rec)
        rrf = fit_recs[LOCKED_KERNEL]
        if not int(rrf.get("fit_ok", 0)):
            continue
        destructive = [fit_recs[k] for k in DESTRUCTIVE_NULLS if k in fit_recs and int(fit_recs[k].get("fit_ok", 0))]
        neighbors = [fit_recs[k] for k in NEIGHBOR_NULLS if k in fit_recs and int(fit_recs[k].get("fit_ok", 0))]
        best_dest = min(destructive, key=lambda d: float(d["aic_v2"])) if destructive else None
        best_nei = min(neighbors, key=lambda d: float(d["aic_v2"])) if neighbors else None
        by_galaxy_rows.append({
            "galaxy": galaxy,
            "stage8_class": row.get("stage8_class", "UNKNOWN"),
            "n_points": int(len(curve.r)),
            "rotmod_file": curve.path,
            "rrf_aic_v2": float(rrf["aic_v2"]),
            "curve_level_rrf_A_kms2": float(rrf["A_kms2"]),
            "curve_level_rrf_rc_kpc": float(rrf["rc_kpc"]),
            "best_destructive_null": best_dest["kernel"] if best_dest else "NONE",
            "best_destructive_null_aic_v2": float(best_dest["aic_v2"]) if best_dest else np.nan,
            "delta_aic_rrf_minus_best_destructive_null": float(rrf["aic_v2"] - best_dest["aic_v2"]) if best_dest else np.nan,
            "best_neighbor_null": best_nei["kernel"] if best_nei else "NONE",
            "best_neighbor_null_aic_v2": float(best_nei["aic_v2"]) if best_nei else np.nan,
            "delta_aic_rrf_minus_best_neighbor_null": float(rrf["aic_v2"] - best_nei["aic_v2"]) if best_nei else np.nan,
        })

    by_kernel = pd.DataFrame(by_kernel_rows)
    by_galaxy = pd.DataFrame(by_galaxy_rows)
    by_kernel.to_csv(out / "stage26_null_kernel_fit_by_galaxy_kernel.csv", index=False)
    by_galaxy.to_csv(out / "stage26_null_kernel_by_galaxy.csv", index=False)
    pd.DataFrame({"missing_or_unreadable_galaxy": missing}).to_csv(out / "stage26_missing_or_unreadable_rotmod.csv", index=False)

    valid_count = int(len(by_galaxy))
    class_summaries = []
    if valid_count:
        class_summaries.append(summarize_group(by_galaxy, "ALL"))
        for cls, sub in by_galaxy.groupby("stage8_class"):
            class_summaries.append(summarize_group(sub, str(cls)))
    class_df = pd.DataFrame(class_summaries)
    class_df.to_csv(out / "stage26_class_null_refit_summary.csv", index=False)

    if valid_count:
        median_dest = float(np.nanmedian(by_galaxy["delta_aic_rrf_minus_best_destructive_null"]))
        beat_dest_frac = float(np.nanmean(by_galaxy["delta_aic_rrf_minus_best_destructive_null"] < 0))
        strong_dest_frac = float(np.nanmean(by_galaxy["delta_aic_rrf_minus_best_destructive_null"] <= -10))
        median_neighbor = float(np.nanmedian(by_galaxy["delta_aic_rrf_minus_best_neighbor_null"]))
        beat_neighbor_frac = float(np.nanmean(by_galaxy["delta_aic_rrf_minus_best_neighbor_null"] < 0))
        robust = by_galaxy[by_galaxy["stage8_class"] == "ROBUST-DIAGNOSTIC-CANDIDATE"]
        robust_beat_dest = float(np.nanmean(robust["delta_aic_rrf_minus_best_destructive_null"] < 0)) if len(robust) else float("nan")
    else:
        median_dest = beat_dest_frac = strong_dest_frac = median_neighbor = beat_neighbor_frac = robust_beat_dest = float("nan")

    guards = {
        "valid_population_count_ge_100": int(valid_count >= 100),
        "rrf_beats_best_destructive_null_fraction_ge_0_70": int(np.isfinite(beat_dest_frac) and beat_dest_frac >= 0.70),
        "median_delta_aic_rrf_minus_best_destructive_null_le_minus_10": int(np.isfinite(median_dest) and median_dest <= -10.0),
        "robust_rrf_beats_best_destructive_null_fraction_ge_0_75": int(np.isfinite(robust_beat_dest) and robust_beat_dest >= 0.75),
        "rotmod_missing_fraction_le_0_10": int((len(missing) / max(len(pop), 1)) <= 0.10),
    }
    guard_pass_count = int(sum(guards.values()))
    guard_count = int(len(guards))

    if guard_pass_count == guard_count:
        if np.isfinite(beat_neighbor_frac) and beat_neighbor_frac >= 0.55 and np.isfinite(median_neighbor) and median_neighbor <= 0:
            decision = "AUTHORIZE-STAGE27-CURVE-LEVEL-NULL-REFIT-SYNTHESIS"
        else:
            decision = "WEAK-AUTHORIZE-STAGE27-DESTRUCTIVE-NULLS-PASSED-NEIGHBOR-KERNELS-COMPETE"
    elif valid_count >= 100 and beat_dest_frac >= 0.60:
        decision = "WEAK-HOLD-STAGE26-PARTIAL-DESTRUCTIVE-NULL-SEPARATION"
    else:
        decision = "HOLD-STAGE26-CURVE-LEVEL-NULL-REFIT-NOT-SUPPORTED"

    summary = {
        "stage": "STAGE26-CURVE-LEVEL-NULL-REFIT-CONTROLS",
        "valid_population_count": valid_count,
        "input_population_count": int(len(pop)),
        "missing_or_unreadable_count": int(len(missing)),
        "fixed_n": args.n_fixed,
        "fixed_ups_d": args.ups_d,
        "fixed_ups_b": args.ups_b,
        "fit_space": "squared_velocity_residual_weighted_least_squares",
        "locked_kernel": LOCKED_KERNEL,
        "destructive_nulls": sorted(DESTRUCTIVE_NULLS),
        "neighbor_nulls": sorted(NEIGHBOR_NULLS),
        "main_results": {
            "median_delta_aic_rrf_minus_best_destructive_null": median_dest,
            "rrf_beats_best_destructive_null_fraction": beat_dest_frac,
            "rrf_strongly_beats_best_destructive_null_fraction": strong_dest_frac,
            "robust_rrf_beats_best_destructive_null_fraction": robust_beat_dest,
            "median_delta_aic_rrf_minus_best_neighbor_null": median_neighbor,
            "rrf_beats_best_neighbor_null_fraction": beat_neighbor_frac,
        },
        "guards": guards,
        "guard_pass_count": guard_pass_count,
        "guard_count": guard_count,
        "decision": decision,
        "claim_boundary": CLAIM_BOUNDARY,
    }
    (out / "stage26_curve_level_null_refit_summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (out / "DECISION_STAGE26.txt").write_text(decision + "\n", encoding="utf-8")

    report = f"""# Stage 26 Curve-Level Null-Refit Controls

## Decision

`{decision}`

## Purpose

Stage 26 refits curve-level squared-velocity residuals directly against the locked SN-RRF/A10-TVC-RRF kernel and adversarial null kernels.

This is a diagnostic control only. It is not a physical model fit and does not reproduce the earlier nonlinear velocity-space audit exactly.

## Inputs

- population table: `{args.population_table}`
- Rotmod directory: `{args.rotmod_dir}`
- fixed exponent: `{args.n_fixed}`
- fixed stellar mass-to-light values: `ups_d={args.ups_d}`, `ups_b={args.ups_b}`

## Main results

- input_population_count: {len(pop)}
- valid_population_count: {valid_count}
- missing_or_unreadable_count: {len(missing)}
- median Delta AIC(RRF - best destructive null): {median_dest:.6g}
- RRF beats best destructive null fraction: {beat_dest_frac:.6g}
- RRF strongly beats best destructive null fraction, Delta AIC <= -10: {strong_dest_frac:.6g}
- robust-class RRF beats best destructive null fraction: {robust_beat_dest:.6g}
- median Delta AIC(RRF - best neighbor monotone null): {median_neighbor:.6g}
- RRF beats best neighbor monotone null fraction: {beat_neighbor_frac:.6g}
- guard_pass_count: {guard_pass_count}/{guard_count}

## Interpretation guide

If destructive nulls are beaten, Stage 26 supports a curve-level radial-response shape signal.

If neighboring monotone kernels compete, the correct repair is not to claim fixed-exponent uniqueness. The safer interpretation is that SN-RRF identifies a scale-normalized residual-response family, with the locked exponent acting as one useful representative kernel.

## Claim boundary

"""
    for item in CLAIM_BOUNDARY:
        report += f"- {item}\n"
    report += "\n## Output files\n\n"
    report += "- `DECISION_STAGE26.txt`\n"
    report += "- `stage26_curve_level_null_refit_summary.json`\n"
    report += "- `stage26_null_kernel_by_galaxy.csv`\n"
    report += "- `stage26_null_kernel_fit_by_galaxy_kernel.csv`\n"
    report += "- `stage26_class_null_refit_summary.csv`\n"
    report += "- `stage26_missing_or_unreadable_rotmod.csv`\n"
    (out / "stage26_curve_level_null_refit_report.md").write_text(report, encoding="utf-8")

    print(decision)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

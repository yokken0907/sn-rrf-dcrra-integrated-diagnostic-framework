#!/usr/bin/env python3
"""Stage 30 kernel-family continuum profile audit.

This script extends Stage 26/28 by scanning a continuous family of monotone saturating
kernels K_n(x)=x^n/(1+x^n). It is a diagnostic-only profile, not a physical model fit.
"""
from __future__ import annotations

import argparse, json, math, re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional

import numpy as np
import pandas as pd

CLAIM_BOUNDARY = [
    "No dark-matter exclusion claim.",
    "No Lambda-CDM replacement claim.",
    "No MOND/RAR defeat claim.",
    "No Bullet-Cluster explanation claim.",
    "No physical proof of a TVC mechanism.",
    "No Hubble-tension solution claim.",
    "Kernel-continuum diagnostic only.",
    "No universal fixed-exponent law claim.",
]

LOCKED_N = 3.258993

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
    finite_err = evobs[np.isfinite(evobs) & (evobs > 0)]
    floor = max(1.0, float(np.nanmedian(finite_err)) * 0.25) if len(finite_err) else 1.0
    evobs = np.where(np.isfinite(evobs) & (evobs > 0), evobs, floor)
    evobs = np.maximum(evobs, floor)
    order = np.argsort(r)
    return Curve(galaxy, r[order], vobs[order], evobs[order], vgas[order], vdisk[order], vbul[order], str(path))


def find_rotmod_file(row: pd.Series, rotmod_dir: Path) -> Optional[Path]:
    galaxy = str(row.get("galaxy", "")).strip()
    for col in ["resolved_rotmod_file", "source_file"]:
        val = row.get(col, None)
        if isinstance(val, str) and val and val.lower() != "nan":
            p = Path(val)
            if p.exists():
                return p
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
        candidates.sort(key=lambda p: ("rotmod" not in p.name.lower(), len(p.name)))
        return candidates[0]
    return None


def saturating_kernel(r: np.ndarray, rc: float, n: float) -> np.ndarray:
    x = np.maximum(r / max(float(rc), 1e-12), 1e-12)
    # Avoid overflow for large n*log(x); clipping is sufficient for stable saturated values.
    z = np.clip(float(n) * np.log(x), -60.0, 60.0)
    xn = np.exp(z)
    return xn / (1.0 + xn)


def fit_saturating_n(curve: Curve, n: float, ups_d: float, ups_b: float, rc_grid_size: int) -> Dict[str, float]:
    r, vobs, ev = curve.r, curve.vobs, curve.evobs
    vbar2 = curve.vgas * np.abs(curve.vgas) + ups_d * curve.vdisk**2 + ups_b * curve.vbul**2
    y = vobs**2 - vbar2
    sigma_y = np.maximum(2.0 * np.maximum(vobs, 1.0) * ev, 1.0)
    w = 1.0 / np.maximum(sigma_y**2, 1e-12)
    valid = np.isfinite(y) & np.isfinite(w) & (w > 0) & np.isfinite(r) & (r > 0)
    y, w, r = y[valid], w[valid], r[valid]
    if len(y) < 5:
        return {"fit_ok": 0, "aic_v2": np.nan, "chi2_v2": np.nan, "A_kms2": np.nan, "rc_kpc": np.nan}
    rmin = max(float(np.nanmin(r)) / 3.0, 1e-4)
    rmax = max(float(np.nanmax(r)) * 3.0, rmin * 10.0)
    rc_grid = np.geomspace(rmin, rmax, int(rc_grid_size))
    best = None
    for rc in rc_grid:
        k = saturating_kernel(r, rc, n)
        denom = float(np.sum(w * k * k))
        if not np.isfinite(denom) or denom <= 0:
            continue
        A = float(np.sum(w * k * y) / denom)
        A = max(0.0, A)
        resid = y - A * k
        chi2 = float(np.sum(w * resid * resid))
        # A and rc are fitted for each fixed n; n is profiled externally and is not counted per grid point.
        aic = chi2 + 2.0 * 2
        rec = (aic, chi2, A, float(rc))
        if best is None or aic < best[0]:
            best = rec
    if best is None:
        return {"fit_ok": 0, "aic_v2": np.nan, "chi2_v2": np.nan, "A_kms2": np.nan, "rc_kpc": np.nan}
    aic, chi2, A, rc = best
    return {"fit_ok": 1, "aic_v2": aic, "chi2_v2": chi2, "A_kms2": A, "rc_kpc": rc}


def parse_n_grid(spec: str, locked_n: float) -> List[float]:
    vals: List[float] = []
    for part in spec.split(','):
        part = part.strip()
        if not part:
            continue
        if ':' in part:
            bits = [float(x) for x in part.split(':')]
            if len(bits) != 3:
                raise ValueError(f"bad n-grid range: {part}")
            start, stop, step = bits
            x = start
            while x <= stop + 1e-12:
                vals.append(round(x, 10))
                x += step
        else:
            vals.append(float(part))
    vals.append(float(locked_n))
    vals = sorted(set(round(float(v), 10) for v in vals if np.isfinite(v) and v > 0))
    return vals


def summarize_class(df: pd.DataFrame, label: str) -> Dict[str, object]:
    if len(df) == 0:
        return {"class": label, "count": 0}
    d = df["delta_aic_locked_minus_best_continuum"].astype(float)
    return {
        "class": label,
        "count": int(len(df)),
        "median_best_n": float(np.nanmedian(df["best_n"])),
        "q25_best_n": float(np.nanquantile(df["best_n"], 0.25)),
        "q75_best_n": float(np.nanquantile(df["best_n"], 0.75)),
        "median_delta_aic_locked_minus_best_continuum": float(np.nanmedian(d)),
        "locked_within_2_fraction": float(np.nanmean(d <= 2.0)),
        "locked_within_10_fraction": float(np.nanmean(d <= 10.0)),
        "locked_best_fraction": float(np.nanmean(np.isclose(df["best_n"], LOCKED_N, rtol=0, atol=1e-8))),
        "best_n_le_2_fraction": float(np.nanmean(df["best_n"] <= 2.0)),
        "best_n_ge_6_fraction": float(np.nanmean(df["best_n"] >= 6.0)),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--population-table", required=True)
    ap.add_argument("--rotmod-dir", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--n-grid", default="0.5:10.0:0.25,12.0")
    ap.add_argument("--locked-n", type=float, default=LOCKED_N)
    ap.add_argument("--ups-d", type=float, default=0.5)
    ap.add_argument("--ups-b", type=float, default=0.7)
    ap.add_argument("--rc-grid-size", type=int, default=120)
    ap.add_argument("--max-galaxies", type=int, default=0)
    args = ap.parse_args()

    out = Path(args.out); out.mkdir(parents=True, exist_ok=True)
    pop = pd.read_csv(args.population_table)
    if args.max_galaxies and args.max_galaxies > 0:
        pop = pop.head(args.max_galaxies).copy()
    rotmod_dir = Path(args.rotmod_dir)
    n_grid = parse_n_grid(args.n_grid, args.locked_n)

    by_n_rows: List[Dict[str, object]] = []
    by_gal_rows: List[Dict[str, object]] = []
    missing: List[str] = []
    locked_n = float(args.locked_n)

    for _, row in pop.iterrows():
        galaxy = str(row.get("galaxy", ""))
        p = find_rotmod_file(row, rotmod_dir)
        if p is None:
            missing.append(galaxy)
            continue
        curve = load_rotmod(p, galaxy)
        if curve is None:
            missing.append(galaxy)
            continue
        fits = []
        for n in n_grid:
            rec = fit_saturating_n(curve, n, args.ups_d, args.ups_b, args.rc_grid_size)
            rec.update({
                "galaxy": galaxy,
                "stage8_class": row.get("stage8_class", "UNKNOWN"),
                "n_grid": float(n),
                "rotmod_file": curve.path,
                "n_points": int(len(curve.r)),
            })
            by_n_rows.append(rec)
            if int(rec.get("fit_ok", 0)):
                fits.append(rec)
        if not fits:
            continue
        best = min(fits, key=lambda x: float(x["aic_v2"]))
        locked_candidates = [x for x in fits if abs(float(x["n_grid"]) - locked_n) < 1e-8]
        locked = locked_candidates[0] if locked_candidates else min(fits, key=lambda x: abs(float(x["n_grid"]) - locked_n))
        delta = float(locked["aic_v2"] - best["aic_v2"])
        # rough width: count how many grid values are within +2/+10 of best
        aics = np.array([float(x["aic_v2"]) for x in fits], dtype=float)
        by_gal_rows.append({
            "galaxy": galaxy,
            "stage8_class": row.get("stage8_class", "UNKNOWN"),
            "n_points": int(len(curve.r)),
            "best_n": float(best["n_grid"]),
            "best_aic_v2": float(best["aic_v2"]),
            "best_A_kms2": float(best["A_kms2"]),
            "best_rc_kpc": float(best["rc_kpc"]),
            "locked_n": locked_n,
            "locked_aic_v2": float(locked["aic_v2"]),
            "locked_A_kms2": float(locked["A_kms2"]),
            "locked_rc_kpc": float(locked["rc_kpc"]),
            "delta_aic_locked_minus_best_continuum": delta,
            "locked_within_2_of_best": int(delta <= 2.0),
            "locked_within_10_of_best": int(delta <= 10.0),
            "grid_count_within_2_of_best": int(np.sum((aics - float(best["aic_v2"])) <= 2.0)),
            "grid_count_within_10_of_best": int(np.sum((aics - float(best["aic_v2"])) <= 10.0)),
        })

    by_n = pd.DataFrame(by_n_rows)
    by_gal = pd.DataFrame(by_gal_rows)
    by_n.to_csv(out/"stage30_continuum_fit_by_galaxy_n.csv", index=False)
    by_gal.to_csv(out/"stage30_continuum_by_galaxy.csv", index=False)
    pd.DataFrame({"missing_or_unreadable_galaxy": missing}).to_csv(out/"stage30_missing_or_unreadable_rotmod.csv", index=False)

    # n-grid profile: for each n, median delta vs galaxy-level best and rank-like summaries.
    n_profile_rows = []
    if len(by_n) and len(by_gal):
        best_map = by_gal.set_index("galaxy")["best_aic_v2"].to_dict()
        tmp = by_n.copy()
        tmp["best_aic_v2"] = tmp["galaxy"].map(best_map)
        tmp["delta_aic_n_minus_best"] = tmp["aic_v2"] - tmp["best_aic_v2"]
        for n, sub in tmp.groupby("n_grid"):
            d = sub["delta_aic_n_minus_best"].astype(float)
            n_profile_rows.append({
                "n_grid": float(n),
                "available_count": int(d.notna().sum()),
                "median_delta_aic_n_minus_best": float(np.nanmedian(d)),
                "within_2_fraction": float(np.nanmean(d <= 2.0)),
                "within_10_fraction": float(np.nanmean(d <= 10.0)),
                "best_fraction": float(np.nanmean(d <= 1e-9)),
            })
    n_profile = pd.DataFrame(n_profile_rows).sort_values("median_delta_aic_n_minus_best") if n_profile_rows else pd.DataFrame()
    n_profile.to_csv(out/"stage30_n_grid_profile.csv", index=False)

    class_rows = []
    if len(by_gal):
        class_rows.append(summarize_class(by_gal, "ALL"))
        for cls, sub in by_gal.groupby("stage8_class"):
            class_rows.append(summarize_class(sub, str(cls)))
    class_df = pd.DataFrame(class_rows)
    class_df.to_csv(out/"stage30_class_continuum_summary.csv", index=False)

    valid = int(len(by_gal))
    if valid:
        d = by_gal["delta_aic_locked_minus_best_continuum"].astype(float)
        locked_within_2 = float(np.nanmean(d <= 2.0))
        locked_within_10 = float(np.nanmean(d <= 10.0))
        median_delta = float(np.nanmedian(d))
        best_n_median = float(np.nanmedian(by_gal["best_n"]))
        best_n_q25 = float(np.nanquantile(by_gal["best_n"], 0.25))
        best_n_q75 = float(np.nanquantile(by_gal["best_n"], 0.75))
        best_n_iqr = best_n_q75 - best_n_q25
        top_best_counts = {str(k): int(v) for k, v in by_gal["best_n"].value_counts().head(10).items()}
    else:
        locked_within_2 = locked_within_10 = median_delta = best_n_median = best_n_q25 = best_n_q75 = best_n_iqr = float("nan")
        top_best_counts = {}

    # Guard logic: we expect heterogeneity; this is not a fixed-exponent rescue.
    guards = {
        "valid_population_count_ge_100": int(valid >= 100),
        "continuum_grid_count_ge_25": int(len(n_grid) >= 25),
        "locked_not_universal_best_fraction_le_0_50": int(valid > 0 and float(np.mean(np.isclose(by_gal["best_n"], locked_n, atol=1e-8))) <= 0.50),
        "continuum_improves_or_competes_median_delta_locked_minus_best_ge_2": int(np.isfinite(median_delta) and median_delta >= 2.0),
        "best_n_distribution_heterogeneous_iqr_ge_1": int(np.isfinite(best_n_iqr) and best_n_iqr >= 1.0),
        "rotmod_missing_fraction_le_0_10": int((len(missing)/max(len(pop),1)) <= 0.10),
    }
    guard_pass_count = int(sum(guards.values()))
    guard_count = int(len(guards))
    if guard_pass_count == guard_count:
        decision = "AUTHORIZE-STAGE31-SN-RRF-CONTINUUM-FAMILY-SYNTHESIS"
    elif valid >= 100 and guard_pass_count >= 4:
        decision = "WEAK-AUTHORIZE-STAGE31-SN-RRF-CONTINUUM-FAMILY-SYNTHESIS"
    else:
        decision = "HOLD-STAGE30-KERNEL-CONTINUUM-PROFILE-INCONCLUSIVE"

    summary = {
        "stage": "STAGE30-KERNEL-FAMILY-CONTINUUM-PROFILE-AUDIT",
        "valid_population_count": valid,
        "input_population_count": int(len(pop)),
        "missing_or_unreadable_count": int(len(missing)),
        "n_grid_count": int(len(n_grid)),
        "n_grid_min": float(min(n_grid)) if n_grid else None,
        "n_grid_max": float(max(n_grid)) if n_grid else None,
        "locked_n": locked_n,
        "main_results": {
            "best_n_median": best_n_median,
            "best_n_q25": best_n_q25,
            "best_n_q75": best_n_q75,
            "best_n_iqr": best_n_iqr,
            "median_delta_aic_locked_minus_best_continuum": median_delta,
            "locked_within_2_fraction": locked_within_2,
            "locked_within_10_fraction": locked_within_10,
            "top_best_n_counts": top_best_counts,
        },
        "guards": guards,
        "guard_pass_count": guard_pass_count,
        "guard_count": guard_count,
        "decision": decision,
        "claim_boundary": CLAIM_BOUNDARY,
    }
    (out/"stage30_kernel_continuum_summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
    (out/"DECISION_STAGE30.txt").write_text(decision+"\n", encoding="utf-8")

    report = f"""# Stage 30 Kernel-Family Continuum Profile Audit

## Decision

`{decision}`

## Purpose

Stage 30 scans a continuous grid of saturating kernels

```text
K_n(x) = x^n / (1 + x^n)
```

to test whether SN-RRF should be treated as a scale-normalized residual-response family rather than as a unique fixed-exponent law.

## Inputs

- population table: `{args.population_table}`
- Rotmod directory: `{args.rotmod_dir}`
- locked n: `{locked_n}`
- n grid count: `{len(n_grid)}`
- fixed stellar mass-to-light values: `ups_d={args.ups_d}`, `ups_b={args.ups_b}`

## Main results

- input_population_count: {len(pop)}
- valid_population_count: {valid}
- missing_or_unreadable_count: {len(missing)}
- best_n median: {best_n_median:.6g}
- best_n IQR: [{best_n_q25:.6g}, {best_n_q75:.6g}]
- median Delta AIC(locked n - best continuum n): {median_delta:.6g}
- locked within +2 AIC of continuum best fraction: {locked_within_2:.6g}
- locked within +10 AIC of continuum best fraction: {locked_within_10:.6g}
- guard_pass_count: {guard_pass_count}/{guard_count}

## Interpretation guide

If the best exponent varies across galaxies and the locked exponent is not uniquely favored, the safe conclusion is not fixed-exponent uniqueness. The safe conclusion is that SN-RRF is a heterogeneous scale-normalized monotone-saturating residual-response family.

## Claim boundary

"""
    for item in CLAIM_BOUNDARY:
        report += f"- {item}\n"
    report += "\n## Output files\n\n"
    for name in [
        "DECISION_STAGE30.txt",
        "stage30_kernel_continuum_summary.json",
        "stage30_continuum_by_galaxy.csv",
        "stage30_continuum_fit_by_galaxy_n.csv",
        "stage30_class_continuum_summary.csv",
        "stage30_n_grid_profile.csv",
        "stage30_kernel_continuum_report.md",
        "stage30_missing_or_unreadable_rotmod.csv",
    ]:
        report += f"- `{name}`\n"
    (out/"stage30_kernel_continuum_report.md").write_text(report, encoding="utf-8")
    print(decision)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

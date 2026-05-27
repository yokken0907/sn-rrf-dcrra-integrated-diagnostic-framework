#!/usr/bin/env python3
"""Stage 28 kernel-family profile audit.

This audit follows Stage 26/27. It profiles which monotone saturating kernels compete
with the locked n=3.258993 kernel. It is diagnostic-only and does not make a
fixed-exponent uniqueness claim.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
import numpy as np
import pandas as pd

CLAIM_BOUNDARY = [
    "No dark-matter exclusion claim.",
    "No Lambda-CDM replacement claim.",
    "No MOND/RAR defeat claim.",
    "No Bullet-Cluster explanation claim.",
    "No physical proof of a TVC mechanism.",
    "No Hubble-tension solution claim.",
    "Kernel-family profile diagnostic only.",
    "No universal fixed-exponent law claim.",
]
LOCKED = "locked_rrf_nfixed"
NEIGHBOR = ["saturating_n1","saturating_n2","saturating_n4","saturating_n6","saturating_n8","exp_saturating","arctan_saturating"]

def safe_float(x):
    try:
        if pd.isna(x): return None
        return float(x)
    except Exception:
        return None

def summarize_best_table(by_galaxy: pd.DataFrame):
    out = {}
    out["valid_population_count"] = int(len(by_galaxy))
    out["best_neighbor_counts"] = {str(k): int(v) for k,v in by_galaxy["best_neighbor_null"].value_counts().items()} if "best_neighbor_null" in by_galaxy else {}
    if "delta_aic_rrf_minus_best_neighbor_null" in by_galaxy:
        d = by_galaxy["delta_aic_rrf_minus_best_neighbor_null"].astype(float)
        out["median_delta_aic_rrf_minus_best_neighbor_null"] = float(np.nanmedian(d))
        out["rrf_beats_best_neighbor_null_fraction"] = float(np.nanmean(d < 0))
    class_rows = []
    if "stage8_class" in by_galaxy:
        for cls, sub in by_galaxy.groupby("stage8_class"):
            row = {"class": str(cls), "count": int(len(sub))}
            if "delta_aic_rrf_minus_best_neighbor_null" in sub:
                d = sub["delta_aic_rrf_minus_best_neighbor_null"].astype(float)
                row["median_delta_aic_rrf_minus_best_neighbor_null"] = float(np.nanmedian(d))
                row["rrf_beats_best_neighbor_null_fraction"] = float(np.nanmean(d < 0))
            if "best_neighbor_null" in sub:
                vc = sub["best_neighbor_null"].value_counts()
                row["top_best_neighbor_null"] = str(vc.index[0]) if len(vc) else "NONE"
                row["top_best_neighbor_fraction"] = float(vc.iloc[0] / len(sub)) if len(vc) else float("nan")
            class_rows.append(row)
    return out, pd.DataFrame(class_rows)

def summarize_full_kernel_table(by_kernel: pd.DataFrame):
    if by_kernel is None or len(by_kernel) == 0:
        return {"available": False}, pd.DataFrame()
    req = {"galaxy","kernel","aic_v2"}
    if not req.issubset(by_kernel.columns):
        return {"available": False, "reason": "required columns missing"}, pd.DataFrame()
    # Pivot AIC by galaxy/kernel.
    piv = by_kernel.pivot_table(index="galaxy", columns="kernel", values="aic_v2", aggfunc="min")
    if LOCKED not in piv.columns:
        return {"available": False, "reason": "locked kernel column missing"}, pd.DataFrame()
    rows = []
    for k in NEIGHBOR:
        if k not in piv.columns: continue
        delta = piv[LOCKED] - piv[k]
        rows.append({
            "neighbor_kernel": k,
            "available_count": int(delta.notna().sum()),
            "median_delta_aic_locked_minus_kernel": float(np.nanmedian(delta)),
            "locked_beats_kernel_fraction": float(np.nanmean(delta < 0)),
            "kernel_beats_locked_fraction": float(np.nanmean(delta > 0)),
            "abs_within_2_fraction": float(np.nanmean(np.abs(delta) <= 2)),
            "abs_within_10_fraction": float(np.nanmean(np.abs(delta) <= 10)),
        })
    df = pd.DataFrame(rows).sort_values("median_delta_aic_locked_minus_kernel") if rows else pd.DataFrame()
    if len(df):
        best_rep = str(df.iloc[0]["neighbor_kernel"])
        best_med = float(df.iloc[0]["median_delta_aic_locked_minus_kernel"])
    else:
        best_rep, best_med = "NONE", float("nan")
    summ = {
        "available": True,
        "kernel_count_profiled": int(len(df)),
        "best_neighbor_by_median_delta": best_rep,
        "best_neighbor_by_median_delta_value": best_med,
        "locked_kernel": LOCKED,
    }
    return summ, df

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--by-galaxy", required=True)
    ap.add_argument("--by-kernel", default="")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    out = Path(args.out); out.mkdir(parents=True, exist_ok=True)
    by_galaxy = pd.read_csv(args.by_galaxy)
    best_summary, class_df = summarize_best_table(by_galaxy)
    by_kernel = None
    if args.by_kernel and Path(args.by_kernel).exists():
        by_kernel = pd.read_csv(args.by_kernel)
    kernel_summary, kernel_df = summarize_full_kernel_table(by_kernel)
    if len(class_df): class_df.to_csv(out/"stage28_class_kernel_family_summary.csv", index=False)
    else: pd.DataFrame().to_csv(out/"stage28_class_kernel_family_summary.csv", index=False)
    if len(kernel_df): kernel_df.to_csv(out/"stage28_neighbor_kernel_profile.csv", index=False)
    else: pd.DataFrame().to_csv(out/"stage28_neighbor_kernel_profile.csv", index=False)

    # Decision logic.
    valid = best_summary.get("valid_population_count", 0)
    rrf_best_frac = best_summary.get("rrf_beats_best_neighbor_null_fraction", np.nan)
    if valid >= 100 and kernel_summary.get("available"):
        decision = "AUTHORIZE-STAGE29-SN-RRF-KERNEL-FAMILY-SYNTHESIS"
    elif valid >= 100:
        decision = "WEAK-AUTHORIZE-STAGE29-BEST-NEIGHBOR-ONLY-KERNEL-FAMILY-SYNTHESIS"
    else:
        decision = "HOLD-STAGE28-KERNEL-FAMILY-PROFILE-INSUFFICIENT"

    summary = {
        "stage": "STAGE28-KERNEL-FAMILY-PROFILE-AUDIT",
        "best_neighbor_table_summary": best_summary,
        "full_kernel_table_summary": kernel_summary,
        "decision": decision,
        "claim_boundary": CLAIM_BOUNDARY,
    }
    (out/"stage28_kernel_family_profile_summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
    (out/"DECISION_STAGE28.txt").write_text(decision+"\n", encoding="utf-8")
    report = f"""# Stage 28 Kernel-Family Profile Audit

## Decision

`{decision}`

## Purpose

Stage 28 profiles the monotone saturating kernel family after Stage 26 showed that destructive nulls are beaten while neighboring monotone kernels compete.

## Main summary

- valid_population_count: {best_summary.get('valid_population_count')}
- median Delta AIC(locked RRF - best neighbor null): {best_summary.get('median_delta_aic_rrf_minus_best_neighbor_null')}
- locked RRF beats best neighbor null fraction: {best_summary.get('rrf_beats_best_neighbor_null_fraction')}
- full per-kernel table available: {kernel_summary.get('available')}

## Interpretation

If the full per-kernel table is available, this stage supports a family-level synthesis rather than fixed-exponent uniqueness. If only the best-neighbor table is available, this stage remains a weaker best-neighbor profile.

## Claim boundary

"""
    for x in CLAIM_BOUNDARY:
        report += f"- {x}\n"
    (out/"stage28_kernel_family_profile_report.md").write_text(report, encoding="utf-8")
    print(decision)
if __name__ == "__main__":
    main()

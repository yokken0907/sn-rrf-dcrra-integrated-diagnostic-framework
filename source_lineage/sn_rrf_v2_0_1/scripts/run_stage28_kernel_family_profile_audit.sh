#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
OUT="$ROOT/31_stage28_kernel_family_profile_audit/results/stage28_kernel_family_profile_audit"
mkdir -p "$OUT"
BY_GAL="$ROOT/29_stage26_curve_level_null_refit_controls/results/stage26_curve_level_null_refit_controls/stage26_null_kernel_by_galaxy.csv"
BY_KERNEL="$ROOT/29_stage26_curve_level_null_refit_controls/results/stage26_curve_level_null_refit_controls/stage26_null_kernel_fit_by_galaxy_kernel.csv"
# Fallback to uploaded result locations if the live Stage 26 output path is unavailable.
if [ ! -f "$BY_GAL" ]; then
  BY_GAL="$ROOT/29_stage26_curve_level_null_refit_controls/results_uploaded_stage26_curve_level_null_refit_controls/stage26_null_kernel_by_galaxy.csv"
fi
if [ ! -f "$BY_KERNEL" ]; then
  BY_KERNEL=""
fi
python "$ROOT/shared/scripts/stage28_kernel_family_profile_audit.py" \
  --by-galaxy "$BY_GAL" \
  --by-kernel "$BY_KERNEL" \
  --out "$OUT"
cat "$OUT/DECISION_STAGE28.txt"
ls -lh "$OUT"

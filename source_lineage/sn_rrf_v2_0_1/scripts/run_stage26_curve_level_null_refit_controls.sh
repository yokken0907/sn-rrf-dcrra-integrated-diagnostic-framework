#!/usr/bin/env bash
set -euo pipefail

ROOT="$(pwd)"
OUT="29_stage26_curve_level_null_refit_controls/results/stage26_curve_level_null_refit_controls"
POP="15_stage13r_rotmod_proxy_repair_audit/results_uploaded_stage13r_repair/stage13r_by_galaxy_population_table.csv"
ROTMOD="data/Rotmod_LTG"

mkdir -p "$OUT"

echo "RUN-STAGE26-CURVE-LEVEL-NULL-REFIT-CONTROLS"
echo "root=$ROOT"
echo "population_table=$POP"
echo "rotmod_dir=$ROTMOD"
echo "out=$OUT"

python shared/scripts/stage26_curve_level_null_refit_controls.py \
  --population-table "$POP" \
  --rotmod-dir "$ROTMOD" \
  --out "$OUT" \
  --seed 20260516 \
  --n-fixed 3.258993 \
  --ups-d 0.5 \
  --ups-b 0.7 \
  --rc-grid-size 140

echo "===== STAGE 26 DECISION ====="
cat "$OUT/DECISION_STAGE26.txt"

echo "===== STAGE 26 OUTPUTS ====="
ls -lh "$OUT"

#!/usr/bin/env bash
set -euo pipefail

ROOT="$(pwd)"
POP="15_stage13r_rotmod_proxy_repair_audit/results_uploaded_stage13r_repair/stage13r_by_galaxy_population_table.csv"
ROTMOD="data/Rotmod_LTG"
OUT="33_stage30_kernel_family_continuum_protocol/results/stage30_kernel_continuum_profile_audit"

mkdir -p "$OUT"

python shared/scripts/stage30_kernel_family_continuum_profile_audit.py   --population-table "$POP"   --rotmod-dir "$ROTMOD"   --out "$OUT"   --n-grid "0.5:10.0:0.25,12.0"   --locked-n 3.258993   --ups-d 0.5   --ups-b 0.7   --rc-grid-size 120

echo "===== STAGE 30 DECISION ====="
cat "$OUT/DECISION_STAGE30.txt"
echo "===== STAGE 30 OUTPUTS ====="
ls -lh "$OUT"

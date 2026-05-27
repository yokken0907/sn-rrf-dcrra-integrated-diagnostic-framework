# Stage 26 Curve-Level Null-Refit Controls

## Decision

`WEAK-AUTHORIZE-STAGE27-DESTRUCTIVE-NULLS-PASSED-NEIGHBOR-KERNELS-COMPETE`

## Purpose

Stage 26 refits curve-level squared-velocity residuals directly against the locked SN-RRF/A10-TVC-RRF kernel and adversarial null kernels.

This is a diagnostic control only. It is not a physical model fit and does not reproduce the earlier nonlinear velocity-space audit exactly.

## Inputs

- population table: `15_stage13r_rotmod_proxy_repair_audit/results_uploaded_stage13r_repair/stage13r_by_galaxy_population_table.csv`
- Rotmod directory: `data/Rotmod_LTG`
- fixed exponent: `3.258993`
- fixed stellar mass-to-light values: `ups_d=0.5`, `ups_b=0.7`

## Main results

- input_population_count: 143
- valid_population_count: 143
- missing_or_unreadable_count: 0
- median Delta AIC(RRF - best destructive null): -85.0215
- RRF beats best destructive null fraction: 0.916084
- RRF strongly beats best destructive null fraction, Delta AIC <= -10: 0.839161
- robust-class RRF beats best destructive null fraction: 0.935065
- median Delta AIC(RRF - best neighbor monotone null): 4.08231
- RRF beats best neighbor monotone null fraction: 0.125874
- guard_pass_count: 5/5

## Interpretation guide

If destructive nulls are beaten, Stage 26 supports a curve-level radial-response shape signal.

If neighboring monotone kernels compete, the correct repair is not to claim fixed-exponent uniqueness. The safer interpretation is that SN-RRF identifies a scale-normalized residual-response family, with the locked exponent acting as one useful representative kernel.

## Claim boundary

- No dark-matter exclusion claim.
- No Lambda-CDM replacement claim.
- No MOND/RAR defeat claim.
- No Bullet-Cluster explanation claim.
- No physical proof of a TVC mechanism.
- No Hubble-tension solution claim.
- Curve-level null-refit diagnostic only.
- No universal fixed-exponent law claim.

## Output files

- `DECISION_STAGE26.txt`
- `stage26_curve_level_null_refit_summary.json`
- `stage26_null_kernel_by_galaxy.csv`
- `stage26_null_kernel_fit_by_galaxy_kernel.csv`
- `stage26_class_null_refit_summary.csv`
- `stage26_missing_or_unreadable_rotmod.csv`

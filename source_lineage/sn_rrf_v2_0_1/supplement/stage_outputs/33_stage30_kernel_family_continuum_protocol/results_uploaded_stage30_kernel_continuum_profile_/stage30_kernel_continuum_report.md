# Stage 30 Kernel-Family Continuum Profile Audit

## Decision

`AUTHORIZE-STAGE31-SN-RRF-CONTINUUM-FAMILY-SYNTHESIS`

## Purpose

Stage 30 scans a continuous grid of saturating kernels

```text
K_n(x) = x^n / (1 + x^n)
```

to test whether SN-RRF should be treated as a scale-normalized residual-response family rather than as a unique fixed-exponent law.

## Inputs

- population table: `15_stage13r_rotmod_proxy_repair_audit/results_uploaded_stage13r_repair/stage13r_by_galaxy_population_table.csv`
- Rotmod directory: `data/Rotmod_LTG`
- locked n: `3.258993`
- n grid count: `41`
- fixed stellar mass-to-light values: `ups_d=0.5`, `ups_b=0.7`

## Main results

- input_population_count: 143
- valid_population_count: 143
- missing_or_unreadable_count: 0
- best_n median: 2.25
- best_n IQR: [1.5, 3.2545]
- median Delta AIC(locked n - best continuum n): 6.29238
- locked within +2 AIC of continuum best fraction: 0.321678
- locked within +10 AIC of continuum best fraction: 0.636364
- guard_pass_count: 6/6

## Interpretation guide

If the best exponent varies across galaxies and the locked exponent is not uniquely favored, the safe conclusion is not fixed-exponent uniqueness. The safe conclusion is that SN-RRF is a heterogeneous scale-normalized monotone-saturating residual-response family.

## Claim boundary

- No dark-matter exclusion claim.
- No Lambda-CDM replacement claim.
- No MOND/RAR defeat claim.
- No Bullet-Cluster explanation claim.
- No physical proof of a TVC mechanism.
- No Hubble-tension solution claim.
- Kernel-continuum diagnostic only.
- No universal fixed-exponent law claim.

## Output files

- `DECISION_STAGE30.txt`
- `stage30_kernel_continuum_summary.json`
- `stage30_continuum_by_galaxy.csv`
- `stage30_continuum_fit_by_galaxy_n.csv`
- `stage30_class_continuum_summary.csv`
- `stage30_n_grid_profile.csv`
- `stage30_kernel_continuum_report.md`
- `stage30_missing_or_unreadable_rotmod.csv`

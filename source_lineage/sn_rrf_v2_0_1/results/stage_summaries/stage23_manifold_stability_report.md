# Stage 23 Manifold Stability Audit

## Decision

`AUTHORIZE-STAGE24-SN-RRF-STABILITY-SYNTHESIS`

## Purpose

Stage 21 authorized the SN-RRF manifold interpretation. Stage 23 stress-tests whether the robust-candidate-calibrated dimensionless manifold is stable under bootstrap recalibration and whether the pathology class remains separated under a shuffled-label permutation guard.

## Main observed results

- valid_population_count: 143
- pathology_moat_hit_rate: 0.857143
- nonpath_pathology_false_positive_rate: 0.000000
- nonpath_q90_manifold_inside_fraction: 0.860294
- pathology_q90_manifold_exclusion_fraction: 0.857143
- pathology-minus-nonpath median distance separation: 18.450155
- permutation p one-sided more-separated: 0.00049975

## Bootstrap medians

- robust_inside_fraction median: 0.896104
- nonpath_inside_fraction median: 0.852941
- pathology_exclusion_fraction median: 0.857143

## Guard result

- guard_pass_count: 7/7

## Interpretation

This is a diagnostic stability audit only. Passing this stage would support the SN-RRF language as a dimensionless central-manifold and pathology-separation diagnostic. It does not promote SN-RRF to a physical mechanism, dark-matter replacement, Lambda-CDM replacement, MOND/RAR defeat claim, Bullet-Cluster explanation, or Hubble-tension solution.

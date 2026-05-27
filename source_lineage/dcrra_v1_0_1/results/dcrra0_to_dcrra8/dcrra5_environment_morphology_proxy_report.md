# DCRRA5 Environment / Morphology Proxy Audit

## Decision

`AUTHORIZE-DCRRA6-DESTRUCTIVE-CONSTRUCTIVE-NULL-AUDIT`

## Purpose

DCRRA5 tests whether DCRRA4 triangular residual classes vary systematically with velocity-scale, gas-fraction, baryon-fraction, response-scale, response-amplitude, continuum-exponent, and curve-sampling proxies. This is a diagnostic association audit only.

## Main results

- input population count: 143

- proxy count: 8

- binning success count: 8

- significant proxy count, permutation p <= 0.05: 6

- moderate proxy count, Cramer's V >= 0.25: 8

- strongest proxy by Cramer's V: n_points

- guard pass count: 7/7

## Proxy association table

| proxy                       |   valid_n |   bin_count |   class_count |   cramers_v_class_association |   permutation_p_value |   association_flag |   moderate_association_flag |
|:----------------------------|----------:|------------:|--------------:|------------------------------:|----------------------:|-------------------:|----------------------------:|
| n_points                    |       143 |           3 |             7 |                      0.396545 |                 0.001 |                  1 |                           1 |
| outer_baryon_fraction_proxy |       143 |           3 |             7 |                      0.377324 |                 0.001 |                  1 |                           1 |
| gas_fraction_proxy          |       143 |           3 |             7 |                      0.36862  |                 0.001 |                  1 |                           1 |
| best_n                      |       143 |           3 |             7 |                      0.361989 |                 0.001 |                  1 |                           1 |
| rrf_rc_over_rlast           |       143 |           3 |             7 |                      0.298193 |                 0.008 |                  1 |                           1 |
| rrf_A_over_vouter2          |       143 |           3 |             7 |                      0.268282 |                 0.044 |                  1 |                           1 |
| v_max_kms                   |       143 |           3 |             7 |                      0.260774 |                 0.075 |                  0 |                           1 |
| v_outer_kms                 |       143 |           3 |             7 |                      0.259262 |                 0.075 |                  0 |                           1 |

## Interpretation

DCRRA4 residual-regime classes exhibit diagnostic association with environment/morphology/fit proxies. Associations are not causal physical classifications and do not imply dark-matter exclusion or NFW/RAR falsification.

## Claim boundary

- No dark-matter exclusion claim.

- No Lambda-CDM replacement claim.

- No MOND/RAR falsification claim.

- No NFW-halo falsification claim.

- No Bullet-Cluster explanation claim.

- No particle-identity claim.

- No Hubble-tension solution claim.

- No SN-RRF as physical dark-matter substitute claim.

- Environment/morphology proxy associations are diagnostic only, not causal physical classifications.

## Output files

- `DCRRA5_DECISION.txt`

- `dcrra5_environment_morphology_proxy_summary.json`

- `dcrra5_proxy_association_summary.csv`

- `dcrra5_proxy_bin_class_summary.csv`

- `dcrra5_class_proxy_medians.csv`

- `dcrra5_triangular_class_proxy_enrichment.csv`

- `dcrra5_environment_morphology_proxy_report.md`

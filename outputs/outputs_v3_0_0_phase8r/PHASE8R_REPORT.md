# Phase 8R Injection-Recovery Diagnostic Separability Audit

## Decision

`LOCK-PHASE8R-INJECTION-RECOVERY-SEPARABILITY-AUDIT-FAIL_OR_NULL`

Interpretation: **SEPARABILITY-LIMITATION-PERSISTS**

## Main metrics

- phase8_overall_recovery_rate: 0.5664335664335665
- phase8_balanced_accuracy: 0.5664335664335663
- best_operational_variant: reported_only_noise_LOW
- best_operational_variant_balanced_accuracy: 0.7762237762237763
- best_full_coverage_operational_variant: phase8_reported_predicted_type
- best_full_coverage_operational_balanced_accuracy: 0.5664335664335663
- low_noise_recovery_rate: 0.7762237762237763
- high_noise_recovery_rate: 0.40326340326340326
- physical_like_mean_recall: 0.43298368298368295
- pathology_nuisance_mean_recall: 0.8333333333333333
- top_offdiagonal_pair: RAR_LIKE->HALO_LIKE
- top_offdiagonal_fraction: 0.30303030303030304
- guard_pass_count: 2
- guard_count: 7
- external_validation: HOLD_NON_SPARC_COMPONENT_CURVE_TABLE_NOT_AVAILABLE

## Weakest confusion pairs

| injection_type       | predicted_type       |   n |   row_fraction |
|:---------------------|:---------------------|----:|---------------:|
| RAR_LIKE             | HALO_LIKE            | 130 |       0.30303  |
| HALO_LIKE            | RAR_LIKE             | 113 |       0.263403 |
| RESPONSE_FAMILY_LIKE | MIXED_RESPONSE_HALO  | 111 |       0.258741 |
| MIXED_RESPONSE_HALO  | RESPONSE_FAMILY_LIKE | 101 |       0.235431 |
| HALO_LIKE            | MIXED_RESPONSE_HALO  |  74 |       0.172494 |
| NUISANCE_GRADIENT    | RAR_LIKE             |  69 |       0.160839 |
| HALO_LIKE            | NUISANCE_GRADIENT    |  68 |       0.158508 |
| RAR_LIKE             | NUISANCE_GRADIENT    |  66 |       0.153846 |
| MIXED_RESPONSE_HALO  | HALO_LIKE            |  63 |       0.146853 |
| RAR_LIKE             | MIXED_RESPONSE_HALO  |  49 |       0.114219 |

## By-type margins

| injection_type       |   n |   reported_recall |   rss_margin_positive_fraction |   corr_margin_positive_fraction |   median_rss_correct_margin |   median_corr_true_minus_best_wrong |   median_rss_best_second_margin |   median_corr_best_second_margin |
|:---------------------|----:|------------------:|-------------------------------:|--------------------------------:|----------------------------:|------------------------------------:|--------------------------------:|---------------------------------:|
| HALO_LIKE            | 429 |          0.333333 |                       0.333333 |                        0.333333 |                -0.001412    |                        -0.00073487  |                      0.00199952 |                      0.00104134  |
| RAR_LIKE             | 429 |          0.384615 |                       0.384615 |                        0.384615 |                -0.000896684 |                        -0.00048609  |                      0.00168683 |                      0.000905768 |
| MIXED_RESPONSE_HALO  | 429 |          0.452214 |                       0.452214 |                        0.452214 |                -0.000987182 |                        -0.000531185 |                      0.00305507 |                      0.00167358  |
| RESPONSE_FAMILY_LIKE | 429 |          0.561772 |                       0.561772 |                        0.561772 |                 0.00143707  |                         0.000736934 |                      0.00404328 |                      0.00221273  |
| NUISANCE_GRADIENT    | 429 |          0.710956 |                       0.710956 |                        0.710956 |                 0.0138084   |                         0.0074581   |                      0.0138084  |                      0.0074581   |
| PATHOLOGY_OUTLIER    | 429 |          0.955711 |                       0.955711 |                        0.955711 |                 0.606816    |                         0.496594    |                      0.606816   |                      0.496594    |

## Classifier variants

| variant                                 |    n |   coverage |   accuracy |   balanced_accuracy |   min_class_recall |
|:----------------------------------------|-----:|-----------:|-----------:|--------------------:|-------------------:|
| phase8_reported_predicted_type          | 2574 |   1        |   0.566434 |            0.566434 |           0.333333 |
| rss_minimum_type                        | 2574 |   1        |   0.566434 |            0.566434 |           0.333333 |
| corr_maximum_type                       | 2574 |   1        |   0.566434 |            0.566434 |           0.333333 |
| hybrid_corr_pathology_nuisance_then_rss | 2574 |   1        |   0.566434 |            0.566434 |           0.333333 |
| reported_only_noise_LOW                 |  858 |   0.333333 |   0.776224 |            0.776224 |           0.552448 |
| reported_only_noise_MEDIUM              |  858 |   0.333333 |   0.519814 |            0.519814 |           0.27972  |
| reported_only_noise_HIGH                |  858 |   0.333333 |   0.403263 |            0.403263 |           0.167832 |
| selective_rss_margin_q0.00              | 2574 |   1        |   0.566434 |            0.566434 |           0.333333 |
| selective_rss_margin_q0.25              | 1930 |   0.749806 |   0.626425 |            0.574564 |           0.244094 |
| selective_rss_margin_q0.50              | 1287 |   0.5      |   0.735043 |            0.557333 |           0        |
| selective_rss_margin_q0.75              |  644 |   0.250194 |   0.864907 |            0.405855 |           0        |
| oracle_diagnostic_correct_margin_q0.25  | 1930 |   0.749806 |   0.75544  |            0.738139 |           0.5      |
| oracle_diagnostic_correct_margin_q0.50  | 1287 |   0.5      |   1        |            1        |           1        |
| oracle_diagnostic_correct_margin_q0.75  |  644 |   0.250194 |   1        |            1        |           1        |

## Claim boundary

Phase 8R is an internal synthetic-control separability audit. It does not establish a physical dark-sector model, does not exclude dark matter, does not falsify MOND/RAR or NFW, and does not remove the non-SPARC external-data HOLD.

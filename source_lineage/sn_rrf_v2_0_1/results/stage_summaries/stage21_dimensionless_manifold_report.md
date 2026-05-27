# Stage 21 Dimensionless Manifold Audit

## Decision

`AUTHORIZE-STAGE22-SN-RRF-MANIFOLD-REFORMULATION`

## Why Stage 21 was needed

Stage 20 tested a strict rectangular normal band:

```text
0.20 <= s_c <= 0.50
0.40 <= lambda <= 1.20
```

Stage 20 was inconclusive because that rectangle did not capture enough individual robust galaxies.

Stage 21 therefore tests a weaker and more defensible claim:

```text
SN-RRF is not a universal per-galaxy normal rectangle.
It may instead be a class-level central manifold plus a pathology-separation moat.
```

## Main results

- valid_population_count: 143
- nonpath_class_medians_in_predeclared_normal_band: True
- pathology_class_median_in_pathology_moat: True
- nonpath_pathology_false_positive_rate: 0.000000
- pathology_moat_hit_rate: 0.857143
- robust_q90_manifold_inside_fraction: 0.896104
- nonpath_q90_manifold_inside_fraction: 0.860294
- pathology_q90_manifold_inside_fraction: 0.142857
- pathology_q90_manifold_exclusion_fraction: 0.857143

## Interpretation

The strict Stage 20 normal rectangle should not be promoted as a universal per-galaxy law.

However, Stage 21 supports a weaker and more useful interpretation:

1. the medians of the non-pathology classes remain inside the originally proposed dimensionless response neighborhood;
2. the pathology class median is far outside that neighborhood and inside the pathology moat;
3. the pathology moat catches most core-pathology cases while producing no non-pathology false positives in this table;
4. a robust-candidate-calibrated q90 manifold includes most non-pathology cases while excluding most pathology cases.

Therefore, the allowed Stage 22 move is not a physical promotion. It is a theory-language repair:

```text
SN-RRF should be described as a dimensionless central-manifold and pathology-separation diagnostic,
not as a universal normal-response rectangle.
```

## Claim boundary

This is a diagnostic manifold audit only. It does not prove a physical mechanism and does not address the Hubble tension directly.

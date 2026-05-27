# Stage 20 Dimensionless Kernel Audit

## Decision

`WEAK-HOLD-STAGE20-DIMENSIONLESS-BAND-INCONCLUSIVE`

## Core idea

This audit tests whether A10/TVC-RRF can be generalized into SN-RRF using dimensionless variables:

```text
s_c = r_c / R_last
lambda = A / v_outer^2
```

## Predeclared bands

Normal response band:

```text
0.20 <= s_c <= 0.50
0.40 <= lambda <= 1.20
```

Pathology band:

```text
s_c > 1.0 or lambda > 5.0
```

## Results

- valid_population_count: 143
- all_normal_band_fraction: 0.48951048951048953
- all_pathology_band_fraction: 0.04195804195804196
- robust_in_normal_band_fraction: 0.4805194805194805
- pathology_class_in_pathology_band_fraction: 0.8571428571428571

## Claim boundary

This is a diagnostic dimensionless-kernel audit only. It does not prove a physical mechanism and does not address the Hubble tension directly.

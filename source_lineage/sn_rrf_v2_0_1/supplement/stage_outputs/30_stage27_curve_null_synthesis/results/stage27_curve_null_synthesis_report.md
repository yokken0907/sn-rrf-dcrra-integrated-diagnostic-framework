# Stage 27 Curve-Level Null-Refit Synthesis

## Decision

`LOCK-STAGE27-CURVE-LEVEL-DESTRUCTIVE-NULLS-PASSED-SATURATING-FAMILY-NOT-UNIQUE`

## What Stage 26 established

Stage 26 refit curve-level squared-velocity residuals against the locked SN-RRF/A10-TVC-RRF kernel and adversarial null kernels.

The destructive-null side is strong:

- valid_population_count: 143
- guard_pass_count: 5/5
- median Delta AIC(RRF - best destructive null): -85.0215
- RRF beats best destructive null fraction: 0.916084
- RRF strongly beats best destructive null fraction: 0.839161
- robust-class RRF beats best destructive null fraction: 0.935065

This supports a curve-level radial-response shape signal. It means the signal is not reproduced well by destructive controls such as constant floors, reversed kernels, radius-shuffled kernels, or outer-step median forms.

## What Stage 26 did not establish

Neighboring monotone saturating kernels compete:

- median Delta AIC(RRF - best neighbor monotone null): 4.08231
- RRF beats best neighbor monotone null fraction: 0.125874

Therefore the locked exponent `n = 3.258993` must not be promoted as a unique law.

## Theory-language repair

The correct Stage 27 repair is:

```text
SN-RRF is a scale-normalized residual-response family.
The locked n = 3.258993 kernel is one useful representative of this family,
not a unique physical exponent and not a fundamental law.
```

This repair is scientifically healthier than forcing a uniqueness claim. Stage 26 supports the existence of a saturating radial-response family more strongly than the uniqueness of the original TVC-derived exponent.

## Best-neighbor distribution

```json
{
  "saturating_n2": 67,
  "saturating_n4": 26,
  "saturating_n1": 16,
  "saturating_n8": 12,
  "arctan_saturating": 10,
  "exp_saturating": 8,
  "saturating_n6": 4
}
```

## Best destructive-null distribution

```json
{
  "shuffled_radius_rrf_nfixed": 85,
  "outer_step_median": 54,
  "constant_floor": 3,
  "reversed_rrf_nfixed": 1
}
```

## Claim boundary

- No dark-matter exclusion claim.
- No Lambda-CDM replacement claim.
- No MOND/RAR defeat claim.
- No Bullet-Cluster explanation claim.
- No physical proof of a TVC mechanism.
- No Hubble-tension solution claim.
- Curve-level null-refit diagnostic only.
- No universal fixed-exponent law claim.
- SN-RRF family diagnostic only.

## Next stage

Stage 28 should profile the kernel family using the full per-kernel curve-level fit table (`stage26_null_kernel_fit_by_galaxy_kernel.csv`) if available. If that file is unavailable, Stage 28 can still summarize the best-neighbor distribution from `stage26_null_kernel_by_galaxy.csv`, but it cannot perform a full family profile.

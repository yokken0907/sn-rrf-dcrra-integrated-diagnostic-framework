# Stage 29 SN-RRF Kernel-Family Synthesis

## Decision

`LOCK-STAGE29-SN-RRF-KERNEL-FAMILY-SYNTHESIS-DIAGNOSTIC-ONLY`

## Why Stage 29 was needed

Stage 26 showed that the locked A10/TVC-RRF/SN-RRF kernel beats destructive curve-level nulls, but neighboring monotone saturating kernels compete. Stage 28 then profiled that neighboring kernel family.

Stage 29 repairs the theory language accordingly.

## Main Stage 28 facts carried forward

- valid_population_count: 143
- median Delta AIC(locked RRF - best neighbor null): 4.082307127320703
- locked RRF beats best neighbor null fraction: 0.1258741258741259
- full per-kernel table available: True
- per-galaxy best-neighbor counts:
  - saturating_n2: 67
  - saturating_n4: 26
  - saturating_n1: 16
  - saturating_n8: 12
  - arctan_saturating: 10
  - exp_saturating: 8
  - saturating_n6: 4

## Synthesis

The fixed exponent `n = 3.258993` should not be promoted as a unique physical law or universal diagnostic optimum.

The safer and stronger theory language is:

```text
SN-RRF = Scale-Normalized Residual Response Family
```

SN-RRF describes a family of scale-normalized, monotone saturating radial response kernels. The locked `n = 3.258993` kernel remains a useful historically motivated and audit-locked representative, but Stage 28 shows that it is not uniquely selected by the curve-level kernel-family profile.

## Interpretation

The result does not weaken the main finding that destructive nulls are beaten. Instead, it refines the finding:

```text
There is evidence for a monotone saturating radial residual-response family,
not for a unique fixed-exponent law.
```

This is a theory-language repair. It avoids overclaiming and makes the framework more robust.

## Claim boundary

- No dark-matter exclusion claim.
- No Lambda-CDM replacement claim.
- No MOND/RAR defeat claim.
- No Bullet-Cluster explanation claim.
- No physical proof of a TVC mechanism.
- No Hubble-tension solution claim.
- Kernel-family diagnostic only.
- No universal fixed-exponent law claim.
- No physical-promotion claim from kernel-family profiling.

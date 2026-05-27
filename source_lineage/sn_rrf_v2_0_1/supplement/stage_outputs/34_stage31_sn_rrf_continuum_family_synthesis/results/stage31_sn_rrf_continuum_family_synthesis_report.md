# Stage 31 SN-RRF Continuum-Family Synthesis

## Decision

`LOCK-STAGE31-SN-RRF-CONTINUUM-FAMILY-SYNTHESIS-DIAGNOSTIC-ONLY`

## Why Stage 31 was needed

Stage 26 showed that the locked A10/TVC-RRF kernel defeats destructive curve-level nulls, but neighboring monotone saturating kernels compete.
Stage 28 therefore repaired the theory language from a fixed-exponent law into a kernel-family interpretation.
Stage 30 then tested this repair by scanning a continuous grid of kernels

```text
K_n(x) = x^n / (1 + x^n)
```

with `n` ranging from 0.5 to 12.0 over 41 grid points.

## Stage 30 results carried into Stage 31

- valid_population_count: 143
- missing_or_unreadable_count: 0
- locked_n: 3.258993
- best_n median: 2.25
- best_n IQR: [1.5, 3.2544965]
- median Delta AIC(locked n - best continuum n): 6.292381
- locked within +2 AIC of continuum best fraction: 0.321678
- locked within +10 AIC of continuum best fraction: 0.636364
- guard_pass_count: 6/6

Top best-n counts:

```json
{
  "1.5": 17,
  "2.25": 16,
  "2.5": 14,
  "2.0": 14,
  "12.0": 9,
  "2.75": 9,
  "1.25": 9,
  "1.75": 7,
  "1.0": 6,
  "3.0": 5
}
```

## Locked interpretation

Stage 31 does **not** support a universal fixed-exponent law at `n = 3.258993`.
The locked exponent remains useful as a representative A10/TVC-derived kernel and as a reproducible audit anchor, but it is not uniquely preferred by the curve-level continuum scan.

The supported synthesis is:

```text
SN-RRF = Scale-Normalized Residual Response Family.
```

In this interpretation, the relevant object is not a single exponent. The relevant object is a family of scale-normalized monotone-saturating radial residual-response kernels whose effective steepness varies across galaxies and diagnostic classes.

## Recommended theory language

Allowed:

```text
SN-RRF identifies a heterogeneous scale-normalized monotone-saturating residual-response family in SPARC rotation-curve residuals.
The historical A10/TVC exponent n = 3.258993 is a useful representative kernel, but the continuum profile does not support fixed-exponent uniqueness.
```

Forbidden:

```text
The exponent n = 3.258993 is a universal physical law.
SN-RRF proves a physical TVC mechanism.
SN-RRF replaces dark matter, Lambda-CDM, MOND/RAR, or solves the Hubble tension.
```

## Scientific meaning

The continuum profile strengthens the move away from old TVC-style overclaiming. It shows that the empirical signal is better understood as a shape-family phenomenon: galaxies prefer related monotone saturating radial response curves, but not all prefer the same steepness.

This is a more robust and more scientific claim than fixed-exponent uniqueness.

## Claim boundary

- No dark-matter exclusion claim.
- No Lambda-CDM replacement claim.
- No MOND/RAR defeat claim.
- No Bullet-Cluster explanation claim.
- No physical proof of a TVC mechanism.
- No Hubble-tension solution claim.
- Kernel-continuum diagnostic only.
- No universal fixed-exponent law claim.
- No physical-promotion claim from Stage 31 synthesis.

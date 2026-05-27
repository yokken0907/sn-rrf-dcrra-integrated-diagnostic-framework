# Stage 26 Protocol — Curve-Level Null-Refit Controls

## Purpose

Stage 21 and Stage 23 supported SN-RRF as a dimensionless central-manifold and pathology-separation diagnostic. Stage 26 asks a stricter curve-level question:

> Does the locked fixed-exponent response kernel retain diagnostic advantage against destructive null kernels when each curve is refit directly?

## Inputs

- Stage 13R population table:
  `15_stage13r_rotmod_proxy_repair_audit/results_uploaded_stage13r_repair/stage13r_by_galaxy_population_table.csv`
- SPARC Rotmod directory:
  `data/Rotmod_LTG/`

The script also uses `resolved_rotmod_file` if that column exists in the population table.

## Diagnostic fitting method

For each galaxy and kernel family, the script fits squared-velocity residuals:

```text
Y(r) = V_obs(r)^2 - V_bar(r)^2
Y(r) ≈ A K(r / r_c)
```

with fixed stellar mass-to-light values by default:

```text
ups_d = 0.5
ups_b = 0.7
```

The fitting is deliberately simple and auditable:

- grid search over `r_c`,
- non-negative weighted least-squares estimate of `A` at each grid point,
- AIC-like score in squared-velocity residual space.

This is not intended to reproduce the earlier nonlinear velocity-space fit exactly. It is a curve-level adversarial control of radial shape.

## Kernel families

Locked response kernel:

```text
K_n(x) = x^n / (1 + x^n), n = 3.258993
```

Destructive nulls include:

- constant residual floor,
- reversed decreasing kernel,
- deterministic radius-shuffled kernel,
- signless outer-only step-like variants.

Neighbor monotone comparators include nearby or generic saturating kernels such as `n=1`, `n=2`, `n=4`, `n=6`, `n=8`, exponential, and arctangent forms.

## Decision logic

Stage 26 distinguishes two questions:

1. Does SN-RRF beat destructive nulls?
2. Is the exact fixed exponent uniquely preferred over neighboring monotone kernels?

Passing question 1 supports a residual-response shape signal. Passing question 2 would be stronger, but is not required for the diagnostic manifold interpretation.

## Claim boundary

No physical-promotion claim is allowed from Stage 26. A pass supports only a reviewer-grade diagnostic control.

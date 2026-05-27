# Phase 8 Injection-Recovery Null Tests

## Decision

`FAIL_OR_NULL-PHASE8-INJECTION-RECOVERY-NULL-TESTS-LOCKED-WITH-CLAIM-BOUNDARY`

Interpretation: **INJECTION-RECOVERY-NOT-SUFFICIENTLY-SUPPORTED**

## Scope

Phase 8 is an internal synthetic-control audit. It uses the Phase 4AB SPARC residual-shape grid and injects known diagnostic residual-pattern families into observed SPARC residual-shape backgrounds. It is not non-SPARC external residual-level validation.

## Main metrics

- Feature rows: 143
- Shape-grid rows: 5720
- Galaxies: 143
- Synthetic cases: 2574
- Overall recovery rate: 0.566434
- Balanced accuracy: 0.566434
- Minimum class recall: 0.333333
- High-noise recovery rate: 0.403263
- False response-family rate: 0.072261
- False halo-like rate: 0.113753
- Guards passed: 2/6

## Claim boundary

This audit can support only the statement that the frozen synthetic injection-recovery protocol is able or unable to recover known injected diagnostic shape families under the tested settings. It does not establish a physical dark-sector model, does not exclude dark matter, does not falsify MOND/RAR or NFW, and does not remove the non-SPARC external-data HOLD.

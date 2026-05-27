# Phase 7 Frozen Holdout Robustness Audit Report

## Decision

`PASS-PHASE7-FROZEN-HOLDOUT-ROBUSTNESS-AUDIT-RUN`

Interpretation: `FROZEN-HOLDOUT-ROBUSTNESS-SUPPORTED-WITH-BOUNDARY-CAUTIONS`

## Scope

This is an internal SPARC holdout robustness audit. It is not non-SPARC external residual-level validation and does not promote SN-RRF/DCRRA into a physical dark-matter model, dark-matter exclusion claim, MOND/RAR/NFW refutation, or Lambda-CDM replacement.

## Key counts

- Feature rows: 143
- Zones: 7
- Evaluated holdouts excluding baseline: 32
- Random 80% holdouts: 10
- Leave-one-zone-out holdouts: 7

## Robustness summary

- Stable holdout fraction: 1.000000
- Mixed holdout fraction: 0.000000
- Fragile holdout fraction: 0.000000
- Random stable fraction: 1.000000
- Zone-leaveout stable fraction: 1.000000
- Median evaluated zone JS divergence: 0.005350
- Maximum evaluated zone JS divergence: 0.153050

## Baseline internal fractions

- Response-family zone fraction: 0.538462
- AICc overflex fraction: 0.468531
- High failure-boundary score >= 4 fraction: 0.188811

## Safe interpretation

The audit tests whether the internal Phase 0-6 diagnostic summaries survive frozen data-split and proxy/quality stress conditions. A stable or mixed result supports internal robustness of the diagnostic framework within SPARC only. It does not address the missing non-SPARC external component-curve validation branch.

External validation status: `HOLD_NON_SPARC_COMPONENT_CURVE_TABLE_NOT_AVAILABLE`

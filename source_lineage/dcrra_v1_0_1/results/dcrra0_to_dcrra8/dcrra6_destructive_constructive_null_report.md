# DCRRA6 Destructive / Constructive Null Audit

## Decision

`AUTHORIZE-DCRRA7-DARK-COMPONENT-RESIDUAL-MAP`

## Purpose

DCRRA6 tests whether the DCRRA4 triangular residual-regime classes retain structure under destructive controls and whether proxy-only constructive reconstruction recovers nontrivial class information.

This is a diagnostic null-control audit only. It is not a physical dark-matter classification.

## Main results

- input population count: 143
- class count: 7
- proxy count: 8
- permutations per null: 1000
- observed mean Cramer's V across proxies: 0.323874
- observed max Cramer's V across proxies: 0.396545
- destructive null reject count, p <= 0.05: 4/4
- proxy-only reconstruction accuracy: 0.314685
- proxy-only reconstruction balanced accuracy: 0.328735
- constructive signal count, p <= 0.05: 2/2
- guard pass count: 7/7

## Interpretation

DCRRA4 triangular residual-regime classes are tested against shuffled class-label and shuffled proxy nulls. A proxy-only nearest-centroid reconstruction is also used as a constructive control. Passing this audit means that the diagnostic classes are not merely arbitrary labels with no proxy-coherent structure. It does not mean that the classes are physical dark-matter categories.

## Claim boundary

- No dark-matter exclusion claim.
- No Lambda-CDM replacement claim.
- No MOND/RAR falsification claim.
- No NFW-halo falsification claim.
- No Bullet-Cluster explanation claim.
- No particle-identity claim.
- No Hubble-tension solution claim.
- No SN-RRF as physical dark-matter substitute claim.
- Destructive/constructive null controls are diagnostic only and not causal physical classifications.

## Output files

- `DCRRA6_DECISION.txt`
- `dcrra6_destructive_constructive_null_summary.json`
- `dcrra6_proxy_signal_profile.csv`
- `dcrra6_destructive_null_results.csv`
- `dcrra6_constructive_control_summary.csv`
- `dcrra6_constructive_proxy_reconstruction_by_galaxy.csv`
- `dcrra6_class_reconstruction_summary.csv`
- `dcrra6_destructive_constructive_null_report.md`

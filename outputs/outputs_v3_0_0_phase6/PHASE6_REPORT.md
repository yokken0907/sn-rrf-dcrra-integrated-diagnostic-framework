# Phase 6 Baryonic-Systematics and Proxy Sensitivity Audit

## Decision
PASS-PHASE6-BARYONIC-SYSTEMATICS-PROXY-SENSITIVITY-AUDIT-RUN

## Claim boundary
This is an internal SPARC proxy/systematics sensitivity audit. It does not constitute non-SPARC external residual-level validation, dark-matter exclusion, MOND/RAR/NFW refutation, or physical model-selection evidence.

## Summary
- feature_rows: 143
- zone_count: 7
- proxy_count_tested: 14
- strong_proxy_split_association_count: 5
- interpretation: PROXY-SENSITIVITY-STRUCTURE-DETECTED
- external_validation: HOLD

## Main interpretation
Phase 6 tests whether DCRRA zones, overflex-null behavior, SN-RRF-family survival, and residual-shape metrics are sensitive to baryonic, kinematic, and quality/systematics proxies. Positive associations are treated as diagnostic structure and/or failure-boundary information, not causal physical classification.

## Strong median-split proxy associations
- n_points -> existing_aicc_overflex_flag: high-low=0.340, p=0.0020
- n_points -> response_family_zone_flag: high-low=0.291, p=0.0020
- v_max_kms -> existing_aicc_overflex_flag: high-low=0.272, p=0.0020
- v_outer_kms -> existing_aicc_overflex_flag: high-low=0.244, p=0.0060
- kernel_curve_rmse -> existing_aicc_overflex_flag: high-low=0.216, p=0.0140

## Failure-boundary use
High-risk rows are ledger candidates, not removals. They identify where low point count, high error, roughness, negative residual fractions, overflex absorption, and nuisance/pathology labels overlap.

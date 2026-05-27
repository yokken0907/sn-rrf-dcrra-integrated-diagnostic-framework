# GitHub Release Draft: v3.0.1-integrated-complete-repository

## Release title

SN-RRF-DCRRA v3.0.1 Complete GitHub Repository

## Release tag

`v3.0.1-integrated-complete-repository`

## Summary

This release provides the complete GitHub-ready repository integrating the SN-RRF v2.0.1 parent diagnostic package, the DCRRA v1.0.1 residual-regime package, and the v3.0.1 integrated consolidation manuscript and Phase 0-9 internal deepening outputs.

## Claim boundary

This release is a claim-bounded diagnostic framework for SPARC galaxy rotation-curve residual regimes. It does not claim dark-matter exclusion, Lambda-CDM replacement, MOND/RAR falsification, NFW-halo falsification, Bullet-Cluster explanation, particle identity, Hubble-tension solution, or full non-SPARC external residual-level validation.

## External validation status

`HOLD_NON_SPARC_COMPONENT_CURVE_TABLE_NOT_AVAILABLE`

## Included lineage

- SN-RRF v2.0.1 parent repository under `source_lineage/sn_rrf_v2_0_1/`
- DCRRA v1.0.1 parent repository under `source_lineage/dcrra_v1_0_1/`
- v3.0.1 integrated paper and active outputs at the repository root

## Verification

```bash
python tools/verify_manifest_excluding_self.py
python scripts/verify_phase10_package.py
python scripts/verify_complete_repository_package.py
```

Expected PASS strings:

```text
PASS-MANIFEST-VERIFICATION
PASS-PHASE10-INTEGRATED-CONSOLIDATION-PACKAGE-VERIFICATION
PASS-COMPLETE-REPOSITORY-PACKAGE-VERIFICATION
```

## Zenodo notes

- Use license `other-open` / source-defined license in repository.
- Do not manually enter an existing DOI as the external DOI for this GitHub release.
- Let Zenodo create a new repository archive DOI from this release.

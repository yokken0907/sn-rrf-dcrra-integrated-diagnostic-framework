# SN-RRF-DCRRA v3.0.1 Complete GitHub Repository

**Version:** `3.0.1-integrated-complete-repository`  
**Suggested GitHub release tag:** `v3.0.1-integrated-complete-repository`  
**Author:** Keiji Yoshimura / Independent Researcher  
**Status:** complete GitHub-ready repository integrating SN-RRF v2.0.1, DCRRA v1.0.1, and the v3.0.1 integrated consolidation manuscript/package.

## What this repository is

This repository is the complete integrated GitHub package for the SN-RRF/DCRRA residual-regime diagnostic line.
It is not merely an addendum. It contains:

- the active integrated manuscript and TeX source under `paper/`;
- Phase 0-9 v3.0.1 outputs under `outputs/`;
- active verification scripts under `scripts/` and `tools/`;
- claim-boundary, no-go, release, and visual-orientation documentation under `docs/`;
- the two parent repository lineages under `source_lineage/`.

## Main paper

- `paper/SN_RRF_DCRRA_integrated_consolidation_v3_0_1.pdf`
- `paper/SN_RRF_DCRRA_integrated_consolidation_v3_0_1.tex`

The previous short v3.0.0 synthesis is preserved in `paper/archive_v3_0_0_short_synthesis/` for provenance.

## Source lineage

- `source_lineage/sn_rrf_v2_0_1/` preserves the prior SN-RRF v2.0.1 repository package.
- `source_lineage/dcrra_v1_0_1/` preserves the prior DCRRA v1.0.1 repository package.
- `SOURCE_LINEAGE.md` and `docs/history/SOURCE_LINEAGE_MAP_v3_0_1_complete.md` describe the integration map.

These are lineage materials, not active release roots. The active release root is this v3.0.1 repository root.

## Core claim boundary

Allowed claim: within the internal SPARC diagnostic protocol, SN-RRF/DCRRA provides a structured residual-regime diagnostic framework with explicit comparator, proxy, holdout, injection-recovery, and failure-boundary limitations.

Not claimed: dark-matter exclusion, Lambda-CDM replacement, MOND/RAR falsification, NFW-halo falsification, Bullet-Cluster explanation, particle identity, Hubble-tension solution, or full non-SPARC external residual-level validation.

## External validation

External residual-level validation remains `HOLD_NON_SPARC_COMPONENT_CURVE_TABLE_NOT_AVAILABLE`.

## Verification

```bash
python tools/verify_manifest_excluding_self.py
python scripts/verify_phase10_package.py
python scripts/verify_complete_repository_package.py
```

Expected:

```text
PASS-MANIFEST-VERIFICATION
PASS-PHASE10-INTEGRATED-CONSOLIDATION-PACKAGE-VERIFICATION
PASS-COMPLETE-REPOSITORY-PACKAGE-VERIFICATION
```

## Release metadata

Use the suggested tag `v3.0.1-integrated-complete-repository` for this complete GitHub repository release. Keep `CITATION.cff` version, `.zenodo.json` version, and the release tag aligned. Do not add a DOI field to `.zenodo.json`; let Zenodo create the archive DOI from the GitHub release.

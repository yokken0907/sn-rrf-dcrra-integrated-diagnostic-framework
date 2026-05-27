# DCRRA4 NFW / RAR / SN-RRF Triangular Comparator Audit

## Decision

`AUTHORIZE-DCRRA5-ENVIRONMENT-MORPHOLOGY-PROXY-AUDIT`

## Purpose

DCRRA4 compares three diagnostic interpretations of dark-component-like galaxy rotation-curve residuals:

1. NFW-like halo comparator.
2. RAR-like acceleration comparator.
3. SN-RRF-family-like scale-normalized monotone-saturating response comparator.

This is not a physical dark-matter classification and not a model-selection claim for cosmology. It is a diagnostic taxonomy audit.

## Main counts

- input population count: 143
- interpretable non-pathology/non-nuisance count: 101
- pathology or nuisance pass-through count: 42
- guard pass count: 7/7

## Triangle class counts

| dcrra4_triangle_class                |   galaxy_count |   fraction |
|:-------------------------------------|---------------:|-----------:|
| SN_RRF_FAMILY_TRIANGLE_DOMINANT      |             54 |  0.377622  |
| NUISANCE_SENSITIVE                   |             30 |  0.20979   |
| SN_RRF_RAR_ADVANTAGE_NFW_COMPETITIVE |             23 |  0.160839  |
| THREE_WAY_COMPETITIVE                |             16 |  0.111888  |
| PATHOLOGY_ARCHIVE                    |             12 |  0.0839161 |
| NFW_TRIANGLE_DOMINANT                |              6 |  0.041958  |
| UNRESOLVED_TRIANGULAR                |              2 |  0.013986  |

## Interpretable diagnostic counts

- SN-RRF-family dominant or RAR-advantage/NFW-competitive: 77
- NFW triangle dominant: 6
- RAR triangle dominant: 0
- mixed or unresolved: 18

## Median diagnostic margins

- median estimated Delta AIC(SN-RRF-family - NFW-like): -11.8461
- median estimated Delta AIC(SN-RRF-family - RAR-like): -48.2298
- median Delta AIC(NFW-like - RAR-like), reconstructed from deltas: -21.8978
- median best-n: 2.25

## Interpretation

The residual population is not monolithic. A sizeable SN-RRF-family-like component remains, but NFW-related and mixed regimes are also preserved. Nuisance-sensitive and pathology/archive cases remain pass-through classes rather than physical classifications.

## Claim boundary

- No dark-matter exclusion claim.
- No Lambda-CDM replacement claim.
- No MOND/RAR falsification claim.
- No NFW-halo falsification claim.
- No Bullet-Cluster explanation claim.
- No particle-identity claim.
- No Hubble-tension solution claim.
- No SN-RRF as physical dark-matter substitute claim.
- Triangular comparator margins are diagnostic only.

## Output files

- `DCRRA4_DECISION.txt`
- `dcrra4_triangular_comparator_summary.json`
- `dcrra4_by_galaxy_triangular_comparator.csv`
- `dcrra4_class_triangular_summary.csv`
- `dcrra4_triangle_class_counts.csv`
- `dcrra4_dcrra3_vs_triangle_crosstab.csv`
- `dcrra4_triangular_comparator_report.md`

# DCRRA7 Dark-Component Residual Map

## Decision

`AUTHORIZE-DCRRA8-CLAIM-BOUNDED-SYNTHESIS`

## Purpose

DCRRA7 converts the DCRRA4 triangular comparator classes and DCRRA6 destructive/constructive null controls into a dark-component-like residual-regime map. This map is diagnostic only. It is not a physical dark-matter classification.

## Main results

- input population count: 143
- map zone count: 7
- response-family-zone count: 77
- NFW-comparator-zone count: 6
- mixed-zone count: 16
- pathology or nuisance pass-through count: 42
- DCRRA6 proxy-only reconstruction accuracy: 0.314685
- DCRRA6 proxy-only reconstruction balanced accuracy: 0.328735
- guard pass count: 8/8

## Map zone counts

| residual_map_zone                         |   galaxy_count |   fraction |
|:------------------------------------------|---------------:|-----------:|
| RESPONSE_FAMILY_DOMINANT_ZONE             |             54 |  0.377622  |
| NUISANCE_SENSITIVE_ZONE                   |             30 |  0.20979   |
| RESPONSE_FAMILY_WITH_NFW_COMPETITIVE_ZONE |             23 |  0.160839  |
| MIXED_THREE_WAY_COMPETITIVE_ZONE          |             16 |  0.111888  |
| PATHOLOGY_ARCHIVE_ZONE                    |             12 |  0.0839161 |
| HALO_COMPARATOR_DOMINANT_ZONE             |              6 |  0.041958  |
| UNRESOLVED_TRIANGULAR_ZONE                |              2 |  0.013986  |

## Map zone medians

| dcrra7_residual_map_zone                  |   galaxy_count |   median_best_n |   median_rrf_rc_over_rlast |   median_rrf_A_over_vouter2 |   median_v_outer_kms |   median_gas_fraction_proxy |   median_outer_baryon_fraction_proxy |   median_family_delta_aic_minus_nfw |   median_family_delta_aic_minus_rar |   proxy_supported_fraction |
|:------------------------------------------|---------------:|----------------:|---------------------------:|----------------------------:|---------------------:|----------------------------:|-------------------------------------:|------------------------------------:|------------------------------------:|---------------------------:|
| HALO_COMPARATOR_DOMINANT_ZONE             |              6 |           3     |                   0.365342 |                    0.67465  |              172     |                   0.0440717 |                             0.471051 |                            18.1752  |                           -78.1193  |                   0.666667 |
| MIXED_THREE_WAY_COMPETITIVE_ZONE          |             16 |           2.5   |                   0.364895 |                    0.724259 |              111.002 |                   0.0844548 |                             0.370301 |                            -2.48578 |                            -2.40919 |                   0.3125   |
| NUISANCE_SENSITIVE_ZONE                   |             30 |           1.625 |                   0.274508 |                    0.759405 |               84.25  |                   0.248966  |                             0.236112 |                           -10.4665  |                           -42.027   |                   0.7      |
| PATHOLOGY_ARCHIVE_ZONE                    |             12 |          12     |                   0.943367 |                    2.19759  |              174.25  |                   0.02633   |                             1.02261  |                            -8.24955 |                          -108.074   |                   0.25     |
| RESPONSE_FAMILY_DOMINANT_ZONE             |             54 |           2.25  |                   0.333515 |                    0.780486 |              111.255 |                   0.0424779 |                             0.363631 |                           -38.4234  |                           -78.459   |                   0.111111 |
| RESPONSE_FAMILY_WITH_NFW_COMPETITIVE_ZONE |             23 |           2.5   |                   0.189134 |                    0.679075 |              110.501 |                   0.0851628 |                             0.393274 |                            -3.61319 |                           -27.478   |                   0.26087  |
| UNRESOLVED_TRIANGULAR_ZONE                |              2 |           3.25  |                   0.520787 |                    0.798709 |               89.5   |                   0.128876  |                             0.44066  |                           -17.3106  |                            -6.24687 |                   0        |

## Interpretation

Dark-component-like rotation-curve residuals are not mapped as a single physical category. They separate into response-family-like, NFW-comparator-like, mixed, nuisance-sensitive, pathology/archive, and unresolved diagnostic zones. The DCRRA6 null controls support that the preceding triangular classes retain proxy-coherent structure, but the map remains a diagnostic taxonomy rather than a causal physical classification.

## Claim boundary

- No dark-matter exclusion claim.
- No Lambda-CDM replacement claim.
- No MOND/RAR falsification claim.
- No NFW-halo falsification claim.
- No Bullet-Cluster explanation claim.
- No particle-identity claim.
- No Hubble-tension solution claim.
- No SN-RRF as physical dark-matter substitute claim.
- Residual maps are diagnostic regime maps, not causal physical classifications.

## Output files

- `DCRRA7_DECISION.txt`
- `dcrra7_dark_component_residual_map_summary.json`
- `dcrra7_by_galaxy_residual_map.csv`
- `dcrra7_map_zone_counts.csv`
- `dcrra7_map_zone_summary.csv`
- `dcrra7_triangle_to_map_zone_crosstab.csv`
- `dcrra7_zone_evidence_tier_crosstab.csv`
- `dcrra7_zone_proxy_support_crosstab.csv`
- `dcrra7_dark_component_residual_map_report.md`

from pathlib import Path
import json
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]
required = [
    'paper/SN_RRF_DCRRA_integrated_consolidation_v3_0_1.pdf',
    'paper/SN_RRF_DCRRA_integrated_consolidation_v3_0_1.tex',
    'source_lineage/sn_rrf_v2_0_1/README.md',
    'source_lineage/sn_rrf_v2_0_1/paper/SN_RRF_claim_bounded_diagnostic_audit_v2_0_1.pdf',
    'source_lineage/dcrra_v1_0_1/README.md',
    'source_lineage/dcrra_v1_0_1/paper/DCRRA_claim_bounded_residual_regime_diagnostics_v1_0_1.pdf',
    'SOURCE_LINEAGE.md',
    'docs/history/SOURCE_LINEAGE_MAP_v3_0_1_complete.md',
]
for rel in required:
    assert (ROOT / rel).exists(), f'missing required file: {rel}'
feature = pd.read_csv(ROOT/'outputs/outputs_v3_0_0/residual_response_feature_table.csv')
fb = pd.read_csv(ROOT/'outputs/outputs_v3_0_0_phase9/phase9_failure_boundary_ledger.csv')
p8 = json.loads((ROOT/'outputs/outputs_v3_0_0_phase8/phase8_decision.json').read_text())
p8r = json.loads((ROOT/'outputs/outputs_v3_0_0_phase8r/phase8r_decision.json').read_text())
p9 = json.loads((ROOT/'outputs/outputs_v3_0_0_phase9/phase9_decision.json').read_text())
assert len(feature) == 143, len(feature)
assert feature['dcrra7_residual_map_zone'].nunique() == 7
assert len(fb) == 14, len(fb)
assert p8['status'] == 'FAIL_OR_NULL'
assert p8r['status'] == 'FAIL_OR_NULL'
assert p9['external_validation'] == 'HOLD_NON_SPARC_COMPONENT_CURVE_TABLE_NOT_AVAILABLE'
zen = json.loads((ROOT/'.zenodo.json').read_text())
assert 'doi' not in zen
assert zen['version'] == '3.0.1-integrated-complete-repository'
print('PASS-COMPLETE-REPOSITORY-PACKAGE-VERIFICATION')
print('feature_rows=143')
print('zone_count=7')
print('source_lineage=SN-RRF-v2.0.1 + DCRRA-v1.0.1')
print('phase9_failure_boundary_rows=14')
print('phase8_status=FAIL_OR_NULL')
print('phase8r_status=FAIL_OR_NULL')
print('external_validation=HOLD_NON_SPARC_COMPONENT_CURVE_TABLE_NOT_AVAILABLE')
print('zenodo_json_has_doi_field=False')

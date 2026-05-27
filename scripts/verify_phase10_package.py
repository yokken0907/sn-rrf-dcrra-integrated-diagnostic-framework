from pathlib import Path
import json, csv
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]
assert (ROOT/'paper/SN_RRF_DCRRA_integrated_consolidation_v3_0_1.pdf').exists(), 'missing integrated PDF'
assert (ROOT/'paper/SN_RRF_DCRRA_integrated_consolidation_v3_0_1.tex').exists(), 'missing integrated TEX'
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
print('PASS-PHASE10-INTEGRATED-CONSOLIDATION-PACKAGE-VERIFICATION')
print('feature_rows=143')
print('zone_count=7')
print('phase9_failure_boundary_rows=14')
print('phase8_status=FAIL_OR_NULL')
print('phase8r_status=FAIL_OR_NULL')
print('external_validation=HOLD_NON_SPARC_COMPONENT_CURVE_TABLE_NOT_AVAILABLE')

from pathlib import Path
import csv, hashlib, sys
ROOT = Path(__file__).resolve().parents[1]
manifest = ROOT/'FILE_MANIFEST.csv'
def sha256(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for chunk in iter(lambda: f.read(1<<20), b''):
            h.update(chunk)
    return h.hexdigest()
errors=[]
with open(manifest, newline='', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        p=ROOT/row['path']
        if not p.exists():
            errors.append(f"missing: {row['path']}")
            continue
        if str(p.stat().st_size) != str(row['size_bytes']):
            errors.append(f"size mismatch: {row['path']}")
        if sha256(p) != row['sha256']:
            errors.append(f"sha256 mismatch: {row['path']}")
if errors:
    print('FAIL-MANIFEST-VERIFICATION')
    for e in errors: print(e)
    sys.exit(1)
print('PASS-MANIFEST-VERIFICATION')
print(f'verified_files={sum(1 for _ in open(manifest, encoding="utf-8"))-1}')

"""Build the flat census the integrator recount scripts read.

    python3 analysis/integrate/b14_11_census_extract.py

Writes census_all.jsonl under results/integrate/b14_11_replay (override with
GCT_WORK), concatenating the delivered per-(delta,ell) census files.
"""
import os, pathlib, sys
ROOT = pathlib.Path(os.environ.get('GCT_ROOT', pathlib.Path(__file__).resolve().parents[2]))
WORK = pathlib.Path(os.environ.get('GCT_WORK', ROOT / 'results' / 'integrate' / 'b14_11_replay'))
WORK.mkdir(parents=True, exist_ok=True)
out = WORK / 'census_all.jsonl'
n = 0
with out.open('w') as fh:
    for d in range(5, 9):
        for l in range(5, 9):
            f = ROOT / 'results' / 'b14_11' / f'census_d{d}_l{l}.jsonl'
            if not f.exists():
                continue
            for line in f.read_text().splitlines():
                if line.strip():
                    fh.write(line + chr(10)); n += 1
print(f'{n} labels -> {out}')
if n != 4198:
    sys.exit(f'expected 4198 labels, got {n}')

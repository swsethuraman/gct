"""Portable discovery index. Never promotes sampled nullity to an identity."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'results/integration'

def read(p):
    return json.loads((ROOT / p).read_text(encoding='utf-8'))

def rows(p):
    return [json.loads(s) for s in (ROOT / p).read_text(encoding='utf-8').splitlines() if s.strip()]

def dump(name, obj):
    (OUT / name).write_text(json.dumps(obj, indent=2) + '\n', encoding='utf-8')

def build():
    OUT.mkdir(parents=True, exist_ok=True)
    cells = {}
    for p in sorted((ROOT / 'results/b13_11').glob('ledger.part*.jsonl')):
        for x in rows(p.relative_to(ROOT)):
            cells[x['id']] = x
    before = len(cells)
    imported = Counter()
    def observe(x, source, n=3, family='per3'):
        lam = tuple(x.get('mu', x.get('lam', [])))
        d, a = x['delta'], x['a']
        assert all(v > 0 for v in lam) and list(lam) == sorted(lam, reverse=True)
        assert sum(lam) == n*d
        key = f'n{n}:d{d}:' + ','.join(map(str, lam))
        cell = cells.setdefault(key, dict(id=key,n=n,delta=d,lam=list(lam),a=a,observations=[],sides={}))
        assert cell['a'] == a, ('ambient conflict', key)
        pp = {p: v['mult_det' if family == 'det' else 'mult'] for p,v in x['per_prime'].items()}
        assert set(pp) == {'2147483647','2147483629'} and all(v == a for v in pp.values())
        cell['observations'].append(dict(source=source,reported_a=a,ranks={family:a},
            per_prime={family:pp},verification='producer_exact_full_rank; integration_record_check_only'))
        side = cell['sides'].setdefault(family, {})
        side.update(rank_floor=a,exact_rank=a,full_rank=True,ideal_dimension_interval=[0,0],
                    status='ADOPTED producer result; independent replay not claimed')
        side.setdefault('evidence', []).append(source)
        imported[source.split(':')[0]] += 1
    paths = ['results/b13_08/per6_d10.jsonl'] + [
        f'results/b13_09/per_r{r}_d{d}.jsonl' for r,d in [(7,7),(7,8),(8,8),(7,9),(8,9)]]
    for p in paths:
        for i,x in enumerate(rows(p),1): observe(x, f'{p}:{i}')
    observe(read('results/b13_10/pilot.json'), 'results/b13_10/pilot.json',4,'det')
    values = sorted(cells.values(), key=lambda x:x['id'])
    parts = []
    for offset in range(0,len(values),1000):
        name = f'cells.part{offset//1000:02d}.jsonl'; parts.append(name)
        (OUT/name).write_text(''.join(json.dumps(x,separators=(',',':'))+'\n' for x in values[offset:offset+1000]),encoding='utf-8')
    tracked = subprocess.check_output(['git','ls-files','--stage','-z'],cwd=ROOT).decode().split('\0')
    artifacts = []
    for entry in tracked:
        if not entry: continue
        meta, name = entry.split('\t',1)
        if not name.startswith(('results/','docs/','analysis/')) or name.startswith('results/integration/'): continue
        p=ROOT/name
        if not p.is_file(): continue
        h=hashlib.sha256()
        with p.open('rb') as f:
            for chunk in iter(lambda:f.read(1048576),b''): h.update(chunk)
        artifacts.append(dict(path=name,bytes=p.stat().st_size,working_tree_sha256=h.hexdigest(),
                              git_index_blob=meta.split()[1]))
    (OUT/'artifacts.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in artifacts),encoding='utf-8')
    parsed = sorted({o['source'].split(':')[0] for x in values for o in x['observations']})
    # Visibility is file-level for unparsed sources, not a claim of semantic completeness.
    unparsed = [x['path'] for x in artifacts if x['path'].startswith('results/') and
                x['path'].endswith(('.json','.jsonl')) and x['path'] not in parsed]
    summary = dict(baseline_cells=before,current_cells=len(cells),new_observations=dict(imported),
        cell_parts=parts,indexed_artifacts=len(artifacts),parsed_observation_sources=len(parsed),
        unparsed_result_files=len(unparsed),coverage_claim='Tracked docs/results/analysis files indexed; not all historical results semantically parsed',
        pending=['Independent replay of producer rank results','Missing/unshipped historical certificates',
                 'Shared production runtime integration tests','New source-specific parsers and inherited-rule reapplication'],
        frontier_provenance='Reviewed integration conclusions; not recomputed by this discovery index',
        current_frontiers=dict(global_equality_through_degree=8,cubic_degree9_length7=47,
          cubic_degree9_length8=52,cubic_degree10_length6=58,lmr_D_interval=[-4,1]))
    dump('coverage.json',summary); dump('unparsed_sources.json',unparsed)
    dump('parsed_sources.json',parsed)
    print(json.dumps(summary))

def find(term):
    term=term.lower()
    summary=read('results/integration/coverage.json')
    count=0
    for name in summary['cell_parts']+['artifacts.jsonl']:
        for line in (OUT/name).read_text(encoding='utf-8').splitlines():
            if term in line.lower():
                x=json.loads(line)
                print(json.dumps({k:x[k] for k in ('id','a','sides','D_interval','path') if k in x}))
                count+=1
                if count>=40:
                    print('Showing first 40 matches; refine search.'); return
    print(f'{count} matches')

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('command',choices=['build','find']); ap.add_argument('term',nargs='?')
    args=ap.parse_args()
    if args.command=='build': build()
    elif args.term: find(args.term)
    else: ap.error('find requires a search term')

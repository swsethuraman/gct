"""Frozen input, source convention and point-contract audit; not a rank sweep."""
from collections import Counter
from math import factorial
from pathlib import Path
import copy
import hashlib
import json
import subprocess
from b14_05_controls import require, rejects, REJECTIONS, PRIMES

BASE = '9898e56941a7665f231873481dae956f08509995'
TREE = 'cb688cd3fe454d638f3202e759e2eaa0c629739f'


def git(*args):
    return subprocess.check_output(['git', *args], text=True).strip()


def check_points(data):
    r, degree = data['r'], data['degree']
    expected = {13: (39, 73, 96, 20), 14: (93, 159, 192, 20)}[degree]
    require(r == 9, 'wrong variable count')
    require((data['source_dimension_adopted'], data['normalization_target_dimension'],
             data['primary_point_count'], data['holdout_point_count']) == expected,
            'point metadata mismatch; dimensions are adopted only')
    exponents = data['cubic_exponents']
    require(len(exponents) == 165 and len(set(map(tuple, exponents))) == 165, 'cubic exponents incomplete')
    require(all(len(a) == r and sum(a) == 3 and min(a) >= 0 for a in exponents), 'bad cubic exponents')
    index = exponents.index([3]+[0]*(r-1))
    pts = data['points']
    require(len(pts) == expected[2]+expected[3] and len({p['id'] for p in pts}) == len(pts), 'missing or duplicate points')
    require(Counter(p['role'] for p in pts) == {'primary': expected[2], 'holdout': expected[3]}, 'point roles')
    rows = []
    for p in pts:
        require(len(p['linear']) == r and len(p['cubic_coefficients']) == 165, 'malformed point')
        require(all(isinstance(x, int) and abs(x) <= 7 for x in p['linear']+p['cubic_coefficients']), 'point arithmetic model')
        u = p['linear'][0]*p['cubic_coefficients'][index]
        require(u != 0 and all(u % q for q in PRIMES), 'u is zero')
        require(p['u_symbol'] == 24*u, 'u_symbol must be 24 times ordinary u')
        rows.append({'id': p['id'], 'role': p['role'], 'u': u, 'msym_u': 24*u})
    return rows


def filling_valid(f):
    require(f['n'] == 4 and f['h'] == 9, 'source shape convention')
    cols = [f['C1'], f['C2']]+f['two']+[[i] for i in f['one']]
    count = Counter(i for col in cols for i in col)
    require(len(f['two']) == 15 and len(f['one']) == 4*f['delta']-48, 'column counts')
    require(set(count) == set(range(f['delta'])) and set(count.values()) == {4}, 'letter counts')
    require(all(len(col) == len(set(col)) for col in cols), 'repeated column letter')


def main():
    require(git('log', '-1', '--format=%H', 'batch14-base') == BASE, 'base commit mismatch')
    require(git('log', '-1', '--format=%T', 'batch14-base') == TREE, 'base tree mismatch')
    manifest = json.loads(Path('results/b14_05/input_manifest.json').read_text(encoding='utf-8-sig'))
    for row in manifest:
        require(git('rev-parse', BASE+':'+row['path']) == row['git_blob'], 'input blob mismatch: '+row['path'])
    contract_blobs = {'results/b14_prep/points/P13.json': '76e1f2ed7be8ba85e14ba74cae5be76504f67072',
                      'results/b14_prep/points/P14.json': 'ebb595c0e61b85bbb1d380caa58d90d80ad133f2',
                      'results/s74/source.json': 'ca17e74393228d9c3d9729e7839f0157cb1e21eb'}
    for path, blob in contract_blobs.items():
        require(git('rev-parse', BASE+':'+path) == blob, 'board blob mismatch')
    source = json.loads(Path('results/s74/source.json').read_text())
    require(source['complete'] is True and len(source['entries']) == source['size'] == 274, 'source missing')
    count = Counter()
    for entry in source['entries']:
        t = entry['rung']; count[t] += 1
        filling_valid(entry['native']); filling_valid(entry['literal'])
        require(entry['native']['delta'] == t and entry['literal']['delta'] == 24, 'source degree')
        require(entry['exponent'] == 24-t and entry['factorial_scalar'] == 24**(24-t), 'source scaling')
    require({str(k): v for k, v in count.items()} == source['birth_profile'], 'birth profile mismatch')
    require(sum(v for t, v in count.items() if t <= 13) == 39, 'degree-13 source row count')
    require(sum(v for t, v in count.items() if t <= 14) == 93, 'degree-14 source row count')
    points = {}
    for d in (13, 14):
        data = json.loads(Path(f'results/b14_prep/points/P{d}.json').read_text())
        points[str(d)] = {'status': 'arithmetic input audit only; no evaluations or target minor',
                          'point_file': f'results/b14_prep/points/P{d}.json',
                          'values_are': 'ordinary u and literal msym_u=24u, recomputed from point definitions',
                          'u_values': check_points(data)}
        mutant = copy.deepcopy(data); mutant['points'] = []
        rejects(f'P{d} missing points', lambda mutant=mutant: check_points(mutant))
        mutant = copy.deepcopy(data); mutant['points'][0]['linear'][0] = 0
        rejects(f'P{d} zero u', lambda mutant=mutant: check_points(mutant))
        mutant = copy.deepcopy(data); mutant['points'][0]['u_symbol'] += 1
        rejects(f'P{d} wrong u scaling', lambda mutant=mutant: check_points(mutant))
    census = json.loads(Path('results/b13_06/components.json').read_text())
    require(census['meaning'] == 'Tensor-domain decomposition, NOT the multiplication image.', 'census semantics')
    # Read complete frozen packet input, but do not duplicate slot 08's reachability work.
    require(len(census['rows']) == 336, 'frozen input rows missing')
    record = {'status': 'PASS input/convention audit, not CI certification', 'base_commit': BASE, 'base_tree': TREE,
              'input_blob_checks': len(manifest), 'board_blob_contracts': contract_blobs,
              'source_native_counts': dict(count), 'source_rows_13_14': [39, 93],
              'census': '336 frozen rows parsed; no decomposition or reachability recomputed',
              'points': points, 'negative_controls': REJECTIONS}
    Path('results/b14_05/input_audit.json').write_text(json.dumps(record, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': record['status'], 'point_counts': {d: len(v['u_values']) for d, v in points.items()},
                      'negative_controls': len(REJECTIONS)}))


if __name__ == '__main__':
    main()

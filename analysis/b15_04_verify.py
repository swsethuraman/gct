"""Independent exact replay of the B15-04 exported small source witness.

Does not import the producer, its determinant expansion, or its raising code.
"""
import hashlib
import json
from pathlib import Path
import time
import sympy as s
from flint import fmpz_mat

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'results/b15_04'


def main():
    t = time.perf_counter()
    raw = (OUT / 'controls.json').read_bytes()
    record = json.loads(raw)
    source = record['source']
    assert source['lam'] == [6, 2] and source['delta'] == 2
    point = record['point']['pencil']
    # Interpolate all ordinary coefficients using exact independent determinants.
    values = []
    for x in range(5):
        mat = [[point[0][i][j]+x*point[1][i][j] for j in range(4)] for i in range(4)]
        values.append(int(fmpz_mat(mat).det()))
    coeffs = s.Matrix([[x**k for k in range(5)] for x in range(5)]).inv()*s.Matrix(values)
    assert all(v.q == 1 for v in coeffs)
    co = {(4-k, k): int(v) for k, v in enumerate(coeffs)}
    # Expand the Leibniz raising action on the exported monomial source.
    raised = {}
    evaluated = 0
    for mon, weight in source['terms']:
        term_value = int(weight)
        for al in mon:
            term_value *= co[tuple(al)]
        evaluated += term_value
        for k, al in enumerate(mon):
            if al[1] == 0:
                continue
            new_mon = [tuple(x) for x in mon]
            new_mon[k] = (al[0]+1, al[1]-1)
            key = tuple(sorted(new_mon))
            raised[key] = raised.get(key, 0)+weight*(al[0]+1)
    assert all(v == 0 for v in raised.values())
    assert evaluated == record['exact_value'] == -1597
    assert all(evaluated % p for p in record['primes'])
    sizing = json.loads((OUT / 'sizing.json').read_text())
    checked_hashes = 0
    for name, hashes in sizing['input_hashes'].items():
        payload = (ROOT / name).read_bytes()
        assert hashlib.sha256(payload).hexdigest() == hashes['sha256_exact']
        checked_hashes += 1
    for row in sizing['cells']:
        b = row['signed_burnside']
        assert sum(x['class_size'] for x in b['classes']) == b['stabilizer_order']
        assert sum(x['class_size']*x['character']*x['fixed_monomials'] for x in b['classes']) == b['n_chi']*b['stabilizer_order']
        assert row['h_pad'] == sum(x['a3'] for x in row['channels'])
        assert row['U_pad_ub'] == min(row['a'], row['h_pad'], row['a']-row['L_pad_lb']) == 3
    result = dict(status='EXACT', verifier_model='gpt-6-astra', small_source_value=evaluated,
                  full_raising_identity=True, coefficient_method='exact Vandermonde interpolation of FLINT integer determinants',
                  witness_sha256=hashlib.sha256(raw).hexdigest(), frozen_input_hashes_checked=checked_hashes,
                  research_rank_claims=False, wall_seconds=time.perf_counter()-t)
    (OUT / 'independent_replay.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(result))


if __name__ == '__main__':
    main()

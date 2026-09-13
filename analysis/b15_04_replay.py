"""Replay only the compact integral certificates and their explicit points.

No carrier build, stored raising matrix, modular kernel, or rational
reconstruction is needed. Coefficients use a fresh Leibniz determinant expansion.
"""
import hashlib
import itertools
import json
import math
from pathlib import Path
import time
import numpy as np
from flint import fmpz_mat
from b15_04_integral import verify_raising, multiset_code

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'results/b15_04'


def determinant_coefficients(point):
    r = len(point)
    answer = {}
    for pi in itertools.permutations(range(4)):
        inversions = sum(pi[i] > pi[j] for i in range(4) for j in range(i+1, 4))
        product = {(0,)*r: (-1)**inversions}
        for row in range(4):
            nxt = {}
            for alpha, c in product.items():
                for j in range(r):
                    beta = list(alpha); beta[j] += 1; beta = tuple(beta)
                    nxt[beta] = nxt.get(beta, 0)+c*point[j][row][pi[row]]
            product = nxt
        for alpha, c in product.items():
            answer[alpha] = answer.get(alpha, 0)+c
    return answer


def main():
    start = time.perf_counter()
    records = []
    for cell in (1, 2):
        cert = json.loads((OUT/f'cell{cell}_integral_certificate.json').read_text())
        path = ROOT/cert['source_npz']
        assert hashlib.sha256(path.read_bytes()).hexdigest() == cert['source_sha256']
        data = np.load(path)
        M, C, letters = data['monomials'], data['coefficients'], data['letters']
        assert np.issubdtype(C.dtype, np.integer) and C.shape == (len(M), 3)
        assert np.all(M[:, 1:] >= M[:, :-1])
        assert len(np.unique(multiset_code(M, len(letters)))) == len(M)
        assert np.all(letters.sum(axis=1) == 4)
        assert np.all(letters[M].sum(axis=1) == cert['lam'])
        raising = verify_raising(M, C, letters)
        p = cert['prime']
        values = []
        for point in cert['points']:
            co = determinant_coefficients(point)
            for s in ([1, 0, 0, 0, 0, 0, 0], [1, 1, -1, 2, -2, 3, 1]):
                direct = int(fmpz_mat([[sum(s[j]*point[j][a][b] for j in range(7)) for b in range(4)] for a in range(4)]).det())
                assert sum(c*math.prod(x**v for x, v in zip(s, alpha)) for alpha, c in co.items()) == direct
            cv = np.array([co.get(tuple(alpha), 0) % p for alpha in letters], dtype=np.int64)
            term = np.ones(len(M), dtype=np.int64)
            for k in range(M.shape[1]):
                term = term*cv[M[:, k]] % p
            assert len(M)*(p-1) < 2**63
            values.append([int(((term*(C[:, j] % p)) % p).sum() % p) for j in range(3)])
        assert values == cert['values']
        determinant = int(fmpz_mat(values).det()) % p
        assert determinant == cert['determinant_minor_mod_p'] and determinant != 0
        # Adding a lone monomial is a deliberately faulty source at this weight.
        try:
            verify_raising(M[:1], np.array([[1, 0, 0]], dtype=np.int64), letters)
        except AssertionError:
            mutation_rejected = True
        else:
            raise AssertionError('source defect control was vacuous')
        records.append(dict(cell=cell, status='REPLAYED_RANK_FLOOR', m_det_lb=3,
                            source_sha256=cert['source_sha256'], prime=p,
                            determinant_minor_mod_p=determinant, all_raising_exact=True,
                            independent_point_expansion=True, source_mutation_rejected=mutation_rejected))
        print('COMPACT REPLAY PASS cell', cell, flush=True)
    receipt = dict(status='REPLAYED_RANK_FLOOR', model='gpt-6-astra', cells=records,
                   wall_seconds=time.perf_counter()-start,
                   scope='fresh polynomial evaluation and exact expanded raising identities from compact integral sources')
    (OUT/'compact_replay.json').write_text(json.dumps(receipt, indent=2)+'\n', encoding='utf-8')


if __name__ == '__main__':
    main()

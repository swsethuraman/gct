"""Reconstruct compact integral sources; independently verify polynomial raising.

This is an exact certificate step, not an additional source or point search.
"""
import hashlib
import argparse
import itertools
import json
import math
import time
import numpy as np
from scipy import sparse
from flint import fmpz_mat
import b15_04_panel as panel


def reconstruct(x, p):
    if not x:
        return 0, 1
    bound = math.isqrt(p//2)
    r0, r1, t0, t1 = p, int(x), 0, 1
    while abs(r1) > bound:
        q = r0//r1
        r0, r1, t0, t1 = r1, r0-q*r1, t1, t0-q*t1
    if t1 < 0:
        r1, t1 = -r1, -t1
    assert 0 < t1 <= bound and math.gcd(r1, t1) == 1 and (r1-x*t1) % p == 0
    return r1, t1


def multiset_code(M, L):
    # Exact integer combinadic, independently assembled from the formula.
    assert math.comb(L+M.shape[1]-1, M.shape[1]) < 2**63
    v = np.zeros(len(M), dtype=np.int64)
    for k in range(M.shape[1]):
        tab = np.array([math.comb(j+k, k+1) for j in range(L)], dtype=np.int64)
        v += tab[M[:, k]]
    return v


def verify_raising(M, C, letters):
    """Different construction: differentiate exported full polynomial terms."""
    index = {tuple(a): j for j, a in enumerate(letters.tolist())}
    result = []
    for i in range(letters.shape[1]-1):
        codes, vals = [], []
        replacement_table = np.zeros(len(letters), dtype=M.dtype)
        for j, al in enumerate(letters.tolist()):
            if al[i+1]:
                al[i] += 1; al[i+1] -= 1
                replacement_table[j] = index[tuple(al)]
        for k in range(M.shape[1]):
            al = letters[M[:, k]]
            use = al[:, i+1] > 0
            if not np.any(use):
                continue
            replacements = replacement_table[M[use, k]]
            mm = M[use].copy(); mm[:, k] = replacements; mm.sort(axis=1)
            codes.append(multiset_code(mm, len(letters)))
            vals.append(C[use]*(al[use, i:i+1]+1))
        code = np.concatenate(codes)
        value = np.vstack(vals)
        # Sums are exact signed int64, with a conservative total-sum bound.
        assert len(value)*int(np.abs(value).max(initial=0)) < 2**63
        order = np.argsort(code)
        st = np.r_[0, np.nonzero(np.diff(code[order]))[0]+1]
        reduced = np.add.reduceat(value[order], st, axis=0)
        assert not np.any(reduced), ('nonzero exact raising', i)
        result.append(dict(operator=[i, i+1], derivative_contributions=len(code),
                           distinct_monomials=len(st), exact_zero=True))
        print('EXACT RAISING', i, 'contributions', len(code), flush=True)
    return result


def one(cell):
    t = time.perf_counter()
    tag = 'cell'+str(cell)
    rank = json.loads((panel.OUT/(tag+'_rank.json')).read_text())
    p = rank['prime']
    K = np.load(panel.OUT/(tag+'_kernel.npz'))['K'].astype(np.int64)
    values = rank['values']
    columns = next(cols for cols in itertools.combinations(range(K.shape[1]), 3)
                   if int(fmpz_mat([[row[j] for j in cols] for row in values]).det()) % p)
    Z = np.zeros((len(K), 3), dtype=np.int64)
    scales = []
    for j, col in enumerate(columns):
        unique = np.unique(K[:, col])
        rat = {int(x): reconstruct(int(x), p) for x in unique}
        den = math.lcm(*(v[1] for v in rat.values()))
        ints = {x: n*(den//d) for x, (n, d) in rat.items()}
        gcd = math.gcd(*ints.values())
        ints = {x: n//gcd for x, n in ints.items()}
        assert max(abs(x) for x in ints.values()) < 2**40
        Z[:, j] = np.array([ints[int(x)] for x in K[:, col]], dtype=np.int64)
        scale = den*pow(gcd, -1, p) % p
        assert np.array_equal(Z[:, j] % p, K[:, col]*scale % p)
        scales.append(scale)
    data = np.load(panel.OUT/(tag+'_native.npz'))
    E = sparse.csr_matrix((data['E_data'], data['E_indices'], data['E_indptr']), shape=tuple(data['E_shape']))
    bound = int(np.diff(E.indptr).max())*int(np.abs(E.data.astype(np.int64)).max())*int(np.abs(Z).max())
    assert bound < 2**63 and not np.any(E @ Z)
    co, sgn, raw = data['col_of'], data['sgn'], data['M']
    selected = np.nonzero(co >= 0)[0]
    selected = selected[np.any(Z[co[selected]] != 0, axis=1)]
    M = raw[selected]
    C = Z[co[selected]]*sgn[selected, None]
    letters = np.array(panel.exps(4, 7), dtype=np.int16)
    print(tag, 'integral terms', len(M), 'max coefficient', int(np.abs(C).max()), flush=True)
    # Revised after the 296730-term measurement: precomputed letter lookup
    # removes per-term Python lists. The native Job Object cap stays unchanged.
    assert len(M) <= 400000, 'expanded certificate exceeds measured small-verification cost gate'
    raising = verify_raising(M, C, letters)
    matrix = []
    for point in rank['points']:
        coefficients = panel.det_coefficients(point)
        cv = np.array([coefficients.get(tuple(a), 0) % p for a in letters], dtype=np.int64)
        value = np.ones(len(M), dtype=np.int64)
        for k in range(M.shape[1]):
            value = value*cv[M[:, k]] % p
        row = [int(((value*(C[:, j] % p)) % p).sum() % p) for j in range(3)]
        matrix.append(row)
    expected = [[row[col]*scales[j] % p for j, col in enumerate(columns)] for row in values]
    assert matrix == expected
    det = int(fmpz_mat(matrix).det()) % p
    assert det
    source_path = panel.OUT/(tag+'_integral_source.npz')
    np.savez_compressed(source_path, monomials=M, coefficients=C, letters=letters)
    assert source_path.stat().st_size < 5000000
    record = dict(status='EXACT', model='gpt-6-astra', n=4, delta=8, lam=rank['lam'],
                  ambient_variables=16, restriction_variables=7,
                  coefficient_convention='ordinary c_alpha; no factorial scaling',
                  source_npz=source_path.relative_to(panel.ROOT).as_posix(),
                  source_sha256=hashlib.sha256(source_path.read_bytes()).hexdigest(),
                  source_columns=list(columns), integral_coefficient_max=int(np.abs(C).max()),
                  union_monomials=len(M), per_source_terms=np.count_nonzero(C, axis=0).tolist(),
                  raising_verifier='independent Leibniz differentiation of expanded ordinary-coefficient polynomial',
                  raising=raising, exact_integer_E_check=True, prime=p,
                  values=matrix, determinant_minor_mod_p=det, points=rank['points'],
                  m_det_lb=3, U_pad_ub=3, D_ub=0,
                  rational_source_justification='explicit integral highest-weight polynomials with all simple raising identities checked over Z',
                  wall_seconds=time.perf_counter()-t)
    panel.save(tag+'_integral_certificate.json', record)
    print(tag, 'INTEGRAL CERTIFICATE PASS', 'minor', det, 'seconds', round(time.perf_counter()-t, 3), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--cell', type=int, choices=[1, 2], required=True)
    one(parser.parse_args().cell)

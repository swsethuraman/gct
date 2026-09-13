"""B15-04 bounded controls, exact sizing, and sparse construction pilot.

Uses banked B13/B14 construction with original attribution; new orchestration,
independent direct evaluation, resource decisions, and receipts: gpt-6-astra.
"""
import argparse
from fractions import Fraction
import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import random
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'results/b15_04'
sys.path[:0] = [str(ROOT / 'analysis'), str(ROOT / 'tools/integrate')]
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
import numpy as np
from flint import fmpz_mat, nmod_mat
import scipy
from scipy import sparse
import sympy
import wk11_s71_codes
wk11_s71_codes.install()
import wk13_b10_lean as lean
import wk9_s45_build as old
from wk8_s30_core import exps, restrict, det_form, build_R
from wk8_s30_pleth import pleth_p, chi
from b14_11_sizes import burnside, controls as sizing_controls
from exclusion_predicates import conclusions_for

PRIMES = [2147483647, 2147483629]
CELLS = [(11, 11, 5, 2, 1, 1, 1), (12, 11, 4, 2, 1, 1, 1)]
INPUTS = ['docs/batch15/WORKER_PREAMBLE.md', 'docs/batch15/ACCEPTED_STATE.md',
          'docs/batch15/briefs/B15-04.md', 'results/b15_prep/small_panel_sizing.json',
          'analysis/b14_11_work.py', 'analysis/b14_12_cell.py', 'analysis/b14_12_families.py',
          'analysis/b14_11_sizes.py', 'analysis/wk13_b10_lean.py', 'analysis/wk11_s71_codes.py',
          'analysis/wk9_s45_build.py', 'analysis/wk8_s30_core.py', 'analysis/wk8_s30_pleth.py',
          'results/integrate/inherited_exclusions.json', 'results/b15_prep/transport_overlay.json',
          'results/b15_prep/shortlist_overlay.json', 'analysis/b15_bound.py']


def clean(obj):
    if isinstance(obj, dict):
        return {str(k): clean(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [clean(v) for v in obj]
    if isinstance(obj, np.generic):
        return clean(obj.item())
    if isinstance(obj, float) and not math.isfinite(obj):
        return None
    return obj


def save(name, obj):
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text(json.dumps(clean(obj), indent=2, allow_nan=False) + '\n', encoding='utf-8')


def hashes():
    return {f: dict(sha256_exact=hashlib.sha256((ROOT / f).read_bytes()).hexdigest(),
                    sha256_utf8_lf=hashlib.sha256((ROOT / f).read_bytes().replace(b'\r\n', b'\n')).hexdigest())
            for f in INPUTS}


def count_a(lam, d, n=4):
    value = sum((cf * chi(tuple(lam), rho) for rho, cf in pleth_p(d, n).items()), Fraction())
    assert value.denominator == 1 and value >= 0
    return int(value)


def strips(lam, d):
    lo = tuple(lam[1:]) + (0,)
    for nu in itertools.product(*(range(lo[i], lam[i] + 1) for i in range(len(lam)))):
        if sum(nu) == 3 * d:
            yield tuple(x for x in nu if x)


def ledger(lam):
    index = json.loads((ROOT / 'results/integrate/inherited_exclusions.json').read_text())
    c = dict(n=4, ell=len(lam), delta=8, **{'lambda': list(lam)})
    contexts = sorted({k for v in index['application_contract']['conclusions_by_id'].values() for k in v})
    hits = {ct: conclusions_for(index, c, ct) for ct in contexts}
    overlay = json.loads((ROOT / 'results/b15_prep/transport_overlay.json').read_text())
    matches = [x for x in overlay['targets'] if x['degree'] == 8 and x['lam'] == list(lam)]
    shortlist = json.loads((ROOT / 'results/b15_prep/shortlist_overlay.json').read_text())
    removed = [x for x in shortlist['removed_queue_entries'] if x['delta'] == 8 and x['lam'] == list(lam)]
    return dict(typed_ledger_hits=hits, transport_overlay_matches=matches, shortlist_removals=removed)


def exact_sizing():
    receipt = dict(status='EXACT', model='gpt-6-astra', input_hashes=hashes(),
                   controls=sizing_controls(), cells=[])
    bank = json.loads((ROOT / 'results/b15_prep/small_panel_sizing.json').read_text())
    for lam in CELLS:
        t = time.perf_counter()
        b = burnside(lam, 8)
        a = count_a(lam, 8)
        channels = [dict(nu=nu, a3=count_a(nu, 8, 3)) for nu in strips(lam, 8)]
        h = sum(x['a3'] for x in channels)
        expected = next(x for x in bank['cells'] if x['target']['lam'] == list(lam))
        assert (a, h, b['N_S'], b['n_chi']) == (expected['target']['a'], expected['target']['h_pad'],
                                               expected['sizing']['N_S'], expected['sizing']['n_chi'])
        nc = b['n_chi']
        ent = dict(lam=lam, n=4, delta=8, ambient_variables=16, restriction_variables=7,
                   a=a, h_pad=h, L_pad_lb=0, U_pad_ub=min(a, h), signed_burnside=b,
                   channels=channels, ledger=ledger(lam), wall_seconds=time.perf_counter()-t,
                   dense_square_uint32_bytes=4*nc*nc, dense_square_int64_bytes=8*nc*nc,
                   raw_monomials_int16_bytes=2*8*b['N_S'],
                   naive_stabilizer_quotient=str(Fraction(b['N_S'], b['stabilizer_order'])))
        receipt['cells'].append(ent)
        save('sizing.json', receipt)
        print(json.dumps({k: ent[k] for k in ('lam', 'a', 'h_pad', 'wall_seconds')}), flush=True)
        chi.cache_clear()
    return receipt


def pencil(seed, r, diagonal=False):
    rng = random.Random(seed)
    return [[[rng.randint(-3, 3) if not diagonal or a == b else 0 for b in range(4)]
             for a in range(4)] for _ in range(r)]


def det_coefficients(pt):
    f, nvars = det_form(4)
    return restrict(f, nvars, 4, len(pt), [[v for row in mat for v in row] for mat in pt])


def direct_det_at(pt, s):
    mat = [[sum(s[i]*pt[i][a][b] for i in range(len(s))) for b in range(4)] for a in range(4)]
    return int(fmpz_mat(mat).det())


def poly_at(co, s):
    return sum(v*math.prod(x**e for x, e in zip(s, al)) for al, v in co.items())


def eval_orbits(arr, co, p, r, chunk=50000):
    """Ordinary c_alpha products; banked signed integral orbit coefficients."""
    cv = np.array([co.get(al, 0) % p for al in exps(4, r)], dtype=np.int64)
    result = np.zeros(arr['n_chi'], dtype=np.int64)
    for start in range(0, len(arr['M']), chunk):
        end = min(start+chunk, len(arr['M']))
        cols = arr['col_of'][start:end]
        use = cols >= 0
        m = arr['M'][start:end][use]
        val = np.ones(len(m), dtype=np.int64)
        for j in range(m.shape[1]):
            val = val * cv[m[:, j]] % p
        val = val * arr['sgn'][start:end][use] % p
        np.add.at(result, cols[use], val)
        result %= p
    return result


def expanded_source(arr, vector, r):
    letters = exps(4, r)
    return [[[[int(v) for v in letters[k]] for k in row], int(sign)*int(vector[col])]
            for row, col, sign in zip(arr['M'], arr['col_of'], arr['sgn']) if col >= 0 and vector[col]]


def eval_terms(terms, co):
    return sum(c*math.prod(co.get(tuple(a), 0) for a in mon) for mon, c in terms)


def triangular_solve(T, dinv, B, p):
    """Upper triangular solve using signed small entries and checked int64 sums."""
    X = np.asarray(B, dtype=np.int64).copy() % p
    signed = T.data.astype(np.int64).copy()
    signed[signed > p//2] -= p
    row_bound = int(np.diff(T.indptr).max(initial=0))*int(np.abs(signed).max(initial=0))
    assert (row_bound+1)*(p-1) < 2**63
    for i in range(T.shape[0]-1, -1, -1):
        start, end = T.indptr[i:i+2]
        js = T.indices[start:end]
        vs = signed[start:end]
        assert np.all(js >= i)
        other = js != i
        X[i] = ((X[i] - vs[other] @ X[js[other]]) % p)*int(dinv[i]) % p
    return X


def residual_probe(E, cov, p, width=16):
    """Measure one narrow residual block; not a kernel or rank certificate."""
    t = time.perf_counter()
    nc = E.shape[1]
    S, U = cov['S'], cov['U']
    colS = np.full(nc, -1, dtype=np.int32); colS[S] = np.arange(len(S))
    colU = np.full(nc, -1, dtype=np.int32); colU[U] = np.arange(len(U))
    T, dinv, TU = lean._split_rows_safe(E, cov['rows'], colS, colU, p)
    split_seconds = time.perf_counter()-t
    width = min(width, len(U))
    if not width:
        return dict(nU=0, split_seconds=split_seconds, measured_columns=0)
    t = time.perf_counter()
    X = triangular_solve(T, dinv, TU[:, :width].toarray(), p)
    solve_seconds = time.perf_counter()-t
    # V has the selected U identity and negative T^{-1}TU in the S rows.
    V = np.zeros((nc, width), dtype=np.int64)
    V[S] = (-X) % p
    V[U[:width]] = np.eye(width, dtype=np.int64)
    # An entrywise int64 bound holds for the sparse dot product, before modulo.
    raw_bound = int(np.diff(E.indptr).max(initial=0))*int(np.abs(E.data.astype(np.int64)).max(initial=0))
    assert raw_bound*(p-1) < 2**63
    t = time.perf_counter()
    digest = hashlib.sha256()
    residual_nonzero = 0
    for r0 in range(0, E.shape[0], 10000):
        residual = (E[r0:r0+10000] @ V) % p
        residual_nonzero += int(np.count_nonzero(residual))
        digest.update(np.asarray(residual, dtype='<i8').tobytes())
    multiply_seconds = time.perf_counter()-t
    assert not np.any((E[cov['rows']] @ V) % p)
    return dict(status='EXACT', purpose='reduction cost and identity control; no geometric rank',
                prime=p, nS=len(S), nU=len(U), measured_columns=width,
                split_seconds=split_seconds, triangular_solve_seconds=solve_seconds,
                residual_multiply_seconds=multiply_seconds, residual_nonzero_entries=residual_nonzero,
                residual_sha256_little_endian_int64=digest.hexdigest(), cover_rows_residual_zero=True,
                full_residual_blocked_seconds_estimate=(solve_seconds+multiply_seconds)*math.ceil(len(U)/width),
                estimate_method='linear extrapolation from first width columns; excludes projection and elimination',
                uncompressed_residual_uint32_bytes=4*E.shape[0]*len(U))


def small_controls():
    cases = []
    for lam in [(6, 2), (3, 3, 1, 1)]:
        b = lean.build_cell_lean(lam, 2, verbose=False, chunk=1000)
        c = old.build_cell(lam, 2, verbose=False)
        assert b['E'].shape == c['E'].shape and (b['E'] != c['E']).nnz == 0
        for key in ('M', 'col_of', 'sgn'):
            assert np.array_equal(b['arr'][key], c['arr'][key])
        cases.append(dict(lam=lam, N_S=b['N_S'], n_chi=b['n_chi'],
                          rows=b['nrows'], nnz=b['nnz'], exact_constructor_match=True))
    b = lean.build_cell_lean((6, 2), 2, verbose=False)
    mat = sympy.Matrix(b['E'].toarray().tolist())
    basis = mat.nullspace()
    assert len(basis) == count_a((6, 2), 2) == 1
    vec = basis[0]
    den = math.lcm(*(int(x.q) for x in vec))
    vec = [int(x*den) for x in vec]
    terms = expanded_source(b['arr'], vec, 2)
    # Verify polynomial source on the independent uncompressed raising matrix.
    monomials, rows = build_R(4, 2, 2, (6, 2))
    coeff = {tuple(tuple(a) for a in mon): c for mon, c in terms}
    aa = exps(4, 2)
    expanded = [coeff.get(tuple(aa[k] for k in m), 0) for m in monomials]
    assert all(sum(v*expanded[j] for j, v in row.items()) == 0 for row in rows)
    point = pencil(1504, 2)
    co = det_coefficients(point)
    # All 5 grid points suffice for a homogeneous binary quartic identity.
    grid = [[1, t] for t in range(5)]
    assert all(poly_at(co, s) == direct_det_at(point, s) for s in grid)
    value = eval_terms(terms, co)
    assert value != 0
    for p in PRIMES:
        assert int(sum(int(x)*v for x, v in zip(eval_orbits(b['arr'], co, p, 2), vec)) % p) == value % p
    fourth = {(4-k, k): math.comb(4, k)*2**k for k in range(5)}
    assert eval_terms(terms, fourth) == 0
    mutant = dict(co); mutant[(4, 0)] = mutant.get((4, 0), 0)+1
    assert poly_at(mutant, [1, 0]) != direct_det_at(point, [1, 0])
    rescaled = {a: v*math.prod(math.factorial(x) for x in a) for a, v in co.items()}
    assert eval_terms(terms, rescaled) != value
    bad_terms = [[m, -c if j == 0 else c] for j, (m, c) in enumerate(terms)]
    assert eval_terms(bad_terms, co) != value
    # Nontrivial, independent exact triangular-solve control at both house primes.
    triangle = sparse.csr_matrix([[2, -3, 5], [0, -7, 11], [0, 0, 13]], dtype=np.int64)
    rhs = np.array([[17, 19], [23, 29], [31, 37]], dtype=np.int64)
    for p in PRIMES:
        inv = np.array([pow(int(v), -1, p) for v in triangle.diagonal()], dtype=np.uint32)
        answer = triangular_solve(triangle, inv, rhs, p)
        flint_answer = nmod_mat(triangle.toarray().tolist(), p).solve(nmod_mat(rhs.tolist(), p))
        assert answer.tolist() == flint_answer.tolist()
        assert np.array_equal((triangle @ answer) % p, rhs)
    probe = residual_probe(b['E'], lean.best_cover_lean(b['E'], b['n_chi']), PRIMES[0], width=1)
    from wk10_s64_pad import pad_frames, pad_coeffs
    frame = pad_frames(1, 1504, 3, 2)[0]
    padco = pad_coeffs(frame)
    for s in grid:
        vals = [sum(s[i]*frame[i][j] for i in range(2)) for j in range(10)]
        perm = sum(math.prod(vals[1+3*a+pi[a]] for a in range(3)) for pi in itertools.permutations(range(3)))
        assert poly_at(padco, s) == vals[0]*perm
    rec = dict(status='EXACT', model='gpt-6-astra', versions=dict(numpy=np.__version__, scipy=scipy.__version__, sympy=sympy.__version__),
               constructors=cases, source=dict(lam=[6, 2], delta=2, n=4, ambient_variables=16,
               convention='ordinary coefficient c_alpha; raising multiplier alpha_i+1', terms=terms,
               integral_kernel_coordinates=vec, full_uncompressed_raising_verified=True),
               point=dict(type='det_pencil', pencil=point), exact_value=value, primes=PRIMES,
               independent_homogeneous_quartic_grid=grid, padded_frame=frame,
               liveness=True, fourth_power_zero=True, altered_point_rejected=True,
               factorial_normalization_defect_rejected=True, altered_source_sign_rejected=True,
               independently_padded_evaluator_checked=True, triangular_solver_flint_control=True,
               tiny_residual_probe=probe)
    save('controls.json', rec)
    print('SMALL CONTROLS PASS; integral source determinant value', value, flush=True)


def pilot(which):
    lam = CELLS[which]
    tag = 'cell' + str(which+1)
    record = dict(status='RESOURCE_STOP', lam=lam, n=4, delta=8, model='gpt-6-astra',
                  stage='before construction', input_hashes=hashes(), phases=[])
    save(tag+'.json', record)
    scratch = Path(tempfile.mkdtemp(prefix='b15_04_'+tag+'_', dir=OUT)).resolve()
    assert scratch.parent == OUT.resolve() and scratch.name.startswith('b15_04_'+tag+'_')
    def phase(info):
        from b15_bound import process_memory
        info = dict(info, native_process_memory=process_memory())
        record['phases'].append(info)
        save(tag+'.json', record)
    t = time.perf_counter()
    try:
        b = lean.build_cell_lean(lam, 8, verbose=True, chunk=50000, blocks='disk', scratch=str(scratch), phase_hook=phase)
        record['build'] = {k: v for k, v in b.items() if k not in ('arr', 'E')}
        record['stage'] = 'cover'
        save(tag+'.json', record)
        c = lean.best_cover_lean(b['E'], b['n_chi'], verbose=True, rows_per=100000)
        nS, nU = len(c['S']), len(c['U'])
        record['cover'] = dict(size=nS, nU=nU, stats=c['stats'], order=c['order'],
                              cover_seconds=time.perf_counter()-t-b['build_secs'])
        record['reduction_storage'] = dict(projected_uint32_bytes=4*(nU+64)*nU,
                                          projected_int64_copy_bytes=8*(nU+64)*nU,
                                          flint_word_matrix_bytes=8*(nU+64)*nU,
                                          dense_X_uint32_bytes=4*nS*nU,
                                          method='exact array sizes; excludes Python lists, sparse arrays, and solver workspace')
        # Archive small structural data; full carriers are reproducible from the construction.
        np.savez_compressed(OUT/(tag+'_cover.npz'), rows=c['rows'], S=c['S'], U=c['U'], pos=c['pos'])
        record['stage'] = 'narrow residual benchmark'
        save(tag+'.json', record)
        record['residual_probe'] = residual_probe(b['E'], c, PRIMES[0])
        record['stage'] = 'reduction cost gate'
        record['reason'] = 'Pilot completed construction and cover; reduction requires a priced, controlled backend.'
        # This pilot is scoped to construction and measured reduction pricing.
        # A compact carrier permits a separately authorized, justified follow-up.
        if nU <= 3000:
            carrier = OUT/(tag+'_native.npz')
            np.savez_compressed(carrier, E_data=b['E'].data, E_indices=b['E'].indices,
                                E_indptr=b['E'].indptr, E_shape=b['E'].shape,
                                M=b['arr']['M'], col_of=b['arr']['col_of'], sgn=b['arr']['sgn'])
            record['local_native_carrier'] = dict(path=str(carrier.relative_to(ROOT)), bytes=carrier.stat().st_size,
                                                  delivery='compact construction retained; local cache staged only if size-compliant')
        record['wall_seconds'] = time.perf_counter()-t
        save(tag+'.json', record)
        print(json.dumps(clean(record['cover'])), flush=True)
        print(json.dumps(record['reduction_storage']), flush=True)
    except (MemoryError, RuntimeError) as exc:
        record['error'] = type(exc).__name__+': '+str(exc)
        record['wall_seconds'] = time.perf_counter()-t
        save(tag+'.json', record)
        raise


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['controls', 'sizing', 'pilot'])
    parser.add_argument('--cell', type=int, choices=[1, 2], default=1)
    args = parser.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    if args.mode == 'controls':
        small_controls()
    elif args.mode == 'sizing':
        exact_sizing()
    else:
        pilot(args.cell-1)


if __name__ == '__main__':
    main()

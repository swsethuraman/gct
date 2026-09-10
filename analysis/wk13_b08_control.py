#!/usr/bin/env python3
"""
B13-08 -- the input-and-control checkpoint (results/PREREG_b13_08.md section 4).

  A. session 79's own controls, re-run here with this session's output path
     (analysis/wk12_s79_per6_control.py writes results/s79_per6_control.json, a
     session-79 file; the checks are the same three): per_form(3) is a hand
     permanent; per_3 and det_3 coefficient dicts differ at all ten recorded
     points; the two a = 2 degree-8 weights of session 43's record reproduce
     mult = a = 2 on the unchanged engine.
  B. two banked degree-10 records reproduced on the unchanged engine with the
     recorded seeds -- (11,6,5,3,3,2) a=5 and (9,8,5,4,3,1) a=13 -- field by
     field against results/s79_per6.jsonl; wall time and peak RSS recorded to
     calibrate this host.
  C. the negative control on the same kernels: diagonal pencils (products of
     three linear forms) MUST give evaluation rank 0 at both primes for a
     length-6 weight; det_3 pencils are recorded.
  D. the lean contingency driver on the same two weights: identical mult,
     n_chi, cover, |U|, and a bit-identical kernel matrix at both primes.

usage: python3 analysis/wk13_b08_control.py [--skip-d] [--out results/b13_08/controls.json]
"""
import sys, os, time, json, random, itertools, hashlib
for _v in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ.setdefault(_v, '1')
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
os.environ.setdefault('S71_SCHUR_SO', '/home/claude/b13_08/schur.so')
import numpy as np
import wk12_s79_per6 as ENGINE
from wk12_s79_per6 import per3_pencils, per3_coeffs, measure_weight, SEED, BOUND, R, n3, PRIMES
from wk8_s30_core import per_form, det_form, restrict
from wk11_s71_hybrid import matmul_mod, rank_mod_p
from wk12_s79_cell6 import ev_rows_from_coeffs
from wk9_s45_build import _rss_gb

PER3, N3 = per_form(3); DET3, _ = det_form(3)
FRONTIER = [((11, 6, 5, 3, 3, 2), 5), ((9, 8, 5, 4, 3, 1), 13)]
NEG_SEED = 20260909


def log(*a):
    print(*a, file=sys.stderr); sys.stderr.flush()


def record_of(mu, delta=10):
    for ln in open(os.path.join(ROOT, 'results', 's79_per6.jsonl')):
        r = json.loads(ln)
        if tuple(r['mu']) == tuple(mu) and r['delta'] == delta: return r
    raise KeyError(mu)


def diag_pencils(K, seed, bound):
    """A_i = diag(x_i, y_i, z_i): per_3(sum s_i A_i) = (sum s_i x_i)(sum s_i y_i)(sum s_i z_i)."""
    rnd = random.Random(seed)
    out = []
    for _ in range(K):
        pen = []
        for i in range(R):
            d = [rnd.randint(-bound, bound) for _ in range(3)]
            pen.append([[d[a] if a == b else 0 for b in range(3)] for a in range(3)])
        out.append(pen)
    return out


def det3_coeffs(pencil):
    As = [[pencil[i][a][b] for a in range(3) for b in range(3)] for i in range(R)]
    return restrict(DET3, 9, n3, R, As)


def khash(K):
    return hashlib.md5(np.ascontiguousarray(np.asarray(K, dtype=np.uint32)).tobytes()).hexdigest()


def main(argv):
    out_path = argv[argv.index('--out') + 1] if '--out' in argv else os.path.join(ROOT, 'results', 'b13_08', 'controls.json')
    res = dict(board_numbering='batch13', session='B13-08', engine='analysis/wk12_s79_per6.py (unchanged)',
               S71_MEM_X=os.environ.get('S71_MEM_X'), host=dict(cpus=os.cpu_count()))
    # ---------------------------------------------------------------- A
    M = [[2, 3, 5], [7, 11, 13], [17, 19, 23]]
    hand = sum(M[0][s[0]] * M[1][s[1]] * M[2][s[2]] for s in itertools.permutations(range(3)))
    val = sum(c * (M[0][0] ** b[0]) * (M[0][1] ** b[1]) * (M[0][2] ** b[2]) * (M[1][0] ** b[3]) * (M[1][1] ** b[4]) * (M[1][2] ** b[5])
              * (M[2][0] ** b[6]) * (M[2][1] ** b[7]) * (M[2][2] ** b[8]) for b, c in PER3.items())
    assert val == hand, (val, hand)
    pts = per3_pencils(10, SEED, BOUND)
    diff = sum(1 for pt in pts if per3_coeffs(pt) != det3_coeffs(pt))
    assert diff == len(pts), diff
    A = dict(per_form_is_permanent=True, hand_value=hand, per3_ne_det3_points=diff, degree8_controls=[])
    for mu in ((11, 4, 4, 2, 2, 1), (10, 6, 4, 2, 1, 1)):
        t = time.time(); r = measure_weight(mu, 8, verbose=False, a_given=2)
        A['degree8_controls'].append(dict(mu=list(mu), a=r['a'], mult=r['mult'], units=r['units'], secs=r['secs'], wall=round(time.time() - t, 1)))
        log(f"  A: control {mu} d8: a={r['a']} mult={r['mult']} [s43 record: mult = a = 2] ({r['secs']}s)")
        assert r['mult'] == 2 and r['primes_agree']
    res['A'] = A; A['status'] = 'PASS'
    log("A PASS")
    # ---------------------------------------------------------------- B + C
    captured = {}
    _hk = ENGINE.hybrid_kernel; _bc = ENGINE.build_cell

    def hk_wrap(E, nc, p, a, cov, **kw):
        K, info = _hk(E, nc, p, a, cov, **kw); captured.setdefault('K', {})[p] = K.copy(); return K, info

    def bc_wrap(*a, **kw):
        B = _bc(*a, **kw); captured['B'] = B; return B
    ENGINE.hybrid_kernel = hk_wrap; ENGINE.build_cell = bc_wrap
    res['B'] = []; res['C'] = []
    for mu, a in FRONTIER:
        captured.clear()
        rec = record_of(mu)
        t = time.time(); r = measure_weight(mu, 10, verbose=True, a_given=a); wall = round(time.time() - t, 1)
        cmp = {}
        for k in ('a', 'N_S', 'stab', 'n_chi', 'nrows', 'nnz', 'mult', 'units', 'primes_agree'):
            cmp[k] = dict(here=r[k], record=rec[k], equal=(r[k] == rec[k]))
        cmp['cover_size'] = dict(here=r['cover_E']['size'], record=rec['cover_E']['size'], equal=r['cover_E']['size'] == rec['cover_E']['size'])
        cmp['cover_order'] = dict(here=r['cover_E']['order'], record=rec['cover_E']['order'], equal=r['cover_E']['order'] == rec['cover_E']['order'])
        for p in PRIMES:
            ps = str(p)
            cmp[f'nU_p{p}'] = dict(here=r['per_prime'][ps]['hybrid']['nU'], record=rec['per_prime'][ps]['hybrid']['nU'],
                                   equal=r['per_prime'][ps]['hybrid']['nU'] == rec['per_prime'][ps]['hybrid']['nU'])
            cmp[f'mult_p{p}'] = dict(here=r['per_prime'][ps]['mult'], record=rec['per_prime'][ps]['mult'],
                                     equal=r['per_prime'][ps]['mult'] == rec['per_prime'][ps]['mult'])
        allok = all(v['equal'] for v in cmp.values())
        entry = dict(mu=list(mu), a=a, compare=cmp, all_equal=allok, wall_secs=wall, secs=r['secs'], hwm_gb=r['hwm_gb'],
                     record_secs=rec['secs'], record_hwm_gb=rec.get('hwm_gb'), build_secs=r['build_secs'], record_build_secs=rec['build_secs'],
                     K_md5={str(p): khash(captured['K'][p]) for p in PRIMES})
        res['B'].append(entry)
        log(f"  B: {mu} a={a}: all fields equal = {allok}; wall {wall}s (record {rec['secs']}s), HWM {r['hwm_gb']} GB (record {rec.get('hwm_gb')})")
        assert allok, cmp
        # C: negative control on the captured kernel
        B = captured['B']; Kp = a + 8
        dpts = diag_pencils(Kp, NEG_SEED, BOUND)
        dco = [per3_coeffs(pt) for pt in dpts]
        # sanity: the diagonal pencil's cubic IS the product of its three diagonal linear forms (independent multiplication)
        for pt, co in zip(dpts, dco):
            prod = {tuple([0] * R): 1}
            for aa in range(3):
                nxt = {}
                for al, c in prod.items():
                    for i in range(R):
                        v = pt[i][aa][aa]
                        if v == 0: continue
                        k = list(al); k[i] += 1; k = tuple(k)
                        nxt[k] = nxt.get(k, 0) + c * v
                prod = nxt
            prod = {k: v for k, v in prod.items() if v}
            assert prod == {k: v for k, v in co.items() if v}, "diagonal pencil is not the product of its linear forms"
        dets = [det3_coeffs(pt) for pt in per3_pencils(Kp, SEED, BOUND)]
        centry = dict(mu=list(mu), a=a, diag_seed=NEG_SEED, points=Kp, per_prime={})
        for p in PRIMES:
            K = captured['K'][p]; Kp_ = np.asarray(K % p, dtype=np.int64)
            EVd = ev_rows_from_coeffs(B['arr'], dco, p, R, n=n3); Gd = matmul_mod(EVd % p, Kp_, p); rd = int(rank_mod_p(Gd, p)); del EVd
            EVt = ev_rows_from_coeffs(B['arr'], dets, p, R, n=n3); Gt = matmul_mod(EVt % p, Kp_, p); rt = int(rank_mod_p(Gt, p)); del EVt
            # the same rows on the recorded per_3 family give a again (the positive side, re-derived on the captured K)
            EVp = ev_rows_from_coeffs(B['arr'], [per3_coeffs(pt) for pt in per3_pencils(Kp, SEED, BOUND)], p, R, n=n3)
            rp = int(rank_mod_p(matmul_mod(EVp % p, Kp_, p), p)); del EVp
            centry['per_prime'][str(p)] = dict(rank_diagonal_pencils=rd, rank_det3_pencils=rt, rank_per3_pencils=rp,
                                              diag_all_rows_zero=bool(not np.any(Gd)))
            log(f"  C: {mu} p={p}: rank on diagonal pencils = {rd} (must be 0), on det_3 pencils = {rt} (<= a = {a}), on per_3 pencils = {rp} (= a)")
            assert rd == 0 and rp == a and rt <= a
        res['C'].append(centry)
        captured.clear()
    ENGINE.hybrid_kernel = _hk; ENGINE.build_cell = _bc
    res['B_status'] = 'PASS'; res['C_status'] = 'PASS'
    log("B PASS, C PASS")
    json.dump(res, open(out_path, 'w'), indent=1)
    # ---------------------------------------------------------------- D
    if '--skip-d' not in argv:
        from wk13_b08_per6_lean import measure_weight_lean
        res['D'] = []
        for (mu, a), bent in zip(FRONTIER, res['B']):
            t = time.time(); r, Ks, B = measure_weight_lean(mu, 10, verbose=True, a_given=a, want_K=True); wall = round(time.time() - t, 1)
            same = dict(mult=r['mult'] == bent['compare']['mult']['here'], n_chi=r['n_chi'] == bent['compare']['n_chi']['here'],
                        cover_size=r['cover_E']['size'] == bent['compare']['cover_size']['here'],
                        nU={str(p): r['per_prime'][str(p)]['hybrid']['nU'] == bent['compare'][f'nU_p{p}']['here'] for p in PRIMES},
                        K_md5={str(p): khash(Ks[p]) == bent['K_md5'][str(p)] for p in PRIMES})
            ok = same['mult'] and same['n_chi'] and same['cover_size'] and all(same['nU'].values()) and all(same['K_md5'].values())
            res['D'].append(dict(mu=list(mu), a=a, identical=same, all_identical=ok, wall_secs=wall, hwm_gb=r['hwm_gb'], mult=r['mult']))
            log(f"  D: lean driver on {mu}: identical = {ok}; wall {wall}s, HWM {r['hwm_gb']} GB")
            assert ok, same
        res['D_status'] = 'PASS'
        log("D PASS")
        json.dump(res, open(out_path, 'w'), indent=1)
    log("controls PASS")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

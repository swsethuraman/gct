#!/usr/bin/env python3
"""
B13-10 -- the acceptance suite of results/PREREG_b13_10.md section 2.2, one cell
at a time, banked per cell.

For each cell: the old builder (wk9_s45_build.build_cell) and the lean builder
(wk13_b10_lean.build_cell_lean) each run in their own bounded subprocess
(analysis/wk13_b10_run.py) and write E and arr to a scratch directory; then, in
this process,

  1. exact operator agreement   E_old == E_new (indptr, indices, data), and
                                 M, col_of, sgn, n_chi from the orbit setup;
                                 on a mismatch, the row-multiset comparison;
  2. kernel                      hybrid_kernel_lean on E_new at both primes,
                                 nullity = a, EVERY vector verified on E_old
                                 (the uncompressed int64 operator), rank = a;
  3. evaluation ranks            on the drivers' recorded point families and
                                 seeds, compared with the banked record.

usage: python3 analysis/wk13_b10_suite.py --ids A1,A2,... [--scratch DIR] [--variants] [--out results/b13_10/suite.jsonl]
"""
import sys, os, time, json, subprocess, random
for _v in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ.setdefault(_v, '1')
os.environ.setdefault('S71_MEM_X', '250000000')
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
os.environ.setdefault('S71_SCHUR_SO', os.path.join(ROOT, '..', 'b13_10_scratch', 'schur.so'))
import numpy as np
from scipy import sparse
import wk11_s71_codes; wk11_s71_codes.install()
from wk8_s30_core import exps, restrict, det_form, per_form, P1, P2
from wk9_s45_build import log, _rss_gb
from wk9_s42_census import a_weyl
from wk11_s71_hybrid import best_cover, matmul_mod, rank_mod_p, rank_tall, check_kernel_mat
from wk12_s79_cell6 import ev_rows_from_coeffs, red_mask, reducible_points, red_coeffs
from wk10_s64_pad import pad_frames, pad_coeffs
from wk13_b10_lean import hybrid_kernel_lean

PRIMES = (P1, P2)
HYB_SEED = 20260908
BOUND = 40
SEEDS = dict(det=11, red=29, pad=37, per4=47, per3=41)
LOGS = os.path.join(ROOT, 'results', 'logs')

SUITE = [
    dict(id='A1', n=4, lam=(13, 5, 2, 2, 2), delta=6, src='results/s60_cells.jsonl'),
    dict(id='A2', n=4, lam=(37, 13, 4, 1, 1), delta=14, src='results/s71_sweep.jsonl'),
    dict(id='A3', n=4, lam=(28, 8, 5, 2, 1), delta=11, src='results/s71_sweep.jsonl'),
    dict(id='A4', n=4, lam=(26, 7, 5, 5, 1), delta=11, src='results/s71_sweep.jsonl'),
    dict(id='B1', n=4, lam=(38, 2, 2, 2, 2, 2), delta=12, src='results/s79_cells.jsonl'),
    dict(id='B2', n=4, lam=(29, 9, 3, 1, 1, 1), delta=11, src='results/s79_cells.jsonl'),
    dict(id='B3', n=4, lam=(33, 7, 2, 2, 2, 2), delta=12, src='results/s79_cells.jsonl'),
    dict(id='B4', n=4, lam=(24, 13, 3, 2, 1, 1), delta=11, src='results/s79_cells.jsonl'),
    dict(id='B5', n=4, lam=(11, 7, 6, 6, 1, 1), delta=8, src='results/s79_cells.jsonl'),
    dict(id='B6', n=4, lam=(12, 8, 6, 2, 2, 2), delta=8, src='results/s79_cells.jsonl'),
    dict(id='B7', n=4, lam=(13, 9, 9, 3, 1, 1), delta=9, src='results/s79_cells.jsonl'),
    dict(id='C1', n=3, lam=(17, 2, 2, 2, 2, 2), delta=9, src='results/s79_per6.jsonl'),
    dict(id='C2', n=3, lam=(12, 5, 5, 3, 1, 1), delta=9, src='results/s79_per6.jsonl'),
    dict(id='C3', n=3, lam=(11, 8, 5, 2, 2, 2), delta=10, src='results/s79_per6.jsonl'),
    dict(id='C4', n=3, lam=(5, 5, 5, 5, 5, 2), delta=9, src='results/s79_per6.jsonl'),
    dict(id='C5', n=3, lam=(10, 7, 6, 4, 2, 1), delta=10, src='results/s79_per6.jsonl'),
    dict(id='C6', n=3, lam=(7, 6, 5, 4, 3, 2), delta=9, src='results/s79_per6.jsonl'),
    dict(id='D1', n=3, lam=(19, 7, 2, 2, 2, 2, 2), delta=12, src='results/s69_sizes.jsonl'),
    # exploratory (addendum A of the PREREG): length 9, a = 0, operator agreement + certified full rank only
    dict(id='X1', n=3, lam=(11, 4, 2, 2, 1, 1, 1, 1, 1), delta=8, src=None),
    dict(id='X2', n=4, lam=(15, 4, 2, 2, 1, 1, 1, 1, 1), delta=7, src=None),
]


def _all_none(r):
    return all(r.get(k) is None for k in ('det_rank', 'generic_rank', 'kernel_dim', 'mult', 'mult_det'))


def banked(cell):
    """the record's values for this cell, read from the file named in the suite."""
    if not cell['src']: return dict(source=None)
    fn = os.path.join(ROOT, cell['src'])
    rows = [json.loads(l) for l in open(fn) if l.strip()]
    lam = list(cell['lam'])
    cands = [r for r in rows if (r.get('lam') or r.get('mu')) == lam and r.get('delta') == cell['delta']]
    # prefer a record that actually carries measurements: s69_sizes.jsonl holds a
    # SPANNING_FAILED first pass with every rank None before the run that succeeded
    cands.sort(key=lambda r: 0 if (r.get('status') in (None, 'OK') and not _all_none(r)) else 1)
    for r in cands:
        if True:
            out = dict(source=cell['src'], a=r.get('a'), N_S=r.get('N_S'), n_chi=r.get('n_chi'), nrows=r.get('nrows'), nnz=r.get('nnz'),
                       build_secs=r.get('build_secs'), build_hwm_gb=r.get('build_hwm_gb', r.get('hwm_gb')))
            if 'mult' in r and 'mult_det' not in r:            # per6
                out['per3'] = r['mult']
            for k in ('mult_det', 'mult_pad', 'mult_per4', 'mult_red_star', 'mult_red_pts', 'mult_red'):
                if k in r: out[k.replace('mult_', '')] = r[k]
            if 'det_rank' in r and isinstance(r['det_rank'], dict):        # s69
                out['det'] = r['det_rank'][str(P1)]; out['kernel_dim'] = r['kernel_dim'][str(P1)]; out['i_det'] = r['i_det'][str(P1)]
                out['a'] = r['a']
            if 'sides' in r and isinstance(r['sides'], dict):
                for sd, v in r['sides'].items():
                    if isinstance(v, dict) and 'mult' in v: out.setdefault(sd, v['mult'])
            return out
    raise KeyError(("banked record not found", cell))


def run_build(cell, builder, scratch, timeout, vlimit_kb, knobs=None):
    tag = cell['id']
    cmd = [sys.executable, os.path.join(HERE, 'wk13_b10_run.py'), '--builder', builder, '--n', str(cell['n']), '--delta', str(cell['delta']),
           '--lam', ','.join(map(str, cell['lam'])), '--out', scratch, '--tag', tag]
    name = f"{tag}_{builder}"
    if knobs:
        cmd += ['--triples', knobs['triples'], '--blocks', knobs['blocks'], '--chunk', str(knobs['chunk'])]
        name += f"_{knobs['triples']}_{knobs['blocks']}_c{knobs['chunk']}"
    elif builder == 'lean':
        name += "_store_memory_c400000"
    os.makedirs(LOGS, exist_ok=True)
    logf = os.path.join(LOGS, f"b13_10_{name}.log")
    shell = f"ulimit -v {vlimit_kb}; exec timeout {timeout} " + ' '.join(repr(c) for c in cmd)
    t0 = time.time()
    with open(logf, 'w') as lf:
        proc = subprocess.Popen(['bash', '-c', shell], stdout=lf, stderr=subprocess.STDOUT)
        with open(os.path.join(LOGS, f"b13_10_{name}.pid"), 'w') as pf: pf.write(str(proc.pid) + "\n")
        rc = proc.wait()
    wall = time.time() - t0
    jf = os.path.join(scratch, name + '.json')
    rec = json.load(open(jf)) if os.path.exists(jf) else None
    return dict(name=name, rc=rc, wall=round(wall, 1), rec=rec, log=os.path.relpath(logf, ROOT))


def load_E(scratch, name):
    z = np.load(os.path.join(scratch, name + '.npz'))
    n_chi = int(z['n_chi'])
    E = sparse.csr_matrix((z['data'], z['indices'], z['indptr']), shape=(len(z['indptr']) - 1, n_chi))
    arr = dict(M=z['M'], col_of=z['col_of'], sgn=z['sgn'], n_chi=n_chi, N_S=int(z['M'].shape[0]))
    return E, arr


def exact_agreement(Eo, ao, En, an):
    out = dict(shape=(Eo.shape == En.shape), n_chi=(ao['n_chi'] == an['n_chi']),
               M=bool(np.array_equal(ao['M'].astype(np.int64), an['M'].astype(np.int64))),
               col_of=bool(np.array_equal(ao['col_of'].astype(np.int64), an['col_of'].astype(np.int64))),
               sgn=bool(np.array_equal(ao['sgn'].astype(np.int64), an['sgn'].astype(np.int64))))
    if out['shape']:
        Eo = Eo.tocsr(); Eo.sort_indices(); En = En.tocsr(); En.sort_indices()
        out['indptr'] = bool(np.array_equal(Eo.indptr.astype(np.int64), En.indptr.astype(np.int64)))
        out['indices'] = bool(np.array_equal(Eo.indices.astype(np.int64), En.indices.astype(np.int64)))
        out['data'] = bool(np.array_equal(Eo.data.astype(np.int64), En.data.astype(np.int64)))
    out['identical'] = all(v for v in out.values() if isinstance(v, bool))
    if not out['identical'] and out['shape']:
        # row multiset comparison: canonical row keys
        def keys(E):
            E = E.tocsr(); E.sort_indices()
            ks = []
            for r in range(E.shape[0]):
                s, e = E.indptr[r], E.indptr[r + 1]
                ks.append((tuple(E.indices[s:e].tolist()), tuple(E.data[s:e].astype(np.int64).tolist())))
            return sorted(ks)
        out['row_multiset_equal'] = keys(Eo) == keys(En)
    return out


def pencils(K, seed, bound, R, k):
    rnd = random.Random(seed)
    return [[[[rnd.randint(-bound, bound) for _ in range(k)] for _ in range(k)] for _ in range(R)] for _ in range(K)]


def form_coeffs(form, Nvar, n, R, pencil, k):
    As = [[pencil[i][a][b] for a in range(k) for b in range(k)] for i in range(R)]
    return restrict(form, Nvar, n, R, As)


def families(cell, a):
    """the drivers' point families, in the drivers' RNG order."""
    n = cell['n']; R = len(cell['lam']); Kp = a + 8
    fam = {}
    if n == 4:
        D4, N4 = det_form(4); Pr4, NP4 = per_form(4)
        fam['det'] = [form_coeffs(D4, N4, 4, R, pt, 4) for pt in pencils(Kp, SEEDS['det'], BOUND, R, 4)]
        fam['per4'] = [form_coeffs(Pr4, NP4, 4, R, pt, 4) for pt in pencils(Kp, SEEDS['per4'], BOUND, R, 4)]
        fam['red_pts'] = [red_coeffs(pt, R) for pt in reducible_points(Kp, SEEDS['red'], BOUND, R)]
        fam['pad'] = [pad_coeffs(V) for V in pad_frames(Kp, SEEDS['pad'], BOUND, R)]
    else:
        Pr3, NP3 = per_form(3); D3, N3 = det_form(3)
        fam['per3'] = [form_coeffs(Pr3, NP3, 3, R, pt, 3) for pt in pencils(Kp, SEEDS['per3'], BOUND, R, 3)]
        fam['det'] = [form_coeffs(D3, N3, 3, R, pt, 3) for pt in pencils(Kp, SEEDS['det'], BOUND, R, 3)]
    return fam


def measure(cell, scratch, args):
    t0 = time.time()
    n = cell['n']; lam = cell['lam']; delta = cell['delta']; R = len(lam)
    a = int(a_weyl(lam, delta, n, {}))
    rec = dict(id=cell['id'], n=n, lam=list(lam), delta=delta, ell=R, a=a, banked=banked(cell), stamp=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))
    vk = int(args.get('--vlimit', 7000000))
    old = run_build(cell, 'old', scratch, int(args.get('--timeout-old', 1800)), vk)
    lean = run_build(cell, 'lean', scratch, int(args.get('--timeout-lean', 3600)), vk)
    rec['build_old'] = old; rec['build_lean'] = lean
    variants = []
    if '--variants' in args:
        for kn in (dict(triples='recompute', blocks='memory', chunk=400000), dict(triples='store', blocks='disk', chunk=400000),
                   dict(triples='recompute', blocks='disk', chunk=200000)):
            variants.append(run_build(cell, 'lean', scratch, int(args.get('--timeout-lean', 3600)), vk, knobs=kn))
        rec['build_lean_variants'] = variants
    if old['rc'] != 0 or lean['rc'] != 0 or old['rec'] is None or lean['rec'] is None:
        rec['status'] = 'BUILD FAILED'; rec['secs'] = round(time.time() - t0, 1); return rec
    Eo, ao = load_E(scratch, old['name']); En, an = load_E(scratch, lean['name'])
    rec['agreement'] = exact_agreement(Eo, ao, En, an)
    for v in variants:
        if v['rec'] is not None:
            Ev, av = load_E(scratch, v['name'])
            v['agreement_with_old'] = exact_agreement(Eo, ao, Ev, av)['identical']
            del Ev, av
    nc = an['n_chi']
    rec['sizes'] = dict(N_S=an['N_S'], n_chi=nc, nrows=int(En.shape[0]), nnz=int(En.nnz), stab=lean['rec']['stab'])
    if nc == 0:
        rec['status'] = 'n_chi = 0 (vacuous)'; rec['secs'] = round(time.time() - t0, 1); return rec
    # 2. the kernel of E_new, verified on E_old
    Eo64 = Eo if Eo.dtype == np.int64 else Eo.astype(np.int64)
    cov = best_cover(En, nc, seed=HYB_SEED)
    rec['cover'] = dict(size=cov['size'], order=cov['order'], stats=cov['stats'], excess=int(nc - cov['size'] - a))
    kern = {}
    Ks = {}
    for p in PRIMES:
        tk = time.time()
        K, info = hybrid_kernel_lean(En, nc, p, a, cov, seed=HYB_SEED, tag=f"[{cell['id']}]", verbose=True, fo=args.get('--fo', 'copy'))
        ver_old = bool(check_kernel_mat(Eo64, K.astype(np.int64), p)) if a else True
        rk = int(rank_tall(K, p)) if a else 0
        kern[str(p)] = dict(nullity=int(K.shape[1]), verified_on_E_old=ver_old, verified_on_E_new=bool(check_kernel_mat(En, K.astype(np.int64), p)) if a else True,
                            rank=rk, hybrid=info, secs=round(time.time() - tk, 1))
        Ks[p] = K
    rec['kernel'] = kern
    rec['kernel_ok'] = all(v['nullity'] == a and v['verified_on_E_old'] and v['rank'] == a for v in kern.values())
    # 3. evaluation ranks on the drivers' families
    fam = families(cell, a) if a else {}
    ranks = {}
    for name, cl in fam.items():
        per = {}
        for p in PRIMES:
            Kp_ = np.asarray(Ks[p] % p, dtype=np.int64)
            parts = []
            for c0 in range(0, len(cl), 8):
                EV = ev_rows_from_coeffs(an, cl[c0:c0 + 8], p, R, n=n)
                parts.append(matmul_mod(EV % p, Kp_, p)); del EV
            G = np.vstack(parts)
            per[str(p)] = int(rank_mod_p(G, p))
        ranks[name] = dict(per_prime=per, agree=(len(set(per.values())) == 1), mult=(per[str(P1)] if len(set(per.values())) == 1 else None))
    if a and n == 4:
        red = red_mask(an, R); nonred = np.nonzero(~red)[0]
        per = {str(p): (int(rank_tall(Ks[p][nonred], p)) if len(nonred) else 0) for p in PRIMES}
        ranks['red_star'] = dict(per_prime=per, agree=(len(set(per.values())) == 1), mult=(per[str(P1)] if len(set(per.values())) == 1 else None))
    rec['ranks'] = ranks
    # compare with the record
    b = rec['banked']; cmp = {}
    for name, r in ranks.items():
        key = {'red_pts': 'red_pts', 'red_star': 'red_star'}.get(name, name)
        if key in b:
            cmp[name] = dict(banked=b[key], here=r['mult'], match=(b[key] == r['mult']))
        elif key == 'red_star' and 'red' in b:
            cmp[name] = dict(banked=b['red'], here=r['mult'], match=(b['red'] == r['mult']))
    rec['rank_compare'] = cmp
    # a check that can silently drop its own targets is not a check: every banked
    # multiplicity must have been placed against a computed family, or this fails
    FAMILY_KEYS = ('det', 'pad', 'per4', 'red', 'red_star', 'red_pts', 'per3')
    banked_families = {k: v for k, v in b.items() if k in FAMILY_KEYS and isinstance(v, int)}
    placed = set()
    for name in cmp:
        placed.add(name)
        if name == 'red_star' and 'red' in banked_families: placed.add('red')
    unplaced = sorted(set(banked_families) - placed)
    rec['banked_families'] = banked_families
    rec['unplaced_banked'] = unplaced
    if a and not cmp and banked_families:
        rec['ranks_ok'] = False
        rec['rank_compare_error'] = ('no banked multiplicity could be placed against a computed family', banked_families)
    elif unplaced:
        rec['ranks_ok'] = False
        rec['rank_compare_error'] = ('banked multiplicities not placed', unplaced)
    else:
        rec['ranks_ok'] = all(v['match'] for v in cmp.values()) if cmp else (None if not banked_families else False)
    rec['status'] = ('PASS' if rec['agreement']['identical'] and rec['kernel_ok'] and rec['ranks_ok'] in (True, None) else 'FAIL')
    rec['secs'] = round(time.time() - t0, 1); rec['driver_hwm_gb'] = round(_rss_gb(), 3)
    return rec


def old_h(rec):
    r = rec['build_old']['rec']; return f"{r['hwm_above_baseline_gb']:.3f}GB/{r['secs']['total']}s" if r else 'n/a'


def lean_h(rec):
    r = rec['build_lean']['rec']; return f"{r['hwm_above_baseline_gb']:.3f}GB/{r['secs']['total']}s" if r else 'n/a'


if __name__ == '__main__':
    argv = sys.argv[1:]
    args = {}; i = 0
    while i < len(argv):
        if argv[i].startswith('--') and i + 1 < len(argv) and not argv[i + 1].startswith('--'):
            args[argv[i]] = argv[i + 1]; i += 2
        else:
            args[argv[i]] = True; i += 1
    ids = args.get('--ids', ','.join(c['id'] for c in SUITE)).split(',')
    scratch = args.get('--scratch', os.path.join(ROOT, '..', 'b13_10_scratch'))
    os.makedirs(scratch, exist_ok=True)
    outp = args.get('--out', os.path.join(ROOT, 'results', 'b13_10', 'suite.jsonl'))
    os.makedirs(os.path.dirname(outp), exist_ok=True)
    for cell in SUITE:
        if cell['id'] not in ids: continue
        log(f"=== {cell['id']} {cell['lam']} d{cell['delta']} n={cell['n']} {time.strftime('%H:%M:%S')}")
        rec = measure(cell, scratch, args)
        with open(outp, 'a') as f: f.write(json.dumps(rec) + "\n")
        s = rec.get('sizes', {})
        log(f"  {cell['id']}: {rec['status']} identical={rec.get('agreement', {}).get('identical')} kernel_ok={rec.get('kernel_ok')} ranks={rec.get('rank_compare')} "
            f"old {old_h(rec)} lean {lean_h(rec)} ({rec['secs']}s)" if 'agreement' in rec else f"  {cell['id']}: {rec['status']}")
        if '--keep' not in args:
            for k in ('build_old', 'build_lean'):
                nm = rec[k]['name']
                fn = os.path.join(scratch, nm + '.npz')
                if os.path.exists(fn) and s.get('nnz', 0) > 2_000_000: os.remove(fn)

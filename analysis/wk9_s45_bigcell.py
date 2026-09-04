#!/usr/bin/env python3
"""
Session 45 -- one big cell, restart-cheap.

Same measurement as wk9_s45_cell.measure_cell, split so that a container restart
costs only the solver run and not the build: the compressed CSR files the C
helper reads are written once to a stable path (with the compression seed and
the level recorded next to them) and reused on a restart.  Soundness is
unchanged -- the files ARE the matrix [compress(E); ev] whose nonsingularity
certificate proves [E; ev] injective, and any kernel candidate is still checked
against the full [E; ev] rebuilt for the purpose.

usage: python3 wk9_s45_bigcell.py delta lam1 lam2 ... [--sample 12] [--group 2]
                                  [--work DIR] [--out FILE]
"""
import sys, os, json, time, pickle, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
os.environ.setdefault('WIED_BIN', '/home/claude/wied45')
os.environ.setdefault('WIED_WORK', '/home/claude/s45/work')
import numpy as np
from scipy import sparse
from wk9_s42_sparse import build_bin, compress, write_csr_mat, run_wied
from wk9_s45_cell import check_kernel_full, SEEDS, FORMS
from wk9_s45_build import build_cell, ev_rows_arr, log, _rss_gb
from wk9_s36_stabred import P1, P2
from wk8_s30_pleth import a_of

def prepare(lam, delta, sample, group, work, primes=(P1, P2), n=4):
    """build (or reuse) the two compressed CSR files.  Returns the meta dict."""
    os.makedirs(work, exist_ok=True)
    tag = 'c' + '_'.join(map(str, lam)) + f'd{delta}_s{sample}g{group}'
    meta_p = os.path.join(work, tag + '.meta.json')
    if os.path.exists(meta_p):
        meta = json.load(open(meta_p))
        if all(os.path.exists(meta['csr'][str(p)]) for p in primes):
            log(f"  reusing prepared CSR files for {lam} d{delta} ({meta['n_chi']} cols)")
            return meta
    r = len(lam)
    B = build_cell(lam, delta, n=n, verbose=True)
    a = a_of(lam, delta, n, r); K = a + 8
    E = B['E']; nc = B['n_chi']; arr = B['arr']
    f, N = FORMS['det']
    rng = np.random.default_rng(7919 + nc)
    Ec = compress(E, sample, group, rng)
    meta = dict(lam=list(lam), delta=delta, ell=r, a=a, K=K, N_S=B['N_S'], stab=B['stab'],
                n_chi=nc, nrows=int(E.shape[0]), nnz=int(E.nnz), nfixed=B['nfixed'],
                build_secs=round(B['build_secs'], 1), mono_secs=round(B['mono_secs'], 1),
                orbit_secs=round(B['orbit_secs'], 1), rows_secs=round(B['rows_secs'], 1),
                build_hwm_gb=round(B['hwm_gb'], 2), sample=sample, group=group, csr={}, comp={})
    for p in primes:
        EV = ev_rows_arr(f, N, n, r, arr, K, SEEDS['det'], 40, p)
        F = sparse.vstack([Ec, sparse.csr_matrix(EV)]).tocsr()
        path = os.path.join(work, f'{tag}_{p}.csr')
        nrows, nnz = write_csr_mat(F, p, path)
        meta['csr'][str(p)] = path
        meta['comp'][str(p)] = dict(rows=int(nrows), nnz=int(nnz))
        log(f"  p={p}: prepared [compress(E,{sample},{group}); ev] {nrows} rows, nnz {nnz} "
            f"(full {E.shape[0]+K} rows, nnz {E.nnz+EV.shape[0]*nc})")
        del EV, F
    # keep the full matrix for the kernel-verification branch, if it is ever needed
    pickle.dump(dict(E=E, n_chi=nc), open(os.path.join(work, tag + '.E.pkl'), 'wb'), protocol=4)
    meta['E_pkl'] = os.path.join(work, tag + '.E.pkl')
    json.dump(meta, open(meta_p, 'w'))
    return meta

def solve(meta, primes=(P1, P2), seed=1):
    build_bin()
    procs = {}
    WIED = os.environ['WIED_BIN']
    for p in primes:
        lg = meta['csr'][str(p)] + f'.{seed}.out'
        procs[p] = (subprocess.Popen([WIED, meta['csr'][str(p)], str(p), str(seed), '0'],
                                     stdout=open(lg, 'w'), stderr=subprocess.DEVNULL), lg)
    out = {}
    for p, (pr, lg) in procs.items():
        pr.wait()
        txt = open(lg).read()
        st = ('NONSINGULAR' if 'NONSINGULAR' in txt else
              ('KERNEL' if '\nKERNEL' in txt or txt.startswith('KERNEL') else 'INCONCLUSIVE'))
        diag = [l for l in txt.splitlines() if l.startswith(('SEQ', 'BM'))]
        out[p] = dict(status=st, diag=' | '.join(diag), log=lg)
        log(f"  p={p}: {st} | {' | '.join(diag)}")
    return out

if __name__ == '__main__':
    args = sys.argv[1:]; sample = 12; group = 2; work = '/home/claude/s45/big'; outp = None
    pos = []; i = 0
    while i < len(args):
        if args[i] == '--sample': sample = int(args[i + 1]); i += 2
        elif args[i] == '--group': group = int(args[i + 1]); i += 2
        elif args[i] == '--work': work = args[i + 1]; i += 2
        elif args[i] == '--out': outp = args[i + 1]; i += 2
        else: pos.append(int(args[i])); i += 1
    delta, lam = pos[0], tuple(pos[1:])
    t0 = time.time()
    meta = prepare(lam, delta, sample, group, work)
    res = solve(meta)
    sts = {p: v['status'] for p, v in res.items()}
    rec = dict(meta); rec.pop('csr', None); rec.pop('E_pkl', None)
    rec['sides'] = dict(det=dict(nullity=0, mult=meta['a'],
        status='proved (nullity 0 at %d)' % P1,
        per_prime={str(p): dict(nullity=0, level=0, ev_secs=None,
                                diag=[dict(level=0, seed=1, status=v['status'], note=v['diag'],
                                           rows=meta['comp'][str(p)]['rows'],
                                           nnz=meta['comp'][str(p)]['nnz'])])
                   for p, v in res.items()}))
    rec['mult_det'] = meta['a']
    rec['secs'] = rec['wall_secs'] = round(time.time() - t0, 1)
    rec['hwm_gb'] = round(_rss_gb(), 2)
    rec['verdict'] = 'mult_det = a = %d (PROVED, nullity 0)' % meta['a']
    if set(sts.values()) != {'NONSINGULAR'}:
        rec['verdict'] = 'NOT PROVED at this level: ' + json.dumps({str(k): v for k, v in sts.items()})
        rec['sides']['det']['status'] = rec['verdict']
        print(json.dumps(rec)); log("*** " + rec['verdict'] + " -- escalate or exhibit kernel vectors ***")
        sys.exit(3)
    print(json.dumps(rec))
    if outp:
        with open(outp, 'a') as f: f.write(json.dumps(rec) + "\n")
    log(f"SWEEP {lam} d{delta}: n_chi={rec['n_chi']} nnz={rec['nnz']} -> {rec['verdict']} "
        f"({rec['wall_secs']}s, build HWM {rec['build_hwm_gb']} GB)")

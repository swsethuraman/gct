#!/usr/bin/env python3
"""Session 73 -- one rung of the n = 3 D-ladder  lambda_delta = (3 delta - 17, 7, 2^5), r = 7.

    mult_det = a - nullity [E; ev_det]      det_3 pencils   (Lemma 1, docs/sparse_det_route.md)
    mult_per = a - nullity [E; ev_per]      per_3 pencils
    D        = i_det - i_per = mult_per - mult_det

E: the simple raising operators on the chi_lambda-isotypic reduction V_chi
(wk9_s45_build.build_cell, n = 3); the nullities by the session-42/45 Wiedemann
certificates (wk9_s45_cell.nullity_stacked, unchanged), the K = a + 8 evaluation
rows pinned, both house primes, run concurrently on the two cores.

  * nullity 0 at one prime PROVES mult = a over Q (rank_p <= rank_Q <= a);
  * a positive nullity k is a measurement at each prime; it is carried to Q by
    rational reconstruction of the kernel vector(s) and exact checks over Z
    (E v = 0; vanishing at fresh integer pencils of the same family; nonvanishing
    at fresh pencils of the other family and at generic cubics).

Optionally (--fullE) the full-E nullity solve returns an explicit basis of
M_delta = ker E (the a highest-weight vectors, mod P1) for the transport checks.

usage: python3 analysis/wk11_s73_cell.py <delta> [--sides det,per] [--fullE] [--K <int>]
                                          [--primes both|one] [--levels s42|cheap|full]
                                          [--seedtag det|det2] [--out results/s73_dladder.jsonl]
"""
import gzip
import json
import os
import sys
import time

import numpy as np
from scipy import sparse

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from wk11_s73_lib import (ROOT, ART, LOGS, LOCAL, N_DEG, R, NENT, FORMS, PRIMES, SEEDS, BOUND, P1, P2,   # noqa: E402
                          log, lam_of, a_two_ways, pencils, pencil_record, coeffs_of,
                          ev_rows_from_pencils, reconstruct_integer, sparse_dot_exact,
                          eval_exact_many, generic_cubics, chi_reps, ufree_columns,
                          save_build, rank_modp, dump_json)
from wk9_s45_build import build_cell                     # noqa: E402
from wk9_s45_cell import nullity_stacked, LEVELS, check_kernel_full   # noqa: E402
from wk9_s42_sparse import build_bin                     # noqa: E402

_SHARED = {}


def _job(args):
    """one (side, prime) Wiedemann job in a forked child; the build is shared
    copy-on-write.  side 'fullE' = the kernel of E alone."""
    side, p, K, seedtag, levels, seed0 = args
    B = _SHARED['B']; arr = B['arr']; E = B['E']; nc = B['n_chi']
    t0 = time.time()
    out = dict(side=side, prime=int(p))
    if side == 'fullE':
        EV = sparse.csr_matrix((0, nc), dtype=np.int64)
        pens = []
    else:
        seedkey = side if seedtag == 'primary' else side + '2'
        pens = pencils(K, SEEDS[seedkey])
        EV = sparse.csr_matrix(ev_rows_from_pencils(arr, FORMS[side], pens, p))
        out['seed'] = SEEDS[seedkey]
    t_ev = time.time() - t0
    tag = f"s73_d{B['delta']}_{side}_{'p1' if p == P1 else 'p2'}_{seedtag}"
    k, kern, lvl, diag = nullity_stacked(E, EV, nc, p, want_kern=True, seed0=seed0, tag=tag,
                                         levels=levels, verbose=True)
    out.update(nullity=int(k), level=int(lvl), diag=diag, ev_secs=round(t_ev, 1),
               secs=round(time.time() - t0, 1), K=int(K))
    if kern:
        out['kern'] = [[int(x) % p for x in v] for v in kern]
    return out


def run(delta, sides=('det', 'per'), fullE=False, K=None, primes=PRIMES, levels='s42',
        seedtag='primary', outpath=None, seed0=1, lam=None):
    lam = tuple(lam) if lam is not None else lam_of(delta)
    assert lam[0] >= lam[1]
    a = a_two_ways(lam, delta)
    log(f"rung delta={delta} lam={lam}: a = {a} (verifier DP = house Weyl alternation)")
    rec = dict(session=73, n=N_DEG, r=R, delta=int(delta), lam=list(lam), a=int(a),
               seedtag=seedtag, levels=levels, primes=[int(p) for p in primes])
    t0 = time.time()
    B = build_cell(lam, delta, n=N_DEG, verbose=True)
    B['delta'] = delta
    nc = B['n_chi']
    rec.update(N_S=int(B['N_S']), stab=int(B['stab']), n_chi=int(nc), nrows_E=int(B['nrows']),
               nnz_E=int(B['nnz']), build_secs=round(B['build_secs'], 1), build_hwm_gb=round(B['hwm_gb'], 2))
    log(f"  built: N_S={B['N_S']} |Stab|={B['stab']} n_chi={nc} rows={B['nrows']} nnz={B['nnz']} ({B['build_secs']:.0f}s)")
    save_build(delta, B)
    reps, sgn_rep = chi_reps(B['arr'])
    uf = ufree_columns(B['arr'])
    rec['n_ufree_columns'] = int(len(uf))
    os.makedirs(ART, exist_ok=True)
    np.savez_compressed(os.path.join(ART, f"s73_chi_basis_d{delta}.npz"), reps=reps, sgn_rep=sgn_rep.astype(np.int8),
                        ufree_columns=uf.astype(np.int64), lam=np.array(lam), delta=np.int64(delta))
    if a == 0:
        rec.update(status='a=0', secs=round(time.time() - t0, 1))
        return rec
    K = K or (a + 8)
    build_bin()
    _SHARED['B'] = B
    lev = LEVELS[levels]
    jobs = []
    if fullE:
        jobs.append(('fullE', P1, K, seedtag, lev, seed0 + 700))
    for sd in sides:
        for p in primes:
            jobs.append((sd, p, K, seedtag, lev, seed0))
    import multiprocessing as mp
    with mp.get_context('fork').Pool(2) as pool:
        res = list(pool.imap_unordered(_job, jobs))
    _SHARED.clear()
    arr = B['arr']; E = B['E']
    rec['sides'] = {}
    kern_by = {}
    for sd in sides:
        rs = sorted([x for x in res if x['side'] == sd], key=lambda x: x['prime'])
        ks = {x['prime']: x['nullity'] for x in rs}
        agree = len(set(ks.values())) == 1
        k = rs[0]['nullity']
        side_rec = dict(K=K, seed=rs[0].get('seed'), nullity_per_prime={str(x['prime']): x['nullity'] for x in rs},
                        primes_agree=agree,
                        per_prime={str(x['prime']): dict(nullity=x['nullity'], level=x['level'], secs=x['secs'],
                                                         ev_secs=x['ev_secs'], diag=x['diag']) for x in rs})
        if not agree:
            side_rec['status'] = 'HALT: primes disagree on the nullity (stopping rule R2)'
            rec['sides'][sd] = side_rec
            log(f"  [{sd}] HALT: primes disagree {ks}")
            continue
        side_rec.update(nullity=int(k), mult=int(a - k), i=int(k),
                        status=('proved: mult = a (nullity 0 at %s)' % ', '.join(str(p) for p in ks)) if k == 0
                        else f'measured: nullity {k} at both primes; mult >= {a-k} proved, = {a-k} measured')
        kern_by[sd] = {x['prime']: x.get('kern', []) for x in rs}
        # cross-prime consistency of the kernel spaces is meaningful only over Z: below
        if k > 0:
            side_rec['kernel_verified_full_matrix_mod_p'] = {}
            for x in rs:
                p = x['prime']
                EVp = sparse.csr_matrix(ev_rows_from_pencils(arr, FORMS[sd], pencils(K, x['seed']), p))
                F = sparse.vstack([E, EVp]).tocsr()
                side_rec['kernel_verified_full_matrix_mod_p'][str(p)] = all(check_kernel_full(F, nc, p, v) for v in x['kern'])
                side_rec.setdefault('kernel_rank_mod_p', {})[str(p)] = rank_modp(x['kern'], nc, p)
        rec['sides'][sd] = side_rec
        log(f"  [{sd}] nullity = {k} at primes {ks} -> mult_{sd} = {a-k}, i_{sd} = {k}")

    # ---- exact (over Z) treatment of the kernel vectors: reconstruction and checks
    rec['over_Z'] = {}
    intvecs = {}
    for sd in sides:
        if sd not in kern_by or not kern_by[sd].get(P1):
            continue
        other = 'per' if sd == 'det' else 'det'
        vints = []
        proofs = []
        for vi, v0 in enumerate(kern_by[sd][P1]):
            vint = reconstruct_integer(v0, P1)
            pr = dict(reconstructed=vint is not None)
            if vint is not None:
                Ev = sparse_dot_exact(E, vint)
                pr['E_v_zero_over_Z'] = all(x == 0 for x in Ev)
                pr['support'] = int(sum(1 for x in vint if x))
                pr['max_abs_coeff'] = int(max(abs(x) for x in vint))
                # lies in the mod-P2 kernel span (P2 vectors are a random basis of ker mod P2)
                if kern_by[sd].get(P2):
                    kP2 = kern_by[sd][P2]
                    red = [x % P2 for x in vint]
                    pr['in_mod_P2_kernel_span'] = rank_modp(kP2 + [red], nc, P2) == rank_modp(kP2, nc, P2)
                # exact evaluations over Z
                same = [coeffs_of(FORMS[sd], pen) for pen in pencils(12, SEEDS['fresh_' + sd])]
                oth = [coeffs_of(FORMS[other], pen) for pen in pencils(12, SEEDS['fresh_' + other])]
                gen = generic_cubics(4, SEEDS['fresh_generic'])
                vs = eval_exact_many(arr, vint, same)
                vo = eval_exact_many(arr, vint, oth)
                vg = eval_exact_many(arr, vint, gen)
                pr[f'vanishes_fresh_{sd}_over_Z'] = all(x == 0 for x in vs)
                pr[f'n_fresh_{sd}'] = len(vs)
                pr[f'nonzero_fresh_{other}_over_Z'] = [x != 0 for x in vo]
                pr['nonzero_generic_cubic_over_Z'] = [x != 0 for x in vg]
                vints.append(vint)
            proofs.append(pr)
            log(f"  [{sd}] kernel vector {vi}: {pr}")
        rec['over_Z'][sd] = proofs
        intvecs[sd] = vints

    # ---- the intersection U_D ∩ U_P and the orientation, mod P1 (and P2)
    if 'det' in kern_by and 'per' in kern_by:
        inter = {}
        for p in primes:
            UD = kern_by['det'].get(p, []); UP = kern_by['per'].get(p, [])
            rD = rank_modp(UD, nc, p); rP = rank_modp(UP, nc, p); rDP = rank_modp(UD + UP, nc, p)
            inter[str(p)] = dict(dim_UD=rD, dim_UP=rP, dim_intersection=rD + rP - rDP,
                                 UD_subset_UP=(rDP == rP), UP_subset_UD=(rDP == rD))
        rec['intersection'] = inter
        iD = rec['sides']['det'].get('i'); iP = rec['sides']['per'].get('i')
        if iD is not None and iP is not None:
            rec['D'] = int(iD - iP)
            rec['decision'] = ('D > 0: multiplicity obstruction (i_per < i_det)' if iD > iP else
                               'D = 0: orientation test decides' if iD == iP else 'D < 0')
            log(f"  D = i_det - i_per = {iD} - {iP} = {rec['D']}; intersection {inter[str(P1)]}")

    # ---- the explicit basis M_delta = ker E (full-E solve), the u-free rank and the birth space
    fe = [x for x in res if x['side'] == 'fullE']
    if fe:
        x = fe[0]
        Mb = x.get('kern', [])
        rec['fullE'] = dict(nullity=x['nullity'], level=x['level'], secs=x['secs'], diag=x['diag'],
                            equals_a=(x['nullity'] == a))
        if x['nullity'] != a:
            rec['fullE']['status'] = 'HALT: nullity(E) != a (stopping rule R3)'
            log(f"  fullE HALT: nullity {x['nullity']} != a {a}")
        else:
            Mb_arr = np.array(Mb, dtype=np.int64)
            ufr = rank_modp([v[uf].tolist() for v in Mb_arr], len(uf), P1) if len(uf) else 0
            rec['fullE'].update(rank_on_ufree_columns=int(ufr), birth_dim=int(ufr),
                                dim_J_M_prev=int(a - ufr), n_ufree_columns=int(len(uf)))
            # every kernel vector of the sides lies in M (it must: ker[E; ev] ⊆ ker E)
            for sd in kern_by:
                for v in kern_by[sd].get(P1, []):
                    assert rank_modp(Mb + [v], nc, P1) == a, ("side kernel vector not in ker E", sd)
                ufp = [int(rank_modp([np.array(v, dtype=np.int64)[uf].tolist()], len(uf), P1)) for v in kern_by[sd].get(P1, [])]
                rec['fullE'][f'{sd}_kernel_ufree_part_nonzero'] = [bool(u) for u in ufp]
            np.savez_compressed(os.path.join(ART, f"s73_M_basis_d{delta}_p1.npz"), M=Mb_arr, prime=np.int64(P1),
                                lam=np.array(lam), delta=np.int64(delta), a=np.int64(a))
            log(f"  fullE: nullity(E) = {x['nullity']} = a; rank on the {len(uf)} u-free columns = {ufr} "
                f"(birth space dim {ufr}, dim J(M_prev) = {a-ufr})")

    # ---- artefacts: kernel vectors (mod both primes and over Z) with the pencils used
    art = dict(cell=dict(n=N_DEG, r=R, lam=list(lam), delta=int(delta), a=int(a), n_chi=int(nc)),
               note="kernel vectors of [E; ev_side] in chi-coordinates (coefficient of monomial m = vec[col_of[m]]*sgn[m], "
                    "wk9_s45_build conventions; chi-basis representatives in s73_chi_basis_d<delta>.npz); "
                    "'int' vectors are exact over Z (rationally reconstructed from P1, verified E v = 0 over Z)",
               seeds={sd: rec['sides'][sd].get('seed') for sd in sides if sd in rec['sides']},
               pencils={sd: [pencil_record(pen) for pen in pencils(K, rec['sides'][sd]['seed'])]
                        for sd in sides if sd in rec['sides'] and rec['sides'][sd].get('seed') is not None},
               U={sd: dict(mod_p={str(p): kern_by[sd].get(p, []) for p in primes}, int=intvecs.get(sd, []))
                  for sd in kern_by})
    with gzip.open(os.path.join(ART, f"s73_kernels_d{delta}_{seedtag}.json.gz"), 'wt', encoding='utf-8') as fh:
        json.dump(art, fh, separators=(',', ':'))
    rec['secs'] = round(time.time() - t0, 1)
    return rec


if __name__ == '__main__':
    args = sys.argv[1:]
    delta = int(args[0])
    def opt(name, default):
        return args[args.index(name) + 1] if name in args else default
    sides = tuple(opt('--sides', 'det,per').split(','))
    fullE = '--fullE' in args
    K = int(opt('--K', 0)) or None
    primes = PRIMES if opt('--primes', 'both') == 'both' else (P1,)
    levels = opt('--levels', 's42')
    seedtag = opt('--seedtag', 'primary')
    outpath = opt('--out', os.path.join(ROOT, 'results', 's73_dladder.jsonl'))
    lam = tuple(int(x) for x in opt('--lam', '').split(',')) if '--lam' in args else None
    rec = run(delta, sides=sides, fullE=fullE, K=K, primes=primes, levels=levels, seedtag=seedtag, lam=lam)
    with open(outpath, 'a') as fh:
        fh.write(json.dumps(rec) + "\n")
    log(f"rung {delta} banked to {outpath}: " + json.dumps({k: rec.get(k) for k in ('a', 'D', 'decision')}))

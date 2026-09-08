#!/usr/bin/env python3
"""Session 73 -- the first-row transport between two rungs, checked on both engines.

J = multiplication by c = c_{(3,0,...,0)} carries V_chi(delta) -> V_chi(delta+1)
(Lemma L, s57; the proof is verbatim at n = 3).  Given the two independently
built cells (analysis/wk11_s73_cell.py at delta and delta+1) this script

  1. transports the explicit basis M_delta = ker E_delta (when banked) and checks
     E_{delta+1} J(v) = 0 mod P1 for every basis vector and rank J(M_delta) = a_delta
     (injectivity); with M_{delta+1} banked too, checks J(M_delta) ⊆ M_{delta+1} and
     reads off the birth dimension a_{delta+1} - a_delta;
  2. transports the exhibited INTEGER kernel vectors U_D(delta), U_P(delta) and checks
     E_{delta+1} J(v) = 0 over Z, then compares J(U_X(delta)) with the directly
     measured U_X(delta+1): containment mod both primes and, over Z, equality of
     the primitive integer vectors up to sign when both are lines;
  3. reads off, mod P1, whether U_X(delta+1) = J(U_X(delta)) (the rung's kernel is
     the transported one) or strictly larger (a vector born at delta+1).

usage: python3 analysis/wk11_s73_transport.py <delta_lo> [--out results/s73_transport.jsonl]
"""
import gzip
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from wk11_s73_lib import (ROOT, ART, PRIMES, P1, P2, log, lam_of, a_two_ways, load_build, Lookup,   # noqa: E402
                          transport, chi_reps, ufree_columns, sparse_dot_exact, check_hwv_modp,
                          rank_modp, reconstruct_integer)


def load_kernels(delta, seedtag='primary'):
    path = os.path.join(ART, f"s73_kernels_d{delta}_{seedtag}.json.gz")
    if not os.path.exists(path):
        return None
    with gzip.open(path, 'rt', encoding='utf-8') as fh:
        return json.load(fh)


def load_M(delta):
    path = os.path.join(ART, f"s73_M_basis_d{delta}_p1.npz")
    if not os.path.exists(path):
        return None
    z = np.load(path)
    return [row.tolist() for row in z['M']]


def primitive(vint):
    import math
    g = 0
    for x in vint:
        g = math.gcd(g, abs(x))
    v = [x // g for x in vint] if g > 1 else list(vint)
    for x in v:
        if x:
            return v if x > 0 else [-y for y in v]
    return v


def run(dlo, seedtag='primary'):
    dhi = dlo + 1
    lam_lo, lam_hi = lam_of(dlo), lam_of(dhi)
    a_lo, a_hi = a_two_ways(lam_lo, dlo), a_two_ways(lam_hi, dhi)
    out = dict(session=73, delta_lo=dlo, delta_hi=dhi, lam_lo=list(lam_lo), lam_hi=list(lam_hi), a_lo=a_lo, a_hi=a_hi)
    t0 = time.time()
    arr_lo, E_lo = load_build(dlo)
    arr_hi, E_hi = load_build(dhi)
    nc_lo, nc_hi = arr_lo['n_chi'], arr_hi['n_chi']
    out.update(n_chi_lo=nc_lo, n_chi_hi=nc_hi)
    look = Lookup(arr_lo)
    log(f"transport {dlo} -> {dhi}: n_chi {nc_lo} -> {nc_hi}, a {a_lo} -> {a_hi} (builds loaded, {time.time()-t0:.0f}s)")

    # 1. the explicit bases
    M_lo, M_hi = load_M(dlo), load_M(dhi)
    if M_lo is not None:
        JM = [transport(arr_lo, look, arr_hi, np.array(v, dtype=np.int64), modulus=P1) for v in M_lo]
        hw = [bool(check_hwv_modp(E_hi, nc_hi, P1, v)) for v in JM]
        rk = rank_modp([v.tolist() for v in JM], nc_hi, P1)
        out['J_M_lo'] = dict(count=len(JM), all_highest_weight_mod_P1=all(hw), rank_mod_P1=rk,
                             injective=(rk == len(JM) == a_lo))
        log(f"  J(M_{dlo}): {len(JM)} vectors, all HWV at {dhi}: {all(hw)}, rank {rk} (a_lo = {a_lo})")
        if M_hi is not None:
            rk2 = rank_modp([v.tolist() for v in JM] + M_hi, nc_hi, P1)
            out['J_M_lo']['contained_in_M_hi'] = (rk2 == a_hi)
            out['J_M_lo']['birth_dim'] = int(a_hi - rk)
            log(f"  J(M_{dlo}) ⊆ M_{dhi}: {rk2 == a_hi}; birth dimension a_hi - rank = {a_hi - rk}")
        # u-free reading at the upper rung: rank of M_hi on the u-free columns = birth dim
        if M_hi is not None:
            uf = ufree_columns(arr_hi)
            ufr = rank_modp([np.array(v, dtype=np.int64)[uf].tolist() for v in M_hi], len(uf), P1)
            out['J_M_lo']['ufree_rank_M_hi'] = int(ufr)
            out['J_M_lo']['ufree_rank_equals_birth'] = (ufr == a_hi - rk)

    # 2./3. the kernel lines
    K_lo, K_hi = load_kernels(dlo, seedtag), load_kernels(dhi, seedtag)
    out['sides'] = {}
    if K_lo is not None:
        for sd in ('det', 'per'):
            U_lo = K_lo['U'].get(sd, {})
            ints = U_lo.get('int', [])
            rec = dict(dim_lo=len(U_lo.get('mod_p', {}).get(str(P1), [])), n_int_lo=len(ints))
            if not ints and not U_lo.get('mod_p', {}).get(str(P1)):
                rec['note'] = 'U empty at the lower rung: nothing to transport'
                out['sides'][sd] = rec
                continue
            Jint = [transport(arr_lo, look, arr_hi, v, modulus=None) for v in ints]
            rec['E_hi_J_v_zero_over_Z'] = [all(x == 0 for x in sparse_dot_exact(E_hi, jv)) for jv in Jint]
            rec['J_int_support'] = [int(sum(1 for x in jv if x)) for jv in Jint]
            Jmod = {p: [transport(arr_lo, look, arr_hi, np.array(v, dtype=np.int64), modulus=p)
                        for v in U_lo['mod_p'][str(p)]] for p in PRIMES if str(p) in U_lo['mod_p']}
            if K_hi is not None and sd in K_hi['U']:
                U_hi = K_hi['U'][sd]
                for p in PRIMES:
                    if str(p) not in U_hi['mod_p'] or p not in Jmod:
                        continue
                    hi = U_hi['mod_p'][str(p)]
                    lo = [v.tolist() for v in Jmod[p]]
                    rh, rl, rb = rank_modp(hi, nc_hi, p), rank_modp(lo, nc_hi, p), rank_modp(hi + lo, nc_hi, p)
                    rec[f'mod_{p}'] = dict(dim_U_hi=rh, dim_J_U_lo=rl, J_U_lo_subset_U_hi=(rb == rh),
                                           U_hi_equals_J_U_lo=(rb == rh == rl),
                                           born_at_hi=int(rh - rl))
                hi_int = U_hi.get('int', [])
                if len(ints) == 1 and len(hi_int) == 1:
                    rec['over_Z_lines_equal'] = (primitive(Jint[0]) == primitive(hi_int[0]))
            out['sides'][sd] = rec
            log(f"  [{sd}] transport of {len(ints)} integer vector(s): {rec}")
    out['secs'] = round(time.time() - t0, 1)
    return out


if __name__ == '__main__':
    dlo = int(sys.argv[1])
    outp = sys.argv[sys.argv.index('--out') + 1] if '--out' in sys.argv else os.path.join(ROOT, 'results', 's73_transport.jsonl')
    rec = run(dlo)
    with open(outp, 'a') as fh:
        fh.write(json.dumps(rec) + "\n")
    log("banked")

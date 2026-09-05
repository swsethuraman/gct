#!/usr/bin/env python3
"""
Session 52 -- the `a = 1` census at n = 4, r = 6.

Region (fixed in results/PREREG_s52.md before any run):
  n = 4, length-reduced model at r = 6 variables, ell(lam) = 6 exactly,
  lam |- 4*delta, obstruction-eligible iff lam_1 >= delta.

Per cell: a, h_pad, N_S, |Stab|, the n_chi lower bound N_S/|Stab|, eligibility,
and the informative flag h_pad >= 1 (Lemma A of the pre-registration: at a = 1,
h_pad = 0 forces mult_pad = 0 hence D <= 0 with no measurement).

Two independent routes for `a`:
  A  Frobenius plethysm            wk8_s30_pleth.amb          (all cells at once)
  B  Weyl alternation + tail DP    wk9_s42_census.a_weyl      (per cell)
Route B is run on every a <= 1 cell and on a sample of the rest, and asserted
equal to route A.  h_pad by wk9_s42_hpad.h_pad (Pieri strips over the cubic
plethysm); a sample is re-checked by wk9_s42_census.h_pad_weyl.

usage: python3 wk9_s52_census.py DELTA [DELTA ...] [--out results/s52_cells.jsonl]
                                 [--sample 40] [--nchi-cap 400000]
"""
import sys, os, json, time, random

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from wk8_s30_pleth import amb, chi
from wk9_s42_hpad import h_pad as h_pad_pleth
from wk9_s36_census import N_S as N_S_dp, stab_order


def log(*a):
    print(*a, file=sys.stderr, flush=True)


def census(delta, sample=40, seed=52, nchi_cap=400_000):
    t0 = time.time()
    A = amb(delta, 4, 6)
    l6 = sorted(l for l in A if len(l) == 6)
    log(f"[s52census d{delta}] route A: {len(l6)} ell=6 cells with a>=1 "
        f"({sum(A[l] for l in l6)} units)  [{time.time()-t0:.0f}s]")
    rows = []
    for lam in l6:
        a = A[lam]
        elig = lam[0] >= delta
        rec = dict(lam=list(lam), delta=delta, ell=6, a=a, eligible=elig,
                   bal=lam[0] - lam[-1])
        if a == 1:
            rec['h_pad'] = h_pad_pleth(lam, delta)
            rec['informative'] = rec['h_pad'] >= 1
            ns = N_S_dp(4, 6, delta, lam)
            so = stab_order(lam)
            rec.update(N_S=ns, stab=so, nchi_lb=(ns + so - 1) // so)
        rows.append(rec)
    log(f"[s52census d{delta}] h_pad + N_S done  [{time.time()-t0:.0f}s]")

    # route B cross-check
    from wk9_s42_census import a_weyl
    cache = {}
    todo = [tuple(r['lam']) for r in rows if r['a'] == 1]
    rest = [tuple(r['lam']) for r in rows if r['a'] != 1]
    random.Random(seed).shuffle(rest)
    todo = todo + rest[:sample]
    nb = 0
    for lam in todo:
        v = a_weyl(lam, delta, 4, cache)
        assert v == A[lam], ("route A/B disagree", lam, delta, A[lam], v)
        nb += 1
    log(f"[s52census d{delta}] route B agreed at {nb} cells "
        f"({len([r for r in rows if r['a']==1])} of them a=1)  [{time.time()-t0:.0f}s]")

    # h_pad second route on a sample of the a=1 cells
    from wk9_s42_census import h_pad_weyl
    a1 = [tuple(r['lam']) for r in rows if r['a'] == 1]
    random.Random(seed + 1).shuffle(a1)
    nh = 0
    for lam in a1[:sample]:
        hv = h_pad_weyl(lam, delta, cache)
        ref = [r for r in rows if tuple(r['lam']) == lam][0]['h_pad']
        assert hv == ref, ("h_pad routes disagree", lam, delta, ref, hv)
        nh += 1
    log(f"[s52census d{delta}] h_pad route 2 agreed at {nh} a=1 cells  [{time.time()-t0:.0f}s]")

    el = [r for r in rows if r['eligible']]
    a1e = [r for r in el if r['a'] == 1]
    inf = [r for r in a1e if r['informative']]
    log(f"[s52census d{delta}] SUMMARY eligible={len(el)} units={sum(r['a'] for r in el)} "
        f"a1_eligible={len(a1e)} informative(h_pad>=1)={len(inf)} "
        f"a1_all_ell6={len([r for r in rows if r['a']==1])}  [{time.time()-t0:.0f}s]")
    chi.cache_clear()
    return rows


if __name__ == '__main__':
    argv = sys.argv[1:]
    out = 'results/s52_cells.jsonl'; sample = 40; deltas = []
    i = 0
    while i < len(argv):
        if argv[i] == '--out': out = argv[i + 1]; i += 2
        elif argv[i] == '--sample': sample = int(argv[i + 1]); i += 2
        elif argv[i] == '--nchi-cap': i += 2
        else: deltas.append(int(argv[i])); i += 1
    fh = open(out, 'a')
    for d in deltas:
        for r in census(d, sample=sample):
            fh.write(json.dumps(r) + "\n")
        fh.flush()
    fh.close()
    log("[s52census] done ->", out)

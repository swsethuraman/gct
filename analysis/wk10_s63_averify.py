#!/usr/bin/env python3
"""
Session 63 -- independent reproduction of the LMR source multiplicities
a_23 = a((61,17,2^7),23) and a_24 = a((65,17,2^7),24), and the whole LMR
a-ladder, by a route written from scratch here and anchored to the definition.

    a(lam, delta) = mult of S_lam(C^r) in Sym^delta(Sym^4 C^r)
                  = sum_{w in S_r} sgn(w) * K(w(lam+rho) - rho ; delta)

with K(mu; delta) the weight-mu dimension of Sym^delta(Sym^4 C^r) = the number
of delta-element MULTISETS of exponent vectors alpha in N^r, |alpha| = 4, with
sum = mu.  K depends only on the multiset {mu_i} (permuting the r variables is a
symmetry of the space), so we evaluate it on mu sorted DESCENDING and take the
largest coordinate as the "free" one of the tail DP -- which minimises the DP box.

Independence.  This file shares no code with wk8_s30_pleth (the direct
partition-sum route `amb`), with wk9_s42_census.a_weyl (the programme's exact
Weyl route) or with wk9_s57_lib.a_weyl_mod (the programme's modular Weyl route).
It is cross-checked against ALL THREE:
  * `amb` is the DEFINITION (chi^lam paired with the plethysm h_delta[h_4] summed
    over every partition of N) -- feasible only for small N; the anchor.
  * a_weyl / a_weyl_mod are the programme's own audited routes -- the reproduction.

The DP is modular at the two house primes and Chinese-remaindered; K at the LMR
cell is ~1.5e11, comfortably inside P1*P2 ~ 4.6e18.

usage:
  python3 analysis/wk10_s63_averify.py anchor      # my route == amb, small LMR-family cells
  python3 analysis/wk10_s63_averify.py ladder      # the LMR a-ladder delta=12..25 (+31 endpoint)
  python3 analysis/wk10_s63_averify.py cross        # my route == programme a_weyl at delta<=~16
  python3 analysis/wk10_s63_averify.py all
"""
import sys, os, time, json, itertools
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.normpath(os.path.join(HERE, '..'))
import numpy as np

P1, P2 = 2147483647, 2147483629


def log(*a):
    print(*a, file=sys.stderr); sys.stderr.flush()


# ------------------------------------------------------------ my tail enum
def _tails(rm1, cap=4):
    """all beta in N^{rm1} with |beta| <= cap (rm1 = r-1 tail slots)."""
    out = []
    def rec(k, left, cur):
        if k == rm1:
            out.append(tuple(cur)); return
        for v in range(left + 1):
            rec(k + 1, left - v, cur + [v])
    rec(0, cap, [])
    return out


_KCACHE = {}


def K_exact(mu, delta, _cache=_KCACHE):
    """weight multiplicity K(mu; delta) of Sym^delta(Sym^4 C^r), EXACT int64,
    mu any composition.  Evaluated on the descending sort (K is
    permutation-symmetric), largest coordinate free -- which minimises the DP
    box.  No modular reduction: K <= N_S ~ 1.5e11 < 2^62, so int64 is exact
    (asserted).  numpy DP over the tail box."""
    key = tuple(sorted((int(x) for x in mu), reverse=True))
    if any(x < 0 for x in key) or sum(key) != 4 * delta:
        return 0
    ck = (key, delta)
    if ck in _cache:
        return _cache[ck]
    r = len(key)
    tail = key[1:]                      # drop the largest (free) coordinate
    rm1 = r - 1
    if rm1 == 0:
        _cache[ck] = 1; return 1
    shape = (delta + 1,) + tuple(t + 1 for t in tail)
    F = np.zeros(shape, dtype=np.int64)
    F[(0,) * len(shape)] = 1
    betas = [b for b in _tails(rm1, 4) if all(b[i] <= tail[i] for i in range(rm1))]
    for beta in betas:
        src = tuple(slice(0, tail[i] + 1 - beta[i]) for i in range(rm1))
        dst = tuple(slice(beta[i], tail[i] + 1) for i in range(rm1))
        for d in range(1, delta + 1):
            F[(d,) + dst] += F[(d - 1,) + src]
    v = int(F[(delta,) + tail])
    assert v < (1 << 62), ("int64 headroom exceeded", key, delta, v)
    _cache[ck] = v
    return v


def a_indep(lam, delta, verbose=False):
    """my Weyl-alternation plethysm multiplicity a(lam,delta), EXACT.

        a = sum_{w in S_r} sgn(w) K(w(lam+rho) - rho ; delta),  K exact int64.
    """
    lam = tuple(int(x) for x in lam if x != 0)
    r = len(lam)
    rho = [r - 1 - i for i in range(r)]
    lr = [lam[i] + rho[i] for i in range(r)]
    acc = 0
    used = [False] * r
    perm = [0] * r
    nterms = 0
    seen = set()
    t0 = time.time()
    def sign_of(pm):
        s = 1
        for i in range(r):
            for j in range(i + 1, r):
                if pm[i] > pm[j]: s = -s
        return s
    def rec(i):
        nonlocal acc, nterms
        if i == r:
            mu = tuple(lr[perm[t]] - rho[t] for t in range(r))
            acc += sign_of(perm) * K_exact(mu, delta)
            nterms += 1
            seen.add(tuple(sorted(mu, reverse=True)))
            return
        for j in range(r):
            if not used[j] and lr[j] - rho[i] >= 0:
                used[j] = True; perm[i] = j
                rec(i + 1)
                used[j] = False
    rec(0)
    assert acc >= 0, ("negative plethysm coefficient", lam, delta, acc)
    if verbose:
        log(f"    a_indep({lam},{delta}) = {acc}  ({nterms} Weyl terms, {len(seen)} distinct K, {time.time()-t0:.1f}s)")
    return acc, nterms, len(seen)


# --------------------------------------------------------- LMR family / ladder
def lmr_tail_cell(delta):
    """the LMR ladder cell at degree delta: lambda = (4*delta - 31, 17, 2^7)."""
    lam1 = 4 * delta - 31
    return (lam1, 17, 2, 2, 2, 2, 2, 2, 2)


def family_cell(k, m):
    """the boundary LMR-type family lambda(k,m) = (3k+2m, k, 2^m) at delta=k+m."""
    return (3 * k + 2 * m,) + (k,) + (2,) * m, k + m


# ----------------------------------------------------------------- commands
def cmd_anchor():
    """my route == amb (the definition, direct partition sum over p(N)) on small
    LMR-family cells and on the LMR tail at small delta."""
    from wk8_s30_pleth import amb
    log("[anchor] my Weyl route vs amb (direct partition sum = the definition)")
    rows = []
    cells = []
    # boundary family small members (2*delta = |rho|+rho_1 with equality), N <= 36
    for (k, m) in [(2, 1), (3, 1), (2, 2), (3, 2), (4, 2), (4, 3), (5, 3), (5, 4)]:
        lam, delta = family_cell(k, m)
        cells.append((lam, delta, f"family(k={k},m={m})"))
    # a couple of generic length-<=5 cells to exercise the route off the family
    cells.append(((8, 4, 2, 2), 4, "generic(8,4,2,2)"))
    cells.append(((12, 4, 2, 2), 5, "generic(12,4,2,2)"))
    ok = True
    for lam, delta, tag in cells:
        N = 4 * delta
        t0 = time.time()
        D = amb(delta, 4, len(lam))            # dict lam -> a, over all partitions of N
        a_def = D.get(tuple(x for x in lam if x), 0)
        t_def = time.time() - t0
        a_me, nt, nd = a_indep(lam, delta)
        match = (a_me == a_def)
        ok = ok and match
        rows.append(dict(cell=tag, lam=list(lam), delta=delta, N=N, a_amb=a_def,
                         a_indep=a_me, weyl_terms=nt, match=match, amb_secs=round(t_def, 1)))
        log(f"  {tag:22s} lam={lam} d={delta}: amb={a_def}  indep={a_me}  {'OK' if match else '*** MISMATCH ***'}")
    print(json.dumps(dict(check="anchor", all_match=ok, rows=rows), indent=1))
    return ok


def cmd_cross():
    """my route == the programme's own audited Weyl routes.
    a_weyl_mod (wk9_s57_lib, modular+CRT, sorts the key) runs the whole LMR
    ladder; a_weyl (wk9_s42_census, exact, unsorted box) is used only on small
    cells where its box is safe."""
    from wk9_s57_lib import a_weyl_mod
    from wk9_s42_census import a_weyl
    log("[cross] my Weyl route vs programme a_weyl_mod (whole ladder) and a_weyl (small cells)")
    rows = []
    ok = True
    cache = {}
    # a_weyl_mod across the whole ladder incl. the two targets
    for delta in list(range(12, 25)):
        lam = lmr_tail_cell(delta)
        a_prog, _, _ = a_weyl_mod(lam, delta, 4, cache)
        a_me, nt, nd = a_indep(lam, delta)
        match = (a_me == a_prog)
        ok = ok and match
        rows.append(dict(lam=list(lam), delta=delta, route="a_weyl_mod", a_prog=a_prog, a_indep=a_me, match=match))
        log(f"  lam={lam} d={delta}: a_weyl_mod={a_prog}  indep={a_me}  {'OK' if match else '*** MISMATCH ***'}")
    # a_weyl (exact, s42) on small safe cells for a third route
    for lam, delta in [((16, 4, 2, 2), 6), ((18, 4, 2, 2, 2), 7), ((21, 5, 2, 2, 2), 8), ((8, 4, 2, 2), 4)]:
        a_prog = a_weyl(lam, delta, 4, {})
        a_me, nt, nd = a_indep(lam, delta)
        match = (a_me == a_prog)
        ok = ok and match
        rows.append(dict(lam=list(lam), delta=delta, route="a_weyl(s42)", a_prog=a_prog, a_indep=a_me, match=match))
        log(f"  lam={lam} d={delta}: a_weyl(s42)={a_prog}  indep={a_me}  {'OK' if match else '*** MISMATCH ***'}")
    print(json.dumps(dict(check="cross", all_match=ok, rows=rows), indent=1))
    return ok


LADDER_JSONL = os.path.join(ROOT, 'results', 's63_aladder.jsonl')


def cmd_ladstep(deltas):
    """compute a for the given LMR-ladder degrees, appending one JSON line each
    to results/s63_aladder.jsonl (checkpointed so batches survive the wall clock)."""
    done = {}
    if os.path.exists(LADDER_JSONL):
        for ln in open(LADDER_JSONL):
            try:
                r = json.loads(ln); done[r['delta']] = r
            except Exception:
                pass
    fh = open(LADDER_JSONL, 'a')
    for delta in deltas:
        if delta in done:
            log(f"  delta={delta} already done (a={done[delta]['a']})"); continue
        lam = lmr_tail_cell(delta)
        t0 = time.time()
        a, nt, nd = a_indep(lam, delta)
        row = dict(delta=delta, lam1=lam[0], lam=list(lam), a=a, weyl_terms=nt, distinctK=nd, secs=round(time.time() - t0, 1))
        fh.write(json.dumps(row) + "\n"); fh.flush()
        log(f"  delta={delta:2d}  lam1={lam[0]:2d}  a={a:4d}  ({time.time()-t0:.1f}s)")
    fh.close()
    return True


def cmd_ladder():
    """assemble the ladder from the checkpoint file and report the verdict."""
    rows = {}
    for ln in open(LADDER_JSONL):
        r = json.loads(ln); rows[r['delta']] = r
    seq = [rows[d]['a'] for d in range(12, 26) if d in rows]
    incs = [None] + [seq[i] - seq[i - 1] for i in range(1, len(seq))]
    for i, d in enumerate(range(12, 12 + len(seq))):
        rows[d]['inc'] = incs[i]
    expected = [2, 39, 93, 145, 188, 219, 241, 255, 264, 269, 272, 273, 274, 274]
    a23 = rows[23]['a']; a24 = rows[24]['a']
    a31 = rows.get(31, {}).get('a')
    res = dict(check="ladder", ladder=seq, expected_12_25=expected,
               matches_s57_s58=(seq == expected[:len(seq)]),
               a_23=a23, a_24=a24, a23_ok=(a23 == 273), a24_ok=(a24 == 274),
               a_inf_31=a31, a_inf_ok=(a31 == 274) if a31 is not None else None,
               final_increment=rows[24]['a'] - rows[23]['a'],
               monotone=all(seq[i + 1] >= seq[i] for i in range(len(seq) - 1)),
               rows=[rows[d] for d in sorted(rows)])
    print(json.dumps(res, indent=1))
    ok = res['a23_ok'] and res['a24_ok'] and res['matches_s57_s58']
    if a31 is not None:
        ok = ok and res['a_inf_ok']
    return ok


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'all'
    results = {}
    if cmd in ('anchor', 'all'):
        results['anchor'] = cmd_anchor()
    if cmd in ('cross', 'all'):
        results['cross'] = cmd_cross()
    if cmd == 'ladstep':
        ds = [int(x) for x in sys.argv[2:]] if len(sys.argv) > 2 else list(range(12, 26)) + [31]
        results['ladstep'] = cmd_ladstep(ds)
    if cmd in ('ladder', 'all'):
        results['ladder'] = cmd_ladder()
    log("SUMMARY " + json.dumps(results))
    sys.exit(0 if all(results.values()) else 1)

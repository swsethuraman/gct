#!/usr/bin/env python3
"""B13-04 -- independent re-derivation of the horizontal-13-strip predecessors
of lambda_13 = (21,17,2^7) for the degree-13 cubic side (n = 3, r = 9).

Own interlacing enumerator (mu_i between lam_{i+1} and lam_i, mu_r may be 0),
N_S by tools/verify/chi_build.weight_monomials_count (the tail DP), and the
cubic plethysm coefficient a^{(3)}(mu, 13) by the Kostant alternation over S_r
with weight multiplicities from that tail DP (the Frobenius route of
analysis/wk8_s30_pleth exceeds this host's memory at delta = 13 and is not
used).  Also prints the fixed-factor weight lam^- = (lam_1 - delta, lam_2, ...)
and its weight-space dimension, and the quartic-side a^{(4)}(lambda_13, 13) by
the same Kostant route.

Writes results/b13_04/pred13.json.  Nothing here evaluates anything at points.
"""
import sys, os, json, time
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'verify'))
sys.path.insert(0, HERE)
sys.setrecursionlimit(100000)
from chi_build import weight_monomials_count

LAM = (21, 17, 2, 2, 2, 2, 2, 2, 2)
DELTA = 13
N = 3
R = 9


def predecessors(lam, k):
    """all mu with lam/mu a horizontal k-strip: lam_1 >= mu_1 >= lam_2 >= mu_2
    >= ... >= lam_r >= mu_r >= 0 and |mu| = |lam| - k.  Shorter mu (mu_r = 0)
    are included: interlacing allows it."""
    r = len(lam)
    out = []

    def rec(i, cur, left):
        if i == r:
            if left == 0:
                out.append(tuple(cur))
            return
        lo = lam[i + 1] if i + 1 < r else 0
        hi = lam[i]
        for m in range(hi, lo - 1, -1):
            if m > left:
                continue
            rec(i + 1, cur + [m], left - m)

    rec(0, [], sum(lam) - k)
    return out


def perm_sign(p):
    s = 1
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                s = -s
    return s


def kostant(n, r, delta, lam):
    """a(lam, delta) = sum_w sgn(w) m(w(lam+rho) - rho) over S_r, m from the tail DP.
    Permutations are enumerated position by position with the constraint
    (lam+rho)_{w(i)} >= rho_i, which prunes the terms that vanish."""
    lam = tuple(lam) + (0,) * (r - len(lam))
    rho = [r - 1 - i for i in range(r)]
    lr = [lam[i] + rho[i] for i in range(r)]
    total = 0
    cache = {}

    def rec(i, used, mu):
        nonlocal total
        if i == r:
            # weight multiplicities are W-invariant: sort mu descending, which also
            # makes the tail DP box (coordinates 2..r) as small as it can be
            key = tuple(sorted(mu, reverse=True))
            if key not in cache:
                cache[key] = weight_monomials_count(n, r, delta, key)
            perm = used
            total += perm_sign(perm) * cache[key]
            return
        for k in range(r):
            if k in used:
                continue
            v = lr[k] - rho[i]
            if v < 0:
                continue
            rec(i + 1, used + [k], mu + [v])

    rec(0, [], [])
    return total


def trim(mu):
    return tuple(x for x in mu if x)


def main():
    t0 = time.time()
    preds = predecessors(LAM, DELTA)
    rows = []
    for mu in preds:
        mt = trim(mu)
        ns = weight_monomials_count(N, len(mt), DELTA, mt)
        rows.append(dict(mu=list(mt), parts=len(mt), size=sum(mt), N_S=ns))
    print(f"lambda_13 = {LAM}  |lambda| = {sum(LAM)}  delta = {DELTA}")
    print(f"horizontal-{DELTA}-strip predecessors: {len(preds)}")
    bad = [r for r in rows if r['size'] != 3 * DELTA or r['parts'] > R]
    print(f"malformed (size != {3*DELTA} or more than {R} parts): {bad}")
    lam_minus = (LAM[0] - DELTA,) + LAM[1:]
    ns_minus = weight_monomials_count(N, R, DELTA, lam_minus)
    print(f"fixed-factor weight lam^- = {lam_minus}, weight-space dim = {ns_minus:,}")
    sys.stdout.flush()

    # cubic plethysm coefficients by the Kostant alternation
    #   a(nu) = sum_{w in S_r} sgn(w) m(w(nu + rho) - rho),
    # with every weight multiplicity m(.) read from the tail DP of
    # tools/verify/chi_build.weight_monomials_count (a count, not an
    # enumeration).  Independent of analysis/wk8_s30_pleth (Frobenius), which
    # exceeds this host's memory at delta = 13.
    a3 = {}
    t1 = time.time()
    for mu in preds:
        mt = trim(mu)
        a3[mt] = kostant(N, len(mt), DELTA, mt)
    print(f"a^(3) by Kostant alternation + tail DP in {time.time()-t1:.0f}s")
    t1 = time.time()
    a4 = kostant(4, R, DELTA, LAM)
    print(f"a^(4)(lambda_13, 13) = {a4}  (Kostant + tail DP, {time.time()-t1:.0f}s)")
    for r in rows:
        if a3 is not None:
            r['a'] = a3[tuple(r['mu'])]
    for r in rows:
        print(f"  {str(tuple(r['mu'])):36s} parts={r['parts']}  |mu|={r['size']}  "
              f"a={r.get('a', '?'):>3}  N_S={r['N_S']:,}")
    if a3 is not None:
        tot = sum(r['a'] for r in rows)
        print(f"sum over predecessors of a^(3)(mu,13) = {tot}   (dim of the Pieri channel space B^lambda)")
        print(f"predecessors with a >= 1: {sum(1 for r in rows if r['a'] >= 1)} of {len(rows)}")
    lens = {}
    for r in rows:
        lens[r['parts']] = lens.get(r['parts'], 0) + 1
    print(f"lengths: {lens}")
    out = dict(board_numbering='batch13', session='B13-04', lam=list(LAM), delta=DELTA, n=N, r=R,
               lam_minus=list(lam_minus), lam_minus_weight_space_dim=ns_minus,
               predecessors=rows, a4_lambda13=a4,
               sum_a3=(sum(r['a'] for r in rows) if a3 is not None else None),
               seconds=round(time.time() - t0, 1))
    os.makedirs(os.path.join(ROOT, 'results', 'b13_04'), exist_ok=True)
    with open(os.path.join(ROOT, 'results', 'b13_04', 'pred13.json'), 'w') as f:
        json.dump(out, f, indent=1)
    print(f"done in {time.time()-t0:.0f}s")


if __name__ == '__main__':
    main()

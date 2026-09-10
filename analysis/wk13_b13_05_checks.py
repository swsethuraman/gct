#!/usr/bin/env python3
"""
B13-05 -- three pre-registered checks (PREREG_b13_05 section 2 and addendum A):

  --bruteforce   I3.3: b(mu, delta) by brute force at delta = 2, 3 -- F-orbit sums of the monomials of
                 Sym^{3 delta}(C^9 (x) C^9) with left content mu and magic right content, then the left
                 raising operators on the orbit-sum basis; exact nullity over Q (fmpq_mat) and mod both primes.
                 Compared with the character-route b(mu) from wk13_b13_05_bound.
  --jacobian     A3: rank of d Phi_r at a random integer point, r = 7, 8, 9, both primes (rank_p <= rank_Q):
                 rank = 9r - 4 proves dim D_r^{per_3} = 9r - 4 (Lemma 1 + Prop. 5 of docs/washout_lemma.md).
  --i4           A4: the inheritance cell (11,2,2,2,2,2,0) at r = 7, delta = 7 with wk8_s30_core.measure.

board_numbering: batch13
"""
import sys, os, time, json, random, argparse, itertools
from fractions import Fraction
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from flint import fmpq_mat, nmod_mat, fmpq
from wk8_s30_core import P1, P2, per_form, restrict, measure, exps
from wk13_b13_05_bound import group_F, magic_squares, bound_for_degree, all_partitions

PER3, N9 = per_form(3)


# ------------------------------------------------------------------ I3.3 brute force
def tables(rows, cols):
    """all nonneg integer matrices with given row sums (len 9) and column sums (len 9) -- recursive by row."""
    n = len(cols)
    out = []
    def rec(i, remaining_cols, cur):
        if i == len(rows):
            if all(x == 0 for x in remaining_cols): out.append(tuple(cur))
            return
        r = rows[i]
        if r == 0:
            rec(i + 1, remaining_cols, cur + [(0,) * n]); return
        # compositions of r into n parts bounded by remaining_cols
        def comp(j, left, row):
            if j == n - 1:
                if left <= remaining_cols[j]:
                    rec(i + 1, tuple(remaining_cols[k] - (row + [left])[k] for k in range(n)), cur + [tuple(row + [left])])
                return
            for v in range(min(left, remaining_cols[j]) + 1):
                comp(j + 1, left - v, row + [v])
        comp(0, r, [])
    rec(0, tuple(cols), [])
    return out


def count_tables(rows, cols):
    """DP count of the tables (to apply the cap before enumerating)."""
    from functools import lru_cache
    n = len(cols)
    @lru_cache(maxsize=None)
    def rec(i, rem):
        if i == len(rows): return 1 if all(x == 0 for x in rem) else 0
        r = rows[i]; tot = 0
        def comp(j, left, remlist):
            nonlocal tot
            if j == n - 1:
                if left <= remlist[j]:
                    rl = list(remlist); rl[j] -= left
                    tot += rec(i + 1, tuple(rl))
                return
            for v in range(min(left, remlist[j]) + 1):
                rl = list(remlist); rl[j] -= v
                comp(j + 1, left - v, tuple(rl))
        comp(0, r, rem)
        return tot
    return rec(0, tuple(cols))


def bruteforce_b(mu, delta, cap=200_000, verbose=False):
    """returns (b_Q, b_p1, b_p2, n_monomials, n_orbits) or None if above the cap."""
    mu9 = tuple(mu) + (0,) * (9 - len(mu))
    MS = magic_squares(delta)
    nmon = sum(count_tables(mu9, nu) for nu in MS)
    if nmon > cap: return dict(skipped=True, n_monomials=nmon)
    F = [f for f, _ in group_F()]
    # monomials with left content mu and right content magic
    mons = []
    for nu in MS:
        mons += tables(mu9, nu)
    monset = set(mons)
    assert len(monset) == nmon
    # F-orbits: f acts on the right index: (E f)[a][f(p)] = E[a][p]
    Finv = [tuple(sorted(range(9), key=lambda p: f[p])) for f in F]
    # canonical representative = min over the orbit; but we need orbit sums: represent each orbit by its canonical form
    canon = {}
    for E in mons:
        if E in canon: continue
        images = set()
        for finv in Finv:
            images.add(tuple(tuple(row[finv[p]] for p in range(9)) for row in E))
        rep = min(images)
        for I in images: canon[I] = rep
    orbits = sorted(set(canon.values()))
    oidx = {o: k for k, o in enumerate(orbits)}
    # orbit sums are F-invariant; the left raising operators commute with F, so map orbit sums to orbit sums.
    # E_{a,a+1} on the monomial y^E: sum_p E[a+1][p] * y^{E - e_{(a+1,p)} + e_{(a,p)}}.
    # image of the orbit sum of O = sum_{E in O} E_{a,a+1} y^E: an F-invariant vector; read its coefficient on each
    # target orbit's canonical representative (all members of an orbit carry the same coefficient).
    rows_by_op = []
    target_index = {}
    for a in range(8):
        # target weight mu + e_a - e_{a+1}
        tw = list(mu9); tw[a] += 1; tw[a + 1] -= 1
        if tw[a + 1] < 0: continue
        tw = tuple(tw)
        # build the matrix: for each source orbit, the vector over target monomials, then restrict to canonical reps
        colvecs = []
        tcanon = {}
        for k, O in enumerate(orbits):
            # enumerate the orbit members
            members = set()
            for finv in Finv:
                members.add(tuple(tuple(row[finv[p]] for p in range(9)) for row in O))
            vec = {}
            for E in members:
                for p in range(9):
                    m = E[a + 1][p]
                    if m == 0: continue
                    NE = [list(r) for r in E]
                    NE[a + 1][p] -= 1; NE[a][p] += 1
                    NE = tuple(tuple(r) for r in NE)
                    vec[NE] = vec.get(NE, 0) + m
            # canonical reps of targets
            cv = {}
            for NE, v in vec.items():
                if NE not in tcanon:
                    images = set()
                    for finv in Finv:
                        images.add(tuple(tuple(row[finv[p]] for p in range(9)) for row in NE))
                    rep = min(images)
                    for I in images: tcanon[I] = rep
                rep = tcanon[NE]
                if NE == rep:
                    cv[rep] = v          # coefficient on the representative
            colvecs.append(cv)
        treps = sorted({rep for cv in colvecs for rep in cv})
        tidx = {r: i for i, r in enumerate(treps)}
        M = [[0] * len(orbits) for _ in treps]
        for k, cv in enumerate(colvecs):
            for rep, v in cv.items():
                M[tidx[rep]][k] = v
        rows_by_op += M
    ncols = len(orbits)
    nrows = len(rows_by_op)
    if nrows == 0:
        return dict(b_Q=ncols, b_p=[ncols, ncols], n_monomials=nmon, n_orbits=ncols, nrows=0)
    flat = [x for r in rows_by_op for x in r]
    MQ = fmpq_mat(nrows, ncols, [fmpq(x) for x in flat])
    rQ = MQ.rank()
    rp = [nmod_mat(nrows, ncols, [x % p for x in flat], p).rank() for p in (P1, P2)]
    return dict(b_Q=ncols - rQ, b_p=[ncols - rp[0], ncols - rp[1]], n_monomials=nmon, n_orbits=ncols, nrows=nrows)


def run_bruteforce(cap):
    out = []
    for delta in (2, 3):
        mus = all_partitions(3 * delta, 9)
        res, _ = bound_for_degree(delta, mus, verbose=False)
        for mu in mus:
            t0 = time.time()
            r = bruteforce_b(mu, delta, cap=cap)
            r.update(mu=list(mu), delta=delta, b_formula=res[mu]['b'], b_T_formula=res[mu]['b_T'], secs=round(time.time() - t0, 2))
            if not r.get('skipped'):
                r['agree'] = (r['b_Q'] == r['b_formula'] == r['b_p'][0] == r['b_p'][1])
            out.append(r)
            print(time.strftime('%H:%M:%S'), f"delta={delta} mu={mu}: " + (f"SKIPPED (n_monomials={r['n_monomials']} > cap)" if r.get('skipped')
                  else f"brute b_Q={r['b_Q']} b_p={r['b_p']} formula b={r['b_formula']} (b_T={r['b_T_formula']}) n_mon={r['n_monomials']} orbits={r['n_orbits']} {'AGREE' if r['agree'] else '*** DISAGREE ***'} [{r['secs']}s]"), flush=True)
    return out


# ------------------------------------------------------------------ A3 Jacobian ranks
def jacobian_rank(r, seed=20260909, bound=10 ** 6):
    """rank of d Phi_r at a random integer point A = (A_1..A_r) in M_3^r, Phi_r(A) = per_3(sum s_i A_i) in Sym^3 C^r,
    columns = the 9r entries, rows = the C(r+2,3) coefficients; exact finite differences (Phi is cubic: use polarisation
    via the linearity of the derivative of per_3 in each entry) -- d/dA_i[e] per_3(sum s A) = coefficient extraction."""
    rnd = random.Random(seed + r)
    As = [[rnd.randint(-bound, bound) for _ in range(9)] for _ in range(r)]
    E = exps(3, r)
    base = restrict(PER3, N9, 3, r, As)
    cols = []
    for i in range(r):
        for e in range(9):
            # derivative in direction (i, e): per_3 is multilinear in rows, so the derivative wrt one entry of A_i is
            # the coefficient polynomial: d/dt per_3(sum s A + t s_i E_e) at t = 0.  Use exact finite differences with
            # steps t = 1, -1 on a cubic: f(1) - f(-1) = 2 f'(0) + 2 f'''(0)/6 ... not exact; instead use the identity
            # for a polynomial of degree <= 3 in t: f'(0) = (8 (f(1) - f(-1)) - (f(2) - f(-2))) / 12.
            vals = {}
            for t in (1, -1, 2, -2):
                As2 = [list(a) for a in As]; As2[i][e] += t
                vals[t] = restrict(PER3, N9, 3, r, As2)
            col = []
            for al in E:
                num = 8 * (vals[1].get(al, 0) - vals[-1].get(al, 0)) - (vals[2].get(al, 0) - vals[-2].get(al, 0))
                assert num % 12 == 0
                col.append(num // 12)
            cols.append(col)
    nrows, ncols = len(E), len(cols)
    flat = [cols[j][i] for i in range(nrows) for j in range(ncols)]
    ranks = {p: nmod_mat(nrows, ncols, [x % p for x in flat], p).rank() for p in (P1, P2)}
    return dict(r=r, seed=seed + r, bound=bound, point=As, nrows=nrows, ncols=ncols, rank_p={str(p): v for p, v in ranks.items()},
                bound_9r_minus_4=9 * r - 4, dim_SymC3=nrows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--bruteforce', action='store_true')
    ap.add_argument('--cap', type=int, default=200_000)
    ap.add_argument('--jacobian', action='store_true')
    ap.add_argument('--i4', action='store_true')
    ap.add_argument('--out', default='results/b13_05_checks.json')
    args = ap.parse_args()
    out = dict(board_numbering='batch13', session='B13-05')
    if os.path.exists(args.out):
        out = json.load(open(args.out))
    if args.jacobian:
        out['jacobian'] = []
        for r in (7, 8, 9):
            t0 = time.time()
            rec = jacobian_rank(r); rec['secs'] = round(time.time() - t0, 1)
            out['jacobian'].append(rec)
            print(time.strftime('%H:%M:%S'), f"r={r}: rank dPhi_r = {rec['rank_p']} (both primes), 9r-4 = {9*r-4}, dim Sym^3 C^r = {rec['nrows']} [{rec['secs']}s]", flush=True)
        json.dump(out, open(args.out, 'w'), indent=0)
    if args.i4:
        t0 = time.time()
        lam = (11, 2, 2, 2, 2, 2, 0)
        res = measure(PER3, N9, 3, 7, 7, lam, seed=11, bound=40)
        rec = dict(cell=list(lam), r=7, delta=7, a=res['a'], mult=res['mult'], nbasis=res['nbasis'], seed=11, bound=40, points=res['a'] + 8,
                   primes=[P1, P2], secs=round(time.time() - t0, 1), expected='a = 1, mult = 1 (s41 line 1 at r = 6)')
        out['i4'] = rec
        print(time.strftime('%H:%M:%S'), 'I4 cell', rec, flush=True)
        json.dump(out, open(args.out, 'w'), indent=0)
    if args.bruteforce:
        out['bruteforce'] = run_bruteforce(args.cap)
        json.dump(out, open(args.out, 'w'), indent=0)
    print(time.strftime('%H:%M:%S'), 'wrote', args.out, flush=True)


if __name__ == '__main__':
    main()

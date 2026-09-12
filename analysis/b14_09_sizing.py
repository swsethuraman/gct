#!/usr/bin/env python3
"""
B14-09 -- n_chi for a length-6 cell as an EXACT character sum, without ever
enumerating the weight space.

Why this exists.  `docs/batch14_board.md` slot 9 and `PROVED.md:
nchi_2_21_guard` both say the same thing: `n_chi` is NOT `N_S/|Stab|`, that
quotient is neither an upper nor a lower bound for it, and a cell must never be
sized, routed or rejected on it.  The only measured route in the tree is to
build the cell -- `wk9_s45_build.orbit_setup_arr` enumerates all `N_S`
monomials, canonicalises each under `Stab_W(mu)` and counts the surviving
twisted orbits -- which costs minutes to hours and gigabytes at the sizes this
slot has to size.  So nobody has an `n_chi` for the 58 open degree-10 cells.

The identity that removes the enumeration.  `n_chi` as the engine computes it is
the number of `G`-orbits on the weight-`mu` monomial set `X` whose point
stabiliser lies in `ker chi_mu`, with `G = Stab_W(mu)` the Young subgroup of
`S_r` fixing `mu` and

    chi_mu(sigma) = prod over blocks B of equal parts of  sgn(sigma|_B)^[mu_B odd]

(`wk9_s36_stabred.stab_group`).  `chi_mu` is one-dimensional and
`C[X] = sum over orbits of Ind_{G_m}^G 1`, so

    <chi, Ind_{G_m}^G 1> = <chi|_{G_m}, 1> = 1 if chi|_{G_m} trivial else 0,

and therefore

    n_chi = <chi_mu, C[X]> = (1/|G|) * sum_{g in G} chi_mu(g) * |Fix_X(g)|.          (*)

`|Fix_X(g)|` still looks like it needs `X`.  It does not.  A multiset `m` of size
`delta` drawn from `A = exps(n,r)` is fixed by `g` iff its multiplicity function
is constant on the `<g>`-orbits of `A`, so a `g`-fixed monomial is exactly a
choice of one multiplicity `c_O >= 0` per `<g>`-orbit `O` with

    sum_O c_O * w(O) = mu,      w(O) = sum of the exponent vectors in O.

The degree constraint is implied: every element of `A` has degree `n`, so
`|mu| = n*delta` forces `sum_O c_O |O| = delta`.  That is an unbounded knapsack
over at most `|A|` items in a box of `prod(mu_i + 1)` states -- at most 46 656
here -- and it is exact integer arithmetic throughout.

So (*) gives a MEASURED `n_chi`, not a bound, at a cost of milliseconds per
cell, for cells whose enumeration would cost gigabytes.

Controls.  `--selftest` runs them and they can fail:
  * the `g = 1` term of (*) is `N_S` (checked against every banked `N_S`);
  * (*) reproduces every banked MEASURED `n_chi` in the tree;
  * the group and character built here are compared element-by-element with
    `wk9_s36_stabred.stab_group`, which is the convention of record;
  * the whole answer is compared with the repository's own enumerate-and-
    canonicalise implementation `wk9_s45_build.orbit_setup_arr` on small cells;
  * three deliberately wrong inputs -- chi dropped, group widened to S_r, weight
    perturbed off `n*delta` -- must each make it DISAGREE.

Note on `exps` orderings: this module never resolves a letter by a literal
index.  It works with the exponent vectors themselves and only ever asks
`wk8_s30_core.exps` for the set, so the two opposite orderings in the tree
cannot bite here.  `_check_perm_tables` asserts the action agrees with
`wk9_s36_stabred.perm_tables` anyway.

usage:
    python3 analysis/b14_09_sizing.py --selftest
    python3 analysis/b14_09_sizing.py --cell 10,6,5,4,3,2 --delta 10
    python3 analysis/b14_09_sizing.py --table results/b14_09/sizing.json
"""
import sys, os, json, time, itertools
from functools import lru_cache
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
from wk8_s30_core import exps


# ------------------------------------------------------------------ group
def blocks_of(mu):
    """index blocks of equal parts, in order -- the Young subgroup's factors."""
    out, i = [], 0
    mu = tuple(mu)
    while i < len(mu):
        j = i
        while j + 1 < len(mu) and mu[j + 1] == mu[i]:
            j += 1
        out.append(tuple(range(i, j + 1)))
        i = j + 1
    return out


def perm_sign(p):
    p = list(p); s = 1
    for i in range(len(p)):
        while p[i] != i:
            j = p[i]; p[i], p[j] = p[j], p[i]; s = -s
    return s


def stab_group_here(mu):
    """[(perm tuple on range(r), chi_mu(perm))] -- written here from the
    definition, not imported, so that the comparison in _check_group has two
    sides.  chi is the sign on a block of ODD equal parts and trivial on a block
    of even equal parts."""
    mu = tuple(mu); r = len(mu)
    per_block = []
    for B in blocks_of(mu):
        m = mu[B[0]]
        opts = []
        for img in itertools.permutations(B):
            # the permutation of the block, as a map position -> image
            rel = [img.index(b) for b in B]          # sign of the block permutation
            sg = perm_sign(rel)
            opts.append((tuple(zip(B, img)), sg if m % 2 else 1))
        per_block.append(opts)
    out = []
    for combo in itertools.product(*per_block):
        p = list(range(r)); ch = 1
        for pairs, c in combo:
            for b, im in pairs:
                p[b] = im
            ch *= c
        out.append((tuple(p), ch))
    return out


def _check_group(mu):
    """CONTROL: the group and character written here must agree, element for
    element, with wk9_s36_stabred.stab_group -- the convention of record."""
    from wk9_s36_stabred import stab_group
    mine = {p: c for p, c in stab_group_here(mu)}
    theirs = {p: c for p, c in stab_group(mu)}
    if mine != theirs:
        bad = [(p, mine.get(p), theirs.get(p)) for p in set(mine) | set(theirs)
               if mine.get(p) != theirs.get(p)]
        raise AssertionError(f"group/character disagree at mu={mu}: {bad[:5]}")
    return len(mine)


def _check_perm_tables(n, r, mu):
    """CONTROL: the action on exponent vectors used here is the action the
    engine uses (wk9_s36_stabred.perm_tables)."""
    from wk9_s36_stabred import perm_tables, stab_group
    A = exps(n, r); idx = {a: k for k, a in enumerate(A)}
    for (p, ch), (tab, ch2) in zip(stab_group(mu), perm_tables(n, r, stab_group(mu))):
        assert ch == ch2
        for k, al in enumerate(A):
            nx = [0] * r
            for i in range(r):
                nx[p[i]] = al[i]
            assert tab[k] == idx[tuple(nx)], "perm action disagrees with perm_tables"
    return True


def _act(p, al):
    """(p . al)[p[i]] = al[i] -- the engine's convention."""
    nx = [0] * len(al)
    for i, v in enumerate(al):
        nx[p[i]] = v
    return tuple(nx)


def cycle_orbits(p, A):
    """<p>-orbits of the exponent vectors A, as a list of (size, weight vector)."""
    idx = {a: k for k, a in enumerate(A)}
    seen = [False] * len(A)
    out = []
    for k, a in enumerate(A):
        if seen[k]:
            continue
        w = [0] * len(a); size = 0; cur = a
        while not seen[idx[cur]]:
            seen[idx[cur]] = True
            size += 1
            for i, v in enumerate(cur):
                w[i] += v
            cur = _act(p, cur)
        out.append((size, tuple(w)))
    return out


# ---------------------------------------------------------------- the DP
def fixed_count(orbits, mu):
    """#{ c >= 0 : sum_O c_O w(O) = mu }, exact, by unbounded knapsack over a
    box of prod(mu_i+1) residual-weight states.  Items with a weight vector not
    componentwise <= mu can never be used and are skipped."""
    mu = tuple(int(x) for x in mu)
    shape = tuple(m + 1 for m in mu)
    dp = np.zeros(shape, dtype=np.int64)
    dp[(0,) * len(mu)] = 1
    for _size, w in orbits:
        if any(wi > mi for wi, mi in zip(w, mu)):
            continue
        ax = next(i for i, wi in enumerate(w) if wi > 0)          # a nonzero axis to march along
        src_sl = [slice(None)] * len(mu)
        dst_sl = [slice(None)] * len(mu)
        for i, wi in enumerate(w):
            if i == ax:
                continue
            dst_sl[i] = slice(wi, None)
            src_sl[i] = slice(0, shape[i] - wi) if wi else slice(None)
        for t in range(w[ax], shape[ax]):
            dst_sl[ax] = t; src_sl[ax] = t - w[ax]
            dp[tuple(dst_sl)] += dp[tuple(src_sl)]
    return int(dp[tuple(mu)])


def n_chi_exact(mu, delta, n=3, chi_on=True, group=None, want_parts=False):
    """(*) -- the exact n_chi, plus N_S as the identity term.

    chi_on=False and a widened `group` are the deliberately wrong inputs of
    controls C3a / C3b; they are not options anyone should use for a real cell."""
    mu = tuple(int(x) for x in mu); r = len(mu)
    if sum(mu) != n * delta:
        raise ValueError(f"weight {mu} sums to {sum(mu)}, not n*delta = {n*delta}")
    A = exps(n, r)
    G = stab_group_here(mu) if group is None else group
    memo = {}
    tot = 0; NS = None; parts = []
    for p, ch in G:
        if not chi_on:
            ch = 1
        key = p
        if key not in memo:
            memo[key] = fixed_count(cycle_orbits(p, A), mu)
        f = memo[key]
        if p == tuple(range(r)):
            NS = f
        tot += ch * f
        if want_parts:
            parts.append((p, ch, f))
    assert tot % len(G) == 0, ("character sum not divisible by |G|", mu, tot, len(G))
    res = dict(mu=list(mu), delta=delta, n=n, r=r, N_S=NS, stab=len(G),
               n_chi=tot // len(G))
    if want_parts:
        res['parts'] = parts
    return res


# ------------------------------------------------------------- the corpus
BOX_CAP = 6_000_000          # prod(mu_i+1); above this the DP box is not built

def box_size(mu):
    b = 1
    for m in mu:
        b *= (int(m) + 1)
        if b > 10 ** 15:
            return b
    return b


def harvest(root=None, verbose=False):
    """Every banked (n, r, mu, delta, N_S, |Stab|, n_chi) record in the tree.

    These are MEASURED values produced by the enumerate-and-canonicalise route
    over five months of sessions and several engines.  They are the corpus
    controls C1 and C2 run against, and they exist before this instrument did,
    so they can falsify it on arrival."""
    root = root or ROOT
    out = {}
    def take(d, src):
        if not isinstance(d, dict):
            return
        mu = d.get('mu') or d.get('lam') or d.get('lambda') or d.get('weight')
        nc = d.get('n_chi'); de = d.get('delta'); ns = d.get('N_S')
        if mu is None or nc is None or de is None or ns is None:
            return
        if not isinstance(mu, (list, tuple)) or not all(isinstance(x, int) for x in mu):
            return
        nn = d.get('n'); rr = d.get('r')
        if nn is None or rr is None:
            return
        mu = tuple(int(x) for x in mu) + (0,) * (int(rr) - len(mu))
        if len(mu) != int(rr) or sum(mu) != int(nn) * int(de):
            return
        if list(mu) != sorted(mu, reverse=True):
            return
        key = (int(nn), int(rr), mu, int(de))
        rec = dict(N_S=int(ns), n_chi=int(nc), stab=(int(d['stab']) if 'stab' in d else None), src=src)
        if key in out:
            p = out[key]
            if (p['N_S'], p['n_chi']) != (rec['N_S'], rec['n_chi']):
                out[key] = dict(rec, conflict=(p['N_S'], p['n_chi'], p['src']))
            return
        out[key] = rec
    def walk(obj, src):
        if isinstance(obj, dict):
            take(obj, src)
            for v in obj.values():
                walk(v, src)
        elif isinstance(obj, list):
            for v in obj:
                walk(v, src)
    for dirpath, _dn, files in os.walk(os.path.join(root, 'results')):
        for fn in files:
            if not (fn.endswith('.json') or fn.endswith('.jsonl')):
                continue
            p = os.path.join(dirpath, fn)
            try:
                if os.path.getsize(p) > 60_000_000:
                    continue
                txt = open(p, encoding='utf-8', errors='replace').read()
            except Exception:
                continue
            if '"n_chi"' not in txt:
                continue
            rel = os.path.relpath(p, root)
            if fn.endswith('.jsonl'):
                for line in txt.splitlines():
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        walk(json.loads(line), rel)
                    except Exception:
                        pass
            else:
                try:
                    walk(json.loads(txt), rel)
                except Exception:
                    pass
    if verbose:
        log(f"harvest: {len(out)} distinct banked (n,r,mu,delta) records with a measured n_chi")
    return out


def log(*a):
    print(*a, file=sys.stderr); sys.stderr.flush()

#!/usr/bin/env python3
"""s77 -- the bridge:  S5 Pieri state  ->  s69 bracket filling.

THE MAP.  A bracket filling of lambda' = (h,h,2^{n2},1^{n1}) gives each of the
delta letters n=4 cells, one per column -- a horizontal 4-strip.  A COLUMN-STRICT
filling (an SSYT of shape lambda with content (4^delta): values 0..delta-1 each
used four times, strictly increasing down columns, weakly increasing along rows)
is exactly a PIERI PATH  lambda = nu^{(delta)} > nu^{(delta-1)} > ... , each step
removing a removable horizontal 4-strip, the cell value = the level at which its
strip was added.  So an SSYT IS a Pieri chain, and F_SSYT = <tableau tensor,
f^{tensor delta}> is the image, under the s69 pairing, of the abstract Pieri
state.  Because letters are unlabelled F_T is S_delta-symmetric, so it realizes
the S_delta-invariant (= tau-invariant) projection the S5 recursion computes as
ker(tau - I).  (docs/s77_report.md and PREREG_s77.md.)

This module: the SSYT <-> Filling conversion, a check that a Filling is column
strict, and two DETERMINISTIC canonical SSYT generators (no RNG):
  order A -- lexicographic on the reading word (row 0, row 1, rows 2..h-1);
  order B -- overlap-major: fill the two tall columns first and try, at each
             column-1 cell, the values already used in column 0 first, so
             high tall-column overlap k = |C1 cap C2| comes first.
Evaluation is always the s69 circuit; this module never expands into carrier
coordinates.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from wk11_s69_circuit import Filling                                      # noqa: E402


# ------------------------------------------------------------------ shape / cells
def shape_cells(h, n2, n1):
    """cells of lambda = (2+n2+n1, 2+n2, 2^{h-2}) as a list of rows, each a list of
    column indices.  row 0 has 2+n2+n1 cells, row 1 has 2+n2, rows 2..h-1 have 2."""
    rows = []
    rows.append(list(range(2 + n2 + n1)))          # row 0
    rows.append(list(range(2 + n2)))               # row 1
    for _ in range(h - 2):
        rows.append([0, 1])                        # rows 2..h-1
    return rows


def tableau_to_filling(T, h, n, delta, n2, n1):
    """T[r] = list of values along row r (0-indexed letters).  Build the Filling."""
    C1 = [T[r][0] for r in range(h)]
    C2 = [T[r][1] for r in range(h)]
    two = [(T[0][2 + e], T[1][2 + e]) for e in range(n2)]
    one = [T[0][2 + n2 + c] for c in range(n1)]
    return Filling(h, n, delta, C1, C2, two, one)


def filling_is_ssyt(F):
    """True iff F is column-strict (strict down every column) AND row-weak (weakly
    increasing along every row) in the tall/two/one layout -- i.e. an SSYT."""
    h = F.h
    # tall columns strictly increasing
    if any(F.C1[r] >= F.C1[r + 1] for r in range(h - 1)):
        return False
    if any(F.C2[r] >= F.C2[r + 1] for r in range(h - 1)):
        return False
    # two-columns strict down
    if any(a >= b for a, b in F.two):
        return False
    # row 0 weakly increasing: C1[0] C2[0] two[.][0] one[.]
    row0 = [F.C1[0], F.C2[0]] + [a for a, _ in F.two] + list(F.one)
    if any(row0[i] > row0[i + 1] for i in range(len(row0) - 1)):
        return False
    # row 1: C1[1] C2[1] two[.][1]
    row1 = [F.C1[1], F.C2[1]] + [b for _, b in F.two]
    if any(row1[i] > row1[i + 1] for i in range(len(row1) - 1)):
        return False
    # rows 2..h-1: C1[r] <= C2[r]
    if any(F.C1[r] > F.C2[r] for r in range(2, h)):
        return False
    return True


# ------------------------------------------------------------------ SSYT backtracking
def _val_order_A(r, c, lo, val, cnt, delta, n):
    """lexicographic: try candidate values in increasing order."""
    return range(lo, delta)


def _val_order_B(r, c, lo, val, cnt, delta, n):
    """overlap-major: at a column-1 cell (c==1), try values already used in
    column 0 first (increasing), then the rest.  Elsewhere increasing."""
    if c == 1:
        col0 = {val[(rr, 0)] for rr in range(0, 5 * n) if (rr, 0) in val}
        pref = sorted(v for v in col0 if v >= lo)
        rest = [v for v in range(lo, delta) if v not in col0]
        return pref + rest
    return range(lo, delta)


def _val_order_R(r, c, lo, val, cnt, delta, n):
    """birth-informed (large-values-first): try the LARGEST feasible value first.  This drives
    the newest (high-index) letters into the tall and two-columns, so they are not pure-u --
    which is exactly the birth condition (a filling not of the form u.F').  Front-loads births
    up the ladder, where the small-values-first order buries them under the u-tower."""
    return range(delta - 1, lo - 1, -1)


def ssyt_fillings(h, n, delta, n2, n1, order="A", limit=None, kset=None):
    """DETERMINISTIC stream of SSYT-fillings of lambda'=(h,h,2^{n2},1^{n1}) in the
    chosen canonical order.  Yields Filling objects.  If `kset` is given, only SSYT whose
    tall-column overlap |C1 cap C2| is in kset are produced (pruned when column 1 completes,
    before the deep two-/one-column enumeration)."""
    rows = shape_cells(h, n2, n1)
    vo = {"A": _val_order_A, "B": _val_order_B, "R": _val_order_R}[order]
    count = 0
    for D in _run(rows, n, delta, vo, kset):
        T = [[D[(r, c)] for c in rows[r]] for r in range(h)]
        F = tableau_to_filling(T, h, n, delta, n2, n1)
        yield F
        count += 1
        if limit is not None and count >= limit:
            return


def _run(rows, n, delta, value_order, kset=None):
    """clean generator of SSYT dicts (r,c)->value.  Prunes on tall-column overlap when kset
    is given: the check fires the moment column 1 is complete (cell index 2h-1)."""
    h = len(rows)
    n2 = len(rows[1]) - 2
    n1 = len(rows[0]) - 2 - n2
    order = []
    order += [(r, 0) for r in range(h)]
    order += [(r, 1) for r in range(h)]
    for e in range(n2):
        order += [(0, 2 + e), (1, 2 + e)]
    for c in range(n1):
        order += [(0, 2 + n2 + c)]
    val = {}; cnt = [0] * delta
    col1_done = 2 * h - 1                                # after this index, column 1 is full
    boundary = 2 * h + 2 * n2                            # cells 0..boundary-1 = tall + two-columns;
    #                                                     the n1 one-columns are then FORCED.

    def complete_ones():
        """the one-columns are the sorted multiset of remaining legs (row-0 tail, weakly
        increasing).  Deterministic -- no branching.  Returns the completed dict or None if
        row-weak with the last two-column top fails."""
        remaining = []
        for l in range(delta):
            remaining += [l] * (n - cnt[l])
        if len(remaining) != n1:
            return None
        remaining.sort()
        # last row-0 value placed (last two-column top, or C2[0] if no two-columns)
        last = val[(0, 1 + n2)] if n2 >= 1 else val[(0, 1)]
        if n1 and remaining[0] < last:
            return None
        D = dict(val)
        for c, v in enumerate(remaining):
            D[(0, 2 + n2 + c)] = v
        return D

    def rec(t):
        if t == boundary:
            D = complete_ones()
            if D is not None:
                yield D
            return
        r, c = order[t]
        av = val.get((r - 1, c)) if r >= 1 else None
        lv = val.get((r, c - 1)) if c >= 1 else None
        lo = max((av + 1) if av is not None else 0, lv if lv is not None else 0)
        for v in value_order(r, c, lo, val, cnt, delta, n):
            if v < lo or v >= delta or cnt[v] >= n:
                continue
            val[(r, c)] = v; cnt[v] += 1
            if kset is not None and t == col1_done:
                C1 = {val[(rr, 0)] for rr in range(h)}
                C2 = {val[(rr, 1)] for rr in range(h)}
                if len(C1 & C2) not in kset:
                    del val[(r, c)]; cnt[v] -= 1
                    continue
            yield from rec(t + 1)
            del val[(r, c)]; cnt[v] -= 1

    yield from rec(0)


def interleaved_ssyt(h, n, delta, n2, n1, order="A", limit=None):
    """DETERMINISTIC SSYT stream that ROUND-ROBINS across tall-column overlap classes
    k = h, h-1, ..., max(0,h-n) (the nonzero range needs k >= h-n).  This gives a basis
    builder diversity across overlaps -- the maximal-overlap k=h class alone spans only a
    low-dimensional subspace (measured: rank 1 at the n=4 delta=12 seed), so a spanning
    deterministic stream must mix k.  Still fully deterministic (no RNG)."""
    ks = list(range(h, max(-1, h - n - 1), -1))
    gens = [ssyt_fillings(h, n, delta, n2, n1, order=order, kset={k}) for k in ks]
    alive = [True] * len(gens)
    count = 0
    while any(alive):
        for i, g in enumerate(gens):
            if not alive[i]:
                continue
            try:
                F = next(g)
            except StopIteration:
                alive[i] = False
                continue
            yield F
            count += 1
            if limit is not None and count >= limit:
                return


# ------------------------------------------------------------------ overlap-major column-strict
# The row-weak SSYT (= Pieri chains) span M_lambda but their nonzero members are rare and deep
# in canonical order (measured: first nonzero n=3 SSYT at #1076).  The natural nonzero fillings
# are column-strict but NOT row-weak.  Every bracket filling equals +- its column-sorted form,
# and F_T is symmetric in the two-columns and in the one-columns, so a CANONICAL representative
# of every filling is: tall columns sorted, two-columns sorted (each pair a<b, pairs ordered),
# one-columns sorted.  Enumerating these canonical representatives, TALL-COLUMN-OVERLAP-MAJOR
# (k = |C1 cap C2| from h downwards -- the brief's explicit overlap treatment), is deterministic
# (no RNG), spans (all fillings span), and front-loads the nonzero region (k >= h-n).
import collections                                                        # noqa: E402
import itertools                                                          # noqa: E402


def _canonical_distribute(delta, n, n2, n1, rem):
    """place the remaining legs rem[l] into n2 two-columns (distinct pair a<b) and n1 one-columns,
    by a fixed canonical greedy: each two-column takes the two SMALLEST-index letters still having
    legs (this front-loads small letters into two-columns, leaving the rest as one-columns).
    Deterministic; returns (two, one) or None if infeasible."""
    cnt = [rem[l] for l in range(delta)]
    two = []
    for _ in range(n2):
        avail = [l for l in range(delta) if cnt[l] > 0]
        if len(avail) < 2:
            return None
        a, b = avail[0], avail[1]            # two smallest distinct letters with legs
        two.append((a, b))
        cnt[a] -= 1; cnt[b] -= 1
    one = []
    for l in range(delta):
        one += [l] * cnt[l]
    if len(one) != n1:
        return None
    return two, one


def columnstrict_fillings(h, n, delta, n2, n1, kmin=None, limit=None):
    """DETERMINISTIC overlap-major stream of canonical column-strict fillings of
    lambda' = (h,h,2^{n2},1^{n1}).  k = |C1 cap C2| runs from h down to kmin (default h-n),
    and within each k the shared set S, then C1-only U1, then C2-only U2 run in lex order.
    One canonical leg-distribution per (S,U1,U2).  Yields Filling objects."""
    if kmin is None:
        kmin = max(0, h - n)
    letters = list(range(delta))
    count = 0
    for k in range(h, kmin - 1, -1):
        m = h - k                                       # size of each tall-only set
        for S in itertools.combinations(letters, k):
            Sset = set(S)
            rest = [l for l in letters if l not in Sset]
            for U1 in itertools.combinations(rest, m):
                U1set = set(U1)
                rest2 = [l for l in rest if l not in U1set]
                for U2 in itertools.combinations(rest2, m):
                    C1 = sorted(S + U1); C2 = sorted(S + U2)
                    rem = [n] * delta
                    for l in C1: rem[l] -= 1
                    for l in C2: rem[l] -= 1
                    if min(rem) < 0:
                        continue
                    dist = _canonical_distribute(delta, n, n2, n1, rem)
                    if dist is None:
                        continue
                    two, one = dist
                    try:
                        F = Filling(h, n, delta, C1, C2, two, one)
                    except AssertionError:
                        continue
                    yield F
                    count += 1
                    if limit is not None and count >= limit:
                        return


if __name__ == "__main__":
    # smoke test: the n=4 delta=12 seed shape, count a few SSYT of each order
    h, n, delta, n2, n1 = 9, 4, 12, 15, 0
    for order in ("A", "B"):
        fs = []
        for F in ssyt_fillings(h, n, delta, n2, n1, order=order, limit=5):
            assert filling_is_ssyt(F), "generator produced a non-SSYT"
            fs.append(F)
        print(f"order {order}: first {len(fs)} SSYT-fillings; "
              f"k=|C1 cap C2| = {[len(set(F.C1)&set(F.C2)) for F in fs]}")

#!/usr/bin/env python3
"""
Independent verifier for the session-51 r=5 syzygy certificate.

Standalone: shares NO code with the worker toolkit (analysis/wk9_s44_poly.py).
Polynomial arithmetic, the determinant, and the partials are re-implemented here
from scratch; python-flint is used only for the mod-p ranks (house rule: no
hand-rolled elimination).  Implements the s49-brief verifier spec:

  Layer 1 (syntactic): parse the declared JSON; error on anything unparseable;
    recompute the annihilation exactly over Z and, independently, by
    Schwartz-Zippel evaluation at random integer points; recompute the
    non-Koszul rank certificate over two distinct primes.
  Layer 2 (semantic): check the recorded pencil really is det_4 of the recorded
    matrices; that each g_i is homogeneous of degree 4 in 5 variables; that F is
    homogeneous of degree 4; that the relation degree |lambda| = 4*? is
    consistent (deg g_i + deg d_iF = 4 + 3 = 7); and that the syzygy is genuinely
    OUTSIDE the Koszul span (the object claimed), independently rebuilt.

Usage:  python3 tools/verify_s51.py results/s51_r5_syzygy.json
Exit 0 on all-pass, 1 on any failure.
"""
import sys, json, random
from itertools import permutations

# ---- independent polynomial arithmetic (dict: exponent-tuple -> int coeff) ----
def padd(a, b, s=1):
    o = dict(a)
    for e, c in b.items():
        o[e] = o.get(e, 0) + s * c
    return {e: c for e, c in o.items() if c}

def pmul(a, b):
    o = {}
    for ea, ca in a.items():
        for eb, cb in b.items():
            e = tuple(x + y for x, y in zip(ea, eb))
            o[e] = o.get(e, 0) + ca * cb
    return {e: c for e, c in o.items() if c}

def pderiv(f, k):
    o = {}
    for e, c in f.items():
        if e[k]:
            ee = list(e); ee[k] -= 1
            t = tuple(ee); o[t] = o.get(t, 0) + c * e[k]
    return {e: c for e, c in o.items() if c}

def peval(f, pt):
    from functools import reduce
    s = 0
    for e, c in f.items():
        t = c
        for xi, ai in zip(e, pt): t *= ai ** xi
        s += t
    return s

def sign(perm):
    perm = list(perm); s = 1
    for i in range(len(perm)):
        while perm[i] != i:
            j = perm[i]; perm[i], perm[j] = perm[j], perm[i]; s = -s
    return s

def det_of_pencil(A, r):
    """F = det( sum_k s_k A_k ), A_k a 4x4 integer matrix.  Independent Leibniz."""
    n = 4
    # entry (i,j) is the linear form sum_k A[k][i][j] * s_k
    def ent(i, j):
        return {tuple(1 if t == k else 0 for t in range(r)): A[k][i][j]
                for k in range(r) if A[k][i][j]}
    F = {}
    for p in permutations(range(n)):
        term = {tuple([0] * r): sign(p)}
        ok = True
        for i in range(n):
            term = pmul(term, ent(i, p[i]))
            if not term: ok = False; break
        if ok: F = padd(F, term)
    return F

def homog_degree(f):
    degs = {sum(e) for e in f}
    return degs.pop() if len(degs) == 1 else None

# ---- mod-p rank via python-flint (only external dependency) ----
def rank_rows_modp(rows, ncols, p):
    from flint import nmod_mat
    data = [0] * (len(rows) * ncols)
    for i, row in enumerate(rows):
        for c, v in row.items():
            data[i * ncols + c] = v % p
    return nmod_mat(len(rows), ncols, data, p).rank()

def monos(d, r):
    out = []
    def rec(pos, rem, cur):
        if pos == r - 1:
            out.append(tuple(cur + [rem])); return
        for k in range(rem + 1):
            rec(pos + 1, rem - k, cur + [k])
    rec(0, d, [])
    return out

def main():
    if len(sys.argv) != 2:
        print("usage: verify_s51.py <cert.json>"); return 1
    cert = json.load(open(sys.argv[1]))
    fails = []
    # ---- parse (layer 1 syntactic) ----
    try:
        n = cert["n"]; r = cert["r"]; d = cert["d"]; A = cert["A"]
        syz = cert["syzygy"]
        assert n == 4 and r == 5 and d == 7, "cert is not the (n,r,d)=(4,5,7) case"
        assert len(A) == r and all(len(m) == 4 and all(len(row) == 4 for row in m) for m in A)
        g = []
        for i in range(r):
            gi = {}
            for k, v in syz[f"g{i}"].items():
                e = tuple(int(x) for x in k.split(","))
                assert len(e) == r
                gi[e] = int(v)
            g.append(gi)
    except Exception as ex:
        print(f"PARSE ERROR: {ex}"); return 1
    print(f"parsed cert: n={n} r={r} d={d}; pencil of {r} 4x4 matrices; syzygy g0..g{r-1}")

    # ---- layer 2: the recorded pencil really is det_4 of the recorded matrices ----
    F = det_of_pencil(A, r)
    degF = homog_degree(F)
    print(f"[L2] F = det_4(pencil) recomputed independently: {len(F)} monomials, homogeneous degree {degF}")
    if degF != 4: fails.append("F is not homogeneous of degree 4")

    # ---- layer 2: each g_i homogeneous degree 4 in r vars ----
    for i in range(r):
        di = homog_degree(g[i])
        if di is not None and di != 4:
            fails.append(f"g_{i} not homogeneous degree 4 (got {di})")
    print(f"[L2] each g_i homogeneous degree 4: {'OK' if not any('g_' in f for f in fails) else 'FAIL'}"
          f"   sizes {[len(gi) for gi in g]}")

    # ---- layer 1: exact Z annihilation  sum g_i d_iF == 0 ----
    grads = [pderiv(F, i) for i in range(r)]
    acc = {}
    for i in range(r):
        acc = padd(acc, pmul(g[i], grads[i]))
    acc = {e: c for e, c in acc.items() if c}
    z_ok = (len(acc) == 0)
    print(f"[L1] exact Z: sum g_i d_iF == 0 : {'PASS' if z_ok else 'FAIL ('+str(len(acc))+' residual terms)'}")
    if not z_ok: fails.append("exact Z annihilation failed")

    # ---- layer 1: independent Schwartz-Zippel Z evaluation at random points ----
    rnd = random.Random(51051); sz_ok = True
    for _ in range(6):
        pt = [rnd.randint(-7, 7) for _ in range(r)]
        val = sum(peval(g[i], pt) * peval(grads[i], pt) for i in range(r))
        if val != 0: sz_ok = False; break
    print(f"[L1] Schwartz-Zippel Z eval at 6 random integer points : {'PASS' if sz_ok else 'FAIL'}")
    if not sz_ok: fails.append("Schwartz-Zippel evaluation nonzero")

    # ---- layer 2: the syzygy is genuinely NON-Koszul, over two primes ----
    # Rebuild the Koszul syzygy space independently and check the syzygy is outside it.
    md = monos(d - 3, r)                     # degree-4 multiplier monomials
    colkey = [(i, m) for i in range(r) for m in md]
    colpos = {k: j for j, k in enumerate(colkey)}
    ncol = len(colkey)
    def tuple_to_row(gs):
        row = {}
        for i in range(r):
            for e, c in gs[i].items():
                row[colpos[(i, e)]] = row.get(colpos[(i, e)], 0) + c
        return row
    m1 = monos(1, r)
    kos = []
    for a in range(r):
        for b in range(a + 1, r):
            for l in m1:
                lf = {l: 1}
                ga = pmul(lf, grads[b]); gb = pmul(lf, grads[a])
                gs = [dict() for _ in range(r)]; gs[a] = ga
                gs[b] = {e: -c for e, c in gb.items()}
                kos.append(tuple_to_row(gs))
    syz_row = tuple_to_row({i: g[i] for i in range(r)})
    nonkoszul_both = True
    for p in (2147483647, 2147483629):
        rk_k = rank_rows_modp(kos, ncol, p)
        rk_k_plus = rank_rows_modp(kos + [syz_row], ncol, p)
        outside = (rk_k_plus == rk_k + 1)
        # also confirm it is a genuine syzygy mod p (image zero): checked exactly above; here rank bookkeeping
        print(f"[L2] prime {p}: dim Koszul={rk_k}, +syzygy={rk_k_plus} -> non-Koszul: {'YES' if outside else 'NO'}")
        nonkoszul_both &= outside
    if not nonkoszul_both: fails.append("syzygy lies in the Koszul span (not the claimed non-Koszul object)")

    print("\n=== VERDICT ===")
    if fails:
        for f in fails: print("  FAIL:", f)
        return 1
    print("  ALL CHECKS PASS: the recorded pencil is det_4; (g_i) is a genuine")
    print("  degree-7 syzygy of its partials, exact over Z; and it is non-Koszul at two primes.")
    return 0

if __name__ == "__main__":
    sys.exit(main())

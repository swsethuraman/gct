"""B19-01: the silent band.

Computes, exactly, for cells (d, lambda):
  a  = [S_lambda : Sym^d(Sym^4 C^n)], n = ell(lambda)   (ambient multiplicity; stable for n >= ell)
  g  = [S^lambda : S^R (x) S^R],  R = (d^4)             (ordinary rectangular Kronecker)
  s  = [S^lambda : Sym^2(S^R)]                          (symmetric rectangular Kronecker, B18-02 (3.1))
and reports the cells of the silent band  lambda_1 + lambda_2 + lambda_3 <= 2d  (Theorem 4.1),
where b = 0 is proved, so the arc ceiling is s - b = s.

Controls (must all pass, else the run is void):
  C1  d = 2: s = 1 for (8), (6,2), (4,4), (4,2,2), (2,2,2,2) and s = 0 for the other 13 partitions of 8
      with at most five rows; a = 1 for (8), (6,2), (4,4) and a = 0 for (4,2,2), (2,2,2,2)   [B18-02 section 6]
  C2  d = 3: (6,3,1,1,1) has g = 3, s = 1;  (5,3,2,1,1) has g = 4, s = 2                     [B18-02 / review]
  C3  sum_lambda g(R,R,lambda) * f^lambda = (f^R)^2, and g(R,R,(4d)) = 1                     [review section 1]
  C4  f^(3,3,3,3) = 462                                                                      [review section 1]
  C5  d = 1: s_(4) = 1 and s_lambda = 0 for every other lambda |- 4                          [B18-02 section 3]

Run bounded: timeout 60 python analysis/b19_01_band.py
"""
import itertools, json, os, sys, time
from fractions import Fraction
from math import comb, factorial, prod

t0 = time.time()
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "results", "b19_01")
os.makedirs(OUT, exist_ok=True)
MAXROWS = 8          # cap on ell(lambda) for the plethysm part (n! alternation)


def partitions(n, maxp=None):
    if maxp is None:
        maxp = n
    if n == 0:
        yield ()
        return
    for f in range(min(n, maxp), 0, -1):
        for rest in partitions(n - f, f):
            yield (f,) + rest


def z_of(eta):
    m = {}
    for p in eta:
        m[p] = m.get(p, 0) + 1
    return prod(k ** v * factorial(v) for k, v in m.items())


def square_type(eta):
    out = []
    for L in eta:
        if L % 2:
            out.append(L)
        else:
            out += [L // 2, L // 2]
    return tuple(sorted(out, reverse=True))


CHI = {}


def chi(lam, eta):
    """Murnaghan-Nakayama: character of S^lam at cycle type eta"""
    key = (lam, eta)
    if key in CHI:
        return CHI[key]
    if not eta:
        r = 1 if not lam else 0
        CHI[key] = r
        return r
    k, rest = eta[0], eta[1:]
    total = 0
    lam = list(lam)
    rows = len(lam)
    # border-strip removal via beta numbers: remove k from one beta number, if the result is new
    beta = [lam[i] + (rows - 1 - i) for i in range(rows)] if rows else []
    for idx in range(rows):
        b = beta[idx] - k
        if b < 0 or b in beta:
            continue
        nb = sorted([x for t, x in enumerate(beta) if t != idx] + [b], reverse=True)
        ht = sum(1 for x in beta if b < x < beta[idx])       # number of rows crossed
        nl = [nb[i] - (len(nb) - 1 - i) for i in range(len(nb))]
        nl = tuple(x for x in nl if x > 0)
        total += (-1) ** ht * chi(nl, rest)
    CHI[key] = total
    return total


def f_dim(lam):
    """number of standard Young tableaux, hook length formula"""
    n = sum(lam)
    conj = [sum(1 for p in lam if p > j) for j in range(lam[0])] if lam else []
    h = 1
    for i, row in enumerate(lam):
        for j in range(row):
            h *= row - j + conj[j] - i - 1
    return factorial(n) // h


def kronecker(d, lams):
    """returns {lam: (g, s)} for the rectangle R = (d^4), lams a list of partitions of 4d"""
    N, R = 4 * d, tuple([d] * 4)
    etas = list(partitions(N))
    data = []
    for eta in etas:
        cR = chi(R, eta)
        data.append((eta, Fraction(1, z_of(eta)), cR, chi(R, square_type(eta))))
    out = {}
    for lam in lams:
        g = s2 = Fraction(0)
        for eta, iz, cR, cR2 in data:
            cl = chi(lam, eta)
            if cl:
                g += iz * cl * cR * cR
                s2 += iz * cl * (cR * cR + cR2)
        s2 = s2 / 2
        assert g.denominator == 1 and s2.denominator == 1, (lam, g, s2)
        out[lam] = (int(g), int(s2))
    return out


def plethysm_mults(d, n):
    """weight multiplicities of Sym^d(Sym^4 C^n) -> dict weight -> multiplicity"""
    mons = [c for c in itertools.product(range(5), repeat=n) if sum(c) == 4]
    layers = [dict() for _ in range(d + 1)]
    layers[0][(0,) * n] = 1
    for al in mons:
        for j in range(1, d + 1):
            src, dst = layers[j - 1], layers[j]
            for w, c in src.items():
                nw = tuple(x + y for x, y in zip(w, al))
                dst[nw] = dst.get(nw, 0) + c
    assert sum(layers[d].values()) == comb(len(mons) + d - 1, d)
    return layers[d]


PERMS = {}


def a_mult(lam, K, n):
    """multiplicity of S_lam(C^n) by the Weyl alternation on weight multiplicities K"""
    if n not in PERMS:
        ps = list(itertools.permutations(range(n)))
        sg = []
        for p in ps:
            s, seen = 1, set()
            for i in range(n):
                if i in seen:
                    continue
                j, L = i, 0
                while j not in seen:
                    seen.add(j); j = p[j]; L += 1
                s *= (-1) ** (L - 1)
            sg.append(s)
        PERMS[n] = (ps, sg)
    ps, sg = PERMS[n]
    rho = [n - 1 - i for i in range(n)]
    lam = list(lam) + [0] * (n - len(lam))
    tot = 0
    for p, s in zip(ps, sg):
        mu = tuple(lam[i] + rho[i] - rho[p[i]] for i in range(n))
        if min(mu) >= 0:
            v = K.get(mu)
            if v:
                tot += s * v
    return tot


report = {"schema": "b19_01-silent-band/1", "controls": {}, "band": {}}

# ---- C4, C3 ----
assert f_dim((3, 3, 3, 3)) == 462
report["controls"]["C4_f_3333_is_462"] = True

# ---- C5: d = 1 ----
k1 = kronecker(1, list(partitions(4)))
report["controls"]["C5_d1"] = {str(l): k1[l] for l in k1}
assert k1[(4,)][1] == 1 and all(v[1] == 0 for l, v in k1.items() if l != (4,))

# ---- C1/C2/C3 and the band ----
for d in (1, 2, 3, 4):
    N = 4 * d
    lams = [l for l in partitions(N)]
    kr = kronecker(d, lams)
    gsum = sum(kr[l][0] * f_dim(l) for l in lams)
    ok_c3 = (gsum == f_dim(tuple([d] * 4)) ** 2) and kr[(N,)][0] == 1
    report["controls"][f"C3_d{d}_sum_g_f_equals_fR2"] = {"ok": bool(ok_c3), "sum": gsum, "fR2": f_dim(tuple([d] * 4)) ** 2}
    assert ok_c3
    # ambient multiplicities, by number of rows (stable in n >= ell)
    Kn = {}
    cells = {}
    for lam in lams:
        L = len(lam)
        if L > MAXROWS:
            continue
        if L not in Kn:
            Kn[L] = plethysm_mults(d, L)
        a = a_mult(lam, Kn[L], L)
        g, s = kr[lam]
        cells[lam] = {"a": a, "g": g, "s": s, "ell": L,
                      "top3": sum(lam[:3]), "silent": sum(lam[:3]) <= 2 * d}
    if d == 2:
        c1 = {str(l): (cells[l]["s"], cells[l]["a"]) for l in cells if len(l) <= 5}
        report["controls"]["C1_d2"] = c1
        assert cells[(8,)]["s"] == 1 and cells[(6, 2)]["s"] == 1 and cells[(4, 4)]["s"] == 1
        assert cells[(4, 2, 2)]["s"] == 1 and cells[(2, 2, 2, 2)]["s"] == 1
        assert cells[(8,)]["a"] == 1 and cells[(6, 2)]["a"] == 1 and cells[(4, 4)]["a"] == 1
        assert cells[(4, 2, 2)]["a"] == 0 and cells[(2, 2, 2, 2)]["a"] == 0
        n5 = [l for l in cells if len(l) <= 5 and cells[l]["s"] > 0]
        assert len(n5) == 5, n5
    if d == 3:
        report["controls"]["C2_d3"] = {"(6,3,1,1,1)": cells[(6, 3, 1, 1, 1)], "(5,3,2,1,1)": cells[(5, 3, 2, 1, 1)]}
        assert cells[(6, 3, 1, 1, 1)]["g"] == 3 and cells[(6, 3, 1, 1, 1)]["s"] == 1
        assert cells[(5, 3, 2, 1, 1)]["g"] == 4 and cells[(5, 3, 2, 1, 1)]["s"] == 2
    band = {str(l): cells[l] for l in cells if cells[l]["silent"]}
    report["band"][d] = {
        "cells_computed": len(cells), "band_cells": len(band),
        "band_with_s_gt_a": {k: v for k, v in band.items() if v["s"] > v["a"]},
        "band_all": band,
    }
    print(f"d={d}: cells {len(cells)}, band {len(band)}, band with s>a "
          f"{sum(1 for v in band.values() if v['s'] > v['a'])}, t={time.time()-t0:.1f}s", flush=True)

report["max_rows_computed"] = MAXROWS
report["wall_seconds"] = round(time.time() - t0, 2)
with open(os.path.join(OUT, "band_cells.json"), "w", newline="\n") as f:
    json.dump(report, f, indent=1)
print("controls all passed; wall", report["wall_seconds"])

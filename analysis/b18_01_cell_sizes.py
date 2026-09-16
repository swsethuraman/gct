"""B18-01 pricing pilot: sizes of five-row cells.

For d <= DMAX computes, exactly:
  K(mu)      weight multiplicities of Sym^d(Sym^4 C^5)   (= number of degree-d monomials in the ordinary
             coefficients c_alpha with total weight mu), i.e. dim of the weight-mu space
  a(d,lam)   highest-weight multiplicity = sum_{w in S5} sgn(w) K(lam + rho - w rho), rho = (4,3,2,1,0)
Control: sum_lam a(d,lam) * dim S_lam(C^5) == binom(69+d, d).
Reports, for ell(lam) = 5, a(d,lam) and K(lam) (the size of the space on which a highest-weight basis must be
computed). No determinant or padding evaluation is performed. Pricing input only.

Run bounded: timeout 60 python analysis/b18_01_cell_sizes.py
"""
import itertools, json, os, sys, time
from math import comb, prod

t0 = time.time()
DMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 6
N = 5
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "results", "b18_01")


def comps(total, n):
    if n == 1:
        yield (total,)
        return
    for e in range(total, -1, -1):
        for rest in comps(total - e, n - 1):
            yield (e,) + rest


MON4 = list(comps(4, N))
assert len(MON4) == 70

# layers[j] : dict weight -> number of multisets of size j of degree-4 monomials with that weight
layers = [dict() for _ in range(DMAX + 1)]
layers[0][(0,) * N] = 1
for alpha in MON4:
    for j in range(1, DMAX + 1):          # unbounded knapsack: allow repeated alpha, iterate j upward
        src = layers[j - 1]
        dst = layers[j]
        for w, c in src.items():
            nw = tuple(x + y for x, y in zip(w, alpha))
            dst[nw] = dst.get(nw, 0) + c

rho = (4, 3, 2, 1, 0)
perms = list(itertools.permutations(range(N)))


def sign(p):
    s, seen = 1, set()
    for i in range(N):
        if i in seen:
            continue
        j, L = i, 0
        while j not in seen:
            seen.add(j); j = p[j]; L += 1
        s *= (-1) ** (L - 1)
    return s


SIGNS = [sign(p) for p in perms]


def dimS(lam):
    return prod((lam[i] - lam[j] + j - i) for i in range(N) for j in range(i + 1, N)) // prod(
        (j - i) for i in range(N) for j in range(i + 1, N))


def partitions(total, parts, maxp):
    if parts == 0:
        if total == 0:
            yield ()
        return
    for f in range(min(total, maxp), -1, -1):
        for rest in partitions(total - f, parts - 1, f):
            yield (f,) + rest


report = {"schema": "b18_01-cell-sizes/1", "convention": "ordinary coefficients; weights of c_alpha are alpha",
          "degrees": {}}
for d in range(1, DMAX + 1):
    K = layers[d]
    assert sum(K.values()) == comb(69 + d, d)
    tot, five = 0, []
    for lam in partitions(4 * d, N, 4 * d):
        a = 0
        for p, sg in zip(perms, SIGNS):
            mu = tuple(lam[i] + rho[i] - rho[p[i]] for i in range(N))
            a += sg * K.get(mu, 0)
        if a < 0:
            raise SystemExit("negative multiplicity: bug")
        tot += a * dimS(lam)
        if lam[4] > 0 and a > 0:
            five.append({"lambda": lam, "a": a, "weight_space_dim_K": K.get(lam, 0)})
    ok = tot == comb(69 + d, d)
    report["degrees"][d] = {
        "control_sum_a_dimS_equals_binom": ok,
        "five_row_cells_with_a_positive": len(five),
        "max_a": max((c["a"] for c in five), default=0),
        "max_weight_space_dim": max((c["weight_space_dim_K"] for c in five), default=0),
        "cells": five,
    }
    print(d, "control", ok, "#5-row cells a>0:", len(five), "max a:", report["degrees"][d]["max_a"],
          "max K:", report["degrees"][d]["max_weight_space_dim"], "t=%.1fs" % (time.time() - t0), flush=True)
report["wall_seconds"] = round(time.time() - t0, 2)
with open(os.path.join(OUT, "cell_sizes.json"), "w", newline="\n") as f:
    json.dump(report, f, indent=1)
print("done", report["wall_seconds"])

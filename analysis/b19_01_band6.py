"""B19-01: the first silent-band cell that can have a >= 1.

The silent band (Theorem 4.1) needs ell(lambda) >= 6; a > 0 needs ell(lambda) <= d (constituents of
Sym^d(Sym^4) have at most d rows). So the first band cell with a possible a >= 1 is d = 6, and by
Proposition 4.4(2) the only length-six band cell is the rectangle lambda = (4,4,4,4,4,4) |- 24.

Computes a, g, s for that cell, exactly. Reuses the validated routines of analysis/b19_01_band.py
(controls C1-C5 pass there).

Sanity checks here: s <= g; g(R,R,(4d)) = 1 and s(R,R,(4d)) = 1; the weight-multiplicity total.

Run bounded: timeout 60 python analysis/b19_01_band6.py
"""
import importlib.util, json, os, sys, time
from fractions import Fraction

t0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "results", "b19_01")
spec = importlib.util.spec_from_file_location("b19base", os.path.join(HERE, "b19_01_band.py"))
sys.argv = [sys.argv[0]]
# import the module's functions without running its __main__ body: it has no guard, so read and exec the defs
src = open(os.path.join(HERE, "b19_01_band.py")).read()
cut = src.index('report = {"schema"')
mod = {"__file__": os.path.join(HERE, "b19_01_band.py"), "__name__": "b19base"}
exec(compile(src[:cut], "b19_01_band.py", "exec"), mod)
partitions, chi, f_dim, z_of, square_type = mod["partitions"], mod["chi"], mod["f_dim"], mod["z_of"], mod["square_type"]
plethysm_mults, a_mult = mod["plethysm_mults"], mod["a_mult"]

d, lam = 6, (4, 4, 4, 4, 4, 4)
N, R = 4 * d, (d, d, d, d)

K = plethysm_mults(d, 6)
a = a_mult(lam, K, 6)
print("a =", a, " (%.1fs)" % (time.time() - t0), flush=True)

# control P1: the plethysm total, sum_lambda a(lambda) * dim S_lambda(C^6) = dim Sym^6(Sym^4 C^6)
from math import comb, prod
def dimS6(l):
    l = list(l) + [0] * (6 - len(l))
    return prod((l[i] - l[j] + j - i) for i in range(6) for j in range(i + 1, 6)) // prod(
        (j - i) for i in range(6) for j in range(i + 1, 6))
tot = 0
for l in partitions(N):
    if len(l) <= 6:
        tot += a_mult(l, K, 6) * dimS6(l)
P1 = tot == comb(comb(4 + 5, 5) + d - 1, d)
print("control P1 (plethysm total):", P1, tot, "(%.1fs)" % (time.time() - t0), flush=True)
assert P1

# control P2: characters at the identity class are the tableaux counts
P2 = chi(R, tuple([1] * N)) == f_dim(R) and chi(lam, tuple([1] * N)) == f_dim(lam)
print("control P2 (chi at 1^N = f):", P2, f_dim(R), f_dim(lam), flush=True)
assert P2

g = s = Fraction(0)
g_top = s_top = Fraction(0)
top = (N,)
for eta in partitions(N):
    iz = Fraction(1, z_of(eta))
    cR = chi(R, eta)
    cR2 = chi(R, square_type(eta))   # nonzero even when cR = 0: the symmetric term must not be skipped
    cl = chi(lam, eta)
    if cl:
        g += iz * cl * cR * cR
        s += iz * cl * (cR * cR + cR2)
    g_top += iz * chi(top, eta) * cR * cR
    s_top += iz * chi(top, eta) * (cR * cR + cR2)
s = s / 2
s_top = s_top / 2
assert g.denominator == 1 and s.denominator == 1 and s_top.denominator == 1
g, s, s_top, g_top = int(g), int(s), int(s_top), int(g_top)
checks = {"s_le_g": s <= g, "g_trivial_is_1": g_top == 1, "s_trivial_is_1": s_top == 1,
          "ell_le_d": len(lam) <= d, "band": sum(lam[:3]) <= 2 * d}
print({"lambda": lam, "d": d, "a": a, "g": g, "s": s, **checks}, flush=True)
assert all(checks.values())

out = {"schema": "b19_01-band-d6/1", "cell": {"d": d, "lambda": list(lam), "a": a, "g": g, "s": s},
       "checks": checks, "wall_seconds": round(time.time() - t0, 2)}
with open(os.path.join(OUT, "band_cell_d6.json"), "w", newline="\n") as f:
    json.dump(out, f, indent=1)
print("wall", out["wall_seconds"])

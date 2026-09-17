"""B20-10 pilot 1: an INDEPENDENT evaluator for the (4^5), d = 5 cell.

No project code is imported. The unique (a = 1) degree-5 SL5-invariant of quinary
quartics is realised as the four-epsilon contraction with one epsilon slot fixed to the
identity (the fourth epsilon only contributes the factor 5!):
    I(F) = sum_{tau,rho,pi in S5} sgn(tau) sgn(rho) sgn(pi) prod_i T[i, tau(i), rho(i), pi(i)],
with T the symmetric coefficient tensor scaled by alpha! (an overall constant).
Evaluated as sum_tau sgn(tau) sum_rho sgn(rho) det(N_{tau,rho}), where row i of
N_{tau,rho} is T[i, tau(i), rho(i), :] (Bareiss, exact integers).
It is nonzero (Fermat control), hence a nonzero multiple of the certified
highest-weight vector of B19-02 results/b19_02/rect_4_4_4_4_4.json (a = 1).

Checks:
  (1) the three recorded determinant points (matrices A, 4x4x5) are expanded here as
      det(sum_k x_k B_k) by Leibniz; I(F) is computed; the ratio I(F)/recorded value must
      be the SAME rational constant at all three points (ties this evaluator to their vector);
  (2) I(F) != 0 at each determinant point => m_det >= 1 = a, independently of their vector;
  (3) the three recorded padding points l * per3(N) give I = 0 (null-cone vanishing,
      B18-01 Prop 8.4, replayed independently);
  (4) Fermat control: I(sum t_a x_a^4) = 24^5 * prod t_a (only tau = rho = pi = id survive);
  (5) B19-01 section 6.3 counts: p_4(7) * sum_j p_3(j) p_9(21-j) = 11 * 955 = 10505;
      the crude count at d = 26.
"""
import functools
import hashlib
import itertools
import json
import sys
import time
from fractions import Fraction
from math import factorial

t0 = time.time()
path = sys.argv[1]
raw = open(path, "rb").read()
cert = json.loads(raw)
out = {"input_path": path, "input_sha256": hashlib.sha256(raw).hexdigest()}

N = 5


def poly_mul(p, q):
    r = {}
    for ea, ca in p.items():
        for eb, cb in q.items():
            e = tuple(x + y for x, y in zip(ea, eb))
            r[e] = r.get(e, 0) + ca * cb
    return {e: c for e, c in r.items() if c}


def linform(v):
    return {tuple(1 if i == j else 0 for i in range(N)): int(v[j]) for j in range(N) if v[j]}


def perm_sign(p):
    s = 1
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                s = -s
    return s


def det_linear(A):
    n = len(A)
    tot = {}
    for perm in itertools.permutations(range(n)):
        s = perm_sign(perm)
        p = {tuple([0] * N): 1}
        for i in range(n):
            p = poly_mul(p, linform(A[i][perm[i]]))
            if not p:
                break
        for e, c in p.items():
            tot[e] = tot.get(e, 0) + s * c
    return {e: c for e, c in tot.items() if c}


def per_linear(A):
    n = len(A)
    tot = {}
    for perm in itertools.permutations(range(n)):
        p = {tuple([0] * N): 1}
        for i in range(n):
            p = poly_mul(p, linform(A[i][perm[i]]))
            if not p:
                break
        for e, c in p.items():
            tot[e] = tot.get(e, 0) + c
    return {e: c for e, c in tot.items() if c}


def tensor(F):
    T = {}
    for e, c in F.items():
        af = 1
        for x in e:
            af *= factorial(x)
        idx = []
        for a, x in enumerate(e):
            idx += [a] * x
        assert len(idx) == 4
        for p in set(itertools.permutations(idx)):
            T[p] = c * af
    return T


def det_int(M):
    """Exact integer determinant by fraction-free (Bareiss) elimination."""
    n = len(M)
    A = [row[:] for row in M]
    sign = 1
    prev = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            sw = None
            for r in range(k + 1, n):
                if A[r][k] != 0:
                    sw = r
                    break
            if sw is None:
                return 0
            A[k], A[sw] = A[sw], A[k]
            sign = -sign
        pk = A[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * pk - A[i][k] * A[k][j]) // prev
            A[i][k] = 0
        prev = pk
    return sign * A[n - 1][n - 1]


PERMS = list(itertools.permutations(range(N)))
SG = {p: perm_sign(p) for p in PERMS}


def invariant(F):
    T = tensor(F)
    get = T.get
    total = 0
    for tau in PERMS:
        M = [[[get((i, tau[i], b, c), 0) for c in range(N)] for b in range(N)] for i in range(N)]
        if any(all(v == 0 for row in M[i] for v in row) for i in range(N)):
            continue
        s = 0
        for rho in PERMS:
            rows = [M[i][rho[i]] for i in range(N)]
            if any(all(v == 0 for v in r) for r in rows):
                continue
            d = det_int(rows)
            if d:
                s += SG[rho] * d
        total += SG[tau] * s
    return total


# (4) Fermat control
ferm = {tuple(4 if i == a else 0 for i in range(N)): (a + 2) for a in range(N)}
fv = invariant(ferm)
fexp = 24 ** 5
for a in range(N):
    fexp *= (a + 2)
out["fermat_control"] = {"value": fv, "expected": fexp, "pass": fv == fexp}
# a second control: a generic small integer quartic must give a nonzero value
gen = {}
rng_state = 12345
for e in itertools.combinations_with_replacement(range(N), 4):
    rng_state = (1103515245 * rng_state + 12345) % (2 ** 31)
    v = (rng_state % 7) - 3
    ex = [0] * N
    for a in e:
        ex[a] += 1
    if v:
        gen[tuple(ex)] = v
gv = invariant(gen)
out["generic_control"] = {"monomials": len(gen), "value": gv, "nonzero": gv != 0}

# (1)-(2) determinant points
dets = []
ratios = set()
for rec in cert["det_values"]:
    A = rec["point"]["A"]
    F = det_linear(A)
    v = invariant(F)
    ratio = Fraction(v, rec["value"]) if rec["value"] else None
    ratios.add(ratio)
    dets.append({"recorded_value": rec["value"], "independent_value": v, "nonzero": v != 0,
                 "ratio_independent_over_recorded": str(ratio), "F_monomials": len(F)})
out["det_points"] = dets
out["ratio_constant_across_three_det_points"] = (len(ratios) == 1)
out["ratio"] = str(next(iter(ratios)))
out["m_det_floor_independent"] = 1 if all(d["nonzero"] for d in dets) else 0

# (3) padding points
pads = []
for rec in cert["pad_values"]:
    l = rec["point"]["l"]
    Nm = rec["point"]["N"]
    C = per_linear(Nm)
    F = poly_mul(linform(l), C)
    v = invariant(F)
    pads.append({"recorded_value": rec["value"], "independent_value": v, "F_monomials": len(F)})
out["pad_points"] = pads
out["all_pad_values_zero"] = all(p["independent_value"] == 0 for p in pads)


# (5) counts
@functools.lru_cache(None)
def _p(n, k, mx):
    if n == 0:
        return 1
    if k == 0:
        return 0
    return sum(_p(n - x, k - 1, x) for x in range(1, min(n, mx) + 1))


def p_atmost(n, k):
    return _p(n, k, n)


def crude(d):
    return p_atmost(d, 4) * sum(p_atmost(j, 3) * p_atmost(3 * d - j, 9) for j in range(2 * d + 1, 3 * d + 1))


out["counts"] = {"d7_p4": p_atmost(7, 4),
                 "d7_inner_sum": sum(p_atmost(j, 3) * p_atmost(21 - j, 9) for j in range(15, 22)),
                 "d7_crude_triples": crude(7), "d26_crude_triples": crude(26)}
out["seconds"] = time.time() - t0
json.dump(out, open(sys.argv[2], "w"), indent=1)
print(json.dumps({k: v for k, v in out.items() if k not in ("det_points", "pad_points")}, indent=1))
for d in dets:
    print(d)
for p in pads:
    print(p)

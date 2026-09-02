#!/usr/bin/env python3
"""
Session 36 -- exact (rational) certificate for a biting HWV.

From the two mod-p exhibits of a vanishing HWV (wk9_s36_bite.py), CRT the
coefficients to Z/(p1 p2) and rationally reconstruct.  Then, over Q with
python ints/Fractions and NO modular arithmetic:
  (1) apply every simple raising operator (corrected rule) to the rational
      vector and check the result is identically zero  -> it IS an HWV over Q;
  (2) evaluate it at integer points of the biting family (true padded
      permanent, and l . cubic), expanded symbolically -> exact zeros;
  (3) evaluate at integer generic quartics and det pencils -> exact nonzeros.
Writes the rational vector (denominator-cleared, integer coefficients) next to
the mod-p exhibits.

usage: python3 wk9_s36_exact.py <lam as 8,4,4,4,4> <delta> <side>
"""
import sys, os, random
from fractions import Fraction
from math import gcd
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from wk9_s36_stabred import exps, P1, P2
from wk9_s36_bite import family, pmul

def ratrec(a, m):
    """rational reconstruction of a mod m (|num|, den <= sqrt(m/2))."""
    a %= m
    bound = int((m // 2) ** 0.5)
    r0, r1, s0, s1 = m, a, 0, 1
    while r1 > bound:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
    if s1 == 0 or abs(s1) > bound: return None
    if s1 < 0: r1, s1 = -r1, -s1
    return Fraction(r1, s1)

def load(lam, delta, side, prime):
    fn = os.path.join(HERE, '..', 'results', 's36_cells',
                      f"{'_'.join(map(str, lam))}_d{delta}_{side}_p{prime}_vec1.txt")
    out = {}
    for ln in open(fn):
        if ln.startswith('#'): continue
        k, v = ln.rsplit(' ', 1)
        out[tuple(tuple(x) for x in eval(k))] = int(v) % prime
    return out

if __name__ == '__main__':
    lam = tuple(int(x) for x in sys.argv[1].split(',')); delta = int(sys.argv[2]); side = sys.argv[3]
    r = len(lam); n = 4
    v1, v2 = load(lam, delta, side, P1), load(lam, delta, side, P2)
    assert set(v1) == set(v2), "supports differ between primes"
    M = P1 * P2
    inv = pow(P1, -1, P2)
    vec = {}
    for m in v1:
        a1, a2 = v1[m], v2[m]
        x = (a1 + P1 * (((a2 - a1) * inv) % P2)) % M       # CRT
        q = ratrec(x, M)
        assert q is not None, ("rational reconstruction failed", m, x)
        vec[m] = q
    den = 1
    for q in vec.values(): den = den * q.denominator // gcd(den, q.denominator)
    ivec = {m: int(q * den) for m, q in vec.items()}
    g = 0
    for v in ivec.values(): g = gcd(g, abs(v))
    ivec = {m: v // g for m, v in ivec.items()}
    # consistency: the integer vector must reduce to the mod-p exhibits up to a scalar
    for prime, vp in ((P1, v1), (P2, v2)):
        m0 = next(iter(ivec)); lam_ = ivec[m0] * pow(vp[m0], prime - 2, prime) % prime
        assert all(ivec[m] % prime == lam_ * vp[m] % prime for m in ivec), ("mod-p mismatch", prime)
    mx = max(abs(v) for v in ivec.values())
    print(f"rational vector reconstructed: {len(ivec)} terms, common denominator {den}, "
          f"integer coefficients up to {mx} (gcd removed {g})")
    # (1) raising operators over Z, corrected rule, on the multiset representation
    A = exps(n, r); idx = {a: k for k, a in enumerate(A)}
    for i in range(r - 1):
        j = i + 1
        acc = {}
        for m, cf in ivec.items():
            for p_ in range(len(m)):
                al = m[p_]
                if al[j] == 0: continue
                nb = list(al); nb[j] -= 1; nb[i] += 1
                nm = tuple(sorted(m[:p_] + (tuple(nb),) + m[p_ + 1:]))
                acc[nm] = acc.get(nm, 0) + cf * (al[i] + 1)
        bad = sum(1 for v in acc.values() if v)
        print(f"  E_{i}{j} . v over Z: {bad} nonzero target coefficients (must be 0)")
        assert bad == 0
    print("  => the vector is an exact highest-weight vector over Q of weight", lam)
    # (2),(3) exact evaluations
    def ev(F):
        tot = 0
        for m, cf in ivec.items():
            t = cf
            for al in m:
                c = F.get(al, 0)
                if c == 0: t = 0; break
                t *= c
            tot += t
        return tot
    rnd = random.Random(360)
    for kind, want0 in (('truepad', True), ('l_cubic', True), ('generic', False), ('det', False)):
        vals = [ev(family(kind, rnd, r, bound=9)) for _ in range(12)]
        nz = sum(1 for v in vals if v)
        print(f"  exact evaluation at 12 integer {kind:8s} points: {nz} nonzero"
              + ("  (expected 0)" if want0 else "  (expected 12)"))
        assert (nz == 0) if want0 else (nz == 12)
    fn = os.path.join(HERE, '..', 'results', 's36_cells',
                      f"{'_'.join(map(str, lam))}_d{delta}_{side}_exactZ.txt")
    with open(fn, 'w') as fh:
        fh.write(f"# weight {lam} delta {delta}: EXACT integer HWV vanishing on the {side} side "
                 f"({len(ivec)} terms; rational reconstruction from primes {P1},{P2}; "
                 f"verified E_i,i+1 . v = 0 over Z for every i, and exact zeros at truepad/l.cubic points)\n")
        for m, v in sorted(ivec.items()): fh.write(f"{[list(a) for a in m]} {v}\n")
    print("wrote", fn)

# ---------------------------------------------------------------------------
# PROOF that the exact HWV vanishes on the whole reducible locus X = {l . c}.
# v is a B-eigenvector (HWV), so v vanishes on B.Y iff on Y; Bruhat
# G = U_w B w P_i with P_i the parabolic stabilising the line of x_i gives
# G.{x_5 c} = U_i B.{x_i c}.  Hence
#     v in I(X)   <=>   v|_{x_i . c} == 0 as a polynomial in c, for i = 1..r,
# and v|_{x_i . c} is obtained by killing every c_alpha with alpha_i = 0 and
# renaming alpha -> alpha - e_i.  Five (six) sparse symbolic substitutions.
def proof_reducible(ivec, r):
    for i in range(r):
        acc = {}
        for m, cf in ivec.items():
            if any(al[i] == 0 for al in m): continue
            key = tuple(sorted(tuple(al[t] - (1 if t == i else 0) for t in range(r)) for al in m))
            acc[key] = acc.get(key, 0) + cf
        surv = sum(1 for v in acc.values() if v)
        print(f"  v restricted to {{x_{i+1} . c}}: {len(acc)} candidate cubic-monomials, {surv} with nonzero coefficient (must be 0)")
        assert surv == 0
    print("  => PROVED (exact, Bruhat + B-eigenvector): v vanishes identically on the reducible locus {l . c}")

if __name__ == '__main__':
    proof_reducible(ivec, r)

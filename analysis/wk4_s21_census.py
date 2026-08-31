"""Session 21 - ambient census by adjoint rim-hook DP.

  dim C[Sym^3 C^m]^{SL_m}_delta  =  < h_delta[h_3] , s_{((3 delta/m)^m)} >

computed as  < 1 , (h_delta[h_3])^perp s_lambda >  by applying the adjoint
power-sum operators p_r^perp (rim-hook removal, Murnaghan-Nakayama) to s_lambda:

  sum_delta t^delta h_delta[h_3] = exp( sum_r (p_r^3 + 3 p_r p_{2r} + 2 p_{3r}) t^r /(6r) )

Every intermediate partition is a subdiagram of lambda, so the whole state space
is the set of partitions inside the m x (3 delta/m) box - 24310 of them for
lambda = (8^9).  Exact rational arithmetic (fractions.Fraction).
"""
import sys
from fractions import Fraction
from collections import defaultdict

def rimhooks(lam, r):
    """All (mu, sign) from removing a rim hook of size r from partition lam."""
    k = len(lam)
    if k == 0:
        return []
    beta = [lam[i] + (k - 1 - i) for i in range(k)]
    S = set(beta)
    out = []
    for f in beta:
        g = f - r
        if g >= 0 and g not in S:
            between = sum(1 for x in S if g < x < f)
            nb = sorted((S - {f}) | {g}, reverse=True)
            kk = len(nb)
            nl = tuple(x - (kk - 1 - i) for i, x in enumerate(nb))
            nl = tuple(p for p in nl if p > 0)
            out.append((nl, (-1) ** between))
    return out

def apply_p(vec, r):
    out = defaultdict(Fraction)
    for lam, c in vec.items():
        for mu, s in rimhooks(lam, r):
            out[mu] += c * s
    return {k: v for k, v in out.items() if v != 0}

def census_all(m, delta_max):
    """Return {delta: dim of SL_m-invariants of degree delta in Sym^3 C^m}."""
    res = {}
    for delta in range(1, delta_max + 1):
        if (3 * delta) % m:
            continue
        k = (3 * delta) // m
        lam = tuple([k] * m)
        # state: (degree_used) -> {partition: coeff}
        V = [dict() for _ in range(delta + 1)]
        V[0] = {lam: Fraction(1)}
        for r in range(1, delta + 1):
            NV = [dict(d) for d in V]
            # exp(t^r X_r):  X_r = (p_r^3 + 3 p_r p_2r + 2 p_3r)/(6r)
            for d0 in range(0, delta + 1):
                if not V[d0]:
                    continue
                cur = V[d0]
                m_ = 1
                while d0 + r * m_ <= delta:
                    nxt = defaultdict(Fraction)
                    for lm, c in cur.items():
                        # p_r p_r p_r
                        t1 = apply_p(apply_p(apply_p({lm: c}, r), r), r)
                        for a, b in t1.items():
                            nxt[a] += b
                        # 3 p_r p_2r
                        t2 = apply_p(apply_p({lm: c}, r), 2 * r)
                        for a, b in t2.items():
                            nxt[a] += 3 * b
                        # 2 p_3r
                        t3 = apply_p({lm: c}, 3 * r)
                        for a, b in t3.items():
                            nxt[a] += 2 * b
                    cur = {a: b / (6 * r) / m_ for a, b in nxt.items() if b != 0}
                    if not cur:
                        break
                    tgt = NV[d0 + r * m_]
                    for a, b in cur.items():
                        tgt[a] = tgt.get(a, Fraction(0)) + b
                    m_ += 1
            V = [{a: b for a, b in d.items() if b != 0} for d in NV]
        val = V[delta].get((), Fraction(0))
        assert val.denominator == 1, (delta, val)
        res[delta] = int(val)
    return res

if __name__ == "__main__":
    m = int(sys.argv[1]) if len(sys.argv) > 1 else 9
    dmax = int(sys.argv[2]) if len(sys.argv) > 2 else 24
    r = {}
    for d in range(3, dmax+1, 3):
        if (3*d) % m: continue
        v = census_all(m, d)[d]
        print(f"m={m}  delta={d:3d}   dim = {v}", flush=True)
        r[d]=v
    for d in sorted(r):
        print(f"m={m}  delta={d:3d}   dim C[Sym^3 C^{m}]^SL_{m}_{d} = {r[d]}", flush=True)

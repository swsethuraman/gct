#!/usr/bin/env python3
"""
Session 47 -- independent verification of a(lam,delta) and h_pad(lam,delta) at
the refutation cell, by three routes that share no code below the partition
enumeration:

  route 1  wk9_s42_hpad.h_pad          symmetric-function plethysm (wk8_s30_pleth.amb)
  route 2  wk9_s42_census.h_pad_weyl   Weyl alternation with a tail DP
  route 3  this file                   Weyl alternation over an INDEPENDENT
                                       weight-multiplicity count K(mu) obtained by
                                       a fresh DP over the degree-3 monomials

Route 3's K(mu) = number of multisets of `delta` degree-3 monomials in r variables
with total exponent vector mu; the plethysm multiplicity is then
c_nu = sum_w sign(w) K(nu + rho - w rho), the ordinary Weyl alternation, and
h_pad = sum over Pieri strips.  Nothing here reuses amb() or the s42 DP.

usage: python3 wk9_s47_hpadcheck.py delta lam1 lam2 ...
"""
import sys, os, itertools
from functools import lru_cache

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)


def deg_monomials(n, r):
    """exponent vectors of the degree-n monomials in r variables."""
    def rec(i, left):
        if i == r - 1:
            yield (left,); return
        for v in range(left + 1):
            for rest in rec(i + 1, left - v):
                yield (v,) + rest
    return sorted(rec(0, n))


def K_all(delta, n, r, cap):
    """{mu: number of multisets of `delta` degree-n monomials with sum mu},
    over all mu with every mu_i <= cap_i.  Multiset count by the standard
    'monomials in a fixed order, choose multiplicities' DP: process the
    monomials one at a time, allowing any multiplicity, tracking (used, mu)."""
    mons = deg_monomials(n, r)
    cur = {(0,) * r: [0] * (delta + 1)}
    cur[(0,) * r][0] = 1
    for m in mons:
        nxt = {}
        for mu, vec in cur.items():
            for k in range(delta + 1):
                if not vec[k]: continue
                # add j copies of m
                mu2 = mu; j = 0
                while k + j <= delta:
                    if j:
                        mu2 = tuple(mu2[i] + m[i] for i in range(r))
                        if any(mu2[i] > cap[i] for i in range(r)): break
                    tgt = nxt.setdefault(mu2, [0] * (delta + 1))
                    tgt[k + j] += vec[k]
                    j += 1
        cur = nxt
    return {mu: v[delta] for mu, v in cur.items() if v[delta]}


def c_nu_all(delta, n, r, cap):
    """{nu: multiplicity of S_nu in Sym^delta(Sym^n C^r)} for dominant nu with
    nu_i <= cap_i, by Weyl alternation over the K table."""
    K = K_all(delta, n, r, [c + r for c in cap])
    rho = tuple(range(r - 1, -1, -1))
    out = {}
    for nu, _ in list(K.items()):
        if any(nu[i] < nu[i + 1] for i in range(r - 1)): continue
        if any(nu[i] > cap[i] for i in range(r)): continue
        tot = 0
        for w in itertools.permutations(range(r)):
            sgn = perm_sign(w)
            mu = tuple(nu[i] + rho[i] - rho[w[i]] for i in range(r))
            if any(v < 0 for v in mu): continue
            tot += sgn * K.get(tuple(sorted(mu, reverse=True)) if False else mu, 0)
        if tot: out[nu] = tot
    return out


def perm_sign(w):
    s = 1
    w = list(w)
    for i in range(len(w)):
        for j in range(i + 1, len(w)):
            if w[i] > w[j]: s = -s
    return s


def pieri_nus(lam, delta):
    r = len(lam); target = sum(lam) - delta
    out = []
    def rec(i, cur, s):
        if i == r:
            if s == target: out.append(tuple(cur))
            return
        lo = lam[i + 1] if i + 1 < r else 0
        for v in range(lo, lam[i] + 1):
            rec(i + 1, cur + [v], s + v)
    rec(0, [], 0)
    return out


def h_pad_route3(lam, delta):
    lam = tuple(lam); r = len(lam)
    nus = pieri_nus(lam, delta)
    cap = list(lam)
    C = c_nu_all(delta, 3, r, cap)
    return sum(C.get(nu, 0) for nu in nus), len(nus)


if __name__ == '__main__':
    delta = int(sys.argv[1]); lam = tuple(int(v) for v in sys.argv[2:])
    from wk9_s42_hpad import h_pad as h1
    from wk8_s30_pleth import a_of
    sys.path.insert(0, HERE)
    from wk9_s42_census import h_pad_weyl, a_weyl
    a1 = a_of(lam, delta, 4, len(lam))
    a2 = a_weyl(lam, delta, 4, {})
    print(f"a  route1 (pleth)      = {a1}", flush=True)
    print(f"a  route2 (Weyl alt)   = {a2}", flush=True)
    v1 = h1(lam, delta)
    print(f"h_pad route1 (pleth)   = {v1}", flush=True)
    v2 = h_pad_weyl(lam, delta, {})
    print(f"h_pad route2 (Weyl alt)= {v2}", flush=True)
    v3, nnu = h_pad_route3(lam, delta)
    print(f"h_pad route3 (fresh DP)= {v3}   ({nnu} Pieri strips)", flush=True)
    assert a1 == a2, "a routes disagree"
    assert v1 == v2 == v3, "h_pad routes disagree"
    print(f"AGREE: a = {a1}, h_pad = {v1}, bound {'FIRES' if v1 < a1 else 'silent'}")

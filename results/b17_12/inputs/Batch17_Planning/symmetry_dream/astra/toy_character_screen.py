"""Exact, bounded GL_16 character screen: n=4, hard ceiling degree 6.

Run only through the inspected existing b15_bound.py (60 s, 512 MiB).
Standard library only. No ranks on polynomial orbit closures are inferred.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from math import factorial, comb
from pathlib import Path
import json
import sys


@lru_cache(None)
def parts(n, cap=None):
    if n == 0:
        return ((),)
    cap = min(n, n if cap is None else cap)
    return tuple((k,) + p for k in range(cap, 0, -1)
                 for p in parts(n-k, k))


def zpart(p):
    ans = 1
    for k, c in Counter(p).items():
        ans *= k**c * factorial(c)
    return ans


@lru_cache(None)
def char(lam, rho):
    if not rho:
        return int(not lam)
    if sum(lam) != sum(rho):
        return 0
    k, tail = rho[0], rho[1:]
    ell = len(lam)
    beta = tuple(lam[i]+ell-i-1 for i in range(ell))
    answer = 0
    for b in beta:
        c = b-k
        if c < 0 or c in beta:
            continue
        sign = (-1)**sum(c < t < b for t in beta)
        new = sorted((t for t in beta if t != b), reverse=True)
        new.append(c)
        new.sort(reverse=True)
        mu = tuple(t-ell+i+1 for i, t in enumerate(new))
        mu = tuple(t for t in mu if t)
        answer += sign * char(mu, tail)
    return answer


@lru_cache(None)
def pleth_ps(d, n):
    result = defaultdict(Fraction)
    for alpha in parts(d):
        current = {(): Fraction(1, zpart(alpha))}
        for k in alpha:
            nxt = defaultdict(Fraction)
            for rho, a in current.items():
                for beta in parts(n):
                    new = tuple(sorted(rho+tuple(k*b for b in beta), reverse=True))
                    nxt[new] += a / zpart(beta)
            current = nxt
        for rho, a in current.items():
            result[rho] += a
    return dict(result)


def pleth_mult(d, n, lam):
    ans = sum(c*char(lam, rho) for rho, c in pleth_ps(d, n).items())
    assert ans.denominator == 1 and ans >= 0
    return int(ans)


def square_type(rho):
    out = []
    for k in rho:
        out.extend([k//2, k//2] if k % 2 == 0 else [k])
    return tuple(sorted(out, reverse=True))


def kron(lam, rect):
    g = Fraction(0)
    trace = Fraction(0)
    for rho in parts(sum(lam)):
        c = Fraction(char(lam, rho), zpart(rho))
        g += c*char(rect, rho)**2
        trace += c*char(rect, square_type(rho))
    plus, minus = (g+trace)/2, (g-trace)/2
    assert all(x.denominator == 1 for x in (g, trace, plus, minus))
    assert min(g, plus, minus) >= 0
    return int(g), int(trace), int(plus), int(minus)


def horizontal(lam, mu):
    m = mu+(0,)*(len(lam)+1-len(mu))
    l = lam+(0,)
    return all(l[i] >= m[i] >= l[i+1] for i in range(len(lam)))


def schur_dim(lam, N):
    l = lam+(0,)*(N-len(lam))
    ans = Fraction(1)
    for i in range(N):
        for j in range(i+1, N):
            ans *= Fraction(l[i]-l[j]+j-i, j-i)
    assert ans.denominator == 1
    return int(ans)


def controls():
    # Full character row orthogonality through S_6 (independent of plethysm).
    for q in range(1, 7):
        for a in parts(q):
            for b in parts(q):
                assert sum(Fraction(char(a,r)*char(b,r),zpart(r))
                           for r in parts(q)) == int(a == b)
    # The transpose trace formula on the explicit S_4 standard representation.
    assert kron((4,), (3,1)) == (1,1,1,0)
    assert kron((2,1,1), (3,1)) == (1,-1,0,1)
    # Sym^2(Sym^4) has the known multiplicity-free decomposition.
    assert {p: pleth_mult(2,4,p) for p in parts(8)
            if pleth_mult(2,4,p)} == {(8,):1,(6,2):1,(4,4):1}


def main():
    lo, hi = (int(x) for x in sys.argv[1:]) if len(sys.argv)>1 else (1,4)
    assert 1 <= lo <= hi <= 6, 'Hard ceiling: degree 6.'
    controls()
    all_rows = []
    summaries = []
    for d in range(lo,hi+1):
        core = {mu: pleth_mult(d,3,mu) for mu in parts(3*d)
                if len(mu) <= min(d,9)}
        rows = []
        for lam in parts(4*d):
            if len(lam) > min(d,10):
                continue
            a = pleth_mult(d,4,lam)
            if not a:
                continue
            g, trace, plus, minus = kron(lam, (d,)*4)
            U_source = sum(c for mu,c in core.items() if horizontal(lam,mu))
            U = min(a, U_source)
            rows.append(dict(d=d, weight=lam, ambient=a,
                             connected=g, transpose_trace=trace,
                             symmetric=plus, alternating=minus,
                             padding_source_raw=U_source,padding_ceiling=U,
                             symmetry_headroom=U-min(a,plus)))
        # Whole ambient Schur decomposition dimension check in 16 variables.
        assert sum(r['ambient']*schur_dim(tuple(r['weight']),16) for r in rows) == comb(comb(19,4)+d-1,d)
        summaries.append(dict(d=d, ambient_cells=len(rows),
                              ambient_multiplicity_sum=sum(r['ambient'] for r in rows),
                              symmetry_deficit_cells=sum(r['symmetric']<r['ambient'] for r in rows),
                              headroom_cells=sum(r['symmetry_headroom']>0 for r in rows)))
        all_rows.extend(rows)
    result = dict(scope=f'n=4, m=3, d={lo}..{hi} only; exact character/source counts, no closure ranks',
                  controls='S_q row orthogonality q<=6; S_4 transpose signs; Sym^2(Sym^4); full GL_16 dimension per degree',
                  summaries=summaries,rows=all_rows)
    outfile = 'toy_character_screen.json' if (lo,hi)==(1,4) else f'toy_character_screen_d{lo}_d{hi}.json'
    Path(outfile).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(summaries,indent=2))
    print(json.dumps([r for r in all_rows if r['symmetry_headroom']>0],indent=2))


if __name__ == '__main__':
    main()

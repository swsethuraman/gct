#!/usr/bin/env python3
"""The u-transport, checked end to end against the delivered artefacts.

The claim under test (S3's continuation, relayed by the reasoning side): a
complete conversion at rung 13 with determinant rank 39 at both house primes
gives i_det(13) = 0, and the multiplication-by-u transport carries that to
rank T_det(24) >= 39, raising the banked determinant lower bound from 2.

What this script establishes, using no number from S1 or S3 except as the thing
being tested:

  A. the mechanism.  Evaluation at a point is a ring homomorphism, so
     (u^k w)(P) = u(P)^k . w(P): the transported matrix is the base matrix with
     column j scaled by u(P_j)^k, and the transported minor is the base minor
     times prod_j u(P_j)^k.  It is nonzero exactly when the base minor is
     nonzero and no sampled point is a u-zero.
  B. the implementation.  S1's transported_det_lower_bound_2.json is exactly
     that product applied to its own 4_det control matrix, entry by entry, at
     both primes -- recovered here by dividing the scaling back out.
  C. the same bound from the repository's own data.  s69_n4_seed.json's twelve
     determinant pencils have u(P) = det(A_1) nonzero at all twelve points and
     a nonzero 2x2 determinant minor at both primes, so rank T_det(24) >= 2
     reproduces without any S1 input.
  D. the arithmetic of the raise.  a_13 = 39 on the banked ladder, u^11 carries
     rung 13 to rung 24, and i_det(13) = 0 gives rank T_det(24) >= 39.
"""
import json, os
from fractions import Fraction

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
P1, P2 = 2147483647, 2147483629
out = {'checks': []}

def rec(name, ok, **kw):
    out['checks'].append(dict(name=name, ok=bool(ok), **kw))
    print(f'[{"PASS" if ok else "FAIL"}] {name}' + (f'  {kw}' if kw else ''))
    return ok

def det_int(M):
    n = len(M); A = [[Fraction(x) for x in r] for r in M]; sg = 1; d = Fraction(1)
    for c in range(n):
        p = next((r for r in range(c, n) if A[r][c] != 0), None)
        if p is None: return 0
        if p != c: A[c], A[p] = A[p], A[c]; sg = -sg
        d *= A[c][c]
        for r in range(c + 1, n):
            f = A[r][c] / A[c][c]
            for k in range(c, n): A[r][k] -= f * A[c][k]
    v = sg * d; assert v.denominator == 1
    return int(v)

# ---------------------------------------------------------------- B: S1's artefact
s1 = json.load(open(f'{ROOT}/results/astra/S1/transported_det_lower_bound_2.json'))
ctl = json.load(open(f'{ROOT}/results/astra/S1/control_matrices.json'))
K = 12                                            # rung 12 -> rung 24
for r in s1:
    p = r['prime']; u = r['u_values']; idx = r['seed_point_indices']; M = r['matrix']
    base = ctl['matrices'][f'4_det_{p}']
    pred = [[base[i][j] * pow(u[c], K, p) % p for c, j in enumerate(idx)] for i in range(2)]
    rec(f'S1 transported matrix = base . diag(u^12), p={p}', pred == M)
    db = (base[idx[0]][idx[0]] * base[idx[1]][idx[1]]
          - base[idx[0]][idx[1]] * base[idx[1]][idx[0]]) % p
    sc = 1
    for c in u: sc = sc * pow(c, K, p) % p
    rec(f'S1 transported det = base minor . prod u^12, p={p}',
        db * sc % p == r['determinant'], base_minor=db, scale=sc, recorded=r['determinant'])
    rec(f'S1 base minor is nonzero, p={p}', db != 0)
    rec(f'no sampled seed point is a u-zero, p={p}', all(c % p for c in u), u_values=u)
    rec(f'S1 base minor agrees with its own control minor, p={p}',
        db == ctl['minors'][f'4_det_{p}']['det'], control=ctl['minors'][f'4_det_{p}']['det'])

# ------------------------------------------------- C: the same bound from repo data
seed = json.load(open(f'{ROOT}/results/s69_n4_seed.json'))
side = int(round(len(seed['det_pencils_A'][0][0]) ** 0.5))
uv = [det_int([pen[0][i*side:(i+1)*side] for i in range(side)]) for pen in seed['det_pencils_A']]
rec('u(P) = det(A_1) nonzero at all 12 repository determinant points',
    all(v != 0 for v in uv), u_values=uv)
for p in (P1, P2):
    rows = seed['rows_det'][str(p)]
    best = None
    for i in range(len(rows[0])):
        for j in range(i + 1, len(rows[0])):
            d = (rows[0][i]*rows[1][j] - rows[0][j]*rows[1][i]) % p
            if d: best = (i, j, d); break
        if best: break
    rec(f'repository seed gives a nonzero 2x2 determinant minor, p={p}', best is not None,
        cols=best[:2] if best else None, minor=best[2] if best else None)
    if best:
        i, j, d = best
        sc = pow(uv[i] % p, K, p) * pow(uv[j] % p, K, p) % p
        rec(f'its transport to rung 24 is nonzero, p={p}', d * sc % p != 0,
            transported_minor=d * sc % p)
out['independent_lower_bound_from_repo_data'] = 2

# ---------------------------------------------------------------- D: the raise
lad = json.load(open(f'{ROOT}/results/s63_aladder.json'))['ladder']   # a_12 .. a_25
a = {12 + i: v for i, v in enumerate(lad)}
rec('a_13 = 39 on the banked ladder', a[13] == 39, a_13=a[13])
rec('a_24 = 274 on the banked ladder', a[24] == 274, a_24=a[24])
rec('u^11 carries rung 13 to rung 24 in degree', 13 + 11 == 24)
lam13 = (4*13 - 31, 17) + (2,)*7
lam24 = (4*24 - 31, 17) + (2,)*7
wt = tuple(x + y for x, y in zip(lam13, (11*4,) + (0,)*8))
rec('u^11 carries rung 13 to rung 24 in weight', wt == lam24, lam13=lam13, shifted=wt, lam24=lam24)
rec('the ladder is nondecreasing, so i_det is too', all(a[d] >= a[d-1] for d in range(13, 25)))
out['raise'] = {'i_det_13': 0, 'a_13': a[13], 'k': 11,
                'rank_T_det_24_lower_bound': a[13],
                'i_det_24_upper_bound': a[24] - a[13]}
print(f'\nif i_det(13) = 0 then rank T_det(24) >= a_13 = {a[13]}, i.e. i_det(24) <= {a[24]-a[13]}')
print(f'ladder of available raises: ' +
      ', '.join(f'rung {d} -> >= {a[d]}' for d in range(13, 24)))

ok = all(c['ok'] for c in out['checks'])
out['status'] = 'OK' if ok else 'FAILURES'
json.dump(out, open(f'{ROOT}/results/wk12_int_transport_check.json', 'w'), indent=1)
print('\nRESULT', out['status'], f"({sum(c['ok'] for c in out['checks'])}/{len(out['checks'])})")

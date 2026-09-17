"""Verification of the recorded certificates of this packet (standard library only; no contraction is re-evaluated).

What is recomputed independently here:
  1. Ranks of the recorded degree-12 and degree-11 forbidden rows on (q3, q7, n02) modulo P (from the sealed parent
     packets' numbers): degree-12 rows rank 1 with constant ratios, degree-11 rows rank 2.
  2. Slice geometry (results/slice_choice.json) with a fresh implementation of the tangent-rank and poisedness
     computations (exact rationals): tangent rank 23 at the transversal point, poised rank 50, degenerate 3-dim
     sub-slice rank 16.
  3. CRT bounds against the prime products used in pilot 3 (results/p3_covariant_relation.json).
  4. Internal consistency of the pilot-3 record: factorization controls passed, exact coordinates, r_top = 3 with all 50
     points done, false-identity control.
What is NOT recomputed: the two-column contraction values (they come from pilot 3's evaluator, validated there by the
factorization control against sealed runner values and by agreement with the sealed int64 path in the smoke test)."""
import itertools, json, sys
from fractions import Fraction
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / 'code'))
P = 524287
ok = True
def check(name, cond, detail=''):
    global ok
    ok &= bool(cond); print(('PASS ' if cond else 'FAIL ') + name + (' ' + str(detail) if detail else ''))
def rank_mod(M):
    M = [[x % P for x in r] for r in M]; r = 0
    for c in range(len(M[0])):
        piv = next((i for i in range(r, len(M)) if M[i][c]), None)
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]; inv = pow(M[r][c], P - 2, P); M[r] = [x * inv % P for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c]: f = M[i][c]; M[i] = [(x - f * y) % P for x, y in zip(M[i], M[r])]
        r += 1
    return r
rows12 = [[176113, 112168, 44818], [190461, 231336, 338217], [232316, 28953, 238815], [376209, 469277, 41046], [469768, 310015, 415152]]
rows11 = [[34725, 239889, 380115], [163934, 316261, 169076], [395778, 379744, 423266], [86170, 71919, 226580], [347334, 318883, 320901]]
check('degree-12 rows (3 S0 + 2 full points) have rank 1', rank_mod(rows12) == 1)
check('degree-11 rows have rank 2', rank_mod(rows11) == 2)
check('degree-12 ratios constant (q7/q3 = 101007, n02/q3 = 295818)', all(r[1] * pow(r[0], P - 2, P) % P == 101007 and r[2] * pow(r[0], P - 2, P) % P == 295818 for r in rows12))
# slice geometry, fresh implementation
NAMES = ['a', 'r1', 'r2', 'r3', 'c1', 'c2', 'c3', 'S11', 'S22', 'S33', 'S12', 'S13', 'S23']; I = {n: i for i, n in enumerate(NAMES)}
def sig(k, l): return 'S%d%d' % (min(k, l), max(k, l))
def gens():
    G = {}
    def M(): return [[Fraction(0)] * 13 for _ in range(13)]
    m = M(); m[0][0] = 1
    for k in (1, 2, 3): m[I['r%d' % k]][I['r%d' % k]] = 1
    G['alpha'] = m
    m = M(); m[0][0] = 1
    for k in (1, 2, 3): m[I['c%d' % k]][I['c%d' % k]] = 1
    G['beta'] = m
    m = M()
    for k in (1, 2, 3): m[I['r%d' % k]][I['r%d' % k]] = 1
    for k in (1, 2, 3):
        for l in range(k, 4): m[I[sig(k, l)]][I[sig(k, l)]] = 1
    G['c'] = m
    for k in (1, 2, 3):
        for l in (1, 2, 3):
            m = M(); m[I['r%d' % k]][I['r%d' % l]] += 1; m[I['c%d' % k]][I['c%d' % l]] += 1
            for n in (1, 2, 3): m[I[sig(k, n)]][I[sig(l, n)]] += 1; m[I[sig(n, k)]][I[sig(n, l)]] += 1
            G['g%d%d' % (k, l)] = m
    for k in (1, 2, 3):
        m = M(); m[I['c%d' % k]][0] += 1
        for n in (1, 2, 3): m[I[sig(k, n)]][I['r%d' % n]] += Fraction(1) if n == k else Fraction(1, 2)
        G['L%d' % k] = m
    for n in (1, 2, 3):
        m = M(); m[I['r%d' % n]][0] += 1
        for k in (1, 2, 3): m[I[sig(k, n)]][I['c%d' % k]] += Fraction(1) if k == n else Fraction(1, 2)
        G['R%d' % n] = m
    return G
PAIRS = [(i, j) for i in range(13) for j in range(i + 1, 13)]
def w2(u, v): return [u[i] * v[j] - u[j] * v[i] for i, j in PAIRS]
def mv(m, v): return [sum(m[i][j] * v[j] for j in range(13)) for i in range(13)]
def rankQ(rows):
    M = [[Fraction(x) for x in r] for r in rows]; rk = 0
    for c in range(len(M[0])):
        piv = next((i for i in range(rk, len(M)) if M[i][c] != 0), None)
        if piv is None: continue
        M[rk], M[piv] = M[piv], M[rk]; inv = 1 / M[rk][c]; M[rk] = [x * inv for x in M[rk]]
        for i in range(len(M)):
            if i != rk and M[i][c] != 0: f = M[i][c]; M[i] = [x - f * y for x, y in zip(M[i], M[rk])]
        rk += 1
    return rk
sl = json.loads((HERE / 'results/slice_choice.json').read_text())
A = [[Fraction(x) for x in v] for v in sl['A']]; s, t = sl['transversal_point']
Z1 = [sum(s[k] * A[k][i] for k in range(5)) for i in range(13)]; Z2 = [sum(t[k] * A[k][i] for k in range(5)) for i in range(13)]
G = gens(); dirs = [[x + y for x, y in zip(w2(mv(m, Z1), Z2), w2(Z1, mv(m, Z2)))] for m in G.values()]
for e in A: dirs.append(w2(e, Z2)); dirs.append(w2(Z1, e))
check('slice tangent rank == 23 (dense orbit saturation)', rankQ(dirs) == 23, rankQ(dirs))
Z1 = [sum(s[k] * A[k][i] for k in range(3)) for i in range(13)]; Z2 = [sum(t[k] * A[k][i] for k in range(3)) for i in range(13)]
dirs = [[x + y for x, y in zip(w2(mv(m, Z1), Z2), w2(Z1, mv(m, Z2)))] for m in G.values()]
for e in A[:3]: dirs.append(w2(e, Z2)); dirs.append(w2(Z1, e))
check('degenerate 3-dim sub-slice is NOT transversal (rank 16 < 23)', rankQ(dirs) == 16, rankQ(dirs))
pts = sl['poised_points']; monos = [(i, j) for i in range(10) for j in range(i, 10)]
def pl(s, t): return [s[i] * t[j] - s[j] * t[i] for i in range(5) for j in range(i + 1, 5)]
E = [[Fraction(pl(s, t)[i] * pl(s, t)[j]) for i, j in monos] for s, t in pts]
check('50 slice points are poised for S_22(C^5) (rank 50)', rankQ(E) == 50 and len(pts) == 50)
maxZ = max(abs(sum(s[k] * int(A[k][i]) for k in range(5))) for s, t in pts for i in range(13)); maxZ = max(maxZ, max(abs(sum(t[k] * int(A[k][i]) for k in range(5))) for s, t in pts for i in range(13)))
check('max |Z entry| on the slice == 2', maxZ == 2)
r = json.loads((HERE / 'results/p3_covariant_relation.json').read_text())
p1, p2, p3 = r['primes']['P'], r['primes']['extra'][0], r['primes']['extra'][1]
check('slice CRT modulus exceeds twice the a-priori bound', p1 * p2 > 2 * 331776 * (120 * maxZ * maxZ) ** 2)
check('Y0 CRT modulus exceeds twice the a-priori bound', p1 * p2 * p3 > 2 * 331776 * (120 * 3 ** 5) ** 2)
check('balanced float64 products exact: 4^8 * (p/2)^2 < 2^53 for every prime', all(4 ** 8 * (p // 2) ** 2 < 2 ** 53 for p in (p1, p2, p3)))
check('factorization controls at Y0 passed for q3, q7, n02', all(v['passed'] for v in r['checks']['factorization_at_Y0'].values()))
check('r_top on the slice == 3 with all 50 points', r['r_top_on_slice'] == {'rank': 3, 'points': 50, 'complete': True})
check('rank of all 18 patterns at Y0 == 3', r['rank_Q_at_Y0']['all_patterns'] == 3)
c = r['coordinates_in_basis']
check('exact coordinates: q3 = 2B(F1,F2), q7 = 2B(F3,F2), n02 = 2B(F1,F1) at Y0', c['q3_h1'] == c['q3_h1t'] == ['1/1', '0/1', '0/1'] and c['q3_h2'] == c['q3_h2t'] == c['q7_h2'] == c['q7_h2t'] == ['0/1', '1/1', '0/1'] and c['q7_h1'] == c['q7_h1t'] == ['0/1', '0/1', '1/1'] and all(c['n02_' + h] == ['-1/1', '0/1', '0/1'] for h in ('h1', 'h1t', 'h2', 'h2t')))
check('false-identity control: corrupted relation rejected', r['checks']['false_identity_rejected']['corrupted_lambda_relation_nonzero'])
S0 = [[34725, 239889, 380115], [176113, 112168, 44818], [163934, 316261, 169076], [190461, 231336, 338217], [395778, 379744, 423266], [232316, 28953, 238815]]
FULL = [[86170, 71919, 226580], [376209, 469277, 41046], [347334, 318883, 320901], [469768, 310015, 415152]]
a_, b_ = 265391, 275398
check('recorded relation holds on all 10 rows with the residues', all((a_ * r[0] + b_ * r[1] - r[2]) % P == 0 for r in S0 + FULL))
check('corrupted residues (alpha+1) are rejected', any((( a_ + 1) * r[0] + b_ * r[1] - r[2]) % P for r in S0 + FULL))
print('ALL CHECKS PASSED' if ok else 'SOME CHECKS FAILED')

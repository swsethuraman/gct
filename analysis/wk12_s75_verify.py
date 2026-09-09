#!/usr/bin/env python3
"""s75 -- independent verification of the two-part delta=12 compact control.

The dimension half (31 -> 2 through the 239-dimensional residual) and the
evaluation conversion (the four pairing scalars A, C = Gram_M^{-1} A, and the
recursive evaluations E_recursive = C^{-t} E_circuit) were constructed by
Astra session S3 (results/astra/S3/, staged on the laptop).  This script is the
s75 consumer/verifier per the batch-12 collision rule ("whoever gets C
invertible first, the other consumes it").  It checks, from first principles and
from the s69 circuit side, everything s75 is responsible for:

  1. g_tc and the two circuit permutation inversion lengths, re-derived from the
     s69 seed (results/s69_n4_seed.json) via S3's own column-superstandard Gram
     formula -- must match S3's normalization exactly.
  2. S3's native bridge at both house primes: Gram_native C = A, det C != 0,
     C^t E_recursive = E_circuit, and the determinant minor.
  3. S3's common rational source (the common-field rule): A_common = L^t A_native,
     C_common = L^{-1} C_native, det C_common != 0, common determinant minor.
  4. i_det(12) = a - rank(det evaluation) reproduced INDEPENDENTLY from the s69
     compact-circuit evaluator (analysis/wk11_s69_circuit) on the seed's own
     fillings and det_4 pencils, at both primes.

A nonzero determinant minor == mult_det = 2 == i_det(12) = 0.  Confirmed on the
circuit side (2) and carried to the recursive source by the invertible C.
"""
import sys, os, json, collections, random
from fractions import Fraction as Q
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.normpath(os.path.join(HERE, '..'))
P1, P2 = 2147483647, 2147483629


def matmul(A, B, p):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) % p for j in range(len(B[0]))]
            for i in range(len(A))]


def det2(M, p):
    return (M[0][0] * M[1][1] - M[0][1] * M[1][0]) % p


def inv2(M, p):
    d = det2(M, p); di = pow(d, p - 2, p)
    return [[M[1][1] * di % p, (-M[0][1]) * di % p], [(-M[1][0]) * di % p, M[0][0] * di % p]]


def transpose(M):
    return [[M[0][0], M[1][0]], [M[0][1], M[1][1]]]


def main():
    out = {"cell": "lambda=(17,17,2^7), delta=12, n=4, r=9, a=2", "checks": {}}
    seed = json.load(open(os.path.join(ROOT, 'results', 's69_n4_seed.json')))
    lam = tuple(seed['lam'])

    # 1. g_tc + permutation lengths from the seed
    boxes = [(r, c) for c in range(lam[0]) for r in range(len(lam)) if lam[r] > c]
    g = Q(1)
    for i, (r, c) in enumerate(boxes):
        for s, t in boxes[i + 1:]:
            if r > s:
                d = c - r - t + s; g *= Q(d - 1, d + 1)
    lens = []
    for f in seed['basis']:
        labels = f['C1'] + f['C2'] + [x for col in f['two'] for x in col] + f['one']
        used = collections.Counter(); pi = []
        for l in labels:
            pi.append(4 * l + used[l]); used[l] += 1
        lens.append(sum(pi[i] > pi[j] for i in range(48) for j in range(i + 1, 48)))
    cert = json.load(open(os.path.join(ROOT, 'results', 's75', 'S3_bridge_certificate.json')))
    g_s3 = cert['normalization']['g_tc']
    out['checks']['g_tc_matches_S3'] = (str(g) == g_s3 and g.denominator == 1)
    out['checks']['g_tc'] = str(g)
    out['checks']['perm_inversion_lengths'] = lens
    out['checks']['perm_lengths_expected'] = [579, 640]

    # 2 + 3. verify S3's native and common bridge at both primes
    bridge = {}
    for res in cert['results']:
        p = res['prime']; A = res['A_native']; G = res['Gram_native']; C = res['C_native']
        e = {}
        e['Gram_C_eq_A'] = matmul(G, C, p) == [[A[i][j] % p for j in range(2)] for i in range(2)]
        e['det_C'] = det2(C, p); e['det_C_nonzero'] = e['det_C'] != 0
        e['det_C_matches_S3'] = e['det_C'] == res['det_C_native']
        Ct = transpose(C)
        e['families'] = {}
        for fam in res['evaluations']:
            Ec, Er = fam['circuit'], fam['native_recursive']
            e['families'][fam['family']] = {
                'Ct_Erec_eq_Ecirc': matmul(Ct, Er, p) == [[Ec[i][j] % p for j in range(2)] for i in range(2)],
                'recursive_minor': det2(Er, p), 'circuit_minor': det2(Ec, p),
                'recursive_minor_nonzero': det2(Er, p) != 0, 'circuit_minor_nonzero': det2(Ec, p) != 0}
        # common-source lift
        L = res['L_common_in_native']; Ac = res['A_common']; Cc = res['C_common']
        e['A_common_eq_Lt_A'] = matmul(transpose(L), A, p) == [[Ac[i][j] % p for j in range(2)] for i in range(2)]
        e['C_common_eq_Linv_C'] = matmul(inv2(L, p), C, p) == [[Cc[i][j] % p for j in range(2)] for i in range(2)]
        e['det_C_common'] = det2(Cc, p); e['det_C_common_nonzero'] = det2(Cc, p) != 0
        for fam in res['evaluations']:
            if fam['family'] == 'det':
                e['common_det_minor'] = det2(fam['common_recursive'], p)
                e['common_det_minor_nonzero'] = det2(fam['common_recursive'], p) != 0
        bridge[str(p)] = e
    out['checks']['S3_bridge'] = bridge

    # 4. independent s69 circuit reproduction of i_det(12)
    from wk11_s69_circuit import (Filling, sym_table, symbols_from_coeffs, dp_eval_c,
                                  rank_mod, det_form, restrict, exps)
    n, r = 4, 9
    fills = [Filling(f['h'], f['n'], f['delta'], f['C1'], f['C2'], f['two'], f['one'])
             for f in seed['basis']]
    f_det, N = det_form(n)
    Amono = exps(n, r)
    det_points = [[int(restrict(f_det, N, n, r, As).get(al, 0)) for al in Amono]
                  for As in seed['det_pencils_A']]
    s69 = {}
    for p in (P1, P2):
        A, idx, fact, tab = sym_table(n, r)
        rows = [[dp_eval_c(F, symbols_from_coeffs(cv, n, r, p), p, tab) for cv in det_points] for F in fills]
        rng = random.Random(20260909 + p % 1000)
        gpts = [[rng.randrange(p) for _ in Amono] for _ in range(6)]
        grows = [[dp_eval_c(F, symbols_from_coeffs(cv, n, r, p), p, tab) for cv in gpts] for F in fills]
        rk_det = rank_mod(rows, p); rk_gen = rank_mod(grows, p)
        s69[str(p)] = {'generic_rank': rk_gen, 'det_rank': rk_det,
                       'mult_det': rk_det, 'i_det': 2 - rk_det}
    out['checks']['s69_circuit_i_det'] = s69

    # overall
    ok = (out['checks']['g_tc_matches_S3'] and lens == [579, 640]
          and all(bridge[str(p)]['Gram_C_eq_A'] and bridge[str(p)]['det_C_nonzero']
                  and bridge[str(p)]['families']['det']['Ct_Erec_eq_Ecirc']
                  and bridge[str(p)]['families']['det']['recursive_minor_nonzero']
                  and bridge[str(p)]['families']['det']['circuit_minor_nonzero']
                  and bridge[str(p)]['A_common_eq_Lt_A'] and bridge[str(p)]['C_common_eq_Linv_C']
                  and bridge[str(p)]['common_det_minor_nonzero'] for p in (P1, P2))
          and all(s69[str(p)]['i_det'] == 0 and s69[str(p)]['generic_rank'] == 2 for p in (P1, P2)))
    out['VERDICT'] = 'PASS -- i_det(12)=0; C invertible both primes; both halves of the control pass' if ok else 'FAIL'
    json.dump(out, open(os.path.join(ROOT, 'results', 's75', 'verification.json'), 'w'), indent=1)
    print(json.dumps({'VERDICT': out['VERDICT'],
                      'g_tc_matches_S3': out['checks']['g_tc_matches_S3'],
                      'perm_lengths': lens,
                      's69_i_det': {p: s69[p]['i_det'] for p in s69},
                      'det_C': {p: bridge[p]['det_C'] for p in bridge}}, indent=1))


if __name__ == '__main__':
    main()

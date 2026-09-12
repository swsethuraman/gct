"""Produce the h=1 CI control. Never imported by the independent verifier."""
from collections import Counter
from fractions import Fraction
import hashlib
import itertools as it
import json
import math
from pathlib import Path
import b13_03_exact as old

OUT = Path('results/b14_03')
P = [2147483647, 2147483629]


def bracket_value(columns, point, modulus=None):
    cubic = {tuple(a): c for a, c in point['cubic']}
    counts = [[0, 0, 0] for _ in range(12)]
    def recurse(k, sign):
        if k == len(columns):
            v = sign
            for j, a in enumerate(counts):
                if j < 6:
                    v *= point['l'][a.index(1)]
                else:
                    v *= math.prod(math.factorial(t) for t in a) * cubic[tuple(a)]
                if not v:
                    return 0
            return v if modulus is None else v % modulus
        total = 0
        col = columns[k]
        for perm in it.permutations(range(3)):
            if any(j < 6 and not point['l'][x] for j, x in zip(col, perm)):
                continue
            s = (-1) ** sum(perm[i] > perm[j] for i in range(3) for j in range(i+1, 3))
            for j, x in zip(col, perm):
                counts[j][x] += 1
            total += recurse(k+1, sign*s)
            for j, x in zip(col, perm):
                counts[j][x] -= 1
        return total if modulus is None else total % modulus
    return recurse(0, 1)


def quartic(point, E):
    d = {tuple(a): c for a, c in point['cubic']}
    return [sum(point['l'][i] * d[tuple(a[j]-(i == j) for j in range(3))]
                for i in range(3) if a[i]) for a in E]


def main():
    raw = Path('results/b13_03/primary_source.json').read_bytes()
    data, E, polys = old.load_source('results/b13_03/primary_source.json')
    old.check_hw(polys, E)
    point = {'type': 'reducible', 'l': [1, 0, 0],
             'cubic': [[list(a), c] for a, c in zip(old.exps(3, 3), [0,-1,-2,-1,-1,1,-1,3,3,0])]}
    points = [point, dict(point, l=[1, 2, 0])]
    edges = [(i, (i+1) % 6) for i in range(6)]
    columns = [[i, 6+a, 6+b] for i, (a, b) in enumerate(edges)] + [[6,7,8], [9,10,11]]
    trials = []
    # Directed candidate first, then bounded deterministic shuffled valence pool.
    import random
    rng = random.Random(1403)
    for attempt in range(64):
        if attempt:
            pool = list(range(6,12))*3
            rng.shuffle(pool)
            columns = [[i, *pool[2*i:2*i+2]] for i in range(6)] + [pool[12:15], pool[15:18]]
            if any(len(set(c)) != 3 for c in columns):
                trials.append({'attempt': attempt, 'structurally_zero': True})
                continue
        value = bracket_value(columns, point)
        trials.append({'attempt': attempt, 'value': value, 'columns': columns})
        if value:
            break
    else:
        raise RuntimeError('bounded bracket search found no nonzero candidate')
    old.write_json(OUT/'bracket_search.json', trials)
    source = [[ [list(m), str(c)] for m, c in sorted(poly.items())] for poly in polys]
    change = [[1, 1], [0, 1]]
    mixed = [{m: sum(change[i][j]*polys[j].get(m, 0) for j in range(2))
              for m in set(polys[0]) | set(polys[1])} for i in range(2)]
    coeffs = [quartic(pt, E) for pt in points]
    A = [[int(old.evaluate(poly, c)) for c in coeffs] for poly in mixed]
    H = [sum(abs(int(c)) for c in poly.values()) * max(1, *(abs(v) for x in coeffs for v in x))**6
         for poly in mixed]
    target = [[bracket_value(columns, pt) for pt in points]]
    cert = {
      'format': 'gct-cert/1', 'kind': 'complete_interpolation', 'profile': 'ternary_quartic_888_d6',
      'title': 'Complete h=1 interpolation with mixed source basis',
      'produced_by': 'B14-03 gpt-6-astra xhigh; analysis/b14_03_produce.py',
      'field': 'Q', 'cell': {'n':4,'r':3,'delta':6,'lambda':[8,8,8]},
      'conventions': {'coefficient':'ordinary', 'raising':'(alpha_i+1)c_(alpha+e_i-e_j)',
                      'bracket':'linear l_i; cubic alpha! d_alpha; no orbit averaging',
                      'orientation':'source rows; point columns; A^T K=0'},
      'points': points,
      'source': {'exponents':[list(a) for a in E], 'basis':source, 'change_of_basis':change,
                 'provenance_sha256':hashlib.sha256(raw).hexdigest(),
                 'dimension_proof': {'method':'complete_raising', 'weight_dimension':561,
                                     'raising_rank':559,'dimension':2}},
      'target': {'dimension_proof':{'method':'pieri_complete_cubic_raising','predecessors':[[8,8,2]],
                                    'weight_dimensions':[38],'raising_ranks':[37],'dimension':1},
                 'members':[{'letter_types':['linear']*6+['cubic']*6, 'columns':columns}],
                 'evaluation':{'values_are':'integral mixed bracket evaluations; target rows', 'entries':target},
                 'minor':{'rows':[0],'columns':[0],'determinant':target[0][0]}},
      'source_arithmetic': {'values_are':'A_Z = diag(row_denominators) A_Q; source rows',
                  'row_denominators':[1,1], 'entries':A, 'height_bounds':H,
                  'crt':{'values_are':'A_Z mod p; source rows; prime-keyed residue matrices',
                         'primes':P,'modulus':math.prod(P),
                         'residues':{str(p):[[v%p for v in row] for row in A] for p in P}}},
      'kernel': {'values_are':'rational coefficients in changed source basis; columns',
                 'entries':[[1],[-1]],'rank':1},
      'claim': {'source_dimension':2,'target_dimension':1,'rank_Q':1,'i_red':1}}
    old.write_json(OUT/'control.json', cert)
    print(json.dumps({'attempts':len(trials), 'target':target, 'source':A, 'bounds':H}), flush=True)


if __name__ == '__main__':
    main()

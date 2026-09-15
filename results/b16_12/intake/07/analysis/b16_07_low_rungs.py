"""Exact one-parameter necessary filtration conditions for B16 slot 07.

Run only through the inspected analysis/b15_bound.py, with -B.
This does not test determinant samples: it tests polynomial degree on ambient
quartics, for a basis of the inherited COMPLETE stable determinant ideal.
"""
from fractions import Fraction
from pathlib import Path
import argparse
import hashlib
import json
import time


# A sparse polynomial has keys (power of u, power of t) and integer values.
def add(*polys):
    ans = {}
    for poly in polys:
        for key, val in poly.items():
            ans[key] = ans.get(key, 0) + val
    return {k: v for k, v in ans.items() if v}


def scale(poly, coefficient=1, u=0, t=0):
    return {(a+u, b+t): coefficient*v for (a, b), v in poly.items()
            if coefficient*v}


def mul(left, right):
    ans = {}
    for (a, b), v in left.items():
        for (c, d), w in right.items():
            key = (a+c, b+d)
            ans[key] = ans.get(key, 0) + v*w
    return {k: v for k, v in ans.items() if v}


def divide_t(poly, divisor):
    assert divisor[(0, 4)] == 1
    assert all(b < 4 or (a, b) == (0, 4) for a, b in divisor)
    rem, quotient = dict(poly), {}
    while rem and max(b for a, b in rem) >= 4:
        power = max(b for a, b in rem)
        lead = {(a, b-4): v for (a, b), v in rem.items() if b == power}
        quotient = add(quotient, lead)
        rem = add(rem, scale(mul(lead, divisor), -1))
    assert add(mul(divisor, quotient), rem) == poly
    return quotient, rem


def determinant(matrix):
    rows = [[Fraction(x) for x in row] for row in matrix]
    value = Fraction(1)
    for j in range(len(rows)):
        k = next((k for k in range(j, len(rows)) if rows[k][j]), None)
        if k is None:
            return Fraction(0)
        if k != j:
            rows[j], rows[k] = rows[k], rows[j]
            value = -value
        pivot = rows[j][j]
        value *= pivot
        for k in range(j+1, len(rows)):
            factor = rows[k][j]/pivot
            for ell in range(j+1, len(rows)):
                rows[k][ell] -= factor*rows[j][ell]
            rows[k][j] = 0
    return value


def select_rows(labelled_rows):
    basis, chosen = {}, []
    for label, row in labelled_rows:
        vec = list(map(Fraction, row))
        for j in sorted(basis):
            if vec[j]:
                q = vec[j]
                vec = [x-q*y for x, y in zip(vec, basis[j])]
        pivot = next((j for j, val in enumerate(vec) if val), None)
        if pivot is not None:
            q = vec[pivot]
            basis[pivot] = [val/q for val in vec]
            chosen.append((label, row))
    return chosen


def encode(poly):
    return [[a, b, str(v)] for (a, b), v in sorted(poly.items())]


def evaluate(poly, u, t):
    return sum(v*u**a*t**b for (a, b), v in poly.items())


def build(binary, transverse):
    A, B, C = binary
    # G=t^4+u*(4*x1*t^3+a2*t^2+a3*t+a4), evaluated at x=e1.
    # a_d=A_d*x1^d+binom(d,2)*sum_i N_di*x1^(d-2)*xi^2.
    htt = {(0, 2): 12, (1, 1): 24, (1, 0): 2*A}
    htx = {(1, 2): 12, (1, 1): 4*A, (1, 0): 3*B}
    hxx = {(1, 2): 2*A, (1, 1): 6*B, (1, 0): 12*C}
    D = add(mul(htt, hxx), scale(mul(htx, htx), -1))
    diagonal = []
    for ai, bi, ci in transverse:
        entry = {(1, 2): 2*ai, (1, 1): 6*bi, (1, 0): 12*ci}
        diagonal.append(entry)
        D = mul(D, entry)
    p = {(0, 4): 1, (1, 3): 4, (1, 2): A, (1, 1): B, (1, 0): C}
    quotient, remainder = divide_t(D, p)
    S = [{(a, 0): v for (a, b), v in remainder.items() if b == j}
         for j in range(4)]
    # The full shear t -> t-u*x1 has determinant one. At x=e1 it is t -> t-u.
    R3 = S[3]
    R2 = add(S[2], scale(S[3], -3, u=1))
    R1 = add(S[1], scale(S[2], -2, u=1), scale(S[3], 3, u=2))
    s2 = {(1, 0): A, (2, 0): -6}
    s3 = {(1, 0): B, (2, 0): -2*A, (3, 0): 8}
    s4 = {(1, 0): C, (2, 0): -B, (3, 0): A, (4, 0): -3}
    phis = [mul(s4, R3), mul(mul(s2, s2), R3), mul(s3, R2), mul(s2, R1)]
    # Tiny exact checks against the ordinary numeric 9x9 Hessian.
    controls = []
    for u, t in [(1, 0), (2, 3), (-1, 2)]:
        H = [[0]*9 for _ in range(9)]
        H[0][0] = evaluate(htt, u, t)
        H[0][1] = H[1][0] = evaluate(htx, u, t)
        H[1][1] = evaluate(hxx, u, t)
        for i, entry in enumerate(diagonal, 2):
            H[i][i] = evaluate(entry, u, t)
        actual = determinant(H)
        expected = evaluate(D, u, t)
        assert actual == expected
        controls.append(dict(u=u, t=t, determinant=str(expected)))
    return dict(binary=binary, transverse=transverse,
                D=encode(D), p=encode(p), quotient=encode(quotient),
                remainder=encode(remainder),
                R=[encode(R1), encode(R2), encode(R3)],
                scalars=[encode(s2), encode(s3), encode(s4)],
                phis=[encode(poly) for poly in phis], controls=controls), phis


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', default='results/b16_07/pilot.json')
    args = parser.parse_args()
    start = time.perf_counter()
    # 2x2 binary block times seven diagonal entries, all authentic quartic jets.
    # A priori D has t-degree <=18, u-degree <=9; division has <=15 stages.
    # Phis have u-degree <=28. The computation has no dense ambient expansion.
    spec, phis = build([2, 3, 5], [[i+1, 2*i+1, 3*i+2] for i in range(7)])
    rows = [(k, [poly.get((k, 0), 0) for poly in phis]) for k in range(28, 14, -1)]
    constraints = []
    for degree in (14, 15):
        selected = select_rows([(k, row) for k, row in rows if k > degree])
        matrix = [row for k, row in selected]
        minor = determinant(matrix) if len(matrix) == 4 else None
        constraints.append(dict(degree=degree, partition=[4*degree-35,21]+[2]*7,
                                rank=len(selected), degrees=[k for k, row in selected],
                                matrix=[[str(x) for x in row] for row in matrix],
                                minor=str(minor) if minor is not None else None,
                                determinant_ideal_upper=4-len(selected)))
    result = dict(status='EXACT_NECESSARY_CONSTRAINTS',
                  input_model='ordinary quartic coefficients; scale every nonleading coefficient by u',
                  stable_basis=['s4*R3','s2^2*R3','s3*R2','s2*R1'],
                  specialization=spec, constraints=constraints,
                  inherited='Complete stable determinant ideal is this four-space; finite restriction is injective.',
                  elapsed_seconds=time.perf_counter()-start,
                  script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['status','constraints','elapsed_seconds']}))


if __name__ == '__main__':
    main()

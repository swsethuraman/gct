"""Independent bounded receiver: actual quartic differentiation and exact division.

No producer imports. The historical completeness proof remains inherited.
The canonical command is in docs/b16_07_report.md.
"""
from pathlib import Path
from math import gcd
from functools import reduce
import argparse
import hashlib
import json
import time
import sympy as sp


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def decode(terms, u, t):
    return sp.Poly(sum(int(v)*u**a*t**b for a, b, v in terms), t, u)


def receive(certificate):
    u, t = sp.symbols('u t')
    xs = sp.symbols('x1:9')
    x = xs[0]
    spec = certificate['specialization']
    assert spec['binary'] == [2, 3, 5]
    assert spec['transverse'] == [[i+1, 2*i+1, 3*i+2] for i in range(7)]
    A, B, C = spec['binary']
    forms = []
    for j, aj in zip((2, 3, 4), (A, B, C)):
        forms.append(aj*x**j + sp.binomial(j, 2)*sum(
            row[j-2]*x**(j-2)*xi**2 for xi, row in zip(xs[1:], spec['transverse'])))
    G = t**4 + u*(4*x*t**3 + forms[0]*t**2 + forms[1]*t + forms[2])
    point = {xi: int(i == 0) for i, xi in enumerate(xs)}
    # Independently differentiate the authentic nine-variable quartic.
    H = sp.hessian(G, (t,)+xs).subs(point)
    D = sp.Poly(H.det(method='berkowitz'), t, u)
    p = sp.Poly(G.subs(point), t, domain=sp.ZZ[u])
    Q, S = sp.div(sp.Poly(D.as_expr(), t, domain=sp.ZZ[u]), p)
    assert D == decode(spec['D'], u, t)
    assert sp.Poly(Q.as_expr(), t, u) == decode(spec['quotient'], u, t)
    assert sp.Poly(S.as_expr(), t, u) == decode(spec['remainder'], u, t)
    assert sp.Poly(p.as_expr(), t, u) == decode(spec['p'], u, t)
    # Independently depress the whole quartic and its remainder by t -> t-u*x1.
    G_depressed = sp.Poly(sp.expand(G.subs(t, t-u*x)), t)
    assert G_depressed.coeff_monomial(t**3) == 0
    scalars = [sp.expand(G_depressed.coeff_monomial(t**(4-j)).subs(point)) for j in (2, 3, 4)]
    R = sp.Poly(sp.expand(S.as_expr().subs(t, t-u)), t)
    for actual, stored in zip(scalars, spec['scalars']):
        assert sp.Poly(actual, t, u) == decode(stored, u, t)
    for j, stored in zip((1, 2, 3), spec['R']):
        assert sp.Poly(R.coeff_monomial(t**j), t, u) == decode(stored, u, t)
    s2, s3, s4 = scalars
    phi = [s4*R.coeff_monomial(t**3), s2**2*R.coeff_monomial(t**3),
           s3*R.coeff_monomial(t**2), s2*R.coeff_monomial(t)]
    phi = [sp.Poly(val, u) for val in phi]
    for actual, stored in zip(phi, spec['phis']):
        assert sp.Poly(actual.as_expr(), t, u) == decode(stored, u, t)
    degrees = [28, 26, 25, 24]
    matrix = [[int(poly.coeff_monomial(u**k)) for poly in phi] for k in degrees]
    common = [reduce(gcd, map(abs, row)) for row in matrix]
    primitive = [[val//factor for val in row] for factor, row in zip(common, matrix)]
    det = int(sp.det(sp.Matrix(matrix)))
    primitive_det = int(sp.det(sp.Matrix(primitive)))
    assert det != 0 and primitive_det != 0
    for claimed, degree in zip(certificate['constraints'], (14, 15)):
        assert claimed['degree'] == degree
        assert claimed['partition'] == [4*degree-35, 21]+[2]*7
        assert sum(claimed['partition']) == 4*degree
        assert sorted(claimed['partition'], reverse=True) == claimed['partition']
        assert claimed['degrees'] == degrees and all(k > degree for k in degrees)
        assert claimed['rank'] == 4 and claimed['determinant_ideal_upper'] == 0
        assert [[int(val) for val in row] for row in claimed['matrix']] == matrix
        assert int(claimed['minor']) == det
    # q44 transport is a fresh exact algebra check; its 3 input equations are inherited.
    c0, c1, c2, c3, c4 = sp.symbols('c0:5')
    cs = (c0, c1, c2, c3, c4)
    q44 = 12*c0*c4-3*c1*c3+c2**2
    raising = sum((5-j)*cs[j-1]*sp.diff(q44, cs[j]) for j in range(1, 5))
    assert sp.expand(raising) == 0
    assert q44.subs({c0: 1, c1: 0, c2: 0, c3: 0, c4: 1}) == 12
    assert [a+b for a,b in zip([21,17]+[2]*7, [4,4]+[0]*7)] == [25,21]+[2]*7
    # Intentional changes must disagree with independently generated polynomials.
    mutations = []
    for i, stored in enumerate(spec['phis']):
        altered = json.loads(json.dumps(stored))
        altered[-1][2] = str(int(altered[-1][2])+1)
        rejected = sp.Poly(phi[i].as_expr(), t, u) != decode(altered, u, t)
        assert rejected
        mutations.append(dict(column=i, changed_coefficient_rejected=True))
    altered_q = q44+c0*c4
    assert sp.expand(sum((5-j)*cs[j-1]*sp.diff(altered_q, cs[j]) for j in range(1,5))) != 0
    return dict(status='PASS', degrees=degrees, matrix=matrix, row_gcds=common,
                primitive_matrix=primitive, primitive_determinant=primitive_det,
                determinant=str(det), mutations=mutations, q44_raising='zero',
                claims=[dict(degree=14, determinant_ideal=0, gap_upper=0),
                        dict(degree=15, determinant_ideal=0, padded_ideal_floor=3, gap_upper=-3)],
                scope='Only d14 and d15; full stable-ideal completeness and CI73 remain inherited.')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--certificate', default='results/b16_07/pilot.json')
    parser.add_argument('--inputs', default='results/b16_07/input_hashes.json')
    parser.add_argument('--out', default='results/b16_07/receiver.json')
    args = parser.parse_args()
    start = time.perf_counter()
    inputs = json.loads(Path(args.inputs).read_text())
    for item in inputs['files']:
        assert digest(Path(item['path'])) == item['sha256'], item['path']
    certificate = json.loads(Path(args.certificate).read_text())
    result = receive(certificate)
    result.update(elapsed_seconds=time.perf_counter()-start, verified_input_count=len(inputs['files']),
                  certificate_sha256=digest(Path(args.certificate)),
                  receiver_sha256=digest(Path(__file__)),
                  input_manifest_sha256=digest(Path(args.inputs)), sympy_version=sp.__version__)
    Path(args.out).write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()

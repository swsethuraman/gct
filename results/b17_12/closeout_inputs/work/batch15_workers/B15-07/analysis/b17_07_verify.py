"""Tiny exact algebra controls for the conormal audit; no geometry is inferred by sampling.

Run only through the inspected analysis/b15_bound.py, using .venv/python.exe -B.
One process, no subprocesses, no third-party imports, no search or elimination.
"""
import hashlib
import json
from itertools import permutations
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT.parents[2]
MAX_TERMS = 16
checks = []


def poly(*terms):
    result = {}
    for coefficient, exponent in terms:
        result[exponent] = result.get(exponent, 0) + coefficient
    result = {e: c for e, c in result.items() if c}
    assert len(result) <= MAX_TERMS
    return result


def add(p, q):
    return poly(*[(c, e) for e, c in p.items()], *[(c, e) for e, c in q.items()])


def mul(p, q):
    assert len(p) * len(q) <= MAX_TERMS
    return poly(*[(c*d, tuple(a+b for a, b in zip(e, f)))
                  for e, c in p.items() for f, d in q.items()])


def scale(c, p):
    return poly(*[(c*d, e) for e, d in p.items()])


def sq(p):
    return mul(p, p)


def check(label, p, q):
    assert p == q, label
    checks.append(label)


# Exponents are (t,x,y,z); these identities hold in Z[t,x,y,z].
t, x, y, z = [poly((1, tuple(int(i == j) for i in range(4)))) for j in range(4)]
FA = add(sq(x), mul(t, mul(y, z)))
a, b, c = scale(2, x), mul(t, z), mul(t, y)
check('A: dual(gradient F) = 4t F', add(mul(t, sq(a)), scale(4, mul(b, c))), scale(4, mul(t, FA)))
FB = add(add(sq(x), mul(t, sq(y))), mul(sq(t), sq(z)))
a, b, c = scale(2, x), scale(2, mul(t, y)), scale(2, mul(sq(t), z))
check('B: dual(gradient F) = 4t^2 F', add(add(mul(sq(t), sq(a)), mul(t, sq(b))), sq(c)), scale(4, mul(sq(t), FB)))
check('A: Euler incidence = 2F', add(add(mul(x, scale(2, x)), mul(y, mul(t, z))), mul(z, mul(t, y))), scale(2, FA))
check('B: Euler incidence = 2F', add(add(mul(x, a), mul(y, b)), mul(z, c)), scale(2, FB))

# The wrong sign in A's dual does not satisfy the universal identity.
a, b, c = scale(2, x), mul(t, z), mul(t, y)
assert add(mul(t, sq(a)), scale(-4, mul(b, c))) != scale(4, mul(t, FA))
checks.append('A dual-sign mutation rejected')

# Matrix determinants for twice the quadratic-form matrices:
# A = [[2,0,0],[0,0,t],[0,t,0]] has det -2t^2;
# B = diag(2,2t,2t^2) has det 8t^3. Both are nonzero for t != 0.
one = poly((1, (0, 0, 0, 0)))


def det3(matrix):
    answer = {}
    for p in permutations(range(3)):
        inversions = sum(p[i] > p[j] for i in range(3) for j in range(i+1, 3))
        term = one
        for i in range(3):
            term = mul(term, matrix[i][p[i]])
        answer = add(answer, scale((-1)**inversions, term))
    return answer


QA = [[scale(2, one), {}, {}], [{}, {}, t], [{}, t, {}]]
QB = [[scale(2, one), {}, {}], [{}, scale(2, t), {}], [{}, {}, scale(2, sq(t))]]
check('A: quadratic determinant = -2t^2', det3(QA), scale(-2, sq(t)))
check('B: quadratic determinant = 8t^3', det3(QB), scale(8, mul(t, sq(t))))

# Projective bundle / jet exact-sequence calculation is proved in the report.
degree_segre = comb(8, 4)
c1_jet_multiple = 9 - 5
assert (degree_segre, c1_jet_multiple, degree_segre*c1_jet_multiple) == (70, 4, 280)
checks.append('det5 seventh coefficient arithmetic: (9-5)*binom(8,4)=280')

inputs = json.loads((ROOT/'results/b17_07/input_hashes.json').read_text(encoding='utf-8-sig'))
assert Path(inputs['project_root']).resolve() == PROJECT.resolve()
for entry in inputs['inputs']:
    content = (PROJECT/entry['project_relative_path']).read_bytes()
    assert len(content) == entry['bytes']
    assert hashlib.sha256(content).hexdigest() == entry['sha256'], entry['project_relative_path']
result = {
    'status': 'PASS', 'checks': checks, 'input_hashes_checked': len(inputs['inputs']),
    'maximum_polynomial_support_allowed': MAX_TERMS,
    'scope': 'Exact displayed algebra and pinned input bytes only; not a computational proof of conormal specialization, cycle multiplicities, or padding polar degrees.',
    'uncomputed': ['delta_7(per3)', 'coordinate-multiplicity bridge', 'all new padding coordinate ranks'],
}
(ROOT/'results/b17_07/verification.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
print(json.dumps(result))

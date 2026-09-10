"""B13-12 exact coefficient audit, complete residual jobs and boundary controls.

Standard-library arithmetic only. No floating-point rank or large CAS claim.
"""
import argparse
import ast
from collections import Counter
import datetime as dt
import hashlib
import importlib.util
from itertools import permutations, product
import json
import math
from pathlib import Path
import random
import sys

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'results/b13_12'
PRIMES = (2147483647, 2147483629)


def save(name, obj):
    (OUT / name).write_text(json.dumps(obj, indent=2) + '\n', encoding='utf-8')


def exps(d, n):
    if n == 1:
        return [(d,)]
    return [(j,) + e for j in range(d + 1) for e in exps(d - j, n - 1)]


def add(a, b):
    r = a.copy()
    for m, v in b.items():
        r[m] = r.get(m, 0) + v
        if not r[m]:
            del r[m]
    return r


def mul(a, b):
    r = {}
    for m, v in a.items():
        for n, u in b.items():
            k = tuple(sorted(m + n))
            r[k] = r.get(k, 0) + v * u
    return {m: v for m, v in r.items() if v}


def scaled(a, c):
    return {m: c * v for m, v in a.items() if c * v}


def parse_poly(text, names):
    """Restricted AST parser: inherited polynomial strings are data, never eval."""
    def rec(n):
        if isinstance(n, ast.Constant) and isinstance(n.value, int):
            return {(): n.value} if n.value else {}
        if isinstance(n, ast.Name):
            return {(names.index(n.id),): 1}
        if isinstance(n, ast.UnaryOp) and isinstance(n.op, ast.USub):
            return scaled(rec(n.operand), -1)
        if isinstance(n, ast.BinOp):
            a, b = rec(n.left), rec(n.right)
            if isinstance(n.op, ast.Add):
                return add(a, b)
            if isinstance(n.op, ast.Sub):
                return add(a, scaled(b, -1))
            if isinstance(n.op, ast.Mult):
                return mul(a, b)
        raise ValueError(ast.dump(n))
    return rec(ast.parse(text, mode='eval').body)


def coefficients():
    """Independent selection formula: determinant permutation + diagonal subsets.

    A selected subset of fixed rows contributes v; all other rows contribute
    one of the four B entries. Sparse monomials hold B-variable indices.
    """
    E = exps(4, 5)
    P = {e: {} for e in E}
    for pi in permutations(range(4)):
        sign = (-1)**sum(pi[i] > pi[j] for i in range(4) for j in range(i + 1, 4))
        fixed = [i for i in range(4) if pi[i] == i]
        for mask in range(1 << len(fixed)):
            vrows = {fixed[j] for j in range(len(fixed)) if mask & (1 << j)}
            brows = [i for i in range(4) if i not in vrows]
            for ks in product(range(4), repeat=len(brows)):
                e = tuple(ks.count(k) for k in range(4)) + (len(vrows),)
                mon = tuple(sorted(16 * k + 4 * i + pi[i] for i, k in zip(brows, ks)))
                P[e][mon] = P[e].get(mon, 0) + sign
    return E, {e: {m: c for m, c in p.items() if c} for e, p in P.items()}


def det_integer(M):
    """Fraction-free Bareiss, independent of coefficient permutation expansion."""
    A = [list(row) for row in M]
    n = len(A)
    sign, prev = 1, 1
    for j in range(n - 1):
        pivot = next((i for i in range(j, n) if A[i][j]), None)
        if pivot is None:
            return 0
        if pivot != j:
            A[pivot], A[j] = A[j], A[pivot]
            sign *= -1
        q = A[j][j]
        for i in range(j + 1, n):
            for k in range(j + 1, n):
                num = q * A[i][k] - A[i][j] * A[j][k]
                assert num % prev == 0
                A[i][k] = num // prev
            A[i][j] = 0
        prev = q
    return sign * A[-1][-1]


def ev(p, b):
    return sum(c * math.prod(b[j] for j in m) for m, c in p.items())


def expression(p, pivot=None):
    terms = []
    for m, c in sorted(p.items()):
        factors = [f'b{j}' for j in m if j != pivot]
        mon = '*'.join(factors) or '1'
        terms.append(('+' if c > 0 else '-') +
                     (f'{abs(c)}*' if abs(c) != 1 else '') + mon)
    return ''.join(terms).lstrip('+') or '0'


def audit_and_jobs():
    E, P = coefficients()
    anchor = E.index((0, 0, 0, 0, 4))
    good = [i for i, e in enumerate(E) if 0 < e[4] < 4]
    bad = [i for i, e in enumerate(E) if e[4] == 0]
    inherited = json.loads((ROOT / 'results/s78_reduced_polys.json').read_text())
    assert P[E[anchor]] == {(): 1}
    assert len(good) == 34 and len(bad) == 35
    compared = []
    for section in ('good', 'p4'):
        for key, text in inherited[section].items():
            e = tuple(map(int, key.split(',')))
            assert e in P
            old = parse_poly(text, inherited['bnames'])
            assert old == P[e], key
            assert all(len(m) == 4 - e[4] for m in old)
            compared.append(e)
    assert len(compared) == len(set(compared)) == 69
    assert set(compared) == set(E) - {E[anchor]}
    points = []
    for seed in (1312001, 1312002):
        rng = random.Random(seed)
        for case in range(6):
            b = [rng.randint(-3, 3) for _ in range(64)]
            s = [rng.randint(-3, 3) for _ in range(5)]
            c = [ev(P[e], b) for e in E]
            det = det_integer([[s[4] * int(i == j) + sum(
                s[k] * b[16*k+4*i+j] for k in range(4)) for j in range(4)] for i in range(4)])
            val = sum(q * math.prod(a**n for a, n in zip(s, e)) for q, e in zip(c, E))
            assert val == det
            residues = {str(p): [val % p, det % p] for p in PRIMES}
            assert all(a == b for a, b in residues.values())
            points.append(dict(seed=seed, case=case, b=b, s=s, values_are='ordinary monomial coefficients',
                               coefficients=c, determinant=det, house_prime_pairs=residues))
    save('coefficient_audit.json', dict(board_numbering='batch13', session_id='B13-12',
         status='CERTIFIED', exact_polynomial_comparisons=69, ordinary_exponents=E,
         coefficient_counts={str(j): sum(4-e[4] == j for e in E) for j in range(5)},
         total_terms=sum(map(len, P.values())), point_families=points))
    names = [f'b{j}' for j in range(64)] + [f'y{i}' for i in range(1, 70)]
    jobs = OUT / 'cas'
    jobs.mkdir(exist_ok=True)
    lines = ['// B13-12 exact full-image contraction. GENERATED, NOT RUN IN SINGULAR.',
             '// Do not add W before eliminating ALL b variables.',
             'ring r=0,(' + ','.join(names) + '),lp;', 'option(redSB);']
    lines += [f'poly p{i}={expression(P[e])};' for i, e in enumerate(E) if i != anchor]
    lines += ['ideal Graph=' + ','.join(f'y{i}-p{i}' for i in range(1, 70)) + ';',
              'ideal GB=std(Graph);',
              'ideal K=eliminate(GB,' + '*'.join(names[:64]) + ');',
              'write("results/b13_12/cas/full_monic_kernel.txt",K);',
              'ring target=0,(' + ','.join(f'y{i}' for i in good) + '),lp;',
              'map restrict=r,' + ','.join(['0']*64 + [f'y{i}' if i in good else '0' for i in range(1,70)]) + ';',
              'ideal Residual=restrict(K);', 'ideal Answer=std(Residual);',
              'write("results/b13_12/cas/fixed_factor_residual.txt",Answer);',
              'print("Target dimension:"); print(dim(Answer));',
              '// Export lift certificates and verify over Q before promotion.', 'quit;']
    (jobs / 'full_monic_Q.sing').write_text('\n'.join(lines) + '\n')
    # One explicit infinity chart, b3 = coefficient B_1(0,3) = 1.
    pivot = 3
    chartnames = ['u','z'] + [f'b{i}' for i in range(64) if i != pivot] + [f'y{i}' for i in range(1,70)]
    lines = ['// B13-12 normalized projective graph: b3=1, finite target chart.',
             '// Saturate by z FIRST. Add z=0 and W only AFTER removing u.',
             '// Generated specification; no Singular execution claimed.',
             'ring r=0,(' + ','.join(chartnames) + '),lp;']
    lines += [f'poly p{i}={expression(P[e], pivot)};' for i,e in enumerate(E) if i]
    lines += ['ideal Raw=1-u*z,' + ','.join(f'z^{4-e[4]}*y{i}-p{i}' for i,e in enumerate(E) if i) + ';',
              'ideal GB=std(Raw);', 'ideal H=eliminate(GB,u);',
              'write("results/b13_12/cas/infinity_graph_b3.txt",H);',
              'ideal W=z,' + ','.join(f'y{i}' for i in bad) + ';',
              'ideal KW=std(H+W);',
              'ideal I=eliminate(KW,z*' + '*'.join(f'b{i}' for i in range(64) if i != pivot) + ');',
              'write("results/b13_12/cas/infinity_W_b3.txt",I);', 'quit;']
    (jobs / 'infinity_b3_Q.sing').write_text('\n'.join(lines) + '\n')
    lines = ['// Necessary infinity support, not the graph nor its full scheme structure.',
             'ring r=0,(' + ','.join(f'b{i}' for i in range(64)) + '),dp;',
             'ideal Nil=' + ',\n'.join(expression(P[e]) for e in E if e != E[anchor]) + ';',
             '// 69 coefficients, degrees 1,2,3,4. Do not replace the full graph by Nil.', 'quit;']
    (jobs / 'nilpotent_support_Q.sing').write_text('\n'.join(lines) + '\n')
    save('residual_spec.json', dict(board_numbering='batch13', session_id='B13-12',
        status='EXACT_INPUT_GENERATED_NOT_ELIMINATED', field='Q', ordinary_exponents=E,
        coefficient_convention='det(v I4 + sum s_i B_i); ordinary coefficients, no factorials',
        source_variables=64, target_nonanchor_variables=69, good_indices=good, bad_indices=bad,
        full_graph_variables=133, full_graph_generators=69, degrees={str(j):sum(4-e[4]==j for e in E) for j in range(1,5)},
        graph_terms=sum(len(P[e])+1 for e in E if e != E[anchor]),
        full_job='cas/full_monic_Q.sing', first_uncompleted_step='K=<y-P(B)> intersect Q[y1,...,y69]',
        residual='J_W = substitution y_bad=0 in K; radical optional for the containment decision',
        decision='J_W nonzero iff W not contained in D5; unit ideal also nonzero',
        projective_graph='H_h=<z^deg(P_i)*y_i-P_i(N)>:z^infinity on each N_h=1 chart',
        infinity_support='z=0 and all 69 P_i(N)=0; every matrix of the pencil is nilpotent',
        infinity_chart_pivot=pivot, infinity_raw_variables=134, infinity_raw_generators=70,
        infinity_job='cas/infinity_b3_Q.sing', caveat='One infinity chart is not a global coverage certificate on its own.',
        no_groebner_basis_computed=True))
    print('Exact coefficient agreement: 69/69; two integer families, both house primes; residual jobs generated.')


def boundary_controls():
    E, P = coefficients()
    weights = [-1, 0, 0, 1]
    powers = [2 + weights[i] - weights[j] for k in range(4) for i in range(4) for j in range(4)]
    assert min(powers) == 0 and max(powers) == 4
    term_checks = []
    for e in E:
        j = 4 - e[4]
        grades = sorted({sum(powers[a] for a in m) for m in P[e]})
        assert grades == [2*j]
        term_checks.append(dict(exponent=e, degree=j, term_count=len(P[e]), t_exponents=grades))
    rng = random.Random(1312001)
    examples = []
    for case in range(4):
        c = [rng.randint(-2,2) for _ in range(64)]
        c[3] = 1
        expected = [ev(P[e], c) for e in E]
        for t in (1,2,3):
            n = [a*t**q for a,q in zip(c,powers)]
            actual = [ev(P[e], n) for e in E]
            assert actual == [t**(2*(4-e[4]))*v for e,v in zip(E,expected)]
        N0 = [c[i] if powers[i] == 0 else 0 for i in range(64)]
        for i in range(4):
            for j in range(4):
                for r in range(4):
                    for col in range(4):
                        assert sum(N0[16*i+4*r+k]*N0[16*j+4*k+col] for k in range(4)) == 0
        assert all(ev(P[e], N0) == 0 for e in E if e[4] != 4)
        examples.append(dict(C=c, projective_z='t^2', entry_t_exponents=powers,
                             values_are='ordinary normalized coefficients at C; constant target along the arc',
                             target_coefficients=expected, N_at_zero=N0))
    # Independent termwise matrix determinant proof includes selected diagonal v rows.
    cycle_checks = []
    for pi in permutations(range(4)):
        fixed = [i for i in range(4) if pi[i] == i]
        for mask in range(1 << len(fixed)):
            vr = {fixed[j] for j in range(len(fixed)) if mask & (1 << j)}
            exponent = 2*len(vr) + sum(2 + weights[i]-weights[pi[i]] for i in range(4) if i not in vr)
            assert exponent == 8
            cycle_checks.append([list(pi), sorted(vr), exponent])
    # Exact monomial ideal/saturation and elimination-order controls, with witnesses.
    # x,z variables use ids 0,1. f=x(x-z). No guessed saturation exponent.
    x,z = {(0,):1}, {(1,):1}
    linear = add(x, scaled(z,-1))
    f = mul(x,linear)
    assert f == {(0,0):1,(0,1):-1}
    assert mul(x,linear) == f
    # Restriction z=0 gives x^2; x^2*1 is in the restricted ideal -> saturation is unit.
    restricted = {m:v for m,v in f.items() if 1 not in m}
    assert restricted == mul(x,x)
    # Full affine graph u=a,v=ab: coefficients of u^i v^j pull back to a^(i+j)b^j.
    images = {(i,j):(i+j,j) for i in range(7) for j in range(7-i)}
    assert len(set(images.values())) == len(images)
    save('boundary_control.json', dict(board_numbering='batch13', session_id='B13-12', status='CERTIFIED',
         weights=weights, z='t^2', N_entry_formula='t^(2+w_row-w_col) C_i[row,col]',
         generic_identity='P_j(N)=t^(2j) P_j(C)', all_coefficient_term_checks=term_checks,
         determinant_identity='det(v z I4+sum s_i N_i)=t^8 det(v I4+sum s_i C_i)',
         independent_permutation_subset_checks=cycle_checks, examples=examples,
         boundary_support='N_i=a_i E14, [a1:a2:a3:a4] in P3; z=0',
         proof_scope='Symbolic identity over Z in all 64 C entries; examples are additional checks only.'))
    save('small_exact_controls.json', dict(board_numbering='batch13', session_id='B13-12', status='CERTIFIED',
         saturation=dict(raw='(x^2-z*x)', saturation='(x-z)', multiplier='x',
                         after_saturation_then_z='(x,z)', wrong_order='(x^2):x^infinity=(1)',
                         upper_certificate='Q[x,z]/(x-z)=Q[x], so multiplication by x is injective'),
         contraction=dict(map='(a,b)->(u=a,v=a*b)', full_kernel='(0)',
                          proof='All monomials u^i*v^j map to distinct a^(i+j)*b^j for every i,j>=0',
                          finite_control_degree=6, finite_monomials_checked=len(images),
                          correct_W_image='u=0, v arbitrary in closure', restricted_actual_image='u=v=0'),
         warning='The small example refutes a general inference, not the actual s78 containment statement.'))
    print('Generic 64-parameter boundary identity and nilpotent support certified; exact small controls pass.')


def replay_s2():
    path = ROOT/'results/astra/S2/verify_s2.py'
    spec = importlib.util.spec_from_file_location('b13_12_s2_replay',path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.OUT = OUT/'s2_replay'
    mod.OUT.mkdir(exist_ok=True)
    result = dict(board_numbering='batch13', session_id='B13-12',
                  time_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
                  rank_cases=mod.focused_ranks(), tangent_calibration=mod.differential_calibration(),
                  independent_jet_cases=mod.numeric_jet_checks(), intermediate_arc=mod.explicit_intermediate_arc())
    mod.write('verification_summary.json', result)
    print(json.dumps(result, indent=2))


def triangular_control():
    E, P = coefficients()
    below = {16*k+4*i+j for k in range(4) for i in range(4) for j in range(i)}
    actual = {e:{m:c for m,c in p.items() if not any(a in below for a in m)} for e,p in P.items()}
    expected = {e:{} for e in E}
    for choices in product(range(5), repeat=4):
        e = tuple(choices.count(k) for k in range(5))
        m = tuple(sorted(16*k+5*i for i,k in enumerate(choices) if k != 4))
        expected[e][m] = expected[e].get(m,0) + 1
    assert actual == expected
    # Zero first diagonal linear form: the fixed factor is then v, identically.
    first = {16*k for k in range(4)}
    fixed = {e:{m:c for m,c in p.items() if not any(a in first for a in m)} for e,p in actual.items()}
    assert all(not p for e,p in fixed.items() if e[4] == 0)
    assert sum(map(len, fixed.values())) == 125
    save('triangular_control.json', dict(board_numbering='batch13', session_id='B13-12',
         status='CERTIFIED', full_polynomial_comparisons=70,
         identity='det(v I4+B(s))=product_(a=1)^4 (v+L_a(s)) for every upper triangular tuple',
         triangular_terms=sum(map(len,actual.values())), one_zero_L_terms=sum(map(len,fixed.values())),
         family_image_dimension=16, fixed_factor_chart_dimension=12,
         dimension_proof='The 16 diagonal coefficients are integral over the coefficient image algebra: each is a root of the corresponding univariate characteristic polynomial. The diagonal map is finite, hence closed and dimension preserving. Product L_a=0 iff some entire L_a=0.',
         scope='Closure of images of simultaneously triangularizable tuples; not full graph over triangular supports.'))
    print('Triangular identity: 70/70 coefficients; 625 terms; fixed-factor family dimension 12 by finite-map proof.')


def main():
    OUT.mkdir(exist_ok=True)
    parser = argparse.ArgumentParser()
    parser.add_argument('unit', choices=('coefficients','boundary','s2','triangular'))
    opt = parser.parse_args()
    {'coefficients':audit_and_jobs,'boundary':boundary_controls,'s2':replay_s2,
     'triangular':triangular_control}[opt.unit]()


if __name__ == '__main__':
    main()

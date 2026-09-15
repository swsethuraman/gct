"""Bounded independent degree-23 equation receiver; see docs/b16_03_proof.md.

Commands: preflight; produce; verify. Invoke through b15_bound.py with
--seconds 60 --memory-mb 512, python -B, and a fresh b16_03 receipt name.
"""
import argparse
import hashlib
import json
from pathlib import Path
import random
import sys
import time
from fractions import Fraction as Q
import b16_03_equation as E

HERE = Path(__file__).resolve().parents[1]
OUT = HERE/'results/b16_03'


def certificate():
    started = time.perf_counter()
    B, T = E.symbolic_recurrence()
    symbolic = dict(variables=['c','a1','a2','a3','a4'],
                   B=[[[list(e), v] for e, v in sorted(p.items())] for p in B],
                   T=[[[list(e), v] for e, v in sorted(p.items())] for p in T],
                   T_supports=[len(p) for p in T], coefficient_degree=23,
                   weight=[61,15]+[2]*8, all_monomial_degree_and_weight_checks=True)
    tried = []
    # At most four independently generated full source maps; stop at first nonzero.
    for seed in range(160303, 160307):
        rng = random.Random(seed)
        L = [[rng.randrange(-2, 3) for j in range(10)] for i in range(10)]
        detL = E.determinant(L)
        assert detL
        G = E.quartic_from_products(E.padding_terms(L))
        assert len(G) <= 715
        point = E.equation(G)
        tried.append(dict(seed=seed, determinant=detL, c=point['g'][4], value=point['P']))
        if point['g'][4] and point['P']:
            break
    else:
        raise AssertionError('No nonzero within the fixed four-map control; stop, do not expand search')
    assert Q(point['P']).denominator == 1
    # Independent Hessian/source route; different complete interpolation nodes.
    srcvalues = []
    for t in range(-10, 11):
        y = [row[0]*t + row[1] for row in L]
        Hsrc, C, HC = E.natural_padding_hessian(y)
        # The source derivative Euler identity is checked without inversion.
        assert all(sum(HC[i][j]*y[j+1] for j in range(9)) == 2*Hsrc[0][i+1] for i in range(9))
        hdet = E.determinant(Hsrc)
        assert 2*hdet == -3*y[0]**8*C*E.determinant(HC)
        if t in (-3, 0, 4):
            assert E.pullback(Hsrc, L) == E.hessian_at(point['H'], t)
        assert E.evaluate(point['g'], t) == y[0]*C
        srcvalues.append(detL**2*hdet)
    srcD = E.interpolate(srcvalues, -10)
    assert srcD == point['D']
    srcrem = E.remainder(srcD, E.multiply(point['g'], point['g']))
    assert point['P'] == point['g'][4]**13*srcrem[7] != 0
    # Complete normalization/depression from every cubic-in-t coefficient.
    F, a1 = E.depress(G)
    normalized = E.equation(F)
    assert normalized['g'][4] == 1 and normalized['g'][3] == 0
    assert point['P'] == point['g'][4]**23 * normalized['remainder'][7]
    # Negative controls exercise recurrence and data consistency.
    bad = list(srcD)
    bad[7] += 1
    assert E.exported_value(point['g'], bad)[0] != point['P']
    # Upper unipotent generators, plus all first-row shears at once.
    shear_values = []
    for i in range(9):
        v = E.equation(E.shear(G, i, i+1, 1))['P']
        assert v == point['P']
        shear_values.append(v)
    # A non-upper shear should generally change the value: detect direction errors.
    opposite = E.equation(E.shear(G, 1, 0, 1))['P']
    assert opposite != point['P']
    scaled = {key: v*2**key[0]*3**key[1]*5**key[2] for key,v in G.items()}
    torus_value = E.equation(scaled)['P']
    assert torus_value == point['P']*2**61*3**15*5**2
    scalar_value = E.equation({key: 2*v for key,v in G.items()})['P']
    assert scalar_value == 2**23*point['P']
    # Extension at c=0 uses the polynomial circuit, compared with 24 full
    # degree-23 parameter interpolation values. No specialization proof claim.
    leading_key = (4,)+(0,)*9
    c = point['g'][4]
    zero_c = dict(G)
    zero_c.pop(leading_key, None)
    at_zero = E.equation(zero_c)
    parameter_values = []
    for u in range(1, 25):
        changed = dict(zero_c)
        changed[leading_key] = Q(u)
        parameter_values.append(E.equation(changed)['P'])
    parameter_polynomial = E.interpolate(parameter_values, 1)
    assert parameter_polynomial[0] == at_zero['P']
    # One fresh arbitrary noncommuting det4 pencil: implementation control only.
    rng = random.Random(160323)
    matrices = [[[rng.randrange(-2, 3) for j in range(4)] for i in range(4)] for k in range(10)]
    singular_matrices = [[list(row) for row in M] for M in matrices]
    singular_control = E.equation(E.quartic_from_products(E.determinant_terms(matrices)))
    assert singular_control['g'][4] == 0 and singular_control['P'] == 0
    # The original deterministic random leading matrix is singular. Keep it as
    # a boundary control and choose an explicitly invertible leading matrix for
    # the chart/remainder control; no blind resampling.
    matrices[0] = [[(i+1)*int(i == j) for j in range(4)] for i in range(4)]
    assert any(sum(matrices[0][i][k]*matrices[1][k][j]-matrices[1][i][k]*matrices[0][k][j]
                   for k in range(4)) for i in range(4) for j in range(4))
    detG = E.quartic_from_products(E.determinant_terms(matrices))
    detpoint = E.equation(detG)
    assert detpoint['g'][4] and detpoint['P'] == 0, (detpoint['g'], detpoint['P'])
    assert not any(detpoint['remainder'])
    saved = dict(status='PASS_EXACT_ARITHMETIC_WITH_GLOBAL_PROOF_IN_DOCS',
                 symbolic=symbolic,
                 padding=dict(seed=seed, source_order=['z']+['X%d%d'%(i,j) for i in range(1,4) for j in range(1,4)],
                              map=L, map_determinant=detL, tried=tried, quartic=E.encode_quartic(G),
                              primary=point, independent_nodes=list(range(-10,11)), independent_values=srcvalues,
                              independent_D=srcD, independent_remainder=srcrem,
                              original_a1_linear_form=a1, normalized=normalized),
                 controls=dict(upper_adjacent_shear_values=shear_values, opposite_shear_value=opposite,
                               torus_scalings=[2,3,5]+[1]*7, torus_value=torus_value,
                               scalar_value=scalar_value, modified_D7_rejected=True,
                               zero_c_value=at_zero['P'], c_parameter_interpolation=parameter_polynomial,
                               c_parameter_nodes=list(range(1,25)),c_parameter_values=parameter_values),
                 determinant=dict(seed=160323, matrices=matrices, primary=detpoint,
                                  singular_leading_matrices=singular_matrices,
                                  singular_leading_control=singular_control,
                                  global_vanishing_evidence='Proof, not this zero control'),
                 claims=dict(degree=23, highest_weight=[61,15]+[2]*8,
                             determinant_ideal_floor=1, padding_coordinate_floor=1,
                             padding_nonzero_direction_in_determinant_ideal=True,
                             positive_gap=False,
                             finite_ambient='See separate finite_comparison.json; not counted by this equation receiver'))
    return E.encode(saved), time.perf_counter()-started


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['preflight','produce','verify'])
    args = parser.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    if args.mode == 'preflight':
        B, T = E.symbolic_recurrence()
        sizing = dict(quartic_monomials_max=715, hessian_size=10, hessian_degree_in_t=2,
                      determinant_degree_in_t_max=20, complete_nodes=21,
                      dense_degree23_coefficient_expansion=False,
                      T_supports=[len(p) for p in T], T_total_terms=sum(map(len,T)),
                      max_initial_padding_maps=4, processes=1, numerical_threads=1,
                      cap_seconds=60, cap_memory_MiB=512,
                      estimate_seconds=20, estimate_MiB=100,
                      note='Small exact 10x10 determinants only; estimates precede measurement')
        (OUT/'sizing.json').write_text(json.dumps(sizing, indent=2)+'\n')
        print(json.dumps(sizing))
        return
    saved, elapsed = certificate()
    target = OUT/'certificate.json'
    if args.mode == 'produce':
        target.write_text(json.dumps(saved, indent=2)+'\n')
    else:
        assert saved == json.loads(target.read_text()), 'Certificate mismatch'
    receipt = dict(mode=args.mode, status='PASS', seconds=elapsed,
                   certificate_sha256=hashlib.sha256(target.read_bytes()).hexdigest(),
                   padding_value=saved['padding']['primary']['P'],
                   map_determinant=saved['padding']['map_determinant'],
                   degree=23, weight=[61,15]+[2]*8)
    finite_path = OUT/'finite_comparison.json'
    if finite_path.exists():
        finite = json.loads(finite_path.read_text())
        assert finite['degree'] == 23 and finite['lambda'] == [61,15]+[2]*8
        assert finite['a'] == 189 and finite['padding_coordinate_upper'] == 158
        assert finite['determinant_ideal_upper'] == 11
        assert finite['padded_ideal_lower'] == finite['a']-finite['padding_coordinate_upper']
        assert finite['D_upper'] == finite['determinant_ideal_upper']-finite['padded_ideal_lower'] == -20
        assert finite['ambient_count_independently_recomputed_by_03'] is False
        receipt['received_finite_comparison'] = 'PASS_ARITHMETIC_WITH_INHERITED_COUNT_AND_BOUNDS'
    (OUT/('receiver_'+args.mode+'.json')).write_text(json.dumps(receipt, indent=2)+'\n')
    print(json.dumps(receipt))


if __name__ == '__main__':
    main()

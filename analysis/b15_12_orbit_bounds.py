"""Exact B15-12 character pilot and independent-padding controls.

The beta-number Murnaghan--Nakayama step follows the banked
wk8_s30_pleth.py routine; the bounded cache, certificate and independent
Jacobi--Trudi permutation-character verifier are new gpt-6-astra work.
No geometric determinant rank is computed here.
"""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import permutations
import json
from math import factorial
from pathlib import Path
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'analysis'))
sys.path.insert(0, str(ROOT / 'tools/integrate'))
from wk8_s30_pleth import parts, zr, chi as banked_chi, pleth_p
from exclusion_predicates import conclusions_for

OUT = ROOT / 'results/b15_12'
INPUTS = [
    'results/b15_prep/candidate_preflight.json',
    'results/b15_prep/small_panel_sizing.json',
    'results/b15_prep/Q1_combined_bound.json',
    'results/b14_12/b14_12.json',
    'results/integrate/inherited_exclusions.json',
    'results/b15_prep/transport_overlay.json',
    'docs/batch15/ACCEPTED_STATE.md',
    'analysis/wk8_s30_pleth.py', 'analysis/wk8_s30_core.py',
    'analysis/wk13_b13_05_bound.py', 'analysis/b15_bound.py',
]


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def write(name, value):
    OUT.mkdir(parents=True, exist_ok=True)
    p = OUT / name
    p.write_text(json.dumps(value, indent=2) + '\n', encoding='utf-8')
    assert p.stat().st_size < 5_000_000


def transpose(lam):
    return tuple(sum(x > j for x in lam) for j in range(lam[0])) if lam else ()


def sign(rho):
    return (-1) ** (sum(rho) - len(rho))


@lru_cache(maxsize=4096)
def hook_dimension(lam):
    den = 1
    for i, width in enumerate(lam):
        for j in range(width):
            den *= width - j + sum(row > j for row in lam[i + 1:])
    return factorial(sum(lam)) // den


@lru_cache(maxsize=200000)
def character(lam, rho):
    if not rho:
        return int(not lam)
    if rho[0] == 1:
        return hook_dimension(lam)
    r, rest, length = rho[0], rho[1:], len(lam)
    beta = tuple(lam[j] + length - 1 - j for j in range(length))
    bs, total = set(beta), 0
    for b in beta:
        nb = b - r
        if nb < 0 or nb in bs:
            continue
        height = sum(nb < x < b for x in beta)
        new = sorted([x for x in beta if x != b] + [nb], reverse=True)
        mu = tuple(x - length + 1 + j for j, x in enumerate(new))
        mu = tuple(x for x in mu if x)
        total += (-1) ** height * character(mu, rest)
    return total


@lru_cache(maxsize=100000)
def permutation_character(capacities, rho):
    """Trace on ordered set partitions: assign each labelled cycle to a bin."""
    if not rho:
        return int(not any(capacities))
    length = rho[0]
    total = 0
    for j, capacity in enumerate(capacities):
        if capacity >= length:
            nxt = list(capacities)
            nxt[j] -= length
            # Equal bins remain distinct; repeated terms are intentionally added.
            total += permutation_character(tuple(sorted(nxt, reverse=True)), rho[1:])
    return total


def jt_character(lam, rho):
    """Jacobi--Trudi determinant in h, followed by induced-character traces."""
    total = 0
    for perm in permutations(range(len(lam))):
        alpha = tuple(lam[i] - i + perm[i] for i in range(len(lam)))
        if min(alpha, default=0) < 0:
            continue
        parity = sum(perm[i] > perm[j] for i in range(len(perm))
                     for j in range(i + 1, len(perm)))
        total += (-1) ** parity * permutation_character(tuple(sorted(alpha, reverse=True)), rho)
    return total


def square_type(rho):
    out = []
    for r in rho:
        out.extend([r // 2, r // 2] if r % 2 == 0 else [r])
    return tuple(sorted(out, reverse=True))


def contract(lam_values, rect_values, rect_square_values, sizes, group_order):
    numerator = sum(s * a * b * b for s, a, b in zip(sizes, lam_values, rect_values))
    trace_num = sum(s * a * b for s, a, b in zip(sizes, lam_values, rect_square_values))
    assert numerator % group_order == trace_num % group_order == 0
    g, trace = numerator // group_order, trace_num // group_order
    assert (g + trace) % 2 == 0 and (g - trace) % 2 == 0
    symmetric, exterior = (g + trace) // 2, (g - trace) // 2
    assert g >= 0 and symmetric >= 0 and exterior >= 0
    return dict(rectangular_orbit_ub=g, symmetric_orbit_ub=symmetric,
                exterior_coefficient=exterior, flip_trace=trace,
                rectangular_numerator=str(numerator), flip_trace_numerator=str(trace_num),
                group_order=str(group_order))


def character_controls():
    checks = 0
    for size in range(1, 7):
        ps = parts(size)
        rows = {}
        for lam in ps:
            row = []
            for rho in ps:
                x = character(lam, rho)
                assert x == banked_chi(lam, rho) == jt_character(lam, rho)
                assert character(transpose(lam), rho) == sign(rho) * x
                row.append(x)
                checks += 1
            rows[lam] = row
            assert row[-1] == hook_dimension(lam)
        order = factorial(size)
        sizes = [order // zr(rho) for rho in ps]
        assert sum(sizes) == order
        for a in ps:
            for b in ps:
                assert sum(s*x*y for s,x,y in zip(sizes,rows[a],rows[b])) == order*int(a==b)
        for rect in ps:
            squares = [character(rect, square_type(rho)) for rho in ps]
            for lam in ps:
                contract(rows[lam], rows[rect], squares, sizes, order)
    # Actual nonzero and zero controls independent of any research-cell rank.
    assert character((2, 1), (3,)) == -1
    assert character((2, 1), (2, 1)) == 0
    assert character((1, 1), (2,)) == -1
    # Removing rim-hook parity gives +1 for the sign representation at (2).
    defective_sign_value = 1
    assert defective_sign_value != jt_character((1, 1), (2,))
    defective_class_norm = Fraction(sum(factorial(6)//zr(r) for r in parts(6)), factorial(6)+1)
    assert defective_class_norm != 1
    return dict(status='EXACT', independent_JT_character_values=checks,
                symmetric_groups=list(range(1, 7)), full_weighted_orthogonality=True,
                all_small_symmetric_exterior_integrality=True,
                transpose_sign_checked=True, rim_hook_sign_defect_detected=True,
                class_normalization_defect_detected=True)


def derivative_matrix(poly, variables):
    derivatives = []
    for v in range(variables):
        deriv = {}
        for exponent, coefficient in poly.items():
            if exponent[v]:
                new = list(exponent)
                new[v] -= 1
                deriv[tuple(new)] = coefficient * exponent[v]
        derivatives.append(deriv)
    monomials = sorted(set().union(*(d.keys() for d in derivatives)))
    rows = [[d.get(m, 0) for m in monomials] for d in derivatives]
    return rows, monomials


def padding_controls():
    from flint import fmpz_mat
    from wk8_s30_core import per_padded, per_form, det_form
    independent, variables = per_padded(3, 4)
    assert variables == 10
    # Independently reconstruct from the six permutations, z first, row-major x.
    construction = {}
    for p in permutations(range(3)):
        exponent = [0] * 10
        exponent[0] = 1
        for i, j in enumerate(p):
            exponent[1 + 3 * i + j] = 1
        construction[tuple(exponent)] = 1
    assert construction == independent
    rows, mons = derivative_matrix(independent, 10)
    assert fmpz_mat(rows).rank() == 10
    selected = []
    for i, row in enumerate(rows):
        eligible = [j for j,c in enumerate(row) if c == 1 and
                    all(rows[k][j] == 0 for k in range(10) if k != i)]
        assert eligible
        selected.append(eligible[0])
    minor = [[row[j] for j in selected] for row in rows]
    assert int(fmpz_mat(minor).det()) == 1
    inside = {}
    for e, c in independent.items():
        v = list(e[1:])
        v[0] += e[0]
        inside[tuple(v)] = inside.get(tuple(v), 0) + c
    irows, imons = derivative_matrix(inside, 9)
    assert fmpz_mat(irows).rank() == 9
    det, nv = det_form(4)
    drows, _ = derivative_matrix(det, nv)
    assert fmpz_mat(drows).rank() == 16
    # Corrupting the committed selected derivative coefficient must fail the minor.
    defective = [r[:] for r in minor]
    defective[0][0] = 0
    assert fmpz_mat(defective).det() == 0
    return dict(status='EXACT', field='Q', variables=['z']+[f'x{i+1}{j+1}' for i in range(3) for j in range(3)],
                polynomial=[dict(exponent=list(e), coefficient=c) for e,c in sorted(independent.items())],
                ordinary_coefficient_convention=True, derivative_matrix_rows=rows,
                cubic_columns=[list(m) for m in mons], minor_column_indices=selected,
                minor=minor, minor_determinant=1, independent_essential_variables=10,
                inside_essential_variables=9, determinant_essential_variables=16,
                corrupted_minor_rejected=True,
                scope='Subspace-variety separation only; no determinant multiplicity gap')


def cells():
    panel = json.loads((ROOT / INPUTS[0]).read_text())
    q1 = json.loads((ROOT / INPUTS[2]).read_text())
    ledger = json.loads((ROOT / 'results/integrate/inherited_exclusions.json').read_text())
    out = []
    raw = panel['small_multiplicity_panel'][:4] + panel['a1_panel'][:2] + [q1]
    for i, r in enumerate(raw):
        c = dict(n=4, delta=r['delta'], lam=r['lam'], ambient_multiplicity=r['a'],
                 h_pad_ub=r.get('h_pad', r.get('h_pad_upper')),
                 determinant_rank_lb=4 if i == 6 else 0,
                 determinant_floor_evidence='B14-12 inherited, not replayed' if i == 6 else 'trivial zero',
                 L_pad_lb=3 if i == 6 else 0,
                 role='known_control' if i == 6 else 'pilot')
        c['U_pad_ub'] = min(c['ambient_multiplicity'], c['h_pad_ub'], c['ambient_multiplicity']-c['L_pad_lb'])
        key = dict(n=4, delta=c['delta'], ell=len(c['lam']), **{'lambda':c['lam']})
        c['ledger_conclusions'] = conclusions_for(ledger, key, 'quartic_padded_gap')
        c['accepted_overlay'] = 'No tail transport entry applies at degree 7 or 8; Q1 control is already closed.'
        out.append(c)
    assert len(out) == 7 and all(sum(c['lam']) == 4*c['delta'] for c in out)
    return out


def sizing():
    sizes = []
    for degree in (7, 8):
        ps = parts(4 * degree)
        sizes.append(dict(delta=degree, symmetric_group_degree=4*degree,
                          conjugacy_classes=len(ps), class_parts=sum(map(len,ps)),
                          cache_entry_cap=200000,
                          cache_memory_estimate_bytes=200000*1024,
                          estimate_method='conservative 1 KiB per cached shape/type/value triple; Job Object is the hard limit',
                          character_rows=3 if degree == 7 else 6))
    return dict(status='EXACT', cells=cells(), counts=sizes,
                heavy_lease='NOT_HELD', full_pilot_not_started=True,
                carrier_allocated=False, intended_wall_cap_seconds=900,
                intended_aggregate_memory_mb=1536)


def pilot():
    pilot_cells = cells()
    class_files = []
    timing = []
    for degree in (7, 8):
        start = time.perf_counter()
        n = 4 * degree
        ps = parts(n)
        order = factorial(n)
        sizes = [order // zr(rho) for rho in ps]
        assert sum(sizes) == order
        rect = (degree,) * 4
        rect_values = [character(rect, rho) for rho in ps]
        square_values = [character(rect, square_type(rho)) for rho in ps]
        assert sum(s*x*x for s,x in zip(sizes,rect_values)) == order
        assert sum(s*x for s,x in zip(sizes,square_values)) == order  # Frobenius--Schur = 1
        rect_time = time.perf_counter() - start
        chosen = [c for c in pilot_cells if c['delta'] == degree]
        values = {}
        for c in chosen:
            t0 = time.perf_counter()
            lam = tuple(c['lam'])
            row = [character(lam, rho) for rho in ps]
            assert sum(s*x*x for s,x in zip(sizes,row)) == order
            assert row[-1] == hook_dimension(lam)
            c['character_seconds'] = time.perf_counter() - t0
            t0 = time.perf_counter()
            c.update(contract(row, rect_values, square_values, sizes, order))
            c['contraction_seconds'] = time.perf_counter() - t0
            # Banked ambient input re-evaluated only at this one shape.
            t0 = time.perf_counter()
            amb = sum(v * character(lam, rho) for rho,v in pleth_p(degree,4).items())
            assert amb.denominator == 1 and amb == c['ambient_multiplicity']
            c['ambient_recount_seconds'] = time.perf_counter() - t0
            c['ambient_recount'] = int(amb)
            c['U_det_ub'] = min(int(amb), c['symmetric_orbit_ub'])
            assert c['determinant_rank_lb'] <= c['U_det_ub']
            c['useful_below_ambient'] = c['symmetric_orbit_ub'] < amb
            c['useful_below_U_pad'] = c['U_det_ub'] < c['U_pad_ub']
            c['status'] = 'EXACT'
            values[lam] = row
            print(json.dumps({k:c[k] for k in ('delta','lam','rectangular_orbit_ub','symmetric_orbit_ub','U_det_ub','character_seconds')}), flush=True)
        for a in values:
            for b in values:
                assert sum(s*x*y for s,x,y in zip(sizes,values[a],values[b])) == order*int(a==b)
        # Complete character rows, class sizes and squared-cycle characters, split below 5MB.
        for shard_start in range(0, len(ps), 1000):
            records = []
            for j in range(shard_start, min(shard_start + 1000, len(ps))):
                records.append(dict(rho=ps[j], z=zr(ps[j]), class_size=sizes[j],
                                    rectangle_character=rect_values[j], rectangle_squared_cycle_character=square_values[j],
                                    lambda_characters=[values[tuple(c['lam'])][j] for c in chosen]))
            name = f'classes_d{degree}_{shard_start//1000:02d}.json'
            write(name, dict(delta=degree, rectangle=rect, lambdas=[c['lam'] for c in chosen], rows=records))
            class_files.append(dict(path=name, sha256=digest(OUT/name)))
        timing.append(dict(delta=degree, classes=len(ps), rectangle_character_seconds=rect_time,
                           total_seconds=time.perf_counter()-start, cache=character.cache_info()._asdict()))
        write('pilot_checkpoint.json', dict(status='EXACT', completed_through_delta=degree, cells=pilot_cells,
                                           class_files=class_files, timing=timing))
        character.cache_clear()
    write('pilot.json', dict(status='EXACT', model='gpt-6-astra', cells=pilot_cells,
                            class_files=class_files, timing=timing,
                            orbit_formula='m_closure <= sk(lambda,(delta^4)) <= g(lambda,(delta^4),(delta^4))',
                            conclusion='No useful bound in seven cells; broad sweep stopped' if not any(c['useful_below_ambient'] for c in pilot_cells) else 'Useful bounds require review'))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['controls', 'sizing', 'pilot'])
    args = parser.parse_args()
    if args.mode == 'controls':
        import numpy, flint
        write('controls.json', dict(model='gpt-6-astra', numpy=numpy.__version__, flint=flint.__version__,
                                   character=character_controls(), padding=padding_controls()))
        print('Exact character and padding controls PASS', flush=True)
    elif args.mode == 'sizing':
        value = sizing()
        write('sizing.json', value)
        print(json.dumps(value), flush=True)
    else:
        pilot()
    write('input_hashes.json', {p:digest(ROOT/p) for p in INPUTS})


if __name__ == '__main__':
    main()

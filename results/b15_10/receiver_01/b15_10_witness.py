"""Portable integral epsilon contraction; standard library only.

New B15-10 implementation by gpt-6-astra. No native raising operator is used.
The exact source and its highest-weight proof are in docs/b15_10_proved.md.
"""
import argparse
from collections import defaultdict
from itertools import permutations, product
import json
from math import comb, factorial, prod
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parents[1]
PRIMES = (2147483647, 2147483629)


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sign(p):
    return -1 if sum(p[i] > p[j] for i in range(len(p))
                     for j in range(i + 1, len(p))) % 2 else 1


def polynomial_product(a, b):
    out = defaultdict(int)
    for x, u in a.items():
        for y, v in b.items():
            out[tuple(i + j for i, j in zip(x, y))] += u * v
    return {x: u for x, u in out.items() if u}


def pencil_coefficients(pencil, permanent=False):
    """Ordinary coefficients of det_n(sum x_i A_i), exactly over Z."""
    r = len(pencil)
    require(1 <= r <= 8, 'pencil dimension bound')
    n = len(pencil[0])
    require(1 <= n <= 4, 'matrix size bound')
    require(all(len(a) == n and all(len(row) == n and
                all(type(x) is int and abs(x) <= 10**6 for x in row)
                for row in a) for a in pencil), 'integer pencil shape')
    require(factorial(n) * r**n <= 100000, 'expansion bound exceeded')
    units = [tuple(int(j == i) for j in range(r)) for i in range(r)]
    out = defaultdict(int)
    for p in permutations(range(n)):
        term = {(0,) * r: 1 if permanent else sign(p)}
        for j in range(n):
            term = polynomial_product(term, {units[i]: pencil[i][j][p[j]]
                                            for i in range(r) if pencil[i][j][p[j]]})
        for a, v in term.items():
            out[a] += v
    return {a: v for a, v in out.items() if v}


def tensor(coeffs, r, normalized=True):
    """t_ijkl = alpha! c_alpha = 4! times the symmetric quartic tensor."""
    out = {}
    for ijkl in product(range(r), repeat=4):
        a = tuple(ijkl.count(i) for i in range(r))
        out[ijkl] = coeffs.get(a, 0) * (prod(factorial(e) for e in a)
                                      if normalized else 1)
    return out


def sizing(r):
    require(1 <= r <= 6, 'contraction dimension bound')
    return dict(method='exact subset dynamic-programming state count',
                states_ub=sum(comb(r, k)**3 for k in range(r + 1)),
                live_layer_states_ub=max(comb(r, k)**3 for k in range(r + 1)),
                transitions_ub=sum(comb(r, k)**3 * (r-k)**3 for k in range(r)),
                tensor_entries=r**4, naive_terms=factorial(r)**3)


def hyperdet(t, r):
    """sum_{sigma,tau,upsilon} signs * prod_i t[i,sigma(i),tau(i),upsilon(i)].

    Equal to the four-epsilon contraction / r!, by permuting identical letters.
    The recurrence never creates the symbolic coefficient expansion.
    """
    sizes = sizing(r)
    require(sizes['live_layer_states_ub'] <= 8000, 'state bound exceeded')
    states = {(0, 0, 0): 1}
    steps = []
    choices = {mask: [(j, 1 << j, -1 if (mask >> (j+1)).bit_count() % 2 else 1)
                      for j in range(r) if not mask & (1 << j)]
               for mask in range(1 << r)}
    for i in range(r):
        nxt = defaultdict(int)
        attempts = 0
        for (a, b, c), value in states.items():
            for j, jb, js in choices[a]:
                for k, kb, ks in choices[b]:
                    for l, lb, ls in choices[c]:
                        v = t[i, j, k, l]
                        if v:
                            nxt[a | jb, b | kb, c | lb] += value * js * ks * ls * v
                            attempts += 1
        states = {key: value for key, value in nxt.items() if value}
        steps.append(dict(layer=i+1, states=len(states), nonzero_transitions=attempts))
    return states.get(((1 << r)-1,) * 3, 0), steps


def brute_hyperdet(t, r, signed=True):
    require(factorial(r)**3 <= 200000, 'direct permutation expansion bound')
    ps = [(p, sign(p) if signed else 1) for p in permutations(range(r))]
    return sum(a*b*c*prod(t[i, p[i], q[i], s[i]] for i in range(r))
               for p, a in ps for q, b in ps for s, c in ps)


def skew_pencil():
    """Pfaffian = x0^2-x5^2+x1^2-x4^2+x2^2-x3^2."""
    out = [[[0]*4 for _ in range(4)] for _ in range(6)]
    entries = {(0, 1): {0: 1, 5: 1}, (2, 3): {0: 1, 5: -1},
               (0, 2): {1: 1, 4: 1}, (1, 3): {1: -1, 4: 1},
               (0, 3): {2: 1, 3: 1}, (1, 2): {2: 1, 3: -1}}
    for (i, j), linear in entries.items():
        for k, value in linear.items():
            out[k][i][j] = value
            out[k][j][i] = -value
    return out


def source_spec():
    return dict(kind='integral_four_epsilon_over_factorial',
                labels=list(range(6)), columns=[list(range(6)) for _ in range(4)],
                tensor='t_ijkl = product(alpha_j!) * ordinary_c_alpha',
                contraction_divisor=720, c400000_power=2,
                orientation='each column ordered by labels 0,1,2,3,4,5',
                convention='Sym^8(Sym^4 V); E_i,i+1 c_alpha = (alpha_i+1)c_(alpha+e_i-e_i+1)')


def verify(cert):
    require(cert['format'] == 'b15-10-integral-bracket/1', 'format')
    require(cert['cell'] == dict(n=4, delta=8, ell=6, ambient_variables=16,
                                partition=[12,4,4,4,4,4]), 'cell')
    require(cert['source'] == source_spec(), 'source definition / normalization')
    require(cert['point']['family'] == 'det4_integer_pencil', 'point family')
    coeffs = pencil_coefficients(cert['point']['pencil'])
    require(len(cert['point']['pencil']) == 6, 'six-variable restriction')
    entries = [[list(a), v] for a, v in sorted(coeffs.items())]
    require(entries == cert['ordinary_coefficients'], 'geometric coefficient mismatch')
    h, steps = hyperdet(tensor(coeffs, 6), 6)
    value = coeffs.get((4,0,0,0,0,0), 0)**2 * h
    require(value == int(cert['minor_Z']) and value != 0, 'nonzero minor mismatch')
    require(cert['minor_mod_p'] == {str(p): value % p for p in PRIMES}, 'residues')
    require(cert['minor_shape'] == [1,1], 'minor shape')
    require(cert['bounds'] == dict(a_ub=4, h_pad_ub=1, U_pad_ub=1,
                                  r_det_lb=1, D_ub=0), 'bounds')
    return dict(status='EXACT', geometric_replay=True, minor_Z=str(value),
                r_det_lb=1, inherited_bounds=cert['bounds'], sizing=sizing(6),
                contraction_layers=steps)


def produce(out):
    pencil = skew_pencil()
    coeffs = pencil_coefficients(pencil)
    q = {tuple(2*int(i == j) for i in range(6)): s
         for j, s in enumerate((1,1,1,-1,-1,-1))}
    require(coeffs == polynomial_product(q, q), 'skew Pfaffian-square control')
    h, _ = hyperdet(tensor(coeffs, 6), 6)
    value = coeffs[(4,0,0,0,0,0)]**2 * h
    cert = dict(format='b15-10-integral-bracket/1', actual_model='gpt-6-astra',
                cell=dict(n=4, delta=8, ell=6, ambient_variables=16,
                          partition=[12,4,4,4,4,4]), source=source_spec(),
                point=dict(family='det4_integer_pencil', pencil=pencil),
                ordinary_coefficients=[[list(a), v] for a, v in sorted(coeffs.items())],
                minor_shape=[1,1], minor_Z=str(value),
                minor_mod_p={str(p): value % p for p in PRIMES},
                bounds=dict(a_ub=4, h_pad_ub=1, U_pad_ub=1, r_det_lb=1, D_ub=0),
                inherited_bound_source='results/b15_prep/Q1_combined_bound.json')
    result = verify(cert)
    out.parent.mkdir(parents=True, exist_ok=True)
    require(not out.exists(), 'preserve existing certificate')
    out.write_text(json.dumps(cert, indent=2)+'\n', encoding='utf-8')
    return result


def main():
    p = argparse.ArgumentParser()
    p.add_argument('mode', choices=('produce','verify','size'))
    p.add_argument('--certificate', type=Path, default=ROOT/'results/b15_10/exclusion.json')
    p.add_argument('--receipt', type=Path)
    a = p.parse_args()
    start = time.perf_counter()
    result = (sizing(6) if a.mode == 'size' else produce(a.certificate)
              if a.mode == 'produce' else verify(json.loads(a.certificate.read_text(encoding='utf-8'))))
    result['wall_seconds'] = time.perf_counter()-start
    if a.receipt:
        require(not a.receipt.exists(), 'preserve existing receipt')
        a.receipt.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(result))


if __name__ == '__main__':
    main()

"""Exact rank-three projected multiplication; all coefficients are rational.

No stored evaluation matrices are used. Matrices have output basis rows and
input basis columns. Run through b15_bound.py from the assigned checkout.
"""
from collections import Counter, defaultdict, deque
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations_with_replacement, permutations, product
from math import comb, factorial, prod
from pathlib import Path
import argparse
import hashlib
import json
import time

from flint import fmpq_mat

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'results/b15_07'
ALPHA = tuple((a, b, 4-a-b) for a in range(4, -1, -1)
              for b in range(4-a, -1, -1))
INDEX = {a: i for i, a in enumerate(ALPHA)}
ROOTS = ((0, 1), (1, 2), (1, 0), (2, 1))


def need(ok, msg):
    if not ok:
        raise ValueError(msg)


def clean(p):
    return {m: Q(c) for m, c in p.items() if c}


def add(*ps):
    out = Counter()
    for p in ps:
        for m, c in p.items():
            out[m] += c
    return clean(out)


def scale(p, q):
    return clean({m: c*q for m, c in p.items()})


def mul(p, q):
    out = Counter()
    for m, c in p.items():
        for n, d in q.items():
            out[tuple(sorted(m+n))] += c*d
    return clean(out)


def variable(a):
    return {(INDEX[tuple(a)],): Q(1)}


def weight(m):
    return tuple(sum(ALPHA[j][i] for j in m) for i in range(3))


@lru_cache(None)
def root_monomial(m, i, j):
    if i == j:
        return {m: Q(weight(m)[i])} if weight(m)[i] else {}
    out = Counter()
    for k, index in enumerate(m):
        a = ALPHA[index]
        if a[j]:
            b = list(a); b[i] += 1; b[j] -= 1
            n = list(m); n[k] = INDEX[tuple(b)]
            out[tuple(sorted(n))] += a[i]+1
    return clean(out)


def root(p, i, j):
    return add(*(scale(root_monomial(m, i, j), c) for m, c in p.items()))


def casimir(p):
    return add(*(root(root(p, j, i), i, j) for i in range(3) for j in range(3)))


def eigen(lam, r=3):
    return sum(x*(x+r-1-2*i) for i, x in enumerate(lam))


def partitions(n, length=3, upper=None):
    if length == 0:
        return [()] if n == 0 else []
    return [(a,)+p for a in range(min(n, n if upper is None else upper), -1, -1)
            for p in partitions(n-a, length-1, a)]


@lru_cache(None)
def blocks(d):
    # Count the full carrier before its first allocation; never a quotient guess.
    count = comb(14+d, d)
    need(count <= 3060, 'small carrier cap')
    out = defaultdict(list)
    for m in combinations_with_replacement(range(15), d):
        out[weight(m)].append(m)
    need(sum(map(len, out.values())) == count, 'carrier count')
    return dict(out)


def sign(p):
    return (-1)**sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1, len(p)))


def character(d):
    counts = {w: len(ms) for w, ms in blocks(d).items()}
    rho = (2, 1, 0)
    out = []
    for lam in partitions(4*d):
        a = sum(sign(p)*counts.get(tuple(lam[i]+rho[i]-rho[p[i]] for i in range(3)), 0)
                for p in permutations(range(3)))
        need(a >= 0, 'negative Schur multiplicity')
        if a:
            dim = prod(Q(lam[i]-lam[j]+j-i, j-i) for i in range(3) for j in range(i+1, 3))
            out.append(dict(partition=list(lam), a=a, dimension=int(dim), casimir=eigen(lam)))
    need(sum(t['a']*t['dimension'] for t in out) == comb(14+d, d), 'character dimension')
    return out


def qmatrix(rows, columns=None):
    if not rows:
        return fmpq_mat(0, columns or 0)
    return fmpq_mat([[str(v) for v in row] for row in rows])


def identity(n):
    return qmatrix([[int(i == j) for j in range(n)] for i in range(n)])


def matrix(polys, basis):
    return qmatrix([[p.get(m, 0) for p in polys] for m in basis], len(polys))


def encode(p):
    return [[list(m), str(c)] for m, c in sorted(p.items())]


def decode(p):
    return {tuple(m): Q(c) for m, c in p}


def encoded_matrix(a):
    return [[str(a[i, j]) for j in range(a.ncols())] for i in range(a.nrows())]


class Projector:
    def __init__(self, d, nu):
        self.d, self.nu, self.value = d, tuple(nu), eigen(nu)
        # All polynomial partitions, including zero multiplicities, are included.
        collisions = [p for p in partitions(4*d) if eigen(p) == self.value and p != self.nu]
        need(not collisions, 'Casimir collision: '+str(collisions))
        self.spectrum = sorted({eigen(p) for p in partitions(4*d)})
        self.cache = {}

    def block(self, w):
        w = tuple(w)
        if w not in self.cache:
            basis = blocks(self.d).get(w, [])
            n = len(basis)
            if not n:
                return [], fmpq_mat(0, 0), fmpq_mat(0, 0)
            c = matrix([casimir({m: Q(1)}) for m in basis], basis)
            one = identity(n); p = one
            for value in self.spectrum:
                if value != self.value:
                    p = (p*(c-one*value))/(self.value-value)
            need(p*p == p and c*p == p*self.value, 'projector identities')
            self.cache[w] = basis, c, p
        return self.cache[w]

    def __call__(self, p):
        groups = defaultdict(dict)
        for m, c in p.items():
            need(len(m) == self.d, 'wrong projection degree')
            groups[weight(m)][m] = c
        out = {}
        for w, group in groups.items():
            basis, _, pr = self.block(w)
            v = pr*matrix([group], basis)
            out.update({m: Q(str(v[i, 0])) for i, m in enumerate(basis) if v[i, 0]})
        return out


def bracket(columns, d, normalized=True):
    need(Counter(x for c in columns for x in c) == Counter({i: 4 for i in range(d)}), 'valence')
    out = Counter()
    choices = [list(permutations(range(len(c)))) for c in columns]
    need(prod(map(len, choices)) <= 100000, 'bracket expansion cap')
    for perms in product(*choices):
        letters = [[0, 0, 0] for _ in range(d)]; coefficient = 1
        for col, p in zip(columns, perms):
            coefficient *= sign(p)
            for letter, index in zip(col, p):
                letters[letter][index] += 1
        if normalized:
            coefficient *= prod(factorial(v) for a in letters for v in a)
        out[tuple(sorted(INDEX[tuple(a)] for a in letters))] += coefficient
    return clean(out)


def module_basis(p):
    """Deterministic independent lowering words, with exact sparse elimination."""
    basis = []; words = []; pivots = {}; queue = deque([(p, [])])
    while queue:
        q, word = queue.popleft(); v = dict(q)
        while v:
            m = min(v)
            if m not in pivots:
                pivots[m] = scale(v, 1/v[m])
                basis.append(q); words.append(word)
                queue.extend((root(q, i, j), word+[[i, j]]) for i, j in ((1, 0), (2, 1)))
                break
            v = add(v, scale(pivots[m], -v[m]))
    return basis, words


def nullspace(rows, n):
    a = [[Q(x) for x in row] for row in rows]; pivots = []; k = 0
    for j in range(n):
        index = next((i for i in range(k, len(a)) if a[i][j]), None)
        if index is None:
            continue
        a[k], a[index] = a[index], a[k]
        t = a[k][j]; a[k] = [v/t for v in a[k]]
        for i in range(len(a)):
            if i != k and a[i][j]:
                t = a[i][j]; a[i] = [x-t*y for x, y in zip(a[i], a[k])]
        pivots.append(j); k += 1
    result = []
    for j in range(n):
        if j not in pivots:
            v = [Q(0)]*n; v[j] = Q(1)
            for i, pivot in enumerate(pivots):
                v[pivot] = -a[i][j]
            result.append(v)
    return result


def highest_weight(d, nu):
    basis = blocks(d)[tuple(nu)]; rows = []
    for i, j in ROOTS[:2]:
        ps = [root({m: Q(1)}, i, j) for m in basis]
        support = sorted(set().union(*(p.keys() for p in ps)))
        rows.extend([[p.get(m, 0) for p in ps] for m in support])
    return [clean(dict(zip(basis, v))) for v in nullspace(rows, len(basis))]


def evaluate(p, values):
    return sum(c*prod(values[j] for j in m) for m, c in p.items())


def write(name, data):
    OUT.mkdir(exist_ok=True)
    (OUT/name).write_text(json.dumps(data, indent=2)+'\n', encoding='utf-8')


def reject(name, test, out):
    try:
        test()
    except (ValueError, AssertionError) as exc:
        out.append(dict(name=name, rejected=True, reason=str(exc)))
    else:
        raise ValueError('defect was not detected: '+name)


def main():
    start = time.perf_counter(); negatives = []
    # Separate nonzero source/evaluator control, independent of research ranks.
    need(evaluate(variable((4, 0, 0)), list(range(1, 16))) == 1, 'liveness evaluation')
    need(root(variable((3, 1, 0)), 0, 1) == scale(variable((4, 0, 0)), 4), 'liveness root')
    chars = {str(d): character(d) for d in (2, 3, 4)}
    write('sizing.json', dict(status='EXACT', coefficient_variables=15,
          monomial_counts={str(d): comb(14+d, d) for d in (2, 3, 4)},
          largest_weight_blocks={str(d): max(map(len, blocks(d).values())) for d in (2, 3, 4)},
          characters=chars))
    print('Character and carrier sizing complete', flush=True)
    q62 = add(scale(mul(variable((4, 0, 0)), variable((2, 2, 0))), 8),
              scale(mul(variable((3, 1, 0)), variable((3, 1, 0))), -3))
    q44 = add(scale(mul(variable((4, 0, 0)), variable((0, 4, 0))), 12),
              scale(mul(variable((3, 1, 0)), variable((1, 3, 0))), -3),
              mul(variable((2, 2, 0)), variable((2, 2, 0))))
    witnesses = json.loads((ROOT/'results/b14_08/witnesses.json').read_text())['witnesses']
    for name, expected in (('w_2_6_2', q62), ('w_2_4_4', q44)):
        w = next(w for w in witnesses if w['id'] == name); p = {}
        for term in w['terms']:
            mon = tuple(sorted(INDEX[tuple(f['alpha'])+(0,)]
                        for f in term['factors'] for _ in range(f['power'])))
            p[mon] = Q(term['coefficient'])
        need(p == expected, 'banked multiplier normalization')
        need(not root(p, 0, 1) and not root(p, 1, 2), 'multiplier highest weight')
    filling = [[0, 1], [0, 1], [0], [0], [1], [1]]
    alternate = [[0, 1], [0, 1], [0], [1], [0], [1]]
    need(bracket(filling, 2) == bracket(alternate, 2) == scale(q62, 24), 'equivalent fillings')
    # Plucker identity multiplied by [01][23] and two singleton slots per letter.
    rest = [[0, 1], [2, 3]]+[[i] for i in range(4) for _ in range(2)]
    plucker = [[[0, 1], [2, 3]]+rest, [[0, 2], [1, 3]]+rest, [[0, 3], [1, 2]]+rest]
    rel = [bracket(t, 4) for t in plucker]
    need(all(rel) and not add(rel[0], scale(rel[1], -1), rel[2]), 'nontrivial Plucker relation')
    # Re-run only the tiny historical binary control; no banked artifact writes.
    import b14_05_controls as old
    historical = old.binary_control()
    bank = json.loads((ROOT/'results/b14_05/controls.json').read_text())['binary_adjunction']
    need(historical == bank, 'historical binary regenerated result differs')
    print('Presentation and inherited multiplier controls complete', flush=True)
    pr = Projector(3, (6, 4, 2)); source, words = module_basis(q62)
    need(len(source) == 60, 'source module dimension')
    total_rank = 0; intertwining = 0; records = []; product_records = []
    for w, basis in sorted(blocks(3).items()):
        _, c, p = pr.block(w)
        total_rank += p.rank()
        # Exact matrices for all four root generators on the complete carrier.
        for i, j in ROOTS:
            w2 = list(w); w2[i] += 1; w2[j] -= 1
            if min(w2) < 0:
                continue
            dest, _, dest_p = pr.block(tuple(w2))
            e = matrix([root({m: Q(1)}, i, j) for m in basis], dest)
            need(dest_p*e == e*p, 'GL generator intertwining')
            intertwining += len(basis)
        if p.rank():
            records.append(dict(weight=list(w), basis=[list(m) for m in basis],
                                casimir=encoded_matrix(c), projector=encoded_matrix(p)))
        columns = []; labels = []
        for si, s in enumerate(source):
            sw = weight(next(iter(s)))
            for vi, a in enumerate(ALPHA):
                if tuple(x+y for x, y in zip(sw, a)) == w:
                    columns.append(mul(s, {(vi,): Q(1)})); labels.append([si, vi])
        if columns:
            images = p*matrix(columns, basis)
            if images.rank():
                product_records.append(dict(weight=list(w), labels=labels,
                    output_monomials=[list(m) for m in basis], matrix=encoded_matrix(images), rank=images.rank()))
    need(total_rank == 27, 'projection image dimension')
    need(sum(r['rank'] for r in product_records) == 27, 'non-Cartan multiplication image')
    hw_record = next(r for r in product_records if r['weight'] == [6, 4, 2])
    # Pick a real product column and project to get an explicit nonzero polynomial.
    first = next(j for j in range(len(hw_record['labels']))
                 if any(Q(row[j]) for row in hw_record['matrix']))
    si, vi = hw_record['labels'][first]
    source_poly = source[si]; factor = {(vi,): Q(1)}
    image = pr(mul(source_poly, factor)); need(bool(image), 'nonzero projected product')
    need(si == 0 and pr(mul(bracket(filling,2),factor)) ==
         pr(mul(bracket(alternate,2),factor)) == scale(image,24), 'equivalent fillings through nonzero map')
    # This weight space need not be highest weight; give a complete HW vector too.
    hw = highest_weight(3, (6, 4, 2)); need(len(hw) == 1 and pr(hw[0]) == hw[0], 'HW normalization')
    # Before multiplication, keep the multiplier letter independent. Solve
    # highest-weight equations in this honest tensor module, including all
    # polynomial relations already resolved in the 60-vector source basis.
    tensor_rows = []
    for i, j in ROOTS[:2]:
        tensor_columns = []
        for sj, vj in hw_record['labels']:
            column = Counter()
            for m, coeff in root(source[sj], i, j).items():
                column[(m, vj)] += coeff
            for (vk,), coeff in root({(vj,): Q(1)}, i, j).items():
                for m, sc in source[sj].items():
                    column[(m, vk)] += coeff*sc
            tensor_columns.append(clean(column))
        support = sorted(set().union(*(p.keys() for p in tensor_columns)))
        tensor_rows.extend([[p.get(m, 0) for p in tensor_columns] for m in support])
    tensors = nullspace(tensor_rows, len(hw_record['labels']))
    need(len(tensors) == 1, 'Pieri tensor multiplicity')
    tensor = tensors[0]; tensor = [v/next(v for v in tensor if v) for v in tensor]
    tensor_image = add(*(scale(mul(source[sj], {(vj,): Q(1)}), coeff)
                         for coeff, (sj, vj) in zip(tensor, hw_record['labels'])))
    need(bool(tensor_image) and pr(tensor_image) == tensor_image and
         not root(tensor_image, 0, 1) and not root(tensor_image, 1, 2), 'normalized HW tensor image')
    tensor_scalar = tensor_image[min(hw[0])]/hw[0][min(hw[0])]
    need(tensor_image == scale(hw[0], tensor_scalar), 'HW tensor image scalar')
    values = list(range(1, 16))
    if evaluate(image, values) == 0:
        values = [i*i+1 for i in range(15)]
    need(evaluate(image, values) != 0, 'explicit nonzero evaluation')
    need(pr(scale(mul(source_poly, factor), 24)) == scale(image, 24), 'source normalization linearity')
    # Conjugate from ordinary coefficients to m_alpha=alpha! c_alpha.
    w = weight(next(iter(image))); basis, c, p = pr.block(w)
    norms = [prod(factorial(v) for j in m for v in ALPHA[j]) for m in basis]
    dmat = qmatrix([[norms[i] if i == j else 0 for j in range(len(basis))] for i in range(len(basis))])
    invd = qmatrix([[Q(1, norms[i]) if i == j else 0 for j in range(len(basis))] for i in range(len(basis))])
    pm = invd*p*dmat
    need(pm*pm == pm and dmat*pm == p*dmat, 'factorial conjugation')
    reject('unconverted factorial basis', lambda: need(pm == p, 'normalization must be conjugated'), negatives)
    reject('wrong source coefficient', lambda: need(not root(add(q62, mul(variable((3,1,0)), variable((3,1,0)))), 0, 1), 'raising derivative changed'), negatives)
    reject('wrong projector normalization', lambda: need((p*2)*(p*2) == p*2, 'not idempotent'), negatives)
    reject('wrong Plucker sign', lambda: need(not add(*rel), 'relation changed'), negatives)
    reject('Casimir eigenvalue collision', lambda: Projector(3, (8, 2, 2)), negatives)
    altered = list(values); altered[0] += 1
    # Check an actual observable whose chosen coordinate has nonzero sensitivity.
    sensitive = next(j for j in range(15) if evaluate(image, [v+int(i==j) for i,v in enumerate(values)]) != evaluate(image, values))
    mutated = [v+int(i==sensitive) for i,v in enumerate(values)]
    reject('altered evaluation point', lambda: need(evaluate(image, mutated) == evaluate(image, values), 'value changed'), negatives)
    write('degree3.json', dict(status='EXACT', n=4, degree=3, ambient_variables=3,
        coefficient_variables=[list(a) for a in ALPHA], source_partition=[6,2,0], output_partition=[6,4,2],
        source_dimension=60, tensor_dimension=900, image_dimension=27, a=1,
        source_generator=encode(q62), source_lowering_words=words, source_basis=[encode(p) for p in source],
        casimir_eigenvalue=pr.value, envelope_spectrum=pr.spectrum,
        values_are='rational ordinary coefficients; output monomial rows, input product columns',
        projector_blocks=records, product_blocks=product_records, generator_intertwining_columns=intertwining,
        witness=dict(source_index=si, coefficient_index=vi, polynomial=encode(image),
                     point=values, value=str(evaluate(image, values))),
        normalized_pieri_tensor=dict(labels=hw_record['labels'], coefficients=list(map(str, tensor)),
            normalization='first nonzero coefficient equals 1', raising_matrix_rows=len(tensor_rows),
            image=encode(tensor_image), image_to_hw_scalar=str(tensor_scalar)),
        highest_weight_polynomial=encode(hw[0]), factorial_change=dict(weight=list(w), diagonal=norms,
            m_projector=encoded_matrix(pm))))
    print('Degree-three complete intertwining and image rank 27 verified', flush=True)
    # Repeated multiplicities: no choice of a preferred copy is built into P.
    nu4 = (10, 4, 2); p4 = Projector(4, nu4); hs = highest_weight(4, nu4)
    multiplicity = next(t['a'] for t in chars['4'] if t['partition'] == list(nu4))
    need(multiplicity > 1 and len(hs) == multiplicity, 'repeated multiplicity control')
    need(all(p4(h) == h for h in hs), 'projector lost a highest-weight copy')
    mixes = [add(hs[i], scale(hs[(i+1)%len(hs)], 2)) for i in range(len(hs))]
    need(all(p4(h) == h for h in mixes), 'multiplicity basis mixing')
    # The Plucker relation is in another degree-four weight; its image still vanishes.
    need(not add(p4(rel[0]), scale(p4(rel[1]), -1), p4(rel[2])), 'projection broke exact relation')
    relation_projector = Projector(4,(12,4,0))
    rel_images = [relation_projector(h) for h in rel]
    need(all(rel_images) and not add(rel_images[0],scale(rel_images[1],-1),rel_images[2]),
         'nonzero Plucker images through projection')
    # Test a nonzero repeated component in multiplication A3 x A1.
    b4, c4, block4 = p4.block(nu4)
    rows4 = [[Q(str(block4[i,j])) for j in range(block4.ncols())] for i in range(block4.nrows())]
    need(block4.rank() >= multiplicity, 'multiplicity matrix rank')
    # A repeated tensor channel as well as a repeated ambient component.
    # Both factors are the same polynomial module, but are kept distinct until
    # multiplication. In particular antisymmetric tensors must map to zero.
    pairs = [(i,j) for i,s in enumerate(source) for j,t in enumerate(source)
             if tuple(a+b for a,b in zip(weight(next(iter(s))),weight(next(iter(t))))) == nu4]
    tensor4_rows = []
    for ri,rj in ROOTS[:2]:
        cols = []
        for i,j in pairs:
            col = Counter()
            for m,c in root(source[i],ri,rj).items():
                for n,v in source[j].items():
                    col[(m,n)] += c*v
            for m,c in source[i].items():
                for n,v in root(source[j],ri,rj).items():
                    col[(m,n)] += c*v
            cols.append(clean(col))
        support = sorted(set().union(*(p.keys() for p in cols)))
        tensor4_rows.extend([[p.get(m,0) for p in cols] for m in support])
    ts4 = nullspace(tensor4_rows,len(pairs))
    from b13_06_decompose import lr_count
    lr4 = lr_count((6,2),(6,2),nu4)
    need(len(ts4)==lr4 and lr4>1,'repeated Littlewood-Richardson channel')
    im4 = [add(*(scale(mul(source[i],source[j]),v) for v,(i,j) in zip(t,pairs))) for t in ts4]
    need(all(p4(h)==h and not root(h,0,1) and not root(h,1,2) for h in im4),'tensor multiplicity images')
    im4matrix = matrix(im4,b4)
    need(im4matrix.rank()>0,'repeated channel liveness')
    swap_index = {pair:i for i,pair in enumerate(pairs)}
    for t in ts4:
        antisymmetric = [v-t[swap_index[(j,i)]] for v,(i,j) in zip(t,pairs)]
        need(not add(*(scale(mul(source[i],source[j]),v) for v,(i,j) in zip(antisymmetric,pairs))), 'antisymmetric tensor kernel')
    write('tensor_multiplicity.json',dict(status='EXACT',source_partitions=[[6,2,0],[6,2,0]],
        output_partition=list(nu4),source_degree=[2,2],tensor_weight_dimension=len(pairs),
        highest_weight_multiplicity=lr4,ambient_hw_multiplicity=multiplicity,
        multiplication_hw_rank=im4matrix.rank(),pairs=pairs,
        tensor_hw_basis=[list(map(str,t)) for t in ts4],tensor_raising_rows=len(tensor4_rows),
        image_polynomials=[encode(h) for h in im4],image_matrix=encoded_matrix(im4matrix),
        output_monomials=[list(m) for m in b4],
        values_are='ordered source-basis pair tensors; multiplication image monomial rows and tensor-HW columns',
        antisymmetric_images_zero=True,rank_kernel_dimension=lr4-im4matrix.rank()))
    write('degree4.json', dict(status='EXACT', degree=4, ambient_variables=3, partition=list(nu4),
        a=multiplicity, weight_space_dimension=len(b4), projected_weight_rank=block4.rank(),
        casimir_eigenvalue=p4.value, envelope_spectrum=p4.spectrum,
        coefficient_variables=[list(a) for a in ALPHA], basis=[list(m) for m in b4],
        casimir=encoded_matrix(c4), projector=encoded_matrix(block4),
        highest_weight_basis=[encode(h) for h in hs], mixed_basis=[encode(h) for h in mixes],
        multiplication_columns=[dict(source_monomial=list(m[:-1]), factor_index=m[-1]) for m in b4],
        multiplication_matrix=encoded_matrix(block4),
        values_are='output monomial rows; A3-monomial times A1-factor columns; repeated isotypic component retained whole'))
    # An exact geometric ideal control independent of the general ideal proof:
    # c_alpha -> multinomial(4,alpha)*t^alpha parametrizes fourth powers.
    veronese_coefficients = [Q(factorial(4), prod(factorial(v) for v in a)) for a in ALPHA]
    need(all(evaluate(s, veronese_coefficients) == 0 for s in source), 'Veronese source ideal')
    need(all(evaluate(pr({m: Q(1)}), veronese_coefficients) == 0
             for ms in blocks(3).values() for m in ms), 'Veronese projected ideal')
    # Stable is an essential hypothesis: a principal coordinate ideal fails.
    input_nonstable = mul(variable((4, 0, 0)), variable((2, 2, 0)))
    nonstable = Projector(2, (6, 2, 0))(input_nonstable)
    need(any(0 not in m for m in nonstable), 'nonstable ideal counterexample')
    write('ideal_control.json', dict(status='EXACT', stable_ideal='ideal of fourth powers in Sym^4(V*)',
        parametrization='c_alpha=4!/alpha! times t^alpha', source_vectors=60,
        projected_monomials=680, source_pullbacks_zero=True, projected_pullbacks_zero=True,
        proof_of_global_zero='Each tested polynomial is weight homogeneous, so its pullback is one t^weight monomial times the checked exact scalar.',
        nonstable_counterexample=dict(ideal='(c_(4,0,0))', input=encode(input_nonstable),
            projection_partition=[6,2,0], image=encode(nonstable)),
        distinction='Image of a known ideal submodule is not the full ideal. No padded ideal multiplicity is computed.'))
    write('presentations.json', dict(status='EXACT', equivalent_fillings=[filling, alternate],
        bracket_to_q62_factor=24, plucker_fillings=plucker, plucker_signs=[1,-1,1],
        plucker_polynomials=[encode(p) for p in rel],
        historical_binary=historical, historical_negative_controls=old.REJECTIONS,
        inherited_n3_transport='RECORDED only; no new filling expansion or transport replay',
        negative_controls=negatives))
    write('control_summary.json', dict(status='EXACT', checks='PASS', actual_model='gpt-6-astra',
        reasoning_effort='xhigh', source_module_dimension=60, noncartan_image_dimension=27,
        repeated_hw_multiplicity=multiplicity, rejected_defects=len(negatives),
        wall_seconds=time.perf_counter()-start, geometric_rank_computed=False,
        exclusions_proposed=0))
    print(json.dumps(dict(status='PASS', image_dimension=27, repeated_multiplicity=multiplicity,
                          seconds=time.perf_counter()-start)), flush=True)


if __name__ == '__main__':
    main()

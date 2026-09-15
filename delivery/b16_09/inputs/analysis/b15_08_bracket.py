"""Three-column brackets, exact bordered determinants and independent eps control.

New work: GPT-6 Astra. B14-06 (Claude Opus 5) supplies the two-column
bordered-determinant input; this module derives the short-column extension.
All tensors use ordinary integral symmetric entries, not divided-power entries.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations_with_replacement, permutations, product
from math import comb, factorial, prod

from flint import fmpz_mat, nmod_mat

DEGS = (2, 3, 4)


def sign(seq):
    return (-1) ** sum(seq[i] > seq[j] for i in range(len(seq))
                       for j in range(i + 1, len(seq)))


def exchange_columns(bracket):
    return tuple(sorted((d, (mask & 4) | ((mask & 1) << 1) | ((mask & 2) >> 1))
                        for d, mask in bracket))


@lru_cache(None)
def enumerate_brackets(h, W, short=2):
    """Explicit source multiset signatures; no spanning claim is assumed.

Mask bits 1,2,4 denote columns A,B,C. Columns read letter IDs in list order;
all unoccupied letter slots read e_0. Singletons are not separate letters.
Duplicate one-column vectors vanish and can be omitted. Swap A/B deduplicates
up to a fixed source sign. No stabilizer quotient is used as a dimension.
"""
    if h < 2 or short not in (0, 2) or W < 2*h + short:
        raise ValueError('unsupported shape')
    short_types = [(d, m) for d in DEGS for m in (4, 5, 6, 7)
                   if m.bit_count() <= d]
    tails = combinations_with_replacement(short_types, short) if short else [()]
    sources = set()
    for tail in tails:
        if short and tail[0] == tail[1] and tail[0][1] == 4:
            continue
        sa = sum(bool(m & 1) for d, m in tail)
        sb = sum(bool(m & 2) for d, m in tail)
        for a in product((0, 1), repeat=3):
            m = h - sa - sum(a)
            if m < 0:
                continue
            for b in product((0, 1), repeat=3):
                if h - sb - sum(b) != m:
                    continue
                for c2 in range(m + 1):
                    for c3 in range(m - c2 + 1):
                        c = (c2, c3, m-c2-c3)
                        base = sum(d for d, _ in tail) + sum(
                            d*(a[i]+b[i]+c[i]) for i, d in enumerate(DEGS))
                        rest = W-base
                        if rest < 0:
                            continue
                        for z2 in range(rest//2+1):
                            for z3 in range((rest-2*z2)//3+1):
                                rr = rest-2*z2-3*z3
                                if rr % 4:
                                    continue
                                z = (z2, z3, rr//4)
                                items = list(tail)
                                for i, d in enumerate(DEGS):
                                    for mask, num in ((0,z[i]), (1,a[i]), (2,b[i]), (3,c[i])):
                                        items.extend([(d,mask)]*num)
                                br = tuple(sorted(items))
                                sources.add(min(br, exchange_columns(br)))
    return tuple(sorted(sources))


def validate(bracket, h, short=2):
    if not bracket or h < 2 or short not in (0, 2):
        raise ValueError('empty or unsupported source')
    for d, mask in bracket:
        if d not in DEGS or mask < 0 or mask > 7 or mask.bit_count() > d:
            raise ValueError('invalid symmetric letter')
    if [sum(bool(m & bit) for d, m in bracket) for bit in (1,2,4)] != [h,h,short]:
        raise ValueError('wrong column occupancies')


def slots(bracket, bit):
    return [i for i, (d, mask) in enumerate(bracket) if mask & bit]


def tensor_get(point, d, indices):
    return point[d][tuple(sorted(tuple(indices)+(0,)*(d-len(indices))))]


def det(matrix, p=None):
    if not matrix:
        return 1
    return int((nmod_mat(matrix, p) if p else fmpz_mat(matrix)).det())


def rank(matrix, p):
    if not matrix or not matrix[0]:
        raise ValueError('empty evaluation matrix')
    return int(nmod_mat(matrix, p).rank())


def work_count(bracket, h, short=2):
    validate(bracket, h, short)
    ordinary = Counter(d for d,m in bracket if m == 3)
    special = sum(m == 7 for d,m in bracket)
    paired = sum(ordinary.values()) + special
    nodes = prod(c+1 for c in ordinary.values()) * 2**special
    return dict(determinants=factorial(short)*nodes, determinant_order=2*h-paired,
                brute_terms=factorial(h)**2*factorial(short), paired_letters=paired,
                mixed_coefficient_factorial=prod(factorial(c) for c in ordinary.values()))


def value(bracket, point, h, p=None, short=2, factorial_defect=False):
    """Exact eps_A eps_B (e_0 wedge e_1) contraction.

Expand C. Reorder A/B to vectors then pairs; retain both permutation signs.
For q pairs, det(border) is homogeneous degree q in the matrix variables.
Its q labelled finite differences at zero select the squarefree monomial.
Grouping identical ordinary pair matrices gives binomial finite differences,
already equal to prod(c_d!) times their ordinary coefficient.
"""
    validate(bracket,h,short)
    ac, bc, cc = (slots(bracket,b) for b in (1,2,4))
    pairs = [i for i in ac if i in bc]
    av = [i for i in ac if i not in bc]
    bv = [i for i in bc if i not in ac]
    assert len(av) == len(bv)
    order_sign = sign([ac.index(i) for i in av+pairs])*sign([bc.index(i) for i in bv+pairs])
    r = len(av)
    total = 0
    for cp in permutations(range(short)):
        cidx = dict(zip(cc,cp))
        scalar = sign(cp)*order_sign*((-1)**r)
        for i,(d,mask) in enumerate(bracket):
            if not mask & 3:
                scalar *= tensor_get(point,d,([cidx[i]] if i in cidx else []))
                if p: scalar %= p
        if not scalar:
            continue
        avec = [[tensor_get(point,bracket[i][0],[j]+([cidx[i]] if i in cidx else []))
                 for j in range(h)] for i in av]
        bvec = [[tensor_get(point,bracket[i][0],[j]+([cidx[i]] if i in cidx else []))
                 for j in range(h)] for i in bv]
        # Canonical vector duplicates are exact zeros even after the C expansion.
        if len(set(map(tuple,avec))) < r or len(set(map(tuple,bvec))) < r:
            continue
        groups = {}
        for i in pairs:
            d = bracket[i][0]
            key = (d,cidx[i]) if i in cidx else (d,None)
            groups[key] = groups.get(key,0)+1
        mats, counts = [], []
        for (d,c),num in groups.items():
            mats.append([[tensor_get(point,d,[i,j]+([] if c is None else [c]))
                          for j in range(h)] for i in range(h)])
            counts.append(num)
        v = 0
        for amounts in product(*(range(c+1) for c in counts)):
            weight = prod((-1)**(c-j)*comb(c,j) for c,j in zip(counts,amounts))
            M = [[sum(k*N[i][j] for k,N in zip(amounts,mats)) for j in range(h)]
                 + [u[i] for u in avec] for i in range(h)]
            M.extend([w+[0]*r for w in bvec])
            if p: M = [[int(x)%p for x in row] for row in M]
            v += weight*det(M,p)
            if p: v %= p
        if factorial_defect:
            f = prod(factorial(c) for c in counts)
            v = v*pow(f,-1,p)%p if p else v//f
        total += scalar*v
        if p: total %= p
    return int(total)


def brute(bracket, point, h, p=None, short=2, columns=None, sign_defect=False):
    """Independent direct definition: all h! h! short! assignments."""
    validate(bracket,h,short)
    cols = columns or [slots(bracket,b) for b in (1,2,4)]
    total = 0
    for pa,pb,pc in product(permutations(range(h)),permutations(range(h)),permutations(range(short))):
        assignments = [dict(zip(ids,perm)) for ids,perm in zip(cols,(pa,pb,pc))]
        term = sign(pa)*sign(pb)*(1 if sign_defect else sign(pc))
        for letter,(d,mask) in enumerate(bracket):
            idx = [a[letter] for a in assignments if letter in a]
            term *= tensor_get(point,d,idx)
            if p: term %= p
        total += term
        if p: total %= p
    return int(total)


def random_point(h, rng, bound=3):
    return {d:{idx:rng.randrange(-bound,bound+1)
               for idx in combinations_with_replacement(range(h),d)} for d in DEGS}


def point_json(point):
    return {str(d):[[list(idx),v] for idx,v in sorted(T.items())] for d,T in point.items()}


def point_read(raw):
    return {int(d):{tuple(idx):v for idx,v in rows} for d,rows in raw.items()}


def ordinary_polynomials(point):
    return {d:{idx:factorial(d)//prod(factorial(v) for v in Counter(idx).values())*entry
               for idx,entry in T.items()} for d,T in point.items()}


def evaluate_polynomial(poly,x,p=None):
    v = sum(c*prod(x[i] for i in idx) for idx,c in poly.items())
    return v%p if p else v


def tensor_from_polynomials(polys,h,p):
    return {d:{idx:(poly.get(idx,0)*pow(factorial(d)//prod(factorial(v) for v in Counter(idx).values()),-1,p))%p
               for idx in combinations_with_replacement(range(h),d)} for d,poly in polys.items()}


def transformed(point,g,p):
    """Tensor substitution T'(i_1,..)=T(g e_i1,..), for small controls."""
    h=len(g)
    return {d:{idx:sum(tensor_get(point,d,js)*prod(g[j][i] for j,i in zip(js,idx))
                      for js in product(range(h),repeat=d))%p
               for idx in combinations_with_replacement(range(h),d)} for d in DEGS}

"""Independent complete-interpolation checker; imports no analysis routines.

gct-cert/1, complete_interpolation, profile ternary_quartic_888_d6.
The finite profile is intentional: no external dimension assertion is trusted.
All acceptance conditions use explicit checks, not Python assert statements.
"""
from collections import defaultdict
from fractions import Fraction as Q
from functools import lru_cache
import itertools as it
import gzip
import json
import math
from pathlib import Path
import re
import sys
import time

PRIMES = (2147483647, 2147483629)
CONVENTIONS = {
    'coefficient': 'ordinary',
    'raising': '(alpha_i+1)c_(alpha+e_i-e_j)',
    'bracket': 'linear l_i; cubic alpha! d_alpha; no orbit averaging',
    'orientation': 'source rows; point columns; A^T K=0'}
CELL = {'n':4, 'r':3, 'delta':6, 'lambda':[8,8,8]}


class Rejected(Exception):
    def __init__(self, status, code, detail):
        self.status, self.code, self.detail = status, code, detail
        super().__init__(detail)


def need(condition, code, detail, status='FAIL'):
    if not condition:
        raise Rejected(status, code, detail)


def keys(d, names, where):
    need(type(d) is dict, 'schema', where + ': expected object', 'UNPARSEABLE')
    expected = set(names.split())
    need(set(d) == expected, 'schema',
         f'{where}: missing={sorted(expected-set(d))}, unknown={sorted(set(d)-expected)}', 'UNPARSEABLE')


def integer(v):
    need(type(v) is int and abs(v).bit_length() <= 4096,
         'integer', 'expected a bounded exact integer', 'UNPARSEABLE')
    return v


def rational(v):
    need(type(v) is int or (type(v) is str and
         re.fullmatch(r'-?\d+(?:/[1-9]\d*)?', v) and len(v) <= 1300),
         'rational', 'expected an exact integer or rational string', 'UNPARSEABLE')
    x = Q(v)
    integer(x.numerator)
    integer(x.denominator)
    return x


def vector(v, length, scalar=integer):
    need(type(v) is list and len(v) == length, 'shape', f'expected vector length {length}', 'UNPARSEABLE')
    return [scalar(x) for x in v]


def matrix(v, rows, cols, scalar=integer):
    need(type(v) is list and len(v) == rows, 'shape', f'expected {rows} rows', 'UNPARSEABLE')
    return [vector(row, cols, scalar) for row in v]


def schema(c):
    keys(c, 'format kind profile title produced_by field cell conventions points source target source_arithmetic kernel claim', 'certificate')
    need(c['format'] == 'gct-cert/1' and c['kind'] == 'complete_interpolation', 'format', 'wrong format or kind', 'UNPARSEABLE')
    need(c['profile'] == 'ternary_quartic_888_d6', 'unsupported_profile', 'NOT VERIFIED: only the exact h=1 profile is implemented', 'UNPARSEABLE')
    need(c['field'] == 'Q', 'field', 'CI acceptance is over Q', 'UNPARSEABLE')
    for name in ['title','produced_by']:
        need(type(c[name]) is str and bool(c[name].strip()), 'schema', name + ' must be nonempty', 'UNPARSEABLE')
    keys(c['cell'], 'n r delta lambda', 'cell')
    for name in ['n','r','delta']:
        integer(c['cell'][name])
    vector(c['cell']['lambda'], 3)
    need(c['cell'] == CELL, 'unsupported_cell', 'NOT VERIFIED: cell outside registered profile', 'UNPARSEABLE')
    keys(c['conventions'], 'coefficient raising bracket orientation', 'conventions')
    need(c['conventions'] == CONVENTIONS, 'conventions', 'unknown normalization/orientation', 'UNPARSEABLE')
    s, t, ar, k = (c[x] for x in ['source','target','source_arithmetic','kernel'])
    keys(s, 'exponents basis change_of_basis provenance_sha256 dimension_proof', 'source')
    keys(s['dimension_proof'], 'method weight_dimension raising_rank dimension', 'source.dimension_proof')
    keys(t, 'dimension_proof members evaluation minor', 'target')
    keys(t['dimension_proof'], 'method predecessors weight_dimensions raising_ranks dimension', 'target.dimension_proof')
    keys(t['evaluation'], 'values_are entries', 'target.evaluation')
    keys(t['minor'], 'rows columns determinant', 'target.minor')
    keys(ar, 'values_are row_denominators entries height_bounds crt', 'source_arithmetic')
    keys(ar['crt'], 'values_are primes modulus residues', 'crt')
    keys(k, 'values_are entries rank', 'kernel')
    keys(c['claim'], 'source_dimension target_dimension rank_Q i_red', 'claim')
    need(type(s['provenance_sha256']) is str and re.fullmatch('[0-9a-f]{64}', s['provenance_sha256']),
         'provenance', 'expected source SHA256', 'UNPARSEABLE')
    need(t['evaluation']['values_are'] == 'integral mixed bracket evaluations; target rows', 'values_are', 'wrong target value convention', 'UNPARSEABLE')
    need(ar['values_are'] == 'A_Z = diag(row_denominators) A_Q; source rows', 'values_are', 'wrong source value convention', 'UNPARSEABLE')
    need(ar['crt']['values_are'] == 'A_Z mod p; source rows; prime-keyed residue matrices',
         'values_are', 'wrong residue value convention', 'UNPARSEABLE')
    need(k['values_are'] == 'rational coefficients in changed source basis; columns', 'values_are', 'wrong kernel convention', 'UNPARSEABLE')
    need(type(c['points']) is list and 1 <= len(c['points']) <= 16,
         'points', 'need 1..16 explicit points', 'UNPARSEABLE')
    need(type(t['members']) is list and len(t['members']) == 1,
         'members', 'need exactly h=1 target members', 'UNPARSEABLE')


@lru_cache(None)
def check_house_primes():
    for p in PRIMES:
        need(p >= 2 and all(p % d for d in range(2,math.isqrt(p)+1)),
             'prime','house modulus is not prime')
    return True


@lru_cache(None)
def exponents(n):
    # Ascending order, reconstructed directly; no house exponent generator.
    return tuple(a for a in it.product(range(n+1), repeat=3) if sum(a) == n)


def rank_q(A):
    if not A:
        return 0
    B = [list(map(Q, row)) for row in A]
    r = 0
    for j in range(len(B[0])):
        pivot = next((i for i in range(r, len(B)) if B[i][j]), None)
        if pivot is None:
            continue
        B[r], B[pivot] = B[pivot], B[r]
        v = B[r][j]
        B[r] = [x/v for x in B[r]]
        for i in range(r+1, len(B)):
            q = B[i][j]
            B[i] = [x-q*y for x, y in zip(B[i], B[r])]
        r += 1
        if r == len(B):
            break
    return r


def mod_rank(A, p):
    # Reduction BEFORE int64 conversion, so arbitrary integer inputs are safe.
    import numpy as np
    need((p-1)**2 + p-1 < 2**63, 'modular_model', 'prime outside int64 safety bound')
    B = np.array([[int(x) % p for x in row] for row in A], dtype=np.int64)
    r = 0
    for j in range(B.shape[1]):
        pivot = next((i for i in range(r, B.shape[0]) if B[i,j]), None)
        if pivot is None:
            continue
        B[[r,pivot]] = B[[pivot,r]]
        B[r,j:] = B[r,j:]*pow(int(B[r,j]),-1,p) % p
        for i in range(r+1, B.shape[0]):
            if B[i,j]:
                B[i,j:] = (B[i,j:] - B[i,j]*B[r,j:]) % p
        r += 1
        if r == B.shape[0]:
            break
    return r


def raise_poly(poly, E, i):
    pos = {a:j for j,a in enumerate(E)}
    out = defaultdict(Q)
    for word, v in poly.items():
        for k, coord in enumerate(word):
            a = E[coord]
            if a[i+1]:
                b = list(a)
                b[i] += 1
                b[i+1] -= 1
                w = list(word)
                w[k] = pos[tuple(b)]
                out[tuple(sorted(w))] += v*(a[i]+1)
    return {m:v for m,v in out.items() if v}


@lru_cache(maxsize=4)
def complete_raising(n, weight):
    E = exponents(n)
    mons = [m for m in it.combinations_with_replacement(range(len(E)),6)
            if tuple(sum(E[j][i] for j in m) for i in range(3)) == weight]
    need(0 < len(mons) <= 3000, 'resource', 'weight monomial cap exceeded', 'UNPARSEABLE')
    rows = defaultdict(dict)
    for col, m in enumerate(mons):
        for i in range(2):
            for word,v in raise_poly({m:1},E,i).items():
                rows[i,word][col] = int(v)
    need(len(rows)*len(mons) <= 5_000_000, 'resource', 'raising matrix cap exceeded', 'UNPARSEABLE')
    A = [[row.get(j,0) for j in range(len(mons))] for key,row in sorted(rows.items())]
    ranks = tuple(mod_rank(A,p) for p in PRIMES)
    return tuple(mons), len(rows), ranks


@lru_cache(maxsize=8)
def source_basis(serialized):
    s = json.loads(serialized)
    E0 = tuple(tuple(vector(a,3)) for a in s['exponents'])
    E = exponents(4)
    need(len(E0) == 15 and set(E0) == set(E), 'coordinates', 'source coordinates incomplete or repeated', 'UNPARSEABLE')
    pos = {a:j for j,a in enumerate(E)}
    need(type(s['basis']) is list and len(s['basis']) == 2, 'source_basis', 'need two source vectors', 'UNPARSEABLE')
    polys = []
    for terms in s['basis']:
        need(type(terms) is list and 1 <= len(terms) <= 2000, 'source_basis', 'empty or oversized source', 'UNPARSEABLE')
        poly = {}
        for term in terms:
            need(type(term) is list and len(term) == 2, 'term', 'expected [monomial,coefficient]', 'UNPARSEABLE')
            m, v = term
            m = vector(m,6)
            need(all(0 <= j < 15 for j in m) and m == sorted(m), 'term', 'invalid coordinate word', 'UNPARSEABLE')
            word = tuple(sorted(pos[E0[j]] for j in m))
            need(word not in poly, 'term', 'duplicate monomial', 'UNPARSEABLE')
            need(tuple(sum(E[j][i] for j in word) for i in range(3)) == (8,8,8), 'source_weight', 'incorrect source weight')
            poly[word] = rational(v)
            need(bool(poly[word]), 'term', 'zero source term', 'UNPARSEABLE')
        for i in range(2):
            need(not raise_poly(poly,E,i), 'source_membership', f'source raising residual at {i}')
        polys.append(poly)
    mons, nr, ranks = complete_raising(4,(8,8,8))
    need(rank_q([[poly.get(m,0) for poly in polys] for m in mons]) == 2,
         'source_independence', 'source vectors are dependent')
    dim = len(mons)-max(ranks)
    need(dim == 2, 'source_completeness', 'modular rank floor does not prove source completeness')
    d = s['dimension_proof']
    for name in ['weight_dimension','raising_rank','dimension']:
        integer(d[name])
    need(d == {'method':'complete_raising','weight_dimension':len(mons),
               'raising_rank':max(ranks),'dimension':2}, 'source_dimension', 'wrong source dimension witness')
    return E, tuple(polys), {'weight_dimension':len(mons),'raising_rows':nr,'ranks_mod_p':ranks,
                             'dimension_Q':2,'independent_exact_HWs':2}


def points_read(points):
    C = exponents(3)
    out = []
    for pt in points:
        keys(pt, 'type l cubic', 'point')
        need(pt['type'] == 'reducible', 'points', 'point must be a reducible substitution', 'UNPARSEABLE')
        linear = vector(pt['l'],3)
        need(all(abs(x) <= 10**6 for x in linear), 'resource', 'point coordinate cap', 'UNPARSEABLE')
        need(type(pt['cubic']) is list and len(pt['cubic']) == len(C), 'points', 'every cubic coefficient, including zero, is required', 'UNPARSEABLE')
        cubic = {}
        for pair in pt['cubic']:
            need(type(pair) is list and len(pair) == 2, 'points', 'expected cubic coefficient pair', 'UNPARSEABLE')
            a = tuple(vector(pair[0],3))
            need(a in C and a not in cubic, 'points', 'bad or repeated cubic coordinate', 'UNPARSEABLE')
            cubic[a] = integer(pair[1])
            need(abs(cubic[a]) <= 10**6, 'resource', 'cubic coordinate cap', 'UNPARSEABLE')
        out.append((linear,cubic))
    return out


@lru_cache(maxsize=8)
def bracket_polynomial(serialized):
    member = json.loads(serialized)
    keys(member,'letter_types columns','target.member')
    types = member['letter_types']
    need(type(types) is list and types == ['linear']*6+['cubic']*6,
         'target_membership','profile requires six linear and six cubic letters')
    need(type(member['columns']) is list and len(member['columns']) == 8,
         'target_membership','weight (8,8,8) requires eight initial columns of height three')
    cols = [vector(col,3) for col in member['columns']]
    need(all(0 <= j < 12 for col in cols for j in col), 'target_membership','letter index outside range')
    counts = [sum(col.count(j) for col in cols) for j in range(12)]
    need(counts == [1]*6+[3]*6, 'target_membership','each linear/cubic letter must have valence 1/3')
    E = exponents(1)+exponents(3)
    index = {a:j for j,a in enumerate(E)}
    if any(len(set(col)) < 3 for col in cols):
        return {}, E  # zero is a member; the full-minor gate must reject it
    # Expand the product of determinant polynomials in labelled auxiliary
    # variables, then apply the linear umbral map at each leaf. No point values
    # enter this expansion, and no producer evaluator is shared.
    column_terms = []
    for col in cols:
        terms = []
        for order in it.permutations(col):
            indices = [col.index(j) for j in order]
            sign = (-1)**sum(indices[a] > indices[b] for a in range(3) for b in range(a+1,3))
            terms.append((order,sign))
        column_terms.append(terms)
    powers = [[0]*3 for _ in types]
    poly = defaultdict(int)
    def expand(k, coefficient):
        if k == 8:
            word = []
            for j,alpha in enumerate(powers):
                a = tuple(alpha)
                word.append(index[a])
                if j >= 6:
                    coefficient *= math.prod(math.factorial(x) for x in a)
            poly[tuple(sorted(word))] += coefficient
            need(len(poly) <= 250_000, 'resource','symbolic term cap exceeded','UNPARSEABLE')
            return
        for order,sign in column_terms[k]:
            for i,j in enumerate(order):
                powers[j][i] += 1
            expand(k+1,coefficient*sign)
            for i,j in enumerate(order):
                powers[j][i] -= 1
    expand(0,1)
    poly = {m:v for m,v in poly.items() if v}
    for word in poly:
        need(sum(j < 3 for j in word) == 6 and len(word) == 12,
             'target_membership','wrong target bidegree')
        need(tuple(sum(E[j][i] for j in word) for i in range(3)) == (8,8,8),
             'target_membership','wrong target weight')
    for i in range(2):
        need(not raise_poly(poly,E,i),'target_membership','mixed bracket has a nonzero raising residual')
    return poly,E


def target_dimension(d):
    # Pieri: lambda_i >= nu_i >= lambda_(i+1), |nu|=18.
    lam = (8,8,8,0)
    predecessors = [nu for nu in it.product(*(range(lam[i+1],lam[i]+1) for i in range(3)))
                    if sum(nu) == 18]
    dims, ranks, details = [], [], []
    for nu in predecessors:
        mons,nr,rp = complete_raising(3,nu)
        dims.append(len(mons))
        ranks.append(max(rp))
        details.append({'nu':nu,'weight_dimension':len(mons),'raising_rows':nr,'ranks_mod_p':rp})
    # This proves an upper bound. Nonzero target minor supplies the lower bound.
    upper = sum(a-b for a,b in zip(dims,ranks))
    vector(d['weight_dimensions'],len(dims))
    vector(d['raising_ranks'],len(ranks))
    integer(d['dimension'])
    matrix(d['predecessors'],len(predecessors),3)
    need(d == {'method':'pieri_complete_cubic_raising','predecessors':[list(v) for v in predecessors],
               'weight_dimensions':dims,'raising_ranks':ranks,'dimension':upper},
         'target_dimension','incorrect target dimension proof')
    need(upper == 1,'target_dimension','target upper bound must be one')
    return details


def evaluate(poly, values):
    return sum(c*math.prod(values[j] for j in m) for m,c in poly.items())


def crt_signed(residues, primes):
    value, modulus = 0,1
    for r,p in zip(residues,primes):
        value += modulus*((r-value)*pow(modulus,-1,p) % p)
        modulus *= p
    return value if 2*value < modulus else value-modulus


def _check(c, log):
    schema(c)
    check_house_primes()
    log.append({'check':'strict required inputs and profile','ok':True})
    pts = points_read(c['points'])
    E,polys,source_proof = source_basis(json.dumps(c['source'],sort_keys=True))
    log.append({'check':'complete source over Q','ok':True,'detail':source_proof})
    B = matrix(c['source']['change_of_basis'],2,2,rational)
    need(rank_q(B) == 2,'source_scaling','change of source basis must be invertible')
    mons = set().union(*(p.keys() for p in polys))
    changed = [{m:sum(B[i][j]*polys[j].get(m,0) for j in range(2)) for m in mons} for i in range(2)]
    td = target_dimension(c['target']['dimension_proof'])
    target,E_target = bracket_polynomial(json.dumps(c['target']['members'][0],sort_keys=True))
    vals = []
    quartics = []
    for linear,cubic in pts:
        tv = [linear[a.index(1)] if sum(a) == 1 else cubic[a] for a in E_target]
        vals.append(int(evaluate(target,tv)))
        quartics.append([sum(linear[i]*cubic[tuple(a[j]-(i == j) for j in range(3))]
                            for i in range(3) if a[i]) for a in E])
    stored = matrix(c['target']['evaluation']['entries'],1,len(pts))
    need(stored == [vals],'target_entries','target entries disagree with reconstructed brackets/points')
    mi = c['target']['minor']
    vector(mi['rows'],1)
    vector(mi['columns'],1)
    integer(mi['determinant'])
    need(mi['rows'] == [0] and 0 <= mi['columns'][0] < len(pts), 'target_minor','invalid full target minor indices')
    determinant = vals[mi['columns'][0]]
    need(determinant != 0,'target_rank','target minor is zero: evaluation not proved injective')
    need(mi['determinant'] == determinant,'target_minor','incorrect target minor determinant')
    log.append({'check':'target dimension, bracket membership and full minor','ok':True,
                'detail':{'upper_bound_proof':td,'dimension_Q':1,'polynomial_terms':len(target),
                          'minor_determinant':determinant,'entries':[vals]}})
    ar = c['source_arithmetic']
    den = vector(ar['row_denominators'],2)
    cleared = []
    for poly,d in zip(changed,den):
        need(d > 0 and d == math.lcm(*(v.denominator for v in poly.values())),
             'source_scaling','row denominator is not the exact coefficient-denominator lcm')
        cleared.append({m:int(v*d) for m,v in poly.items()})
    pmax = max(1,*(abs(x) for point in quartics for x in point))
    bounds = [sum(abs(v) for v in poly.values()) * pmax**6 for poly in cleared]
    need(vector(ar['height_bounds'],2) == bounds,'height_bound','height bound must be independently derived from cleared source coefficients and points')
    primes = vector(ar['crt']['primes'],len(ar['crt']['primes']))
    need(bool(primes) and len(set(primes)) == len(primes) and all(p in PRIMES for p in primes),
         'crt_primes','profile admits only distinct house primes')
    M = integer(ar['crt']['modulus'])
    need(M == math.prod(primes),'crt_modulus','modulus must equal product of certified primes')
    need(all(M > 2*h for h in bounds),'crt_insufficient','CRT modulus must exceed twice each independently derived height bound')
    need(all(math.gcd(d,p) == 1 for d in den for p in PRIMES),
         'denominator_prime','prime divides a source denominator; no common specialization')
    AZ = matrix(ar['entries'],2,len(pts))
    expected = [[evaluate(poly,pt) for pt in quartics] for poly in cleared]
    need(AZ == expected,'source_entries','integer source entry differs from exact polynomial evaluation')
    keys(ar['crt']['residues'],' '.join(str(p) for p in primes),'CRT residues')
    residues = {}
    for p in primes:
        residues[p] = matrix(ar['crt']['residues'][str(p)],2,len(pts))
        for i,poly in enumerate(cleared):
            for j,point in enumerate(quartics):
                v = 0
                for word,coef in poly.items():
                    term = coef % p
                    for x in word:
                        term = term*(point[x] % p) % p
                    v = (v+term) % p
                need(0 <= residues[p][i][j] < p and residues[p][i][j] == v,
                     'crt_residues','residue differs from independently reduced source evaluation')
    for i in range(2):
        for j in range(len(pts)):
            need(abs(AZ[i][j]) <= bounds[i] and crt_signed([residues[p][i][j] for p in primes],primes) == AZ[i][j],
                 'crt_reconstruction','signed CRT or certified bound fails')
    AQ = [[Q(x,d) for x in row] for row,d in zip(AZ,den)]
    rank = rank_q(AQ)
    rkmod = {str(p):mod_rank(AZ,p) for p in PRIMES}
    need(all(v <= rank for v in rkmod.values()),'rank_specialization','modular rank exceeds rational rank')
    k = c['kernel']
    kdim = integer(k['rank'])
    need(0 <= kdim <= 2,'kernel_shape','invalid kernel rank')
    K = matrix(k['entries'],2,kdim,rational)
    need(rank_q(K) == kdim and kdim == 2-rank,'kernel_rank','kernel has wrong rank/nullity')
    need(all(sum(AQ[i][j]*K[i][q] for i in range(2)) == 0 for j in range(len(pts)) for q in range(kdim)),
         'left_kernel','A^T K is nonzero in rational source coordinates')
    for value in c['claim'].values():
        integer(value)
    need(c['claim'] == {'source_dimension':2,'target_dimension':1,'rank_Q':rank,'i_red':2-rank},
         'claim','claimed multiplicities differ from certified dimensions/rank')
    log.append({'check':'exact source arithmetic and left kernel','ok':True,
                'detail':{'A_Z':AZ,'row_denominators':den,'height_bounds':bounds,'CRT_modulus':M,
                          'ranks_mod_p':rkmod,'rank_Q':rank,'left_nullity':kdim}})
    return c['claim']


def verify(c):
    log = []
    start = time.perf_counter()
    try:
        claim = _check(c,log)
        result = {'status':'PASS','claim':claim,'checks':log}
    except Rejected as e:
        result = {'status':e.status,'code':e.code,'detail':e.detail,'checks':log}
    except (KeyError,TypeError,ValueError,IndexError,ZeroDivisionError) as e:
        result = {'status':'UNPARSEABLE','code':'malformed','detail':str(e),'checks':log}
    result['wall_seconds'] = time.perf_counter()-start
    return result


def load(path):
    need(Path(path).stat().st_size <= 5_000_000,'resource','certificate exceeds 5 MB','UNPARSEABLE')
    if str(path).endswith('.gz'):
        with gzip.open(path,'rb') as stream:
            raw = stream.read(5_000_001)
    else:
        raw = Path(path).read_bytes()
    need(len(raw) <= 5_000_000,'resource','expanded certificate exceeds 5 MB','UNPARSEABLE')
    def unique(pairs):
        out = {}
        for k,v in pairs:
            need(k not in out,'duplicate_key','duplicate JSON key: '+k,'UNPARSEABLE')
            out[k] = v
        return out
    return json.loads(raw.decode('utf-8-sig'),object_pairs_hook=unique)


def main():
    import argparse
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('certificate')
    ap.add_argument('--output')
    args = ap.parse_args()
    try:
        result = verify(load(args.certificate))
    except (OSError,ValueError,Rejected) as e:
        result = {'status':'UNPARSEABLE','code':'read','detail':str(e)}
    rendered = json.dumps(result,indent=2)+'\n'
    if args.output:
        Path(args.output).write_text(rendered,encoding='utf-8')
    print(rendered,flush=True)
    return 0 if result['status'] == 'PASS' else 1


if __name__ == '__main__':
    sys.exit(main())

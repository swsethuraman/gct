"""B17-11 sole bounded receiver. Fixed saved inputs only; no search.

Run with existing .venv/python.exe -B analysis/b15_bound.py, 60s / 512MiB.
01 arithmetic, LR, minor elimination and 06 controls are independent code.
05 point evaluation is explicitly a replay of the inspected producer circuit.
Never invokes producer main(), writes siblings, or runs symbolic expansion.
"""
from fractions import Fraction as Q
from itertools import product, permutations
from math import comb, isqrt
from pathlib import Path
from collections import defaultdict
import hashlib
import importlib.util
import json
import time

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'results/b17_11'
PROJECT = ROOT.parents[2]
WORKERS = ROOT.parent
START = time.perf_counter()
RESULT = {'status': 'RUNNING', 'checks': {}}


def need(ok, label):
    if not ok:
        raise AssertionError(label)


def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj


def det(matrix, p=None):
    """Independent row-normalized elimination; exact rationals or prime field."""
    a = [[v % p if p else Q(v) for v in row] for row in matrix]
    n, value = len(a), 1
    need(all(len(row) == n for row in a), 'square minor')
    for k in range(n):
        r = next((i for i in range(k, n) if a[i][k]), None)
        if r is None:
            return 0
        if r != k:
            a[k], a[r] = a[r], a[k]
            value = -value
        pivot = a[k][k]
        value *= pivot
        if p:
            value %= p
        inverse = pow(pivot, -1, p) if p else 1 / pivot
        a[k] = [(v * inverse) % p if p else v * inverse for v in a[k]]
        for i in range(k + 1, n):
            m = a[i][k]
            if m:
                a[i] = [(x-m*y) % p if p else x-m*y for x,y in zip(a[i],a[k])]
    return value % p if p else value


def pmul(a, b):
    c = defaultdict(int)
    for e,x in a.items():
        for f,y in b.items():
            c[tuple(i+j for i,j in zip(e,f))] += x*y
    return {e:x for e,x in c.items() if x}


def padd(*terms):
    c = defaultdict(int)
    for a in terms:
        for e,x in a.items():
            c[e] += x
    return {e:x for e,x in c.items() if x}


def scale(a, c):
    return {e:x*c for e,x in a.items() if x*c}


def derivative(a, k):
    return {tuple(v-int(i==k) for i,v in enumerate(e)):x*e[k]
            for e,x in a.items() if e[k]}


def mono(e):
    return {tuple(e):1}


def review01():
    cert = read(WORKERS/'B15-01/results/b17_01/certificate.json')
    A, p = cert['matrices_A0_to_A4'], cert['prime']
    need(all(p%d for d in range(2,isqrt(p)+1)), '01 prime')
    xs = [mono([int(i==j) for i in range(5)]) for j in range(5)]
    L = [[padd(*(scale(xs[k],A[k][i][j]) for k in range(5)))
          for j in range(3)] for i in range(3)]
    perm_terms = []
    for sig in permutations(range(3)):
        term = {(0,)*5:1}
        for i in range(3):
            term = pmul(term,L[i][sig[i]])
        perm_terms.append(term)
    cubic = padd(*perm_terms)
    exps = list(map(tuple,cert['cubic_exponents']))
    need([cubic.get(e,0) for e in exps] == cert['cubic_coefficients'], '01 full cubic')
    jac = []
    for k,i,j in product(range(5),range(3),range(3)):
        terms = []
        for sig in permutations(range(3)):
            if sig[i] == j:
                term = xs[k]
                for r in range(3):
                    if r != i:
                        term = pmul(term,L[r][sig[r]])
                terms.append(term)
        row = padd(*terms)
        jac.append([row.get(e,0) for e in exps])
    square = [jac[i] for i in cert['density']['selected_rows']]
    exact, modular = det(square), det(square,p)
    need(exact == int(cert['density']['minor_integer']), '01 rational minor')
    need(modular == cert['density']['minor_mod_prime'] == 17609, '01 modular minor')
    cols = list(map(tuple,cert['smoothness']['column_exponents']))
    need(len(cols)==len(set(cols))==210 and all(sum(e)==6 for e in cols), '01 sextic basis')
    grad = [derivative(cubic,i) for i in range(5)]
    smooth = []
    for i,beta in cert['smoothness']['selected_row_labels']:
        row = pmul(mono(beta),grad[i])
        smooth.append([row.get(e,0) for e in cols])
    sm = det(smooth,p)
    need(sm == cert['smoothness']['minor_mod_prime'] == 61614, '01 smoothness')
    frame = [[A[k][i][j] for k in range(5)] for i,j in product(range(3),repeat=2)]
    fm = det([frame[i] for i in cert['source_frame']['selected_rows']])
    need(fm == int(cert['source_frame']['minor_integer']) == 2562, '01 injective frame')
    need(all(L[i][j] for i,j in product(range(3),repeat=2)), '01 all entries')
    corrupt = [row[:] for row in square]
    corrupt[1] = corrupt[0][:]
    need(det(corrupt,p)==0, '01 duplicate Jacobian row control')
    singular = {(3,0,0,0,0):1}
    need(all(not any(v for e,v in derivative(singular,i).items() if e[0]==0) for i in range(5)), '01 singular cubic has projective gradient zero')
    signed = padd(*(scale(t,(-1)**sum(sig[i]>sig[j] for i in range(3) for j in range(i+1,3)))
                    for t,sig in zip(perm_terms,permutations(range(3)))))
    need(signed != cubic, '01 determinant/permanent sign mutation')
    return {'density_minor_integer':str(exact),'density_minor_mod':modular,
            'smoothness_minor_mod':sm,'frame_minor':int(fm),'all_1575_jacobian_entries_constructed':True,
            'controls':['duplicate Jacobian row','singular x0^3','permanent sign mutation'],
            'independent_of_worker_arithmetic':True}


def lr(content):
    """All LR tableaux in the fixed eight-box skew shape; no worker enumerator."""
    outer,inner=(69,19)+(2,)*8,(65,17)+(2,)*7+(0,)
    boxes=[(i,j) for i in range(10) for j in range(outer[i],inner[i],-1)]
    good=[]
    for word in product(range(1,len(content)+1),repeat=8):
        if any(word.count(k+1)!=n for k,n in enumerate(content)):
            continue
        filled=dict(zip(boxes,word))
        if any((i,j+1) in filled and filled[i,j]>filled[i,j+1] for i,j in boxes):
            continue
        if any((i-1,j) in filled and filled[i-1,j]>=filled[i,j] for i,j in boxes):
            continue
        if any(any(word[:r].count(k)<word[:r].count(k+1) for k in range(1,len(content))) for r in range(1,9)):
            continue
        good.append(word)
    return good


def review05():
    cert=read(WORKERS/'B15-05/results/b17_05/image_certificate.json')
    p=cert['field_prime']
    need(all(p%d for d in range(2,isqrt(p)+1)), '05 prime')
    tableaux=[lr(c) for c in ((8,),(6,2),(4,4))]
    need(list(map(len,tableaux))==[1,3,1], '05 independent LR ceiling')
    worker=load('b17_11_replayed05',WORKERS/'B15-05/analysis/b17_05_verify.py')
    inherited=load('b17_11_inherited_hessian',PROJECT/'Batch15_Launch/native_20260913/reviews_filesystem/Hessian11_1631/verify_small.py')
    # No producer main, no symbolic(), no point search. Replay fixed ten inputs.
    Vinv=worker.nmod_mat([[pow(t,k,p) for k in range(21)] for t in range(21)],p).inv()
    products,basis=[],[]
    for i,pt in enumerate(cert['points'][:10]):
        row,E=worker.point(pt['N'],Vinv,inherited)
        need(row==cert['product_rows'][i], '05 replay product row')
        E=[E[j] for j in (0,1,2,3,4,5,6,7,8,10,11)]
        need(E==cert['basis_rows'][i], '05 replay E order')
        products.append(row)
        basis.append(E)
    m5=det([products[i] for i in cert['selected_rows']],p)
    need(m5==cert['minor5']==77620181, '05 independent 5 minor')
    def fq(x):
        q=Q(x)
        return q.numerator*pow(q.denominator,-1,p)%p
    augmented=[r+[sum(fq(v)*x for v,x in zip(rep['rational_E_coordinates'],E))%p
                  for rep in cert['quotient_representatives']] for r,E in zip(products,basis)]
    square=[augmented[i] for i in cert['quotient_rows']]
    need(square==cert['quotient_matrix'], '05 independent quotient reconstruction')
    m10=det(square,p)
    need(m10==cert['quotient_minor10']==1583314678,'05 independent 10 minor')
    broken=[r[:] for r in square]
    broken[1]=broken[0][:]
    need(det(broken,p)==0,'05 duplicate row')
    broken=[r[:] for r in square]
    for r in broken:
        r[5]=r[0]
    need(det(broken,p)==0,'05 image column passed as quotient representative')
    return {'source_counts':[len(t) for t in tableaux],'LR_tableaux':tableaux,'minor5':m5,'minor10':m10,
            'fixed_points_replayed':10,'inherited_formula_controls':30,
            'independent':['LR enumeration','modular elimination','quotient reconstruction','duplicate/image-column controls'],
            'shared':['05 point circuit implementation','historical Hessian candidates'],
            'not_replayed':['B16 stable completeness','B16 universal pole proof','last four unused saved points']}


def compositions(d,n):
    if n==1:
        yield (d,)
    else:
        for k in range(d+1):
            for rest in compositions(d-k,n-1):
                yield (k,)+rest


def review06():
    # Dual numbers compute only the two required Hasse rows, no six-y expansion.
    def dm(a,b): return (a[0]*b[0],a[0]*b[1]+a[1]*b[0])
    def da(a,b): return (a[0]+b[0],a[1]+b[1])
    def ds(c,a): return (c*a[0],c*a[1])
    def conv(a,b):
        z=[(0,0)]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b): z[i+j]=da(z[i+j],dm(x,y))
        return z
    def values(weights,last=5):
        base=[[[1,1],[2],[1]],[[3],[1,1],[2]],[[2],[1],[last,1]]]
        coef=[(0,0)]*5
        for sig in permutations(range(3)):
            term=[(2,0),(1,0)]
            for i,j in enumerate(sig):
                term=conv(term,[(v,weights[3*i+j]*v) for v in base[i][j]])
            for k,v in enumerate(term): coef[k]=da(coef[k],v)
        c,a1,a2,a3,a4=reversed(coef)
        h=da(ds(8,dm(c,a2)),ds(-3,dm(a1,a1)))
        I=da(da(dm(a2,a2),ds(-3,dm(a1,a3))),ds(12,dm(c,a4)))
        return dm(dm(dm(c,c),c),I),dm(c,dm(h,h))
    simple=values([0,1,0,0,0,0,0,0,0])
    encoded=values([0,0,0,0,1,6,0,36,216])
    need(simple==((-59,-18),(1369,3552)), '06 dual number simple arc')
    need(encoded==((-59,-67494),(1369,1018869)), '06 dual number encoded arc')
    minors=[a[0]*b[1]-a[1]*b[0] for a,b in (simple,encoded)]
    need(minors==[-184926,32286015], '06 minors')
    old=values([0,1,0,0,0,0,0,0,0],4)
    need(old[0][0]==49 and old[1]==tuple(64*x for x in old[0]), '06 old-base control')
    perms=list(permutations(range(3)))
    def image(a):
        return tuple(sum(a[k] for k,s in enumerate(perms) if s[i]==j) for i,j in product(range(3),repeat=2))
    counts=[]
    for d in range(6):
        exps={image(a) for a in compositions(d,6)}
        expected=comb(d+5,5)-(comb(d+2,5) if d>=3 else 0)
        need(len(exps)==expected,'06 independent incidence support')
        need(len({sum(T[j]*(d+1)**i for i,j in enumerate((4,5,7,8))) for T in exps})==expected,'06 arc injectivity')
        counts.append(expected)
    even=tuple(int(sum(s[i]>s[j] for i in range(3) for j in range(i+1,3))%2==0) for s in perms)
    odd=tuple(1-x for x in even)
    need(image(even)==image(odd)==(1,)*9,'06 cancellation collision')
    return {'simple_minor':minors[0],'encoded_minor':minors[1],'supports':counts,
            'old_base_rank_one_control':True,'signed_collision_image':[1]*9,
            'independent_dual_number_arithmetic':True}


def review07():
    # Exact coefficient identities in (t,x,y,z), derived from adjugate quadrics.
    t,x,y,z=[mono([int(i==j) for i in range(4)]) for j in range(4)]
    sq=lambda a:pmul(a,a)
    F=padd(sq(x),pmul(t,pmul(y,z)))
    G=padd(sq(x),pmul(t,sq(y)),pmul(sq(t),sq(z)))
    a,b,c=[derivative(F,i) for i in (1,2,3)]
    need(padd(pmul(t,sq(a)),scale(pmul(b,c),4))==scale(pmul(t,F),4),'07 dual F')
    need(padd(pmul(t,sq(a)),scale(pmul(b,c),-4))!=scale(pmul(t,F),4),'07 wrong sign')
    a,b,c=[derivative(G,i) for i in (1,2,3)]
    need(padd(pmul(sq(t),sq(a)),pmul(t,sq(b)),sq(c))==scale(pmul(sq(t),G),4),'07 dual G')
    need((9-5)*comb(8,4)==280,'07 Segre target')
    return {'universal_dual_identities':2,'wrong_sign_rejected':True,'delta7_det5':280,'delta7_per3':'UNCOMPUTED'}


def main():
    need(not (OUT/'verification.json').exists(),'preserve single-run receipt')
    pins=read(OUT/'input_hashes.json')['files']
    for row in pins:
        need(hashlib.sha256(Path(row['path']).read_bytes()).hexdigest()==row['sha256'],'input hash '+row['path'])
    RESULT['input_hashes_checked']=len(pins)
    for slot,fn in [('01',review01),('05',review05),('06',review06),('07',review07)]:
        RESULT['checks'][slot]=fn()
        print(json.dumps({'slot':slot,'status':'PASS','seconds_so_far':time.perf_counter()-START}),flush=True)
    RESULT.update(status='PASS',seconds=time.perf_counter()-START,
                  scope='Fixed-input receiver only; theorem review in report, no candidate search',
                  mathematical_processes=1,positive_gap=False)


if __name__=='__main__':
    try:
        main()
    except BaseException as exc:
        RESULT.update(status='FAIL',error=repr(exc),seconds=time.perf_counter()-START)
        raise
    finally:
        (OUT/'verification.json').write_text(json.dumps(RESULT,indent=2)+'\n',encoding='utf-8')

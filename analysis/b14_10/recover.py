"""Independent stdlib replay of four compact, integral catalecticant certificates.

No analysis/ producer code or modular HWV is imported. Rows are shifted quadratic
monomials; columns are linear variables. Each entry is alpha! [s^alpha] per3.
"""
import argparse, collections, copy, hashlib, itertools, json, math, pathlib, time

ROOT=pathlib.Path(__file__).resolve().parents[2]
PRIMES=(2147483647,2147483629)
CELLS=((7,5,5,2,2,1,1,1),(7,6,3,3,2,1,1,1),(8,5,3,2,2,2,1,1),(9,4,2,2,2,2,2,1))

def det_bareiss(a):
    a=[r[:] for r in a]; n=len(a)
    if not n or any(len(r)!=n for r in a): raise ValueError('nonempty square matrix required')
    sign=1; divisor=1
    for k in range(n-1):
        pivot=next((i for i in range(k,n) if a[i][k]),None)
        if pivot is None: return 0
        if pivot!=k: a[k],a[pivot]=a[pivot],a[k];sign=-sign
        value=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                v=a[i][j]*value-a[i][k]*a[k][j]
                assert v%divisor==0, 'Bareiss nonexact division'
                a[i][j]=v//divisor
            a[i][k]=0
        divisor=value
    return sign*a[-1][-1]

def sign_of(p): return -1 if sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2 else 1

def det_leibniz(a):
    return sum(sign_of(p)*math.prod(a[i][p[i]] for i in range(len(a))) for p in itertools.permutations(range(len(a))))

def per3(pencil):
    r=len(pencil)
    assert r and all(len(row)==9 and all(type(x) is int for x in row) for row in pencil)
    out=collections.defaultdict(int)
    for p in itertools.permutations(range(3)):
        for ijk in itertools.product(range(r),repeat=3):
            coeff=math.prod(pencil[ijk[i]][3*i+p[i]] for i in range(3))
            alpha=[0]*r
            for i in ijk: alpha[i]+=1
            out[tuple(alpha)]+=coeff
    return {k:v for k,v in out.items() if v}

def alpha(i,j,k,r):
    a=[0]*r
    for x in (i,j,k): a[x]+=1
    return tuple(a)

def afact(a): return math.prod(math.factorial(i) for i in a)

def diagram(nu): return [(i,j) for i,w in enumerate(nu) for j in range(i,i+w)]

def matrix(nu,pencil,normalized=True):
    r=len(pencil); coeffs=per3(pencil)
    return [[(afact(alpha(i,j,k,r)) if normalized else 1)*coeffs.get(alpha(i,j,k,r),0)
             for k in range(r)] for i,j in diagram(nu)]

def polynomial(nu,r):
    pairs=diagram(nu); out=collections.defaultdict(int)
    for p in itertools.permutations(range(r)):
        factors=tuple(sorted(alpha(i,j,p[t],r) for t,(i,j) in enumerate(pairs)))
        out[factors]+=sign_of(p)*math.prod(afact(a) for a in factors)
    return {m:c for m,c in out.items() if c}

def hwv(poly,weight):
    if not poly: return False
    r=len(weight)
    for mon,c in poly.items():
        if not c or len(mon)!=r or tuple(sum(a[i] for a in mon) for i in range(r))!=tuple(weight): return False
    for i in range(r-1):
        derivative=collections.defaultdict(int)
        for mon,c in poly.items():
            for k,a in enumerate(mon):
                if not a[i+1]: continue
                b=list(a);b[i]+=1;b[i+1]-=1
                new=tuple(sorted(mon[:k]+(tuple(b),)+mon[k+1:]))
                derivative[new]+=c*(a[i]+1)
        if any(derivative.values()): return False
    return True

def poly_hash(poly):
    return hashlib.sha256(json.dumps(sorted(poly.items()),separators=(',',':')).encode()).hexdigest()

def verify(cert,check_hwv=True):
    required={'format','kind','cell','nu','point','matrix','determinant_Z','determinants_mod_p','proof_dependency',
              'polynomial_terms_sha256','normalization','matrix_orientation','values_are','coefficient_denominators'}
    if not required<=cert.keys(): raise ValueError('required certificate input missing')
    assert cert['format']=='b14-10-catalecticant/1' and cert['kind']=='integral_nonvanishing'
    c=cert['cell'];r=c['ell'];nu=cert['nu'];weight=c['lambda']
    assert c['n']==3 and c['delta']==r==8 and len(weight)==r and sum(weight)==3*r
    assert nu and all(type(x) is int and x>0 for x in nu) and sum(nu)==r and all(nu[i]>nu[i+1] for i in range(len(nu)-1))
    pairs=diagram(nu); expected=[1]*r
    for i,j in pairs: expected[i]+=1;expected[j]+=1
    assert expected==weight, 'shifted-diagram weight mismatch'
    assert cert['point']['type']=='permanent_pencil' and len(cert['point']['pencil'])==r
    assert cert['normalization']=='alpha! times plain cubic coefficient'
    assert cert['values_are']=='integer catalecticant entries alpha! * c_alpha(per3(pencil))'
    assert cert['matrix_orientation']=='rows: shifted quadratic diagram; columns: s_1,...,s_8'
    assert cert['coefficient_denominators']==[1]
    assert cert['proof_dependency']=='PROVED:top_cells_catalecticant'
    rebuilt=matrix(nu,cert['point']['pencil'])
    assert rebuilt==cert['matrix']['values'], 'matrix entry differs from rebuilt pencil'
    assert cert['matrix']['values_are']==cert['values_are']
    d=det_bareiss(rebuilt)
    assert d==int(cert['determinant_Z'])==det_leibniz(rebuilt) and d!=0, 'nonzero integer determinant mismatch'
    assert set(cert['determinants_mod_p'])==set(map(str,PRIMES))
    assert all(cert['determinants_mod_p'][str(p)]==d%p!=0 for p in PRIMES)
    assert all(math.gcd(p,6)==1 for p in PRIMES)
    if check_hwv:
        poly=polynomial(nu,r)
        assert poly_hash(poly)==cert['polynomial_terms_sha256']
        assert hwv(poly,weight), 'integer highest-weight check failed'
    return True

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--index',type=int);ap.add_argument('--verify')
    a=ap.parse_args()
    if a.verify:
        cert=json.loads(pathlib.Path(a.verify).read_text());verify(cert);print('CERTIFIED compact integral witness');return
    assert a.index in range(4)
    start=time.monotonic();weight=CELLS[a.index]
    bank=json.loads((ROOT/'results/b13_05_topcells.json').read_text())
    rows=[r for r in bank['cells'] if tuple(r['mu'])==weight and r['delta']==8]
    assert len(rows)==1
    row=rows[0];pencil=row['pencils'][0]['pencil'];nu=row['nu'];poly=polynomial(nu,8)
    assert hwv(poly,weight), 'new independent exact raising check'
    m=matrix(nu,pencil);d=det_bareiss(m)
    assert d==int(row['pencils'][0]['det']) and [d%p for p in PRIMES]==row['pencils'][0]['det_mod']
    values_are='integer catalecticant entries alpha! * c_alpha(per3(pencil))'
    cert=dict(format='b14-10-catalecticant/1',kind='integral_nonvanishing',board_numbering='batch14',
              actual_model='gpt-6-astra',cell=dict(n=3,ell=8,delta=8,**{'lambda':list(weight)}),nu=nu,
              point=dict(type='permanent_pencil',pencil=pencil),
              matrix=dict(values_are=values_are,shape=[8,8],values=m),values_are=values_are,
              determinant_Z=str(d),determinants_mod_p={str(p):d%p for p in PRIMES},
              normalization='alpha! times plain cubic coefficient',coefficient_denominators=[1],
              tensor_coordinate_scale_factors=[1,2,6],matrix_orientation='rows: shifted quadratic diagram; columns: s_1,...,s_8',
              proof_dependency='PROVED:top_cells_catalecticant',polynomial_terms_sha256=poly_hash(poly),
              polynomial_nonzero_terms=len(poly),source='results/b13_05_topcells.json',
              source_sha256=hashlib.sha256((ROOT/'results/b13_05_topcells.json').read_bytes()).hexdigest(),
              recovery_semantics='new exact replacement for two absent B13-09 prime certificates; original bytes remain missing',
              conclusion='mult_per3(lambda,8)=a=1; i_per3(lambda,8)=0 over Q; no new frontier closure')
    assert verify(cert)
    controls=[]
    def reject(name,mutator):
        bad=copy.deepcopy(cert);mutator(bad)
        try: verify(bad,check_hwv=False)
        except (AssertionError,ValueError,KeyError,TypeError): controls.append(dict(name=name,rejected=True))
        else: raise AssertionError(name+' did not fail')
    reject('altered_matrix_entry',lambda b:b['matrix']['values'][0].__setitem__(0,b['matrix']['values'][0][0]+1))
    reject('altered_determinant',lambda b:b.__setitem__('determinant_Z',str(d+1)))
    reject('wrong_tensor_normalization',lambda b:b['matrix'].__setitem__('values',matrix(nu,pencil,False)))
    reject('missing_point',lambda b:b.pop('point'))
    reject('wrong_degree',lambda b:b['cell'].__setitem__('delta',9))
    bad_poly=poly.copy();term=next(iter(bad_poly));bad_poly[term]+=1
    assert not hwv(bad_poly,weight);controls.append(dict(name='altered_HWV_coefficient',rejected=True))
    zero=[[0]*9 for _ in range(8)]
    diag=[[pencil[t][k] if k in (0,4,8) else 0 for k in range(9)] for t in range(8)]
    for name,pt in [('zero_pencil',zero),('diagonal_per3_forced_zero',diag)]:
        assert det_bareiss(matrix(nu,pt))==0
        reject(name,lambda b,pt=pt:b['point'].__setitem__('pencil',pt))
    out=ROOT/'results/b14_10/recovered';out.mkdir(parents=True,exist_ok=True)
    name='cubic8_'+ '_'.join(map(str,weight))
    (out/(name+'.json')).write_text(json.dumps(cert,indent=2)+'\n')
    result=dict(cell=cert['cell'],status='CERTIFIED',certificate='results/b14_10/recovered/'+name+'.json',
                arithmetic='exact integers, independent polynomial raising and two determinant algorithms',
                controls=controls,terms=len(poly),elapsed_seconds=round(time.monotonic()-start,4),
                original_certificate_bytes_recovered=False)
    (out/(name+'.validation.json')).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))

if __name__=='__main__':main()

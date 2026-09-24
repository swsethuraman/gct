"""R27-03 independent finite checks: sparse polynomial arithmetic and Macaulay minors.
No producer mathematical code is imported. The sole premise is the committed witness.
"""
import hashlib, itertools, json, math, pathlib, subprocess, sys
from collections import defaultdict
from functools import lru_cache

ROOT = pathlib.Path('C:/Users/swami/Projects/gct-gpt/work/batch27/b27-03r')
TIP = '7c36a52ddf338eb390a9bcd491cb9c50cf9e2a19'
raw = subprocess.check_output(['git','-c','safe.directory='+ROOT.as_posix(),'-C',str(ROOT),
                               'show',TIP+':results/b27_03/witness.json'])
witness = json.loads(raw)
P = 32003

def exponents(n, d):
    if n == 1:
        yield (d,)
    else:
        for a in range(d, -1, -1):
            for b in exponents(n-1,d-a): yield (a,)+b
def mul(a,b):
    out=defaultdict(int)
    for u,c in a.items():
        for v,d in b.items(): out[tuple(x+y for x,y in zip(u,v))] += c*d
    return {u:c for u,c in out.items() if c}
def linear(row): return {tuple(int(i==j) for i in range(5)):c for j,c in enumerate(row) if c}

rows=witness['T_prime_10x5_rows_z_y11_to_y33']
forms=list(map(linear,rows))
cubic=defaultdict(int)
for perm in itertools.permutations(range(3)):
    term={(0,)*5:1}
    for r in range(3): term=mul(term,forms[1+3*r+perm[r]])
    for a,c in term.items(): cubic[a]+=c
cubic={a:c for a,c in cubic.items() if c}
quartic=mul(forms[0],cubic)
E70=list(exponents(5,4)); E65=[a for a in E70 if max(a)>=2]
retained=[[list(a),quartic.get(a,0)] for a in E65]
omitted=[[list(a),quartic.get(a,0)] for a in E70 if max(a)==1]
assert retained==witness['pi_PT_65'] and omitted==witness['omitted_K5_coefficients']

def gradient_matrix(poly,n,degree):
    cols=list(exponents(n,degree)); index={a:i for i,a in enumerate(cols)}
    deriv=[]
    for j in range(n):
        part={}
        for a,c in poly.items():
            if a[j]:
                b=list(a); b[j]-=1; part[tuple(b)]=a[j]*c
        deriv.append(part)
    matrix=[]
    for part in deriv:
        for shift in exponents(n,degree-2):
            row=[0]*len(cols)
            for a,c in part.items(): row[index[tuple(x+y for x,y in zip(a,shift))]]=c
            matrix.append(row)
    return matrix

def eliminate(matrix):
    a=[[v%P for v in row] for row in matrix]
    labels=list(range(len(a))); r=0; pivots=[]
    for col in range(len(a[0])):
        found=next((j for j in range(r,len(a)) if a[j][col]),None)
        if found is None: continue
        a[r],a[found]=a[found],a[r]; labels[r],labels[found]=labels[found],labels[r]
        pivots.append(labels[r])
        inv=pow(a[r][col],-1,P)
        top=[v*inv%P for v in a[r][col:]]
        for j in range(r+1,len(a)):
            f=a[j][col]
            if f: a[j][col:]=[(v-f*t)%P for v,t in zip(a[j][col:],top)]
        r+=1
        if r==len(a): break
    return r,pivots

def determinant_mod(matrix):
    a=[[v%P for v in row] for row in matrix]; det=1; n=len(a)
    for i in range(n):
        j=next(j for j in range(i,n) if a[j][i])
        if j!=i: a[j],a[i]=a[i],a[j]; det=-det
        v=a[i][i]; det=det*v%P; inv=pow(v,-1,P)
        for j in range(i+1,n):
            f=a[j][i]*inv%P
            if f:
                for k in range(i,n): a[j][k]=(a[j][k]-f*a[i][k])%P
    return det%P

def certificate(poly,n,degree):
    matrix=gradient_matrix(poly,n,degree)
    rank,pivots=eliminate(matrix)
    square=[matrix[j] for j in pivots]
    full=rank==len(matrix[0])
    return {'n':n,'degree':degree,'shape':[len(matrix),len(matrix[0])],
            'rank_mod_32003':rank,'full_column_rank':full,'selected_original_rows':pivots,
            'minor_determinant_mod_32003':determinant_mod(square) if full else None,
            'matrix_sha256':hashlib.sha256(json.dumps(matrix,separators=(',',':')).encode()).hexdigest()}

main=certificate(cubic,5,6)
assert main['full_column_rank']
planes=[]
for keep in itertools.combinations(range(5),3):
    restricted={tuple(a[j] for j in keep):c for a,c in cubic.items()
                if all(a[j]==0 for j in range(5) if j not in keep)}
    rec=certificate(restricted,3,4); rec['plane']=[j+1 for j in keep]; planes.append(rec)
expected=[i for i,row in enumerate(witness['ternary_restrictions']) if row['smooth']]
assert [i for i,row in enumerate(planes) if row['full_column_rank']]==expected

# Independent recursive coefficient count with memoization; no determinant evaluation.
def dimension(k,w):
    eligible=tuple(a for a in E65 if all(x<=y for x,y in zip(a,w)))
    @lru_cache(None)
    def count(start,left,rem):
        if left==0: return int(not any(rem))
        if start==len(eligible): return 0
        total=0
        for j in range(start,len(eligible)):
            a=eligible[j]
            if all(x<=y for x,y in zip(a,rem)):
                total+=count(j,left-1,tuple(y-x for x,y in zip(a,rem)))
        return total
    value=count(0,k,tuple(w)); states=count.cache_info().currsize
    count.cache_clear()
    return {'k':k,'w':list(w),'dim65':value,'memoized_states':states}

dims=[dimension(10,(30,4,2,2,2)),dimension(10,(30,3,3,2,2))]
primes={str(p):all(p%d for d in range(2,math.isqrt(p)+1)) for p in (32003,1_000_000_007)}
assert all(primes.values())
out={'input_witness_sha256':hashlib.sha256(raw).hexdigest(),
     'method':'Independent sparse six-term permanent; gradient-ideal Macaulay matrices and explicit nonzero minors.',
     'coefficient_rows_match':True,'nonzero_retained':sum(c!=0 for _,c in retained),
     'omitted':omitted,'cubic_monomials':[[list(a),c] for a,c in sorted(cubic.items(),reverse=True)],
     'smooth_cubic_certificate':main,'coordinate_plane_certificates':planes,
     'good_plane_count':len(expected),'next_stable_degree_dimensions':dims,
     'prime_checks_by_trial_division':primes,
     'dense_degree5_parameter_monomial_bound':math.comb(75,25)}
pathlib.Path(sys.argv[1]).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'smooth_rank':main['rank_mod_32003'],'good_planes':len(expected),'dims':dims,
                  'degree5_bound':out['dense_degree5_parameter_monomial_bound']}))

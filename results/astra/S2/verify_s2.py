"""S2 focused exact verification. Python standard library only; no sampled upper bounds."""
from pathlib import Path
from fractions import Fraction as F
from itertools import permutations, product
import json, random, datetime, math
OUT=Path(__file__).resolve().parent
P1,P2=2147483647,2147483629

def exps(d,n):
    if n==1: return [(d,)]
    return [(i,)+e for i in range(d+1) for e in exps(d-i,n-1)]
def add(a,b):
    c=a.copy()
    for e,v in b.items():
        c[e]=c.get(e,0)+v
        if not c[e]: del c[e]
    return c
def scale(a,c): return {e:v*c for e,v in a.items() if v*c}
def mul(a,b):
    c={}
    for e,v in a.items():
        for f,w in b.items():
            g=tuple(x+y for x,y in zip(e,f)); c[g]=c.get(g,0)+v*w
    return {e:v for e,v in c.items() if v}
def var(i,n): return {tuple(int(j==i) for j in range(n)):1}
def one(n): return {(0,)*n:1}
def det(M):
    n=len(M)
    if n==1: return M[0][0]
    r={}
    for j in range(n): r=add(r,scale(mul(M[0][j],det([[M[i][k] for k in range(n) if k!=j] for i in range(1,n)])),(-1)**j))
    return r
def adj(M):
    n=len(M)
    return [[scale(det([[M[r][c] for c in range(n) if c!=i] for r in range(n) if r!=j]),(-1)**(i+j)) for j in range(n)] for i in range(n)]
def dot(a,b):
    r={}
    for x,y in zip(a,b): r=add(r,mul(x,y))
    return r
def mv(A,b): return [dot(row,b) for row in A]
def coeff(p,E): return [p.get(e,0) for e in E]
def ev(p,x): return sum(v*math.prod(t**i for t,i in zip(x,e)) for e,v in p.items())
def rref(A,p=None):
    A=[[F(x).numerator*pow(F(x).denominator,-1,p)%p for x in row] if p else list(map(F,row)) for row in A]; r=0; piv=[]; ids=list(range(len(A)))
    if not A:return A,piv,[]
    chosen=[]
    for j in range(len(A[0])):
        k=next((k for k in range(r,len(A)) if A[k][j]),None)
        if k is None:continue
        A[r],A[k]=A[k],A[r]; ids[r],ids[k]=ids[k],ids[r]; chosen.append(ids[r])
        q=pow(A[r][j],-1,p) if p else 1/A[r][j]
        A[r]=[(x*q)%p for x in A[r]] if p else [x*q for x in A[r]]
        for k in range(len(A)):
            if k==r or not A[k][j]:continue
            q=A[k][j]
            A[k]=[(x-q*y)%p for x,y in zip(A[k],A[r])] if p else [x-q*y for x,y in zip(A[k],A[r])]
        piv.append(j);r+=1
        if r==len(A):break
    return A,piv,chosen
def numeric_det(A):
    # Leibniz, independent of polynomial cofactor expansion and RREF.
    n=len(A);s=0
    for pi in permutations(range(n)):
        sg=(-1)**sum(pi[i]>pi[j] for i in range(n) for j in range(i+1,n))
        s+=sg*math.prod(A[i][pi[i]] for i in range(n))
    return s
def rankcert(A):
    rr,cols,rows=rref(A);k=len(cols)
    # Bareiss determinant (independent of RREF) for potentially large minors.
    B=[[F(A[i][j]) for j in cols] for i in rows];prev=F(1);sign=1
    for i in range(k-1):
        j=next(j for j in range(i,k) if B[j][i])
        if j!=i:B[i],B[j]=B[j],B[i];sign=-sign
        q=B[i][i]
        for r in range(i+1,k):
            for c in range(i+1,k):B[r][c]=(q*B[r][c]-B[r][i]*B[i][c])/prev
            B[r][i]=0
        prev=q
    minor=sign*B[-1][-1] if k else F(1)
    assert minor
    # Exact kernel gives matching rational upper bound for THIS stored matrix.
    free=[j for j in range(len(A[0])) if j not in cols];kernel=[]
    for j in free:
        v=[F(0)]*len(A[0]);v[j]=1
        for i,c in enumerate(cols):v[c]=-rr[i][j]
        assert all(sum(x*y for x,y in zip(row,v))==0 for row in A);kernel.append(v)
    assert len(kernel)+k==len(A[0])
    ranks={str(p):len(rref(A,p)[1]) for p in (P1,P2)}
    assert all(v==k for v in ranks.values())
    minor_mod={str(p):minor.numerator*pow(minor.denominator,-1,p)%p for p in (P1,P2)}
    assert all(minor_mod.values())
    return dict(rank_Q=k,house_prime_ranks=ranks,rows=rows,cols=cols,minor=str(minor),minor_mod=minor_mod,kernel=kernel)
def quotient_matrix(B,b):
    E=exps(4,4);V=[var(i,4) for i in range(4)];f=det(B)
    rel=[coeff(mul(f,v),E) for v in V];RR,piv,_=rref(rel)
    assert len(piv)==4
    keep=[i for i in range(35) if i not in piv]
    ab=mv(adj(B),b);cols=[]
    for j in range(3):
        for v in V:
            c=list(map(F,coeff(mul(ab[j],v),E)))
            for i,p in enumerate(piv):
                q=c[p];c=[a-q*z for a,z in zip(c,RR[i])]
            assert all(c[p]==0 for p in piv);cols.append([c[i] for i in keep])
    A=[list(row) for row in zip(*cols)]
    return dict(B=B,b=b,f=f,quartic_exponents=E,quotient_kept_indices=keep,relation_rref=RR,
                columns=[(j,i) for j in range(3) for i in range(4)],matrix=A,certificate=rankcert(A))
def jsonable(x):
    if isinstance(x,F):return int(x) if x.denominator==1 else str(x)
    if isinstance(x,dict):
        if x and all(isinstance(k,tuple) for k in x):return [[list(k),jsonable(v)] for k,v in sorted(x.items())]
        return {str(k):jsonable(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [jsonable(v) for v in x]
    return x
def write(name,x):(OUT/name).write_text(json.dumps(jsonable(x),indent=2),encoding='utf-8')

def focused_ranks():
    x,y,z,w=[var(i,4) for i in range(4)];Z={}
    Bint=[[x,y,Z],[Z,x,z],[w,Z,x]]
    Bred=[[x,w,Z],[Z,y,Z],[Z,Z,z]]
    cases={
      'integral_rank9':(Bint,[w,Z,Z]),
      'integral_rank0':(Bint,[x,Z,w]), # first column B
      'reducible_rank3':(Bred,[w,Z,Z]),
    }
    result={name:quotient_matrix(B,b) for name,(B,b) in cases.items()}
    assert [result[k]['certificate']['rank_Q'] for k in cases]==[9,0,3]
    # Symbolic cofactor identity on arbitrary linear b for the two exact examples.
    for B in [Bint,Bred]:
        A=adj(B);f=det(B)
        for i in range(3):
            for j in range(3):assert dot(A[i],[B[k][j] for k in range(3)])==(f if i==j else {})
    # Additional rank9 at a fresh deterministic integer b, not a random search.
    b=[[2,-1,3,1],[-2,1,0,4],[1,1,-1,2]]
    bp=[{tuple(int(k==i) for k in range(4)):a for i,a in enumerate(row) if a} for row in b]
    result['integral_fresh_rank9']=quotient_matrix(Bint,bp)
    assert result['integral_fresh_rank9']['certificate']['rank_Q']==9
    write('ker_coker_certificates.json',result)
    return {k:v['certificate']['rank_Q'] for k,v in result.items()}

def differential_calibration():
    V=[var(i,5) for i in range(5)];E=exps(4,5); rng=random.Random(660072)
    mask1={(r,c) for r in range(1,4) for c in (2,3)}
    mask2={(r,c) for r in (2,3) for c in (1,2,3)}
    mask=mask1|mask2
    points=[[[rng.randint(-7,7) if (r,c) not in mask else 0 for c in range(4)] for r in range(4)] for k in range(5)]
    M=[[{tuple(int(i==k) for i in range(5)):points[k][r][c] for k in range(5) if points[k][r][c]} for c in range(4)] for r in range(4)]
    assert det(M)=={}
    Ad=adj(M);cols=[]
    for k in range(5):
        for r in range(4):
            for c in range(4):
                q=mul(Ad[c][r],V[k]);N=[[entry.copy() for entry in row] for row in M]
                N[r][c]=add(N[r][c],V[k])
                assert det(N)==q # determinant is affine in this entry, det M=0
                cols.append(coeff(q,E))
    D=[list(v) for v in zip(*cols)]
    def tang(missing):
        T=[]
        for k in range(5):
            for r in range(4):
                for c in range(4):
                    if (r,c) not in missing:
                        v=[0]*80;v[16*k+4*r+c]=1;T.append(v)
        for r in range(4):
            for c in range(4):
                L=[0]*80;R=[0]*80
                for k in range(5):
                    for j in range(4):
                        L[16*k+4*r+j]=points[k][c][j]
                        R[16*k+4*j+c]=points[k][j][r]
                T.extend([L,R])
        assert all(all(sum(x*y for x,y in zip(row,v))==0 for row in D) for v in T)
        return T
    T1,T2=tang(mask1),tang(mask2)
    rec=dict(seed=660072,point=points,row_exponents=E,column_order='(k,r,c), each ascending, 0-based',dPhi=D,
       certificate=rankcert(D),T_c21=T1,T_c32=T2)
    rec['tangent_ranks']={str(p):[len(rref(T,p)[1]) for T in (T1,T2,T1+T2)] for p in (P1,P2)}
    rec['tangent_certificates_Q']=[rankcert(T) for T in (T1,T2,T1+T2)]
    assert rec['certificate']['rank_Q']==16
    assert all(v==[57,57,64] for v in rec['tangent_ranks'].values())
    rec['kernel_dim']=64;rec['intersection_dim']=50;rec['transverse_quotient_dim']=0
    write('tangent_calibration.json',rec)
    return dict(rank_dPhi=16,kernel=64,tangents=[57,57],intersection=50,span=64,quotient=0)

def numeric_jet_checks():
    rng=random.Random(20260908);checks=[]
    # t^2 coefficient by Lagrange interpolation on 0,...,8; independent of cofactor path.
    def weight2(k):
        poly=[F(1)];den=1
        for j in range(9):
            if j==k:continue
            nxt=[F(0)]*(len(poly)+1)
            for i,c in enumerate(poly):nxt[i]-=j*c;nxt[i+1]+=c
            poly=nxt;den*=k-j
        return poly[2]/den
    weights=[weight2(k) for k in range(9)]
    for case in range(8):
        B=[[rng.randint(-5,5) for _ in range(3)] for _ in range(3)]
        b=[rng.randint(-5,5) for _ in range(3)];c=[rng.randint(-5,5) for _ in range(3)]
        A=[[rng.randint(-5,5) for _ in range(3)] for _ in range(3)];H=[[rng.randint(-5,5) for _ in range(4)] for _ in range(4)]
        M0=[row+[0] for row in B]+[[0]*4];N=[A[i]+[b[i]] for i in range(3)]+[c+[0]]
        vals=[numeric_det([[M0[i][j]+t*N[i][j]+t*t*H[i][j] for j in range(4)] for i in range(4)]) for t in range(9)]
        observed=sum(v*w for v,w in zip(vals,weights))
        adjnum=[[(-1)**(i+j)*numeric_det([[B[r][s] for s in range(3) if s!=i] for r in range(3) if r!=j]) for j in range(3)] for i in range(3)]
        expected=H[3][3]*numeric_det(B)-sum(c[i]*adjnum[i][j]*b[j] for i in range(3) for j in range(3))
        assert observed==expected
        for p in (P1,P2):
            modular=sum((v%p)*(w.numerator*pow(w.denominator,-1,p)%p) for v,w in zip(vals,weights))%p
            assert modular==expected%p
        checks.append(dict(B=B,b=b,c=c,A=A,H=H,t_grid=list(range(9)),det_values=vals,coefficient=expected))
    write('independent_jet_checks.json',dict(seed=20260908,weights=weights,checks=checks))
    return len(checks)

def explicit_intermediate_arc():
    x,y,z,w,v=[var(i,5) for i in range(5)];Z={}
    B=[[add(x,v),w,Z],[Z,add(y,v),v],[Z,Z,add(z,v)]]
    b=[w,Z,Z];c=[x,Z,Z]
    g2=add(mul(w,det(B)),scale(dot(c,mv(adj(B),b)),-1))
    target=mul(mul(v,w),mul(add(y,v),add(z,v)))
    assert g2==target and g2
    pen=[]
    for k in range(5):
        e=tuple(int(i==k) for i in range(5))
        pen.append([[B[r][col].get(e,0) if r<3 and col<3 else 0 for col in range(4)] for r in range(4)])
    assert len(rref([[a for row in A for a in row] for A in pen])[1])==5
    # Check whole t-polynomial at integer points using independent determinant.
    rng=random.Random(20260909);points=[]
    for _ in range(8):
        s=[rng.randint(-4,4) for _ in range(5)]
        for t in (1,2,3):
            BM=[[ev(e,s) for e in row] for row in B]
            N=[BM[i]+[t*ev(b[i],s)] for i in range(3)]+[[t*ev(e,s) for e in c]+[t*t*ev(w,s)]]
            assert numeric_det(N)==t*t*ev(target,s)
        points.append(s)
    write('intermediate_rank3_arc.json',dict(coordinates=['x','y','z','w','v'],base_pencil=pen,
      B=B,b=b,c=c,M2_44=w,g2=g2,expected='v*w*(y+v)*(z+v)',base_span_dimension=5,
      dPhi_rank=5,rank_of_reduced_M=3,seed=20260909,independent_points=points,
      scope='A genuine order-two fixed-factor arc on a special ker/coker incidence; no containment claim.'))
    return dict(base_span=5,rank_M=3,leading_form='v*w*(y+v)*(z+v)',independent_point_checks=24)

if __name__=='__main__':
    result=dict(time_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),rank_cases=focused_ranks(),
                tangent_calibration=differential_calibration(),independent_jet_cases=numeric_jet_checks(),
                intermediate_arc=explicit_intermediate_arc())
    write('verification_summary.json',result);print(json.dumps(result,indent=2))

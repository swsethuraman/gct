"""Small exact Hessian image audit. New gpt-6-astra code, no worker imports.
Run from this directory through the retained b15_bound.py, 60s / 512 MiB.
Source bracket normalization follows the Claude Opus 5 attributed B14 source.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
from itertools import permutations, product
from math import factorial, comb
import json, random, sys, hashlib
from flint import fmpz_mat, fmpq_mat

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
ZERO=(0,0,0)
DEGS=(2,3,4)

def det(a):
    return int(fmpz_mat(a).det())

def interpolate(vals):
    out=[Q(0)]*len(vals); base=[Q(1)]; diff=list(map(Q,vals))
    for k in range(len(vals)):
        for i,b in enumerate(base): out[i]+=b*diff[0]
        diff=[diff[i+1]-diff[i] for i in range(len(diff)-1)]
        nxt=[Q(0)]*(len(base)+1)
        for i,b in enumerate(base):
            nxt[i]-=k*b/(k+1); nxt[i+1]+=b/(k+1)
        base=nxt
    return out

def pmul(a,b):
    z=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): z[i+j]+=x*y
    return z

def rem(a,p):
    a=list(a)
    for i in range(len(a)-1,len(p)-2,-1):
        x=a[i]/p[-1]
        for j,y in enumerate(p): a[i-len(p)+1+j]-=x*y
    return a[:len(p)-1]

def evalp(a,t):
    return sum(x*t**i for i,x in enumerate(a))

def border(B,u,v):
    return [row+[v[i]] for i,row in enumerate(B)]+[list(u)+[0]]

def polynomials(N):
    s=[M[0][0] for M in N]; u=[[row[0] for row in M] for M in N]
    vals=[[] for _ in range(8)]
    for t in range(21):
        B=[[2*t*t*N[0][i][j]+6*t*N[1][i][j]+12*N[2][i][j] for j in range(9)] for i in range(9)]
        v=[4*t*u[0][i]+3*u[1][i] for i in range(9)]; h=12*t*t+2*s[0]
        H=[[h]+v]+[[v[i]]+B[i] for i in range(9)]
        A=det(B)
        # adj(H)_(0,x) contracted with u_d is -u_d adj(B) v.
        J2=det(border(B,u[0],v)); J3=det(border(B,u[1],v))
        w=[0]+u[0]
        Q22=-det(border(H,w,w))
        dh=det(H)
        if dh:
            inv=fmpq_mat(H).inv()
            adj=[[int(inv[i,j]*dh) for j in range(10)] for i in range(10)]
        else:
            adj=[[(-1)**(i+j)*det([[H[a][b] for b in range(10) if b!=i] for a in range(10) if a!=j]) for j in range(10)] for i in range(10)]
        Td=[sum(adj[i+1][j+1]*M[j][i] for i in range(9) for j in range(9)) for M in N]
        for a,x in zip(vals,[A,J2,J3,Q22,dh]+Td): a.append(x)
    polys=[interpolate(v) for v in vals]
    for a,b in zip(polys,vals): assert all(evalp(a,t)==x for t,x in enumerate(b))
    return s,polys

NAMES=['A_R1','s2_A_R3','J2_R2','J3_R3','Q22_R3','D_S3','s2_D_S5','s3_D_S6','s4_D_S7','s2_squared_D_S7','T2_R1','s2_T2_R3','T3_R2','T4_R3']

def candidates(N):
    s,ps=polynomials(N); p=[s[2],s[1],s[0],0,1]
    rs=[rem(a,p) for a in ps[:4]]; S=rem(ps[4],pmul(p,p))
    row=[rs[0][1],s[0]*rs[0][3],rs[1][2],rs[2][3],rs[3][3],S[3],s[0]*S[5],s[1]*S[6],s[2]*S[7],s[0]**2*S[7]]
    ts=[rem(a,p) for a in ps[5:]]
    row += [ts[0][1],s[0]*ts[0][3],ts[1][2],ts[2][3]]
    assert all(x.denominator==1 for x in row)
    return list(map(int,row)), ps, rs, S

def generic(seed):
    rng=random.Random(seed); out=[]
    for d in DEGS:
        M=[[0]*9 for _ in range(9)]
        for i in range(9):
            for j in range(i,9): M[i][j]=M[j][i]=rng.randint(-3,3)
        out.append(M)
    return out

def derivative_hessian(terms,t):
    H=[[0]*10 for _ in range(10)]
    for sign,ls in terms:
        vs=[a[0]*t+a[1] for a in ls]
        for a in range(4):
            for b in range(4):
                if a==b: continue
                fac=sign
                for k in range(4):
                    if k not in (a,b): fac*=vs[k]
                for i in range(10):
                    for j in range(10): H[i][j]+=fac*ls[a][i]*ls[b][j]
    return H

def geometry(seed,padded):
    rng=random.Random(seed)
    B=[[[rng.randint(-2,2) for j in range(3 if padded else 4)] for i in range(3 if padded else 4)] for k in range(9)]
    if padded:
        # Full independent ten-variable z*per3; c=1, cubic term zero identically.
        assert det([[x for row in M for x in row] for M in B])!=0
        z=[1]+[-sum(M[i][i] for i in range(3)) for M in B]
        X=[[[int(i==j)]+[M[i][j] for M in B] for j in range(3)] for i in range(3)]
        terms=[(1,[z]+[X[i][q[i]] for i in range(3)]) for q in permutations(range(3))]
    else:
        for M in B: M[3][3]=-sum(M[i][i] for i in range(3))
        X=[[[int(i==j)]+[M[i][j] for M in B] for j in range(4)] for i in range(4)]
        terms=[]
        for q in permutations(range(4)):
            sign=(-1)**sum(q[i]>q[j] for i in range(4) for j in range(i+1,4))
            terms.append((sign,[X[i][q[i]] for i in range(4)]))
    Hm,H0,Hp=[derivative_hessian(terms,t) for t in (-1,0,1)]
    N=[[[Q(Hp[i+1][j+1]+Hm[i+1][j+1]-2*H0[i+1][j+1],4) for j in range(9)] for i in range(9)],
       [[Q(Hp[i+1][j+1]-Hm[i+1][j+1],12) for j in range(9)] for i in range(9)],
       [[Q(H0[i+1][j+1],12) for j in range(9)] for i in range(9)]]
    # Integer rescaling of the x directions clears fixed tensor denominators;
    # f_d -> 6^d f_d, keeping a monic depressed genuine pencil.
    N=[[[int(x*6**d) if (x*6**d).denominator==1 else None for x in row] for row in M] for d,M in zip(DEGS,N)]
    assert all(x is not None for M in N for row in M for x in row)
    return N,B

def pivot_columns(rows):
    work=[list(map(Q,row)) for row in rows]; rr=0; piv=[]
    for j in range(len(work[0])):
        i=next((i for i in range(rr,len(work)) if work[i][j]),None)
        if i is None: continue
        work[rr],work[i]=work[i],work[rr]; a=work[rr][j]; work[rr]=[x/a for x in work[rr]]
        for i in range(rr+1,len(work)):
            if work[i][j]:
                a=work[i][j]; work[i]=[x-a*y for x,y in zip(work[i],work[rr])]
        piv.append(j); rr+=1
        if rr==len(work): break
    return piv

def compositions(n):
    for i in range(n+1):
        for j in range(n-i+1): yield (i,j,n-i-j)

def scalar_exponents(n):
    for a in range(n//2+1):
        for b in range((n-2*a)//3+1):
            c=n-2*a-3*b
            if c%4==0: yield (a,b,c//4)

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def unit(i): return tuple(int(i==j) for j in range(3))
def clean(d): return {k:v for k,v in d.items() if v}

def symbolic():
    # Keys: (left border bits,right border bits,N multiplicities,scalar powers).
    def source(a,b,c,z): return (min(a,b),max(a,b),c,z)
    def terms(a,b,m,shift=0,z=ZERO,mul=1):
        out=[]
        for c in compositions(m):
            fac=Q(mul*2**c[0]*6**c[1]*12**c[2],factorial(c[0])*factorial(c[1])*factorial(c[2]))
            out.append((source(a,b,c,z),2*c[0]+c[1]+shift,fac))
        return out
    U,V=unit(0),unit(1)
    A=terms(ZERO,ZERO,9)
    C22=terms(U,U,8); C23=terms(U,V,8); C33=terms(V,V,8)
    J2=terms(U,U,8,1,mul=-4)+terms(U,V,8,mul=-3)
    J3=terms(U,V,8,1,mul=-4)+terms(V,V,8,mul=-3)
    Q22=terms(U,U,8,2,mul=12)+terms(U,U,8,z=U,mul=2)+terms(add(U,V),add(U,V),7,mul=-9)
    D=terms(ZERO,ZERO,9,2,mul=12)+terms(ZERO,ZERO,9,z=U,mul=2)+terms(U,U,8,2,mul=-16)+terms(U,V,8,1,mul=-24)+terms(V,V,8,mul=-9)
    def powers(square):
        divisor={(4,ZERO):1,(2,U):1,(1,V):1,(0,unit(2)):1}
        if square:
            z=defaultdict(int)
            for (i,a),x in divisor.items():
                for (j,b),y in divisor.items(): z[(i+j,add(a,b))]+=x*y
            divisor=dict(z)
        degree=8 if square else 4
        rr=[{(k,ZERO):1} for k in range(degree)]
        for k in range(degree,21):
            row=defaultdict(int)
            for (j,a),x in divisor.items():
                if j==degree: continue
                for (i,b),y in rr[k-degree+j].items(): row[(i,add(a,b))]-=x*y
            rr.append(clean(row))
        return rr
    choices=[(A,False,1,ZERO),(A,False,3,U),(J2,False,2,ZERO),(J3,False,3,ZERO),(Q22,False,3,ZERO),
             (D,True,3,ZERO),(D,True,5,U),(D,True,6,V),(D,True,7,unit(2)),(D,True,7,(2,0,0))]
    Td=[]
    for d in range(3):
        Td.append([(key,k-(2-d),x*key[2][d]/(2,6,12)[d]) for key,k,x in D if key[2][d]])
    choices += [(Td[0],False,1,ZERO),(Td[0],False,3,U),(Td[1],False,2,ZERO),(Td[2],False,3,ZERO)]
    rrs=[powers(False),powers(True)]; vs=[]
    for ts,square,j,scalar in choices:
        row=defaultdict(Q)
        for (a,b,c,z),k,x in ts:
            for (power,s),y in rrs[square][k].items():
                if power==j: row[source(a,b,c,add(add(z,s),scalar))]+=x*y
        vs.append(clean(row))
    # Exact Euler relations; these are identically zero for genuine slice jets.
    relations=[]
    for d in range(3):
        for h in compositions(9):
            w=35-DEGS[d]-sum(x*y for x,y in zip(DEGS,h))
            if w<0: continue
            for z in scalar_exponents(w):
                row={source(ZERO,ZERO,h,add(z,unit(d))):Q(-1)}
                for e in range(3):
                    if h[e]: row[source(unit(d),unit(e),tuple(h[i]-int(i==e) for i in range(3)),z)]=Q(h[e])
                relations.append(row)
    piv={}
    def reduce(row):
        row=dict(row)
        for p,b in sorted(piv.items(),reverse=True):
            a=row.get(p,0)
            if a:
                for k,v in b.items(): row[k]=row.get(k,0)-a*v
                row=clean(row)
        return row
    for row in relations:
        row=reduce(row)
        if row:
            p=max(row); a=row[p]; piv[p]={k:v/a for k,v in row.items()}
    reduced=[reduce(v) for v in vs]
    keys=sorted(set().union(*(set(v) for v in reduced)))
    mat=[[v.get(k,0) for v in reduced] for k in keys]
    cols=pivot_columns(mat)
    return vs,reduced,{'formal_source_supports':[len(v) for v in vs], 'euler_relations':len(relations),'euler_rank':len(piv),'rank_modulo_these_euler_relations':len(cols),'independent_columns_modulo_euler':cols}

def encode_vector(v):
    return [[list(map(list,k)),str(x)] for k,x in sorted(v.items())]

def direct_source_check(N,vs,expected):
    # Independent complete two-variable interpolation of each homogeneous
    # bordered determinant, at y4=1. No Hessian remainder code in this route.
    patterns=sorted({k[:2] for v in vs for k in v})
    scalars=[M[0][0] for M in N]; us=[[row[0] for row in M] for M in N]
    coeffs={}
    for a,b in patterns:
        k=sum(a); m=9-k; vals={}
        for i in range(m+1):
            for j in range(m-i+1):
                B=[[i*N[0][r][c]+j*N[1][r][c]+N[2][r][c] for c in range(9)] for r in range(9)]
                rowborder=[us[d] for d in range(3) if a[d]]
                colborder=[us[d] for d in range(3) if b[d]]
                big=[row+[v[r] for v in colborder] for r,row in enumerate(B)]
                big += [v+[0]*k for v in rowborder]
                vals[i,j]=(-1)**k*det(big)
        binoms=[[Q(1)]]
        for i in range(m):
            z=pmul(binoms[-1],[-i,1]); binoms.append([x/(i+1) for x in z])
        coef=defaultdict(Q)
        for i in range(m+1):
            for j in range(m-i+1):
                diff=sum((-1)**(i+j-r-c)*comb(i,r)*comb(j,c)*vals[r,c] for r in range(i+1) for c in range(j+1))
                for r,x in enumerate(binoms[i]):
                    for c,y in enumerate(binoms[j]): coef[(r,c,m-r-c)]+=diff*x*y
        coeffs[a,b]=coef
    actual=[]
    for v in vs:
        val=Q(0)
        for (a,b,c,z),x in v.items():
            bv=coeffs[a,b][c]*factorial(c[0])*factorial(c[1])*factorial(c[2])
            for s,k in zip(scalars,z): bv*=s**k
            val+=x*bv
        actual.append(val)
    assert actual==expected,'Source expansion disagrees with direct Hessians'
    mutated=list(expected); mutated[0]+=1
    assert actual!=mutated
    return {'all_source_expansions_match_direct_Hessian':True,'border_patterns':len(patterns),'changed_value_rejected':True}

def main():
    vs,reduced,summary=symbolic()
    for v in vs:
        for a,b,c,z in v:
            assert sum(a)+sum(c)==sum(b)+sum(c)==9
            assert sum(d*(a[i]+b[i]+c[i]+z[i]) for i,d in enumerate(DEGS))==35
    rows=[]; points=[]; lower15=[]; lower17=[]
    for seed in range(91300,91314):
        N=generic(seed); row,ps,rs,S=candidates(N); rows.append(row); points.append(N)
        s2=N[0][0][0]
        lower15.append([int(S[7])])
        lower17.append([int(rs[0][3]),int(rem(ps[5],[N[2][0][0],N[1][0][0],s2,0,1])[3]),int(S[5]),int(s2*S[7])])
    cols=pivot_columns(rows); r=len(cols)
    rids=pivot_columns([[row[j] for row in rows] for j in cols])
    minor=[[rows[i][j] for j in cols] for i in rids]
    assert det(minor)!=0
    assert r<=summary['rank_modulo_these_euler_relations']
    # Solve all candidate dependencies against selected exact ambient values;
    # then prove each equality modulo the explicit Euler relation space.
    B=fmpq_mat(minor); coords=[]; identities=[]
    for j in range(len(NAMES)):
        sol=B.solve(fmpq_mat([[rows[i][j]] for i in rids]))
        co=[Q(str(sol[i,0])) for i in range(r)]; coords.append(list(map(str,co)))
        diff=defaultdict(Q,reduced[j])
        for a,k in zip(co,cols):
            for key,x in reduced[k].items(): diff[key]-=a*x
        identities.append(not clean(diff))
    summary.update(exact_generic_rank=r, basis_columns=cols, all_dependencies_proved_modulo_euler=all(identities), dependency_checks=identities)
    adjcols=[0,1,2,3,4,10,11,12,13]; sqcols=[5,6,7,8,9]
    ar=len(pivot_columns([[row[j] for j in adjcols] for row in rows]))
    sr=len(pivot_columns([[row[j] for j in sqcols] for row in rows]))
    summary.update(adjugate_image_rank=ar,squared_division_image_rank=sr,intersection_dimension=ar+sr-r)
    source_control=direct_source_check(points[0],vs,rows[0])
    lower={}
    for name,values,labels in [('r10_t15',lower15,['S7']),('r10_t17',lower17,['A_R3','T2_R3','S5','s2_S7'])]:
        cc=pivot_columns(values); ii=pivot_columns([[row[j] for row in values] for j in cc])
        mm=[[values[i][j] for j in cc] for i in ii]
        assert det(mm)!=0
        lower[name]={'names':labels,'values':values,'rank':len(cc),'minor_rows':ii,'minor_columns':cc,'minor':mm,'determinant':str(det(mm))}
    # One nonspecial determinant pencil is a code control, not the global proof.
    N,Bdet=geometry(91350,False); row,ps,rs,S=candidates(N)
    assert not any(row) and not any(x for a in rs for x in a) and not any(S)
    padrows=[]; padpoints=[]
    for seed in range(91400,91404):
        N,Bpad=geometry(seed,True); row,_,_,_=candidates(N)
        padrows.append(row); padpoints.append(Bpad)
    pcols=pivot_columns(padrows); pr=len(pcols)
    prids=pivot_columns([[row[j] for row in padrows] for j in pcols])
    pminor=[[padrows[i][j] for j in pcols] for i in prids]
    assert pr==0 or det(pminor)!=0
    result={'status':'EXACT_SMALL_CONSTRUCTION_REQUIRES_REPORT_GLOBAL_PROOF','model':'gpt-6-astra','effort':'xhigh',
      'candidate_names':NAMES,'summary':summary,'coordinates_in_basis':coords,
      'source_expansion_control':source_control,
      'lower_tail_exact_controls':lower,
      'generic_points_N':points,'generic_evaluations':rows,'minor_rows':rids,'minor_columns':cols,'minor':minor,'minor_determinant':str(det(minor)),
      'determinant_control_B':Bdet,'determinant_all_minor_remainders_zero':True,'determinant_p_squared_remainder_zero':True,
      'padding_points_B':padpoints,'padding_evaluations':padrows,'padding_rank_floor':pr,'padding_minor_rows':prids,'padding_minor_columns':pcols,'padding_minor':pminor,'padding_minor_determinant':str(det(pminor)) if pr else None,
      'source_vectors':[encode_vector(v) for v in vs]}
    path=HERE/'small_evidence.json'
    if '--write' in sys.argv: path.write_text(json.dumps(result,indent=2)+'\n')
    else: assert result==json.loads(path.read_text()),'Saved evidence mismatch'
    print(json.dumps({'summary':summary,'padding_rank_floor':pr,'mode':'write' if '--write' in sys.argv else 'replay'}))

if __name__=='__main__': main()

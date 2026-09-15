"""B16-04: exact necessary pole constraints on the inherited Hessian space.

Use .venv/python.exe -B analysis/b15_bound.py --seconds 60 --memory-mb 512
--name b16_04_NAME --slot 04 analysis/b16_04_filtration.py MODE.
All samples below are ambient quartic jets, not determinant/padding samples.
Inherited Hessian evaluator: gpt-6-astra; bracket convention: Claude Opus 5.
"""
from pathlib import Path
import sys, json, importlib.util, hashlib, time
from fractions import Fraction as Q
from flint import fmpq_mat

HERE=Path(__file__).resolve().parents[1]
ROOT=HERE.parents[2]
EVIDENCE=ROOT/'Batch15_Launch/native_20260913/reviews_filesystem/Hessian11_1631'
OUT=HERE/'results/b16_04'
OUT.mkdir(exist_ok=True)
spec=importlib.util.spec_from_file_location('hessian11',EVIDENCE/'verify_small.py')
old=importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)
BASIS=[0,1,2,3,4,5,6,7,8,10,11]

def dump(name,obj):
    (OUT/name).write_text(json.dumps(obj,indent=2)+'\n')

def transformed(M,c,l=None):
    """K_d=c^d N_d for G=c*t^4+4*L*t^3+a2*t^2+a3*t+a4.
    M_d=Hess(a_d)(e)/(d(d-1)); these symmetric matrices are arbitrary.
    Scale raw M2 by6 and M3 by4 so all evaluations are integral.
    """
    if l is None: l=[1]+[0]*8
    a=l[0]; s=M[0][0][0]
    u=[[row[0] for row in mat] for mat in M]
    K=[[[0]*9 for _ in range(9)] for _ in range(3)]
    for i in range(9):
        for j in range(9):
            ll=l[i]*l[j]
            lu2=l[i]*u[0][j]+u[0][i]*l[j]
            lu3=l[i]*u[1][j]+u[1][i]*l[j]
            K[0][i][j]=c*M[0][i][j]-6*ll
            K[1][i][j]=c*c*M[1][i][j]-Q(2*c,3)*(a*M[0][i][j]+lu2)+8*a*ll
            K[2][i][j]=c**3*M[2][i][j]-Q(c*c,4)*(2*a*M[1][i][j]+lu3)+Q(c,6)*(a*a*M[0][i][j]+2*a*lu2+s*ll)-3*a*a*ll
    assert all(Q(x).denominator==1 for mat in K for row in mat for x in row)
    return [[[int(x) for x in row] for row in mat] for mat in K]

def raw(seed):
    return [[[scale*x for x in row] for row in mat] for scale,mat in zip((6,4,1),old.generic(seed))]

def families(N):
    row,ps,rs,S=old.candidates(N)
    s2=N[0][0][0]
    p=[N[2][0][0],N[1][0][0],s2,0,1]
    return {19:[row[i] for i in BASIS],
            17:[rs[0][3],old.rem(ps[5],p)[3],S[5],s2*S[7]],
            15:[S[7]]}

def nullspace(rows,n):
    if not rows: return [[int(i==j) for i in range(n)] for j in range(n)]
    R,rank=fmpq_mat([[str(x) for x in row] for row in rows]).rref()
    piv=[]
    for i in range(rank): piv.append(next(j for j in range(n) if R[i,j]))
    out=[]
    for f in range(n):
        if f in piv: continue
        v=[Q(0)]*n; v[f]=Q(1)
        for i,p in enumerate(piv): v[p]=-Q(str(R[i,f]))
        out.append(v)
    return out

def encode(rows): return [[str(x) for x in row] for row in rows]

def sizing():
    vs,_,summary=old.symbolic()
    bounds=[]
    for j,v in enumerate(vs):
        bound=max(sum((d-1)*(a[i]+b[i]+c[i]+z[i]) for i,d in enumerate((2,3,4))) for a,b,c,z in v)
        bounds.append(bound)
    result={'source_summary':summary,'cleared_polynomial_degree_bounds':bounds,
      'safe_interpolation_nodes':36,'heldout_nodes':1,'t_interpolation_nodes':21,
      'largest_hessian_order':10,'largest_bordered_order':11,
      'raw_jet_entries':135,'scalar_c_degree_safe_bound':35,
      'memory_estimate_MiB':128,'wall_estimate_seconds':15,
      'policy':'one sequential small control per run, 60 seconds / 512 MiB; no heavy lease',
      'purpose':'Specializations give necessary pole constraints only; universal lifts must match their kernels before exact filtration is claimed.'}
    dump('sizing.json',result); print(json.dumps(result))

def pilot(seed,write=True):
    started=time.perf_counter(); M=raw(seed)
    # W=t+16 is the common weighted degree of the corresponding family.
    values={t:[] for t in (15,17,19)}
    for c in range(36):
        f=families(transformed(M,c))
        for t in values: values[t].append(f[t])
    extra=families(transformed(M,37))
    result={'seed':seed,'raw_jets':M,'linear_L':[1]+[0]*8,'families':{},'claims':'necessary upper bounds only'}
    for t,rows in values.items():
        coeffs=[old.interpolate([row[j] for row in rows]) for j in range(len(rows[0]))]
        assert all(old.evalp(p,37)==x for p,x in zip(coeffs,extra[t]))
        W=t+16
        assert all(all(x==0 for x in p[W+1:]) for p in coeffs)
        constraints={}
        for d in range(20,36):
            matrix=[[p[k] for p in coeffs] for k in range(max(0,W-d))]
            ker=nullspace(matrix,len(coeffs))
            constraints[d]={'kernel_dimension':len(ker),'kernel':encode(ker)}
        result['families'][t]={'weight':W,'columns':BASIS if t==19 else (['A_R3','T2_R3','S5','s2_S7'] if t==17 else ['S7']),
          'coefficients':encode(coeffs),'constraints':constraints}
    result['wall_seconds']=time.perf_counter()-started
    if write:
        dump(f'pilot_{seed}.json',result)
        print(json.dumps({'seed':seed,'wall_seconds':result['wall_seconds'],'dimensions':{t:{d:v['kernel_dimension'] for d,v in f['constraints'].items()} for t,f in result['families'].items()}}))
    return result

def combine():
    pilots=[json.loads(p.read_text()) for p in sorted(OUT.glob('pilot_*.json'))]
    result={}
    for t in (15,17,19):
        fs=[x['families'][str(t)] for x in pilots]; W=t+16
        n=len(fs[0]['coefficients']); result[t]={}
        for d in range(20,28):
            rows=[[Q(p[k]) for p in f['coefficients']] for f in fs for k in range(max(0,W-d))]
            ker=nullspace(rows,n)
            result[t][d]={'dimension_upper':len(ker),'kernel':encode(ker)}
    dump('joint_pole_constraints.json',result); print(json.dumps(result))

if __name__=='__main__':
    mode=sys.argv[1]
    if mode=='size': sizing()
    elif mode=='pilot': pilot(int(sys.argv[2]))
    elif mode=='combine': combine()
    else: raise ValueError(mode)

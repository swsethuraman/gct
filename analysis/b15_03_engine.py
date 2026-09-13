"""Local Windows sparse reduction adapter. No shared implementation is edited."""
from pathlib import Path
import json
import time
import random
import numpy as np
import scipy
from scipy import sparse
import flint
from flint import nmod_mat
from numba import njit
import numba
from wk8_s30_core import exps, det_form, restrict, P1, P2
from wk13_b10_lean import build_cell_lean, best_cover_lean, check_kernel_mat_lean
from wk12_s79_cell6 import det_pencils, det_coeffs, ev_rows_from_coeffs
from wk10_s64_pad import pad_frames, pad_coeffs

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'results/b15_03'
OUT.mkdir(exist_ok=True)

def save(name,obj):
    (OUT/name).write_text(json.dumps(obj,indent=2,allow_nan=False)+'\n',encoding='utf-8')

def rank(A,p):
    A=np.asarray(A,dtype=np.int64)%p
    return int(nmod_mat(A.shape[0],A.shape[1],A.ravel().tolist(),p).rank())

def kernel(A,p):
    A=np.asarray(A,dtype=np.int64)%p
    X,nul=nmod_mat(A.shape[0],A.shape[1],A.ravel().tolist(),p).nullspace()
    return np.array([[int(X[i,j]) for j in range(nul)] for i in range(A.shape[1])],dtype=np.int64).reshape(A.shape[1],nul)

@njit(cache=False)
def triangular(indptr,indices,data,inv,B,p):
    """In-place exact upper-triangular solve, int64 products below 2^62."""
    for i in range(B.shape[0]-1,-1,-1):
        for k in range(indptr[i],indptr[i+1]):
            j=indices[k]
            if j==i:
                continue
            assert j>i
            v=int(data[k])%p
            for b in range(B.shape[1]):
                B[i,b]=(B[i,b]-v*B[j,b])%p
        for b in range(B.shape[1]):
            B[i,b]=(B[i,b]*inv[i])%p
    return B

@njit(cache=False)
def spmm(indptr,indices,data,X,p):
    """Exact sparse/dense multiplication, reducing after every summand."""
    result=np.zeros((len(indptr)-1,X.shape[1]),dtype=np.int64)
    for i in range(len(indptr)-1):
        for k in range(indptr[i],indptr[i+1]):
            j=indices[k]
            v=int(data[k])%p
            for b in range(X.shape[1]):
                result[i,b]=(result[i,b]+v*X[j,b])%p
    return result

def sparse_product(A,X,p):
    A=A.tocsr()
    return spmm(A.indptr,A.indices,A.data.astype(np.int64),np.asarray(X,dtype=np.int64),p)

def reduce(E,a,p,cov=None,seed=1503):
    """Projected Schur kernel plus complete E verification; capped before dense work."""
    start=time.perf_counter()
    nc=E.shape[1]
    cov=cov if cov is not None else best_cover_lean(E,nc,verbose=False)
    S,U,rows=cov['S'],cov['U'],cov['rows']
    ns,nu=len(S),len(U)
    info={'cover_rank_lb':ns,'uncovered_columns':nu,'order':cov['order'],'cover_stats':cov['stats']}
    # Several live dense arrays and flint's Python conversion are priced together.
    estimated=24*ns*nu+100*(nu+32)*nu+E.data.nbytes+E.indices.nbytes+E.indptr.nbytes
    info['estimated_dense_and_operator_bytes']=estimated
    info['estimate_method']='24*nS*nU + 100*(nU+32)*nU + CSR bytes; excludes baseline'
    if nu>2500 or estimated>800*1024**2:
        raise MemoryError(json.dumps(info))
    R=E[rows].astype(np.int64)
    T=R[:,S].tocsr(); T.sort_indices()
    diag=T.diagonal()%p
    assert np.all(diag)
    inv=np.array([pow(int(v),-1,p) for v in diag],dtype=np.int64)
    X=R[:,U].toarray()%p
    triangular(T.indptr,T.indices,T.data,inv,X,p)
    info['triangular_seconds']=time.perf_counter()-start
    for attempt in range(3):
        m=nu+32+attempt*32
        rng=np.random.default_rng(seed+attempt)
        rows_for_projection=rng.integers(0,m,size=E.shape[0])
        signs=2*rng.integers(0,2,size=E.shape[0])-1
        P=sparse.csr_matrix((signs,(rows_for_projection,np.arange(E.shape[0]))),shape=(m,E.shape[0]),dtype=np.int64)
        PE=(P@E.astype(np.int64)).tocsr()
        G=(PE[:,U].toarray()-sparse_product(PE[:,S],X,p))%p
        Y=kernel(G,p)
        assert Y.shape[1]>=a, ('nullity below exact ambient',Y.shape,a)
        if Y.shape[1]>a:
            continue
        K=np.zeros((nc,a),dtype=np.int64)
        K[U]=Y
        # X is dense; use flint only on the small-width lift to avoid int64 sums.
        for i in range(ns):
            for j in range(a):
                K[S[i],j]=-sum(int(x)*int(y) for x,y in zip(X[i],Y[:,j]))%p
        assert check_kernel_mat_lean(E,K,p)
        assert rank(K,p)==a
        info.update({'modular_nullity_exact':a,'verified_full_E':True,'source_rank_lb':a,
                     'projection_attempt':attempt,'projection_seed':seed+attempt,'projection_rows':m,
                     'reduction_seconds':time.perf_counter()-start})
        return K,info
    raise RuntimeError('three projections left surplus nullity')

def build(lam,d):
    # Memory blocks avoid any inherited scratch-directory removal path.
    return build_cell_lean(tuple(lam),d,n=4,chunk=20000,blocks='memory',verbose=False)

def eval_native(arr,K,coeffs,p,r):
    EV=ev_rows_from_coeffs(arr,coeffs,p,r,chunk=20000,n=4)
    # K has few columns; flint multiplies exactly before reduction.
    A=nmod_mat(EV.shape[0],EV.shape[1],EV.ravel().tolist(),p)
    B=nmod_mat(K.shape[0],K.shape[1],K.ravel().tolist(),p)
    C=A*B
    return [[int(C[i,j]) for j in range(K.shape[1])] for i in range(EV.shape[0])]

def eval_direct(arr,K,co,p,r):
    A=exps(4,r)
    result=[0]*K.shape[1]
    for mon,col,sgn in zip(arr['M'],arr['col_of'],arr['sgn']):
        if col<0:
            continue
        term=int(sgn)
        for k in mon:
            term=term*co.get(A[int(k)],0)%p
        for j in range(K.shape[1]):
            result[j]=(result[j]+term*int(K[col,j]))%p
    return result

def diagonal_points(count,r,seed=150303):
    rng=random.Random(seed)
    return [[[[rng.randint(-3,3) if a==b else 0 for b in range(4)] for a in range(4)]
             for _ in range(r)] for _ in range(count)]

def poly_value(co,x,p):
    return sum(c*math_product(pow(xi,ai,p) for xi,ai in zip(x,al)) for al,c in co.items())%p

def math_product(values):
    result=1
    for v in values: result*=v
    return result

def point_check(pencil,co,p):
    r=len(pencil); x=list(range(1,r+1))
    mat=[[sum(x[i]*pencil[i][a][b] for i in range(r)) for b in range(4)] for a in range(4)]
    return poly_value(co,x,p)==int(nmod_mat(mat,p).det())

def controls():
    t=time.perf_counter(); p=P1
    B=build((6,2),2); K,info=reduce(B['E'],1,p)
    arr=B['arr']; letters=exps(4,2)
    # Exact integral known HWV 8*c40*c22 - 3*c31^2.
    coeff_by_mon={tuple(sorted([letters.index((4,0)),letters.index((2,2))])):8,
                  (letters.index((3,1)),)*2:-3}
    known=np.array([[coeff_by_mon.get(tuple(m),0)] for m in arr['M']],dtype=np.int64)
    assert np.array_equal(arr['col_of'],np.arange(2))
    assert not np.any(B['E'].astype(np.int64)@known)
    bad=known.copy(); bad[0,0]+=1
    assert np.any(B['E'].astype(np.int64)@bad)
    pts=det_pencils(3,11,3,2); coeffs=[det_coeffs(pt,2) for pt in pts]
    vals=eval_native(arr,K,coeffs,p,2)
    assert rank(vals,p)==1
    assert all(eval_direct(arr,K,c,p,2)==v for c,v in zip(coeffs,vals))
    assert all(point_check(pt,c,p) for pt,c in zip(pts,coeffs))
    badco=dict(coeffs[0]); badco[(4,0)]=badco.get((4,0),0)+1
    assert not point_check(pts[0],badco,p)
    # Near-prime products force modular arithmetic paths and catch overflow.
    rng=np.random.default_rng(3)
    A=sparse.csr_matrix(rng.integers(0,p,size=(5,7),dtype=np.int64))
    X=rng.integers(0,p,size=(7,4),dtype=np.int64)
    C=sparse_product(A,X,p)
    exact=nmod_mat(A.toarray().tolist(),p)*nmod_mat(X.tolist(),p)
    assert C.tolist()==exact.tolist()
    tri=sparse.csr_matrix(np.triu(rng.integers(1,p,size=(7,7),dtype=np.int64)))
    rhs=rng.integers(0,p,size=(7,3),dtype=np.int64)
    solved=triangular(tri.indptr,tri.indices,tri.data,np.array([pow(int(x),-1,p) for x in tri.diagonal()],dtype=np.int64),rhs.copy(),p)
    assert sparse_product(tri,solved,p).tolist()==rhs.tolist()
    # Separate known six-row liveness and forced-zero control, never the main cell.
    C=build((14,2,2,2,2,2),6); KC,ci=reduce(C['E'],1,p)
    dp=det_pencils(2,11,3,6); diagonal=diagonal_points(2,6)
    live=eval_native(C['arr'],KC,[det_coeffs(x,6) for x in dp],p,6)
    zero=eval_native(C['arr'],KC,[det_coeffs(x,6) for x in diagonal],p,6)
    assert rank(live,p)==1 and not any(v for row in zero for v in row)
    mutation=KC.copy(); mutation[0,0]=(mutation[0,0]+1)%p
    assert not check_kernel_mat_lean(C['E'],mutation,p)
    rec={'status':'EXACT','model':'gpt-6-astra','prime':p,
         'versions':{'numpy':np.__version__,'scipy':scipy.__version__,'flint':flint.__version__,'numba':numba.__version__},
         'known_binary_quartic_HVW':'8*c40*c22-3*c31^2','source_mutation_rejected':True,
         'point_mutation_rejected':True,'normalization_checked_against_integral_formula':True,
         'direct_polynomial_evaluation_agrees':True,'overflow_control_passed':True,
         'triangular_solve_control_passed':True,'binary_control':info,'binary_det_values':vals,
         'separate_six_row_control':ci,'six_row_det_values':live,'six_row_diagonal_values':zero,
         'six_row_source_mutation_rejected':True,'wall_seconds':time.perf_counter()-t}
    save('engine_controls.json',rec)
    print(json.dumps(rec),flush=True)

if __name__=='__main__':
    controls()

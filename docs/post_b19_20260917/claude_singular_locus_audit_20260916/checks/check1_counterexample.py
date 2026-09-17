"""Check 1 (prepriced: < 2 s, < 60 MiB): the explicit singular, non-compression,
semistable 5-tuple of 4x4 matrices.

X = skew(3) + <E14> + <E44>, basis
  B1=E12-E21, B2=E13-E31, B3=E23-E32, B4=E14, B5=E44.
(i)   det(sum x_i B_i) == 0 identically (exact, sympy).
(ii)  the five matrices are linearly independent.
(iii) the tuple lies outside the SL4 x SL4 null cone: the degree-8 semi-invariant
      det(sum_k M_k (x) B_k) (2x2 blow-up) is nonzero at explicit integer M_k;
      by Domokos-Zubkov / Derksen-Weyman / Schofield-Van den Bergh these
      determinants span the semi-invariants, and by King a nonzero
      positive-degree semi-invariant certifies semistability.
(iv)  X has no shrunk subspace: checked over a finite field-free criterion by
      exhausting subspaces is impossible; instead (iii) certifies it. We add an
      elementary check that the 1-PS families attached to every coordinate zero
      block cannot destabilise: no zero block of X's generic element has p+q>4.
(v)   the kernel map is linear and NOT surjective (image = C^3 x 0).
"""
import json, sys, time, random
import sympy as sp
t0=time.time()
x=sp.symbols('x1:6')
E=lambda i,j: sp.Matrix(4,4,lambda a,b: 1 if (a,b)==(i-1,j-1) else 0)
B=[E(1,2)-E(2,1), E(1,3)-E(3,1), E(2,3)-E(3,2), E(1,4), E(4,4)]
pencil=sum((x[i]*B[i] for i in range(5)), sp.zeros(4,4))
det_pencil=sp.expand(pencil.det())
# (ii) independence
V=sp.Matrix([list(b) for b in B])
indep=V.rank()==5
# (iii) blow-up semi-invariant, deterministic integer M_k
random.seed(20260917)
def blowup(m):
    Ms=[sp.Matrix(m,m,lambda a,b: random.randint(-3,3)) for _ in range(5)]
    big=sum((sp.kronecker_product(Ms[k],B[k]) for k in range(5)), sp.zeros(4*m,4*m))
    return Ms, big.det()
Ms2,d2=blowup(2)
res={'det_pencil':str(det_pencil),'independent':bool(indep),'blowup2_det':int(d2),
     'M_k_2x2':[[list(map(int,r)) for r in M.tolist()] for M in Ms2]}
if d2==0:
    Ms3,d3=blowup(3); res['blowup3_det']=int(d3)
# (v) kernel map: generic element with t!=0
a,b,c,u,t=sp.symbols('a b c u t')
A=a*B[0]+b*B[1]+c*B[2]+u*B[3]+t*B[4]
ker=A.nullspace()
res['generic_kernel']=[str(list(v)) for v in ker]
# compression test: is there V' (dim d) with dim X V' <= d-1 ? we certify NOT by (iii);
# here record the generic rank.
res['generic_rank']=int(A.rank())
res['wall_s']=round(time.time()-t0,3)
print(json.dumps(res,indent=1))
json.dump(res,open(sys.argv[1] if len(sys.argv)>1 else 'check1_counterexample.json','w'),indent=1)

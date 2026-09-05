#!/usr/bin/env python3
"""
Session 54 -- dimension of the q=1 boundary components of D_5^{det_4}.

Over a bounded-rank-3 base stratum E, the order-1 exceptional image is
  Y_E = closure{ f_1 = tr(adj M_0(s) . M_1(s)) : M_0 a pencil into E, M_1 free }.
dim Y_E = rank of the Jacobian of (params) -> f_1 in C^70, computed exactly mod p
by dual numbers (eps^2=0). This is the affine (cone) dimension in Sym^4 C^5.

DECISION RULE (PREREG T3 + the boundary argument):
  R_5 subset D_5  =>  R_5 subset boundary(D_5)  [since generic l.c not in the
  image, s32 Thm 5]  =>  some boundary component has dim >= dim R_5 = 39.
So if every boundary component has dim < 39, then R_5 not subset D_5.

Strata bases E (bounded-rank-3 spaces of M_4; s32 Thm 4 / Atkinson-HL):
  ker(12), coker(12), c21(10), c32(10), prim(4).
"""
import sys, random, itertools, json, argparse
sys.path.insert(0, 'analysis')
from flint import nmod_mat
P = 2147483647
R, n = 5, 4

# ---- dual-number scalars mod P: (a,b) ~ a + b*eps, eps^2=0 ----
def dadd(x, y): return ((x[0]+y[0]) % P, (x[1]+y[1]) % P)
def dsub(x, y): return ((x[0]-y[0]) % P, (x[1]-y[1]) % P)
def dmul(x, y): return ((x[0]*y[0]) % P, (x[0]*y[1]+x[1]*y[0]) % P)

# s-polynomials: dict{exp-tuple: dual scalar}
def spadd(acc, b, coef=(1,0)):
    for e, c in b.items():
        acc[e] = dadd(acc.get(e, (0,0)), dmul(coef, c))
def spmul(a, b):
    out = {}
    for ea, ca in a.items():
        for eb, cb in b.items():
            e = tuple(ea[i]+eb[i] for i in range(R))
            out[e] = dadd(out.get(e, (0,0)), dmul(ca, cb))
    return out

def linform(coeffs):
    """coeffs: list of R dual scalars -> linear s-poly."""
    d = {}
    for i in range(R):
        if coeffs[i] != (0,0):
            e = [0]*R; e[i] = 1; d[tuple(e)] = coeffs[i]
    return d

def det3(M):
    """3x3 determinant of a matrix of s-polys (dual)."""
    def term(p, sgn):
        pr = {(0,)*R: (sgn % P, 0)}
        for i in range(3): pr = spmul(pr, M[i][p[i]])
        return pr
    out = {}
    for p in itertools.permutations(range(3)):
        sgn = 1
        for i in range(3):
            for j in range(i+1,3):
                if p[i] > p[j]: sgn = -sgn
        spadd(out, term(p, sgn))
    return out

def adjugate(M0):
    """adj of 4x4 matrix M0 of s-polys (dual). adj_{ij} = (-1)^{i+j} minor_{ji}."""
    adj = [[None]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rows = [r for r in range(n) if r != j]
            cols = [c for c in range(n) if c != i]
            sub = [[M0[r][c] for c in cols] for r in rows]
            m = det3(sub)
            sgn = 1 if (i+j) % 2 == 0 else -1
            adj[i][j] = {e: (sgn*c[0] % P, sgn*c[1] % P) for e, c in m.items()}
    return adj

def f1_vector(M0mats, M1mats, QIDX):
    """M0mats,M1mats: list of R matrices (n x n) of dual scalars (the pencils'
    B_i, H_i). f_1 = tr(adj(M0(s)) M1(s)) as a dual 70-vector."""
    # build M0(s), M1(s) entries as linear s-polys (dual coeffs)
    M0 = [[linform([M0mats[k][a][b] for k in range(R)]) for b in range(n)] for a in range(n)]
    M1 = [[linform([M1mats[k][a][b] for k in range(R)]) for b in range(n)] for a in range(n)]
    adj = adjugate(M0)
    # tr(adj . M1) = sum_{i,j} adj[i][j] * M1[j][i]
    f = {}
    for i in range(n):
        for j in range(n):
            spadd(f, spmul(adj[i][j], M1[j][i]))
    val = [0]*len(QIDX); dval = [0]*len(QIDX)
    for e, c in f.items():
        val[QIDX[e]] = c[0] % P; dval[QIDX[e]] = c[1] % P
    return val, dval

# quartic exponent index
QEXP = []
def _q(k,left,cur):
    if k==R-1: QEXP.append(tuple(cur+[left])); return
    for v in range(left+1): _q(k+1,left-v,cur+[v])
_q(0,4,[])
QIDX = {e:i for i,e in enumerate(QEXP)}

def stratum_basis(name, rng):
    G = []
    if name == 'full':      # calibration: generic pencil, adj full rank; dim = dim D_5 = 50
        for a in range(n):
            for b in range(n):
                E=[[0]*n for _ in range(n)]; E[a][b]=1; G.append(E)
        return G
    if name in ('ker','coker'):
        for a in range(n):
            for b in range(n):
                if name=='ker' and b==0: continue      # col 0 = 0
                if name=='coker' and a==0: continue     # row 0 = 0
                E=[[0]*n for _ in range(n)]; E[a][b]=1; G.append(E)
    elif name=='c21':
        for a in range(n):
            for b in range(n):
                if b in (0,1) and a in (1,2,3): continue
                E=[[0]*n for _ in range(n)]; E[a][b]=1; G.append(E)
    elif name=='c32':   # (3,2): cols 0,1,2 -> rows 0,1 ; zero rows 2,3 of cols 0,1,2
        for a in range(n):
            for b in range(n):
                if b in (0,1,2) and a in (2,3): continue
                E=[[0]*n for _ in range(n)]; E[a][b]=1; G.append(E)
    elif name=='prim':
        phi=[[[0]*n for _ in range(n)] for _ in range(n)]
        for a in range(n):
            for b in range(n):
                for c in range(b+1,n):
                    v=rng.randint(1,P-1); phi[a][b][c]=v; phi[a][c][b]=(-v)%P
        for c in range(n):
            G.append([[phi[a][b][c] for b in range(n)] for a in range(n)])
    return G

def boundary_dim(name, seed=1):
    rng = random.Random(seed)
    G = stratum_basis(name, rng)      # basis of E, m matrices
    m = len(G)
    # base pencils: M0(s)=sum_i s_i (sum_j c_ij G_j); M1(s)=sum_i s_i H_i
    c = [[rng.randint(0,P-1) for _ in range(m)] for _ in range(R)]
    H = [[[rng.randint(0,P-1) for _ in range(n)] for _ in range(n)] for _ in range(R)]
    def M0mats(cc):
        return [[[sum(cc[i][j]*G[j][a][b] for j in range(m)) % P
                  for b in range(n)] for a in range(n)] for i in range(R)]
    # parameters: c_ij (R*m) and H entries (R*n*n)
    cols = []
    # M1 derivatives: linear in M1, exact columns = f_1 at (M0, unit H)
    M0base = M0mats(c)
    # helper: dual-off vectors
    def as_dual(mat): return mat  # placeholder
    # We compute Jacobian columns by dual perturbation of each param.
    def eval_dual(param_kind, idx):
        # build M0mats, H as dual scalars with one param carrying eps
        cc = [[ (c[i][j],0) for j in range(m)] for i in range(R)]
        HH = [[[ (H[i][a][b],0) for b in range(n)] for a in range(n)] for i in range(R)]
        if param_kind=='c':
            i,j = idx; cc[i][j] = (c[i][j],1)
        else:
            i,a,b = idx; HH[i][a][b] = (H[i][a][b],1)
        # M0mats as dual: entry (k,a,b) = sum_j cc[k][j]*G[j][a][b]
        M0d = [[[ (0,0) for b in range(n)] for a in range(n)] for k in range(R)]
        for k in range(R):
            for a in range(n):
                for b in range(n):
                    acc=(0,0)
                    for j in range(m):
                        if G[j][a][b]:
                            acc = dadd(acc, dmul(cc[k][j], (G[j][a][b]%P,0)))
                    M0d[k][a][b]=acc
        val,dval = f1_vector(M0d, HH, QIDX)
        return dval
    ncol_c = 0
    for i in range(R):
        for j in range(m):
            cols.append(eval_dual('c',(i,j))); ncol_c += 1
    Hcols = []
    for i in range(R):
        for a in range(n):
            for b in range(n):
                Hcols.append(eval_dual('H',(i,a,b)))
    allcols = cols + Hcols
    def rank_of(colset):
        if not colset: return 0
        M = nmod_mat(len(colset), len(QEXP),
                     [int(colset[r][cc]) for r in range(len(colset)) for cc in range(len(QEXP))], P)
        return M.rank()
    return dict(stratum=name, dimE=m, nparams=len(allcols),
                boundary_dim=rank_of(allcols),
                Honly_rank=rank_of(Hcols),   # tangent to D_5 if M0 generic (calib=50)
                ambient=len(QEXP))

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--strata', default='ker,coker,c21,c32,prim')
    ap.add_argument('--out', default='results/s54_boundary_dims.json')
    a = ap.parse_args()
    res = []
    for name in a.strata.split(','):
        r = boundary_dim(name)
        res.append(r)
        print(f"[{name}] dimE={r['dimE']} nparams={r['nparams']} "
              f"q1_boundary_dim={r['boundary_dim']} Honly={r['Honly_rank']} "
              f" (dim R_5=39, dim D_5=50)", flush=True)
    json.dump(res, open(a.out,'w'), indent=1)
    print("wrote", a.out)

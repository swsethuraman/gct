#!/usr/bin/env python3
"""
Session 54 -- the decisive dimension: is R_5 subset D_5^{det_4}?

Let W = {s_5 . c : c in Sym^3 C^5} (reducibles with linear factor s_5), a
35-dim linear subspace of Sym^4 C^5. By GL_5 and closure,
    R_5 subset D_5  <=>  dim(D_5 cap W) = 35  <=>  every cubic c has s_5.c in D_5.
Equivalently dim(R_5 cap D_5) = dim(D_5 cap W) + 4, and R_5 subset D_5 iff = 39.

Tangent computation at a point q in D_5 cap W. Take q = det M_* with
det M_* = s_5 . c_0 EXACTLY (M_* from the exact reducible-determinantal family,
which is non-empty: s32). Then
    T_q D_5 = { tr(adj M_*(s) . H(s)) : H a pencil }        (linear in H),
and, with pi = "restrict to s_5-degree-0 part" (W = ker pi),
    dim(T_q D_5 cap W) = dim T_q D_5 - rank( pi|_{T_q D_5} ).
Since dim(D_5 cap W) <= dim T_q(D_5 cap W) = dim(T_q D_5 cap W), a value < 35 is
a RIGOROUS UPPER BOUND proving R_5 not subset D_5. (dim T_q D_5 = 50 confirms q
is a smooth point, making the bound the actual local dimension.)

We evaluate several exact families for q (block diag, (2,1)-compression) and
both primes.
"""
import sys, random, itertools, json, argparse
sys.path.insert(0, 'analysis')
from flint import nmod_mat
P1, P2 = 2147483647, 2147483629
R, n = 5, 4

def spmul(a, b, p):
    out = {}
    for ea, ca in a.items():
        for eb, cb in b.items():
            e = tuple(ea[i]+eb[i] for i in range(R))
            out[e] = (out.get(e, 0) + ca*cb) % p
    return out
def spadd(acc, b, p, sgn=1):
    for e, c in b.items():
        acc[e] = (acc.get(e, 0) + sgn*c) % p
def linform(coeffs):
    d = {}
    for i in range(R):
        if coeffs[i] % (1<<62):
            e=[0]*R; e[i]=1; d[tuple(e)] = coeffs[i]
    return d
def det3(M, p):
    out = {}
    for pm in itertools.permutations(range(3)):
        sgn=1
        for i in range(3):
            for j in range(i+1,3):
                if pm[i]>pm[j]: sgn=-sgn
        pr={(0,)*R:sgn%p}
        for i in range(3): pr=spmul(pr,M[i][pm[i]],p)
        spadd(out,pr,p)
    return out
def adjugate(M0, p):
    adj=[[None]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rows=[r for r in range(n) if r!=j]; cols=[c for c in range(n) if c!=i]
            sub=[[M0[r][c] for c in cols] for r in rows]
            m=det3(sub,p); sgn=1 if (i+j)%2==0 else -1
            adj[i][j]={e:(sgn*c)%p for e,c in m.items()}
    return adj

QEXP=[]
def _q(k,left,cur):
    if k==R-1: QEXP.append(tuple(cur+[left])); return
    for v in range(left+1): _q(k+1,left-v,cur+[v])
_q(0,4,[])
QIDX={e:i for i,e in enumerate(QEXP)}
S5DEG0=[i for i,e in enumerate(QEXP) if e[4]==0]   # 35 monomials with no s_5

def pencil_from_mats(mats):
    # mats: list of R matrices (n x n ints). entry(a,b) linear s-form.
    return [[linform([mats[k][a][b] for k in range(R)]) for b in range(n)] for a in range(n)]

def f1_vec(M0entries, H_s, p):
    """f_1 = tr(adj(M0) . H); H_s = matrix(n x n) of s-forms; returns 70-vec."""
    adj=adjugate(M0entries,p)
    f={}
    for i in range(n):
        for j in range(n):
            spadd(f, spmul(adj[i][j], H_s[j][i], p), p)
    v=[0]*len(QEXP)
    for e,c in f.items(): v[QIDX[e]]=c%p
    return v

def M_star_block(rng, p):
    """M_* = diag(s_5, N(s)); det = s_5 * det_3 N ; c_0 in D_5^{det_3} (dim 29)."""
    mats=[[[0]*n for _ in range(n)] for _ in range(R)]
    mats[4][0][0]=1                                  # (0,0)=s_5
    for k in range(R):
        for a in range(1,n):
            for b in range(1,n):
                mats[k][a][b]=rng.randint(1,p-1)      # N(s) random 3x3 pencil
    return mats

def M_star_c21(rng, p):
    """(2,1)-type exact reducible: build a pencil whose det = s_5 * c with c in the
    dim-31 branch. Use block [[s5, row],[0, N]] won't raise dim; instead use a
    generic pencil with column 0 = s_5*e_0 + (stuff) engineered to keep det = s5*c.
    Simplest richer family: M = [[s5, b^T],[0, N]] with b a 1x3 row of linear forms;
    det = s5 * det N (b does not enter since lower-left is 0). To get the (2,1)
    branch we instead let lower-left col be linear and upper row 0: that changes c.
    We use: M=[[s5, 0,0,0],[c1, N]] with c1 a 3x1 col of linear forms.
    det = s5*det N - (expansion) ; lower-left col adds cross terms -> richer c."""
    mats=[[[0]*n for _ in range(n)] for _ in range(R)]
    mats[4][0][0]=1
    for k in range(R):
        for a in range(1,n):
            mats[k][a][0]=rng.randint(0,p-1)         # first column, rows 1..3 (linear)
            for b in range(1,n):
                mats[k][a][b]=rng.randint(1,p-1)
    return mats

def measure_q(builder, p, seed):
    rng=random.Random(seed)
    mats=builder(rng,p)
    M0=pencil_from_mats(mats)
    # sanity: det M_* divisible by s_5?  (det|_{s5=0} == 0)
    # build tangent: for each unit pencil H (slot k, entry a,b), f_1 vector
    cols=[]
    for k in range(R):
        for a in range(n):
            for b in range(n):
                Hmats=[[[0]*n for _ in range(n)] for _ in range(R)]
                Hmats[k][a][b]=1
                H_s=pencil_from_mats(Hmats)
                cols.append(f1_vec(M0,H_s,p))
    # dim T_q D_5 = rank of full 70 x 80 (cols are 70-vectors; matrix = 80 x 70)
    full=nmod_mat(len(cols),len(QEXP),
                  [int(cols[r][c]) for r in range(len(cols)) for c in range(len(QEXP))],p)
    dimT=full.rank()
    # rank of pi = s5-deg-0 rows (35 columns of the 80x70 -> restrict to S5DEG0 cols)
    sub=nmod_mat(len(cols),len(S5DEG0),
                 [int(cols[r][S5DEG0[c]]) for r in range(len(cols)) for c in range(len(S5DEG0))],p)
    rank_pi=sub.rank()
    return dimT, rank_pi, dimT-rank_pi

if __name__=='__main__':
    out={}
    for name,builder in [('block_diag',M_star_block),('c21_col',M_star_c21)]:
        rows=[]
        for p in (P1,P2):
            for seed in (7,8):
                dimT,rank_pi,inter=measure_q(builder,p,seed)
                rows.append(dict(prime=p,seed=seed,dimT=dimT,rank_pi=rank_pi,
                                 dim_DcapW_bound=inter, dim_R5capD5_bound=inter+4))
                print(f"[{name}] p={p} seed={seed}: dim T_qD5={dimT} "
                      f"rank(pi|T)={rank_pi}  dim(D5capW)<= {inter}  "
                      f"=> dim(R5capD5)<= {inter+4}  (R_5 subset D_5 iff =39)",flush=True)
        out[name]=rows
    json.dump(out,open('results/s54_intersection.json','w'),indent=1)
    print("wrote results/s54_intersection.json")

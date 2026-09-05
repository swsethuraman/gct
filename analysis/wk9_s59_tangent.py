#!/usr/bin/env python3
"""
Session 59 -- section 2C : first-order tangent to D_5 at a reducible q_0 = s_5 c_0,
intersected with W, at two kinds of reducible :

  (A) SPECIAL  q = s_5 . det_3(N)  (c_0 a 3x3 determinant, in the 29-family).
      This is s54's point. Its determinantal fibre carries genuinely inequivalent
      BLOCK representations -- upper-triangular [[s5, r],[0,N]] and lower-
      triangular [[s5,0],[c,N]] are in the fibre for ALL r,c (triangular-block
      det = s5 det N = q), plus GL_3 acting on N. The union of im dPhi over these
      saturates the Zariski-tangent lower bound; s54 reported 64. Reproducing 64
      cross-checks the machinery against s54 ; then intersect with W.

  (B) GENERIC  q = s_5 c_0, c_0 in the 31-family (c21 exact config, NOT a 3x3
      determinant). No block representation exists, so the natural determinantal
      representation's tangent im dPhi is the honest object (48 here). Intersect
      with W.

dim(T cap W) = dim T - rank(pi|_T),  pi : f |-> f|_{s5=0} (35 coords).
This is a lower bound on dim T_{q_0}(D_5 cap W) (an upper bound on the local
dim of D_5 cap W), so it is corroborating evidence, not a proof either way.
"""
import sys, random, argparse, json
sys.path.insert(0, 'analysis')
from flint import nmod_mat
from wk9_s59_core import (R, n, NQ, QIDX, S5DEG0, det_arc, pencils_to_entry,
                          rank_mod, quartic_vec, stratum_E_basis)
from wk9_s59_exact import A_in_E

P1, P2 = 2147483647, 2147483629

def im_dPhi_cols(B, p):
    """columns { tr(adj M(s) N(s)) : N one-hot } = im dPhi_M, 80 quartic vecs."""
    cols = []
    for k in range(R):
        for a in range(n):
            for b in range(n):
                D = [[[0]*n for _ in range(n)] for _ in range(R)]
                D[k][a][b] = 1
                entry = pencils_to_entry([B], p, duals=[D])
                det = det_arc(entry, p, 0)
                cols.append(quartic_vec(det.get(0, {}), p, part=1))
    return cols

def cap_W(rows, p):
    dimT = rank_mod(rows, NQ, p)
    piRows = [[row[j] for j in S5DEG0] for row in rows]
    rk_pi = rank_mod(piRows, len(S5DEG0), p)
    return dimT, dimT - rk_pi

# ---------- (A) special point q = s5 * det_3(N) : block reps ----------
def matmul(P, M, p):
    return [[sum(P[a][k]*M[k][b] for k in range(n)) % p for b in range(n)] for a in range(n)]

def special_saturate(p, seed=7):
    rng = random.Random(seed)
    # N(s) : 3x3 pencil (linear forms in s_1..s_5) -> use as lower-right block
    N = [[[rng.randint(1, p-1) for _ in range(3)] for _ in range(3)] for _ in range(R)]
    def block(r=None, c=None):
        """M = [[s5, r],[c, N]] as a 5-var 4x4 pencil B_k[a][b]."""
        B = [[[0]*n for _ in range(n)] for _ in range(R)]
        B[4][0][0] = 1                       # (0,0) entry = s_5
        for a in range(3):
            for b in range(3):
                for k in range(R):
                    B[k][a+1][b+1] = N[k][a][b] % p
        if r is not None:                    # top row (0, b+1) = r_b(s)
            for b in range(3):
                for k in range(R):
                    B[k][0][b+1] = r[b][k] % p
        if c is not None:                    # left col (a+1, 0) = c_a(s)
            for a in range(3):
                for k in range(R):
                    B[k][a+1][0] = c[a][k] % p
        return B
    reps = [block()]
    for _ in range(4):                       # upper-tri : random top row, c=0
        r = [[rng.randint(0, p-1) for _ in range(R)] for _ in range(3)]
        reps.append(block(r=r, c=None))
    for _ in range(4):                       # lower-tri : random left col, r=0
        c = [[rng.randint(0, p-1) for _ in range(R)] for _ in range(3)]
        reps.append(block(r=None, c=c))
    for _ in range(4):                       # GL_3 conjugates of N (new tangents)
        P3 = [[rng.randint(0, p-1) for _ in range(3)] for _ in range(3)]
        Q3 = [[rng.randint(0, p-1) for _ in range(3)] for _ in range(3)]
        Nc = [[[sum(P3[a][i]*N[k][i][j]*0 for i in range(3)) for j in range(3)] for a in range(3)] for k in range(R)]
        # conjugate each slice : N'_k = P3 N_k Q3
        Bc = [[[0]*n for _ in range(n)] for _ in range(R)]
        Bc4 = block()
        for k in range(R):
            Nk = [[N[k][i][j] for j in range(3)] for i in range(3)]
            PN = [[sum(P3[a][i]*Nk[i][j] for i in range(3)) % p for j in range(3)] for a in range(3)]
            PNQ = [[sum(PN[a][j]*Q3[j][b] for j in range(3)) % p for b in range(3)] for a in range(3)]
            for a in range(3):
                for b in range(3):
                    Bc[k][a+1][b+1] = PNQ[a][b]
            Bc[4][0][0] = 1
        reps.append(Bc)
    rows = []; curve = []
    for i, B in enumerate(reps):
        rows.extend(im_dPhi_cols(B, p))
        curve.append(rank_mod(rows, NQ, p))
    dimT, dimTW = cap_W(rows, p)
    single = rank_mod(im_dPhi_cols(reps[0], p), NQ, p)
    return dict(single_rep=single, dimT=dimT, curve=curve, dim_T_cap_W=dimTW,
                nreps=len(reps))

# ---------- (B) generic point q = s5 c_0 (c21 config) ----------
def generic_point(p, seed=3):
    rng = random.Random(seed)
    Eb = stratum_E_basis('c21', rng, p); m = len(Eb)
    u = [[rng.randint(1, p-1) for _ in range(m)] for _ in range(4)]
    A5 = [[rng.randint(1, p-1) for _ in range(n)] for _ in range(n)]
    Ai = [A_in_E(Eb, u[i], p) for i in range(4)]
    B = [[[0]*n for _ in range(n)] for _ in range(R)]
    for i in range(4):
        for a in range(n):
            for b in range(n):
                B[i][a][b] = Ai[i][a][b]
    for a in range(n):
        for b in range(n):
            B[4][a][b] = A5[a][b]
    rows = im_dPhi_cols(B, p)
    dimT, dimTW = cap_W(rows, p)
    return dict(single_rep=dimT, dim_T_cap_W=dimTW)

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--primes', default='both')
    ap.add_argument('--out', default='results/s59_tangent.json')
    a = ap.parse_args()
    primes = [P1, P2] if a.primes == 'both' else [int(a.primes)]
    res = {}
    for p in primes:
        A = special_saturate(p)
        Bd = generic_point(p)
        res[str(p)] = {'special_det3': A, 'generic_c21': Bd}
        print(f"[p={p}] (A) special q=s5*det3(N): single_rep im dPhi={A['single_rep']} "
              f"(s54: <=42)  saturated dim T={A['dimT']} (s54: 64)  curve={A['curve']}",
              flush=True)
        print(f"[p={p}]     dim(T cap W) at special point = {A['dim_T_cap_W']}", flush=True)
        print(f"[p={p}] (B) generic q=s5 c_0 (c21): im dPhi={Bd['single_rep']}  "
              f"dim(im dPhi cap W) = {Bd['dim_T_cap_W']}  (exact locus = 31)", flush=True)
    json.dump(res, open(a.out, 'w'), indent=1)
    print("wrote", a.out)

#!/usr/bin/env python3
"""
Session 59 -- emit a gct-cert/1 `matrix` certificate for the load-bearing claim:
the exact reducible-determinantal Jacobian at the c21 config has rank 31, so
dim(D_5 cap W) >= 31 (fixing l = s_5). Integer arithmetic throughout (dual
numbers over Z), so the verifier's exact rank-over-Q check applies. The matrix is
the 35 x P Jacobian d c / d(params), c = det M / s_5 a cubic (35 coords), params
= the A_i (i<5) coords in the c21 space and the entries of A_5.
"""
import sys, random, itertools, json, argparse
sys.path.insert(0, 'analysis')

n, R = 4, 5

# ---- integer linear/poly arithmetic in dual numbers (val, dval), eps^2 = 0 ----
def dmulZ(x, y): return (x[0]*y[0], x[0]*y[1] + x[1]*y[0])
def daddZ(x, y): return (x[0]+y[0], x[1]+y[1])

def poly_mul_lf_Z(poly, lf):
    out = {}
    for e1, c1 in poly.items():
        for k2, c2 in lf.items():
            e = list(e1); e[k2] += 1; e = tuple(e)
            out[e] = daddZ(out.get(e, (0, 0)), dmulZ(c1, c2))
    return out

def detZ(entry):
    """entry[a][b] = linear form {var:(val,dval)}. Return quartic {exp5:(val,dval)}."""
    out = {}
    for perm in itertools.permutations(range(n)):
        sgn = 1; pl = list(perm)
        for i in range(n):
            for j in range(i+1, n):
                if pl[i] > pl[j]: sgn = -sgn
        prod = {(0,)*R: (sgn, 0)}
        for a in range(n):
            lf = entry[a][perm[a]]
            prod = poly_mul_lf_Z(prod, lf)
        for e, c in prod.items():
            out[e] = daddZ(out.get(e, (0, 0)), c)
    return out

# cubic / quartic exponent indexing
def mk_exp(deg):
    out = []
    def rec(k, left, cur):
        if k == R-1: out.append(tuple(cur+[left])); return
        for v in range(left+1): rec(k+1, left-v, cur+[v])
    rec(0, deg, []); return out
CEXP = mk_exp(3); CIDX = {e: i for i, e in enumerate(CEXP)}

def c21_basis():
    G = []
    for a in range(n):
        for b in range(n):
            if b in (0, 1) and a in (1, 2, 3): continue
            E = [[0]*n for _ in range(n)]; E[a][b] = 1; G.append(E)
    return G

def entry_from(Ai, A5, dual=None):
    """Ai[i] (i<4) and A5 integer 4x4 ; M(s)=s5 A5 + sum_{i<4} s_i A_i.
    entry[a][b] = {var:(val,dval)} ; dual=('Ai',i,a,b) or ('A5',a,b)."""
    ent = [[dict() for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            d = {}
            for i in range(4):
                if Ai[i][a][b]:
                    d[i] = (Ai[i][a][b], 0)
            if A5[a][b]:
                d[4] = (A5[a][b], 0)
            # dual
            if dual and dual[0] == 'Ai' and dual[1] is not None:
                _, i, aa, bb = dual
                if a == aa and b == bb:
                    d[i] = (d.get(i, (0, 0))[0], d.get(i, (0, 0))[1] + 1)
            if dual and dual[0] == 'A5':
                _, aa, bb = dual
                if a == aa and b == bb:
                    d[4] = (d.get(4, (0, 0))[0], d.get(4, (0, 0))[1] + 1)
            ent[a][b] = d
    return ent

def c_col(Ai, A5, dual):
    ent = entry_from(Ai, A5, dual)
    q = detZ(ent)
    col = [0]*len(CEXP)
    for e, c in q.items():
        if e[4] == 0:
            assert c[0] == 0, "det not divisible by s5 at the point"
            continue
        ce = (e[0], e[1], e[2], e[3], e[4]-1)
        col[CIDX[ce]] = c[1]      # dual part = derivative
    return col

def build_matrix(seed=3, lohi=7):
    rng = random.Random(seed)
    Eb = c21_basis(); m = len(Eb)
    u = [[rng.randint(-lohi, lohi) for _ in range(m)] for _ in range(4)]
    A5 = [[rng.randint(-lohi, lohi) for _ in range(n)] for _ in range(n)]
    def A_of(coords):
        A = [[0]*n for _ in range(n)]
        for j, Eb_j in enumerate(Eb):
            for a in range(n):
                for b in range(n):
                    if Eb_j[a][b]: A[a][b] += coords[j]*Eb_j[a][b]
        return A
    Ai = [A_of(u[i]) for i in range(4)]
    cols = []           # each column = d c / d param (length 35)
    params = []
    for i in range(4):
        for j in range(m):
            # direction : move A_i along E_j
            dcol = c_col_dir(Eb, Ai, A5, i, j)
            cols.append(dcol); params.append(('Ai', i, j))
    for a in range(n):
        for b in range(n):
            cols.append(c_col(Ai, A5, ('A5', a, b))); params.append(('A5', a, b))
    # matrix rows = 35 cubic coords, columns = params ; transpose to rows x cols
    P = len(cols)
    mat = [[cols[j][r] for j in range(P)] for r in range(len(CEXP))]  # 35 x P
    return mat, params

def c_col_dir(Eb, Ai, A5, i, j):
    """derivative of c wrt moving A_i along basis matrix E_j (integer)."""
    ent = [[dict() for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            d = {}
            for ii in range(4):
                if Ai[ii][a][b]:
                    d[ii] = (Ai[ii][a][b], 0)
            if A5[a][b]:
                d[4] = (A5[a][b], 0)
            if Eb[j][a][b]:
                d[i] = (d.get(i, (0, 0))[0], d.get(i, (0, 0))[1] + Eb[j][a][b])
            ent[a][b] = d
    q = detZ(ent)
    col = [0]*len(CEXP)
    for e, c in q.items():
        if e[4] == 0:
            assert c[0] == 0
            continue
        ce = (e[0], e[1], e[2], e[3], e[4]-1)
        col[CIDX[ce]] = c[1]
    return col

def find_minor(mat, p, want):
    """find `want` independent rows and cols mod p ; return (rows, cols)."""
    from flint import nmod_mat
    m = len(mat); ncol = len(mat[0])
    # independent columns
    A = nmod_mat(m, ncol, [int(mat[r][c]) % p for r in range(m) for c in range(ncol)], p)
    # column pivots via reduced row echelon of transpose
    At = nmod_mat(ncol, m, [int(mat[r][c]) % p for c in range(ncol) for r in range(m)], p)
    rr, rank = At.rref()
    pivot_cols = []
    used = set()
    # greedy: pick columns of mat that raise the rank
    cur = None; chosen = []
    from flint import nmod_mat as NM
    rows_acc = []
    cols_pick = []
    r0 = 0
    for c in range(ncol):
        trial = cols_pick + [c]
        sub = NM(m, len(trial), [int(mat[r][t]) % p for r in range(m) for t in trial], p)
        if sub.rank() > r0:
            cols_pick.append(c); r0 = sub.rank()
        if r0 == want: break
    rows_pick = []; r0 = 0
    for r in range(m):
        trial = rows_pick + [r]
        sub = NM(len(trial), len(cols_pick), [int(mat[t][c]) % p for t in trial for c in cols_pick], p)
        if sub.rank() > r0:
            rows_pick.append(r); r0 = sub.rank()
        if r0 == want: break
    return rows_pick, cols_pick

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default='results/certs/s59_exact31.json')
    a = ap.parse_args()
    P1, P2 = 2147483647, 2147483629
    mat, params = build_matrix()
    from flint import nmod_mat
    m, ncol = len(mat), len(mat[0])
    r1 = nmod_mat(m, ncol, [int(mat[r][c]) % P1 for r in range(m) for c in range(ncol)], P1).rank()
    r2 = nmod_mat(m, ncol, [int(mat[r][c]) % P2 for r in range(m) for c in range(ncol)], P2).rank()
    print(f"matrix {m}x{ncol} rank mod P1={r1} mod P2={r2}")
    rows_pick, cols_pick = find_minor(mat, P1, r1)
    cert = {
        "format": "gct-cert/1", "kind": "matrix",
        "title": f"s59: exact reducible-determinantal Jacobian at the c21 config has rank {r1} (dim(D_5 cap W) >= {r1})",
        "produced_by": "analysis/wk9_s59_cert.py (session 59)",
        "matrix": mat,
        "claimed_rank_Q": r1,
        "claimed_ranks_mod_p": {str(P1): r1, str(P2): r2},
        "nonvanishing_minor": {"rows": rows_pick, "cols": cols_pick},
        "notes": ("Jacobian of c = det(s5 A5 + sum_{i<5} s_i A_i)/s_5, A_i in the "
                  "c21 bounded-rank-3 space, over Z at a random integer point; rows "
                  "= 35 cubic coords, columns = A_i coords + A_5 entries. Rank = "
                  "dim of the exact reducible locus fixing l=s_5 = 31 (s32).")
    }
    import os
    os.makedirs('results/certs', exist_ok=True)
    json.dump(cert, open(a.out, 'w'))
    print("wrote", a.out, "rows_pick", len(rows_pick), "cols_pick", len(cols_pick))

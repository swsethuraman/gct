"""Part (C) fixed: stabilizer subalgebras of the boundary components (left null space)."""
import itertools
import numpy as np
import sympy as sp

X = sp.symbols('x1:10')
M_tr = sp.Matrix(3, 3, lambda i, j: X[3*i+j]); M_tr[2, 2] = -X[0]-X[4]
P1 = sp.expand(M_tr.det())
P2 = sp.expand(X[3]*X[0]**2 + X[4]*X[1]**2 + X[5]*X[2]**2
               + X[6]*X[0]*X[1] + X[7]*X[1]*X[2] + X[8]*X[0]*X[2])
mons9 = [m for m in itertools.combinations_with_replacement(range(9), 3)]
mon_ix = {m: i for i, m in enumerate(mons9)}

def act_matrix(f):
    rows = []
    for s in range(9):
        for t in range(9):
            d = sp.expand(X[s]*sp.diff(f, X[t]))
            Pd = sp.Poly(d, *X)
            v = np.zeros(len(mons9))
            for mono, cf in Pd.terms():
                if cf == 0 or sum(mono) != 3: continue
                idx = tuple(sorted([i for i in range(9) for _ in range(mono[i])]))
                v[mon_ix[idx]] = float(cf)
            rows.append(v)
    return np.array(rows)

def left_null(A, tol=1e-8):
    U, s, Vh = np.linalg.svd(A.T)
    rank = int((s > tol*max(A.shape)*s[0]).sum())
    return Vh[rank:, :].T          # vectors v with A^T v = 0, i.e. sum v_i row_i = 0

for name, f in [("P1 (traceless det)", P1), ("P2 (universal quadric)", P2)]:
    A = act_matrix(f)
    ns = left_null(A)
    dim = ns.shape[1]
    mats = [ns[:, i].reshape(9, 9) for i in range(dim)]
    G = np.zeros((dim, dim))
    for i in range(dim):
        for j in range(dim):
            G[i, j] = np.trace(mats[i] @ mats[j])
    rk = np.linalg.matrix_rank(G, tol=1e-6)
    print(f"stab({name}): dim = {dim} (expect 17), trace-form rank = {rk}",
          "-> degenerate: nonreductive directions present" if rk < dim else "-> nondegenerate on range")

"""B20-01 flag-locus reduction utilities (Theorem A of docs/b20_01_report.md).

Adapted coordinates (B18-02 par. 1): a = Y[0][0], r = Y[0][1:], c = Y[1:][0], block E = Sigma + A(v),
A(v)_{ij} = -eps_{ijk} v_k (0-based block indices).  nu_k := A(e_k).  W' = {Y : v = 0} (dim 13).
For a tuple Y = (Y_1..Y_5) with skew matrix v (3 x 5, v[k][m] = v_k of Y_m) of rank 3, choose g in GL_5 with
rows u_1, u_2 spanning ker v and v u_{k+2} = e_k.  Then Ytilde = g.Y has the slice form
    (Z_1, Z_2, Z_3 + nu_1, Z_4 + nu_2, Z_5 + nu_3),   Z_i in W',
and for every z in M and every skew degree n:  z^{[n]}(Ytilde) = det(g)^4 z^{[n]}(Y)   (column tensors scale by det g).
On the slice, z^{[11]} = F_1 + F_2 + F_3 with F_k(Z_1, Z_2, Z_{k+2}) := z^{[11]} at the tuple that keeps only Z_{k+2}
among (Z_3, Z_4, Z_5).  At such a tuple, scaling the nu's by u gives z(u) = sum_{n=8}^{12} u^n z^{[n]} (five nodes).
All arithmetic mod P = 524287.  Uses only the pinned runner/carrier (b20_01_pinned)."""
import numpy as np
P = 524287
INV2 = pow(2, P - 2, P)

def eps3(i, j, k):
    return 1 if (i, j, k) in ((0, 1, 2), (1, 2, 0), (2, 0, 1)) else (-1 if (i, j, k) in ((0, 2, 1), (2, 1, 0), (1, 0, 2)) else 0)

def nu_matrices():
    NU = []
    for k in range(3):
        m = np.zeros((4, 4), dtype=np.int64)
        for i in range(3):
            for j in range(3): m[i + 1, j + 1] = -eps3(i, j, k)
        NU.append(m % P)
    return NU
NU = nu_matrices()

def skew_coords(Y):
    """v[k][m] mod P for a (5,4,4) tuple; v_k = -(1/2) sum_{ij} eps_{ijk} K_{ij}, K the skew part of the block."""
    Y = Y % P
    E = Y[:, 1:, 1:]
    K = ((E - np.swapaxes(E, 1, 2)) * INV2) % P
    v = np.zeros((3, 5), dtype=np.int64)
    for k in range(3):
        for i in range(3):
            for j in range(3):
                if eps3(i, j, k): v[k, :] = (v[k, :] - eps3(i, j, k) * K[:, i, j]) % P
    v = (v * INV2) % P
    return v

def wprime_part(Y):
    """Remove the skew part of the block (projection W -> W' along W_0), mod P."""
    Y = Y % P
    E = Y[:, 1:, 1:]
    S = ((E + np.swapaxes(E, 1, 2)) * INV2) % P
    Z = Y.copy(); Z[:, 1:, 1:] = S
    return Z

def reconstruct(Y):
    """Y_m == W'-part(Y_m) + sum_k v[k][m] nu_k  (mod P): self-check of the sign conventions."""
    v = skew_coords(Y); Z = wprime_part(Y)
    R = Z.copy()
    for m in range(5):
        for k in range(3): R[m] = (R[m] + v[k, m] * NU[k]) % P
    return bool(np.array_equal(R % P, Y % P))

def inv_mod(x): return pow(int(x) % P, P - 2, P)

def solve_mod(A, b):
    """One solution x of A x = b mod P (A: 3x5 rank 3) and a basis of ker A; Gauss-Jordan mod P."""
    A = [[int(x) % P for x in row] + [int(bb) % P] for row, bb in zip(A, b)]
    m, n = len(A), len(A[0]) - 1
    piv = []; r = 0
    for col in range(n):
        p = next((i for i in range(r, m) if A[i][col]), None)
        if p is None: continue
        A[r], A[p] = A[p], A[r]; iv = inv_mod(A[r][col]); A[r] = [(x * iv) % P for x in A[r]]
        for i in range(m):
            if i != r and A[i][col]: f = A[i][col]; A[i] = [(x - f * y) % P for x, y in zip(A[i], A[r])]
        piv.append(col); r += 1
        if r == m: break
    assert r == 3, 'skew matrix v has rank %d < 3 at this point' % r
    x = [0] * n
    for i, col in enumerate(piv): x[col] = A[i][n]
    free = [j for j in range(n) if j not in piv]
    kernel = []
    for fj in free:
        k = [0] * n; k[fj] = 1
        for i, col in enumerate(piv): k[col] = (-A[i][fj]) % P
        kernel.append(k)
    return x, kernel

def det_mod(M):
    n = len(M); A = [[int(x) % P for x in r] for r in M]; det = 1
    for k in range(n):
        p = next((i for i in range(k, n) if A[i][k]), None)
        if p is None: return 0
        if p != k: A[k], A[p] = A[p], A[k]; det = (-det) % P
        det = det * A[k][k] % P; iv = inv_mod(A[k][k])
        for i in range(k + 1, n):
            f = A[i][k] * iv % P; A[i] = [(x - f * y) % P for x, y in zip(A[i], A[k])]
    return det

def slice_form(Y):
    """Returns (g, detg, Ztilde) with Ztilde the (5,4,4) tuple g.Y in slice form and its W'-parts.
    g rows: u_1, u_2 (kernel of v), u_{k+2} with v u_{k+2} = e_k."""
    v = skew_coords(Y)
    rows = []
    x0, ker = solve_mod(v, [0, 0, 0]); assert len(ker) == 2
    rows += ker
    for k in range(3):
        e = [1 if i == k else 0 for i in range(3)]
        x, _ = solve_mod(v, e); rows.append(x)
    g = np.array(rows, dtype=np.int64) % P
    detg = det_mod(rows); assert detg != 0
    Yt = np.zeros((5, 4, 4), dtype=np.int64)
    for i in range(5):
        for m in range(5): Yt[i] = (Yt[i] + g[i, m] * (Y[m] % P)) % P
    vt = skew_coords(Yt)
    want = np.array([[0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]], dtype=np.int64)
    assert np.array_equal(vt, want), (vt, want)
    return g, detg, Yt

def tuple_F(Z1, Z2, Z, k, u):
    """The tuple (Z_1, Z_2, [Z]+u nu_1, [Z]+u nu_2, [Z]+u nu_3) with Z placed in slot k+2 only, mod P."""
    T = np.zeros((5, 4, 4), dtype=np.int64)
    T[0] = Z1 % P; T[1] = Z2 % P
    for j in range(3):
        T[2 + j] = ((Z % P) if j == k else 0) + (u % P) * NU[j]
        T[2 + j] %= P
    return T

NODES5 = [1, 2, 3, 4, 5]
def vandermonde_solve(nodes, values, degrees):
    """Coefficients c_d (d in degrees) with values[i] = sum_d c_d nodes[i]^d mod P."""
    n = len(nodes); assert n == len(degrees)
    A = [[pow(int(t), d, P) for d in degrees] + [int(val) % P] for t, val in zip(nodes, values)]
    for col in range(n):
        p = next((i for i in range(col, n) if A[i][col]), None); assert p is not None
        A[col], A[p] = A[p], A[col]; iv = inv_mod(A[col][col]); A[col] = [(x * iv) % P for x in A[col]]
        for i in range(n):
            if i != col and A[i][col]: f = A[i][col]; A[i] = [(x - f * y) % P for x, y in zip(A[i], A[col])]
    return {d: A[i][n] for i, d in enumerate(degrees)}

def rank_mod(rows):
    M = [[int(x) % P for x in r] for r in rows]; rk = 0; ncol = len(M[0]) if M else 0
    for col in range(ncol):
        p = next((i for i in range(rk, len(M)) if M[i][col]), None)
        if p is None: continue
        M[rk], M[p] = M[p], M[rk]; iv = inv_mod(M[rk][col]); M[rk] = [(x * iv) % P for x in M[rk]]
        for i in range(len(M)):
            if i != rk and M[i][col]: f = M[i][col]; M[i] = [(x - f * y) % P for x, y in zip(M[i], M[rk])]
        rk += 1
        if rk == len(M): break
    return rk

#!/usr/bin/env python3
"""
Session 66 -- independent re-derivation of the headline tangent rows (generic P,
generic SP, P cap SP, P cap coker) sharing no code with wk10_s66_core /
wk9_s59_core :

  * dPhi_{M_0}(N) = tr(adj M_0(s) N(s)) with adj M_0(s) computed as a 4x4 matrix
    of cubic forms by explicit 3x3 cofactors over F_p (dict polynomials), never
    by dual numbers or det_arc ;
  * the tangent space of the component as the Jacobian of the parametrisation
    obtained by sympy's symbolic differentiation over Z, evaluated at the point ;
  * ranks by python-flint at a THIRD prime, 2147483587.
"""
import sys, random, itertools, json
sys.path.insert(0, 'analysis')
from flint import nmod_mat
import sympy as sp

P3 = 2147483587
R, n = 5, 4

# ---- dict polynomials in s_1..s_5 over F_p : {exp tuple: coeff}
def padd(a, b, p):
    out = dict(a)
    for e, c in b.items():
        out[e] = (out.get(e, 0) + c) % p
    return {e: c for e, c in out.items() if c}
def pmul(a, b, p):
    out = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            e = tuple(x + y for x, y in zip(e1, e2))
            out[e] = (out.get(e, 0) + c1*c2) % p
    return {e: c for e, c in out.items() if c}
def pscale(a, c, p): return {e: (v*c) % p for e, v in a.items() if (v*c) % p}
def lin(vec, p):
    out = {}
    for k in range(R):
        if vec[k] % p:
            e = [0]*R; e[k] = 1; out[tuple(e)] = vec[k] % p
    return out

def det3(M, p):
    """M : 3x3 of polynomials."""
    t = {}
    for perm in itertools.permutations(range(3)):
        sgn = 1
        for i in range(3):
            for j in range(i+1, 3):
                if perm[i] > perm[j]: sgn = -sgn
        prod = {(0,)*R: sgn % p}
        for i in range(3): prod = pmul(prod, M[i][perm[i]], p)
        t = padd(t, prod, p)
    return t

def adjugate(M, p):
    """adj(M)_{ij} = (-1)^{i+j} det(M with row j, column i deleted)."""
    adj = [[None]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rows = [r for r in range(n) if r != j]; cols = [c for c in range(n) if c != i]
            sub = [[M[r][c] for c in cols] for r in rows]
            adj[i][j] = pscale(det3(sub, p), (-1)**(i+j) % p, p)
    return adj

QEXP = sorted({e for e in itertools.product(range(5), repeat=R) if sum(e) == 4})
QIDX = {e: i for i, e in enumerate(QEXP)}
assert len(QEXP) == 70

def dPhi_indep(pen, p):
    """70 x 80 matrix of dPhi via the explicit adjugate."""
    M = [[lin([pen[k][a][b] for k in range(R)], p) for b in range(n)] for a in range(n)]
    adj = adjugate(M, p)
    cols = []
    for k in range(R):
        for a in range(n):
            for b in range(n):
                # N = E_ab * s_k ;  tr(adj N) = adj[b][a] * s_k
                e = [0]*R; e[k] = 1
                q = pmul(adj[b][a], {tuple(e): 1}, p)
                v = [0]*70
                for ee, c in q.items(): v[QIDX[ee]] = c
                cols.append(v)
    return nmod_mat(70, 80, [cols[j][i] for i in range(70) for j in range(80)], p)

# ---- sympy parametrisations
PAIRS = [(b, c) for b in range(n) for c in range(b+1, n)]
def sym_prim(phi, u):
    """phi 4x6 symbols, u 5x4 : pencil B_k[a][b] = sum_c phit[a][b][c] u_k[c] with
    phit[a][b][c] = phi[a][(b,c)] for b<c, -phi[a][(c,b)] for b>c."""
    pen = []
    for k in range(R):
        B = [[0]*n for _ in range(n)]
        for a in range(n):
            for si, (b, c) in enumerate(PAIRS):
                B[a][b] += phi[a][si]*u[k][c]
                B[a][c] -= phi[a][si]*u[k][b]
        pen.append(B)
    return pen

def sym_sp(phi, x, c, P, Q):
    def N(v): return sp.Matrix([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
    pen = []
    for k in range(R):
        L = sp.Matrix(phi) * N(x[k])
        B = sp.zeros(n, n)
        for a in range(n):
            for j in range(3): B[a, j] = L[a, j]
            B[a, 3] = c[k][a]
        B = sp.Matrix(P) * B * sp.Matrix(Q)
        pen.append([[B[a, b] for b in range(n)] for a in range(n)])
    return pen

def jac_rank(pen_expr, params, subs, p):
    flat = [pen_expr[k][a][b] for k in range(R) for a in range(n) for b in range(n)]
    J = [[sp.diff(f, v) for v in params] for f in flat]
    Jn = [[int(sp.Poly(entry, *params).eval(subs) if entry != 0 else 0) % p if not isinstance(entry, int) else 0
           for entry in row] for row in J]
    return nmod_mat(80, len(params), [x for row in Jn for x in row], p).rank()

def eval_pen(pen_expr, params, vals, p):
    d = dict(zip(params, vals))
    return [[[int(sp.sympify(pen_expr[k][a][b]).subs(d)) % p for b in range(n)] for a in range(n)] for k in range(R)]

def run(p=P3, seed=11):
    rng = random.Random(seed)
    out = {}
    # ---- generic P
    phi = [[sp.Symbol(f'f{a}{s}') for s in range(6)] for a in range(n)]
    u = [[sp.Symbol(f'u{k}{c}') for c in range(n)] for k in range(R)]
    params = [v for row in phi for v in row] + [v for row in u for v in row]
    pen_expr = sym_prim(phi, u)
    vals = [rng.randint(1, p-1) for _ in params]
    pen = eval_pen(pen_expr, params, vals, p)
    dP = dPhi_indep(pen, p); rk = dP.rank()
    d = dict(zip(params, vals))
    T = jac_rank(pen_expr, params, [vals[i] for i in range(len(params))], p) if False else None
    # Jacobian by sympy substitution (explicit)
    flat = [pen_expr[k][a][b] for k in range(R) for a in range(n) for b in range(n)]
    Jn = [[int(sp.diff(f, v).subs(d)) % p for v in params] for f in flat]
    T = nmod_mat(80, len(params), [x for row in Jn for x in row], p).rank()
    # every Jacobian column annihilates dPhi ?
    cols = [[Jn[i][j] for i in range(80)] for j in range(len(params))]
    bad = sum(1 for cvec in cols if any(int(x) for x in (dP * nmod_mat(80, 1, cvec, p)).entries()))
    out['P_generic'] = dict(rank_dPhi=rk, dim_ker=80-rk, dim_T=T, bad=bad, quotient=80-rk-T)
    print(f"[indep p={p}] generic P : rank dPhi={rk} ker={80-rk} T_P={T} (bad {bad}) quotient={80-rk-T}", flush=True)
    # ---- P cap SP : u of rank 3
    v3 = [[sp.Symbol(f'v{k}{j}') for j in range(3)] for k in range(R)]
    w3 = [[sp.Symbol(f'w{j}{c}') for c in range(n)] for j in range(3)]
    u3 = [[sum(v3[k][j]*w3[j][c] for j in range(3)) for c in range(n)] for k in range(R)]
    params2 = [v for row in phi for v in row] + [v for row in v3 for v in row] + [v for row in w3 for v in row]
    pen_expr2 = sym_prim(phi, u3)
    vals2 = [rng.randint(1, p-1) for _ in params2]
    pen2 = eval_pen(pen_expr2, params2, vals2, p)
    dP2 = dPhi_indep(pen2, p); rk2 = dP2.rank()
    d2 = dict(zip(params2, vals2))
    flat2 = [pen_expr2[k][a][b] for k in range(R) for a in range(n) for b in range(n)]
    Jn2 = [[int(sp.diff(f, v).subs(d2)) % p for v in params2] for f in flat2]
    T2 = nmod_mat(80, len(params2), [x for row in Jn2 for x in row], p).rank()
    out['P_SP'] = dict(rank_dPhi=rk2, dim_ker=80-rk2, dim_T_P=T2)
    print(f"[indep p={p}] P cap SP : rank dPhi={rk2} ker={80-rk2} T_P (Jacobian)={T2}", flush=True)
    # ---- P cap coker : phi = psi rho
    psi = [[sp.Symbol(f'p{a}{i}') for i in range(3)] for a in range(n)]
    rho = [[sp.Symbol(f'r{i}{s}') for s in range(6)] for i in range(3)]
    phi3 = [[sum(psi[a][i]*rho[i][s] for i in range(3)) for s in range(6)] for a in range(n)]
    params3 = [v for row in psi for v in row] + [v for row in rho for v in row] + [v for row in u for v in row]
    pen_expr3 = sym_prim(phi3, u)
    vals3 = [rng.randint(1, p-1) for _ in params3]
    pen3 = eval_pen(pen_expr3, params3, vals3, p)
    dP3 = dPhi_indep(pen3, p); rk3 = dP3.rank()
    out['P_coker'] = dict(rank_dPhi=rk3, dim_ker=80-rk3)
    print(f"[indep p={p}] P cap coker : rank dPhi={rk3} ker={80-rk3}", flush=True)
    # ---- generic SP
    phs = [[sp.Symbol(f'g{a}{j}') for j in range(3)] for a in range(n)]
    xs = [[sp.Symbol(f'x{k}{j}') for j in range(3)] for k in range(R)]
    cs = [[sp.Symbol(f'c{k}{a}') for a in range(n)] for k in range(R)]
    Ps = [[sp.Symbol(f'P{a}{b}') for b in range(n)] for a in range(n)]
    Qs = [[sp.Symbol(f'Q{a}{b}') for b in range(n)] for a in range(n)]
    params4 = [v for row in phs for v in row] + [v for row in xs for v in row] + [v for row in cs for v in row] + \
              [v for row in Ps for v in row] + [v for row in Qs for v in row]
    pen_expr4 = sym_sp(phs, xs, cs, Ps, Qs)
    vals4 = [rng.randint(1, p-1) for _ in params4]
    pen4 = eval_pen(pen_expr4, params4, vals4, p)
    dP4 = dPhi_indep(pen4, p); rk4 = dP4.rank()
    d4 = dict(zip(params4, vals4))
    flat4 = [pen_expr4[k][a][b] for k in range(R) for a in range(n) for b in range(n)]
    Jn4 = [[int(sp.diff(f, v).subs(d4)) % p for v in params4] for f in flat4]
    T4 = nmod_mat(80, len(params4), [x for row in Jn4 for x in row], p).rank()
    out['SP_generic'] = dict(rank_dPhi=rk4, dim_ker=80-rk4, dim_T=T4, quotient=80-rk4-T4)
    print(f"[indep p={p}] generic SP : rank dPhi={rk4} ker={80-rk4} T_SP={T4} quotient={80-rk4-T4}", flush=True)
    return out

if __name__ == '__main__':
    out = run()
    json.dump(out, open('results/s66_indep.json', 'w'), indent=1)

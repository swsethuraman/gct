"""Check 1: normal spaces at the quadratic-square skew pencils K6 (six variables) and K5 (five
variables), and the invariant counts j_m(r) = dim Sym^m(N_r)^{Stab^0}, m = 2, 4, 6, 8.

Part A (linear algebra, exact): tangent space of the SL_r x H^0 orbit at K, radial direction,
symmetric/skew split, dimension of the normal space N = T/(T_orb + radial).
Part B (characters, exact): weights of S_(3,1)C^4 (SL_4) and of the Sp_4-module Sym^2 (x) Lambda^2_0
minus (10 + 5); Sym^m characters by a truncated product DP; trivial multiplicity by the Weyl
alternant; controls on known cases.
No source contraction is evaluated. Output: c1_normal_space_counts.json in the same directory.
"""
import itertools as it, json, math, time
from collections import defaultdict
from pathlib import Path
import sympy as sp
from sympy.combinatorics import Permutation

HERE = Path(__file__).resolve().parent
t0 = time.perf_counter()
out = {}

# ---------------------------------------------------------------- Part A: tangent spaces
def E(i, j):
    m = sp.zeros(4, 4); m[i, j] = 1; return m

def skew(i, j):
    return E(i, j) - E(j, i)

K6 = [skew(0, 1), skew(0, 2), skew(0, 3), skew(1, 2), skew(1, 3), skew(2, 3)]          # K(x): x1..x6
K5 = [skew(0, 1) + skew(2, 3), skew(0, 2), skew(0, 3), skew(1, 2), skew(1, 3)]         # K5(x): (3,4) entry = x1

def flat(tuple_):
    return [entry for Y in tuple_ for entry in Y]

def tangent_data(K):
    r = len(K)
    gens = {'sl_r': [], 'gl4_left': [], 'gl4_right': []}
    for i in range(r):
        for j in range(r):
            if i == j: continue
            T = [sp.zeros(4, 4) for _ in range(r)]; T[i] = K[j]; gens['sl_r'].append(flat(T))
    for i in range(1, r):
        T = [sp.zeros(4, 4) for _ in range(r)]; T[0] = K[0]; T[i] = -K[i]; gens['sl_r'].append(flat(T))
    for a in range(4):
        for b in range(4):
            gens['gl4_left'].append(flat([E(a, b) * Y for Y in K]))
            gens['gl4_right'].append(flat([Y * E(a, b) for Y in K]))
    radial = flat(K)
    def rank(rows):
        return sp.Matrix(rows).rank() if rows else 0
    sl = gens['sl_r']; L = gens['gl4_left']; R = gens['gl4_right']
    # h^0 = {(A,B): tr A + tr B = 0}: basis = off-diagonal pairs, (E_aa - E_00, 0), (0, E_aa - E_00), (E_00, -E_00)
    h0 = []
    for a in range(4):
        for b in range(4):
            if a != b:
                h0.append(L[4 * a + b]); h0.append(R[4 * a + b])
    for a in range(1, 4):
        h0.append([x - y for x, y in zip(L[4 * a + a], L[0])])
        h0.append([x - y for x, y in zip(R[4 * a + a], R[0])])
    h0.append([x - y for x, y in zip(L[0], R[0])])
    T_orb = rank(sl + h0)
    T_orb_rad = rank(sl + h0 + [radial])
    T_all = rank(sl + L + R)          # gl_r would add nothing beyond sl_r + radial
    # symmetric / skew coordinates: projection matrices
    def sym_part(vec):
        outv = []
        for k in range(r):
            Y = sp.Matrix(4, 4, vec[16 * k:16 * k + 16]); S = (Y + Y.T) / 2
            outv += list(S)
        return outv
    def skew_part(vec):
        outv = []
        for k in range(r):
            Y = sp.Matrix(4, 4, vec[16 * k:16 * k + 16]); S = (Y - Y.T) / 2
            outv += list(S)
        return outv
    sym_proj = rank([sym_part(v) for v in sl + h0])
    skew_proj = rank([skew_part(v) for v in sl + h0 + [radial]])
    # all skew directions lie in T_orb + radial?  (then N is a quotient of the symmetric directions)
    skew_basis = []
    for k in range(r):
        for (i, j) in it.combinations(range(4), 2):
            T = [sp.zeros(4, 4) for _ in range(r)]; T[k] = skew(i, j); skew_basis.append(flat(T))
    T_orb_rad_skew = rank(sl + h0 + [radial] + skew_basis)
    return dict(r=r, dim_T=16 * r, dim_T_orb=T_orb, dim_T_orb_plus_radial=T_orb_rad,
                radial_in_T_orb=(T_orb == T_orb_rad), dim_span_all_gl=T_all,
                dim_sym_projection_of_T_orb=sym_proj, dim_skew_projection_of_T_orb_plus_radial=skew_proj,
                dim_skew_directions=6 * r, dim_sym_directions=10 * r,
                skew_directions_inside_T_orb_plus_radial=(T_orb_rad_skew == T_orb_rad),
                dim_normal_space=16 * r - T_orb_rad,
                dim_normal_from_symmetric=10 * r - sym_proj)

out['A_tangent_K6'] = tangent_data(K6)
out['A_tangent_K5'] = tangent_data(K5)
# stabiliser dimension of K5 inside {(A,B)}: D with K_i D = D^T K_i for all i (D = B A^{-T}); expect only scalars
D = sp.Matrix(4, 4, sp.symbols('d0:16'))
eqs = []
for Y in K5:
    M = Y * D - D.T * Y
    eqs += list(M)

out['A_K5_commutant_dimension'] = len(list(D)) - sp.Matrix([[sp.diff(e, s) for s in D] for e in eqs]).rank()
out['A_K5_commutant_is_scalars'] = out['A_K5_commutant_dimension'] == 1
out['A_elapsed_s'] = time.perf_counter() - t0

# ---------------------------------------------------------------- Part B: characters
def ssyt_weights(shape, n):
    """weights (content vectors) of all SSYT of the given shape with entries 1..n"""
    cells = [(i, j) for i, row in enumerate(shape) for j in range(row)]
    weights = []
    def rec(idx, filled):
        if idx == len(cells):
            w = [0] * n
            for v in filled.values(): w[v] += 1
            weights.append(tuple(w)); return
        i, j = cells[idx]
        lo = 0
        if j > 0: lo = max(lo, filled[(i, j - 1)])
        if i > 0: lo = max(lo, filled[(i - 1, j)] + 1)
        for v in range(lo, n):
            filled[(i, j)] = v; rec(idx + 1, filled); del filled[(i, j)]
    rec(0, {})
    return weights

def char_from_list(ws):
    c = defaultdict(int)
    for w in ws: c[tuple(w)] += 1
    return dict(c)

def add(cA, cB, sign=1):
    c = defaultdict(int, cA)
    for w, m in cB.items(): c[w] += sign * m
    return {w: m for w, m in c.items() if m}

def tensor(cA, cB):
    c = defaultdict(int)
    for w1, m1 in cA.items():
        for w2, m2 in cB.items():
            c[tuple(a + b for a, b in zip(w1, w2))] += m1 * m2
    return dict(c)

def sym_power_chars(c, mmax):
    """characters of Sym^m for m = 0..mmax via truncated product of 1/(1 - x^w)^mult"""
    dim = len(next(iter(c)))
    state = {(0, (0,) * dim): 1}
    for w, mu in c.items():
        new = defaultdict(int)
        for (deg, wt), val in state.items():
            for j in range(0, mmax - deg + 1):
                coeff = math.comb(mu + j - 1, j)
                new[(deg + j, tuple(a + j * b for a, b in zip(wt, w)))] += val * coeff
        state = dict(new)
    res = {m: {} for m in range(mmax + 1)}
    for (deg, wt), val in state.items():
        if val: res[deg][wt] = val
    return res

def dominant_mult_A(c, mu, n):
    """multiplicity of the irreducible GL_n-module of highest weight mu in a character c (Weyl alternant)"""
    rho = tuple(range(n - 1, -1, -1))
    total = 0
    for perm in it.permutations(range(n)):
        sign = Permutation(list(perm)).signature()
        wrho = tuple(rho[perm[i]] for i in range(n))
        target = tuple(mu[i] + rho[i] - wrho[i] for i in range(n))
        total += sign * c.get(target, 0)
    return total

def dominant_mult_C2(c, mu):
    """multiplicity of the irreducible Sp_4-module of highest weight mu (epsilon coordinates) in c"""
    rho = (2, 1)
    total = 0
    for perm in it.permutations(range(2)):
        for signs in it.product((1, -1), repeat=2):
            sign = Permutation(list(perm)).signature() * signs[0] * signs[1]
            wrho = tuple(signs[i] * rho[perm[i]] for i in range(2))
            target = tuple(mu[i] + rho[i] - wrho[i] for i in range(2))
            total += sign * c.get(target, 0)
    return total

B = {}
# --- SL_4 side: N_6 = S_(3,1) C^4
c31 = char_from_list(ssyt_weights((3, 1), 4))
B['dim_S31'] = sum(c31.values())
c2 = char_from_list(ssyt_weights((2,), 4)); c11 = char_from_list(ssyt_weights((1, 1), 4))
csym = tensor(c2, c11)
B['dim_Sym2_tensor_Lambda2'] = sum(csym.values())
B['Sym2xLambda2_mult_S31'] = dominant_mult_A(csym, (3, 1, 0, 0), 4)
B['Sym2xLambda2_mult_S211'] = dominant_mult_A(csym, (2, 1, 1, 0), 4)
B['S31_is_irreducible_control'] = dominant_mult_A(c31, (3, 1, 0, 0), 4) == 1 and sum(c31.values()) == 45
# dual of S31 as SL_4-module is S_(3,3,2,0) (control that it differs from S31: non-self-dual)
c332 = char_from_list(ssyt_weights((3, 3, 2), 4))
B['S31_dual_is_S332_control'] = dominant_mult_A({tuple(3 - x for x in w): m for w, m in c31.items()}, (3, 3, 2, 0), 4) == 1
symp6 = sym_power_chars(c31, 6)
B["j_m_6"] = {m: dominant_mult_A(symp6[m], (m,) * 4, 4) for m in (2, 4, 6)}
B["dims_Sym_m_N6"] = {m: sum(symp6[m].values()) for m in (2, 4, 6)}
# controls for the alternant: adjoint sl_4 = S_(2,1,1) (x) det^-1 ; use S211 itself (weights shifted by det do not matter)
c211 = char_from_list(ssyt_weights((2, 1, 1), 4))
B['control_Sym2_adjoint_invariants'] = dominant_mult_A(sym_power_chars(c211, 2)[2], (2, 2, 2, 2), 4)   # expect 1 (Killing form)
B['control_Sym2_C4_invariants'] = dominant_mult_A(sym_power_chars(char_from_list(ssyt_weights((1,), 4)), 2)[2], (0, 0, 0, 0), 4)  # expect 0
B['control_Lambda2_via_S11_det'] = dominant_mult_A(c11, (1, 1, 0, 0), 4)  # expect 1

# --- Sp_4 side: C^4 has weights +-e1, +-e2
V4 = {(1, 0): 1, (-1, 0): 1, (0, 1): 1, (0, -1): 1}
S2 = sym_power_chars(V4, 2)[2]                     # adjoint, dim 10
L2 = defaultdict(int)
for (w1, w2) in it.combinations(list(V4.keys()), 2):
    L2[tuple(a + b for a, b in zip(w1, w2))] += 1  # Lambda^2, dim 6
L2 = dict(L2)
L20 = add(L2, {(0, 0): 1}, -1)                     # Lambda^2_0, dim 5
B['dim_Sp4_adjoint'] = sum(S2.values()); B['dim_Lambda2_0'] = sum(L20.values())
Vsym5 = tensor(S2, L20)                            # symmetric directions at K5 as Sp_4-module, dim 50
B['dim_Vsym5'] = sum(Vsym5.values())
B['Vsym5_mult_(3,1)'] = dominant_mult_C2(Vsym5, (3, 1))
B['Vsym5_mult_(2,0)'] = dominant_mult_C2(Vsym5, (2, 0))
B['Vsym5_mult_(1,1)'] = dominant_mult_C2(Vsym5, (1, 1))
N5 = add(add(Vsym5, S2, -1), L20, -1)
B['dim_N5'] = sum(N5.values())
B['N5_irreducible_control'] = dominant_mult_C2(N5, (3, 1)) == 1 and all(m > 0 for m in N5.values())
symp5 = sym_power_chars(N5, 8)
B['j_m_5'] = {m: dominant_mult_C2(symp5[m], (0, 0)) for m in (2, 4, 6, 8)}
B['dims_Sym_m_N5'] = {m: sum(symp5[m].values()) for m in (2, 4, 6, 8)}
B['control_Sym2_C4_Sp4_invariants'] = dominant_mult_C2(sym_power_chars(V4, 2)[2], (0, 0))   # expect 0 (symplectic)
B['control_Sym2_L20_Sp4_invariants'] = dominant_mult_C2(sym_power_chars(L20, 2)[2], (0, 0)) # expect 1 (orthogonal 5)
B['control_Sym2_adjoint_Sp4_invariants'] = dominant_mult_C2(sym_power_chars(S2, 2)[2], (0, 0)) # expect 1
B['control_Lambda2_N5_invariants'] = dominant_mult_C2(add(tensor(N5, N5), symp5[2], -1), (0, 0))  # expect 0 (form is symmetric)
B['control_Lambda2_N6_invariants'] = dominant_mult_A(add(tensor(c31, c31), symp6[2], -1), (2, 2, 2, 2), 4)  # expect 0
# target-side controls: H_4 of C^6 = S_(4,4)C^4 (dim 105) and H_4 of C^5 (dim 55): Sym^2 invariants = 1
c44 = char_from_list(ssyt_weights((4, 4), 4))
B['dim_H4_C6_as_S44'] = sum(c44.values())
B['control_Sym2_H4_C6_invariants'] = dominant_mult_A(sym_power_chars(c44, 2)[2], (4, 4, 4, 4), 4)
# H_4(C^5) under Sp_4: Sym^4(L20) - Sym^2(L20) (harmonic decomposition), highest weight (4,0)? no: (2,2) in epsilon coords
H4_5 = add(sym_power_chars(L20, 4)[4], sym_power_chars(L20, 2)[2], -1)
B['dim_H4_C5'] = sum(H4_5.values())
B['control_Sym2_H4_C5_invariants'] = dominant_mult_C2(sym_power_chars(H4_5, 2)[2], (0, 0))
out['B_characters'] = B
out['elapsed_s'] = time.perf_counter() - t0
(HERE / 'c1_normal_space_counts.json').write_text(json.dumps(out, indent=1, default=str) + '\n')
print(json.dumps(out, indent=1, default=str))

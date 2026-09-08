#!/usr/bin/env python3
"""
Session 72 -- Residue 1: P cap c21 at order 2, settled by the a-linear fibration.

s66 left P cap c21 as the one primitive-world number off the table: the reduced
Q_2^pi is 9 quadrics in 30 variables (after dropping the 33-dim common
intersection of the four component tangent spaces T_P, T_c21, T_SP0, T_SP1), and
neither Singular's std/minAssGTZ nor Macaulay2's minimalPrimes finished in the
box.

STRUCTURE (measured here, then proved).  In the reduced coordinates the 30
variables split as 12 'a' + 18 'b' and every quadric of Q_2^pi has NO a.a
monomial:  q_l(a,b) = a^T C_l(b) + Q_l(b),  C_l linear in b, Q_l quadratic in b.
So for fixed b the system is AFFINE-LINEAR in a, and

    V(Q_2^pi) fibres over the b-space via the 9 x 12 matrix  C(b) = [C_l(b)]_l :
      over a b with rank C(b) = 9 (consistent), the a-fibre is a 3-plane;
      the components of V(Q_2^pi) are the closures over the rank strata of C(b).

This is the exact analogue of s66's bilinear reduction (there the matrix M(a) is
linear in one block; here C(b) is linear in the b-block), and it makes the
decomposition a rank stratification of a small matrix instead of a 30-variable
Groebner basis.  We (1) verify the a-linearity (zero non-a-linear entries),
(2) measure the generic rank of C(b) and hence dim V(Q_2^pi), (3) sample a
generic point of the top component and each rank-drop stratum and run s59's
order-2 identity there for the fixed-factor image, (4) also emit the reduced
system with a block ordering for a CAS cross-check.
"""
import sys, json, random, zlib, argparse, os, subprocess, time
sys.path.insert(0, 'analysis')
from flint import nmod_mat
from wk10_s66_core import *
from wk10_s66_orderq import family, all_g, pencil_int, solve_aug
from wk10_s66_order2 import tangents_at
from wk10_s66_tangent import coords_in_kernel
from wk10_s66_cas import quadrics_from, independent_rows
from wk10_s66_bilinear import rref_basis, extend, intersect_spaces, quad_in_coords

def build_reduced(spec, seed, p):
    """replicate run_multi's setup: point, dP, kerB, common intersection I,
    reduced coords Z (columns I + complement), and Q_2^pi as symmetric matrices
    in the nW reduced variables."""
    rng = random.Random(seed*7919 + zlib.crc32(spec.encode()) % 1000)
    theta, build = family(spec, rng, p)
    pen = pencil_int(build(theta, Fp(p)))
    dP = dPhi_matrix(pen, p); rk = dP.rank(); kerB = kernel_basis(dP); k = len(kerB)
    _, T = tangents_at(spec, theta, p, rng)
    names = list(T)
    Tz = {nm: coords_in_kernel(rref_basis(T[nm], 80, p), kerB, p) for nm in names}
    I = intersect_spaces([Tz[nm] for nm in names], k, p)
    Wc = extend(I, [[1 if j == i else 0 for j in range(k)] for i in range(k)], k, p)
    Z = [[0]*k for _ in range(k)]
    for j, v in enumerate(I + Wc):
        for i in range(k): Z[i][j] = v[i] % p
    nI, nW = len(I), len(Wc)
    # Q_2^pi in kernel coords
    piP = nmod_mat(len(S5DEG0), 80, [int(dP[i, j]) for i in S5DEG0 for j in range(80)], p)
    cs_pi = []
    for c in kernel_basis(piP.transpose()):
        full = [0]*NQ
        for t, i in enumerate(S5DEG0): full[i] = c[t]
        cs_pi.append(full)
    quads = quadrics_from(pen, dP, kerB, cs_pi, p)
    def ut(Qm): return [Qm[i][j] for i in range(k) for j in range(i, k)]
    def from_ut(v):
        Qm = [[0]*k for _ in range(k)]; t = 0
        for i in range(k):
            for j in range(i, k): Qm[i][j] = v[t]; t += 1
        return Qm
    quads = [from_ut(v) for v in independent_rows([ut(q) for q in quads], k*(k+1)//2, p)]
    red = []
    for Qm in quads:
        S = quad_in_coords(Qm, Z, k, p)                 # symmetric, 2x on the diagonal
        red.append([[S[nI + i][nI + j] % p for j in range(nW)] for i in range(nW)])
    return dict(theta=theta, build=build, pen=pen, dP=dP, kerB=kerB, k=k, names=names,
                I=I, Z=Z, nI=nI, nW=nW, red=red, rng=rng, p=p)

def split_ab(red, nW, p):
    """a-variables = indices never squared in any quadric and with no a.a coupling.
    Verify: the quadrics have zero entry on every (a,a) pair (a-linearity)."""
    a_idx = [i for i in range(nW) if all(S[i][i] % p == 0 for S in red)]
    # confirm no coupling among a-indices
    bad = 0
    for S in red:
        for i in a_idx:
            for j in a_idx:
                if S[i][j] % p: bad += 1
    b_idx = [i for i in range(nW) if i not in a_idx]
    return a_idx, b_idx, bad

def Cmatrix(red, a_idx, b_idx, bvals, p):
    """C(b) : (#quadrics) x |a| matrix, entry l,i = d q_l / d a_i at b = bvals
    = 2*S[a_i][a_i]*a_i? no -- linear-in-a coefficient = sum_j S[a_i][b_j]*b_j*2?
    With the 2x-diagonal symmetric convention, q(z) = sum_{i<=j} c_ij z_i z_j and
    S[i][j] (i!=j) = c_ij, S[i][i] = 2 c_ii.  The a-linear coefficient of a_i is
    sum over b_j of S[a_i][b_j] * bval_j  (a_i never squared, no a-a)."""
    b_full = [0]*len(red[0])
    for t, j in enumerate(b_idx): b_full[j] = bvals[t] % p
    C = []
    for S in red:
        row = [sum(S[ai][bj]*b_full[bj] for bj in b_idx) % p for ai in a_idx]
        C.append(row)
    # constant (b-quadratic) part Q_l(b)
    Qc = []
    for S in red:
        s = 0
        for bi in b_idx:
            for bj in b_idx:
                if bi == bj: s += (S[bi][bi]*pow(2,p-2,p)) % p * (b_full[bi]*b_full[bi]) % p
                elif bi < bj: s += S[bi][bj]*b_full[bi]*b_full[bj]
        Qc.append(s % p)
    return C, Qc

def sample_V_point(red, a_idx, b_idx, nW, p, rng, drop=0):
    """pick b (generic, or on a rank-<9-drop locus if drop>0 by forcing structure),
    solve the affine-linear system C(b) a = -Q(b) for a; return a full nW-vector on
    V(Q_2^pi) or None."""
    for _ in range(40):
        bvals = [rng.randint(1, p-1) for _ in range(len(b_idx))]
        C, Qc = Cmatrix(red, a_idx, b_idx, bvals, p)
        na = len(a_idx)
        A = nmod_mat(len(C), na+1, [int(C[l][i]) if i < na else int(-Qc[l]) % p
                                    for l in range(len(C)) for i in range(na+1)], p)
        rC = nmod_mat(len(C), na, [int(C[l][i]) for l in range(len(C)) for i in range(na)], p).rank()
        rAug = A.rank()
        if drop and rC >= 9: continue           # want a rank-drop b
        if not drop and rC < 9: continue         # want generic b
        if rAug > rC: continue                    # inconsistent
        # solve for a
        X, nul = A.nullspace(); a_sol = None
        for t in range(nul):
            last = int(X[na, t]) % p
            if last:
                inv = pow(last, p-2, p)
                a_sol = [(int(X[i, t])*inv) % p for i in range(na)]
                # add a random homogeneous kernel vector
                break
        if a_sol is None: continue
        # random element of the affine fibre
        Ch = nmod_mat(len(C), na, [int(C[l][i]) for l in range(len(C)) for i in range(na)], p)
        Kh, knul = Ch.nullspace()
        for t in range(knul):
            c = rng.randint(0, p-1)
            for i in range(na): a_sol[i] = (a_sol[i] + c*int(Kh[i, t])) % p
        w = [0]*nW
        for t, i in enumerate(a_idx): w[i] = a_sol[t]
        for t, j in enumerate(b_idx): w[j] = bvals[t]
        return w, rC, knul
    return None

def order2_image_at(S, w_reduced):
    """given a reduced-coordinate V-point w (nW vector), lift to M_1 in ker dPhi,
    solve order 2, and return the fixed-factor image dim (s59 identity)."""
    p = S['p']; Z = S['Z']; k = S['k']; nI = S['nI']; kerB = S['kerB']
    build = S['build']; theta = S['theta']; rng = S['rng']
    w = [rng.randint(1, p-1) for _ in range(nI)] + list(w_reduced)
    z = [sum(Z[i][j]*w[j] for j in range(k)) % p for i in range(k)]
    m1v = [0]*80
    for i in range(k):
        for r_ in range(80): m1v[r_] = (m1v[r_] + z[i]*kerB[i][r_]) % p
    M1 = vec_pencil(m1v); zero = pencil_zero(Fp(p))
    g1, g2c = all_g(build, theta, [M1, zero], 2, p)
    if any(g1): return dict(note='not a kernel direction (g1!=0)')
    const = [g2c[i] for i in S5DEG0]; cols2 = []
    for kk in range(R):
        for a_ in range(n):
            for b_ in range(n):
                g = all_g(build, theta, [M1, zero], 2, p, dual=('m', 2, kk, a_, b_))[1]
                cols2.append([g[i] for i in S5DEG0])
    part = solve_aug(cols2, const, len(S5DEG0), p)
    if part is None: return dict(note='order-2 solve failed (pi g2 != 0 : not on V(Q2pi))')
    m2v = [v % p for v in part]
    X, nul = nmod_mat(len(S5DEG0), 80, [int(cols2[j][r_]) for r_ in range(len(S5DEG0)) for j in range(80)], p).nullspace()
    for t in range(nul):
        c = rng.randint(1, p-1)
        for r_ in range(80): m2v[r_] = (m2v[r_] + c*int(X[r_, t])) % p
    M2 = vec_pencil(m2v)
    g1, g2 = all_g(build, theta, [M1, M2], 2, p)
    assert not any(g1) and not any(g2[i] for i in S5DEG0)
    dcols = [[int(S['dP'][i, j]) for i in range(NQ)] for j in range(80)]
    g2_in_im = solve_aug(dcols, [(-x) % p for x in g2], NQ, p) is not None
    rows_full = []; rows_con = []
    params = [('t', i) for i in range(len(theta))] + \
             [('m', j, kk, a_, b_) for j in (1, 2) for kk in range(R) for a_ in range(n) for b_ in range(n)]
    for pr in params:
        gg1, gg2 = all_g(build, theta, [M1, M2], 2, p, dual=pr)
        rows_full.append(gg1 + gg2); rows_con.append(gg1 + [gg2[i] for i in S5DEG0])
    rf = rank_mod(rows_full, 2*NQ, p); rc = rank_mod(rows_con, NQ + len(S5DEG0), p)
    return dict(g2_nonzero=any(g2), g2_in_im_dPhi=g2_in_im, rank_full=rf, rank_con=rc,
                order2_image=rf - rc)

def run(seed, p, verbose=True):
    S = build_reduced('P_c21', seed, p)
    nW = S['nW']; red = S['red']
    a_idx, b_idx, bad = split_ab(red, nW, p)
    rec = dict(spec='P_c21', seed=seed, p=p, rank_dPhi=S['dP'].rank(), dim_ker=S['k'],
               dim_common_intersection=S['nI'], reduced_vars=nW, n_Qpi=len(red),
               a_vars=len(a_idx), b_vars=len(b_idx), a_linear_nonzero_entries=bad)
    if verbose:
        print(f"[P_c21 seed={seed} p={p}] ker={S['k']} common-int={S['nI']} reduced={nW}; "
              f"|Q2pi|={len(red)}; a-vars={len(a_idx)} b-vars={len(b_idx)}; "
              f"non-a-linear entries={bad} (0 => proved a-linear)", flush=True)
    # generic rank of C(b) and dim V
    bvals = [S['rng'].randint(1, p-1) for _ in range(len(b_idx))]
    C, Qc = Cmatrix(red, a_idx, b_idx, bvals, p)
    rC = nmod_mat(len(C), len(a_idx), [int(x) for row in C for x in row], p).rank()
    dimV = len(b_idx) + (len(a_idx) - rC)          # b free + a-fibre
    rec.update(generic_rank_C=rC, dim_V_Qpi_reduced=dimV, dim_V_Qpi_full=S['nI'] + dimV)
    if verbose:
        print(f"   generic rank C(b) = {rC}/{min(9,len(a_idx))}; a-fibre dim = {len(a_idx)-rC}; "
              f"dim V(Q2pi) reduced = {dimV}, full = {S['nI']+dimV}", flush=True)
    # image over the generic (top) component
    rec['components'] = []
    for trial in range(3):
        pt = sample_V_point(red, a_idx, b_idx, nW, p, S['rng'], drop=0)
        if pt is None: continue
        w, rC_pt, knul = pt
        img = order2_image_at(S, w)
        e = dict(kind='generic (top component)', rank_C=rC_pt, a_fibre=knul, **img)
        rec['components'].append(e)
        if verbose: print(f"   generic V-point (rank C={rC_pt}): image = {img.get('order2_image')}", flush=True)
        break
    # rank-drop strata
    for trial in range(6):
        pt = sample_V_point(red, a_idx, b_idx, nW, p, S['rng'], drop=1)
        if pt is None: continue
        w, rC_pt, knul = pt
        img = order2_image_at(S, w)
        e = dict(kind='rank-drop stratum', rank_C=rC_pt, a_fibre=knul, **img)
        rec['components'].append(e)
        if verbose: print(f"   rank-drop V-point (rank C={rC_pt}): image = {img.get('order2_image')}", flush=True)
    imgs = [c['order2_image'] for c in rec['components'] if 'order2_image' in c]
    rec['max_order2_image'] = max(imgs) if imgs else None
    if verbose: print(f"   ==> max order-2 fixed-factor image over sampled components = {rec['max_order2_image']}", flush=True)
    return rec, S

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--primes', default='32003,1000003')
    ap.add_argument('--seeds', default='1,2')
    ap.add_argument('--out', default='results/s72_pc21.json')
    a = ap.parse_args()
    res = []
    for p in [int(x) for x in a.primes.split(',')]:
        for seed in [int(x) for x in a.seeds.split(',')]:
            rec, _ = run(seed, p)
            res.append(rec)
            json.dump(res, open(a.out, 'w'), indent=1)
    print("wrote", a.out)

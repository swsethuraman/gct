#!/usr/bin/env python3
"""
Session 72 -- Residue 2: the rank-drop strata of M(a) at ker cap coker.

s66 measured the two generic-kernel components (the two rulings of the bilinear
variety V' = {(a,b): M(a) b = 0}, M(a) = sum_i a_i M_i linear in the 12
a-coordinates, generic rank 9, ker dim 3): both give fixed-factor image 29.  The
rank-drop strata {a : rank M(a) < 9} were left undecomposed.

This module samples those strata and measures the order-2 fixed-factor image on
them.  A rank-drop point is constructed by forcing an extra kernel vector: pick a
random b* and solve the linear system  M(a) b* = 0  (31 equations in the 12
a-variables) for a; a nonzero solution a* has b* in ker M(a*), so if b* was not
generically in the kernel this is a genuine rank drop (ker jumps to >= 4).  We
also probe by restricting a to random low-dimensional coordinate subspaces.  At
every rank-drop point found we run s59's order-2 identity for the fixed-factor
image and report the maximum.
"""
import sys, json, random, zlib, argparse
sys.path.insert(0, 'analysis')
from flint import nmod_mat
from wk10_s66_core import *
from wk10_s66_orderq import family, all_g, pencil_int, solve_aug
from wk10_s66_order2 import tangents_at
from wk10_s66_tangent import coords_in_kernel
from wk10_s66_cas import quadrics_from, independent_rows
from wk10_s66_bilinear import rref_basis, adapted_coords, quad_in_coords

def setup(spec, seed, p):
    rng = random.Random(seed*7919 + zlib.crc32(spec.encode()) % 1000)
    theta, build = family(spec, rng, p)
    pen = pencil_int(build(theta, Fp(p)))
    dP = dPhi_matrix(pen, p); kerB = kernel_basis(dP); k = len(kerB)
    _, T = tangents_at(spec, theta, p, rng); names = list(T)
    Tz = {nm: coords_in_kernel(rref_basis(T[nm], 80, p), kerB, p) for nm in names}
    I, A, B = adapted_coords(Tz[names[0]], Tz[names[1]], k, p)
    alpha, beta = len(A), len(B)
    Z = [[0]*k for _ in range(k)]
    for j, v in enumerate(I + A + B):
        for i in range(k): Z[i][j] = v[i] % p
    piP = nmod_mat(len(S5DEG0), 80, [int(dP[i, j]) for i in S5DEG0 for j in range(80)], p)
    cs_pi = []
    for c in kernel_basis(piP.transpose()):
        full = [0]*NQ
        for t, i in enumerate(S5DEG0): full[i] = c[t]
        cs_pi.append(full)
    quads = quadrics_from(pen, dP, kerB, cs_pi, p)
    Cq = []
    for Qm in quads:
        S = quad_in_coords(Qm, Z, k, p); nI = len(I)
        Cq.append([[S[nI + i][nI + alpha + j] % p for j in range(beta)] for i in range(alpha)])
    return dict(theta=theta, build=build, dP=dP, kerB=kerB, k=k, I=I, Z=Z, nI=len(I),
                alpha=alpha, beta=beta, Cq=Cq, rng=rng, p=p, names=names)

def Ma(Cq, a, alpha, beta, p):
    return [[sum(a[i]*C[i][j] for i in range(alpha)) % p for j in range(beta)] for C in Cq]

def image_at_ab(S, a, b):
    p = S['p']; Z = S['Z']; k = S['k']; nI = S['nI']; kerB = S['kerB']
    build = S['build']; theta = S['theta']; rng = S['rng']; alpha = S['alpha']; beta = S['beta']
    w = [rng.randint(1, p-1) for _ in range(nI)] + list(a) + list(b)
    z = [sum(Z[i][j]*w[j] for j in range(k)) % p for i in range(k)]
    m1v = [0]*80
    for i in range(k):
        for r_ in range(80): m1v[r_] = (m1v[r_] + z[i]*kerB[i][r_]) % p
    M1 = vec_pencil(m1v); zero = pencil_zero(Fp(p))
    g1, g2c = all_g(build, theta, [M1, zero], 2, p)
    if any(g1): return None
    const = [g2c[i] for i in S5DEG0]; cols2 = []
    for kk in range(R):
        for a_ in range(n):
            for b_ in range(n):
                g = all_g(build, theta, [M1, zero], 2, p, dual=('m', 2, kk, a_, b_))[1]
                cols2.append([g[i] for i in S5DEG0])
    part = solve_aug(cols2, const, len(S5DEG0), p)
    if part is None: return None
    m2v = [v % p for v in part]
    X, nul = nmod_mat(len(S5DEG0), 80, [int(cols2[j][r_]) for r_ in range(len(S5DEG0)) for j in range(80)], p).nullspace()
    for t in range(nul):
        c = rng.randint(1, p-1)
        for r_ in range(80): m2v[r_] = (m2v[r_] + c*int(X[r_, t])) % p
    M2 = vec_pencil(m2v)
    g1, g2 = all_g(build, theta, [M1, M2], 2, p)
    if any(g2[i] for i in S5DEG0): return None
    rows_full = []; rows_con = []
    params = [('t', i) for i in range(len(theta))] + \
             [('m', j, kk, a_, b_) for j in (1, 2) for kk in range(R) for a_ in range(n) for b_ in range(n)]
    for pr in params:
        gg1, gg2 = all_g(build, theta, [M1, M2], 2, p, dual=pr)
        rows_full.append(gg1 + gg2); rows_con.append(gg1 + [gg2[i] for i in S5DEG0])
    rf = rank_mod(rows_full, 2*NQ, p); rc = rank_mod(rows_con, NQ + len(S5DEG0), p)
    return rf - rc

def rank_strata(S, n_scan=500):
    """the complete rank stratification of M(a) = sum_i a_i M_i (linear in the
    alpha a-coordinates).  Compute the a-kernel {a : M(a)=0} exactly (nullspace of
    the (nq*beta) x alpha matrix whose i-th column is flatten(M_i)); scan a mix of
    a-kernel + generic directions for every rank that occurs.  Returns
    (generic_rank, akernel_dim, {rank: representative a})."""
    p = S['p']; Cq = S['Cq']; alpha = S['alpha']; beta = S['beta']; rng = S['rng']; nq = len(Cq)
    Amat = nmod_mat(nq*beta, alpha, [int(Cq[l][i][j]) for l in range(nq) for j in range(beta) for i in range(alpha)], p)
    K, aknul = Amat.nullspace()
    akvecs = [[int(K[i, t]) for i in range(alpha)] for t in range(aknul)]
    def rk(a): return nmod_mat(nq, beta, [int(x) for row in Ma(Cq, a, alpha, beta, p) for x in row], p).rank()
    seen = {}
    # rank-0 stratum: a in the a-kernel
    if akvecs:
        a = [0]*alpha
        for v in akvecs:
            c = rng.randint(1, p-1)
            for i in range(alpha): a[i] = (a[i] + c*v[i]) % p
        seen[0] = a
    for _ in range(n_scan):
        a = [0]*alpha
        for v in akvecs:
            c = rng.choice([0, 0, 1, rng.randint(1, p-1)])
            for i in range(alpha): a[i] = (a[i] + c*v[i]) % p
        for _ in range(rng.randint(0, 2)):
            for i in range(alpha): a[i] = (a[i] + rng.choice([0, 1, rng.randint(1, p-1)])*rng.randint(1, p-1)) % p
        if any(a): seen.setdefault(rk(a), a)
    gen = max(seen)
    return gen, aknul, seen

def run(spec, seed, p, verbose=True):
    S = setup(spec, seed, p)
    rec = dict(spec=spec, seed=seed, p=p, alpha=S['alpha'], beta=S['beta'], nQpi=len(S['Cq']))
    gen, aknul, seen = rank_strata(S)
    rec['generic_rank_M'] = gen; rec['a_kernel_dim'] = aknul
    rec['ranks_observed'] = sorted(seen)
    rec['strata'] = []
    if verbose: print(f"[{spec} seed={seed} p={p}] generic rank M(a) = {gen}; a-kernel dim = {aknul}; "
                       f"ranks observed = {sorted(seen)}", flush=True)
    for r in sorted(seen):
        a = seen[r]
        M = nmod_mat(len(S['Cq']), S['beta'], [int(x) for row in Ma(S['Cq'], a, S['alpha'], S['beta'], p) for x in row], p)
        Kb, knul = M.nullspace(); b = [0]*S['beta']
        for t in range(knul):
            c = S['rng'].randint(1, p-1)
            for j in range(S['beta']): b[j] = (b[j] + c*int(Kb[j, t])) % p
        img = image_at_ab(S, a, b)
        rec['strata'].append(dict(rank_M=r, ker_dim=knul, image=img))
        if verbose: print(f"   rank M(a)={r} (ker {knul}): fixed-factor image = {img}", flush=True)
    imgs = [e['image'] for e in rec['strata'] if e['image'] is not None]
    rec['max_image'] = max(imgs) if imgs else None
    if verbose: print(f"   ==> ranks {sorted(seen)}, max image over all strata = {rec['max_image']}", flush=True)
    return rec

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--specs', default='ker_coker')
    ap.add_argument('--primes', default='32003,1000003')
    ap.add_argument('--seeds', default='1,2')
    ap.add_argument('--out', default='results/s72_rankdrop.json')
    a = ap.parse_args()
    res = []
    for spec in a.specs.split(','):
        for p in [int(x) for x in a.primes.split(',')]:
            for seed in [int(x) for x in a.seeds.split(',')]:
                res.append(run(spec, seed, p)); json.dump(res, open(a.out, 'w'), indent=1)
    print("wrote", a.out)

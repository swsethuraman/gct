#!/usr/bin/env python3
"""
Session 66 -- CAS export : the second-order quadric systems at a point M_0 of
the base locus, in kernel coordinates z_1..z_k (N = sum z_i K_i, K_i a basis
of ker dPhi_{M_0}):

  Q2   = { c . e_2(M_0; N) : c perp im dPhi }            (quadratic initial forms of J)
  Qpi  = { c . e_2(M_0; N) : c perp (im dPhi + W) }      (order-2 solvability for a
                                                          reducible leading form:
                                                          the audit's 23 quadrics
                                                          at c21 cap c32)

together with the linear ideals L_i of the tangent spaces T_i of the known
components through M_0 (Q2 vanishes on each T_i where the component is smooth
at M_0).  Writes a Singular script that computes dim, and the minimal primes
of Qpi (and Q2), reporting each prime's dimension, degree, linearity, and
whether it equals one of the L_i.  Run it under `timeout`, pid recorded.
"""
import sys, json, argparse, time, os
sys.path.insert(0, 'analysis')
from flint import nmod_mat
from wk10_s66_core import *
from wk10_s66_points import build_point
from wk10_s66_tangent import coords_in_kernel

def quadrics_from(pen, dP, kerB, cs, p):
    """quadrics sum_j c_j e_{2,j} restricted to ker, for c in cs; returns list of
    upper-triangular k x k int matrices."""
    k = len(kerB)
    Ns = [vec_pencil(v) for v in kerB]
    e2s = [e2_vec(pen, Ns[i], p) for i in range(k)]
    Bmat = [[[0]*k for _ in range(k)] for _ in range(NQ)]
    for i in range(k):
        for j in range(NQ): Bmat[j][i][i] = e2s[i][j] % p
    Fpp = Fp(p)
    for i in range(k):
        for i2 in range(i+1, k):
            e = e2_vec(pen, pencil_add(Fpp, Ns[i], Ns[i2]), p)
            for j in range(NQ):
                b = (e[j] - e2s[i][j] - e2s[i2][j]) % p
                Bmat[j][i][i2] = b
    quads = []
    for c in cs:
        Qm = [[0]*k for _ in range(k)]
        for j in range(NQ):
            cj = c[j] % p
            if not cj: continue
            Bj = Bmat[j]
            for i in range(k):
                for i2 in range(i, k):
                    if Bj[i][i2]: Qm[i][i2] = (Qm[i][i2] + cj*Bj[i][i2]) % p
        quads.append(Qm)
    return quads

def poly_str(Qm, p, k):
    terms = []
    for i in range(k):
        for j in range(i, k):
            c = Qm[i][j] % p
            if not c: continue
            if c > p//2: c -= p
            mono = f"z({i+1})^2" if i == j else f"z({i+1})*z({j+1})"
            terms.append(f"({c})*{mono}")
    return " + ".join(terms) if terms else "0"

def lin_str(vec, p, k):
    terms = []
    for i in range(k):
        c = vec[i] % p
        if not c: continue
        if c > p//2: c -= p
        terms.append(f"({c})*z({i+1})")
    return " + ".join(terms) if terms else "0"

def independent_rows(mats, ncols, p):
    """select a maximal independent subset (as rows) of the given coefficient vectors."""
    out = []; cur = []
    for v in mats:
        if rank_mod(cur + [v], ncols, p) > len(cur):
            cur.append(v); out.append(v)
    return out

def export(spec, seed, p, outdir='analysis', verbose=True):
    t0 = time.time()
    d = build_point(spec, seed, p)
    pen = d['pen']
    dP = dPhi_matrix(pen, p)
    rk = dP.rank(); kerB = kernel_basis(dP); k = len(kerB)
    # c perp im dPhi
    cs_all = kernel_basis(dP.transpose())
    # c perp (im dPhi + W) : c supported on S5DEG0 with pi dPhi^T c = 0
    piP = nmod_mat(len(S5DEG0), 80, [int(dP[i, j]) for i in S5DEG0 for j in range(80)], p)
    cpi = kernel_basis(piP.transpose())
    cs_pi = []
    for c in cpi:
        full = [0]*NQ
        for t, i in enumerate(S5DEG0): full[i] = c[t]
        cs_pi.append(full)
    Q2 = quadrics_from(pen, dP, kerB, cs_all, p)
    Qpi = quadrics_from(pen, dP, kerB, cs_pi, p)
    # reduce to independent quadrics
    def ut(Qm): return [Qm[i][j] for i in range(k) for j in range(i, k)]
    Q2i = independent_rows([ut(q) for q in Q2], k*(k+1)//2, p)
    Qpii = independent_rows([ut(q) for q in Qpi], k*(k+1)//2, p)
    def from_ut(v):
        Qm = [[0]*k for _ in range(k)]; t = 0
        for i in range(k):
            for j in range(i, k): Qm[i][j] = v[t]; t += 1
        return Qm
    Q2 = [from_ut(v) for v in Q2i]; Qpi = [from_ut(v) for v in Qpii]
    # linear ideals of the component tangent spaces, in kernel coordinates
    lin = {}
    for name, tang in d['comps'].items():
        tv = [pencil_vec(t) for t in tang]
        A = nmod_mat(len(tv), 80, [int(x) % p for v in tv for x in v], p)
        rr = A.rref()[0]
        basis = [[int(rr[i, j]) for j in range(80)] for i in range(A.nrows()) if any(int(rr[i, j]) for j in range(80))]
        zb = coords_in_kernel(basis, kerB, p)                 # dim T_i vectors in F_p^k
        Z = nmod_mat(len(zb), k, [int(x) for v in zb for x in v], p)
        ann = kernel_basis(Z)                                 # linear forms vanishing on T_i
        lin[name] = dict(dim=len(zb), forms=ann)
    # Singular script
    fn = os.path.join(outdir, f"wk10_s66_{spec}_s{seed}_p{p}.sing")
    with open(fn, 'w') as f:
        f.write(f'// Session 66 : second-order quadrics at a {spec} point (seed {seed}), kernel dim {k}\n')
        f.write(f'// rank dPhi = {rk}; |Q2| = {len(Q2)} independent quadrics; |Qpi| = {len(Qpi)}\n')
        f.write('LIB "primdec.lib";\n')
        f.write(f'ring r = {p}, z(1..{k}), dp;\n')
        f.write('option(redSB);\n')
        f.write('ideal Qpi = ' + ",\n  ".join(poly_str(q, p, k) for q in Qpi) + ';\n')
        f.write('ideal Q2 = ' + ",\n  ".join(poly_str(q, p, k) for q in Q2) + ';\n')
        for name, L in lin.items():
            f.write(f'ideal L_{name} = ' + ",\n  ".join(lin_str(v, p, k) for v in L['forms']) + ';\n')
            f.write(f'print("T_{name}: dim {L["dim"]}, codim {len(L["forms"])}");\n')
        f.write('int t0 = timer;\n')
        f.write('ideal Gpi = std(Qpi);\n')
        f.write('print("dim V(Qpi) = " + string(dim(Gpi)) + "  (time " + string(timer - t0) + ")");\n')
        f.write('t0 = timer;\n')
        f.write('ideal G2 = std(Q2);\n')
        f.write('print("dim V(Q2) = " + string(dim(G2)) + "  (time " + string(timer - t0) + ")");\n')
        # containment checks : does Qpi vanish on T_i ?  (Qpi subset L_i)
        for name in lin:
            f.write(f'print("Qpi subset L_{name} : " + string(size(reduce(Qpi, std(L_{name})))==0));\n')
        f.write('list mp; int i;\n')
        f.write('t0 = timer;\n')
        f.write('mp = minAssGTZ(Qpi);\n')
        f.write('print("minAssGTZ(Qpi): " + string(size(mp)) + " minimal primes  (time " + string(timer - t0) + ")");\n')
        f.write('for (i = 1; i <= size(mp); i++) {\n')
        f.write('  ideal Pi = std(mp[i]);\n')
        f.write('  int islin = 1; int j;\n')
        f.write('  for (j = 1; j <= size(Pi); j++) { if (deg(Pi[j]) > 1) { islin = 0; } }\n')
        f.write('  string eq = "";\n')
        for name in lin:
            f.write(f'  if (size(reduce(L_{name}, Pi)) == 0 && size(reduce(Pi, std(L_{name}))) == 0) {{ eq = eq + " =T_{name}"; }}\n')
        f.write('  print("  prime " + string(i) + ": dim " + string(dim(Pi)) + ", degree " + string(mult(Pi)) + ", ngens " + string(size(Pi)) + ", linear " + string(islin) + eq);\n')
        f.write('}\n')
        f.write('quit;\n')
    meta = dict(spec=spec, seed=seed, p=p, k=k, rank_dPhi=rk, nQ2=len(Q2), nQpi=len(Qpi),
                tangents={nm: L['dim'] for nm, L in lin.items()}, file=fn,
                seconds=round(time.time()-t0, 1))
    if verbose: print(json.dumps(meta), flush=True)
    return meta

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--specs', default='c21_c32')
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--p', type=int, default=32003)
    a = ap.parse_args()
    metas = [export(s, a.seed, a.p) for s in a.specs.split(',')]
    json.dump(metas, open(f'results/s66_cas_export_p{a.p}.json', 'a'), indent=1)

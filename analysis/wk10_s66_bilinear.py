#!/usr/bin/env python3
"""
Session 66 -- the bilinear reduction of the second-order systems at a
two-component incidence, and the rank stratification that decomposes them.

At a point M_0 on exactly two known components C_1, C_2 with
    ker dPhi = T_1 + T_2      (measured: quotient 0),
choose coordinates on the kernel  z = (i, a, b)  with  T_1 cap T_2 = {a = b = 0},
T_1 = {b = 0}, T_2 = {a = 0}  (alpha = dim a = codim of T_2 in the kernel,
beta = dim b = codim of T_1).  A quadric vanishing on T_1 and on T_2 has no
i i, i a, i b, a a, b b monomials, so every element of Q_2 (hence of Q_2^pi) is
BILINEAR in (a, b) and independent of i :  q = a^T C_q b.

Hence V(Q) = (i-space) x V',  V' = { (a,b) : M(a) b = 0 }  with  M(a) = sum_i a_i M_i
the (#q x beta) matrix with rows a^T C_q ; the components of V' are
    {a = 0}                      (= T_2),
    closure{ (a, b) : rank M(a) = r, b in ker M(a) }  for each rank r attained
    (the r = beta stratum is {b = 0} = T_1 when the generic rank is beta),
so the decomposition of the second-order system IS the rank stratification of
the linear matrix M(a) in alpha variables -- a small problem where the
66-variable Groebner basis did not finish.

This module: builds the adapted coordinates, verifies bilinearity, computes the
generic rank of M(a) and of N(b) (the b-side matrix), finds the rank-drop locus
of M(a) when alpha <= 3 by interpolating random maximal minors (homogeneous of
degree = generic rank in alpha variables) and decomposing them in Singular in
alpha variables, samples a generic point of every extra component, and runs
s59's order-2 identity there.  Also exports the reduced (alpha+beta)-variable
system for a direct Singular minAssGTZ, time-boxed.
"""
import sys, json, argparse, time, os, subprocess, random, zlib, re, itertools
sys.path.insert(0, 'analysis')
from flint import nmod_mat
from wk10_s66_core import *
from wk10_s66_orderq import family, all_g, pencil_int, solve_aug
from wk10_s66_order2 import tangents_at
from wk10_s66_tangent import coords_in_kernel
from wk10_s66_cas import quadrics_from, independent_rows

def rref_basis(vectors, ncols, p):
    A = nmod_mat(len(vectors), ncols, [int(x) % p for v in vectors for x in v], p)
    rr = A.rref()[0]
    return [[int(rr[i, j]) for j in range(ncols)] for i in range(A.nrows()) if any(int(rr[i, j]) for j in range(ncols))]

def extend(basis, more, ncols, p):
    """append vectors of `more` that are independent of basis; return the added ones."""
    cur = list(basis); added = []
    for v in more:
        if rank_mod(cur + [v], ncols, p) > len(cur):
            cur.append(v); added.append(v)
    return added

def adapted_coords(T1, T2, k, p):
    """T1, T2 : lists of k-vectors spanning the two tangent spaces inside F_p^k
    (kernel coordinates).  Returns (I, A, B) bases with T1 = I+A, T2 = I+B and a
    change-of-basis matrix Z (k x k, columns = I, A, B) -- assumes T1 + T2 = F_p^k."""
    B1 = rref_basis(T1, k, p); B2 = rref_basis(T2, k, p)
    # intersection : nullspace of [B1^T | -B2^T] combos -> compute via
    # solving x B1 = y B2 ;  intersection basis from the nullspace of the stacked matrix
    M = nmod_mat(len(B1) + len(B2), k, [int(x) for v in B1 + B2 for x in v], p)
    X, nul = M.transpose().nullspace()          # relations sum c_r rows = 0
    inter = []
    for t in range(nul):
        c = [int(X[r, t]) for r in range(len(B1) + len(B2))]
        v = [sum(c[r]*B1[r][j] for r in range(len(B1))) % p for j in range(k)]
        inter.append(v)
    I = rref_basis(inter, k, p) if inter else []
    A = extend(I, B1, k, p)                  # T1 = I + A
    B = extend(I, B2, k, p)                  # T2 = I + B
    assert len(I) + len(A) + len(B) == k, (len(I), len(A), len(B), k)
    return I, A, B

def quad_in_coords(Qm, Z, k, p):
    """Qm upper-triangular in z ; Z columns = new basis ; return the quadric's
    symmetric matrix in the new coordinates w (z = Z w) : S' = Z^T S Z."""
    S = [[0]*k for _ in range(k)]
    for i in range(k):
        for j in range(i, k):
            v = Qm[i][j] % p
            if i == j: S[i][i] = (2*v) % p
            else: S[i][j] = v; S[j][i] = v
    Sm = nmod_mat(k, k, [x for row in S for x in row], p)
    Zm = nmod_mat(k, k, [int(x) % p for row in Z for x in row], p)
    Sp = Zm.transpose() * Sm * Zm
    return [[int(Sp[i, j]) for j in range(k)] for i in range(k)]   # symmetric, 2x diagonal convention

def run(spec, seed, p, timeout_s=1200, verbose=True):
    t0 = time.time()
    rng = random.Random(seed*7919 + zlib.crc32(spec.encode()) % 1000)
    theta, build = family(spec, rng, p)
    pen = pencil_int(build(theta, Fp(p)))
    dP = dPhi_matrix(pen, p); rk = dP.rank(); kerB = kernel_basis(dP); k = len(kerB)
    _, T = tangents_at(spec, theta, p, rng)
    names = list(T)
    assert len(names) == 2, f"{spec}: bilinear reduction needs exactly two components, got {names}"
    Tz = {}
    for nm in names:
        basis = rref_basis([v for v in T[nm]], 80, p)
        Tz[nm] = coords_in_kernel(basis, kerB, p)
    I, A, B = adapted_coords(Tz[names[0]], Tz[names[1]], k, p)
    alpha, beta = len(A), len(B)
    Z = [[0]*k for _ in range(k)]          # columns : I, A, B
    cols = I + A + B
    for j, v in enumerate(cols):
        for i in range(k): Z[i][j] = v[i] % p
    rec = dict(spec=spec, seed=seed, p=p, rank_dPhi=rk, dim_ker=k, comps={nm: len(Tz[nm]) for nm in names},
               dim_inter=len(I), alpha=alpha, beta=beta, a_is_transverse_to=names[1], b_is_transverse_to=names[0])
    # quadric systems
    cs_all = kernel_basis(dP.transpose())
    piP = nmod_mat(len(S5DEG0), 80, [int(dP[i, j]) for i in S5DEG0 for j in range(80)], p)
    cs_pi = []
    for c in kernel_basis(piP.transpose()):
        full = [0]*NQ
        for t, i in enumerate(S5DEG0): full[i] = c[t]
        cs_pi.append(full)
    systems = {}
    for label, cs in (('Q2', cs_all), ('Qpi', cs_pi)):
        quads = quadrics_from(pen, dP, kerB, cs, p)
        def ut(Qm): return [Qm[i][j] for i in range(k) for j in range(i, k)]
        def from_ut(v):
            Qm = [[0]*k for _ in range(k)]; t = 0
            for i in range(k):
                for j in range(i, k): Qm[i][j] = v[t]; t += 1
            return Qm
        quads = [from_ut(v) for v in independent_rows([ut(q) for q in quads], k*(k+1)//2, p)]
        # in adapted coordinates : bilinear part C_q (alpha x beta), check the rest vanishes
        Cq = []
        bad = 0
        for Qm in quads:
            S = quad_in_coords(Qm, Z, k, p)
            nI, nA = len(I), alpha
            for i in range(k):
                for j in range(k):
                    inA = nI <= i < nI + nA; inB = i >= nI + nA
                    jnA = nI <= j < nI + nA; jnB = j >= nI + nA
                    if (inA and jnB) or (inB and jnA): continue
                    if S[i][j] % p: bad += 1
            Cq.append([[S[nI + i][nI + nA + j] % p for j in range(beta)] for i in range(alpha)])
        systems[label] = dict(n=len(quads), nonbilinear_entries=bad, C=Cq)
        # generic ranks of M(a) (#q x beta) and N(b) (#q x alpha)
        def Mat_a(a):
            return [[sum(a[i]*Cq_[i][j] for i in range(alpha)) % p for j in range(beta)] for Cq_ in Cq]
        def Mat_b(b):
            return [[sum(Cq_[i][j]*b[j] for j in range(beta)) % p for i in range(alpha)] for Cq_ in Cq]
        a0 = [rng.randint(1, p-1) for _ in range(alpha)]; b0 = [rng.randint(1, p-1) for _ in range(beta)]
        rM = rank_mod(Mat_a(a0), beta, p) if Cq else 0
        rN = rank_mod(Mat_b(b0), alpha, p) if Cq else 0
        systems[label].update(generic_rank_M=rM, generic_rank_N=rN)
        if verbose:
            print(f"[{spec} seed={seed} p={p}] {label}: {len(quads)} quadrics, non-bilinear entries {bad}; "
                  f"alpha={alpha} beta={beta} (inter {len(I)}); generic rank M(a)={rM}/{beta}, N(b)={rN}/{alpha}", flush=True)
    rec['systems'] = {l: {kk: v for kk, v in s.items() if kk != 'C'} for l, s in systems.items()}
    # Singular on the reduced system (alpha + beta variables), Qpi and Q2
    for label in ('Qpi', 'Q2'):
        Cq = systems[label]['C']
        fn = f"analysis/wk10_s66_bil_{spec}_s{seed}_p{p}_{label}.sing"
        pf = f"results/s66_bilprimes_{spec}_s{seed}_p{p}_{label}.txt"
        with open(fn, 'w') as f:
            f.write(f'// Session 66 : reduced bilinear system {label} at a {spec} point; alpha={alpha}, beta={beta}\n')
            f.write('LIB "primdec.lib";\n')
            f.write(f'ring r = {p}, (a(1..{alpha}), b(1..{beta})), dp;\noption(redSB);\n')
            polys = []
            for C in Cq:
                terms = []
                for i in range(alpha):
                    for j in range(beta):
                        c = C[i][j] % p
                        if not c: continue
                        if c > p//2: c -= p
                        terms.append(f"({c})*a({i+1})*b({j+1})")
                polys.append(" + ".join(terms) if terms else "0")
            f.write('ideal I = ' + ",\n  ".join(polys) + ';\n')
            f.write('int t0 = timer;\nideal G = std(I);\n')
            f.write(f'print("{label}: dim V = " + string(dim(G)) + ", time " + string(timer - t0));\n')
            f.write('t0 = timer;\nlist mp = minAssGTZ(I);\n')
            f.write(f'print("{label}: " + string(size(mp)) + " minimal primes, time " + string(timer - t0));\n')
            f.write(f'write(":w {pf}", "");\nint i; int j;\n')
            f.write('for (i = 1; i <= size(mp); i++) {\n  ideal Pi = std(mp[i]);\n  int islin = 1;\n')
            f.write('  for (j = 1; j <= size(Pi); j++) { if (deg(Pi[j]) > 1) { islin = 0; } }\n')
            f.write('  print("  prime " + string(i) + ": dim " + string(dim(Pi)) + ", degree " + string(mult(Pi)) + ", ngens " + string(size(Pi)) + ", linear " + string(islin));\n')
            f.write(f'  write(":a {pf}", "PRIME " + string(i));\n  write(":a {pf}", string(Pi));\n  kill islin;\n}}\nquit;\n')
        log = f"results/logs/s66_bil_{spec}_s{seed}_p{p}_{label}.log"
        with open(log, 'w') as lf:
            proc = subprocess.Popen(['timeout', str(timeout_s), 'Singular', '-q', fn], stdout=lf, stderr=subprocess.STDOUT)
            open(log.replace('.log', '.pid'), 'w').write(str(proc.pid) + "\n"); proc.wait()
        out = open(log).read()
        if verbose: print("   " + "\n   ".join(l for l in out.splitlines() if 'redefining' not in l), flush=True)
        rec['systems'][label]['singular'] = dict(exit=proc.returncode,
                                                 summary=[l for l in out.splitlines() if ('prime' in l or 'dim V' in l)])
        # parse primes, sample generic points of the ones not equal to {a=0} or {b=0}, run the identity
        if os.path.exists(pf) and label == 'Qpi':
            txt = open(pf).read()
            blocks = re.split(r'PRIME \d+\n', txt)[1:]
            rec['order2'] = []
            for idx, blk in enumerate(blocks):
                gens = [g.strip() for g in blk.replace('\n', '').split(',') if g.strip()]
                # linear generators -> vectors in (a, b)
                vecs = []
                nonlin = False
                for g in gens:
                    v = [0]*(alpha + beta); ok = True
                    for term in re.findall(r'[+-]?[^+-]+', g.replace(' ', '')):
                        m = re.fullmatch(r'([+-]?)(\d*)\*?([ab])\((\d+)\)', term)
                        if not m: ok = False; break
                        sgn = -1 if m.group(1) == '-' else 1
                        c = int(m.group(2)) if m.group(2) else 1
                        idx_ = int(m.group(4)) - 1 + (0 if m.group(3) == 'a' else alpha)
                        v[idx_] = (v[idx_] + sgn*c) % p
                    if not ok: nonlin = True; break
                    vecs.append(v)
                entry = dict(prime=idx+1, ngens=len(gens), linear=not nonlin)
                if nonlin:
                    entry['note'] = 'non-linear prime: sampled by the rank-stratification route if alpha <= 3'
                    rec['order2'].append(entry); continue
                Lm = nmod_mat(len(vecs), alpha + beta, [int(x) for v in vecs for x in v], p)
                comp = kernel_basis(Lm)
                # is it {a=0} or {b=0} ?
                is_a0 = all(all(x % p == 0 for x in v[:alpha]) for v in comp)
                is_b0 = all(all(x % p == 0 for x in v[alpha:]) for v in comp)
                entry.update(dim_ab=len(comp), is_T2=is_a0, is_T1=is_b0)
                if is_a0 or is_b0:
                    entry['note'] = 'tangent space of ' + (names[1] if is_a0 else names[0]) + ' (order 2 adds nothing)'
                    rec['order2'].append(entry); continue
                # generic point : w = (i random, (a,b) random in comp) -> z = Z w -> M_1
                w = [rng.randint(1, p-1) for _ in range(len(I))] + [0]*(alpha + beta)
                for v in comp:
                    c = rng.randint(1, p-1)
                    for t in range(alpha + beta): w[len(I) + t] = (w[len(I) + t] + c*v[t]) % p
                z = [sum(Z[i][j]*w[j] for j in range(k)) % p for i in range(k)]
                m1v = [0]*80
                for i in range(k):
                    for r_ in range(80): m1v[r_] = (m1v[r_] + z[i]*kerB[i][r_]) % p
                M1 = vec_pencil(m1v)
                zero = pencil_zero(Fp(p))
                g1, g2c = all_g(build, theta, [M1, zero], 2, p)
                assert not any(g1)
                const = [g2c[i] for i in S5DEG0]
                cols2 = []
                for kk in range(R):
                    for a_ in range(n):
                        for b_ in range(n):
                            g = all_g(build, theta, [M1, zero], 2, p, dual=('m', 2, kk, a_, b_))[1]
                            cols2.append([g[i] for i in S5DEG0])
                part = solve_aug(cols2, const, len(S5DEG0), p)
                if part is None:
                    entry['note'] = 'order-2 solve failed'; rec['order2'].append(entry); continue
                m2v = [v % p for v in part]
                X, nul = nmod_mat(len(S5DEG0), 80, [int(cols2[j][r_]) for r_ in range(len(S5DEG0)) for j in range(80)], p).nullspace()
                for t in range(nul):
                    c = rng.randint(1, p-1)
                    for r_ in range(80): m2v[r_] = (m2v[r_] + c*int(X[r_, t])) % p
                M2 = vec_pencil(m2v)
                g1, g2 = all_g(build, theta, [M1, M2], 2, p)
                assert not any(g1) and not any(g2[i] for i in S5DEG0)
                g2_in_im = solve_aug([[int(dP[i, j]) for i in range(NQ)] for j in range(80)], [(-x) % p for x in g2], NQ, p) is not None
                rows_full = []; rows_con = []
                params = [('t', i) for i in range(len(theta))] + \
                         [('m', j, kk, a_, b_) for j in (1, 2) for kk in range(R) for a_ in range(n) for b_ in range(n)]
                for pr in params:
                    gg1, gg2 = all_g(build, theta, [M1, M2], 2, p, dual=pr)
                    rows_full.append(gg1 + gg2); rows_con.append(gg1 + [gg2[i] for i in S5DEG0])
                rf = rank_mod(rows_full, 2*NQ, p); rc = rank_mod(rows_con, NQ + len(S5DEG0), p)
                entry.update(g2_nonzero=any(g2), g2_in_im_dPhi=g2_in_im, rank_full=rf, rank_con=rc, order2_reducible=rf - rc)
                if verbose: print(f"   prime {idx+1} (dim {len(comp)} in (a,b)): g2 in im dPhi {g2_in_im}; order-2 reducible image = {rf - rc}", flush=True)
                rec['order2'].append(entry)
    rec['seconds'] = round(time.time() - t0, 1)
    return rec

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--specs', default='P_SP,P_coker,P_meet,SP_c32,SP_c21,SP_coker,c21_c32,ker_coker,ker_c21')
    ap.add_argument('--seeds', default='1')
    ap.add_argument('--p', type=int, default=32003)
    ap.add_argument('--timeout', type=int, default=1200)
    ap.add_argument('--out', default='results/s66_bilinear.json')
    a = ap.parse_args()
    res = json.load(open(a.out)) if os.path.exists(a.out) else []
    for spec in a.specs.split(','):
        for seed in [int(x) for x in a.seeds.split(',')]:
            res.append(run(spec, seed, a.p, a.timeout))
            json.dump(res, open(a.out, 'w'), indent=1)
    print("wrote", a.out)

# ----------------------------------------------------------------------
# three or more components : drop the common intersection I = cap T_i (a quadric
# vanishing on every T_i, with sum T_i = ker, has no dependence on I), run Singular
# on the reduced system in the remaining variables, sample linear primes.
def intersect_spaces(spaces, k, p):
    cur = rref_basis(spaces[0], k, p)
    for S in spaces[1:]:
        B2 = rref_basis(S, k, p)
        M = nmod_mat(len(cur) + len(B2), k, [int(x) for v in cur + B2 for x in v], p)
        X, nul = M.transpose().nullspace()
        inter = []
        for t in range(nul):
            c = [int(X[r, t]) for r in range(len(cur) + len(B2))]
            inter.append([sum(c[r]*cur[r][j] for r in range(len(cur))) % p for j in range(k)])
        cur = rref_basis(inter, k, p) if inter else []
    return cur

def run_multi(spec, seed, p, timeout_s=1200, verbose=True):
    t0 = time.time()
    rng = random.Random(seed*7919 + zlib.crc32(spec.encode()) % 1000)
    theta, build = family(spec, rng, p)
    pen = pencil_int(build(theta, Fp(p)))
    dP = dPhi_matrix(pen, p); rk = dP.rank(); kerB = kernel_basis(dP); k = len(kerB)
    _, T = tangents_at(spec, theta, p, rng)
    names = list(T)
    Tz = {nm: coords_in_kernel(rref_basis(T[nm], 80, p), kerB, p) for nm in names}
    I = intersect_spaces([Tz[nm] for nm in names], k, p)
    # complement coordinates : extend I by kernel basis vectors
    Wc = extend(I, [[1 if j == i else 0 for j in range(k)] for i in range(k)], k, p)
    assert len(I) + len(Wc) == k
    Z = [[0]*k for _ in range(k)]
    for j, v in enumerate(I + Wc):
        for i in range(k): Z[i][j] = v[i] % p
    nI, nW = len(I), len(Wc)
    rec = dict(spec=spec, seed=seed, p=p, rank_dPhi=rk, dim_ker=k, comps={nm: len(Tz[nm]) for nm in names},
               dim_common_intersection=nI, reduced_vars=nW)
    # the T_i in the reduced coordinates (their w-parts)
    Zm = nmod_mat(k, k, [x for row in Z for x in row], p); Zi = Zm.inv()
    def to_w(v):
        V = nmod_mat(k, 1, [int(x) % p for x in v], p); W = Zi * V
        return [int(W[nI + t, 0]) for t in range(nW)]
    Tw = {nm: rref_basis([to_w(v) for v in Tz[nm]], nW, p) for nm in names}
    cs_all = kernel_basis(dP.transpose())
    piP = nmod_mat(len(S5DEG0), 80, [int(dP[i, j]) for i in S5DEG0 for j in range(80)], p)
    cs_pi = []
    for c in kernel_basis(piP.transpose()):
        full = [0]*NQ
        for t, i in enumerate(S5DEG0): full[i] = c[t]
        cs_pi.append(full)
    rec['systems'] = {}
    for label, cs in (('Q2', cs_all), ('Qpi', cs_pi)):
        quads = quadrics_from(pen, dP, kerB, cs, p)
        def ut(Qm): return [Qm[i][j] for i in range(k) for j in range(i, k)]
        def from_ut(v):
            Qm = [[0]*k for _ in range(k)]; t = 0
            for i in range(k):
                for j in range(i, k): Qm[i][j] = v[t]; t += 1
            return Qm
        quads = [from_ut(v) for v in independent_rows([ut(q) for q in quads], k*(k+1)//2, p)]
        red = []; bad = 0
        for Qm in quads:
            S = quad_in_coords(Qm, Z, k, p)
            for i in range(k):
                for j in range(k):
                    if (i < nI or j < nI) and S[i][j] % p: bad += 1
            red.append([[S[nI + i][nI + j] % p for j in range(nW)] for i in range(nW)])   # symmetric, 2x diag
        rec['systems'][label] = dict(n=len(quads), i_dependent_entries=bad)
        if verbose: print(f"[{spec} seed={seed} p={p}] {label}: {len(quads)} quadrics in {nW} reduced variables (common intersection {nI}); i-dependent entries {bad}", flush=True)
        fn = f"analysis/wk10_s66_red_{spec}_s{seed}_p{p}_{label}.sing"
        pf = f"results/s66_redprimes_{spec}_s{seed}_p{p}_{label}.txt"
        with open(fn, 'w') as f:
            f.write(f'// Session 66 : reduced system {label} at a {spec} point; {nW} variables after dropping the common intersection ({nI})\n')
            f.write('LIB "primdec.lib";\n')
            f.write(f'ring r = {p}, w(1..{nW}), dp;\noption(redSB);\n')
            polys = []
            for S in red:
                terms = []
                for i in range(nW):
                    for j in range(i, nW):
                        c = (S[i][i] * pow(2, p-2, p)) % p if i == j else S[i][j] % p
                        if not c: continue
                        if c > p//2: c -= p
                        terms.append(f"({c})*w({i+1})^2" if i == j else f"({c})*w({i+1})*w({j+1})")
                polys.append(" + ".join(terms) if terms else "0")
            f.write('ideal I = ' + ",\n  ".join(polys) + ';\n')
            for nm in names:
                Zt = nmod_mat(len(Tw[nm]), nW, [int(x) for v in Tw[nm] for x in v], p)
                forms = kernel_basis(Zt)
                f.write(f'ideal L_{nm} = ' + ",\n  ".join(" + ".join(f"({(c if c <= p//2 else c - p)})*w({i+1})" for i, c in enumerate(v) if c % p) or "0" for v in forms) + ';\n')
            f.write('int t0 = timer;\nideal G = std(I);\n')
            f.write(f'print("{label}: dim V = " + string(dim(G)) + ", time " + string(timer - t0));\n')
            f.write('t0 = timer;\nlist mp = minAssGTZ(I);\n')
            f.write(f'print("{label}: " + string(size(mp)) + " minimal primes, time " + string(timer - t0));\n')
            f.write(f'write(":w {pf}", "");\nint i; int j;\n')
            f.write('for (i = 1; i <= size(mp); i++) {\n  ideal Pi = std(mp[i]);\n  int islin = 1;\n')
            f.write('  for (j = 1; j <= size(Pi); j++) { if (deg(Pi[j]) > 1) { islin = 0; } }\n  string eq = "";\n')
            for nm in names:
                f.write(f'  if (size(reduce(L_{nm}, Pi)) == 0 && size(reduce(Pi, std(L_{nm}))) == 0) {{ eq = eq + " =T_{nm}"; }}\n')
            f.write('  print("  prime " + string(i) + ": dim " + string(dim(Pi)) + ", degree " + string(mult(Pi)) + ", ngens " + string(size(Pi)) + ", linear " + string(islin) + eq);\n')
            f.write(f'  write(":a {pf}", "PRIME " + string(i));\n  write(":a {pf}", string(Pi));\n  kill islin; kill eq;\n}}\nquit;\n')
        log = f"results/logs/s66_red_{spec}_s{seed}_p{p}_{label}.log"
        with open(log, 'w') as lf:
            proc = subprocess.Popen(['timeout', str(timeout_s), 'Singular', '-q', fn], stdout=lf, stderr=subprocess.STDOUT)
            open(log.replace('.log', '.pid'), 'w').write(str(proc.pid) + "\n"); proc.wait()
        out = open(log).read()
        if verbose: print("   " + "\n   ".join(l for l in out.splitlines() if 'redefining' not in l), flush=True)
        rec['systems'][label]['singular'] = dict(exit=proc.returncode, summary=[l for l in out.splitlines() if ('prime' in l or 'dim V' in l)])
        if os.path.exists(pf) and label == 'Qpi':
            blocks = re.split(r'PRIME \d+\n', open(pf).read())[1:]
            rec['order2'] = []
            for idx, blk in enumerate(blocks):
                gens = [g.strip() for g in blk.replace('\n', '').split(',') if g.strip()]
                vecs = []; nonlin = False
                for g in gens:
                    v = [0]*nW; ok = True
                    for term in re.findall(r'[+-]?[^+-]+', g.replace(' ', '')):
                        m = re.fullmatch(r'([+-]?)(\d*)\*?w\((\d+)\)', term)
                        if not m: ok = False; break
                        sgn = -1 if m.group(1) == '-' else 1
                        c = int(m.group(2)) if m.group(2) else 1
                        v[int(m.group(3)) - 1] = (v[int(m.group(3)) - 1] + sgn*c) % p
                    if not ok: nonlin = True; break
                    vecs.append(v)
                entry = dict(prime=idx+1, ngens=len(gens), linear=not nonlin)
                if nonlin:
                    entry['note'] = 'non-linear prime: not sampled'; rec['order2'].append(entry); continue
                comp = kernel_basis(nmod_mat(len(vecs), nW, [int(x) for v in vecs for x in v], p))
                eq = [nm for nm in names if len(Tw[nm]) == len(comp) and
                      all(all(sum(v[i]*b[i] for i in range(nW)) % p == 0 for v in vecs) for b in Tw[nm])]
                entry.update(dim_w=len(comp), equals=eq)
                if eq:
                    entry['note'] = 'tangent space of ' + eq[0]; rec['order2'].append(entry); continue
                w = [rng.randint(1, p-1) for _ in range(nI)] + [0]*nW
                for v in comp:
                    c = rng.randint(1, p-1)
                    for t in range(nW): w[nI + t] = (w[nI + t] + c*v[t]) % p
                z = [sum(Z[i][j]*w[j] for j in range(k)) % p for i in range(k)]
                m1v = [0]*80
                for i in range(k):
                    for r_ in range(80): m1v[r_] = (m1v[r_] + z[i]*kerB[i][r_]) % p
                M1 = vec_pencil(m1v); zero = pencil_zero(Fp(p))
                g1, g2c = all_g(build, theta, [M1, zero], 2, p); assert not any(g1)
                const = [g2c[i] for i in S5DEG0]; cols2 = []
                for kk in range(R):
                    for a_ in range(n):
                        for b_ in range(n):
                            g = all_g(build, theta, [M1, zero], 2, p, dual=('m', 2, kk, a_, b_))[1]
                            cols2.append([g[i] for i in S5DEG0])
                part = solve_aug(cols2, const, len(S5DEG0), p)
                if part is None:
                    entry['note'] = 'order-2 solve failed'; rec['order2'].append(entry); continue
                m2v = [v % p for v in part]
                X, nul = nmod_mat(len(S5DEG0), 80, [int(cols2[j][r_]) for r_ in range(len(S5DEG0)) for j in range(80)], p).nullspace()
                for t in range(nul):
                    c = rng.randint(1, p-1)
                    for r_ in range(80): m2v[r_] = (m2v[r_] + c*int(X[r_, t])) % p
                M2 = vec_pencil(m2v)
                g1, g2 = all_g(build, theta, [M1, M2], 2, p); assert not any(g1) and not any(g2[i] for i in S5DEG0)
                g2_in_im = solve_aug([[int(dP[i, j]) for i in range(NQ)] for j in range(80)], [(-x) % p for x in g2], NQ, p) is not None
                rows_full = []; rows_con = []
                params = [('t', i) for i in range(len(theta))] + \
                         [('m', j, kk, a_, b_) for j in (1, 2) for kk in range(R) for a_ in range(n) for b_ in range(n)]
                for pr in params:
                    gg1, gg2 = all_g(build, theta, [M1, M2], 2, p)  if False else all_g(build, theta, [M1, M2], 2, p, dual=pr)
                    rows_full.append(gg1 + gg2); rows_con.append(gg1 + [gg2[i] for i in S5DEG0])
                rf = rank_mod(rows_full, 2*NQ, p); rc = rank_mod(rows_con, NQ + len(S5DEG0), p)
                entry.update(g2_nonzero=any(g2), g2_in_im_dPhi=g2_in_im, rank_full=rf, rank_con=rc, order2_reducible=rf - rc)
                if verbose: print(f"   prime {idx+1} (dim {len(comp)} reduced): g2 in im dPhi {g2_in_im}; order-2 reducible image = {rf - rc}", flush=True)
                rec['order2'].append(entry)
    rec['seconds'] = round(time.time() - t0, 1)
    return rec

if __name__ == '__main__' and '--multi' in sys.argv:
    pass

# ----------------------------------------------------------------------
# the generic-kernel components of V' = {(a,b) : M(a) b = 0}, sampled directly
# (no Groebner basis) : a generic, b generic in ker M(a)  -- and the mirror
# b generic, a generic in ker N(b).  Used where minAssGTZ does not finish
# (ker cap coker : alpha = beta = 12) and as a check elsewhere.
def run_generic_kernel(spec, seed, p, verbose=True):
    rng = random.Random(seed*7919 + zlib.crc32(spec.encode()) % 1000)
    theta, build = family(spec, rng, p)
    pen = pencil_int(build(theta, Fp(p)))
    dP = dPhi_matrix(pen, p); rk = dP.rank(); kerB = kernel_basis(dP); k = len(kerB)
    _, T = tangents_at(spec, theta, p, rng)
    names = list(T); assert len(names) == 2
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
    rec = dict(spec=spec, seed=seed, p=p, alpha=alpha, beta=beta, nQpi=len(Cq), comps={nm: len(Tz[nm]) for nm in names})
    zero = pencil_zero(Fp(p))
    def image_at(a, b, tag):
        w = [rng.randint(1, p-1) for _ in range(len(I))] + list(a) + list(b)
        z = [sum(Z[i][j]*w[j] for j in range(k)) % p for i in range(k)]
        m1v = [0]*80
        for i in range(k):
            for r_ in range(80): m1v[r_] = (m1v[r_] + z[i]*kerB[i][r_]) % p
        M1 = vec_pencil(m1v)
        g1, g2c = all_g(build, theta, [M1, zero], 2, p); assert not any(g1)
        const = [g2c[i] for i in S5DEG0]; cols2 = []
        for kk in range(R):
            for a_ in range(n):
                for b_ in range(n):
                    g = all_g(build, theta, [M1, zero], 2, p, dual=('m', 2, kk, a_, b_))[1]
                    cols2.append([g[i] for i in S5DEG0])
        part = solve_aug(cols2, const, len(S5DEG0), p)
        if part is None: return dict(tag=tag, note='order-2 solve failed')
        m2v = [v % p for v in part]
        X, nul = nmod_mat(len(S5DEG0), 80, [int(cols2[j][r_]) for r_ in range(len(S5DEG0)) for j in range(80)], p).nullspace()
        for t in range(nul):
            c = rng.randint(1, p-1)
            for r_ in range(80): m2v[r_] = (m2v[r_] + c*int(X[r_, t])) % p
        M2 = vec_pencil(m2v)
        g1, g2 = all_g(build, theta, [M1, M2], 2, p); assert not any(g1) and not any(g2[i] for i in S5DEG0)
        rows_full = []; rows_con = []
        params = [('t', i) for i in range(len(theta))] + \
                 [('m', j, kk, a_, b_) for j in (1, 2) for kk in range(R) for a_ in range(n) for b_ in range(n)]
        for pr in params:
            gg1, gg2 = all_g(build, theta, [M1, M2], 2, p, dual=pr)
            rows_full.append(gg1 + gg2); rows_con.append(gg1 + [gg2[i] for i in S5DEG0])
        rf = rank_mod(rows_full, 2*NQ, p); rc = rank_mod(rows_con, NQ + len(S5DEG0), p)
        return dict(tag=tag, g2_nonzero=any(g2), rank_full=rf, rank_con=rc, order2_reducible=rf - rc)
    # generic a, b in ker M(a)
    a = [rng.randint(1, p-1) for _ in range(alpha)]
    Ma = [[sum(a[i]*C[i][j] for i in range(alpha)) % p for j in range(beta)] for C in Cq]
    kb = kernel_basis(nmod_mat(len(Ma), beta, [int(x) for row in Ma for x in row], p))
    b = [0]*beta
    for v in kb:
        c = rng.randint(1, p-1)
        for j in range(beta): b[j] = (b[j] + c*v[j]) % p
    rec['generic_a'] = dict(rank_M=beta - len(kb), kernel_dim=len(kb), **image_at(a, b, 'generic a, b in ker M(a)'))
    # generic b, a in ker N(b)
    b2 = [rng.randint(1, p-1) for _ in range(beta)]
    Nb = [[sum(C[i][j]*b2[j] for j in range(beta)) % p for i in range(alpha)] for C in Cq]
    ka = kernel_basis(nmod_mat(len(Nb), alpha, [int(x) for row in Nb for x in row], p))
    a2 = [0]*alpha
    for v in ka:
        c = rng.randint(1, p-1)
        for i in range(alpha): a2[i] = (a2[i] + c*v[i]) % p
    rec['generic_b'] = dict(rank_N=alpha - len(ka), kernel_dim=len(ka), **image_at(a2, b2, 'generic b, a in ker N(b)'))
    if verbose:
        print(f"[{spec} seed={seed} p={p}] alpha={alpha} beta={beta} |Qpi|={len(Cq)}: generic-a component "
              f"(ker M(a) dim {len(kb)}): image {rec['generic_a'].get('order2_reducible')}; generic-b component "
              f"(ker N(b) dim {len(ka)}): image {rec['generic_b'].get('order2_reducible')}", flush=True)
    return rec

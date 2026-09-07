#!/usr/bin/env python3
"""
Session 66 -- section 3B/3C at contact order 2 over an incidence locus Z.

At M_0 = M_0(theta) in Z (family builder from wk10_s66_orderq, standard frame):
  ker dPhi (basis K_i), the tangent spaces T_i of the known components through
  M_0, the quadric systems Q_2 and Q_2^pi in kernel coordinates, a Singular run
  (timeout, pid recorded) for the minimal primes of Q_2^pi, and then, for every
  minimal prime that is NOT the tangent space of a known component, a generic
  M_1 in it, the order-2 V-point (M_2 with pi g_2 = 0), and s59's identity

      dim{[g_2/s_5]}  =  rank d(g_1, g_2) - rank d(g_1, pi g_2)

  over (theta, M_1, M_2) at that V-point : the reducible exceptional image of
  the order-2 arcs whose first-order direction lies in that component.

Only linear minimal primes are sampled here (a non-linear prime is reported
and left for a solver); in every case run so far the primes were linear.
"""
import sys, json, argparse, time, os, subprocess, random, zlib, re
sys.path.insert(0, 'analysis')
from flint import nmod_mat
from wk10_s66_core import *
from wk10_s66_points import (comp_tangent, sp_frame_from_prim, complete_basis, mat_inv,
                             common_kernel, common_cokernel, hyperplane_basis, col_span)
from wk10_s66_orderq import family, all_g, pencil_int, solve_aug
from wk10_s66_tangent import coords_in_kernel
from wk10_s66_cas import quadrics_from, poly_str, lin_str, independent_rows

def tangents_at(spec, theta, p, rng):
    """tangent vectors (80-vectors) of every known component through the family
    point M_0(theta), in the standard frame of the family."""
    Rg = Fp(p)
    pen = pencil_int(family_build(spec, theta, p))
    T = {}
    I4 = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    def _mat(off, r, c): return [[theta[off + i*c + j] for j in range(c)] for i in range(r)]
    if spec.startswith('P'):
        # recover (phi, u) from theta through the family's own layout
        phi, u = prim_params(spec, theta, p)
        T['P'] = [pencil_vec(t) for t in prim_point(Rg, phi, u)[1]]
        if spec in ('P_SP', 'P_c32'):
            Y = [[1,0,0,0],[0,1,0,0],[0,0,1,0]] if spec == 'P_c32' else _mat(39, 3, n)   # im u
            spar = sp_frame_from_prim(phi, u, Y, rng, p)
            pen2, tang2 = sp_point(Rg, spar['phi'], spar['x'], spar['c'], spar['P'], spar['Q'])
            assert pencil_vec(pen2) == pencil_vec(pen)
            T['SP'] = [pencil_vec(t) for t in tang2]
        if spec == 'P_c32':
            def phi_wedge(yi, yj):
                w = [(yi[b]*yj[c] - yi[c]*yj[b]) % p for (b, c) in PAIRS]
                return [sum(phi[a][s]*w[s] for s in range(6)) % p for a in range(n)]
            Y = [[1,0,0,0],[0,1,0,0],[0,0,1,0]]
            vecs = [phi_wedge(Y[0], Y[1]), phi_wedge(Y[0], Y[2]), phi_wedge(Y[1], Y[2])]
            A = nmod_mat(3, n, [int(x) for vv in vecs for x in vv], p); assert A.rank() == 2
            rr = A.rref()[0]; W2 = [[int(rr[i, j]) for j in range(n)] for i in range(2)]
            T['c32'] = [pencil_vec(t) for t in comp_tangent('c32', I4, complete_basis(W2, rng, p), pen, p)]
        if spec == 'P_coker':
            cok = common_cokernel(pen, p); assert len(cok) == 1
            W = hyperplane_basis(cok[0], rng, p); extra = complete_basis(W, rng, p)
            cols = [[extra[a][3] for a in range(n)]] + [[extra[a][j] for a in range(n)] for j in range(3)]
            h2 = [[cols[j][a] for j in range(n)] for a in range(n)]
            T['coker'] = [pencil_vec(t) for t in comp_tangent('coker', I4, h2, pen, p)]
        if spec == 'P_c21':
            gi = None
            v = _mat(24, R, 2); w = _mat(34, 2, n)
            U2 = [w[0], w[1]]
            def phi_wedge(yi, yj):
                ww = [(yi[b]*yj[c] - yi[c]*yj[b]) % p for (b, c) in PAIRS]
                return [sum(phi[a][s]*ww[s] for s in range(6)) % p for a in range(n)]
            W1 = [phi_wedge(U2[0], U2[1])]
            T['c21'] = [pencil_vec(t) for t in comp_tangent('c21', complete_basis(U2, rng, p),
                                                             complete_basis(W1, rng, p), pen, p)]
            for t_ in range(2):
                Y = [U2[0], U2[1], [rng.randint(1, p-1) for _ in range(n)]]
                spar = sp_frame_from_prim(phi, u, Y, rng, p)
                pen2, tang2 = sp_point(Rg, spar['phi'], spar['x'], spar['c'], spar['P'], spar['Q'])
                assert pencil_vec(pen2) == pencil_vec(pen)
                T[f'SP{t_}'] = [pencil_vec(t) for t in tang2]
        if spec == 'P_meet':
            from wk10_s66_points import sp_frame_from_pencil
            par = sp_frame_from_pencil(pencil_T(pen), rng, p); assert par is not None
            pen2, tang2 = sp_point(Rg, par['phi'], par['x'], par['c'], par['P'], par['Q'])
            assert pencil_vec(pencil_T(pen2)) == pencil_vec(pen)
            T['SPT'] = [pencil_vec(pencil_T(t)) for t in tang2]
    elif spec.startswith('SP'):
        phi, x, c = sp_params(spec, theta, p)
        T['SP'] = [pencil_vec(t) for t in sp_point(Rg, phi, x, c, I4, I4)[1]]
        if spec == 'SP_c32':
            W2 = col_span(phi, p); assert len(W2) == 2
            T['c32'] = [pencil_vec(t) for t in comp_tangent('c32', I4, complete_basis(W2, rng, p), pen, p)]
        if spec == 'SP_c21':
            X = x; A = nmod_mat(R, 3, [int(v) for row in X for v in row], p); rr = A.rref()[0]
            xb = [[int(rr[i, j]) for j in range(3)] for i in range(2)]
            U2 = [xb[0] + [0], xb[1] + [0]]
            cr = [(xb[0][1]*xb[1][2] - xb[0][2]*xb[1][1]) % p, (xb[0][2]*xb[1][0] - xb[0][0]*xb[1][2]) % p,
                  (xb[0][0]*xb[1][1] - xb[0][1]*xb[1][0]) % p]
            W1 = [[sum(phi[a][j]*cr[j] for j in range(3)) % p for a in range(n)]]
            T['c21'] = [pencil_vec(t) for t in comp_tangent('c21', complete_basis(U2, rng, p),
                                                             complete_basis(W1, rng, p), pen, p)]
        if spec == 'SP_coker':
            cok = common_cokernel(pen, p); assert len(cok) == 1
            W = hyperplane_basis(cok[0], rng, p); extra = complete_basis(W, rng, p)
            cols = [[extra[a][3] for a in range(n)]] + [[extra[a][j] for a in range(n)] for j in range(3)]
            h2 = [[cols[j][a] for j in range(n)] for a in range(n)]
            T['coker'] = [pencil_vec(t) for t in comp_tangent('coker', I4, h2, pen, p)]
    elif spec in ('c21_c32', 'ker_coker', 'ker_c21'):
        a_, b_ = spec.split('_')
        for nm in (a_, b_):
            T[nm] = [pencil_vec(t) for t in comp_tangent(nm, I4, I4, pen, p)]
    return pen, T

_FAM = {}
def family_build(spec, theta, p):
    if spec not in _FAM:
        _FAM[spec] = family(spec, random.Random(0), p)[1]
    return _FAM[spec](theta, Fp(p))

def prim_params(spec, theta, p):
    Rg = Fp(p)
    def _mat(off, r, c): return [[theta[off + i*c + j] for j in range(c)] for i in range(r)]
    if spec == 'P': return _mat(0, n, 6), _mat(24, R, n)
    if spec == 'P_coker': return mat_mul(Rg, _mat(0, n, 3), _mat(12, 3, 6)), _mat(30, R, n)
    if spec == 'P_SP': return _mat(0, n, 6), mat_mul(Rg, _mat(24, R, 3), _mat(39, 3, n))
    if spec == 'P_c21': return _mat(0, n, 6), mat_mul(Rg, _mat(24, R, 2), _mat(34, 2, n))
    if spec == 'P_c32':
        s01 = PAIRS.index((0, 1)); phi = [[0]*6 for _ in range(n)]; t = 0
        for a in range(n):
            for si in range(6):
                if si == s01: continue
                phi[a][si] = theta[t]; t += 1
        v = _mat(t, R, 3); u = [[v[k][0], v[k][1], v[k][2], 0] for k in range(R)]
        return phi, u
    if spec in ('P_tan', 'P_meet'):
        # rebuild through the builder's annihilator basis : evaluate the pencil and
        # recover phi from it is not needed -- use the builder's phi directly
        b = family(spec, random.Random(0), p)[1]
        # the builder returns only the pencil ; recompute phi here the same way
        def pl(bb, cc):
            v = [0]*6; v[PAIRS.index((bb, cc))] = 1; return v
        e12, e13, e24 = pl(0, 1), pl(0, 2), pl(1, 3)
        k1 = e12; k2 = e13 if spec == 'P_meet' else [x + y for x, y in zip(e13, e24)]
        Km = nmod_mat(2, 6, [x % p for x in k1] + [x % p for x in k2], p)
        NS, nul = Km.nullspace(); ann = [[int(NS[i, j]) for i in range(6)] for j in range(4)]
        phi = []
        for a in range(n):
            row = [0]*6
            for j in range(4):
                for i in range(6):
                    row[i] = (row[i] + theta[a*4 + j]*ann[j][i]) % p
            phi.append(row)
        return phi, _mat(16, R, n)
    raise ValueError(spec)

def sp_params(spec, theta, p):
    Rg = Fp(p)
    def _mat(off, r, c): return [[theta[off + i*c + j] for j in range(c)] for i in range(r)]
    if spec == 'SP': return _mat(0, n, 3), _mat(12, R, 3), _mat(27, R, n)
    if spec == 'SP_c32': return mat_mul(Rg, _mat(0, n, 2), _mat(8, 2, 3)), _mat(14, R, 3), _mat(29, R, n)
    if spec == 'SP_c21': return _mat(0, n, 3), mat_mul(Rg, _mat(12, R, 2), _mat(22, 2, 3)), _mat(28, R, n)
    if spec == 'SP_coker':
        phi = _mat(0, n, 3); x = _mat(12, R, 3); cp = _mat(27, R, 3)
        c = [[sum(phi[a][j]*cp[k][j] for j in range(3)) % p for a in range(n)] for k in range(R)]
        return phi, x, c
    raise ValueError(spec)

# ----------------------------------------------------------------------
def parse_primes(fn, k, p):
    """parse the primes file written by Singular : blocks 'PRIME i' then lines
    of generators (Singular string of an ideal, comma separated)."""
    txt = open(fn).read()
    blocks = re.split(r'PRIME \d+\n', txt)[1:]
    primes = []
    for b in blocks:
        gens = [g.strip() for g in b.replace('\n', '').split(',') if g.strip()]
        primes.append(gens)
    return primes

def linear_form_vec(g, k, p):
    """parse a Singular linear polynomial in z(i) into a length-k coefficient vector;
    returns None if not linear."""
    v = [0]*k
    g = g.replace(' ', '')
    for term in re.findall(r'[+-]?[^+-]+', g):
        m = re.fullmatch(r'([+-]?)(\d*)\*?z\((\d+)\)(\^(\d+))?', term)
        if not m: return None
        if m.group(4): return None
        sgn = -1 if m.group(1) == '-' else 1
        c = int(m.group(2)) if m.group(2) else 1
        v[int(m.group(3)) - 1] = (v[int(m.group(3)) - 1] + sgn*c) % p
    return v

def run_point(spec, seed, p, timeout_s=1800, verbose=True):
    t0 = time.time()
    rng = random.Random(seed*7919 + zlib.crc32(spec.encode()) % 1000)
    theta, build = family(spec, rng, p)
    pen = pencil_int(build(theta, Fp(p)))
    assert not any(det_value(pen, p))
    dP = dPhi_matrix(pen, p); rk = dP.rank(); kerB = kernel_basis(dP); k = len(kerB)
    pen_chk, T = tangents_at(spec, theta, p, rng)
    assert pencil_vec(pen_chk) == pencil_vec(pen)
    rec = dict(spec=spec, seed=seed, p=p, rank_dPhi=rk, dim_ker=k, comps={})
    spans = {}
    for nm, tv in T.items():
        ok, bad = in_kernel_count(dP, tv, p); assert bad == 0, (nm, bad)
        spans[nm] = span_rank(tv, 80, p)
        rec['comps'][nm] = spans[nm]
    union = span_rank([v for tv in T.values() for v in tv], 80, p)
    rec['union'] = union; rec['quotient'] = k - union
    # quadrics
    cs_all = kernel_basis(dP.transpose())
    piP = nmod_mat(len(S5DEG0), 80, [int(dP[i, j]) for i in S5DEG0 for j in range(80)], p)
    cs_pi = []
    for c in kernel_basis(piP.transpose()):
        full = [0]*NQ
        for t, i in enumerate(S5DEG0): full[i] = c[t]
        cs_pi.append(full)
    def ut(Qm): return [Qm[i][j] for i in range(k) for j in range(i, k)]
    def from_ut(v):
        Qm = [[0]*k for _ in range(k)]; t = 0
        for i in range(k):
            for j in range(i, k): Qm[i][j] = v[t]; t += 1
        return Qm
    Q2 = [from_ut(v) for v in independent_rows([ut(q) for q in quadrics_from(pen, dP, kerB, cs_all, p)], k*(k+1)//2, p)]
    Qpi = [from_ut(v) for v in independent_rows([ut(q) for q in quadrics_from(pen, dP, kerB, cs_pi, p)], k*(k+1)//2, p)]
    rec['dimQ2'] = len(Q2); rec['dimQpi'] = len(Qpi)
    # linear ideals of the T_i in kernel coordinates
    lin = {}
    for nm, tv in T.items():
        A = nmod_mat(len(tv), 80, [int(x) % p for v in tv for x in v], p); rr = A.rref()[0]
        basis = [[int(rr[i, j]) for j in range(80)] for i in range(A.nrows()) if any(int(rr[i, j]) for j in range(80))]
        zb = coords_in_kernel(basis, kerB, p)
        Z = nmod_mat(len(zb), k, [int(x) for v in zb for x in v], p)
        lin[nm] = dict(dim=len(zb), forms=kernel_basis(Z), zbasis=zb)
    if verbose:
        print(f"[{spec} seed={seed} p={p}] rank dPhi={rk} ker={k} T={spans} union={union} quotient={k-union} "
              f"|Q2|={len(Q2)} |Qpi|={len(Qpi)}", flush=True)
    # Singular : minimal primes of Qpi and of Q2
    base = f"analysis/wk10_s66_o2_{spec}_s{seed}_p{p}"
    primes_out = {}
    for label, Qs in (('Qpi', Qpi), ('Q2', Q2)):
        fn = base + f"_{label}.sing"; pf = f"results/s66_primes_{spec}_s{seed}_p{p}_{label}.txt"
        with open(fn, 'w') as f:
            f.write(f'// Session 66 : minimal primes of {label} at a {spec} point, kernel dim {k}, rank dPhi {rk}\n')
            f.write('LIB "primdec.lib";\n')
            f.write(f'ring r = {p}, z(1..{k}), dp;\noption(redSB);\n')
            f.write(f'ideal I = ' + ",\n  ".join(poly_str(q, p, k) for q in Qs) + ';\n')
            for nm, L in lin.items():
                f.write(f'ideal L_{nm} = ' + ",\n  ".join(lin_str(v, p, k) for v in L['forms']) + ';\n')
            f.write('int t0 = timer;\nideal G = std(I);\n')
            f.write(f'print("{label}: dim V = " + string(dim(G)) + ", time " + string(timer - t0));\n')
            f.write('t0 = timer;\nlist mp = minAssGTZ(I);\n')
            f.write(f'print("{label}: " + string(size(mp)) + " minimal primes, time " + string(timer - t0));\n')
            f.write(f'write(":w {pf}", "");\n')
            f.write('int i; int j;\nfor (i = 1; i <= size(mp); i++) {\n  ideal Pi = std(mp[i]);\n')
            f.write('  int islin = 1;\n  for (j = 1; j <= size(Pi); j++) { if (deg(Pi[j]) > 1) { islin = 0; } }\n')
            f.write('  string eq = "";\n')
            for nm in lin:
                f.write(f'  if (size(reduce(L_{nm}, Pi)) == 0 && size(reduce(Pi, std(L_{nm}))) == 0) {{ eq = eq + " =T_{nm}"; }}\n')
            f.write('  print("  prime " + string(i) + ": dim " + string(dim(Pi)) + ", degree " + string(mult(Pi)) + ", ngens " + string(size(Pi)) + ", linear " + string(islin) + eq);\n')
            f.write(f'  write(":a {pf}", "PRIME " + string(i));\n  write(":a {pf}", string(Pi));\n')
            f.write('  kill islin; kill eq;\n}\nquit;\n')
        log = f"results/logs/s66_o2_{spec}_s{seed}_p{p}_{label}.log"
        with open(log, 'w') as lf:
            proc = subprocess.Popen(['timeout', str(timeout_s), 'Singular', '-q', fn], stdout=lf, stderr=subprocess.STDOUT)
            open(log.replace('.log', '.pid'), 'w').write(str(proc.pid) + "\n")
            proc.wait()
        out = open(log).read()
        if verbose: print("   " + out.strip().replace('\n', '\n   '), flush=True)
        primes_out[label] = dict(log=out, exit=proc.returncode)
        rec[label] = dict(exit=proc.returncode, summary=[l for l in out.splitlines() if 'prime' in l or 'dim V' in l])
        if os.path.exists(pf):
            primes_out[label]['primes'] = parse_primes(pf, k, p)
    # order-2 reducible image over every linear minimal prime of Qpi that is not a T_i
    rec['order2'] = []
    if 'primes' in primes_out.get('Qpi', {}):
        for idx, gens in enumerate(primes_out['Qpi']['primes']):
            vecs = [linear_form_vec(g, k, p) for g in gens]
            if any(v is None for v in vecs):
                rec['order2'].append(dict(prime=idx+1, note='non-linear prime, not sampled')); continue
            Lm = nmod_mat(len(vecs), k, [int(x) for v in vecs for x in v], p)
            comp_basis = kernel_basis(Lm)                      # z-vectors spanning the component
            dimc = len(comp_basis)
            # which T_i does it contain / equal ?
            contains = {nm: all(all(sum(v[i]*zb[i] for i in range(k)) % p == 0 for v in vecs) for zb in L['zbasis'])
                        for nm, L in lin.items()}
            equal = [nm for nm, L in lin.items() if contains[nm] and L['dim'] == dimc]
            entry = dict(prime=idx+1, dim=dimc, contains=[nm for nm in contains if contains[nm]], equals=equal)
            if equal:
                entry['note'] = 'tangent space of a known component; order 2 adds nothing there (proved in the report)'
                rec['order2'].append(entry); continue
            # generic M_1 in the component (z-coords -> 80-vector)
            z = [0]*k
            for b in comp_basis:
                w = rng.randint(1, p-1)
                for i in range(k): z[i] = (z[i] + w*b[i]) % p
            m1v = [0]*80
            for i in range(k):
                for r_ in range(80): m1v[r_] = (m1v[r_] + z[i]*kerB[i][r_]) % p
            M1 = vec_pencil(m1v)
            # V-point : M_2 with pi g_2 = 0 ; g_2 = e_2(M_0;M_1) + dPhi(M_2)
            g1, g2c = all_g(build, theta, [M1, pencil_zero(Fp(p))], 2, p)
            assert not any(g1), "M_1 not in the kernel?"
            const = [g2c[i] for i in S5DEG0]
            cols2 = []
            for kk in range(R):
                for a in range(n):
                    for b in range(n):
                        g = all_g(build, theta, [M1, pencil_zero(Fp(p))], 2, p, dual=('m', 2, kk, a, b))[1]
                        cols2.append([g[i] for i in S5DEG0])
            part = solve_aug(cols2, const, len(S5DEG0), p)
            if part is None:
                entry['note'] = 'order-2 solve failed (M_1 not second-order solvable)'; rec['order2'].append(entry); continue
            m2v = [0]*80
            for r_, v in enumerate(part): m2v[r_] = v % p
            # add a random element of ker(pi dPhi) for genericity
            X, nul = nmod_mat(len(S5DEG0), 80, [int(cols2[j][r_]) for r_ in range(len(S5DEG0)) for j in range(80)], p).nullspace()
            for t in range(nul):
                w = rng.randint(1, p-1)
                for r_ in range(80): m2v[r_] = (m2v[r_] + w*int(X[r_, t])) % p
            M2 = vec_pencil(m2v)
            g1, g2 = all_g(build, theta, [M1, M2], 2, p)
            assert not any(g1) and not any(g2[i] for i in S5DEG0), "V-point check failed"
            entry['g2_nonzero'] = any(g2)
            # is g_2 in im dPhi (would make it an order-1 form) ?
            g2_in_im = solve_aug([[int(dP[i, j]) for i in range(NQ)] for j in range(80)], [(-x) % p for x in g2], NQ, p) is not None
            entry['g2_in_im_dPhi'] = g2_in_im
            # Jacobian over theta, M_1, M_2
            rows_full = []; rows_con = []
            params = [('t', i) for i in range(len(theta))] + \
                     [('m', j, kk, a, b) for j in (1, 2) for kk in range(R) for a in range(n) for b in range(n)]
            for pr in params:
                gg1, gg2 = all_g(build, theta, [M1, M2], 2, p, dual=pr)
                rows_full.append(gg1 + gg2)
                rows_con.append(gg1 + [gg2[i] for i in S5DEG0])
            rf = rank_mod(rows_full, 2*NQ, p); rc = rank_mod(rows_con, NQ + len(S5DEG0), p)
            entry.update(rank_full=rf, rank_con=rc, order2_reducible=rf - rc)
            if verbose:
                print(f"   prime {idx+1}: dim {dimc}, contains {entry['contains']}: g2!=0 {entry['g2_nonzero']}, "
                      f"g2 in im dPhi {g2_in_im}; order-2 reducible image = {rf-rc}", flush=True)
            rec['order2'].append(entry)
    rec['seconds'] = round(time.time() - t0, 1)
    return rec

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--specs', default='P_SP')
    ap.add_argument('--seeds', default='1')
    ap.add_argument('--p', type=int, default=32003)
    ap.add_argument('--timeout', type=int, default=1800)
    ap.add_argument('--out', default='results/s66_order2.json')
    a = ap.parse_args()
    res = json.load(open(a.out)) if os.path.exists(a.out) else []
    for spec in a.specs.split(','):
        for seed in [int(x) for x in a.seeds.split(',')]:
            res.append(run_point(spec, seed, a.p, a.timeout))
            json.dump(res, open(a.out, 'w'), indent=1)
    print("wrote", a.out)

#!/usr/bin/env python3
"""
Session 66 -- the tangent table (PREREG s66 section 3A/3B).

For every point spec (wk10_s66_points), prime and seed:
  rank dPhi, dim ker dPhi, for every component through the point the number of
  tangent vectors, how many annihilate dPhi (KC2: must be all), the span
  dimension, the limit tangent space along a curve where a curve is declared,
  the span of all component tangents, the transverse quotient, and the
  second-order quadric space Q_2 with the union-ideal bound.
"""
import sys, json, argparse, time
sys.path.insert(0, 'analysis')
from flint import nmod_mat
from wk10_s66_core import *
from wk10_s66_points import build_point, SPECS_ORDER

COMP_DIM = {'ker': 63, 'coker': 63, 'c21': 57, 'c32': 57, 'SP': 49, 'SPT': 49,
            'P': 43, 'PT': 43}
def comp_dim(name):
    base = name.rstrip('0123456789') if name.startswith('SP') else name
    return COMP_DIM[base]

def union_ideal_deg2(spaces, k, p):
    """dim of the space of quadrics on F_p^k vanishing on every linear space in
    `spaces` (each a list of k-vectors spanning it)."""
    idx = [(i, j) for i in range(k) for j in range(i, k)]
    rows = []
    for Sp in spaces:
        # conditions : for basis vectors b_r, b_s of the space, Q(b_r, b_s) = 0
        # (polarised) ; Q(z) = sum_{i<=j} q_ij z_i z_j ;  Q(b, b') polarised
        # = sum_{i<=j} q_ij (b_i b'_j + b_j b'_i) [i<j] or 2 b_i b'_i [i=j]
        B = Sp
        m = len(B)
        for r in range(m):
            for s in range(r, m):
                br, bs = B[r], B[s]
                row = []
                for (i, j) in idx:
                    if r == s:
                        row.append((br[i]*br[j]) % p)                      # Q(b) = sum_{i<=j} q_ij b_i b_j
                    elif i == j:
                        row.append((2*br[i]*bs[i]) % p)                    # polarised diagonal
                    else:
                        row.append((br[i]*bs[j] + br[j]*bs[i]) % p)        # polarised off-diagonal
                rows.append(row)
    # for r == s : Q(b,b) = sum q_ii b_i^2 + sum_{i<j} q_ij b_i b_j  (no factor 2)
    # for r != s : polarised  Q(b,b') = sum 2 q_ii b_i b'_i + sum_{i<j} q_ij (b_i b'_j + b_j b'_i)
    A = nmod_mat(len(rows), len(idx), [int(x) % p for row in rows for x in row], p)
    return len(idx) - A.rank()

def quadric_vanishes_on(Qm, basis, p):
    """does the upper-triangular quadric Qm vanish identically on span(basis)?
    Check Q(b_r + b_s) for all r <= s (over F_p, char != 2 : Q|_V = 0 iff
    Q(b_r)=0 and Q(b_r+b_s)=0 for all r<s)."""
    m = len(basis)
    for r in range(m):
        if quad_eval(Qm, basis[r], p): return False
    for r in range(m):
        for s in range(r+1, m):
            v = [(a + b) % p for a, b in zip(basis[r], basis[s])]
            if quad_eval(Qm, v, p): return False
    return True

def coords_in_kernel(vecs, kerB, p):
    """express vectors (80-dim, assumed in ker dPhi) in the kernel basis kerB."""
    k = len(kerB)
    # solve kerB^T z = v : kerB as 80 x k matrix
    A = nmod_mat(80, k, [int(kerB[j][i]) % p for i in range(80) for j in range(k)], p)
    out = []
    for v in vecs:
        if True:
            # solve via the augmented nullspace (A is 80 x k, not square)
            Aug = nmod_mat(80, k+1, [int(kerB[j][i]) % p if j < k else int(v[i]) % p
                                     for i in range(80) for j in range(k+1)], p)
            X, nul = Aug.nullspace()
            z = None
            for t in range(nul):
                last = int(X[k, t]) % p
                if last:
                    inv = pow(last, p-2, p)
                    z = [(-int(X[j, t]) * inv) % p for j in range(k)]
                    break
            assert z is not None, "vector not in kernel span"
            out.append(z)
    return out

def analyse(spec, seed, p, do_quad=True, K=4, verbose=True):
    t0 = time.time()
    d = build_point(spec, seed, p)
    pen = d['pen']
    assert not any(det_value(pen, p)), f"{spec}: det not identically zero"
    dP = dPhi_matrix(pen, p)
    rk = dP.rank(); kdim = 80 - rk
    kerB = kernel_basis(dP)                      # k vectors of length 80
    assert len(kerB) == kdim
    rec = dict(spec=spec, seed=seed, p=p, rank_dPhi=rk, dim_ker=kdim, comps={}, info=d['info'])
    spans = {}
    allvecs = []
    for name, tang in d['comps'].items():
        tv = [pencil_vec(t) for t in tang]
        ok, bad = in_kernel_count(dP, tv, p)
        dimT = span_rank(tv, 80, p)
        rec['comps'][name] = dict(nvec=len(tv), in_ker=ok, bad=bad, dimT=dimT,
                                  expected=comp_dim(name))
        spans[name] = tv
        allvecs += tv
    # limit tangents along declared curves
    for name, (penE, tangE) in d['curves'].items():
        cols = [[x for B in t for row in B for x in row] for t in tangE]   # 80-vectors of K-tuples
        # sanity : the curve passes through the point at eps = 0
        pen0 = [[[x[0] for x in row] for row in B] for B in penE]
        assert pencil_vec(pen0) == pencil_vec(pen), f"{spec}/{name}: curve does not start at the point"
        lim, piv = limit_colspace(cols, 80, p, K)
        ok, bad = in_kernel_count(dP, lim, p)
        dimL = span_rank(lim, 80, p)
        rec['comps'][name]['limit'] = dict(dim=dimL, in_ker=ok, bad=bad,
                                           valuations=sorted(set(v for _, _, v in piv)))
        together = spans[name] + lim
        rec['comps'][name]['dimT_with_limit'] = span_rank(together, 80, p)
        spans[name] = together
        allvecs += lim
    union = span_rank(allvecs, 80, p)
    rec['union'] = union
    rec['quotient'] = kdim - union
    # pairwise intersections (for two-component points)
    names = list(spans)
    if len(names) >= 2:
        inter = {}
        for i in range(len(names)):
            for j in range(i+1, len(names)):
                a, b = names[i], names[j]
                da = span_rank(spans[a], 80, p); db = span_rank(spans[b], 80, p)
                dab = span_rank(spans[a] + spans[b], 80, p)
                inter[f'{a}&{b}'] = da + db - dab
        rec['pairwise_intersection'] = inter
    if verbose:
        print(f"[{spec} seed={seed} p={p}] rank dPhi={rk} ker={kdim} union={union} "
              f"quotient={kdim-union}  " +
              "  ".join(f"{nm}:T={c['dimT']}{'/'+str(c['dimT_with_limit']) if 'dimT_with_limit' in c else ''}"
                        f"(exp {c['expected']}, bad {c['bad']})" for nm, c in rec['comps'].items()),
              flush=True)
    if do_quad:
        tq = time.time()
        dimQ2, quads, ncs = quadric_space(pen, dP, kerB, p)
        rec['Q2'] = dict(dim=dimQ2, n_generators=ncs)
        # express the component spans in kernel coordinates ; union-ideal bound
        spaces_k = {}
        for name, vv in spans.items():
            # reduce to a basis first
            A = nmod_mat(len(vv), 80, [int(x) % p for v in vv for x in v], p)
            rr = A.rref()[0]
            basis = []
            for i in range(A.nrows()):
                row = [int(rr[i, j]) for j in range(80)]
                if any(row): basis.append(row)
            spaces_k[name] = coords_in_kernel(basis, kerB, p)
        bound = union_ideal_deg2(list(spaces_k.values()), kdim, p)
        rec['Q2']['union_ideal_deg2'] = bound
        # does every quadric of Q_2 vanish on every component tangent space ?
        van = {name: all(quadric_vanishes_on(Qm, basis, p) for Qm in quads)
               for name, basis in spaces_k.items()}
        rec['Q2']['vanishes_on'] = van
        # is Q_2 contained in the union ideal ? (dim of Q_2 + I(union)_2 vs bound)
        if verbose:
            print(f"    Q2: dim={dimQ2} (generators {ncs}), I(union T)_2 = {bound}, "
                  f"vanishes on tangents: {van}  [{time.time()-tq:.1f}s]", flush=True)
    rec['seconds'] = round(time.time() - t0, 1)
    return rec

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--specs', default=','.join(SPECS_ORDER))
    ap.add_argument('--primes', default='both')
    ap.add_argument('--seeds', default='1,2')
    ap.add_argument('--noquad', action='store_true')
    ap.add_argument('--out', default='results/s66_tangent.json')
    a = ap.parse_args()
    primes = HOUSE if a.primes == 'both' else [int(x) for x in a.primes.split(',')]
    seeds = [int(x) for x in a.seeds.split(',')]
    res = []
    for spec in a.specs.split(','):
        for p in primes:
            for seed in seeds:
                res.append(analyse(spec, seed, p, do_quad=not a.noquad))
                json.dump(res, open(a.out, 'w'), indent=1)
    print("wrote", a.out)

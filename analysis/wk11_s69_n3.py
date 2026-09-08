#!/usr/bin/env python3
"""Session 69, regimes R1/R2: the n = 3 LMR ladder  lambda_delta = (3 delta - 17, 7, 2^5),
delta = 12, 13, 14  (det_3, r = 7), by the compact circuit.

For one cell:
  1. build the cell in the house chi-coordinates (wk9_s45_build.build_cell): arr, E, n_chi;
  2. sample column-strict fillings of lambda' = (7, 7, 2^5, 1^{3 delta - 24}), evaluate them
     at generic points (C evaluator, Identity 3), keep a greedy independent set until the
     generic rank reaches a = 6 (a from a_weyl);
  3. evaluate the basis fillings at det_3 pencils, both primes: rank = mult_det, kernel = U_D;
  4. expand every basis filling EXACTLY into the weight-lambda monomial basis (C, the Leibniz
     sum) and fold into chi-coordinates: assert chi-isotypy (orbit consistency, dropped orbits
     zero), E v = 0 over Z, rank 6 as chi-vectors, and that the coordinate-side evaluation of
     each expansion equals the circuit's value at every point used (evaluator vs expander);
  5. (delta = 12) compare the circuit's U_D with the banked vector, entry by entry, mod P1
     and over Z after rational reconstruction.

    python3 analysis/wk11_s69_n3.py 12 [--kgen 16] [--kdet 16] [--k K] [--tag name]

Writes results/s69_n3_d<delta>[_<tag>].json and appends a line to results/s69_sizes.jsonl.
"""
import argparse, ctypes, gzip, json, math, os, pickle, random, sys, time
import numpy as np
from math import comb
from scipy import sparse

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from wk8_s30_core import exps, P1, P2                                   # noqa: E402
from wk9_s45_build import build_cell                                    # noqa: E402
from wk9_s42_orbits import _codes                                       # noqa: E402
from wk9_s42_census import a_weyl                                       # noqa: E402
from wk11_s69_circuit import (random_filling, sym_table, symbols_from_coeffs, generic_point,
                              det_point, fast_eval_c, rank_mod, left_kernel_mod,
                              reconstruct_integer_vector, PRIMES)       # noqa: E402

N_DEG, R, H = 3, 7, 7
CACHE = os.environ.get("S69_CACHE", "/home/claude/s69cache")
T0 = time.time()


def log(*a):
    print(f"[{time.time()-T0:8.1f}s]", *a, flush=True)


def get_cell(lam, delta):
    os.makedirs(CACHE, exist_ok=True)
    f = os.path.join(CACHE, f"cell_n3_{'_'.join(map(str, lam))}_d{delta}.pkl")
    if os.path.exists(f):
        with open(f, "rb") as fh: return pickle.load(fh)
    B = build_cell(lam, delta, n=N_DEG, verbose=True)
    B["arr"].pop("mem", None); B["arr"].pop("starts", None)
    with open(f, "wb") as fh: pickle.dump(B, fh, protocol=4)
    return B


# --------------------------------------------------------------- coordinate-side evaluation
def chi_eval_rows(arr, cv_mod, p, chunk=2_000_000):
    """row[j] = sum_{m in O_j} sgn_m prod_k cv[M[m,k]]  (mod p), the chi-coordinate evaluation
    functional at the point with coefficient vector cv_mod (same formula as ev_rows_arr)."""
    M = arr["M"]; sgn = arr["sgn"]; col_of = arr["col_of"]; n_chi = arr["n_chi"]
    cv = np.array(cv_mod, dtype=np.int64) % p
    idx_k = np.nonzero(col_of >= 0)[0]
    o = np.argsort(col_of[idx_k], kind="stable")
    mem = idx_k[o]; cols = col_of[mem]
    row = np.zeros(n_chi, dtype=np.int64)
    for b0 in range(0, len(mem), chunk):
        mm = mem[b0:b0 + chunk]
        term = cv[M[mm, 0]].copy()
        for k in range(1, M.shape[1]):
            term *= cv[M[mm, k]]; term %= p
        term *= sgn[mm]; term %= p
        np.add.at(row, cols[b0:b0 + chunk], term)
        row %= p
    return row


def chi_dot(row, v, p):
    return int(sum((int(r) * int(x)) % p for r, x in zip(row.tolist(), v) if x) % p)


# --------------------------------------------------------------- exact expansion (C)
_ELIB = None


def elib():
    global _ELIB
    if _ELIB is None:
        so = os.path.join(HERE, "wk11_s69_expand.so"); src = os.path.join(HERE, "wk11_s69_expand.c")
        if not os.path.exists(so) or os.path.getmtime(so) < os.path.getmtime(src):
            os.system(f"gcc -O3 -march=native -shared -fPIC -o {so} {src}")
        _ELIB = ctypes.CDLL(so); _ELIB.expand_filling.restype = ctypes.c_longlong
    return _ELIB


class Expander:
    def __init__(self, B, n, r):
        arr = B["arr"]; self.arr = arr
        self.M = arr["M"]; self.N, self.d = self.M.shape
        A, idx, fact, tab = sym_table(n, r)
        self.L = len(A); self.n = n; self.r = r
        codes = _codes(self.M, self.L)
        self.order = np.argsort(codes, kind="stable").astype(np.int64)
        self.sorted_codes = codes[self.order].astype(np.int64)
        assert np.all(np.diff(self.sorted_codes) > 0)
        t2a = np.full(r ** n, -1, dtype=np.int32)
        for tup, a in tab.items():
            key = sum(i * r ** q for q, i in enumerate(tup)); t2a[key] = a
        self.tup2a = t2a
        self.afact = np.array(fact, dtype=np.int64)
        self.binom = np.array([[comb(m + k, k + 1) for m in range(self.L)] for k in range(self.d)], dtype=np.int64)

    def expand(self, F):
        d, n, n2 = F.delta, F.n, F.n2
        assert d == self.d
        cells = F.cells_of_letter()
        cc = np.zeros(d * n, np.int32); cr = np.zeros(d * n, np.int32)
        for l in range(d):
            assert len(cells[l]) == n
            for q, (c, rw) in enumerate(cells[l]): cc[l * n + q] = c; cr[l * n + q] = rw
        lo = np.zeros(self.N, np.int64); hi = np.zeros(self.N, np.int64)
        I32 = ctypes.POINTER(ctypes.c_int32); I64 = ctypes.POINTER(ctypes.c_int64)
        t = time.time()
        nt = elib().expand_filling(F.h, d, n, n2, self.r, self.L,
                                   cc.ctypes.data_as(I32), cr.ctypes.data_as(I32),
                                   self.tup2a.ctypes.data_as(I32), self.afact.ctypes.data_as(I64),
                                   self.binom.ctypes.data_as(I64), self.sorted_codes.ctypes.data_as(I64),
                                   self.order.ctypes.data_as(I64), ctypes.c_longlong(self.N),
                                   lo.ctypes.data_as(I64), hi.ctypes.data_as(I64))
        assert nt > 0, ("expander failed", nt)
        secs = time.time() - t
        # exact coefficients as python ints on the support
        lou = lo.view(np.uint64)
        nz = np.nonzero((lo != 0) | (hi != 0))[0]
        coef = {}
        for m in nz.tolist():
            coef[m] = (int(hi[m]) << 64) + int(lou[m])
        return coef, int(nt), secs

    def to_chi(self, coef):
        """fold monomial coefficients into chi-coordinates; assert chi-isotypy."""
        col_of = self.arr["col_of"]; sgn = self.arr["sgn"]; n_chi = self.arr["n_chi"]
        v = [0] * n_chi; seen = [False] * n_chi
        bad_orbit, bad_dropped = 0, 0
        for m, c in coef.items():
            j = int(col_of[m])
            if j < 0:
                bad_dropped += 1; continue
            val = c * int(sgn[m])
            if seen[j]:
                if v[j] != val: bad_orbit += 1
            else:
                v[j] = val; seen[j] = True
        # every member of a kept orbit whose representative is nonzero must appear in coef
        # (a missing member means coefficient 0 there, i.e. an inconsistency)
        cols_hit = np.array([j for j in range(n_chi) if seen[j] and v[j] != 0], dtype=np.int64)
        members = np.nonzero(np.isin(col_of, cols_hit))[0]
        missing = int(sum(1 for m in members.tolist() if m not in coef))
        return v, dict(orbit_inconsistent=bad_orbit, dropped_nonzero=bad_dropped, missing_members=missing,
                       support=int(sum(1 for x in v if x)), max_abs=int(max((abs(x) for x in v), default=0)))


def E_times_exact(E, v):
    C = E.tocoo(); out = {}
    rows = C.row.tolist(); cols = C.col.tolist(); data = C.data.tolist()
    for i, j, dd in zip(rows, cols, data):
        vj = v[j]
        if vj: out[i] = out.get(i, 0) + int(dd) * vj
    return sum(1 for x in out.values() if x != 0)


# --------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("delta", type=int)
    ap.add_argument("--kgen", type=int, default=16)
    ap.add_argument("--kdet", type=int, default=16)
    ap.add_argument("--k", type=int, default=None, help="force the number of shared tall-column letters")
    ap.add_argument("--kset", default="5,6,7", help="sample k uniformly from this set (ignored if --k given)")
    ap.add_argument("--maxsamples", type=int, default=300)
    ap.add_argument("--tag", default="")
    ap.add_argument("--seed", type=int, default=69)
    ap.add_argument("--no-expand", action="store_true")
    args = ap.parse_args()
    delta = args.delta
    lam = (3 * delta - 17, 7, 2, 2, 2, 2, 2)
    n2, n1 = 5, 3 * delta - 24
    a = a_weyl(lam, delta, N_DEG, {})
    log(f"cell {lam} delta={delta}: a={a}; fillings of lambda'=(7,7,2^{n2},1^{n1})")
    kset = [int(x) for x in args.kset.split(",")]
    rec = dict(lam=list(lam), delta=delta, n=N_DEG, r=R, a=a, n2=n2, n1=n1, k_forced=args.k, kset=kset, seed=args.seed)

    B = get_cell(lam, delta)
    arr, E = B["arr"], B["E"]; n_chi = B["n_chi"]
    rec.update(N_S=int(B["N_S"]), stab=int(B["stab"]), n_chi=int(n_chi), E_rows=int(E.shape[0]), E_nnz=int(E.nnz))
    log(f"  built: N_S={B['N_S']} |Stab|={B['stab']} n_chi={n_chi} E {E.shape} nnz {E.nnz}")

    A, idx, fact, tab = sym_table(N_DEG, R)
    rng = random.Random(args.seed)
    # points: generic (uniform mod p, drawn per prime) and det_3 pencils (integers, shared by both primes)
    gen_pts = {p: [generic_point(N_DEG, R, p, random.Random(args.seed * 1000 + i)) for i in range(args.kgen)] for p in PRIMES}
    det_rng = random.Random(11)
    det_pts = [det_point(N_DEG, R, det_rng, bound=30)[0] for _ in range(args.kdet)]
    msym_gen = {p: [symbols_from_coeffs(cv, N_DEG, R, p) for cv in gen_pts[p]] for p in PRIMES}
    msym_det = {p: [symbols_from_coeffs(cv, N_DEG, R, p) for cv in det_pts] for p in PRIMES}

    # 2. sample fillings, greedy independent set by generic rank at P1
    basis, basis_rows = [], []          # rows: values at generic points (P1)
    samples = 0; t_eval = 0.0; n_eval = 0
    hist = []
    while len(basis) < a and samples < args.maxsamples:
        kk = args.k if args.k is not None else rng.choice(kset)
        F = random_filling(H, N_DEG, delta, n2, n1, rng, k=kk)
        samples += 1
        t = time.time()
        row = [fast_eval_c(F, ms, P1, tab) for ms in msym_gen[P1]]
        t_eval += time.time() - t; n_eval += len(row)
        if all(x == 0 for x in row):
            hist.append((samples, "zero", len(F.shared))); continue
        r_new = rank_mod(basis_rows + [row], P1)
        if r_new > len(basis):
            basis.append(F); basis_rows.append(row)
            hist.append((samples, "new", len(F.shared)))
            log(f"  sample {samples}: rank -> {r_new} (shared k={len(F.shared)})")
        else:
            hist.append((samples, "dep", len(F.shared)))
    rec.update(samples=samples, basis_size=len(basis), generic_rank_P1=len(basis),
               eval_secs_per_point=round(t_eval / max(n_eval, 1), 4), sample_history=hist,
               basis=[F.to_json() for F in basis], basis_shared=[len(F.shared) for F in basis])
    log(f"  generic rank {len(basis)} of a={a} after {samples} samples; {t_eval/max(n_eval,1):.4f}s per evaluation")
    if len(basis) < a:
        log("  SPANNING FAILED (P2 falsified)"); rec["status"] = "SPANNING_FAILED"
        dump(rec, delta, args.tag); return
    # generic rank at P2 too (independence over Q needs only one prime; both reported)
    rows_gen = {p: [[fast_eval_c(F, ms, p, tab) for ms in msym_gen[p]] for F in basis] for p in PRIMES}
    rec["generic_rank"] = {str(p): rank_mod(rows_gen[p], p) for p in PRIMES}

    # 3. det pencils: rank = mult_det, left kernel = U_D
    rows_det = {p: [[fast_eval_c(F, ms, p, tab) for ms in msym_det[p]] for F in basis] for p in PRIMES}
    det_rank = {str(p): rank_mod(rows_det[p], p) for p in PRIMES}
    kern = {p: left_kernel_mod(rows_det[p], p) for p in PRIMES}
    rec["det_rank"] = det_rank
    rec["mult_det"] = {str(p): det_rank[str(p)] for p in PRIMES}
    rec["i_det"] = {str(p): a - det_rank[str(p)] for p in PRIMES}
    rec["kernel_dim"] = {str(p): len(kern[p]) for p in PRIMES}
    rec["kernel_coeffs_modp"] = {str(p): kern[p] for p in PRIMES}
    log(f"  det rank {det_rank} -> mult_det, i_det = {rec['i_det']}; kernel dims {rec['kernel_dim']}")

    if args.no_expand:
        dump(rec, delta, args.tag); return

    # 4. exact expansion of the basis
    X = Expander(B, N_DEG, R)
    chi_vecs = []; exp_info = []
    for i, F in enumerate(basis):
        coef, nt, secs = X.expand(F)
        v, info = X.to_chi(coef)
        info.update(terms=nt, expand_secs=round(secs, 1), monomials=len(coef))
        ez = E_times_exact(E, v)
        info["E_v_nonzero_rows"] = ez
        # evaluator vs expander: coordinate-side evaluation of v at every point used
        agree = True
        for p in PRIMES:
            for cv, val in zip(gen_pts[p], rows_gen[p][i]):
                if chi_dot(chi_eval_rows(arr, cv, p), [x % p for x in v], p) != val % p: agree = False
            for cv, val in zip(det_pts, rows_det[p][i]):
                if chi_dot(chi_eval_rows(arr, cv, p), [x % p for x in v], p) != val % p: agree = False
        info["coord_eval_equals_circuit"] = agree
        chi_vecs.append(v); exp_info.append(info)
        log(f"  filling {i}: {nt} terms in {secs:.0f}s, {len(coef)} monomials -> chi support {info['support']}, "
            f"max|c|={info['max_abs']}, orbit-inconsistent {info['orbit_inconsistent']}, dropped-nonzero {info['dropped_nonzero']}, "
            f"missing {info['missing_members']}, E v nonzero rows {ez}, coord-eval==circuit {agree}")
    rec["expansions"] = exp_info
    rec["chi_rank"] = {str(p): rank_mod([[x % p for x in v] for v in chi_vecs], p) for p in PRIMES}
    log(f"  chi-vector rank {rec['chi_rank']}")
    P1_ok = all(i["orbit_inconsistent"] == 0 and i["dropped_nonzero"] == 0 and i["missing_members"] == 0
                and i["E_v_nonzero_rows"] == 0 and i["coord_eval_equals_circuit"] for i in exp_info)
    rec["P1_semantics"] = P1_ok

    # 5. U_D in chi-coordinates, compare with the banked vector (delta = 12)
    comp = {}
    for p in PRIMES:
        for kv in kern[p]:
            u = [0] * n_chi
            for c, v in zip(kv, chi_vecs):
                if c % p:
                    for j in range(n_chi):
                        if v[j]: u[j] = (u[j] + c * v[j]) % p
            comp.setdefault(str(p), []).append(u)
    banked_path = os.path.join(ROOT, "results", "artefacts", "s69_banked_n3_d12.json")
    if delta == 12 and os.path.exists(banked_path):
        bk = json.load(open(banked_path))["vector_chi_coords"]
        assert len(bk) == n_chi
        res = {}
        for p in PRIMES:
            us = comp[str(p)]
            if len(us) != 1: res[str(p)] = dict(kernel_dim=len(us), proportional=False); continue
            u = us[0]; bkp = [x % p for x in bk]
            j0 = next(j for j in range(n_chi) if bkp[j])
            if u[j0] == 0: res[str(p)] = dict(proportional=False, reason="pivot zero"); continue
            lamb = u[j0] * pow(bkp[j0], -1, p) % p
            mism = sum(1 for j in range(n_chi) if (u[j] - lamb * bkp[j]) % p)
            res[str(p)] = dict(proportional=(mism == 0), mismatches=mism, scalar=lamb,
                               support_u=sum(1 for x in u if x), support_banked=sum(1 for x in bkp if x))
        # over Z: reconstruct the P1 kernel coefficients, form the integer combination
        kv = kern[P1][0] if len(kern[P1]) == 1 else None
        overZ = None
        if kv is not None:
            kint = reconstruct_integer_vector(kv, P1)
            if kint is not None:
                u = [0] * n_chi
                for c, v in zip(kint, chi_vecs):
                    if c:
                        for j in range(n_chi):
                            if v[j]: u[j] += c * v[j]
                g = 0
                for x in u: g = math.gcd(g, abs(x))
                if g > 1: u = [x // g for x in u]
                j0 = next(j for j in range(n_chi) if bk[j])
                sgn = 1 if (u[j0] > 0) == (bk[j0] > 0) else -1
                overZ = dict(kernel_coeffs_Z=kint, equal_up_to_sign=all(sgn * u[j] == bk[j] for j in range(n_chi)),
                             sign=sgn, support=sum(1 for x in u if x), max_abs=max(abs(x) for x in u))
                # E u = 0 and the exact match are what the brief asks for
                overZ["E_u_nonzero_rows"] = E_times_exact(E, u)
        rec["banked_comparison"] = dict(mod_p=res, over_Z=overZ, banked_file=os.path.basename(banked_path))
        log(f"  banked comparison: {res}  over Z: {overZ and {k: overZ[k] for k in ('equal_up_to_sign','sign','support','max_abs','E_u_nonzero_rows')}}")
    rec["status"] = "OK"
    dump(rec, delta, args.tag)
    # artefact: the basis fillings and their chi-expansions (compressed)
    art = dict(lam=list(lam), delta=delta, n=N_DEG, r=R, n_chi=n_chi, prime_note="exact integers",
               chi_coordinates="wk9_s45_build.orbit_setup_arr (house)", basis=[F.to_json() for F in basis],
               chi_vectors=chi_vecs, kernel_coeffs_modp={str(p): kern[p] for p in PRIMES})
    os.makedirs(os.path.join(ROOT, "results", "artefacts"), exist_ok=True)
    with gzip.open(os.path.join(ROOT, "results", "artefacts", f"s69_n3_d{delta}_basis{args.tag}.json.gz"), "wt") as fh:
        json.dump(art, fh)
    log("done")


def dump(rec, delta, tag):
    with open(os.path.join(ROOT, "results", f"s69_n3_d{delta}{tag}.json"), "w") as fh:
        json.dump(rec, fh, indent=1)
    line = {k: rec.get(k) for k in ("lam", "delta", "a", "N_S", "n_chi", "samples", "basis_size", "eval_secs_per_point",
                                   "generic_rank", "det_rank", "i_det", "kernel_dim", "chi_rank", "P1_semantics", "status", "k_forced")}
    line["expand_terms"] = rec["expansions"][0]["terms"] if rec.get("expansions") else None
    line["expand_secs"] = [e["expand_secs"] for e in rec.get("expansions", [])]
    line["chi_support"] = [e["support"] for e in rec.get("expansions", [])]
    with open(os.path.join(ROOT, "results", "s69_sizes.jsonl"), "a") as fh:
        fh.write(json.dumps(line) + "\n")


if __name__ == "__main__":
    main()

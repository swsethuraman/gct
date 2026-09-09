#!/usr/bin/env python3
"""s77 -- the two controls, reproduced from the DETERMINISTIC SSYT basis (the bridge),
not by sampling.

For a cell lambda' = (h,h,2^{n2},1^{n1}):
  1. stream canonical SSYT-fillings (wk12_s77_bridge, order A or B), evaluate at generic
     points through the s69 circuit, greedily keep a filling when it raises the rank, stop
     at a.  DETERMINISTIC: same fillings every run.  Records SSYT scanned and nonzero count.
  2. evaluate the basis at det_n pencils, both primes: rank = mult_det, left kernel = U_D.
  3. (n=3) expand every basis filling EXACTLY into chi-coordinates (wk11_s69_n3.Expander),
     assert chi-isotypy / E v = 0 / evaluator==expander, and compare U_D with the banked
     ideal vector entry for entry, mod p and over Z.

    python3 analysis/wk12_s77_control.py n3 [--order A|B] [--maxscan 4000]
    python3 analysis/wk12_s77_control.py n4 [--order A|B] [--maxscan 4000]
"""
import argparse, json, math, os, random, sys, time
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from wk8_s30_core import P1, P2                                          # noqa: E402
from wk11_s69_circuit import (sym_table, symbols_from_coeffs, generic_point, det_point,  # noqa: E402
                              dp_eval_c, fast_eval_c, rank_mod, left_kernel_mod,
                              reconstruct_integer_vector, PRIMES)
from wk12_s77_bridge import (ssyt_fillings, filling_is_ssyt, columnstrict_fillings,  # noqa: E402
                             interleaved_ssyt)

T0 = time.time()


def log(*a):
    print(f"[{time.time()-T0:8.1f}s]", *a, flush=True)


CELLS = {
    "n3": dict(n=3, r=7, h=7, delta=12, n2=5, n1=12, lam=(19, 7, 2, 2, 2, 2, 2), a=6),
    "n4": dict(n=4, r=9, h=9, delta=12, n2=15, n1=0, lam=(17, 17, 2, 2, 2, 2, 2, 2, 2), a=2),
}


def ev(F, ms, p, tab):
    try:
        return dp_eval_c(F, ms, p, tab) % p
    except Exception:                                                    # noqa: BLE001
        return fast_eval_c(F, ms, p, tab) % p


def deterministic_basis(C, tab, maxscan):
    """greedy basis at P1 generic points from the DETERMINISTIC SSYT (Pieri-chain) stream,
    canonical order A (no RNG).  The SSYT span M_lambda (the bridge); returns basis + scan stats."""
    n, r, h, delta, n2, n1, a = C["n"], C["r"], C["h"], C["delta"], C["n2"], C["n1"], C["a"]
    pts = [symbols_from_coeffs(generic_point(n, r, P1, random.Random(31 * i + 7)), n, r, P1)
           for i in range(a + 6)]
    basis, rows, scanned, nonzero, first_nz = [], [], 0, 0, None
    for F in interleaved_ssyt(h, n, delta, n2, n1, order="A", limit=maxscan):
        assert filling_is_ssyt(F)
        scanned += 1
        row = [ev(F, ms, P1, tab) for ms in pts]
        if any(row):
            nonzero += 1
            if first_nz is None:
                first_nz = scanned
            if rank_mod(rows + [row], P1) > len(rows):
                rows.append(row); basis.append(F)
                log(f"    +filling {len(basis)} (SSYT #{scanned}, k={len(set(F.C1)&set(F.C2))})")
                if len(basis) == a:
                    break
    return basis, dict(scanned=scanned, nonzero=nonzero, first_nonzero=first_nz,
                       basis_size=len(basis), spans=(len(basis) == a))


def run(C, tag, maxscan):
    n, r, h, delta, a = C["n"], C["r"], C["h"], C["delta"], C["a"]
    A, idx, fact, tab = sym_table(n, r)
    log(f"cell {C['lam']} delta={delta}: a={a}; deterministic SSYT (Pieri-chain) basis")
    rec = dict(cell=tag, lam=list(C["lam"]), delta=delta, n=n, r=r, a=a)

    basis, scan = deterministic_basis(C, tab, maxscan)
    rec["scan"] = scan
    log(f"  SSYT basis: generic rank {scan['basis_size']}/{a} spans={scan['spans']}; "
        f"scanned {scan['scanned']} SSYT, {scan['nonzero']} nonzero (first at #{scan['first_nonzero']})")
    if scan["basis_size"] < a:
        rec["status"] = "SPANNING_FAILED"; return rec

    # generic rank at both primes (independence over Q needs one prime)
    gp = {p: [symbols_from_coeffs(generic_point(n, r, p, random.Random(91 * i + 3)), n, r, p)
              for i in range(a + 6)] for p in PRIMES}
    grank = {}
    for p in PRIMES:
        rows = [[ev(F, ms, p, tab) for ms in gp[p]] for F in basis]
        grank[str(p)] = rank_mod(rows, p)
    rec["generic_rank"] = grank
    log(f"  generic rank both primes: {grank}")

    # det pencils: rank = mult_det, kernel = U_D
    det_rng = random.Random(11)
    det_cv = [det_point(n, r, det_rng, bound=30)[0] for _ in range(a + 10)]
    msd = {p: [symbols_from_coeffs(cv, n, r, p) for cv in det_cv] for p in PRIMES}
    rowsd = {p: [[ev(F, ms, p, tab) for ms in msd[p]] for F in basis] for p in PRIMES}
    det_rank = {str(p): rank_mod(rowsd[p], p) for p in PRIMES}
    kern = {p: left_kernel_mod(rowsd[p], p) for p in PRIMES}
    rec["det_rank"] = det_rank
    rec["mult_det"] = det_rank
    rec["i_det"] = {str(p): a - det_rank[str(p)] for p in PRIMES}
    rec["kernel_dim"] = {str(p): len(kern[p]) for p in PRIMES}
    log(f"  mult_det {det_rank}, i_det {rec['i_det']}, kernel dim {rec['kernel_dim']}")
    rec["basis"] = [F.to_json() for F in basis]
    _dump(rec, tag)                                    # checkpoint the fast part

    if n == 3:
        rec["banked"] = expand_and_compare(C, basis, kern, gp, rowsd, det_cv, tab, rec, tag)
    rec["status"] = "OK"
    return rec


def _dump(rec, tag):
    out = os.path.join(ROOT, "results", f"s77_control_{tag}.json")
    json.dump(rec, open(out + ".tmp", "w"), indent=1); os.replace(out + ".tmp", out)


def expand_and_compare(C, basis, kern, gp, rowsd, det_cv, tab, rec, tag):
    """exact expansion + banked-vector comparison (n=3), reusing wk11_s69_n3 machinery."""
    from wk11_s69_n3 import get_cell, Expander, E_times_exact, chi_eval_rows, chi_dot
    n, r, delta = C["n"], C["r"], C["delta"]
    lam = C["lam"]
    B = get_cell(lam, delta)
    arr, E = B["arr"], B["E"]; n_chi = B["n_chi"]
    X = Expander(B, n, r)
    chi_vecs, info = [], []
    for i, F in enumerate(basis):
        coef, nt, secs = X.expand(F)
        v, meta = X.to_chi(coef)
        ez = E_times_exact(E, v)
        agree = True
        # coordinate-side check at the det points (both primes): evaluator == expander
        for p in PRIMES:
            for cv, val in zip(det_cv, rowsd[p][i]):
                if chi_dot(chi_eval_rows(arr, cv, p), [x % p for x in v], p) != val % p:
                    agree = False
        meta.update(terms=nt, expand_secs=round(secs, 1), E_v_nonzero_rows=ez,
                    coord_eval_equals_circuit=agree)
        chi_vecs.append(v); info.append(meta)
        log(f"    expand filling {i}: {nt} terms in {secs:.0f}s, chi support {meta['support']}, "
            f"E v nz {ez}, coord==circuit {agree}")
        rec.setdefault("banked", {})["expansions_partial"] = info
        _dump(rec, tag)
    chi_rank = {str(p): rank_mod([[x % p for x in v] for v in chi_vecs], p) for p in PRIMES}
    out = dict(chi_rank=chi_rank, semantics_ok=all(m["orbit_inconsistent"] == 0 and m["dropped_nonzero"] == 0
               and m["missing_members"] == 0 and m["E_v_nonzero_rows"] == 0 and m["coord_eval_equals_circuit"]
               for m in info), expansions=info)
    # banked comparison
    bpath = os.path.join(ROOT, "results", "artefacts", "s69_banked_n3_d12.json")
    bk = json.load(open(bpath))["vector_chi_coords"]
    assert len(bk) == n_chi
    modp = {}
    for p in PRIMES:
        us = []
        for kv in kern[p]:
            u = [0] * n_chi
            for c, vv in zip(kv, chi_vecs):
                if c % p:
                    for j in range(n_chi):
                        if vv[j]:
                            u[j] = (u[j] + c * vv[j]) % p
            us.append(u)
        if len(us) != 1:
            modp[str(p)] = dict(kernel_dim=len(us), proportional=False); continue
        u = us[0]; bkp = [x % p for x in bk]
        j0 = next(j for j in range(n_chi) if bkp[j])
        lamb = u[j0] * pow(bkp[j0], -1, p) % p if u[j0] else 0
        mism = sum(1 for j in range(n_chi) if (u[j] - lamb * bkp[j]) % p) if lamb else n_chi
        modp[str(p)] = dict(proportional=(mism == 0), mismatches=mism, scalar=lamb,
                            support_u=sum(1 for x in u if x), support_banked=sum(1 for x in bkp if x))
    out["mod_p"] = modp
    # over Z
    overZ = None
    if len(kern[P1]) == 1:
        kint = reconstruct_integer_vector(kern[P1][0], P1)
        if kint is not None:
            u = [0] * n_chi
            for c, vv in zip(kint, chi_vecs):
                if c:
                    for j in range(n_chi):
                        if vv[j]:
                            u[j] += c * vv[j]
            g = 0
            for x in u:
                g = math.gcd(g, abs(x))
            if g > 1:
                u = [x // g for x in u]
            j0 = next(j for j in range(n_chi) if bk[j])
            sgn = 1 if (u[j0] > 0) == (bk[j0] > 0) else -1
            overZ = dict(equal_up_to_sign=all(sgn * u[j] == bk[j] for j in range(n_chi)),
                         sign=sgn, support=sum(1 for x in u if x), max_abs=max(abs(x) for x in u),
                         E_u_nonzero_rows=E_times_exact(E, u))
    out["over_Z"] = overZ
    log(f"  banked: mod_p {modp}  over_Z {overZ}")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cell", choices=["n3", "n4"])
    ap.add_argument("--maxscan", type=int, default=6000)
    args = ap.parse_args()
    rec = run(CELLS[args.cell], args.cell, args.maxscan)
    out = os.path.join(ROOT, "results", f"s77_control_{args.cell}.json")
    json.dump(rec, open(out, "w"), indent=1)
    log(f"wrote {out}  status={rec.get('status')}")


if __name__ == "__main__":
    main()

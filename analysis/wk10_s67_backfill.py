#!/usr/bin/env python3
"""
Session 67, Part A3 -- back-fill session 60's 264 uncertified sparse-route cells
as gct-cert/1 'sparse_nullity' certificates.

Session 60 proved mult_det = a at 419 length-5 cells; 264 ran the sparse
(Wiedemann) route, whose single-prime nonsingularity proofs had no home in the
certificate format.  This script reads results/s60_cells.jsonl and, for every
sparse-route cell whose determinant side is nullity 0 at both house primes,
writes a self-contained sparse_nullity certificate: the cell, the finite field,
the evaluation points reconstructed from the retained seed (as substitution
data, so the certificate is self-contained and checkable), the reproducible
recipe (seeds, levels), and the recorded Wiedemann provenance (both primes'
Berlekamp-Massey degree and f0, the conclusive compression level).

Stopping rule (brief): a cell whose retained data is insufficient is reported as
an uncertified claim, never re-run to manufacture a certificate.  This script
reports any such cell rather than skipping it silently.

usage: python3 analysis/wk10_s67_backfill.py [--out-dir results/certs/s60] [--limit N]
"""
import sys, os, json, gzip, random, re
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..'))

P1, P2 = 2147483647, 2147483629
CONVENTIONS = {"coefficient": "c_alpha(F) = coefficient of s^alpha in F",
               "raising": "E_ij c_alpha = (alpha_i + 1) c_{alpha + e_i - e_j}"}
R = 5


def det_pencils(K, seed, bound):
    """K det_4 pencils as substitution-data points -- EXACTLY the draw of
    wk9_s60_cell.det_pencils (random.Random(seed), K pencils of R integer 4x4
    matrices, entries in [-bound, bound]).  Reconstructed from the retained seed."""
    rnd = random.Random(seed)
    out = []
    for _ in range(K):
        out.append({"type": "det_pencil",
                    "pencil": [[[rnd.randint(-bound, bound) for _ in range(4)] for _ in range(4)]
                               for _ in range(R)]})
    return out


def _bm(note):
    """parse 'BM deg=<d> f0=<f>' out of a diagnostic note."""
    m = re.search(r"BM deg=(\d+) f0=(\d+)", note or "")
    return (int(m.group(1)), int(m.group(2))) if m else (None, None)


def _det_provenance(rec):
    prov = {}
    for p in (P1, P2):
        side = rec['per_prime'][str(p)]['sides']['det']
        concl = next((d for d in side['diag'] if d['status'] == 'NONSINGULAR'), None)
        deg, f0 = _bm(concl['note']) if concl else (None, None)
        prov[str(p)] = {"nullity": side['nullity'], "conclusive_level": (concl['level'] if concl else None),
                        "bm_degree": deg, "f0": f0}
    return prov


def make_cert(rec):
    lam = list(rec['lam']); delta = rec['delta']; a = rec['a']; K = rec['K']
    seed_det = rec['seeds']['det']; bound = rec['bound']
    prov = _det_provenance(rec)
    tag = '_'.join(map(str, lam)) + f'_d{delta}'
    cert = {
        "format": "gct-cert/1", "kind": "sparse_nullity",
        "title": f"mult_det_pencil({tuple(lam)}, {delta}) = a = {a} by the sparse route "
                 f"(session 60), re-derivable; nullity_p([E; ev_det]) = 0",
        "produced_by": "analysis/wk10_s67_backfill.py (session 67) from results/s60_cells.jsonl",
        "cell": {"n": 4, "r": R, "lambda": lam, "delta": delta, "a": a},
        "conventions": dict(CONVENTIONS),
        "field": f"F_{P1}", "variety": "det_pencil", "nullity": 0,
        "points": det_pencils(K, seed_det, bound),
        "recipe": {"K": K, "point_seed": seed_det, "bound": bound,
                   "levels": rec.get('levels'), "wied_seed": rec['seeds'].get('wied', 1),
                   "n_chi": rec['n_chi'], "N_S": rec['N_S']},
        "provenance": {"produced_in": "session 60", "instrument": "sparse [E; ev_det]",
                       "primes": [P1, P2], "per_prime": prov,
                       "note": "NONSINGULAR (nullity 0) at both house primes; a single prime suffices "
                               "(rank_p <= rank_Q), the second is the cross-check"},
        "basis": None,
    }
    return tag, cert


def main(argv):
    out_dir = os.path.join(ROOT, 'results/certs/s60')
    limit = None
    i = 0
    while i < len(argv):
        if argv[i] == '--out-dir': out_dir = argv[i + 1]; i += 2
        elif argv[i] == '--limit': limit = int(argv[i + 1]); i += 2
        else: i += 1
    os.makedirs(out_dir, exist_ok=True)
    rows = [json.loads(l) for l in open(os.path.join(ROOT, 'results/s60_cells.jsonl'))]
    sp = [r for r in rows if r['route'] == 'sparse']
    written, shortfall = [], []
    for rec in sp:
        # required data present, and the determinant side is a clean nullity-0 proof at both primes?
        try:
            ok = (rec['per_prime'][str(P1)]['sides']['det']['nullity'] == 0
                  and rec['per_prime'][str(P2)]['sides']['det']['nullity'] == 0
                  and 'det' in rec['seeds'])
        except (KeyError, TypeError):
            ok = False
        if not ok:
            shortfall.append((tuple(rec['lam']), rec['delta'], "det side not a clean nullity-0 proof at both primes in retained data"))
            continue
        tag, cert = make_cert(rec)
        path = os.path.join(out_dir, f"{tag}_det_sparse_p{P1}.json.gz")
        with gzip.open(path, 'wt', encoding='utf-8') as f:
            json.dump(cert, f, separators=(',', ':'))
        written.append((path, os.path.getsize(path)))
        if limit and len(written) >= limit:
            break
    print(f"sparse-route cells: {len(sp)}")
    print(f"certificates written: {len(written)}  (dir {os.path.relpath(out_dir, ROOT)})")
    print(f"total size: {sum(s for _, s in written)/1024:.0f} KB; largest {max((s for _, s in written), default=0)} bytes")
    if shortfall:
        print(f"SHORTFALL -- uncertified from retained data: {len(shortfall)}")
        for lam, d, why in shortfall:
            print(f"  {lam} d{d}: {why}")
    else:
        print("SHORTFALL: none -- every sparse-route determinant claim is certifiable from the retained data")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

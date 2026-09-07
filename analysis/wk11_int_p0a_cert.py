#!/usr/bin/env python3
"""Emit the gct-cert/1 sparse_nullity certificates for the P0-A permanent result.

nullity_p([E ; ev_per]) = 0 at the n = 3 LMR-family cell certifies
mult_per = a = 6 over Q, which is the rigorous half of D = +1 (batch-11 plan
section 1.1).  The determinant half is LMR's theorem and needs no certificate.

The points are the same 14 per_3 pencils the measurement used, written out as
substitution data so the certificate is self-contained.
"""
import gzip, json, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..'))

P1, P2 = 2147483647, 2147483629
N3, R, LAM, DELTA, A = 3, 7, [19, 7, 2, 2, 2, 2, 2], 12, 6
SEED, BOUND, K = 20260907, 40, A + 8

CONVENTIONS = {
    "coefficient": "c_alpha(F) = coefficient of s^alpha in F",
    "raising": "E_ij c_alpha = (alpha_i + 1) c_{alpha + e_i - e_j}",
}


def pencils():
    """Identical to analysis/wk11_int_p0a.py: random.Random(SEED), r blocks of 3x3."""
    rnd = random.Random(SEED)
    return [[[[rnd.randint(-BOUND, BOUND) for _ in range(3)] for _ in range(3)]
             for _ in range(R)] for _ in range(K)]


def cert(p):
    return {
        "format": "gct-cert/1",
        "kind": "sparse_nullity",
        "title": ("mult_per3 = 6 = a at the n = 3 LMR-family cell (19,7,2^5), delta 12 "
                  "-- the permanent half of D = +1"),
        "produced_by": "integrator, batch 11 pre-batch check P0-A (analysis/wk11_int_p0a.py)",
        "notes": ("The UNPADDED per_3 comparison, not the programme's padded model.  With "
                  "i_det >= 1 supplied by LMR's theorem at this cell, nullity 0 here gives "
                  "D = i_det - i_per = +1 over Q: a multiplicity obstruction (both "
                  "multiplicities are nonzero), certifying that per_3 is not in the closure "
                  "of GL_9 . det_3 -- a separation also visible from dim 59 > 47, so the "
                  "content is the certificate and not the statement."),
        "cell": {"n": N3, "r": R, "lambda": LAM, "delta": DELTA, "a": A},
        "conventions": CONVENTIONS,
        "field": f"F_{p}",
        "variety": "permanent",
        "nullity": 0,
        "points": [{"type": "permanent", "pencil": q} for q in pencils()],
        "recipe": {"K": K, "point_seed": SEED, "bound": BOUND, "levels": "cheap", "wied_seed": 1},
        "provenance": {
            "instrument": "sparse [E; ev_per], nullity_stacked (wk9_s45_cell)",
            "produced_in": "batch 11 pre-batch check P0-A",
            "cross_checked_prime": P2 if p == P1 else P1,
            "n_chi_of_the_reduced_run": 17047,
            "N_S": 1155302,
            "companion_determinant_measurement": "i_det = 1, mult_det = 5, both primes (session 63, reproduced here)",
        },
        "basis": None,
    }


def main():
    out = os.path.join(ROOT, 'results', 'certs')
    os.makedirs(out, exist_ok=True)
    written = []
    for p in (P1, P2):
        path = os.path.join(out, f'19_7_2_2_2_2_2_d12_n3_permanent_p{p}.json.gz')
        with gzip.open(path, 'wt') as fh:
            json.dump(cert(p), fh, indent=1)
        written.append(path)
        print(path, os.path.getsize(path), 'bytes')
    return 0


if __name__ == '__main__':
    sys.exit(main())

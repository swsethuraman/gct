#!/usr/bin/env python3
"""Session 73 -- certificates for one rung, in the declared format gct-cert/1
(tools/verify/FORMAT.md, extended this session to n in {3,4}, the
permanent_pencil family and the sparse_nullity kind).

For the rung delta (record in results/s73_dladder.jsonl, kernels in
results/artefacts/s73_kernels_d<delta>_<seedtag>.json.gz):

  * one `sparse_nullity` certificate per (side, prime): the recorded Wiedemann
    run that closed the nullity count, with the K evaluation pencils as
    substitution data (so the verifier rebuilds det_3 / per_3 of the pencil);
  * one `sparse_nullity` certificate for the full-E solve (variety "none") when
    it was run;
  * one `hwv` certificate (integer coefficients, modulus null) per exhibited
    kernel vector, expanded from chi-coordinates to the monomial basis, claiming
    annihilation by the raising operators over Z, vanishing at the recorded
    pencils of its own family, nonvanishing at the recorded pencils of the other
    family, and the same at fresh points from the pre-registered seed.

usage: python3 analysis/wk11_s73_certs.py <delta> [--seedtag primary] [--fresh-count 6]
"""
import gzip
import json
import os
import re
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from wk11_s73_lib import (ROOT, ART, CERTS, N_DEG, R, P1, P2, SESSION_SEED, log, lam_of, a_two_ways,   # noqa: E402
                          load_build, expand_terms_int)

CONVENTIONS = {"coefficient": "c_alpha(F) = coefficient of s^alpha in F",
               "raising": "E_ij c_alpha = (alpha_i + 1) c_{alpha + e_i - e_j}"}
VARIETY = dict(det="det_pencil", per="permanent_pencil")
TAG = dict(det="det", per="permanent")


def latest_record(delta, seedtag):
    rec = None
    with open(os.path.join(ROOT, 'results', 's73_dladder.jsonl')) as fh:
        for ln in fh:
            r = json.loads(ln)
            if r['delta'] == delta and r.get('seedtag') == seedtag and 'sides' in r:
                rec = r
    assert rec is not None, ("no record", delta, seedtag)
    return rec


def closing_run(diag):
    """the wied run that closed the count: the last NONSINGULAR entry."""
    last = None
    for d in diag:
        if d['status'] == 'NONSINGULAR':
            last = d
    assert last is not None, "no NONSINGULAR closing run in the diagnostics"
    m = re.search(r"BM deg=(\d+) f0=(\d+)", last['note'])
    k = re.search(r" k=(\d+) ", last['note'])
    return dict(level=list(LEVEL_OF[last['level']]), seed0=1, wied_seed=int(last['seed']),
                k_extra=int(k.group(1)), bm_degree=int(m.group(1)), bm_f0=int(m.group(2)),
                rows=int(last['rows']), nnz=int(last['nnz']), log=last['note'])


LEVEL_OF = {0: (12, 2), 1: (0, 1)}      # levels 's42': (12,2) then the uncompressed matrix (sample None -> 0)


def write(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if path.endswith('.gz'):
        with gzip.open(path, 'wt', encoding='utf-8') as fh:
            json.dump(obj, fh, separators=(',', ':'))
    else:
        with open(path, 'w', encoding='utf-8') as fh:
            json.dump(obj, fh, indent=1)
    return os.path.getsize(path)


def main(delta, seedtag='primary', fresh_count=6):
    lam = lam_of(delta)
    a = a_two_ways(lam, delta)
    rec = latest_record(delta, seedtag)
    with gzip.open(os.path.join(ART, f"s73_kernels_d{delta}_{seedtag}.json.gz"), 'rt', encoding='utf-8') as fh:
        K = json.load(fh)
    lamstr = '_'.join(map(str, lam))
    cell = {"n": N_DEG, "r": R, "lambda": list(lam), "delta": int(delta), "a": int(a)}
    red = {"N_S": rec['N_S'], "n_chi": rec['n_chi'], "stab": rec['stab'], "nrows_E": rec['nrows_E'],
           "nnz_E": rec['nnz_E'],
           "note": "chi_lambda-isotypic reduction of the weight-lambda monomial space (docs/stabiliser_reduction.md), "
                   "built by analysis/wk9_s45_build.build_cell(n=3)"}
    arr = None
    written = []
    # hwv certificates first (their names go into the sparse_nullity records)
    hwv_names = {}
    for sd in ('det', 'per'):
        ints = K['U'].get(sd, {}).get('int', [])
        hwv_names[sd] = []
        if not ints:
            continue
        if arr is None:
            arr, _ = load_build(delta)
        other = 'per' if sd == 'det' else 'det'
        for vi, vint in enumerate(ints):
            terms = expand_terms_int(arr, vint)
            name = f"s73_{lamstr}_d{delta}_n3_{TAG[sd]}_kernel_vec{vi}_int.json.gz"
            cert = {"format": "gct-cert/1", "kind": "hwv",
                    "title": f"s73: integer highest-weight vector of weight {lam} (delta={delta}, n=3, r=7) in the kernel of "
                             f"the {VARIETY[sd]} evaluation pairing: an element of I({'D' if sd == 'det' else 'P'}_7)^HWV "
                             f"{'not vanishing on P_7' if sd == 'det' else 'not vanishing on D_7'}",
                    "produced_by": "analysis/wk11_s73_certs.py (session 73)",
                    "notes": f"chi-coordinate support {sum(1 for x in vint if x)} of n_chi = {rec['n_chi']}; {len(terms)} monomial terms; "
                             f"reconstructed over Z from the mod-{P1} kernel vector, E v = 0 checked over Z by the producer; "
                             f"the verifier re-derives everything here from scratch (raising operators over Z, forms rebuilt from the pencils)",
                    "cell": cell, "conventions": dict(CONVENTIONS), "modulus": None,
                    "vectors": [{"terms": terms}],
                    "claims": {"independent": True,
                               "vanishes_at": [{"type": VARIETY[sd], "pencil": pen} for pen in K['pencils'][sd]],
                               "nonvanishing_at": [{"type": VARIETY[other], "pencil": pen} for pen in K['pencils'][other]],
                               "fresh_points": {"seed": SESSION_SEED, "count": int(fresh_count),
                                                "vanishes_on": [VARIETY[sd]],
                                                "nonvanishing_on": [VARIETY[other], "generic"]}}}
            sz = write(os.path.join(CERTS, name), cert)
            hwv_names[sd].append(name)
            written.append((name, sz))
            log(f"  wrote {name} ({sz/1e6:.2f} MB, {len(terms)} terms)")
    # sparse_nullity certificates
    for sd in ('det', 'per'):
        if sd not in rec['sides'] or 'nullity' not in rec['sides'][sd]:
            continue
        side = rec['sides'][sd]
        for pstr, pp in side['per_prime'].items():
            p = int(pstr)
            run = closing_run(pp['diag'])
            run['secs'] = pp['secs']
            k = side['nullity']
            name = f"s73_{lamstr}_d{delta}_n3_{TAG[sd]}_p{p}_sparse_nullity.json"
            cert = {"format": "gct-cert/1", "kind": "sparse_nullity",
                    "title": f"s73: nullity_p([E; ev_{sd}]) = {k} at p = {p} for lambda = {lam}, delta = {delta} (n = 3, r = 7): "
                             f"mult_{sd} = {a - k}" + (" = a, proved over Q" if k == 0 else f" (>= {a-k} proved, = {a-k} measured)"),
                    "produced_by": "analysis/wk11_s73_cell.py via wk9_s45_cell.nullity_stacked (session 73)",
                    "notes": f"K = {side['K']} pencils from random.Random({side['seed']}), entries in [-40, 40]; levels s42 "
                             f"((12,2) then uncompressed), Wiedemann seeds from seed0 = 1; the ev rows are pinned through "
                             f"every level.  Level recorded as [sample_factor, group]; [0, 1] = the uncompressed E.",
                    "cell": cell, "conventions": dict(CONVENTIONS), "prime": p, "variety": VARIETY[sd],
                    "points": [{"type": VARIETY[sd], "pencil": pen} for pen in K['pencils'][sd]],
                    "reduction": red, "run": run, "claim": {"nullity": int(k), "mult": int(a - k)}}
            if k > 0:
                cert["kernel_certificates"] = list(hwv_names[sd])
            sz = write(os.path.join(CERTS, name), cert)
            written.append((name, sz))
            log(f"  wrote {name}")
    if 'fullE' in rec and rec['fullE'].get('equals_a'):
        fe = rec['fullE']
        run = closing_run(fe['diag']); run['secs'] = fe['secs']
        name = f"s73_{lamstr}_d{delta}_n3_fullE_p{P1}_sparse_nullity.json"
        cert = {"format": "gct-cert/1", "kind": "sparse_nullity",
                "title": f"s73: nullity_p(E) = {fe['nullity']} = a at p = {P1} for lambda = {lam}, delta = {delta} (n = 3, r = 7): "
                         f"the raising operators on V_chi have kernel of the plethysm dimension",
                "produced_by": "analysis/wk11_s73_cell.py via wk9_s45_cell.nullity_stacked (session 73)",
                "notes": "the kernel of E alone (no evaluation rows); its a vectors are the explicit basis of M_delta "
                         "banked in results/artefacts/s73_M_basis_d<delta>_p1.npz (mod P1)",
                "cell": cell, "conventions": dict(CONVENTIONS), "prime": P1, "variety": "none", "points": [],
                "reduction": red, "run": run, "claim": {"nullity": int(fe['nullity']), "mult": int(a - fe['nullity'])}}
        sz = write(os.path.join(CERTS, name), cert)
        written.append((name, sz))
        log(f"  wrote {name}")
    return written


if __name__ == '__main__':
    delta = int(sys.argv[1])
    seedtag = sys.argv[sys.argv.index('--seedtag') + 1] if '--seedtag' in sys.argv else 'primary'
    fc = int(sys.argv[sys.argv.index('--fresh-count') + 1]) if '--fresh-count' in sys.argv else 6
    w = main(delta, seedtag, fc)
    log(f"{len(w)} certificate(s) written")

#!/usr/bin/env python3
"""Session 73 -- cross-checks on the exhibited delta = 12 kernel line U_D(12).

  1. this session's integer vector v_12 (reconstructed from the P1 kernel of
     [E; ev_det] at the pre-registered seed family) against session 62's
     exhibited integer vector (results/s62_n3_vec_d12.json of the s62 bundle,
     same chi-coordinates of wk9_s45_build): the two primitive vectors must
     coincide up to sign -- two sessions, two drivers, two evaluation families,
     one line;
  2. the same against the vector of the second (verification-protocol) family
     when it has been run (--seedtag second);
  3. the u-free part of v_12 (birth at delta = 12) and its evaluation at fresh
     per_3 pencils over Z (the orientation U_D ⊄ U_P, exactly).

usage: python3 analysis/wk11_s73_crosscheck.py [--s62 path] [--out results/s73_crosscheck.json]
"""
import gzip
import json
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from wk11_s73_lib import ROOT, ART, P1, P2, SEEDS, FORMS, log, load_build, ufree_columns, eval_exact_many, pencils, coeffs_of  # noqa: E402


def primitive(v):
    g = 0
    for x in v:
        g = math.gcd(g, abs(x))
    v = [x // g for x in v] if g > 1 else list(v)
    for x in v:
        if x:
            return v if x > 0 else [-y for y in v]
    return v


def load_kernels(delta, seedtag):
    p = os.path.join(ART, f"s73_kernels_d{delta}_{seedtag}.json.gz")
    if not os.path.exists(p):
        return None
    with gzip.open(p, 'rt', encoding='utf-8') as fh:
        return json.load(fh)


def main(s62_path, outp):
    out = {}
    K1 = load_kernels(12, 'primary')
    v1 = K1['U']['det']['int'][0]
    out['primary'] = dict(support=sum(1 for x in v1 if x), max_abs=max(abs(x) for x in v1))
    if s62_path and os.path.exists(s62_path):
        v62 = json.load(open(s62_path))['vector_chi_coords']
        out['s62'] = dict(support=sum(1 for x in v62 if x), max_abs=max(abs(x) for x in v62),
                          equal_up_to_sign=(primitive(v62) == primitive(v1)))
        log(f"v_12 (s73 primary) vs s62's exhibited vector: equal up to sign = {out['s62']['equal_up_to_sign']}")
    K2 = load_kernels(12, 'second')
    if K2 is not None and K2['U'].get('det', {}).get('int'):
        v2 = K2['U']['det']['int'][0]
        out['second'] = dict(support=sum(1 for x in v2 if x), max_abs=max(abs(x) for x in v2),
                             equal_up_to_sign=(primitive(v2) == primitive(v1)))
        log(f"v_12 (primary) vs second family: equal up to sign = {out['second']['equal_up_to_sign']}")
    arr, E = load_build(12)
    uf = ufree_columns(arr)
    vu = np.array(v1, dtype=object)[uf]
    out['ufree'] = dict(n_ufree_columns=int(len(uf)), ufree_support=int(sum(1 for x in vu if x)),
                        note="nonzero u-free part <=> v_12 not divisible by c_{(3,0,...,0)} <=> not transported from delta = 11 (born at 12)")
    pens = pencils(12, SEEDS['fresh_per'])
    vals = eval_exact_many(arr, v1, [coeffs_of(FORMS['per'], pen) for pen in pens])
    out['fresh_per_values_over_Z'] = dict(count=len(vals), nonzero=[x != 0 for x in vals],
                                          digits=[len(str(abs(x))) for x in vals])
    log(f"u-free support of v_12: {out['ufree']['ufree_support']} of {len(uf)}; fresh per_3 values nonzero: {out['fresh_per_values_over_Z']['nonzero']}")
    with open(outp, 'w') as fh:
        json.dump(out, fh, indent=1)
    return out


if __name__ == '__main__':
    a = sys.argv[1:]
    s62 = a[a.index('--s62') + 1] if '--s62' in a else '/home/claude/s73/s62/s62_n3_vec_d12.json'
    outp = a[a.index('--out') + 1] if '--out' in a else os.path.join(ROOT, 'results', 's73_crosscheck.json')
    main(s62, outp)

#!/usr/bin/env python3
"""
Session 42 -- demonstration (not part of the deliverable table): the same sparse
nonsingularity certificate proves mult_det = a.

mult_det(lam, delta) = rank of the evaluation pairing on HWV_lam at K >= a det
points = a - dim(HWV_lam ∩ {h : h(pt_1) = ... = h(pt_K) = 0}).  With E the
raising operators on V_chi and Ev the K evaluation rows in chi-coordinates
(wk9_s36_stabred.point_rows, the house det points det_4(sum s_i A_i)),

    HWV_lam ∩ ann(points) = ker [E; Ev],

so nullity_p([E; Ev]) = 0 PROVES mult_det = a over Q (rank_p <= rank_Q), by one
Wiedemann certificate on a sparse matrix, no kernel, no dense elimination.
(nullity k > 0 gives mult_det >= a - k proved, = a - k measured, as usual; a
measured det-side bite would then get the full sceptical protocol.)

usage: python3 wk9_s42_detcert.py delta lam1 lam2 ...
"""
import sys, os, time, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from wk9_s42_redengine import build
from wk9_s42_sparse import nullity_sparse, log
from wk9_s36_stabred import point_rows, DET4, N_DET, P1, P2
from wk8_s30_pleth import a_of

def det_certificate(lam, delta, primes=(P1, P2), seed=11, bound=40):
    t0 = time.time()
    B = build(lam, delta, verbose=False)
    a = a_of(lam, delta, 4, len(lam))
    K = a + 8
    out = dict(lam=list(lam), delta=delta, a=a, n_chi=B['n_chi'], K=K, primes={})
    for p in primes:
        ev = point_rows(DET4, N_DET, 4, len(lam), B['basis'], B['vecs'], K, seed, bound, p)
        rows = list(B['rows']) + [{j: v for j, v in enumerate(e) if v} for e in ev]
        t1 = time.time()
        k, _ = nullity_sparse(rows, B['n_chi'], p, tag=f"det{'_'.join(map(str, lam))}d{delta}", verbose=False)
        out['primes'][str(p)] = dict(nullity=k, secs=round(time.time() - t1, 1))
        log(f"  {lam} d{delta} p={p}: nullity_p([E; Ev]) = {k} -> mult_det >= {a - k}" + (" = a PROVED" if k == 0 else "") + f" ({time.time()-t1:.0f}s)")
    ks = {v['nullity'] for v in out['primes'].values()}
    assert len(ks) == 1
    k = ks.pop()
    out['mult_det'] = a - k
    out['status'] = 'proved (nullity 0)' if k == 0 else f'measured (nullity {k})'
    out['secs'] = round(time.time() - t0, 1)
    return out

if __name__ == '__main__':
    delta = int(sys.argv[1]); lam = tuple(int(x) for x in sys.argv[2:])
    res = det_certificate(lam, delta)
    print(json.dumps(res))
    with open(os.path.join(HERE, '..', 'results', 's42_detcert.jsonl'), 'a') as f: f.write(json.dumps(res) + "\n")

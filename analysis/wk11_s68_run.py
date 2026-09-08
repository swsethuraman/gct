#!/usr/bin/env python3
"""
Session 68 -- validate the ladder algorithm on reachable ladders, both primes,
with the full three-part rung certificate, cost/support measurements and the
i_det/i_pad by-products.  Emits results/s68_rungs.jsonl and saves the seed + rung
bases as artefacts under results/artefacts/.

Ladders (n=4), tail fixed, lam_delta = (4 delta - |t|, t):
  L1  tail (6,4,2)   ell=4  |Stab|=1  -- multi-dim seed a=3, births 8,7,4
  L2  tail (4,4,2)   ell=4  |Stab|=2  -- births 1,2,2,1,0, nontrivial stabiliser
"""
import os, sys, time, json, resource
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
os.environ.setdefault('WIED_BIN', '/home/claude/wied68')
os.environ.setdefault('WIED_WORK', '/home/claude/s68/work')
import numpy as np
from wk11_s68_ladder import (build_one, certify_rung, transport_matrix, deflate,
                             i_of, support_frac, support_size, nmod_to_np)
from wk9_s36_stabred import P1, P2

OUT = '/home/claude/gct/results'
ART = os.path.join(OUT, 'artefacts')
os.makedirs(ART, exist_ok=True)

LADDERS = {
    'L1': dict(tail=(6, 4, 2), ell=4, deltas=list(range(5, 9))),   # a=3,11,18,22
    'L2': dict(tail=(4, 4, 2), ell=4, deltas=list(range(4, 9))),   # a=1,3,5,6,6
}

def rss_gb():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024.0 * 1024.0)

def run_ladder(name, spec, primes=(P1, P2), save_art=False):
    tail = spec['tail']; deltas = spec['deltas']
    rows = []
    # cache builds per (delta) reused across primes via rebuild (cheap)
    per_prime = {}
    for p in primes:
        rng = np.random.default_rng(20240908 + p % 100000)
        prev = None
        seq = []
        for d in deltas:
            l1 = 4 * d - sum(tail); lam = (l1,) + tail
            t0 = time.time()
            cur = build_one(lam, d, p, verbose=False)
            build_t = time.time() - t0
            t1 = time.time()
            if prev is None:
                cert = certify_rung(None, cur, p, rng); mats = None
            else:
                cert, mats = certify_rung(prev, cur, p, rng)
            cert_t = time.time() - t1
            cert['build_secs'] = round(build_t, 2)
            cert['cert_secs'] = round(cert_t, 2)
            cert['hwm_gb'] = round(rss_gb(), 3)
            # by-products
            try:
                cert['i_det'] = i_of(cur, 'det', p)['i']
                cert['i_pad'] = i_of(cur, 'pad', p)['i']
            except Exception as e:
                cert['i_det'] = cert['i_pad'] = None
                cert['i_err'] = repr(e)[:120]
            seq.append(cert)
            if save_art and p == primes[0]:
                _save_artefact(name, cur, prev, mats)
            prev = cur
        per_prime[p] = seq
    # merge across primes: assert agreement on the load-bearing integers
    merged = []
    for i, d in enumerate(deltas):
        a = [per_prime[p][i] for p in primes]
        base = dict(a[0])
        base['ladder'] = name; base['tail'] = list(tail)
        for key in ('a', 'birth', 'birth_expected'):
            vals = set(x.get(key) for x in a)
            assert len(vals) == 1, ("primes disagree", name, d, key, vals)
        base['primes'] = list(primes)
        base['ok_all_primes'] = all(x.get('ok') for x in a)
        base['i_det_primes'] = {str(p): per_prime[p][i].get('i_det') for p in primes}
        base['i_pad_primes'] = {str(p): per_prime[p][i].get('i_pad') for p in primes}
        # keep the per-prime certificate booleans
        base['cert_by_prime'] = {str(p): {k: per_prime[p][i][k] for k in per_prime[p][i]
                                          if k.startswith('cert_') or k in ('transport_rank','transported_rank','sum_rank','span_equals_kernel')}
                                 for p in primes}
        merged.append(base)
    return merged

def _save_artefact(name, cur, prev, mats):
    """Save the chi-coordinate bases (mod P1) for this cell as .npz."""
    d = cur['delta']; lam = cur['lam']
    K = nmod_to_np(cur['K']).astype(np.int64)          # n_chi x a
    payload = dict(lam=np.array(lam), delta=d, p=cur['p'], n_chi=cur['n_chi'],
                   a=cur['a'], N_S=cur['N_S'], stab=cur['stab'], kernel=K)
    if mats is not None:
        payload['transported'] = nmod_to_np(mats['JK']).astype(np.int64)   # n_chi x a_prev
        payload['births'] = nmod_to_np(mats['Bdef']).astype(np.int64)      # n_chi x birth
    fn = os.path.join(ART, f's68_{name}_d{d}.npz')
    np.savez_compressed(fn, **payload)

def main():
    allrows = []
    for name, spec in LADDERS.items():
        log = f"=== ladder {name} tail={spec['tail']} ==="
        print(log, file=sys.stderr, flush=True)
        rows = run_ladder(name, spec, save_art=(name == 'L1'))
        allrows.extend(rows)
        for r in rows:
            print("  d=%d lam=%s a=%d %s birth=%s/%s ok=%s supp=%.3f i_det=%s i_pad=%s (build %.1fs cert %.1fs hwm %.2fGB)"
                  % (r['delta'], r['lam'], r['a'], r['role'], r['birth'], r.get('birth_expected', '-'),
                     r['ok_all_primes'], r['support_frac'], r['i_det'], r['i_pad'],
                     r['build_secs'], r['cert_secs'], r['hwm_gb']), file=sys.stderr, flush=True)
    with open(os.path.join(OUT, 's68_rungs.jsonl'), 'w') as f:
        for r in allrows:
            f.write(json.dumps(r) + "\n")
    print("WROTE", os.path.join(OUT, 's68_rungs.jsonl'), len(allrows), "rows", file=sys.stderr)

if __name__ == '__main__':
    main()

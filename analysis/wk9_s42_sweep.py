#!/usr/bin/env python3
"""
Session 42 -- the sweep: mult_red at every reachable cell of the census, by
the sparse certificate route (both primes), banked one JSON line per cell.

usage: python3 wk9_s42_sweep.py --census results/s42_census.json --out results/s42_cells_A.jsonl
          [--deltas 7,8] [--ells 6,7] [--nchi-cap 150000] [--ns-cap 8000000] [--nred-cap 120000]
          [--split k/m] [--hours H] [--done results/s42_cells_A.jsonl,results/s42_cells_B.jsonl]

--split k/m : this worker takes the cells with rank index = k mod m in the
              ascending-nchi_lb order (static split; workers never share a cell).
Cells whose build shows n_red above --nred-cap are banked as status 'beyond'
(with the exact n_chi, n_red) and not measured.
"""
import sys, os, time, json, pickle
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from wk9_s42_redengine import build
from wk9_s42_sparse import nullity_sparse, log
from wk8_s30_pleth import a_of
from wk9_s36_stabred import P1, P2, monomials

def main():
    args = sys.argv[1:]
    opt = dict(census=None, out=None, deltas=None, ells=None, nchi_cap=150000, ns_cap=8000000,
               nred_cap=120000, split=(0, 1), hours=1e9, done='')
    i = 0
    while i < len(args):
        k = args[i]
        if k == '--census': opt['census'] = args[i + 1]; i += 2
        elif k == '--out': opt['out'] = args[i + 1]; i += 2
        elif k == '--deltas': opt['deltas'] = [int(x) for x in args[i + 1].split(',')]; i += 2
        elif k == '--ells': opt['ells'] = [int(x) for x in args[i + 1].split(',')]; i += 2
        elif k == '--nchi-cap': opt['nchi_cap'] = int(args[i + 1]); i += 2
        elif k == '--ns-cap': opt['ns_cap'] = int(args[i + 1]); i += 2
        elif k == '--nred-cap': opt['nred_cap'] = int(args[i + 1]); i += 2
        elif k == '--split': a, b = args[i + 1].split('/'); opt['split'] = (int(a), int(b)); i += 2
        elif k == '--hours': opt['hours'] = float(args[i + 1]); i += 2
        elif k == '--done': opt['done'] = args[i + 1]; i += 2
        else: raise SystemExit("unknown arg " + k)
    cells = json.load(open(opt['census']))
    if opt['deltas']: cells = [c for c in cells if c['delta'] in opt['deltas']]
    if opt['ells']: cells = [c for c in cells if c['ell'] in opt['ells']]
    cells = [c for c in cells if c['nchi_lb'] <= opt['nchi_cap'] and c['N_S'] <= opt['ns_cap']]
    cells.sort(key=lambda c: (c['nchi_lb'], c['N_S']))
    k, m = opt['split']
    cells = [c for j, c in enumerate(cells) if j % m == k]
    done = set()
    for fn in ([opt['out']] + [x for x in opt['done'].split(',') if x]):
        if fn and os.path.exists(fn):
            for line in open(fn):
                d = json.loads(line); done.add((tuple(d['lam']), d['delta']))
    log(f"sweep: {len(cells)} cells in this worker's share, {len([c for c in cells if (tuple(c['lam']), c['delta']) not in done])} to do")
    t_start = time.time()
    for c in cells:
        lam, delta = tuple(c['lam']), c['delta']
        if (lam, delta) in done: continue
        if time.time() - t_start > opt['hours'] * 3600: log("time budget reached"); break
        t0 = time.time()
        a = c['a']
        assert a == a_of(lam, delta, 4, len(lam))
        B = build(lam, delta, verbose=False, want_vecs=False)
        rec = dict(lam=list(lam), delta=delta, ell=len(lam), a=a, h_pad=c['h_pad'], N_S=B['N_S'], stab=B['stab'],
                   n_chi=B['n_chi'], n_red=B['n_red'], nrows_red=int(B['E_red'].shape[0]),
                   nnz_red=int(B['E_red'].nnz), cons=B['cons'], build_secs=round(B['build_secs'], 1))
        if B['n_red'] > opt['nred_cap']:
            rec.update(status='beyond', secs=round(time.time() - t0, 1))
            log(f"beyond: {lam} d{delta}: n_chi {B['n_chi']} n_red {B['n_red']} > cap")
        else:
            nuls, kerns = {}, {}
            try:
                for p in (P1, P2):
                    t1 = time.time()
                    kk, kern = nullity_sparse(B['E_red'], B['n_red'], p, want_kern=True,
                                              tag=f"s{'_'.join(map(str, lam))}d{delta}", verbose=False)
                    nuls[str(p)] = dict(nullity=kk, secs=round(time.time() - t1, 1))
                    kerns[p] = kern
                    log(f"  {lam} d{delta} p={p}: nullity {kk} ({time.time()-t1:.0f}s)")
                    if kk > a:
                        raise AssertionError(("nullity_p(E_red) > a", lam, delta, p, kk, a))
                ks = {v['nullity'] for v in nuls.values()}
                assert len(ks) == 1, ("primes disagree", lam, delta, nuls)
                kk = ks.pop()
                rec.update(primes=nuls, nullity=kk, mult_red=a - kk,
                           status=('proved' if kk == 0 else 'measured'), secs=round(time.time() - t0, 1))
                if kk > 0:
                    os.makedirs('/root/s42/kern', exist_ok=True)
                    pickle.dump(dict(rec=rec, kern={p: kerns[p] for p in (P1, P2)}, red=B['red'], vecs_len=B['n_chi']),
                                open(f"/root/s42/kern/{'_'.join(map(str, lam))}_d{delta}.pkl", 'wb'))
            except Exception as e:
                rec.update(status='failed', error=repr(e)[:300], secs=round(time.time() - t0, 1))
                log(f"FAILED {lam} d{delta}: {e!r}")
        with open(opt['out'], 'a') as f: f.write(json.dumps(rec) + "\n")
        log(f"banked {lam} d{delta}: {rec['status']} mult_red={rec.get('mult_red')} a={a} h_pad={c['h_pad']} n_chi={rec['n_chi']} n_red={rec['n_red']} ({rec['secs']}s)")
        monomials.cache_clear()
    log("sweep done")

if __name__ == '__main__':
    main()

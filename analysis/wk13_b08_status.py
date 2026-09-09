#!/usr/bin/env python3
"""
B13-08 -- merge the lane files into one record and one status document.

    results/b13_08/per6_d10_lane<k>.jsonl  ->  results/b13_08/per6_d10.jsonl   (one record per weight, by rank)
    results/b13_08/failed_lane<k>.jsonl    ->  results/b13_08/status.json      (reached / not reached, priced)
                                               results/b13_08/per6_d10.md      (the table for the report)

Prints the summary: reached count, sum a, the completed prefix, drops, prime disagreements,
and the not-reached weights priced by N_S*delta under session 79's hybrid cost model.
"""
import os, sys, json, glob, collections

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..'))
RES = os.path.join(ROOT, 'results', 'b13_08')
DELTA = 10


def read_jsonl(path):
    out = []
    if os.path.exists(path):
        for ln in open(path):
            ln = ln.strip()
            if ln:
                try: out.append(json.loads(ln))
                except Exception: pass
    return out


def main():
    Q = json.load(open(os.path.join(RES, 'queue.json')))
    queue = Q['queue']; byrank = {w['rank']: w for w in queue}; rank_of = {tuple(w['mu']): w['rank'] for w in queue}
    recs = {}
    for f in sorted(glob.glob(os.path.join(RES, 'per6_d10_lane*.jsonl'))):
        for r in read_jsonl(f):
            mu = tuple(r['mu'])
            if r.get('delta') != DELTA or mu not in rank_of: continue
            r['rank'] = rank_of[mu]; r['lane_file'] = os.path.basename(f)
            r.setdefault('engine', 'analysis/wk12_s79_per6.py (unchanged)')
            if mu not in recs or (recs[mu].get('mult') is None and r.get('mult') is not None): recs[mu] = r
    fails = collections.defaultdict(list)
    for f in sorted(glob.glob(os.path.join(RES, 'failed_lane*.jsonl'))):
        for r in read_jsonl(f): fails[tuple(r['mu'])].append(r)
    with open(os.path.join(RES, 'per6_d10.jsonl'), 'w') as f:
        for mu in sorted(recs, key=lambda m: rank_of[m]): f.write(json.dumps(recs[mu]) + "\n")
    reached, not_reached = [], []
    for w in queue:
        mu = tuple(w['mu'])
        if mu in recs and recs[mu].get('mult') is not None:
            r = recs[mu]
            reached.append(dict(rank=w['rank'], mu=w['mu'], a=w['a'], N_S=w['N_S'], stab=r.get('stab'), n_chi=r.get('n_chi'), nrows=r.get('nrows'),
                                nnz=r.get('nnz'), mult=r['mult'], units=r['units'], primes_agree=r.get('primes_agree'), status=r.get('status'),
                                secs=r.get('secs'), build_secs=r.get('build_secs'), hwm_gb=r.get('hwm_gb'), engine=r['engine'],
                                nU={p: r['per_prime'][p]['hybrid']['nU'] for p in r.get('per_prime', {})},
                                certs=r.get('certs', [])))
        else:
            fl = fails.get(mu, [])
            price = dict(NS_delta=w['NS_delta'], build_model_secs=round(2.1e-6 * w['NS_delta'], 1),
                         rows_model_secs=round(2 * 2.7e-8 * (w['a'] + 8) * w['NS_delta'], 1))
            not_reached.append(dict(rank=w['rank'], mu=w['mu'], a=w['a'], N_S=w['N_S'], pred_peak_gb=w['pred_peak_gb'],
                                    attempts=[dict(engine=x['engine'], reason=x['reason'], rc=x['rc'], wall=x['wall'], ulimit_kb=x.get('ulimit_kb')) for x in fl],
                                    reason=(fl[-1]['reason'] if fl else 'not attempted'), price=price))
    # the completed prefix in cost order
    prefix = 0
    for w in queue:
        if tuple(w['mu']) in recs and recs[tuple(w['mu'])].get('mult') is not None: prefix += 1
        else: break
    drops = [r for r in reached if r['units'] != 0]
    disagree = [r for r in reached if not r['primes_agree']]
    st = dict(board_numbering='batch13', session='B13-08', delta=DELTA, queue=len(queue), reached=len(reached), not_reached=len(not_reached),
              sum_a_reached=sum(r['a'] for r in reached), sum_a_not_reached=sum(r['a'] for r in not_reached),
              completed_prefix_in_cost_order=prefix, prefix_last_rank=(queue[prefix - 1]['rank'] if prefix else None),
              full_rank_at_both_primes=sum(1 for r in reached if r['units'] == 0 and r['primes_agree']),
              drops=drops, primes_disagree=disagree,
              max_secs=max((r['secs'] or 0) for r in reached) if reached else None,
              total_secs=round(sum((r['secs'] or 0) for r in reached), 1), max_hwm_gb=max((r['hwm_gb'] or 0) for r in reached) if reached else None,
              lean_engine_weights=[r['rank'] for r in reached if 'lean' in r['engine']],
              by_bucket={'N_S<5e6': dict(reached=sum(1 for r in reached if r['N_S'] < 5e6), not_reached=sum(1 for r in not_reached if r['N_S'] < 5e6)),
                         '5e6<=N_S<1e7': dict(reached=sum(1 for r in reached if r['N_S'] >= 5e6), not_reached=sum(1 for r in not_reached if r['N_S'] >= 5e6))},
              not_reached_list=not_reached, reached_list=reached)
    json.dump(st, open(os.path.join(RES, 'status.json'), 'w'), indent=1)
    with open(os.path.join(RES, 'per6_d10.md'), 'w') as f:
        f.write(f"# `I(D_6^{{per_3}})_10` on the cubic side, the B13-08 remainder\n\n")
        f.write(f"{len(reached)} of the 95 frozen weights reached (`results/b13_08/queue.json`, session 79's cost order), points "
                f"`per_3(Σ s_i A_i)` (seed 41, bound 40, `a + 8`), both house primes, hybrid route; `engine` = U for the unchanged "
                f"`analysis/wk12_s79_per6.py`, L for the lean driver.\n\n")
        f.write("| rank | `μ` | `a` | `N_S` | Stab | `n_χ` | `mult` | units | secs | HWM GB | engine |\n|---|---|---|---|---|---|---|---|---|---|---|\n")
        for r in reached:
            f.write(f"| {r['rank']} | `({','.join(map(str, r['mu']))})` | {r['a']} | {r['N_S']} | {r['stab']} | {r['n_chi']} | {r['mult']} | {r['units']} | "
                    f"{r['secs']} | {r['hwm_gb']} | {'L' if 'lean' in r['engine'] else 'U'} |\n")
        if not_reached:
            f.write("\nNot reached:\n\n| rank | `μ` | `a` | `N_S` | `N_S·δ` | reason | attempts |\n|---|---|---|---|---|---|---|\n")
            for r in not_reached:
                f.write(f"| {r['rank']} | `({','.join(map(str, r['mu']))})` | {r['a']} | {r['N_S']} | {r['price']['NS_delta']:.2e} | {r['reason']} | "
                        f"{'; '.join(a['engine'] + ':' + a['reason'] + ' rc ' + str(a['rc']) for a in r['attempts']) or '—'} |\n")
    print(f"reached {len(reached)}/95 (sum a {st['sum_a_reached']}), not reached {len(not_reached)} (sum a {st['sum_a_not_reached']}); "
          f"completed prefix {prefix} (through rank {st['prefix_last_rank']}); full rank at both primes {st['full_rank_at_both_primes']}; "
          f"drops {len(drops)}; prime disagreements {len(disagree)}; max secs {st['max_secs']}; total secs {st['total_secs']}; max HWM {st['max_hwm_gb']} GB; "
          f"lean-engine weights {st['lean_engine_weights']}")
    for r in not_reached:
        print(f"  not reached: rank {r['rank']} {tuple(r['mu'])} a={r['a']} N_S={r['N_S']} pred {r['pred_peak_gb']} GB: {r['reason']} "
              f"[{'; '.join(a['engine'] + ':' + a['reason'] + ' rc ' + str(a['rc']) + ' ' + str(a['wall']) + 's' for a in r['attempts'])}]")
    return 0


if __name__ == '__main__':
    sys.exit(main())

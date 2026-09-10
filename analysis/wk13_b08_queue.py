#!/usr/bin/env python3
"""
B13-08 -- the frozen queue: the degree-10 length-6 cubic weights session 79
priced and did not reach, restricted to N_S < 10^7, in session 79's recorded
cost order (N_S ascending).

    input   results/s79_per6_queue.json['10']   the 402 weights mu |- 30 of length 6 with a(mu,10) >= 1,
                                                 with a (plethysm) and N_S, sorted by N_S (session 79, frozen)
            results/s79_per6.jsonl               the 296 records session 79 banked at delta = 10
    output  results/b13_08/queue.json            the 95 remaining weights with N_S < 10^7, rank = position in
                                                 the 402-queue, plus |Stab| and the memory-model prediction
                                                 used only for lane scheduling (never for a result)

The eleven weights with N_S >= 10^7 are listed in the same file under
"deferred_batch14" and are not run.
"""
import json, os, sys, collections, math

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..'))
NS_CAP = 10 ** 7
DELTA = 10

# nrows / N_S by |Stab|, medians (max) over session 79's 506 cubic-scan records; used for the memory
# prediction only.  Unlisted stabiliser orders fall back to 3.3 (the |Stab| = 1 value, the largest).
NROWS_RATIO = {1: 3.72, 2: 3.03, 4: 2.16, 6: 2.58, 8: 1.23, 12: 1.51, 24: 1.5, 36: 0.72, 48: 0.73, 120: 0.7, 720: 0.7}


def stab_order(mu):
    s = 1
    for v in collections.Counter(mu).values(): s *= math.factorial(v)
    return s


def predicted_peak_gb(N_S, a, mu, delta=DELTA):
    """a rough peak-RSS model of the unchanged engine (wk12_s79_per6.py with S71_MEM_X = 2.5e8), fitted by eye
    on session 79's records: build/E ~ 3e-8 GB per unit of N_S*delta; then the larger of the hybrid's X-block
    transient (~1.25 GB at S71_MEM_X = 2.5e8), the kernel check E @ K (~32 bytes per row per kernel column,
    at most 16 columns at once) and the evaluation-row product (~32 bytes per chi-column per point)."""
    s = stab_order(mu)
    nrows = NROWS_RATIO.get(s, 3.72) * N_S
    n_chi = N_S / s
    build = 0.3 + 3e-8 * N_S * delta
    hyb = max(1.25, 32.0 * nrows * min(a, 16) / 1e9, 32.0 * (a + 8) * n_chi / 1e9)
    return round(build + hyb, 2)


def main():
    Q = json.load(open(os.path.join(ROOT, 'results', 's79_per6_queue.json')))[str(DELTA)]
    assert all(Q[i]['N_S'] <= Q[i + 1]['N_S'] for i in range(len(Q) - 1)), "s79 queue not in N_S order"
    done = {}
    for ln in open(os.path.join(ROOT, 'results', 's79_per6.jsonl')):
        r = json.loads(ln)
        if r['delta'] == DELTA: done[tuple(r['mu'])] = r
    assert len(done) == 296, len(done)
    remaining = [dict(rank=i + 1, mu=c['mu'], a=int(c['a']), N_S=int(c['N_S'])) for i, c in enumerate(Q) if tuple(c['mu']) not in done]
    assert len(remaining) == 106, len(remaining)
    for w in remaining:
        w['stab'] = stab_order(w['mu']); w['NS_delta'] = w['N_S'] * DELTA
        w['pred_peak_gb'] = predicted_peak_gb(w['N_S'], w['a'], w['mu'])
    queue = [w for w in remaining if w['N_S'] < NS_CAP]
    deferred = [w for w in remaining if w['N_S'] >= NS_CAP]
    assert len(queue) == 95 and len(deferred) == 11
    out = dict(board_numbering='batch13', session='B13-08', delta=DELTA, n=3, r=6, N_S_cap=NS_CAP,
               source=dict(queue='results/s79_per6_queue.json', banked='results/s79_per6.jsonl', banked_delta10=len(done)),
               order='session 79 recorded cost order: N_S ascending (rank = position in the 402-weight queue)',
               count=len(queue), sum_a=sum(w['a'] for w in queue), queue=queue,
               deferred_batch14=deferred, deferred_sum_a=sum(w['a'] for w in deferred))
    os.makedirs(os.path.join(ROOT, 'results', 'b13_08'), exist_ok=True)
    with open(os.path.join(ROOT, 'results', 'b13_08', 'queue.json'), 'w') as f:
        json.dump(out, f, indent=1)
    print(f"| # | rank | `mu` | `a` | `N_S` | `|Stab|` | `N_S*delta` | pred. peak GB |")
    print("|---|---|---|---|---|---|---|---|")
    for i, w in enumerate(queue, 1):
        print(f"| {i} | {w['rank']} | `({','.join(map(str, w['mu']))})` | {w['a']} | {w['N_S']} | {w['stab']} | {w['NS_delta']:.2e} | {w['pred_peak_gb']} |")
    print(f"\n{len(queue)} weights, sum a = {out['sum_a']}; deferred (N_S >= 1e7): {len(deferred)}, sum a = {out['deferred_sum_a']}")
    for w in deferred:
        print(f"  deferred rank {w['rank']} ({','.join(map(str, w['mu']))}) a={w['a']} N_S={w['N_S']}")


if __name__ == '__main__':
    main()

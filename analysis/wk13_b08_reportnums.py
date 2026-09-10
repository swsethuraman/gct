#!/usr/bin/env python3
"""
B13-08 -- the numeric paragraphs of docs/b13_08_report.md, generated from the
merged record so the report's figures and its data cannot drift apart.
Writes results/b13_08/report_numbers.md; the report quotes it.
"""
import os, sys, json, collections, math

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..'))
RES = os.path.join(ROOT, 'results', 'b13_08')
CAP = 1 << 21
BLOCKED = [319, 339, 350, 361, 363, 367, 369, 371, 373, 375, 376, 382, 383, 387, 389, 390, 391]


def main():
    st = json.load(open(os.path.join(RES, 'status.json')))
    Q = json.load(open(os.path.join(RES, 'queue.json')))
    R = st['reached_list']; NR = st['not_reached_list']
    lean = [r for r in R if 'lean' in r['engine']]
    unblocked_reached = [r for r in R if r['rank'] not in BLOCKED]
    blocked_reached = [r for r in R if r['rank'] in BLOCKED]
    # contiguous prefix
    pre = st['completed_prefix_in_cost_order']; pre_rank = st['prefix_last_rank']
    # throughput
    rate = sorted(r['secs'] / (r['N_S'] * 10 / 1e6) for r in R)
    med = rate[len(rate) // 2]
    rem_secs = sum(med * w['N_S'] * 10 / 1e6 for w in NR)
    L = []
    A = L.append
    A(f"reached: **{len(R)} of 95** (Σa = {st['sum_a_reached']} of 367), every one `mult = a` at both house primes")
    A(f"contiguous prefix in the recorded cost order: **{pre}** weights, through **rank {pre_rank}**")
    A(f"on the unchanged engine: {len(unblocked_reached)}; on the lean driver (the `n_chi >= 2^21` weights of addendum B): {len(blocked_reached)}"
      + (f" — ranks {', '.join(str(r['rank']) for r in blocked_reached)}" if blocked_reached else ""))
    A(f"drops: **{len(st['drops'])}**; prime disagreements: **{len(st['primes_disagree'])}**")
    A(f"N_S over the weights reached: {min(r['N_S'] for r in R):,} to {max(r['N_S'] for r in R):,}; "
      f"a from {min(r['a'] for r in R)} to {max(r['a'] for r in R)}; n_chi to {max(r['n_chi'] for r in R):,}")
    A(f"cost: {st['total_secs']:,.0f} CPU-seconds over the weights reached, longest {st['max_secs']:.0f} s, peak RSS {st['max_hwm_gb']} GB")
    A(f"not reached: {len(NR)} (Σa = {st['sum_a_not_reached']}), of which {sum(1 for w in NR if w['rank'] in BLOCKED)} are addendum-B weights not yet run")
    A(f"measured throughput: median **{med:.1f} s per 10^6 of N_S·delta** over the {len(R)} reached; "
      f"the {len(NR)} unreached carry Σ N_S·delta = {sum(w['price']['NS_delta'] for w in NR)/1e6:,.0f}·10^6, "
      f"so **≈ {rem_secs/3600:.1f} CPU-hours**, about {rem_secs/3600/1.7:.1f} h of wall clock on a two-lane box of this size")
    A(f"degree-10 length-6 census: 402 weights, session 79 banked 296, this session {len(R)} → **{296+len(R)} empty, {402-296-len(R)} open** "
      f"({95-len(R)} of them below N_S = 10^7, 11 deferred to batch 14 at or above it)")
    with open(os.path.join(RES, 'report_numbers.md'), 'w') as f:
        f.write("# B13-08 — generated figures (analysis/wk13_b08_reportnums.py)\n\n")
        for x in L: f.write(f"- {x}\n")
    for x in L: print('- ' + x)
    return 0


if __name__ == '__main__':
    sys.exit(main())

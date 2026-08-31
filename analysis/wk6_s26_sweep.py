"""Session 26 -- the sweep: measure mult at every ambient-supported weight whose
weight space is small enough, all lengths, and rebuild the published
total-deficit sequence from scratch.

Weights whose weight space exceeds `cap` monomials are reported as SKIPPED, not
silently assumed.  The printed total then carries the assumption mult = a on the
skipped set, and the skipped set is printed so the assumption stays visible.
"""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wk6_s26_core import partitions, a_pleth, m_det
from wk6_s26_hwv import measure_np, weight_basis

PUB = {2: 1, 3: 6, 4: 31, 5: 141, 6: 618, 7: 2488}


def run(dmax=7, cap=900, kind='det'):
    for d in range(2, dmax + 1):
        t = time.time()
        rows, bad, skipped = [], [], []
        for lam in partitions(3 * d):
            if len(lam) > 9:
                continue
            aa = a_pleth(lam, d)
            if aa == 0:
                continue
            src, _ = weight_basis(d, len(lam), lam)
            if len(src) > cap:
                skipped.append((lam, aa, len(src)))
                continue
            a2, mu, ns = measure_np(lam, d, kind, a_known=aa)
            rows.append((lam, aa, mu, ns))
            if mu != aa:
                bad.append((lam, d, aa, mu))
        sm = sum(m_det(l, 3, d) for l in partitions(3 * d) if len(l) <= 9)
        meas_a = sum(a for _, a, _, _ in rows)
        meas_m = sum(mu for _, _, mu, _ in rows)
        skip_a = sum(a for _, a, _ in skipped)
        tot = sm - meas_m - skip_a
        print("delta=%d: measured %d (sum a=%d, sum mult=%d) | skipped %d "
              "(sum a=%d, dim>%d) | sum m_det=%d -> total def=%d (published %s) %s"
              " | mult<a at %d  [%.0fs]"
              % (d, len(rows), meas_a, meas_m, len(skipped), skip_a, cap, sm,
                 tot, PUB.get(d, '?'),
                 "MATCH" if tot == PUB.get(d) else "*** MISMATCH ***",
                 len(bad), time.time() - t), flush=True)
        for b in bad[:10]:
            print("    mult < a:", b, flush=True)
        for sk in skipped[:14]:
            print("    skipped:", sk, flush=True)


if __name__ == '__main__':
    run(int(sys.argv[1]) if len(sys.argv) > 1 else 7,
        int(sys.argv[2]) if len(sys.argv) > 2 else 900)

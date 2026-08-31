"""Session 26 -- the full sweep: measure mult at every ambient-supported weight,
all lengths, and rebuild the published total-deficit sequence from scratch."""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wk6_s26_core import partitions, a_pleth, m_det
from wk6_s26_hwv import measure_np

PUB = {2: 1, 3: 6, 4: 31, 5: 141, 6: 618, 7: 2488}


def run(dmax=7):
    for d in range(2, dmax + 1):
        t = time.time(); rows = []; bad = []
        for lam in partitions(3 * d):
            if len(lam) > 9:
                continue
            aa = a_pleth(lam, d)
            if aa == 0:
                continue
            a2, mu, ns = measure_np(lam, d, 'det', a_known=aa)
            rows.append((lam, aa, mu, ns))
            if mu != aa:
                bad.append((lam, d, aa, mu))
        sm = sum(m_det(l, 3, d) for l in partitions(3 * d) if len(l) <= 9)
        tot = sm - sum(mu for _, _, mu, _ in rows)
        print("delta=%d: %d weights a>0, sum a=%d, sum mult=%d, sum m_det=%d "
              "-> total def=%d (published %d) %s ; mult<a at %d  [%.0fs]"
              % (d, len(rows), sum(a for _, a, _, _ in rows),
                 sum(mu for _, _, mu, _ in rows), sm, tot, PUB.get(d, -1),
                 "MATCH" if tot == PUB.get(d) else "*** MISMATCH ***",
                 len(bad), time.time() - t), flush=True)
        for b in bad[:10]:
            print("    mult < a:", b, flush=True)


if __name__ == '__main__':
    run(int(sys.argv[1]) if len(sys.argv) > 1 else 7)

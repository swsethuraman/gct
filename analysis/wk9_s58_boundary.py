#!/usr/bin/env python3
"""Session 58 -- the boundary family of the integrator's note.

    lam = (3k + 2m, k, 2^m),  delta = k + m,  rho = (k, 2^m):  2 delta = |rho| + rho_1 exactly,

the family on which the LMR cell (k = 17, m = 7) sits, at exact equality on the
stability boundary.  Every member is computed DIRECTLY at its own delta by the
reduction (no stability hypothesis enters: the box condition beta_1 <= delta is part
of the exact computation), and re-derived by the Pieri organisation, by the brute-force
p(4 delta) character sum with this session's own Murnaghan-Nakayama, by the house
Python m_det (N <= 40) and by the s39 C engine (N <= 64) where those routes reach.
The integrator's nine values (direct p(4 delta) sums) are the banked comparison."""
import sys, os, time, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts'))
import wk9_s58_sk as S

S.log_pid('s58_boundary')
INTEGRATOR = {(2, 1): (2, 2), (3, 1): (2, 2), (2, 2): (5, 5), (3, 2): (6, 6), (4, 2): (20, 18), (4, 3): (61, 47),
              (5, 3): (110, 77), (5, 4): (311, 197), (6, 4): (657, 410)}          # (k, m) -> (g, sk)
FAMILY = list(INTEGRATOR) + [(7, 4), (8, 4), (7, 5), (9, 5), (8, 6), (10, 6), (11, 5), (12, 4), (9, 7), (13, 3)]
brute_max = int(sys.argv[1]) if len(sys.argv) > 1 else 40
engine_max = int(sys.argv[2]) if len(sys.argv) > 2 else 64
rows = []
E39 = {}
def engine(delta):
    if delta not in E39:
        import wk9_s39_chars as C
        C.LIB.memo_reset()
        E39.clear()
        E39[delta] = C.MdetEngine(delta, n=4)
    return E39[delta]
for k, m in FAMILY:
    delta = k + m; N = 4 * delta
    lam = (3 * k + 2 * m, k) + (2,) * m
    assert sum(lam) == N and 2 * delta == (k + 2 * m) + k
    t0 = time.time(); g, A, sk = S.sk_reduced(lam, delta, 4); t1 = time.time()
    gp, Ap, skp = S.sk_pieri(lam, delta, 4)
    row = {'k': k, 'm': m, 'delta': delta, 'N': N, 'lam': list(lam), 'g': g, 'A': A, 'sk': sk, 'ak': (g - A) // 2,
           'time': round(t1 - t0, 3), 'pieri_agree': (gp, Ap, skp) == (g, A, sk)}
    if (k, m) in INTEGRATOR:
        row['integrator'] = list(INTEGRATOR[(k, m)])
        row['integrator_agree'] = (g, sk) == INTEGRATOR[(k, m)]
    if N <= brute_max:
        t2 = time.time(); gb, Ab, skb = S.sk_brute(lam, delta, 4); t3 = time.time()
        row['brute'] = [gb, Ab, skb]; row['brute_agree'] = (gb, Ab, skb) == (g, A, sk); row['brute_time'] = round(t3 - t2, 1)
        t4 = time.time(); h = S.house_m_det(lam, delta, 4); t5 = time.time()
        row['house'] = h; row['house_agree'] = (h == sk); row['house_time'] = round(t5 - t4, 1)
    if N <= engine_max and N >= 44:
        try:
            t6 = time.time(); v = engine(delta).m_det(lam); t7 = time.time()
            row['s39_engine'] = v; row['s39_agree'] = (v == sk); row['s39_time'] = round(t7 - t6, 1)
        except Exception as e:
            row['s39_engine'] = 'unavailable: %r' % (e,)
    rows.append(row)
    print(json.dumps(row)); sys.stdout.flush()
    json.dump(rows, open(os.path.join(S.ROOT, 'results', 's58_boundary.json'), 'w'), indent=1)
bad = [r for r in rows if not all(r.get(key, True) for key in ('pieri_agree', 'integrator_agree', 'brute_agree', 'house_agree', 's39_agree'))]
print("boundary family: %d cells, %d disagreements" % (len(rows), len(bad)))

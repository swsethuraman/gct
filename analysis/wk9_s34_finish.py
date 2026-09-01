#!/usr/bin/env python3
"""
Session 34 -- completion pass: one cell per fresh process.

For the giants the in-sweep guard deferred (the census-constant prediction
cannot pass 0.85 * MemAvailable while a long-lived worker holds residual
heap), the prereg allows a post-F attempt under the OBSERVED peak-RSS
constant (PREREG_s34.md sections 4, 7.5).  A fresh interpreter per cell gives
the gate an honest MemAvailable and the cell an empty heap.

    wk9_s34_finish.py LAM_UNDERSCORED C_OBS [FLAG]

Same discipline as the sweep: fast path, a_expect asserted, both primes,
sceptical branch with kernel exhibit, STOP_ALL on D > 0, bank + fsync.
The banked row carries FLAG (default none) -- "EXT" for beyond-frontier cells.
"""
import sys, os, json, time, resource
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wk8_s30_core import measure, det_form, per_padded
from wk8_s30_fast import cell as fast_cell
import wk9_s34_run_d7 as R

if __name__ == '__main__':
    lam = tuple(int(x) for x in sys.argv[1].split("_"))
    c_obs = float(sys.argv[2])
    flag0 = sys.argv[3] if len(sys.argv) > 3 else ""
    d = json.load(open(os.path.join(R.ROOT, "results", "d7_cells.json")))
    c = next(c for c in d['cells'] if tuple(c['lam']) == lam)
    av, ns, r = c['a'], c['ns'], c['ell']
    need = c_obs * ns * ns
    R.WHO = "finish"
    if os.path.exists(R.STOP):
        print("STOP_ALL present -- refusing to run"); sys.exit(1)
    free = R.free_gb()
    print("cell %s: a=%d N_S=%d  observed-constant prediction %.2f GB, free %.2f GB"
          % (lam, av, ns, need, free)); sys.stdout.flush()
    if need > 0.90 * free:
        print("does not fit even under the observed constant -- honest stop"); sys.exit(2)
    if R.taken(lam):
        print("already claimed -- nothing to do"); sys.exit(0)
    if not R.claim(lam):
        print("claim race lost -- nothing to do"); sys.exit(0)
    d4, N4 = det_form(4); pd, Np = per_padded(3, 4)
    t0 = time.time()
    out = fast_cell([("det", d4, N4), ("pad", pd, Np)], 4, r, R.DELTA, lam,
                    a_expect=av, seeds={'det': 11, 'pad': 29}, verbose=True)
    assert out['nbasis'] == ns, ("N_S mismatch vs census", lam, out['nbasis'], ns)
    md, mp = out['det'], out['pad']
    flag = flag0
    for nm, m, f, N in (("det", md, d4, N4), ("pad", mp, pd, Np)):
        if m < av:
            R.sceptical(nm, f, N, lam, r, av, m)
            flag = (flag + " " if flag else "") + "bite:%s" % nm
    D = mp - md
    if D > 0:
        open(R.STOP, "w").write("D>0 at %s by finish pid %d\n" % (lam, os.getpid()))
        with open(os.path.join(R.ROOT, "results", "d7_hit.json"), "w") as fh:
            json.dump(dict(lam=list(lam), a=av, ns=ns, mult_det=md, mult_pad=mp,
                           worker="finish"), fh)
        flag = (flag + " " if flag else "") + "*** D>0 STOP-EVERYTHING ***"
    R.bank("| %s | %d | %d | %d | %d | %d | %+d | %s |"
           % (str(lam), r, av, ns, md, mp, D, flag))
    print("%-24s %2d %3d %6d    %2d %-5s  %2d %-5s %+3d %s [%.0fs, maxrss %.2f GB]"
          % (str(lam), r, av, ns, md, "(=a)" if md == av else "(<a)",
             mp, "(=a)" if mp == av else "(<a)", D, flag, time.time() - t0,
             resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1048576.0))
    sys.exit(3 if D > 0 else 0)

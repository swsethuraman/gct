#!/usr/bin/env python3
"""
Session 30 -- coordinated two-worker sweep of the 62.

Why this file exists.  The first attempt ran two independent drivers, one in
the pre-registered interleaved order and one in ascending N_S.  Their cheap
ends coincide, so they recomputed the same four cells.  This driver replaces
both with a shared work queue: a cell is CLAIMED by creating
results/claims/<lam>.claim with O_CREAT|O_EXCL, which is atomic on the local
filesystem, so exactly one worker gets each cell and no coordination message
is needed.  Cells already banked are pre-claimed at launch.

Worker "bal" walks the balanced / largest-a end (the regime test).
Worker "asc" walks ascending N_S (coverage).
Both draw from the same 62 and skip anything already claimed, so the two
streams meet in the middle and stop rather than overlap.

Pre-registration is unaffected: the union of the two streams is still
"ascending sweep for coverage plus a deliberate pass over the largest-a and
most balanced cells the budget can reach" (results/PREREG_s30.md).
"""
import sys, time, os
sys.path.insert(0, '/root/gct/analysis')
from wk8_s30_core import measure, det_form, per_padded, monomials
from wk8_s30_pleth import amb
from wk8_s30_sweep import NINE, cells62, balance

# ---- memory guard -------------------------------------------------------
# Peak RSS of a cell is quadratic in N_S: the flint matrices are N_S columns
# wide with more rows than columns.  Measured 2.4 GB at N_S = 6789, which
# fixes the constant at 5.2e-8 GB per N_S^2.  Worker "bal" was OOM-killed at
# N_S = 9224 (4.76 GB anon-rss) running alongside "asc", which is what this
# guard exists to prevent: a cell that does not fit is WAITED for, not
# skipped, so coverage is never silently reduced by a transient memory dip.
MEM_PER = 5.2e-8            # GB per N_S^2
HEADROOM = 0.85             # do not plan to use the last 15% of free memory

def predicted_gb(ns):
    return MEM_PER * ns * ns

def free_gb():
    for ln in open("/proc/meminfo"):
        if ln.startswith("MemAvailable:"):
            return int(ln.split()[1]) / 1048576.0
    return 0.0

def wait_for_memory(ns, tag, patience=40):
    """Block until the cell plausibly fits.  Returns False to defer it."""
    need = predicted_gb(ns)
    for k in range(patience):
        if need <= HEADROOM * free_gb():
            return True
        if k == 0:
            print("   [mem] %s needs ~%.1f GB, %.1f GB free -- waiting"
                  % (tag, need, free_gb()))
            sys.stdout.flush()
        time.sleep(30)
    print("   [mem] %s still does not fit after %d min -- deferring"
          % (tag, patience // 2))
    sys.stdout.flush()
    return False

CLAIMS = "/root/gct/results/claims"
LEDGER = "/root/gct/results/sweep62_ledger.md"

def claim(lam):
    """Atomic take.  True if this worker got the cell."""
    os.makedirs(CLAIMS, exist_ok=True)
    p = os.path.join(CLAIMS, "%s.claim" % ("_".join(map(str, lam))))
    try:
        fd = os.open(p, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        return False
    os.write(fd, ("%s %d\n" % (WHO, os.getpid())).encode())
    os.close(fd)
    return True

def bank(line):
    with open(LEDGER, "a") as fh:
        fh.write(line + "\n")
        fh.flush(); os.fsync(fh.fileno())

if __name__ == '__main__':
    WHO = sys.argv[1]                       # "bal" or "asc"
    CAP = int(sys.argv[2])
    allc  = cells62()
    live  = [c for c in allc if c[0] not in set(NINE)]
    sizes = {lam: len(monomials(4, len(lam), 6, lam)) for lam, _ in live}
    pool  = [c for c in live if sizes[c[0]] <= CAP]
    if WHO == "bal":
        pool.sort(key=lambda c: (-c[1], balance(c[0]), sizes[c[0]]))
    else:
        pool.sort(key=lambda c: sizes[c[0]])
    print("worker %s: %d of the %d live cells within cap N_S <= %d"
          % (WHO, len(pool), len(live), CAP))
    print("lam                     ell  a   N_S   mult_det  mult_pad   D")
    sys.stdout.flush()

    d4, N4 = det_form(4); pd, Np = per_padded(3, 4)
    done, hits, deferred = 0, [], []
    for lam, av in pool:
        r  = len(lam)
        ns = sizes[lam]
        if predicted_gb(ns) > HEADROOM * free_gb():
            if not wait_for_memory(ns, str(lam)):
                deferred.append(lam); continue
        if not claim(lam):
            continue
        t0 = time.time()
        md = measure(d4, N4, 4, r, 6, lam, a_expect=av)
        mp = measure(pd, Np, 4, r, 6, lam, seed=29, a_expect=av)
        # any rank strictly below the ambient cap is re-run at 3x points
        # before it is believed -- a short rank is the interesting outcome,
        # so it gets the sceptical treatment, not the credulous one.
        for nm, m, f, N in (("det", md, d4, N4), ("pad", mp, pd, Np)):
            if m['mult'] < av:
                m2 = measure(f, N, 4, r, 6, lam, npts=3 * av + 24, seed=907,
                             a_expect=av)
                assert m2['mult'] == m['mult'], ("short rank unstable", lam, nm, m, m2)
        D = mp['mult'] - md['mult']
        done += 1
        flag = ""
        if D > 0:
            hits.append((lam, av, md['mult'], mp['mult'])); flag = "  *** D>0 ***"
        bank("| %s | %d | %d | %d | %d | %d | %+d |"
             % (str(lam), r, av, ns, md['mult'], mp['mult'], D))
        print("%-24s %2d %3d %6d    %2d %-5s  %2d %-5s %+3d%s  [%.0fs]"
              % (str(lam), r, av, ns, md['mult'],
                 "(=a)" if md['mult'] == av else "(<a)", mp['mult'],
                 "(=a)" if mp['mult'] == av else "(<a)", D, flag, time.time() - t0))
        sys.stdout.flush()
        if hits:
            print("*** STOPPING: D > 0 ***"); break
    print()
    print("worker %s done: %d cells ; D>0: %d ; deferred for memory: %s"
          % (WHO, done, len(hits), deferred if deferred else "-"))

#!/usr/bin/env python3
"""
Session 34 -- claim-queue sweep of the 46 feasible delta=7 cells.

Inherits s30's engineering wholesale (wk8_s30_run62c.py): O_CREAT|O_EXCL claim
files, PID-owned; existence pre-check BEFORE the memory gate; the memory guard
WAITS, it does not skip; kill only by explicit PID.  Claims in
results/claims_d7/.  STOP-EVERYTHING sentinel: results/claims_d7/STOP_ALL --
created on any D > 0; every worker checks it before every claim.

Measurement path (pre-registered, PREREG_s34.md section 4): wk8_s30_fast.cell
-- R built once per cell, shared by det and pad, all rows used -- with
a_expect from the plethysm, seeds det 11 / pad 29, bound 40, npts = a+8,
primes 2147483647 / 2147483629.  Sceptical branch (either side < a):
wk8_s30_core.measure at npts = 3a+24, fresh seed 907, want_U -- the kernel is
exhibited to results/d7_kernels/ -- before the row is banked.

Workers: "asc" (ascending N_S), "bal" (largest-a / most-balanced probes),
"solo" (the pre-registered 3:1 interleaved master order).  argv:
    wk9_s34_run_d7.py WHO CAP [HEADROOM]
"""
import sys, time, os, json, resource
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wk8_s30_core import measure, det_form, per_padded
from wk8_s30_fast import cell as fast_cell

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLAIMS = os.path.join(ROOT, "results", "claims_d7")
LEDGER = os.path.join(ROOT, "results", "d7_ledger.md")
KERNELS = os.path.join(ROOT, "results", "d7_kernels")
STOP = os.path.join(CLAIMS, "STOP_ALL")
DELTA = 7
MEM_PER = 5.6e-8               # census constant (prereg sections 3, 8)
HEADROOM = 0.85

HEADER = """# Sweep ledger — delta = 7 (n = 4, a >= 2, ell >= 5), the 46 feasible cells
#
# Corrected raising rule E_ij c_alpha = (alpha_i+1) c_{alpha+e_i-e_j} throughout.
# Ranks by python-flint nmod_mat.rank() over primes 2147483647, 2147483629;
# a checked against the plethysm at every cell; rank(R) = N_S - a asserted;
# N_S asserted equal to the census DP value.  D := mult_pad - mult_det;
# an obstruction is D > 0 only (PREREG_s34.md section 0).
# flag: "" normal | DEFER-MEM attempted, deferred (memory) -- not a measurement
#       | EXT beyond the pre-registered frontier | bite:* sceptical branch banked
#
| lam | ell | a | N_S | mult_det | mult_pad | D | flag |
|---|---|---|---|---|---|---|---|
"""

def predicted_gb(ns): return MEM_PER * ns * ns

def free_gb():
    for ln in open("/proc/meminfo"):
        if ln.startswith("MemAvailable:"):
            return int(ln.split()[1]) / 1048576.0
    return 0.0

def wait_for_memory(ns, tag, patience=40):
    need = predicted_gb(ns)
    for k in range(patience):
        if need <= HEADROOM * free_gb(): return True
        if k == 0:
            print("   [mem] %s needs ~%.1f GB, %.1f GB free -- waiting" % (tag, need, free_gb()))
            sys.stdout.flush()
        time.sleep(30)
    print("   [mem] %s still does not fit after %d min -- deferring" % (tag, patience // 2))
    sys.stdout.flush()
    return False

def taken(lam):
    return os.path.exists(os.path.join(CLAIMS, "%s.claim" % "_".join(map(str, lam))))

def claim(lam):
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
    new = not os.path.exists(LEDGER)
    with open(LEDGER, "a") as fh:
        if new: fh.write(HEADER)
        fh.write(line + "\n")
        fh.flush(); os.fsync(fh.fileno())

def load_pool():
    d = json.load(open(os.path.join(ROOT, "results", "d7_cells.json")))
    F = [c for c in d['cells'] if c['feas_s34']]
    for c in F: c['lam'] = tuple(c['lam'])
    asc = sorted(F, key=lambda c: (c['ns'], tuple(-x for x in c['lam'])))
    bal = sorted(F, key=lambda c: (-c['a'], c['balance'], c['ns'], tuple(-x for x in c['lam'])))
    if WHO == "bal": return bal
    if WHO == "asc": return asc
    seq, seen = [], set()
    ia = ib = 0
    while len(seq) < len(F):
        for _ in range(3):
            while ia < len(asc) and asc[ia]['lam'] in seen: ia += 1
            if ia < len(asc): seq.append(asc[ia]); seen.add(asc[ia]['lam'])
        while ib < len(bal) and bal[ib]['lam'] in seen: ib += 1
        if ib < len(bal): seq.append(bal[ib]); seen.add(bal[ib]['lam'])
    return seq

def sceptical(side, f, N, lam, r, av, m_first):
    """re-run at 3x points, fresh seed, both primes, kernel exhibited."""
    print("   [sceptical] %s mult=%d < a=%d at %s -- 3x points, seed 907, want_U"
          % (side, m_first, av, lam)); sys.stdout.flush()
    m2 = measure(f, N, 4, r, DELTA, lam, npts=3 * av + 24, seed=907,
                 a_expect=av, want_U=True)
    assert m2['mult'] == m_first, ("short rank unstable", lam, side, m_first, m2['mult'])
    os.makedirs(KERNELS, exist_ok=True)
    with open(os.path.join(KERNELS, "%s_%s.json" % ("_".join(map(str, lam)), side)), "w") as fh:
        json.dump(dict(lam=list(lam), side=side, a=av, mult=m2['mult'],
                       Udim=m2['Udim'], U=m2['U'],
                       note="U = kernel vectors in the a-dim coordinates of "
                            "ker(R) mod 2147483647; npts=3a+24 seed=907"), fh)
    print("   [sceptical] confirmed mult=%d, kernel (dim %d) exhibited" %
          (m2['mult'], m2['Udim'])); sys.stdout.flush()
    return m2

if __name__ == '__main__':
    WHO = sys.argv[1]
    CAP = int(sys.argv[2])
    if len(sys.argv) > 3: HEADROOM = float(sys.argv[3])
    pool = [c for c in load_pool() if c['ns'] <= CAP]
    d4, N4 = det_form(4); pd, Np = per_padded(3, 4)
    print("worker %s (pid %d): %d cells within cap N_S <= %d, headroom %.2f"
          % (WHO, os.getpid(), len(pool), CAP, HEADROOM))
    print("lam                     ell  a   N_S   mult_det  mult_pad   D")
    sys.stdout.flush()
    done, deferred = 0, []
    for c in pool:
        lam, av, ns, r = c['lam'], c['a'], c['ns'], c['ell']
        if os.path.exists(STOP):
            print("STOP_ALL sentinel present -- worker exits"); break
        if taken(lam):                 # cheap pre-check: never wait on memory
            continue                   # for a cell someone else already holds
        if predicted_gb(ns) > HEADROOM * free_gb():
            if not wait_for_memory(ns, str(lam)):
                deferred.append(lam)
                bank("| %s | %d | %d | %d | — | — | — | DEFER-MEM |" % (str(lam), r, av, ns))
                continue
        if not claim(lam):
            continue
        t0 = time.time()
        out = fast_cell([("det", d4, N4), ("pad", pd, Np)], 4, r, DELTA, lam,
                        a_expect=av, seeds={'det': 11, 'pad': 29}, verbose=True)
        assert out['nbasis'] == ns, ("N_S mismatch vs census", lam, out['nbasis'], ns)
        md, mp = out['det'], out['pad']
        flag = ""
        for nm, m, f, N in (("det", md, d4, N4), ("pad", mp, pd, Np)):
            if m < av:
                sceptical(nm, f, N, lam, r, av, m)
                flag = (flag + " " if flag else "") + "bite:%s" % nm
        D = mp - md
        done += 1
        if D > 0:
            open(STOP, "w").write("D>0 at %s by %s pid %d\n" % (lam, WHO, os.getpid()))
            with open(os.path.join(ROOT, "results", "d7_hit.json"), "w") as fh:
                json.dump(dict(lam=list(lam), a=av, ns=ns, mult_det=md, mult_pad=mp,
                               worker=WHO), fh)
            flag = (flag + " " if flag else "") + "*** D>0 STOP-EVERYTHING ***"
        bank("| %s | %d | %d | %d | %d | %d | %+d | %s |"
             % (str(lam), r, av, ns, md, mp, D, flag))
        print("%-24s %2d %3d %6d    %2d %-5s  %2d %-5s %+3d %s [%.0fs, maxrss %.2f GB]"
              % (str(lam), r, av, ns, md, "(=a)" if md == av else "(<a)",
                 mp, "(=a)" if mp == av else "(<a)", D, flag,
                 time.time() - t0,
                 resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1048576.0))
        sys.stdout.flush()
        if D > 0:
            print("*** STOPPING EVERYTHING: D > 0 ***"); break
    print()
    print("worker %s done: %d cells ; deferred for memory: %s"
          % (WHO, done, deferred if deferred else "-"))

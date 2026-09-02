#!/usr/bin/env python3
"""
Session 39 -- Phase 0: the long-weight occurrence screen.

For delta in 8..12 and every lam |- 4*delta with 6 <= ell(lam) <= min(delta, 10)
and lam_1 >= delta (results/PREREG_s39.md section 1.2), tabulate

    a(lam, delta)   ambient plethysm  <h_delta[h_4], s_lam>        (C engine)
    m_det(lam)      symmetric rectangular Kronecker, rect (delta^4)  (C engine)

and classify:  one-bit  a = 1, m_det = 0
               forced   a > m_det >= 1
               silent   otherwise (a <= m_det)
Rows with a = 0 are not cells and are counted only.

Work is chunked by (delta, ell).  A chunk is CLAIMED atomically
(O_CREAT|O_EXCL claim file, PID-owned) so two workers never overlap; a claim
is released at start-up only if its owner PID is dead (reconcile).  Rows are
appended (flushed + fsync) to results/s39_screen/d<delta>_l<ell>.csv as they
are computed, so a restart resumes from the banked rows.  Logs go to
results/logs/.  No pkill -f anywhere; kill by explicit PID only.

usage:  wk9_s39_screen.py <worker-name> <asc|desc> [--dmin 8] [--dmax 12]
        wk9_s39_screen.py reconcile          # release claims of dead owners
"""
import sys, os, time, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from wk9_s39_chars import MdetEngine, PlethEngine, LIB, partitions

ROOT = os.path.join(HERE, '..')
OUTDIR = os.path.join(ROOT, 'results', 's39_screen')
CLAIMS = os.path.join(ROOT, 'results', 'logs', 's39_claims')
LOGDIR = os.path.join(ROOT, 'results', 'logs')


def log(fh, *a):
    s = time.strftime('%H:%M:%S ') + ' '.join(str(x) for x in a)
    print(s, flush=True)
    if fh:
        fh.write(s + '\n'); fh.flush()


def chunks(dmin=8, dmax=12):
    out = []
    for delta in range(dmin, dmax + 1):
        for ell in range(6, min(delta, 10) + 1):
            out.append((delta, ell))
    return out


def chunk_lams(delta, ell):
    N = 4 * delta
    return [lam for lam in partitions(N) if len(lam) == ell and lam[0] >= delta]


def csv_path(delta, ell):
    return os.path.join(OUTDIR, 'd%d_l%d.csv' % (delta, ell))


def claim_path(delta, ell):
    return os.path.join(CLAIMS, 'd%d_l%d.claim' % (delta, ell))


def pid_alive(pid):
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


def reconcile(fh=None):
    """release claims whose owner is dead (the chunk resumes from its csv)."""
    os.makedirs(CLAIMS, exist_ok=True)
    for fn in sorted(os.listdir(CLAIMS)):
        p = os.path.join(CLAIMS, fn)
        try:
            who, pid = open(p).read().split()[:2]
            pid = int(pid)
        except Exception:
            continue
        if not pid_alive(pid):
            os.remove(p)
            log(fh, 'reconcile: released %s (owner %s pid %d dead)' % (fn, who, pid))


def claim(delta, ell, who):
    os.makedirs(CLAIMS, exist_ok=True)
    try:
        fd = os.open(claim_path(delta, ell), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        return False
    os.write(fd, ('%s %d %s\n' % (who, os.getpid(), time.strftime('%Y-%m-%dT%H:%M:%S'))).encode())
    os.close(fd)
    return True


def done_lams(delta, ell):
    p = csv_path(delta, ell)
    done = {}
    if os.path.exists(p):
        for ln in open(p):
            if ln.startswith('delta') or not ln.strip(): continue
            f = ln.strip().split(',')
            done[tuple(int(x) for x in f[1].split('|'))] = f
    return done


def chunk_complete(delta, ell):
    p = csv_path(delta, ell) + '.done'
    return os.path.exists(p)


def run_chunk(delta, ell, who, fh, engines):
    lams = chunk_lams(delta, ell)
    done = done_lams(delta, ell)
    p = csv_path(delta, ell)
    os.makedirs(OUTDIR, exist_ok=True)
    new = not os.path.exists(p)
    out = open(p, 'a')
    if new:
        out.write('delta,lam,ell,a,m_det,class,margin\n'); out.flush()
    if delta not in engines:
        engines.clear()          # one delta's engines in memory at a time
        LIB.memo_reset()
        t0 = time.time()
        engines[delta] = (PlethEngine(delta, d=4), MdetEngine(delta, n=4))
        log(fh, 'engines for delta=%d built (%d W-support classes, %d plethysm classes) [%.0fs]'
            % (delta, engines[delta][1].rl.n, engines[delta][0].rl.n, time.time() - t0))
    PE, ME = engines[delta]
    t0 = time.time(); n_a0 = n_cells = n_one = n_forced = 0; tight = None
    log(fh, 'chunk delta=%d ell=%d: %d candidates, %d already banked' % (delta, ell, len(lams), len(done)))
    for i, lam in enumerate(lams):
        if lam in done:
            f = done[lam]
            if int(f[3]) == 0: n_a0 += 1
            else:
                n_cells += 1
                if f[5] == 'onebit': n_one += 1
                if f[5] == 'forced': n_forced += 1
            continue
        av = PE.a(lam)
        if av == 0:
            md, cls, margin = -1, 'a0', ''
            n_a0 += 1
        else:
            md = ME.m_det(lam)
            n_cells += 1
            if av == 1 and md == 0: cls = 'onebit'; n_one += 1
            elif av > md: cls = 'forced'; n_forced += 1
            else: cls = 'silent'
            margin = md - av
            if tight is None or margin < tight[0]: tight = (margin, lam, av, md)
        out.write('%d,%s,%d,%d,%d,%s,%s\n' % (delta, '|'.join(map(str, lam)), ell, av, md, cls, margin))
        out.flush(); os.fsync(out.fileno())
        if cls in ('onebit', 'forced'):
            log(fh, '  *** %s cell: delta=%d lam=%s a=%d m_det=%d ***' % (cls.upper(), delta, lam, av, md))
        if (i + 1) % 200 == 0:
            log(fh, '  ... %d/%d (a>=1: %d, a=0: %d; one-bit %d, forced %d; memo %d entries, %d clears) [%.0fs]'
                % (i + 1, len(lams), n_cells, n_a0, n_one, n_forced, LIB.memo_entries(), LIB.memo_clears(), time.time() - t0))
    out.close()
    open(p + '.done', 'w').write('%s %d %s\n' % (who, os.getpid(), time.strftime('%Y-%m-%dT%H:%M:%S')))
    log(fh, 'chunk delta=%d ell=%d DONE: %d candidates, %d cells (a>=1), %d with a=0; one-bit %d, forced %d; tightest %s [%.0fs]'
        % (delta, ell, len(lams), n_cells, n_a0, n_one, n_forced, tight, time.time() - t0))
    return n_one + n_forced


def main(argv):
    if argv and argv[0] == 'reconcile':
        reconcile(); return 0
    who, order = argv[0], argv[1]
    dmin = int(argv[argv.index('--dmin') + 1]) if '--dmin' in argv else 8
    dmax = int(argv[argv.index('--dmax') + 1]) if '--dmax' in argv else 12
    os.makedirs(LOGDIR, exist_ok=True)
    fh = open(os.path.join(LOGDIR, 's39_screen_%s.log' % who), 'a')
    log(fh, 'worker %s (%s) pid %d starting, delta %d..%d' % (who, order, os.getpid(), dmin, dmax))
    LIB.memo_set_cap(1 << 25)        # 32M entries x 32 B = 1 GB per worker at most
    reconcile(fh)
    cl = chunks(dmin, dmax)
    if order == 'desc':
        cl = cl[::-1]
    engines = {}
    hits = 0
    for delta, ell in cl:
        if chunk_complete(delta, ell): continue
        if os.path.exists(claim_path(delta, ell)): continue     # cheap pre-check
        if not claim(delta, ell, who): continue
        hits += run_chunk(delta, ell, who, fh, engines)
    log(fh, 'worker %s finished; one-bit/forced cells seen by this worker: %d' % (who, hits))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

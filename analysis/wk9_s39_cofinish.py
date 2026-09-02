#!/usr/bin/env python3
"""
Session 39 -- co-process one (delta, ell) screen chunk from the OTHER end, so a
single large chunk (e.g. delta=12 ell=8) is split between two cores instead of
running on one while the second worker sits idle.

Safe concurrency: rows are appended one line at a time in O_APPEND mode
(Python 'a'), each line < PIPE_BUF, so concurrent appends by the primary worker
and this co-worker are atomic and never interleave.  The banked set is re-read
every REFRESH cells so the two ends stop when they meet (a lam banked by the
other side is skipped).  A lam computed by both sides near the meeting point
yields two IDENTICAL rows; wk9_s39_publish.py dedups by lam and asserts the
duplicates agree.  This co-worker does NOT write the .done marker (the primary
owner of the claim does, after its own pass); it just fills from the far end.

The chunk is finished when every candidate is banked; whichever co-worker
observes that writes the .done marker (idempotent).  Run one `fwd` and one
`rev` co-worker to split a chunk across two cores, each skipping the other's
banked rows.

usage: wk9_s39_cofinish.py <delta> <ell> [fwd|rev]
"""
import sys, os, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from wk9_s39_chars import MdetEngine, PlethEngine, LIB, partitions

ROOT = os.path.join(HERE, '..')
OUTDIR = os.path.join(ROOT, 'results', 's39_screen')
LOGDIR = os.path.join(ROOT, 'results', 'logs')
REFRESH = 100


def csv_path(delta, ell):
    return os.path.join(OUTDIR, 'd%d_l%d.csv' % (delta, ell))


def banked(delta, ell):
    p = csv_path(delta, ell)
    s = set()
    if os.path.exists(p):
        for ln in open(p):
            if ln.startswith('delta') or not ln.strip(): continue
            s.add(ln.strip().split(',')[1])
    return s


def main(argv):
    delta, ell = int(argv[0]), int(argv[1])
    direction = argv[2] if len(argv) > 2 else 'rev'
    os.makedirs(LOGDIR, exist_ok=True)
    fh = open(os.path.join(LOGDIR, 's39_screen_cofinish_d%dl%d_%s.log' % (delta, ell, direction)), 'a')

    def log(*a):
        s = time.strftime('%H:%M:%S ') + ' '.join(str(x) for x in a)
        print(s, flush=True); fh.write(s + '\n'); fh.flush()

    LIB.memo_set_cap(1 << 25)
    N = 4 * delta
    lams = [lam for lam in partitions(N) if len(lam) == ell and lam[0] >= delta]
    ncand = len(lams)
    if direction == 'rev':
        lams = lams[::-1]
    log('cofinish delta=%d ell=%d pid %d dir=%s: %d candidates'
        % (delta, ell, os.getpid(), direction, ncand))
    PE, ME = PlethEngine(delta, d=4), MdetEngine(delta, n=4)
    done = banked(delta, ell)
    p = csv_path(delta, ell)
    out = open(p, 'a')                      # O_APPEND
    n_new = n_cells = n_hit = 0
    t0 = time.time()
    for i, lam in enumerate(lams):
        key = '|'.join(map(str, lam))
        if key in done:
            continue
        av = PE.a(lam)
        if av == 0:
            md, cls, margin = -1, 'a0', ''
        else:
            md = ME.m_det(lam); n_cells += 1
            if av == 1 and md == 0: cls = 'onebit'; n_hit += 1
            elif av > md: cls = 'forced'; n_hit += 1
            else: cls = 'silent'
            margin = md - av
        out.write('%d,%s,%d,%d,%d,%s,%s\n' % (delta, key, ell, av, md, cls, margin))
        out.flush(); os.fsync(out.fileno())
        n_new += 1
        if cls in ('onebit', 'forced'):
            log('  *** %s cell: delta=%d lam=%s a=%d m_det=%d ***' % (cls.upper(), delta, lam, av, md))
        if n_new % REFRESH == 0:
            done = banked(delta, ell)       # meet-in-the-middle: pick up the other end's rows
            log('  ...%d processed by %s (%d cells), %d/%d banked total; memo clears %d [%.0fs]'
                % (n_new, direction, n_cells, len(done), ncand, LIB.memo_clears(), time.time() - t0))
            if len(done) >= ncand:
                log('  chunk fully banked -- stopping'); break
    out.close()
    done = banked(delta, ell)
    if len(done) >= ncand:
        dp = csv_path(delta, ell) + '.done'
        if not os.path.exists(dp):
            open(dp, 'w').write('cofinish %d %s\n' % (os.getpid(), time.strftime('%Y-%m-%dT%H:%M:%S')))
            log('  wrote %s' % dp)
    log('cofinish delta=%d ell=%d dir=%s done: %d new rows, %d cells, %d hits, %d/%d banked [%.0fs]'
        % (delta, ell, direction, n_new, n_cells, n_hit, len(done), ncand, time.time() - t0))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

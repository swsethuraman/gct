#!/usr/bin/env python3
"""
Session 43, Phase A -- the 49 eligible six-row cells inside session 41's
frontier that were never measured.

Order: strictly ascending n_chi, delta = 7 first then delta = 8, exactly as
results/s43_todo.md publishes it (that file is rebuilt from
results/sixrow_census.md by wk9_s43_todo.py; the inherited counts are not
trusted).  Measurement is wk9_s41_cell.py unchanged -- the validated pipeline
of results/s41_validation.md -- run in its own process so the banked HWM is the
cell's own peak.  Per cell: a by kernel dimension and by plethysm (asserted
equal in the cell process); rank(R) = n_chi - a asserted; mult_det and mult_pad
at a + 8 true points; two primes; point-free mult_red by the (*) criterion.

Independent re-check (results/PREREG_s43.md section 1): any cell with mult < a
on either side is re-measured at 3a + 24 fresh points, seed 907, both primes,
and the vanishing vector is exhibited and run through wk9_s41_bite.py, before
the row is banked.

D > 0 writes the STOP flag; every worker stops and the verification protocol
takes over.

Bounding: each cell process is launched under `timeout` and `ulimit -v`, and
its process id is written to results/logs/s43_cell_<who>.pid.  A run that must
be ended early is ended by that recorded id.

usage: python3 wk9_s43_sweep.py <small|big> [--split 6300] [--headroom 0.85] [--dry]
"""
import sys, os, time, json, pickle, subprocess, resource

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
from wk9_s43_guard import predicted_gb, free_gb, heavy_lock, wait_for_memory, WORK

LEDGER = os.path.join(ROOT, 'results', 's43_ledger.md')
CELLS = os.path.join(ROOT, 'results', 's43_cells')
LOGS = os.path.join(ROOT, 'results', 'logs')
CLAIMS = os.path.join(WORK, 'claims')
STOP = os.path.join(WORK, 'STOP')
FAILED = os.path.join(LOGS, 's43_failed.txt')
TODO = os.path.join(WORK, 'todo.pkl')
VMCAP_KB = 6900000          # ulimit -v for a cell process (VSZ/RSS ~ 1.25 measured)
TIMEOUT_BASE = 900          # seconds; scaled by the n_chi model below

HEADER = """# Session 43 ledger — closing the six-row region already in reach (`n = 4`, `ℓ(λ) = 6`, `a ≥ 1`, `δ = 7, 8, 9`)

Pipeline exactly as `results/s41_ledger.md`: the stabiliser reduction `analysis/wk9_s36_stabred.py` unchanged up
to the kernel; kernel by the in-place rref route of `analysis/wk9_s41_kernel.py`, every kernel vector verified
against the uncompressed raising-operator rows; `a` by kernel dimension AND by plethysm (asserted equal);
`rank(R) = n_χ − a` asserted; ranks by python-flint `nmod_mat` over `2147483647` and `2147483629`; `a + 8`
evaluation points per side; independent re-check (`3a + 24` fresh points, seed 907, both primes) on any
`mult < a`.  **Points.**  det: `det_4(Σ s_i A_i)`, random integer `4×4` `A_i`.  pad: the **true padded-permanent
restriction** `x_0 · per_3(x_1..x_9)` with each `x_t` a random linear form in `s_1..s_6` (`per_padded(3,4)`
through `restrict()`) — never `l · (random cubic)`.  `mult_red` is the point-free reducibility multiplicity by
(★) (`docs/reducible_ideal.md`, Corollary A).  `m_det` is the symmetric rectangular Kronecker bound.  Convention
`D = mult_pad − mult_det`; only `D > 0` is an obstruction.  `HWM` is the cell's own peak resident set (GB), one
process per cell.  Cells are taken in ascending `n_χ` from `results/s43_todo.md`.

| delta | lam | a | m_det | N_S | Stab | n_chi | rows | route | mult_det | mult_pad | mult_red | D | secs | HWM |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
"""


def log(*a):
    print(time.strftime('%H:%M:%S'), *a, flush=True)


def key(lam, delta):
    return "%d_%s" % (delta, "_".join(map(str, lam)))


def claim(lam, delta, who):
    os.makedirs(CLAIMS, exist_ok=True)
    p = os.path.join(CLAIMS, key(lam, delta) + '.claim')
    try:
        fd = os.open(p, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        return False
    os.write(fd, ("%s %d\n" % (who, os.getpid())).encode()); os.close(fd)
    return True


def banked():
    out = set()
    if not os.path.exists(LEDGER):
        return out
    for ln in open(LEDGER):
        if ln[:4] in ('| 7 ', '| 8 ', '| 9 '):
            c = [x.strip() for x in ln.strip().strip('|').split('|')]
            out.add((tuple(int(x) for x in c[1].strip('`').strip('()').split(',')), int(c[0])))
    return out


def failed():
    out = set()
    if os.path.exists(FAILED):
        for ln in open(FAILED):
            if ln.strip():
                d, l = ln.split()[:2]
                out.add((tuple(int(x) for x in l.strip('()').split(',')), int(d)))
    return out


def bank(line):
    new = not os.path.exists(LEDGER)
    with open(LEDGER, 'a') as fh:
        if new:
            fh.write(HEADER)
        fh.write(line + "\n"); fh.flush(); os.fsync(fh.fileno())


def commit(msg):
    subprocess.run(['git', '-C', ROOT, 'add', 'results/s43_ledger.md'], capture_output=True)
    if os.path.isdir(CELLS):
        subprocess.run(['git', '-C', ROOT, 'add', 'results/s43_cells'], capture_output=True)
    subprocess.run(['git', '-C', ROOT, '-c', 'user.name=s43', '-c', 'user.email=s43@gct',
                    'commit', '-q', '-m',
                    msg + "\n\nCo-Authored-By: Claude Opus 5 <noreply@anthropic.com>"],
                   capture_output=True)


def timeout_for(n_chi):
    """generous wall-clock bound from the s41 timing model (2500 s at n_chi 19985)"""
    return int(max(TIMEOUT_BASE, 6.0 * 2500 * (n_chi / 19985.0) ** 2.7))


def run_subprocess(args, logfile, n_chi, who):
    pidfile = os.path.join(LOGS, f's43_cell_{who}.pid')
    cmd = ("ulimit -v %d; exec timeout %d %s %s %s"
           % (VMCAP_KB, timeout_for(n_chi), sys.executable,
              os.path.join(HERE, 'wk9_s41_cell.py'), ' '.join(args)))
    with open(logfile, 'a') as lf:
        pr = subprocess.Popen(['bash', '-c', cmd], stdout=subprocess.PIPE, stderr=lf, text=True)
        open(pidfile, 'w').write("%d %s\n" % (pr.pid, ' '.join(args)))
        out, _ = pr.communicate()
    res = None
    for ln in out.splitlines():
        if ln.startswith('RESULT '):
            res = json.loads(ln[7:])
    return pr.returncode, res


def run_cell(x, who, headroom):
    lam, delta, a = x['lam'], x['delta'], x['a']
    gb = predicted_gb(x['n_chi'])
    tag = f"{lam} d={delta} a={a} n_chi={x['n_chi']}"
    if os.path.exists(STOP):
        return 'stop'
    if not claim(lam, delta, who):
        return None
    with heavy_lock(gb, tag, log):
        if os.path.exists(STOP):
            return 'stop'
        wait_for_memory(gb, tag, headroom, log)
        log(f"START {tag} (pred {gb:.1f} GB, free {free_gb():.1f}, timeout {timeout_for(x['n_chi'])}s)")
        pk = os.path.join(WORK, 'cell_%s.pkl' % key(lam, delta))
        lf = os.path.join(LOGS, f's43_cells_{who}.log')
        route = 'exact' if x['n_chi'] <= 800 else 'inplace'
        base = ['--lam', ','.join(map(str, lam)), '--delta', str(delta), '--a', str(a),
                '--out', pk, '--route', route]
        rc, res = run_subprocess(base, lf, x['n_chi'], who)
        if rc != 0 or res is None:
            with open(FAILED, 'a') as fh:
                fh.write(f"{delta} ({','.join(map(str, lam))}) rc={rc} n_chi={x['n_chi']} pred={gb:.1f}GB\n")
            log(f"NOT REACHED {tag}: rc={rc} (recorded in results/logs/s43_failed.txt)")
            return 'failed'
        note = ''
        for sd in ('det', 'pad'):
            if res['mult_' + sd] < a:
                log(f"  *** {tag}: mult_{sd} = {res['mult_'+sd]} < a = {a}: independent re-check "
                    f"(3a+24 = {3*a+24} points, seed 907, both primes)")
                pk2 = os.path.join(WORK, 'cell_%s_recheck.pkl' % key(lam, delta))
                rc2, res2 = run_subprocess(base[:6] + ['--out', pk2, '--route', route,
                                                       '--npts', str(3 * a + 24),
                                                       '--seed-det', '907', '--seed-pad', '907'],
                                           lf, x['n_chi'], who)
                assert rc2 == 0 and res2 is not None, ("re-check run did not complete", lam, rc2)
                assert res2['mult_' + sd] == res['mult_' + sd], \
                    ("short rank unstable", lam, sd, res['mult_' + sd], res2['mult_' + sd])
                os.makedirs(CELLS, exist_ok=True)
                with open(os.path.join(CELLS, "%s_%s.txt" % (key(lam, delta), sd)), 'w') as fh:
                    fh.write(f"# {tag}: mult_{sd} = {res['mult_'+sd]} < a = {a}; re-check at "
                             f"{3*a+24} points seed 907 both primes: {res2['mult_'+sd]}; "
                             f"mult_red = {res['mult_red']}\n")
                bl = os.path.join(LOGS, f's43_bite_{key(lam, delta)}_{sd}.log')
                with open(bl, 'a') as bf:
                    subprocess.run([sys.executable, os.path.join(HERE, 'wk9_s41_bite.py'), pk, sd],
                                   stdout=bf, stderr=bf, text=True)
                # wk9_s41_bite.py writes to a hard-coded results/s41_cells path; this
                # session's artefacts belong in results/s43_cells (see wk9_s43_relocate.py)
                subprocess.run([sys.executable, os.path.join(HERE, 'wk9_s43_relocate.py'), 'origin/main'],
                               capture_output=True, text=True)
                note += f' {sd}-bite'
    D = res['mult_pad'] - res['mult_det']
    line = (f"| {delta} | `{lam}` | {a} | {x['m_det']} | {res['N_S']} | {res['stab']} | {res['n_chi']} | "
            f"{res['nrows']} | {res['route']} | {res['mult_det']} | {res['mult_pad']} | {res['mult_red']} | "
            f"{D:+d} | {res['secs']:.0f} | {res['hwm']:.2f} |")
    bank(line)
    commit(f"s43: bank {lam} delta={delta}: a={a} mult_det={res['mult_det']} mult_pad={res['mult_pad']} "
           f"mult_red={res['mult_red']} D={D:+d}{note}")
    log(line)
    if D > 0:
        open(STOP, 'w').write(f"D>0 at {lam} delta={delta}\n")
        log("*** D > 0: halt the sweep; the verification protocol takes over ***")
        return 'stop'
    return D


if __name__ == '__main__':
    who = sys.argv[1]
    split = int(sys.argv[sys.argv.index('--split') + 1]) if '--split' in sys.argv else 6300
    headroom = float(sys.argv[sys.argv.index('--headroom') + 1]) if '--headroom' in sys.argv else 0.85
    tpath = sys.argv[sys.argv.index('--todo') + 1] if '--todo' in sys.argv else TODO
    todo = pickle.load(open(tpath, 'rb'))
    seq = [x for d in sorted(todo) for x in todo[d]]
    seq.sort(key=lambda x: (x['n_chi'], x['delta'], x['lam']))
    if '--dry' in sys.argv:
        for x in seq:
            print(x['delta'], x['lam'], 'a', x['a'], 'n_chi', x['n_chi'],
                  f"pred {predicted_gb(x['n_chi']):.2f} GB", 'timeout', timeout_for(x['n_chi']))
        print(len(seq), 'cells;', sum(x['a'] for x in seq), 'units')
        sys.exit(0)
    cap = int(sys.argv[sys.argv.index('--cap') + 1]) if '--cap' in sys.argv else 10 ** 9
    seq = [x for x in seq if x['n_chi'] <= cap]
    mine = [x for x in seq if (x['n_chi'] <= split) == (who == 'small')]
    rest = [x for x in seq if x not in mine] if who == 'big' else []
    log(f"worker {who}: {len(mine)} cells in class ({len(rest)} to pick up after), split {split}")
    for x in mine + rest:
        if os.path.exists(STOP):
            log("STOP flag present; exiting"); break
        k = (x['lam'], x['delta'])
        if k in banked() or k in failed():
            continue
        if os.path.exists(os.path.join(CLAIMS, key(*k) + '.claim')):
            continue
        if run_cell(x, who, headroom) == 'stop':
            break
    log(f"worker {who} done")

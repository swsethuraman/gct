#!/usr/bin/env python3
"""
Session 41 -- the sweep driver (results/PREREG_s41.md section 4 order).

Order, applied to /root/s41/census.pkl:
  1. arithmetic-forced cells (a > m_det), reachable, ascending n_chi;
  2. delta = 7: census cells not banked by s36, reachable, ascending n_chi,
     interleaved 3:1 with probes drawn in turn from the largest-a and the
     most-balanced reachable unmeasured cell;
  3. delta = 8: the same rule.
Reachable = n_chi <= --frontier (20000 once the in-place route has validated;
15500 otherwise).  Two workers under the claim queue (O_CREAT|O_EXCL claim
files in /root/s41/claims, PID-owned): worker `small` takes only cells with
n_chi <= 5000, worker `big` the rest (and the small leftovers once the big list
is exhausted).  The memory guard WAITS, never skips.  Each cell runs in its own
process (wk9_s41_cell.py); a cell whose process dies (OOM) is recorded as
attempted-and-killed in /root/s41/failed.txt and the sweep continues.
Sceptical branch on any mult < a: 3a + 24 points, seed 907, both primes, must
reproduce; the vanishing vectors exhibited by wk9_s41_bite.py.  D > 0 writes
/root/s41/STOP and every worker stops.  Every cell is banked to
results/s41_ledger.md and committed before the next cell starts.

usage: python3 wk9_s41_sweep.py <small|big> [--frontier 20000] [--headroom 0.85] [--small-cap 5000] [--dry]
"""
import sys, os, time, json, pickle, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
LEDGER = os.path.join(ROOT, 'results', 's41_ledger.md')
CELLS = os.path.join(ROOT, 'results', 's41_cells')
WORK = '/root/s41'
CLAIMS = os.path.join(WORK, 'claims')
STOP = os.path.join(WORK, 'STOP')
FAILED = os.path.join(WORK, 'failed.txt')
CENSUS = os.path.join(WORK, 'census.pkl')
MEM_PEAK_INPL = 1.4e-8; MEM_INPL_BASE = 0.4

HEADER = """# Session 41 ledger — the six-row frontier (`n = 4`, `ℓ(λ) = 6`, `a ≥ 1`, `δ = 7, 8`)

Pipeline: the stabiliser reduction `analysis/wk9_s36_stabred.py` unchanged up to the kernel; kernel by the
in-place rref route of `analysis/wk9_s41_kernel.py` (validated in `results/s41_validation.md`: identical
kernel span to s36's exact and compressed routes on nine cells, both primes), every kernel vector verified
against the uncompressed raising-operator rows; `a` by kernel dimension AND by plethysm (asserted equal);
`rank(R) = n_χ − a` asserted; ranks by python-flint `nmod_mat` over `2147483647` and `2147483629`;
`a + 8` evaluation points per side; sceptical branch (`3a + 24` fresh points, seed 907, both primes) on any
`mult < a`.  **Points.**  det: `det_4(Σ s_i A_i)`, random integer `4×4` `A_i`.  pad: the **true
padded-permanent restriction** `x_0 · per_3(x_1..x_9)` with each `x_t` a random linear form in `s_1..s_6`
(`per_padded(3,4)` through `restrict()`) — never `l · (random cubic)`.  `mult_red` is the point-free
reducibility multiplicity by (★) (`docs/reducible_ideal.md`, Corollary A); at `r = 6`, `mult_pad ≤ mult_red`
with a strict gap iff a permanent-specific equation exists.  `m_det` is the symmetric rectangular Kronecker
bound (`mult_det ≤ m_det`).  Convention `D = mult_pad − mult_det`; only `D > 0` is an obstruction.
`HWM` is the cell's own peak resident set (GB), one process per cell.

| delta | lam | a | m_det | N_S | Stab | n_chi | rows | route | mult_det | mult_pad | mult_red | D | secs | HWM |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
"""

def log(*a):
    print(time.strftime('%H:%M:%S'), *a, flush=True)

def free_gb():
    for ln in open('/proc/meminfo'):
        if ln.startswith('MemAvailable:'): return int(ln.split()[1]) / 1048576.0
    return 0.0

def predicted_gb(x):
    if x['n_chi'] <= 800: return 0.5
    return MEM_PEAK_INPL * x['n_chi'] ** 2 + MEM_INPL_BASE

def wait_for_memory(gb, tag, headroom):
    while gb > headroom * free_gb():
        log(f"   [mem] {tag} needs ~{gb:.1f} GB, {free_gb():.1f} GB free -- waiting")
        time.sleep(60)

def key(lam, delta): return "%d_%s" % (delta, "_".join(map(str, lam)))

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
    if not os.path.exists(LEDGER): return out
    for ln in open(LEDGER):
        if ln.startswith('| 7 |') or ln.startswith('| 8 |'):
            c = [x.strip() for x in ln.strip().strip('|').split('|')]
            out.add((eval(c[1].strip('`')), int(c[0])))
    return out

def failed():
    out = set()
    if os.path.exists(FAILED):
        for ln in open(FAILED):
            if ln.strip():
                d, l = ln.split()[:2]
                out.add((eval(l), int(d)))
    return out

def bank(line):
    new = not os.path.exists(LEDGER)
    with open(LEDGER, 'a') as fh:
        if new: fh.write(HEADER)
        fh.write(line + "\n"); fh.flush(); os.fsync(fh.fileno())

def commit(msg):
    subprocess.run(['git', '-C', ROOT, 'add', 'results/s41_ledger.md'], capture_output=True)
    if os.path.isdir(CELLS):
        subprocess.run(['git', '-C', ROOT, 'add', 'results/s41_cells'], capture_output=True)
    subprocess.run(['git', '-C', ROOT, '-c', 'user.name=s41', '-c', 'user.email=s41@gct', 'commit', '-q', '-m',
                    msg + "\n\nCo-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>\n"
                    "Claude-Session: https://claude.ai/code/session_01H25jyjcL346hHpBdn8L7dT"], capture_output=True)

def order(census, frontier):
    """the pre-registered order; returns [(phase, cell)]"""
    def reach(x): return x['approx'] == '' and x['n_chi'] <= frontier
    seq, used = [], set()
    def take(x, phase):
        k = (x['lam'], x['delta'])
        if k in used: return
        used.add(k); seq.append((phase, x))
    forced = [x for d in sorted(census) for x in census[d] if x['forced'] and reach(x)]
    for x in sorted(forced, key=lambda x: (x['n_chi'], x['lam'])): take(x, 'forced')
    for d in sorted(census):
        cells = [x for x in census[d] if reach(x) and not x['banked'] and (x['lam'], d) not in used]
        asc = sorted(cells, key=lambda x: (x['n_chi'], x['lam']))
        probes = [sorted(cells, key=lambda x: (-x['a'], x['bal'], x['n_chi'])),
                  sorted(cells, key=lambda x: (x['bal'], -x['a'], x['n_chi']))]
        k, turn = 0, 0
        for x in asc:
            if (x['lam'], d) in used: continue
            take(x, f'd{d}'); k += 1
            if k % 3 == 0:
                for pr in probes[turn % 2]:
                    if (pr['lam'], d) not in used:
                        take(pr, f'd{d}-probe'); break
                turn += 1
    return seq

def run_subprocess(args, logfile):
    with open(logfile, 'a') as lf:
        pr = subprocess.run([sys.executable, os.path.join(HERE, 'wk9_s41_cell.py')] + args,
                            stdout=subprocess.PIPE, stderr=lf, text=True)
    res = None
    for ln in pr.stdout.splitlines():
        if ln.startswith('RESULT '): res = json.loads(ln[7:])
    return pr.returncode, res

def run_cell(phase, x, who, headroom):
    lam, delta, a = x['lam'], x['delta'], x['a']
    tag = f"{phase} {lam} d={delta} a={a} n_chi={x['n_chi']}"
    if os.path.exists(STOP): return 'stop'
    wait_for_memory(predicted_gb(x), tag, headroom)
    if os.path.exists(STOP): return 'stop'
    if not claim(lam, delta, who): return None
    log(f"START {tag} (pred {predicted_gb(x):.1f} GB, free {free_gb():.1f})")
    os.makedirs(WORK, exist_ok=True)
    pk = os.path.join(WORK, 'cell_%s.pkl' % key(lam, delta))
    lf = os.path.join(ROOT, 'results', 'logs', f's41_cells_{who}.log')
    route = 'exact' if x['n_chi'] <= 800 else 'inplace'
    rc, res = run_subprocess(['--lam', ','.join(map(str, lam)), '--delta', str(delta), '--a', str(a),
                              '--out', pk, '--route', route], lf)
    if rc != 0 or res is None:
        with open(FAILED, 'a') as fh: fh.write(f"{delta} {str(lam).replace(' ', '')} rc={rc} n_chi={x['n_chi']}\n")
        log(f"FAILED {tag}: rc={rc} (recorded in failed.txt)")
        return 'failed'
    note = ''
    for sd in ('det', 'pad'):
        if res['mult_' + sd] < a:
            log(f"  *** {tag}: mult_{sd} = {res['mult_'+sd]} < a = {a}: sceptical branch (3a+24 pts, seed 907)")
            pk2 = os.path.join(WORK, 'cell_%s_sceptical.pkl' % key(lam, delta))
            rc2, res2 = run_subprocess(['--lam', ','.join(map(str, lam)), '--delta', str(delta), '--a', str(a),
                                        '--out', pk2, '--route', route, '--npts', str(3 * a + 24),
                                        '--seed-det', '907', '--seed-pad', '907'], lf)
            assert rc2 == 0 and res2 is not None, ("sceptical re-run failed", lam, rc2)
            assert res2['mult_' + sd] == res['mult_' + sd], ("short rank unstable", lam, sd, res['mult_' + sd], res2['mult_' + sd])
            os.makedirs(CELLS, exist_ok=True)
            with open(os.path.join(CELLS, "%s_%s.txt" % (key(lam, delta), sd)), 'w') as fh:
                fh.write(f"# {tag}: mult_{sd} = {res['mult_'+sd]} < a = {a}; re-run 3a+24 = {3*a+24} points seed 907: {res2['mult_'+sd]}; "
                         f"mult_red = {res['mult_red']}\n")
            bl = os.path.join(ROOT, 'results', 'logs', f's41_bite_{key(lam, delta)}_{sd}.log')
            with open(bl, 'a') as bf:
                subprocess.run([sys.executable, os.path.join(HERE, 'wk9_s41_bite.py'), pk, sd], stdout=bf, stderr=bf, text=True)
            note += f' {sd}-bite'
    D = res['mult_pad'] - res['mult_det']
    line = (f"| {delta} | `{lam}` | {a} | {x['m_det']} | {res['N_S']} | {res['stab']} | {res['n_chi']} | {res['nrows']} | "
            f"{res['route']} | {res['mult_det']} | {res['mult_pad']} | {res['mult_red']} | {D:+d} | {res['secs']:.0f} | {res['hwm']:.2f} |")
    bank(line)
    commit(f"s41: bank {phase} {lam} delta={delta}: a={a} mult_det={res['mult_det']} mult_pad={res['mult_pad']} "
           f"mult_red={res['mult_red']} D={D:+d}{note}")
    log(line)
    if D > 0:
        open(STOP, 'w').write(f"D>0 at {lam} delta={delta}\n")
        log("*** D > 0: STOP-EVERYTHING — obstruction protocol ***")
        return 'stop'
    return D

if __name__ == '__main__':
    who = sys.argv[1]
    frontier = int(sys.argv[sys.argv.index('--frontier') + 1]) if '--frontier' in sys.argv else 20000
    headroom = float(sys.argv[sys.argv.index('--headroom') + 1]) if '--headroom' in sys.argv else 0.85
    small_cap = int(sys.argv[sys.argv.index('--small-cap') + 1]) if '--small-cap' in sys.argv else 5000
    census = pickle.load(open(CENSUS, 'rb'))
    seq = order(census, frontier)
    if '--dry' in sys.argv:
        for ph, x in seq:
            print(ph, x['delta'], x['lam'], 'a', x['a'], 'm_det', x['m_det'], 'n_chi', x['n_chi'], 'bal', x['bal'],
                  f"pred {predicted_gb(x):.2f} GB")
        print(len(seq), 'cells;', sum(x['a'] for _, x in seq), 'units')
        sys.exit(0)
    mine = [(ph, x) for ph, x in seq if (x['n_chi'] <= small_cap) == (who == 'small')]
    rest = [(ph, x) for ph, x in seq if (ph, x) not in mine] if who == 'big' else []
    log(f"worker {who}: {len(mine)} cells in class, frontier {frontier}, headroom {headroom}")
    for ph, x in mine + rest:
        if os.path.exists(STOP): log("STOP flag present; exiting"); break
        k = (x['lam'], x['delta'])
        if k in banked() or k in failed(): continue
        if os.path.exists(os.path.join(CLAIMS, key(*k) + '.claim')): continue
        r = run_cell(ph, x, who, headroom)
        if r == 'stop': break
    log(f"worker {who} done")

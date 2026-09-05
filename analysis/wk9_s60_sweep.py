#!/usr/bin/env python3
"""
Session 60 -- the sweep driver: one cell per process, cheapest first, banked
as it completes, halted on a refutation.

Each cell runs as   bash -c 'ulimit -v <kb>; exec timeout <s> python3 analysis/wk9_s60_cell.py ...'
with the child's process id written to results/logs/<tag>_<cell>.pid, its stderr
to results/logs/<tag>_<cell>.log, and its RESULT line appended to the ledger
JSONL; a cell that exceeds its timeout or fails is banked as DEFER with the
return code and the tail of its log.  The sweep stops when a banked cell has
mult_red > mult_det (the halt rule of PREREG_s60.md sec. 4).

usage: python3 analysis/wk9_s60_sweep.py --census results/s60_census.json --out results/s60_cells.jsonl
          [--tag s60_sweep] [--deltas 6,7,8,9] [--max-key 1e12] [--max-nchi N] [--limit N]
          [--timeout 7200] [--ulimit-gb 5.5] [--dense-cap 4000] [--red-points-nchi 20000]
          [--certs results/certs/s60] [--include-dead] [--cells FILE.json]
"""
import sys, os, json, time, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))


def log(*a):
    print(*a, file=sys.stderr, flush=True)


def banked(path):
    out = {}
    if not os.path.exists(path): return out
    for ln in open(path):
        ln = ln.strip()
        if not ln: continue
        r = json.loads(ln)
        out[(tuple(r['lam']), r['delta'])] = r
    return out


def arg(args, name, default):
    if name in args:
        v = args[args.index(name) + 1]
        return type(default)(v) if not isinstance(default, bool) else v
    return default


if __name__ == '__main__':
    args = sys.argv[1:]
    census = arg(args, '--census', os.path.join(ROOT, 'results/s60_census.json'))
    out = arg(args, '--out', os.path.join(ROOT, 'results/s60_cells.jsonl'))
    tag = arg(args, '--tag', 's60_sweep')
    deltas = [int(x) for x in arg(args, '--deltas', '6,7,8,9').split(',')]
    max_key = float(arg(args, '--max-key', '1e30'))
    max_nchi = int(arg(args, '--max-nchi', '1000000000'))
    limit = int(arg(args, '--limit', '100000'))
    tmo = int(arg(args, '--timeout', '7200'))
    ulim_kb = int(float(arg(args, '--ulimit-gb', '5.5')) * 1048576)
    dense_cap = int(arg(args, '--dense-cap', '4000'))
    red_pts_nchi = int(arg(args, '--red-points-nchi', '20000'))
    certs = arg(args, '--certs', os.path.join(ROOT, 'results/certs/s60'))
    include_dead = '--include-dead' in args
    cells_file = arg(args, '--cells', '')
    logdir = os.path.join(ROOT, 'results/logs'); os.makedirs(logdir, exist_ok=True)
    if cells_file:
        todo = json.load(open(cells_file))
    else:
        C = json.load(open(census))
        todo = [c for d in deltas for c in C[str(d)]['cells']]
        todo = [c for c in todo if (include_dead or c['red'] == 'informative')]
        todo.sort(key=lambda c: (c['key'], c['N_S']))
    done = banked(out)
    n = 0; t_start = time.time()
    with open(os.path.join(logdir, f'{tag}.pid'), 'w') as f: f.write(str(os.getpid()) + "\n")
    for c in todo:
        lam = tuple(c['lam']); d = c['delta']
        if (lam, d) in done and done[(lam, d)].get('status') != 'DEFER': continue
        if (c.get('key') or 0) > max_key or (c.get('n_chi') or 0) > max_nchi: continue
        if n >= limit: break
        n += 1
        name = f"{tag}_{'_'.join(map(str, lam))}_d{d}"
        red_mode = 'always' if (c.get('n_chi') or 0) <= red_pts_nchi else 'dense'
        cmd = (f"ulimit -v {ulim_kb}; exec timeout {tmo} python3 {os.path.join(ROOT, 'analysis/wk9_s60_cell.py')} "
               f"{d} {' '.join(map(str, lam))} --route auto --dense-cap {dense_cap} --red-points {red_mode} "
               f"--certs {certs}" + (f" --a {c['a']}" if c.get('a') is not None else '') + (f" --hpad {c['h_pad']}" if c.get('h_pad') is not None else ''))
        log(f"[{tag}] {n}: d{d} {lam} a={c.get('a')} h_pad={c.get('h_pad')} n_chi~{c.get('n_chi')} "
            f"N_S={c.get('N_S')} red_points={red_mode} ...")
        t0 = time.time()
        with open(os.path.join(logdir, name + '.log'), 'w') as lf:
            p = subprocess.Popen(['bash', '-c', cmd], stdout=subprocess.PIPE, stderr=lf, text=True, cwd=ROOT)
            with open(os.path.join(logdir, name + '.pid'), 'w') as f: f.write(str(p.pid) + "\n")
            so, _ = p.communicate()
        last = [l for l in so.strip().split('\n') if l.startswith('RESULT ')]
        if p.returncode != 0 or not last:
            tail = open(os.path.join(logdir, name + '.log')).read().strip().split('\n')[-3:]
            rec = dict(lam=list(lam), delta=d, a=c.get('a'), h_pad=c.get('h_pad'), N_S=c.get('N_S'),
                       n_chi=c.get('n_chi'), status='DEFER', rc=p.returncode, secs=round(time.time() - t0, 1),
                       timeout=tmo, tail=tail)
        else:
            rec = json.loads(last[-1][len('RESULT '):])
            rec['status'] = 'measured'
            rec['h_pad'] = c.get('h_pad'); rec['red_class'] = c.get('red'); rec['census_key'] = c.get('key')
        with open(out, 'a') as fh:
            fh.write(json.dumps(rec) + "\n")
        log(f"[{tag}] banked d{d} {lam}: {rec.get('status')} route={rec.get('route')} "
            f"mult_det={rec.get('mult_det')} mult_red(star)={rec.get('mult_red_star')} "
            f"mult_red(pts)={rec.get('mult_red_pts')} D={rec.get('D')} ok={rec.get('ok')} "
            f"({rec.get('secs')}s, HWM {rec.get('hwm_gb')} GB) [{round(time.time()-t_start)}s elapsed]")
        if rec.get('refute'):
            log(f"[{tag}] mult_red > mult_det at d{d} {lam} -- halting the sweep; the verification protocol takes over")
            break
        if rec.get('status') == 'measured' and not rec.get('ok', True):
            log(f"[{tag}] self-check failed at d{d} {lam} (primes disagree or (star) != points) -- halting for inspection")
            break
    log(f"[{tag}] done: {n} cells this run, {round(time.time()-t_start)}s")

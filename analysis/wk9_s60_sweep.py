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
          [--certs results/certs/s60] [--include-dead] [--cells FILE.json] [--by-ladder]

--by-ladder (integrator note, session 60): cells sharing a tail rho = (lam_2..lam_5)
form a ladder lam_delta = (4 delta - |rho|, rho); multiplication by the highest-weight
vector u = c_(4,0,0,0,0) is injective HWV_{lam_delta} -> HWV_{lam_{delta+1}} and descends
injectively to C[D_5] and C[R_5] (both irreducible, u vanishing on neither), so
a, mult_det, mult_red, i_det = a - mult_det and i_red = a - mult_red are all
non-decreasing in delta along a ladder.  Hence i_det = 0 (i_red = 0) at the TOP
measured member forces i_det = 0 (i_red = 0) at every lower member.  In this mode
the queue is grouped by tail, each ladder is entered at its most expensive-to-skip
end (largest delta) and, once that top is full rank on both sides, the lower
members are banked as 'implied' rows (source cell named) instead of being run.
A top that bites on either side implies nothing for the lower members' bitten
side, and they stay in the queue.
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
        extra = arg(args, '--census2', '')
        if extra:
            C.update(json.load(open(extra)))
        todo = [c for d in deltas for c in C[str(d)]['cells']]
        todo = [c for c in todo if (include_dead or c['red'] == 'informative')]
        todo.sort(key=lambda c: (c['key'], c['N_S']))
    by_ladder = '--by-ladder' in args
    if by_ladder:
        import collections
        lad = collections.defaultdict(list)
        for c in todo: lad[tuple(c['lam'][1:])].append(c)
        order = []
        for rho, mem in lad.items():
            mem.sort(key=lambda c: -c['delta'])                 # top (largest delta) first
            order.append((max(c['key'] for c in mem), mem))
        order.sort(key=lambda x: x[0])
        todo = [c for _, mem in order for c in mem]
        log(f"[{tag}] by-ladder: {len(lad)} tails, {len(todo)} cells; "
            f"{sum(1 for _, m in order if len(m) > 1)} tails with more than one member")
    done = banked(out)
    n = 0; t_start = time.time()

    def ladder_source(lam, d):
        """a banked higher-delta member of the same tail with mult_det = a (and its red status)."""
        rho = tuple(lam[1:])
        best = None
        for (l2, d2), r in done.items():
            if d2 > d and tuple(l2[1:]) == rho and r.get('status') in ('measured', 'implied') \
               and r.get('mult_det') is not None and r['mult_det'] == r['a']:
                if best is None or d2 > best[1]: best = (l2, d2, r)
        return best
    with open(os.path.join(logdir, f'{tag}.pid'), 'w') as f: f.write(str(os.getpid()) + "\n")
    for c in todo:
        lam = tuple(c['lam']); d = c['delta']
        if (lam, d) in done and done[(lam, d)].get('status') != 'DEFER': continue
        if (c.get('key') or 0) > max_key or (c.get('n_chi') or 0) > max_nchi: continue
        if n >= limit: break
        if by_ladder:
            src = ladder_source(lam, d)
            if src is not None:
                l2, d2, r2 = src
                red_full = (r2.get('mult_red') is not None and r2['mult_red'] == r2['a'])
                rec = dict(lam=list(lam), delta=d, ell=5, a=c['a'], h_pad=c.get('h_pad'), N_S=c.get('N_S'),
                           stab=c.get('stab'), n_chi=c.get('n_chi'), red_class=c.get('red'), census_key=c.get('key'),
                           status='implied', route='ladder',
                           source=dict(lam=list(l2), delta=d2, mult_det=r2['mult_det'], mult_red=r2.get('mult_red'), a=r2['a']),
                           mult_det=c['a'], mult_red=(c['a'] if red_full else None), mult_red_star=(c['a'] if red_full else None),
                           mult_red_pts=None, D=(0 if red_full else None), refute=False, ok=True, secs=0.0, hwm_gb=0.0,
                           note=('i_det = 0 and i_red = 0 at the higher member of the same ladder force both at every lower member '
                                 '(multiplication by u = c_(4,0,0,0,0) is injective and descends to C[D_5], C[R_5])'
                                 if red_full else
                                 'i_det = 0 at the higher member of the same ladder forces i_det = 0 here (mult_det = a); the '
                                 'reducible side of the source bites, so mult_red is only bounded here: a - (a_src - mult_red_src) <= mult_red <= a'))
                if not red_full:
                    rec['mult_red_lower_bound'] = c['a'] - (r2['a'] - r2['mult_red']) if r2.get('mult_red') is not None else None
                with open(out, 'a') as fh: fh.write(json.dumps(rec) + "\n")
                done[(lam, d)] = rec
                log(f"[{tag}] implied d{d} {lam} by d{d2} {tuple(l2)}: mult_det = a = {c['a']}"
                    + (f", mult_red = a" if red_full else f", mult_red bounded (source mult_red {r2.get('mult_red')} < a {r2['a']})"))
                continue
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
                       timeout=tmo, log_tail=tail)
            for k in ('closing', 'tail', 't', 'rungs_settled'):
                if k in c: rec[k] = c[k]
        else:
            rec = json.loads(last[-1][len('RESULT '):])
            rec['status'] = 'measured'
            rec['h_pad'] = c.get('h_pad'); rec['red_class'] = c.get('red'); rec['census_key'] = c.get('key')
            for k in ('closing', 'tail', 't', 'rungs_settled'):
                if k in c: rec[k] = c[k]
        with open(out, 'a') as fh:
            fh.write(json.dumps(rec) + "\n")
        done[(lam, d)] = rec
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

#!/usr/bin/env python3
"""
Session 71 -- the falsifier sweep over the frozen queue (results/s71_queue.json),
in pre-registered order, banking every cell with a commit.

Each cell runs as its own bounded process (`timeout`, `ulimit -v`, pid file):
    python3 analysis/wk11_s71_cell.py delta lam... --a A --hpad H --certs results/certs/s71 --out results/s71_sweep.jsonl
A cell that exceeds its bound is recorded as `not reached` with the bound.

Stopping rules (results/PREREG_s71.md sec. 6): any record with halt=True (D > 0,
i_det >= 1, i_per4 >= 1, prime disagreement, (star) != points) ends the sweep
and writes results/s71_HALT.json; the verification protocol takes over.  The
sweep also ends at the wall-clock deadline or by the information-rate rule.

usage: python3 analysis/wk11_s71_sweep.py [--deadline 2026-09-08T12:00:00Z] [--start-rank 1] [--max-rank 976]
          [--cost-scale 1.0] [--no-commit]
"""
import sys, os, json, time, subprocess, datetime
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))

QUEUE = os.path.join(ROOT, 'results', 's71_queue.json')
OUT = os.path.join(ROOT, 'results', 's71_sweep.jsonl')
CERTS = os.path.join(ROOT, 'results', 'certs', 's71')
LOGS = os.path.join(ROOT, 'results', 'logs')
HALT = os.path.join(ROOT, 'results', 's71_HALT.json')

# re-fitted cost model (results/s71_calibration.md); prior constants in the PREREG
CAL = dict(c_b=1.5e-6, rho=10.0, c_c=2e-7, c_h=1e-7, c_v=2e-8, f=0.005)


def log(*a):
    print(time.strftime('%H:%M:%S'), *a, file=sys.stderr); sys.stderr.flush()


def predict(q, cal):
    """re-fitted certified cost (results/s71_cost_refit.json) and the hybrid's memory per prime"""
    n = q['n_chi_census']; a = q['a']; N = q['N_S']; d = q['delta']
    nnz = cal['rho'] * n; U = a + cal['f'] * n
    mem = min(4.0 * n * U, 1.0e9) + 4.0 * n * a            # one X block (capped, blocked over U) + the uint32 kernel, per prime
    tb = cal['c_b'] * N * d; tc = cal['c_c'] * nnz * 5; th = cal['c_h'] * nnz * U + cal['c_v'] * nnz * a
    te = cal.get('c_e', 2.7e-8) * 3 * (a + 8) * N * d * (1 if 2 * mem < 3.0e9 else 2)
    tr = cal.get('c_r', 1e-9) * 3 * (a + 8) * n * a
    return tb + tc + th + te + tr, mem


def done_cells():
    done = {}
    if os.path.exists(OUT):
        for line in open(OUT):
            r = json.loads(line); done[(tuple(r['lam']), r['delta'])] = r
    return done


def commit(msg, paths):
    subprocess.run(['git', '-C', ROOT, 'add'] + paths, check=False)
    subprocess.run(['git', '-C', ROOT, '-c', 'user.name=s71 worker', '-c', 'user.email=s71@gct.local', 'commit', '-q', '-m',
                    msg + "\n\nCo-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"], check=False)


if __name__ == '__main__':
    args = sys.argv[1:]
    def arg(name, default):
        return type(default)(args[args.index(name) + 1]) if name in args else default
    deadline = datetime.datetime.strptime(arg('--deadline', '2026-09-08T12:00:00Z'), '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=datetime.timezone.utc)
    start_rank = arg('--start-rank', 1); max_rank = arg('--max-rank', 976)
    cal = dict(CAL)
    if os.path.exists(os.path.join(ROOT, 'results', 's71_cost_refit.json')):
        cal.update(json.load(open(os.path.join(ROOT, 'results', 's71_cost_refit.json')))['constants'])
    no_commit = '--no-commit' in args
    queue = json.load(open(QUEUE))
    os.makedirs(CERTS, exist_ok=True); os.makedirs(LOGS, exist_ok=True)
    done = done_cells()
    log(f"sweep: {len(queue)} cells in queue, {len(done)} done; deadline {deadline.isoformat()}; constants {cal}")
    recent = []
    for q in queue:
        if q['rank'] < start_rank or q['rank'] > max_rank: continue
        key = (tuple(q['lam']), q['delta'])
        if key in done: continue
        if os.path.exists(HALT):
            log("HALT marker present; not starting another cell"); break
        now = datetime.datetime.now(datetime.timezone.utc)
        pred, mem = predict(q, cal)
        remaining = (deadline - now).total_seconds()
        if pred > remaining:
            log(f"rank {q['rank']} {q['lam']} d{q['delta']}: predicted {pred:.0f}s exceeds the remaining budget {remaining:.0f}s; sweep ends (rule 5)")
            break
        if q['N_S'] * q['delta'] > 2.0e8:
            log(f"rank {q['rank']} {q['lam']}: beyond reach of the build in this container (N_S*delta = {q['N_S']*q['delta']:.2e} > 2e8); sweep ends")
            break
        bound = int(min(max(10 * pred, 1200), 4 * 3600))
        tag = '_'.join(map(str, q['lam'])) + f"_d{q['delta']}"
        logf = os.path.join(LOGS, f's71_cell_{tag}.log')
        cmd = ['python3', os.path.join(HERE, 'wk11_s71_cell.py'), str(q['delta'])] + [str(x) for x in q['lam']] + \
              ['--a', str(q['a']), '--hpad', str(q['h_pad']), '--certs', CERTS, '--out', OUT]
        log(f"rank {q['rank']}/{len(queue)} {q['lam']} d{q['delta']}: a={q['a']} n_chi~{q['n_chi_census']} predicted {pred:.0f}s "
            f"(prior {q['pred_cost_s']}s), bound {bound}s, mem {mem/1e9:.2f} GB")
        t0 = time.time()
        with open(logf, 'w') as lf:
            proc = subprocess.Popen(['bash', '-c', f'ulimit -v 6500000; exec timeout {bound} ' + ' '.join(cmd)], stdout=lf, stderr=subprocess.STDOUT)
            with open(os.path.join(LOGS, 's71_cell.pid'), 'w') as pf: pf.write(str(proc.pid))
            rc = proc.wait()
        secs = time.time() - t0
        rec = None
        for line in open(logf):
            if line.startswith('RESULT '): rec = json.loads(line[7:])
        if rec is None:
            nr = dict(lam=q['lam'], delta=q['delta'], a=q['a'], h_pad=q['h_pad'], rank=q['rank'], status='not reached',
                      bound_secs=bound, rc=rc, secs=round(secs, 1), pred_secs=round(pred, 1), pred_secs_prior=q['pred_cost_s'])
            with open(OUT, 'a') as f: f.write(json.dumps(nr) + "\n")
            log(f"  not reached (rc {rc}, {secs:.0f}s of {bound}s)")
            if not no_commit: commit(f"s71 sweep: {q['lam']} d{q['delta']} not reached within {bound}s", [OUT])
            recent.append((secs, 0))
            continue
        # annotate the banked line with the queue data (the cell script wrote the raw line; rewrite it with rank/predictions)
        lines = open(OUT).read().splitlines()
        last = json.loads(lines[-1]); assert tuple(last['lam']) == key[0] and last['delta'] == key[1]
        last.update(rank=q['rank'], pred_secs=round(pred, 1), pred_secs_prior=q['pred_cost_s'], pred_route=q['pred_route'],
                    tail=q['tail'], t=q['t'], rungs=q['rungs'], n_chi_census=q['n_chi_census'], status='measured')
        lines[-1] = json.dumps(last)
        open(OUT, 'w').write("\n".join(lines) + "\n")
        log(f"  RESULT a={last['a']} n_chi={last['n_chi']} |U|={last['n_chi'] - last['cover_E']['size']} i_det={last['i_det']} "
            f"i_red={last['i_red']} i_per4={last['i_per4']} D={last['D']} ({last['secs']}s, pred {pred:.0f}s){'  HALT' if last['halt'] else ''}")
        if not no_commit:
            commit(f"s71 sweep rank {q['rank']}: {q['lam']} d{q['delta']} a={last['a']} i_det={last['i_det']} i_red={last['i_red']} "
                   f"i_per4={last['i_per4']} D={last['D']} ({last['secs']}s)", [OUT, CERTS])
        if last['halt']:
            json.dump(dict(cell=last, reason='halt condition (PREREG sec. 6)'), open(HALT, 'w'), indent=1)
            log("*** HALT: the verification protocol takes over ***")
            if not no_commit: commit(f"s71 sweep HALT at {q['lam']} d{q['delta']}", [HALT])
            break
        recent.append((secs, 1))
        # information-rate rule: the last three cells cost more than everything before them, one tail each
        if len(recent) >= 6:
            tail3 = sum(s for s, _ in recent[-3:]); before = sum(s for s, _ in recent[:-3])
            if tail3 > before and all(c == 1 for _, c in recent[-3:]) and before > 3600:
                log(f"information rate flattened: last three cells {tail3:.0f}s > everything before {before:.0f}s; sweep ends (rule 5)")
                break
    log("sweep loop ended")

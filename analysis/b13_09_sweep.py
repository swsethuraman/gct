#!/usr/bin/env python3
"""
B13-09 -- the cubic-side scan I(D_r^{per_3})_delta at length r in {7, 8}, weights
of the pre-registered queue in N_S order, one weight per bounded subprocess
(analysis/b13_09_per_r.py), banking each result as it completes and halting at
the first drop.

Bounds, per docs/brief_wording.md sec. 1: every subprocess is launched under
`timeout` (wall clock) and `ulimit -v` (address space); the sweep's own process
id is in results/logs/<run>.pid and the current child's in
results/logs/<run>_child.pid, so a run that must end early is ended by a
recorded id, never by name.

usage: python3 analysis/b13_09_sweep.py r delta [--census results/b13_09_census.json]
          [--out results/b13_09/per_r7_d9.jsonl] [--certs results/certs/b13_09] [--no-certs]
          [--until HH:MM (UTC)] [--max-ns N] [--max-nsd N] [--weight-timeout S] [--ulimit-kb KB]
          [--commit] [--run NAME] [--order N_S|cost] [--max-cost SECONDS]
"""
import json, os, subprocess, sys, time, datetime

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..'))


def arg(args, name, default):
    return type(default)(args[args.index(name) + 1]) if name in args else default


def main(argv):
    r, delta = int(argv[0]), int(argv[1])
    census = arg(argv, '--census', os.path.join(ROOT, 'results', 'b13_09_census.json'))
    run = arg(argv, '--run', f'b13_09_r{r}_d{delta}')
    out = arg(argv, '--out', os.path.join(ROOT, 'results', 'b13_09', f'per_r{r}_d{delta}.jsonl'))
    certs = arg(argv, '--certs', os.path.join(ROOT, 'results', 'certs', 'b13_09'))
    until = arg(argv, '--until', '')
    max_ns = float(arg(argv, '--max-ns', '1e12'))
    max_nsd = float(arg(argv, '--max-nsd', '1.5e8'))          # s79's build wall in a 7 GB box; the boundary, reported with its N_S*delta
    timeout_s = int(arg(argv, '--weight-timeout', 5400))
    ulimit_kb = int(arg(argv, '--ulimit-kb', 6500000))
    do_commit = '--commit' in argv
    max_cost = float(arg(argv, '--max-cost', '0'))
    Q = json.load(open(census))['cells'][f'r{r}_d{delta}']
    # order: 'N_S' is the pre-registered order of PREREG sec. 3.3; 'cost' is the refitted
    # c1*N_S*delta + c2*|Stab|*N_S of Addendum C, which at lengths 7-8 is a different order
    # because the orbit setup costs O(|Stab| * N_S) and |Stab| reaches 5040 here.
    order_by = arg(argv, '--order', 'N_S')
    if order_by == 'cost':
        assert all('cost_model_s' in c for c in Q), 'census not repriced: run analysis/b13_09_costfit.py --reprice'
        Q = sorted(Q, key=lambda c: (c['cost_model_s'], c['mu']))
    else:
        Q = sorted(Q, key=lambda c: (c['N_S'], c['mu']))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    os.makedirs(os.path.join(ROOT, 'results', 'logs'), exist_ok=True)
    with open(os.path.join(ROOT, 'results', 'logs', f'{run}.pid'), 'w') as f: f.write(str(os.getpid()) + '\n')
    done = {}
    if os.path.exists(out):
        for ln in open(out):
            try:
                rec = json.loads(ln); done[(tuple(rec['mu']), rec['delta'])] = rec
            except Exception:
                pass
    deadline = None
    if until:
        hh, mm = map(int, until.split(':'))
        now = datetime.datetime.utcnow()
        deadline = now.replace(hour=hh, minute=mm, second=0, microsecond=0)
        if deadline <= now: deadline += datetime.timedelta(days=1)
    status_path = os.path.join(ROOT, 'results', 'b13_09', f'status_r{r}_d{delta}.json')
    status = dict(board_numbering='batch13', session='B13-09', r=r, delta=delta, run=run,
                  started=datetime.datetime.utcnow().isoformat(), weights=len(Q), bounds=dict(weight_timeout_s=timeout_s, ulimit_v_kb=ulimit_kb,
                  max_N_S=max_ns, max_NS_delta=max_nsd, until_utc=until or None, order=order_by), reached=[], not_reached=[], halted=None)
    log_path = os.path.join(ROOT, 'results', 'logs', f'{run}.log')
    child_pid_path = os.path.join(ROOT, 'results', 'logs', f'{run}_child.pid')

    def save():
        status['updated'] = datetime.datetime.utcnow().isoformat()
        json.dump(status, open(status_path, 'w'), indent=1)

    for rank, c in enumerate(Q, 1):
        key = (tuple(c['mu']), delta)
        base = dict(rank=rank, mu=c['mu'], a=c['a'], N_S=c['N_S'], NS_delta=c['NS_delta'])
        if key in done:
            rec = done[key]
            status['reached'].append(dict(base, n_chi=rec.get('n_chi'), mult=rec.get('mult'), units=rec.get('units'), halt=rec.get('halt'),
                                          secs=rec.get('secs'), hwm_gb=rec.get('hwm_gb'), status='banked earlier'))
            if rec.get('halt'):
                status['halted'] = status['reached'][-1]; save(); print("HALT (banked earlier)", flush=True); return 2
            continue
        if deadline and datetime.datetime.utcnow() >= deadline:
            status['not_reached'].append(dict(base, reason='wall clock')); continue
        if c['N_S'] > max_ns:
            status['not_reached'].append(dict(base, reason=f'above the N_S cap {max_ns:g}')); continue
        if max_cost and c.get('cost_model_s', 0) > max_cost:
            status['not_reached'].append(dict(base, cost_model_s=c.get('cost_model_s'),
                                              reason=f"above the per-weight refitted-cost cap {max_cost:g} s")); continue
        if c['NS_delta'] > max_nsd:
            status['not_reached'].append(dict(base, reason=f'above the N_S*delta cap {max_nsd:g} (the build wall)')); continue
        cmd = ['python3', os.path.join(HERE, 'b13_09_per_r.py'), str(delta)] + [str(x) for x in c['mu']] + ['--out', out, '--a', str(c['a'])] + \
              ([] if '--no-certs' in argv else ['--certs', certs])
        t0 = time.time()
        with open(log_path, 'a') as lf:
            lf.write(f"\n=== rank {rank}/{len(Q)} {key} N_S {c['N_S']} a {c['a']} NS*delta {c['NS_delta']} {datetime.datetime.utcnow().isoformat()}\n"); lf.flush()
            pr = subprocess.Popen(['timeout', str(timeout_s)] + cmd, stdout=subprocess.PIPE, stderr=lf, text=True,
                                  preexec_fn=(lambda: __import__('resource').setrlimit(__import__('resource').RLIMIT_AS, (ulimit_kb * 1024, ulimit_kb * 1024))))
            with open(child_pid_path, 'w') as f: f.write(f"{pr.pid} {key} {datetime.datetime.utcnow().isoformat()}\n")
            stdout, _ = pr.communicate()
            rc = pr.returncode
        wall = round(time.time() - t0, 1)
        res = None
        for line in stdout.splitlines():
            if line.startswith('RESULT '): res = json.loads(line[7:])
        if res is None:
            reason = f'timeout {timeout_s}s' if rc == 124 else f'no result (rc {rc}; memory bound {ulimit_kb} kB or an assertion -- see the log)'
            status['not_reached'].append(dict(base, reason=reason, wall=wall)); save()
            print(f"[{rank}/{len(Q)}] r{r} d{delta} {key[0]} NOT REACHED: {reason} ({wall}s)", flush=True)
            continue
        rec = dict(base, n_chi=res.get('n_chi'), mult=res['mult'], units=res['units'], halt=res['halt'], secs=res['secs'],
                   hwm_gb=res.get('hwm_gb'), build_secs=res.get('build_secs'), wall=wall, status=res['status'])
        status['reached'].append(rec); save()
        print(f"[{rank}/{len(Q)}] r{r} d{delta} {key[0]} a={res['a']} N_S={res.get('N_S')} n_chi={res.get('n_chi')} mult={res['mult']} units={res['units']} ({wall}s, HWM {res.get('hwm_gb')} GB)", flush=True)
        if do_commit:
            # two streams and the session both commit into one repository: serialise on a
            # lock file so a concurrent write can never leave a half-staged index (the
            # 'cannot lock ref HEAD' race, seen once here before this was added).
            msg = (f"B13-09: bank r={r} d={delta} {tuple(c['mu'])} a={res['a']} mult={res['mult']} units={res['units']}\n\n"
                   f"Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>")
            # NO session-link trailer.  Removed at batch-13 integration: this line
            # re-emitted it on every banked weight, and a history rewrite does not
            # fix a script.  Same defect class as analysis/wk9_s41_sweep.py:117.
            lock = os.path.join(ROOT, 'results', 'logs', 'b13_09_git.lock')
            subprocess.run(['flock', lock, 'sh', '-c',
                            f'cd {ROOT} && git add {out} {status_path} && git commit -q -F -'],
                           input=msg, text=True, check=False)
        if res['halt']:
            status['halted'] = rec; save()
            print("HALT: a drop on the cubic side -- the verification protocol takes over", flush=True)
            return 2
    save()
    print(f"r {r} delta {delta}: queue exhausted ({len(status['reached'])} reached, {len(status['not_reached'])} not reached)", flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

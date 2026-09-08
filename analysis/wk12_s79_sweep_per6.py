#!/usr/bin/env python3
"""
Session 79 -- the cubic-side scan I(D_6^{per_3})_delta, weights in N_S order,
one weight per subprocess (analysis/wk12_s79_per6.py), halting at the first drop.

usage: python3 analysis/wk12_s79_sweep_per6.py delta [--queue results/s79_per6_queue.json]
                 [--out results/s79_per6.jsonl] [--certs results/certs/s79_per6] [--until HH:MM] [--max-ns 3e7]
"""
import json, os, subprocess, sys, time, datetime

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..'))


def arg(args, name, default):
    return type(default)(args[args.index(name) + 1]) if name in args else default


def main(argv):
    delta = int(argv[0])
    queue = arg(argv, '--queue', os.path.join(ROOT, 'results', 's79_per6_queue.json'))
    out = arg(argv, '--out', os.path.join(ROOT, 'results', 's79_per6.jsonl'))
    certs = arg(argv, '--certs', os.path.join(ROOT, 'results', 'certs', 's79_per6'))
    until = arg(argv, '--until', '')
    max_ns = float(arg(argv, '--max-ns', '3e7'))
    timeout_s = arg(argv, '--weight-timeout', 5400)
    Q = json.load(open(queue))[str(delta)]
    done = set()
    if os.path.exists(out):
        for ln in open(out):
            try:
                r = json.loads(ln); done.add((tuple(r['mu']), r['delta']))
            except Exception:
                pass
    deadline = None
    if until:
        hh, mm = map(int, until.split(':'))
        now = datetime.datetime.utcnow()
        deadline = now.replace(hour=hh, minute=mm, second=0, microsecond=0)
        if deadline <= now: deadline += datetime.timedelta(days=1)
    status_path = os.path.join(ROOT, 'results', f's79_per6_status_d{delta}.json')
    status = dict(delta=delta, started=datetime.datetime.utcnow().isoformat(), weights=len(Q), reached=[], not_reached=[], halted=None)
    log_path = os.path.join(ROOT, 'results', 'logs', f's79_per6_d{delta}.log')
    for rank, c in enumerate(Q, 1):
        key = (tuple(c['mu']), delta)
        if key in done:
            status['reached'].append(dict(rank=rank, mu=c['mu'], a=c['a'], N_S=c['N_S'], status='banked earlier')); continue
        if deadline and datetime.datetime.utcnow() >= deadline:
            status['not_reached'].append(dict(rank=rank, mu=c['mu'], a=c['a'], N_S=c['N_S'], reason='wall clock')); continue
        if c['N_S'] > max_ns:
            status['not_reached'].append(dict(rank=rank, mu=c['mu'], a=c['a'], N_S=c['N_S'], reason='above the N_S cap')); continue
        cmd = ['python3', os.path.join(HERE, 'wk12_s79_per6.py'), str(delta)] + [str(x) for x in c['mu']] + ['--out', out, '--certs', certs]
        t0 = time.time()
        with open(log_path, 'a') as lf:
            lf.write(f"\n=== rank {rank} {key} N_S {c['N_S']} a {c['a']} {datetime.datetime.utcnow().isoformat()}\n"); lf.flush()
            try:
                pr = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=lf, timeout=timeout_s, text=True,
                                    preexec_fn=lambda: os.system('ulimit -v 6500000'))
            except subprocess.TimeoutExpired:
                status['not_reached'].append(dict(rank=rank, mu=c['mu'], a=c['a'], N_S=c['N_S'], reason=f'timeout {timeout_s}s')); continue
        res = None
        for line in pr.stdout.splitlines():
            if line.startswith('RESULT '): res = json.loads(line[7:])
        if res is None:
            status['not_reached'].append(dict(rank=rank, mu=c['mu'], a=c['a'], N_S=c['N_S'], reason=f'no result (rc {pr.returncode})')); continue
        rec = dict(rank=rank, mu=c['mu'], a=res['a'], N_S=res.get('N_S'), n_chi=res.get('n_chi'), mult=res['mult'], units=res['units'],
                   halt=res['halt'], secs=res['secs'], wall=round(time.time() - t0, 1))
        status['reached'].append(rec)
        json.dump(status, open(status_path, 'w'), indent=1)
        print(f"[{rank}/{len(Q)}] d{delta} {tuple(c['mu'])} a={res['a']} N_S={res.get('N_S')} n_chi={res.get('n_chi')} mult={res['mult']} units={res['units']} ({rec['wall']}s)", flush=True)
        if res['halt']:
            status['halted'] = rec; json.dump(status, open(status_path, 'w'), indent=1)
            print("HALT: a drop on the cubic side -- the verification protocol takes over", flush=True)
            return 2
    json.dump(status, open(status_path, 'w'), indent=1)
    print(f"delta {delta}: scan complete", flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

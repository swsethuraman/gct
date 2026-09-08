#!/usr/bin/env python3
"""
Session 79, part 2 -- the ell = 6 queue in cost order, one cell per subprocess.

Reads results/s79_queue.json (frozen at pre-registration: session 57's T1/T2
six-row nominees not in the record, by N_S*delta), skips cells already banked in
the output file, runs analysis/wk12_s79_cell6.py on each with a wall-clock and
memory bound, and stops at the first cell that HALTS (i_det >= 1, mult_pad <
mult_red, D > 0, i_per4 >= 1, or the primes disagree) -- the verification
protocol of results/PREREG_s79.md sec. 2.5 takes over from there.

usage: python3 analysis/wk12_s79_sweep6.py [--queue FILE] [--out FILE] [--certs DIR]
                                           [--max-cost 2e8] [--cell-timeout 7200] [--until HH:MM(UTC)]
"""
import json, os, subprocess, sys, time, datetime

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..'))


def arg(args, name, default):
    return type(default)(args[args.index(name) + 1]) if name in args else default


def main(argv):
    queue = arg(argv, '--queue', os.path.join(ROOT, 'results', 's79_queue.json'))
    out = arg(argv, '--out', os.path.join(ROOT, 'results', 's79_cells.jsonl'))
    certs = arg(argv, '--certs', os.path.join(ROOT, 'results', 'certs', 's79_cells'))
    max_cost = float(arg(argv, '--max-cost', '2e8'))
    cell_timeout = arg(argv, '--cell-timeout', 7200)
    until = arg(argv, '--until', '')
    log_path = os.path.join(ROOT, 'results', 'logs', 's79_sweep6.log')
    Q = json.load(open(queue))
    done = set()
    if os.path.exists(out):
        for ln in open(out):
            try:
                r = json.loads(ln); done.add((tuple(r['lam']), r['delta']))
            except Exception:
                pass
    status_path = os.path.join(ROOT, 'results', 's79_sweep6_status.json')
    status = dict(started=datetime.datetime.utcnow().isoformat(), queue=len(Q), reached=[], skipped_cost=[], not_reached=[], halted=None)
    for rank, c in enumerate(Q, 1):
        key = (tuple(c['lam']), c['delta'])
        if until:
            hh, mm = map(int, until.split(':'))
            now = datetime.datetime.utcnow()
            if (now.hour, now.minute) >= (hh, mm) and now.hour >= hh:
                status['not_reached'].append(dict(rank=rank, lam=c['lam'], delta=c['delta'], NS_delta=c['NS_delta'], reason='wall clock'))
                continue
        if key in done:
            status['reached'].append(dict(rank=rank, lam=c['lam'], delta=c['delta'], NS_delta=c['NS_delta'], status='banked earlier'))
            continue
        if c['NS_delta'] is None or c['NS_delta'] > max_cost:
            status['skipped_cost'].append(dict(rank=rank, lam=c['lam'], delta=c['delta'], NS_delta=c['NS_delta'], reason='above the build wall'))
            continue
        cmd = ['python3', os.path.join(HERE, 'wk12_s79_cell6.py'), str(c['delta'])] + [str(x) for x in c['lam']] + \
              ['--out', out, '--certs', certs, '--sequential']
        t0 = time.time()
        with open(log_path, 'a') as lf:
            lf.write(f"\n=== rank {rank} {key} N_S*delta {c['NS_delta']} a {c['a']} {datetime.datetime.utcnow().isoformat()}\n"); lf.flush()
            try:
                pr = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=lf, timeout=cell_timeout, text=True,
                                    preexec_fn=lambda: os.system('ulimit -v 6500000'))
                res = None
                for line in pr.stdout.splitlines():
                    if line.startswith('RESULT '):
                        res = json.loads(line[7:])
                if res is None:
                    status['not_reached'].append(dict(rank=rank, lam=c['lam'], delta=c['delta'], NS_delta=c['NS_delta'], reason=f'no result (rc {pr.returncode})'))
                    lf.write(f"  no RESULT line (rc {pr.returncode})\n")
                    continue
            except subprocess.TimeoutExpired:
                status['not_reached'].append(dict(rank=rank, lam=c['lam'], delta=c['delta'], NS_delta=c['NS_delta'], reason=f'timeout {cell_timeout}s'))
                lf.write(f"  TIMEOUT after {cell_timeout}s\n")
                continue
        rec = dict(rank=rank, lam=c['lam'], delta=c['delta'], NS_delta=c['NS_delta'], a=res['a'], n_chi=res['n_chi'],
                   mult_det=res['mult_det'], mult_pad=res['mult_pad'], mult_red=res['mult_red'], mult_per4=res['mult_per4'],
                   i_det=res['i_det'], i_pad=res['i_pad'], i_red=res['i_red'], i_per4=res['i_per4'], D=res['D'], D_R=res['D_R'],
                   pad_lt_red=res['pad_lt_red'], halt=res['halt'], secs=res['secs'], hwm_gb=res['hwm_gb'], wall=round(time.time() - t0, 1))
        status['reached'].append(rec)
        json.dump(status, open(status_path, 'w'), indent=1)
        print(f"[{rank}/{len(Q)}] {key} a={res['a']} n_chi={res['n_chi']} det={res['mult_det']} pad={res['mult_pad']} red={res['mult_red']} "
              f"per4={res['mult_per4']} i_det={res['i_det']} pad<red={res['pad_lt_red']} D={res['D']} ({rec['wall']}s)", flush=True)
        if res['halt']:
            status['halted'] = rec
            json.dump(status, open(status_path, 'w'), indent=1)
            print("HALT: the verification protocol takes over (PREREG_s79 sec. 2.5)", flush=True)
            return 2
    json.dump(status, open(status_path, 'w'), indent=1)
    print("queue exhausted", flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

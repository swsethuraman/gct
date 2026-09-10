#!/usr/bin/env python3
"""
B13-08 -- the bounded, resumable, two-lane sweep over the frozen queue
(results/b13_08/queue.json), one weight per subprocess of the UNCHANGED engine
analysis/wk12_s79_per6.py (or, on a re-run pass, the lean driver
analysis/wk13_b08_per6_lean.py), in session 79's recorded cost order.

Every weight is launched as

    bash -c 'ulimit -v <kB>; exec timeout <s> python3 analysis/<driver> 10 mu1..mu6 --a A --out <lane file> --certs <dir>'

with its process id in results/logs/b13_08_w<rank>.pid and its stderr in
results/logs/b13_08_w<rank>.log; the lane's own id is in
results/logs/b13_08_sweep_lane<k>.pid.  A weight is claimed by an O_EXCL lock
file before launch (results/b13_08/claims/w<rank>.claim) so no weight runs
twice; each lane appends to its own results file (single writer).  Lane 1
takes only weights whose predicted peak is <= --max-pred GB, and a lane starts a
weight only when the predicted peaks of the two running weights sum to <=
--sum-cap GB.  A weight that ends without a RESULT line is recorded in
results/b13_08/failed_lane<k>.jsonl with the reason and the lane moves on.
The sweep takes no new weight after --until (UTC HH:MM).

usage: python3 analysis/wk13_b08_sweep.py --lane 0 [--until 23:30] [--max-pred 99] [--sum-cap 6.3]
                                          [--engine unchanged|lean] [--only-failed] [--ulimit-kb 7000000]
"""
import os, sys, json, time, datetime, subprocess

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..'))
RES = os.path.join(ROOT, 'results', 'b13_08'); LOGS = os.path.join(ROOT, 'results', 'logs')
CLAIMS = os.path.join(RES, 'claims'); CERTS = os.path.join(ROOT, 'results', 'certs', 'b13_08_per6')
DRIVERS = dict(unchanged='wk12_s79_per6.py', lean='wk13_b08_per6_lean.py')
DELTA = 10


def arg(argv, name, default):
    return type(default)(argv[argv.index(name) + 1]) if name in argv else default


def now(): return datetime.datetime.utcnow()


def read_jsonl(path):
    out = []
    if os.path.exists(path):
        for ln in open(path):
            ln = ln.strip()
            if not ln: continue
            try: out.append(json.loads(ln))
            except Exception: pass
    return out


def done_set():
    s = set()
    for k in range(4):
        for r in read_jsonl(os.path.join(RES, f'per6_d10_lane{k}.jsonl')):
            if r.get('delta') == DELTA and r.get('mult') is not None: s.add(tuple(r['mu']))
    return s


def failed_map():
    m = {}
    for k in range(4):
        for r in read_jsonl(os.path.join(RES, f'failed_lane{k}.jsonl')):
            m.setdefault(tuple(r['mu']), []).append(r)
    return m


def other_lanes_pred(lane):
    tot = 0.0
    for k in range(4):
        if k == lane: continue
        f = os.path.join(RES, f'lane{k}.current')
        if os.path.exists(f):
            try:
                cur = json.load(open(f))
                if cur.get('pid') and os.path.exists(f"/proc/{cur['pid']}"): tot += float(cur['pred'])
            except Exception: pass
    return tot


def main(argv):
    lane = arg(argv, '--lane', 0)
    until = arg(argv, '--until', '')
    max_pred = float(arg(argv, '--max-pred', '99'))
    sum_cap = float(arg(argv, '--sum-cap', '6.3'))
    engine = arg(argv, '--engine', 'unchanged'); assert engine in DRIVERS
    only_failed = '--only-failed' in argv
    only_ranks = None
    if '--only-ranks' in argv:
        only_ranks = {int(x) for x in arg(argv, '--only-ranks', '').split(',') if x.strip()}
    ulimit_kb = arg(argv, '--ulimit-kb', 7000000)
    timeout_s = arg(argv, '--timeout', 7200)
    os.makedirs(CLAIMS, exist_ok=True); os.makedirs(LOGS, exist_ok=True); os.makedirs(CERTS, exist_ok=True)
    with open(os.path.join(LOGS, f'b13_08_sweep_lane{lane}.pid'), 'w') as f: f.write(f"{os.getpid()}\n")
    deadline = None
    if until:
        hh, mm = map(int, until.split(':'))
        deadline = now().replace(hour=hh, minute=mm, second=0, microsecond=0)
        if deadline <= now(): deadline += datetime.timedelta(days=1)
    Q = json.load(open(os.path.join(RES, 'queue.json')))['queue']
    # scheduling estimate: the frozen queue's a-priori pred_peak_gb, or the recalibrated
    # results/b13_08/schedule.json (pre-registration addendum A) when --sched is given.
    # Scheduling only -- no result depends on either.
    sched = None
    if '--sched' in argv:
        sp = arg(argv, '--sched', os.path.join(RES, 'schedule.json'))
        sched = json.load(open(sp))['sched']
        print(f"[lane {lane}] scheduling from {os.path.relpath(sp, ROOT)} (addendum A), not the frozen pred_peak_gb", flush=True)
    out_path = os.path.join(RES, f'per6_d10_lane{lane}.jsonl')
    fail_path = os.path.join(RES, f'failed_lane{lane}.jsonl')
    status_path = os.path.join(RES, f'status_lane{lane}.json')
    cur_path = os.path.join(RES, f'lane{lane}.current')
    status = dict(board_numbering='batch13', lane=lane, engine=engine, started=now().isoformat(), reached=[], not_reached=[], skipped=[], halted=None)
    env = dict(os.environ); env.setdefault('S71_SCHUR_SO', '/home/claude/b13_08/schur.so'); env.setdefault('S71_MEM_X', '250000000')
    for w in Q:
        mu = tuple(w['mu']); rank = w['rank']; a = w['a']
        pred = float(sched[str(rank)]) if sched and str(rank) in sched else float(w['pred_peak_gb'])
        key = dict(rank=rank, mu=list(mu), a=a, N_S=w['N_S'], NS_delta=w['NS_delta'], pred_peak_gb=pred)
        if mu in done_set():
            status['skipped'].append(dict(key, reason='banked')); continue
        if only_failed:
            fm = failed_map()
            if mu not in fm: status['skipped'].append(dict(key, reason='not a failed weight')); continue
            claim = os.path.join(CLAIMS, f'w{rank}.rerun.claim')
        else:
            claim = os.path.join(CLAIMS, f'w{rank}.claim')
        if only_ranks is not None and rank not in only_ranks:
            continue
        if pred > max_pred:
            status['skipped'].append(dict(key, reason=f'predicted peak {pred} GB > lane cap {max_pred}')); continue
        if deadline and now() >= deadline:
            status['not_reached'].append(dict(key, reason='wall clock')); continue
        try:
            fd = os.open(claim, os.O_CREAT | os.O_EXCL | os.O_WRONLY); os.write(fd, f"lane {lane} {now().isoformat()}\n".encode()); os.close(fd)
        except FileExistsError:
            status['skipped'].append(dict(key, reason='claimed by another lane')); continue
        # concurrency rule: wait while ANOTHER lane is running and the two together exceed the cap.
        # A weight whose own estimate exceeds the cap is not made unrunnable by it -- it waits for the
        # other lanes to be idle and then runs solo, bounded by its own ulimit.
        waited = 0
        while (o := other_lanes_pred(lane)) > 0 and o + pred > sum_cap:
            time.sleep(20); waited += 20
            if deadline and now() >= deadline: break
        if deadline and now() >= deadline:
            os.remove(claim); status['not_reached'].append(dict(key, reason='wall clock')); continue
        kb = ulimit_kb
        other = other_lanes_pred(lane)
        if other > 0:
            kb = min(kb, int((7.0 - other - 0.4) * 1e6))          # leave the other lane its predicted room plus a margin
        cmd = f"ulimit -v {kb}; exec timeout {timeout_s} python3 {os.path.join(HERE, DRIVERS[engine])} {DELTA} {' '.join(map(str, mu))} --out {out_path} --a {a} --certs {CERTS}"
        t0 = time.time()
        with open(os.path.join(LOGS, f'b13_08_w{rank}.log'), 'a') as lf:
            lf.write(f"\n=== lane {lane} rank {rank} {mu} a {a} N_S {w['N_S']} pred {pred} GB engine {engine} ulimit_kb {kb} {now().isoformat()}\n$ {cmd}\n"); lf.flush()
            pr = subprocess.Popen(['bash', '-c', cmd], stdout=subprocess.PIPE, stderr=lf, text=True, env=env, cwd=ROOT)
            with open(os.path.join(LOGS, f'b13_08_w{rank}.pid'), 'a') as pf: pf.write(f"{pr.pid} bash/timeout wrapper, lane {lane}, {engine}, {now().isoformat()}\n")
            json.dump(dict(pid=pr.pid, rank=rank, mu=list(mu), pred=pred, started=now().isoformat()), open(cur_path, 'w'))
            stdout, _ = pr.communicate()
            rc = pr.returncode
        try: os.remove(cur_path)
        except FileNotFoundError: pass
        wall = round(time.time() - t0, 1)
        res = None
        for line in stdout.splitlines():
            if line.startswith('RESULT '): res = json.loads(line[7:])
        if res is None:
            tail = open(os.path.join(LOGS, f'b13_08_w{rank}.log')).read()[-6000:]
            reason = ('timeout' if rc == 124 else 'memory' if ('MemoryError' in tail or 'Cannot allocate' in tail or 'std::bad_alloc' in tail or rc in (137, -9, 134, -6))
                      else 'error')
            rec = dict(key, engine=engine, lane=lane, rc=rc, reason=reason, wall=wall, waited=waited, ulimit_kb=kb, when=now().isoformat())
            with open(fail_path, 'a') as f: f.write(json.dumps(rec) + "\n")
            status['not_reached'].append(rec)
            print(f"[lane {lane}] rank {rank} {mu} a={a}: NOT REACHED ({reason}, rc {rc}, {wall}s)", flush=True)
        else:
            rec = dict(key, engine=engine, lane=lane, n_chi=res.get('n_chi'), mult=res['mult'], units=res['units'], halt=res['halt'],
                       secs=res['secs'], wall=wall, waited=waited, hwm_gb=res.get('hwm_gb'), ulimit_kb=kb, when=now().isoformat())
            status['reached'].append(rec)
            print(f"[lane {lane}] rank {rank} {mu} a={a} N_S={w['N_S']} n_chi={res.get('n_chi')} mult={res['mult']} units={res['units']} "
                  f"({wall}s, HWM {res.get('hwm_gb')} GB, pred {pred})", flush=True)
            if res['halt']:
                status['halted'] = rec; json.dump(status, open(status_path, 'w'), indent=1)
                print(f"[lane {lane}] HALT: a drop on the cubic side at {mu} -- the verification protocol takes over", flush=True)
                open(os.path.join(RES, 'HALT'), 'a').write(json.dumps(rec) + "\n")
                return 2
        json.dump(status, open(status_path, 'w'), indent=1)
        if os.path.exists(os.path.join(RES, 'HALT')):
            print(f"[lane {lane}] the other lane halted; stopping", flush=True); return 2
    status['finished'] = now().isoformat()
    json.dump(status, open(status_path, 'w'), indent=1)
    print(f"[lane {lane}] sweep complete", flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

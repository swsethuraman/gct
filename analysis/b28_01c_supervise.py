#!/usr/bin/env python3
"""
B28-01c -- job supervisor for R28-01 repair P5: one aggregate MONOTONIC wall
limit over the whole producer-plus-replay job, whole-job termination, an
artifact-size stop, and a resource-stop receipt.

It is started inside the job's single systemd scope (MemoryMax, MemorySwapMax=0)
by the launcher.  It runs the steps strictly sequentially, each in its own
process group under GNU time -v; the literal token {REMAINING} in a step's
arguments is replaced by the whole seconds left on the aggregate monotonic
deadline when that step starts.  A step with a nonzero exit ends the job (no
later step runs).  On the deadline, or when the output directory exceeds the
artifact stop, the running step's whole process group is sent SIGTERM and,
after a grace period, SIGKILL; no later step runs; the receipt records the
reason.  A step killed by SIGKILL that the supervisor did not kill is recorded
as a memory stop (the scope's OOM killer; memory.events is read when present).

usage: b28_01c_supervise.py --cap-secs S --out DIR --artifact-stop BYTES --receipt FILE
                            --steps JSON        (list of {"label": .., "argv": [..]})
exit: the failing step's exit code; 0 if every step exited 0; 124 wall stop;
      125 artifact stop; 137 memory stop.
"""
import sys, os, json, time, signal, subprocess, argparse

POLL = 5.0
GRACE = 30.0


def tree_bytes(path):
    tot = 0
    for root, _, files in os.walk(path):
        for f in files:
            try: tot += os.lstat(os.path.join(root, f)).st_size
            except OSError: pass
    return tot


def cgroup_file(name):
    try:
        rel = open('/proc/self/cgroup').read().strip().split('::', 1)[1]
        with open(f'/sys/fs/cgroup{rel}/{name}') as f: return f.read().strip()
    except (OSError, IndexError):
        return None


def kill_group(proc):
    for sig, wait in ((signal.SIGTERM, GRACE), (signal.SIGKILL, None)):
        try: os.killpg(proc.pid, sig)
        except ProcessLookupError: return
        try:
            proc.wait(timeout=wait); return
        except subprocess.TimeoutExpired:
            continue
    proc.wait()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--cap-secs', type=float, required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--artifact-stop', type=int, required=True)
    ap.add_argument('--receipt', required=True)
    ap.add_argument('--steps', required=True)
    args = ap.parse_args()
    steps = json.loads(args.steps)
    t0 = time.monotonic(); deadline = t0 + args.cap_secs
    rec = dict(schema='b28-01c-job-receipt/1', clock='time.monotonic', cap_secs=args.cap_secs, artifact_stop_bytes=args.artifact_stop,
               out=args.out, start_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), steps=[],
               scope=dict(memory_max=cgroup_file('memory.max'), memory_swap_max=cgroup_file('memory.swap.max')))

    def finish(code, stop=None):
        rec['elapsed_monotonic_secs'] = round(time.monotonic() - t0, 3)
        rec['end_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
        rec['resource_stop'] = stop
        rec['exit'] = code
        rec['scope_end'] = dict(memory_peak=cgroup_file('memory.peak'), memory_events=cgroup_file('memory.events'))
        rec['artifact_bytes_at_end'] = tree_bytes(args.out)
        with open(args.receipt, 'w') as f: json.dump(rec, f, indent=1)
        print(f'JOB exit={code} resource_stop={stop}', flush=True)
        sys.exit(code)

    for st in steps:
        left = deadline - time.monotonic()
        if left <= 0:
            finish(124, dict(reason='wall', detail=f"aggregate monotonic limit reached before step {st['label']}"))
        argv = [x.replace('{REMAINING}', str(int(left))) for x in st['argv']]
        tf = os.path.join(os.path.dirname(args.receipt), f"{st['label']}.time")
        lf = os.path.join(os.path.dirname(args.receipt), f"{st['label']}.log")
        ts = time.monotonic(); stop = None
        with open(lf, 'wb') as log:
            proc = subprocess.Popen(['/usr/bin/time', '-v', '-o', tf] + argv, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
            while True:
                try:
                    rc = proc.wait(timeout=max(0.05, min(POLL, deadline - time.monotonic())))
                    break
                except subprocess.TimeoutExpired:
                    if time.monotonic() >= deadline:
                        stop = dict(reason='wall', detail=f"aggregate monotonic limit {args.cap_secs} s reached during step {st['label']}")
                    elif tree_bytes(args.out) > args.artifact_stop:
                        stop = dict(reason='artifact', detail=f"output exceeded {args.artifact_stop} bytes during step {st['label']}")
                    if stop:
                        kill_group(proc); rc = proc.returncode; break
        tinfo = open(tf).read() if os.path.exists(tf) else ''
        sig9 = 'Command terminated by signal 9' in tinfo
        maxrss = next((int(l.split()[-1]) * 1024 for l in tinfo.splitlines() if 'Maximum resident set size' in l), None)
        rec['steps'].append(dict(label=st['label'], argv=argv, rc=rc, secs_monotonic=round(time.monotonic() - ts, 3), maxrss_bytes=maxrss,
                                 killed_by_supervisor=bool(stop)))
        if stop:
            finish(124 if stop['reason'] == 'wall' else 125, stop)
        if sig9:
            finish(137, dict(reason='memory', detail=f"step {st['label']} was killed by SIGKILL inside the job scope (OOM)"))
        if rc != 0:
            finish(rc, None)
    finish(0, None)


if __name__ == '__main__':
    main()

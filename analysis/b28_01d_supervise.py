#!/usr/bin/env python3
"""
B28-01d -- job supervisor for R28-01 repair P5, with R28-01b's repairs P5a/P5b:
one aggregate MONOTONIC wall limit over the whole producer-plus-replay job,
whole-job termination, an artifact-size stop, and a resource-stop receipt.

It is started inside the job's single systemd scope (MemoryMax, MemorySwapMax=0)
by the launcher.  It runs the steps strictly sequentially, each in its own
process group (session) under GNU time -v; the literal token {REMAINING} in a
step's arguments is replaced by the whole seconds left on the aggregate
monotonic deadline when that step starts.  A step with a nonzero exit ends the
job (no later step runs).

P5a  The supervisor is a child subreaper (prctl PR_SET_CHILD_SUBREAPER), so every
     orphaned job process is re-parented to it.  The group id is kept
     independently of the /usr/bin/time leader.  On a stop the group is sent
     SIGTERM; after a grace period (or at once if the group is already empty)
     every surviving group member and every remaining descendant is sent
     SIGKILL, and the supervisor reaps and re-checks until NO job process
     remains before it writes the receipt and returns.  The same sweep runs
     after every normal step exit (leftover group members are killed and
     recorded), so no job process outlives its step.
P5b  Immediately after each step exits -- before any next step and before a
     success return -- the artifact size and the monotonic deadline are
     rechecked; an excess returns 125 (artifact) or 124 (wall) with the
     resource-stop receipt.  During a step they are also checked at every poll.
A step killed by SIGKILL that the supervisor did not kill is recorded as a
memory stop (the scope's OOM killer).

usage: b28_01d_supervise.py --cap-secs S --out DIR --artifact-stop BYTES --receipt FILE
                            --steps JSON        (list of {"label": .., "argv": [..]})
exit: the failing step's exit code; 0 if every step exited 0 and no limit was
      exceeded; 124 wall stop; 125 artifact stop; 137 memory stop.
"""
import sys, os, json, time, signal, subprocess, argparse, ctypes

POLL = 5.0
GRACE = 30.0
PR_SET_CHILD_SUBREAPER = 36


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


def become_subreaper():
    libc = ctypes.CDLL(None, use_errno=True)
    if libc.prctl(PR_SET_CHILD_SUBREAPER, 1, 0, 0, 0) != 0:
        raise OSError(ctypes.get_errno(), 'prctl(PR_SET_CHILD_SUBREAPER) failed')


def children(zombie):
    """pids of this supervisor's children (orphans are re-parented here), zombies or live ones."""
    me = os.getpid(); out = []
    for d in os.listdir('/proc'):
        if not d.isdigit(): continue
        try:
            st = open(f'/proc/{d}/stat').read()
        except OSError:
            continue
        rest = st.rsplit(')', 1)[1].split()
        if int(rest[1]) == me and (rest[0] == 'Z') == zombie: out.append(int(d))
    return out


def reap(leader=None):
    """reap exited orphans; the step leader is reaped only through its Popen object."""
    if leader is not None: leader.poll()
    for pid in children(zombie=True):
        if leader is not None and pid == leader.pid: continue
        try: os.waitpid(pid, os.WNOHANG)
        except ChildProcessError: pass


def group_alive(pgid):
    try:
        os.killpg(pgid, 0); return True
    except ProcessLookupError:
        return False
    except PermissionError:
        return True


def sweep(proc, pgid):
    """SIGKILL every remaining member of the group and every descendant left
    with this supervisor; reap; repeat until none remains.  Returns the pids
    that were still alive when first found here (the group leader excluded)."""
    found = set()
    while True:
        reap(proc)
        kids = [k for k in children(zombie=False) if k != proc.pid]
        if proc.poll() is not None and not group_alive(pgid) and not kids:
            return sorted(found)
        found.update(kids)
        try: os.killpg(pgid, signal.SIGKILL)
        except ProcessLookupError: pass
        for k in kids:
            try: os.kill(k, signal.SIGKILL)
            except ProcessLookupError: pass
        time.sleep(0.05)


def stop_group(proc, pgid):
    """SIGTERM the group; wait up to GRACE for it (and every descendant) to be
    gone; then SIGKILL the survivors and do not return until none remains."""
    try: os.killpg(pgid, signal.SIGTERM)
    except ProcessLookupError: pass
    t = time.monotonic() + GRACE
    while time.monotonic() < t:
        reap(proc)
        if proc.poll() is not None and not group_alive(pgid) and not children(zombie=False): break
        time.sleep(0.05)
    return sweep(proc, pgid)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--cap-secs', type=float, required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--artifact-stop', type=int, required=True)
    ap.add_argument('--receipt', required=True)
    ap.add_argument('--steps', required=True)
    args = ap.parse_args()
    steps = json.loads(args.steps)
    become_subreaper()
    t0 = time.monotonic(); deadline = t0 + args.cap_secs
    rec = dict(schema='b28-01d-job-receipt/1', clock='time.monotonic', cap_secs=args.cap_secs, artifact_stop_bytes=args.artifact_stop,
               out=args.out, start_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), steps=[], subreaper=True,
               scope=dict(memory_max=cgroup_file('memory.max'), memory_swap_max=cgroup_file('memory.swap.max')))

    def finish(code, stop=None):
        reap()
        rec['job_processes_remaining_at_end'] = len(children(zombie=False))
        rec['elapsed_monotonic_secs'] = round(time.monotonic() - t0, 3)
        rec['end_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
        rec['resource_stop'] = stop
        rec['exit'] = code
        rec['scope_end'] = dict(memory_peak=cgroup_file('memory.peak'), memory_events=cgroup_file('memory.events'))
        rec['artifact_bytes_at_end'] = tree_bytes(args.out)
        with open(args.receipt, 'w') as f: json.dump(rec, f, indent=1)
        print(f'JOB exit={code} resource_stop={stop}', flush=True)
        sys.exit(code)

    def boundary(where):
        """P5b: the limits at a completion boundary; returns a stop or None."""
        size = tree_bytes(args.out)
        if size > args.artifact_stop:
            return dict(reason='artifact', detail=f'output {size} bytes exceeds {args.artifact_stop} {where}')
        if time.monotonic() >= deadline:
            return dict(reason='wall', detail=f'aggregate monotonic limit {args.cap_secs} s reached {where}')
        return None

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
            pgid = proc.pid                                       # the group id, kept independently of the leader
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
                        killed = stop_group(proc, pgid); rc = proc.returncode; break
            if not stop:
                killed = sweep(proc, pgid)                              # leftovers of a normally exited step
        tinfo = open(tf).read() if os.path.exists(tf) else ''
        sig9 = 'Command terminated by signal 9' in tinfo
        maxrss = next((int(l.split()[-1]) * 1024 for l in tinfo.splitlines() if 'Maximum resident set size' in l), None)
        rec['steps'].append(dict(label=st['label'], argv=argv, rc=rc, pgid=pgid, secs_monotonic=round(time.monotonic() - ts, 3), maxrss_bytes=maxrss,
                                 killed_by_supervisor=bool(stop), survivors_sigkilled=killed,
                                 group_alive_after_step=group_alive(pgid)))
        if stop:
            finish(124 if stop['reason'] == 'wall' else 125, stop)
        if sig9:
            finish(137, dict(reason='memory', detail=f"step {st['label']} was killed by SIGKILL inside the job scope (OOM)"))
        b = boundary(f"at the exit of step {st['label']}")
        if b:
            finish(124 if b['reason'] == 'wall' else 125, b)
        if rc != 0:
            finish(rc, None)
    b = boundary('before the success return')
    if b:
        finish(124 if b['reason'] == 'wall' else 125, b)
    finish(0, None)


if __name__ == '__main__':
    main()

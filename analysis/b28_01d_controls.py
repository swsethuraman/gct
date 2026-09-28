#!/usr/bin/env python3
"""
B28-01d -- the supervisor controls, strictly sequential, meant to run inside ONE
aggregate scope (systemd-run --user --scope -p MemoryMax=8000000000
-p MemorySwapMax=0, outer timeout 1800 s).  No matrix work beyond B28-01c's
registered two-step supervisor control on the small control cell; no Cell A.

  B28-01c's supervisor controls, re-run on the repaired supervisor:
    sup_wall          3 s cap on sleep 60                    -> 124, wall stop
    sup_artifact      slow writer, 10 MB stop                -> 125, artifact stop
    sup_ctl           driver then verifier, control cell     -> 0, 0, FULL_RANK
  R28-01b's two fixtures:
    fx_term_resistant child ignoring SIGTERM, 2 s deadline   -> 124, and NO process alive
    fx_fast_writer    2,048 bytes against a 1,024-byte stop  -> 125 with the receipt
  added:
    fx_fast_writer_two_step  as above, then a marker step    -> 125, marker step never ran
    fx_stray_child    step exits 0 leaving a background child -> 0, the child killed, none alive
    launcher_preflight  b28_01d_cellA.sh --preflight-only     -> 0

Each step's command, exit, monotonic seconds and receipt go to
OUT/controls_receipt.json; the first missed expectation stops the harness (exit 1).

usage: b28_01d_controls.py FROZEN_D OUT
       b28_01d_controls.py --term-resistant-child PIDFILE     (fixture child)
"""
import sys, os, json, time, glob, hashlib, subprocess, signal

if len(sys.argv) > 1 and sys.argv[1] == '--term-resistant-child':
    signal.signal(signal.SIGTERM, signal.SIG_IGN)
    with open(sys.argv[2], 'w') as f: f.write(str(os.getpid()))
    time.sleep(40)
    sys.exit(0)

F, OUT = sys.argv[1], sys.argv[2]
HOME = os.path.expanduser('~')
ENG = f'{HOME}/b28_01/engine'; PY = f'{HOME}/b28venv/bin/python'
P1, P2 = 2147483647, 2147483629
CT = ['--lam', '22', '6', '5', '2', '1', '--delta', '9', '--a', '24']; TAG = '22_6_5_2_1_d9'
ENV = dict(os.environ, B28_ENGINE=ENG, S71_SCHUR_SO=f'{ENG}/schur.so', B28_VFY_SO=f'{F}/b28_01c_vfy.so',
           B28_SCHUR_SO_SHA256='d6024a63dca11dc5b820864bc87ac842dcfba3a39e1f35792d6febacc8ee936d',
           OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', MKL_NUM_THREADS='1', NUMEXPR_NUM_THREADS='1', PYTHONDONTWRITEBYTECODE='1')
SUP = [PY, f'{F}/b28_01d_supervise.py']
steps = []; t_all = time.monotonic()


def sha_file(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def alive(pid):
    try:
        st = open(f'/proc/{pid}/stat').read()
    except OSError:
        return False
    return st.rsplit(')', 1)[1].split()[0] != 'Z'


def finish(ok):
    rec = dict(schema='b28-01d-controls-receipt/1', clock='time.monotonic', total_secs=round(time.monotonic() - t_all, 3), all_expectations_met=ok,
               frozen_d={os.path.basename(p): sha_file(p) for p in sorted(glob.glob(f'{F}/*')) if os.path.isfile(p)}, steps=steps)
    json.dump(rec, open(os.path.join(OUT, 'controls_receipt.json'), 'w'), indent=1)
    print('ALL EXPECTATIONS MET' if ok else 'STOPPED: an expectation failed', flush=True)
    sys.exit(0 if ok else 1)


def run(label, argv, expect_rc, check=None):
    lf = os.path.join(OUT, 'logs', f'{label}.log')
    ts = time.monotonic()
    with open(lf, 'wb') as log:
        rc = subprocess.run(argv, stdout=log, stderr=subprocess.STDOUT, env=ENV, timeout=300).returncode
    secs = time.monotonic() - ts
    detail = check() if check else None
    ok = rc == expect_rc and (detail is None or detail.get('ok', True))
    steps.append(dict(label=label, argv=argv, rc=rc, expected_rc=expect_rc, secs_monotonic=round(secs, 3), log_sha256=sha_file(lf),
                      check=detail, expectation_met=ok))
    print(f'{label}: rc={rc} (expected {expect_rc}) {secs:.1f}s ok={ok} {json.dumps(detail)[:400] if detail else ""}', flush=True)
    if not ok: finish(False)


def J(p):
    return json.load(open(p))


def sup(label, cap, stop, st, expect_rc, check):
    d = f'{OUT}/{label}'; os.makedirs(f'{d}/out')
    st = [dict(s, argv=[x.replace('{OUT}', f'{d}/out').replace('{D}', d) for x in s['argv']]) for s in st]
    run(label, SUP + ['--cap-secs', str(cap), '--out', f'{d}/out', '--artifact-stop', str(stop), '--receipt', f'{d}/job_receipt.json',
                      '--steps', json.dumps(st)], expect_rc, lambda: check(d, J(f'{d}/job_receipt.json')))


def stopped(why):
    def f(d, r):
        return dict(resource_stop=r['resource_stop'], elapsed=r['elapsed_monotonic_secs'], remaining=r['job_processes_remaining_at_end'],
                    ok=(r['resource_stop'] or {}).get('reason') == why and r['job_processes_remaining_at_end'] == 0
                    and not r['steps'][-1]['group_alive_after_step'])
    return f


def main():
    assert not os.path.exists(OUT)
    os.makedirs(f'{OUT}/logs')
    drv = [PY, f'{F}/b28_01c_driver.py']; ver = [PY, f'{F}/b28_01c_verify.py']

    # ---- B28-01c's supervisor controls on the repaired supervisor
    sup('sup_wall', 3, 1000000000, [{'label': 'sleeper', 'argv': ['/bin/sleep', '60']}], 124, stopped('wall'))
    sup('sup_artifact', 600, 10000000, [{'label': 'writer', 'argv': [PY, '-c', "import time,sys\nf=open(sys.argv[1]+'/blob','wb')\nfor i in range(40):\n f.write(b'0'*1000000); f.flush(); time.sleep(0.5)", '{OUT}']}],
        125, stopped('artifact'))
    st = [dict(label='ctl_driver', argv=drv + CT + ['--nchi', '21093', '--primes', str(P1), str(P2), '--out', '{OUT}', '--wall-budget', '{REMAINING}',
                                                    '--mem-cap', '8000000000', '--rates', f'{F}/gate_rates_c.json']),
          dict(label='ctl_verify', argv=ver + CT + ['--prime', str(P1), '--dir', '{OUT}', '--out', '{OUT}/' + f'{TAG}_p{P1}_verify.json'])]
    sup('sup_ctl', 600, 1000000000, st, 0,
        lambda d, r: dict(steps=[(s['label'], s['rc']) for s in r['steps']], verdict=J(f'{d}/out/{TAG}_p{P1}_verify.json')['verdict'],
                          ok=[s['rc'] for s in r['steps']] == [0, 0] and J(f'{d}/out/{TAG}_p{P1}_verify.json')['verdict'] == 'FULL_RANK'
                          and r['resource_stop'] is None and r['job_processes_remaining_at_end'] == 0))

    # ---- R28-01b fixture 1: a child that ignores SIGTERM under a 2 s deadline must not survive
    def term_check(d, r):
        pid = int(open(f'{d}/child_pid.txt').read())
        live = alive(pid)
        if live: os.kill(pid, signal.SIGKILL)                  # cleanup only if the repair failed
        x = stopped('wall')(d, r)
        x.update(child_pid=pid, child_alive_after_supervisor=live, survivors_sigkilled=r['steps'][-1]['survivors_sigkilled'],
                 ok=x['ok'] and not live and pid in r['steps'][-1]['survivors_sigkilled'])
        return x
    sup('fx_term_resistant', 2, 1000000, [{'label': 'term_resistant', 'argv': [PY, f'{F}/b28_01d_controls.py', '--term-resistant-child', '{D}/child_pid.txt']}],
        124, term_check)

    # ---- R28-01b fixture 2: a fast writer crossing the stop before the first poll
    fast = 'from pathlib import Path; import sys; Path(sys.argv[1]).write_bytes(bytes(2048))'
    def fast_check(d, r):
        x = stopped('artifact')(d, r); x.update(artifact_bytes=r['artifact_bytes_at_end'], limit=1024, ok=x['ok'] and r['artifact_bytes_at_end'] == 2048)
        return x
    sup('fx_fast_writer', 10, 1024, [{'label': 'writer', 'argv': [PY, '-c', fast, '{OUT}/blob']}], 125, fast_check)
    sup('fx_fast_writer_two_step', 10, 1024, [{'label': 'writer', 'argv': [PY, '-c', fast, '{OUT}/blob']},
                                              {'label': 'marker', 'argv': ['/usr/bin/touch', '{D}/marker_ran']}], 125,
        lambda d, r: dict(fast_check(d, r), marker_ran=os.path.exists(f'{d}/marker_ran'), steps=len(r['steps']),
                          ok=fast_check(d, r)['ok'] and not os.path.exists(f'{d}/marker_ran') and len(r['steps']) == 1))

    # ---- added: a normally exiting step that leaves a background child behind
    def stray_check(d, r):
        pid = int(open(f'{d}/stray_pid.txt').read())
        live = alive(pid)
        if live: os.kill(pid, signal.SIGKILL)
        return dict(stray_pid=pid, stray_alive_after_supervisor=live, survivors_sigkilled=r['steps'][-1]['survivors_sigkilled'],
                    remaining=r['job_processes_remaining_at_end'],
                    ok=not live and pid in r['steps'][-1]['survivors_sigkilled'] and r['resource_stop'] is None and r['job_processes_remaining_at_end'] == 0)
    sup('fx_stray_child', 60, 1000000, [{'label': 'stray', 'argv': ['/bin/bash', '-c', 'sleep 120 & echo $! > "$1"; exit 0', 'stray', '{D}/stray_pid.txt']}],
        0, stray_check)

    # ---- the frozen launcher's preflight (builds nothing)
    run('launcher_preflight', ['/bin/bash', f'{F}/b28_01d_cellA.sh', '--preflight-only'], 0)
    finish(True)


if __name__ == '__main__':
    main()

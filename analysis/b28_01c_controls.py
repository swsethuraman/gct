#!/usr/bin/env python3
"""
B28-01c -- every control and replay of this slot, strictly sequential, meant to run
inside ONE aggregate scope (systemd-run --user --scope -p MemoryMax=8000000000
-p MemorySwapMax=0, outer timeout 3600 s).  Small control cell (22,6,5,2,1)_9
(s71 record line 5) and the calibration cells only; no Cell A.

Each step runs under GNU time -v; its command, exit code, monotonic seconds,
maximum RSS and the hashes of its inputs/outputs go to OUT/controls_receipt.json
(timing lives only there).  Each step has a registered expectation; the first
step that misses it stops the harness (exit 1).

usage: b28_01c_controls.py FROZEN_C OUT
"""
import sys, os, json, time, glob, hashlib, subprocess, shutil

F, OUT = sys.argv[1], sys.argv[2]
HOME = os.path.expanduser('~')
ENG = f'{HOME}/b28_01/engine'; PY = f'{HOME}/b28venv/bin/python'; OLD = f'{HOME}/b28_01/frozen'
P1, P2 = 2147483647, 2147483629
CT = ['--lam', '22', '6', '5', '2', '1', '--delta', '9', '--a', '24']; TAG = '22_6_5_2_1_d9'
C1 = ['--lam', '24', '6', '5', '3', '2', '--delta', '10', '--a', '47']
C2 = ['--lam', '13', '9', '9', '3', '1', '1', '--delta', '9', '--a', '70']
RATES = f'{F}/gate_rates_c.json'
ENV = dict(os.environ, B28_ENGINE=ENG, S71_SCHUR_SO=f'{ENG}/schur.so', B28_VFY_SO=f'{F}/b28_01c_vfy.so',
           B28_SCHUR_SO_SHA256='d6024a63dca11dc5b820864bc87ac842dcfba3a39e1f35792d6febacc8ee936d',
           OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', MKL_NUM_THREADS='1', NUMEXPR_NUM_THREADS='1', PYTHONDONTWRITEBYTECODE='1')
LOG = os.path.join(OUT, 'logs')
steps = []; t_all = time.monotonic()


def sha_file(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def tree_hashes(d):
    return {os.path.relpath(p, OUT): sha_file(p) for p in sorted(glob.glob(os.path.join(d, '**', '*'), recursive=True)) if os.path.isfile(p)}


def finish(ok):
    rec = dict(schema='b28-01c-controls-receipt/1', clock='time.monotonic', total_secs=round(time.monotonic() - t_all, 3), all_expectations_met=ok,
               frozen_c={os.path.basename(p): sha_file(p) for p in sorted(glob.glob(f'{F}/*')) if os.path.isfile(p)}, steps=steps)
    json.dump(rec, open(os.path.join(OUT, 'controls_receipt.json'), 'w'), indent=1)
    print('ALL EXPECTATIONS MET' if ok else 'STOPPED: an expectation failed', flush=True)
    sys.exit(0 if ok else 1)


def run(label, argv, expect_rc, check=None, outdir=None):
    tf = os.path.join(LOG, f'{label}.time'); lf = os.path.join(LOG, f'{label}.log')
    ts = time.monotonic()
    with open(lf, 'wb') as log:
        rc = subprocess.run(['/usr/bin/time', '-v', '-o', tf] + argv, stdout=log, stderr=subprocess.STDOUT, env=ENV).returncode
    secs = time.monotonic() - ts
    t = open(tf).read()
    maxrss = next((int(l.split()[-1]) * 1024 for l in t.splitlines() if 'Maximum resident set size' in l), None)
    detail = check() if (check and rc == expect_rc) else None
    ok = rc == expect_rc and (detail is None or detail.get('ok', True))
    steps.append(dict(label=label, argv=argv, rc=rc, expected_rc=expect_rc, secs_monotonic=round(secs, 3), maxrss_bytes=maxrss,
                      log_sha256=sha_file(lf), check=detail, expectation_met=ok,
                      outputs=(tree_hashes(outdir) if outdir and os.path.isdir(outdir) else None)))
    print(f'{label}: rc={rc} (expected {expect_rc}) {secs:.1f}s maxrss={maxrss} ok={ok} {json.dumps(detail)[:300] if detail else ""}', flush=True)
    if not ok: finish(False)


def J(p):
    return json.load(open(p))


def verdict(path, want, extra=None):
    def f():
        v = J(path); d = dict(verdict=v['verdict'], ok=v['verdict'] == want)
        if extra: d.update(extra(v)); d['ok'] = d['ok'] and d.pop('_ok', True)
        return d
    return f


def main():
    assert not os.path.exists(OUT)
    os.makedirs(LOG)
    drv = [PY, f'{F}/b28_01c_driver.py']; ver = [PY, f'{F}/b28_01c_verify.py']
    ctl = f'{OUT}/control'

    # ---- regression 1: the small control cell at both primes (s71_sweep.jsonl line 5)
    run('reg_ctl_driver', drv + CT + ['--nchi', '21093', '--primes', str(P1), str(P2), '--out', ctl, '--wall-budget', '3000',
                                     '--mem-cap', '8000000000', '--rates', RATES], 0,
        lambda: dict(primes=J(f'{ctl}/{TAG}_primes.json')['verdict']), ctl)
    for p in (P1, P2):
        run(f'reg_ctl_verify_p{p}', ver + CT + ['--prime', str(p), '--dir', ctl, '--out', f'{ctl}/{TAG}_p{p}_verify.json'], 0,
            verdict(f'{ctl}/{TAG}_p{p}_verify.json', 'FULL_RANK'))

    # ---- B28-01a's two corrupted controls, now against the repaired verifier
    cc = f'{OUT}/corrupt'; os.makedirs(cc)
    subprocess.run([PY, f'{OLD}/b28_01_corrupt.py', 'kernel', f'{ctl}/{TAG}_p{P1}_K.u32', f'{cc}/K_corrupt.u32', str(P1)], check=True, env=ENV)
    subprocess.run([PY, f'{OLD}/b28_01_corrupt.py', 'pencil', f'{ctl}/{TAG}_pencils.json', f'{cc}/pencils_corrupt.json'], check=True, env=ENV)
    run('ctl_corrupt_kernel', ver + CT + ['--prime', str(P1), '--dir', ctl, '--kernel', f'{cc}/K_corrupt.u32', '--out', f'{cc}/verify_corrupt_kernel.json'], 5,
        verdict(f'{cc}/verify_corrupt_kernel.json', 'REJECT'))
    run('ctl_corrupt_point', ver + CT + ['--prime', str(P1), '--dir', ctl, '--pencils', f'{cc}/pencils_corrupt.json', '--out', f'{cc}/verify_corrupt_point.json'], 5,
        verdict(f'{cc}/verify_corrupt_point.json', 'REJECT'))

    # ---- R28-01's two malformed-certificate controls: must now be REJECTED
    for kind, key in (('missing_minor', 'M1_claimed_minor_nonzero'), ('wrong_recipe', 'projection_recipe_registered')):
        d = f'{OUT}/malformed_{kind}'
        subprocess.run([PY, f'{F}/b28_01c_fixture.py', kind, ctl, d, str(P1)], check=True, env=ENV)
        for q in glob.glob(f'{d}/*verify*'): os.remove(q)
        run(f'ctl_malformed_{kind}', ver + CT + ['--prime', str(P1), '--dir', d, '--out', f'{d}/verify.json'], 5,
            verdict(f'{d}/verify.json', 'REJECT', lambda v, key=key: dict(failed_check=key, _ok=v['checks'][key] is False)))

    # ---- deficiency fixture: first 22 < a = 24 points at P1; one valid and one corrupted candidate
    dd = f'{OUT}/deficiency'
    run('fx_deficiency_driver', drv + CT + ['--nchi', '21093', '--primes', str(P1), '--out', dd, '--wall-budget', '3000',
                                           '--mem-cap', '8000000000', '--rates', RATES, '--fixture-npts', f'{P1}:22'], 0,
        lambda: (lambda c: dict(outcome=c['outcome'], lower_bound=c['mult_det_lower_bound'], driver_checks=c['candidates']['checks'],
                                ok=c['outcome'] == 'MODULAR_DEFICIENCY' and all(c['candidates']['checks'].values())))(J(f'{dd}/{TAG}_p{P1}_cert.json')), dd)
    run('fx_deficiency_verify_valid', ver + CT + ['--prime', str(P1), '--dir', dd, '--out', f'{dd}/verify.json', '--fixture-npts', '22'], 8,
        verdict(f'{dd}/verify.json', 'MODULAR_DEFICIENCY', lambda v: dict(lower_bound=v['mult_det_lower_bound'],
                candidates_valid=[c['valid'] for c in v['candidates']], _ok=all(c['valid'] for c in v['candidates']))))
    dc = f'{OUT}/deficiency_corrupted'
    subprocess.run([PY, f'{F}/b28_01c_fixture.py', 'corrupt_candidate', dd, dc, str(P1)], check=True, env=ENV)
    for q in glob.glob(f'{dc}/verify*'): os.remove(q)
    run('fx_deficiency_verify_corrupted', ver + CT + ['--prime', str(P1), '--dir', dc, '--out', f'{dc}/verify.json', '--fixture-npts', '22'], 5,
        verdict(f'{dc}/verify.json', 'REJECT', lambda v: dict(candidates=v['candidates'],
                _ok=v['candidates'][0]['valid'] and not v['candidates'][1]['valid'] and not v['candidates'][1]['zero_at_every_saved_point'])))

    # ---- source-gate-failure fixture: projection with 40 < |U| - a rows; must exit 4 at P1, before P2, without a lift
    sg = f'{OUT}/source_gate'
    def sg_check():
        c = J(f'{sg}/{TAG}_p{P1}_cert.json'); r = J(f'{sg}/{TAG}_receipt.json'); names = [x['phase'] for x in r['phases']]
        d = dict(status=c['status'], projected_nullity=c['hybrid']['projected_nullity'], phases=names,
                 p2_cert_exists=os.path.exists(f'{sg}/{TAG}_p{P2}_cert.json'), K_files=glob.glob(f'{sg}/*_K.u32'))
        d['ok'] = (c['status'].startswith('SOURCE GATE FAILED') and names.count('schur') == 1 and 'lift_check' not in names
                   and not d['p2_cert_exists'] and not d['K_files'])
        return d
    run('fx_source_gate', drv + CT + ['--nchi', '21093', '--primes', str(P1), str(P2), '--out', sg, '--wall-budget', '3000',
                                     '--mem-cap', '8000000000', '--rates', RATES, '--fixture-proj-m', '40'], 4, sg_check, sg)

    # ---- prime-disagreement fixture: P2 restricted to 22 points; must be INCONCLUSIVE (exit 6)
    di = f'{OUT}/disagreement'
    run('fx_disagreement', drv + CT + ['--nchi', '21093', '--primes', str(P1), str(P2), '--out', di, '--wall-budget', '3000',
                                      '--mem-cap', '8000000000', '--rates', RATES, '--fixture-npts', f'{P2}:22'], 6,
        lambda: (lambda c: dict(verdict=c['verdict'], per_prime=c['per_prime'], ok=c['agree'] is False and c['verdict'].startswith('INCONCLUSIVE')))(
            J(f'{di}/{TAG}_primes.json')), di)

    # ---- P5 supervisor: wall stop, artifact stop, and the launcher's two-step path on the control cell
    sv = [PY, f'{F}/b28_01c_supervise.py']
    for lab, cap, stop, st, rc_, why in (
            ('sup_wall', '3', '1000000000', [{'label': 'sleeper', 'argv': ['/bin/sleep', '60']}], 124, 'wall'),
            ('sup_artifact', '600', '10000000', [{'label': 'writer', 'argv': [PY, '-c', "import time,sys\nf=open(sys.argv[1]+'/blob','wb')\nfor i in range(40):\n f.write(b'0'*1000000); f.flush(); time.sleep(0.5)", '{OUT}']}], 125, 'artifact')):
        d = f'{OUT}/{lab}'; os.makedirs(f'{d}/out')
        st = [dict(s, argv=[x.replace('{OUT}', f'{d}/out') for x in s['argv']]) for s in st]
        run(lab, sv + ['--cap-secs', cap, '--out', f'{d}/out', '--artifact-stop', stop, '--receipt', f'{d}/job_receipt.json', '--steps', json.dumps(st)], rc_,
            lambda d=d, why=why: (lambda r: dict(resource_stop=r['resource_stop'], elapsed=r['elapsed_monotonic_secs'],
                                                 ok=(r['resource_stop'] or {}).get('reason') == why and r['steps'][-1]['killed_by_supervisor']))(J(f'{d}/job_receipt.json')))
    d = f'{OUT}/sup_ctl'; os.makedirs(d)
    st = [dict(label='ctl_driver', argv=drv + CT + ['--nchi', '21093', '--primes', str(P1), str(P2), '--out', f'{d}/out', '--wall-budget', '{REMAINING}',
                                                    '--mem-cap', '8000000000', '--rates', RATES]),
          dict(label='ctl_verify', argv=ver + CT + ['--prime', str(P1), '--dir', f'{d}/out', '--out', f'{d}/out/{TAG}_p{P1}_verify.json'])]
    run('sup_ctl', sv + ['--cap-secs', '600', '--out', f'{d}/out', '--artifact-stop', '1000000000', '--receipt', f'{d}/job_receipt.json', '--steps', json.dumps(st)], 0,
        lambda: (lambda r: dict(steps=[(s['label'], s['rc']) for s in r['steps']], verdict=J(f'{d}/out/{TAG}_p{P1}_verify.json')['verdict'],
                                ok=[s['rc'] for s in r['steps']] == [0, 0]))(J(f'{d}/job_receipt.json')))

    # ---- the frozen launcher's preflight (builds nothing)
    run('launcher_preflight', ['/bin/bash', f'{F}/b28_01c_cellA.sh', '--preflight-only'], 0)

    # ---- cal1 sizing only (gate inputs for the memory-model check; no Schur): not a calibration replay
    run('cal1_gate_only', drv + C1 + ['--nchi', '188872', '--primes', str(P1), '--out', f'{OUT}/cal1_gate', '--wall-budget', '3000',
                                     '--mem-cap', '24000000000', '--rates', RATES, '--gate-only'], 0, None, f'{OUT}/cal1_gate')

    # ---- regression 2: one calibration cell, (13,9,9,3,1,1)_9 (s79_cells.jsonl line 121), P1, driver and verifier
    c2 = f'{OUT}/cal2'
    run('reg_cal2_driver', drv + C2 + ['--nchi', '732815', '--primes', str(P1), '--out', c2, '--wall-budget', '3000',
                                      '--mem-cap', '24000000000', '--rates', RATES], 0, None, c2)
    run('reg_cal2_verify', ver + C2 + ['--prime', str(P1), '--dir', c2, '--out', f'{c2}/13_9_9_3_1_1_d9_p{P1}_verify.json'], 0,
        verdict(f'{c2}/13_9_9_3_1_1_d9_p{P1}_verify.json', 'FULL_RANK'))
    finish(True)


if __name__ == '__main__':
    main()

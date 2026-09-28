#!/usr/bin/env python3
"""
B28-01c -- bookkeeping after the controls harness (no arithmetic on matrices beyond
hashing): copies the deterministic outputs into the worktree, compares the
regression outputs with B28-01a's committed or host-retained bytes, lists every
JSON field that differs, checks the gate's memory model against the measured
calibration peaks, and binds the host-retained files.

usage: b28_01c_finalize.py WORKTREE
"""
import sys, os, json, glob, shutil, hashlib

WT = sys.argv[1]
HOME = os.path.expanduser('~')
OUT = f'{HOME}/b28_01/out_c'; DEV = f'{HOME}/b28_01/c_dev'; FC = f'{HOME}/b28_01/frozen_c'
RES = os.path.join(WT, 'results/b28_01c'); OLD = os.path.join(WT, 'results/b28_01')
P1 = 2147483647
LIMIT = 5_000_000
sys.path.insert(0, FC)
import b28_01c_model as MODEL


def sha_file(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 24), b''): h.update(b)
    return h.hexdigest()


def J(p):
    return json.load(open(p))


def flat(x, pre=''):
    if isinstance(x, dict):
        out = {}
        for k, v in x.items(): out.update(flat(v, f'{pre}.{k}' if pre else k))
        return out
    return {pre: x}


def json_diff(old, new):
    a, b = flat(J(old)), flat(J(new))
    return dict(added=sorted(set(b) - set(a)), removed=sorted(set(a) - set(b)),
                changed={k: dict(old=a[k], new=b[k]) for k in sorted(set(a) & set(b)) if a[k] != b[k]})


def main():
    assert not os.path.exists(RES)
    os.makedirs(RES)
    retained = []
    # ---- copy the harness outputs (files above LIMIT are host-retained, bound by hash)
    for p in sorted(glob.glob(f'{OUT}/**/*', recursive=True)):
        if not os.path.isfile(p): continue
        rel = os.path.relpath(p, OUT); sz = os.path.getsize(p)
        if sz > LIMIT:
            retained.append(dict(host_path=f'out_c/{rel}', bytes=sz, sha256=sha_file(p))); continue
        dst = os.path.join(RES, 'out_c', rel); os.makedirs(os.path.dirname(dst), exist_ok=True); shutil.copyfile(p, dst)
    for nm in ('host_rates_c.json', 'cellA_price_c.json', 'frozen_c_hashes.txt', 'scope_limits_receipt.txt', 'harness_stdout.txt',
               'harness_start.txt', 'harness_end.txt'):
        shutil.copyfile(os.path.join(DEV, nm), os.path.join(RES, nm))
    shutil.copyfile(os.path.join(FC, 'gate_rates_c.json'), os.path.join(RES, 'gate_rates_c.json'))
    # the committed analysis/ copies must be the frozen bytes
    fro = dict(l.split()[::-1] for l in open(os.path.join(DEV, 'frozen_c_hashes.txt')))
    code_match = {k: (sha_file(os.path.join(WT, 'analysis', k)) == v) for k, v in fro.items() if k.endswith(('.py', '.c', '.sh'))}

    # ---- regression: the control cell at both primes
    reg = dict(control={}, cal2={})
    oc, nc = os.path.join(OLD, 'control'), f'{OUT}/control'; t = '22_6_5_2_1_d9'
    for f in [f'{t}_p{p}_{x}.u32' for p in (P1, 2147483629) for x in ('K', 'VK')] + [f'{t}_pencils.json'] + [f'{t}_cover_{x}.npy' for x in ('S', 'U', 'rows')]:
        reg['control'][f] = dict(old=sha_file(os.path.join(oc, f)), new=sha_file(os.path.join(nc, f)))
        reg['control'][f]['identical'] = reg['control'][f]['old'] == reg['control'][f]['new']
    jd = {f'{t}_cell.json': json_diff(os.path.join(oc, f'{t}_cell.json'), os.path.join(nc, f'{t}_cell.json'))}
    for p in (P1, 2147483629):
        for s in ('cert', 'verify'):
            f = f'{t}_p{p}_{s}.json'; jd[f] = json_diff(os.path.join(oc, f), os.path.join(nc, f))
    reg['control_json_fields'] = jd
    # ---- regression: cal2 at P1 (large files against HOST_RETAINED.json)
    hr = {e['host_path']: e['sha256'] for e in J(os.path.join(OLD, 'HOST_RETAINED.json'))['files']}
    oc, nc = os.path.join(OLD, 'cal2'), f'{OUT}/cal2'; t = '13_9_9_3_1_1_d9'
    for f in (f'{t}_p{P1}_K.u32', f'{t}_cover_S.npy', f'{t}_cover_rows.npy'):
        reg['cal2'][f] = dict(old=hr[f'out/cal2/{f}'], old_source='results/b28_01/HOST_RETAINED.json', new=sha_file(os.path.join(nc, f)))
    for f in (f'{t}_p{P1}_VK.u32', f'{t}_pencils.json', f'{t}_cover_U.npy'):
        reg['cal2'][f] = dict(old=sha_file(os.path.join(oc, f)), old_source='results/b28_01/cal2', new=sha_file(os.path.join(nc, f)))
    for v in reg['cal2'].values(): v['identical'] = v['old'] == v['new']
    reg['cal2_json_fields'] = {f: json_diff(os.path.join(oc, f), os.path.join(nc, f))
                               for f in (f'{t}_cell.json', f'{t}_p{P1}_cert.json', f'{t}_p{P1}_verify.json')}
    # mathematical values that must not move (ranks, minors, hashes) -- flagged if any changed field names one of them
    guard = ('sha256', 'rank', 'minor', 'mult_det', 'nullity', 'nU', 'nS', 'n_chi', 'N_S', 'rows_E', 'nnz_E', 'cover')
    moved = [(f, k) for grp in ('control_json_fields', 'cal2_json_fields') for f, d in reg[grp].items() for k in d['changed']
             if any(g in k for g in guard)]
    files_ok = all(v['identical'] for grp in ('control', 'cal2') for v in reg[grp].values())
    reg['summary'] = dict(all_binary_outputs_identical=files_ok, mathematical_json_values_changed=moved,
                          regression_unchanged=bool(files_ok and not moved))
    json.dump(reg, open(os.path.join(RES, 'REGRESSION.json'), 'w'), indent=1, sort_keys=True)

    # ---- the gate's memory model against measured peaks (verifier and producer, per phase)
    cov = []
    def model_for(gate, cell):
        return MODEL.verifier_mem(cell['n_chi'], gate['N_S'], cell['delta'], cell['a'], gate['z'], gate['rows_E'], gate['U'],
                                  gate['nS'], gate['rows_other'], gate['z_cover_rows'], gate['z_other_rows'])[0]
    cases = [('control (22,6,5,2,1)_9', f'{OUT}/control', '22_6_5_2_1_d9',
              [f'{OUT}/control/22_6_5_2_1_d9_p{P1}_verify_receipt.json', os.path.join(OLD, f'control/22_6_5_2_1_d9_p{P1}_verify_receipt.json')],
              [f'{OUT}/control/22_6_5_2_1_d9_receipt.json', os.path.join(OLD, 'control/22_6_5_2_1_d9_receipt.json')]),
             ('cal1 (24,6,5,3,2)_10 [gate inputs from the sizing run; peaks from B28-01a]', f'{OUT}/cal1_gate', '24_6_5_3_2_d10',
              [os.path.join(OLD, f'cal1/24_6_5_3_2_d10_p{P1}_verify_receipt.json')], [os.path.join(OLD, 'cal1/24_6_5_3_2_d10_receipt.json')]),
             ('cal2 (13,9,9,3,1,1)_9', f'{OUT}/cal2', '13_9_9_3_1_1_d9',
              [f'{OUT}/cal2/13_9_9_3_1_1_d9_p{P1}_verify_receipt.json', os.path.join(OLD, f'cal2/13_9_9_3_1_1_d9_p{P1}_verify_receipt.json')],
              [f'{OUT}/cal2/13_9_9_3_1_1_d9_receipt.json', os.path.join(OLD, 'cal2/13_9_9_3_1_1_d9_receipt.json')])]
    for name, d, t, vrs, prs in cases:
        cell = J(f'{d}/{t}_cell.json'); gate = J(f'{d}/{t}_receipt.json')['gate']
        est = model_for(gate, cell)
        vpk = max(ph['peak_rss_bytes'] for r in vrs for ph in J(r)['phases'])
        ppk = max(ph['peak_rss_bytes'] for r in prs for ph in J(r)['phases'])
        cov.append(dict(cell=name, verifier_estimate_bytes=est, recorded_gate_estimate_bytes=gate['verifier_mem_estimate_bytes'],
                        producer_envelope_bytes=gate['mem_envelope_bytes'], needed_bytes=gate['mem_needed_bytes'],
                        max_verifier_phase_peak_bytes=vpk, max_producer_phase_peak_bytes=ppk,
                        verifier_covered=est >= vpk, producer_covered=gate['mem_envelope_bytes'] >= ppk, needed_covers_both=gate['mem_needed_bytes'] >= max(vpk, ppk),
                        verifier_peaks_from=[os.path.relpath(r, WT) if r.startswith(WT) else 'out_c/' + os.path.relpath(r, OUT) for r in vrs]))
    # the regression's cal2 timings against the gate's own prediction at cal2
    g2 = J(f'{OUT}/cal2/13_9_9_3_1_1_d9_receipt.json'); v2 = J(f'{OUT}/cal2/13_9_9_3_1_1_d9_p{P1}_verify_receipt.json')
    timing = dict(cal2_gate_predicted_producer_remaining_secs=g2['gate']['predicted_producer_remaining_secs'],
                  cal2_measured_producer_after_gate_secs=round(sum(p['secs'] for p in g2['phases'] if p['phase'] not in ('build', 'cover')), 3),
                  cal2_gate_predicted_verifier_secs=g2['gate']['predicted_verifier_secs'], cal2_measured_verifier_secs=v2['total_secs'],
                  note='receipt times (monotonic); nondeterministic, reported only as a check that the gate did not under-price the cell it was fitted on')
    json.dump(dict(schema='b28-01c-memory-model-check/1', rule='verifier estimate (b28_01c_model.verifier_mem) >= max measured verifier phase VmHWM; '
                   'producer envelope >= max measured producer phase VmHWM', cases=cov, timing_check=timing),
              open(os.path.join(RES, 'GATE_MODEL_CHECK.json'), 'w'), indent=1, sort_keys=True)
    json.dump(dict(schema='b28-01c-host-retained/1', rule='files larger than 5000000 bytes are not committed; bound here by raw SHA-256; host root ~/b28_01',
                   files=retained), open(os.path.join(RES, 'HOST_RETAINED.json'), 'w'), indent=1)
    json.dump(dict(code_matches_frozen=code_match), open(os.path.join(RES, 'CODE_BINDING.json'), 'w'), indent=1, sort_keys=True)
    print(json.dumps(dict(regression=reg['summary'], coverage=[(c['cell'][:5], c['verifier_covered'], c['producer_covered'], c['needed_covers_both']) for c in cov],
                          timing=timing, code_match=all(code_match.values()), retained=len(retained)), indent=1))


if __name__ == '__main__':
    main()

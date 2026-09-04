#!/usr/bin/env python3
"""
Session 46 -- the Phase 3 sweep: one cell at a time, in the pre-registered
order, banked with a commit before the next is started.

Order: results/s46_order.json, written by wk9_s46_reach.py before any Phase 3
cell is measured (ascending in predicted cost, most balanced first at each
size).  Cells already present in results/s46_cells.jsonl are skipped.

Each cell is launched in its own process with `timeout` and `ulimit -v` set at
launch and its process id written to results/logs/<tag>.pid, as the standing
rules require; a cell that exits non-zero is recorded as not reached and the
sweep moves on rather than retrying at a coarser setting.

Level policy (docs/sparse_det_route.md section 3c): start at (12,2) when the
predicted n_rows / n_chi is above 10, else at (3,2).

usage: python3 wk9_s46_sweep.py [--budget SECONDS] [--per-cell SECONDS] [--dry]
"""
import sys, os, json, time, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
R = os.path.join(HERE, '..', 'results')
LOGS = os.path.join(R, 'logs')

def done_cells():
    p = os.path.join(R, 's46_cells.jsonl')
    out = set()
    if os.path.exists(p):
        for l in open(p):
            try: d = json.loads(l)
            except Exception: continue
            out.add((tuple(d['lam']), d['delta']))
    return out

def bank(tag, msg):
    subprocess.run(['git', 'add', '-A', 'results/'], cwd=os.path.join(HERE, '..'))
    subprocess.run(['git', '-c', 'user.name=session46', '-c', 'user.email=s46@gct.local',
                    'commit', '-q', '-m', msg + "\n\nCo-Authored-By: Claude Opus 5 <noreply@anthropic.com>"],
                   cwd=os.path.join(HERE, '..'))

def run_cell(rec, per_cell, vlimit=6800000):
    lam = tuple(rec['lam']); delta = rec['delta']
    tag = 'c' + '_'.join(map(str, lam)) + f'd{delta}'
    lv = 's42' if rec.get('rows_over_nchi', 0) > 10 else 'cheap'
    args = [str(delta)] + [str(x) for x in lam] + ['--side', 'det', '--levels', lv,
                                                   '--out', os.path.join(R, 's46_cells.jsonl')]
    cmd = (f"ulimit -v {vlimit}; exec timeout {per_cell} python3 wk9_s46_cell.py " +
           ' '.join(args))
    out = open(os.path.join(LOGS, f's46_{tag}.out'), 'w')
    err = open(os.path.join(LOGS, f's46_{tag}.err'), 'w')
    p = subprocess.Popen(['bash', '-c', cmd], cwd=HERE, stdout=out, stderr=err,
                         stdin=subprocess.DEVNULL, start_new_session=True)
    with open(os.path.join(LOGS, f's46_{tag}.pid'), 'w') as f: f.write(str(p.pid) + "\n")
    rc = p.wait()
    out.close(); err.close()
    return tag, rc, lv

if __name__ == '__main__':
    budget = 10 ** 9; per_cell = 43200; dry = False
    a = sys.argv[1:]; i = 0
    while i < len(a):
        if a[i] == '--budget': budget = float(a[i + 1]); i += 2
        elif a[i] == '--per-cell': per_cell = int(a[i + 1]); i += 2
        elif a[i] == '--dry': dry = True; i += 1
        else: i += 1
    order = json.load(open(os.path.join(R, 's46_order.json')))
    t0 = time.time()
    for rec in order:
        key = (tuple(rec['lam']), rec['delta'])
        if key in done_cells():
            print(f"skip {key} (banked)", flush=True); continue
        if time.time() - t0 + rec['secs'] > budget:
            print(f"stop: {key} predicted {rec['secs']:.0f}s does not fit the remaining budget",
                  flush=True); break
        print(f"=== {key} bal={rec['bal']} a={rec['a']} n_chi={rec['n_chi']} "
              f"predicted {rec['secs']/3600:.2f} h ===", flush=True)
        if dry: continue
        tag, rc, lv = run_cell(rec, per_cell)
        if rc != 0:
            print(f"  NOT REACHED (exit {rc}); recorded and moving on", flush=True)
            with open(os.path.join(R, 's46_notreached.jsonl'), 'a') as f:
                f.write(json.dumps(dict(lam=list(key[0]), delta=key[1], exit=rc,
                                        level=lv, predicted_secs=rec['secs'])) + "\n")
            bank(tag, f"s46 sweep: {key[0]} d{key[1]} not reached (exit {rc})")
            continue
        last = None
        for l in open(os.path.join(R, 's46_cells.jsonl')):
            d = json.loads(l)
            if (tuple(d['lam']), d['delta']) == key: last = d
        v = last['sides']['det'] if last else {}
        print(f"  {key}: nullity {v.get('nullity')} -> mult_det = {v.get('mult')} "
              f"(a = {last['a']}) in {last['secs']}s", flush=True)
        bank(tag, f"s46 sweep: {key[0]} d{key[1]} balance {rec['bal']} n_chi {last['n_chi']} "
                  f"-- nullity {v.get('nullity')}, mult_det = {v.get('mult')} of a = {last['a']}")
        if v.get('nullity', 0) != 0:
            print("  *** nullity > 0: halting the sweep; the verification protocol takes over "
                  "(results/PREREG_s46.md section 5)", flush=True)
            break
    print("SWEEP DONE", flush=True)

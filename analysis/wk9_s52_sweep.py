#!/usr/bin/env python3
"""
Session 52 -- the a = 1 sweep.

Runs results/s52_todo.json ascending in the n_chi estimate, one cell per
process group, through the session-45 sparse certificate
(analysis/wk9_s45_cell.py), banking each row to results/s52_ledger.jsonl before
the next cell starts.  Every run is bounded by `timeout`; the process id of the
run is written to results/logs/s52_sweep.pid.

At a = 1 the determinant-side certificate is exactly the brief's cheap
direction: nullity_p([E; ev_det]) = 0 at one prime proves mult_det = 1 = a over
Q, i.e. i_det = 0.  A nonzero nullity at BOTH primes is a candidate i_det = 1
and halts the sweep for the verification protocol.

usage: python3 wk9_s52_sweep.py [--limit N] [--timeout 3600] [--max-nchi 200000]
"""
import sys, os, json, subprocess, time

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
LEDGER = os.path.join(ROOT, 'results/s52_ledger.jsonl')


def done():
    if not os.path.exists(LEDGER): return set()
    out = set()
    for ln in open(LEDGER):
        r = json.loads(ln)
        out.add((tuple(r['lam']), r['delta']))
    return out


def arg(name, default):
    return type(default)(sys.argv[sys.argv.index(name) + 1]) if name in sys.argv else default


if __name__ == '__main__':
    limit = arg('--limit', 100)
    tmo = arg('--timeout', 3600)
    maxn = arg('--max-nchi', 200000)
    todo = json.load(open(os.path.join(ROOT, 'results/s52_todo.json')))
    D = done()
    env = dict(os.environ, WIED_BIN='/home/claude/wied45', WIED_WORK='/home/claude/s45/work')
    n = 0
    for c in todo:
        if n >= limit: break
        lam = tuple(c['lam']); d = c['delta']
        if (lam, d) in D: continue
        if c['nchi_lb'] > maxn: continue
        n += 1
        cmd = ['timeout', str(tmo), 'python3', os.path.join(ROOT, 'analysis/wk9_s45_cell.py'),
               str(d)] + [str(x) for x in lam] + ['--side', 'both']
        t0 = time.time()
        print(f"[sweep] {n}: d{d} {lam} h_pad={c['h_pad']} nchi~{c['nchi_lb']} ...", file=sys.stderr, flush=True)
        p = subprocess.run(cmd, capture_output=True, text=True, env=env, cwd=ROOT)
        last = [l for l in p.stdout.strip().split('\n') if l.startswith('{')]
        if p.returncode != 0 or not last:
            rec = dict(lam=list(lam), delta=d, a=1, h_pad=c['h_pad'], status='DEFER',
                       rc=p.returncode, secs=round(time.time() - t0, 1),
                       tail=p.stderr.strip().split('\n')[-3:])
        else:
            rec = json.loads(last[-1])
            rec['h_pad'] = c['h_pad']
            rec['status'] = 'measured'
            rec['i_det'] = rec['a'] - rec['mult_det'] if rec.get('mult_det') is not None else None
            rec['i_pad'] = rec['a'] - rec['mult_pad'] if rec.get('mult_pad') is not None else None
            rec['D'] = (rec['mult_pad'] - rec['mult_det']) if rec.get('mult_pad') is not None else None
        with open(LEDGER, 'a') as fh:
            fh.write(json.dumps(rec) + "\n")
        print(f"[sweep] banked {lam} d{d}: {rec.get('status')} "
              f"mult_det={rec.get('mult_det')} mult_pad={rec.get('mult_pad')} D={rec.get('D')} "
              f"({rec.get('secs')}s)", file=sys.stderr, flush=True)
        if rec.get('D') is not None and rec['D'] > 0:
            print("[sweep] D > 0 -- halting the sweep; the verification protocol takes over",
                  file=sys.stderr, flush=True)
            break

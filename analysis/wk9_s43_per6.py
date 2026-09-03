#!/usr/bin/env python3
"""
Session 43, Phase B -- closing I(D_6^{per_3})_7 = 0, and continuing the same
scan at delta = 8.

Session 41's Phase 0b measured 20 of the 27 length-6 weights mu |- 21 with
a(mu, 7) >= 1 (all a = 1, all mult = a), stopping at n_chi <= 6000.  The seven
left are (9,4,3,2,2,1), (8,5,3,2,2,1), (7,6,3,2,2,1), (7,5,4,3,1,1),
(7,5,4,2,2,1), (6,6,4,2,2,1) and (6,5,4,3,2,1); this driver measures them in
ascending n_chi, then continues at delta = 8 above n_chi = 6000 while budget
allows.  If every delta = 7 weight is empty then I(D_6^{per_3})_7 = 0 outright
and, by Prop. 8(1) of docs/transfer_lemma.md, mult_pad = mult_red in every
weight of degree 7 -- a theorem with no points in it.

Measurement is wk9_s41_per6.measure_per6 unchanged (points per_3(sum s_i A_i),
n = 3, r = 6, both house primes, a + 8 points), each weight in its own process,
under the shared memory guard of wk9_s43_guard.py.  A weight with mult < a gets
the independent re-check (3a + 24 points, fresh seed 907, both primes) inside
the same process before it is banked, and then halts the phase: it would be the
first permanent equation the programme has seen.

Bounding: each weight process runs under `timeout` and `ulimit -v`, its process
id recorded in results/logs/s43_per6.pid.

usage: python3 wk9_s43_per6.py <delta_lo> <delta_hi> [--nchi-cap 20000] [--min-nchi 6000]
"""
import sys, os, time, json, subprocess

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
from wk9_s43_guard import predicted_gb, free_gb, heavy_lock, wait_for_memory, WORK
from wk8_s30_pleth import a_of
from wk9_s41_per6 import partitions
from wk9_s36_stabred import orbit_setup, monomials

OUT = os.path.join(ROOT, 'results', 's43_per6.md')
LOGS = os.path.join(ROOT, 'results', 'logs')
STOP = os.path.join(WORK, 'STOP_B')
VMCAP_KB = 6900000

HEADER = """# `I(D_6^{per_3})` in `C[Sym^3 C^6]` above session 41's cap — session 43, Phase B

Continuation of `results/s41_per6.md` (which measured every length-6 weight `μ ⊢ 3δ`, `a(μ,δ) ≥ 1`, with
`n_χ ≤ 6000`).  Same reduced pipeline (`wk9_s36_stabred`, `n = 3`, `r = 6`), points `per_3(Σ s_i A_i)`, both
house primes, `a + 8` points; independent re-check at `3a + 24` points (seed 907, both primes) on any
`mult < a`.  `units = a − mult` is the ideal's share.  By Prop. 8(1) of `docs/transfer_lemma.md`,
`I(D_6^{per_3})_δ = 0` ⇒ `mult_pad = mult_red` at **every** weight of degree `δ`.  `route` is `dense` for the
in-place rref of `analysis/wk9_s41_kernel.py`, `inject` for the `a = 1` sparse injectivity certificate of
`analysis/wk9_s43_inject.py` (pre-registered in `results/PREREG_s43.md` §2 P3, validated before use).

| delta | mu | a | N_S | Stab | n_chi | route | mult | units | secs | HWM |
|---|---|---|---|---|---|---|---|---|---|---|
"""


def log(*a):
    print(time.strftime('%H:%M:%S'), *a, flush=True)


def banked():
    done = set()
    if os.path.exists(OUT):
        for ln in open(OUT):
            if ln.startswith('| ') and ln[2].isdigit():
                c = [x.strip() for x in ln.strip().strip('|').split('|')]
                try:
                    done.add((int(c[0]), tuple(int(x) for x in c[1].strip('`').strip('()').split(','))))
                except Exception:
                    pass
    return done


def bank(line):
    new = not os.path.exists(OUT)
    with open(OUT, 'a') as fh:
        if new:
            fh.write(HEADER)
        fh.write(line + "\n"); fh.flush(); os.fsync(fh.fileno())


def commit(msg):
    subprocess.run(['git', '-C', ROOT, 'add', 'results/s43_per6.md'], capture_output=True)
    subprocess.run(['git', '-C', ROOT, '-c', 'user.name=s43', '-c', 'user.email=s43@gct',
                    'commit', '-q', '-m',
                    msg + "\n\nCo-Authored-By: Claude Opus 5 <noreply@anthropic.com>"],
                   capture_output=True)


def timeout_for(n_chi):
    return int(max(900, 6.0 * 2500 * (n_chi / 19985.0) ** 2.7))


if __name__ == '__main__':
    USE_INJECT = '--inject' in sys.argv
    if sys.argv[1] == '--one':
        from wk9_s41_per6 import measure_per6
        from wk9_s41_kernel import vm_hwm
        delta = int(sys.argv[2]); mu = tuple(int(x) for x in sys.argv[3].split(',')); a = int(sys.argv[4])
        res = measure_per6(delta, mu, a)
        if res['mult'] < a:
            log(f"   *** {mu}: mult {res['mult']} < a {a} — independent re-check (3a+24 points, seed 907)")
            res2 = measure_per6(delta, mu, a, npts=3 * a + 24, seed=907)
            assert res2['mult'] == res['mult'], ("short rank unstable", mu, res, res2)
            res['recheck'] = res2['mult']
        res['hwm'] = vm_hwm(); res['route'] = 'dense'
        print("RESULT " + json.dumps(res), flush=True)
        sys.exit(0)

    lo, hi = int(sys.argv[1]), int(sys.argv[2])
    cap = int(sys.argv[sys.argv.index('--nchi-cap') + 1]) if '--nchi-cap' in sys.argv else 20000
    lo_nchi = int(sys.argv[sys.argv.index('--min-nchi') + 1]) if '--min-nchi' in sys.argv else 6000
    done = banked()
    # session 41's rows count as banked too: this file is a continuation, not a redo
    s41 = os.path.join(ROOT, 'results', 's41_per6.md')
    for ln in open(s41):
        if ln.startswith('| ') and ln[2].isdigit():
            c = [x.strip() for x in ln.strip().strip('|').split('|')]
            try:
                done.add((int(c[0]), tuple(int(x) for x in c[1].strip('`').strip('()').split(','))))
            except Exception:
                pass
    for delta in range(lo, hi + 1):
        cells = [(m, a_of(m, delta, 3, 6)) for m in partitions(3 * delta, 6)]
        cells = [(m, a) for m, a in cells if a >= 1]
        log(f"== delta={delta}: {len(cells)} length-6 weights with a>=1, sum a = {sum(a for _, a in cells)}")
        todo = []
        for m, a in cells:
            if (delta, m) in done:
                continue
            basis, vecs, group = orbit_setup(3, 6, delta, m, verbose=False)
            nchi = len(vecs); monomials.cache_clear()
            todo.append((nchi, m, a, len(basis), len(group)))
        todo.sort()
        log(f"   {len(todo)} unmeasured; {sum(1 for t in todo if lo_nchi < t[0] <= cap)} inside "
            f"({lo_nchi}, {cap}]")
        for nchi, m, a, NS, st in todo:
            if os.path.exists(STOP):
                log("STOP_B present; exiting"); sys.exit(0)
            if USE_INJECT and a == 1 and nchi > lo_nchi:
                pass
            elif not (lo_nchi < nchi <= cap):
                log(f"   skip {m} a={a} n_chi={nchi} (outside ({lo_nchi}, {cap}])"); continue
            if USE_INJECT and a == 1:
                # the a = 1 sparse injectivity certificate (results/PREREG_s43.md P3);
                # validated against the dense route at nine weights of this same family
                # (results/s43_validation.md part D and results/s43_inject_crosscheck.md)
                from wk9_s43_inject import inject_one
                tag = f"per6 d={delta} {m} a=1 n_chi={nchi} [inject]"
                log(f"START {tag}")
                try:
                    res = inject_one(delta, m, 1, verbose=True)
                except Exception as e:
                    with open(os.path.join(LOGS, 's43_failed.txt'), 'a') as fh:
                        fh.write(f"per6-inject {delta} ({','.join(map(str, m))}) {e!r} n_chi={nchi}\n")
                    log(f"NOT REACHED {tag}: {e!r}")
                    continue
                line = (f"| {delta} | `{m}` | 1 | {res['N_S']} | {res['stab']} | {res['n_chi']} | inject | "
                        f"{res['mult']} | {1 - res['mult']} | {res['secs']:.0f} | {res['hwm']:.2f} |")
                bank(line)
                commit(f"s43: per6 delta={delta} {m}: a=1 mult={res['mult']} units={1 - res['mult']} (injectivity route)")
                log(line)
                if res['mult'] < 1:
                    open(STOP, 'w').write(f"permanent equation at {m} delta={delta}\n")
                    log("*** mult < a on the permanent's own ideal — halt Phase B; certify and report ***")
                    sys.exit(0)
                continue
            gb = predicted_gb(nchi)
            tag = f"per6 d={delta} {m} a={a} n_chi={nchi}"
            with heavy_lock(gb, tag, log):
                wait_for_memory(gb, tag, 0.85, log)
                log(f"START {tag} (pred {gb:.1f} GB, free {free_gb():.1f})")
                cmd = ("ulimit -v %d; exec timeout %d %s %s --one %d %s %d"
                       % (VMCAP_KB, timeout_for(nchi), sys.executable, os.path.abspath(__file__),
                          delta, ','.join(map(str, m)), a))
                lf = os.path.join(LOGS, 's43_per6.log')
                with open(lf, 'a') as fh:
                    pr = subprocess.Popen(['bash', '-c', cmd], stdout=subprocess.PIPE, stderr=fh, text=True)
                    open(os.path.join(LOGS, 's43_per6.pid'), 'w').write("%d %s\n" % (pr.pid, tag))
                    out, _ = pr.communicate()
            res = None
            for ln in out.splitlines():
                if ln.startswith('RESULT '):
                    res = json.loads(ln[7:])
            if pr.returncode != 0 or res is None:
                with open(os.path.join(LOGS, 's43_failed.txt'), 'a') as fh:
                    fh.write(f"per6 {delta} ({','.join(map(str, m))}) rc={pr.returncode} n_chi={nchi}\n")
                log(f"NOT REACHED {tag}: rc={pr.returncode}")
                continue
            line = (f"| {delta} | `{m}` | {a} | {res['N_S']} | {res['stab']} | {res['n_chi']} | {res['route']} | "
                    f"{res['mult']} | {a - res['mult']} | {res['secs']:.0f} | {res.get('hwm', 0):.2f} |")
            bank(line)
            commit(f"s43: per6 delta={delta} {m}: a={a} mult={res['mult']} units={a - res['mult']}")
            log(line)
            if res['mult'] < a:
                open(STOP, 'w').write(f"permanent equation at {m} delta={delta}\n")
                log("*** mult < a on the permanent's own ideal — halt Phase B; certify and report ***")
                sys.exit(0)
    log("phase B driver done")

#!/usr/bin/env python3
"""
Session 36 -- the sweep driver (results/PREREG_s36.md section 3 order).

Single worker by default (the container is a one-worker machine above
n_chi ~ 6000); the claim-queue design of wk8_s30_run62c.py is kept so a second
worker on the cheap end cannot collide: O_CREAT|O_EXCL claim files, PID-owned,
released only by wk8_s30_reconcile-style logic when the owner is dead.  The
memory guard WAITS, never skips.  Every cell is banked to results/s36_ledger.md
and committed before the next cell starts.

usage: python3 wk9_s36_sweep.py <who> [--stratum A|B6|B7|all] [--cap-gb 6.5] [--headroom 0.85]
"""
import sys, os, time, pickle, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from wk9_s36_stabred import measure_reduced, expand, orbit_setup, monomials, P1, P2, log
from wk9_s36_census import MEM_PER

ROOT = os.path.join(HERE, '..')
LEDGER = os.path.join(ROOT, 'results', 's36_ledger.md')
CLAIMS = os.path.join(ROOT, 'results', 'claims_s36')
CENSUS = '/root/s36/census.pkl'

HEADER = """# Session 36 ledger — stabiliser-reduced sweep (`n = 4`, `ell >= 5`, `a >= 2`)

Pipeline: `analysis/wk9_s36_stabred.py` (validated: `results/stabred_validation.md`).
`a` by kernel dimension on the `chi_lam`-isotypic component AND by plethysm (asserted
equal); `rank(R) = n_chi − a` asserted; ranks by python-flint `nmod_mat` over
`2147483647` and `2147483629`; `a + 8` evaluation points per side; certified compressed
kernel (`dim ker(Agg) = a` asserted) above `n_chi = 2500`, exact single-rref route below.
**Points.**  det: `det_4(sum_{i<=r} s_i A_i)`, random integer `4x4` `A_i`.  pad: the
**true padded-permanent restriction** `x_0 · per_3(x_1..x_9)` with each `x_t` a random
linear form in `s_1..s_r` (`per_padded(3,4)` through `restrict()`), at every `r` —
never `l · (random cubic)`, which over-estimates `mult_pad` at `r = 6`
(`dim D_6^{per_3} = 50 < 56`).  Convention `D = mult_pad − mult_det`; only `D > 0` is
an obstruction.  **Stratum A** (`delta = 6, ell = 5`) cannot be permanent-specific
(`docs/s35_review.md` §1); **Stratum B** (`ell = 6`) is the first permanent-sensitive
stratum in the programme.

| stratum | lam | delta | ell | a | N_S | Stab | n_chi | rows | route | mult_det | mult_pad | D | secs |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
"""

def free_gb():
    for ln in open("/proc/meminfo"):
        if ln.startswith("MemAvailable:"):
            return int(ln.split()[1]) / 1048576.0
    return 0.0

def wait_for_memory(gb, tag, headroom):
    while gb > headroom * free_gb():
        print(f"   [mem] {tag} needs ~{gb:.1f} GB, {free_gb():.1f} GB free -- waiting", flush=True)
        time.sleep(60)

def claim(lam, who):
    os.makedirs(CLAIMS, exist_ok=True)
    p = os.path.join(CLAIMS, "%s.claim" % "_".join(map(str, lam)))
    try:
        fd = os.open(p, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        return False
    os.write(fd, ("%s %d\n" % (who, os.getpid())).encode()); os.close(fd)
    return True

def banked():
    if not os.path.exists(LEDGER): return set()
    out = set()
    for ln in open(LEDGER):
        if ln.startswith("| A") or ln.startswith("| B"):
            cells = [c.strip() for c in ln.strip().strip('|').split('|')]
            out.add(eval(cells[1].strip('`')))
    return out

def bank(line):
    new = not os.path.exists(LEDGER)
    with open(LEDGER, "a") as fh:
        if new: fh.write(HEADER)
        fh.write(line + "\n"); fh.flush(); os.fsync(fh.fileno())

def commit(msg):
    subprocess.run(["git", "-C", ROOT, "add", "results/s36_ledger.md", "results/s36_cells"],
                   capture_output=True)
    subprocess.run(["git", "-C", ROOT, "-c", "user.name=s36", "-c", "user.email=s36@gct",
                    "commit", "-q", "-m", msg + "\n\nCo-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>\n"
                    "Claude-Session: https://claude.ai/code/session_01QB6t2UxtgLpGwCj9oQ2ZkD"],
                   capture_output=True)

def order(r6, r7, cap_gb):
    """the pre-registered order (PREREG_s36.md section 3)."""
    fits = lambda x: x['gb'] <= cap_gb and not x['s34']
    A = [x for x in r6 if x['ell'] == 5 and fits(x)]
    B6 = [x for x in r6 if x['ell'] == 6 and fits(x)]
    B7 = [x for x in r7 if x['ell'] == 6 and fits(x)]
    A7 = [x for x in r7 if x['ell'] == 5 and fits(x)]      # outside the strata; last
    from wk8_s30_sweep import NINE
    s30 = set()
    for ln in open(os.path.join(ROOT, 'results', 'sweep62_ledger.md')):
        if ln.startswith("| ("): s30.add(eval(ln.split('|')[1].strip()))
    A = [x for x in A if x['lam'] not in s30]
    head = [(8, 4, 4, 4, 4), (8, 8, 4, 2, 2), (8, 6, 6, 2, 2)]
    Ahead = [x for l in head for x in A if x['lam'] == l]
    Arest = [x for x in A if x['lam'] not in head]
    def interleave(cells, key_probe):
        asc = sorted(cells, key=lambda x: x['n_chi'])
        out, used = [], set()
        probes = sorted(cells, key=key_probe)
        k = 0
        for x in asc:
            if x['lam'] in used: continue
            out.append(x); used.add(x['lam']); k += 1
            if k % 3 == 0:
                for pr in probes:
                    if pr['lam'] not in used:
                        out.append(pr); used.add(pr['lam']); break
        return out
    Aseq = Ahead + interleave(Arest, lambda x: (x['bal'], -x['a'], x['n_chi']))
    B6seq = sorted(B6, key=lambda x: (x['lam'] != (7, 7, 4, 4, 1, 1), x['n_chi']))
    B7seq = interleave(B7, lambda x: (-x['a'], x['bal'], x['n_chi']))
    # B's first two before A's tail
    seq = [('A', x) for x in Aseq[:3]] + [('B', x) for x in B6seq[:2]] + \
          [('A', x) for x in Aseq[3:]] + [('B', x) for x in B6seq[2:]] + \
          [('B', x) for x in B7seq] + [('A7', x) for x in sorted(A7, key=lambda x: x['n_chi'])]
    return seq

def run_cell(strat, x, delta, who, headroom, npts=None, seed_shift=0):
    lam = x['lam']; r = len(lam); a = x['a']
    tag = f"{strat} {lam} d={delta}"
    wait_for_memory(x['gb'], tag, headroom)
    if not claim(lam, who): return None
    t0 = time.time()
    seeds = dict(det=11 + seed_shift, pad=29 + seed_shift)
    out = measure_reduced(4, r, delta, lam, a, npts=npts, seeds=seeds)
    for sd in ('det', 'pad'):
        if out['mult_' + sd] < a:
            log(f"  *** {tag}: mult_{sd} = {out['mult_'+sd]} < a = {a}: sceptical branch (3a+24 pts, seed 907)")
            o2 = measure_reduced(4, r, delta, lam, a, npts=3 * a + 24, seeds=dict(det=907, pad=907))
            assert o2['mult_' + sd] == out['mult_' + sd], ("short rank unstable", lam, sd, out['mult_' + sd], o2['mult_' + sd])
            os.makedirs(os.path.join(ROOT, 'results', 's36_cells'), exist_ok=True)
            with open(os.path.join(ROOT, 'results', 's36_cells', "%s_%s.txt" % ("_".join(map(str, lam)), sd)), 'w') as fh:
                fh.write(f"# {tag}: mult_{sd} = {out['mult_'+sd]} < a = {a}; re-run 3a+24 points seed 907: {o2['mult_'+sd]}\n")
                fh.write(f"# per-prime kernels (chi-coordinates) and full expansions follow\n")
                for p in (P1, P2):
                    fh.write(f"prime {p}\n")
                    for kv in out['per_prime'][p]['kern']: fh.write(repr(kv) + "\n")
    D = out['mult_pad'] - out['mult_det']
    line = (f"| {strat} | `{lam}` | {delta} | {r} | {a} | {out['N_S']} | {out['stab']} | {out['n_chi']} | "
            f"{out['nrows']} | {out['route']} | {out['mult_det']} | {out['mult_pad']} | {D:+d} | {out['secs']:.0f} |")
    bank(line)
    pickle.dump({k: v for k, v in out.items()}, open(f"/root/s36/cell_{'_'.join(map(str, lam))}_d{delta}.pkl", 'wb'))
    commit(f"s36: bank {strat} {lam} delta={delta}: a={a} mult_det={out['mult_det']} mult_pad={out['mult_pad']} D={D:+d}")
    print(line, flush=True)
    monomials.cache_clear()
    return D

if __name__ == '__main__':
    who = sys.argv[1]
    strat_sel = sys.argv[sys.argv.index('--stratum') + 1] if '--stratum' in sys.argv else 'all'
    cap = float(sys.argv[sys.argv.index('--cap-gb') + 1]) if '--cap-gb' in sys.argv else 6.5
    headroom = float(sys.argv[sys.argv.index('--headroom') + 1]) if '--headroom' in sys.argv else 0.85
    r6, r7 = pickle.load(open(CENSUS, 'rb'))
    seq = order(r6, r7, cap)
    done = banked()
    print("order:", [(s, x['lam'], x['n_chi']) for s, x in seq], flush=True)
    for strat, x in seq:
        delta = sum(x['lam']) // 4
        s = {'A': 'A', 'B': 'B6' if delta == 6 else 'B7', 'A7': 'A7'}[strat]
        if strat_sel != 'all' and s != strat_sel: continue
        if x['lam'] in done: continue
        D = run_cell(strat, x, delta, who, headroom)
        if D is not None and D > 0:
            print("*** D > 0: STOP-EVERYTHING — obstruction protocol ***", flush=True); break
    print("worker done", flush=True)

"""Session 56 — validate the C signed kernel at delta = 4 against the direct
tensor sum on a random sample of partitions (the coset-decomposition sign
formula is validated exhaustively at delta = 2, 3 by wk9_s56_hecke.py; here it is
spot-checked where the exhaustive comparison is not affordable)."""
import os
import random
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import wk9_s56_core as C   # noqa: E402

delta = 4
N = 16
t0 = time.time()
out = os.path.join(ROOT, "results", "logs", "s56_krow_d4.txt")
cmd = f"ulimit -v 4000000; exec timeout 600 {HERE}/wk9_s56_pass 4 0 /dev/null krow > {out}"
proc = subprocess.Popen(["bash", "-c", cmd])
with open(os.path.join(ROOT, "results", "logs", "s56_krow_d4.pid"), "w") as fp:
    fp.write(str(proc.pid) + "\n")
assert proc.wait() == 0
with open(out) as fh:
    krow = [int(x) for x in fh]
print(f"C krow: {len(krow)} values in {time.time()-t0:.1f}s; distinct |K|: {sorted(set(abs(k) for k in krow))}")
H = C.set_partitions(N)
assert len(H) == len(krow) == 2627625
pi0 = C.standard_partition(delta)
assert krow[H.index(pi0)] == 24 ** 4
rng = random.Random(56)
idx = rng.sample(range(len(H)), 24)
bad = 0
for i in idx:
    direct = C.kernel_K(pi0, H[i], N)
    ok = direct == krow[i]
    bad += not ok
    print(f"  pi index {i}: C {krow[i]:>8d}  direct {direct:>8d}  {'ok' if ok else 'MISMATCH'}", flush=True)
# every |K| class value equals a double-coset value: the multiset of |K| by class
print(f"sample mismatches: {bad}; total {time.time()-t0:.1f}s")
sys.exit(1 if bad else 0)

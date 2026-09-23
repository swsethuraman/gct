"""B27-03 run 5: rank certificates along the peaked ray w_k=(4k-8,2,2,2,2), k=3..7 (both rings),
and the next ray (4k-9,3,2,2,2) at k=9 (65-ring).  Library: analysis/b27_03_kernel_lib.py;
points: seed 7777 LCG, entries in {-5..5}, N+32 points."""
import json, sys, time, importlib.util
spec = importlib.util.spec_from_file_location("k", "analysis/b27_03_kernel_lib.py")
k = importlib.util.module_from_spec(spec); spec.loader.exec_module(k)
t0 = time.time()
k.state = 7777
def lcg11():
    k.state = (1103515245 * k.state + 12345) % 2**31
    return ((k.state >> 16) % 11) - 5
k.lcg = lcg11
k.EXTRA = 32
src = open("analysis/b27_03_kernel_lib.py").read()
assert "npts = N + 16 if EXTRA is not None else 2 * N" in src
_old = k.certify
def certify(*a, **kw):   # N+32 rows instead of N+16
    k.EXTRA = 32
    return _old(*a, **kw)
jobs = []
for kk in range(3, 8):
    for ring in (65, 70):
        jobs.append((f"ray1 k={kk}, {ring}-ring", kk, (4 * kk - 8, 2, 2, 2, 2), ring))
jobs.append(("ray2 k=9 w=(27,3,2,2,2), 65-ring", 9, (27, 3, 2, 2, 2), 65))
res = []
for j in jobs:
    t1 = time.time()
    rec = certify(*j, cap=1100)
    rec["wall_s"] = round(time.time() - t1, 2)
    res.append(rec); print(rec, flush=True)
    if time.time() - t0 > 50: print("time guard hit"); break
json.dump({"script": "analysis/b27_03_rays.py", "p": k.P, "lcg_seed": 7777, "entries": "-5..5",
           "rows": "N+16 (library constant)", "results": res, "wall_s": round(time.time() - t0, 2)},
          open(sys.argv[1], "w"), indent=1)

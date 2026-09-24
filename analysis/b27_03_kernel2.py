"""B27-03 run 3: re-test with an independent point set (seed 7777, entries in {-5..5}, 2N points)
and extend to nearby degree-8 weights of the 65-coordinate ring.  Same certificate logic as
analysis/b27_03_kernel.py (imported); only the point generator and job list differ."""
import json, sys, time, importlib.util
import numpy as np
spec = importlib.util.spec_from_file_location("k", "analysis/b27_03_kernel_lib.py")
k = importlib.util.module_from_spec(spec); spec.loader.exec_module(k)
t0 = time.time()
k.state = 7777
def lcg11():
    k.state = (1103515245 * k.state + 12345) % 2**31
    return ((k.state >> 16) % 11) - 5
k.lcg = lcg11
k.EXTRA = None   # use 2N points
jobs = [("A26-01 weight, 70-ring, fresh points", 8, (24, 2, 2, 2, 2), 70),
        ("A26-01 H, 65-ring, fresh points",      8, (24, 2, 2, 2, 2), 65),
        ("k=8 w=(23,3,2,2,2), 65-ring",          8, (23, 3, 2, 2, 2), 65),
        ("k=8 w=(22,4,2,2,2), 65-ring",          8, (22, 4, 2, 2, 2), 65),
        ("k=8 w=(22,3,3,2,2), 65-ring",          8, (22, 3, 3, 2, 2), 65)]
res = []
for j in jobs:
    t1 = time.time()
    rec = k.certify(*j, cap=1500)
    rec["wall_s"] = round(time.time() - t1, 2)
    res.append(rec); print(rec, flush=True)
    if time.time() - t0 > 45: print("time guard hit"); break
json.dump({"script": "analysis/b27_03_kernel2.py", "p": k.P, "lcg_seed": 7777, "entries": "-5..5",
           "results": res, "wall_s": round(time.time() - t0, 2)}, open(sys.argv[1], "w"), indent=1)

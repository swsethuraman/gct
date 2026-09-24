"""B27-03 run 7: rank certificates on ray 2, w_k=(4k-9,3,2,2,2), k=4..7, 65-coordinate ring.
Library analysis/b27_03_kernel_lib.py; seed 7777 LCG, entries -5..5, N+16 points."""
import json, sys, time, importlib.util
spec = importlib.util.spec_from_file_location("k", "analysis/b27_03_kernel_lib.py")
k = importlib.util.module_from_spec(spec); spec.loader.exec_module(k)
t0 = time.time()
k.state = 7777
def lcg11():
    k.state = (1103515245 * k.state + 12345) % 2**31
    return ((k.state >> 16) % 11) - 5
k.lcg = lcg11
res = []
for kk in range(4, 8):
    t1 = time.time()
    rec = k.certify(f"ray2 k={kk}, 65-ring", kk, (4 * kk - 9, 3, 2, 2, 2), 65, cap=1100)
    rec["wall_s"] = round(time.time() - t1, 2); res.append(rec); print(rec, flush=True)
    if time.time() - t0 > 50: print("time guard hit"); break
json.dump({"script": "analysis/b27_03_ray2.py", "p": k.P, "lcg_seed": 7777, "entries": "-5..5",
           "results": res, "wall_s": round(time.time() - t0, 2)}, open(sys.argv[1], "w"), indent=1)

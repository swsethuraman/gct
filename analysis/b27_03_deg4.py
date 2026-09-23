"""B27-03 run 6: whole-degree certificate I(D)_4 = 0 via the balanced weight (4,3,3,3,3) of the
70-coordinate ring (every GL5-isotypic S_nu, nu |- 16, contains this weight; HAND lemma in the
report).  Library evaluation (analysis/b27_03_kernel_lib.py, seed 7777 LCG, entries -5..5, N+16
points); rank by forward elimination mod p restricted to columns >= pivot, with a 55 s guard."""
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
P = k.P
class Guard(Exception): pass
def rank_forward(M):
    M = M % P
    nr, nc = M.shape; r = 0
    for c in range(nc):
        if time.time() - t0 > 55: raise Guard(f"guard at column {c}, rank so far {r}")
        piv = np.nonzero(M[r:, c])[0]
        if len(piv) == 0: continue
        pr = r + piv[0]
        if pr != r: M[[r, pr]] = M[[pr, r]]
        inv = pow(int(M[r, c]), P - 2, P)
        M[r, c:] = (M[r, c:] * inv) % P
        f = M[r + 1:, c].copy()
        nz = np.nonzero(f)[0]
        if len(nz):
            rows = r + 1 + nz
            M[rows, c:] = (M[rows, c:] - f[nz][:, None] * M[r, c:][None, :]) % P
        r += 1
        if r == nr: break
    return r
k.rank_mod_p = rank_forward
try:
    rec = k.certify("balanced k=4, whole ring", 4, (4, 3, 3, 3, 3), 70, cap=2000)
except Guard as g:
    rec = {"name": "balanced k=4, whole ring", "status": f"NOT COMPLETED: {g}"}
rec["wall_s"] = round(time.time() - t0, 2); print(rec)
json.dump({"script": "analysis/b27_03_deg4.py", "p": P, "lcg_seed": 7777, "entries": "-5..5",
           "results": [rec]}, open(sys.argv[1], "w"), indent=1)

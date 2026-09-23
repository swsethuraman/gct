"""B27-03 run 4: exact dimensions of coefficient-weight spaces (counting only, no evaluation).
dim H_{k,w} = [t^k x^w] prod_{alpha in E} 1/(1 - t x^alpha), by an exact integer DP over E.
Usage: python b27_03_dims.py OUT.json"""
import json, sys, time, itertools
import numpy as np
t0 = time.time()
E70 = sorted([a for a in itertools.product(range(5), repeat=5) if sum(a) == 4], reverse=True)
E65 = [a for a in E70 if max(a) >= 2]
def dim(k, w, E):
    A = np.zeros((k + 1,) + tuple(x + 1 for x in w), dtype=object); A[(0,) * 6] = 1
    for a in E:
        # multiply by 1/(1 - t x^a): A[j, v] += A[j-1, v-a] (in increasing j, i.e. unbounded use)
        for j in range(1, k + 1):
            src = (slice(j - 1, j),) + tuple(slice(0, w[i] + 1 - a[i]) for i in range(5))
            dst = (slice(j, j + 1),) + tuple(slice(a[i], w[i] + 1) for i in range(5))
            if all(w[i] >= a[i] for i in range(5)):
                A[dst] = A[dst] + A[src]
    return int(A[(k,) + tuple(w)])
jobs = [(4, (4, 3, 3, 3, 3)), (5, (4, 4, 4, 4, 4)),
        (8, (24, 2, 2, 2, 2)), (8, (23, 3, 2, 2, 2)), (8, (22, 4, 2, 2, 2)), (8, (22, 3, 3, 2, 2)),
        (8, (20, 3, 3, 3, 3)), (8, (16, 4, 4, 4, 4)), (8, (12, 5, 5, 5, 5)), (8, (8, 6, 6, 6, 6)),
        (8, (7, 7, 6, 6, 6)), (9, (28, 2, 2, 2, 2)), (10, (32, 2, 2, 2, 2))]
res = []
for k, w in jobs:
    r = {"k": k, "w": list(w), "dim65": dim(k, w, E65), "dim70": dim(k, w, E70)}
    res.append(r); print(r, flush=True)
json.dump({"script": "analysis/b27_03_dims.py", "results": res, "wall_s": round(time.time() - t0, 2)},
          open(sys.argv[1], "w"), indent=1)

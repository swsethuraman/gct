"""B25-04 pilot 2: non-vacuous component-product control; see results/b25_04/PREREG_b25_04_p2.md."""
import hashlib
import json
import random
from pathlib import Path

PREREG = Path("results/b25_04/PREREG_b25_04_p2.md")
PREREG_SHA = "d67ff53405d7e438e5c1cb42c0989e2e5488d0ece271e1701acb07407a8cf5a4"
got = hashlib.sha256(PREREG.read_bytes()).hexdigest()
print("prereg", PREREG, got, flush=True)
assert got == PREREG_SHA, "preregistration hash mismatch"
P1_OUT_SHA = "cc6031c8ed9fe6a354e53676fc03e21426feae661fbbfa70e5581e2f1ed40ce5"
assert hashlib.sha256(Path("results/b25_04/p1_factor.json").read_bytes()).hexdigest() == P1_OUT_SHA

src = Path("analysis/b25_04_p1_factor.py").read_text()
prefix = src[:src.index("# T_g: shape (8,2)")]
ns = {"__name__": "b25_04_p1_prefix"}
exec(compile(prefix, "b25_04_p1_factor.py[prefix]", "exec"), ns)
f, shape, singletons, N_FORM = ns["f"], ns["shape"], ns["singletons"], ns["N_FORM"]
rng = random.Random(2509210402)


def point(R=3):
    return [[rng.randint(-3, 3) for _ in range(3)] for _ in range(R)], [1] * R


def components(cols):
    parent = {a: a for c in cols for a in c}
    def find(a):
        while parent[a] != a:
            a = parent[a]
        return a
    for c in cols:
        for a in c[1:]:
            parent[find(a)] = find(c[0])
    comps = {}
    for a in parent:
        comps.setdefault(find(a), set()).add(a)
    return sorted(sorted(s) for s in comps.values())


T_g = [(1, 2), (1, 2)] + singletons({1: 3, 2: 3})
T_h = [(1, 2)] * 4 + singletons({1: 1, 2: 1})
assert shape(T_g) == [8, 2] and shape(T_h) == [6, 4]
T = [(1, 2), (1, 2)] + [(3, 4)] * 4 + singletons({1: 3, 2: 3, 3: 1, 4: 1})
assert shape(T) == [14, 6] and components(T) == [[1, 2], [3, 4]]
T5 = T + singletons({5: 5})
assert shape(T5) == [19, 6] and components(T5) == [[1, 2], [3, 4], [5]]

out = {"prereg_sha256": got, "p1_output_sha256": P1_OUT_SHA, "seed": 2509210402,
       "components_T": components(T), "components_T5": components(T5)}
rows = []
for _ in range(5):
    e, c = point()
    g, h = f(T_g, e, c), f(T_h, e, c)
    c5 = sum(ci * ei[0] ** N_FORM for ci, ei in zip(c, e))
    lhs, lhs5 = f(T, e, c), f(T5, e, c)
    rows.append({"ells": e, "g": g, "h": h, "c_5e1": c5, "f_T": lhs, "f_T5": lhs5,
                 "K2p": lhs == g * h, "K2pp": lhs5 == g * h * c5})
    assert lhs == g * h, "K2' product failed"
    assert lhs5 == g * h * c5, "K2'' product failed"
out["rows"] = rows
nv2 = sum(1 for r in rows if r["g"] != 0 and r["h"] != 0)
nv3 = sum(1 for r in rows if r["g"] != 0 and r["h"] != 0 and r["c_5e1"] != 0)
out["nonvacuous_K2p"], out["nonvacuous_K2pp"] = nv2, nv3
assert nv2 >= 3, "K2' vacuous"
assert nv3 >= 3, "K2'' vacuous"
out["verdict"] = "ALL CHECKS PASSED (non-vacuous)"
Path("results/b25_04/p2_nonvacuous.json").write_text(json.dumps(out, indent=1) + "\n")
print(json.dumps({"verdict": out["verdict"], "nonvacuous": [nv2, nv3],
                  "g_h": [(r["g"], r["h"]) for r in rows]}), flush=True)

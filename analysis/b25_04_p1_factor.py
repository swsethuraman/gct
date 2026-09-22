"""B25-04 pilot 1: control on the reading of BDI eq. (5.2); see results/b25_04/PREREG_b25_04_p1.md.

Project variables: form degree N_FORM = n = 5, variable count R_VARS = r = 3, equation degree d.
A tableau is a list of columns (tuples of entries, top to bottom); entries are 1..d, each n times.
"""
import hashlib
import itertools
import json
import random
from pathlib import Path

PREREG = Path("results/b25_04/PREREG_b25_04_p1.md")
PREREG_SHA = "101c086e9916f5280d78db5397c6ddbc889a13ebf0a1a11316e58688fbfb6516"
got = hashlib.sha256(PREREG.read_bytes()).hexdigest()
print("prereg", PREREG, got, flush=True)
assert got == PREREG_SHA, "preregistration hash mismatch"

N_FORM, R_VARS = 5, 3
rng = random.Random(2509210401)


def det(M):
    if len(M) == 1:
        return M[0][0]
    return sum((-1) ** j * M[0][j] * det([row[:j] + row[j + 1:] for row in M[1:]])
               for j in range(len(M)))


def check_content(cols):
    entries = sorted({a for c in cols for a in c})
    d = len(entries)
    assert entries == list(range(1, d + 1))
    for a in entries:
        assert sum(c.count(a) for c in cols) == N_FORM, (a, cols)
    return d


def shape(cols):
    lengths = sorted((len(c) for c in cols), reverse=True)
    return [sum(1 for L in lengths if L >= i) for i in range(1, lengths[0] + 1)]


def f(cols, ells, cs):
    """BDI (5.2) with weights: p = sum_i cs[i] * ells[i]^n."""
    d = check_content(cols)
    total = 0
    for phi in itertools.product(range(len(ells)), repeat=d):
        w = 1
        for a in range(d):
            w *= cs[phi[a]]
        for c in cols:
            M = [[ells[phi[a - 1]][row] for a in c] for row in range(len(c))]
            w *= det(M)
            if w == 0:
                break
        total += w
    return total


def singletons(counts):
    return [(a,) for a, k in counts.items() for _ in range(k)]


def point(R):
    return [[rng.randint(-3, 3) for _ in range(R_VARS)] for _ in range(R)], [1] * R


# T_g: shape (8,2), content 2 x 5, row1 = 1 1 1 1 1 2 2 2, row2 = 2 2.
T_g = [(1, 2), (1, 2)] + singletons({1: 3, 2: 3})
assert shape(T_g) == [8, 2]
# K2 tableau and its components.
T_123 = [(1, 2, 3), (1, 2)] + singletons({1: 3, 2: 3, 3: 4})
T_45 = [(1, 2), (1, 2)] + singletons({1: 3, 2: 3})          # entries 4,5 relabelled 1,2
T_K2 = [(1, 2, 3), (1, 2), (4, 5), (4, 5)] + singletons({1: 3, 2: 3, 3: 4, 4: 3, 5: 3})
assert shape(T_K2) == [20, 4, 1]
T_iso = T_g + singletons({3: 5})
assert shape(T_iso) == [13, 2]
T_bad = [(1, 1), (1, 2)] + singletons({1: 2, 2: 4})          # repeated entry in a column

out = {"prereg_sha256": got, "n": N_FORM, "r": R_VARS, "seed": 2509210401}

# K1
K1 = []
for _ in range(3):
    e, c = point(3)
    K1.append({"ells": e, "g": f(T_g, e, c)})
out["K1_g_values"] = K1
assert any(x["g"] != 0 for x in K1), "K1 failed: g vanished at every sampled point"

# K2
K2 = []
for _ in range(5):
    e, c = point(3)
    lhs, a, b = f(T_K2, e, c), f(T_123, e, c), f(T_45, e, c)
    K2.append({"lhs": lhs, "f123": a, "f45": b, "ok": lhs == a * b})
    assert lhs == a * b, "K2 component product failed"
ISO = []
for _ in range(5):
    e, c = point(3)
    lhs, gv = f(T_iso, e, c), f(T_g, e, c)
    c5 = sum(ci * ei[0] ** N_FORM for ci, ei in zip(c, e))
    ISO.append({"lhs": lhs, "g": gv, "c_5e1": c5, "ok": lhs == gv * c5})
    assert lhs == gv * c5, "K2 isolated-vertex factor failed"
out["K2_components"], out["K2_isolated"] = K2, ISO

# K3
e, c = point(3)
g0 = f(T_g, e, c)
K3 = {"g": g0, "unipotent": [], "torus": None}
for _ in range(3):
    L = [[1, 0, 0], [rng.randint(-3, 3), 1, 0], [rng.randint(-3, 3), rng.randint(-3, 3), 1]]
    e2 = [[sum(L[i][k] * v[k] for k in range(3)) for i in range(3)] for v in e]
    g1 = f(T_g, e2, c)
    K3["unipotent"].append({"L": L, "g": g1, "ok": g1 == g0})
    assert g1 == g0, "K3 unipotent invariance failed"
al = [rng.choice([2, 3, -2]) for _ in range(3)]
e3 = [[al[i] * v[i] for i in range(3)] for v in e]
g3 = f(T_g, e3, c)
K3["torus"] = {"alpha": al, "g": g3, "expected": al[0] ** 8 * al[1] ** 2 * g0,
               "ok": g3 == al[0] ** 8 * al[1] ** 2 * g0}
assert K3["torus"]["ok"], "K3 torus weight failed"
out["K3"] = K3

# Controls
C1 = []
for _ in range(3):
    e, c = point(3)
    C1.append(f(T_bad, e, c))
assert all(v == 0 for v in C1), "C1 Lemma 5.5 control failed"
C2 = f(T_g, [[1, 0, 0]], [1])
assert C2 == 0, "C2 pure-power control failed"
e, _ = point(3)
C3 = {}
for name, T in (("g", T_g), ("K2", T_K2)):
    v_w = f(T, e, [2, 1, 1])
    v_r = f(T, [e[0]] + e, [1, 1, 1, 1])
    C3[name] = {"weighted": v_w, "repeated": v_r, "ok": v_w == v_r}
    assert v_w == v_r, "C3 well-definedness failed"
out["C1_bad_values"], out["C2_pure_power"], out["C3"] = C1, C2, C3
out["verdict"] = "ALL CHECKS PASSED"

dest = Path("results/b25_04/p1_factor.json")
dest.write_text(json.dumps(out, indent=1) + "\n")
print(json.dumps({"verdict": out["verdict"], "K1": [x["g"] for x in K1]}), flush=True)

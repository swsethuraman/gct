"""Session 56 — the weight-space route on H_{4,delta} through the C pass
(analysis/wk9_s56_pass.c): for every dominant weight mu of 4*delta with at most
delta parts, the Gram matrices b^mu (sign-free, = Theta^+) and k^mu (signed, the
Specht check), their exact ranks, and then by inverse Kostka the isotypic ranks
m_lambda = rank Hom_{S_N}([lambda], Theta^+_delta) and a_lambda for every lambda.

    python3 analysis/wk9_s56_weights.py <delta> [--specht K] [--only mu1,mu2 ...]

Writes results/s56_weights_d<delta>.json and the raw C outputs under
results/logs/s56_w<delta>_<mu>.txt.  Every C run is bounded (timeout, ulimit -v)
and its pid recorded in results/logs/.
"""
import json
import os
import subprocess
import sys
import time
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "tools", "verify"))
import wk9_s56_core as C            # noqa: E402
from pleth import ambient_multiplicity   # noqa: E402

delta = int(sys.argv[1])
N = 4 * delta
specht_extra = 0
only = None
args = sys.argv[2:]
while args:
    if args[0] == "--specht":
        specht_extra = int(args[1]); args = args[2:]
    elif args[0] == "--only":
        only = [tuple(int(x) for x in a.split(",")) for a in args[1:]]; args = []
    else:
        args = args[1:]
EXE = os.path.join(HERE, "wk9_s56_pass")
LOGS = os.path.join(ROOT, "results", "logs")
t0 = time.time()
log = []


def say(*a):
    s = " ".join(str(x) for x in a)
    print(f"[{time.time()-t0:8.1f}s] {s}", flush=True)
    log.append(s)


def run_pass(mu, timeout_s=14400, mem_kb=6000000):
    tag = f"s56_w{delta}_" + "_".join(str(x) for x in mu)
    out = os.path.join(LOGS, tag + ".txt")
    err = os.path.join(LOGS, tag + ".err")
    cmd = f"ulimit -v {mem_kb}; exec timeout {timeout_s} {EXE} {delta} {','.join(str(x) for x in mu)} {out} weight"
    with open(err, "w") as fe:
        proc = subprocess.Popen(["bash", "-c", cmd], stderr=fe, stdout=subprocess.DEVNULL)
        with open(os.path.join(LOGS, tag + ".pid"), "w") as fp:
            fp.write(str(proc.pid) + "\n")
        rc = proc.wait()
    if rc != 0:
        raise RuntimeError(f"pass failed for {mu}: rc={rc}, see {err}")
    return parse_pass(out)


def parse_pass(path):
    with open(path) as fh:
        lines = fh.read().split("\n")
    hdr = lines[1].split()
    Hn, nb = int(hdr[1]), int(hdr[3])
    times = lines[2].split()
    t1, t2 = float(times[1]), float(times[3])
    assert lines[3] == "orbits"
    orbits = []
    for i in range(nb):
        parts = lines[4 + i].split()
        orbits.append((int(parts[0]), [int(x) for x in parts[1:]]))
    assert lines[4 + nb] == "b"
    b = [[int(x) for x in lines[5 + nb + i].split()] for i in range(nb)]
    assert lines[5 + 2 * nb] == "k"
    k = [[int(x) for x in lines[6 + 2 * nb + i].split()] for i in range(nb)]
    return {"H": Hn, "nb": nb, "orbits": orbits, "b": b, "k": k, "pass1": t1, "pass2": t2}


def decode_content(code, ncol):
    v = []
    for _ in range(ncol):
        v.append(code % 5)
        code //= 5
    return tuple(reversed(v))


weights = list(C.partitions(N, maxlen=delta))
weights.sort(key=lambda mu: tuple(-x for x in mu))
extra = []
if specht_extra:
    cand = [mu for mu in C.partitions(N) if 4 <= len(mu) <= 8 and mu not in weights]
    step = max(1, len(cand) // specht_extra)
    extra = cand[::step][:specht_extra]
todo = weights + extra
if only:
    todo = only
Hsize = None
results = {}
for mu in todo:
    res = run_pass(mu)
    nb = res["nb"]
    Hsize = res["H"] if Hsize is None else Hsize
    assert res["H"] == Hsize
    sizes = [o[0] for o in res["orbits"]]
    assert sum(sizes) == Hsize, (mu, sum(sizes), Hsize)
    b, k = res["b"], res["k"]
    # symmetry b(O,O')|O'| = b(O',O)|O|
    for i in range(nb):
        for j in range(nb):
            assert b[i][j] * sizes[j] == b[j][i] * sizes[i], (mu, i, j)
    rb = C.rank_both_primes(b)
    assert rb[0] == rb[1], (mu, rb)
    rb_Q = C.rank_Q(b) if nb <= 700 else None
    if rb_Q is not None:
        assert rb_Q == rb[0], (mu, rb_Q, rb)
    ncol = len(mu)
    contents = [[decode_content(c, ncol) for c in o[1]] for o in res["orbits"]]
    multi = [i for i, cv in enumerate(contents) if all(max(v) <= 1 for v in cv)]
    km = [[k[i][j] for j in multi] for i in multi]
    for ii, i in enumerate(multi):          # signed symmetry holds on multilinear orbits
        for jj, j in enumerate(multi):
            assert k[i][j] * sizes[j] == k[j][i] * sizes[i], (mu, i, j)
    rk = C.rank_both_primes(km) if multi else (0, 0)
    kost = C.kostka((delta,) * 4, mu)
    assert rk[0] == rk[1] == kost, (mu, rk, kost)
    results[str(mu)] = {"mu": list(mu), "nb": nb, "r": rb[0], "r_Q": rb_Q, "nb_minus_r": nb - rb[0],
                        "multilinear_orbits": len(multi), "rank_k_multilinear": rk[0],
                        "kostka_rect": kost, "pass1_s": res["pass1"], "pass2_s": res["pass2"],
                        "specht_check_only": mu in extra}
    say(f"weight {mu}: nb={nb} r={rb[0]}{'' if rb_Q is None else ' (Q ok)'} nb-r={nb-rb[0]} | "
        f"multilinear {len(multi)} rank k={rk[0]} = Kostka {kost} | {res['pass2']:.1f}s")

out = {"delta": delta, "N": N, "H": Hsize, "weights": results, "log": log}
if not only:
    Kmat, Kinv = C.inverse_kostka_matrix(weights)
    cells = {}
    for i, lam in enumerate(weights):
        m = sum(Kinv[j][i] * results[str(weights[j])]["r"] for j in range(len(weights)))
        a = sum(Kinv[j][i] * results[str(weights[j])]["nb"] for j in range(len(weights)))
        assert m.denominator == 1 and a.denominator == 1
        m, a = int(m), int(a)
        a_house = ambient_multiplicity(lam, delta)
        assert a == a_house, (lam, a, a_house)
        cells[str(lam)] = {"lambda": list(lam), "a": a, "m": m, "i_det": a - m,
                           "sk": C.sk_coefficient(lam, delta) if a else None,
                           "f": C.hook_length_f(lam)}
        if a:
            say(f"cell {lam}: a={a} m={m} sk={cells[str(lam)]['sk']}")
        else:
            assert m == 0, (lam, m)
    out["cells"] = cells
    out["sum_a_f"] = sum(c["a"] * c["f"] for c in cells.values())
    out["sum_m_f"] = sum(c["m"] * c["f"] for c in cells.values())
    say(f"sum a f = {out['sum_a_f']}, sum m f = {out['sum_m_f']}, |H| = {Hsize}")
    fname = f"s56_weights_d{delta}.json"
else:
    fname = f"s56_weights_d{delta}_only.json"
out["seconds"] = time.time() - t0
with open(os.path.join(ROOT, "results", fname), "w") as fh:
    json.dump(out, fh, indent=1, default=str)
say("written", fname)

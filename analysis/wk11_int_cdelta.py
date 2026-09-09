"""C_delta -- the recoupling dimension of the S5 one-block recursion.

S5's recursion presents the invariant source at delta as

    W_delta = (S^{lambda_delta})^{K_delta},   K_delta = H_{delta-1} x S_4,
    M_delta = W_delta ^ Fix(tau),

with dim W_delta = B_delta (analysis/wk11_int_bdelta.py).  The block swap tau
does NOT preserve W_delta: tau v is invariant under tau K_delta tau^{-1}, not
under K_delta.  So the equation "tau v = v" cannot be written inside W_delta.
Both v and tau v lie in the invariants of

    K' = K_delta ^ tau K_delta tau^{-1} = H_{delta-2} x S_4 x S_4,

and that is where the residual tau v - v lives.  Its dimension is

    C_delta = dim (S^{lambda_delta})^{K'}
            = sum over two-step horizontal-4-strip paths lambda -> mu -> nu
              of a_{delta-2}(nu)
            = sum_{mu one-strip predecessor of lambda} B_{delta-1}(mu).

C_delta, not B_delta, is the size of the linear algebra the block swap does.
This script computes it exactly by the same pruned-Weyl / tail-census route
that wk11_int_b24.py used for B_24, with a per-key checkpoint so a long run
survives being interrupted.

Usage:  python3 wk11_int_cdelta.py <delta> [seconds] [state.pkl]

Banked: C_12 = 239  (B_12 = 31, a_12 = 2), 36 paths over 23 shapes, 21 nonzero.
"""
import json
import os
import pickle
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..'))
sys.path.insert(0, HERE)
from wk9_s42_census import N_S_tail_n, perm_sign
from wk11_int_bdelta import lam_of, horiz_strips


def weyl_terms(lam):
    """Pruned Weyl alternation: {mu: signed multiplicity} for the shape lam."""
    r = len(lam)
    rho = tuple(range(r - 1, -1, -1))
    lr = [lam[i] + rho[i] for i in range(r)]
    order = sorted(range(r), key=lambda i: lr[i])
    used = [False] * r
    w = [0] * r
    acc = {}

    def rec(k):
        if k == r:
            mu = tuple(lr[i] - rho[w[i]] for i in range(r))
            acc[mu] = acc.get(mu, 0) + perm_sign(w)
            return
        i = order[k]
        for j in range(r):
            if not used[j] and rho[j] <= lr[i]:
                used[j] = True
                w[i] = j
                rec(k + 1)
                used[j] = False

    rec(0)
    return {m: s for m, s in acc.items() if s}


def two_strip_paths(delta, n=4):
    """[(mu, nu)] with lambda_delta/mu and mu/nu both horizontal n-strips."""
    lam = lam_of(delta)
    return [(mu, nu) for mu in horiz_strips(lam, n) for nu in horiz_strips(mu, n)]


def c_delta(delta, n=4, budget=None, state_path=None):
    """Exact C_delta.  Returns (C, {nu: a_{delta-2}(nu)}) or None if unfinished."""
    paths = two_strip_paths(delta, n)
    shapes = sorted({nu for _, nu in paths})
    state = {}
    if state_path and os.path.exists(state_path):
        state = pickle.load(open(state_path, "rb"))
    t0 = time.time()
    for nu in shapes:
        k = str(nu)
        if k in state and state[k]["done"] == len(state[k]["keys"]):
            continue
        if budget is not None and time.time() - t0 > budget:
            break
        if k not in state:
            terms = weyl_terms(nu)
            state[k] = {"keys": sorted(terms), "sgn": terms, "done": 0, "tot": 0}
        s = state[k]
        while s["done"] < len(s["keys"]):
            if budget is not None and time.time() - t0 > budget:
                break
            mu = s["keys"][s["done"]]
            s["tot"] += s["sgn"][mu] * N_S_tail_n(mu, delta - 2, n)
            s["done"] += 1
        if state_path:
            pickle.dump(state, open(state_path, "wb"))
    if any(str(nu) not in state or state[str(nu)]["done"] != len(state[str(nu)]["keys"])
           for nu in shapes):
        return None
    a = {str(nu): state[str(nu)]["tot"] for nu in shapes}
    return sum(a[str(nu)] for _, nu in paths), a


if __name__ == "__main__":
    import json

    delta = int(sys.argv[1]) if len(sys.argv) > 1 else 12
    budget = float(sys.argv[2]) if len(sys.argv) > 2 else None
    st = sys.argv[3] if len(sys.argv) > 3 else f"c{delta}_state.pkl"
    paths = two_strip_paths(delta)
    shapes = sorted({nu for _, nu in paths})
    print(f"delta = {delta}: {len(paths)} two-strip paths over {len(shapes)} shapes",
          flush=True)
    out = c_delta(delta, budget=budget, state_path=st)
    if out is None:
        done = sum(1 for nu in shapes
                   if str(nu) in pickle.load(open(st, "rb"))
                   and pickle.load(open(st, "rb"))[str(nu)]["done"]
                   == len(pickle.load(open(st, "rb"))[str(nu)]["keys"]))
        print(f"  incomplete: {done}/{len(shapes)} shapes -- rerun to continue")
        sys.exit(0)
    C, a = out
    print(f"  C_{delta} = {C}")
    json.dump({"delta": delta, "C": C, "paths": len(paths),
               "shapes": len(shapes), "a_by_shape": a},
              open(os.path.join(ROOT, "results", f"wk11_int_c{delta}_result.json"),
                   "w"), indent=1)

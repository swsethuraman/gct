#!/usr/bin/env python3
"""Session 74 -- Python binding of the compact-state DP evaluator (wk12_s74_dpc.c),
a drop-in for wk11_s69_circuit.dp_eval_c: same packing (dp_pack), same signs,
same value.  `validate()` checks it against the s69 evaluator on random
(filling, point) pairs across the ladder's rungs at both primes.
"""
import ctypes
import os
import random
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from wk11_s69_circuit import dp_pack, dp_eval_c, random_filling, sym_table, symbols_from_coeffs, generic_point   # noqa: E402
from wk8_s30_core import P1, P2                                                                           # noqa: E402

_LIB = None


def _lib():
    global _LIB
    if _LIB is None:
        so = os.path.join(HERE, "wk12_s74_dpc.so")
        src = os.path.join(HERE, "wk12_s74_dpc.c")
        if not os.path.exists(so) or os.path.getmtime(so) < os.path.getmtime(src):
            rc = os.system(f"gcc -O3 -march=native -shared -fPIC -o {so} {src}")
            assert rc == 0, "compile failed"
        _LIB = ctypes.CDLL(so)
        _LIB.dp_eval_compact.restype = ctypes.c_longlong
    return _LIB


def dp_eval_compact(F, msym, p, tab=None, order=None, max_W=8):
    P = dp_pack(F, msym, p, tab, order)
    if P["W"] > max_W:
        raise RuntimeError(f"pathwidth W={P['W']} exceeds max_W={max_W}")
    lib = _lib()
    I32 = ctypes.POINTER(ctypes.c_int32)
    I64 = ctypes.POINTER(ctypes.c_int64)
    val = lib.dp_eval_compact(
        ctypes.c_int(P["h"]), ctypes.c_int(P["d"]), ctypes.c_int(P["n2"]), ctypes.c_int(P["W"]), ctypes.c_longlong(p),
        P["l_inC1"].ctypes.data_as(I32), P["l_inC2"].ctypes.data_as(I32), P["l_d2"].ctypes.data_as(I32),
        P["l_edge"].ctypes.data_as(I32), P["l_side"].ctypes.data_as(I32), ctypes.c_int(P["l_edge"].shape[1]),
        P["l_off"].ctypes.data_as(I64), P["tens"].ctypes.data_as(I64),
        P["slot"].ctypes.data_as(I32), P["first"].ctypes.data_as(I32), P["firstside"].ctypes.data_as(I32))
    assert val >= 0, "dp_eval_compact failed (allocation)"
    return P["sign"] * int(val) % p


def validate(n_pairs=40, seed=74):
    """exact agreement with dp_eval_c on random fillings of the LMR ladder shapes."""
    N, H, N2 = 4, 9, 15
    _A, _idx, _fact, TAB = sym_table(N, H)
    rng = random.Random(seed)
    ok = 0
    t_old = t_new = 0.0
    for t in range(n_pairs):
        d = rng.choice(list(range(12, 25)))
        n1 = N * d - 2 * H - 2 * N2
        F = random_filling(H, N, d, N2, n1, rng, k=rng.choice([5, 6, 7, 8, 9]))
        p = P1 if t % 2 == 0 else P2
        cv = generic_point(N, H, p, rng)
        if rng.random() < 0.3:
            cv[-1] = 0                                   # u = 0 points too
        ms = symbols_from_coeffs(cv, N, H, p)
        t0 = time.time()
        a = dp_eval_c(F, ms, p, TAB)
        t1 = time.time()
        b = dp_eval_compact(F, ms, p, TAB)
        t2 = time.time()
        t_old += t1 - t0
        t_new += t2 - t1
        ok += (a == b)
        if a != b:
            print(f"MISMATCH d={d} p={p}: s69 {a} vs compact {b}")
    print(f"compact DP vs s69 DP: {ok}/{n_pairs} agree; mean {t_old/n_pairs:.3f}s vs {t_new/n_pairs:.3f}s per evaluation")
    return ok == n_pairs


if __name__ == "__main__":
    sys.exit(0 if validate(int(sys.argv[1]) if len(sys.argv) > 1 else 40) else 1)

#!/usr/bin/env python3
"""Session 40 -- the Milnor-algebra row dim M(F)_t, t = 2..7, of a determinantal
cubic threefold against the smooth row, at two fresh pencils, both primes.
Prediction (Dimca Thm 3.1 + the s37 bookkeeping, docs/onset_conjecture.md
section 3): dim M(F)_t = mu_t + def_{5-t}(N) for t <= 5, i.e. 10, 10, 6, 6
(def_3 = def_2 = 0, def_1 = 1, def_0 = 5), and mu_t + tau = 0 + 6 for t >= 6
(Dimca's tau-stabilisation of H^4(K^*)_j for j >= n(d-1) = 8, i.e. t >= 6)."""
import sys, random, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wk9_s40_poly import *
from wk9_s40_cap import mu
SEED = 20260903
for trial in range(2):
    rnd = random.Random(SEED + trial)
    A = rand_pencil(3, rnd, 10 ** 6); ent = pencil_entries(A, 3); F = det_form(ent, 3)
    G = randform(3, rnd, 99)
    row_det = [[macaulay_corank(F, 3, t, p) for p in (P1, P2)] for t in range(2, 8)]
    row_gen = [[macaulay_corank(G, 3, t, p) for p in (P1, P2)] for t in range(2, 8)]
    assert all(a == b for a, b in row_det) and all(a == b for a, b in row_gen)
    print(f"pencil {trial}: dim M(det)_t, t=2..7 = {[a for a, b in row_det]}   smooth = {[a for a, b in row_gen]}   mu_t = {[mu(t, 3) for t in range(2, 8)]}")

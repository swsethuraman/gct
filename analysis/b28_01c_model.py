#!/usr/bin/env python3
"""
B28-01c -- the gate's time and memory model, shared by the driver's
build-and-cover gate and the repricer (so the gate evaluates exactly the
priced formulas).  Pure integer/float arithmetic; no I/O.

Time (B27-06 PREREGISTRATION.md phase model), seconds:
  B = cB n k   S = cS z   H = cH z U   V = cV (a+8) n k   R = cR (a+8) n a   D = cD U^3
  producer remaining after the gate = npr (H + V + R + D)
  verifier (one independent rebuild/replay) = max( direct verifier model  sum_X cX_v X,
                                                   rho_up * producer model sum_X cX_p X )
  with rho_up = max_X cX_v / cX_p rounded UP to 4 decimals (R28-01 P3).  Since
  sum_X cX_v X <= rho_up sum_X cX_p X term by term, the ratio bound dominates.

Memory, bytes (R28-01 P4): the gate needs max(producer envelope, verifier estimate)
  <= 75% of the job cap.  The producer envelope is the preregistered one.  The
verifier estimate is its live set, phase by phase, each term an upper bound on
the arrays b28_01c_verify.py holds at that moment:
  base      5e8 (interpreter, numpy/scipy/flint) + carrier N_S (4 d + 24) + E (12 z + 8 rows)
  build     64 N_S d + 12 z                        (raising-operator targets, unique, blocks, vstack)
  schur     max of three stages:
    A (projection)  76 z_R1 + 12 z_Fo + 64 nproj ro + 48 nnzPF
                    (R1, T, TU, coo, triu and its int64 copies; F_o; the splitmix
                     projection's coo lists and CSR; P F_o, its CSC copy, the S/U
                     column slices and |PF_S|;  nnzPF <= min(m n, nproj z_Fo))
    B (dense)       76 z_R1 + 12 z_Fo + 12 nproj ro + 12 nnzPF + 8 m U + 5e8 + 32 m w
                    (as A after the construction temporaries are freed; G; the
                     250 MB solve block and its int64 copy; PF_S Y and dense PF_U)
    C (rank G)      72 m U                          (G, G mod p, Python list, nmod_mat)
  lift      4 n a + 640 rows + 384 n                (K; 16-column limb chunks of E K)
  eval      20 n a + 64 n + N_S (4 d + 32)          (K and candidates; V batch of 8; carrier slices)
  estimate  = base + max(build, schur, lift, eval)
with m = U + 64, nproj = 8, w = max(1, floor(2.5e8 / (8 nS))) solve-block columns,
ro = rows of E outside the cover, z_R1 / z_Fo = nonzeros of E in / outside the cover rows.
"""
import math

NPROJ = 8
EXTRA = 64
BUDGET = 250_000_000


def phase_model(n, k, a, z, U, r):
    K = a + 8
    return dict(B=r['cB'] * n * k, S=r['cS'] * z, H=r['cH'] * z * U, V=r['cV'] * K * n * k,
                R=r['cR'] * K * n * a, D=r['cD'] * U ** 3)


def ratio_up(producer, verifier):
    """max over the six coefficients of verifier/producer, rounded up to 4 decimals."""
    q = max(verifier[c] / producer[c] for c in ('cB', 'cS', 'cH', 'cV', 'cR', 'cD'))
    return math.ceil(q * 10000) / 10000


def remaining_secs(n, k, a, z, U, npr, rates):
    """(producer seconds after the gate, verifier seconds, detail) for the gate."""
    pm = phase_model(n, k, a, z, U, rates['producer'])
    vm = phase_model(n, k, a, z, U, rates['verifier'])
    per_pass = pm['H'] + pm['V'] + pm['R'] + pm['D']
    v_direct = sum(vm.values())
    v_ratio = rates['verifier_ratio_up'] * sum(pm.values())
    return npr * per_pass, max(v_direct, v_ratio), dict(producer_phase_secs=pm, verifier_phase_secs=vm,
                                                        verifier_direct_secs=v_direct, verifier_ratio_secs=v_ratio)


def mem_envelope(n, a, z, U):
    """the preregistered producer envelope."""
    return 16 * n * a + 100 * z + 400 * n + 5 * max(250_000_000, 128 * n) + 80 * U * U + 500_000_000


def verifier_mem(n, N_S, d, a, z, rows, U, nS, ro, z_R1, z_Fo):
    m = U + EXTRA
    w = max(1, BUDGET // (8 * max(nS, 1)))
    nnzPF = min(m * n, NPROJ * z_Fo)
    base = 500_000_000 + N_S * (4 * d + 24) + 12 * z + 8 * rows
    build = 64 * N_S * d + 12 * z
    stA = 76 * z_R1 + 12 * z_Fo + 64 * NPROJ * ro + 48 * nnzPF
    stB = 76 * z_R1 + 12 * z_Fo + 12 * NPROJ * ro + 12 * nnzPF + 8 * m * U + 500_000_000 + 32 * m * w
    stC = 72 * m * U
    schur = max(stA, stB, stC)
    lift = 4 * n * a + 640 * rows + 384 * n
    ev = 20 * n * a + 64 * n + N_S * (4 * d + 32)
    est = base + max(build, schur, lift, ev)
    return int(est), dict(base=base, build=build, schur_A=stA, schur_B=stB, schur_C=stC, lift=lift, eval=ev, m=m, w=w, nnzPF_bound=nnzPF)

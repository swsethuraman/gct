"""Session 56 — setup checks for the shared routines (P6 and the arithmetic
cross-checks), run before the engine.  Independent implementations here
(analysis/wk9_s56_core.py) against the house ones (scripts/ambient_screen.py,
tools/verify/pleth.py)."""
import csv
import os
import sys
import time
from math import factorial

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "scripts"))
sys.path.insert(0, os.path.join(ROOT, "tools", "verify"))

import wk9_s56_core as C                     # noqa: E402
from ambient_screen import chi as house_chi, m_det as house_m_det   # noqa: E402
from pleth import ambient_multiplicity        # noqa: E402

t0 = time.time()
fails = 0


def check(label, got, want):
    global fails
    ok = got == want
    if not ok:
        fails += 1
    print(f"[{'ok' if ok else 'FAIL'}] {label}: got {got} want {want}")


# 1. characters: own Murnaghan–Nakayama vs house, all of S_8 and S_12
for N in (8, 12):
    bad = 0
    parts = list(C.partitions(N))
    for lam in parts:
        for rho in parts:
            if C.mn_char(lam, rho) != house_chi(lam, rho):
                bad += 1
    check(f"MN characters agree with house at N={N} ({len(parts)}^2 values)", bad, 0)
    # column orthogonality: sum_lam chi(rho)^2 = |centraliser| = N!/|class|
    rho = parts[len(parts) // 2]
    check(f"orthogonality at N={N}, rho={rho}",
          sum(C.mn_char(lam, rho) ** 2 for lam in parts), factorial(N) // C.class_size(rho))
    check(f"sum f^2 = N! at N={N}", sum(C.hook_length_f(lam) ** 2 for lam in parts), factorial(N))

# 2. Kostka: K_{nu nu} = 1, sum_nu K_{nu mu} f_nu = multinomial(mu)
for mu in [(4, 4), (6, 2), (4, 4, 4), (8, 2, 2), (4, 4, 4, 4), (7, 5, 3, 1), (4, 4, 4, 4, 4)]:
    N = sum(mu)
    check(f"K_{{mu,mu}}=1 at {mu}", C.kostka(mu, mu), 1)
    multinom = factorial(N)
    for m in mu:
        multinom //= factorial(m)
    s = sum(C.kostka(nu, mu) * C.hook_length_f(nu) for nu in C.partitions(N))
    check(f"sum_nu K f = multinomial at {mu}", s, multinom)
check("K_{(3,2,1),(2,2,1,1)} = 4", C.kostka((3, 2, 1), (2, 2, 1, 1)), 4)
check("K_{(4,2),(2,2,1,1)} = 4 (hand enumeration: rows 2 in {22,23,24,34})", C.kostka((4, 2), (2, 2, 1, 1)), 4)

# 3. P6: sk recomputed vs house m_det, all constituents at delta = 2, 3, 4
for delta in (2, 3, 4):
    N = 4 * delta
    bad = []
    cells = 0
    for lam in C.partitions(N, maxlen=delta):
        a = ambient_multiplicity(lam, delta)
        if not a:
            continue
        cells += 1
        mine = C.sk_coefficient(lam, delta)
        theirs = house_m_det(lam, 4, delta)
        if mine != theirs:
            bad.append((lam, mine, theirs))
    check(f"P6 sk == house m_det at delta={delta} ({cells} cells)", bad, [])

# 3b. P6 at delta = 5 against the 23 committed rows of the occurrence screen
rows = []
with open(os.path.join(ROOT, "results", "occurrence_screen.csv")) as fh:
    for r in csv.DictReader(fh):
        if r["delta"] == "5":
            rows.append(r)
bad = []
for r in rows:
    lam = tuple(int(x) for x in r["lam"].split("|"))
    mine = C.sk_coefficient(lam, 5)
    if mine != int(r["m_det"]):
        bad.append((lam, mine, r["m_det"]))
check(f"P6 sk == occurrence_screen m_det at delta=5 ({len(rows)} rows)", bad, [])
# and the ordinary Kronecker g >= sk at the same rows
check("g >= sk at all delta=5 rows",
      all(C.g_coefficient(tuple(int(x) for x in r["lam"].split("|")), 5)
          >= int(r["m_det"]) for r in rows), True)

# 4. set partitions and the standard kernel values
for delta in (2, 3):
    N = 4 * delta
    H = C.set_partitions(N)
    check(f"|H_{{4,{delta}}}|", len(H), factorial(N) // (24 ** delta * factorial(delta)))
    pi0 = C.standard_partition(delta)
    check(f"K(pi0,pi0) = 24^{delta}", C.kernel_K(pi0, pi0, N), 24 ** delta)

print(f"setup checks done in {time.time()-t0:.1f}s, failures = {fails}")
sys.exit(1 if fails else 0)

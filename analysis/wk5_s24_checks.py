#!/usr/bin/env python3
"""Session 24 -- validation of the World A tables (pre-registered H4,H5,H2)."""
import sys
sys.path.insert(0, '/root/gct/analysis')
from wk5_s24_worldA import *

tab = build()
D = DMAX

def show(title, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + title + ("  " + detail if detail else ""))
    return ok

allok = True

# ---- H5 : World A Theorem 2.1 reproduced by two independent routes
bad = []
for d in range(1, D + 1):
    for b in range(0, 2 * d + 1):
        a = 4 * d - b
        mm, mu, df = tab[('Jz', d, b)]
        pred = max(0, (a - 3 * b) // 8)
        if df != pred:
            bad.append((d, a, b, df, pred))
allok &= show("H5  def_{J=0} = max(0,floor((a-3b)/8)) for all delta<=%d" % D,
              not bad, "violations: %s" % bad[:4])

# ---- H5b : m_{J=0} from the ray route agrees with the character count N(a,b)
bad = []
for d in range(1, D + 1):
    for b in range(0, 2 * d + 1):
        ray, k = m_by_ray('Jz', d, b, 2, 4)      # boundary of {J=0} cut by I
        if ray != N_Jz(4 * d - b, b):
            bad.append((d, b, ray, N_Jz(4 * d - b, b)))
allok &= show("H5b m_{J=0}: ray route == mu_4^2|xS_2 character count", not bad,
              "violations: %s" % bad[:4])

# ---- H5c : m_{A_c} from the ray route agrees with the order-16 character count
bad = []
for d in range(1, D + 1):
    for b in range(0, 2 * d + 1):
        ray, k = m_by_ray('Ac', d, b, 2, 4)      # boundary of A_c cut by I
        if ray != m_Ac(4 * d - b, b):
            bad.append((d, b, ray, m_Ac(4 * d - b, b)))
allok &= show("H5c m_{A_c}: ray route == order-16 character count", not bad,
              "violations: %s" % bad[:4])

# ---- H4 : def_Q = 0 and def_tau = [b=1]
bad = [(d, b) for d in range(1, D + 1) for b in range(0, 2 * d + 1)
       if tab[('Q', d, b)][2] != 0]
allok &= show("H4a def_Q == 0 identically", not bad, "violations: %s" % bad[:4])
bad = [(d, b, tab[('tau', d, b)][2]) for d in range(1, D + 1)
       for b in range(0, 2 * d + 1) if tab[('tau', d, b)][2] != (1 if b == 1 else 0)]
allok &= show("H4b def_tau == [b=1]", not bad, "violations: %s" % bad[:4])

# ---- H2 : mult_D == mult_Ac everywhere; m_D = dim S_lambda; Def == P
bad = [(d, b) for d in range(1, D + 1) for b in range(0, 2 * d + 1)
       if tab[('D', d, b)][1] != tab[('Ac', d, b)][1]]
allok &= show("H2a mult_D == mult_{A_c} for all lambda", not bad,
              "violations: %s" % bad[:4])
bad = []
for d in range(1, D + 1):
    for b in range(0, 2 * d + 1):
        Pw = tab[('Ac', d, b)][0] - tab[('D', d, b)][0]
        Df = tab[('Ac', d, b)][2] - tab[('D', d, b)][2]
        if Pw != Df:
            bad.append((d, b, Pw, Df))
allok &= show("H2b Def == P exactly for the pair (D, A_c)  =>  D_obstr == 0",
              not bad, "violations: %s" % bad[:4])

print()
print("ALL VALIDATION CHECKS PASSED" if allok else "SOME CHECKS FAILED")

# ---- ROUTE-1 vs ROUTE-2 for the parametrised closures (added after the
#      containment check caught a wrong closed form for C[Q])
from wk5_s24_param import mult_param
bad = []
PMAX = 10
for name in ['Gam', 'tau', 'Q']:
    for d in range(1, PMAX + 1):
        mm = mult_param(name, d)
        for b in range(0, 2 * d + 1):
            if mm.get(b, 0) != MULT[name](d, b):
                bad.append((name, d, b, mm.get(b, 0), MULT[name](d, b)))
show("R12 substitution-rank == closed form for Gam, tau, Q (delta<=%d)" % PMAX,
     not bad, "violations: %s" % bad[:6])

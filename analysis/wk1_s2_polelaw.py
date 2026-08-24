"""Week 1, session 2 — systematic per-class pole law.
Classes e_{p,q,b} on the Fermat-quartic orbit, pole orders in I-units along the
transversal family; candidates: floor((p+q)/8)  vs  floor((p+q-2b)/8).
"""
import sympy as sp

x, y, tau = sp.symbols('x y tau')
R8 = sp.Rational(-1, 4)
C1 = sp.Pow(8, R8) / tau
C2 = sp.Pow(-1, sp.Rational(1, 4)) * sp.Pow(8, R8) / tau
l1 = x + tau**4 * y
l2 = x - tau**4 * y
w_norm = sp.expand(C1 * C2 * (-2 * tau**4))

def tau_order(expr):
    e = sp.expand(sp.radsimp(sp.powsimp(expr, force=True)))
    e = sp.expand(e * tau**400)
    P = sp.Poly(e, x, y, tau)
    degs = [m[2] for m in P.monoms()]
    return (min(degs) - 400) if degs else None

def pole_I(p, q, b):
    A = (C1*l1)**p * (C2*l2)**q
    B = (C1*l1)**q * (C2*l2)**p
    e = sp.expand(sp.powsimp((A + (-1)**b * B) * w_norm**b, force=True))
    if sp.simplify(e) == 0:
        return None
    o = tau_order(e)
    po = sp.Rational(-o, 8)
    assert po == int(po), (p, q, b, o)
    return int(po)

results = []
mismA = mismB = 0
for b in range(0, 7):
    for total in range(0, 25):
        if (total + 2*b) % 4 != 0:
            continue
        for p in range(total, (total-1)//2, -1):
            q = total - p
            if (p + b) % 4 or (q + b) % 4:
                continue
            if p == q and b % 2 == 1:
                continue
            po = pole_I(p, q, b)
            if po is None:
                continue
            candA = total // 8              # floor((a-b)/8)
            candB = max(0, (total - 2*b)) // 8   # floor((a-3b)/8), clipped
            candB_raw = (total - 2*b) // 8
            results.append((p, q, b, po, candA, candB_raw))
            if po != candA: mismA += 1
            if po != candB_raw: mismB += 1

print(f"classes computed: {len(results)}")
print(f"mismatches vs floor((p+q)/8):        {mismA}")
print(f"mismatches vs floor((p+q-2b)/8):     {mismB}")
print("\nrows where the two candidates differ (p, q, b, pole, candA, candB):")
shown = 0
for r in results:
    if r[4] != r[5]:
        print("  ", r); shown += 1
        if shown >= 15: break
if shown == 0:
    print("  (candidates never differ on this grid — enlarge b or reduce total)")
neg = [r for r in results if r[3] < 0]
print(f"\nclasses with NEGATIVE pole (i.e. vanishing on the boundary to positive order): {len(neg)}")
for r in neg[:10]:
    print("  ", r)

"""Backward-endgame feasibility tester (salvaged from stale branch f0c6ecd).

Complement of wk3_s12_wedgefeas (forward DFS) and wk3_s12_satfeas (SAT):
walks BACKWARD from the completed contraction state, un-applying the last
`depth` copies' options, and reports the per-level backward-reachable set
sizes. An empty set at any level proves the subproblem is structurally dead
regardless of the early game; nonempty sets certify a live endgame only
(the forward frontier may still miss them, and exact cancellation can still
produce VALUE 0 with final states 0 — as at the rank-1 point P, where this
tester correctly reported all 36 endgames live).

State: packed 60-bit int (6 wide columns x 9 bits + 2 short columns x 3).
Bounded by CAP (over-cap counts as "alive at cap").

Usage:
  python3 wk3_s12_backfeas.py                 # C control + a point's 36 subproblems
"""
import itertools
import sympy as sp

X = sp.symbols('x0:9')
det3 = sp.expand(sp.Matrix(3,3, lambda i,j: X[3*i+j]).det())

def scheme1_tris():
    SHORTS = [(0,1,6),(2,3,6),(4,5,6),(0,2,7),(1,4,7),(3,5,7)]
    REMOVED = {(0,1,2),(3,4,5),(0,1,3),(2,4,5),(0,2,4),(1,3,5)}
    ALL20 = [t for t in itertools.combinations(range(6),3)]
    pure = [t for t in ALL20 if t not in REMOVED]
    tris = SHORTS + pure
    ordered, used = [], set()
    for sym in range(8):
        batch = [t for t in tris if t not in used and sym in t]
        batch.sort(key=lambda t: (0 if (6 in t or 7 in t) else 1, t))
        for t in batch: ordered.append(t); used.add(t)
    return ordered

TRIS = scheme1_tris()
S6 = [i for i,t in enumerate(TRIS) if 6 in t]
S7 = [i for i,t in enumerate(TRIS) if 7 in t]
OFF = [9*e for e in range(6)] + [54, 57]
FULL = sum(0x1FF << OFF[e] for e in range(6)) | (0b111 << 54) | (0b111 << 57)
CAP = 3_000_000

def mons_of(subs):
    f = sp.expand(det3.subs(subs, simultaneous=True))
    return [(int(cf), tuple(i for i in range(9) for _ in range(mono[i])))
            for mono, cf in sp.Poly(f, *X).terms()]

def optmasks(mons, p6, p7, i):
    """Packed leg-bit masks of copy i's admissible options under (p6, p7)."""
    t = TRIS[i]; out = set()
    for c, vs in mons:
        for a in set(itertools.permutations(vs)):
            mask = 0; ok = True
            for k in range(3):
                e, v = t[k], a[k]
                if e == 6 and v != p6[S6.index(i)]: ok = False; break
                if e == 7 and v != p7[S7.index(i)]: ok = False; break
                b = 1 << (OFF[e]+v)
                if mask & b: ok = False; break
                mask |= b
            if ok: out.add(mask)
    return out

def back_feasible(mons, p6, p7, depth=5):
    """Backward-reachable set sizes for the last `depth` copies.
    Ends with 0 => that subproblem is structurally dead."""
    states = {FULL}; sizes = []
    for i in range(19, 19-depth, -1):
        opts = optmasks(mons, p6, p7, i)
        nst = set()
        for st in states:
            for m in opts:
                if st & m == m: nst.add(st ^ m)
        states = nst; sizes.append(len(states))
        if not states or len(states) > CAP: break
    return sizes

def run_point(subs, label, depth=5):
    perms = list(itertools.permutations((0,1,2)))
    mons = mons_of(subs)
    dead = []
    for i6, p6 in enumerate(perms):
        for i7, p7 in enumerate(perms):
            sz = back_feasible(mons, p6, p7, depth)
            if sz and sz[-1] == 0: dead.append(6*i6+i7)
    print(f"{label}: {36-len(dead)}/36 live endgames"
          + (f"; dead: {dead}" if dead else ""))
    return dead

if __name__ == '__main__':
    perms = list(itertools.permutations((0,1,2)))
    ctrl = back_feasible(mons_of({X[5]: X[5]+X[1], X[7]: X[7]+X[2]}), perms[0], perms[0])
    print("control C sub00 (known nonzero) backward sizes:", ctrl)
    assert ctrl[-1] > 0
    run_point({X[3]: X[3]+X[0], X[6]: X[6]+X[0]}, "P (rank-1)")

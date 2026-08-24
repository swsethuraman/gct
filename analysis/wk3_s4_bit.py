"""Week 3, session 4 — evaluate the bit: Phi_18(det_3) != 0 ?
Pattern: 6 epsilon_9's in a cycle; 18 f-copies in 6 groups of 3; each f sends
two legs to its own epsilon and one leg forward to the next.  The contraction
becomes trace(M^6) for an 84x84 integer transfer matrix over sorted forward-triples.
Any nonzero pattern value at any cubic decides via dim(invariants) = 1:
  - value(det_3) != 0        => e(det_3) = 18 and Phi_18 is the fundamental invariant
  - value(det_3) = 0 but value(random) != 0  => Phi_18(det_3) = 0, e(det_3) >= 24
Multilinear monomials only (distinct variable triples), so derivative
combinatorics are clean; global constant factors are irrelevant to the bit.
"""
import itertools, random

def sort_sign(seq):
    """sign of the permutation sorting seq (0 if repeats), bubble count."""
    s = list(seq)
    sign = 1
    n = len(s)
    for i in range(n):
        for j in range(n-1-i):
            if s[j] == s[j+1]: return 0, None
            if s[j] > s[j+1]:
                s[j], s[j+1] = s[j+1], s[j]
                sign = -sign
    return sign, tuple(s)

# det_3 monomials: variables x_{rc} -> index 3*r + c
DET_MONS = []
for sigma in itertools.permutations((0,1,2)):
    sg = 1
    for i in range(3):
        for j in range(i+1,3):
            if sigma[i] > sigma[j]: sg = -sg
    trip = tuple(3*r + sigma[r] for r in range(3))
    DET_MONS.append((trip, sg))

STATES = [tuple(c) for c in itertools.combinations(range(9), 3)]
SIX = {s: i for i, s in enumerate(STATES)}

def f_choices(mons):
    """per f-copy: (fwd_index, pair_sorted, sign) over monomials and forward picks."""
    out = []
    for trip, cf in mons:
        for k in range(3):
            fwd = trip[k]
            rest = tuple(sorted(trip[:k] + trip[k+1:]))
            out.append((fwd, rest, cf))
    return out

def transfer_matrix(mons):
    ch = f_choices(mons)
    n = len(STATES)
    M = [[0]*n for _ in range(n)]
    for si, t_in in enumerate(STATES):
        row = M[si]
        for c1 in ch:
            for c2 in ch:
                for c3 in ch:
                    nine = list(t_in) + list(c1[1]) + list(c2[1]) + list(c3[1])
                    sg_e, srt = sort_sign(nine)
                    if sg_e == 0: continue
                    fwd = (c1[0], c2[0], c3[0])
                    sg_f, fs = sort_sign(fwd)
                    if sg_f == 0: continue
                    row[SIX[fs]] += sg_e*sg_f*c1[2]*c2[2]*c3[2]
    return M

def mat_mul(A, B):
    n = len(A)
    Bt = list(zip(*B))
    return [[sum(a*b for a, b in zip(row, col)) for col in Bt] for row in A]

def trace_pow(M, k):
    R = M
    for _ in range(k-1):
        R = mat_mul(R, M)
    return sum(R[i][i] for i in range(len(R)))

print("building transfer matrix for det_3 ...")
M = transfer_matrix(DET_MONS)
nz = sum(1 for row in M for v in row if v)
print(f"  nonzero entries: {nz}")
val_det = trace_pow(M, 6)
print(f"pattern value at det_3: trace(M^6) = {val_det}")

# sparse random multilinear cubics as pattern-nonvanishing witnesses
random.seed(101)
def random_mons(nmon):
    mons = []
    trips = random.sample(list(itertools.combinations(range(9), 3)), nmon)
    for t in trips:
        mons.append((t, random.choice((1, -1, 2, -2, 3))))
    return mons

if val_det != 0:
    print("\n=> THE BIT IS 1: e(det_3) = 18, and the unique degree-18 invariant is the")
    print("   fundamental invariant of det_3; by BI Prop 3.9 its zero set in the orbit")
    print("   closure equals the boundary — the discriminant of determinantal complexity.")
else:
    print("\nvalue at det_3 is 0; testing whether the pattern is nonzero as a polynomial ...")
    witness = 0
    for trial in range(6):
        Mr = transfer_matrix(random_mons(8 + trial))
        v = trace_pow(Mr, 6)
        print(f"  random sparse cubic #{trial}: value {v}")
        if v != 0:
            witness = v; break
    if witness:
        print("\n=> pattern is a NONZERO invariant vanishing at det_3:")
        print("   THE BIT IS 0: Phi_18(det_3) = 0 and e(det_3) >= 24.")
    else:
        print("\n=> pattern appears identically zero; variant patterns needed (offset-2 forward etc.)")

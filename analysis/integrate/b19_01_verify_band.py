"""Integrator check of B19-01's Silence theorem scope.

Band condition: lambda_1 + lambda_2 + lambda_3 <= 2d, for lambda |- 4d with ell rows.
Claims: empty for ell <= 5; non-empty for ell = 6..10; at ell = 6 it is the single
rectangle ((2d/3)^6).
"""
def parts(n, k, maxp=None):
    "partitions of n into exactly k positive parts, weakly decreasing"
    if maxp is None: maxp = n
    if k == 0:
        if n == 0: yield ()
        return
    for f in range(min(n - (k-1), maxp), 0, -1):
        for rest in parts(n-f, k-1, f): yield (f,)+rest

print(f"{'d':>3} {'ell':>4} {'partitions':>11} {'in band':>8}   band members (if few)")
for d in (5,6,7,8):
    for ell in range(3, 11):
        P = list(parts(4*d, ell))
        band = [l for l in P if l[0]+l[1]+l[2] <= 2*d]
        show = ''
        if 0 < len(band) <= 3: show = '   ' + ', '.join(str(b) for b in band)
        print(f"{d:>3} {ell:>4} {len(P):>11} {len(band):>8}{show}")
    print()

print("the two structural facts, checked as arithmetic:")
print("  ell <= 5: top three of five parts sum to >= (3/5)*4d = 2.4d > 2d, so the band is empty")
print("  ell  = 6: top three of six sum to >= (3/6)*4d = 2d, equality iff all parts equal")
for d in (6,9,12):
    tgt = tuple([2*d//3]*6)
    ok = (sum(tgt) == 4*d) and (2*d) % 3 == 0
    print(f"     d={d}: ((2d/3)^6) = {tgt}, sums to {sum(tgt)} (4d = {4*d})  {'OK' if ok else 'not an integer rectangle'}")

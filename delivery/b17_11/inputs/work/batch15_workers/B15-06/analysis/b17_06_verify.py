"""One bounded B17-06 control: exact integers, no external modules or subprocesses.

Run from the assigned worktree using .venv/python.exe -B analysis/b15_bound.py
--slot 06 --name b17_06_control_01 --seconds 60 --memory-mb 512
analysis/b17_06_verify.py --output results/b17_06/control_01.json
This is a degree-five instrument check, never a candidate search.
"""
import argparse
from fractions import Fraction
from itertools import permutations
from math import comb, factorial
from pathlib import Path
import hashlib
import json
import os
import time

ROOT = Path(__file__).resolve().parents[1]
PERMS = tuple(permutations(range(3)))
EVEN = (0, 3, 4)
ODD = (1, 2, 5)
STATS = {"products": 0, "term_pairs": 0, "max_support": 0,
         "max_coefficient_bits": 0}
START = time.monotonic()


def need(ok, message):
    if not ok:
        raise ValueError(message)


def guard():
    need(time.monotonic() < float(os.environ["CI73_DEADLINE"]) - 2,
         "UNCOMPUTED: deadline guard")
    need(STATS["term_pairs"] <= 250000, "UNCOMPUTED: priced term-pair cap")


def clean(p):
    p = {a: c for a, c in p.items() if c}
    need(len(p) <= 252, "UNCOMPUTED: support cap")
    bits = max((abs(c).bit_length() for c in p.values()), default=0)
    need(bits <= 4096, "UNCOMPUTED: coefficient bit cap")
    STATS["max_support"] = max(STATS["max_support"], len(p))
    STATS["max_coefficient_bits"] = max(STATS["max_coefficient_bits"], bits)
    return p


def add(*ps):
    ans = {}
    for p in ps:
        for a, c in p.items():
            ans[a] = ans.get(a, 0) + c
    return clean(ans)


def scale(p, c):
    return clean({a: b*c for a, b in p.items()})


def mul(p, q):
    STATS["products"] += 1
    ans = {}
    for a, c in p.items():
        for b, e in q.items():
            STATS["term_pairs"] += 1
            k = tuple(x+y for x, y in zip(a, b))
            ans[k] = ans.get(k, 0) + c*e
    guard()
    return clean(ans)


def power(p, d):
    n = len(next(iter(p)))
    ans = {(0,)*n: 1}
    for _ in range(d):
        ans = mul(ans, p)
    return ans


def var(i, n):
    return {tuple(int(j == i) for j in range(n)): 1}


def sources(a):
    c, a1, a2, a3, a4 = a
    h = add(scale(mul(c, a2), 8), scale(power(a1, 2), -3))
    inv = add(power(a2, 2), scale(mul(a1, a3), -3),
              scale(mul(c, a4), 12))
    return mul(power(c, 3), inv), mul(c, power(h, 2))


def raising(p):
    ans = {}
    for a, c in p.items():
        for i in range(1, 5):
            if a[i]:
                b = list(a)
                b[i] -= 1
                b[i-1] += 1
                b = tuple(b)
                ans[b] = ans.get(b, 0) + c*a[i]*(5-i)
    return clean(ans)


def unimul(p, q):
    ans = [0]*(len(p)+len(q)-1)
    for i, c in enumerate(p):
        for j, e in enumerate(q):
            ans[i+j] += c*e
    return ans


def q_coefficients(last):
    # Binary restriction of ten independent linear forms. Lists ascend in t.
    entries = [[[1, 1], [2], [1]],
               [[3], [1, 1], [2]],
               [[2], [1], [last, 1]]]
    out = []
    for perm in PERMS:
        p = [2, 1]  # z=t+2
        for i in range(3):
            p = unimul(p, entries[i][perm[i]])
        p += [0]*(5-len(p))
        out.append(list(reversed(p)))
    return out


def universal_sources(last):
    qs = q_coefficients(last)
    return sources([add(*(scale(var(s, 6), qs[s][j]) for s in range(6)))
                    for j in range(5)])


def normal(a):
    k = min(a[i] for i in EVEN)
    return tuple(v-k if i in EVEN else v+k for i, v in enumerate(a))


def normal_poly(p):
    ans = {}
    for a, c in p.items():
        b = normal(a)
        ans[b] = ans.get(b, 0) + c
    return clean(ans)


def incidence(a):
    ans = [0]*9
    for multiplicity, perm in zip(a, PERMS):
        for i, j in enumerate(perm):
            ans[3*i+j] += multiplicity
    return tuple(ans)


def image_poly(p):
    ans = {}
    for a, c in p.items():
        b = incidence(a)
        ans[b] = ans.get(b, 0) + c
    return clean(ans)


def compositions(d, n):
    if n == 1:
        yield (d,)
    else:
        for i in range(d+1):
            for a in compositions(d-i, n-1):
                yield (i,)+a


def det(mat):
    a = [[Fraction(c) for c in row] for row in mat]
    result = Fraction(1)
    for j in range(len(a)):
        pivot = next((i for i in range(j, len(a)) if a[i][j]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            result = -result
        v = a[j][j]
        result *= v
        for i in range(j+1, len(a)):
            q = a[i][j]/v
            for k in range(j+1, len(a)):
                a[i][k] -= q*a[j][k]
    return result


def arc_rows(p, entry, order):
    return [sum(c*comb(a[entry], k) for a, c in p.items())
            for k in range(order+1)]


def encoded(p, d):
    base = d+1
    weights = (1, base, base**2, base**3)
    ans = {}
    for a, c in p.items():
        e = sum(a[i]*w for i, w in zip((4, 5, 7, 8), weights))
        need(e not in ans, "base encoding collision")
        ans[e] = c
    return ans


def serialized(p):
    return [{"exponent": list(a), "coefficient": c} for a, c in sorted(p.items())]


def check_pins():
    manifest = json.loads((ROOT/'delivery/b17_06/INPUTS.json').read_text(encoding='utf-8-sig'))
    pinned = {}
    for row in manifest['entries']:
        raw = (ROOT/row['snapshot']).read_bytes()
        need(hashlib.sha256(raw).hexdigest() == row['sha256'], "input snapshot hash")
        pinned[row['original_path'].replace('\\', '/')] = row
    def entry(suffix):
        return next(v for k, v in pinned.items() if k.endswith(suffix))
    for name in ['docs/b16_10_proof.md', 'results/jet_certificate.json']:
        original = ('results/b16_10/jet_certificate.json' if name.startswith('results') else name)
        need(entry('/B15-10/'+original)['sha256'] ==
             entry('/Batch16/reviews/10/'+name)['sha256'], "original/review equality")
    package = json.loads((ROOT/entry('/delivery/b16_10/SHA256_MANIFEST.json')['snapshot']).read_text())
    for name, original in [('docs/b16_10_proof.md', 'docs/b16_10_proof.md'),
                           ('results/jet_certificate.json', 'results/b16_10/jet_certificate.json')]:
        expected = next(v for v in package['files'] if v['path'] == name)
        need(expected['sha256'] == entry('/B15-10/'+original)['sha256'], "accepted package binding")
    old_inputs = json.loads((ROOT/entry('/results/b16_10/input_hashes.json')['snapshot']).read_text())
    for leaf in ['REPORT.md', 'integrator_review.json']:
        suffix = '/Hessian11_1631/'+leaf
        inherited = next(v for v in old_inputs['entries']
                         if v['original_path'].replace('\\', '/').endswith(suffix))
        need(inherited['sha256'] == entry(suffix)['sha256'], "original Hessian source binding")
    return {"input_snapshots_verified": len(pinned),
            "original_review_and_accepted_package_binding": "PASS",
            "original_hessian_input_binding": "PASS",
            "historical_hessian_arithmetic_replayed": False}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    need(output.is_relative_to(ROOT/'results/b17_06'), "authorized output path")
    need(not output.exists(), "preserve existing receipt")
    pins = check_pins()

    # First: the known degree-five multiplicity-two control, independently explicit.
    ambient = sources([var(i, 5) for i in range(5)])
    for f in ambient:
        need(not raising(f), "highest-weight raising equation")
        need(all(sum(a) == 5 and sum(i*a[i] for i in range(5)) == 4 for a in f),
             "same finite degree and weight")
    weight_counts = [sum(1 for a in compositions(5, 5)
                         if sum(i*a[i] for i in range(5)) == w) for w in (4, 3)]
    need(weight_counts == [5, 3], "binary ambient multiplicity control")

    f1, f2 = universal_sources(5)
    im1, im2 = image_poly(f1), image_poly(f2)
    rows1, rows2 = arc_rows(im1, 1, 5), arc_rows(im2, 1, 5)
    need(rows1 == [-59, -18, 36, 0, 0, 0], "F1 exact unit arc")
    need(rows2 == [1369, 3552, 2304, 0, 0, 0], "F2 exact unit arc")
    minor = rows1[0]*rows2[1]-rows2[0]*rows1[1]
    need(minor == -184926, "known two-row control minor")
    # Full ten-by-ten matrix, including every permanent entry.
    a = [1, 1, 0, 0, 0, 1, 0, 0, 0, 1]
    b = [2, 1, 2, 1, 3, 1, 2, 2, 1, 5]
    matrix = [[a[i], b[i]]+[int(i == j) for j in range(2, 10)] for i in range(10)]
    need(det(matrix) == -1, "full-support base invertible")
    changed = [row[:] for row in matrix]
    changed[2] = [3*x for x in changed[2]]
    need(det(changed) == -3, "entry scaling determinant control")

    # Then: all collision classes in degrees zero through five, never a higher job.
    counts = []
    total_compositions = 0
    for d in range(6):
        fibers, normals, four_digits, codes = {}, set(), set(), set()
        for alpha in compositions(d, 6):
            total_compositions += 1
            t, n = incidence(alpha), normal(alpha)
            need(incidence(n) == t, "normal form preserves entries")
            need(min(n[i] for i in EVEN) == 0, "canonical normal form")
            if t in fibers:
                need(fibers[t] == n, "complete signed collision fibers")
            fibers[t] = n
            normals.add(n)
        for t in fibers:
            need(all(sum(t[3*i:3*i+3]) == d for i in range(3)), "row margins")
            need(all(sum(t[j::3]) == d for j in range(3)), "column margins")
            digits = tuple(t[i] for i in (4, 5, 7, 8))
            four_digits.add(digits)
            codes.add(sum(v*(d+1)**i for i, v in enumerate(digits)))
        expected = comb(d+5, 5) - (comb(d+2, 5) if d >= 3 else 0)
        need(len(fibers) == len(normals) == len(four_digits) == len(codes) == expected,
             "support count / four-parameter / arc injectivity")
        counts.append({"degree": d, "raw": comb(d+5, 5), "merged": expected})

    n1, n2 = normal_poly(f1), normal_poly(f2)
    need(image_poly(n1) == im1 and image_poly(n2) == im2, "two independent aggregation routes")
    rplus = tuple(int(i in EVEN) for i in range(6))
    rminus = tuple(int(i in ODD) for i in range(6))
    relation = {rplus: 1, rminus: -1}
    need(not normal_poly(relation) and not image_poly(relation), "cubic signed cancellation")
    need(image_poly({rplus: 1, rminus: 1}) == {(1,)*9: 2}, "wrong sign detected")

    old1, old2 = universal_sources(4)
    need(not normal_poly(add(old2, scale(old1, -64))), "old base torus blind identity")
    need(normal_poly(add(f2, scale(f1, -64))), "base perturbation restores information")

    enc1, enc2 = encoded(im1, 5), encoded(im2, 5)
    support = sorted(set(enc1) | set(enc2))
    jets = [[sum(c*comb(e, k) for e, c in enc.items()) for enc in (enc1, enc2)]
            for k in range(len(support))]
    found = next(((i, j, jets[i][0]*jets[j][1]-jets[i][1]*jets[j][0])
                  for i in range(len(jets)) for j in range(i+1, len(jets))
                  if jets[i][0]*jets[j][1] != jets[i][1]*jets[j][0]), None)
    need(found is not None, "encoded invertible arc preserves independence")
    sample = support[:4]
    vandermonde = [[comb(e, k) for e in sample] for k in range(len(sample))]
    expected = Fraction(1)
    for i, x in enumerate(sample):
        for y in sample[i+1:]:
            expected *= y-x
    for k in range(len(sample)):
        expected /= factorial(k)
    need(det(vandermonde) == expected != 0, "binomial Vandermonde control")

    receipt = {"status": "PASS", "scope": "known d=5 lambda=(16,4) control; no new-cell search",
               "pins": pins, "permutation_order": [list(p) for p in PERMS],
               "source_formulas": ["c^3*(a2^2-3*a1*a3+12*c*a4)", "c*(8*c*a2-3*a1^2)^2"],
               "highest_weight_checks": "PASS", "weight_counts_4_3": weight_counts,
               "base_matrix": matrix, "base_determinant": -1,
               "binary_permutation_coefficients_t4_to_t0": q_coefficients(5),
               "simple_arc": {"entry": "X12", "scale": "1+u", "determinant": "-(1+u)",
                              "F1_coefficients": rows1, "F2_coefficients": rows2,
                              "minor_rows": [0, 1], "minor": minor, "rank": 2},
               "normal_forms": [serialized(n1), serialized(n2)],
               "direct_entry_coefficients": [serialized(im1), serialized(im2)],
               "support_counts": counts, "compositions_checked": total_compositions,
               "signed_cancellation_and_wrong_sign_control": "PASS",
               "old_base_last_entry_4": {"global_torus_identity": "F2=64*F1", "rank": 1},
               "encoded_arc": {"four_entry_weights": [1, 6, 36, 216],
                               "support_exponents": support, "support_count": len(support),
                               "Hasse_rows": jets, "nonzero_minor": list(found),
                               "four_by_four_binomial_minor": str(expected)},
               "statistics": STATS, "script_seconds": time.monotonic()-START,
               "historical_B16_arc_replayed": False,
               "positive_multiplicity_gap": False}
    output.write_text(json.dumps(receipt, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({"status": "PASS", "simple_arc_minor": minor,
                      "encoded_arc_minor": list(found), "statistics": STATS}))


if __name__ == '__main__':
    main()

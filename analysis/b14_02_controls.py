#!/usr/bin/env python3
"""B14-02 controls C1 (forced zero), C2 (transport identity), C4 (CRT soundness),
C5 (u-nonvanishing).  Every control is run twice: on the real input, and on an
input constructed so a working control MUST report failure.

C1  forced zero.  F_T has weight lambda = (21,17,2^7), which has 9 nonzero parts,
    and F_T(f) is a sum of monomials prod_l c_{alpha_l} with sum_l alpha_l =
    lambda exactly.  If f is supported on a PROPER COORDINATE SUBSPACE -- say it
    does not involve x_8 -- then c_alpha = 0 unless supp(alpha) is inside that
    subspace, so every surviving monomial would need sum_l alpha_l supported
    there, contradicting lambda_9 = 2 > 0.  Hence F_T(f) = 0 for all 39 rows,
    forced by the weight and provable without any computation
    (PROVED.md: negative_control_forced).  Stated for coordinate-supported
    points only; the general "span < l(lambda)" form is not needed and is not
    claimed here.

C2  transport identity: F_{T^up13}(f) = F_T(f) * msym_u(f)^(13 - d).  Live only
    for the two rung-12 rows (exponent 1); trivial for the 37 rung-13 rows.
    Must-fail: the degree-24 exponent 24 - d that source.json stores.
"""
import argparse, json, math, os, random, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from wk8_s30_core import exps                                        # noqa: E402
from wk11_s69_circuit import Filling, sym_table                      # noqa: E402
from wk12_s74_dp import dp_eval_compact                              # noqa: E402
from b14_02_source13 import (PRIMES, climb_to, load_rows, load_points,   # noqa: E402
                             height_bound, crt_pair, OUT, N, H, DEG, E4, FACT, IU)

T0 = time.time()


def log(*a):
    print(f"[{time.time()-T0:8.1f}s]", *a, flush=True)


def cv_from(lin, cub):
    """quartic coefficient vector of l*c over exps(4,9); cub keyed by exps(3,9)."""
    co = {}
    for al, cc in cub.items():
        if cc == 0:
            continue
        for i in range(H):
            if lin[i] == 0:
                continue
            a = list(al); a[i] += 1
            k = tuple(a)
            co[k] = co.get(k, 0) + lin[i] * cc
    return [int(co.get(al, 0)) for al in E4]


def control_points(seed=1402):
    """three coordinate-supported reducible quartics (forced zero) and one
    full-support point (the must-fail input, which must NOT be zero)."""
    rng = random.Random(seed)
    E3 = exps(3, H)
    out = []

    # N1: l * c omitting x_8 entirely -> supported on {x_0..x_7}
    lin = [rng.randint(-7, 7) for _ in range(H)]; lin[8] = 0
    cub = {b: (0 if b[8] else rng.randint(-7, 7)) for b in E3}
    out.append(dict(name="N1_missing_x8", forced_zero=True,
                    why="coordinate-supported on 8 of 9 variables",
                    cv=cv_from(lin, cub)))

    # N2: product of four linear forms in x_0..x_3 only
    fs = [[rng.randint(-7, 7) if i < 4 else 0 for i in range(H)] for _ in range(4)]
    lin2 = fs[0]
    cub2 = {}
    for b1 in range(H):
        if fs[1][b1] == 0: continue
        for b2 in range(H):
            if fs[2][b2] == 0: continue
            for b3 in range(H):
                if fs[3][b3] == 0: continue
                a = [0] * H; a[b1] += 1; a[b2] += 1; a[b3] += 1
                k = tuple(a)
                cub2[k] = cub2.get(k, 0) + fs[1][b1] * fs[2][b2] * fs[3][b3]
    out.append(dict(name="N2_four_linear_forms_4vars", forced_zero=True,
                    why="product of four linear forms in x_0..x_3; coordinate-supported on 4 of 9",
                    cv=cv_from(lin2, cub2)))

    # N3: l * (product of three linear forms), all in x_0..x_7
    l3 = [rng.randint(-7, 7) if i < 8 else 0 for i in range(H)]
    gs = [[rng.randint(-7, 7) if i < 8 else 0 for i in range(H)] for _ in range(3)]
    cub3 = {}
    for b1 in range(H):
        if gs[0][b1] == 0: continue
        for b2 in range(H):
            if gs[1][b2] == 0: continue
            for b3 in range(H):
                if gs[2][b3] == 0: continue
                a = [0] * H; a[b1] += 1; a[b2] += 1; a[b3] += 1
                k = tuple(a)
                cub3[k] = cub3.get(k, 0) + gs[0][b1] * gs[1][b2] * gs[2][b3]
    out.append(dict(name="N3_reducible_8vars", forced_zero=True,
                    why="l * (three linear forms), coordinate-supported on 8 of 9",
                    cv=cv_from(l3, cub3)))
    return out


def run(prime, workers=2):
    rows = load_rows()[1]
    _, pts = load_points("primary")
    res = dict(prime=prime, values_are="raw evaluator outputs mod the stated prime; no transform")
    _A, _idx, _fact, TAB = sym_table(N, H)

    # ---------------- C1 forced zero, plus the must-fail input
    c1 = []
    for cp in control_points():
        ms = [(c % prime) * FACT[a] % prime for a, c in enumerate(cp["cv"])]
        vals = [dp_eval_compact(r["F"], ms, prime, TAB) for r in rows]
        nz = sum(1 for v in vals if v % prime)
        c1.append(dict(name=cp["name"], why=cp["why"], expect="all zero",
                       nonzero_rows=nz, pass_=(nz == 0)))
        log(f"C1 {cp['name']}: {nz}/39 nonzero rows -> {'PASS' if nz==0 else 'FAIL'}")
    # must-fail: a real, full-support primary point must NOT be all zero
    q = pts[0]
    ms = [(c % prime) * FACT[a] % prime for a, c in enumerate(q["cv"])]
    vals = [dp_eval_compact(r["F"], ms, prime, TAB) for r in rows]
    nz = sum(1 for v in vals if v % prime)
    c1_mustfail = dict(point=q["id"], nonzero_rows=nz, control_can_fail=(nz > 0))
    log(f"C1 MUST-FAIL on real point {q['id']}: {nz}/39 nonzero -> "
        f"{'control can fail' if nz else 'CONTROL IS VACUOUS'}")

    # ---------------- C2 transport identity
    c2, c2_bad = [], []
    for r in rows:
        if r["exponent"] == 0:
            continue                      # rung 13: T^up13 IS the native filling
        Fn = Filling.from_json(r["native"])
        for q in pts[:4]:
            ms = [(c % prime) * FACT[a] % prime for a, c in enumerate(q["cv"])]
            u = ms[IU]
            lit = dp_eval_compact(r["F"], ms, prime, TAB)
            nat = dp_eval_compact(Fn, ms, prime, TAB) * pow(u, r["exponent"], prime) % prime
            c2.append(dict(row=r["index"], rung=r["rung"], col=q["id"],
                           exponent=r["exponent"], literal=lit, scaled_native=nat,
                           ok=(lit == nat)))
            wrong = dp_eval_compact(Fn, ms, prime, TAB) * pow(u, 24 - r["rung"], prime) % prime
            c2_bad.append(dict(row=r["index"], col=q["id"], wrong_exponent=24 - r["rung"],
                               differs=(wrong != lit)))
    log(f"C2 transport: {sum(c['ok'] for c in c2)}/{len(c2)} agree at exponent 13-d")
    log(f"C2 MUST-FAIL (exponent 24-d): {sum(c['differs'] for c in c2_bad)}/{len(c2_bad)} differ "
        f"-> {'control can fail' if all(c['differs'] for c in c2_bad) else 'VACUOUS'}")

    # ---------------- C5 u-nonvanishing, integer and modular
    c5 = dict(integer_zero=[q["id"] for q in pts if q["u"] == 0],
              mod_zero={str(p): [q["id"] for q in pts if q["u"] % p == 0] for p in PRIMES})
    c5["pass_"] = not c5["integer_zero"] and not any(c5["mod_zero"].values())
    log(f"C5 u-nonvanishing over all 96 columns and 7 primes: "
        f"{'PASS' if c5['pass_'] else 'FAIL'}")

    res.update(C1=c1, C1_must_fail=c1_mustfail, C2=c2,
               C2_must_fail=c2_bad, C5=c5)
    os.makedirs(OUT, exist_ok=True)
    json.dump(res, open(os.path.join(OUT, f"controls_{prime}.json"), "w"), indent=1)
    log("wrote " + os.path.join(OUT, f"controls_{prime}.json"))
    return res


def crt_soundness():
    """C4: reconstruct with a deliberately insufficient modulus and show it breaks."""
    H13, _ = height_bound()
    full = math.prod(PRIMES)
    short = math.prod(PRIMES[:3])
    rows = load_rows()[1]
    _, pts = load_points("primary")
    blocks = {p: json.load(open(os.path.join(OUT, f"residues_primary_{p}.json"),
                                encoding="utf-8")) for p in PRIMES}

    def recon(prime_list):
        m0 = prime_list[0]
        bad = 0; total = 0
        for r in rows[:6]:
            key = str(r["index"])
            for j in range(len(pts)):
                acc, m = blocks[m0]["rows"][key][j] % m0, m0
                for p in prime_list[1:]:
                    acc, m = crt_pair(acc, m, blocks[p]["rows"][key][j] % p, p)
                acc %= m
                v = acc - m if acc > m // 2 else acc
                total += 1
                # the honest test: does this integer reproduce ALL SEVEN residues?
                if any(v % p != blocks[p]["rows"][key][j] % p for p in PRIMES):
                    bad += 1
        return bad, total

    bad_s, tot = recon(PRIMES[:3])
    bad_f, _ = recon(PRIMES)
    log(f"C4 three primes ({short.bit_length()} bits < {(2*H13).bit_length()} needed): "
        f"{bad_s}/{tot} entries fail the seven-residue test")
    log(f"C4 seven primes ({full.bit_length()} bits): {bad_f}/{tot} fail")
    out = dict(values_are="counts of reconstruction failures; no transform",
               bound_bits=(2 * H13).bit_length(),
               three_prime_bits=short.bit_length(), three_prime_failures=bad_s,
               seven_prime_bits=full.bit_length(), seven_prime_failures=bad_f,
               tested=tot,
               control_can_fail=(bad_s > 0), pass_=(bad_f == 0 and bad_s > 0))
    json.dump(out, open(os.path.join(OUT, "crt_soundness.json"), "w"), indent=1)
    return out


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--prime", type=int, default=PRIMES[0])
    ap.add_argument("--crt", action="store_true")
    a = ap.parse_args(argv)
    if a.crt:
        crt_soundness()
    else:
        run(a.prime)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

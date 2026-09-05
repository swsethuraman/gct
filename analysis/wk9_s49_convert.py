#!/usr/bin/env python3
"""Session 49 -- convert the certificates on record into the declared format
(tools/verify/FORMAT.md) under results/certs/.

This is worker-side code: it imports the pipeline's orbit expansion
(analysis/wk9_s42_orbits.orbit_setup_fast) to turn the chi-coordinate vectors
of results/s42_certs/ and results/s41_cells/*_cert_chi.txt into explicit
monomial vectors, and it parses the expanded mod-p vectors of
results/s41_cells/ and results/s43_cells/.  The verifier (tools/verify/) shares
no code with this file or with anything it imports; whatever the expansion
gets wrong the verifier is meant to catch.

Claims written into each converted certificate are exactly the claims the
record makes for that vector: (star) support (the pipeline's definition of the
red columns), linear independence of the lifted vectors, vanishing at fresh
padded-permanent and reducible points, non-vanishing at fresh generic quartics,
and non-vanishing at fresh det_4 pencils only at cells where the record has
mult_det = a (results/sixrow_record.md, results/s36_ledger.md).

usage: python3 analysis/wk9_s49_convert.py [--only NAME]
"""
import sys, os, re, ast, json, gzip, glob, time
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
sys.path.insert(0, HERE)
from wk9_s42_orbits import orbit_setup_fast          # pipeline code (worker side)
from wk8_s30_core import exps, monomials              # pipeline code (worker side)
from wk8_s30_pleth import a_of                         # pipeline code (worker side)

# A converted certificate whose committed size would come within reach of the
# 5 MB commit limit is written to a scratch directory instead (regenerable from
# this converter and the committed chi-form certificate), and verified there.
COMMIT_LIMIT = 4_500_000
OUT = os.path.join(ROOT, "results", "certs")
BIG_OUT = os.environ.get("S49_BIG_OUT", "/root/s49_bigcerts")

FORMAT = "gct-cert/1"
CONVENTIONS = {
    "coefficient": "c_alpha(F) = coefficient of s^alpha in F",
    "raising": "E_ij c_alpha = (alpha_i + 1) c_{alpha + e_i - e_j}",
}
SEED = 20260905

# cells where the record has mult_det = a (so a nonzero reducibility HWV is
# nonvanishing on D_r): the fourteen bites of results/sixrow_record.md and the
# length-5 bites of results/s36_ledger.md
DET_EMPTY = {
    ((8, 4, 4, 4, 4), 6), ((12, 4, 4, 4, 4), 7), ((9, 9, 8, 1, 1), 7), ((8, 8, 8, 2, 2), 7),
    ((10, 8, 7, 1, 1, 1), 7), ((11, 9, 9, 1, 1, 1), 8), ((11, 10, 8, 1, 1, 1), 8),
    ((12, 9, 8, 1, 1, 1), 8), ((12, 10, 7, 1, 1, 1), 8), ((13, 8, 8, 1, 1, 1), 8),
    ((13, 9, 7, 1, 1, 1), 8), ((13, 10, 6, 1, 1, 1), 8), ((13, 12, 4, 1, 1, 1), 8),
    ((14, 8, 7, 1, 1, 1), 8), ((16, 13, 4, 1, 1, 1), 9), ((17, 12, 4, 1, 1, 1), 9),
}


def claims_for(lam, delta, modulus):
    fams_nonvan = ["generic"] + (["det_pencil"] if (tuple(lam), delta) in DET_EMPTY else [])
    return {
        "independent": True,
        "star_support": {"k": 1},
        "fresh_points": {"seed": SEED, "count": 6,
                         "vanishes_on": ["padded_permanent", "reducible"],
                         "nonvanishing_on": fams_nonvan},
    }


def write_cert(name, obj):
    """Serialise, then place by final artifact size: committable files go to
    results/certs/, anything within reach of the 5 MB limit goes to the scratch
    directory (regenerable, still verified)."""
    raw = json.dumps(obj, separators=(",", ":")).encode("utf-8")
    gzipped = len(raw) > 400_000
    blob = gzip.compress(raw) if gzipped else raw
    big = len(blob) > COMMIT_LIMIT
    outdir = BIG_OUT if big else OUT
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, name + ".json" + (".gz" if gzipped else ""))
    with open(path, "wb") as f:
        f.write(blob)
    where = path if big else os.path.relpath(path, ROOT)
    print(f"  wrote {where} ({len(blob)/1e6:.2f} MB){' [scratch: within reach of the 5 MB limit]' if big else ''}", flush=True)
    return path


def expand_chi(lam, delta, red, chivecs):
    """chi-coordinate vectors (one per red orbit) -> explicit term lists."""
    r = len(lam)
    A = exps(4, r)
    basis, vecs, group = orbit_setup_fast(4, r, delta, lam, verbose=False, want_vecs=True)
    out = []
    for x in chivecs:
        assert len(x) == len(red), (len(x), len(red))
        acc = {}
        for coeff, oj in zip(x, red):
            if coeff == 0:
                continue
            for mono, sgn in vecs[oj].items():
                acc[mono] = acc.get(mono, 0) + coeff * sgn
        terms = []
        for mono, c in acc.items():
            if c:
                terms.append([[list(A[k]) for k in mono], c])
        terms.sort(key=lambda t: t[0])
        out.append({"terms": terms})
    return out


def convert_chi_file(path, title_prefix):
    txt = open(path).read().splitlines()
    head = [l for l in txt if l.startswith("#")]
    body = [l for l in txt if l and not l.startswith("#")]
    m = re.search(r"lam=\((.*?)\) delta=(\d+) a=(\d+) nullity=(\d+)", " ".join(head))
    lam = tuple(int(x) for x in m.group(1).split(","))
    delta, a, k = int(m.group(2)), int(m.group(3)), int(m.group(4))
    red = ast.literal_eval(next(l for l in head if l.startswith("# red = "))[len("# red = "):])
    chivecs = [[int(v) for v in l.split()] for l in body]
    assert len(chivecs) == k, (path, len(chivecs), k)
    assert a == a_of(lam, delta, 4, len(lam))
    vectors = expand_chi(lam, delta, red, chivecs)
    name = f"{'_'.join(map(str, lam))}_d{delta}_int"
    obj = {
        "format": FORMAT, "kind": "hwv",
        "title": f"{title_prefix}: {k} integer HWV(s) of weight {lam} in degree {delta} in I(R_{len(lam)})",
        "produced_by": f"analysis/wk9_s49_convert.py from {os.path.relpath(path, ROOT)}",
        "notes": "chi-coordinates of the red orbits expanded with analysis/wk9_s42_orbits.orbit_setup_fast; "
                 f"record claims mult_red = {a - k} = a - {k} at this cell",
        "cell": {"n": 4, "r": len(lam), "lambda": list(lam), "delta": delta, "a": a},
        "conventions": dict(CONVENTIONS), "modulus": None,
        "vectors": vectors, "claims": claims_for(lam, delta, None),
    }
    p = write_cert(name, obj)
    exps.cache_clear(); monomials.cache_clear()
    return p


def convert_vec_file(path, title_prefix):
    opener = gzip.open if path.endswith(".gz") else open
    with opener(path, "rt") as f:
        lines = f.read().splitlines()
    head = lines[0]
    m = re.search(r"weight \((.*?)\) delta (\d+) HWV vanishing on the pad side, mod (\d+)", head)
    lam = tuple(int(x) for x in m.group(1).split(","))
    delta, p = int(m.group(2)), int(m.group(3))
    terms = []
    for l in lines[1:]:
        if not l.strip():
            continue
        lst, coeff = l.rsplit(" ", 1)
        alphas = ast.literal_eval(lst)
        c = int(coeff) % p
        if c:
            terms.append([[list(a) for a in alphas], c])
    terms.sort(key=lambda t: t[0])
    base = os.path.basename(path).replace(".txt.gz", "").replace(".txt", "")
    a = a_of(lam, delta, 4, len(lam))
    obj = {
        "format": FORMAT, "kind": "hwv",
        "title": f"{title_prefix}: mod-{p} HWV of weight {lam} in degree {delta} vanishing on the pad side ({base})",
        "produced_by": f"analysis/wk9_s49_convert.py from {os.path.relpath(path, ROOT)}",
        "notes": "a mod-p vector: raising operators and evaluations are checked modulo p only",
        "cell": {"n": 4, "r": len(lam), "lambda": list(lam), "delta": delta, "a": a},
        "conventions": dict(CONVENTIONS), "modulus": p,
        "vectors": [{"terms": terms}], "claims": claims_for(lam, delta, p),
    }
    return write_cert(base + "_modp", obj)


def main():
    only = None
    if "--only" in sys.argv:
        only = sys.argv[sys.argv.index("--only") + 1]
    t0 = time.time()
    for path in sorted(glob.glob(os.path.join(ROOT, "results", "s42_certs", "*.txt"))):
        if only and only not in path:
            continue
        print(f"[chi] {os.path.relpath(path, ROOT)}", flush=True)
        convert_chi_file(path, "s42/s47 lift")
    for path in sorted(glob.glob(os.path.join(ROOT, "results", "s41_cells", "*_cert_chi.txt"))):
        if only and only not in path:
            continue
        print(f"[chi] {os.path.relpath(path, ROOT)}", flush=True)
        convert_chi_file(path, "integrator lift (s41 cell)")
    for path in sorted(glob.glob(os.path.join(ROOT, "results", "s41_cells", "*_vec*.txt"))
                       + glob.glob(os.path.join(ROOT, "results", "s43_cells", "*_vec*.txt.gz"))):
        if only and only not in path:
            continue
        print(f"[vec] {os.path.relpath(path, ROOT)}", flush=True)
        convert_vec_file(path, "s41/s43 pad-side kernel vector")
    print(f"done in {time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()

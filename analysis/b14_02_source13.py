#!/usr/bin/env python3
"""B14-02 -- the exact degree-13 LMR source matrix at P13.

Rows    the 39 source entries of results/s74/source.json with rung <= 13
        (2 at rung 12, 37 at rung 13), each climbed to degree 13 -- transport
        exponent 13 - native_degree.  source.json's stored `literal` is climbed
        to degree 24 and is deliberately NOT used.
Columns the 96 role == "primary" points of results/b14_prep/points/P13.json,
        reducible quartics f = l*c with |l_i| <= 7, |c_beta| <= 7.
Values  F_{T_i^{up13}}(f_j) as exact integers, by signed CRT over SEVEN primes
        against the bound re-derived in results/PREREG_b14_02.md section 4.

Source vectors are ROWS and points are COLUMNS, so ideal relations live in the
LEFT kernel: c^T A = 0.

    --residues --prime P     one prime's 39 x 96 residue block (resumable)
    --reconstruct            signed CRT over the seven blocks -> the exact matrix
"""
import argparse, json, math, os, sys, time
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from wk8_s30_core import exps                                        # noqa: E402
from wk11_s69_circuit import Filling, sym_table                      # noqa: E402
from wk12_s74_dp import dp_eval_compact                              # noqa: E402

N, H, DEG = 4, 9, 13
N2_EXPECT, N1_EXPECT = 15, 4

# the six primes carried by P13.json, plus the seventh this session adds.
# Board section 1: six primes give 1.38x headroom over 2*H_13, which is too thin.
PRIMES6 = [2147483647, 2147483629, 2147483587, 2147483579, 2147483563, 2147483549]
P7 = 2147483543
PRIMES = PRIMES6 + [P7]

OUT = os.path.join(ROOT, "results", "b14_02")
SRC = os.path.join(ROOT, "results", "s74", "source.json")
PTS = os.path.join(ROOT, "results", "b14_prep", "points", "P13.json")

E4 = exps(N, H)                       # wk8_s30_core ordering: first exponent UP from 0
_A, _IDX, FACT, TAB = sym_table(N, H)
IU = E4.index(tuple([N] + [0] * (H - 1)))    # the u-letter (4,0^8); resolved by index()
T0 = time.time()


def log(*a):
    print(f"[{time.time()-T0:8.1f}s]", *a, flush=True)


# ------------------------------------------------------------------ height bound
def height_bound(delta=DEG, n2=N2_EXPECT, h=H, coeff_bound=7):
    """|F_T(f)| <= (h!)^2 * 2^n2 * M^delta,  M = max_alpha |alpha! c_alpha(l*c)|.

    Derived in the pre-registration section 4 from the Leibniz definition:
    (h!)^2 * 2^n2 signed terms, each a product of delta symbols."""
    best = 0
    def parts(k, maxp=None):
        if k == 0:
            yield ()
            return
        for first in range(min(k, maxp or k), 0, -1):
            for rest in parts(k - first, first):
                yield (first,) + rest
    for pa in parts(N):
        best = max(best, math.prod(math.factorial(x) for x in pa) * len(pa) * coeff_bound ** 2)
    return math.factorial(h) ** 2 * 2 ** n2 * best ** delta, best


# ------------------------------------------------------------------ objects
def climb_to(nat, top=DEG):
    """the source's own climb rule: each added degree contributes one fresh
    letter occupying N one-columns."""
    F = Filling.from_json(nat)
    assert F.delta <= top, (F.delta, top)
    one = list(F.one)
    nxt = F.delta
    for _ in range(top - F.delta):
        one += [nxt] * N
        nxt += 1
    return Filling(H, N, top, F.C1, F.C2, F.two, one)


def load_rows():
    src = json.load(open(SRC, encoding="utf-8"))
    ent = [e for e in src["entries"] if e["rung"] <= DEG]
    assert [e["index"] for e in ent] == list(range(len(ent))), "row order is not file order"
    assert len(ent) == 39, len(ent)
    rows = []
    for e in ent:
        F = climb_to(e["native"], DEG)
        assert (F.delta, F.n2, F.n1) == (DEG, N2_EXPECT, N1_EXPECT), (e["index"], F.delta, F.n2, F.n1)
        assert F.lam == (2 + F.n2 + F.n1, 2 + F.n2) + (2,) * (H - 2)
        rows.append(dict(index=e["index"], rung=e["rung"], exponent=DEG - e["rung"],
                         native=e["native"], up13=F.to_json(), F=F))
    return src, rows


def quartic_cv(pt, ce):
    """integer coefficient vector of f = l*c over exps(4,9), from the point's
    own cubic_exponents ordering (which is the REVERSE of exps(3,9))."""
    lin, cub = pt["linear"], pt["cubic_coefficients"]
    co = {}
    for al, cc in zip(ce, cub):
        if cc == 0:
            continue
        for i in range(H):
            if lin[i] == 0:
                continue
            a4 = list(al)
            a4[i] += 1
            k = tuple(a4)
            co[k] = co.get(k, 0) + lin[i] * cc
    return [int(co.get(al, 0)) for al in E4]


def load_points(role="primary"):
    P = json.load(open(PTS, encoding="utf-8"))
    ce = [tuple(x) for x in P["cubic_exponents"]]
    assert list(ce) == list(reversed(exps(3, H))), "cubic_exponents ordering changed"
    pts = [q for q in P["points"] if q["role"] == role]
    out = []
    for q in pts:
        cv = quartic_cv(q, ce)
        msym_int = [FACT[a] * cv[a] for a in range(len(E4))]
        u = msym_int[IU]
        assert u == q["u_symbol"], (q["id"], u, q["u_symbol"])
        m = max(abs(x) for x in msym_int)
        assert m == q["max_abs_quartic_symbol"], (q["id"], m, q["max_abs_quartic_symbol"])
        out.append(dict(id=q["id"], cv=cv, u=u, maxsym=m))
    return P, out


# ------------------------------------------------------------------ evaluation
_MS = _P = None


def _init(msyms, p):
    global _MS, _P
    _MS, _P = msyms, p


def _row(up13):
    F = Filling.from_json(up13)
    return [dp_eval_compact(F, ms, _P, TAB) for ms in _MS]


def residues(prime, workers, role="primary"):
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, f"residues_{role}_{prime}.json")
    src, rows = load_rows()
    P, pts = load_points(role)
    st = json.load(open(path, encoding="utf-8")) if os.path.exists(path) else dict(
        prime=prime, role=role, values_are=f"F_{{T_i^up13}}(f_j) mod {prime}; rows = source"
        " vectors (rung<=13, climbed to degree 13), columns = P13 points in file order",
        n_rows=len(rows), n_cols=len(pts), rows={}, secs=0.0)
    # u must be nonzero mod this prime in every column (control C5)
    uz = [q["id"] for q in pts if q["u"] % prime == 0]
    assert not uz, f"u-symbol vanishes mod {prime} at {uz}"
    st["u_mod_p"] = [q["u"] % prime for q in pts]
    msyms = [[(c % prime) * FACT[a] % prime for a, c in enumerate(q["cv"])] for q in pts]
    todo = [r for r in rows if str(r["index"]) not in st["rows"]]
    log(f"p={prime} role={role}: {len(st['rows'])} rows banked, {len(todo)} to do, {len(pts)} cols")
    if todo:
        t0 = time.time()
        with Pool(workers, initializer=_init, initargs=(msyms, prime)) as pool:
            for s in range(0, len(todo), workers * 2):
                chunk = todo[s:s + workers * 2]
                res = pool.map(_row, [r["up13"] for r in chunk], chunksize=1)
                for r, v in zip(chunk, res):
                    st["rows"][str(r["index"])] = v
                st["secs"] = round(st["secs"] + time.time() - t0, 1)
                t0 = time.time()
                json.dump(st, open(path + ".tmp", "w"), separators=(",", ":"))
                os.replace(path + ".tmp", path)
                log(f"p={prime} {role}: {len(st['rows'])}/{len(rows)} rows, {st['secs']:.0f}s")
    return st


# ------------------------------------------------------------------ signed CRT
def crt_pair(r1, m1, r2, m2):
    g, x, _ = _egcd(m1 % m2, m2)
    assert g == 1
    t = ((r2 - r1) % m2) * x % m2
    return r1 + m1 * t, m1 * m2


def _egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = _egcd(b, a % b)
    return g, y, x - (a // b) * y


def reconstruct(role="primary"):
    src, rows = load_rows()
    P, pts = load_points(role)
    H13, M = height_bound()
    blocks = {}
    for p in PRIMES:
        path = os.path.join(OUT, f"residues_{role}_{p}.json")
        assert os.path.exists(path), f"missing residue block for {p}"
        blocks[p] = json.load(open(path, encoding="utf-8"))
        assert len(blocks[p]["rows"]) == len(rows)
    mod = math.prod(PRIMES)
    assert mod > 2 * H13, (mod.bit_length(), (2 * H13).bit_length())
    log(f"modulus {mod.bit_length()} bits; 2*H13 {(2*H13).bit_length()} bits; "
        f"headroom {mod/(2*H13):.4g}")
    A, viol = [], []
    for r in rows:
        key = str(r["index"])
        out = []
        for j, q in enumerate(pts):
            acc, m = blocks[PRIMES[0]]["rows"][key][j] % PRIMES[0], PRIMES[0]
            for p in PRIMES[1:]:
                acc, m = crt_pair(acc, m, blocks[p]["rows"][key][j] % p, p)
            acc %= m
            v = acc - m if acc > m // 2 else acc            # symmetric range
            Hj = math.factorial(H) ** 2 * 2 ** N2_EXPECT * q["maxsym"] ** DEG
            if abs(v) > min(H13, Hj):
                viol.append(dict(row=r["index"], col=q["id"], bits=abs(v).bit_length()))
            for p in PRIMES:                                 # residues reproduce
                if v % p != blocks[p]["rows"][key][j] % p:
                    viol.append(dict(row=r["index"], col=q["id"], residue_mismatch=p))
            out.append(v)
        A.append(out)
    return A, rows, pts, H13, mod, viol


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--residues", action="store_true")
    ap.add_argument("--prime", type=int, default=PRIMES[0])
    ap.add_argument("--workers", type=int, default=2)
    ap.add_argument("--role", default="primary")
    ap.add_argument("--reconstruct", action="store_true")
    a = ap.parse_args(argv)
    os.makedirs(OUT, exist_ok=True)
    if a.residues:
        residues(a.prime, a.workers, a.role)
    if a.reconstruct:
        A, rows, pts, H13, mod, viol = reconstruct(a.role)
        assert not viol, viol[:6]
        payload = dict(
            values_are="exact integers F_{T_i^up13}(f_j) over Z, signed CRT over seven "
                       "primes in symmetric range; rows = the 39 source vectors of "
                       "results/s74/source.json with rung<=13 climbed to degree 13, in file "
                       "order; columns = the 96 role=='primary' points of P13.json in file "
                       "order. NO transform applied to the numbers.",
            transform="none", degree=DEG, n_rows=len(rows), n_cols=len(pts),
            primes=PRIMES, modulus=str(mod), height_bound=str(H13),
            height_bound_derivation="(9!)^2 * 2^15 * (24*7^2)^13, re-derived in "
                                    "results/PREREG_b14_02.md section 4",
            row_index=[r["index"] for r in rows], row_rung=[r["rung"] for r in rows],
            row_transport_exponent=[r["exponent"] for r in rows],
            col_id=[q["id"] for q in pts], col_u_symbol=[q["u"] for q in pts],
            col_max_abs_quartic_symbol=[q["maxsym"] for q in pts],
            A=[[str(x) for x in row] for row in A])
        path = os.path.join(OUT, f"A13_{a.role}.json")
        json.dump(payload, open(path, "w"), indent=0)
        nz = sum(1 for row in A for x in row if x)
        log(f"wrote {path}: {len(A)}x{len(A[0])}, {nz} nonzero, "
            f"max bits {max(abs(x).bit_length() for row in A for x in row)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

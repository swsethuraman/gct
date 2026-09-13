"""B15-01: exact audits and bounded construction of integral N14 members.

Uses the accepted CI73 independent evaluator; inherited code is unmodified.
New orchestration and construction: gpt-6-astra. S74/B14-07 inputs retain
their original attribution, including Claude Opus 5 source arithmetic.
"""
import argparse
from collections import Counter
import copy
from fractions import Fraction
import gzip
import hashlib
import json
import math
from pathlib import Path
import random
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results/b15_01"
sys.path.insert(0, str(ROOT / "tools/verify"))
import ci73_dimension as dim
import ci73_eval as ev
import ci73_linear as la
from flint import fmpz_mat, nmod_mat
import numpy as np

P = 2147483647
PRIMES = [P, 2147483629, 2147483587, 2147483579, 2147483563, 2147483549, 2147483543]
ev.CACHE = OUT / "cache"
START = time.monotonic()
STATS = Counter()
CALLS = 0


def read(name):
    p = ROOT / name
    raw = p.read_bytes()
    if p.suffix == ".gz":
        raw = gzip.decompress(raw)
    return json.loads(raw)


def save(name, data):
    OUT.mkdir(parents=True, exist_ok=True)
    p = OUT / name
    raw = (json.dumps(data, separators=(",", ":"), sort_keys=True) + "\n").encode()
    if p.suffix == ".gz":
        raw = gzip.compress(raw, mtime=0)
    tmp = p.with_suffix(p.suffix + ".tmp")
    tmp.write_bytes(raw)
    tmp.replace(p)


def log(message):
    print(f"[{time.monotonic()-START:.2f}s] {message}", flush=True)


def need(ok, message):
    if not ok:
        raise ValueError(message)


def verify_member(f, degree=14):
    f = ev.filling(f)
    need(f["h"] == 9 and len(f["two"]) == 15, "column shape")
    need(len(f["one"]) == 4 * degree - 48, "singleton shape")
    need(sorted(f["val"]) == [1] * degree + [3] * degree, "bidegree")
    return f


def evaluate(f, symbols, prime=P, name="value"):
    global CALLS
    t = time.monotonic()
    plan = ev.plan(json.dumps(ev.filling(f), sort_keys=True))
    STATS["planning_seconds"] += time.monotonic() - t
    unit = plan["peak_states_pair"] * (8 if prime else 32)
    batch = min(48, max(1, 380_000_000 // max(1, unit)))
    need(unit <= 380_000_000, "single point exceeds array budget")
    result = []
    for offset in range(0, len(symbols), batch):
        CALLS += 1
        vals, receipt = ev.evaluate(f, symbols[offset:offset+batch], prime,
                                   name=f"b15_01_{name}_{CALLS}", seconds=100)
        result.extend(vals)
        STATS["evaluation_seconds"] += receipt["wall_seconds"]
        STATS["evaluated_entries"] += len(vals)
        STATS["max_array_bytes"] = max(STATS["max_array_bytes"], receipt["peak_array_bytes"])
    return result


class Basis:
    def __init__(self, prime=P):
        self.p = prime
        self.rows = []
        self.pivots = []

    def add(self, row):
        t = time.monotonic()
        a = np.array([int(x) % self.p for x in row], dtype=np.int64)
        for j, b in zip(self.pivots, self.rows):
            if a[j]:
                a = (a - int(a[j]) * b) % self.p
        nz = np.flatnonzero(a)
        if len(nz):
            j = int(nz[0])
            a = a * pow(int(a[j]), -1, self.p) % self.p
            self.pivots.append(j)
            self.rows.append(a)
        STATS["reduction_seconds"] += time.monotonic() - t
        return bool(len(nz))


def inputs():
    names = ["analysis/b14_07_source14.py", "analysis/b14_07_kernel.py",
             "results/b14_07/K14.json", "results/b14_07/A14_exact.json.gz",
             "results/b14_04/hpad14.json", "results/b14_04/hpad14_power.json.gz",
             "results/b15_prep/degree14_target_seed88.json", "results/ci73/certificate.json",
             "docs/ci73_proof.md", "results/s74/source.json", "results/b14_prep/points/P14.json",
             "tools/verify/ci73_eval.py",
             "tools/verify/ci73_backend.cs", "tools/verify/ci73_dimension.py",
             "tools/verify/ci73_linear.py", "docs/batch15/ACCEPTED_STATE.md",
             "results/integrate/inherited_exclusions.json", "results/b15_prep/transport_overlay.json"]
    save("input_hashes.json", {n: hashlib.sha256((ROOT/n).read_bytes()).hexdigest() for n in names})


def controls():
    rng = random.Random(150100)
    ce = ev.exps(3, 3)
    pts = [dict(linear=[rng.randint(-4, 4) for _ in range(3)],
                cubic_coefficients=[rng.randint(-4, 4) for _ in ce]) for _ in range(5)]
    symbols = [ev.mixed_symbols(pt, ce) for pt in pts]
    records = []
    for attempt in range(500):
        letters = [0, 1, 2] + [x for x in range(3, 6) for _ in range(3)]
        rng.shuffle(letters)
        f = dict(h=3, val=[1]*3+[3]*3, C1=letters[:3], C2=letters[3:6],
                 two=[letters[6:8], letters[8:10]], one=letters[10:])
        try:
            ev.filling(f)
        except ValueError:
            continue
        values = [ev.literal(f, s) for s in symbols]
        if not any(values):
            continue
        for p in [0, P, PRIMES[1]]:
            need(evaluate(f, symbols, p, "control") == [x % p if p else x for x in values], "literal liveness")
        bad = copy.deepcopy(f)
        bad["C1"][:2] = reversed(bad["C1"][:2])
        need(evaluate(bad, symbols, 0, "sign") == [-x for x in values], "column sign mutation")
        wrong = copy.deepcopy(symbols)
        for s in wrong:
            s[3] = {a: v // math.prod(math.factorial(i) for i in a) for a, v in s[3].items()}
        need(evaluate(f, wrong, 0, "factorial") != values, "factorial defect undetected")
        altered = copy.deepcopy(symbols)
        altered[0][1] = {a: 2*v for a, v in altered[0][1].items()}
        got = evaluate(f, altered, 0, "point")
        need(got[0] == 8*values[0] and got[1:] == values[1:], "point homogeneity defect")
        records.append(dict(filling=f, exact_values=values))
        if len(records) == 3:
            break
    need(len(records) == 3, "insufficient live controls")
    # A separate quartic control has an elementary nonzero exact value.
    f = dict(h=2, val=[4, 4], C1=[0, 1], C2=[0, 1], two=[], one=[0, 0, 1, 1])
    q = {4:{a: (1+sum((j+1)*v for j, v in enumerate(a)))*math.prod(math.factorial(v) for v in a)
            for a in ev.exps(4, 2)}}
    value = ev.literal(f, q)
    need(value != 0, "quartic liveness zero")
    need(evaluate(f, [q], 0, "quartic") == [value], "quartic literal")
    save("controls.json", dict(status="EXACT", points=pts, cubic_exponents=ce,
         records=records, quartic=dict(filling=f, symbols=[[list(a),v] for a,v in q[4].items()], value=value),
         column_sign_checked=True, factorial_defect_rejected=True, point_scaling_checked=True,
         comparisons=3*5*3+1))
    log("literal mixed/quartic liveness and altered sign/factorial/point controls PASS")


def audit():
    inputs()
    controls()
    t = time.monotonic()
    dim.selfcheck_rim()
    power = dim.cubic_exact(14)[14]
    mods = {p:dim.modular_newton(14, p, cubic_outer=True)[14] for p in PRIMES[:2]}
    cert = read("results/b14_04/hpad14.json")
    h = dim.check_hpad(14, power, mods, cert, read("results/b14_04/hpad14_power.json.gz"))
    save("dimension.json", dict(status="EXACT", h= h, degree=14, n=4, variables=9,
         partition=cert["lambda"], channels=cert["rows"], classes=len(power),
         method="fresh exact Newton and outer-rim MN; complete Pieri enumeration", seconds=time.monotonic()-t))
    log(f"independent full target dimension {h}, {len(power)} power classes")
    # Ambient dimension is independently recomputed, not inferred from ranks.
    t = time.monotonic()
    apower = dim.power_plethysm(4, 14)
    a = sum(c*dim.character(tuple(cert["lambda"]), rho) for rho,c in apower.items())
    need(a.denominator == 1 and a == 93, "ambient dimension mismatch")
    dim.character.cache_clear()
    save("ambient.json", dict(status="EXACT", a= int(a), classes=len(apower),
         method="fresh exact Newton h14[h4] and outer-rim MN", seconds=time.monotonic()-t))
    log(f"independent source ambient dimension {a}")
    src = read("results/s74/source.json")["entries"][:93]
    old = read("results/b14_07/A14_exact.json.gz")
    A = [[int(x) for x in row] for row in old["matrix"]]
    kj = read("results/b14_07/K14.json")
    K = fmpz_mat([[c[i] for c in kj["kernel_columns"]] for i in range(93)])
    AZ = fmpz_mat(A)
    need(K.rank() == 5 and (AZ.transpose()*K).is_zero(), "exact kernel")
    seed = read("results/b15_prep/degree14_target_seed88.json")
    indices = seed["source_indices_zero_based"]
    cols = seed["minor_point_indices"]
    need(len(indices) == len(cols) == 88, "seed dimensions")
    determinant = fmpz_mat([[A[i][j] for j in cols] for i in indices]).det()
    need(str(determinant) == seed["exact_minor_determinant"] and determinant != 0, "seed exact minor")
    need(seed["exact_values"] == [[str(x) for x in A[i][:192]] for i in indices], "seed source values")
    for j, i in enumerate(indices):
        need(seed["source_native_definitions"][j] == src[i]["native"], "native seed definition")
        need(seed["exponents"][j] == 14-src[i]["rung"], "seed exponent")
    for i, e in enumerate(src):
        f = ev.native_source(e, 14)
        need(len(f["two"]) == 15 and len(f["one"]) == 8 and f["h"] == 9, "source shape")
        need(e["index"] == i and old["rows"][i]["index"] == i, "source indexing")
    ci = read("results/ci73/certificate.json")
    small = [[Fraction(ci["kernel"]["entries"][i][j])*Fraction(ci["source_rows"][i]["scale"])
              for j in range(3)] for i in range(39)]
    padded = [[int(v) for v in r] for r in small] + [[0]*3 for _ in range(54)]
    need(all(x.denominator == 1 for r in small for x in r), "integer effective degree13 kernel")
    oldK = fmpz_mat(padded)
    need(oldK.rank() == 3 and (AZ.transpose()*oldK).is_zero(), "degree13 inclusion")
    combined = fmpz_mat([[int(K[i,j]) for j in range(5)] + padded[i] for i in range(93)])
    need(combined.rank() == 5, "degree13 span inclusion")
    bad = fmpz_mat(K)
    bad[0, 0] += 1
    need(not (AZ.transpose()*bad).is_zero(), "kernel alteration undetected")
    points = read("results/b14_prep/points/P14.json")
    ce = points["cubic_exponents"]
    qsymbols = [{4:ev.quartic_symbols(pt, ce)} for pt in points["points"]]
    need(max(abs(v) for s in qsymbols for v in s[4].values()) <= 1176, "source height coefficient")
    H = 2**15 * math.factorial(9)**2 * 1176**14
    M = math.prod(PRIMES)
    need(M > 2*H and 2**256 > 2*H and all(abs(x) <= H for row in A for x in row), "signed bounds")
    fresh = []
    for i in [0, 15, 39, 92]:
        values = evaluate(ev.native_source(src[i],14), qsymbols[:3], 0, "source_audit")
        need(values == A[i][:3], "fresh exact source mismatch")
        fresh.append(dict(source_index=i, point_indices=[0,1,2], values=[str(v) for v in values]))
        log(f"fresh exact degree14 source {i} agrees on three points")
    save("source_audit.json", dict(status="EXACT", source_ambient_dimension=93,
         stored_matrix_rank=88, stored_kernel_rank=5, stored_primary_and_holdout_identities=1060,
         first39_degree13_rank=3, combined_kernel_rank=5, kernel_defect_rejected=True,
         seed_members=indices, seed_minor_columns=cols, seed_minor_determinant=str(determinant),
         integer_bound=str(H), crt_modulus=str(M), crt_signed_margin=str(M-2*H),
         integer_modulus=str(2**256), integer_signed_margin=str(2**256-2*H),
         fresh_values=fresh, fresh_source_entries=12,
         source_basis_independence="inherited S74; generic 93-minor not replayed by this audit",
         scope="stored exact matrix identities; only the listed 12 entries have fresh geometric replay"))
    save("audit_summary.json", dict(status="EXACT", wall_seconds=time.monotonic()-START, stats=STATS,
         dimension=159, ambient=93, source_rank=88, kernel_rank=5, model="gpt-6-astra"))
    log("audit PASS")


def lift13(f):
    f = copy.deepcopy(verify_member(f,13))
    d = len(f["val"])
    f["val"] += [1,3]
    f["one"] += [d,d+1,d+1,d+1]
    return verify_member(f)


def moves(f):
    """Finite one-occurrence exchanges with the new cubic singleton letter.

    Column order is part of the definition. Valences are preserved exactly.
    Exhaustiveness is asserted only for this enumerated finite move list.
    """
    new = len(f["val"])-1
    for kind, number, col in [("C1",-1,f["C1"]),("C2",-1,f["C2"])]+[("two",j,c) for j,c in enumerate(f["two"])]:
        for pos, old in enumerate(col):
            if f["val"][old] != 3 or new in col:
                continue
            g = copy.deepcopy(f)
            (g[kind] if number == -1 else g[kind][number])[pos] = new
            g["one"][g["one"].index(new)] = old
            yield dict(kind=kind,column=number,position=pos,old=old,new=new), verify_member(g)


def pilot(seconds, resume=False):
    need(read("results/b15_01/audit_summary.json")["dimension"] == 159, "audit gate")
    inputs()
    pts = read("results/b14_prep/points/P14.json")
    points = pts["points"][:192]
    ce = pts["cubic_exponents"]
    symbols = [ev.mixed_symbols(pt, ce) for pt in points]
    factor = [s[1][(1,)+(0,)*8]*s[3][(3,)+(0,)*8] % P for s in symbols]
    seed = read("results/b15_prep/degree14_target_seed88.json")
    basis = Basis()
    members = [dict(kind="source_pullback",source_index=i,degree=14) for i in seed["source_indices_zero_based"]]
    rows = [[int(x)%P for x in row] for row in seed["exact_values"]]
    for row in rows:
        need(basis.add(row), "seed88 dependent")
    c13 = [m["filling"] for m in read("results/ci73/certificate.json")["target_members"] if m["kind"] == "mixed_bracket"]
    all_lifted = [lift13(f) for f in c13]
    candidates = [(dict(phase="transport",degree13_member=i), f) for i,f in enumerate(all_lifted)]
    # Interleave positions across the 72 parents, rather than exhaust one parent.
    move_lists = [list(moves(f)) for f in all_lifted]
    for j in range(max(map(len, move_lists))):
        for i, entries in enumerate(move_lists):
            if j < len(entries):
                change, f = entries[j]
                candidates.append((dict(phase="exchange",degree13_member=i,move=change), f))
    log(f"candidate construction: {len(candidates)} finite members; initial rank88")
    tested = []
    next_index = 0
    if resume:
        prev = read("results/b15_01/pilot.json")
        members = prev["members"]
        rows = prev["rows_mod_p"]
        tested = prev["tested"]
        next_index = prev["next_candidate_index"]
        basis = Basis()
        for row in rows:
            need(basis.add(row), "resume basis")
    begun = time.monotonic()
    def checkpoint(reason):
        save("pilot.json", dict(status="CANDIDATE", reason=reason, prime=P,
             degree=14, variables=9, partition=[25,17]+[2]*7,
             point_indices=list(range(192)), point_ids=[pt["id"] for pt in points],
             point_source="results/b14_prep/points/P14.json", members=members,rows_mod_p=rows,
             rank_mod_p=len(rows), pivot_columns=basis.pivots, next_candidate_index=next_index,
             candidate_count=len(candidates), tested=tested, stats=STATS,
             wall_seconds=time.monotonic()-begun,
             seed_scope="stored B14-07 values; added mixed rows freshly evaluated",
             evaluation="integral initial-column brackets; singleton lift factor ell0*m300(c)=u/4",
             completeness=False, new_global_kernel_lb=0, inherited_global_kernel_lb=3))
    checkpoint("RUNNING")
    for idx in range(next_index, len(candidates)):
        if time.monotonic()-begun > seconds-25:
            break
        desc, f = candidates[idx]
        t = time.monotonic()
        if desc["phase"] == "transport":
            native = c13[desc["degree13_member"]]
            values = evaluate(native,symbols,P,"transport")
            values = [v*x % P for v,x in zip(values,factor)]
        else:
            values = evaluate(f,symbols,P,"exchange")
        gain = basis.add(values)
        cost = time.monotonic()-t
        tested.append(dict(index=idx,definition=desc,seconds=cost,nonzero=any(values),added=gain,rank=len(basis.rows)))
        next_index = idx+1
        if gain:
            members.append(dict(kind="mixed_bracket",filling=f,construction=desc))
            rows.append(values)
            log(f"rank {len(rows)}/159 after candidate {idx}: {desc['phase']}, {cost:.2f}s")
        elif idx % 8 == 0:
            log(f"candidate {idx}, rank {len(rows)}, {cost:.2f}s")
        checkpoint("RUNNING")
        if len(rows) == 159:
            break
        need(len(rows) < 159, "rank exceeds proved dimension")
    checkpoint("FULL_RANK" if len(rows)==159 else "BOUNDED_PILOT_STOP")
    log(f"finished rank {len(rows)}/159; tested={len(tested)}; seconds={time.monotonic()-begun:.2f}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["audit","pilot"])
    ap.add_argument("--seconds", type=int, default=850)
    ap.add_argument("--resume", action="store_true")
    args = ap.parse_args()
    if args.mode == "audit":
        audit()
    else:
        pilot(args.seconds,args.resume)

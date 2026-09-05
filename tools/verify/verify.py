#!/usr/bin/env python3
"""The independent two-layer verifier (session 49).

    python3 tools/verify/verify.py <cert.json | cert.json.gz | directory> ...
                                   [--report out.md] [--quiet]

Reads certificates in the declared format (tools/verify/FORMAT.md), refuses
anything it cannot parse -- an unknown key, a missing key, a wrong type, a
non-canonical term -- with the reason, and never guesses.  Layer 1 (layer1.py)
recomputes ranks over Q and modulo primes, minors over Z and nullity-zero
claims on serialised integer matrices.  Layer 2 (layer2.py) checks that the
recorded object is the object claimed: weights, raising operators over Z (or
modulo the recorded prime, reported as such), the ambient multiplicity by an
independent plethysm, (star) support, and evaluation points rebuilt from their
substitution data.  This directory imports nothing from analysis/ and
duplicates none of its code.

Exit status 0 iff every certificate parsed and passed.
"""
import sys, os, json, gzip, time, traceback

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from layer1 import check_matrix_certificate          # noqa: E402
from layer2 import check_hwv_certificate, check_full_rank_certificate  # noqa: E402
from points import FAMILIES                          # noqa: E402

FORMAT = "gct-cert/1"
CONVENTIONS = {
    "coefficient": "c_alpha(F) = coefficient of s^alpha in F",
    "raising": "E_ij c_alpha = (alpha_i + 1) c_{alpha + e_i - e_j}",
}


class Unparseable(Exception):
    pass


def _need(d, keys, allowed=None, where="certificate"):
    if not isinstance(d, dict):
        raise Unparseable(f"{where}: expected an object")
    missing = [k for k in keys if k not in d]
    if missing:
        raise Unparseable(f"{where}: missing key(s) {missing}")
    extra = [k for k in d if k not in (allowed if allowed is not None else keys)]
    if extra:
        raise Unparseable(f"{where}: unknown key(s) {extra}")


def _int(x, where):
    if not isinstance(x, int) or isinstance(x, bool):
        raise Unparseable(f"{where}: expected an integer")
    return x


def _check_cell(cell):
    _need(cell, ["n", "r", "lambda", "delta", "a"], where="cell")
    for k in ("n", "r", "delta", "a"):
        _int(cell[k], f"cell.{k}")
    if not (isinstance(cell["lambda"], list) and cell["lambda"]
            and all(isinstance(x, int) and not isinstance(x, bool) for x in cell["lambda"])):
        raise Unparseable("cell.lambda: expected a nonempty list of integers")


def _check_conventions(conv):
    _need(conv, ["coefficient", "raising"], where="conventions")
    for k, v in CONVENTIONS.items():
        if conv[k] != v:
            raise Unparseable(f"conventions.{k}: must read exactly {v!r}, got {conv[k]!r}")


def _check_points(pts, where):
    if not isinstance(pts, list) or not pts:
        raise Unparseable(f"{where}: expected a nonempty list of points")
    for pt in pts:
        if not (isinstance(pt, dict) and "type" in pt):
            raise Unparseable(f"{where}: point without a type")


def validate(cert):
    """Strict schema check; raises Unparseable."""
    _need(cert, ["format", "kind", "title", "produced_by"],
          allowed=["format", "kind", "title", "produced_by", "notes", "cell", "conventions",
                   "modulus", "vectors", "claims", "matrix", "matrix_source", "claimed_rank_Q",
                   "claimed_ranks_mod_p", "nonvanishing_minor", "nullity_zero", "prime",
                   "variety", "points", "basis"])
    if cert["format"] != FORMAT:
        raise Unparseable(f"format: expected {FORMAT!r}")
    kind = cert["kind"]
    if "notes" in cert and not isinstance(cert["notes"], str):
        raise Unparseable("notes: expected a string")
    base = {"format", "kind", "title", "produced_by", "notes"}
    if kind == "hwv":
        _need(cert, ["cell", "conventions", "modulus", "vectors", "claims"],
              allowed=list(base | {"cell", "conventions", "modulus", "vectors", "claims"}))
        _check_cell(cert["cell"])
        _check_conventions(cert["conventions"])
        if cert["modulus"] is not None:
            m = _int(cert["modulus"], "modulus")
            if m < 3:
                raise Unparseable("modulus: expected a prime >= 3")
        if not (isinstance(cert["vectors"], list) and cert["vectors"]):
            raise Unparseable("vectors: expected a nonempty list")
        cl = cert["claims"]
        _need(cl, [], allowed=["independent", "star_support", "vanishes_at", "nonvanishing_at",
                               "fresh_points"], where="claims")
        if "independent" in cl and not isinstance(cl["independent"], bool):
            raise Unparseable("claims.independent: expected true/false")
        if "star_support" in cl:
            _need(cl["star_support"], ["k"], where="claims.star_support")
            if _int(cl["star_support"]["k"], "claims.star_support.k") < 1:
                raise Unparseable("claims.star_support.k: expected k >= 1")
        for key in ("vanishes_at", "nonvanishing_at"):
            if key in cl:
                _check_points(cl[key], f"claims.{key}")
        if "fresh_points" in cl:
            fp = cl["fresh_points"]
            _need(fp, ["seed", "count"], allowed=["seed", "count", "vanishes_on", "nonvanishing_on"],
                  where="claims.fresh_points")
            _int(fp["seed"], "claims.fresh_points.seed")
            if _int(fp["count"], "claims.fresh_points.count") < 1:
                raise Unparseable("claims.fresh_points.count: expected >= 1")
            for key in ("vanishes_on", "nonvanishing_on"):
                fams = fp.get(key, [])
                if not isinstance(fams, list) or any(f not in FAMILIES for f in fams):
                    raise Unparseable(f"claims.fresh_points.{key}: families must be among {FAMILIES}")
    elif kind == "matrix":
        _need(cert, [], allowed=list(base | {"matrix", "matrix_source", "claimed_rank_Q",
                                             "claimed_ranks_mod_p", "nonvanishing_minor", "nullity_zero"}))
        if "matrix" not in cert and "matrix_source" not in cert:
            raise Unparseable("matrix certificate needs a matrix or a matrix_source")
        if "claimed_rank_Q" in cert:
            _int(cert["claimed_rank_Q"], "claimed_rank_Q")
        if "claimed_ranks_mod_p" in cert:
            d = cert["claimed_ranks_mod_p"]
            if not isinstance(d, dict) or not d:
                raise Unparseable("claimed_ranks_mod_p: expected a nonempty object prime -> rank")
            for k, v in d.items():
                if not (isinstance(k, str) and k.isdigit() and int(k) >= 3):
                    raise Unparseable("claimed_ranks_mod_p: keys must be decimal primes")
                _int(v, "claimed_ranks_mod_p value")
        if "nonvanishing_minor" in cert:
            _need(cert["nonvanishing_minor"], ["rows", "cols"], where="nonvanishing_minor")
        if "nullity_zero" in cert:
            _need(cert["nullity_zero"], ["prime"], where="nullity_zero")
            _int(cert["nullity_zero"]["prime"], "nullity_zero.prime")
        if not any(k in cert for k in ("claimed_rank_Q", "claimed_ranks_mod_p", "nonvanishing_minor", "nullity_zero")):
            raise Unparseable("matrix certificate makes no claim")
    elif kind == "full_rank":
        _need(cert, ["cell", "conventions", "prime", "variety", "points", "basis"],
              allowed=list(base | {"cell", "conventions", "prime", "variety", "points", "basis"}))
        _check_cell(cert["cell"])
        _check_conventions(cert["conventions"])
        if _int(cert["prime"], "prime") < 3:
            raise Unparseable("prime: expected a prime >= 3")
        if cert["variety"] not in ("det_pencil", "padded_permanent", "reducible"):
            raise Unparseable("variety: expected det_pencil, padded_permanent or reducible")
        _check_points(cert["points"], "points")
        if cert["basis"] is not None and not (isinstance(cert["basis"], list) and cert["basis"]):
            raise Unparseable("basis: expected null or a nonempty list of vectors")
    else:
        raise Unparseable(f"kind: unknown kind {kind!r}")
    return kind


def load(path):
    if path.endswith(".gz"):
        with gzip.open(path, "rt", encoding="utf-8") as f:
            return json.load(f)
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def verify_file(path):
    """Returns (status, log): status in PASS / FAIL / UNPARSEABLE / ERROR."""
    log = []
    try:
        cert = load(path)
    except Exception as e:                       # noqa: BLE001
        return "UNPARSEABLE", [("read/parse JSON", False, str(e))]
    try:
        kind = validate(cert)
    except Unparseable as e:
        return "UNPARSEABLE", [("schema", False, str(e))]
    try:
        if kind == "hwv":
            ok = check_hwv_certificate(cert, log)
        elif kind == "matrix":
            ok = check_matrix_certificate(cert, log)
        else:
            ok = check_full_rank_certificate(cert, log)
    except ValueError as e:                      # malformed content found while checking
        return "UNPARSEABLE", log + [("content", False, str(e))]
    except Exception as e:                       # noqa: BLE001
        return "ERROR", log + [("internal error", False, f"{e!r}\n{traceback.format_exc()}")]
    return ("PASS" if ok else "FAIL"), log


def collect(paths):
    out = []
    for p in paths:
        if os.path.isdir(p):
            for fn in sorted(os.listdir(p)):
                if fn.endswith(".json") or fn.endswith(".json.gz"):
                    out.append(os.path.join(p, fn))
        else:
            out.append(p)
    return out


def main(argv):
    report = None
    quiet = False
    paths = []
    i = 0
    while i < len(argv):
        if argv[i] == "--report":
            report = argv[i + 1]
            i += 2
        elif argv[i] == "--quiet":
            quiet = True
            i += 1
        else:
            paths.append(argv[i])
            i += 1
    files = collect(paths)
    if not files:
        print(__doc__)
        return 2
    lines = ["# Verifier report", "", f"{len(files)} certificate file(s); verifier tools/verify at "
             f"{time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}", ""]
    summary = {"PASS": 0, "FAIL": 0, "UNPARSEABLE": 0, "ERROR": 0}
    for path in files:
        t0 = time.time()
        status, log = verify_file(path)
        summary[status] += 1
        title = ""
        try:
            title = load(path).get("title", "")
        except Exception:                        # noqa: BLE001
            pass
        head = f"{status:11s} {os.path.relpath(path)}  ({time.time()-t0:.1f}s)  {title}"
        print(head, flush=True)
        lines.append(f"## {status} — `{os.path.relpath(path)}`")
        lines.append("")
        if title:
            lines.append(f"*{title}*  ({time.time()-t0:.1f}s)")
            lines.append("")
        for name, ok, detail in log:
            mark = "ok  " if ok else "FAIL"
            if not quiet or not ok:
                print(f"    [{mark}] {name}" + (f" — {detail}" if detail else ""), flush=True)
            lines.append(f"- [{'x' if ok else ' '}] {name}" + (f" — {detail}" if detail else ""))
        lines.append("")
    tail = (f"PASS {summary['PASS']}, FAIL {summary['FAIL']}, UNPARSEABLE {summary['UNPARSEABLE']}, "
            f"ERROR {summary['ERROR']}")
    print(tail)
    lines.insert(3, tail)
    if report:
        with open(report, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
    return 0 if (summary["FAIL"] == summary["UNPARSEABLE"] == summary["ERROR"] == 0) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

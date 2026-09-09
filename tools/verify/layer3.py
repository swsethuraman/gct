"""Layer 3 -- the sparse-route ("sparse_nullity") certificate checker (session 67).

A sparse-route claim is `mult_X(lambda, delta) = a`, proved by
`nullity_p([E; ev_X]) = 0` at a single prime: since `rank_p <= rank_Q`,
`a - nullity_p([E; ev]) <= mult_X <= a`, so a zero nullity mod p forces
mult_X = a over Q (docs/sparse_det_route.md, Lemmas 1-2).  The original run
decided the nullity by the session-42 Wiedemann certificate; this checker
RE-DERIVES it independently:

  * it rebuilds E (the stacked simple raising operators on the full weight-lambda
    space) and the evaluation rows ev at the recorded points, in tools/verify's
    own code (chi_build.py), importing nothing from analysis/ and NOT using the
    stabiliser reduction the original run used -- so the re-derivation is also an
    independent check of that reduction;
  * it decides nullity_p([E; ev]) itself: an exact flint rank for cells small
    enough to densify, else its own preconditioned Wiedemann (wied_check.c).

The certificate records the recipe (seeds/levels/points as substitution data) so
the run is reproducible; the checker does not trust the recorded verdict, it
recomputes it.  The FIELD is declared and enforced (Part A4): a finite-field
full-column-rank certificate concludes characteristic zero, a finite-field
*kernel* does not.

Soundness of the build is anchored by `check_build_kernel` (nullity_p(E) = a):
E's kernel is the highest-weight space, of dimension the plethysm value a, so a
correct build has nullity_p(E) = a exactly; the back-fill validates this by an
exact flint rank on a spread of cells before trusting the Wiedemann path.
"""
import os, sys, time, subprocess, tempfile
import numpy as np
from scipy import sparse
from flint import nmod_mat

HERE = os.path.dirname(os.path.abspath(__file__))
import chi_build
from pleth import ambient_multiplicity

HOUSE_PRIMES = (2147483647, 2147483629)
WIED = os.path.join(HERE, "wied_check")
WORK = os.environ.get("VERIFY_WORK", tempfile.gettempdir())
DENSE_CAP = int(os.environ.get("VERIFY_DENSE_CAP", "2200"))     # N_S below which an exact flint rank is used (dense is memory-heavy: it holds a ~3*N_S x N_S array); above it the memory-light Wiedemann decides the nullity
VERIFY_MAX_NS = int(os.environ.get("VERIFY_MAX_NS", "80000"))   # above this, re-derivation is skipped this run


def _rec(log, name, ok, detail=""):
    log.append((name, bool(ok), detail))
    return bool(ok)


def build_bin():
    src = os.path.join(HERE, "wied_check.c")
    if not os.path.exists(WIED) or os.path.getmtime(WIED) < os.path.getmtime(src):
        subprocess.check_call(["gcc", "-O3", "-march=native", "-o", WIED, src])


def _nullity_dense(F, p):
    """exact nullity_p of a scipy CSR F, by densifying and one flint rank."""
    F = sparse.csr_matrix(F)
    m, n = F.shape
    if m == 0:
        return n
    D = np.zeros((m, n), dtype=np.int64)
    coo = F.tocoo()
    D[coo.row, coo.col] = coo.data % p
    return n - nmod_mat(m, n, D.ravel().tolist(), p).rank()


def _write_csr(F, p, path):
    F = sparse.csr_matrix(F); F.sort_indices()
    nrows, nc = F.shape
    with open(path, "wb") as f:
        np.array([nc, nrows, int(F.indptr[-1])], dtype=np.int64).tofile(f)
        F.indptr.astype(np.int64).tofile(f)
        F.indices.astype(np.int32).tofile(f)
        (F.data % p).astype(np.uint32).tofile(f)
    return nrows, int(F.indptr[-1])


def _wied(F, p, seed, k_extra):
    """run the verifier's Wiedemann on F = [given rows; k_extra random rows];
    returns ('NONSINGULAR'|'KERNEL'|'INCONCLUSIVE', payload)."""
    build_bin()
    os.makedirs(WORK, exist_ok=True)
    path = os.path.join(WORK, f"vchk_{p}_{os.getpid()}_{seed}.csr")
    try:
        _write_csr(F, p, path)
        out = subprocess.run([WIED, path, str(p), str(seed), str(k_extra)],
                             capture_output=True, text=True)
        if out.returncode != 0:
            raise RuntimeError(("wied_check failed", out.returncode, out.stderr[-300:]))
        status, payload = None, None
        for line in out.stdout.splitlines():
            if line.startswith("NONSINGULAR"): status = "NONSINGULAR"; payload = line
            elif line.startswith("KERNEL"): status = "KERNEL"; payload = [int(x) for x in line.split()[1:]]
            elif line.startswith("INCONCLUSIVE"): status = "INCONCLUSIVE"; payload = line
        if status is None:
            raise RuntimeError(("wied_check: no verdict", out.stdout[-200:]))
        return status, payload
    finally:
        try: os.remove(path)
        except OSError: pass


def _wied_full_col_rank(F, p, nc, tries=6, seed0=1):
    """decide nullity_p(F) == 0 (full column rank) by Wiedemann; retries on an
    inconclusive run (randomness only affects conclusiveness).  Returns
    (is_full_rank, note)."""
    for t in range(tries):
        st, payload = _wied(F, p, seed0 + t, 0)
        if st == "NONSINGULAR":
            return True, f"NONSINGULAR (seed {seed0 + t})"
        if st == "KERNEL":
            # verify the kernel vector against F, then it is a genuine nullity
            y = np.array(payload, dtype=np.int64) % p
            r = _spmv(F, y, p)
            if not np.any(r):
                return False, f"kernel vector found and verified (nullity >= 1, seed {seed0 + t})"
            # spurious compressed kernel should not happen (no compression here); retry
        # INCONCLUSIVE: retry with a fresh seed
    return None, "inconclusive after retries"


def _spmv(F, y, p):
    F = sparse.csr_matrix(F)
    d = (F.data % p).astype(np.int64)
    Flo = sparse.csr_matrix((d & 0xFFFF, F.indices, F.indptr), shape=F.shape)
    Fhi = sparse.csr_matrix((d >> 16, F.indices, F.indptr), shape=F.shape)
    yv = np.asarray(y, dtype=np.int64) % p
    return ((Flo @ (yv & 0xFFFF)) % p + ((Flo @ (yv >> 16)) % p + (Fhi @ (yv & 0xFFFF)) % p) % p * 65536
            + (Fhi @ (yv >> 16)) % p * ((65536 * 65536) % p)) % p


def check_build_kernel(E, a, p, nc, dense_cap=DENSE_CAP):
    """confirm nullity_p(E) == a (E's kernel is the a-dimensional highest-weight
    space).  Exact where affordable, else the two-sided Wiedemann test
    {[E; R_{a-1}] singular, [E; R_a] nonsingular}."""
    if nc <= dense_cap:
        k = _nullity_dense(E, p)
        return k == a, f"nullity_p(E) = {k} (exact), a = {a}"
    # nullity <= a : [E; R_a] nonsingular
    up, _ = _wied(E if a == 0 else _stack_random(E, a, p, 7001), p, 11, 0) if a == 0 else _wied(E, p, 11, a)
    up_ok = (up == "NONSINGULAR")
    if a == 0:
        return up_ok, "a = 0: [E] nonsingular" if up_ok else "a=0 but E singular"
    # nullity >= a : [E; R_{a-1}] singular (has a kernel)
    st, _ = _wied(E, p, 23, a - 1)
    lo_ok = (st == "KERNEL")
    return (up_ok and lo_ok), f"nullity_p(E): [E;R_{a}] {'nonsingular' if up_ok else up}, [E;R_{a-1}] {'singular' if lo_ok else st} -> ={a}? {up_ok and lo_ok}"


def _stack_random(E, k, p, seed):
    rng = np.random.default_rng(seed)
    nc = E.shape[1]
    Rr = sparse.csr_matrix(rng.integers(0, p, size=(k, nc), dtype=np.int64))
    return sparse.vstack([E, Rr]).tocsr()


def parse_field(field):
    """'Q' -> ('Q', None); 'F_<p>' -> ('Fp', p).  Raises ValueError otherwise."""
    if field == "Q":
        return "Q", None
    if isinstance(field, str) and field.startswith("F_") and field[2:].isdigit():
        return "Fp", int(field[2:])
    raise ValueError(f"field must be 'Q' or 'F_<p>', got {field!r}")


def sparse_nullity_view(cert):
    """The three dialect-sensitive fields of a sparse_nullity certificate, read
    from whichever spelling the certificate uses.

    TWO DIALECTS exist, written independently -- session 67's
    (field / nullity / recipe) and session 73's (prime / claim.nullity /
    reduction) -- because s73 branched before s67's tree was merged.  The schema
    layer in verify.py has accepted both since the batch-11 merge; THIS layer did
    not, and read cert["field"] unconditionally, so every s73-dialect certificate
    passed schema validation and then died with KeyError('field') in
    re-derivation.  Schema validation is not re-derivation, and the merge-time
    pass was the former.  Found by tools/verify/sample_corpus.py on its first
    stratified draw; the defect is the integrator's, introduced by extending one
    layer of the reconciliation and not the other.

    Returns (field_string, nullity, recorded_N_S_or_None).  No check is
    weakened: the finite-field discipline, the nonnegative nullity and the
    recorded-size guard all still apply, each read off the dialect in use.  One
    check is STRENGTHENED -- s73's reduction.N_S is now compared against the
    verifier's own N_S exactly as s67's recipe.N_S always was, so a certificate
    that misrepresents its size is refused in either dialect.
    """
    if "field" in cert:
        field = cert["field"]
    elif "prime" in cert:
        field = f"F_{int(cert['prime'])}"
    else:
        raise ValueError("sparse_nullity: no field and no prime")
    if "nullity" in cert:
        nullity = cert["nullity"]
    elif isinstance(cert.get("claim"), dict) and "nullity" in cert["claim"]:
        nullity = cert["claim"]["nullity"]
    else:
        raise ValueError("sparse_nullity: no nullity and no claim.nullity")
    rec_ns = (cert.get("recipe") or {}).get("N_S")
    if rec_ns is None:
        rec_ns = (cert.get("reduction") or {}).get("N_S")
    return field, nullity, rec_ns


def check_sparse_nullity_certificate(cert, log):
    """Checker for kind == 'sparse_nullity'."""
    from layer2 import check_cell
    from points import form_of_point
    cell = cert["cell"]
    n, r, lam, delta, a = cell["n"], cell["r"], tuple(cell["lambda"]), cell["delta"], cell["a"]
    ok = check_cell(cell, log)
    field_str, nullity_claim, recorded_N_S = sparse_nullity_view(cert)
    kind_field, p = parse_field(field_str)
    variety = cert["variety"]

    # field discipline (Part A4)
    if kind_field != "Fp":
        return _rec(log, "field: sparse_nullity is a finite-field certificate", False,
                    "field must be F_<p>; a char-0 sparse nullity is not a certificate") and False
    _rec(log, "field declared", True, f"F_{p} (finite field); conclusion over Q via rank_p <= rank_Q")
    if nullity_claim > 0 and kind_field == "Fp":
        _rec(log, "field/nullity: a mod-p kernel bounds the ideal, it does not certify a char-0 bite", True,
             f"nullity_p = {nullity_claim} gives only mult >= a - {nullity_claim} (i = a - mult <= {nullity_claim})")

    # points on the variety (rebuilt from substitution data)
    pts = cert["points"]
    for pt in pts:
        if pt.get("type") != variety:
            return _rec(log, "points are of the claimed variety", False, f"{pt.get('type')} vs {variety}") and False
    try:
        forms = [form_of_point(pt, r, n) for pt in pts]
    except ValueError as e:
        return _rec(log, "points rebuilt from substitution data (lie on the variety)", False, str(e)) and False
    _rec(log, f"{len(pts)} points rebuilt from substitution data (variety {variety})", True)

    # size guard
    a_ind = ambient_multiplicity(lam, delta, n=n)
    if a_ind is not None and a_ind != a:
        return _rec(log, "a recomputed", False, f"{a_ind} vs {a}") and False

    # size guard, on the TRUE N_S -- computed here, never trusted from the
    # certificate.  A budget skip enumerates only the weight-lambda monomials
    # (cheap, level-by-level numpy) to get N_S; the expensive raising-operator
    # build is done only when the cell is within budget.  A recipe.N_S in the
    # certificate is provenance and is checked against the truth, never trusted.
    t0 = time.time()
    # N_S is COUNTED first and enumerated only if the cell is within budget.
    # weight_monomials_idx materialises every monomial, and at the LMR goal cell
    # that is 1.56e11 rows: the guard below used to run after it, so pointing the
    # verifier at a goal-cell certificate would try to build the array in order to
    # learn that it must not.  Session 74 reported that.  The tail DP counts the
    # same number in about three seconds and costs 8 MB.
    N_S = chi_build.weight_monomials_count(n, r, delta, lam)
    if isinstance(recorded_N_S, int) and recorded_N_S != N_S:
        return _rec(log, "recorded N_S matches the true weight-space dimension", False,
                    f"recorded {recorded_N_S}, true {N_S} -- certificate misrepresents its size") and False
    if N_S > VERIFY_MAX_NS:
        _rec(log, f"__RECORDED__ true N_S = {N_S} exceeds VERIFY_MAX_NS = {VERIFY_MAX_NS}", True,
             "schema/field/points and the true N_S validated (counted, not enumerated); the nullity "
             "claim is NOT re-derived this run (reproducible on demand at the cost of one build + "
             "Wiedemann sequence)")
        return ok
    # within budget: enumerate, and check the count against the enumeration
    M = chi_build.weight_monomials_idx(n, r, delta, lam)
    if M.shape[0] != N_S:
        return _rec(log, "the counted N_S matches the enumerated weight space", False,
                    f"counted {N_S}, enumerated {M.shape[0]} -- the verifier's own two routes "
                    f"disagree, which is a fault in the verifier and not in the certificate") and False
    # rebuild E on the monomial basis just enumerated
    E, M = chi_build.raising_operator_full(n, r, delta, lam)
    _rec(log, "E and monomial basis rebuilt (full weight space, verifier-owned)", True,
         f"N_S = {N_S}, E {E.shape}, nnz {E.nnz} ({time.time()-t0:.1f}s)")
    EV = chi_build.eval_rows_full(M, n, r, pts, p)
    F = sparse.vstack([E, sparse.csr_matrix(EV.astype(np.int64))]).tocsr()

    # soundness anchor: nullity_p(E) = a.  On by default; a coverage run over many
    # cells may set VERIFY_SKIP_BUILD_CHECK=1 after validating the (deterministic,
    # cell-shape-independent) build separately -- the log then says so.
    if os.environ.get("VERIFY_SKIP_BUILD_CHECK") == "1" and N_S > DENSE_CAP:
        _rec(log, "build check: nullity_p(E) = a  [assumed from separate build validation]", True,
             "VERIFY_SKIP_BUILD_CHECK=1; chi_build validated independently (see results/s67_verify_sparse.md)")
    else:
        bk_ok, bk_note = check_build_kernel(E, a, p, N_S)
        ok &= _rec(log, "build check: nullity_p(E) = a (E's kernel is the highest-weight space)", bk_ok, bk_note)
        if not bk_ok:
            return False

    # decide nullity_p([E; ev])
    if nullity_claim == 0:
        if N_S <= DENSE_CAP:
            k = _nullity_dense(F, p)
            full = (k == 0)
            _rec(log, f"nullity_p([E; ev]) recomputed exactly (flint), mod {p}", full, f"nullity = {k}")
        else:
            full, note = _wied_full_col_rank(F, p, N_S)
            if full is None:
                return _rec(log, "nullity_p([E; ev]) by Wiedemann", False, note) and False
            _rec(log, f"nullity_p([E; ev]) = 0 by Wiedemann, mod {p}", full, note)
        ok &= full
        if full:
            _rec(log, f"conclusion: mult_{variety}(lambda, delta) = a = {a} over Q "
                      f"(nullity_p([E; ev]) = 0, rank_p <= rank_Q <= a)", True)
    else:
        # k > 0: check recorded kernel vectors against [E; ev] and their independence
        return _rec(log, "sparse_nullity with nullity > 0: kernel-vector checking", False,
                    "not exercised by session 60's cells (all det-side nullity 0); "
                    "record such a bite as an hwv certificate (char-0) per Part A4") and False
    return ok

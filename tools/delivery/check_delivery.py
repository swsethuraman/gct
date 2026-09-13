#!/usr/bin/env python3
"""Pre-bundle delivery gate.  Run this BEFORE building the bundle, and again
after, with --bundle and --manifest.

Batch 13 shipped four recurring defects that a preamble sentence did not
prevent: HEAD-only bundles (a fetch by branch name then fails), session-link
trailers on 195 commits, and two staging gaps.  A prose checklist did not stop
them; this does.

Batch 14 then shipped nine more that THIS tool did not catch, because it held
six of the integrator gate's nine checks and nothing at all about the manifest,
the index or the ledger.  Counts from that batch, out of twelve deliveries:

    the packet's `base..HEAD` bundle form               7 sessions
    no dispatch message carrying the base               11 sessions
    garbled bundle_prerequisites in the manifest         4 of 6 Astra deliveries
    PROVED.md section-letter collision                   6, every one "F"
    unescaped pipes in a PROVED.md table row             1
    ledger entry appended with no application contract   1, and it broke the consumer
    wording-list word added to a delivered .md           0 -- but the integrator
                                                            gate false-failed a
                                                            clean delivery on it

Every one of those is now a check here, so a session catches it rather than the
integrator.  A check that cannot fail is not a check: run --selftest to watch
each one rejected by a constructed bad input, alongside a good delivery that
must come back clean.

usage:
    python3 tools/delivery/check_delivery.py --branch <name> --base <sha>
            [--bundle <file>] [--manifest <file>] [--slot NN]
    python3 tools/delivery/check_delivery.py --selftest

exit 0 = clean, 1 = defects found (each printed with its fix).
"""
import argparse, hashlib, json, os, re, shutil, subprocess, sys, tempfile

SINGLE_WRITER = ["paper/det3-conductor.tex", "paper/det4-onset.tex",
                 "PROJECT_NOTES.md", "docs/boundary_deficit.html"]
MAX_BYTES = 5 * 1024 * 1024
# Parameterised, because hardcoding "batch14" meant that in the next batch check 7
# would degrade to a note and check 9 would find no slot number -- both would stop
# checking without saying so.  Override with --base-tag / --batch.
BASE_TAG = os.environ.get("GCT_BASE_TAG", "batch14-base")
BATCH = os.environ.get("GCT_BATCH", "b14")
BANNED = ["kill", "pkill", "hunt", "brutal", "attack", "exploit",
          "proxy", "bypass", "circumvent", "STOP-EVERYTHING"]
# The consumer, tools/integrate/exclusion_predicates.py, FAILS CLOSED: an
# unrecognised predicate key raises rather than being skipped, so an entry that
# uses a new shape breaks every query until integration implements it.
LEDGER = "results/integrate/inherited_exclusions.json"
PREDICATE_KEYS = {"n", "r", "r_min", "r_max", "delta", "delta_min", "delta_max",
                  "family", "context", "lambda_in", "any_of",
                  "lambda_length_gt_delta", "lambda_1_lt_delta", "explicit_cell_keys"}

def git(*a, allow_fail=False):
    # Returning "" on a nonzero exit is what made this tool useless exactly when
    # it mattered: given a --base that no longer resolves (after a history
    # rewrite, say), every check read an empty string, passed vacuously, and the
    # tool printed "(0 files)" plus a bogus "no Co-Authored-By" defect instead of
    # saying the base was wrong.  A check that cannot fail loudly is not a check.
    r = subprocess.run(["git", *a], capture_output=True, text=True)
    if r.returncode and not allow_fail:
        sys.exit(f"git {' '.join(a)}\n  exit {r.returncode}: {r.stderr.strip()}")
    return r.stdout


def require_ancestor(base, branch):
    """--base must resolve, --branch must resolve, and base must be an ancestor.

    Without this a rewritten base silently yields an empty diff and an empty
    log, and the gate reports on nothing at all."""
    for name, rev in (("--base", base), ("--branch", branch)):
        r = subprocess.run(["git", "rev-parse", "--verify", f"{rev}^{{commit}}"],
                           capture_output=True, text=True)
        if r.returncode:
            sys.exit(f"{name} {rev!r} does not resolve to a commit in this repository.\n"
                     f"  after a history rewrite the old hashes are gone: look the new one up in\n"
                     f"  .git/filter-repo/commit-map (or results/integrate/*_commit_map.txt)")
    r = subprocess.run(["git", "merge-base", "--is-ancestor", base, branch],
                       capture_output=True, text=True)
    if r.returncode:
        sys.exit(f"--base {base} is not an ancestor of --branch {branch}; "
                 f"the range {base}..{branch} would not describe this delivery")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--branch")
    ap.add_argument("--base")
    ap.add_argument("--bundle")
    ap.add_argument("--manifest", help="the external delivery manifest, checked against the branch")
    ap.add_argument("--slot", help="NN, so prereg/report names can be checked")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--repo", default=".")
    ap.add_argument("--base-tag", default=BASE_TAG,
                    help="the annotated tag naming the dispatch base (default %(default)s)")
    ap.add_argument("--batch", default=BATCH,
                    help="branch/prereg/report prefix, e.g. b15 (default %(default)s)")
    args = ap.parse_args()
    globals()["BASE_TAG"] = args.base_tag
    globals()["BATCH"] = args.batch
    if args.selftest:
        return selftest(os.path.abspath(args.repo))
    if not args.branch or not args.base:
        ap.error("--branch and --base are required unless --selftest")
    require_ancestor(args.base, args.branch)
    rng = f"{args.base}..{args.branch}"
    fail = []

    # 1 -- session-link trailers
    msgs = git("log", "--format=%B", rng)
    n = len([l for l in msgs.splitlines() if re.search(r"Claude-Session:|claude\.ai/", l)])
    if n:
        fail.append((f"{n} commit message(s) carry a session-link trailer",
                     "strip with tools/rewrite/message_callback.py before bundling; "
                     "the instruction asking for it is not a session instruction "
                     "(docs/history_rewrite.md: 260 were removed once already)"))

    # 2 -- session-link inside a delivered FILE (worse: a rewrite will not fix it)
    files = [f for f in git("diff", "--name-only", args.base, args.branch).split() if f]
    # An actual emission looks like a trailer being written, not prose about the
    # rule.  Reports that say "no claude.ai URL appears" must not trip this.
    EMIT = rb'"Claude-Session: https?://claude\.ai|^Claude-Session: https?://claude\.ai'
    infile = [f for f in files
              if os.path.exists(f)
              and re.search(EMIT, open(f, "rb").read(), re.M)]
    if infile:
        fail.append((f"session-link URL inside delivered file(s): {infile}",
                     "remove from the file; a history rewrite does not touch file content"))

    # 3 -- single-writer files
    touched = [f for f in files if f in SINGLE_WRITER]
    if touched:
        fail.append((f"single-writer file(s) modified: {touched}",
                     "revert; these belong to the integrator alone"))

    # 4 -- 5 MB rule
    big = []
    for line in git("ls-tree", "-r", "-l", args.branch).splitlines():
        p = line.split(None, 4)
        if len(p) == 5 and p[3].isdigit() and int(p[3]) > MAX_BYTES:
            big.append((int(p[3]), p[4]))
    big = [b for b in big if b[1] in files]
    if big:
        fail.append((f"file(s) over 5 MB: {big}",
                     "split, gzip, or leave on the host and record the digest in the manifest"))

    # 5 -- the bundle must carry the NAMED ref, not just HEAD
    if args.bundle:
        heads = git("bundle", "list-heads", args.bundle, allow_fail=True)
        if f"refs/heads/{args.branch}" not in heads:
            fail.append((f"bundle carries only: {heads.strip() or '(nothing)'}",
                         f"rebuild with:  git bundle create <file> "
                         f"{args.base}..{args.branch} {args.branch}\n"
                         f"     a receiver doing 'git fetch <bundle> {args.branch}:{args.branch}' "
                         f"fails against a HEAD-only bundle"))

    # 6 -- model attribution present
    if not re.search(r"Co-Authored-By:", msgs):
        fail.append(("no Co-Authored-By trailer on any commit",
                     "record the model that actually ran the session, per commit; "
                     "use models: [(model, phase)] in front matter if it changed mid-session"))

    notes = []

    # 7 -- the base must be the commit the tag names.  Eleven of twelve batch-14
    # sessions reported that no dispatch message carrying it reached them, and the
    # value was wrong three times before the tag settled it.  Resolve it yourself:
    #     git log -1 --format=%H batch14-base       <- the COMMIT
    #     git rev-parse batch14-base                <- the tag OBJECT, not a base
    tagged = git("log", "-1", "--format=%H", BASE_TAG, allow_fail=True).strip()
    if not tagged:
        notes.append(f"the {BASE_TAG} tag is not in this clone, so the base could not be "
                     f"checked against it -- fetch it: git fetch origin "
                     f"refs/tags/{BASE_TAG}:refs/tags/{BASE_TAG}")
    else:
        base_sha = git("rev-parse", f"{args.base}^{{commit}}").strip()
        if base_sha != tagged:
            fail.append((f"--base {base_sha[:12]} is not the commit {BASE_TAG} names ({tagged[:12]})",
                         f"use  git log -1 --format=%H {BASE_TAG}  -- note that "
                         f"git rev-parse {BASE_TAG} returns the annotated TAG OBJECT, "
                         f"which is not a commit and is not a base"))

    # 8 -- exactly one ref in the bundle, and it must require exactly the base
    if args.bundle:
        heads = [l for l in git("bundle", "list-heads", args.bundle, allow_fail=True).splitlines() if l.strip()]
        if len(heads) > 1:
            fail.append((f"bundle carries {len(heads)} refs: {[h.split()[-1] for h in heads]}",
                         "cut it with exactly one branch: "
                         f"git bundle create <file> {args.base}..{args.branch} {args.branch}"))
        ver = subprocess.run(["git", "bundle", "verify", args.bundle],
                             capture_output=True, text=True)
        # `git bundle verify` writes to STDERR.  Reading stdout alone made the
        # integrator's own gate pass five constructed bad bundles for the wrong
        # reason; only its positive control could tell the difference.
        vtext = (ver.stdout or "") + (ver.stderr or "")
        req = re.findall(r"^([0-9a-f]{40})\s*$", vtext, re.M)
        if ver.returncode:
            fail.append((f"git bundle verify failed: {vtext.strip().splitlines()[-1] if vtext.strip() else '(no output)'}",
                         "rebuild the bundle"))
        elif req and tagged and any(r != tagged for r in req) and len(req) == 1:
            fail.append((f"bundle requires {req[0][:12]}, not the dispatch base {tagged[:12]}",
                         "you branched from the wrong commit; rebase onto the base and re-cut"))

    # 9 -- pre-registration exists and is the FIRST commit
    nn = args.slot or (re.search(rf"{re.escape(BATCH)}[-_](\d\d)", args.branch or "") or [None, None])[1]
    if nn:
        pre = [f for f in files if re.search(rf"PREREG_{BATCH}_{nn}", f)]
        if not pre:
            fail.append((f"no results/PREREG_{BATCH}_{nn}.md in the delivery",
                         "pre-registration is a deliverable, not a note"))
        else:
            order = list(reversed(git("log", "--format=%H", rng).split()))
            first_pre = git("log", "--format=%H", rng, "--reverse", "--", *pre).split()
            if first_pre and order and order.index(first_pre[0]) != 0:
                fail.append((f"pre-registration lands at commit {order.index(first_pre[0]) + 1} "
                             f"of {len(order)}, not first",
                             "everything committed before it is exploratory; commit the "
                             "pre-registration before any measurement"))
        if not any(re.search(rf"{BATCH}_{nn}_report", f) for f in files):
            fail.append((f"no docs/{BATCH}_{nn}_report.md in the delivery", "the report is a deliverable"))

    # 10 -- the house wording list, on ADDED lines only.  Scanning whole files
    # makes a prose audit inherit the wording debt of every document it edits:
    # the integrator's gate failed a clean delivery that way, on seven files whose
    # words pre-dated the policy and which it had not touched.
    for f in files:
        if not f.endswith(".md") or not os.path.exists(f):
            continue
        d = git("diff", args.base, args.branch, "--", f)
        added = [l[1:] for l in d.splitlines() if l.startswith("+") and not l.startswith("+++")]
        hits = sorted({w for w in BANNED for l in added if re.search(rf"\b{w}\b", l, re.I)})
        if hits:
            fail.append((f"{f} adds wording-list word(s) {hits}",
                         "see docs/brief_wording.md section 2 for the substitution"))

    # 11 -- docs/PROVED.md: a new section letter must not collide, and a table row
    # must stay a table row.  Six collisions in batch 14, every one of them "F",
    # and one row shipped |G_lambda| with the pipes unescaped, which splits one
    # cell into four.
    if "docs/PROVED.md" in files and os.path.exists("docs/PROVED.md"):
        before = git("show", f"{args.base}:docs/PROVED.md", allow_fail=True)
        after = open("docs/PROVED.md").read()
        old_l = set(re.findall(r"^## ([A-Z])\.", before, re.M))
        new_l = [l for l in re.findall(r"^## ([A-Z])\.", after, re.M)]
        clash = sorted(set(x for x in new_l if x in old_l and new_l.count(x) > 1))
        if clash:
            fail.append((f"docs/PROVED.md section letter(s) {clash} already exist",
                         f"the file already uses {''.join(sorted(old_l))}; take the next free letter"))
        badrow = [i + 1 for i, l in enumerate(after.split("\n"))
                  if l.startswith("|") and len(re.findall(r"(?<!\\)\|", l)) not in (4, 5)]
        if badrow:
            fail.append((f"docs/PROVED.md line(s) {badrow[:5]} are malformed table rows",
                         r"escape every pipe inside a cell as \| -- |G| and |Stab| are the usual culprits"))

    # 12 -- the ledger's consumer fails closed.  An entry appended with no
    # application contract, or with a predicate shape the matcher does not know,
    # does not get skipped: it RAISES, and every query for every cell then fails.
    if LEDGER in files and os.path.exists(LEDGER):
        try:
            led = json.load(open(LEDGER))
            contracts = set(led.get("application_contract", {}).get("conclusions_by_id", {}))
            for e in led.get("exclusions", []):
                if e["id"] not in contracts:
                    fail.append((f"ledger entry {e['id']} has no application_contract entry",
                                 "add it to application_contract.conclusions_by_id in the same commit"))
                unknown = sorted(set(e.get("predicate", {})) - PREDICATE_KEYS)
                if unknown:
                    fail.append((f"ledger entry {e['id']} uses predicate key(s) {unknown} "
                                 f"that the consumer does not implement",
                                 "tools/integrate/exclusion_predicates.py RAISES on an unknown key, "
                                 "it does not skip; implement it there in the same delivery or "
                                 "hand the shape to the integrator explicitly"))
        except Exception as exc:
            fail.append((f"{LEDGER} does not parse: {exc}", "fix the JSON"))

    # 13 -- the external manifest, against the branch it describes.  Four of six
    # Astra deliveries in batch 14 captured the base commit's SUBJECT LINE
    # alongside the hash in bundle_prerequisites.
    if args.manifest and os.path.exists(args.manifest):
        try:
            man = json.load(open(args.manifest))
        except Exception as exc:
            man = None
            fail.append((f"manifest does not parse: {exc}", "fix the JSON"))
        if man:
            # A check that cannot fail is not a check.  This one reads named fields,
            # so a manifest using different names was silently checked against
            # NOTHING and passed -- the same species of defect this tool exists to
            # catch.  Recognise something, or say so.
            KNOWN = {"head", "head_tree", "bundle_prerequisites", "base", "base_commit",
                     "md5", "sha256", "bundle_md5", "bundle_sha256", "bundle_bytes"}
            seen = KNOWN & set(man)
            if not seen:
                fail.append((f"manifest carries none of the fields this gate knows how to "
                             f"check ({sorted(KNOWN)}); it was checked against nothing",
                             "name the fields as above, or tell the integrator which names "
                             "you use so the gate learns them -- an unchecked manifest that "
                             "reports CLEAN is worse than no manifest"))
            elif not ({"head", "head_tree"} & seen):
                notes.append(f"manifest has no head/head_tree field, so the tip and tree were "
                             f"not checked (it does carry {sorted(seen)})")
            tip = git("rev-parse", f"{args.branch}^{{commit}}").strip()
            tree = git("show", "-s", "--format=%T", args.branch).strip()
            for key, want, what in (("head", tip, "branch tip"), ("head_tree", tree, "branch tree")):
                got = str(man.get(key, "")).strip()
                if got and got != want:
                    fail.append((f"manifest {key} is {got[:12]}, the {what} is {want[:12]}",
                                 "regenerate the manifest after the last commit"))
            for key in ("bundle_prerequisites", "base", "base_commit"):
                v = man.get(key)
                for item in (v if isinstance(v, list) else [v] if v else []):
                    if isinstance(item, str) and not re.fullmatch(r"[0-9a-f]{40}", item.strip()):
                        fail.append((f"manifest {key} is not a bare 40-hex commit: {item[:70]!r}",
                                     "git bundle verify prints the hash and the subject line on "
                                     "one line -- capture only the hash"))
            if args.bundle and os.path.exists(args.bundle):
                raw = open(args.bundle, "rb").read()
                for key, algo in (("md5", hashlib.md5), ("sha256", hashlib.sha256),
                                  ("bundle_md5", hashlib.md5), ("bundle_sha256", hashlib.sha256)):
                    if key in man and str(man[key]).strip() != algo(raw).hexdigest():
                        fail.append((f"manifest {key} does not match the bundle",
                                     "regenerate the manifest after building the bundle"))
                if "bundle_bytes" in man and int(man["bundle_bytes"]) != len(raw):
                    fail.append((f"manifest bundle_bytes is {man['bundle_bytes']}, the bundle is {len(raw)}",
                                 "regenerate the manifest after building the bundle"))

    print(f"delivery check: {args.branch} over {args.base}  ({len(files)} files)")
    for n_ in notes:
        print(f"  note: {n_}")
    if not fail:
        print("  CLEAN")
        return 0
    for what, fix in fail:
        print(f"\n  DEFECT: {what}\n     fix: {fix}")
    return 1

def selftest(repo):
    """Every check must be rejected by a constructed bad input, and a good
    delivery must come back clean.  The positive control is the one that
    distinguishes a working gate from one that refuses everything -- the
    integrator's gate passed five bad bundles for the wrong reason without it."""
    here = os.path.dirname(os.path.abspath(__file__))
    tool = os.path.join(here, "check_delivery.py")
    tmp = tempfile.mkdtemp(prefix="delivchk")
    wc = os.path.join(tmp, "wc")
    subprocess.run(["git", "clone", "-q", "--no-local", "-b", "integration/batch13", repo, wc], check=True)
    subprocess.run(["git", "-C", wc, "fetch", "-q", repo,
                    f"refs/tags/{BASE_TAG}:refs/tags/{BASE_TAG}"], check=True)
    base = subprocess.run(["git", "-C", wc, "log", "-1", "--format=%H", BASE_TAG],
                          capture_output=True, text=True).stdout.strip()

    def g(*a, **kw):
        return subprocess.run(["git", "-C", wc, *a], capture_output=True, text=True, **kw).stdout

    def commit(msg, trailer=True):
        g("add", "-A")
        body = msg + ("\n\nCo-Authored-By: Claude Opus 5 <noreply@anthropic.com>" if trailer else "")
        subprocess.run(["git", "-C", wc, "-c", "user.name=w", "-c", "user.email=w@x",
                        "commit", "-q", "-m", body], check=True)

    def w(rel, text, mode="w"):
        fp = os.path.join(wc, rel)
        os.makedirs(os.path.dirname(fp), exist_ok=True)
        open(fp, mode).write(text)

    def good():
        w("results/PREREG_b14_01.md", "# prereg\n"); commit("prereg")
        w("docs/b14_01_report.md", "# report\nPROVED nothing.\n"); commit("report")

    cases = []
    def case(name, build, want, why):
        cases.append((name, build, want, why))

    case("good", good, 0, "a clean delivery must pass")
    case("noprereg", lambda: (w("docs/b14_01_report.md", "# r\n"), commit("report only")), 1,
         "no pre-registration")
    case("prereg-late", lambda: (w("docs/b14_01_report.md", "# r\n"), commit("measured first"),
                                 w("results/PREREG_b14_01.md", "# p\n"), commit("prereg after")), 1,
         "pre-registration not first")
    case("no-report", lambda: (w("results/PREREG_b14_01.md", "# p\n"), commit("prereg only")), 1,
         "no report")
    case("single-writer", lambda: (good(), w("PROJECT_NOTES.md", "\nworker edit\n", "a"),
                                   commit("touch a protected file")), 1,
         "single-writer file touched")
    case("wording", lambda: (good(), w("docs/b14_01_report.md", "\nkill criteria: none.\n", "a"),
                             commit("wording")), 1,
         "a wording-list word ADDED")
    case("wording-inherited",
         lambda: (good(), w("docs/n4_gate.md", "\n**B14 note.** The gate is stated above.\n", "a"),
                  commit("edit a historical document")), 0,
         "editing a base document that already contains one, adding none -- MUST PASS")
    case("session-link", lambda: (good(), w("docs/b14_01_report.md",
                                            '\nClaude-Session: https://claude.ai/x\n', "a"),
                                  commit("link")), 1,
         "a session link inside a delivered file")
    case("proved-clash",
         lambda: (good(), w("docs/PROVED.md", "\n## C. a second section C\n\n| id | s | st | src |\n|---|---|---|---|\n", "a"),
                  commit("index")), 1,
         "a PROVED.md section letter that already exists")
    case("proved-pipes",
         lambda: (good(), w("docs/PROVED.md", "\n| `x` | uses |G| unescaped | PROVED | src |\n", "a"),
                  commit("index")), 1,
         "a malformed PROVED.md table row")
    case("ledger-no-contract",
         lambda: (good(), _ledger(wc), commit("ledger")), 1,
         "a ledger entry with no application contract and an unknown predicate key")

    results = []
    for name, build, want, why in cases:
        branch = f"b14-01-{name}"
        subprocess.run(["git", "-C", wc, "checkout", "-q", "-B", branch, BASE_TAG], check=True)
        build()
        r = subprocess.run([sys.executable, tool, "--branch", branch, "--base", base, "--slot", "01"],
                           capture_output=True, text=True, cwd=wc)
        got = 0 if r.returncode == 0 else 1
        ok = got == want
        results.append(ok)
        print(f"  {'PASS' if ok else 'FAIL'}  {branch:26s} expected {'clean' if want == 0 else 'rejection'}"
              f" ({why})")
        if not ok:
            print("        " + (r.stdout or r.stderr).strip().replace("\n", "\n        ")[:600])

    # bundle-shaped and manifest-shaped cases need artefacts, not just commits
    subprocess.run(["git", "-C", wc, "checkout", "-q", "-B", "b14-01-bundle", BASE_TAG], check=True)
    good()
    okb = os.path.join(tmp, "ok.bundle")
    headonly = os.path.join(tmp, "headonly.bundle")
    subprocess.run(["git", "-C", wc, "bundle", "create", okb, f"{base}..b14-01-bundle",
                    "b14-01-bundle"], capture_output=True, check=True)
    subprocess.run(["git", "-C", wc, "bundle", "create", headonly, f"{base}..HEAD"],
                   capture_output=True, check=True)

    def run(extra):
        r = subprocess.run([sys.executable, tool, "--branch", "b14-01-bundle", "--base", base,
                            "--slot", "01", *extra], capture_output=True, text=True, cwd=wc)
        return (0 if r.returncode == 0 else 1), (r.stdout or "") + (r.stderr or "")

    tip = g("rev-parse", "b14-01-bundle^{commit}").strip()
    tree = g("show", "-s", "--format=%T", "b14-01-bundle").strip()
    manifests = {
        "manifest-ok": {"head": tip, "head_tree": tree, "bundle_prerequisites": [base],
                        "sha256": hashlib.sha256(open(okb, "rb").read()).hexdigest(),
                        "bundle_bytes": os.path.getsize(okb)},
        "manifest-garbled-prereq": {"head": tip, "head_tree": tree,
                                    "bundle_prerequisites": [base + " A packet cannot contain its own hash"]},
        "manifest-stale-head": {"head": base, "head_tree": tree, "bundle_prerequisites": [base]},
        "manifest-wrong-sha": {"head": tip, "head_tree": tree, "bundle_prerequisites": [base],
                               "sha256": "0" * 64},
        # the silent-pass case: a manifest whose field names this gate does not know
        # was previously checked against nothing and reported CLEAN
        "manifest-unknown-fields": {"head_commit": tip, "tree_sha": tree,
                                    "prerequisite": base, "digest": "0" * 64},
    }
    extra = [("bundle-named-ref", ["--bundle", okb], 0, "a bundle carrying the named ref"),
             ("bundle-head-only", ["--bundle", headonly], 1, "a HEAD-only bundle"),
             ("base-not-the-tag", ["--base-override"], 1, "a --base that is not the tag's commit")]
    for name, args_, want, why in extra:
        if name == "base-not-the-tag":
            wrong = g("rev-parse", f"{BASE_TAG}~1").strip()
            r = subprocess.run([sys.executable, tool, "--branch", "b14-01-bundle", "--base", wrong,
                                "--slot", "01"], capture_output=True, text=True, cwd=wc)
            got = 0 if r.returncode == 0 else 1
        else:
            got, _ = run(args_)
        ok = got == want
        results.append(ok)
        print(f"  {'PASS' if ok else 'FAIL'}  {name:26s} expected {'clean' if want == 0 else 'rejection'} ({why})")
    for name, man in manifests.items():
        mp = os.path.join(tmp, name + ".json")
        json.dump(man, open(mp, "w"))
        got, out = run(["--bundle", okb, "--manifest", mp])
        want = 0 if name == "manifest-ok" else 1
        ok = got == want
        results.append(ok)
        print(f"  {'PASS' if ok else 'FAIL'}  {name:26s} expected {'clean' if want == 0 else 'rejection'}")
        if not ok:
            print("        " + out.strip().replace("\n", "\n        ")[:500])

    shutil.rmtree(tmp, ignore_errors=True)
    print("SELFTEST " + ("PASS" if all(results) else "FAIL"))
    return 0 if all(results) else 1


def _ledger(wc):
    """append an exclusion with no contract and a predicate shape the consumer
    does not implement -- the B14-11 case, which raised rather than skipping."""
    fp = os.path.join(wc, LEDGER)
    d = json.load(open(fp))
    d["exclusions"].append({"id": "selftest_new_shape",
                            "predicate": {"n": 4, "some_shape_the_matcher_lacks": True},
                            "statement": "constructed by --selftest", "status": "PROVED",
                            "source": "selftest"})
    json.dump(d, open(fp, "w"), indent=2)


if __name__ == "__main__":
    sys.exit(main())

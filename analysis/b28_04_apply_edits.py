"""B28-04: apply the approved B27-04b FIND/REPLACE pairs verbatim.

Usage: python b28_04_apply_edits.py <draft.md> <p2 worktree> <p3 worktree> [--apply] [--out <dir>]

The FIND/REPLACE texts are read directly from the draft's fenced blocks (no retyping).
Each FIND (LF rendering) must occur exactly once in its target (after converting to the
target's line endings); otherwise that item is STOPPED and its target is left unchanged
for that pair.  Output: a deterministic JSON record (no timestamps).
"""
import hashlib, json, re, sys, os

EXPECTED_DRAFT = "5d8f40124402c298321450c7ab31c192276655e5767665ec50a29f6f09d38663"

# (item, kind, repo, path) in the draft's order; kind F = FIND/REPLACE pair, A = append.
PLAN = [
    ("1",  "F", "p2", "paper/det4-onset.tex"),
    ("2",  "F", "p2", "paper/det4-onset.tex"),
    ("3a", "F", "p3", "papers/det4-blindness/det4-blindness.tex"),
    ("3b", "F", "p3", "papers/det4-blindness/det4-blindness.tex"),
    ("3c", "F", "p3", "papers/det4-blindness/det4-blindness.tex"),
    ("3d", "F", "p3", "papers/det4-blindness/GAPS.md"),
    ("3d", "F", "p3", "papers/det4-blindness/GAPS.md"),
    ("4",  "F", "p3", "papers/det4-blindness/det4-blindness.tex"),
    ("4",  "F", "p3", "papers/det4-blindness/det4-blindness.tex"),
    ("5",  "A", "p2", "PAPER2_GAPS.md"),
    ("6",  "F", "p2", "PAPER2_CLAIMS.md"),
    ("6",  "F", "p2", "PAPER2_READINESS.md"),
    ("6",  "F", "p2", "PAPER2_READINESS.md"),
]


def sha(b):
    return hashlib.sha256(b).hexdigest()


def main():
    args = sys.argv[1:]
    apply = "--apply" in args
    out = None
    if "--out" in args:
        out = args[args.index("--out") + 1]
    draft_p, p2, p3 = [a for a in args if not a.startswith("--") and a != out][:3]
    draft = open(draft_p, "rb").read()
    if sha(draft) != EXPECTED_DRAFT:
        sys.exit("draft hash mismatch: " + sha(draft))
    text = draft.decode("utf-8")
    assert "\r" not in text
    blocks = re.findall(r"^```\n(.*?)\n```$", text, flags=re.S | re.M)
    need = sum(2 if k == "F" else 1 for _, k, _, _ in PLAN)
    if len(blocks) != need:
        sys.exit("fenced block count %d != %d" % (len(blocks), need))
    roots = {"p2": p2, "p3": p3}
    files = {}  # (repo,path) -> bytes (current state)
    before = {}
    records = []
    bi = 0
    for n, (item, kind, repo, path) in enumerate(PLAN, 1):
        key = (repo, path)
        if key not in files:
            files[key] = open(os.path.join(roots[repo], path), "rb").read()
            before[key] = files[key]
        cur = files[key]
        crlf = cur.count(b"\r\n")
        lf = cur.count(b"\n")
        eol = "CRLF" if crlf == lf and lf > 0 else ("LF" if crlf == 0 else "MIXED")
        if eol == "MIXED":
            sys.exit("mixed line endings in " + path)
        conv = (lambda s: s.replace("\n", "\r\n")) if eol == "CRLF" else (lambda s: s)
        rec = {"step": n, "item": item, "repo": repo, "path": path, "eol": eol}
        if kind == "F":
            find, repl = blocks[bi], blocks[bi + 1]
            bi += 2
            fb, rb = conv(find).encode("utf-8"), conv(repl).encode("utf-8")
            cnt = cur.count(fb)
            rec.update(kind="FIND/REPLACE", find_sha256=sha(find.encode()),
                       replace_sha256=sha(repl.encode()), occurrences=cnt)
            if cnt == 1:
                files[key] = cur.replace(fb, rb)
                rec["status"] = "APPLIED"
                rec["offset"] = cur.index(fb)
            else:
                rec["status"] = "STOPPED"
        else:
            blk = blocks[bi]
            bi += 1
            ab = conv(blk + "\n").encode("utf-8")
            rec.update(kind="APPEND", block_sha256=sha(blk.encode()),
                       file_ends_with_newline=cur.endswith(b"\n"))
            if cur.endswith(b"\n"):
                files[key] = cur + ab
                rec["status"] = "APPLIED"
            else:
                rec["status"] = "STOPPED"
        records.append(rec)
    summary = []
    for key, b in files.items():
        summary.append({"repo": key[0], "path": key[1],
                        "before_sha256": sha(before[key]), "before_bytes": len(before[key]),
                        "after_sha256": sha(b), "after_bytes": len(b),
                        "after_crlf": b.count(b"\r\n"), "after_lf": b.count(b"\n")})
        if apply and b != before[key]:
            with open(os.path.join(roots[key[0]], key[1]), "wb") as fh:
                fh.write(b)
    res = {"draft_sha256": EXPECTED_DRAFT, "applied_to_disk": apply,
           "steps": records, "files": summary}
    s = json.dumps(res, indent=2, ensure_ascii=False) + "\n"
    if out:
        with open(out, "wb") as fh:
            fh.write(s.encode("utf-8"))
    sys.stdout.write(s)


if __name__ == "__main__":
    main()

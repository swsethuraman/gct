"""Batch 15 delivery checks on committed objects, not mutable working files.

This supplements the preserved historical check_delivery.py. Scientific claims
still require their own verifiers. Exit 0 means packaging checks passed.
"""
import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

LIMIT = 5_000_000
SHARED = {"paper/det3-conductor.tex", "paper/det4-onset.tex", "PROJECT_NOTES.md",
          "docs/boundary_deficit.html", "docs/PROVED.md",
          "results/integrate/inherited_exclusions.json"}
WORDS = ["kill", "pkill", "hunt", "brutal", "attack", "exploit", "proxy", "bypass", "circumvent", "STOP-EVERYTHING"]


def git(repo, *args, check=True):
    p = subprocess.run(["git", "-C", str(repo), *args], capture_output=True)
    if check and p.returncode:
        raise ValueError(p.stderr.decode("utf-8", "replace").strip())
    return p.stdout


def txt(repo, *args):
    return git(repo, *args).decode("utf-8").strip()


def json_load(path):
    def unique(pairs):
        out = {}
        for k, v in pairs:
            if k in out:
                raise ValueError("duplicate JSON key: " + k)
            out[k] = v
        return out
    return json.loads(Path(path).read_text(encoding="utf-8"), object_pairs_hook=unique,
                      parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))


def bundle_header(path):
    with Path(path).open("rb") as f:
        first = f.readline().rstrip()
        if first not in (b"# v2 git bundle", b"# v3 git bundle"):
            raise ValueError("unrecognized bundle header")
        refs, prereqs = [], []
        for _ in range(10000):
            line = f.readline()
            if line in (b"\n", b"\r\n"):
                return refs, prereqs
            if not line:
                break
            s = line.decode("utf-8").strip()
            if s.startswith("@"):
                continue
            sha, _, name = s.partition(" ")
            if sha.startswith("-"):
                sha = sha[1:]
                if not re.fullmatch("[0-9a-f]{40}", sha):
                    raise ValueError("invalid prerequisite hash")
                prereqs.append(sha)
            else:
                if not re.fullmatch("[0-9a-f]{40}", sha) or not name:
                    raise ValueError("invalid bundle ref")
                refs.append((sha, name))
    raise ValueError("incomplete bundle header")


def check(repo, branch, base, slot, base_tag="batch15-base", batch="b15", bundle=None, manifest=None):
    repo = Path(repo).resolve()
    errors = []
    def need(ok, message):
        if not ok:
            errors.append(message)
    if not re.fullmatch(r"\d{2}", slot):
        raise ValueError("slot must have exactly two digits")
    if not re.fullmatch(r"[A-Za-z0-9_-]+", batch):
        raise ValueError("invalid batch prefix")
    base = txt(repo, "rev-parse", "--verify", base + "^{commit}")
    head = txt(repo, "rev-parse", "--verify", "refs/heads/" + branch + "^{commit}")
    tree = txt(repo, "rev-parse", head + "^{tree}")
    git(repo, "merge-base", "--is-ancestor", base, head)
    # Missing or incorrectly typed tags fail, even if --base itself resolves.
    tag_type = txt(repo, "cat-file", "-t", "refs/tags/" + base_tag)
    need(tag_type == "tag", "dispatch base tag must be annotated")
    need(txt(repo, "rev-parse", "refs/tags/" + base_tag + "^{commit}") == base, "base differs from dispatch tag")
    annotation = txt(repo, "for-each-ref", "--format=%(contents)", "refs/tags/" + base_tag)
    need(base in annotation and txt(repo, "rev-parse", base + "^{tree}") in annotation,
         "tag annotation must identify expected commit and tree")
    changed = git(repo, "diff", "--name-only", "-z", base, head).decode("utf-8").split("\0")
    changed = [p for p in changed if p]
    need(bool(changed), "delivery has no changed files")
    commits = txt(repo, "rev-list", "--reverse", "--topo-order", base + ".." + head).splitlines()
    need(bool(commits), "delivery has no commits")
    blobs = {}
    for p in changed:
        mode = git(repo, "ls-tree", head, "--", p).decode("utf-8").split()
        if not mode:  # deletion is still checked for protected paths
            continue
        need(mode[0] == "100644" or mode[0] == "100755", "unsupported changed file type: " + p)
        if mode[0] not in ("100644", "100755"):
            continue
        size = int(txt(repo, "cat-file", "-s", head + ":" + p))
        need(size < LIMIT, "changed file must be below 5,000,000 bytes: " + p)
        if size < LIMIT:
            blobs[p] = git(repo, "show", head + ":" + p)
    need(not (set(changed) & SHARED), "shared files must be proposed through per-slot fragments: " + str(sorted(set(changed) & SHARED)))
    for c in commits:
        body = txt(repo, "show", "-s", "--format=%B", c)
        need("Co-Authored-By:" in body, "missing model attribution in commit " + c[:12])
        need(not re.search(r"https?://claude\.ai/", body, re.I), "session URL in commit " + c[:12])
    for p, data in blobs.items():
        if p.endswith((".md", ".json", ".jsonl", ".txt", ".py")):
            need(not re.search(rb"https?://claude\.ai/", data, re.I), "session URL in file " + p)
        if p.endswith(".md"):
            diff = git(repo, "diff", "--no-ext-diff", "--unified=0", base, head, "--", p).decode("utf-8")
            additions = "\n".join(s[1:] for s in diff.splitlines() if s.startswith("+") and not s.startswith("+++"))
            hits = [w for w in WORDS if re.search(r"\b" + re.escape(w) + r"\b", additions, re.I)]
            need(not hits, p + " adds disallowed operational wording: " + str(hits))
    pre = f"results/PREREG_{batch}_{slot}.md"
    report = f"docs/{batch}_{slot}_report.md"
    need(pre in blobs and bool(blobs.get(pre, b"").strip()), "missing or empty canonical preregistration")
    need(report in blobs and bool(blobs.get(report, b"").strip()), "missing or empty canonical report")
    if commits:
        first_files = git(repo, "diff-tree", "--no-commit-id", "--name-only", "-r", "-z", commits[0]).decode("utf-8").split("\0")
        need(pre in first_files, "preregistration is not in the first commit")
        need(not git(repo, "ls-tree", base, "--", pre).strip(), "preregistration already existed at dispatch base")
    if bundle is not None:
        bundle = Path(bundle).resolve()
        if not bundle.is_file():
            raise ValueError("bundle path does not exist")
        refs, prereqs = bundle_header(bundle)
        need(refs == [(head, "refs/heads/" + branch)], "bundle must contain exactly the named branch at its current head")
        need(prereqs == [base], "bundle must require exactly the dispatch base")
        git(repo, "bundle", "verify", str(bundle))
        if manifest is None:
            raise ValueError("post-bundle check requires a manifest")
    if manifest is not None:
        if bundle is None:
            raise ValueError("manifest check requires the actual bundle")
        man = json_load(manifest)
        if not isinstance(man, dict) or not man:
            raise ValueError("manifest must be a nonempty object")
        required = {"head", "head_tree", "base_commit", "bundle_prerequisites", "bundle_bytes", "sha256", "md5", "models", "slot", "branch"}
        need(required <= set(man), "manifest missing fields: " + str(sorted(required - set(man))))
        for key, want in (("head", head), ("head_tree", tree), ("base_commit", base), ("branch", branch), ("slot", slot)):
            need(man.get(key) == want, "manifest " + key + " mismatch")
        for key in ("head", "head_tree", "base_commit"):
            need(type(man.get(key)) is str and bool(re.fullmatch("[0-9a-f]{40}", man.get(key, ""))), "manifest " + key + " must be bare 40-hex")
        need(man.get("bundle_prerequisites") == [base], "manifest prerequisites must be the one-element list of the actual base hash")
        raw = bundle.read_bytes()
        need(type(man.get("bundle_bytes")) is int and man["bundle_bytes"] == len(raw), "manifest byte count mismatch")
        for key, fn in (("sha256", hashlib.sha256), ("md5", hashlib.md5)):
            need(man.get(key) == fn(raw).hexdigest(), "manifest " + key + " mismatch")
        models = man.get("models")
        need(isinstance(models, list) and bool(models) and all(isinstance(m, dict) and isinstance(m.get("model"), str) and m["model"] and isinstance(m.get("phase"), str) and m["phase"] for m in models), "manifest must record actual model/phase entries")
        if len(raw) >= LIMIT:
            parts = man.get("parts", [])
            need(isinstance(parts, list) and bool(parts), "large local bundle requires delivery parts")
            joined = bytearray()
            for part in parts:
                name = part.get("name") if isinstance(part, dict) else None
                if not isinstance(name, str) or Path(name).name != name or name in (".", ".."):
                    raise ValueError("invalid part filename")
                data = (bundle.parent / name).read_bytes()
                need(len(data) < LIMIT and part.get("bytes") == len(data), "part size mismatch: " + name)
                need(part.get("sha256") == hashlib.sha256(data).hexdigest(), "part checksum mismatch: " + name)
                joined.extend(data)
            need(joined == raw, "ordered delivery parts do not reproduce the bundle")
    return dict(status="PASS" if not errors else "FAIL", errors=errors, branch=branch, base=base, head=head, head_tree=tree,
                changed_files=len(changed), commits=len(commits), mathematical_claims_verified=False)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--repo", default="."); p.add_argument("--branch", required=True)
    p.add_argument("--base", required=True); p.add_argument("--slot", required=True)
    p.add_argument("--base-tag", default="batch15-base"); p.add_argument("--batch", default="b15")
    p.add_argument("--bundle"); p.add_argument("--manifest"); p.add_argument("--json-report")
    a = p.parse_args()
    try:
        result = check(a.repo, a.branch, a.base, a.slot, a.base_tag, a.batch, a.bundle, a.manifest)
    except Exception as exc:
        result = dict(status="FAIL", errors=[str(exc)], mathematical_claims_verified=False)
    if a.json_report:
        Path(a.json_report).write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())

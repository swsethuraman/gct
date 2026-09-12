"""Export the committed B14-04 branch, checks, evidence and bare-name hashes."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
BASE = "9898e56941a7665f231873481dae956f08509995"
TREE = "cb688cd3fe454d638f3202e759e2eaa0c629739f"
BRANCH = "b14-04-astra"
LIMIT = 5 * 1024 * 1024


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def checksums(folder, stem="CHECKSUMS"):
    files = sorted(p for p in folder.iterdir() if p.is_file() and p.suffix not in (".md5", ".sha256"))
    for algorithm in ("md5", "sha256"):
        lines = [hashlib.new(algorithm, p.read_bytes()).hexdigest() + "  " + p.name for p in files]
        (folder / (stem + "." + algorithm)).write_text("\n".join(lines) + "\n", encoding="ascii")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("destination", type=Path)
    a = ap.parse_args()
    dest = a.destination.resolve()
    assert dest == Path("C:/Users/swami/Projects/gct-gpt/Batch14_Results/B14-04").resolve(), "wrong delivery directory"
    assert git("branch", "--show-current") == BRANCH
    assert git("log", "-1", "--format=%H", "batch14-base") == BASE
    assert git("log", "-1", "--format=%T", "batch14-base") == TREE
    assert not git("status", "--porcelain"), "commit intentional session files before packaging"
    verification = json.loads((ROOT / "results/b14_04/verification.json").read_text())
    assert verification["status"] == "PASS" and verification["complete"]
    dest.mkdir(parents=True, exist_ok=True)
    bundle = dest / "b14_04_astra.bundle"
    checker = [sys.executable, "tools/delivery/check_delivery.py", "--branch", BRANCH, "--base", BASE]
    checks = []
    def run_check(name, command):
        run = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        (dest / name).write_text(run.stdout + run.stderr, encoding="utf-8")
        checks.append({"log": name, "command": command, "exit_code": run.returncode})
        if run.returncode:
            raise RuntimeError(name + " failed; see delivered log")
    run_check("delivery_check_before.log", checker)
    run_check("bundle_create.log", ["git", "bundle", "create", str(bundle), BASE + ".." + BRANCH, BRANCH])
    run_check("delivery_check_after.log", checker + ["--bundle", str(bundle)])
    run_check("bundle_verify.log", ["git", "bundle", "verify", str(bundle)])
    heads = git("bundle", "list-heads", str(bundle))
    assert "refs/heads/" + BRANCH in heads
    (dest / "bundle_heads.txt").write_text(heads + "\n")
    shutil.copy2(ROOT / "docs/b14_04_report.md", dest / "b14_04_report.md")
    shutil.copy2(ROOT / "results/b14_04/REPLAY.md", dest / "REPLAY.md")
    for relative, target_name, pattern in (("results/b14_04", "artifacts", "*"), ("results/logs", "logs", "b14_04_*")):
        target = dest / target_name
        target.mkdir(exist_ok=True)
        for path in sorted((ROOT / relative).glob(pattern)):
            if path.is_file():
                assert path.stat().st_size <= LIMIT
                shutil.copy2(path, target / path.name)
        checksums(target)
    parts = []
    data = bundle.read_bytes()
    if len(data) > LIMIT:
        for start in range(0, len(data), LIMIT):
            part = bundle.with_name(bundle.name + ".part" + str(len(parts)).zfill(2))
            part.write_bytes(data[start:start + LIMIT])
            parts.append(part)
    for algorithm in ("md5", "sha256"):
        rows = [hashlib.new(algorithm, p.read_bytes()).hexdigest() + "  " + p.name for p in [bundle] + parts]
        bundle.with_suffix(bundle.suffix + "." + algorithm).write_text("\n".join(rows) + "\n", encoding="ascii")
    header = data.split(b"\n\n", 1)[0].decode("ascii")
    manifest = {"status": "DELIVERED", "board_numbering": "batch14", "actual_model": "gpt-6-astra",
                "base_commit": BASE, "base_tree": TREE, "head_commit": git("rev-parse", BRANCH),
                "head_tree": git("log", "-1", "--format=%T", BRANCH),
                "branch": BRANCH, "bundle": bundle.name, "bundle_heads": heads.splitlines(),
                "prerequisites": [line for line in header.splitlines() if line.startswith("-")],
                "numbered_part_count": len(parts), "checks": checks,
                "verification": {"status": verification["status"], "stable": verification["stable"], "hpad": verification["hpad"]},
                "files": []}
    for path in sorted(dest.rglob("*")):
        if path.is_file() and path.name not in ("delivery_manifest.json", "CHECKSUMS.md5", "CHECKSUMS.sha256"):
            raw = path.read_bytes()
            manifest["files"].append({"path": str(path.relative_to(dest)).replace("\\", "/"),
                                      "bytes": len(raw), "md5": hashlib.md5(raw).hexdigest(),
                                      "sha256": hashlib.sha256(raw).hexdigest()})
    (dest / "delivery_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    checksums(dest)
    # Verify every sidecar after copies and manifest creation.
    verified = 0
    for sidecar in dest.rglob("*"):
        if sidecar.suffix not in (".md5", ".sha256"):
            continue
        for line in sidecar.read_text().splitlines():
            digest, filename = line.split("  ", 1)
            assert "/" not in filename and "\\" not in filename
            assert hashlib.new(sidecar.suffix[1:], (sidecar.parent / filename).read_bytes()).hexdigest() == digest
            verified += 1
    print(json.dumps({"destination": str(dest), "head": manifest["head_commit"],
                      "bundle_bytes": len(data), "part_count": len(parts), "checksum_entries_verified": verified,
                      "delivery_checks": "PASS", "bundle_verified": True}, indent=2))


if __name__ == "__main__":
    main()

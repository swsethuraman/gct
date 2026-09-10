"""Freeze B13-03 provenance and copy its single-part local bundle delivery."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BASE = "00495110c62acfbbbc951e82cc218ed091563b3f"
DELIVERY = Path("C:/Users/swami/Projects/gct-gpt/Batch13_Results/B13-03")
INPUTS = [
    "docs/batch13_worker_preamble.md", "docs/batch13_board.md",
    "docs/batch13_corrections.md", "docs/stocktake_batch12.md", "docs/brief_wording.md",
    "docs/reducible_ideal.md", "docs/s64_integrator_note1.md", "docs/transfer_lemma.md",
    "analysis/wk8_s30_core.py", "results/astra/S4/S4_report.md",
    "results/astra/S4/src/calibrate.py", "results/astra/S4/REPLAY.md",
    "results/astra/S4/artifacts/s64_control.json",
    "results/astra/S4/artifacts/s64_r5_exact_kernel.json.gz",
]


def now():
    return datetime.now(timezone.utc).isoformat()


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def digest(path):
    b = Path(path).read_bytes()
    return {"bytes": len(b), "sha256": hashlib.sha256(b).hexdigest(),
            "md5": hashlib.md5(b).hexdigest()}


def own_files():
    paths = [ROOT / "docs/b13_03_report.md", ROOT / "results/PREREG_b13_03.md"]
    paths += sorted((ROOT / "analysis").glob("b13_03_*.py"))
    paths += sorted((ROOT / "results/b13_03").glob("*"))
    paths += sorted((ROOT / "results/logs").glob("b13_03_*"))
    return [p for p in paths if p.is_file() and p.name != "manifest.json"]


def write(path, obj):
    Path(path).write_text(json.dumps(obj, indent=2)+"\n", encoding="utf-8")


def freeze():
    assert git("branch", "--show-current") == "b13-03"
    assert git("merge-base", BASE, "HEAD") == BASE
    files = own_files()
    records = [{"path": p.relative_to(ROOT).as_posix(), **digest(p)} for p in files]
    assert all(x["bytes"] < 5_000_000 for x in records)
    inputs = [{"path": p, "frozen_base_blob": git("rev-parse", f"{BASE}:{p}"),
               **digest(ROOT / p)} for p in INPUTS]
    independent = json.loads((ROOT / "results/b13_03/independent_verification.json").read_text())
    assert independent["status"] == "PASS"
    out = {"board_numbering": "batch13", "session_id": "B13-03",
           "model": "gpt-6-astra", "reasoning_effort": "xhigh",
           "model_evidence": "this task's local turn_context.model and .effort",
           "base": BASE, "branch": "b13-03", "generated_utc": now(),
           "outcome": "SUCCESS: complete exact control and reusable algorithm",
           "head_before_report_commit": git("rev-parse", "HEAD"),
           "history_rewritten": False, "bundle_parts": 1,
           "dependencies": {"python": "3.12.14", "numpy_verifier_only": "2.3.5",
                            "installed_during_run": [], "missing_flint_install": "blocked by WinError 10013"},
           "control": {"lambda": [8, 8, 8], "degree": 6, "variables": 3,
                       "source_dimension_Q": 2, "reducible_rank_Q": 1, "ideal_dimension_Q": 1,
                       "accepted_source_coordinates": [1, 0],
                       "non_element_exact_value": 729},
           "verification": "independent_verification.json: PASS; exact symbolic replay and both house primes",
           "primes": [2147483647, 2147483629],
           "hash_convention": "raw filesystem bytes; CRLF/LF conversion changes hashes; Git blob IDs separately identify frozen inputs",
           "self_hash": "excluded; delivery_manifest.json hashes this file after the final commit",
           "inputs": inputs, "outputs": records}
    write(ROOT / "results/b13_03/manifest.json", out)
    print(json.dumps({"manifest": "results/b13_03/manifest.json", "outputs": len(records),
                      "inputs": len(inputs), "largest_output_bytes": max(x["bytes"] for x in records)}))


def deliver():
    assert git("branch", "--show-current") == "b13-03"
    assert not git("status", "--porcelain"), "commit the complete deliverable first"
    manifest = json.loads((ROOT / "results/b13_03/manifest.json").read_text())
    for item in manifest["outputs"] + manifest["inputs"]:
        assert digest(ROOT / item["path"])["sha256"] == item["sha256"], item["path"]
    DELIVERY.mkdir(parents=True, exist_ok=True)
    copies = own_files() + [ROOT / "results/b13_03/manifest.json"]
    copies += [ROOT / p for p in INPUTS]
    for source in copies:
        target = DELIVERY / source.relative_to(ROOT)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
    shutil.copy2(ROOT / "docs/b13_03_report.md", DELIVERY / "b13_03_report.md")
    bundle = DELIVERY / "b13_03_exact_reducible_membership.bundle"
    git("bundle", "create", str(bundle), BASE+"..HEAD", "b13-03")
    checked = subprocess.run(["git", "bundle", "verify", str(bundle)], cwd=ROOT,
                             text=True, capture_output=True, check=True)
    (DELIVERY / "bundle_verify.txt").write_text(checked.stdout+checked.stderr)
    part = Path(str(bundle)+".part00")
    shutil.copy2(bundle, part)
    assert bundle.read_bytes() == part.read_bytes()
    for algorithm in ("md5", "sha256"):
        Path(str(bundle)+"."+algorithm).write_text(
            "".join(f"{digest(p)[algorithm]}  {p.name}\n" for p in (bundle, part)))
    final = {"board_numbering": "batch13", "session_id": "B13-03", "model": "gpt-6-astra",
             "generated_utc": now(), "base": BASE, "head": git("rev-parse", "HEAD"),
             "branch": "b13-03", "status": "SUCCESS; verified local bundle delivered",
             "bundle": {"filename": bundle.name, **digest(bundle)},
             "part_count": 1, "parts": [{"index": 0, "filename": part.name, **digest(part)}],
             "git_bundle_verify": "PASS; see bundle_verify.txt",
             "all_files": [{"path": p.relative_to(DELIVERY).as_posix(), **digest(p)}
                           for p in sorted(DELIVERY.rglob("*")) if p.is_file()
                           and p.name not in ("delivery_manifest.json", "delivery_checksums.sha256")],
             "self_hash": "excluded from this manifest; included in delivery_checksums.sha256"}
    write(DELIVERY / "delivery_manifest.json", final)
    checksum_paths = [p for p in sorted(DELIVERY.rglob("*")) if p.is_file()
                      and p.name != "delivery_checksums.sha256"]
    (DELIVERY / "delivery_checksums.sha256").write_text("".join(
        f"{digest(p)['sha256']}  {p.relative_to(DELIVERY).as_posix()}\n" for p in checksum_paths))
    for item in final["all_files"]:
        assert digest(DELIVERY / item["path"])["sha256"] == item["sha256"]
    print(json.dumps({"delivery": str(DELIVERY), "head": final["head"],
                      "bundle_bytes": bundle.stat().st_size, "parts": 1,
                      "bundle_sha256": digest(bundle)["sha256"],
                      "copied_files_verified": len(final["all_files"])}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["freeze", "deliver"])
    args = parser.parse_args()
    {"freeze": freeze, "deliver": deliver}[args.action]()

"""B26-10A administrative sealing only: Git reads, hashes, inventory and clocks.

No symbolic algebra, arithmetic certificate, mathematical test, search or replay.
Run with --seal to author receipts, or --verify-only to check the sealed packet.
Writes are confined to the assigned report and results/b26_10a.
"""

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
from datetime import datetime, timezone

WORKTREE = Path(__file__).resolve().parents[2]
OUT = WORKTREE / "results/b26_10a"
REPORT = WORKTREE / "docs/b26_10a_review.md"
PROJECT = WORKTREE.parents[2]
HANDOVER = PROJECT / "Claude_Handover_B15_B18/post_b19_housekeeping_20260917"
HEAD = "65736d9f9b27ae508697c87f306f494760e87007"
START = "2026-09-23T02:43:59Z"
SUBSTANTIVE_STOP = "2026-09-23T02:54:01Z"
STATUS = "UNCOMMITTED / REVIEWER ONLY"

# Each expected digest below names exact git-show blob bytes, never decoded text.
SPECS = [
    (HEAD, "docs/b26_04_report.md", "sections 0-7; certificate and proposed wording",
     "9d61f5e24e2ed4e91f5e8db84b2bec50393194ba05696fb51965d2b10c772d47"),
    (HEAD, "results/b26_04/MANIFEST.json", "entire manifest",
     "ee7805c874c8e1c5a9877c6ce452fc55549c8185679db647d61dfefc1caf830e"),
    ("2688efd1b5b14c78c11a9855e83357f4516cba54", "docs/b25_05_report.md",
     "section A and source ledger E; additional context viewed, not relied on",
     "38834c316c1b182e6acbe120b1608e3fb325c65e0f12790d0312e1c3a2373455"),
    ("42e7f4ba45e8bd1fda529de9ce116f64e7ac6be1", "docs/b25_10_review.md", "section 2",
     "0488ce1e90a6cd08158eb277dd482b783aa4c58cfd6cec744bd35d25b589477e"),
    ("79b68dcf7597e3b0efa63984327ad9f34e5bf74d", "paper/det4-onset.tex",
     "lines 100-125,235-287,688-711,780-806,838-897,990-1100,1210-1241; all eq:lengthred occurrences",
     "065f8799dbec4b24b0ddd93b2cd1fdf8528d435c4464bcc529700010f08f55d8"),
    ("721d54a2afc1e0a89eacd3e1e9bf5a78cea12dce", "docs/b26_05_report.md",
     "section 5; surrounding editorial context viewed",
     "26717997562a20ee9e8c42981d48a1f1a641727972b55715d8dc48304f5a673e"),
    ("cdf6839cd81031d42e43dc640b08e2746a7ef22c", "docs/b26_02_review.md",
     "section 4; sections 0-3 read as context, not independently re-audited",
     "14de8f0f03f45b97ce7a82ca47801ae7d22e6a65d8c09fd1e68f847b36ec8bd0"),
    ("82633a60", "docs/isotypic_rank.md", "sections 1-3",
     "5f33e38e72be947a23941dc223502b87fcd057708edc24ec3d98a0e8942d517f"),
    ("0cce6172", "docs/b17_03_report.md", "coefficient convention and Lemmas 1-2",
     "bcb38b5f2682f69c86c39fbf04250cb7729cd9a749ea185c228b6e75234da43e"),
    ("82633a60", "docs/s73_report.md", "section 1; opening summary context only",
     "f40783ba4dd5489da922eaec9cd19b465b1c55a340bceb36b636c45c552dd94e"),
    ("82633a60", "docs/s26_review.md", "sections 1-4; historical context only", None),
    ("82633a60", "docs/reducible_ideal.md", "Corollary D; historical context only", None),
]
ADMIN = [
    ("batch26_launch/B26_COMMON.md",
     "a22c91034244d48aae2be5c9f5ecb4337cff609cda1aaf08e593e497656a51fd"),
    ("batch26_launch/B26-10A.md",
     "b0c8e755c61020a41ad4dfa3cde1c6ca751a15a6683ee0474f811c591f082474"),
    ("BATCH26_LIVE_LEDGER.md",
     "8260cd3772c5208960b941d6243962e0e42012317f173dc48c68f28ac231de14"),
]
PATHS = [
    "docs/b26_10a_review.md",
    "results/b26_10a/INPUT_BINDINGS.json",
    "results/b26_10a/LMR_1004.4802v1.pdf",
    "results/b26_10a/admin_receipts.py",
    "results/b26_10a/resource_receipt.json",
    "results/b26_10a/PROPOSED_DELIVERY_PATHS.txt",
    "results/b26_10a/MANIFEST.json",
]


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def git(*args):
    env = os.environ.copy()
    env["GIT_OPTIONAL_LOCKS"] = "0"
    command = ["git", "-C", str(WORKTREE), "-c",
               "safe.directory=" + WORKTREE.as_posix(), *args]
    result = subprocess.run(command, check=True, capture_output=True, env=env)
    return result.stdout


def write_json(path, data):
    path.write_bytes((json.dumps(data, indent=2, ensure_ascii=False) + "\n").encode("utf-8"))


def status_snapshot():
    branch = git("branch", "--show-current").decode().strip()
    head = git("rev-parse", "HEAD").decode().strip()
    if branch != "b15-01-ci159" or head != HEAD:
        raise RuntimeError("Branch/HEAD mismatch: stop")
    counts = {}
    own_all = set()
    for name, opts, expected in [
        ("default", [], 10383),
        ("all_files", ["--untracked-files=all"], 20761),
    ]:
        entries = git("status", "--porcelain", *opts).decode("utf-8").splitlines()
        if any(not line.startswith("?? ") for line in entries):
            raise RuntimeError("Tracked/staged changes detected: stop")
        own = [line for line in entries
               if line[3:] == "docs/b26_10a_review.md"
               or line[3:].startswith("results/b26_10a/")]
        remaining = len(entries) - len(own)
        if remaining != expected:
            raise RuntimeError(f"Pre-existing inventory count changed: {name}={remaining}")
        counts[name] = {"total_entries": len(entries), "slot_entries": len(own),
                        "preexisting_entries": remaining}
        if name == "all_files":
            own_all = {line[3:] for line in own}
    return {"branch": branch, "head": head, "tracked_or_staged_changes": 0,
            "counts": counts, "slot_untracked_paths": sorted(own_all)}


def assert_packet_inventory():
    actual = {"docs/b26_10a_review.md"}
    actual.update(p.relative_to(WORKTREE).as_posix() for p in OUT.rglob("*") if p.is_file())
    if actual != set(PATHS):
        raise RuntimeError(f"Payload inventory mismatch: {sorted(actual ^ set(PATHS))}")


def seal_manifest():
    payloads = []
    for rel in PATHS[:-1]:
        data = (WORKTREE / rel).read_bytes()
        payloads.append({"path": rel, "bytes": len(data), "sha256_raw": digest(data),
                         "byte_kind": "raw binary PDF" if rel.endswith(".pdf") else "raw UTF-8 LF working copy"})
    write_json(OUT / "MANIFEST.json", {
        "slot": "B26-10A", "status": STATUS,
        "verdicts": {"part_1": "ACCEPT", "part_2": "ACCEPT"},
        "paper_2_transfer_flag_recommendation": "remove after separate delivery/adjudication",
        "achievement_level": "transfer lemma and literal-family classification only",
        "payloads": payloads,
        "excluded_from_own_hashes": "results/b26_10a/MANIFEST.json",
        "note": "All SHA-256 values bind exact raw payload bytes; no Git filter was applied."
    })


def verify():
    assert_packet_inventory()
    manifest = json.loads((OUT / "MANIFEST.json").read_text(encoding="utf-8"))
    listed = (OUT / "PROPOSED_DELIVERY_PATHS.txt").read_text(encoding="utf-8").splitlines()
    if listed != PATHS or len(set(listed)) != len(listed):
        raise RuntimeError("Delivery list mismatch")
    if {p["path"] for p in manifest["payloads"]} != set(PATHS[:-1]):
        raise RuntimeError("Manifest path mismatch")
    for item in manifest["payloads"]:
        data = (WORKTREE / item["path"]).read_bytes()
        if len(data) != item["bytes"] or digest(data) != item["sha256_raw"]:
            raise RuntimeError(f"Payload hash mismatch: {item['path']}")
        if not item["path"].endswith(".pdf"):
            if b"\r" in data or any(c < 32 and c not in (9, 10) for c in data):
                raise RuntimeError(f"Unexpected text control byte: {item['path']}")
            data.decode("utf-8")
    snapshot = status_snapshot()
    if set(snapshot["slot_untracked_paths"]) != set(PATHS):
        raise RuntimeError("Packet is not wholly untracked or has missing status entries")
    return snapshot


def seal():
    status_snapshot()
    inputs = []
    for ref, path, extent, expected in SPECS:
        data = git("show", f"{ref}:{path}")
        actual = digest(data)
        if expected and actual != expected:
            raise RuntimeError(f"Pinned-input mismatch: {ref}:{path}")
        cr = data.count(b"\r")
        lf = data.count(b"\n")
        inputs.append({
            "commit": git("rev-parse", ref + "^{commit}").decode().strip(),
            "path": path,
            "git_blob_id": git("rev-parse", f"{ref}:{path}").decode().strip(),
            "sha256_blob_content": actual, "bytes": len(data),
            "CR_bytes": cr, "LF_bytes": lf,
            "byte_kind": "committed CRLF blob" if cr and cr == lf else "committed LF blob",
            "read_label": "READ", "read_extent": extent,
        })
    admin = []
    for path, expected in ADMIN:
        data = (HANDOVER / path).read_bytes()
        actual = digest(data)
        if actual != expected:
            raise RuntimeError(f"Administrative brief/ledger changed: {path}")
        admin.append({"path_relative_to_handover": path, "bytes": len(data),
                      "sha256_raw_working_copy": actual, "unchanged_since_preflight": True})
    pdf = (OUT / "LMR_1004.4802v1.pdf").read_bytes()
    if digest(pdf) != "cfc28275a8c6b27f0ad6946d495ed4f889f7617df479be943d8d35718dbf2d79":
        raise RuntimeError("Archived PDF hash mismatch")
    write_json(OUT / "INPUT_BINDINGS.json", {
        "slot": "B26-10A", "status": STATUS, "committed_inputs": inputs,
        "administrative_inputs": admin,
        "external_primary": {
            "title": "Hypersurfaces with degenerate duals and the geometric complexity theory program",
            "authors": "J. M. Landsberg, Laurent Manivel, Nicolas Ressayre",
            "version": "arXiv:1004.4802v1, 2010-04-27",
            "url": "https://arxiv.org/pdf/1004.4802v1",
            "archive": "results/b26_10a/LMR_1004.4802v1.pdf",
            "bytes": len(pdf), "sha256_raw_binary_pdf": digest(pdf),
            "read_label": "PRIMARY at statement level",
            "read_extent": "printed pages 4-6: Theorem 2.3.1, section 3.1, Theorem 3.1.1 and following paragraph; title/version header",
            "method": "web source, pypdf extraction from these exact archived bytes, and local render inspection",
            "proofs_audited": False, "journal_version_read": False,
        }
    })
    (OUT / "PROPOSED_DELIVERY_PATHS.txt").write_bytes(("\n".join(PATHS) + "\n").encode())
    receipt = {
        "slot": "B26-10A", "status": STATUS,
        "utc_start_first_tool_record_after_brief_reading": START,
        "utc_preflight_completed": "2026-09-23T02:44:34Z",
        "utc_incremental_checkpoint": "2026-09-23T02:46:01Z",
        "utc_substantive_stop_and_early_final_checkpoint": SUBSTANTIVE_STOP,
        "elapsed_seconds_including_interleaved_administration": 602,
        "checkpoint_30_minutes": "not reached; every item decided and substantive work stopped early",
        "ceiling_minutes": 60, "interruptions": [], "deducted_seconds": 0,
        "pilots": 0, "mathematical_programs": 0, "subagents": 0,
        "other_sessions_contacted": 0, "compute_lease": "none",
        "administrative_operations": [
            "read-only Git with command-scoped safe.directory; no persistent configuration changes",
            "file inventory and SHA-256 hashing",
            "public-source PDF retrieval; sandbox socket failure then approved normal-account retry",
            "pypdf text extraction; UTF-8 retry after output-encoding failure",
            "Poppler renders of source pages 4-6, inspected and then removed",
            "Markdown report authoring and escape-format repair",
            "JSON receipt/manifest generation and raw-byte verification",
        ],
        "prohibited_mutations_performed": [],
        "limitations": "No computation or certificate replay; no LMR full-proof audit; no paper or ledger edit."
    }
    write_json(OUT / "resource_receipt.json", receipt)
    # Create a complete packet before capturing the final status inventory.
    seal_manifest()
    snapshot = verify()
    close = now()
    footer = (
        "\n### Final clock and verification\n\n"
        f"- **Substantive stop / early-final checkpoint:** {SUBSTANTIVE_STOP}. "
        "Elapsed time from the recorded start: **10m02s**, including interleaved administration; "
        "no interruption deductions. The 30-minute checkpoint was not reached.\n"
        f"- **Packet administrative close:** {close}.\n"
        "- Final read-only checks: branch and HEAD unchanged; zero tracked/staged changes; "
        "the pre-existing inventory remains 10,383 default-status entries / 20,761 individual files. "
        "These counts are inventory checks, not a fresh hash audit of every unrelated file.\n"
        "- All twelve committed input bindings and the three preflight administrative hashes "
        "were rechecked; all six payloads are bound by the manifest, and the seven-path delivery "
        "list matches exactly. Every packet path is untracked.\n"
        "- **Part 1 ACCEPT; Part 2 ACCEPT**, with the scope and source limitations above. "
        "Recommended flag action: **remove the length-restriction flag** after separate "
        "delivery/adjudication. No paper edit was made.\n"
    )
    current = REPORT.read_text(encoding="utf-8").split("\n### Final clock and verification")[0]
    REPORT.write_bytes((current.rstrip() + "\n" + footer).encode("utf-8"))
    receipt["utc_packet_administrative_close"] = close
    receipt["final_status"] = snapshot
    receipt["verified_payloads"] = 6
    receipt["delivery_paths"] = 7
    write_json(OUT / "resource_receipt.json", receipt)
    seal_manifest()
    return verify()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--seal", action="store_true")
    mode.add_argument("--verify-only", action="store_true")
    args = parser.parse_args()
    snapshot = seal() if args.seal else verify()
    manifest_data = (OUT / "MANIFEST.json").read_bytes()
    print(json.dumps({
        "result": "PASS", "mode": "seal" if args.seal else "verify-only",
        "utc_check": now(), "payloads_verified": 6, "delivery_paths": 7,
        "manifest_sha256_raw": digest(manifest_data), "manifest_bytes": len(manifest_data),
        "status": snapshot,
    }, indent=2))

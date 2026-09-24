"""Administrative byte binding and PDF text extraction; no mathematical computation.

Third-party PDFs and their extracted text stay in the temporary directory.
Payload JSON is deterministic. Timing metadata appears only in the resource receipt.
"""
import argparse
import hashlib
import json
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "results/b28_02"
COMMIT = "96a8074d240033161302233672aed5980d84eccb"


def binding(data):
    return {"sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}


def write_json(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")


def git(*args):
    return subprocess.check_output(["git", "-c", f"safe.directory={ROOT.as_posix()}", "-C", str(ROOT), *args])


def extract(folder):
    from pypdf import PdfReader
    for pdf in sorted(pathlib.Path(folder).glob("*.pdf")):
        pages = PdfReader(pdf).pages
        text = "\n".join(f"\n--- PDF PAGE {i + 1} ---\n{page.extract_text()}" for i, page in enumerate(pages))
        pdf.with_suffix(".txt").write_text(text, encoding="utf-8", newline="\n")
        print(json.dumps({"id": pdf.stem, "pages": len(pages), **binding(pdf.read_bytes())}))


def render(folder):
    import pdfplumber
    for name, number in [("DW2000", 4), ("LMR", 9), ("HThesis2017", 113)]:
        path = pathlib.Path(folder) / f"{name}.pdf"
        with pdfplumber.open(path) as pdf:
            dest = path.with_name(f"{name}_page_{number}.png")
            pdf.pages[number - 1].to_image(resolution=120).save(str(dest))
            print(dest)


def inputs():
    paths = {
        "results/b27_05/REPORT.md": "Entire report, including exact image map and feasibility conclusion",
        "docs/b27_01_report.md": "Entire report; in particular class (iii) and distinction between closure and literal image",
        "docs/batch_closes/BATCH27_CLOSE.md": "Entire close; standing conventions and carried questions L3/L5/L7",
        "docs/s56_report.md": "Sections 1-2 (image map and Gram rank), section 4 (relations), section 5 (cost), section 6 (certificates); calibration is historical READ only",
        "docs/s38_review.md": "Sections 1-2; exhaustive length-five occurrence screen through degree ten",
    }
    entries = []
    for path, scope in paths.items():
        data = git("show", f"{COMMIT}:{path}")
        entries.append({"commit": COMMIT, "path": path, "git_blob": git("rev-parse", f"{COMMIT}:{path}").decode().strip(), **binding(data), "label": "READ", "read_extent": scope})
    write_json(OUT / "INPUT_BINDINGS.json", {"hash_semantics": "SHA-256 of raw committed blob payload, excluding the Git object header; not working-copy or decoded text bytes", "inputs": entries})
    print(json.dumps(entries, indent=2))


def sources(folder):
    registry = json.loads((OUT / "SOURCES.json").read_text(encoding="utf-8"))
    for source in registry["sources"]:
        if source.get("local_filename"):
            path = pathlib.Path(folder) / source["local_filename"]
            source.update(binding(path.read_bytes()))
    write_json(OUT / "SOURCES.json", registry)
    print("Source byte bindings updated.")


def receipt(folder):
    folder = pathlib.Path(folder)
    registry = json.loads((OUT / "SOURCES.json").read_text(encoding="utf-8"))
    artifacts = []
    for source in registry["sources"]:
        path = folder / source["local_filename"]
        actual = binding(path.read_bytes())
        assert actual == {key: source[key] for key in ("sha256", "bytes")}, source["id"]
        artifacts.append({"id": source["id"], "input_pdf": actual,
                          "output_text": binding(path.with_suffix(".txt").read_bytes())})
    rendered = [{"file": p.name, **binding(p.read_bytes())} for p in sorted(folder.glob("*_page_*.png"))]
    first = ["DM2017", "DM2020", "HL2016", "IQS2015", "LMR", "SVB1999"]
    second = first + ["ASS2022", "BI2015", "CIM2015", "HK2025"]
    third = second + ["DW2000", "H2017"]
    obj = {
        "slot": "B28-02", "label": "READ (administrative receipt)",
        "resource_policy": {"session_ceiling_minutes": 90, "scheduled_checkpoint_minutes": 45,
                            "maximum_mathematical_runs": 10, "per_mathematical_run_seconds": 60,
                            "per_mathematical_run_megabytes": 512},
        "mathematical_runs": [], "mathematical_run_count": 0,
        "computation_scope": "No ranks, symbolic algebra, numerical experiments, random searches, or new mathematical certificates. Historical computations were read only.",
        "installs": 0, "subagents": 0, "other_sessions": 0,
        "clock_observations": {"preflight_utc": "2026-09-24 11:51:02 UTC",
                               "completion_checkpoint_utc": "2026-09-24 12:05:05 UTC",
                               "seconds_between_samples": 843,
                               "note": "The control-file read preceded the first clock sample; its duration was not separately measured. The literature audit reached an early completion checkpoint, so the 45-minute checkpoint was not reached."},
        "python": "C:/Users/swami/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe",
        "script": "analysis/b28_02_provenance.py", "temporary_source_directory": folder.as_posix(),
        "timing_semantics": "Observed exec tool wall_time_seconds for each enclosing shell invocation; these are upper bounds on individual subcommands when a shell included additional downloads or reads. PDF processing is administrative IO, not a mathematical run. Peak memory was not measured and no mathematical resource certificate is claimed for IO.",
        "binding_semantics": "The following inventory binds the final temporary PDF-extraction artifacts used for reading. Input IDs resolve to their raw PDF SHA-256 and bytes here and in SOURCES.json. Earlier extraction passes were superseded by the final pass; their transient output bytes were not separately archived. No third-party artifact is delivered.",
        "administrative_runs": [
            {"command": "python analysis/b28_02_provenance.py extract <temporary_source_directory>", "input_ids": first, "output": "Same-ID output_text entries", "shell_wall_seconds": 2.210089},
            {"command": "python analysis/b28_02_provenance.py extract <temporary_source_directory>", "input_ids": second, "output": "Same-ID output_text entries", "shell_wall_seconds": 4.6733866, "other_shell_work": "Source reads and text searches"},
            {"command": "python analysis/b28_02_provenance.py extract <temporary_source_directory>", "input_ids": third, "output": "Same-ID output_text entries", "shell_wall_seconds": 7.4410823, "other_shell_work": "Dissertation download"},
            {"command": "python analysis/b28_02_provenance.py render <temporary_source_directory>; python analysis/b28_02_provenance.py inputs", "input_ids": ["DW2000", "LMR", "H2017"], "other_inputs": "Five committed blobs in INPUT_BINDINGS.json", "output": "Rendered-page entries below; initial INPUT_BINDINGS.json later superseded by a corrected read-extent description", "shell_wall_seconds": 1.3911798},
            {"command": "python analysis/b28_02_provenance.py extract <temporary_source_directory>", "input_ids": third + ["M2015"], "output": "All output_text entries", "shell_wall_seconds": 7.1620566, "other_shell_work": "Makam PDF download"},
            {"command": "python analysis/b28_02_provenance.py inputs", "input": "Raw committed blobs bound in INPUT_BINDINGS.json", "output": {"path": "results/b28_02/INPUT_BINDINGS.json", **binding((OUT / "INPUT_BINDINGS.json").read_bytes())}, "shell_wall_seconds": 0.6260803}
        ],
        "temporary_extraction_artifacts": artifacts, "temporary_rendered_artifacts": rendered,
        "packaging": "receipt validates downloaded source hashes; manifest binds delivered payloads; verify checks raw bytes and Git filter parity. These administrative packaging operations are not mathematical runs. No timing fields are inserted into the manifest or report.",
        "checkpoint": "CHECKPOINT.md", "outcomes": {"2a": "B", "2b": "B", "2c": "complete"},
        "achievement": "PRIMARY/READ literature audit with HAND applicability assessments; no new mathematical achievement or record change"
    }
    write_json(OUT / "RESOURCE_RECEIPT.json", obj)
    print("Resource receipt written; all 13 raw PDF source bindings verified.")


def manifest(verify):
    paths = [ROOT / "docs/b28_02_report.md", ROOT / "analysis/b28_02_provenance.py"]
    paths += sorted(p for p in OUT.rglob("*") if p.is_file() and p.name != "MANIFEST.json")
    payloads = [{"path": p.relative_to(ROOT).as_posix(), **binding(p.read_bytes())} for p in paths]
    obj = {"slot": "B28-02", "hash_semantics": "Raw file bytes; SHA-256; manifest excludes itself", "payloads": payloads}
    dest = OUT / "MANIFEST.json"
    if verify:
        assert json.loads(dest.read_text(encoding="utf-8")) == obj, "Manifest mismatch"
        for entry in payloads + [{"path": "results/b28_02/MANIFEST.json"}]:
            path = entry["path"]
            assert git("hash-object", path) == git("hash-object", "--no-filters", path), path
        print("All manifest bindings and Git filter parity checks passed.")
    else:
        write_json(dest, obj)
    print(json.dumps({"manifest": str(dest), **binding(dest.read_bytes()), "payload_count": len(payloads)}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("operation", choices=["extract", "render", "inputs", "sources", "receipt", "manifest", "verify"])
    parser.add_argument("folder", nargs="?")
    args = parser.parse_args()
    if args.operation == "extract":
        extract(args.folder)
    elif args.operation == "render":
        render(args.folder)
    elif args.operation == "inputs":
        inputs()
    elif args.operation == "sources":
        sources(args.folder)
    elif args.operation == "receipt":
        receipt(args.folder)
    else:
        manifest(args.operation == "verify")

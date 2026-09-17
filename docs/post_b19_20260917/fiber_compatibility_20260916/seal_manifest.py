"""Hash the new evidence and read-only mathematical/code inputs."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def entry(path):
    raw = path.read_bytes()
    return {"path": path.relative_to(ROOT).as_posix(), "bytes": len(raw),
            "sha256": hashlib.sha256(raw).hexdigest()}


inputs = [
    ROOT / "work/extension_descent_20260916/REPORT.md",
    ROOT / "work/batch15_workers/B15-02/docs/b17_02_report.md",
    ROOT / "work/batch15_workers/B15-02/docs/b18_02_report.md",
    ROOT / "work/batch15_workers/B15-02/analysis/b18_02_carrier.py",
    ROOT / "work/batch15_workers/B15-02/analysis/b15_bound.py",
]
files = sorted(p for p in HERE.rglob("*") if p.is_file()
               and p.name != "MANIFEST.json" and "__pycache__" not in p.parts
               and p.suffix != ".pid")
record = {"date": "2026-09-16", "claim": "nonzero five-row fiber test; zero arc increment in the tested cell",
          "artifacts": [entry(p) for p in files], "read_only_inputs": [entry(p) for p in inputs],
          "primary_reference": {"title": "The ideal of relations for the ring of invariants of n points on the line",
                                "authors": "Howard, Millson, Snowden, Vakil",
                                "location": "Lemma 6.6, printed page 33",
                                "url": "https://ems.press/content/serial-article-files/31806"}}
(HERE / "MANIFEST.json").write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"artifacts": len(files), "read_only_inputs": len(inputs)}))

"""Pin inputs and outputs of work/claude_image_ceiling_20260916 by SHA-256. Run after REPORT.md is final."""
import hashlib, json, os, time
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()
inputs = [
 "Claude_Handover_B15_B18/CLAUDE_DESCENT_FOLLOWUP_20260916.md",
 "work/descent_followup_claude_20260916/REPORT.md",
 "work/extension_descent_20260916/REPORT.md",
 "work/fiber_compatibility_20260916/REPORT.md",
 "work/batch15_workers/B15-12/docs/b18_12_coefficient_algebra.md",
 "work/batch15_workers/B15-08/docs/b17_08_report.md",
 "work/batch15_workers/B15-03/docs/b17_03_report.md",
 "work/batch15_workers/B15-01/docs/b18_01_report.md",
 "work/batch15_workers/B15-06/docs/b18_06_sweep.md",
 "work/batch13_astra/B13-02/docs/d5_ideal.md",
 "work/batch13_astra/B13-02/docs/transfer_lemma.md",
 "work/batch13_astra/B13-02/docs/session_28.md",
 "work/batch13_astra/B13-02/docs/det_onset.md",
 "work/batch13_astra/B13-02/paper/det3-conductor.tex",
 "Batch17_Planning/symmetry_dream/astra/toy_character_screen_d5_d6.json",
 "Batch17_Planning/symmetry_dream/astra/toy_character_screen.py",
 "work/batch15_workers/B15-02/analysis/b15_bound.py",
 "work/batch15_workers/B15-02/.venv/python.exe",
]
outputs = ["REPORT.md", "checks/c1_pieri_transfer.py", "checks/c2_residue_length6.py",
           "results/c1_pieri_transfer.json", "results/c2_residue_length6.json",
           "results/logs/c1_pieri_transfer_resources.json", "results/logs/c2_residue_length6_resources.json",
           "results/logs/c1_pieri_transfer.pid", "results/logs/c2_residue_length6.pid", "seal_manifest.py"]
man = {
 "session": "claude_image_ceiling_20260916", "sealed_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
 "note": "REPORT.md finalized before hashing. Inputs are read-only historical files; outputs are this directory only. "
         "Wrapper: b15_bound.py unchanged, caps 60 s / 512 MiB, one worker, one BLAS thread. Runtime: B15-02 .venv Python 3.12.10.",
 "inputs": {p: sha(ROOT / p) for p in inputs},
 "outputs": {p: sha(HERE / p) for p in outputs},
 "checks": {"c1": json.load(open(HERE / "results/logs/c1_pieri_transfer_resources.json")),
            "c2": json.load(open(HERE / "results/logs/c2_residue_length6_resources.json"))},
}
(HERE / "MANIFEST.json").write_text(json.dumps(man, indent=1) + "\n")
print(json.dumps({"inputs": len(man["inputs"]), "outputs": len(man["outputs"]),
                  "wrapper": man["inputs"]["work/batch15_workers/B15-02/analysis/b15_bound.py"][:16],
                  "report": man["outputs"]["REPORT.md"][:16]}))

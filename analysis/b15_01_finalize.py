"""Archive B15-01 backend receipts and write an explicit staging inventory."""
import gzip
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"results/b15_01"
LOGS=ROOT/"results/logs"


def main():
    # Runtime and integrator smoke records are setup provenance, not research.
    excluded=("b15_01_runtime", "b15_01_integrator_smoke")
    receipts={}
    for path in sorted(LOGS.glob("b15_01_*.json")):
        if path.name.startswith(excluded) or path.name.endswith("_resources.json"):
            continue
        data=json.loads(path.read_text(encoding="utf-8-sig"))
        if "plan" in data and "pid" in data:
            receipts[path.name]=data
    (OUT/"backend_receipts.json.gz").write_bytes(gzip.compress(json.dumps(receipts,separators=(",",":"),sort_keys=True).encode(),mtime=0))
    # Retain even a per-call PID whose interrupted evaluation produced no
    # completed JSON receipt. Parent bounded-run PID files remain separate.
    backend_pids={}
    for path in sorted(LOGS.glob("b15_01_*.pid")):
        if path.name.startswith(excluded) or (LOGS/(path.stem+"_resources.json")).exists():
            continue
        backend_pids[path.name]=dict(pid=int(path.read_text().strip()),
                                    completed_receipt=(path.stem+".json") in receipts)
    (OUT/"backend_pid_records.json").write_text(json.dumps(backend_pids,indent=2)+"\n",encoding="utf-8")
    resources={}
    for path in sorted(LOGS.glob("b15_01_*_resources.json")):
        if not path.name.startswith(excluded):
            resources[path.name]=json.loads(path.read_text(encoding="utf-8-sig"))
    (OUT/"run_resources.json").write_text(json.dumps(resources,indent=2)+"\n",encoding="utf-8")
    stages=["results/PREREG_b15_01.md", "docs/b15_01_report.md", "docs/b15_01_proved.md",
            "tools/verify/b15_01_ci159.py", "tools/verify/verify.py"]
    stages += [p.relative_to(ROOT).as_posix() for p in sorted((ROOT/"analysis").glob("b15_01_*.py"))]
    stages += [p.relative_to(ROOT).as_posix() for p in sorted(OUT.rglob("*"))
               if p.is_file() and not any(v in {"cache","verification_cache","__pycache__"} for v in p.relative_to(OUT).parts)
               and p.name not in {"stage_paths.txt","delivery_inventory.json"} and not p.name.endswith(".tmp")]
    for suffix in (".log","_resources.json",".pid"):
        for path in sorted(LOGS.glob("b15_01_*"+suffix)):
            if path.name.startswith(excluded):
                continue
            # Backend per-call PID receipts are included in the compressed
            # archive above; retain the bounded runner PID files separately.
            if suffix==".pid" and not (LOGS/(path.stem+"_resources.json")).exists():
                continue
            stages.append(path.relative_to(ROOT).as_posix())
    stages += ["results/b15_01/stage_paths.txt","results/b15_01/delivery_inventory.json"]
    stages=sorted(set(stages))
    (OUT/"stage_paths.txt").write_text("\n".join(stages)+"\n",encoding="utf-8")
    inventory={}
    for name in stages:
        if name=="results/b15_01/delivery_inventory.json":
            continue
        p=ROOT/name
        if not p.is_file():
            raise ValueError("Intended delivery file absent: "+name)
        raw=p.read_bytes()
        if len(raw)>=5_000_000:
            raise ValueError("Delivery size limit: "+name)
        inventory[name]=dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
    (OUT/"delivery_inventory.json").write_text(json.dumps(dict(files=inventory,
        hash_basis="working-file bytes before Git text normalization; the external delivery manifest checks the committed bundle",
        excludes="pre-existing setup logs and reproducible backend tensor caches",backend_receipt_count=len(receipts)),indent=2)+"\n",encoding="utf-8")
    print(json.dumps(dict(intended_files=len(stages),backend_receipts=len(receipts),maximum_bytes=max(x["bytes"] for x in inventory.values()))))


if __name__=="__main__":
    main()

"""Integration controls on a relocated receiver payload, under b15_bound."""
import copy
import hashlib
import json
import os
from pathlib import Path
import runpy
import shutil
import time

OWN=Path(__file__).resolve().parents[1]
OUT=OWN/"results/b16_11"


def main():
    if "CI73_DEADLINE" not in os.environ: raise RuntimeError("resource wrapper required")
    stamp=str(os.getpid())
    relocated=OUT/("relocated_control_"+stamp)
    # Preserve each control artifact; never alter the delivery or old evidence.
    shutil.copytree(OWN/"delivery/b16_11",relocated)
    ns=runpy.run_path(str(relocated/"b16_11_receiver.py"),run_name="receiver_control")
    start=time.perf_counter()
    result=ns["verify"](relocated)
    checks=[dict(name="relocated_portable_payload",status="PASS",payload_files=result["payload_files"],
                 live_input_access=False)]
    m=json.loads((relocated/"INPUT_HASHES.json").read_text())
    target=relocated/m["inputs"][0]["copy"]
    old=target.read_bytes()
    target.write_bytes(bytes([old[0]^1])+old[1:])
    try:
        ns["verify"](relocated)
    except ValueError as exc:
        if "hash mismatch" not in str(exc): raise
        checks.append(dict(name="same_length_payload_byte_corruption",status="REJECTED_AS_REQUIRED",reason=str(exc)))
    else: raise RuntimeError("corruption was admitted")
    finally: target.write_bytes(old)
    original_manifest=(relocated/"INPUT_HASHES.json").read_bytes()
    m["inputs"][0]["sha256"]="0"*64
    (relocated/"INPUT_HASHES.json").write_text(json.dumps(m))
    try:
        ns["verify"](relocated)
    except ValueError as exc:
        checks.append(dict(name="manifest_hash_mutation",status="REJECTED_AS_REQUIRED",reason=str(exc)))
    else: raise RuntimeError("manifest mutation admitted")
    finally: (relocated/"INPUT_HASHES.json").write_bytes(original_manifest)
    valid=dict(exit_code=0,job_object_enforced=True,workers=1,blas_threads=1,
               wall_seconds=0.1,wall_cap_seconds=60,memory_cap_mb=512,
               job_memory=dict(peak_job_memory=20*1024**2))
    for name,changes in (("incomplete_timeout_receipt",dict(exit_code=None)),
                         ("resource_overrun",dict(wall_seconds=61)),
                         ("unleased_heavy_caps",dict(wall_cap_seconds=900,memory_cap_mb=1536))):
        bad=copy.deepcopy(valid); bad.update(changes)
        try: ns["check_resources"](bad)
        except ValueError as exc:
            checks.append(dict(name=name,status="REJECTED_AS_REQUIRED",reason=str(exc)))
        else: raise RuntimeError("resource mutation admitted")
    checks+=result["controls"]
    record=dict(status="PASS",checks=checks,control_count=len(checks),
                relocated_path=str(relocated),seconds=time.perf_counter()-start,
                semantic_scope="Metadata/conditional-bound receiver only; no inherited mathematical implementation ran.")
    (OUT/"integration_controls.json").write_text(json.dumps(record,indent=2)+"\n")
    print(json.dumps({k:record[k] for k in ("status","control_count","seconds")}))


if __name__=="__main__": main()

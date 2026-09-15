"""Record exact external mathematical inputs and produce local delivery hashes."""
from pathlib import Path
import json,hashlib,sys,platform
import flint
from b16_04_filtration import ROOT,HERE,OUT,EVIDENCE,dump

def digest(p):
    p=Path(p).resolve()
    return {'path':str(p),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}

def inputs():
    paths=[ROOT/'Batch16/BOARD.md',ROOT/'Batch16/launch/INPUT_MANIFEST.json',
      ROOT/'Batch16/launch/B16-04.md',ROOT/'Batch16/launch/runtime_04.json',
      ROOT/'Batch15_Launch/native_20260913/INTAKE.json',
      *[EVIDENCE/n for n in ('REPORT.md','integrator_review.json','input_receipt.json','verify_small.py','small_evidence.json')],
      ROOT/'Batch15_Launch/native_20260913/equation_review/astra/REVIEW.md',
      ROOT/'work/batch15_workers/B15-06/docs/b15_06_proved.md',
      ROOT/'work/batch15_workers/B15-05/docs/b15_05_report.md',
      ROOT/'work/batch15_workers/B15-05/docs/b15_05_proved.md',
      ROOT/'Batch16/reviews/02/integrator_review.json',
      HERE/'analysis/b15_bound.py',Path(sys.executable)]
    paths += [p for p in (HERE/'.venv/pyvenv.cfg',HERE/'.venv/python312._pth',HERE/'.venv/python312.dll') if p.exists()]
    # Include the installed FLINT Python/native modules actually loaded by this
    # receiver's inherited evaluator. Standard-library identity is Python version.
    paths += sorted({Path(m.__file__).resolve() for name,m in sys.modules.items()
                     if name.startswith('flint') and getattr(m,'__file__',None)})
    record={'status':'EXACT_NATIVE_BYTES','inputs':[digest(p) for p in paths],
      'runtime':{'python':sys.version,'executable':sys.executable,'flint':flint.__version__,'platform':platform.platform()},
      'attribution':'B16 derivation gpt-6-astra/xhigh; Hessian11 evaluator gpt-6-astra; bracket normalization Claude Opus 5.',
      'scope':'Files whose contents were read or used as mathematical/provenance/runtime inputs. Inventoried filenames are not mathematical inputs. Runtime standard-library identity is recorded by Python version rather than recursive stdlib hashing.',
      'frozen_slot04_head':'3d3f9f8b427f257a0d5db678b1645212033652ff',
      'git_binding':'Inherited launch manifest only; no fresh Git operation.'}
    launch=json.loads((ROOT/'Batch16/launch/INPUT_MANIFEST.json').read_text())
    expected={x['path']:x['sha256'] for x in launch['inputs']}
    for item in record['inputs']:
        if item['path'] in expected: assert item['sha256']==expected[item['path']]
    dump('input_hashes.json',record)
    print(json.dumps({'inputs':len(record['inputs']),'frozen_input_hashes_match':True}))

if __name__=='__main__': inputs()

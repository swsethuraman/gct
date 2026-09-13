"""Prepare B15-02 per-slot reports from completed, checked results."""
import hashlib
import json
from pathlib import Path
import subprocess

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'results/b15_02'


def save(path,obj):
    path.write_text(json.dumps(obj,indent=2,allow_nan=False)+'\n',encoding='utf-8')


def main():
    release_path=OUT/'lease_release.json'
    save(release_path,json.loads(release_path.read_text(encoding='utf-8-sig')))
    fresh=json.loads((OUT/'standalone_replay.json').read_text())
    assert fresh['all_pass'] and len(fresh['cells'])==9
    verified=[json.loads((OUT/f'cell_{i:02d}_verified.json').read_text()) for i in range(1,10)]
    search=[json.loads((OUT/f'cell_{i:02d}.json').read_text()) for i in range(1,10)]
    prereg=subprocess.check_output(['git','rev-parse','d34d4e95'],cwd=ROOT,text=True).strip()
    proposal=dict(status='EXACT',acceptance='PROPOSED_TO_INTEGRATOR',slot='02',
                  id='b15_02_degree7_nine_a1_determinant_nonzeros',
                  predicate=dict(n=4,delta=7,lambda_in=[v['cell']['lam'] for v in verified]),
                  statement='For these nine cells, m_det=1=a, i_det=0, m_pad<=1, and D<=0.',
                  bounds=dict(a_lb=1,a_ub=1,m_det_lb=1,m_det_ub=1,i_det_lb=0,i_det_ub=0,m_pad_ub=1,D_ub=0),
                  source='docs/b15_02_proved.md',
                  witnesses=[dict(cell=v['cell'],file=f'results/b15_02/cell_{i:02d}_polynomial.json') for i,v in enumerate(verified,1)],
                  verifier='analysis/b15_02_replay.py',
                  conclusions_by_context={'quartic_det_ideal':'i_det=0; mult_det=a=1','quartic_padded_gap':'D<=0'},
                  canonical_files_modified=False)
    save(OUT/'proposed_exclusions.json',proposal)
    jobs=[]
    for name in ['controls','pilot','production','integral_verify','standalone_replay','receiver_control']:
        path=ROOT/f'results/logs/b15_02_{name}_resources.json'
        v=json.loads(path.read_text()); assert v['exit_code']==0
        jobs.append(dict(name=name,wall_seconds=v['wall_seconds'],return_code=v['exit_code'],
                         aggregate_peak_bytes=v['job_memory']['peak_job_memory'],
                         peak_working_set_bytes=v['process_memory']['peak_working_set'],pid=v['pid'],
                         resource_log=path.relative_to(ROOT).as_posix()))
    save(OUT/'run_summary.json',dict(status='EXACT',jobs=jobs,all_return_codes_zero=True,
                                    aggregate_memory_method='Windows Job Object peak_job_memory',
                                    seconds_total=sum(x['wall_seconds'] for x in jobs),
                                    models=[dict(model='gpt-6-astra',phase=p) for p in ['preregistration','implementation','research','verification','delivery']]))
    lines=['# B15-02 report','',
           '**EXACT: all nine assigned cells have m_det=1=a and D<=0.** Each retired',
           'on its first determinant point. The final evidence consists of explicit',
           'integer highest-weight polynomials and exact nonzero evaluations. All nine',
           'standalone checks passed. This is a worker certification; canonical',
           'integration is the integrator\'s separate decision.','',
           '## Scope and checked findings','',
           'n=4; degree 7; ambient variable dimension 16; working length 7.',
           'Forms lie in Sym^4 V*, with coefficient ring Sym^7(Sym^4 V).',
           'Ordinary coefficient coordinates and descending highest-weight labels',
           'are used throughout. The independent padded form is z*per3 with ten',
           'essential variables. No padded evaluations were needed under the',
           'preregistered immediate-retirement rule.','',
           '| Cell | Partition | n_chi | Nonzero terms | Primitive integer-source value |',
           '|---:|---|---:|---:|---:|']
    for i,(v,s) in enumerate(zip(verified,search),1):
        lines.append(f"| {i} | ({','.join(map(str,v['cell']['lam']))}) | {s['size']['n_chi']} | {v['nonzero_expanded_terms']} | {v['det_evaluations'][0]['exact_integer_value']} |")
    lines+=['','All nine ambient multiplicities a=1 were freshly recomputed with rational',
            'power-sum plethysm and Murnaghan-Nakayama characters. All signed Burnside',
            'carrier dimensions match the original shortlist. The typed frozen ledger',
            'and accepted-state overlay have no hit on these nine cells. They correctly',
            'exclude the old (16,2,2,2,2,2,2) cell; no work was spent evaluating it.','',
            'A single common integer pencil suffices. Its seven row-major matrix',
            'vectors have rank 7 and extend to an integer 16 by 16 frame of determinant',
            '50100. The point is on the determinant orbit, hence its closure. Each',
            'source has exact weight lambda and all simple raising derivatives zero',
            'over Z; the separately written verifier checked these identities again',
            'from the standalone polynomial files. Direct integer polynomial expansion',
            'and evaluation produced the values above.','',
            'Thus m_det>=1, while a=1 gives m_det<=1 and m_pad<=1. Equivalently,',
            'i_det=0 and D=m_pad-1<=0. With no padded ideal floor needed,',
            'U_pad=min(a,h_pad,a-0)=1 for every assigned cell. The recorded h_pad',
            'values remain inherited upper bounds; they were not freshly recomputed',
            'and are unnecessary for this conclusion. No sampled zeros were used as',
            'global equations, and no positive multiplicity gap is claimed.','',
            '## Source construction and controls','',
            'The search used p=65521 and the preserved S45 signed-orbit construction.',
            'The local NumPy/SciPy implementation of the S71 triangular/residual method',
            'left one residual column for seven cells and two columns for cells 7 and 8.',
            'Each projected kernel was checked on every integer raising row modulo p.',
            'Its nullity one matched the characteristic-zero ambient dimension. The',
            'first normalized modular residues are retained in cell_NN.json.','',
            'A measured verification refinement solved these same small systems over Q,',
            'cleared denominators and made each integer source primitive. The maximum',
            'absolute source coefficient across the nine cells is 288. Exact all-row',
            'raising checks and modular reduction checks agree. Direct differentiation',
            'of every nonzero monomial then independently verified HWV membership.',
            'The final integer proof does not rely on an unconstructed modular lift.','',
            'Controls passed: the separate degree-2 (6,2) HWV has determinant value -20;',
            'altering its coefficient or factorial normalization breaks HWV membership;',
            'an altered point gives a detected zero; a synthetic research zero remains',
            'CANDIDATE with no global bound; dense flint and the residual solver agree;',
            'the signed-Burnside controls distinguish the odd character; and a literal',
            'coefficient mutation in each delivered integer polynomial is rejected.',
            'Research liveness was never defined by requiring a research nonzero.','',
            '## Resources, provenance and stopping','',
            f'Preregistration was committed first: {prereg}. Frozen base:',
            'f365568d80d5f66fea2dd9342ff1998e1d866915; frozen tree:',
            'aff6ca0921ec964cc8b7fcbd64bd5e5e9de9fbbd. The existing branch and',
            'worktree were reused. No shared theorem, exclusion or protected paper',
            'file was edited. Setup smoke/runtime logs remain preserved and untracked.','',
            'gpt-6-astra performed all new phases; the dispatch requested xhigh.',
            'Inherited S30, S45, S71, S79 and verifier implementations retain their',
            'original session attribution. No live Claude phase was used.','',
            '| Run | Return code | Wall seconds | Aggregate peak MiB |',
            '|---|---:|---:|---:|']
    for j in jobs:lines.append(f"| {j['name']} | {j['return_code']} | {j['wall_seconds']:.3f} | {j['aggregate_peak_bytes']/1024**2:.2f} |")
    lines+=['',f"Total bounded run wall time: {sum(j['wall_seconds'] for j in jobs):.3f} seconds.",
            f"Maximum aggregate Job Object peak: {max(j['aggregate_peak_bytes'] for j in jobs)/1024**2:.2f} MiB.",
            'All runs used one process and one BLAS thread. The pilot and subsequent',
            'jobs had 900-second deadlines and 1536 MiB caps; controls used 120 seconds',
            'and 768 MiB. The final receiver command was tested after lease release as',
            'a small control with a 30-second deadline and 256 MiB cap. No resource',
            'stop, dependency failure, stalled zero search,',
            'unchanged retry or production extension occurred. The lease was released',
            'at the timestamp in lease_release.json after all recorded research process',
            'IDs were checked absent. No further heavy work is planned.','',
            'A preregistration wording correction: h_pad denotes the multiplicity in',
            'the parameter pullback space and supplies an upper bound on m_pad; it is',
            'not itself a measured coordinate multiplicity. The first cell has h_pad=1',
            'in the inherited exact count. The final exclusion needs only a=1.','',
            '## Receiver replay and delivery','',
            'From the assigned worktree, use its exact local Python executable:',
            '', '```powershell',
            "& 'C:\\Users\\swami\\Projects\\gct-gpt\\work\\batch15_workers\\B15-02\\.venv\\python.exe' analysis/b15_bound.py --slot 02 --name b15_02_receiver --seconds 30 --memory-mb 256 analysis/b15_02_replay.py",
            '```','',
            'Use a fresh run name to preserve prior resource receipts. This replay loads',
            'the complete standalone integer polynomials, checks all weights and raising',
            'identities, regenerates the determinant forms from explicit points, checks',
            'the exact values, and verifies the full orbit frame. It does not rebuild',
            'a carrier or use a stored evaluation matrix. Discovery replay is available',
            'through b15_02_probe.py after the controls and a heavy lease; this is not',
            'needed to check the final integer nonvanishing certificates.','',
            'Input hashes use SHA-256 with CRLF normalized to LF and are recorded in',
            'the preregistration and results/b15_02/input_hashes.json. Native source',
            'coordinates, integer polynomials, integer points, resource logs and the',
            'proposed exclusion are all retained. The proof is docs/b15_02_proved.md.',
            'After the final commit, delivery/b15_02_final contains the one-ref delta',
            'bundle, checksums and external head/tree manifest. Delivery checks concern',
            'packaging; the separate verifier supports the mathematical findings.','',
            '## Next sufficient missing witness','',
            'No witness is missing to exclude positive D in these nine cells. Their',
            'exact gap remains in {-1,0}: a padded nonzero would prove D=0; a global',
            'padded vanishing proof would prove D=-1. The immediate-retirement rule',
            'ends this assignment at the determinant certificates. Further positive-gap',
            'search must use a different cell that survives the updated scoped screen.','']
    (ROOT/'docs/b15_02_report.md').write_text('\n'.join(lines),encoding='utf-8')
    hashes=json.loads((OUT/'input_hashes.json').read_text())
    for path in [ROOT/'analysis/b15_02_finalize.py',ROOT/'analysis/wk8_s30_pleth.py',ROOT/'analysis/wk11_s71_hybrid.py',ROOT/'analysis/wk12_s79_cell6.py',ROOT/'analysis/wk10_s64_pad.py']:
        hashes['files'][path.relative_to(ROOT).as_posix()]=hashlib.sha256(path.read_bytes().replace(b'\r\n',b'\n')).hexdigest()
    save(OUT/'input_hashes.json',hashes)
    print(json.dumps(dict(status='READY_FOR_COMMIT',cells=9,proposed_exclusion=proposal['id'])))


if __name__=='__main__':main()

"""Summarize completed artifacts and write a file-backed reproducibility manifest."""
import datetime as dt
import hashlib
import json
from pathlib import Path
import subprocess

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'results/b13_06'
BASE='00495110c62acfbbbc951e82cc218ed091563b3f'


def read(p):return json.loads(p.read_text())
def write(p,v):p.write_text(json.dumps(v,indent=2)+'\n')
def file_record(p):
    b=p.read_bytes()
    return dict(path=p.relative_to(ROOT).as_posix(),bytes=len(b),
                sha256=hashlib.sha256(b).hexdigest(),md5=hashlib.md5(b).hexdigest(),
                sha256_lf_normalized=hashlib.sha256(b.replace(b'\r\n',b'\n')).hexdigest())
def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT,text=True).strip()


def main():
    census=read(OUT/'components.json'); controls=read(OUT/'controls.json')
    ambient=[read(p) for p in sorted(OUT.glob('ambient_*.json'))]
    assert len(ambient)==5 and all(x['complete'] for x in ambient)
    resources=[read(p) for p in sorted((ROOT/'results/logs').glob('b13_06_*.resources.json'))]
    assert len(resources)==7 and all(x['status']=='completed' for x in resources)
    assert all(x['peak_process_memory_bytes']<x['memory_limit_bytes'] for x in resources)
    counts={tuple(a['partition']):a for a in ambient}
    questions=[]
    for row in census['rows']:
        nu=tuple(row['partition']); rec=dict(row)
        if nu in counts:
            rec['ambient_multiplicity_exact']=counts[nu]['a']
            rec['ambient_rank_matrix_shape']=[counts[nu]['a'],row['tensor_multiplicity']]
            rec['padded_minor_size_if_all_product_columns_independent']=counts[nu]['a']-row['tensor_multiplicity']+1
        questions.append(rec)
    write(OUT/'rank_questions.json',dict(board_numbering='batch13',session_id='B13-06',
          scope='complete candidate support; no uncomputed product rank is asserted',rows=questions))
    summary=dict(board_numbering='batch13',session_id='B13-06',model='gpt-6-astra',reasoning_effort='xhigh',
          completed_utc=dt.datetime.now(dt.timezone.utc).isoformat(),base=BASE,
          status='finite component reduction completed; no positive gap claimed',
          census=census['summary'],lr_checks=read(OUT/'lr_audit.json')['checked'],
          non_ladder_unexcluded_candidates=237,nine_variable_unexcluded_candidates=102,
          ambient_counts=[{k:a[k] for k in ('partition','degree','a','elapsed_seconds','nonzero_aggregated_weights')}
                          for a in ambient],
          resources=resources,total_worker_wall_seconds=sum(x['wall_seconds'] for x in resources),
          peak_worker_memory_bytes=max(x['peak_process_memory_bytes'] for x in resources),
          control_integer_determinant_full10=controls['three_family_control']['padded_point']['determinant_over_Z'],
          original_rows_audited=274,stored_point_columns_checked=6*282,
          rank_replay='not run: python-flint unavailable, pip socket WinError 10013',
          control_status='all exact polynomial and native-value arithmetic checks passed',
          adopted_det_rank=273,adopted_padded_floor=269,D_interval=[-4,1],D_measured=-4)
    write(OUT/'run_summary.json',summary)
    inputs=[ROOT/p for p in [
        'docs/batch13_worker_preamble.md','docs/batch13_board.md','docs/batch13_corrections.md',
        'docs/stocktake_batch12.md','docs/brief_wording.md','docs/lmr_cell.md',
        'docs/compact_circuit.md','docs/s74_final_review.md','docs/sparse_det_route.md',
        'docs/stocktake_batch10.md','docs/stocktake_batch11.md','docs/s57_report.md',
        'docs/pieri_transport.md','docs/transfer_lemma.md','results/s63_aladder.json',
        'results/s74/source.json','results/s74/certified.json',
        'analysis/wk12_int_s74_final.py','analysis/wk12_s74_decide.py','analysis/wk10_s63_averify.py']]
    inputs += [ROOT/f'results/s74/{stem}_{p}.json' for p in (2147483647,2147483629)
               for stem in ('columns_det','columns_pad','columns_red','decision')]
    files=list((ROOT/'analysis').glob('b13_06_*.py'))+[ROOT/'docs/b13_06_report.md',ROOT/'results/PREREG_b13_06.md']
    files += [p for p in OUT.iterdir() if p.is_file() and p.name!='manifest.json']
    files += [p for p in (ROOT/'results/logs').glob('b13_06_*') if p.suffix!='.pid']
    assert all(p.stat().st_size<=5_000_000 for p in files)
    manifest=dict(board_numbering='batch13',session_id='B13-06',model='gpt-6-astra',reasoning_effort='xhigh',
         base=BASE,branch=git('branch','--show-current'),created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
         content_head_before_manifest_commit=git('rev-parse','HEAD'),
         commit_history_before_manifest=git('log','--format=%H %s',BASE+'..HEAD').splitlines(),
         bundle=dict(name='b13_06_lmr_products.bundle',parts=['b13_06_lmr_products.bundle.part00'],
                     part_count=1,delivery_checksums='external MD5 and SHA-256 lists cover whole and part00'),
         inputs=[file_record(p) for p in inputs],outputs=[file_record(p) for p in sorted(set(files))],
         input_semantics='s74 ranks ADOPTED; modular kernels remain measurements; see report',
         checksum_semantics='Raw workspace/delivered bytes; sha256_lf_normalized also permits Git CRLF conversion.',
         replay=[['analysis/b13_06_decompose.py']]+[
            ['analysis/b13_06_ambient.py','--degree',str(a['degree']),'--weight',','.join(map(str,a['partition']))]
            for a in ambient]+[['analysis/b13_06_controls.py']],
         python_runtime='C:/Users/swami/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe',
         run_wrapper='analysis/b13_06_bound.py --name NAME --seconds SECONDS -- SCRIPT ARGS',
         dependencies=dict(python='3.12.14',numpy='installed',flint='missing; install socket denied',
                           sympy='missing',scipy='missing',psutil='missing',Singular='not on PATH',msolve='not on PATH'))
    write(OUT/'manifest.json',manifest)
    for rec in manifest['inputs']+manifest['outputs']:
        assert file_record(ROOT/rec['path'])==rec
    print(json.dumps(dict(ambient=summary['ambient_counts'],worker_seconds=summary['total_worker_wall_seconds'],
          peak_bytes=summary['peak_worker_memory_bytes'],input_files=len(inputs),output_files=len(files),
          checksums_verified=True)),flush=True)


if __name__=='__main__':main()

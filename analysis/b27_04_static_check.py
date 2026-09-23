# B27-04 static source check of Papers 1-3 (administrative text scan, NOT a compile and NOT a
# mathematical computation). No TeX toolchain is installed; the integrator compiles.
# Checks (PART 17 set): brace balance, $ parity, every \ref/\eqref defined by a \label, every
# \cite / \lit key defined by a \bibitem, and no slot labels or "Claude" outside the
# acknowledgement. Each file is checked at its PART 25 setup commit (before) and in the worktree
# (after). Usage: python analysis/b27_04_static_check.py <worktree-root-of-batch27>
import hashlib, re, subprocess, sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else '..'
PAPERS = [
    ('P1', 'b27-04-p1', 'f3b1d3297f44ac0819042847b8064bad5e38d159', 'paper/det3-conductor.tex'),
    ('P2', 'b27-04-p2', 'e3823bd519cf7ec3dc531c924bf561cd38aa7593', 'paper/det4-onset.tex'),
    ('P3', 'b27-04-p3', '64424450850bd7b6e1da1759e1586719e033599e', 'papers/det4-blindness/det4-blindness.tex'),
]
SLOT = re.compile(r'\b(?:[ABR]\d{2}-\d{2}[A-Za-z]?|B\d{2}|PART\s?\d+[a-z]?|G-A\d|G-P2-\d+|G-\d{2})\b')


def strip_comments(t):
    return re.sub(r'(?<!\\)%.*', '', t)


def ack_span(t):
    m = re.search(r'\\(?:section\*?|subsection\*?)\{Acknowledg[^}]*\}|\\begin\{acknowledg', t)
    if not m:
        return None
    e = re.search(r'\\(?:section|bibliography|begin\{thebibliography\}|end\{document\})', t[m.end():])
    return (m.start(), m.end() + (e.start() if e else len(t)))


def check(raw):
    t = strip_comments(raw.decode('utf8'))
    out = {}
    out['brace_balance'] = t.count('{') - t.count('\\{') - (t.count('}') - t.count('\\}'))
    dollars = len(re.findall(r'(?<!\\)\$', t))
    out['dollar_count'] = dollars
    out['dollar_parity_even'] = dollars % 2 == 0
    labels = re.findall(r'\\label\{([^}]*)\}', t)
    out['labels_duplicated'] = sorted({l for l in labels if labels.count(l) > 1})
    refs = set(re.findall(r'\\(?:eq|auto|c)?ref\{([^}]*)\}', t))
    out['refs_undefined'] = sorted(refs - set(labels))
    cites = set()
    for grp in re.findall(r'\\(?:no)?cite[tp]?\*?(?:\[[^\]]*\])*\{([^}]*)\}', t):
        cites |= {k.strip() for k in grp.split(',')}
    cites |= set(re.findall(r'\\lit\{([^}#]*)\}', t))
    cites.discard('#1')
    bib = set(re.findall(r'\\bibitem(?:\[[^\]]*\])?\{([^}]*)\}', t))
    out['cites_undefined'] = sorted(cites - bib)
    out['bibitems_uncited'] = sorted(bib - cites)
    span = ack_span(t)
    claude = [m.start() for m in re.finditer(r'Claude', t)]
    out['claude_outside_ack'] = [p for p in claude if not (span and span[0] <= p < span[1])]
    out['claude_in_ack'] = len(claude) - len(out['claude_outside_ack'])
    body = t[:span[0]] + t[span[1]:] if span else t
    slots = SLOT.findall(body)
    out['slot_labels_outside_ack'] = len(slots)
    out['slot_label_kinds'] = sorted(set(slots))[:12]
    return out


for name, wt, setup, path in PAPERS:
    base = subprocess.run(['git', '-C', f'{ROOT}/{wt}', 'cat-file', 'blob', f'{setup}:{path}'],
                          capture_output=True, check=True).stdout
    after = open(f'{ROOT}/{wt}/{path}', 'rb').read()
    print(f'== {name} {path}')
    print(f'   before (setup {setup[:8]}) sha256 {hashlib.sha256(base).hexdigest()}')
    print(f'   after  (worktree)        sha256 {hashlib.sha256(after).hexdigest()}')
    b, a = check(base), check(after)
    for k in a:
        flag = '' if a[k] == b[k] else '   <- changed'
        print(f'   {k}: before={b[k]} after={a[k]}{flag}')

"""Administrative helper: derive amsart theorem numbering (shared counter, per section)
from LaTeX source order, and list labels / refs / cites. Not a mathematical computation."""
import re, sys

BS = chr(92)
ENVS = ('theorem', 'proposition', 'lemma', 'corollary', 'definition', 'remark', 'question', 'conjecture')

def scan(path, want_sec=None):
    t = open(path, encoding='utf-8', errors='replace').read().replace('\r', '')
    lines = t.split('\n')
    sec = 0; cnt = 0; out = []
    env_re = re.compile(re.escape(BS) + r'begin\{(' + '|'.join(ENVS) + r')\}')
    lab_re = re.compile(re.escape(BS) + r'label\{([^}]*)\}')
    for i, l in enumerate(lines, 1):
        if l.startswith(BS + 'section{') or l.startswith(BS + 'section*{') is False and l.startswith(BS + 'section{'):
            pass
        if l.startswith(BS + 'section{'):
            sec += 1; cnt = 0
            m = lab_re.search(l)
            out.append((i, str(sec), 'section', m.group(1) if m else ''))
        m = env_re.search(l)
        if m:
            cnt += 1
            ctx = l + (lines[i] if i < len(lines) else '')
            lm = lab_re.search(ctx)
            out.append((i, f'{sec}.{cnt}', m.group(1), lm.group(1) if lm else ''))
    return t, out

if __name__ == '__main__':
    t, out = scan(sys.argv[1])
    for row in out:
        print(*row)
    labels = re.findall(re.escape(BS) + r'label\{([^}]*)\}', t)
    refs = re.findall(re.escape(BS) + r'(?:ref|eqref)\{([^}]*)\}', t)
    cites = []
    for c in re.findall(re.escape(BS) + r'cite(?:\[[^\]]*\])?\{([^}]*)\}', t):
        cites += [x.strip() for x in c.split(',')]
    bib = re.findall(re.escape(BS) + r'bibitem\{([^}]*)\}', t)
    print('labels', len(labels), 'dup', sorted({x for x in labels if labels.count(x) > 1}))
    print('undefined refs', sorted(set(refs) - set(labels)))
    print('unused labels', sorted(set(labels) - set(refs)))
    print('cited-not-in-bib', sorted(set(cites) - set(bib)))
    print('bib-not-cited', sorted(set(bib) - set(cites)))
    print('braces', t.count('{') - t.count('}'))
    print('empty or bare-section locators', re.findall(re.escape(BS) + r'cite\[' + re.escape(BS) + r'S\]', t))

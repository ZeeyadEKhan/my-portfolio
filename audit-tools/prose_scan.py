"""Extract prose text nodes from case study pages, excluding script/style/code/pre
and all attributes, then report hyphenated tokens and dashes."""
import re, glob, sys, html
from html.parser import HTMLParser

class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.skip = 0
        self.out = []      # (file, text)
        self.stack = []
    def handle_starttag(self, tag, attrs):
        cls = dict(attrs).get('class', '')
        if tag in ('script', 'style', 'code', 'pre') or 'code-wrap' in cls:
            self.skip += 1
            self.stack.append(True)
        else:
            self.stack.append(False)
    def handle_endtag(self, tag):
        if self.stack:
            if self.stack.pop():
                self.skip -= 1
    def handle_data(self, d):
        if self.skip == 0 and d.strip():
            self.out.append(d)

files = sys.argv[1:] or sorted(glob.glob('projects/*/index.html'))
tokens = {}
dashes = {}
for f in files:
    p = P()
    p.feed(open(f).read())
    for t in p.out:
        for m in re.finditer(r'[A-Za-z][A-Za-z0-9]*(?:-[A-Za-z0-9]+)+', t):
            tokens.setdefault(m.group(0), set()).add(f.split('/')[-2] if '/' in f else f)
        for m in re.finditer(r'[—–]', t):
            dashes.setdefault(f, []).append(t.strip()[:90])
for tok in sorted(tokens):
    print(f'{tok} :: {",".join(sorted(tokens[tok]))}')
print('\n=== DASHES ===')
for f, ts in dashes.items():
    for t in ts:
        print(f'{f} :: {t}')

"""Remove img-wrap / img-cell blocks whose img src basename is in the cuts list.
Unwraps a grid left with one cell into an img-wrap. Reports what it did."""
import re, sys

page, cuts_file = sys.argv[1], sys.argv[2]
path = f'projects/{page}/index.html'
src = open(path).read()
cuts = set(l.strip() for l in open(cuts_file) if l.strip())

def block_spans(html, cls):
    """yield (start, end) spans of <div class="cls ..."> ... </div> balanced"""
    out = []
    for m in re.finditer(r'<div class="' + cls + r'[" ]', html):
        depth = 0
        i = m.start()
        for t in re.finditer(r'<div\b|</div>', html[m.start():]):
            depth += 1 if t.group(0) == '<div' else -1
            if depth == 0:
                out.append((m.start(), m.start() + t.end()))
                break
    return out

def src_base(block):
    m = re.search(r'src="([^"]+)"', block)
    return m.group(1).rsplit('/', 1)[-1].rsplit('.', 1)[0] if m else None

removed = []
# pass 1: remove img-cell blocks with cut srcs
while True:
    changed = False
    for a, b in block_spans(src, 'img-cell'):
        base = src_base(src[a:b])
        if base in cuts:
            src = src[:a] + src[b:]
            removed.append(('cell', base))
            changed = True
            break
    if not changed:
        break
# pass 2: remove img-wrap blocks with cut srcs
while True:
    changed = False
    for a, b in block_spans(src, 'img-wrap'):
        base = src_base(src[a:b])
        if base in cuts:
            # swallow trailing whitespace up to next non-blank line
            end = b
            m = re.match(r'\s*\n', src[b:])
            if m: end = b + m.end()
            src = src[:a] + src[end:]
            removed.append(('wrap', base))
            changed = True
            break
    if not changed:
        break
# pass 3: fix img-groups: empty grid -> remove group; single cell -> unwrap to img-wrap
while True:
    changed = False
    for a, b in block_spans(src, 'img-group'):
        block = src[a:b]
        cells = block_spans(block, 'img-cell')
        cap = re.search(r'<p class="img-caption">.*?</p>', block, re.S)
        if len(cells) == 0:
            end = b
            m = re.match(r'\s*\n', src[b:])
            if m: end = b + m.end()
            src = src[:a] + src[end:]
            removed.append(('empty-group', src_base(block) or ''))
            changed = True
            break
        if len(cells) == 1:
            ca, cb = cells[0]
            inner = re.search(r'<img\b.*?>', block[ca:cb], re.S).group(0)
            new = '<div class="img-wrap">\n          ' + inner + ('\n          ' + cap.group(0) if cap else '') + '\n        </div>'
            src = src[:a] + new + src[b:]
            removed.append(('unwrapped', src_base(block[ca:cb])))
            changed = True
            break
    if not changed:
        break

open(path, 'w').write(src)
for kind, base in removed:
    print(f'{kind:12} {base}')
print(f'\nimgs now: {len(re.findall(chr(60)+"img ", src)) + len(re.findall(chr(60)+"img"+chr(10), src))}')
print('imgs tags:', len(re.findall(r'<img\b', src)))

"""Inject width/height attributes on every img tag with a local src, using sips."""
import re, glob, subprocess, os, functools

@functools.lru_cache(maxsize=None)
def dims(path):
    out = subprocess.run(['sips', '-g', 'pixelWidth', '-g', 'pixelHeight', path],
                         capture_output=True, text=True).stdout
    w = re.search(r'pixelWidth: (\d+)', out)
    h = re.search(r'pixelHeight: (\d+)', out)
    return (w.group(1), h.group(1)) if w and h else None

for f in sorted(glob.glob('*.html') + glob.glob('projects/*/index.html')):
    src = open(f).read()
    changed = 0
    def repl(m):
        global changed
        t = m.group(0)
        if 'width=' in t or 'height=' in t:
            return t
        sm = re.search(r'src="(/[^"]+\.(?:webp|png|jpg|jpeg))"', t)
        if not sm:
            return t
        p = sm.group(1).lstrip('/')
        if not os.path.exists(p):
            print(f'  MISSING FILE {p} in {f}')
            return t
        d = dims(p)
        if not d:
            print(f'  NO DIMS {p}')
            return t
        changed += 1
        # insert before the closing '>' keeping any newline style
        if t.endswith('\n    >') or re.search(r'\n\s*>$', t):
            return re.sub(r'(\n\s*)>$', rf'\1  width="{d[0]}"\1  height="{d[1]}"\1>', t)
        return t[:-1].rstrip() + f' width="{d[0]}" height="{d[1]}">'
    new = re.sub(r'<img\b[^>]*>', repl, src, flags=re.S)
    if new != src:
        open(f, 'w').write(new)
    print(f'{f}: {changed} imgs updated')

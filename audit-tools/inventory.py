import re, os, sys, html
page = sys.argv[1]
src = open(f'projects/{page}/index.html').read()
# walk through headings and imgs in document order
pat = re.compile(r'<(h[1-4])[^>]*>(.*?)</\1>|<img\s+([^>]*?)>', re.S)
n = 0
for m in pat.finditer(src):
    if m.group(1):
        txt = re.sub(r'<[^>]+>', '', m.group(2)).strip()
        print(f'\n## {m.group(1).upper()}: {html.unescape(txt)}')
    else:
        attrs = m.group(3)
        srcm = re.search(r'src="([^"]+)"', attrs)
        altm = re.search(r'alt="([^"]*)"', attrs, re.S)
        p = srcm.group(1) if srcm else '?'
        fp = p.lstrip('/')
        size = os.path.getsize(fp)//1024 if os.path.exists(fp) else -1
        alt = html.unescape(re.sub(r'\s+', ' ', altm.group(1))) if altm else 'NO-ALT'
        n += 1
        print(f'  [{n:3}] {size:5}KB {os.path.basename(p)} :: {alt[:150]}')
print(f'\nTOTAL {n} images')

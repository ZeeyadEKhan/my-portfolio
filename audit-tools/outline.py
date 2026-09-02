import re, sys, html
src = open(f'projects/{sys.argv[1]}/index.html').read()
pat = re.compile(r'<(h[1-4])[^>]*>(.*?)</\1>|<img\b([^>]*?)>|<p\b[^>]*class="([^"]*)"[^>]*>(.*?)</p>|<p>(.*?)</p>', re.S)
n=0
for m in pat.finditer(src):
    if m.group(1):
        print(f'{m.group(1).upper()}: {html.unescape(re.sub(r"<[^>]+>","",m.group(2))).strip()}')
    elif m.group(3) is not None:
        n+=1
        s = re.search(r'src="([^"]+)"', m.group(3))
        print(f'   IMG[{n}] {s.group(1).split("/")[-1] if s else "NOSRC:"+re.sub(chr(10)," ",m.group(3))[:80]}')
    else:
        cls = m.group(4) or ''
        txt = html.unescape(re.sub(r'<[^>]+>','',m.group(5) if m.group(5) is not None else m.group(6) or '')).strip()
        txt = re.sub(r'\s+',' ',txt)
        tag = 'CAP' if 'caption' in cls else 'P'
        print(f'   {tag}: {txt[:180]}')

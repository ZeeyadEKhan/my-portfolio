import re, glob, os, json

files = sorted(glob.glob('*.html') + glob.glob('projects/*/index.html'))
print(f'{"page":34} h1  main  skip  img(alt/w/h)  orphans')
for f in files:
    s = open(f).read()
    h1 = len(re.findall(r'<h1\b', s))
    mains = len(re.findall(r'<main\b', s))
    body = s[s.find('<body'):]
    skip_first = bool(re.match(r'<body[^>]*>\s*<a class="skip-link" href="#main-content">', body))
    nc = re.sub(r'<!--.*?-->', '', s, flags=re.S)
    nc = re.sub(r'<script\b.*?</script>', '', nc, flags=re.S)
    imgs = [t for t in re.findall(r'<img\b[^>]*>', nc, re.S)]
    bad_alt = bad_wh = 0
    for t in imgs:
        dynamic = 'src=""' in t
        if dynamic: continue
        if not re.search(r'alt="[^"]+"', t, re.S): bad_alt += 1
        if 'width=' not in t or 'height=' not in t: bad_wh += 1
    flat = re.sub(r'<!--.*?-->', '', s, flags=re.S)
    flat = re.sub(r'\s+', ' ', flat)
    orph = re.findall(r'<h([23])[^>]*>(.*?)</h\1>\s*(?:</section>|<h[23])', flat)
    print(f'{f:34} {h1}   {mains}     {str(skip_first)[0]}     alt-miss={bad_alt} wh-miss={bad_wh}   {[o[1][:30] for o in orph] if orph else "none"}')

print('\n-- rebuilt page budgets --')
for p in ['explorius', 'wonderbudi', 'baloo']:
    s = open(f'projects/{p}/index.html').read()
    srcs = re.findall(r'src="(/projects/[^"]+\.(?:webp|png|jpg))"', s)
    total = sum(os.path.getsize(x.lstrip('/')) for x in set(srcs) if os.path.exists(x.lstrip('/')))
    n = len([t for t in re.findall(r'<img\b[^>]*>', s, re.S) if 'src=""' not in t])
    print(f'{p}: {n} images, {total//1024} KB  {"PASS" if n <= 30 and total <= 1500*1024 else "FAIL"}')

print('\n-- json-ld --')
for f in ['index.html', 'about.html']:
    s = open(f).read()
    m = re.search(r'<script type="application/ld\+json">\s*(\{.*?\})\s*</script>', s, re.S)
    d = json.loads(m.group(1))
    print(f, 'Person' if d.get('@type') == 'Person' else 'BAD', 'no-email' if 'email' not in m.group(1) else 'HAS-EMAIL')

print('\n-- sitemap & canonicals --')
import subprocess
sm_changed = subprocess.run(['git', 'diff', 'HEAD~9', '--', 'sitemap.xml', 'robots.txt'], capture_output=True, text=True).stdout
print('sitemap/robots diff since start:', 'NONE' if not sm_changed else 'CHANGED!')
import xml.etree.ElementTree as ET
ET.parse('sitemap.xml')
print('sitemap parses: OK')
urls = [e.text for e in ET.parse('sitemap.xml').getroot().iter() if e.tag.endswith('loc')]
canon = {}
for f in files:
    m = re.search(r'rel="canonical" href="([^"]+)"', open(f).read())
    if m: canon[f] = m.group(1)
missing = [u for u in urls if not any(c == u or c == u.rstrip('/') for c in canon.values())]
print(f'sitemap urls: {len(urls)}, canonicals found: {len(canon)}, sitemap urls missing a matching canonical: {missing if missing else "none"}')

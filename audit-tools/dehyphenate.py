"""Normalize case study prose to the site's no hyphen style.
Only touches text nodes; never attributes, script, style, code, pre,
or .code-wrap subtrees. Em dashes in prose become commas."""
import re, glob

MAP = {
    'AI-powered': 'AI powered', 'Cross-document': 'Cross document',
    'De-escalation': 'De escalation', 'Five-section': 'Five section',
    'High-Fidelity': 'High Fidelity', 'Lo-fi': 'Lo fi', 'lo-fi': 'lo fi',
    'Low-Fi': 'Low Fi', 'Low-fidelity': 'Low fidelity', 'Mid-research': 'Mid research',
    'Mid-size': 'Midsize', 'Two-Stage': 'Two Stage',
    'action-oriented': 'action oriented', 'always-visible': 'always visible',
    'calm-down': 'calm down', 'card-based': 'card based',
    'carousel-based': 'carousel based', 'check-in': 'check in',
    'check-ins': 'check ins', 'child-facing': 'child facing',
    'clause-aware': 'clause aware', 'co-working': 'coworking',
    'community-first': 'community first', 'community-focused': 'community focused',
    'cost-based': 'cost based', 'cross-class': 'cross class',
    'end-to-end': 'end to end', 'fast-growing': 'fast growing',
    'follow-up': 'follow up', 'full-body': 'full body',
    'high-fidelity': 'high fidelity', 'high-priority': 'high priority',
    'in-depth': 'in depth', 'in-product': 'in product', 'in-school': 'in school',
    'long-term': 'long term', 'lower-cost': 'lower cost',
    'mid-project': 'mid project', 'most-used': 'most used',
    'multi-semester': 'multi semester', 'non-nomads': 'non nomads',
    'non-nomad': 'non nomad', 'non-threatening': 'non threatening',
    'parent-facing': 'parent facing', 'planning-focused': 'planning focused',
    'play-based': 'play based', 'pre-planning': 'pre planning',
    'pressure-test': 'pressure test', 'pressure-tested': 'pressure tested',
    're-entry anxiety': 'anxiety about returning to class',
    'real-time': 'real time', 'school-day': 'school day',
    'self-awareness': 'self awareness', 'self-contained': 'self contained',
    'self-directed': 'self directed', 'sign-up': 'sign up',
    'single-select': 'single select', 'six-step': 'six step',
    'sub-questions': 'sub questions', 'surface-level': 'surface level',
    'table-based': 'table based', 'tablet-only': 'tablet only',
    'tap-to-start': 'tap to start', 'three-part': 'three part',
    'time-intensive': 'time intensive', 'utility-first': 'utility first',
    '10-point': '10 point', '20-minute': '20 minute', '3-option': '3 option',
    '3-point': '3 point', '5-category': '5 category', '8-column': '8 column',
}
pat = re.compile('|'.join(re.escape(k) for k in sorted(MAP, key=len, reverse=True)))

def fix_text(t):
    t = pat.sub(lambda m: MAP[m.group(0)], t)
    t = re.sub(r'\s*—\s*', ', ', t)
    t = re.sub(r'(?<=[A-Za-z0-9])\s*–\s*(?=[A-Za-z0-9])', ' to ', t)
    return t

for f in sorted(glob.glob('projects/*/index.html')):
    src = open(f).read()
    out = []
    skip = 0
    changed = 0
    for part in re.split(r'(<[^>]*>)', src):
        if part.startswith('<'):
            low = part.lower()
            if re.match(r'<(script|style|code|pre)\b', low) or 'code-wrap' in low:
                skip += 1
            elif re.match(r'</(script|style|code|pre)\b', low):
                skip = max(0, skip - 1)
            elif skip and re.match(r'</div', low):
                # close of code-wrap div
                skip = max(0, skip - 1)
            out.append(part)
        else:
            if skip == 0:
                new = fix_text(part)
                if new != part: changed += 1
                out.append(new)
            else:
                out.append(part)
    open(f, 'w').write(''.join(out))
    print(f, 'segments changed:', changed)

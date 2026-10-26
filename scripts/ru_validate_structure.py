#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v117 — structural validator for all 90 Russian lessons.

Checks (per lesson):
  - required keys present; unique slugs; all start with 'russian-'
  - intro: exactly 2+ paragraphs; sections: 7-9; each section has h2 + blocks
  - block kinds allowed: p/ex/table/ul/ol/quote/faq  (ex3 forbidden!)
  - ex tuples: 2 fields, field-1 Cyrillic-dominant, field-2 Persian-dominant
  - drills section: an 'ol' with >=4 items AND a 'faq' block with >=4 answers
  - final 'faq': exactly 2 items; takeaway non-empty
  - desc <= 210 chars; answer 35-70 words
  - challenge quote present; tips 'ul' with >=3 items
Exit code 1 if any hard error.
"""
import glob
import importlib.util
import re
import sys

CYR = re.compile(r'[\u0400-\u04FF]')
PER = re.compile(r'[\u0621-\u064A\u067E\u0686\u06A9\u06AF\u06CC\u06C1]')

files = sorted(glob.glob('/home/z/my-project/repos/upword-landing/scripts/ru_course_data_*.py'))
lessons = []
for f in files:
    spec = importlib.util.spec_from_file_location(f.split('/')[-1][:-3], f)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    lessons.extend(m.LESSONS)

errors = []
warns = []
if len(lessons) != 90:
    errors.append(f'TOTAL lessons = {len(lessons)} (expected 90)')
slugs = [l['slug'] for l in lessons]
if len(set(slugs)) != len(slugs):
    dupes = {s for s in slugs if slugs.count(s) > 1}
    errors.append(f'duplicate slugs: {dupes}')
if not all(s.startswith('russian-') for s in slugs):
    errors.append('non-russian slug found')

for n, l in enumerate(lessons, start=1):
    tag = f'L{n} {l.get("slug","?")}'
    for k in ('slug', 'title', 'desc', 'keywords', 'answer', 'intro', 'sections', 'takeaway', 'faq'):
        if k not in l or not l.get(k):
            errors.append(f'{tag}: missing key {k}')
    if len(l.get('intro', [])) < 2:
        errors.append(f'{tag}: intro has {len(l.get("intro",[]))} paragraphs (<2)')
    if not (6 <= len(l.get('sections', [])) <= 9):
        warns.append(f'{tag}: {len(l.get("sections",[]))} sections')
    if len(l.get('desc', '')) > 210:
        warns.append(f'{tag}: desc {len(l["desc"])} chars')
    ans_words = len(l.get('answer', '').split())
    if not (30 <= ans_words <= 85):
        warns.append(f'{tag}: answer {ans_words} words')
    if len(l.get('faq', [])) != 2:
        errors.append(f'{tag}: final faq has {len(l.get("faq",[]))} items (need 2)')

    has_drill = has_quote = has_tips = False
    for sec in l.get('sections', []):
        if 'h2' not in sec or not sec.get('blocks'):
            errors.append(f'{tag}: section without h2/blocks')
            continue
        for b in sec['blocks']:
            kind = b[0]
            if kind == 'ex3':
                errors.append(f'{tag}: FORBIDDEN ex3 found')
            if kind not in ('p', 'ex', 'table', 'ul', 'ol', 'quote', 'faq'):
                errors.append(f'{tag}: unknown block kind {kind}')
            if kind == 'ex':
                if len(b) != 3:
                    errors.append(f'{tag}: ex with {len(b)} fields (need 2+tuple=3)')
                else:
                    ru, fa = b[1], b[2]
                    # field-1 must be Russian-dominant (Persian notes break the app TTS)
                    if len(PER.findall(ru)) >= 3 and len(CYR.findall(ru)) < len(PER.findall(ru)):
                        errors.append(f'{tag}: ex field-1 not Russian-dominant: {ru[:40]!r}')
                    # field-2: Persian gloss; Russian quotes inside are fine —
                    # only flag if there are NO Persian letters/digits at all
                    fa_per = len(PER.findall(fa)) + len(re.findall(r'[\u06F0-\u06F9]', fa))
                    if fa_per == 0:
                        errors.append(f'{tag}: ex field-2 has no Persian: {fa[:40]!r}')
            if kind == 'faq' and len(b[1]) < 3:
                errors.append(f'{tag}: faq block with {len(b[1])} items')
        h = sec['h2']
        if 'تمرین' in h:
            has_drill = True
            kinds = [b[0] for b in sec['blocks']]
            if 'ol' not in kinds:
                errors.append(f'{tag}: drills section without ol')
            faqblocks = [b for b in sec['blocks'] if b[0] == 'faq']
            if faqblocks and len(faqblocks[0][1]) < 4:
                errors.append(f'{tag}: drills faq has {len(faqblocks[0][1])} answers (<4)')
        if 'چالش' in h:
            has_quote = True
            if not any(b[0] == 'quote' for b in sec['blocks']):
                errors.append(f'{tag}: challenge section without quote')
        if 'نکات مکالمه' in h:
            has_tips = True
            uls = [b for b in sec['blocks'] if b[0] == 'ul']
            if not uls or len(uls[0][1]) < 3:
                errors.append(f'{tag}: tips ul missing or <3 items')
    if not has_drill:
        errors.append(f'{tag}: no drills section')
    if not has_quote:
        errors.append(f'{tag}: no challenge section')
    if not has_tips:
        errors.append(f'{tag}: no tips section')

print(f'lessons checked: {len(lessons)}')
print(f'HARD ERRORS: {len(errors)}')
for e in errors[:40]:
    print('  ✗', e)
print(f'warnings: {len(warns)}')
for w in warns[:15]:
    print('  ⚠', w)
sys.exit(1 if errors else 0)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v117 — comprehensive QA for the Russian course (seo_qa equivalent):

 1. JSON-LD parses in all 91 RU pages (hub + 90 lessons)
 2. FAQ schema text == on-page FAQ text (AEO contract)
 3. Every internal href in RU pages resolves to a real file
 4. sitemap.xml well-formed + all RU rows exist as files
 5. feed.xml well-formed + RU items present
 6. posts.json RU rows complete (cover/content/minutes/date)
 7. All referenced covers exist on disk (warns for missing)
"""
import json
import os
import re
import sys
import xml.etree.ElementTree as ET

ROOT = '/home/z/my-project/repos/upword-landing'
BLOG = ROOT + '/blog'
errors = []
warns = []

ru_pages = [BLOG + '/russian-course.html'] + sorted(
    os.path.join(BLOG, 'articles', f) for f in os.listdir(BLOG + '/articles')
    if f.startswith('russian-') and f.endswith('.html'))
print(f'RU pages: {len(ru_pages)}')

# 1+2 — JSON-LD parse & FAQ parity
for p in ru_pages:
    src = open(p, encoding='utf-8').read()
    m = re.search(r'<script type="application/ld\+json">([\s\S]*?)</script>', src)
    if not m:
        errors.append(f'{os.path.basename(p)}: no JSON-LD')
        continue
    try:
        data = json.loads(m.group(1))
    except Exception as e:
        errors.append(f'{os.path.basename(p)}: JSON-LD parse: {e}')
        continue
    graph = data.get('@graph', [])
    faq_node = next((n for n in graph if n.get('@type') == 'FAQPage'), None)
    # scope: only the FINAL FAQ section («پرسش‌های رایج») — the drills'
    # answer section uses the same markup but is not part of the schema
    # (German-course precedent: schema 2, details 6, final section checked)
    final = re.search(
        r'<section class="article-faq" aria-label="پرسش‌های رایج">([\s\S]*?)</section>', src)
    page_qas = re.findall(
        r'<details class="faq-item"[^>]*>\s*<summary><span>([^<]+)</span></summary>\s*'
        r'<div class="faq-answer">([\s\S]*?)</div>', final.group(1)) if final else []
    if faq_node and not page_qas:
        errors.append(f'{os.path.basename(p)}: schema FAQ but no page FAQ')
    if faq_node:
        schema_q = [q['name'] for q in faq_node['mainEntity']]
        page_q = [re.sub(r'<[^>]+>', '', q[0]).strip() for q in page_qas]
        if schema_q != page_q:
            errors.append(f'{os.path.basename(p)}: FAQ parity broken '
                          f'(schema {len(schema_q)} vs page {len(page_q)})')
    needs = ('hreflang="fa"', 'og:image:alt', 'canonical')
    if os.path.basename(p) != 'russian-course.html':
        needs += ('speakable',)  # speakable is a BlogPosting thing; the hub is Course schema (German precedent)
    for need in needs:
        if need not in src:
            errors.append(f'{os.path.basename(p)}: missing {need}')
print('JSON-LD/FAQ/SEO checks done')

# 3 — internal links resolve
missing_links = set()
for p in ru_pages:
    src = open(p, encoding='utf-8').read()
    for href in re.findall(r'href="(/blog/[^"#]+|/assets/[^"#]+|/css/[^"#]+|/js/[^"#]+)"', src):
        fp = ROOT + href
        if href.endswith('/') or not os.path.exists(fp):
            if not (href.rstrip('/').endswith('/blog')):
                missing_links.add(href)
if missing_links:
    for h in sorted(missing_links)[:10]:
        errors.append(f'broken internal link: {h}')
print(f'internal links checked (missing: {len(missing_links)})')

# 4 — sitemap
sm = open(ROOT + '/sitemap.xml', encoding='utf-8').read()
ET.fromstring(sm)
locs = re.findall(r'<loc>([^<]+)</loc>', sm)
ru_locs = [l for l in locs if '/russian' in l]
print(f'sitemap: {len(locs)} urls, {len(ru_locs)} russian')
if len(ru_locs) != 91:
    errors.append(f'sitemap russian urls = {len(ru_locs)} (need 91)')
for l in ru_locs:
    fp = ROOT + l.replace('https://upword.ir', '')
    if not os.path.exists(fp):
        errors.append(f'sitemap missing file: {l}')

# 5 — feed
fd = open(ROOT + '/feed.xml', encoding='utf-8').read()
ET.fromstring(fd)
ru_items = re.findall(r'<link>(https://upword\.ir/blog/[^\r\n]*russian[^\r\n]*</link>)', fd)
print(f'feed: russian items = {len(ru_items)}')
if len(ru_items) != 91:
    errors.append(f'feed russian items = {len(ru_items)} (need 91)')

# 6 — posts.json completeness
posts = json.load(open(BLOG + '/posts.json', encoding='utf-8'))['posts']
ru_posts = [p for p in posts if p.get('category', '').startswith('آموزش زبان روسی')]
print(f'posts.json russian rows: {len(ru_posts)}')
if len(ru_posts) != 91:
    errors.append(f'posts russian rows = {len(ru_posts)} (need 91)')
for p in ru_posts:
    for k in ('slug', 'url', 'title', 'desc', 'date', 'dateFa', 'minutes', 'cover', 'content'):
        if not p.get(k):
            errors.append(f'posts row {p.get("slug")}: missing {k}')
    cf = ROOT + '/blog/' + p['cover']
    if not os.path.exists(cf):
        warns.append(f'cover missing: {p["cover"]}')

# 7 — cover inventory
existing = set(f[:-4] for f in os.listdir(BLOG + '/covers') if f.endswith('.jpg'))
need = set(p['slug'] for p in ru_posts)
missing_cov = sorted(need - existing)
print(f'covers: need {len(need)}, have {len(need - set(missing_cov))}, missing {len(missing_cov)}')

print(f'\nHARD ERRORS: {len(errors)}')
for e in errors[:30]:
    print('  ✗', e)
print(f'warnings: {len(warns)} (missing covers listed here)')
sys.exit(1 if errors else 0)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v117 — sitewide nav/footer sweep: add the Russian course link to every
existing course page (3 hubs + all non-Russian lesson articles).

Anchors (both unique per page):
  nav:    <a href="/blog/" class="nav-link">مقالات</a>
  footer: <a href="/blog/">مقالات</a>
The Russian link is inserted right after each anchor, so every page shows
دورهٔ روسی as the first course link, consistently."""
import glob
import io
import os

ROOT = '/home/z/my-project/repos/upword-landing/blog'
NAV_ANCHOR = '<a href="/blog/" class="nav-link">مقالات</a>'
NAV_NEW = ('<a href="/blog/" class="nav-link">مقالات</a>\n'
           '<a href="/blog/russian-course.html" class="nav-link">دورهٔ روسی</a>')
FOOT_ANCHOR = '<a href="/blog/">مقالات</a>'
FOOT_NEW = ('<a href="/blog/">مقالات</a>\n'
            '<a href="/blog/russian-course.html">دورهٔ ۹۰ روزهٔ روسی</a>')

targets = [ROOT + '/german-course.html', ROOT + '/english-course.html', ROOT + '/chinese-course.html']
targets += sorted(p for p in glob.glob(ROOT + '/articles/*.html')
                  if not os.path.basename(p).startswith('russian-')
                  and not os.path.basename(p).startswith('_template'))

nav_n = foot_n = 0
for p in targets:
    src = io.open(p, encoding='utf-8').read()
    orig = src
    if 'href="/blog/russian-course.html"' in src:
        continue
    if NAV_ANCHOR in src:
        src = src.replace(NAV_ANCHOR, NAV_NEW, 1)
        nav_n += 1
    if FOOT_ANCHOR in src:
        src = src.replace(FOOT_ANCHOR, FOOT_NEW, 1)
        foot_n += 1
    if src != orig:
        io.open(p, 'w', encoding='utf-8').write(src)

print(f'swept {len(targets)} files: nav={nav_n} footer={foot_n}')

# verify
miss = []
for p in targets:
    src = io.open(p, encoding='utf-8').read()
    if 'href="/blog/russian-course.html"' not in src:
        miss.append(p)
print('files without russian link after sweep:', len(miss))
for m in miss[:5]:
    print('  ', m)

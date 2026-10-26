#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v117 — browser QA: render the Russian hub + 2 lessons at desktop & 390px,
check horizontal overflow + console errors, save screenshots."""
from playwright.sync_api import sync_playwright

ROOT = '/home/z/my-project/repos/upword-landing'
OUT = '/home/z/my-project/blogimg/qa'
import os
os.makedirs(OUT, exist_ok=True)

PAGES = [
    ('hub', ROOT + '/blog/russian-course.html'),
    ('lesson1', ROOT + '/blog/articles/russian-from-zero.html'),
    ('lesson50', ROOT + '/blog/articles/russian-aspect.html'),
    ('lesson90', ROOT + '/blog/articles/russian-final-review.html'),
]

with sync_playwright() as pw:
    browser = pw.chromium.launch()
    for name, path in PAGES:
        for kind, vw in (('d', 1280), ('m', 390)):
            pg = browser.new_page(viewport={'width': vw, 'height': 900})
            errors = []
            pg.on('console', lambda m: errors.append(m.text) if m.type == 'error' else None)
            pg.on('pageerror', lambda e: errors.append(str(e)))
            pg.goto('file://' + path, wait_until='networkidle')
            overflow = pg.evaluate(
                'document.documentElement.scrollWidth - document.documentElement.clientWidth')
            pg.screenshot(path=f'{OUT}/{name}_{kind}.png', full_page=(kind == 'm'))
            print(f'{name}_{kind}: overflow={overflow}px console_errors={len(errors)}')
            for e in errors[:3]:
                print('   console:', e[:110])
            pg.close()
    browser.close()
print('done')

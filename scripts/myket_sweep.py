#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v119 — remove every Myket trace from the landing: the app is Cafe-Bazaar-only.

Targets:
  1. blog/articles/*.html + blog/*.html hubs + blog/index.html:
     - CTA ghost button line  <a href="https://myket.ir/..." ...>دانلود از مایکت</a>
     - footer plain link      <a href="https://myket.ir/..." ...>مایکت</a>
  2. index.html: hero ghost CTA + glass CTA + footer icon + footer link +
     JSON-LD sameAs entry + meta description/keywords + FAQ JSON-LD texts +
     b7 bento text + store-chip + premium note.
  3. js/main.js: hero.ctaMyket / cta.myket i18n entries (fa + en) + b7.desc /
     premium.note / faq.a1 / faq.a2 store-wording (fa + en).
  4. scripts/{ru,de,en}_course_lib.py: template CTA lines (so rebuilds stay clean).
  5. README.md / DESIGN.md: doc mentions.
  6. _template.html: guidance text + CTA + footer.
Inline prose mentions («کافه بازار یا مایکت») are reworded via the swaps below.
"""
import glob
import io
import re
import subprocess

ROOT = '/home/z/my-project/repos/upword-landing'
MYKET_ANCHOR = re.compile(r'[ \t]*<a href="https://myket\.ir/app/ir\.upword\.twa"[^>]*>[\s\S]*?</a>\n?')

report = {}


def fix(path, fn):
    src = io.open(path, encoding='utf-8').read()
    out = fn(src)
    if out != src:
        io.open(path, 'w', encoding='utf-8').write(out)
        report[path] = True


# ── 1) blog pages: drop every myket anchor (CTA + footer) ────────────────
blog_pages = sorted(glob.glob(ROOT + '/blog/articles/*.html'))
blog_pages += [ROOT + '/blog/' + h for h in
               ('index.html', 'russian-course.html', 'german-course.html',
                'english-course.html', 'chinese-course.html')]
for p in blog_pages:
    fix(p, lambda s: MYKET_ANCHOR.sub('', s))


# ── 2) landing index.html ─────────────────────────────────────────────────
def fix_index(src):
    src = MYKET_ANCHOR.sub('', src)
    src = src.replace(
        '"sameAs": [\n'
        '        "https://cafebazaar.ir/app/?id=ir.upword.twa",\n'
        '        "https://myket.ir/app/ir.upword.twa"\n'
        '      ]',
        '"sameAs": [\n'
        '        "https://cafebazaar.ir/app/?id=ir.upword.twa"\n'
        '      ]')
    src = src.replace('دانلود از کافه بازار و مایکت.', 'دانلود از کافه بازار.')
    src = src.replace('کافه بازار, مایکت', 'کافه بازار')
    src = src.replace('از کافه بازار یا مایکت دانلود کن،', 'از کافه بازار دانلود کن،')
    src = src.replace('از طریق کافه بازار یا مایکت انجام می‌شود', 'از طریق کافه بازار انجام می‌شود')
    src = src.replace('و امن از کافه بازار و مایکت،', 'و امن از کافه بازار،')
    src = src.replace(' <span class="store-chip"><i>🤖</i> مایکت</span>', '')
    src = src.replace('پنل فروشگاه (کافه بازار / مایکت) نمایش داده می‌شوند',
                      'پنل فروشگاه (کافه بازار) نمایش داده می‌شوند')
    return src


fix(ROOT + '/index.html', fix_index)


# ── 3) js/main.js — i18n entries + store wording ─────────────────────────
def fix_js(src):
    for key in ('hero.ctaMyket', 'cta.myket'):
        for val in ('دانلود از مایکت', 'Download from Myket'):
            src = src.replace(f'"{key}":"{val}",', '')
    swaps = [
        ('پرداخت ریالی و امن از کافه بازار و مایکت، تقویم هفتهٔ ایرانی',
         'پرداخت ریالی و امن از کافه بازار، تقویم هفتهٔ ایرانی'),
        ('از پنل فروشگاه (کافه بازار / مایکت) می‌بینی', 'از پنل فروشگاه (کافه بازار) می‌بینی'),
        ('از کافه بازار یا مایکت نصبش کن؛', 'از کافه بازار نصبش کن؛'),
        ('از طریق کافه بازار یا مایکت انجام می‌شود؛', 'از طریق کافه بازار انجام می‌شود؛'),
        ('Rial payments via Cafe Bazaar and Myket, the Iranian week calendar',
         'Rial payments via Cafe Bazaar, the Iranian week calendar'),
        ('based on the store panel (Cafe Bazaar / Myket)', 'based on the store panel (Cafe Bazaar)'),
        ('Download from Cafe Bazaar or Myket, pick your target language',
         'Download from Cafe Bazaar, pick your target language'),
        ('securely through Cafe Bazaar or Myket; prices are shown',
         'securely through Cafe Bazaar; prices are shown'),
    ]
    for old, new in swaps:
        src = src.replace(old, new)
    return src


fix(ROOT + '/js/main.js', fix_js)

# ── 4) course lib templates ──────────────────────────────────────────────
for lib in ('ru', 'de', 'en'):
    fix(f'{ROOT}/scripts/{lib}_course_lib.py', lambda s: MYKET_ANCHOR.sub('', s))

# ── 5) docs ──────────────────────────────────────────────────────────────
def fix_readme(src):
    src = src.replace('- 🛍 دکمه‌های دانلود از **کافه بازار** و **مایکت**',
                      '- 🛍 دکمهٔ دانلود از **کافه بازار**')
    src = src.replace(
        'تمام لینک‌های `https://cafebazaar.ir/app/?id=ir.upword.twa` و `https://myket.ir/app/ir.upword.twa` را در `index.html` جستجو و جایگزین کنید.',
        'تمام لینک‌های `https://cafebazaar.ir/app/?id=ir.upword.twa` را در `index.html` جستجو و جایگزین کنید (اپ فقط روی کافه بازار منتشر می‌شود).')
    return src


fix(ROOT + '/README.md', fix_readme)
fix(ROOT + '/DESIGN.md', lambda s: s.replace('download (Cafe Bazaar + Myket)', 'download (Cafe Bazaar)'))


# ── 6) article template guidance ─────────────────────────────────────────
def fix_template(src):
    src = MYKET_ANCHOR.sub('', src)
    src = src.replace(
        'لینک دانلود با &lt;a href="https://cafebazaar.ir/app/?id=ir.upword.twa"&gt;کافه بازار&lt;/a&gt; و &lt;a href="https://myket.ir/app/ir.upword.twa"&gt;مایکت&lt;/a&gt;',
        'لینک دانلود با &lt;a href="https://cafebazaar.ir/app/?id=ir.upword.twa"&gt;کافه بازار&lt;/a&gt;')
    return src


fix(ROOT + '/blog/articles/_template.html', fix_template)

print(f'files touched: {len(report)}')

# ── verify: what myket text remains anywhere? ────────────────────────────
r = subprocess.run(['grep', '-rn', '-i', '-E', 'myket|مایکت', ROOT,
                    '--include=*.html', '--include=*.js', '--include=*.css',
                    '--include=*.json', '--include=*.xml', '--include=*.md',
                    '--include=*.py'],
                   capture_output=True, text=True)
rest = [l for l in r.stdout.splitlines() if '/.git/' not in l]
print(f'remaining myket refs: {len(rest)}')
for l in rest[:40]:
    print('  ', l[:150])

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v117 — blog/index.html: add the Russian course banner + refresh the ItemList
(latest 12) to the Russian course, and widen the page metas to the 4 courses."""
import io
import json
import re

ROOT = '/home/z/my-project/repos/upword-landing'
P = ROOT + '/blog/index.html'
src = io.open(P, encoding='utf-8').read()

# 1) Russian course banner BEFORE the German banner
banner = '''<section class="course-banner" aria-label="دورهٔ کامل زبان روسی">
<a class="course-card" href="/blog/russian-course.html">
<span class="cc-eyebrow">📕 دورهٔ ۹۰ روزه · مخصوص دانشجوها و مهاجرها · رایگان</span>
<span class="cc-title">زبان روسی از صفر تا تحصیل و زندگی <b class="cc-zh">Русский</b></span>
<span class="cc-desc">نقشهٔ کامل زبان برای فارسی‌زبانی که نقشهٔ تحصیل یا کار یا زندگی در روسیه دارد: از الفبای سیریلیک و خوابگاه و دانشگاه до МФЦ، РВП و ВНЖ و مکالمهٔ روان — با صدای روسی برای همهٔ مثال‌ها.</span>
<span class="cc-cta">از درس ۱ شروع کن ←</span>
</a>
</section>
'''
anchor = '<section class="course-banner" aria-label="دورهٔ کامل زبان آلمانی">'
assert anchor in src, 'german banner anchor missing'
if 'href="/blog/russian-course.html"' not in src:
    src = src.replace(anchor, banner + anchor)
    print('banner inserted')
else:
    print('banner already present')

# 2) ItemList refresh — latest 12 from posts.json (RU hub + lessons 1..11)
posts = json.load(open(ROOT + '/blog/posts.json', encoding='utf-8'))['posts']
top = posts[:12]
items = ',\n'.join(
    f'{{ "@type": "ListItem", "position": {i+1}, "name": "{p["title"].replace(chr(34), "")}", "url": "https://upword.ir/blog/articles/{p["slug"]}.html" }}'
    if p['slug'] != 'russian-course' else
    f'{{ "@type": "ListItem", "position": {i+1}, "name": "{p["title"].replace(chr(34), "")}", "url": "https://upword.ir/blog/russian-course.html" }}'
    for i, p in enumerate(top))
new_block = ('      "itemListElement": [\n        ' + items + '\n      ]')
src = re.sub(r'      "itemListElement": \[\n[\s\S]*?\n      \]', new_block, src, count=1)
print('ItemList refreshed ->', top[0]['slug'], '…', top[-1]['slug'])

# 3) widen the page metas to the 4-course reality
meta_swaps = [
    ('<title>مقالات آموزش زبان آپ‌ورد | نکات یادگیری انگلیسی، مکالمه و تلفظ</title>',
     '<title>مقالات و دوره‌های آموزش زبان آپ‌ورد | انگلیسی، آلمانی، روسی و چینی</title>'),
    ('<meta name="description" content="مقالات آموزشی آپ‌ورد برای فارسی‌زبان‌ها: یادگیری انگلیسی در خانه، تمرین مکالمه با هوش مصنوعی، روش شدوینگ، واژگان و انگیزه — هر روز یک نکته تازه.">',
     '<meta name="description" content="دوره‌های کامل و رایگان زبان برای فارسی‌زبان‌ها: انگلیسی، آلمانی، روسی و چینی از صفر تا مکالمه — به‌همراه مقالات مکالمه با هوش مصنوعی، شدوینگ و واژگان.">'),
    ('<meta property="og:title" content="مقالات آموزش زبان آپ‌ورد">',
     '<meta property="og:title" content="مقالات و دوره‌های آموزش زبان آپ‌ورد">'),
    ('<meta property="og:description" content="یادگیری انگلیسی در خانه، مکالمه با هوش مصنوعی، روش شدوینگ و نکات عملی — مقالات تازه هر روز.">',
     '<meta property="og:description" content="دوره‌های کامل انگلیسی، آلمانی، روسی و چینی از صفر تا مکالمه، به‌همراه نکات عملی یادگیری زبان.">'),
    ('<meta name="twitter:title" content="مقالات آموزش زبان آپ‌ورد">',
     '<meta name="twitter:title" content="مقالات و دوره‌های آموزش زبان آپ‌ورد">'),
    ('<meta name="twitter:description" content="یادگیری انگلیسی در خانه، مکالمه با هوش مصنوعی، روش شدوینگ و نکات عملی — مقالات تازه هر روز.">',
     '<meta name="twitter:description" content="دوره‌های کامل انگلیسی، آلمانی، روسی و چینی از صفر تا مکالمه، به‌همراه نکات عملی یادگیری زبان.">'),
]
for old, new in meta_swaps:
    if old in src:
        src = src.replace(old, new)
    else:
        print('meta swap MISS:', old[:60])

io.open(P, 'w', encoding='utf-8').write(src)
print('index.html updated')

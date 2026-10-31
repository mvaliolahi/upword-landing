#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The 90-DAY GERMAN course builder (v134) — the engine for the programmer-
immigration German course, data-driven from scripts/de_course_data_*.py
modules. Mirrors en_course_lib.py (the English course's proven builder):

  blog/articles/german-*.html — the SEO web article (source of truth)
  blog/content/german-*.json  — derived by extract_article_content.py for
                                the app's native reader (run separately)
  blog/german-course.html     — the hub (فهرست ۹۰ درس) with 5 phase blocks
  blog/posts.json entries     — hub first, then lessons 1..90 in order
  sitemap.xml / feed.xml      — one row per article + the hub

The 90 lessons are authored COMPLETE (base + dialogue + grammar + mistakes
+ drills + challenge + tips in their final section order) — no multi-stage
merging pass.

Audience: a Persian-speaking programmer planning to immigrate to a
German-speaking country (Germany first, Austria/Switzerland acknowledged)
to live and work. Examples ride on dev life (Standup, Code Review, Tickets)
and immigration reality (Anmeldung, Termin, Ausländerbehörde).
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOG = os.path.join(ROOT, 'blog')

TOTAL = 90
CATEGORY = 'آموزش زبان آلمانی (دورهٔ ۹۰ روزه)'
DATE = '2026-10-25'
DATE_FA = '۳ آبان ۱۴۰۵'
HUB_SLUG = 'german-course'
COVER_PREFIX = 'de-course-p'

FA = '۰۱۲۳۴۵۶۷۸۹'


def fa_num(n: int) -> str:
    return ''.join(FA[int(c)] for c in str(n))


# ── inline markup: **bold**, `code` ───────────────────────────────────────
def inline(text: str) -> str:
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    return text


# ── block renderers ───────────────────────────────────────────────────────
def render_block(b) -> str:
    kind = b[0]
    if kind == 'p':
        return f'\n<p>{inline(b[1])}</p>'
    if kind == 'ex':
        return (f'\n<div class="zh-ex"><span class="zh">{b[1]}</span>'
                f'<span class="fa">{b[2]}</span></div>')
    if kind == 'ex3':
        return (f'\n<div class="zh-ex"><span class="zh">{b[1]}</span>'
                f'<span class="py">{b[2]}</span><span class="fa">{b[3]}</span></div>')
    if kind == 'table':
        heads, rows = b[1], b[2]
        out = '\n<table><thead><tr>\n'
        for h in heads:
            out += f'<th>{inline(h)}</th>\n'
        out += '</tr></thead><tbody>\n'
        for row in rows:
            out += '<tr>\n'
            for c in row:
                out += f'<td>{inline(c)}</td>\n'
            out += '</tr>\n'
        out += '</tbody></table>'
        return out
    if kind == 'ul':
        out = '\n<ul>'
        for it in b[1]:
            out += f'\n<li>{inline(it)}</li>'
        return out + '\n</ul>'
    if kind == 'ol':
        out = '\n<ol>'
        for it in b[1]:
            out += f'\n<li>{inline(it)}</li>'
        return out + '\n</ol>'
    if kind == 'quote':
        return f'\n<blockquote>{inline(b[1])}</blockquote>'
    if kind == 'faq':
        out = ('\n<section class="article-faq" aria-label="پاسخ تمرین‌ها">\n'
               '<h2>پاسخ تمرین‌ها — اول خودت جواب بده، بعد باز کن</h2>\n')
        for i, (q, a) in enumerate(b[1]):
            out += (f'\n<details class="faq-item"{" open" if i == 0 else ""}>\n'
                    f'<summary><span>{inline(q)}</span></summary>\n'
                    f'<div class="faq-answer">{inline(a)}</div>\n</details>\n')
        out += '\n</section>'
        return out
    if kind == 'callout':
        return (f'\n<div class="short-answer"><span class="sa-label">{b[1]}</span>'
                f'\n<p>{inline(b[2])}</p></div>')
    raise ValueError(f'unknown block kind: {kind}')


def render_prose(lesson: dict) -> str:
    out = ''
    for para in lesson['intro']:
        out += f'\n<p>{inline(para)}</p>'
    for sec in lesson['sections']:
        out += f'\n<h2>{inline(sec["h2"])}</h2>'
        for b in sec['blocks']:
            out += render_block(b)
    if lesson.get('takeaway'):
        out += (f'\n<div class="short-answer"><span class="sa-label">🔑 جمع‌بندی این درس</span>'
                f'\n<p>{inline(lesson["takeaway"])}</p></div>')
    return out


# ── the article page ──────────────────────────────────────────────────────
def word_count(prose_html: str) -> int:
    text = re.sub(r'<[^>]+>', ' ', prose_html)
    return len(re.findall(r'\S+', text))


def minutes_of(words: int, floor: int = 6) -> int:
    return max(floor, round(words / 95))


def render_article(lesson: dict, n: int, prev, nxt) -> str:
    prose = render_prose(lesson)
    words = word_count(prose)
    minutes = minutes_of(words)
    slug = lesson['slug']
    num_fa = fa_num(n)
    title = lesson['title']
    desc = lesson['desc']
    faqs = lesson.get('faq', [])
    cover = lesson.get('cover', f'covers/{COVER_PREFIX}{PHASE_OF[n]}.jpg')
    prev_html = (
        f'<a class="prev" href="/blog/articles/{prev["slug"]}.html"><span class="lbl">← درس قبلی</span><span>{prev["title"]}</span></a>'
        if prev else
        '<a class=\'prev\' href=\'/blog/\'><span class=\'lbl\'>← مقالات</span><span>بازگشت به وبلاگ</span></a>')
    nxt_html = (
        f'<a class="next" href="/blog/articles/{nxt["slug"]}.html"><span class="lbl">درس بعدی →</span><span>{nxt["title"]}</span></a>'
        if nxt else
        f'<a class="next" href="/blog/german-course.html"><span class="lbl">فهرست دوره →</span><span>جمع‌بندی و نقشهٔ ادامهٔ مسیر</span></a>')
    jsonld_faq = ''
    if faqs:
        qa = ','.join(
            '{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}'
            % (q.replace('"', '&quot;'), a.replace('"', '&quot;'))
            for q, a in faqs)
        jsonld_faq = (',{"@type":"FAQPage","mainEntity":[' + qa + ']}')
    faq_html = ''
    if faqs:
        items = ''.join(
            f'<details class="faq-item"{" open" if i == 0 else ""}>\n<summary><span>{q}</span></summary>\n<div class="faq-answer">{a}</div>\n</details>'
            for i, (q, a) in enumerate(faqs))
        faq_html = (f'\n<section class="article-faq" aria-label="پرسش‌های رایج">\n<h2>پرسش‌های رایج</h2>\n{items}\n</section>')
    related = lesson.get('related', [])
    rel_html = ''
    if related:
        cards = ''
        for r in related:
            cards += (f'<a href="/blog/articles/{r["slug"]}.html">\n'
                      f'<span class="rel-cat">{CATEGORY}</span>\n'
                      f'<span class="rel-title">{r["title"]}</span>\n'
                      f'<span class="rel-meta">⏱ {fa_num(r["minutes"])} دقیقه مطالعه</span>\n</a>\n')
        rel_html = (f'\n<section class="related" aria-label="ادامهٔ دوره">\n<h2>ادامهٔ مسیر یادگیری</h2>\n'
                    f'<div class="related-grid">\n{cards}\n</div>\n</section>')

    return f'''<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#04231A">
<title>درس {num_fa} از ۹۰ · {title} | آپ‌ورد</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<link rel="canonical" href="https://upword.ir/blog/articles/{slug}.html">
<meta property="og:type" content="article">
<meta property="og:title" content="درس {num_fa} از ۹۰ · {title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="https://upword.ir/blog/articles/{slug}.html">
<meta property="og:site_name" content="آپ‌ورد (UpWord)">
<meta property="og:locale" content="fa_IR">
<meta property="og:image" content="https://upword.ir/blog/{cover}">
<meta property="og:image:width" content="1344">
<meta property="og:image:height" content="768">
<meta property="article:published_time" content="{DATE}T09:00:00+03:30">
<meta property="article:modified_time" content="{DATE}T09:00:00+03:30">
<meta property="article:section" content="{CATEGORY}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="درس {num_fa} از ۹۰ · {title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="https://upword.ir/blog/{cover}">
<link rel="icon" type="image/png" href="/assets/images/app-icon.png">
<link rel="apple-touch-icon" type="image/png" href="/assets/images/app-icon.png">
<link rel="preload" href="/assets/fonts/vazirmatn-ar.woff2" as="font" type="font/woff2" crossorigin>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "BlogPosting",
      "@id": "https://upword.ir/blog/articles/{slug}.html#article",
      "headline": "درس {num_fa} از ۹۰ · {title}",
      "description": "{desc}",
      "inLanguage": "fa-IR",
      "image": "https://upword.ir/blog/{cover}",
      "datePublished": "{DATE}T09:00:00+03:30",
      "dateModified": "{DATE}T09:00:00+03:30",
      "wordCount": {words},
      "keywords": "{lesson.get('keywords', '')}",
      "articleSection": "{CATEGORY}",
      "author": {{ "@id": "https://upword.ir/#organization" }},
      "publisher": {{ "@id": "https://upword.ir/#organization" }},
      "mainEntityOfPage": {{ "@type": "WebPage", "@id": "https://upword.ir/blog/articles/{slug}.html" }}
    }},
    {{
      "@type": "BreadcrumbList",
      "itemListElement": [
        {{ "@type": "ListItem", "position": 1, "name": "خانه", "item": "https://upword.ir/" }},
        {{ "@type": "ListItem", "position": 2, "name": "دورهٔ ۹۰ روزهٔ آلمانی", "item": "https://upword.ir/blog/german-course.html" }},
        {{ "@type": "ListItem", "position": 3, "name": "درس {num_fa}" }}
      ]
    }}{jsonld_faq}
  ]
}}
</script>
<link rel="stylesheet" href="/css/styles.css">
<link rel="stylesheet" href="/css/blog.css">
</head>
<body>
<div class="bg-scene" aria-hidden="true">
<div class="orb orb-a"></div>
<div class="orb orb-b"></div>
<div class="orb orb-c"></div>
<div class="bg-grain"></div>
</div>
<header class="navbar" id="navbar">
<div class="container nav-inner">
<a href="/" class="brand" aria-label="آپ‌ورد">
<img src="/assets/images/app-icon.png" alt="" width="40" height="40" class="brand-icon">
<span class="brand-text">آپ‌ورد</span>
</a>
<nav class="nav-links" aria-label="ناوبری وبلاگ">
<a href="/" class="nav-link">صفحه اصلی</a>
<a href="/blog/" class="nav-link">مقالات</a>
<a href="/blog/german-course.html" class="nav-link">دورهٔ آلمانی</a>
<a href="/blog/english-course.html" class="nav-link">دورهٔ انگلیسی</a>
<a href="/blog/chinese-course.html" class="nav-link">دورهٔ چینی</a>
</nav>
<a href="https://cafebazaar.ir/app/?id=ir.upword.twa" target="_blank" rel="noopener" class="btn btn-primary btn-sm nav-cta">
<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M19 9h-4V3H9v6H5l7 7 7-7zM5 18v2h14v-2H5z"/></svg>
<span>دانلود اپ</span>
</a>
</div>
</header>
<main id="main" class="blog-page">
<div class="container">
<div class="article-wrap">
<nav class="crumbs" aria-label="مسیر صفحه">
<a href="/">خانه</a><span class="sep">/</span>
<a href="/blog/german-course.html">دورهٔ ۹۰ روزهٔ آلمانی</a><span class="sep">/</span>
<span class="cur">درس {num_fa} از ۹۰</span>
</nav>
<article class="article-card">
<div class="article-head">
<span class="post-chip">{CATEGORY} · درس {num_fa} از ۹۰</span>
<h1>{title}</h1>
<div class="article-meta">
<span><time datetime="{DATE}">🗓 {DATE_FA}</time></span>
<span>⏱ {fa_num(minutes)} دقیقه مطالعه</span>
<span>✍ تیم آپ‌ورد</span>
</div>
</div>
<div class="short-answer">
<span class="sa-label">⚡ پاسخ کوتاه</span>
<p>{inline(lesson['answer'])}</p>
</div>
<figure class="article-cover">
<img src="/blog/{cover}" alt="" width="1344" height="768" loading="lazy">
<figcaption>درس {num_fa} از ۹۰ — {title}</figcaption>
</figure>
<div class="prose">{prose}
</div>
<nav class="lesson-nav" aria-label="ناوبری دوره">
{prev_html}
<a class="hub" href="/blog/german-course.html">📘 فهرست دوره</a>
{nxt_html}
</nav>
{faq_html}
{rel_html}
</article>

<section class="blog-cta">
<h2>آلمانی را همین امروز در گوشی‌ات تمرین کن</h2>
<p>واژه‌های این درس را هر جا که دیدی با منوی «ذخیره در آپ‌ورد» به فلش‌کارت‌هایت اضافه کن؛ الگوریتم مرور فاصله‌دار سرِ موعد یادآوری‌شان می‌کند، تلفظ‌شان را با صدای آلمانی می‌شنوی و در مکالمهٔ هوش مصنوعی همان‌جا که لازم است استفاده‌شان می‌کنی.</p>
<div class="cta-buttons">
<a href="https://cafebazaar.ir/app/?id=ir.upword.twa" target="_blank" rel="noopener" class="btn btn-primary btn-lg">دانلود از کافه بازار</a>
</div>
</section>
</div>
</div>
</main>
<footer class="blog-footer">
<div class="container inner">
<div class="links">
<a href="/">صفحه اصلی</a>
<a href="/blog/">مقالات</a>
<a href="/blog/german-course.html">دورهٔ ۹۰ روزهٔ آلمانی</a>
<a href="/blog/english-course.html">دورهٔ ۹۰ درسی انگلیسی</a>
<a href="/blog/chinese-course.html">دورهٔ زبان چینی</a>
</div>
<p class="copy">© ۲۰۲۶ آپ‌ورد — ساخته‌شده برای فارسی‌زبان‌ها</p>
</div>
</footer>
<script src="/js/main.js" defer></script>
<script src="/js/blog.js" defer></script>
</body>
</html>
'''


# ── the hub page ──────────────────────────────────────────────────────────
PHASES = [
    (1, 15, 'فاز ۱ · روزهای اول: از «Hallo» تا اولین جمله‌ها',
     'فرض ما این است که هیچ آلمانی بلد نیستی و نقشهٔ مهاجرت داری. این پانزده درس صداها و ä و ö و ü، مهم‌ترین انتخابِ اجتماعی زبان (du یا Sie)، قانون طلایی جای فعل، der/die/das و اعداد و ساعت را می‌سازد — همهٔ چیزهایی که برای روزهای اولِ فرودگاه تا Anmeldung لازم داری.'),
    (16, 33, 'فاز ۲ · زندگی روزمره در آلمان',
     'از اینجا دوره «زبان برای اداره و خیابان» می‌شود: سوپرمارکت و Pfand، تاکسی و مترو و بلیت، بانک و بیمه و دکتر، آپارتمان و همسایه‌ها و تفکیک زباله، نامهٔ رسمی و اضطرارها — هر درس یک موقعیت واقعیِ زندگی مهاجر با جمله‌های آمادهٔ استفاده.'),
    (34, 52, 'فاز ۳ · آلمانیِ برنامه‌نویس در محیط کار',
     'قلب تخصصی دوره: اولین روز کار، استندآپ و اسکرام، ایمیل و چت کاری، کدریویو و جلسه، وضعیتِ تسک و ددلاین، گزارش باگ و دیپلوی، قرارداد و حقوق و مرخصی، مصاحبهٔ فنی و رزومهٔ آلمانی (Lebenslauf) — زبان واقعی تیم‌های نرم‌افزاری آلمان.'),
    (53, 72, 'فاز ۴ · مهاجرت، اداره و استقلال',
     'نقشهٔ بوروکراسی آلمان به آلمانی: ویزا و بلوکارت و Ausländerbehörde، Termin و مدارک، مالیات و Steuer-ID، Krankenkasse و گواهی‌نامهٔ رانندگی، حقوق مستأجر و Verein، Integrationskurs و مسیر B1 تا اقامت دائم و تابعیت.'),
    (73, 90, 'فاز ۵ · حرفه‌ای‌شدن و رشد',
     'گرامرِ روایت و مؤدب‌بودن (Perfekt و Konjunktiv II)، جمله‌های پیچیده و ارائهٔ فنی، تلفن و تعارض و فرهنگ بازخورد آلمانی، گویش‌ها و اتریش و سوئیس، مذاکرهٔ سالانه و مسیر B1 به C1 — از «سرِ هستم» تا «حرفه‌ای حرف می‌زنم».'),
]

PHASE_OF = {}
for _pi, (_lo, _hi, _name, _desc) in enumerate(PHASES, start=1):
    for _n in range(_lo, _hi + 1):
        PHASE_OF[_n] = _pi


def render_hub(lessons, minutes_map) -> str:
    total_minutes = sum(minutes_map.values())
    stats = (f'<div class="course-stats">\n'
             f'<span>📘 ۹۰ درس در ۵ فاز</span>\n'
             f'<span>⏱ مجموعاً {fa_num(total_minutes)} دقیقه مطالعه</span>\n'
             f'<span>🎯 صفر مطلق تا کار و زندگی در کشور آلمانی‌زبان</span>\n'
             f'</div>')
    phases_html = ''
    first = lessons[0]
    for pi, (lo, hi, name, desc) in enumerate(PHASES, start=1):
        links = ''
        for k in range(lo, hi + 1):
            les = lessons[k - 1]
            links += (f'<a class="lesson-link" href="/blog/articles/{les["slug"]}.html">'
                      f'<span class="ll-num">درس {fa_num(k)}</span>'
                      f'<span class="ll-title">{les["title"]}</span>'
                      f'<span class="ll-meta">⏱ {fa_num(minutes_map[les["slug"]])} دقیقه</span></a>')
        phases_html += (f'\n<section class="course-phase" id="phase-{pi}"><h2>{name}</h2>'
                        f'<p class="phase-desc">{desc}</p>'
                        f'<div class="lesson-list">{links}</div></section>')
    return f'''<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#04231A">
<title>دورهٔ کامل زبان آلمانی برای برنامه‌نویس‌ها از صفر تا حرفه‌ای (۹۰ روز) | آپ‌ورد</title>
<meta name="description" content="دورهٔ رایگان ۹۰ روزهٔ زبان آلمانی برای فارسی‌زبان‌ها با محوریت مهاجرت و کارِ برنامه‌نویس‌ها در آلمان، اتریش و سوئیس: از الفبا و Anmeldung و اداره تا استندآپ، کدریویو، مصاحبهٔ فنی، مالیات و اقامت دائم.">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<link rel="canonical" href="https://upword.ir/blog/german-course.html">
<meta property="og:type" content="article">
<meta property="og:title" content="دورهٔ کامل زبان آلمانی برای برنامه‌نویس‌ها — ۹۰ روز">
<meta property="og:description" content="از صفر مطلق تا کار و زندگی در کشور آلمانی‌زبان؛ برای برنامه‌نویس‌هایی که نقشهٔ مهاجرت دارند، همراه با همهٔ مهارت‌های زندگی روزمره و بوروکراسی.">
<meta property="og:url" content="https://upword.ir/blog/german-course.html">
<meta property="og:site_name" content="آپ‌ورد (UpWord)">
<meta property="og:locale" content="fa_IR">
<meta property="og:image" content="https://upword.ir/blog/covers/de-course-p1.jpg">
<meta property="og:image:width" content="1344">
<meta property="og:image:height" content="768">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="دورهٔ کامل زبان آلمانی برای برنامه‌نویس‌ها — ۹۰ روز">
<meta name="twitter:description" content="از صفر مطلق تا کار و زندگی در کشور آلمانی‌زبان؛ برای برنامه‌نویس‌هایی که نقشهٔ مهاجرت دارند.">
<meta name="twitter:image" content="https://upword.ir/blog/covers/de-course-p1.jpg">
<link rel="icon" type="image/png" href="/assets/images/app-icon.png">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "Course",
      "name": "دورهٔ ۹۰ روزهٔ زبان آلمانی از صفر تا حرفه‌ای",
      "description": "دورهٔ رایگان ۹۰ روزهٔ زبان آلمانی برای فارسی‌زبان‌ها با محوریت مهاجرت و کارِ برنامه‌نویس‌ها در کشورهای آلمانی‌زبان.",
      "inLanguage": "fa-IR",
      "provider": {{ "@type": "Organization", "name": "آپ‌ورد (UpWord)", "url": "https://upword.ir" }},
      "hasCourseInstance": {{
        "@type": "CourseInstance",
        "courseMode": "online",
        "courseWorkload": "PT{total_minutes}M"
      }}
    }},
    {{
      "@type": "BreadcrumbList",
      "itemListElement": [
        {{ "@type": "ListItem", "position": 1, "name": "خانه", "item": "https://upword.ir/" }},
        {{ "@type": "ListItem", "position": 2, "name": "مقالات", "item": "https://upword.ir/blog/" }},
        {{ "@type": "ListItem", "position": 3, "name": "دورهٔ ۹۰ روزهٔ آلمانی" }}
      ]
    }}
  ]
}}
</script>
<link rel="stylesheet" href="/css/styles.css">
<link rel="stylesheet" href="/css/blog.css">
</head>
<body>
<div class="bg-scene" aria-hidden="true">
<div class="orb orb-a"></div>
<div class="orb orb-b"></div>
<div class="orb orb-c"></div>
<div class="bg-grain"></div>
</div>
<header class="navbar" id="navbar">
<div class="container nav-inner">
<a href="/" class="brand" aria-label="آپ‌ورد">
<img src="/assets/images/app-icon.png" alt="" width="40" height="40" class="brand-icon">
<span class="brand-text">آپ‌ورد</span>
</a>
<nav class="nav-links" aria-label="ناوبری وبلاگ">
<a href="/" class="nav-link">صفحه اصلی</a>
<a href="/blog/" class="nav-link">مقالات</a>
<a href="/blog/german-course.html" class="nav-link">دورهٔ آلمانی</a>
<a href="/blog/english-course.html" class="nav-link">دورهٔ انگلیسی</a>
<a href="/blog/chinese-course.html" class="nav-link">دورهٔ چینی</a>
</nav>
<a href="https://cafebazaar.ir/app/?id=ir.upword.twa" target="_blank" rel="noopener" class="btn btn-primary btn-sm nav-cta">
<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M19 9h-4V3H9v6H5l7 7 7-7zM5 18v2h14v-2H5z"/></svg>
<span>دانلود اپ</span>
</a>
</div>
</header>
<main id="main" class="blog-page">
<div class="container">
<article class="article-card">
<div class="article-head course-hero">
<span class="post-chip">{CATEGORY}</span>
<h1>دورهٔ کامل زبان آلمانی؛ از صفر تا کار و زندگی</h1>
<p>نود درسِ عمیق اما ساده برای فارسی‌زبانی که هیچ آلمانی بلد نیست و نقشهٔ مهاجرت و کار در کشور آلمانی‌زبان را دارد — از اولین «Hallo» و ثبت‌آدرس و اداره تا استندآپ صبحگاهی، کدریویو، مصاحبهٔ فنی، مالیات و اقامت دائم. محور دوره «زبان برای زندگی و کارِ برنامه‌نویس در آلمان» است: سوپرمارکت و بیمه و اجارهٔ خانه کنار گیت و اسکرام و ارائهٔ فنی.</p>
{stats}
<div class="start-cta">
<a href="/blog/articles/{first['slug']}.html">از درس ۱ شروع کن ←</a>
</div>
</div>
{phases_html}
<section class="course-phase" id="practice">
<h2>در گوشی‌ات آلمانی تمرین کن</h2>
<p class="phase-desc">هر درس این دوره را با اپ آپ‌ورد زنده کن: واژه‌های جدید را حین خواندن همین مقاله‌ها انتخاب کن و «ذخیره در آپ‌ورد» بزن، با مرور فاصله‌دار تا تسلط نگه‌شان دار، تلفظ‌شان را با صدای آلمانی بشنو و در مکالمهٔ هوش مصنوعی از همان درس تمرین کن — بدون این‌که از متن خارج شوی.</p>
</section>
</article>

<section class="blog-cta">
<h2>از درس ۱ همین حالا شروع کن</h2>
<p>اولین فاز کاملاً از صفر شروع می‌شود؛ هیچ پیش‌نیازی جز یک گوشی و روزی ۱۵ دقیقه نمی‌خواهد.</p>
<div class="cta-buttons">
<a href="https://cafebazaar.ir/app/?id=ir.upword.twa" target="_blank" rel="noopener" class="btn btn-primary btn-lg">دانلود از کافه بازار</a>
</div>
</section>
</div>
</main>
<footer class="blog-footer">
<div class="container inner">
<div class="links">
<a href="/">صفحه اصلی</a>
<a href="/blog/">مقالات</a>
<a href="/blog/german-course.html">دورهٔ ۹۰ روزهٔ آلمانی</a>
<a href="/blog/english-course.html">دورهٔ ۹۰ درسی انگلیسی</a>
<a href="/blog/chinese-course.html">دورهٔ زبان چینی</a>
</div>
<p class="copy">© ۲۰۲۶ آپ‌ورد — ساخته‌شده برای فارسی‌زبان‌ها</p>
</div>
</footer>
<script src="/js/main.js" defer></script>
<script src="/js/blog.js" defer></script>
</body>
</html>
'''


# ── registry: posts.json / sitemap / feed ────────────────────────────────
def register_everything(lessons, minutes_map, descs):
    # posts.json — DE block at the very front (newest course), en + zh after
    posts_path = os.path.join(BLOG, 'posts.json')
    data = json.load(open(posts_path, encoding='utf-8'))
    posts = data['posts']
    rest = [p for p in posts if p.get('category') != CATEGORY]
    hub_post = {
        'slug': HUB_SLUG, 'url': 'german-course.html',
        'title': 'دورهٔ کامل زبان آلمانی برای برنامه‌نویس‌ها؛ از صفر تا کار و زندگی (فهرست ۹۰ درس)',
        'desc': 'نقطهٔ شروع: فهرست کامل دورهٔ ۹۰ روزهٔ زبان آلمانی برای فارسی‌زبان‌ها — از الفبا و ثبت‌آدرس و اداره تا استندآپ، کدریویو، مصاحبهٔ فنی، مالیات و اقامت دائم.',
        'category': CATEGORY, 'date': DATE, 'dateFa': DATE_FA,
        'minutes': 3, 'cover': f'covers/{COVER_PREFIX}1.jpg',
        'content': f'content/{HUB_SLUG}.json',
    }
    lesson_posts = []
    for n, les in enumerate(lessons, start=1):
        lesson_posts.append({
            'slug': les['slug'], 'url': f'articles/{les["slug"]}.html',
            'title': f'درس {fa_num(n)} از ۹۰ · {les["title"]}',
            'desc': les['desc'], 'category': CATEGORY,
            'date': DATE, 'dateFa': DATE_FA,
            'minutes': minutes_map[les['slug']],
            'cover': f'covers/{COVER_PREFIX}{PHASE_OF[n]}.jpg',
            'content': f'content/{les["slug"]}.json',
        })
    data['posts'] = [hub_post] + lesson_posts + rest
    data['updated'] = DATE
    with open(posts_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')

    # sitemap — drop any stale german rows, then add the fresh set on top
    sm_path = os.path.join(ROOT, 'sitemap.xml')
    sm = open(sm_path, encoding='utf-8').read()
    sm = re.sub(r'\s*<url>\s*<loc>https://upword\.ir/blog/(articles/german-[a-z0-9-]+\.html|german-course\.html)</loc>[\s\S]*?</url>', '', sm)
    entries = ''
    entries += sitemap_row(f'https://upword.ir/blog/german-course.html', '1.0')
    for les in lessons:
        entries += sitemap_row(f'https://upword.ir/blog/articles/{les["slug"]}.html')
    sm = sm.replace('</urlset>', entries + '</urlset>')
    with open(sm_path, 'w', encoding='utf-8') as f:
        f.write(sm)

    # feed — drop stale GERMAN items only (the English course's «از ۹۰»
    # titles must survive!): the <link> line is the German discriminator.
    feed_path = os.path.join(ROOT, 'feed.xml')
    fd = open(feed_path, encoding='utf-8').read()
    fd = re.sub(r'\s*<item>\s*<title>[^<]*</title>\s*<link>https://upword\.ir/blog/(articles/german-[a-z0-9-]+\.html|german-course\.html)</link>[\s\S]*?</item>', '', fd)
    items = ''
    items += feed_item('دورهٔ کامل زبان آلمانی برای برنامه‌نویس‌ها؛ از صفر تا کار و زندگی (فهرست ۹۰ درس)',
                       'https://upword.ir/blog/german-course.html',
                       hub_post['desc'], f'covers/{COVER_PREFIX}1.jpg')
    for n, les in enumerate(lessons, start=1):
        items += feed_item(f'درس {fa_num(n)} از ۹۰ · {les["title"]}',
                           f'https://upword.ir/blog/articles/{les["slug"]}.html',
                           les['desc'], f'covers/{COVER_PREFIX}{PHASE_OF[n]}.jpg')
    fd = fd.replace('</channel>', items + '</channel>')
    with open(feed_path, 'w', encoding='utf-8') as f:
        f.write(fd)


def sitemap_row(loc, prio='0.8'):
    return (f'\n<url>\n<loc>{loc}</loc>\n<lastmod>{DATE}</lastmod>\n'
            f'<changefreq>monthly</changefreq>\n<priority>{prio}</priority>\n</url>')


def feed_item(title, link, desc, cover):
    return (f'\n<item>\n<title>{escape_xml(title)}</title>\n<link>{link}</link>\n'
            f'<description>{escape_xml(desc)}</description>\n'
            f'<enclosure url="https://upword.ir/blog/{cover}" type="image/jpeg" length="0"/>\n'
            f'<guid isPermaLink="true">{link}</guid>\n<pubDate>Sun, 25 Oct 2026 09:00:00 +0330</pubDate>\n</item>')


def escape_xml(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def write_hub_content_json(lessons, minutes_map, descs):
    """The hub's structured content for the app reader."""
    phases = []
    for pi, (lo, hi, name, desc) in enumerate(PHASES, start=1):
        rows = [[f'درس {fa_num(k)}', lessons[k - 1]['title'], f'{fa_num(minutes_map[lessons[k-1]["slug"]])} دقیقه']
                for k in range(lo, hi + 1)]
        phases.append({'name': name, 'desc': desc, 'rows': rows})
    blocks = [{'type': 'callout', 'label': '⚡ این دوره برای کیست؟',
               'spans': [{'t': 'برای فارسی‌زبانی که هیچ آلمانی بلد نیست و می‌خواهد در کشور آلمانی‌زبان زندگی و کار کند — از ثبت‌آدرس و اداره و بیمه و مالیات تا استندآپ و کدریویو و مصاحبهٔ فنی و مذاکرهٔ حقوق. ۹۰ درس، ۵ فاز، از صفر مطلق، با نگاهِ ویژه به مهاجرتِ برنامه‌نویس‌ها.'}]}]
    for ph in phases:
        blocks.append({'type': 'h2', 'spans': [{'t': ph['name']}]})
        blocks.append({'type': 'p', 'spans': [{'t': ph['desc']}]})
        blocks.append({'type': 'table', 'header': ['درس', 'عنوان', 'زمان'], 'rows': ph['rows']})
    doc = {'meta': {
        'slug': HUB_SLUG,
        'title': 'دورهٔ کامل زبان آلمانی برای برنامه‌نویس‌ها؛ از صفر تا کار و زندگی (فهرست ۹۰ درس)',
        'desc': 'فهرست کامل دورهٔ ۹۰ روزهٔ زبان آلمانی برای فارسی‌زبان‌ها — از صفر تا کار و زندگی در کشور آلمانی‌زبان.',
        'category': CATEGORY, 'cover': f'covers/{COVER_PREFIX}1.jpg',
        'date': DATE, 'dateFa': DATE_FA, 'minutes': 3,
    }, 'blocks': blocks}
    path = os.path.join(BLOG, 'content', f'{HUB_SLUG}.json')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
        f.write('\n')

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The 90-lesson ENGLISH course builder (v131) — the engine shared by all
three authoring stages (design → expand → strengthen).

Everything is data-driven from scripts/en_course_data_*.py modules; this
lib renders the SAME article family the Chinese course uses:

  blog/articles/<slug>.html  — the SEO web article (source of truth)
  blog/content/<slug>.json   — derived by extract_article_content.py for
                               the app's native reader (run separately)
  blog/english-course.html   — the hub (فهرست ۹۰ درس) with 5 phase blocks
  blog/posts.xml entries     — hub first, then lessons 1..90 in order
  sitemap.xml / feed.xml     — one row per article + the hub

Idempotent: re-running rebuilds every generated file from scratch (the
generated set is fully a function of the data files).
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOG = os.path.join(ROOT, 'blog')

TOTAL = 90
CATEGORY = 'آموزش زبان انگلیسی (دورهٔ ۹۰ درسی)'
DATE = '2026-10-24'
DATE_FA = '۲ آبان ۱۴۰۵'
HUB_SLUG = 'english-course'

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
    cover = lesson.get('cover', f'covers/en-course-p{PHASE_OF[n]}.jpg')
    prev_html = (
        f'<a class="prev" href="/blog/articles/{prev["slug"]}.html"><span class="lbl">← درس قبلی</span><span>{prev["title"]}</span></a>'
        if prev else
        '<a class=\'prev\' href=\'/blog/\'><span class=\'lbl\'>← مقالات</span><span>بازگشت به وبلاگ</span></a>')
    nxt_html = (
        f'<a class="next" href="/blog/articles/{nxt["slug"]}.html"><span class="lbl">درس بعدی →</span><span>{nxt["title"]}</span></a>'
        if nxt else
        f'<a class="next" href="/blog/english-course.html"><span class="lbl">فهرست دوره →</span><span>جمع‌بندی و نقشهٔ ادامهٔ مسیر</span></a>')
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
                    f'<div class="related-grid">\n{cards}</div>\n</section>')

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
        {{ "@type": "ListItem", "position": 2, "name": "دورهٔ ۹۰ درسی انگلیسی", "item": "https://upword.ir/blog/english-course.html" }},
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
<a href="/blog/english-course.html">دورهٔ ۹۰ درسی انگلیسی</a><span class="sep">/</span>
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
<a class="hub" href="/blog/english-course.html">📘 فهرست دوره</a>
{nxt_html}
</nav>
{faq_html}
{rel_html}
</article>

<section class="blog-cta">
<h2>انگلیسی را همین امروز در گوشی‌ات تمرین کن</h2>
<p>واژه‌های این درس را هر جا که دیدی با منوی «ذخیره در آپ‌ورد» به فلش‌کارت‌هایت اضافه کن؛ الگوریتم مرور فاصله‌دار سرِ موعد یادآوری‌شان می‌کند، تلفظ‌شان را می‌شنوی و در مکالمهٔ هوش مصنوعی همان‌جا که لازم است استفاده‌شان می‌کنی.</p>
<div class="cta-buttons">
<a href="https://cafebazaar.ir/app/?id=ir.upword.twa" target="_blank" rel="noopener" class="btn btn-primary btn-lg">دانلود از کافه بازار</a>
<a href="https://myket.ir/app/ir.upword.twa" target="_blank" rel="noopener" class="btn btn-ghost btn-lg">دانلود از مایکت</a>
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
    (1, 15, 'فاز ۱ · پایه‌ها: از «Hello» تا اولین جمله‌ها',
     'فرض ما این است که هیچ انگلیسی بلد نیستی. این پانزده درس الفبا و صداها، فعل to be، اعداد و پول و ساعت، خانواده و غذا و خریدِ ساده را می‌سازد — یعنی همهٔ چیزهایی که برای زنده‌ماندن در روزهای اول لازم داری.'),
    (16, 33, 'فاز ۲ · زندگی روزمره در کشور انگلیسی‌زبان',
     'از اینجا دوره «حرف‌زدن برای زندگی» می‌شود: رستوران و سوپرمارکت، تاکسی و مترو، دکتر و داروخانه، تلفن و وقت‌گذاشتن، خانه و همسایه‌ها — هر درس یک موقعیت واقعی با جمله‌های آمادهٔ استفاده.'),
    (34, 50, 'فاز ۳ · استقلال: سفر، خانه و اولین کار',
     'زمان‌های گذشته و آینده، فرودگاه و هتل، اجارهٔ خانه و قبض‌ها، اضطراری‌ها، دوست‌یابی و اولین قدم‌های کاری: رزومه، مصاحبهٔ عمومی و روز اول در محیط کار.'),
    (51, 72, 'فاز ۴ · برنامه‌نویس در محیط کار',
     'قلب تخصصی دوره: استندآپ و کدریویو، گیت و اسکرام، دیباگ و تخمین، اسلک و ایمیل فنی، مصاحبه‌های coding و system design و رفتاری، دمو و ارائه — زبان واقعی تیم‌های نرم‌افزاری.'),
    (73, 90, 'فاز ۵ · حرفه‌ای‌شدن: رهبری، مذاکره و فرهنگ',
     'لحن و رجیستر، اصطلاحات و phrasal verbs کاری، جلسه‌گردانی و RFC، ارائه برای مدیران، مذاکرهٔ حقوق، مدیریت حادثه، فرهنگ مکالمهٔ انگلیسی‌زبان‌ها و نقشهٔ بعد از این دوره.'),
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
             f'<span>🎯 صفر مطلق تا مکالمهٔ حرفه‌ای در محیط فنی</span>\n'
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
<title>دورهٔ کامل انگلیسی از صفر تا حرفه‌ای (۹۰ درس) | آپ‌ورد</title>
<meta name="description" content="دورهٔ رایگان ۹۰ درسی زبان انگلیسی برای فارسی‌زبان‌ها با محوریت کار برنامه‌نویس‌ها و دانشجویان تکنولوژی: از الفبا و خرید و دکتر و تاکسی تا استندآپ، کدریویو، مصاحبهٔ فنی، مذاکرهٔ حقوق و رهبری تیم.">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<link rel="canonical" href="https://upword.ir/blog/english-course.html">
<meta property="og:type" content="article">
<meta property="og:title" content="دورهٔ کامل انگلیسی از صفر تا حرفه‌ای — ۹۰ درس">
<meta property="og:description" content="از صفر مطلق تا مکالمهٔ حرفه‌ای در محیط فنی؛ برای برنامه‌نویس‌ها و دانشجویان تکنولوژی، همراه با همهٔ مهارت‌های زندگی روزمره.">
<meta property="og:url" content="https://upword.ir/blog/english-course.html">
<meta property="og:site_name" content="آپ‌ورد (UpWord)">
<meta property="og:locale" content="fa_IR">
<meta property="og:image" content="https://upword.ir/blog/covers/en-course-p1.jpg">
<meta property="og:image:width" content="1344">
<meta property="og:image:height" content="768">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="دورهٔ کامل انگلیسی از صفر تا حرفه‌ای — ۹۰ درس">
<meta name="twitter:description" content="از صفر مطلق تا مکالمهٔ حرفه‌ای در محیط فنی؛ برای برنامه‌نویس‌ها و دانشجویان تکنولوژی.">
<meta name="twitter:image" content="https://upword.ir/blog/covers/en-course-p1.jpg">
<link rel="icon" type="image/png" href="/assets/images/app-icon.png">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "Course",
      "name": "دورهٔ ۹۰ درسی زبان انگلیسی از صفر تا حرفه‌ای",
      "description": "دورهٔ رایگان ۹۰ درسی زبان انگلیسی برای فارسی‌زبان‌ها با محوریت کار برنامه‌نویس‌ها و دانشجویان تکنولوژی.",
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
        {{ "@type": "ListItem", "position": 3, "name": "دورهٔ ۹۰ درسی انگلیسی" }}
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
<h1>دورهٔ کامل زبان انگلیسی؛ از صفر تا حرفه‌ای</h1>
<p>نود درسِ عمیق اما ساده برای فارسی‌زبانی که هیچ انگلیسیِ واقعی بلد نیست — از اولین «Hello» تا استندآپ صبحگاهی، کدریویو، مصاحبهٔ فنی و مذاکرهٔ حقوق. محور دوره «زبان برای زندگی و کارِ برنامه‌نویس‌ها و دانشجویان تکنولوژی» است: خرید و دکتر و تاکسی و اجارهٔ خانه کنار گیت و اسکرام و ارائهٔ فنی.</p>
{stats}
<div class="start-cta">
<a href="/blog/articles/{first['slug']}.html">از درس ۱ شروع کن ←</a>
</div>
</div>
{phases_html}
<section class="course-phase" id="practice">
<h2>در گوشی‌ات انگلیسی تمرین کن</h2>
<p class="phase-desc">هر درس این دوره را با اپ آپ‌ورد زنده کن: واژه‌های جدید را حین خواندن همین مقاله‌ها انتخاب کن و «ذخیره در آپ‌ورد» بزن، با مرور فاصله‌دار تا تسلط نگه‌شان دار، تلفظ‌شان را بشنو و در مکالمهٔ هوش مصنوعی از همان درس تمرین کن — بدون این‌که از متن خارج شوی.</p>
</section>
</article>

<section class="blog-cta">
<h2>از درس ۱ همین حالا شروع کن</h2>
<p>اولین فاز کاملاً از صفر شروع می‌شود؛ هیچ پیش‌نیازی جز یک گوشی و روزی ۱۵ دقیقه نمی‌خواهد.</p>
<div class="cta-buttons">
<a href="https://cafebazaar.ir/app/?id=ir.upword.twa" target="_blank" rel="noopener" class="btn btn-primary btn-lg">دانلود از کافه بازار</a>
<a href="https://myket.ir/app/ir.upword.twa" target="_blank" rel="noopener" class="btn btn-ghost btn-lg">دانلود از مایکت</a>
</div>
</section>
</div>
</main>
<footer class="blog-footer">
<div class="container inner">
<div class="links">
<a href="/">صفحه اصلی</a>
<a href="/blog/">مقالات</a>
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
def load_lessons(stage_modules):
    """stage_modules: list of module objects each exposing LESSONS/EXPANSIONS."""
    lessons = []
    expansions = {}
    for mod in stage_modules:
        if hasattr(mod, 'LESSONS'):
            lessons.extend(mod.LESSONS)
        if hasattr(mod, 'EXPANSIONS'):
            expansions.update(mod.EXPANSIONS)
    return lessons, expansions


def apply_expansions(lessons, expansions):
    """Stage 2/3: append each expansion's extra sections + dialogue before
    the takeaway. Expansion dict: slug -> {extra_sections: [...], dialogue: (title, rows),
    grammar: (h2, blocks), tips: [...]}."""
    by_slug = {l['slug']: l for l in lessons}
    for slug, exp in expansions.items():
        les = by_slug.get(slug)
        if les is None:
            continue
        if exp.get('grammar'):
            h2, blocks = exp['grammar']
            les['sections'].append({'h2': h2, 'blocks': blocks})
        if exp.get('extra_sections'):
            les['sections'].extend(exp['extra_sections'])
        if exp.get('tips'):
            tip_items = [t if isinstance(t, str) else ('**' + t[0] + '** — ' + t[1]) for t in exp['tips']]
            les['sections'].append({'h2': 'نکات مکالمهٔ واقعی که کتاب‌ها کم می‌گویند', 'blocks': [('ul', tip_items)]})
    return lessons


def register_everything(lessons, minutes_map, descs):
    # posts.json — EN block at the very front (newest course), zh stays after
    posts_path = os.path.join(BLOG, 'posts.json')
    data = json.load(open(posts_path, encoding='utf-8'))
    posts = data['posts']
    rest = [p for p in posts if p.get('category') != CATEGORY]
    hub_post = {
        'slug': HUB_SLUG, 'url': 'english-course.html',
        'title': 'دورهٔ کامل زبان انگلیسی؛ از صفر تا حرفه‌ای (فهرست ۹۰ درس)',
        'desc': 'نقطهٔ شروع: فهرست کامل دورهٔ ۹۰ درسی زبان انگلیسی برای فارسی‌زبان‌ها — از الفبا و زندگی روزمره تا استندآپ، کدریویو، مصاحبهٔ فنی و مذاکرهٔ حقوق.',
        'category': CATEGORY, 'date': DATE, 'dateFa': DATE_FA,
        'minutes': 3, 'cover': 'covers/en-course-p1.jpg',
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
            'cover': f'covers/en-course-p{PHASE_OF[n]}.jpg',
            'content': f'content/{les["slug"]}.json',
        })
    data['posts'] = [hub_post] + lesson_posts + rest
    with open(posts_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')

    # sitemap
    sm_path = os.path.join(ROOT, 'sitemap.xml')
    sm = open(sm_path, encoding='utf-8').read()
    sm = re.sub(r'\s*<url>\s*<loc>https://upword\.ir/blog/(articles/[a-z0-9-]+\.html|english-course\.html)</loc>[\s\S]*?</url>', '', sm)
    entries = ''
    entries += sitemap_row(f'https://upword.ir/blog/english-course.html', '1.0')
    for les in lessons:
        entries += sitemap_row(f'https://upword.ir/blog/articles/{les["slug"]}.html')
    sm = sm.replace('</urlset>', entries + '</urlset>')
    open(sm_path, 'w', encoding='utf-8').write(sm)

    # feed
    feed_path = os.path.join(ROOT, 'feed.xml')
    fd = open(feed_path, encoding='utf-8').read()
    fd = re.sub(r'\s*<item>\s*<title>درس [^<]*از ۹۰[^<]*</title>[\s\S]*?</item>', '', fd)
    fd = re.sub(r'\s*<item>\s*<title>دورهٔ کامل زبان انگلیسی[^<]*</title>[\s\S]*?</item>', '', fd)
    items = ''
    items += feed_item(f'دورهٔ کامل زبان انگلیسی؛ از صفر تا حرفه‌ای (فهرست ۹۰ درس)',
                       f'https://upword.ir/blog/english-course.html',
                       hub_post['desc'], 'covers/en-course-p1.jpg')
    for n, les in enumerate(lessons, start=1):
        items += feed_item(f'درس {fa_num(n)} از ۹۰ · {les["title"]}',
                           f'https://upword.ir/blog/articles/{les["slug"]}.html',
                           les['desc'], f'covers/en-course-p{PHASE_OF[n]}.jpg')
    fd = fd.replace('</channel>', items + '</channel>')
    open(feed_path, 'w', encoding='utf-8').write(fd)


def sitemap_row(loc, prio='0.8'):
    return (f'\n<url>\n<loc>{loc}</loc>\n<lastmod>{DATE}</lastmod>\n'
            f'<changefreq>monthly</changefreq>\n<priority>{prio}</priority>\n</url>')


def feed_item(title, link, desc, cover):
    return (f'\n<item>\n<title>{escape_xml(title)}</title>\n<link>{link}</link>\n'
            f'<description>{escape_xml(desc)}</description>\n'
            f'<enclosure url="https://upword.ir/blog/{cover}" type="image/jpeg" length="0"/>\n'
            f'<guid isPermaLink="true">{link}</guid>\n<pubDate>Fri, 24 Oct 2026 09:00:00 +0330</pubDate>\n</item>')


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
               'spans': [{'t': 'برای فارسی‌زبانی که هیچ انگلیسیِ واقعی بلد نیست و می‌خواهد هم در زندگی روزمرهٔ یک کشور انگلیسی‌زبان دوام بیاورد و هم در محیط کار فنی — از استندآپ و کدریویو تا مصاحبه و مذاکرهٔ حقوق — حرفه‌ای حرف بزند. ۹۰ درس، ۵ فاز، از صفر مطلق.'}]}]
    for ph in phases:
        blocks.append({'type': 'h2', 'spans': [{'t': ph['name']}]})
        blocks.append({'type': 'p', 'spans': [{'t': ph['desc']}]})
        blocks.append({'type': 'table', 'header': ['درس', 'عنوان', 'زمان'], 'rows': ph['rows']})
    doc = {'meta': {
        'slug': HUB_SLUG,
        'title': 'دورهٔ کامل زبان انگلیسی؛ از صفر تا حرفه‌ای (فهرست ۹۰ درس)',
        'desc': 'فهرست کامل دورهٔ ۹۰ درسی زبان انگلیسی برای فارسی‌زبان‌ها — از صفر تا مکالمهٔ حرفه‌ای در محیط فنی.',
        'category': CATEGORY, 'cover': 'covers/en-course-p1.jpg',
        'date': DATE, 'dateFa': DATE_FA, 'minutes': 3,
    }, 'blocks': blocks}
    path = os.path.join(BLOG, 'content', f'{HUB_SLUG}.json')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
        f.write('\n')

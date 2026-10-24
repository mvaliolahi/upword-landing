#!/usr/bin/env python3
"""Number the 50-lesson Chinese course so the learner can see the order
EVERYWHERE the titles appear:

  1. posts.json  — the manifest the APP's native article list renders
     (the owner's ask: «تا کاربر بفهمه ترتیب مقالات به چه صورته») and
     the web blog index (js/blog.js renders the same titles).
     Title becomes: «درس N از ۵۰ · <old>». The hub post
     (chinese-course — the ordered index) moves to the FRONT of the
     course block so the course category starts with its فهرست.
  2. each lesson article's SEO surfaces — <title>, og:title,
     twitter:title, JSON-LD headline, and the BreadcrumbList tail
     (which was inconsistent: «درس ۴ — چینی»).
  3. feed.xml — the static RSS items carry the same numbered titles.

Idempotent: skips titles already carrying the «درس N از ۵۰ ·» prefix.
"""
import json
import re
import sys
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOG = os.path.join(ROOT, 'blog')

FA_DIGITS = '۰۱۲۳۴۵۶۷۸۹'


def fa_num(n: int) -> str:
    return ''.join(FA_DIGITS[int(c)] for c in str(n))


def main() -> None:
    posts_path = os.path.join(BLOG, 'posts.json')
    data = json.load(open(posts_path, encoding='utf-8'))
    posts = data['posts']

    zh = [p for p in posts if p.get('category') == 'آموزش زبان چینی']
    lessons = [p for p in zh if p['slug'] != 'chinese-course']
    hub = next(p for p in zh if p['slug'] == 'chinese-course')
    assert len(lessons) == 50, f'expected 50 lessons, got {len(lessons)}'

    # ── 1. posts.json titles ─────────────────────────────────────────
    numbered = {}   # slug -> (n, old_title, new_title)
    for i, p in enumerate(lessons, start=1):
        old = p['title']
        prefix = f'درس {fa_num(i)} از ۵۰'
        if old.startswith(prefix):
            new = old
        else:
            # strip any stale prefix, then re-apply
            stripped = re.sub(r'^درس [۰-۹]+ از ۵۰\s*[·:—-]*\s*', '', old)
            new = f'{prefix} · {stripped}'
        p['title'] = new
        numbered[p['slug']] = (i, old, new)

    # move the hub to the front of the course block (it is the فهرست)
    zh_new = [hub] + lessons
    rest = [p for p in posts if p.get('category') != 'آموزش زبان چینی']
    data['posts'] = zh_new + rest
    with open(posts_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')

    # ── 2. article SEO surfaces ──────────────────────────────────────
    for slug, (n, old, new) in numbered.items():
        path = os.path.join(BLOG, 'articles', slug + '.html')
        html = open(path, encoding='utf-8').read()
        prefix = f'درس {fa_num(n)} از ۵۰'
        # <title>old | آپ‌ورد</title>
        html = html.replace(f'<title>{old} | آپ‌ورد</title>',
                            f'<title>{prefix} · {old} | آپ‌ورد</title>')
        # og/twitter/title content="old"
        html = re.sub(r'(og:title" content=")' + re.escape(old) + '"',
                      r'\g<1>' + prefix + ' · ' + old + '"', html)
        html = re.sub(r'(twitter:title" content=")' + re.escape(old) + '"',
                      r'\g<1>' + prefix + ' · ' + old + '"', html)
        # JSON-LD headline
        html = re.sub(r'("headline":\s*")' + re.escape(old) + '"',
                      r'\g<1>' + prefix + ' · ' + old + '"', html)
        # BreadcrumbList tail — normalize whatever it was to «درس N از ۵۰»
        html = re.sub(r'("position": 3, "name": ")[^"]*(")',
                      r'\g<1>' + prefix + r'\g<2>', html)
        open(path, 'w', encoding='utf-8').write(html)

    # ── 3. feed.xml ──────────────────────────────────────────────────
    feed_path = os.path.join(ROOT, 'feed.xml')
    feed = open(feed_path, encoding='utf-8').read()
    for slug, (n, old, new) in numbered.items():
        feed = feed.replace(f'<title>{old}</title>', f'<title>{new}</title>')
    open(feed_path, 'w', encoding='utf-8').write(feed)

    print(f'numbered {len(numbered)} lessons; hub moved to front; feed synced')
    for slug, (n, old, new) in list(numbered.items())[:3]:
        print(f'  {n}: {new[:70]}…')


if __name__ == '__main__':
    sys.exit(main())

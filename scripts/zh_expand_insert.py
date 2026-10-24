#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert the 50 expansion packs into the lesson articles + sync metadata.

For every lesson (posts.json order):
  1. insert the pack's HTML right before the .prose closing </div>
     (i.e. before `\n</div>\n<nav class="lesson-nav"`);
  2. recount the prose words -> JSON-LD wordCount;
  3. recompute minutes = max(old, round(words / 95)) and sync:
       - posts.json
       - the article's own visible meta (⏱ N دقیقه مطالعه)
       - the hub page's lesson list (⏱ N دقیقه)
       - every OTHER article's related-grid entry linking to the lesson
  4. (run separately) regenerate blog/content/*.json with the upgraded
     extractor.

Idempotent: skips lessons whose prose already contains the pack's
signature heading.
"""
import importlib.util
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOG = os.path.join(ROOT, 'blog')
FA = '۰۱۲۳۴۵۶۷۸۹'


def fa_num(n):
    return ''.join(FA[int(c)] for c in str(n))


def load_packs():
    packs = {}
    for phase in range(1, 6):
        path = os.path.join(ROOT, 'scripts', f'zh_expand_phase{phase}.py')
        spec = importlib.util.spec_from_file_location(f'p{phase}', path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        packs.update(mod.EXPANSIONS)
    return packs


def prose_words(html):
    m = re.search(r'<div class="prose">([\s\S]*?)</div>\s*<nav class="lesson-nav"', html)
    if not m:
        return 0
    text = re.sub(r'<[^>]+>', ' ', m.group(1))
    return len(text.split())


def main():
    packs = load_packs()
    posts_path = os.path.join(BLOG, 'posts.json')
    data = json.load(open(posts_path, encoding='utf-8'))
    lessons = [p for p in data['posts']
               if p.get('category') == 'آموزش زبان چینی' and p['slug'] != 'chinese-course']
    assert len(lessons) == 50

    minutes_by_slug = {}

    # ── 1+2+3 per lesson ──────────────────────────────────────────────
    for post in lessons:
        slug = post['slug']
        pack = packs.get(slug)
        if pack is None:
            print(f'!! no pack for {slug}')
            continue
        path = os.path.join(BLOG, 'articles', slug + '.html')
        html = open(path, encoding='utf-8').read()

        signature = re.search(r'<h2>([^<]+)</h2>', pack).group(1)
        if signature in html:
            print(f'-- {slug}: already expanded, syncing minutes only')
        else:
            anchor = '\n</div>\n<nav class="lesson-nav"'
            assert anchor in html, f'{slug}: prose anchor missing'
            html = html.replace(anchor, '\n' + pack + anchor, 1)
            open(path, 'w', encoding='utf-8').write(html)

        # recount + minutes
        html = open(path, encoding='utf-8').read()
        words = prose_words(html)
        new_minutes = max(post['minutes'], round(words / 95) or 1)
        minutes_by_slug[slug] = new_minutes

        # JSON-LD wordCount
        html = re.sub(r'"wordCount": \d+', f'"wordCount": {words}', html)
        # own visible minutes
        old_min = post['minutes']
        html = re.sub(r'<span>⏱ [۰-۹0-9]+ دقیقه مطالعه</span>',
                      f'<span>⏱ {fa_num(new_minutes)} دقیقه مطالعه</span>', html)
        open(path, 'w', encoding='utf-8').write(html)
        post['minutes'] = new_minutes

    # persist posts.json
    with open(posts_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')

    # ── 4. cross-article minute sync (related grids + hub) ────────────
    def sync_file(path):
        src = open(path, encoding='utf-8').read()
        changed = False
        for slug, mins in minutes_by_slug.items():
            # every anchor link to this slug followed by a ⏱ N دقیقه badge
            pat = re.compile(
                r'(href="[^"]*/(?:blog/)?articles/' + re.escape(slug) + r'\.html"[\s\S]{0,600}?⏱ )[۰-۹0-9]+( دقیقه)')
            new_src = pat.sub(lambda m: m.group(1) + fa_num(mins) + m.group(2), src)
            if new_src != src:
                changed = True
                src = new_src
        if changed:
            open(path, 'w', encoding='utf-8').write(src)
        return changed

    for fname in sorted(os.listdir(os.path.join(BLOG, 'articles'))):
        if fname.endswith('.html'):
            sync_file(os.path.join(BLOG, 'articles', fname))
    sync_file(os.path.join(BLOG, 'chinese-course.html'))

    total_words = 0
    for post in lessons:
        path = os.path.join(BLOG, 'articles', post['slug'] + '.html')
        total_words += prose_words(open(path, encoding='utf-8').read())
    print(f'expanded 50 lessons; course prose now {total_words} words')
    print('sample minutes:', {s: minutes_by_slug[s] for s in list(minutes_by_slug)[:4]})


if __name__ == '__main__':
    sys.exit(main())

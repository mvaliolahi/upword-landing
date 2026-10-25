#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the 90-day GERMAN course: articles + hub + registries.

The lessons are authored COMPLETE in de_course_data_01..10.py (each lesson
carries its full final section order: core teaching → dialogue → deep
grammar → ❌/✅ mistakes → drills+answers → daily challenge → conversation
tips). This script renders every article, the hub page, and registers
everything in posts.json / sitemap.xml / feed.xml. Idempotent.

Usage:  python3 scripts/de_course_build.py
"""
import importlib.util
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import de_course_lib as lib

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
DATA_FILES = [f'de_course_data_{i:02d}' for i in range(1, 11)]


def load_all():
    lessons = []
    for name in DATA_FILES:
        path = os.path.join(SCRIPTS, name + '.py')
        if not os.path.exists(path):
            continue
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        lessons.extend(mod.LESSONS)
    return lessons


def main():
    lessons = load_all()
    assert len(lessons) == lib.TOTAL, f'expected {lib.TOTAL} lessons, got {len(lessons)}'
    slugs = [l['slug'] for l in lessons]
    assert len(set(slugs)) == len(slugs), 'duplicate slugs!'
    assert all(s.startswith('german-') for s in slugs), 'every slug must start with german-'

    # 1) render every article + collect minutes (+ the related tail grid)
    minutes_map = {}
    descs = {}
    for n, les in enumerate(lessons, start=1):
        prev = lessons[n - 2] if n >= 2 else None
        nxt = lessons[n] if n < lib.TOTAL else None
        html = lib.render_article(les, n, prev, nxt)
        path = os.path.join(lib.BLOG, 'articles', les['slug'] + '.html')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        prose = lib.render_prose(les)
        minutes_map[les['slug']] = lib.minutes_of(lib.word_count(prose))
        descs[les['slug']] = les['desc']
        # two related links: the next lesson + the one after (last lessons
        # point back to the phase's closing lessons)
        if nxt:
            rel = [nxt['slug'], lessons[n]['slug'] if n < lib.TOTAL - 1 else lessons[lib.TOTAL - 3]['slug']]
        else:
            rel = [lessons[lib.TOTAL - 2]['slug'], lessons[lib.TOTAL - 3]['slug']]
        les['_rel'] = rel
    # second pass: stamp the related grid's minutes now that the map is full
    for n, les in enumerate(lessons, start=1):
        path = os.path.join(lib.BLOG, 'articles', les['slug'] + '.html')
        html = open(path, encoding='utf-8').read()
        for slug in les.get('_rel', []):
            other = next(l for l in lessons if l['slug'] == slug)
            html = html.replace(
                f'<a href="/blog/articles/{slug}.html">\n<span class="rel-cat">{lib.CATEGORY}</span>\n'
                f'<span class="rel-title">{other["title"]}</span>\n'
                f'<span class="rel-meta">⏱ ۰ دقیقه مطالعه</span>\n</a>',
                f'<a href="/blog/articles/{slug}.html">\n<span class="rel-cat">{lib.CATEGORY}</span>\n'
                f'<span class="rel-title">{other["title"]}</span>\n'
                f'<span class="rel-meta">⏱ {lib.fa_num(minutes_map[slug])} دقیقه مطالعه</span>\n</a>')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)

    # 2) the hub page
    hub = lib.render_hub(lessons, minutes_map)
    with open(os.path.join(lib.BLOG, 'german-course.html'), 'w', encoding='utf-8') as f:
        f.write(hub)
    lib.write_hub_content_json(lessons, minutes_map, descs)

    # 3) posts.json + sitemap + feed
    lib.register_everything(lessons, minutes_map, descs)

    print(f'built {lib.TOTAL} articles + hub; minutes total = {sum(minutes_map.values())}')
    print('sample minutes:', {k: minutes_map[k] for k in list(minutes_map)[:5]})


if __name__ == '__main__':
    main()

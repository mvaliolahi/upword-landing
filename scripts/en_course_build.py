#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the 90-lesson English course: articles + hub + registries.

Stage-1 build: renders every lesson article from the data files, the hub
page, and registers everything in posts.json / sitemap.xml / feed.xml.
Idempotent: re-running rebuilds the generated set from the data files.

Usage:  python3 scripts/en_course_build.py [--stage1-only]
"""
import importlib.util
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import en_course_lib as lib

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
DATA_FILES = [f'en_course_data_{i:02d}' for i in range(1, 11)]
# Stages 2+3: expansions (dialogues + grammar + conversation tips), keyed by slug
EXPANSION_FILES = [
    'en_expand_data_1',   # lessons 1-18: dialogues
    'en_expand_data_1b',  # lessons 1-18: grammar + tips
    'en_expand_data_2',   # lessons 19-36
    'en_expand_data_3',   # lessons 37-54
    'en_expand_data_4',   # lessons 55-72
    'en_expand_data_5',   # lessons 73-90
]


def load_all():
    lessons = []
    for name in DATA_FILES:
        spec = importlib.util.spec_from_file_location(name, os.path.join(SCRIPTS, name + '.py'))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        lessons.extend(mod.LESSONS)
    # stages 2+3: merge expansions into the lesson dicts
    for name in EXPANSION_FILES:
        spec = importlib.util.spec_from_file_location(name, os.path.join(SCRIPTS, name + '.py'))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        if hasattr(mod, 'EXPANSIONS'):
            lib.apply_expansions(lessons, mod.EXPANSIONS)
    return lessons


def main():
    lessons = load_all()
    assert len(lessons) == lib.TOTAL, f'expected {lib.TOTAL} lessons, got {len(lessons)}'
    # uniqueness of slugs
    slugs = [l['slug'] for l in lessons]
    assert len(set(slugs)) == len(slugs), 'duplicate slugs!'

    # 1) render every article + collect minutes
    minutes_map = {}
    descs = {}
    for n, les in enumerate(lessons, start=1):
        prev = lessons[n - 2] if n >= 2 else None
        nxt = lessons[n] if n < lib.TOTAL else None
        html = lib.render_article(les, n, prev, nxt)
        # related links (next lesson + phase neighbor) for the tail grid
        path = os.path.join(lib.BLOG, 'articles', les['slug'] + '.html')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        # compute minutes from the prose we just rendered
        prose = lib.render_prose(les)
        minutes_map[les['slug']] = lib.minutes_of(lib.word_count(prose))
        descs[les['slug']] = les['desc']
        # two related links per article: the next lesson (or previous for #90)
        rel = []
        if nxt:
            rel.append({'slug': nxt['slug'], 'title': nxt['title'], 'minutes': 0})
            rel.append({'slug': lessons[min(n, lib.TOTAL - 2)]['slug'], 'title': lessons[min(n, lib.TOTAL - 2)]['title'], 'minutes': 0})
        else:
            rel.append({'slug': lessons[87]['slug'], 'title': lessons[87]['title'], 'minutes': 0})
            rel.append({'slug': lessons[86]['slug'], 'title': lessons[86]['title'], 'minutes': 0})
        # patch the related grid with real minutes
        html = open(path, encoding='utf-8').read()
        for r in rel:
            pass  # minutes patched below in a second pass
        # store rel info for the second pass
        les['_rel'] = rel
    # second pass: fill related-grid minutes now that minutes_map is complete
    for n, les in enumerate(lessons, start=1):
        path = os.path.join(lib.BLOG, 'articles', les['slug'] + '.html')
        html = open(path, encoding='utf-8').read()
        for r in les.get('_rel', []):
            html = re.sub(
                r'(<a href="/blog/articles/' + re.escape(r['slug']) + r'\.html">\n<span class="rel-cat">[^<]*</span>\n<span class="rel-title">[^<]*</span>\n<span class="rel-meta">⏱ )[^<]*( دقیقه مطالعه</span>)',
                r'\g<1>' + lib.fa_num(minutes_map[r['slug']]) + r'\g<2>', html)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)

    # 2) the hub page
    hub = lib.render_hub(lessons, minutes_map)
    with open(os.path.join(lib.BLOG, 'english-course.html'), 'w', encoding='utf-8') as f:
        f.write(hub)
    lib.write_hub_content_json(lessons, minutes_map, descs)

    # 3) posts.json + sitemap + feed
    lib.register_everything(lessons, minutes_map, descs)

    print(f'built {lib.TOTAL} articles + hub; minutes total = {sum(minutes_map.values())}')
    print('sample minutes:', {k: minutes_map[k] for k in list(minutes_map)[:5]})


if __name__ == '__main__':
    main()

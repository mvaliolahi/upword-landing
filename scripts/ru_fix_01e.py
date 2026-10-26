#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v117 — pass 5: the last 4 mixed-token fixes, both sides in \\u escapes."""
import io

P = '/home/z/my-project/repos/upword-landing/scripts/ru_course_data_01.py'
src = io.open(P, encoding='utf-8').read()

FIXES = [
    # L704 преподаватель translit
    ('\\u067e\\u0652\\u0440\\u0650\\u067e\\u064e\\u0434\\u0430\\u200c\\u0648\\u064e\\u062a\\u06cc\\u043b',
     '\\u067e\\u0652\\u0631\\u0650\\u067e\\u064e\\u062f\\u0627\\u0648\\u064e\\u062a\\u06cc\\u0644'),
    # L705 юрист translit
    ('\\u200c\\u0439\\u0648\\u200c\\u0440\\u0438\\u0441\\u0442',
     '\\u06cc\\u0648\\u0631\\u0650\\u0633\\u062a'),
    # L706 бизнесмен translit (Cyrillic н)
    ('\\u0628\\u06cc\\u200c\\u0632\\u043d\\u0650\\u0633\\u0645\\u0650\\u0646',
     '\\u0628\\u06cc\\u200c\\u0632\\u0646\\u0650\\u0633\\u0645\\u0650\\u0646'),
    # L929 двадцать translit (Cyrillic в)
    ('\\u062f\\u200c\\u0432\\u064e\\u062a\\u200c\\u0633\\u064e\\u062a',
     '\\u062f\\u200c\\u0648\\u064e\\u062a\\u200c\\u0633\\u064e\\u062a'),
]

for old, new in FIXES:
    ro = old.encode().decode('unicode_escape')
    rn = new.encode().decode('unicode_escape')
    cnt = src.count(ro)
    if cnt == 0:
        print('MISS:', old[:50])
    else:
        src = src.replace(ro, rn)
        print(f'fixed x{cnt}')

io.open(P, 'w', encoding='utf-8').write(src)
print('done')

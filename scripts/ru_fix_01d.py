#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v117 — pass 4: final 8 mixed-script fixes for ru_course_data_01.py."""
import io

P = '/home/z/my-project/repos/upword-landing/scripts/ru_course_data_01.py'
src = io.open(P, encoding='utf-8').read()

FIXES = [
    # L704 преподаватель translit cell (Cyrillic р and в)
    ('\\u067e\\u0652\\u0440\\u0650\\u067e\\u064e\\u062f\\u0627\\u200c\\u0432\\u064e\\u062a\\u064c\\u0644',
     'پْرِپَداوَتیل'),
    # L705 юрист translit cell
    ("'\\u200c\\u0439\\u043e\\u200c\\u0440\\u0438\\u0441\\u0442'", "'یورِست'"),
    # L706 бизнесмен translit cell (Cyrillic з)
    ('\\u0628\\u06cc\\u200c\\u0437\\u0646\\u0650\\u0633\\u0645\\u0650\\u0646', 'بی‌زنِسمِن'),
    # L707 переводчик translit cell (Cyrillic в)
    ('\\u067e\\u0650\\u0631\\u06cc\\u200c\\u0432\\u064f\\u062f\\u200c\\u0686\\u0650\\u06a9', 'پِری‌وُد‌چِک'),
    # L739 деканат (Cyrillic декан + Persian ات)
    ('\\u0434\\u0435\\u043a\\u0430\\u043d\\u0627\\u062a', 'деканат'),
    # L818 «вы» translit (Cyrillic в)
    ('\\u0432\\u0650\\u06cc', 'وِی'),
    # L913 восемь translit (Cyrillic в)
    ('\\u0432\\u064f\\u0633\\u0650\\u0645', 'وُسِم'),
    # L929 двадцать translit (Cyrillic в)
    ('\\u062f\\u200c\\u0432\\u064e\\u062a\\u200c\\u0641\\u064e\\u062a', 'د‌وَت‌سَت'),
]

for old, new in FIXES:
    real_old = old.encode().decode('unicode_escape')
    cnt = src.count(real_old)
    if cnt == 0:
        print('MISS:', repr(old[:46]))
    else:
        src = src.replace(real_old, new)
        print(f'fixed x{cnt}')

io.open(P, 'w', encoding='utf-8').write(src)
print('done')

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v117 — byte-precise mixed-script fixes for ru_course_data_01.py (pass 2).
Old strings are written with \\u escapes so the dirty look-alike characters
are addressed exactly; new strings are typed clean in one script each."""
import io

P = '/home/z/my-project/repos/upword-landing/scripts/ru_course_data_01.py'
src = io.open(P, encoding='utf-8').read()

FIXES = [
    # L46 translit «Я студент.» — Persian س + Cyrillic ту inside
    ('\\u0633\\u0442\\u0443\\u200c\\u062f\\u0650\\u0646\\u062a', 'استودِنت'),
    # L112 «ТРки» Persian ک ی
    ('\\u0422\\u0420\\u06a9\\u06cc', 'ТРКИ'),
    # L236 «Тегеран» dirty (Persian ان ending)
    ('\\u0422\\u0435\\u0433\\u0435\\u0440\\u0627\\u0646', 'Тегеран'),
    # L307 syllable «по-پу» Persian پ
    ('\\u067e\\u0443', 'пу'),
    # L314 «зima» Latin ima
    ('\\u0437\\u0069\\u006d\\u0061', 'зима'),
    # L315 «Исфахан» dirty (Persian ان ending)
    ('\\u0418\\u0441\\u0444\\u0430\\u0445\\u0627\\u0646', 'Исфахан'),
    # L373 «гُرُت» Cyrillic г т
    ('\\u0433\\u064f\\u0631\\u064f\\u0442', 'گُرُت'),
    # L374 «гَتُف» Cyrillic г
    ('\\u0433\\u064e\\u062a\\u064f\\u0641', 'گَتُف'),
    # L385 «дِши‌وْله» Cyrillic д
    ('\\u0434\\u0650\\u0634', 'دِش'),
    # L446 «за́мок» Persian м
    ('\\u0437\\u0430\\u0301\\u0645\\u043e\\u043a', 'за́мок'),
    # L480 table header «بی‌ь»
    ("'\\u0628\\u06cc\\u200c\\u044c'", "'بدون ь'"),
]

n = 0
for old, new in FIXES:
    real_old = old.encode().decode('unicode_escape')
    cnt = src.count(real_old)
    if cnt == 0:
        print('MISS:', repr(old[:40]))
    else:
        src = src.replace(real_old, new)
        n += cnt
        print(f'fixed x{cnt}:', repr(old[:40]))

io.open(P, 'w', encoding='utf-8').write(src)
print('total replacements:', n)

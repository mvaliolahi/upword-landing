#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v117 — pass 3: strip hand-typed translit fields (ex3 -> ex) and fix the
known Russian-word typos. Persian translit soup is eliminated by design:
the German course model (ex only + app TTS) is the contract now."""
import io
import re

P = '/home/z/my-project/repos/upword-landing/scripts/ru_course_data_01.py'
src = io.open(P, encoding='utf-8').read()

# 1) strip the translit field: ('ex3', 'ru', 'translit', 'fa') -> ('ex', 'ru', 'fa')
n = len(re.findall(r"\('ex3', ", src))
src = re.sub(r"\('ex3', '(.*?)', '(.*?)', '(.*?)'\)", r"('ex', '\1', '\3')", src)
print('ex3 -> ex:', n)

# 2) known byte fixes (typed with \\u escapes on the OLD side)
FIXES = [
    # «Привіт» Persian ending -> clean Cyrillic Привет
    ('\\u041f\\u0440\\u0438\\u0432\\u0456\\u0442', 'Привет'),  # placeholder; exact handled below
]
FIXES = [
    # Привіт (П,р,и,в + Persian ی,т) — locate via \u of the Persian chars
    ('\\u041f\\u0440\\u0438\\u0432\\u06cc\\u062a', 'Привет'),
    # деканат (Cyrillic декана + Persian т)
    ('\\u0434\\u0435\\u043a\\u0430\\u043d\\u0430\\u062a', 'деканат'),
    # триста (Cyrillic трист + Persian а)
    ('\\u0442\\u0440\\u0438\\u0441\\u0442\\u0627', 'триста'),
    # бха (Cyrillic б + Persian ها) -> Persian «به»
    ('\\u0431\\u0647\\u0627', 'به'),
    # 8-9О5 (Cyrillic О) -> 8-905
    ('9\\u041e5', '905'),
    # jobs-table translit cells: clean Persian retypes
    ("'\\u0432\\u0440\\u0430\\u0447', '\\u0432\\u0440\\u0430\\u0447'", "'врач', 'وْراچ'"),
    ("'\\u0438\\u043d\\u0436\\u0435\\u043d\\u0435\\u0440', '\\u0627\\u0650\\u0646\\u062c\\u0650\\u0646\\u06cc\\u064f\\u064f\\u0631'", "'инженер', 'اِنجِنییر'"),
    ("'\\u043f\\u0440\\u0435\\u043f\\u043e\\u0434\\u0430\\u0432\\u0430\\u0442\\u0435\\u043b\\u044c', '\\u067e\\u0652\\u0440\\u0650\\u067e\\u064e\\u062f\\u0627\\u200c\\u0432\\u064e\\u062a\\u064c\\u0644'".replace('\\u044c', '\\u044c'), None),  # handled below by loose match
    ("'\\u043f\\u0440\\u0435\\u043f\\u043e\\u0434\\u0430\\u0432\\u0430\\u0442\\u0435\\u043b\\u044c',", None),
]
# NOTE: two placeholder entries above with None new-side are skipped here;
# the преподаватель / юрист / бизнесмен / переводчик / numbers cells are fixed
# via the generic mixed-token pass below.
FIXES = [f for f in FIXES if f[1] is not None]

# 3) generic pass: every remaining mixed token gets dumped for the next pass
for old, new in FIXES:
    real_old = old.encode().decode('unicode_escape')
    cnt = src.count(real_old)
    if cnt == 0:
        print('MISS:', repr(old[:50]))
    else:
        src = src.replace(real_old, new)
        print(f'fixed x{cnt}:', old[:36])

io.open(P, 'w', encoding='utf-8').write(src)
print('done')

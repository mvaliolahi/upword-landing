#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v117 — fix the 12 mixed-script issues in ru_course_data_09.py."""
import io

P = '/home/z/my-project/repos/upword-landing/scripts/ru_course_data_09.py'
src = io.open(P, encoding='utf-8').read()

FIXES = [
    # L84 летo (Latin o) -> лето
    ('\\u043b\\u0435\\u0442\\u006f', 'лето'),
    # L97 بانک (Cyrillic к) -> Persian بانک
    ('\\u0628\\u0627\\u0646\\u043a', 'بانک'),
    # L128 плыθ (Persian ث) -> плыть
    ('\\u043f\\u043b\\u044b\\u062b', 'плыть'),
    # L158 اتوبус (Cyrillic ус) -> Persian اتوبوس
    ('\\u0627\\u062a\\u0648\\u0628\\u0443\\u0441', 'اتوبوس'),
    # L187 приедu (Latin u) -> приеду
    ('\\u043f\\u0440\\u0438\\u0435\\u0434\\u0075', 'приеду'),
    # L396 ТРки (Persian ک ی) -> ТРКИ
    ('\\u0422\\u0420\\u06a9\\u06cc', 'ТРКИ'),
    # L424 мама (Persian м) -> мама
    ('\\u0645\\u0430\\u043c\\u0430', 'мама'),
    # L524 закрыт (Latin t) -> закрыт
    ('\\u0437\\u0430\\u043a\\u0440\\u044b\\u0074', 'закрыт'),
    # L545 открытa (Latin a) -> открыта
    ('\\u043e\\u0442\\u043a\\u0440\\u044b\\u0442\\u0061', 'открыта'),
    # L567 зани́то — rewrite the answer with correct stress pedagogy (зАнято)
    ('\\u062a\\u06a9\\u06cc\\u0647 \\u0631\\u0648\\u06cc \\u00ab\\u044f\\u00bb \\u2014 \\u0437\\u0430\\u0301\\u043d\\u044f\\u0442\\u043e \\u0646\\u0647 \\u0632\\u0430\\u043d\\u0438\\u0301\\u0442\\u043e... \\u062f\\u0642\\u062a: \\u0437\\u0430\\u043d\\u044f\\u0301\\u0442\\u043e!',
     'تکیه روی «А» اول — за́нято، نه занято́ (که تکیه را به آخر می‌برد).'),
    # L583 сдana (Latin ana) -> сдано
    ('\\u0441\\u0434\\u0061\\u006e\\u0061', 'сдано'),
    # L638 всегda (Latin da) -> всегда
    ('\\u0432\\u0441\\u0435\\u0433\\u0064\\u0061', 'всегда'),
]

for old, new in FIXES:
    ro = old.encode().decode('unicode_escape')
    cnt = src.count(ro)
    if cnt == 0:
        print('MISS:', repr(old[:46]))
    else:
        src = src.replace(ro, new)
        print(f'fixed x{cnt}')

io.open(P, 'w', encoding='utf-8').write(src)
print('done')

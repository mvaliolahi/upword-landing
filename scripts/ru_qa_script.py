#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v117 — mixed-script QA for the Russian course data files.

Catches invisible look-alike bugs inside authored text:
  1. Cyrillic + Latin letters in the SAME token  (утro, MФЦ…)
  2. Cyrillic + Persian letters in the SAME token (Cyrillic б inside بعداً…)
  3. Persian + Latin letters in the SAME token
Digits, ZWNJ, tatweel and harakat are class-neutral.
Usage:  python3 scripts/ru_qa_script.py [file1 file2 ...]
"""
import glob
import io
import re
import sys

PERSIAN = re.compile(r'[\u0621-\u064A\u067E\u0686\u06A9\u06AF\u06CC\u06C1\u06D2]')
CYR = re.compile(r'[\u0400-\u04FF]')
LATIN = re.compile(r'[A-Za-z]')
# token = letters of any script glued together (incl. digits/ZWNJ/tatweel/harakat)
TOK = re.compile(r'[\u0400-\u04FF\u0621-\u064A\u067E\u0686\u06A9\u06AF\u06CC\u06C1\u06D2A-Za-z0-9\u200C\u064B-\u0652\u0640]+')

ALLOWED_MIXED = {
    # deliberately mixed tokens (brand names, bilingual acronyms)
    'ТРКИ/TORFL', 'TORFL/ТРКИ',
}


def scan_text(text, path, base_line=1):
    issues = []
    for m in TOK.finditer(text):
        t = m.group(0)
        if t in ALLOWED_MIXED or (len(t) <= 2 and not t.isalpha()):
            continue
        has_p = bool(PERSIAN.search(t))
        has_c = bool(CYR.search(t))
        has_l = bool(LATIN.search(t))
        if (has_p and has_c) or (has_c and has_l) or (has_p and has_l):
            line = text.count('\n', 0, m.start()) + base_line
            issues.append((line, t, ''.join(
                'P' if PERSIAN.search(ch) else ('C' if CYR.search(ch) else ('L' if LATIN.search(ch) else '.'))
                for ch in t)))
    return issues


def scan_file(path):
    src = io.open(path, encoding='utf-8').read()
    issues = scan_text(src, path)
    if issues:
        print(f'── {path}')
        seen = set()
        for line, tok, cls in issues:
            key = (tok, cls)
            if key in seen:
                continue
            seen.add(key)
            print(f'  L{line}: {tok!r}  [{cls}]')
    return len(issues)


def main():
    targets = sys.argv[1:]
    if not targets:
        targets = sorted(glob.glob('/home/z/my-project/repos/upword-landing/scripts/ru_course_data_*.py'))
    total = 0
    for t in targets:
        total += scan_file(t)
    print(f'{total} mixed-script issues')
    sys.exit(1 if total else 0)


if __name__ == '__main__':
    main()

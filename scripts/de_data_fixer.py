#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Auto-fix stray-paren errors in the de_course_data_* files.

Error class: the LAST item of a ('ul'|'ol', [ ... ]) block was written with a
trailing `')` instead of `',` — producing a premature tuple close. The fixer
compiles iteratively; on each SyntaxError pointing at such a line, it patches
and retries until the file compiles clean.
"""
import sys, re

def try_compile(path):
    try:
        with open(path, encoding='utf-8') as f:
            src = f.read()
        compile(src, path, 'exec')
        return None, src
    except SyntaxError as e:
        return e, None

def fix(path):
    for _ in range(200):
        err, _ = try_compile(path)
        if err is None:
            print(f'{path}: compiles clean')
            return True
        src = open(path, encoding='utf-8').read()
        lines = src.split('\n')
        ln = err.lineno - 1
        line = lines[ln] if ln < len(lines) else ''
        stripped = line.strip()
        # case 1: list item ends with '), or ') — the ')' is stray
        if (stripped.endswith("'),") or stripped.endswith("')")) and err.msg.startswith("closing parenthesis ')' does not match opening parenthesis '['"):
            indent = line[:len(line) - len(line.lstrip())]
            body = stripped
            if body.endswith("'),"):
                body = body[:-3] + "',"
            else:
                body = body[:-2] + "'"
            lines[ln] = indent + body
            open(path, 'w', encoding='utf-8').write('\n'.join(lines))
            print(f'  fixed line {ln+1}: ul/ol item stray paren')
            continue
        # case 2: paragraph tuple missing close paren (ends with ' not ')
        if stripped.endswith("'") and "does not match" in err.msg and "']'" in err.msg or (
                stripped.endswith("'") and err.msg.startswith("closing parenthesis ']' does not match opening parenthesis '('")):
            lines[ln] = stripped + ")"
            open(path, 'w', encoding='utf-8').write('\n'.join(lines))
            print(f'  fixed line {ln+1}: tuple missing close paren')
            continue
        # case 3: table last row `]],` missing one paren -> `]]),`
        if stripped.endswith(']],') and "does not match" in err.msg:
            lines[ln] = stripped[:-1] + '),'
            open(path, 'w', encoding='utf-8').write('\n'.join(lines))
            print(f'  fixed line {ln+1}: table rows missing paren')
            continue
        # case 4: a bracket line that doesn't match an open '(' — the line
        # above usually holds the unclosed tuple.
        if ("does not match opening parenthesis '('" in err.msg and
                stripped in (']', '])', '],')):
            if ln > 0 and lines[ln - 1].strip().endswith("'") and not lines[ln - 1].strip().endswith("'),"):
                lines[ln - 1] = lines[ln - 1].rstrip() + '),'
                open(path, 'w', encoding='utf-8').write('\n'.join(lines))
                print(f'  fixed line {ln}: closed tuple on line above')
                continue
            if stripped == ']':
                lines[ln] = ']),'
                open(path, 'w', encoding='utf-8').write('\n'.join(lines))
                print(f'  fixed line {ln+1}: bare ] -> ]),')
                continue
        print(f'  UNFIXABLE at line {ln+1}: {err.msg}')
        print(f'  line: {line[:160]}')
        return False
    return False

if __name__ == '__main__':
    ok = True
    for p in sys.argv[1:]:
        ok = fix(p) and ok
    sys.exit(0 if ok else 1)

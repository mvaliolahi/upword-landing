#!/usr/bin/env python3
"""v126 — extract each article's HTML into structured content JSON for the
app's NATIVE reader (the owner's «چرا محتوا هم native نیست؟» round).

Source of truth stays the HTML (SEO, web readers); this script derives
blog/content/<slug>.json from it. Run after every article edit, then commit.

Block schema (the app renders unknown types as plain paragraphs — new block
types in future articles degrade gracefully WITHOUT an app release):
  {"type":"h2"|"h3"|"p","spans":[span,...]}
  {"type":"callout","label":"⚡ پاسخ کوتاه","spans":[...]}
  {"type":"ul"|"ol","items":[[span,...],...]}
  {"type":"table","header":[".."],"rows":[[".."],..]}
  {"type":"faq","qa":[{"q":"..","a":[span,...]}]}
Inline span: {"t":"text","b":bool,"c":bool,"href":"url"}
"""
import json, os, re
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOG = os.path.join(ROOT, 'blog')


class SpanCollector:
    """Accumulates text with inline bold/code/link flags."""

    def __init__(self):
        self.spans = []
        self.buf = ''
        self.b = False
        self.c = False
        self.href = ''

    def text(self, t):
        self.buf += t

    def toggle(self, tag, attrs):
        self._flush()
        if tag in ('strong', 'b'):
            self.b = not self.b
        elif tag == 'code':
            self.c = not self.c
        elif tag == 'a':
            self.href = '' if self.href else attrs.get('href', '')

    def _flush(self):
        if self.buf:
            s = {'t': self.buf}
            if self.b:
                s['b'] = True
            if self.c:
                s['c'] = True
            if self.href:
                s['href'] = self.href
            self.spans.append(s)
            self.buf = ''

    def result(self):
        self._flush()
        return self.spans


def spans_to(spans):
    """Normalize: strip empty, merge identical-format neighbours."""
    res = []
    for s in spans:
        t = s.get('t', '')
        if not t or not t.strip():
            continue
        e = {'t': t}
        if s.get('b'):
            e['b'] = True
        if s.get('c'):
            e['c'] = True
        if s.get('href'):
            e['href'] = s['href']
        if res:
            p = res[-1]
            if (p.get('b') == e.get('b') and p.get('c') == e.get('c')
                    and p.get('href') == e.get('href') and 'href' not in e):
                p['t'] += e['t']
                continue
            if 'href' in e or 'href' in p:
                res.append(e)
                continue
            if p.get('b') == e.get('b') and p.get('c') == e.get('c'):
                p['t'] += e['t']
                continue
        res.append(e)
    if res:
        res[0]['t'] = res[0]['t'].lstrip()
        res[-1]['t'] = res[-1]['t'].rstrip()
        # drop spans that became empty
        res = [s for s in res if s['t']] or []
        for i, s in enumerate(res[:-1]):
            if not s['t'].endswith(' ') and s['t'] and res[i + 1]['t']:
                pass  # keep original spacing fidelity
    return res


class ArticleParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.mode = None            # None|head|callout|prose|faq
        self.meta_title = ''
        self.blocks = []
        self.callout = {}
        self.faq_items = []
        self.cur = None
        self.in_table = False
        self.table = None
        self.row = None
        self.cell = None
        self.faq_q = None
        self.faq_a = None
        self.col = None             # head/label collector
        self.head_part = None       # chip|h1|meta

    # ── helpers ────────────────────────────────────────────────────────
    def _active_col(self):
        if self.cur is None:
            return None
        if self.cur['type'] in ('ul', 'ol'):
            return self.cur.get('li_col')
        return self.cur.get('col')

    # ── tags ───────────────────────────────────────────────────────────
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = a.get('class', '')

        if tag == 'div' and 'article-head' in cls:
            self.mode = 'head'
            return
        if tag == 'div' and 'short-answer' in cls:
            self.mode = 'callout'
            self.callout = {}
            return
        if tag == 'div' and 'prose' in cls:
            self.mode = 'prose'
            return
        if tag == 'section' and 'article-faq' in cls:
            self.mode = 'faq'
            return
        if tag in ('section', 'footer') and self.mode == 'faq':
            self._close_faq_section()
            return
        if tag in ('section', 'footer'):
            self.mode = None
            return

        if self.mode == 'head':
            if 'post-chip' in cls:
                self.col = SpanCollector()
                self.head_part = 'chip'
            elif tag == 'h1':
                self.col = SpanCollector()
                self.head_part = 'h1'
            return

        if self.mode == 'callout':
            if 'sa-label' in cls:
                self.col = SpanCollector()
                self.head_part = 'sa-label'
            elif tag == 'p':
                self.col = SpanCollector()
                self.head_part = 'sa-body'
            return

        if self.mode == 'prose':
            if self.in_table:
                if tag == 'tr':
                    self.row = []
                elif tag in ('th', 'td'):
                    self.cell = SpanCollector()
                return
            if tag == 'table':
                self.in_table = True
                self.table = {'header': [], 'rows': []}
                return
            if tag in ('h2', 'h3'):
                self.cur = {'type': tag, 'col': SpanCollector()}
            elif tag == 'p':
                self.cur = {'type': 'p', 'col': SpanCollector()}
            elif tag in ('ul', 'ol'):
                self.cur = {'type': tag, 'items': [], 'li_col': None}
            elif tag == 'li' and self.cur and self.cur['type'] in ('ul', 'ol'):
                self.cur['li_col'] = SpanCollector()
            elif tag in ('strong', 'b', 'code', 'a'):
                c = self._active_col()
                if c:
                    c.toggle(tag, a)
            return

        if self.mode == 'faq':
            if tag == 'details':
                self.faq_q = SpanCollector()
                self.faq_a = None
            elif tag == 'summary' and self.faq_q is not None:
                pass
            elif tag == 'div' and 'faq-answer' in cls:
                self.faq_a = SpanCollector()
            elif tag in ('strong', 'b', 'code', 'a'):
                c = self.faq_a if self.faq_a is not None else self.faq_q
                if c:
                    c.toggle(tag, a)
            return

    def handle_endtag(self, tag):
        if self.mode == 'head':
            if tag == 'span' and self.head_part == 'chip':
                self.chip = ''.join(s['t'] for s in self.col.result()).strip()
                self.col = None
                self.head_part = None
            elif tag == 'h1' and self.head_part == 'h1':
                self.meta_title = ''.join(s['t'] for s in self.col.result()).strip()
                self.col = None
                self.head_part = None
            elif tag == 'div' and self.head_part is None:
                self.mode = None
            return

        if self.mode == 'callout':
            if tag == 'span' and self.head_part == 'sa-label':
                self.callout['label'] = ''.join(s['t'] for s in self.col.result()).strip()
                self.col = None
                self.head_part = None
            elif tag == 'p' and self.head_part == 'sa-body':
                self.callout['spans'] = spans_to(self.col.result())
                self.col = None
                self.head_part = None
            elif tag == 'div' and self.head_part is None:
                self.mode = None
            return

        if self.mode == 'prose':
            if self.in_table:
                if tag in ('th', 'td') and self.cell is not None:
                    txt = re.sub(r'\s+', ' ', ''.join(s['t'] for s in self.cell.result())).strip()
                    if self.row is not None:
                        self.row.append(txt)
                    self.cell = None
                elif tag == 'tr' and self.row is not None:
                    if self.table is not None:
                        if not self.table['header']:
                            self.table['header'] = self.row
                        else:
                            self.table['rows'].append(self.row)
                    self.row = None
                elif tag == 'table':
                    self.in_table = False
                    if self.table and self.table['header']:
                        self.blocks.append({'type': 'table',
                                            'header': self.table['header'],
                                            'rows': self.table['rows']})
                    self.table = None
                return
            if tag in ('h2', 'h3', 'p') and self.cur and self.cur['type'] == tag:
                self.blocks.append({'type': tag, 'spans': spans_to(self.cur['col'].result())})
                self.cur = None
            elif tag in ('ul', 'ol') and self.cur and self.cur['type'] == tag:
                items = [spans_to(c.result()) for c in self.cur['items']]
                self.blocks.append({'type': tag, 'items': items})
                self.cur = None
            elif tag == 'li' and self.cur and self.cur['type'] in ('ul', 'ol'):
                if self.cur['li_col'] is not None:
                    self.cur['items'].append(self.cur['li_col'])
                    self.cur['li_col'] = None
            elif tag in ('strong', 'b', 'code', 'a'):
                c = self._active_col()
                if c:
                    c.toggle(tag, {})
            return

        if self.mode == 'faq':
            if tag == 'details' and self.faq_q is not None:
                q = re.sub(r'\s+', ' ', ''.join(s['t'] for s in self.faq_q.result())).strip()
                a = spans_to(self.faq_a.result()) if self.faq_a else []
                if q:
                    self.faq_items.append({'q': q, 'a': a})
                self.faq_q = None
                self.faq_a = None
            return

    def handle_data(self, data):
        if self.mode == 'head' and self.col is not None:
            self.col.text(data)
            return
        if self.mode == 'callout' and self.col is not None:
            self.col.text(data)
            return
        if self.mode == 'prose':
            if self.in_table:
                if self.cell is not None:
                    self.cell.text(data)
                return
            c = self._active_col()
            if c:
                c.text(data)
            return
        if self.mode == 'faq':
            if self.faq_a is not None:
                self.faq_a.text(data)
            elif self.faq_q is not None:
                self.faq_q.text(data)

    def _close_faq_section(self):
        if self.faq_items:
            self.blocks.append({'type': 'faq', 'qa': self.faq_items})
            self.faq_items = []
        self.mode = None

    def close(self):
        super().close()
        if self.faq_items:
            self.blocks.append({'type': 'faq', 'qa': self.faq_items})


def extract(slug, post):
    path = os.path.join(BLOG, 'articles', slug + '.html')
    html = open(path, encoding='utf-8').read()
    html = re.sub(r'<script[\s\S]*?</script>', '', html)
    p = ArticleParser()
    p.feed(html)
    p.close()
    meta = {k: post.get(k, '') for k in ('slug', 'title', 'desc', 'category', 'cover', 'date', 'dateFa')}
    meta['minutes'] = post.get('minutes', 5)
    blocks = []
    if p.callout.get('spans'):
        blocks.append({'type': 'callout', 'label': p.callout.get('label', ''),
                       'spans': p.callout['spans']})
    blocks += [b for b in p.blocks if b]
    return {'meta': meta, 'blocks': blocks}


def main():
    feed = json.load(open(os.path.join(BLOG, 'posts.json'), encoding='utf-8'))
    outdir = os.path.join(BLOG, 'content')
    os.makedirs(outdir, exist_ok=True)
    for post in feed['posts']:
        slug = post['slug']
        content = extract(slug, post)
        out = os.path.join(outdir, slug + '.json')
        with open(out, 'w', encoding='utf-8') as f:
            json.dump(content, f, ensure_ascii=False, separators=(',', ':'))
        types = {}
        for b in content['blocks']:
            types[b['type']] = types.get(b['type'], 0) + 1
        print(f"{slug}: {len(content['blocks'])} blocks {types} -> {os.path.getsize(out)}B")
        post['content'] = f"content/{slug}.json"
    with open(os.path.join(BLOG, 'posts.json'), 'w', encoding='utf-8') as f:
        json.dump(feed, f, ensure_ascii=False, indent=2)
        f.write('\n')
    print('posts.json: content pointers added')


if __name__ == '__main__':
    main()

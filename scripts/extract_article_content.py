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
        self.mode_before_faq = None # v-deepen — prose restoration after mid-body FAQ
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
        # v130 — .zh-ex example blocks → dedicated `zh` blocks (the app's
        # native example card + per-example TTS), and <blockquote> → `quote`.
        self.zhex = None            # {'zh','py','fa'} text parts while inside
        self.zhex_part = None       # current span class collector
        self.zhex_col = None        # SpanCollector for the current part
        self.quote_col = None       # blockquote inline collector

    # ── helpers ────────────────────────────────────────────────────────
    def _active_col(self):
        if self.zhex_col is not None:
            return self.zhex_col
        if self.quote_col is not None:
            return self.quote_col
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
            # v-deepen — drill-answer sections can appear MID-PROSE; remember
            # where we were so closing returns to prose, not to nothing.
            self.mode_before_faq = self.mode
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
            if tag == 'div' and 'zh-ex' in cls:
                self.zhex = {'zh': '', 'py': '', 'fa': ''}
                return
            if self.zhex is not None and tag == 'span':
                part = 'zh' if 'zh' in cls else ('py' if 'py' in cls else ('fa' if 'fa' in cls else None))
                if part:
                    self.zhex_part = part
                    self.zhex_col = SpanCollector()
                return
            if tag == 'blockquote':
                self.quote_col = SpanCollector()
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
            if self.zhex is not None:
                if tag == 'span' and self.zhex_col is not None:
                    self.zhex[self.zhex_part] = re.sub(
                        r'\s+', ' ', ''.join(s['t'] for s in self.zhex_col.result())).strip()
                    self.zhex_part = None
                    self.zhex_col = None
                elif tag == 'div':
                    z = self.zhex
                    self.zhex = None
                    if z and (z['zh'] or z['py'] or z['fa']):
                        # Flat spans keep OLD apps rendering the full text
                        # (unknown block type degrades to a paragraph) —
                        # the forward-compat contract of the native reader.
                        flat = ' · '.join(x for x in (z['zh'], z['py'], z['fa']) if x)
                        self.blocks.append({'type': 'zh', 'zh': z['zh'], 'py': z['py'],
                                            'fa': z['fa'], 'spans': [{'t': flat}]})
                return
            if tag == 'blockquote' and self.quote_col is not None:
                spans = spans_to(self.quote_col.result())
                self.quote_col = None
                if spans:
                    self.blocks.append({'type': 'quote', 'spans': spans})
                return
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
            elif tag in ('section', 'footer'):
                # v-deepen — close the FAQ section on its OWN closing tag
                # (previously this only happened when the NEXT section
                # opened, or at EOF — so a mid-prose drill-answers section
                # swallowed every block that followed it).
                self._close_faq_section()
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
        # v-deepen — a mid-prose drill-answers section hands the parser
        # BACK to prose; the trailing article (dialogue, grammar, tips…)
        # keeps flowing instead of being silently dropped.
        self.mode = 'prose' if self.mode_before_faq == 'prose' else None
        self.mode_before_faq = None

    def close(self):
        super().close()
        if self.faq_items:
            self.blocks.append({'type': 'faq', 'qa': self.faq_items})


def article_path(slug):
    """The hub page lives at blog/<slug>.html; every other post at
    blog/articles/<slug>.html."""
    in_articles = os.path.join(BLOG, 'articles', slug + '.html')
    if os.path.exists(in_articles):
        return in_articles
    return os.path.join(BLOG, slug + '.html')


def extract(slug, post):
    path = article_path(slug)
    html = open(path, encoding='utf-8').read()
    html = re.sub(r'<script[\s\S]*?</script>', '', html)
    if slug in ('chinese-course', 'english-course', 'german-course', 'russian-course'):
        return extract_hub(post)
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


def extract_hub(post):
    """The course hub is a lesson INDEX, not prose: the reader gets the
    hero paragraph + one summary line per phase; the 50 lesson links live
    on the web page (the reader's browser action)."""
    html = open(os.path.join(BLOG, post['slug'] + '.html'), encoding='utf-8').read()
    html = re.sub(r'<script[\s\S]*?</script>', '', html)
    meta = {k: post.get(k, '') for k in ('slug', 'title', 'desc', 'category', 'cover', 'date', 'dateFa')}
    meta['minutes'] = post.get('minutes', 5)
    blocks = []
    hero = re.search(r'class="[^"]*course-hero[^"]*"[\s\S]*?<p>([\s\S]*?)</p>', html)
    if hero:
        blocks.append({'type': 'p', 'spans': [{'t': re.sub(r'\s+', ' ', hero.group(1)).strip()}]})
    phases = re.findall(r'<h2>(فاز[^<]*)</h2><p class="phase-desc">([\s\S]*?)</p>', html)
    for title, desc in phases:
        text = re.sub(r'<[^>]+>', '', desc)
        text = re.sub(r'\s+', ' ', text).strip()
        blocks.append({'type': 'p', 'spans': [{'t': title + ' — ' + text}]})
    cta = re.search(r'<h2>(در گوشی[^<]*)</h2>\s*<p[^>]*>([\s\S]*?)</p>', html)
    if cta:
        blocks.append({'type': 'callout', 'label': cta.group(1),
                       'spans': [{'t': re.sub(r'\s+', ' ', cta.group(2)).strip()}]})
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

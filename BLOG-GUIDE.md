# 📝 راهنمای انتشار مقاله جدید (روزانه)

این راهنما برای انتشار روزانه مقاله در وبلاگ `upword.ir/blog` نوشته شده است. کل فرایند حدود ۱۰ تا ۱۵ دقیقه است و نیاز به ابزار خاصی ندارد — همه کارها از خود GitHub (وب‌سایت github.com) هم قابل انجام است.

---

## 🗂 ساختار وبلاگ

```
upword-landing/
├── blog/
│   ├── index.html              # صفحه اصلی وبلاگ (لیست مقالات)
│   ├── posts.json              # ⭐ فهرست مقالات — برای هر مقاله جدید یک ردیف اضافه می‌شود
│   └── articles/
│       ├── _template.html      # قالب آماده مقاله (کپی کن و پر کن)
│       ├── english-at-home.html
│       ├── ai-conversation-practice.html
│       └── shadowing-technique.html
├── sitemap.xml                 # نقشه سایت — آدرس مقاله جدید اضافه می‌شود
├── feed.xml                    # RSS — آیتم مقاله جدید اضافه می‌شود
└── robots.txt
```

---

## ✅ شش قدم انتشار

### قدم ۱ — ساخت فایل مقاله

1. فایل `blog/articles/_template.html` را باز کن، محتوایش را کپی کن.
2. در پوشه `blog/articles/` یک فایل جدید با نام **انگلیسی کوتاه و معنادار** بساز؛ مثلاً:
   `best-english-podcasts.html` یا `how-to-remember-vocabulary.html`
   - فقط حروف کوچک انگلیسی، خط تیره (-) و بدون فاصله.
   - این نام همان slug مقاله است.
3. **تصویر کاور مقاله** را بساز و در پوشه `blog/covers/` با نام `<slug>.jpg` ذخیره کن:
   - ابعاد **۱۳۴۴×۷۶۸** (افقی ۱۶:۹ تقریبی)، فرمت JPG، حجم حدود ۵۰ تا ۱۵۰ کیلوبایت.
   - سبک همه‌ی کاورهای فعلی: تصویرسازی سه‌بعدی نرم و دوستانه با پس‌زمینه سبز تیره‌ی برند، **بدون متن داخل تصویر**.
   - برای ساخت می‌توانی از ابزارهای تصویرسازی هوش مصنوعی استفاده کنی؛ فقط عبارت «soft 3D clay render, Pixar-style, deep dark emerald green background, no text» را در پرامپت نگه دار تا ست کاورها یکدست بماند.
   - یک مقاله بدون کاور در اپلیکیشن هم درست نمایش داده می‌شود (جایگزین شیشه‌ای نشان می‌دهد)، اما هر مقاله کاور خودش را دارد.

### قدم ۲ — پر کردن قالب

در فایل جدید همه جای‌گذار‌های `{{...}}` را با محتوای واقعی عوض کن (در قالب با کامنت مشخص شده‌اند):

| چی را | کجا |
|---|---|
| عنوان و توضیح | `<title>` و `<meta name="description">` (توضیح حداکثر ۱۶۰ کاراکتر) |
| آدرس مقاله | `canonical` و `og:url` و `mainEntityOfPage` و `@id` در JSON-LD |
| تاریخ | `article:published_time`، `datePublished` و `<time datetime>` |
| عنوان و متن | `h1`، بخش «پاسخ کوتاه»، محتوای `<div class="prose">` |
| پرسش‌ها | بخش FAQ انتهای مقاله **و** همان متن‌ها در JSON-LD (عیناً یکسان!) |

⚠️ **سه قانون طلایی سئو/AEO:**
1. **پاسخ کوتاه**: باکس اول مقاله را ۴۰ تا ۶۰ واژه بنویس؛ مستقیم و بدون مقدمه. موتورهای پاسخ (ChatGPT، گوگل، پرشیجو) معمولاً همین بند را نقل می‌کنند.
2. **عین‌ویژگی FAQ**: متن پرسش/پاسخ داخل صفحه باید با متن `FAQPage` در JSON-LD دقیقاً یکی باشد.
3. **زیرعنوان‌های پرسشی**: سعی کن h2ها شکل سؤال داشته باشند («چطور...؟»، «چرا...؟») — برای نمایش در نتایج گوگل و پاسخ AI عالی است.

### قدم ۳ — ثبت در فهرست مقالات

فایل `blog/posts.json` را باز کن و **بالای آرایه posts** یک ردیف جدید اضافه کن:

```json
{
  "slug": "best-english-podcasts",
  "url": "articles/best-english-podcasts.html",
  "title": "عنوان فارسی مقاله",
  "desc": "خلاصه دو خطی که در کارت وبلاگ نمایش داده می‌شود.",
  "category": "یادگیری انگلیسی",
  "cover": "covers/best-english-podcasts.jpg",
  "date": "2026-10-18",
  "dateFa": "۲۶ مهر ۱۴۰۵",
  "minutes": 7
}
```

- `cover` مسیر تصویر کاور نسبت به پوشه وبلاگ (فایل را در قدم ۱ ساخته‌ای)
- `date` میلادی به شکل `YYYY-MM-DD`
- `dateFa` تاریخ شمسی
- `minutes` زمان تقریبی مطالعه
- دسته‌بندی‌های فعلی: «یادگیری انگلیسی»، «مکالمه و هوش مصنوعی»، «تلفظ و شنیداری»، «واژگان»، «انگیزه و عادت» — یا دسته جدید بساز.

### قدم ۴ — ثبت در sitemap و feed

**`sitemap.xml`**: یک بلوک جدید قبل از `</urlset>`:

```xml
<url>
  <loc>https://upword.ir/blog/articles/best-english-podcasts.html</loc>
  <lastmod>2026-10-18</lastmod>
  <changefreq>monthly</changefreq>
  <priority>0.8</priority>
</url>
```

**`feed.xml`**: یک بلوک جدید قبل از `</channel>` (اولین آیتم = جدیدترین مقاله):

```xml
<item>
  <title>عنوان فارسی مقاله</title>
  <link>https://upword.ir/blog/articles/best-english-podcasts.html</link>
  <guid isPermaLink="true">https://upword.ir/blog/articles/best-english-podcasts.html</guid>
  <description>خلاصه مقاله</description>
  <pubDate>Sun, 18 Oct 2026 09:00:00 +0330</pubDate>
  <category>یادگیری انگلیسی</category>
  <enclosure url="https://upword.ir/blog/covers/best-english-podcasts.jpg" type="image/jpeg" length="102400"/>
</item>
```

### قدم ۵ — ساخت JSON محتوا برای اپلیکیشن (مهم!)

اپلیکیشن مقاله‌ها را **کاملاً native** (بدون WebView) نمایش می‌دهد؛ محتوای هر مقاله باید به شکل JSON ساختاریافته هم منتشر شود:

```bash
python3 scripts/extract_article_content.py
```

- این اسکریپت از خود HTML مقاله‌ها `blog/content/<slug>.json` می‌سازد و فیلد `"content"` را در `posts.json` اضافه/به‌روز می‌کند.
- HTML منبع اصلی می‌ماند (برای سئو و وب)؛ JSON فقط یک خروجی مشتق است — پس بعد از هر تغییر در مقاله‌ها، فقط اسکریپت را دوباره اجرا کن.
- اگر مقاله‌ای ساختار جدیدی دارد که اسکریپت نمی‌شناسد، بلوک ناشناخته در اپ به‌صورت پاراگراف ساده نمایش داده می‌شود — اپ نیازی به آپدیت ندارد.
- **انتشار فقط از طریق سایت GitHub (بدون ترمینال):** اگر به اسکریپت دسترسی نداری، `blog/content/<slug>.json` را دستی طبق الگوی مقاله‌های قبلی بساز و کامیت کن — ساختار بلوک‌ها در سربرگ خود اسکریپت مستند شده است.

### قدم ۶ — کامیت و انتشار

```bash
git add blog/ sitemap.xml feed.xml
git commit -m "blog: new article — best-english-podcasts"
git push origin main
```

بعد از push، GitHub Pages طی ۱ تا ۳ دقیقه مقاله را روی `upword.ir/blog/articles/...` منتشر می‌کند.

---

## 💡 انتشار فقط از طریق سایت GitHub (بدون ترمینال)

1. در ریپو روی **Add file → Create new file** بزن و مسیر را با `/` تایپ کن: `blog/articles/nome-file.html`
2. محتوای قالب پرشده را paste کن و **Commit changes**.
3. سپس `blog/posts.json` را باز کن، دکمه pencil ✏️، ردیف جدید را اضافه کن، کامیت.
4. همین کار را برای `sitemap.xml` و `feed.xml` انجام بده.
5. تمام — صفحات جدید خودکار publish می‌شوند.

---

## 🔎 چک‌لیست نهایی قبل از کامیت

- [ ] همه `{{...}}`های قالب با محتوای واقعی جایگزین شده‌اند (با Ctrl+F جستجو کن: `{{`)
- [ ] `canonical` و `og:url` با نام فایل جدید هم‌خوان‌اند
- [ ] تاریخ در `<time>`، `article:published_time` و `datePublished` یکی است
- [ ] متن FAQ داخل صفحه = متن FAQPage در JSON-LD
- [ ] مقاله در `posts.json` ثبت شده
- [ ] آدرس مقاله در `sitemap.xml` و آیتم آن در `feed.xml` اضافه شده
- [ ] لینک مقالات مرتبط به‌روز شده

## 🧪 تست سریع بعد از انتشار

1. آدرس مقاله را در مرورگر باز کن — عنوان و تاریخ درست باشد.
2. [ Rich Results Test گوگل](https://search.google.com/test/rich-results) را باز کن، آدرس مقاله را بده و مطمئن شو Article و FAQ بدون خطا سبز می‌شوند.
3. `https://upword.ir/blog/` را رفرش کن — کارت مقاله جدید اول لیست باشد.

---

سؤال یا نیاز به مقاله با موضوع خاصی داشتی، همین قالب کافی است؛ ساختار سئو (Schema، Canonical، OG، RSS و Sitemap) از قبل برایت آماده است.

# آپ‌وورد | UpWord Landing Page

لندینگ پیج رسمی اپلیکیشن **آپ‌وورد** — یادگیری زبان با مکالمه هوش مصنوعی، درس‌های ساختاریافته و گیمیفیکیشن.

Official landing page for the **UpWord** language-learning app.

---

## ساختار پروژه | Project Structure

```
upword-landing/
├── index.html              # صفحه اصلی لندینگ (فارسی پیش‌فرض + انگلیسی)
├── css/
│   └── styles.css          # سیستم طراحی شیشه‌ای سبز تیره + فونت‌های self-host
├── js/
│   └── main.js             # دوزبانه، انیمیشن، Lottie (lazy)، تعاملات
├── assets/
│   ├── images/             # آیکون اپ + تصویر هیرو (responsive srcset) + orb های pre-baked
│   ├── fonts/              # فونت‌های متغیر self-host (Vazirmatn / Inter / Space Grotesk)
│   ├── js/
│   │   └── vendor/         # lottie-light player (local)
│   └── lottie/             # انیمیشن‌های لاک‌پشت
├── .nojekyll               # غیرفعال‌سازی Jekyll در GitHub Pages
├── DESIGN.md               # مستندات سیستم طراحی
└── README.md
```

## امکانات لندینگ | Landing Features

- 🎨 طراحی **شیشه‌ای (Glassmorphism)** هم‌راستا با طراحی داخل اپ — سبز تیره + پنل‌های شیشه‌ای + نورپردازی محیطی
- 🌍 **دوزبانه کامل**: فارسی (RTL، پیش‌فرض) و انگلیسی (LTR) با ۲۱۱ کلید ترجمه و ذخیره انتخاب کاربر
- 🧩 نمایش **جز به جز ارزش اپ**: درس‌های ساختاریافته A1 با حلقه پیشرفت دایره‌ای، مکالمه AI با بازخورد، تمرین شدوینگ، گیمیفیکیشن (XP / سطح / جواهر / دستاورد / زنجیره روزها با تقویم ایرانی)، یادآور تمرین، ۷ زبان و…
- 📱 موکاپ‌های اپ با HTML/CSS خالص (صفحه اصلی، درس‌ها، چت، دستاوردها، واژگان)
- 💎 بخش **رایگان vs پرمیوم** با طرح‌های اشتراک (بدون قیمت hardcoded — قیمت‌ها از پنل فروشگاه)
- 🛍 دکمه‌های دانلود از **کافه بازار** و **مایکت**
- 🐢 انیمیشن‌های Lottie لاک‌پشت (شنا، موفقیت، مدیتیشن)
- ♿️ دسترس‌پذیری: کنتراست AA، فوکوس مرئی، skip-link، reduced-motion، Escape برای منوها
- ⚡ واکنش‌گرا — موبایل، تبلت، دسکتاپ
- 🚀 **پرفورمنس بهینه**: بدون هیچ درخواست خارجی (self-host کامل)، فونت‌ها و تصاویر با preload، Lottie با lazy-load، رندر بخش‌های پایین صفحه با content-visibility — امتیاز Lighthouse موبایل ۹۹

## پرفورمنس | Performance

این صفحه برای کاربران ایرانی (شبکه کند و CDNهای خارجی کند/فیلتر) به حداکثر سرعت بهینه شده است — همه‌چیز از یک origin واحد سرو می‌شود:

- **فونت‌های self-host**: سه فایل فونت متغیر subset شده (`assets/fonts/`) به‌جای ~۱۵ فایل از دو دامنه خارجی (fonts.googleapis.com + gstatic) — کل وزن فونت از ~۲۱۵KB به ~۱۴۸KB برای همه وزن‌ها رسید و CSS گوگل‌فونت (که ۱.۹ ثانیه رندر را بلاک می‌کرد) حذف شد.
- **Lottie lazy**: پلیر سبک‌تر `lottie-light` (local) + فایل‌های JSON فقط وقتی بخش لاک‌پشت به viewport نزدیک شود دانلود می‌شوند — ~۳۷۰KB از مسیر بحرانی حذف شد.
- **Orb های pre-baked**: بلور ۹۰px با سه تصویر webp کوچک (رندرشده با خود مرورگر) جایگزین شد؛ انیمیشن فقط transform است و فیلتر دوباره محاسبه نمی‌شود.
- **Backdrop-filter فقط روی سطوح کلیدی**: کارت‌های شیشه‌ای روی پس‌زمینه تخت با گرادیانت نیمه‌شفاف — اسکرول روی موبایل دیگر هر فریم را re-filter نمی‌کند.
- **content-visibility: auto** برای سکشن‌های زیر fold — DOM اولیه از ۱۲۹۲ به ۸۰۵ عنصر و main-thread از ۲.۴s به ۱.۳s رسید.
- **تصاویر بهینه**: og-cover ۳۳۰→۸۲KB، هیرو با srcset (۴۸۰w/۶۴۰w) و ۶۴KB.
- **Minify**: HTML/CSS/JS با csso + terser + html-minifier-terser.

نتیجه Lighthouse (لوکال، شبیه‌سازی شبکه):

| متریک | قبل | بعد |
|---|---|---|
| امتیاز موبایل | 75 | 99 |
| امتیاز دسکتاپ | 72 | 89 |
| FCP موبایل | 3.9s | 0.8s |
| LCP موبایل | 4.5s | 2.3s |
| TBT دسکتاپ | 200ms | 50ms |
| درخواست دامنه خارجی | ۲ | ۰ |

## انتشار روی GitHub Pages | Deploy to GitHub Pages

### روش ۱: از طریق GitHub UI (ساده‌ترین)

1. به صفحه ریپازیتوری بروید: `https://github.com/mvaliolahi/upword-landing`
2. روی **Settings** کلیک کنید
3. از منوی سمت چپ، **Pages** را انتخاب کنید
4. در بخش **Source**، گزینه **Deploy from a branch** را انتخاب کنید
5. **Branch** را روی `main` و فولدر را روی `/ (root)` تنظیم کنید
6. روی **Save** کلیک کنید
7. بعد از چند دقیقه، لندینگ روی این آدرس در دسترس خواهد بود:

   ```
   https://mvaliolahi.github.io/upword-landing/
   ```

### روش ۲: از طریق GitHub CLI

```bash
git push origin main
# سپس در GitHub UI همان مراحل بالا را دنبال کنید
```

## توسعه محلی | Local Development

نیازی به build نیست — یک سایت استاتیک کامل است:

```bash
# با هر سرور محلی ساده:
python3 -m http.server 8000
# یا
npx serve .
```

سپس به `http://localhost:8000` بروید.

## شخصی‌سازی | Customization

### تغییر رنگ‌ها

فایل `css/styles.css` را باز کنید و متغیرهای CSS را در `:root` تغییر دهید:

```css
:root {
  --green: #22C55E;      /* رنگ اصلی برند */
  --green-lite: #4ADE80; /* روشن */
  --bg-0: #04231A;       /* سبز تیره پس‌زمینه */
  --butter: #F5E7AE;     /* رنگ دوم (جواهر/بازخورد) */
}
```

### تغییر لینک‌های فروشگاه

تمام لینک‌های `https://cafebazaar.ir/app/?id=ir.upword.twa` و `https://myket.ir/app/ir.upword.twa` را در `index.html` جستجو و جایگزین کنید.

### افزودن متن دوزبانه جدید

1. در `index.html` مشخصه `data-i18n="کلید.جدید"` را به عنصر اضافه کنید (متن پیش‌فرض فارسی).
2. در `js/main.js` کلید را به هر دو دیکشنری `fa` و `en` اضافه کنید.

### افزودن انیمیشن Lottie جدید

1. فایل JSON را در `assets/lottie/` قرار دهید
2. در `js/main.js`، تابع `loadLottie` را فراخوانی کنید:

```javascript
loadLottie('containerId', 'assets/lottie/your-animation.json');
```

3. در `index.html`، یک `<div id="containerId"></div>` اضافه کنید.

## تکنولوژی‌ها | Technologies

- **HTML5** — semantic markup
- **CSS3** — Custom Properties, Grid, Flexbox, backdrop-filter, content-visibility
- **Vanilla JavaScript** — بدون فریم‌ورک
- **Lottie Web (light build, self-hosted)** — انیمیشن‌های لاک‌پشت
- **Vazirmatn / Inter / Space Grotesk** — فونت‌های متغیر self-host در `assets/fonts/`

## سازنده | Author

**mvaliolahi** — [GitHub](https://github.com/mvaliolahi)

ساخته‌شده با ❤️ در ایران

---

© ۲۰۲۶ آپ‌ورد — تمام حقوق محفوظ است.

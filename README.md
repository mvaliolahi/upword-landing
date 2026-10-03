# آپ‌وورد | UpWord Landing Page

لندینگ پیج رسمی اپلیکیشن **آپ‌وورد** — یادگیری زبان با مکالمه هوش مصنوعی، درس‌های ساختاریافته و گیمیفیکیشن.

Official landing page for the **UpWord** language-learning app.

---

## ساختار پروژه | Project Structure

```
upword-landing/
├── index.html              # صفحه اصلی لندینگ (فارسی پیش‌فرض + انگلیسی)
├── css/
│   └── styles.css          # سیستم طراحی شیشه‌ای سبز تیره
├── js/
│   └── main.js             # دوزبانه، انیمیشن، Lottie، تعاملات
├── assets/
│   ├── images/             # آیکون اپ + تصویر هیرو
│   └── lottie/             # انیمیشن‌های لاک‌پشت
├── .nojekyll               # غیرفعال‌سازی Jekyll در GitHub Pages
├── DESIGN.md               # مستندات سیستم طراحی
└── README.md
```

## امکانات لندینگ | Landing Features

- 🎨 طراحی **شیشه‌ای (Glassmorphism)** هم‌راستا با طراحی داخل اپ — سبز تیره + پنل‌های شیشه‌ای + نورپردازی محیطی
- 🌍 **دوزبانه کامل**: فارسی (RTL، پیش‌فرض) و انگلیسی (LTR) با ۲۱۱ کلید ترجمه و ذخیره انتخاب کاربر
- 🧩 نمایش **جز به جز ارزش اپ**: درس‌های ساختاریافته A1 با حلقه پیشرفت دایره‌ای، مکالمه AI با بازخورد، تمرین شدوینگ، گیمیفیکیشن (XP / سطح / جواهر / دستاورد / زنجیره روزها با تقویم ایرانی)، یادآور تمرین، ۶ زبان و…
- 📱 موکاپ‌های اپ با HTML/CSS خالص (صفحه اصلی، درس‌ها، چت، دستاوردها، واژگان)
- 💎 بخش **رایگان vs پرمیوم** با طرح‌های اشتراک (بدون قیمت hardcoded — قیمت‌ها از پنل فروشگاه)
- 🛍 دکمه‌های دانلود از **کافه بازار** و **مایکت**
- 🐢 انیمیشن‌های Lottie لاک‌پشت (شنا، موفقیت، مدیتیشن)
- ♿️ دسترس‌پذیری: کنتراست AA، فوکوس مرئی، skip-link، reduced-motion، Escape برای منوها
- ⚡ واکنش‌گرا — موبایل، تبلت، دسکتاپ

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
- **CSS3** — Custom Properties, Grid, Flexbox, backdrop-filter
- **Vanilla JavaScript** — بدون فریم‌ورک
- **Lottie Web** — انیمیشن‌های لاک‌پشت
- **Vazirmatn / Inter / Space Grotesk** — فونت‌ها از گوگل فونتس

## سازنده | Author

**mvaliolahi** — [GitHub](https://github.com/mvaliolahi)

ساخته‌شده با ❤️ در ایران

---

© ۲۰۲۶ آپ‌ورد — تمام حقوق محفوظ است.

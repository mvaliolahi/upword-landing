# آپ‌وورد | UpWord Landing Page

لندینگ پیج رسمی اپلیکیشن **آپ‌وورد** — یادگیری زبان با مکالمه واقعی هوش مصنوعی.

Official landing page for the **UpWord** language-learning app.

---

## ساختار پروژه | Project Structure

```
upword-landing/
├── index.html              # صفحه اصلی لندینگ
├── css/
│   └── styles.css          # تمام استایل‌ها
├── js/
│   └── main.js             # تعاملات، انیمیشن، Lottie
├── assets/
│   ├── images/             # آیکون اپلیکیشن
│   └── lottie/             # انیمیشن‌های لاکپشت
├── .nojekyll               # غیرفعال‌سازی Jekyll در GitHub Pages
└── README.md
```

## امکانات لندینگ | Landing Features

- 🎨 طراحی RTL کامل با فونت فارسی Vazirmatn
- 🟢 رنگ سبز اصلی برند (#22C55E) با افکت ۳D
- 🐢 انیمیشن‌های Lottie لاکپشت در سراسر صفحه
- 📱 واکنش‌گرا (Responsive) — موبایل، تبلت، دسکتاپ
- ⚡ انیمیشن‌های اسکرول و افکت‌های تعاملی
- 🎯 دکمه‌های Call-to-Action به کافه‌بazaar
- 🔢 شمارنده‌های متحرک با اعداد فارسی
- ❓ بخش سوالات متداول (Accordion)
- 💬 بخش نظرات کاربران
- 📸 موکاپ‌های اپلیکیشن با CSS خالص

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

### تغییر رنگ اصلی

فایل `css/styles.css` را باز کنید و متغیرهای CSS را در `:root` تغییر دهید:

```css
:root {
  --green: #22C55E;        /* رنگ اصلی */
  --green-dark: #15803D;   /* رنگ تیره برای ۳D effect */
  --green-light: #4ADE80;  /* رنگ روشن برای hover */
}
```

### تغییر لینک کافه‌بazaar

تمام لینک‌های `http://cafebazaar.ir/app/?id=ir.upword.twa` را در `index.html` جستجو و جایگزین کنید.

### افزودن انیمیشن Lottie جدید

1. فایل JSON را در `assets/lottie/` قرار دهید
2. در `js/main.js`، تابع `loadLottie` را فراخوانی کنید:

```javascript
loadLottie('containerId', 'assets/lottie/your-animation.json');
```

3. در `index.html`، یک `<div id="containerId"></div>` اضافه کنید.

## تکنولوژی‌ها | Technologies

- **HTML5** — semantic markup
- **CSS3** — Custom Properties, Grid, Flexbox, animations
- **Vanilla JavaScript** — بدون فریم‌ورک
- **Lottie Web** — انیمیشن‌های لاکپشت
- **Vazirmatn** — فونت فارسی گوگل فونتس

## سازنده | Author

**mvaliolahi** — [GitHub](https://github.com/mvaliolahi)

ساخته‌شده با ❤️ در ایران

---

© ۲۰۲۶ آپ‌وورد — تمام حقوق محفوظ است.

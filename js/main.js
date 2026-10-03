/* ============================================
   UpWord Landing — Main JavaScript
   Bilingual: Persian (default, rtl) + English (ltr)
   ============================================ */

(function () {
  'use strict';

  /* ===== i18n dictionary ===== */
  const I18N = {
    fa: {
      'nav.skip': 'رفتن به محتوای اصلی',
      'nav.features': 'امکانات',
      'nav.journey': 'مسیر یادگیری',
      'nav.preview': 'پیش‌نمایش اپ',
      'nav.premium': 'پرمیوم',
      'nav.reviews': 'تجربه کاربران',
      'nav.faq': 'پرسش‌های رایج',
      'nav.download': 'دانلود',

      'hero.pill': 'نسخه ۲.۸۵ · با طراحی شیشه‌ای جدید',
      'hero.title': 'از «سلام» تا<br /><span class="text-gradient">مکالمه‌های واقعی</span>',
      'hero.subtitle': 'آپ‌ورد برای فارسی‌زبان‌ها ساخته شده: درس‌های کوتاه و موضوعی، تمرین مکالمه با هوش مصنوعی، تمرین شدوینگ و مرور هوشمند — همه در یک اپلیکیشن با طراحی شیشه‌ای که دوستش داری.',
      'hero.ctaBazaar': 'دانلود از کافه بازار',
      'hero.ctaMyket': 'دانلود از مایکت',
      'hero.free': 'شروع رایگان · موضوع اول سطح A1 با سه درس',
      'hero.chip1': '۶ زبان مقصد',
      'hero.chip2': '۳ درس در هر موضوع',
      'hero.chip3': 'اندروید ۸ به بالا',
      'hero.alt': 'تصویر نمایشی: کاربر آپ‌ورد در حال تبریک گفت‌وگو، همراه با لاک‌پشت نماد آپ‌ورد',
      'hero.notifTitle': 'یادآور تمرین',
      'hero.notifBody': 'وقت تمرین امروزه! ۱۰ دقیقه کافیه 🐢',
      'hero.notifNow': 'شروع تمرین',
      'hero.notifLater': 'بعداً',
      'hero.streakCard': '۷ روز پیاپی',
      'hero.streakSub': 'زنجیره تمرینت قطع نشده!',
      'hero.xpCard': '‎+۸۰ XP',
      'hero.xpSub': 'سطح ۵ · پیشرفت عالی',
      'hero.caption': 'تصویر نمایشی از حال‌وهوای آپ‌ورد',

      'mock.time': '۹:۴۱',
      'mock.notifTime': '۲۰:۰۰',
      'mock.xpNum': '۱٬۲۴۰',
      'mock.gemNum': '۱۲۰',

      'languages.label': 'زبان مقصدت را انتخاب کن:',
      'languages.en': 'انگلیسی',
      'languages.es': 'اسپانیایی',
      'languages.fr': 'فرانسوی',
      'languages.de': 'آلمانی',
      'languages.tr': 'ترکی',
      'languages.ar': 'عربی',
      'languages.note': 'در اولین ورود انتخاب می‌شود و هر وقت خواستی، از تنظیمات یا صفحه اصلی عوضش کن.',

      'journey.eyebrow': 'مسیر یادگیری',
      'journey.title': 'چهار قدم تا اولین مکالمه',
      'journey.subtitle': 'از اولین ورود تا گفت‌وگوهای روان، آپ‌ورد قدم‌به‌قدم همراهته.',
      'journey.s1.title': 'زبان و سطحت را انتخاب کن',
      'journey.s1.desc': 'در اولین ورود، زبان مقصد و سطحت را انتخاب می‌کنی — مبتدی (A1) بهترین نقطه شروع است. هر وقت خواستی از تنظیمات تغییرش بده.',
      'journey.s2.title': 'درس‌ها را قدم‌به‌قدم جلو برو',
      'journey.s2.desc': 'هر موضوع — مثل «سلام و معرفی» — سه درس کوتاه دارد: واژه‌ها، جمله‌های کاربردی و تمرین. پیشرفت هر درس در حلقه‌ای دایره‌ای نمایش داده می‌شود.',
      'journey.s3.title': 'مکالمه را با هوش مصنوعی تمرین کن',
      'journey.s3.desc': 'آموخته‌هایت را در مکالمه واقعی به کار ببر؛ جواب می‌گیری، اشتباه‌هایت اصلاح می‌شود و راه‌های بهتر گفتن را یاد می‌گیری.',
      'journey.s4.title': 'پیشرفتت را ببین و ادامه بده',
      'journey.s4.desc': 'XP، سطح، جواهر و دستاوردها پیشرفتت را نشان می‌دهند و یادآور تمرین کمک می‌کند روتین یادگیری‌ات قطع نشود.',

      'features.eyebrow': 'امکانات، جز به جز',
      'features.title': 'هر چیزی که برای یادگیری لازم داری، سر جایش است',
      'features.subtitle': 'آپ‌ورد فقط یک اپ مکالمه یا فقط یک اپ واژگان نیست؛ همه ابزارهای یادگیری، کنار هم و هماهنگ با هم.',

      'f1.eyebrow': 'دوره‌های ساختاریافته',
      'f1.title': 'موضوع به موضوع، درس به درس',
      'f1.desc': 'یادگیری از سطح A1 و موضوع‌های کاربردی زندگی روزمره شروع می‌شود: «سلام و معرفی»، خانواده، خرید و…. هر موضوع سه درس کوتاه دارد و پیشرفت هر درس در حلقه‌ای دایره‌ای نشان داده می‌شود. موضوع اول برای همه رایگان است تا بدون ریسک شروع کنی.',
      'f1.b1': 'درس‌های کوتاه ۵ تا ۱۰ دقیقه‌ای',
      'f1.b2': 'حلقه پیشرفت دایره‌ای برای هر درس',
      'f1.b3': 'موضوع اول A1 کاملاً رایگان',
      'f1.b4': 'واژه‌ها همراه با تلفظ و مثال',

      'courses.screenTitle': 'درس‌ها',
      'courses.topic': 'سلام و معرفی',
      'courses.free': 'رایگان',
      'courses.l1': 'درس ۱ · سلام کردن',
      'courses.done': 'کامل شد ✓',
      'courses.l2': 'درس ۲ · معرفی خودت',
      'courses.current': 'در حال یادگیری · ۶۰٪',
      'courses.l3': 'درس ۳ · سؤال کردن',
      'courses.locked': 'قفل · درس قبلی را کامل کن',
      'courses.nextTopic': 'خانواده و دوستان',
      'courses.premiumBadge': 'پرمیوم',

      'f2.eyebrow': 'مکالمه با هوش مصنوعی',
      'f2.title': 'همراهی که همیشه وقت دارد',
      'f2.desc': 'با هوش مصنوعی درباره موضوع‌های واقعی حرف بزن: سفارش قهوه، معرفی خودت، تعریف روزت. جمله‌هایت بازخورد می‌گیرد، شکل درست‌تر و مؤدبانه‌تر را یاد می‌گیری و کم‌کم اعتمادبه‌نفس گفتاری‌ات ساخته می‌شود — با متن یا صدا.',
      'f2.b1': 'بازخورد و اصلاح روی هر جمله',
      'f2.b2': 'موضوع‌های واقعی زندگی روزمره',
      'f2.b3': 'ورودی متنی و صوتی',
      'f2.b4': 'بدون خجالت — هر بار بهتر از قبل',

      'chat.partner': 'شریک تمرین',
      'chat.online': 'آنلاین',
      'chat.fbTitle': 'یک نکته کوچک',
      'chat.fbBody': '«goed» درست نیست؛ گذشته‌ی «go» می‌شود «went»: I went to the cafe.',
      'chat.placeholder': 'بنویس یا بگو…',

      'f3.eyebrow': 'گیمیفیکیشن',
      'f3.title': 'انگیزه، هر روز تازه می‌شود',
      'f3.desc': 'هدف روزانه، XP و سطح، جواهر، دستاوردها و زنجیره روزهای پیاپی — همه کنار هم، تمرین کردن را به عادتی تبدیل می‌کنند که با میل ادامه می‌دهی. تقویم هفته با استاندارد ایران (شنبه تا جمعه) و تیک روزهای تمرین‌شده، پیشرفتت را یک‌جا نشان می‌دهد.',
      'f3.b1': 'هدف روزانه و زنجیره روزهای پیاپی',
      'f3.b2': 'XP، سطح و جواهر',
      'f3.b3': 'دستاوردها و مدال‌های یادگیری',
      'f3.b4': 'یادآور تمرین هوشمند',

      'game.name': 'سارا',
      'game.level': 'سطح ۵ · Learner',
      'game.gemsVal': '💎 ۱۲۰',
      'game.xpLabel': 'امتیاز تجربه (XP)',
      'game.xpVal': '۷۲۰ / ۱۰۰۰',
      'game.streakVal': '🔥 ۷',
      'game.streak': 'روز پیاپی',
      'game.xpTotalVal': '⚡ ۱٬۲۴۰',
      'game.xpTotal': 'کل XP',
      'game.trophyVal': '🏆 ۱۲',
      'game.trophies': 'دستاورد',
      'game.weekTitle': 'این هفته',
      'game.ach1': 'اولین مکالمه',
      'game.ach2': '۷ روز پیاپی',
      'game.ach3': '۱۰ ماموریت',

      'bento.eyebrow': 'جزئیاتی که تجربه را می‌سازند',
      'bento.title': 'یک اپ، همه ابزارها',
      'b1.title': 'تمرین شدوینگ',
      'b1.desc': 'جمله را گوش بده، همراه با آن تکرار کن و ریتم و تلفظ زبان را در ذهنت و گفتارت بنشان.',
      'b2.title': 'یادآور تمرین',
      'b2.desc': 'نوتیفیکیشن هوشمند در ساعتی که خودت انتخاب می‌کنی؛ روتین یادگیری‌ات قطع نمی‌شود.',
      'b3.title': 'طراحی شیشه‌ای',
      'b3.desc': 'رابط کاربری مدرن با پنل‌های شیشه‌ای، انیمیشن‌های نرم و رنگ آرامش‌بخش سبز.',
      'b4.title': '۶ زبان مقصد',
      'b4.desc': 'انگلیسی، اسپانیایی، فرانسوی، آلمانی، ترکی و عربی — در هر زمان قابل تغییر.',
      'b5.title': 'متن یا صدا',
      'b5.desc': 'با کیبورد بنویس یا با میکروفون حرف بزن؛ با همان که راحت‌تر شروع کن.',
      'b6.title': 'داده‌هایت مال خودت',
      'b6.desc': 'تاریخچه یادگیری روی دستگاهت ذخیره می‌شود؛ فقط برای پاسخ AI به سرویس انتخابی‌ات ارسال می‌شود.',
      'b7.title': 'ساخته‌شده برای ایران',
      'b7.desc': 'پرداخت ریالی و امن از کافه بازار و مایکت، تقویم هفته‌ی ایرانی و تجربه فارسی‌اول.',
      'b8.title': 'زبانت را هر وقت خواستی عوض کن',
      'b8.desc': 'از صفحه اصلی و با یک لمس، زبان مقصدت را عوض کن و یادگیری زبان جدید را شروع کن.',

      'preview.eyebrow': 'پیش‌نمایش اپ',
      'preview.title': 'نگاهی به داخل آپ‌ورد',
      'preview.subtitle': 'از صفحه اصلی تا مکالمه و دستاوردها — این نمونه‌های نمایشی، حال‌وهوای واقعی اپ را نشان می‌دهند.',
      'preview.note': 'همه‌ی صفحات بالا نمونه‌های نمایشی هستند تا حس واقعی اپ را بگیری.',

      'home.greeting': 'سلام، سارا 👋',
      'home.sub': 'امروز چ تمرین می‌کنیم؟',
      'home.streakVal': '🔥 ۷',
      'home.goalTitle': 'هدف امروز',
      'home.goalPct': '۶۰٪',
      'home.goalSub': '۳۰ از ۵۰ XP',
      'home.mission': 'ماموریت امروز',
      'home.missionSub': 'سفارش دادن در کافه',
      'home.vocab': 'واژگان جدید',
      'home.vocabSub': '۱۲ واژه یاد گرفتی',

      'ach.title': 'دستاوردها',
      'ach.subtitle': 'دستاورد جدید!',
      'ach.name': '۷ روز پیاپی',
      'ach.desc': 'یک هفته کامل تمرین کردی!',
      'ach.xpVal': '+۱۰۰ XP',
      'ach.a1': 'اولین مکالمه',
      'ach.a2': '۷ روز پیاپی',
      'ach.a3': '۱۰ ماموریت',

      'vocab.title': 'واژگان',
      'vocab.progress': '۱۲ واژه از ۲۰ واژه',
      'vocab.meaning': 'اتفاق خوشایند و غیرمنتظره',
      'vocab.listen': 'گوش بده',
      'vocab.know': 'بلدم!',

      'premium.eyebrow': 'رایگان شروع کن، هر وقت خواستی ارتقا بده',
      'premium.title': 'ساده شروع کن. وقتی رضایت داشتی، کامل کن.',
      'premium.subtitle': 'بدون کارت بانکی و بدون فشار — موضوع اول برای همیشه رایگان است.',
      'premium.badge': 'انتخاب بیشتر کاربران',
      'premium.free.title': 'رایگان',
      'premium.free.price': '۰ تومان · همیشه',
      'premium.free.f1': 'موضوع اول سطح A1: «سلام و معرفی» با ۳ درس',
      'premium.free.f2': 'مکالمه‌های اولیه با هوش مصنوعی',
      'premium.free.f3': 'واژگان و مرور پایه',
      'premium.free.f4': 'گیمیفیکیشن کامل: XP، سطح، دستاوردها',
      'premium.free.cta': 'دانلود و شروع رایگان',
      'premium.pro.title': 'پرمیوم',
      'premium.pro.price': 'همه مسیر، بدون قفل',
      'premium.pro.f1': 'همه موضوع‌های A1 و سطوح بالاتر',
      'premium.pro.f2': 'مکالمه نامحدود با هوش مصنوعی',
      'premium.pro.f3': 'تمرین شدوینگ کامل',
      'premium.pro.f4': 'یادآور و آمار پیشرفته',
      'premium.pro.f5': 'پشتیبانی زنجیره‌ی پیشرفت',
      'premium.tier1': 'ماهانه',
      'premium.tier2': 'شش‌ماهه',
      'premium.tier3': 'سالانه · بهترین انتخاب',
      'premium.tier4': 'مادام‌العمر',
      'premium.note': 'قیمت‌ها در صفحه پرداخت داخل اپ و بر اساس پنل فروشگاه (کافه بازار / مایکت) نمایش داده می‌شوند. پرداخت امن و ریالی از طریق همان فروشگاه انجام می‌شود.',

      'testi.eyebrow': 'تجربه کاربران',
      'testi.title': 'کاربران درباره آپ‌ورد چه می‌گویند؟',
      'testi.subtitle': 'چند نظر واقعی از کاربران آپ‌ورد در کافه بازار. برای تازه‌ترین امتیازها به صفحه اپ سر بزن.',
      'testi.r1.translation': '«بی‌نظیر و کامل. همه‌چیز را پوشش می‌دهد. بهترین قسمتش پیدا کردن تلفظ و استفاده روتین کلمه در دیالوگ فیلم‌هاست. عاااالیه.»',
      'testi.r1.role': 'کاربر کافه بازار',
      'testi.r2.translation': '«خیلی باحاله؛ یک پکیج کامل از ابزارهای مختلف که در همه زمینه‌ها کمک می‌کند.»',
      'testi.r2.role': 'کاربر کافه بازار',
      'testi.r3.translation': '«برنامه خیلی خوب و کاربردی است و امکانات جالبی دارد.»',
      'testi.r3.role': 'کاربر کافه بازار',
      'testi.summary': 'دوست داری تجربه بقیه را هم بخوانی؟ تازه‌ترین نظرها و امتیازها را در صفحه آپ‌ورد در کافه بازار ببین.',
      'testi.viewAll': 'مشاهده در کافه بازار',

      'faq.eyebrow': 'پرسش‌های رایج',
      'faq.title': 'هر چیزی که ممکن است بپرسی',
      'faq.q1': 'چطور شروع کنم؟',
      'faq.a1': 'از کافه بازار یا مایکت دانلود کن، در اولین ورود زبان مقصد و سطحت را انتخاب کن و موضوع رایگان «سلام و معرفی» را با سه درس شروع کن — بدون نیاز به پرداخت.',
      'faq.q2': 'پرمیوم چیست و چطور آن را بخرم؟',
      'faq.a2': 'پرمیوم همه موضوع‌ها، مکالمه نامحدود و امکانات کامل را باز می‌کند. خرید از داخل اپ و به‌صورت امن از طریق کافه بازار یا مایکت انجام می‌شود؛ قیمت‌ها در پنل فروشگاه داخل اپ نمایش داده می‌شوند و پرداخت ریالی است.',
      'faq.q3': 'چه زبان‌هایی می‌توانم یاد بگیرم؟',
      'faq.a3': 'انگلیسی، اسپانیایی، فرانسوی، آلمانی، ترکی و عربی. زبان مقصد را در اولین ورود انتخاب می‌کنی و هر وقت خواستی از تنظیمات یا صفحه اصلی تغییرش می‌دهی.',
      'faq.q4': 'مکالمه با هوش مصنوعی چطور کار می‌کند؟',
      'faq.a4': 'برای مکالمه و دریافت بازخورد به اینترنت نیاز داری و باید سرویس هوش مصنوعی سازگار را در تنظیمات اپ متصل کنی. هزینه و محدودیت استفاده به سرویس انتخابی‌ات بستگی دارد؛ همراه دانلود اپ اعتبار رایگان تعلق نمی‌گیرد.',
      'faq.q5': 'اطلاعات من کجا ذخیره می‌شود؟',
      'faq.a5': 'تاریخچه یادگیری و پیشرفتت روی دستگاه خودت ذخیره می‌شود. برای دریافت پاسخ و بازخورد، متن مکالمه به سرویس هوش مصنوعی انتخابی‌ات ارسال می‌شود؛ نحوه استفاده و نگهداری داده‌ها به سیاست‌های همان سرویس بستگی دارد.',
      'faq.q6': 'در چه سطحی باید باشم؟',
      'faq.a6': 'سطح خودت را انتخاب می‌کنی (مثلاً A1 برای مبتدی). این انتخاب فقط سطح تمرین‌ها را مشخص می‌کند؛ آپ‌ورد آزمون تعیین سطح خودکار برگزار نمی‌کند و مدرک زبان نمی‌دهد. بازخورد هوش مصنوعی هم ممکن است گاهی اشتباه باشد.',
      'faq.q7': 'یادآور تمرین چطور کار می‌کند؟',
      'faq.a7': 'در تنظیمات، ساعت دلخواه یادآور را انتخاب می‌کنی و آپ‌ورد همان‌وقت با نوتیفیکیشنی دوستانه یادت می‌اندازد. روی اندروید ۱۳ به بالا باید اجازه نوتیفیکیشن را به اپ بدهی تا یادآور کار کند.',

      'cta.title': 'اولین جمله‌ات را<br />همین امروز بگو.',
      'cta.subtitle': 'دانلود کن، موضوع رایگان را شروع کن و ببین یادگیری زبان چقدر می‌تواند لذت‌بخش باشد. لاک‌پشت آپ‌ورد کنارته — قدم‌به‌قدم و با حوصله.',
      'cta.bazaar': 'دانلود از کافه بازار',
      'cta.myket': 'دانلود از مایکت',
      'cta.note': 'اندروید ۸ به بالا · موضوع اول رایگان · پرداخت پرمیوم از داخل اپ',

      'footer.desc': 'همراه هوشمند فارسی‌زبان‌ها برای یادگیری زبان با مکالمه، درس و تمرین.',
      'footer.product': 'محصول',
      'footer.download': 'دانلود',
      'footer.about': 'درباره',
      'footer.android': 'اندروید ۸+',
      'footer.copyright': '© ۲۰۲۶ آپ‌ورد — تمامی حقوق محفوظ است.',
    },

    en: {
      'nav.skip': 'Skip to content',
      'nav.features': 'Features',
      'nav.journey': 'Learning path',
      'nav.preview': 'App preview',
      'nav.premium': 'Premium',
      'nav.reviews': 'Reviews',
      'nav.faq': 'FAQ',
      'nav.download': 'Download',

      'hero.pill': 'v2.85 · fresh glass design',
      'hero.title': 'From “hello” to<br /><span class="text-gradient">real conversations</span>',
      'hero.subtitle': 'UpWord is built for Persian speakers: short topic-based lessons, AI conversation practice, shadowing drills, and smart review — all in one beautifully glass-designed app.',
      'hero.ctaBazaar': 'Download from Cafe Bazaar',
      'hero.ctaMyket': 'Download from Myket',
      'hero.free': 'Free to start · first A1 topic with three lessons',
      'hero.chip1': '6 target languages',
      'hero.chip2': '3 lessons per topic',
      'hero.chip3': 'Android 8 and up',
      'hero.alt': 'Illustration: an UpWord learner greeting, with the UpWord turtle mascot',
      'hero.notifTitle': 'Practice reminder',
      'hero.notifBody': 'Time for today’s practice! 10 minutes is enough 🐢',
      'hero.notifNow': 'Start now',
      'hero.notifLater': 'Later',
      'hero.streakCard': '7-day streak',
      'hero.streakSub': 'Your practice chain is alive!',
      'hero.xpCard': '+80 XP',
      'hero.xpSub': 'Level 5 · great progress',
      'hero.caption': 'An illustrative glimpse of the UpWord experience',

      'mock.time': '9:41',
      'mock.notifTime': '8:00 PM',
      'mock.xpNum': '1,240',
      'mock.gemNum': '120',

      'languages.label': 'Pick your target language:',
      'languages.en': 'English',
      'languages.es': 'Spanish',
      'languages.fr': 'French',
      'languages.de': 'German',
      'languages.tr': 'Turkish',
      'languages.ar': 'Arabic',
      'languages.note': 'Chosen on first launch — and changeable anytime from settings or the home screen.',

      'journey.eyebrow': 'Your learning path',
      'journey.title': 'Four steps to your first conversation',
      'journey.subtitle': 'From first launch to fluent chats, UpWord walks with you step by step.',
      'journey.s1.title': 'Pick your language & level',
      'journey.s1.desc': 'On first launch you choose your target language and level — A1 beginner is the best starting point. Change it anytime in settings.',
      'journey.s2.title': 'Move through lessons step by step',
      'journey.s2.desc': 'Every topic — like “Hello & Introduction” — has three short lessons: words, useful phrases, and practice. Each lesson shows its progress in a circular ring.',
      'journey.s3.title': 'Practice conversation with AI',
      'journey.s3.desc': 'Put what you learned into real conversations — get replies, see your mistakes corrected, and learn better ways to say it.',
      'journey.s4.title': 'See your progress, keep going',
      'journey.s4.desc': 'XP, levels, gems, and achievements visualize your progress — and practice reminders keep your routine alive.',

      'features.eyebrow': 'Every feature, piece by piece',
      'features.title': 'Everything you need to learn, exactly where it belongs',
      'features.subtitle': 'UpWord isn’t just a chat app or a vocab app — it’s every learning tool, together and in sync.',

      'f1.eyebrow': 'Structured courses',
      'f1.title': 'Topic by topic, lesson by lesson',
      'f1.desc': 'Learning starts at A1 with practical everyday topics: “Hello & Introduction”, family, shopping and more. Each topic has three short lessons with progress rings — and the first topic is free for everyone, so you can start risk-free.',
      'f1.b1': 'Short 5–10 minute lessons',
      'f1.b2': 'Circular progress ring for every lesson',
      'f1.b3': 'First A1 topic completely free',
      'f1.b4': 'Words with pronunciation and examples',

      'courses.screenTitle': 'Lessons',
      'courses.topic': 'Hello & Introduction',
      'courses.free': 'Free',
      'courses.l1': 'Lesson 1 · Saying hello',
      'courses.done': 'Completed ✓',
      'courses.l2': 'Lesson 2 · Introducing yourself',
      'courses.current': 'In progress · 60%',
      'courses.l3': 'Lesson 3 · Asking questions',
      'courses.locked': 'Locked · finish the previous lesson',
      'courses.nextTopic': 'Family & Friends',
      'courses.premiumBadge': 'Premium',

      'f2.eyebrow': 'AI conversation',
      'f2.title': 'A partner who always has time',
      'f2.desc': 'Talk about real situations: ordering coffee, introducing yourself, sharing your day. Your sentences get feedback, you learn more natural phrasing, and your speaking confidence grows — by text or voice.',
      'f2.b1': 'Feedback and corrections on every sentence',
      'f2.b2': 'Real everyday situations',
      'f2.b3': 'Text and voice input',
      'f2.b4': 'No embarrassment — better every time',

      'chat.partner': 'Practice partner',
      'chat.online': 'Online',
      'chat.fbTitle': 'A quick note',
      'chat.fbBody': '“goed” isn’t right — the past of “go” is “went”: I went to the cafe.',
      'chat.placeholder': 'Type or speak…',

      'f3.eyebrow': 'Gamification',
      'f3.title': 'Motivation, refreshed every day',
      'f3.desc': 'A daily goal, XP and levels, gems, achievements, and streaks — together they turn practice into a habit you actually want to keep. The week calendar follows the Iranian week (Saturday to Friday) with checkmarks on your practice days.',
      'f3.b1': 'Daily goal and streak chain',
      'f3.b2': 'XP, levels, and gems',
      'f3.b3': 'Achievements and learning medals',
      'f3.b4': 'Smart practice reminders',

      'game.name': 'Sara',
      'game.level': 'Level 5 · Learner',
      'game.gemsVal': '💎 120',
      'game.xpLabel': 'Experience points (XP)',
      'game.xpVal': '720 / 1000',
      'game.streakVal': '🔥 7',
      'game.streak': 'day streak',
      'game.xpTotalVal': '⚡ 1,240',
      'game.xpTotal': 'Total XP',
      'game.trophyVal': '🏆 12',
      'game.trophies': 'Achievements',
      'game.weekTitle': 'This week',
      'game.ach1': 'First conversation',
      'game.ach2': '7-day streak',
      'game.ach3': '10 missions',

      'bento.eyebrow': 'The details that make the experience',
      'bento.title': 'One app, every tool',
      'b1.title': 'Shadowing practice',
      'b1.desc': 'Listen to a phrase, repeat along with it, and internalize the rhythm and pronunciation of the language.',
      'b2.title': 'Practice reminders',
      'b2.desc': 'A friendly notification at the hour you choose — your learning routine never breaks.',
      'b3.title': 'Glass design',
      'b3.desc': 'A modern UI with frosted-glass panels, smooth animations, and a calming green palette.',
      'b4.title': '6 target languages',
      'b4.desc': 'English, Spanish, French, German, Turkish, and Arabic — switchable anytime.',
      'b5.title': 'Text or voice',
      'b5.desc': 'Type with the keyboard or speak into the mic — start with whatever feels easier.',
      'b6.title': 'Your data stays yours',
      'b6.desc': 'Your learning history is stored on your device; it’s only sent to your chosen AI service to generate replies.',
      'b7.title': 'Built for Iran',
      'b7.desc': 'Rial payments via Cafe Bazaar and Myket, the Iranian week calendar, and a Persian-first experience.',
      'b8.title': 'Switch languages anytime',
      'b8.desc': 'From the home screen, switch your target language with one tap and start a new one.',

      'preview.eyebrow': 'App preview',
      'preview.title': 'A look inside UpWord',
      'preview.subtitle': 'From the home screen to conversations and achievements — these illustrative previews show the real feel of the app.',
      'preview.note': 'The screens above are illustrative examples, so you can feel the real app.',

      'home.greeting': 'Hi, Sara 👋',
      'home.sub': 'What shall we practice today?',
      'home.streakVal': '🔥 7',
      'home.goalTitle': 'Today’s goal',
      'home.goalPct': '60%',
      'home.goalSub': '30 of 50 XP',
      'home.mission': 'Today’s mission',
      'home.missionSub': 'Ordering at a café',
      'home.vocab': 'New vocabulary',
      'home.vocabSub': '12 words learned',

      'ach.title': 'Achievements',
      'ach.subtitle': 'New achievement!',
      'ach.name': '7-Day Streak',
      'ach.desc': 'A full week of practice!',
      'ach.xpVal': '+100 XP',
      'ach.a1': 'First conversation',
      'ach.a2': '7-day streak',
      'ach.a3': '10 missions',

      'vocab.title': 'Vocabulary',
      'vocab.progress': '12 of 20 words',
      'vocab.meaning': 'A happy, unexpected coincidence',
      'vocab.listen': 'Listen',
      'vocab.know': 'I know it!',

      'premium.eyebrow': 'Start free, upgrade anytime',
      'premium.title': 'Start simple. Go all-in when you love it.',
      'premium.subtitle': 'No credit card, no pressure — the first topic stays free forever.',
      'premium.badge': 'Most popular choice',
      'premium.free.title': 'Free',
      'premium.free.price': '0 Toman · forever',
      'premium.free.f1': 'First A1 topic: “Hello & Introduction” with 3 lessons',
      'premium.free.f2': 'Initial AI conversations',
      'premium.free.f3': 'Vocabulary and basic review',
      'premium.free.f4': 'Full gamification: XP, levels, achievements',
      'premium.free.cta': 'Download & start free',
      'premium.pro.title': 'Premium',
      'premium.pro.price': 'The whole path, unlocked',
      'premium.pro.f1': 'All A1 topics and higher levels',
      'premium.pro.f2': 'Unlimited AI conversations',
      'premium.pro.f3': 'Full shadowing practice',
      'premium.pro.f4': 'Advanced reminders and stats',
      'premium.pro.f5': 'Streak protection & progress support',
      'premium.tier1': 'Monthly',
      'premium.tier2': '6 months',
      'premium.tier3': 'Yearly · best choice',
      'premium.tier4': 'Lifetime',
      'premium.note': 'Prices are shown in the in-app payment screen based on the store panel (Cafe Bazaar / Myket). Payment is secure, in Rial, through the same store.',

      'testi.eyebrow': 'Learner stories',
      'testi.title': 'What UpWord users say',
      'testi.subtitle': 'A few real reviews from UpWord users on Cafe Bazaar. Visit the store page for the latest ratings.',
      'testi.r1.translation': '“Incredible and complete. Covers everything. The best part is finding pronunciation and everyday word usage in movie dialogues. Aweeesome.”',
      'testi.r1.role': 'Cafe Bazaar user',
      'testi.r2.translation': '“Really cool — a complete package of different tools that helps in every area.”',
      'testi.r2.role': 'Cafe Bazaar user',
      'testi.r3.translation': '“A very good and practical app with interesting features.”',
      'testi.r3.role': 'Cafe Bazaar user',
      'testi.summary': 'Curious what other learners think? Read the latest reviews and ratings on UpWord’s Cafe Bazaar page.',
      'testi.viewAll': 'View on Cafe Bazaar',

      'faq.eyebrow': 'FAQ',
      'faq.title': 'Everything you might ask',
      'faq.q1': 'How do I get started?',
      'faq.a1': 'Download from Cafe Bazaar or Myket, pick your target language and level on first launch, and start the free “Hello & Introduction” topic with three lessons — no payment needed.',
      'faq.q2': 'What is Premium and how do I buy it?',
      'faq.a2': 'Premium unlocks every topic, unlimited conversation, and the full feature set. Purchase happens inside the app, securely through Cafe Bazaar or Myket; prices are shown in the store panel inside the app and payment is in Rial.',
      'faq.q3': 'Which languages can I learn?',
      'faq.a3': 'English, Spanish, French, German, Turkish, and Arabic. You choose your target language on first launch and can change it anytime from settings or the home screen.',
      'faq.q4': 'How does the AI conversation work?',
      'faq.a4': 'Conversations and feedback need internet, and you connect a compatible AI service in the app’s settings. Usage costs and limits depend on your chosen provider; downloading the app does not include free AI credit.',
      'faq.q5': 'Where is my data stored?',
      'faq.a5': 'Your learning history and progress stay on your device. To generate replies and feedback, conversation text is sent to your chosen AI service; how that data is handled follows the provider’s own policies.',
      'faq.q6': 'What level should I be?',
      'faq.a6': 'You choose your own level (for example A1 for beginners). It only sets the difficulty of practice — UpWord doesn’t run an automatic placement test and doesn’t issue certificates. AI feedback can also be wrong sometimes.',
      'faq.q7': 'How do practice reminders work?',
      'faq.a7': 'In settings you pick your preferred reminder time, and UpWord sends a friendly notification at that hour. On Android 13 and above, you need to grant the notification permission for reminders to work.',

      'cta.title': 'Say your first sentence<br />today.',
      'cta.subtitle': 'Download, start the free topic, and see how enjoyable language learning can be. The UpWord turtle is with you — step by step, at your own pace.',
      'cta.bazaar': 'Download from Cafe Bazaar',
      'cta.myket': 'Download from Myket',
      'cta.note': 'Android 8+ · first topic free · premium purchase inside the app',

      'footer.desc': 'The smart companion for Persian speakers learning languages through conversation, lessons, and practice.',
      'footer.product': 'Product',
      'footer.download': 'Download',
      'footer.about': 'About',
      'footer.android': 'Android 8+',
      'footer.copyright': '© 2026 UpWord — All rights reserved.',
    }
  };

  /* ===== Language management ===== */
  const STORAGE_KEY = 'upword-lang';
  const SUPPORTED = ['en', 'fa'];
  const DEFAULT_LANG = 'fa';

  function getStoredLang() {
    try {
      const stored = localStorage.getItem(STORAGE_KEY);
      if (stored && SUPPORTED.includes(stored)) return stored;
    } catch (e) {}
    return DEFAULT_LANG;
  }

  function setStoredLang(lang) {
    try { localStorage.setItem(STORAGE_KEY, lang); } catch (e) {}
  }

  function applyLang(lang) {
    if (!SUPPORTED.includes(lang)) lang = DEFAULT_LANG;
    const dict = I18N[lang];
    const html = document.documentElement;

    html.lang = lang;
    html.dir = lang === 'fa' ? 'rtl' : 'ltr';

    // Plain-text translations
    document.querySelectorAll('[data-i18n]').forEach((el) => {
      const key = el.getAttribute('data-i18n');
      if (dict[key] !== undefined) {
        el.textContent = dict[key];
      }
    });

    // HTML-content translations (inline markup like <span>)
    document.querySelectorAll('[data-i18n-html]').forEach((el) => {
      const key = el.getAttribute('data-i18n-html');
      if (dict[key] !== undefined) {
        el.innerHTML = dict[key];
      }
    });

    // Alt-text translations
    document.querySelectorAll('[data-i18n-alt]').forEach((el) => {
      const key = el.getAttribute('data-i18n-alt');
      if (dict[key] !== undefined) {
        el.setAttribute('alt', dict[key]);
      }
    });

    // Language switcher UI
    const langCurrent = document.getElementById('langCurrent');
    if (langCurrent) langCurrent.textContent = lang === 'fa' ? 'فا' : 'EN';

    document.querySelectorAll('.lang-option').forEach((opt) => {
      opt.classList.toggle('active', opt.getAttribute('data-lang') === lang);
    });
  }

  /* ===== Language switcher wiring ===== */
  function initLangSwitcher() {
    const langBtn = document.getElementById('langBtn');
    const langDropdown = document.getElementById('langDropdown');
    if (!langBtn || !langDropdown) return;

    langBtn.setAttribute('aria-haspopup', 'true');
    langBtn.setAttribute('aria-expanded', 'false');

    function openDropdown() {
      langDropdown.classList.add('open');
      langBtn.setAttribute('aria-expanded', 'true');
    }
    function closeDropdown() {
      langDropdown.classList.remove('open');
      langBtn.setAttribute('aria-expanded', 'false');
    }
    function toggleDropdown() {
      if (langDropdown.classList.contains('open')) closeDropdown();
      else openDropdown();
    }

    langBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      toggleDropdown();
    });
    langBtn.addEventListener('touchstart', (e) => {
      e.stopPropagation();
    }, { passive: true });

    document.addEventListener('click', (e) => {
      if (!langDropdown.contains(e.target) && !langBtn.contains(e.target)) {
        closeDropdown();
      }
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && langDropdown.classList.contains('open')) {
        closeDropdown();
        langBtn.focus();
      }
    });

    document.querySelectorAll('.lang-option').forEach((opt) => {
      const handler = (e) => {
        e.preventDefault();
        e.stopPropagation();
        const newLang = opt.getAttribute('data-lang');
        if (!SUPPORTED.includes(newLang)) return;
        setStoredLang(newLang);
        applyLang(newLang);
        closeDropdown();
        langBtn.focus();
      };
      opt.addEventListener('click', handler);
      opt.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') handler(e);
      });
    });
  }

  /* ===== Scroll progress bar ===== */
  const progressBar = document.getElementById('scrollProgress');
  function updateScrollProgress() {
    if (!progressBar) return;
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const pct = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
    progressBar.style.transform = 'scaleX(' + Math.min(1, Math.max(0, pct / 100)) + ')';
  }

  /* ===== Navbar scrolled state ===== */
  const navbar = document.getElementById('navbar');
  function updateNavbar() {
    if (!navbar) return;
    if (window.scrollY > 20) navbar.classList.add('scrolled');
    else navbar.classList.remove('scrolled');
  }

  let scrollFrame = 0;
  function onScroll() {
    if (scrollFrame) return;
    scrollFrame = requestAnimationFrame(() => {
      updateScrollProgress();
      updateNavbar();
      scrollFrame = 0;
    });
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll);

  /* ===== Mobile nav toggle ===== */
  const navToggle = document.getElementById('navToggle');
  const navLinks = document.getElementById('navLinks');
  if (navToggle && navLinks) {
    navToggle.addEventListener('click', () => {
      navToggle.classList.toggle('active');
      navLinks.classList.toggle('open');
      navToggle.setAttribute('aria-expanded', String(navLinks.classList.contains('open')));
    });
    navLinks.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', () => {
        navToggle.classList.remove('active');
        navLinks.classList.remove('open');
        navToggle.setAttribute('aria-expanded', 'false');
      });
    });
    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape' && navLinks.classList.contains('open')) {
        navLinks.classList.remove('open');
        navToggle.classList.remove('active');
        navToggle.setAttribute('aria-expanded', 'false');
        navToggle.focus();
      }
    });
  }

  /* ===== Reveal on scroll ===== */
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const activeReveals = new Map();
  const motionTokens = getComputedStyle(document.documentElement);
  const revealDuration = parseFloat(motionTokens.getPropertyValue('--t-reveal')) || 650;
  const revealEasing = 'cubic-bezier(0.16, 1, 0.3, 1)';
  const revealDistance = '26px';

  if ('IntersectionObserver' in window && 'animate' in Element.prototype) {
    const revealEls = document.querySelectorAll(
      '.hero-content > *, .hero-visual, .lang-strip .container > *, .section-head, .journey-step, .feature-row > *, .bcard, .preview-phone, .preview-note, .plan, .review, .faq-item, .cta-card, .footer-grid > *'
    );
    const io = new IntersectionObserver((entries) => {
      entries.filter((entry) => entry.isIntersecting).forEach((entry, index) => {
        io.unobserve(entry.target);
        if (reducedMotion.matches || entry.target.contains(document.activeElement)) return;
        const animation = entry.target.animate([
          { opacity: 0, transform: 'translateY(' + revealDistance + ')' },
          { opacity: 1, transform: 'translateY(0)' },
        ], {
          duration: revealDuration,
          delay: (index % 3) * 75,
          easing: revealEasing,
          fill: 'backwards',
        });
        activeReveals.set(entry.target, animation);
        animation.onfinish = animation.oncancel = () => activeReveals.delete(entry.target);
      });
    }, { threshold: 0.08 });
    revealEls.forEach((el) => io.observe(el));
  }

  document.addEventListener('focusin', (event) => {
    activeReveals.forEach((animation, el) => {
      if (el.contains(event.target)) animation.cancel();
    });
  });
  if (reducedMotion.addEventListener) {
    reducedMotion.addEventListener('change', () => {
      if (reducedMotion.matches) activeReveals.forEach((animation) => animation.cancel());
    });
  }

  /* ===== Lottie animations ===== */
  const turtleStates = new Map();
  function syncTurtle(state) {
    if (!state.ready) return;
    if (reducedMotion.matches) {
      state.animation.goToAndStop(Math.round(state.animation.totalFrames * 0.4), true);
      state.started = false;
    } else if (!state.visible || document.hidden || state.completed) {
      state.animation.pause();
    } else if (!state.started) {
      state.started = true;
      state.animation.goToAndPlay(0, true);
    } else {
      state.animation.play();
    }
  }
  const turtleObserver = 'IntersectionObserver' in window ? new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      const state = turtleStates.get(entry.target);
      if (!state) return;
      state.visible = entry.isIntersecting;
      syncTurtle(state);
    });
  }, { threshold: 0.15 }) : null;
  document.addEventListener('visibilitychange', () => turtleStates.forEach(syncTurtle));
  if (reducedMotion.addEventListener) {
    reducedMotion.addEventListener('change', () => turtleStates.forEach(syncTurtle));
  }

  function loadLottie(containerId, path) {
    const el = document.getElementById(containerId);
    if (!el || typeof lottie === 'undefined') return;
    const animation = lottie.loadAnimation({
      container: el,
      renderer: 'svg',
      loop: false,
      autoplay: false,
      path: path,
      rendererSettings: { preserveAspectRatio: 'xMidYMid meet' },
    });
    const state = { animation, ready: false, visible: false, started: false, completed: false };
    turtleStates.set(el, state);
    animation.addEventListener('DOMLoaded', () => {
      state.ready = true;
      animation.goToAndStop(Math.round(animation.totalFrames * 0.4), true);
      if (turtleObserver) turtleObserver.observe(el);
      syncTurtle(state);
    });
    animation.addEventListener('complete', () => { state.completed = true; });
  }

  loadLottie('journeyTurtle', 'assets/lottie/turtle-swimming.json');
  loadLottie('achTurtle', 'assets/lottie/turtle-success.json');
  loadLottie('ctaTurtle', 'assets/lottie/turtle-meditation.json');

  /* ===== Smooth scroll for anchor links (with navbar offset) ===== */
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener('click', (e) => {
      const href = anchor.getAttribute('href');
      if (href === '#' || href === '#!') return;
      const target = document.querySelector(href);
      if (!target) return;
      e.preventDefault();
      const offset = navbar ? navbar.offsetHeight : 0;
      const top = target.getBoundingClientRect().top + window.scrollY - offset;
      window.scrollTo({
        top,
        behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth',
      });
      if (target.id === 'main') target.focus({ preventScroll: true });
    });
  });

  /* ===== FAQ: only one open at a time ===== */
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach((item) => {
    item.addEventListener('toggle', () => {
      if (item.open) {
        faqItems.forEach((other) => {
          if (other !== item) other.open = false;
        });
      }
    });
  });

  /* ===== Initial render ===== */
  applyLang(getStoredLang());
  initLangSwitcher();
  updateScrollProgress();
  updateNavbar();
})();

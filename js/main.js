/* ============================================
   Upword Landing — Main JavaScript
   Bilingual (English default + Persian toggle)
   ============================================ */

(function () {
  'use strict';

  /* ===== i18n dictionary ===== */
  const I18N = {
    en: {
      'nav.features': 'Features',
      'nav.how': 'How it Works',
      'nav.screens': 'App Preview',
      'nav.testimonials': 'Reviews',
      'nav.faq': 'FAQ',
      'nav.download': 'Download',

      'hero.pill': 'v2.45.7 released — with new turtle animations',
      'hero.title': 'Learn a language through <span class="text-gradient">real conversation</span>',
      'hero.subtitle': 'No memorization, no boring tests — real conversation with an AI assistant, interactive missions, and shadowing practice. Learn how to actually speak, not just memorize words.',
      'hero.ctaPrimary': 'Download from Cafe Bazaar',
      'hero.ctaSecondary': 'How it works?',

      'stats.languages': 'Languages',
      'stats.topics': 'Conversation Topics',
      'stats.rating': 'User Rating',
      'stats.votes': 'Verified Reviews',

      'badge.streak': '7 days',

      'trust.privacy': 'Your privacy respected',
      'trust.ai': 'Advanced AI',
      'trust.android': 'Android 8+',
      'trust.free': 'Free to start',

      'features.eyebrow': 'Why Upword?',
      'features.title': 'Everything for real language learning',
      'features.subtitle': "Upword isn't just an educational app — it's your complete companion on the language-learning journey. From your first word to fluent conversation, all in one place.",
      'features.f1.title': 'Real AI Conversation',
      'features.f1.desc': 'Chat with a smart assistant that adapts to your level. Everyday topics like travel, restaurants, work, and health — without fear of making mistakes.',
      'features.f2.title': 'Interactive Missions',
      'features.f2.desc': 'Role-play in real scenarios: job interviews, hotel bookings, doctor visits. Each mission is a step toward speaking more fluently.',
      'features.f3.title': 'Shadowing Practice',
      'features.f3.desc': 'Listen and repeat. Refine your pronunciation with targeted exercises and build the confidence to actually speak.',
      'features.f4.title': 'Smart Vocabulary',
      'features.f4.desc': 'Learn new words in context, not as a dry list. Each word sticks with real examples and native pronunciation.',
      'features.f5.title': 'XP & Streak System',
      'features.f5.desc': 'Earn XP with every exercise, keep your daily streak alive, and level up. Learning becomes a rewarding habit.',
      'features.f6.title': 'Personalized Path',
      'features.f6.desc': 'From complete beginner to advanced, the learning path is tuned to your progress. Every user gets a unique experience.',

      'how.eyebrow': 'How it works',
      'how.title': 'Start in three steps',
      'how.subtitle': 'From install to your first real conversation, less than 5 minutes away.',
      'how.s1.title': 'Pick your language and level',
      'how.s1.desc': 'Choose your native language, target language, and current level to build your personal path.',
      'how.s2.title': 'Start your first conversation',
      'how.s2.desc': 'Pick a topic and start chatting with the AI assistant. It corrects your mistakes in real time.',
      'how.s3.title': 'Practice daily and progress',
      'how.s3.desc': 'With daily goals, streaks, and new missions, learning becomes a delightful habit.',

      'mascot.eyebrow': 'The Upword Turtle',
      'mascot.title': 'Your companion on the journey',
      'mascot.desc': 'The turtle symbolizes patience and persistence — exactly what you need to learn a language. It\'s with you at every step: it celebrates when you succeed, motivates you when you\'re tired, and brings calm when you complete your goal.',
      'mascot.l1': 'Encouragement at every small win',
      'mascot.l2': 'Lively, delightful animations',
      'mascot.l3': 'A sense of companionship throughout',
      'mascot.l4': 'A symbol of patience and persistence',
      'mascot.cta': 'Get started now',

      'screens.eyebrow': 'App Preview',
      'screens.title': 'A look inside Upword',
      'screens.subtitle': 'A simple, elegant, and Persian UI — so you focus on learning, not the software.',

      'screen.chat.title': 'Free Talk',
      'screen.chat.feedback': 'Great! Your sentence was natural.',
      'screen.ach.title': 'Achievements',
      'screen.ach.subtitle': 'New Achievement!',
      'screen.ach.name': '7-Day Streak',
      'screen.ach.desc': 'A full week of practice!',
      'screen.ach.a1': 'First Conversation',
      'screen.ach.a2': '7-Day Streak',
      'screen.ach.a3': '10 Missions',
      'screen.vocab.title': 'Vocabulary',
      'screen.vocab.progress': '12 of 20 words',
      'screen.vocab.meaning': 'A lucky coincidence',
      'screen.vocab.listen': '🔊 Listen',
      'screen.vocab.know': 'I know it',

      'mock.greeting': 'Hi Ali 👋',
      'mock.greetingSub': "Let's learn today!",
      'mock.dailyGoal': 'Daily Goal',
      'mock.dailyGoalMeta': '30 of 50 XP',
      'mock.todaysMission': "Today's Mission",
      'mock.todaysMissionMeta': 'Ordering food at a restaurant',
      'mock.newVocab': 'New Vocabulary',
      'mock.newVocabMeta': '12 words learned',

      'testi.eyebrow': 'User Reviews',
      'testi.title': 'What Upword users say',
      'testi.subtitle': 'Real reviews from Cafe Bazaar — verbatim, untranslated. Average rating: 4.7 out of 5 from 13 votes.',
      'testi.r1.translation': '"Incredible and complete. Covers everything. The best part is finding pronunciation and the routine use of words in movie dialogues. Aweeesome."',
      'testi.r1.role': 'Cafe Bazaar User',
      'testi.r2.translation': '"Really cool — a complete package of different tools that helps in every area."',
      'testi.r2.role': 'Cafe Bazaar User',
      'testi.r3.translation': '"A very good and practical app with interesting features."',
      'testi.r3.role': 'Cafe Bazaar User',
      'testi.summary': 'Based on 13 verified votes on Cafe Bazaar — Upword maintains an excellent 4.7/5 rating. Join the growing community of happy learners.',
      'testi.viewAll': 'View on Cafe Bazaar',

      'faq.eyebrow': 'FAQ',
      'faq.title': 'Everything you want to know',
      'faq.q1': 'Is Upword free?',
      'faq.a1': 'Downloading and starting Upword is free. You can try daily conversations, missions, and shadowing practice. For access to advanced content, special missions, and more languages, you can make in-app purchases.',
      'faq.q2': 'Do I need internet to use it?',
      'faq.a2': 'AI conversations require internet. However, you can review learned vocabulary and shadowing exercises offline.',
      'faq.q3': 'Which languages are supported?',
      'faq.a3': 'Currently English, Turkish, Arabic, German, French, and Spanish are supported. More languages are on the way.',
      'faq.q4': 'Is my data secure?',
      'faq.a4': 'Yes. All your learning data is stored locally on your device. Conversations are only sent to the AI service for processing and are not retained.',
      'faq.q5': 'What level do I need?',
      'faq.a5': 'No specific level needed. Upword supports complete beginners to advanced learners. At the start, your level is detected and your path is personalized.',

      'cta.title': 'Take your first step today',
      'cta.subtitle': "Language learning doesn't happen overnight — but with Upword, you take a step closer to your goal every day. Start now.",
      'cta.button': 'Download from Cafe Bazaar',
      'cta.note': 'Free to start • In-app purchases for full content • v2.45.7',

      'footer.desc': 'Your smart companion for learning languages through real conversation. Built with love in Iran.',
      'footer.product': 'Product',
      'footer.download': 'Download',
      'footer.about': 'About',
      'footer.android': 'Android',
      'footer.aboutApp': 'About Upword',
      'footer.copyright': '© 2026 Upword — All rights reserved.',
    },

    fa: {
      'nav.features': 'امکانات',
      'nav.how': 'چطور کار می‌کند',
      'nav.screens': 'نمای اپ',
      'nav.testimonials': 'نظرات',
      'nav.faq': 'سوالات',
      'nav.download': 'دانلود',

      'hero.pill': 'نسخه ۲.۴۵.۷ منتشر شد — با انیمیشن‌های لاکپشت جدید',
      'hero.title': 'زبان را با <span class="text-gradient">مکالمه واقعی</span> یاد بگیر',
      'hero.subtitle': 'نه حفظ کردن، نه تست‌های خسته‌کننده — مکالمه واقعی با دستیار هوش مصنوعی، ماموریت‌های تعاملی و تمرین شدوینگ. یاد بگیر چطور واقعاً صحبت کنی، نه فقط کلمات را حفظ کنی.',
      'hero.ctaPrimary': 'دانلود از کافه بازار',
      'hero.ctaSecondary': 'چطور کار می‌کند؟',

      'stats.languages': 'زبان قابل یادگیری',
      'stats.topics': 'موضوع مکالمه',
      'stats.rating': 'امتیاز کاربران',
      'stats.votes': 'نظرات تأییدشده',

      'badge.streak': '۷ روز',

      'trust.privacy': 'حریم خصوصی شما محترم است',
      'trust.ai': 'هوش مصنوعی پیشرفته',
      'trust.android': 'اندروید ۸ به بالا',
      'trust.free': 'شروع رایگان',

      'features.eyebrow': 'چرا آپ ورد؟',
      'features.title': 'همه‌چیز برای یادگیری واقعی زبان',
      'features.subtitle': 'آپ ورد یک اپلیکیشن آموزشی نیست؛ همراه کامل تو در سفر زبان‌آموزی است. از اولین کلمه تا مکالمه روان، همه‌چیز در یک جا.',
      'features.f1.title': 'مکالمه واقعی با هوش مصنوعی',
      'features.f1.desc': 'با دستیار هوشمندی چت کن که خودش را به سطح تو سازگار می‌کند. موضوعات روزمره مثل سفر، رستوران، کار و سلامت — بدون ترس از اشتباه کردن.',
      'features.f2.title': 'ماموریت‌های تعاملی',
      'features.f2.desc': 'در سناریوهای واقعی نقش بازی کن: مصاحبه شغلی، رزرو هتل، ویزیت پزشک. هر ماموریت یک قدم به سمت روان‌تر صحبت کردن است.',
      'features.f3.title': 'تمرین شدوینگ',
      'features.f3.desc': 'گوش بده و تکرار کن. تلفظت را با تمرین‌های هدفمند اصلاح کن و اعتماد به نفس صحبت کردن را در خودت بساز.',
      'features.f4.title': 'واژگان هوشمند',
      'features.f4.desc': 'کلمات جدید را در زمینه یاد بگیر، نه به صورت لیست خشک. هر واژه با مثال واقعی و تلفظ بومی، در حافظه‌ات می‌ماند.',
      'features.f5.title': 'سیستم XP و استریک',
      'features.f5.desc': 'با هر تمرین امتیاز بگیر، استریک روزانه‌ات را حفظ کن و در سطح‌ها بالا برو. یادگیری تبدیل به عادت لذت‌بخش می‌شود.',
      'features.f6.title': 'مسیر شخصی‌سازی‌شده',
      'features.f6.desc': 'از سطح مبتدی تا پیشرفته، مسیر یادگیری بر اساس پیشرفت تو تنظیم می‌شود. هر کاربر تجربه‌ای منحصربه‌فرد دارد.',

      'how.eyebrow': 'چطور کار می‌کند',
      'how.title': 'در سه قدم شروع کن',
      'how.subtitle': 'از نصب تا اولین مکالمه واقعی، کمتر از ۵ دقیقه فاصله داری.',
      'how.s1.title': 'زبان و سطحت را انتخاب کن',
      'how.s1.desc': 'زبان مادری، زبان هدف و سطح فعلی‌ات را مشخص کن تا مسیر شخصی تو ساخته شود.',
      'how.s2.title': 'اولین مکالمه را شروع کن',
      'how.s2.desc': 'یک موضوع انتخاب کن و با دستیار هوشمند شروع به چت کن. اشتباهاتت را همان لحظه اصلاح می‌کند.',
      'how.s3.title': 'هر روز تمرین کن و پیشرفت کن',
      'how.s3.desc': 'با هدف روزانه، استریک و ماموریت‌های جدید، یادگیری به عادت لذت‌بخش تبدیل می‌شود.',

      'mascot.eyebrow': 'لاکپشت آپ ورد',
      'mascot.title': 'همراهت در مسیر یادگیری',
      'mascot.desc': 'لاکپشت نماد صبر و استمرار است — همان چیزی که برای یادگیری زبان نیاز داری. در هر قدم کنارت است: وقتی موفق می‌شوی جشن می‌گیرد، وقتی خسته می‌شوی بهت انگیزه می‌دهد و وقتی هدفت را کامل می‌کنی آرامش می‌بخشد.',
      'mascot.l1': 'تشویق در هر موفقیت کوچک',
      'mascot.l2': 'انیمیشن‌های زنده و دلپذیر',
      'mascot.l3': 'حس همراهی در کل مسیر یادگیری',
      'mascot.l4': 'نماد صبر و استمرار در یادگیری',
      'mascot.cta': 'همین حالا شروع کن',

      'screens.eyebrow': 'نمای اپلیکیشن',
      'screens.title': 'نگاهی به داخل آپ ورد',
      'screens.subtitle': 'رابط کاربری ساده، شیک و فارسی — برای اینکه روی یادگیری تمرکز کنی، نه نرم‌افزار را.',

      'screen.chat.title': 'مکالمه آزاد',
      'screen.chat.feedback': 'عالی! جمله‌ات طبیعی بود.',
      'screen.ach.title': 'دستاوردها',
      'screen.ach.subtitle': 'دستاورد جدید!',
      'screen.ach.name': '۷ روز استریک',
      'screen.ach.desc': 'یک هفته کامل تمرین کردی!',
      'screen.ach.a1': 'اولین مکالمه',
      'screen.ach.a2': 'استریک ۷ روزه',
      'screen.ach.a3': '۱۰ ماموریت',
      'screen.vocab.title': 'واژگان',
      'screen.vocab.progress': '۱۲ از ۲۰ واژه',
      'screen.vocab.meaning': 'تصادف خوش',
      'screen.vocab.listen': '🔊 گوش بده',
      'screen.vocab.know': 'می‌دانم',

      'mock.greeting': 'سلام علی 👋',
      'mock.greetingSub': 'بریم امروز یاد بگیریم!',
      'mock.dailyGoal': 'هدف روزانه',
      'mock.dailyGoalMeta': '۳۰ از ۵۰ XP',
      'mock.todaysMission': 'ماموریت امروز',
      'mock.todaysMissionMeta': 'سفارش غذا در رستوران',
      'mock.newVocab': 'واژگان جدید',
      'mock.newVocabMeta': '۱۲ واژه آموختی',

      'testi.eyebrow': 'نظرات کاربران',
      'testi.title': 'کاربران آپ ورد چه می‌گویند؟',
      'testi.subtitle': 'نظرات واقعی از کافه بازار — عین کلمه‌شون، بدون ترجمه. میانگین امتیاز: ۴.۷ از ۵ از ۱۳ رأی.',
      'testi.r1.translation': '«بی‌نظیر و کامل. همه‌چیز را پوشش می‌دهد. بهترین قسمتش پیدا کردن تلفظ و استفاده روتین کلمه در دیالوگ فیلم‌هاست. عاااالیه.»',
      'testi.r1.role': 'کاربر کافه بازار',
      'testi.r2.translation': '«خیلی باحاله — یک پکیج کامل از ابزارهای مختلف که در همه زمینه‌ها کمک می‌کند.»',
      'testi.r2.role': 'کاربر کافه بازار',
      'testi.r3.translation': '«برنامه خیلی خوب و کاربردی است و امکانات جالبی دارد.»',
      'testi.r3.role': 'کاربر کافه بازار',
      'testi.summary': 'بر اساس ۱۳ رأی تأییدشده در کافه بازار — آپ ورد امتیاز عالی ۴.۷ از ۵ را حفظ کرده. به جمع زبان‌آموزان راضی بپیوند.',
      'testi.viewAll': 'مشاهده در کافه بازار',

      'faq.eyebrow': 'سوالات متداول',
      'faq.title': 'هر چی می‌خوای بدونی',
      'faq.q1': 'آیا آپ ورد رایگان است؟',
      'faq.a1': 'دانلود و شروع آپ ورد رایگان است. می‌توانید مکالمات روزانه، ماموریت‌ها و تمرین شدوینگ را امتحان کنید. برای دسترسی به محتوای پیشرفته‌تر، ماموریت‌های ویژه و زبان‌های بیشتر، می‌توانید خرید درون‌برنامه‌ای انجام دهید.',
      'faq.q2': 'آیا برای استفاده به اینترنت نیاز دارم؟',
      'faq.a2': 'برای مکالمه با هوش مصنوعی به اینترنت نیاز دارید. اما واژگان آموخته‌شده و تمرین‌های شدوینگ را می‌توانید به صورت آفلاین مرور کنید.',
      'faq.q3': 'چه زبان‌هایی پشتیبانی می‌شوند؟',
      'faq.a3': 'در حال حاضر انگلیسی، ترکی، عربی، آلمانی، فرانسوی و اسپانیایی پشتیبانی می‌شوند. زبان‌های بیشتری در راه است.',
      'faq.q4': 'آیا داده‌های من امن هستند؟',
      'faq.a4': 'بله. تمام داده‌های یادگیری شما به صورت محلی روی دستگاه ذخیره می‌شود. مکالمات فقط برای پردازش به سرویس هوش مصنوعی ارسال می‌شوند و نگه‌داری نمی‌شوند.',
      'faq.q5': 'چه سطحی از زبان را نیاز دارم؟',
      'faq.a5': 'هیچ سطح خاصی لازم نیست. آپ ورد از مبتدی کامل تا پیشرفته پشتیبانی می‌کند. در شروع، سطح تو شناسایی می‌شود و مسیر شخصی‌سازی می‌شود.',

      'cta.title': 'امروز اولین قدم رو بردار',
      'cta.subtitle': 'یادگیری زبان یک‌شبه اتفاق نمی‌افتد — اما با آپ ورد، هر روز یک قدم به هدفت نزدیک‌تر می‌شوی. همین حالا شروع کن.',
      'cta.button': 'دانلود از کافه بازار',
      'cta.note': 'شروع رایگان • خرید درون‌برنامه‌ای برای محتوای کامل • نسخه ۲.۴۵.۷',

      'footer.desc': 'همراه هوشمندت برای یادگیری زبان از طریق مکالمه واقعی. ساخته‌شده با عشق در ایران.',
      'footer.product': 'محصول',
      'footer.download': 'دانلود',
      'footer.about': 'درباره',
      'footer.android': 'اندروید',
      'footer.aboutApp': 'درباره آپ ورد',
      'footer.copyright': '© ۲۰۲۶ آپ ورد — تمام حقوق محفوظ است.',
    }
  };

  /* ===== Persian numeral conversion ===== */
  function toPersianDigits(num) {
    const persian = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹'];
    return String(num).replace(/\d/g, (d) => persian[d]);
  }
  function toEnglishDigits(num) {
    return String(num).replace(/[۰-۹]/g, (d) => '۰۱۲۳۴۵۶۷۸۹'.indexOf(d));
  }

  /* ===== Language management ===== */
  const STORAGE_KEY = 'upword-lang';
  const SUPPORTED = ['en', 'fa'];

  function getStoredLang() {
    try {
      const stored = localStorage.getItem(STORAGE_KEY);
      if (stored && SUPPORTED.includes(stored)) return stored;
    } catch (e) {}
    return 'en'; // default to English
  }

  function setStoredLang(lang) {
    try { localStorage.setItem(STORAGE_KEY, lang); } catch (e) {}
  }

  function applyLang(lang) {
    if (!SUPPORTED.includes(lang)) lang = 'en';
    const dict = I18N[lang];
    const html = document.documentElement;

    html.lang = lang;
    html.dir = lang === 'fa' ? 'rtl' : 'ltr';

    // Apply translations
    document.querySelectorAll('[data-i18n]').forEach((el) => {
      const key = el.getAttribute('data-i18n');
      if (dict[key] !== undefined) {
        el.textContent = dict[key];
      }
    });

    // HTML-content translations (allow inline markup like <span>)
    document.querySelectorAll('[data-i18n-html]').forEach((el) => {
      const key = el.getAttribute('data-i18n-html');
      if (dict[key] !== undefined) {
        el.innerHTML = dict[key];
      }
    });

    // Update lang switcher UI
    const langCurrent = document.getElementById('langCurrent');
    if (langCurrent) langCurrent.textContent = lang.toUpperCase();

    document.querySelectorAll('.lang-option').forEach((opt) => {
      opt.classList.toggle('active', opt.getAttribute('data-lang') === lang);
    });

    // Re-render counters for the new digit system
    recountStats(lang);
  }

  function recountStats(lang) {
    // Reset and re-animate counters with the appropriate digit system
    document.querySelectorAll('[data-count]').forEach((el) => {
      const target = parseFloat(el.getAttribute('data-count'));
      const suffix = el.getAttribute('data-suffix') || '';
      if (lang === 'fa') {
        el.textContent = toPersianDigits(target) + suffix;
      } else {
        el.textContent = target + suffix;
      }
    });
  }

  /* ===== Language switcher wiring ===== */
  function initLangSwitcher() {
    const langBtn = document.getElementById('langBtn');
    const langDropdown = document.getElementById('langDropdown');
    if (!langBtn || !langDropdown) return;

    // ARIA + keyboard accessibility
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

    // Click on the button — toggle the dropdown
    langBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      toggleDropdown();
    });

    // Touchstart — make sure mobile devices get the event reliably
    langBtn.addEventListener('touchstart', (e) => {
      e.stopPropagation();
    }, { passive: true });

    // Click outside — close dropdown
    document.addEventListener('click', (e) => {
      if (!langDropdown.contains(e.target) && !langBtn.contains(e.target)) {
        closeDropdown();
      }
    });

    // Escape key — close dropdown and return focus to the button
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && langDropdown.classList.contains('open')) {
        closeDropdown();
        langBtn.focus();
      }
    });

    // Wire up each language option
    document.querySelectorAll('.lang-option').forEach((opt) => {
      const handler = (e) => {
        e.preventDefault();
        e.stopPropagation();
        const newLang = opt.getAttribute('data-lang');
        if (!SUPPORTED.includes(newLang)) return;
        setStoredLang(newLang);
        applyLang(newLang);
        closeDropdown();
      };
      opt.addEventListener('click', handler);
      // Keyboard support: Enter / Space already fire 'click' on <button>, but be defensive
      opt.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') handler(e);
      });
    });
  }

  /* ===== Scroll progress bar ===== */
  const progressBar = document.getElementById('scrollProgress');
  function updateScrollProgress() {
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const pct = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
    progressBar.style.width = pct + '%';
  }

  /* ===== Navbar scrolled state ===== */
  const navbar = document.getElementById('navbar');
  function updateNavbar() {
    if (window.scrollY > 20) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  }

  function onScroll() {
    updateScrollProgress();
    updateNavbar();
  }
  window.addEventListener('scroll', onScroll, { passive: true });

  /* ===== Mobile nav toggle ===== */
  const navToggle = document.getElementById('navToggle');
  const navLinks = document.getElementById('navLinks');
  navToggle.addEventListener('click', () => {
    navToggle.classList.toggle('active');
    navLinks.classList.toggle('open');
  });
  navLinks.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      navToggle.classList.remove('active');
      navLinks.classList.remove('open');
    });
  });

  /* ===== Reveal on scroll ===== */
  const revealEls = document.querySelectorAll(
    '.feature-card, .step, .testimonial, .faq-item, .screen-mockup, .mascot-content, .mascot-visual, .section-head, .stats-row > *'
  );
  revealEls.forEach((el, i) => {
    el.classList.add('reveal');
    el.setAttribute('data-delay', String((i % 4) + 1));
  });

  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('in');
          io.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12, rootMargin: '0px 0px -50px 0px' }
  );
  revealEls.forEach((el) => io.observe(el));

  /* ===== Number counter animation ===== */
  // Disabled for now — values are set directly by applyLang() to handle digit locale.
  // Original animation logic kept for reference but bypassed to avoid double-render.
  const counters = document.querySelectorAll('[data-count]');
  // counters not animated — applyLang sets final value with correct digit system.

  /* ===== Lottie animations ===== */
  function loadLottie(containerId, path, opts) {
    const el = document.getElementById(containerId);
    if (!el || typeof lottie === 'undefined') return;
    lottie.loadAnimation({
      container: el,
      renderer: 'svg',
      loop: opts && opts.loop !== undefined ? opts.loop : true,
      autoplay: opts && opts.autoplay !== undefined ? opts.autoplay : true,
      path: path,
      rendererSettings: { preserveAspectRatio: 'xMidYMid meet' },
    });
  }

  loadLottie('heroTurtle1', 'assets/lottie/turtle-swimming.json');
  loadLottie('heroTurtle2', 'assets/lottie/turtle-water.json');
  loadLottie('stepTurtle1', 'assets/lottie/turtle-show.json');
  loadLottie('stepTurtle2', 'assets/lottie/turtle-success.json');
  loadLottie('stepTurtle3', 'assets/lottie/turtle-progress.json');
  loadLottie('mascotTurtle', 'assets/lottie/turtle-ninja.json');
  loadLottie('achievementTurtle', 'assets/lottie/turtle-success.json', { loop: true });
  loadLottie('ctaTurtle', 'assets/lottie/turtle-meditation.json');

  /* ===== Smooth scroll for anchor links (with navbar offset) ===== */
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener('click', (e) => {
      const href = anchor.getAttribute('href');
      if (href === '#' || href === '#!') return;
      const target = document.querySelector(href);
      if (!target) return;
      e.preventDefault();
      const offset = 72;
      const top = target.getBoundingClientRect().top + window.scrollY - offset;
      window.scrollTo({ top, behavior: 'smooth' });
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
  const initialLang = getStoredLang();
  applyLang(initialLang);
  initLangSwitcher();
  updateScrollProgress();
  updateNavbar();
})();

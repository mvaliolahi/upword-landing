/* ============================================
   UpWord Landing — Main JavaScript
   Bilingual (English default + Persian toggle)
   ============================================ */

(function () {
  'use strict';

  /* ===== i18n dictionary ===== */
  const I18N = {
    en: {
      "loop.repeat": "Revisit useful phrases",

      "loop.learn": "Learn from feedback",

      "loop.speak": "Practice a situation",

      "practice.note": "This is a fixed teaching example, not generated feedback or a live app session.",

      "practice.reveal": "Show the correction and try again",

      "practice.label": "Worked example · English · past tense",

      "practice.desc": "Feedback is most useful when you can do something with it. Here is a worked English example of turning a correction into another attempt.",

      "practice.title": "Don’t just spot a mistake.\nUnderstand the next step.",

      "practice.eyebrow": "A small example. A useful difference.",

      'nav.features': 'Features',
      'nav.how': 'How it Works',
      'nav.screens': 'App Preview',
      "nav.testimonials": "Learner stories",
      'nav.faq': 'FAQ',
      'nav.download': 'Download',

      "hero.pill": "A little practice. A more confident you.",
      "hero.title": "Find your words.<br><span class=\"text-gradient\">Then your voice.</span>",
      "hero.subtitle": "Turn the language you know into conversations you can have. Practice everyday situations with AI, understand your mistakes, and come back a little more confident.",
      "hero.studioLabel": "Your everyday speaking practice",
      'hero.sceneLabel': 'REAL LIFE, REHEARSED',
      "hero.sceneTitle": "One coffee. A first step.",
      'hero.sceneLevel': 'At the café · English practice',
      "hero.session": "Practice. Get feedback. Try again.",
      "hero.ctaPrimary": "Get UpWord for Android",
      "hero.ctaSecondary": "Explore a practice example",
      "hero.note": "Android 8+ · AI provider setup required. Provider usage may cost extra.",
      'hero.encourage': 'Small steps. Real confidence.',
      'hero.encourageSub': 'Your next conversation starts here.',
      'hero.practice': 'TODAY’S PRACTICE · AT THE CAFÉ',
      "hero.preview": "Illustrative English practice, not a live AI conversation",
      'nav.skip': 'Skip to content',
      'languages.label': 'YOUR NEXT CHAPTER, IN…',
      'languages.en': 'English',
      'languages.es': 'Spanish',
      'languages.fr': 'French',
      'languages.de': 'German',
      'languages.tr': 'Turkish',
      'languages.ar': 'Arabic',

      'stats.languages': 'Languages',
      'stats.topics': 'Conversation Topics',
      'stats.rating': 'User Rating',
      'stats.votes': 'Verified Reviews',

      'badge.streak': '7 days',

      'trust.privacy': 'Your privacy respected',
      'trust.ai': 'Advanced AI',
      'trust.android': 'Android 8+',
      'trust.free': 'Free to start',

      "features.eyebrow": "Made for the moment you need to speak",
      "features.title": "More than knowing a word.\nKnowing what to say.",
      "features.subtitle": "Build your practice around useful conversations, then give the words and phrases another go.",
      "features.f1.title": "A conversation, at your level",
      "features.f1.desc": "Choose a topic and a level. Reply by text or supported voice input, and get AI feedback on your sentences. There is room to make mistakes here.",
      "features.f2.title": "Real situations. A clear mission.",
      "features.f2.desc": "Order a meal, check into a hotel, or rehearse a work conversation. Mission objectives give you something practical to work toward.",
      "features.f3.title": "Listen. Repeat. Find your rhythm.",
      "features.f3.desc": "Use shadowing to listen to a phrase and repeat it aloud. Audio and speech recognition depend on your selected service and device.",
      "features.f4.title": "Keep the useful words close",
      "features.f4.desc": "Collect vocabulary and revisit saved mistakes. Make review part of your practice instead of leaving feedback behind in a chat.",
      "features.f5.title": "Small wins you can see",
      "features.f5.desc": "Daily goals, XP, streaks, and achievements make your practice visible. They track activity, not a certified language level.",
      "features.f6.title": "You choose the starting point",
      "features.f6.desc": "Set your target language and select beginner, intermediate, or advanced practice. Adjust your level as your needs change.",

      'how.eyebrow': 'How it works',
      "how.title": "Your first conversation starts here.",
      "how.subtitle": "A little setup first. Then a space to practice at your own pace.",
      "how.s1.title": "Make it yours",
      "how.s1.desc": "Install the Android app. Choose your native language, target language, and current level.",
      "how.s2.title": "Connect your AI provider",
      "how.s2.desc": "In AI settings, add credentials for a compatible provider and select a model. You need internet; availability and usage charges depend on that provider.",
      "how.s3.title": "Choose a situation. Say something.",
      "how.s3.desc": "Open a conversation or mission. Try a reply, read the feedback, and practice a useful phrase again. Text is a good place to start.",

      "mascot.eyebrow": "Small steps count",
      "mascot.title": "A reason to return.\nAt your own pace.",
      "mascot.desc": "A daily goal gives you a starting point. XP and achievements mark the practice you put in. And our turtle is a reminder: progress takes patience, not perfection.",
      "mascot.l1": "Choose a daily goal",
      "mascot.l2": "See your practice add up",
      "mascot.l3": "Celebrate your milestones",
      "mascot.l4": "Make room for another try",
      "mascot.cta": "Build your practice habit",

      'screens.eyebrow': 'App Preview',
      'screens.title': 'A look inside UpWord',
      'screens.subtitle': 'Conversation, vocabulary, and small wins. Explore these illustrative previews of your learning journey.',

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

      'mock.greeting': 'A little better, every day.',
      'mock.greetingSub': 'Let’s practice together.',
      'mock.dailyGoal': 'Daily Goal',
      'mock.dailyGoalMeta': '30 of 50 XP',
      'mock.todaysMission': "Today's Mission",
      'mock.todaysMissionMeta': 'Ordering food at a restaurant',
      'mock.newVocab': 'New Vocabulary',
      'mock.newVocabMeta': '12 words learned',

      'testi.eyebrow': 'User Reviews',
      'testi.title': 'What UpWord users say',
      "testi.subtitle": "A few learner stories from the original Cafe Bazaar listing. See the store for current reviews and ratings.",
      'testi.r1.translation': '"Incredible and complete. Covers everything. The best part is finding pronunciation and the routine use of words in movie dialogues. Aweeesome."',
      'testi.r1.role': 'Cafe Bazaar User',
      'testi.r2.translation': '"Really cool — a complete package of different tools that helps in every area."',
      'testi.r2.role': 'Cafe Bazaar User',
      'testi.r3.translation': '"A very good and practical app with interesting features."',
      'testi.r3.role': 'Cafe Bazaar User',
      "testi.summary": "Curious what other learners think? Read the latest reviews, check the current app details, and decide whether UpWord fits your practice.",
      'testi.viewAll': 'View on Cafe Bazaar',

      'faq.eyebrow': 'FAQ',
      'faq.title': 'Everything you want to know',
      "faq.q1": "What do I need to get started?",
      "faq.a1": "An Android 8+ device, internet for AI conversations, and credentials for a compatible AI provider. Check Cafe Bazaar for the current app price. AI usage is subject to your provider’s pricing and limits; downloading the app does not include an AI allowance.",
      'faq.q2': 'Do I need internet to use it?',
      "faq.a2": "AI conversations and generated feedback need internet. Saved content can remain on your device, but audio, speech recognition, and other connected features may still need a network connection.",
      'faq.q3': 'Which languages are supported?',
      "faq.a3": "The app offers English, Turkish, Arabic, German, French, and Spanish as target languages. Conversation, voice, and content availability can vary by language, device, and AI provider.",
      "faq.q4": "Where do my conversations go?",
      "faq.a4": "Learning history is stored on your device. To generate replies and feedback, conversation content is sent to your configured AI service. Voice features may send audio to a speech provider. Those services have their own data and retention policies.",
      'faq.q5': 'What level do I need?',
      "faq.a5": "Choose beginner, intermediate, or advanced in the app. This is a self-selected practice level, not an automatic placement test or a language certification. AI feedback can be mistaken.",

      "cta.title": "Your next conversation\nstarts with this one.",
      "cta.subtitle": "Give yourself a place to practice, make mistakes, and find the words you want to say.",
      'cta.button': 'Download from Cafe Bazaar',
      "cta.note": "Android 8+ · Internet and compatible AI provider credentials required. Provider charges may apply.",

      'footer.desc': 'Your smart companion for learning languages through real conversation.',
      'footer.product': 'Product',
      'footer.download': 'Download',
      'footer.about': 'About',
      'footer.android': 'Android',
      'footer.aboutApp': 'About UpWord',
      'footer.copyright': '© 2026 UpWord — All rights reserved.',
    },

    fa: {
      "loop.repeat": "جمله‌های کاربردی را مرور کن",

      "loop.learn": "از بازخورد یاد بگیر",

      "loop.speak": "مکالمه را تمرین کن",

      "practice.note": "این مثال از پیش نوشته شده و بخشی از یک مکالمه زنده با هوش مصنوعی نیست.",

      "practice.reveal": "شکل درست جمله و تمرین بعدی را ببین",

      "practice.label": "نمونه تمرین · انگلیسی · زمان گذشته",

      "practice.desc": "دیدن شکل درست جمله، تازه شروع یادگیری است. در این مثال انگلیسی، دلیل اشتباه را می‌فهمی و همان نکته را در جمله‌ای تازه به کار می‌بری.",

      "practice.title": "اشتباهت را بشناس.\nدفعه بعد بهتر بگو.",

      "practice.eyebrow": "یک مثال ساده، یک نکته کاربردی",

      'nav.features': 'امکانات',
      "nav.how": "راهنمای شروع",
      "nav.screens": "نگاهی به اپ",
      "nav.testimonials": "تجربه کاربران",
      "nav.faq": "پرسش‌های رایج",
      'nav.download': 'دانلود',

      "hero.pill": "هر بار تمرین، یک قدم بااعتمادبه‌نفس‌تر",
      "hero.title": "کلمه‌ها را بلدی.<br><span class=\"text-gradient\">حالا حرف بزن.</span>",
      "hero.subtitle": "وقت آن است که از کلمه‌هایی که بلدی استفاده کنی. مکالمه‌های روزمره را با هوش مصنوعی تمرین کن، از اشتباهاتت یاد بگیر و راحت‌تر حرف بزن.",
      "hero.studioLabel": "همراه تو در تمرین مکالمه",
      "hero.sceneLabel": "تمرین برای موقعیت‌های واقعی",
      "hero.sceneTitle": "یک قهوه، شروع یک مکالمه.",
      'hero.sceneLevel': 'در کافه · تمرین انگلیسی',
      "hero.session": "تمرین کن، بازخورد بگیر، دوباره امتحان کن.",
      "hero.ctaPrimary": "دانلود آپ‌ورد برای اندروید",
      "hero.ctaSecondary": "نمونه تمرین را ببین",
      "hero.note": "اندروید ۸ به بالا · سرویس هوش مصنوعی را باید جداگانه تنظیم کنی. استفاده از آن ممکن است هزینه داشته باشد.",
      'hero.encourage': 'قدم‌های کوچک، اعتمادبه‌نفس واقعی',
      "hero.encourageSub": "مکالمه بعدی‌ات از همین‌جا شروع می‌شود.",
      'hero.practice': 'تمرین امروز · در کافه',
      "hero.preview": "نمونه‌ای از تمرین انگلیسی؛ این مکالمه زنده نیست.",
      "nav.skip": "رفتن به محتوای اصلی",
      "languages.label": "به چه زبانی می‌خواهی حرف بزنی؟",
      'languages.en': 'انگلیسی',
      'languages.es': 'اسپانیایی',
      'languages.fr': 'فرانسوی',
      'languages.de': 'آلمانی',
      'languages.tr': 'ترکی',
      'languages.ar': 'عربی',

      'stats.languages': 'زبان قابل یادگیری',
      'stats.topics': 'موضوع مکالمه',
      'stats.rating': 'امتیاز کاربران',
      'stats.votes': 'نظرات تأییدشده',

      "badge.streak": "۷ روز پیاپی",

      'trust.privacy': 'حریم خصوصی شما محترم است',
      'trust.ai': 'هوش مصنوعی پیشرفته',
      'trust.android': 'اندروید ۸ به بالا',
      'trust.free': 'شروع رایگان',

      "features.eyebrow": "برای وقتی که می‌خواهی حرف بزنی",
      "features.title": "فقط کلمه یاد نگیر.\nیاد بگیر چه بگویی.",
      "features.subtitle": "با مکالمه‌های کاربردی تمرین کن و با مرور واژه‌ها و جمله‌ها، آموخته‌هایت را به کار بگیر.",
      "features.f1.title": "مکالمه‌ای متناسب با سطح تو",
      "features.f1.desc": "موضوع و سطح تمرینت را انتخاب کن. پاسخ را بنویس یا، اگر دستگاه و سرویس انتخابی‌ات پشتیبانی می‌کنند، با صدا جواب بده. برای جمله‌هایت بازخورد بگیر و بدون نگرانی از اشتباه کردن تمرین کن.",
      "features.f2.title": "هر موقعیت، یک ماموریت",
      "features.f2.desc": "غذا سفارش بده، اتاق هتل بگیر یا برای یک گفت‌وگوی کاری آماده شو. هر ماموریت هدف مشخصی دارد تا بدانی چه چیزی را تمرین می‌کنی.",
      "features.f3.title": "گوش بده و همراهش تکرار کن",
      "features.f3.desc": "در تمرین شدوینگ، جمله را می‌شنوی و با صدای بلند تکرار می‌کنی تا با آهنگ و ریتم زبان آشنا شوی. پخش صدا و تشخیص گفتار به دستگاه و سرویس انتخابی‌ات بستگی دارد.",
      "features.f4.title": "واژه‌های کاربردی را فراموش نکن",
      "features.f4.desc": "واژه‌های تازه را ذخیره کن و اشتباهات قبلی‌ات را مرور کن. به نکته‌هایی که یاد گرفته‌ای برگرد تا بازخوردها فقط در مکالمه باقی نمانند.",
      "features.f5.title": "تمرینت را ببین، انگیزه بگیر",
      "features.f5.desc": "هدف روزانه، امتیاز، روزهای پیاپی تمرین و دستاوردها به تو نشان می‌دهند چقدر تمرین کرده‌ای. این‌ها نشانه فعالیت تو هستند و سطح زبانت را تعیین نمی‌کنند.",
      "features.f6.title": "از سطح خودت شروع کن",
      "features.f6.desc": "زبان موردنظرت و سطح مبتدی، متوسط یا پیشرفته را انتخاب کن. هر وقت تمرین‌ها برایت آسان یا سخت شدند، سطح را تغییر بده.",

      "how.eyebrow": "راهنمای شروع",
      "how.title": "تا اولین مکالمه، سه قدم فاصله داری.",
      "how.subtitle": "تنظیمات اولیه را انجام بده و بعد، با خیال راحت تمرین را شروع کن.",
      "how.s1.title": "زبان و سطحت را انتخاب کن",
      "how.s1.desc": "آپ‌ورد را روی گوشی اندرویدی‌ات نصب کن. زبان مادری، زبانی که می‌خواهی یاد بگیری و سطح فعلی‌ات را مشخص کن.",
      "how.s2.title": "هوش مصنوعی را راه‌اندازی کن",
      "how.s2.desc": "در تنظیمات هوش مصنوعی، اطلاعات دسترسی به یک سرویس سازگار را وارد کن و مدل دلخواهت را انتخاب کن. برای استفاده به اینترنت نیاز داری؛ هزینه و محدودیت‌ها به همان سرویس بستگی دارد.",
      "how.s3.title": "اولین مکالمه‌ات را شروع کن",
      "how.s3.desc": "یک موضوع یا ماموریت انتخاب کن. پاسخ بده، بازخورد را بخوان و جمله‌های کاربردی را دوباره تمرین کن. برای شروع می‌توانی پاسخ‌هایت را بنویسی.",

      "mascot.eyebrow": "قدم‌های کوچک مهم‌اند",
      "mascot.title": "هر روز، کمی تمرین.\nبا سرعت خودت.",
      "mascot.desc": "با یک هدف روزانه شروع کن و قدم‌هایی را که برداشته‌ای در امتیازها و دستاوردهایت ببین. لاک‌پشت آپ‌ورد هم یادت می‌اندازد که برای پیشرفت، لازم نیست بی‌نقص باشی؛ کافی است با حوصله ادامه بدهی.",
      "mascot.l1": "یک هدف روزانه انتخاب کن",
      "mascot.l2": "حاصل تمرین‌هایت را ببین",
      "mascot.l3": "موفقیت‌های کوچکت را جشن بگیر",
      "mascot.l4": "به خودت فرصت دوباره بده",
      "mascot.cta": "تمرین را به عادت تبدیل کن",

      "screens.eyebrow": "نگاهی به اپ",
      "screens.title": "در آپ‌ورد چه خبر است؟",
      "screens.subtitle": "از تمرین مکالمه تا مرور واژگان و ثبت دستاوردها؛ این نمونه‌های نمایشی، حال‌وهوای یادگیری در آپ‌ورد را نشان می‌دهند.",

      'screen.chat.title': 'مکالمه آزاد',
      'screen.chat.feedback': 'عالی! جمله‌ات طبیعی بود.',
      'screen.ach.title': 'دستاوردها',
      'screen.ach.subtitle': 'دستاورد جدید!',
      "screen.ach.name": "۷ روز تمرین پیاپی",
      'screen.ach.desc': 'یک هفته کامل تمرین کردی!',
      'screen.ach.a1': 'اولین مکالمه',
      "screen.ach.a2": "۷ روز تمرین پیاپی",
      'screen.ach.a3': '۱۰ ماموریت',
      'screen.vocab.title': 'واژگان',
      "screen.vocab.progress": "۱۲ واژه از ۲۰ واژه",
      "screen.vocab.meaning": "اتفاق خوشایند و غیرمنتظره",
      'screen.vocab.listen': '🔊 گوش بده',
      "screen.vocab.know": "بلدم",

      'mock.greeting': 'هر روز، کمی بهتر',
      'mock.greetingSub': 'بیا با هم تمرین کنیم.',
      'mock.dailyGoal': 'هدف روزانه',
      "mock.dailyGoalMeta": "۳۰ امتیاز از ۵۰ امتیاز",
      'mock.todaysMission': 'ماموریت امروز',
      'mock.todaysMissionMeta': 'سفارش غذا در رستوران',
      'mock.newVocab': 'واژگان جدید',
      "mock.newVocabMeta": "۱۲ واژه یاد گرفته‌ای",

      'testi.eyebrow': 'نظرات کاربران',
      "testi.title": "کاربران درباره آپ‌ورد چه می‌گویند؟",
      "testi.subtitle": "چند نظر از کاربران در صفحه اولیه آپ‌ورد در کافه بازار. برای دیدن تازه‌ترین نظرها و امتیازها، به صفحه اپ در فروشگاه سر بزن.",
      'testi.r1.translation': '«بی‌نظیر و کامل. همه‌چیز را پوشش می‌دهد. بهترین قسمتش پیدا کردن تلفظ و استفاده روتین کلمه در دیالوگ فیلم‌هاست. عاااالیه.»',
      'testi.r1.role': 'کاربر کافه بازار',
      'testi.r2.translation': '«خیلی باحاله — یک پکیج کامل از ابزارهای مختلف که در همه زمینه‌ها کمک می‌کند.»',
      'testi.r2.role': 'کاربر کافه بازار',
      'testi.r3.translation': '«برنامه خیلی خوب و کاربردی است و امکانات جالبی دارد.»',
      'testi.r3.role': 'کاربر کافه بازار',
      "testi.summary": "دوست داری تجربه بقیه را هم بخوانی؟ نظرهای تازه و اطلاعات اپ را در کافه بازار ببین و تصمیم بگیر که آپ‌ورد برای تمرین تو مناسب است یا نه.",
      'testi.viewAll': 'مشاهده در کافه بازار',

      "faq.eyebrow": "پرسش‌های رایج",
      "faq.title": "پیش از شروع، بیشتر بدان",
      "faq.q1": "برای شروع چه چیزهایی لازم دارم؟",
      "faq.a1": "یک دستگاه با اندروید ۸ یا بالاتر، اینترنت و اطلاعات دسترسی به یک سرویس هوش مصنوعی سازگار لازم داری. قیمت فعلی اپ را در کافه بازار ببین. هزینه و سقف استفاده از هوش مصنوعی را سرویس انتخابی‌ات مشخص می‌کند؛ با دانلود اپ، اعتبار استفاده از هوش مصنوعی دریافت نمی‌کنی.",
      'faq.q2': 'آیا برای استفاده به اینترنت نیاز دارم؟',
      "faq.a2": "برای مکالمه با هوش مصنوعی و دریافت بازخورد به اینترنت نیاز داری. محتوای ذخیره‌شده روی دستگاه می‌ماند، اما پخش صدا، تشخیص گفتار و بعضی قابلیت‌های دیگر ممکن است همچنان به اینترنت نیاز داشته باشند.",
      'faq.q3': 'چه زبان‌هایی پشتیبانی می‌شوند؟',
      "faq.a3": "می‌توانی انگلیسی، ترکی، عربی، آلمانی، فرانسوی یا اسپانیایی را به‌عنوان زبان یادگیری انتخاب کنی. امکانات مکالمه، صدا و محتوای در دسترس ممکن است بسته به زبان، دستگاه و سرویس هوش مصنوعی متفاوت باشد.",
      "faq.q4": "اطلاعات مکالمه‌هایم کجا ذخیره یا ارسال می‌شود؟",
      "faq.a4": "تاریخچه یادگیری روی دستگاهت ذخیره می‌شود. برای دریافت پاسخ و بازخورد، متن مکالمه به سرویس هوش مصنوعی انتخابی‌ات ارسال می‌شود. هنگام استفاده از امکانات صوتی هم ممکن است صدایت به سرویس پردازش گفتار فرستاده شود. نحوه استفاده از این اطلاعات و مدت نگهداری آن‌ها به سیاست‌های هر سرویس بستگی دارد.",
      "faq.q5": "برای استفاده باید در چه سطحی باشم؟",
      "faq.a5": "می‌توانی سطح مبتدی، متوسط یا پیشرفته را انتخاب کنی. این انتخاب فقط سطح تمرین‌ها را مشخص می‌کند؛ آپ‌ورد آزمون تعیین سطح خودکار برگزار نمی‌کند و مدرک زبان نمی‌دهد. بازخورد هوش مصنوعی هم ممکن است اشتباه باشد.",

      "cta.title": "اولین جمله را بگو.\nراه می‌افتی.",
      "cta.subtitle": "جایی برای تمرین، اشتباه کردن و یاد گرفتن؛ تا هر بار راحت‌تر حرف بزنی.",
      'cta.button': 'دانلود از کافه بازار',
      "cta.note": "اندروید ۸ به بالا · به اینترنت و اطلاعات دسترسی به یک سرویس هوش مصنوعی سازگار نیاز داری. استفاده از سرویس ممکن است هزینه جداگانه داشته باشد.",

      "footer.desc": "همراه هوشمند تو برای یادگیری زبان با تمرین مکالمه.",
      'footer.product': 'محصول',
      'footer.download': 'دانلود',
      "footer.about": "درباره ما",
      'footer.android': 'اندروید',
      "footer.aboutApp": "درباره آپ‌ورد",
      "footer.copyright": "© ۲۰۲۶ آپ‌ورد — تمامی حقوق محفوظ است.",
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
        langBtn.focus();
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
    progressBar.style.transform = 'scaleX(' + Math.min(1, Math.max(0, pct / 100)) + ')';
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

  /* ===== Reveal on scroll ===== */
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const activeReveals = new Map();
  const motionTokens = getComputedStyle(document.documentElement);
  const revealDuration = parseFloat(motionTokens.getPropertyValue('--motion-reveal'));
  const revealStagger = parseFloat(motionTokens.getPropertyValue('--motion-stagger'));
  const revealDistance = motionTokens.getPropertyValue('--motion-distance').trim();
  const revealEasing = motionTokens.getPropertyValue('--ease-out').trim();

  if ('IntersectionObserver' in window && 'animate' in Element.prototype) {
    const revealEls = document.querySelectorAll(
      '.hero-content > *, .hero-visual, .feature-card, .step, .testimonial, .screen-mockup, .mascot-content, .mascot-visual, .section-head, .stats-row > *, .cta-card'
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
          delay: (index % 3) * revealStagger,
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
  reducedMotion.addEventListener('change', () => {
    if (reducedMotion.matches) activeReveals.forEach((animation) => animation.cancel());
  });

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
      state.visible = entry.isIntersecting;
      syncTurtle(state);
    });
  }, { threshold: 0.15 }) : null;
  document.addEventListener('visibilitychange', () => turtleStates.forEach(syncTurtle));
  reducedMotion.addEventListener('change', () => turtleStates.forEach(syncTurtle));

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

  loadLottie('stepTurtle1', 'assets/lottie/turtle-swimming.json');
  loadLottie('stepTurtle2', 'assets/lottie/turtle-success.json');
  loadLottie('stepTurtle3', 'assets/lottie/turtle-progress.json');
  loadLottie('mascotTurtle', 'assets/lottie/turtle-ninja.json');
  loadLottie('achievementTurtle', 'assets/lottie/turtle-success.json');
  loadLottie('ctaTurtle', 'assets/lottie/turtle-meditation.json');

  /* ===== Smooth scroll for anchor links (with navbar offset) ===== */
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener('click', (e) => {
      const href = anchor.getAttribute('href');
      if (href === '#' || href === '#!') return;
      const target = document.querySelector(href);
      if (!target) return;
      e.preventDefault();
      const offset = navbar.offsetHeight;
      const top = target.getBoundingClientRect().top + window.scrollY - offset;
      window.scrollTo({ top, behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth' });
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
  const initialLang = getStoredLang();
  applyLang(initialLang);
  initLangSwitcher();
  updateScrollProgress();
  updateNavbar();
})();

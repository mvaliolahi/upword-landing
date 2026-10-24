#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""گسترش درس‌به‌درس (v-deepen) · درس‌های ۸۲ تا ۹۰ — اشتباه‌های رایج + تمرین + چالش."""

DEEPEN = {
 # ── درس ۸۲ ──────────────────────────────────────────────────────────────
 'english-incident-management': {
  'mistakes': [
   ('Dara\'s deploy broke the production — I will tell him to be careful.', 'Working theory: a DB pool change in the last deploy likely triggered this — rollback is running.', 'روایتِ فارسیِ حادثه با فاعلِ آدمی شروع می‌شود («فلانی خرابش کرد»)، اما انگلیسیِ حادثه فرایند را نشانه می‌گیرد، نه شخص را. جملهٔ با نامِ همکار، تیم را ساکت و دفاعی می‌کند و قاعدهٔ بی‌اتهامی را همان‌جا می‌شکند.'),
   ('The problem solved and everything returned normal.', 'The issue is resolved — error rates are back to baseline.', '«مسئله حل شد» با فعلِ کاملاً فعال فرستاده می‌شود: The problem solved یعنی «مسئله حل کرد»! حل‌شدن صرفِ مجهول می‌خواهد: is resolved. و «به حالتِ عادی برگشت» هم return نمی‌گیرد — زبانِ حادثه برایِ برگشتنِ متریک‌ها back to baseline می‌گوید.'),
   ('We are working on it and will inform you when it finished.', 'Rollback is at 3/12 pods — next update at 14:30, sooner if anything changes.', '«تا حل شود خبر می‌کنیم» ترجمهٔ مستقیمِ فارسی است و وعدهٔ بی‌زمان می‌سازد؛ زبانِ حادثه همان‌جا زمانِ آپدیتِ بعدی را قول می‌دهد. سکوتِ بی‌برنامه در کانال وحشت می‌سازد؛ وعدهٔ آپدیتِ بعدی، همان سکوت را بی‌خطر می‌کند.'),
  ],
  'drills': (
   'حادثه، تمرینِ نوشتنِ زیرِ فشار است؛ هر چهار را با تایمرِ پنج‌دقیقه‌ای اول خودت بلند بگو، بعد پاسخ را باز کن.',
   [
    'اولین خطِ اعلامِ حادثه را بنویس: قطعیِ checkout از ساعت ۱۴:۰۲ برایِ حدود ۳۰٪ کاربرها؛ کانالِ جنگ: #inc-042. (قالبِ درس: سطح + سیستم + دامنه + زمان + کانال)',
    'جملهٔ اتهام‌دار را بازنویسی کن: «Sara\'s config change broke the cache.» — فرایند را نشانه بگیر، نه آدم را.',
    'دارا در پلِ جنگ می‌گوید: «I think it\'s the DNS.» — حرفش را با برچسبِ درست در بریفِ وضعیت ثبت کن.',
    'بریفِ پایانِ حادثه را بنویس: خطاها ۳۰ دقیقه در سطحِ پایه مانده، پایش برداشته می‌شود، پست‌مورتم جمعه ساعت ۱۰.',
   ],
   [
    ('پاسخ تمرین ۱', '**P1 — checkout is degraded for ~30% of users since 14:02. Channel: #inc-042.** چهار قطعهٔ اعلام همین‌قدر فشرده است: سطح، سیستم، دامنه و زمان، و در آخر آدرسِ کانال. خطِ اولِ تمیز، تمامِ وحشتِ کانال را می‌خواباند.'),
    ('پاسخ تمرین ۲', '**A cache config change in the last deploy is the likely trigger — we\'re rolling it back now.** اسمِ فرایند جایِ اسمِ آدم می‌نشیند؛ در پست‌مورتمِ بی‌اتهام سؤال «چه چیزی اشتباه شد» است، نه «چه کسی».'),
    ('پاسخ تمرین ۳', '**CAUSE (working theory): DNS propagation — not yet confirmed.** برچسبِ working theory حدس را از واقعیت جدا می‌کند؛ تا متریک تأیید نکند هیچ چیزی confirmed نمی‌شود — همین مرز، قلبِ بی‌اتهامی است.'),
    ('پاسخ تمرین ۴', '**All-clear: error rates have been at baseline for 30 minutes. Monitoring is standing down. Postmortem Friday at 10:00 — blameless; bring your timelines.** جملهٔ پایانی دو کار می‌کند: قفلِ امنیت + قرارِ یادگیری؛ بدونِ این دو، حادثه «بسته» نمی‌شود، فقط «تمام» می‌شود.'),
   ],
  ),
  'challenge': 'برایِ آخرین قطعی یا باگِ جدیِ تیم‌تان یک بریفِ چهارخطیِ STATUS / CAUSE / ACTION / NEXT UPDATE بنویس — حتی اگر هفته‌ها پیش بوده؛ عضلهٔ حادثه با بازنویسی ساخته می‌شود.',
 },

 # ── درس ۸۳ ──────────────────────────────────────────────────────────────
 'english-performance-reviews': {
  'mistakes': [
   ('I tried my best and did many good things for the team this year.', 'I led the retry redesign — shipped two months early, cut failures 38%, and two teams adopted the pattern.', 'ادبِ فارسی از عدد می‌ترسد که «خودستایی» نشود و به «تلاش کردم» پناه می‌برد؛ اما review انگلیسی اثر می‌خواهد، نه کوشش: فعل + عدد + دامنه. «did many good things» هیچ ردیفی در برگهٔ مدیر نمی‌سازد.'),
   ('I worked hardly this quarter, day and night.', 'This was my hardest quarter — and the most measurable: failures down 38%.', '«سخت کار کردم» با hardly فرستاده می‌شود؛ اما hardly یعنی «تقریباً هیچ» — I worked hardly یعنی «تقریباً کار نکردم»! قیدِ درست hard است؛ و در review به‌جای قید، عدد بگذار تا ادعا سند شود.'),
   ('No, this rating is wrong — you don\'t know how much I did.', 'Thanks — I\'d like to understand the gap: what would "exceeds" have looked like on the retry project?', 'در برابرِ نمرهٔ ناامیدکننده، ذهنِ فارسی اول انکار می‌فرستد («نه، برعکسه»)؛ پاسخِ حرفه‌ای اول نقد را می‌پذیرد و بعد معیار را می‌پرسد. سؤالِ «فراتر از انتظار چه شکلی بود؟» جنگِ نمره را به نقشهٔ سالِ بعد تبدیل می‌کند.'),
  ],
  'drills': (
   'تمرینِ این درس نوشتنِ خودارزیابی و پاسخِ آرام به نقد است؛ هر چهار را اول خودت بنویس، بعد پاسخ را باز کن.',
   [
    'این جملهٔ خودارزیابی را با فرمولِ «فعل + عدد + دامنه» بازنویسی کن: «I helped the team a lot with the migration.»',
    'مدیر می‌گوید: «You need to be more visible.» — با پذیرشِ کوتاه + سؤالِ عملیاتی جواب بده.',
    'نمره‌ات «در حدِ انتظار» شد در حالی که پروژه‌ات ۳۸٪ خطا کم کرده. سؤالِ معیار را کامل بپرس.',
    'جملهٔ شروعِ گفتگوی رشد به سمتِ senior را با سه قطعه بساز: خواسته + فاصله از نگاهِ تو + دعوت به برنامه.',
   ],
   [
    ('پاسخ تمرین ۱', '**I led the data migration — zero downtime, two weeks ahead of schedule, and three teams reused our checklist.** عدد و دامنه، ادعا را سند می‌کنند؛ helped a lot هیچ مقیاسی ندارد و در برگهٔ مدیر وزن نمی‌کند.'),
    ('پاسخ تمرین ۲', '**That\'s fair — could you be more specific? Would writing the retry pattern up as an internal post count as the visibility you mean?** فرمول: پذیرشِ کوتاه + سؤالِ دقیق؛ فیدبکِ مبهم را همان‌جا به قراردادِ قابلِ اندازه‌گیری تبدیل می‌کنی.'),
    ('پاسخ تمرین ۳', '**Thanks — I want to understand the gap. The retry redesign shipped early and cut failures 38%: what would "exceeds" have looked like there?** پاسخِ این سؤال، نقشهٔ دقیقِ سالِ بعدِ توست؛ بهترین پرسشِ کلِ فرایندِ review همین است.'),
    ('پاسخ تمرین ۴', '**I want to grow toward senior — from my read, the gap is cross-team influence. Can we turn that into a plan?** سه قطعه: خواستهٔ روشن، فاصلهٔ صادقانه، دعوت به برنامه — نه گلایه، نه التماس؛ همین لحن، ارتقا را مذاکره می‌کند نه درخواست.'),
   ],
  ),
  'challenge': 'امروز «دفترِ بردها» را باز کن: سه ردیفِ «فعل + عدد + دامنه» از کارهای امسال بنویس و اولین پنجشنبهٔ هر ماه سه ردیفِ تازه اضافه کن — خودارزیابیِ دسامبر از این دفتر نوشته می‌شود، نه از حافظه.',
 },

 # ── درس ۸۴ ──────────────────────────────────────────────────────────────
 'english-cultural-pragmatics': {
  'mistakes': [
   ('Thank you! I knew this proposal was brave!', 'Thanks — just to check: when you say "brave", is that enthusiasm, or a concern I should hear before I build on it?', 'در جدولِ کم‌گوییِ بریتانیایی، «brave proposal» تقریباً هرگز تعریف نیست — یعنی «به‌نظرم ریسکِ بی‌حساب است»! ذهنِ فارسی کلمه را لغت‌نامه‌ای می‌خواند و روی نُهِ مخفی خانه می‌چیند؛ جوابِ حرفه‌ای شفاف‌سازی است، نه سپاسِ زودهنگام.'),
   ('He said "quite good" — so it means very good, and we are approved!', 'He said "quite good" — in UK English that is one step below very good, so I asked what he would tighten.', 'ذهنِ مترجمِ تازه‌کار quite را تقویت‌کننده می‌خواند و «کویت گود» را «خیلی خوب» می‌گیرد؛ در بریتانیا quite good پله‌ای پایین‌تر از very good است. قاعدهٔ کلیدی: هرچه جملهٔ بریتانیایی آرام‌تر و خنثی‌تر، پیامِ زیرین احتمالاً جدی‌تر.'),
   ('Sorry, sorry — my question is very small and maybe stupid.', 'Sorry — quick question: could we revisit the dates?', 'عذرخواهیِ زنجیره‌ای و تحقیرِ خودی («سؤالِ کوچکِ شاید احمقانه») از ادبِ فارسی می‌آید اما سیگنالِ بی‌اعتمادی می‌فرستد و سؤال را بی‌وزن می‌کند. قالبِ بومیِ کارکردی: یک sorryِ فرهنگی + quick question — کوتاه، محترم، بی‌خودکمتی.'),
  ],
  'drills': (
   'این درس، تمرینِ گوشِ فرهنگی است؛ هر چهار را اول بلند جواب بده، بعد پاسخ را باز کن.',
   [
    'همکارِ بریتانیایی دربارهٔ تایم‌لاین می‌گوید: «A little optimistic, perhaps?» — پیامِ واقعی چیست و چه جوابی می‌دهی؟',
    'معنای زیرینِ این سه را بگو: «That\'s a brave proposal» · «With the greatest respect…» · «Very interesting.»',
    'همکارِ کانادایی: «This is maybe fine, but sorry — could we maybe revisit the dates?» — جوابی بده که پیام را گم نکند.',
    'برایِ ایمیلِ «The rollout plan is… interesting.» یک جملهٔ شفاف‌سازِ محترمانه بنویس.',
   ],
   [
    ('پاسخ تمرین ۱', 'پیامِ واقعی: **این تایم‌لاین رخ نمی‌دهد.** جوابِ درست: **"So that\'s a gentle no on the timeline — good, let\'s renegotiate the dates before we commit."** کم‌گویی را با برون‌ریزیِ صریحِ خودت قفل می‌کنی؛ این حرکت در جلسه‌های چندفرهنگی امضای بلوغ است.'),
    ('پاسخ تمرین ۲', 'به‌ترتیب: **«به‌نظرم بی‌حساب است» · «به‌نظرم اشتباه می‌کنی» · «قانع نشده‌ام»** — هیچ‌کدام تعریف نیستند؛ هر سه نقدِ نرم‌اند و هر سه منتظرِ واکنشِ دقیقِ تو هستند تا لایهٔ زیرین بیرون بیاید.'),
    ('پاسخ تمرین ۳', 'گم‌کننده: «Thanks! So it\'s fine?» — پیام‌گیر: **"Taking that as a real flag — we\'ll revisit the dates. Thanks for raising it kindly."** sorryِ کانادایی اقرار نیست، هشدارِ مهربان است؛ جدی‌گرفتنش نه ضعف است نه تعارف — دقتِ فرهنگی است.'),
    ('پاسخ تمرین ۴', '**"When you say \'interesting\' — is that a concern I should address now, or genuinely interesting? Happy to hear either."** یک جمله، ابهامِ فرهنگی را به اطلاعاتِ قابلِ استفاده تبدیل می‌کند؛ این را ابزارِ دائمی‌ات کن و بدونِ خجالت بفرست.'),
   ],
  ),
  'challenge': 'پیامِ مهمِ امروزت را سه‌بار در ذهن بخوان — با چشمِ آمریکایی (مستقیم)، بریتانیایی (کم‌گو)، کانادایی (نرم) — و اگر ریسکِ بدفهمی دیدی، همان جملهٔ شفاف‌سازِ درس را بفرست.',
 },

 # ── درس ۸۵ ──────────────────────────────────────────────────────────────
 'english-humor-banter': {
  'mistakes': [
   ('You are so slow, like a turtle! 😄', 'The build is so slow I finished a podcast episode waiting for it 😅', 'شوخیِ صمیمیِ فارسی آدم را هدف می‌گیرد («مثلِ لاک‌پشتی!»)؛ اما در فضای کاریِ انگلیسی هدفِ امن سه چیز است: خودت، ابزار و کد، موقعیت. جملهٔ شوخی که با You are شروع شود، دیگر شوخی نیست — روستِ شخصی است.'),
   ('Great job. Now the test fails again.', 'Great job — and the flaky test says hi again 🙃 I\'ll take this one.', 'متنِ شوخی‌دارِ بی‌لحن، در چتِ انگلیسی سرد یا حتی پرخاش خوانده می‌شود؛ ایموجی و عبارت‌هایی مثل to be fair همان لبخندِ صدا هستند. جملهٔ دومِ خشکِ بی‌لحن، اولین جمله را می‌کُشد.'),
   ('Actually, it is not a competition — it is a known flaky issue.', 'Beat me? At this point we\'re in a committed relationship — I\'m naming it in my will 😄', 'وقتی banter پرتاب می‌شود، ذهنِ مهندسِ ما آن را «سؤال» می‌گیرد و جوابِ اداریِ دقیق می‌دهد؛ اما سکوت یا تصحیحِ خشک بازی را می‌شکند و فضا را سرد می‌کند. جوابِ banter، خودِ banter است — اغراقِ مهربان.'),
  ],
  'drills': (
   'شوخی هم تمرین می‌خواهد؛ هر چهار را اول خودت بلند بگو، بعد پاسخ را باز کن.',
   [
    'هدفِ این شوخی را از آدم به قلمروی امن جابه‌جا کن: «You type so slow! 😂»',
    'شوخیِ خود-هدفی‌ات را دربارهٔ یک باگِ خودت بساز — فرمول: کارِ کوچکِ اشتباه + اغراقِ بزرگِ آرام + 😅',
    'همکار: «Ali, did the flaky test beat you again?» — با بانتر جواب بده، نه با گزارشِ فنی.',
    'شوخی به انگلیسی و لهجه‌ات خورد. مرز را خصوصی و آرام بگو — با پیشنهادِ هدفِ جایگزین.',
   ],
   [
    ('پاسخ تمرین ۱', 'نمونه: **"My keyboard has filed a formal complaint against me — honestly, the CI has more faith in my syntax than I do 😅"** هدف از همکار به خودت و ابزار منتقل می‌شود؛ شوخی می‌ماند، ریسکِ دل‌خوری صفر می‌شود.'),
    ('پاسخ تمرین ۲', 'نمونه: **"I spent forty minutes on a typo today — truly at the peak of my powers 😅"** ساختارِ طلایی: کارِ کوچکِ معلوم + اغراقِ بامزه؛ خودت تنها هدفی هستی که همیشه رضایتش را داری.'),
    ('پاسخ تمرین ۳', '**"Beat me? We\'re basically co-dependent now — it fails, I show up. A true partnership 😄"** فرمولِ جواب: بگیر، اغراقِ مهربان کن، ایموجی بگذار؛ ورودت به بازی، ورودت به جمع است.'),
    ('پاسخ تمرین ۴', '**"Hey, the speed jokes are all fair — but could we keep my English out of the banter? Roast my code all day, it deserves it 😄"** فرمولِ مرز: خصوصی + آرام + جایگزینِ بامزه — نود درصدِ موارد همان‌جا تمام می‌شود و رابطه سالم می‌ماند.'),
   ],
  ),
  'challenge': 'امروز در استندآپ یا چتِ تیم یک شوخیِ خود-هدفیِ یک‌خطی دربارهٔ کارِ خودت بگذار (با یک 😅) و اگر کسی banter پرتاب کرد، با بانتر جواب بده — ورود به بازی، ورود به تیم است.',
 },

 # ── درس ۸۶ ──────────────────────────────────────────────────────────────
 'english-technical-leadership': {
  'mistakes': [
   ('I think maybe we should possibly consider another approach.', 'The real problem here isn\'t the test suite — it\'s ownership.', 'ادبِ فارسی هر حکم را زیرِ سه لایه «فکر می‌کنم / شاید / بهتر باشد» دفن می‌کند؛ اما رهبریِ فنیِ انگلیسی حکمِ کوتاه می‌گوید و I think را حذف می‌کند. سه شاید، وزنِ پیام را به صفر می‌رساند و سیگنالِ «مطمئن نیستم» می‌فرستد.'),
   ('Sara, this task is for you. Good luck.', 'Sara, you own the flaky queue this quarter — I\'ll unblock you with time and air cover.', '«حله، برو» در فارسی سپردنِ کار است و تمامش؛ اما واگذاریِ سالمِ انگلیسی دو جمله دارد: مالکیت + پشتیبانی. مالکیتِ بی‌پشتیبانی، سپردنِ شکست است — Good luckِ تنها، تنهاییِ طرف را مستند می‌کند.'),
   ('Okay, I will fix it myself, it is faster.', 'What\'s your read? If you\'re stuck by Thursday, I\'ll pair with you — you keep the wheel.', 'مهندسِ سنیورِ فارسی‌زبان سریع‌ترین راه یعنی «خودم» را انتخاب می‌کند؛ اما جملهٔ رهبری اول فکرِ طرف را می‌پرسد تا رشد بسازد. هر جوابِ آمادهٔ بی‌ملاحظه، یک فرصتِ رشدِ خورده‌شده و یک گلوگاهِ تازه برایِ خودت است.'),
  ],
  'drills': (
   'تمرینِ این درس، حرف‌زدن مثل tech lead است؛ هر چهار جمله را اول خودت بگو، بعد پاسخ را باز کن.',
   [
    'جلسه روی «تست‌های بی‌ثبات» دعوا می‌کند. قاب را در دو جمله بکش: «مسئلهٔ واقعی X نیست — Y است.»',
    'این واگذاریِ ناقص را کامل کن: «Sara, fix the flaky tests. Good luck.»',
    'برایِ این دو تصمیم جملهٔ درست را انتخاب کن — «Reversible — let\'s try it» یا «This deserves an RFC»: (الف) تغییرِ متنِ دکمه، (ب) مهاجرتِ دیتابیس به موتورِ جدید.',
    'جملهٔ واحدِ «چکرِ گلوگاه» را بگو که با آن جلسهٔ ده‌دقیقه‌ایِ دوشنبه‌ها را اجرا می‌کنی.',
   ],
   [
    ('پاسخ تمرین ۱', '**"The real problem isn\'t flaky tests — it\'s ownership: nobody owns flakiness, so everybody fights symptoms."** قاب‌گذاریِ خوب کوتاه و حکم‌دار است؛ بیش از سه جمله دیگر قاب نیست — سخنرانی است.'),
    ('پاسخ تمرین ۲', '**"Sara, you own the flaky queue this quarter — not to fix every test, but to own the system that kills them. I\'ll unblock you: a fix-day each sprint, and I\'ll run air cover with the product team."** مالکیتِ روشن + تعریفِ موفقیت + پشتیبانیِ مشخص؛ واگذاریِ سالم همیشه این سه قطعه را با هم دارد.'),
    ('پاسخ تمرین ۳', '**الف: "Reversible — let\'s try it today." ب: "This deserves an RFC — one-way doors get writing."** تفکیکِ هزینهٔ تصمیم، گرامرِ روزانهٔ رهبریِ فنی است: درِ دوطرفه یعنی آزمایش، درِ یک‌طرفه یعنی سند و بحث.'),
    ('پاسخ تمرین ۴', '**"What are you waiting on, and who has it?"** یک جمله برایِ هر نفر، ده دقیقه برایِ کلِ جلسه؛ جواب‌ها را بنویس و تا بعدی‌شان دنبالشان برو — ارزان‌ترین جلسهٔ رهبریِ فنی که می‌شناسی.'),
   ],
  ),
  'challenge': 'دوشنبهٔ آینده جلسهٔ ده‌دقیقه‌ایِ گلوگاه را با همان یک جمله اجرا کن، و برایِ یکی از گلوگاه‌های باز، جملهٔ «You own this — I\'ll unblock you» را واقعاً به صاحبش بگو.',
 },

 # ── درس ۸۷ ──────────────────────────────────────────────────────────────
 'english-open-source': {
  'mistakes': [
   ('When will you fix this bug? It is very important for us.', 'Not sure if this is a bug or intended behavior — happy to close if it\'s a duplicate. If it\'s in scope, I\'d like to take a shot at a fix.', 'روتینِ فارسیِ پشتیبانی مستقیم ترجمه می‌شود: «کی درستش می‌کنید؟ برایِ ما مهم است.» اما متن‌باز داوطلبانه است؛ نگه‌دارنده پیمانکارِ تو نیست. جملهٔ تقاضا، issue را در صفِ سرد می‌خواباند؛ جملهٔ داوطلب، درِ مرج را باز می‌کند.'),
   ('I prepared one big PR: 3000 lines — new feature, docs, and refactor all together.', 'I\'ve split the work into three small PRs — the docs fix first, then the feature, then the refactor.', 'ذهنِ ما «کارِ بزرگ، PRِ بزرگ» را نشانِ جدیت می‌داند؛ فرهنگِ متن‌باز برعکس می‌خواند: PRِ کوچک هدیه است، PRِ غول‌آسا بارِ ریلویو. کسی که سه‌هزار خط می‌فرستد، عملاً «بعداً نگاه می‌کنم» خریده است.'),
   ('Sorry for my bad English and sorry if my question bothers you.', 'First time contributing here — let me know if I\'m missing any conventions. Happy to adjust anything.', 'عذرخواهیِ زنجیره‌ای از ادبِ فارسی می‌آید اما سیگنالِ بی‌اعتمادی می‌فرستد و سؤال را بی‌وزن می‌کند. سنجاقِ درست فقط یک جمله است: اعلامِ تازگی + دعوت به اصلاح — صداقتِ حرفه‌ای، نه خودکمتی.'),
  ],
  'drills': (
   'تمرینِ این درس، نوشتن مثل داوطلبِ محترمِ متن‌باز است؛ هر چهار را اول خودت بنویس، بعد پاسخ را باز کن.',
   [
    'اولین کامنتِ issue یا PR را بنویس: اعلامِ اولین مشارکت + دعوت به اصلاحِ قراردادها.',
    'زبانِ تقاضا را به زبانِ داوطلب بازنویسی کن: «Please fix this bug soon, it is urgent for us.»',
    'نگه‌دارنده می‌گوید: «We prefer tests in a separate file.» — جوابِ استاندارد را بده.',
    'PRِ دو‌هزارخطی‌ات هفته‌ها بی‌جواب مانده. پیامِ بازساختار را بنویس.',
   ],
   [
    ('پاسخ تمرین ۱', '**"First time contributing here — let me know if I\'m missing any conventions. I\'d like to take a shot at fixing the CLI docs; happy to adjust the scope to fit the roadmap."** سنجاقِ طلایی: تازگی + پیشنهاد + انعطاف؛ نصفِ اعتمادِ نگه‌دارنده همین‌جا ساخته می‌شود.'),
    ('پاسخ تمرین ۲', '**"Not sure if this is intended behavior — here\'s a minimal repro. If it\'s a real bug, I\'d be happy to take a shot at the fix."** تقاضا تبدیل می‌شود به مشاهدهٔ دقیق + دستِ کمکی؛ در متن‌باز داوطلب اول می‌نشیند و متقاضی آخر — همین ترتیب، نتیجه را عوض می‌کند.'),
    ('پاسخ تمرین ۳', '**"Makes sense — moved and pushed. Happy to adjust anything else that doesn\'t match the house style."** سه حرکتِ کوتاه: پذیرش، گزارشِ انجام، بازبودنِ ادامه — بدونِ دفاع از خود و بدونِ عذرخواهیِ اضافه.'),
    ('پاسخ تمرین ۴', '**"This grew bigger than any review should be — I\'m splitting it into three small PRs (docs, fix, refactor) so each can land on its own. Closing for now; the smaller ones follow today."** کوچک‌سازیِ داوطلبانه، امتیاز است نه عقب‌نشینی؛ نگه‌دارنده‌ها این پیام را نشانهٔ حرفه‌ای‌بودن می‌خوانند.'),
   ],
  ),
  'challenge': 'این هفته در یک پروژهٔ متن‌بازی که واقعاً استفاده می‌کنی، یک issue کوچکِ داکی یا تایپویی پیدا کن و با همان جملهٔ «First time contributing here…» کامنت بگذار — اولین مشارکت هرقدر کوچک، همان‌قدر واقعی است.',
 },

 # ── درس ۸۸ ──────────────────────────────────────────────────────────────
 'english-staff-interviews': {
  'mistakes': [
   ('It depends on the situation.', 'Depends on the read/write ratio — if it\'s read-heavy, I\'d cache first; if it\'s write-heavy, I\'d queue first.', '«بسته به موقعیت» در فارسی جوابِ کامل و حرفه‌ای است و ذهن همان را می‌فرستد؛ اما در مصاحبهٔ سطحِ staff، dependsِ برهنه طفره خوانده می‌شود. dependsِ دوتایی — گزینهٔ الف اگر…، گزینهٔ ب اگر… — نامِ دیگرِ تحلیل است.'),
   ('We did it org-wide — huge success, very big impact.', 'Honestly, it started with one team — but the pattern generalized: the checklist is now the default for three teams.', 'بزرگ‌نمایی از عادتِ تعریفِ فارسی می‌آید («مقاوم بود، عالی شد»)؛ اما مصاحبه‌گرِ staff ابزارِ شکارِ بزرگ‌نمایی را دارد. فرمولِ امن: دامنهٔ صادقانه + جملهٔ generalized — تعمیمِ الگو امتیازِ واقعی است، نه وسعتِ ادعا.'),
   ('To improve your code review, everyone must review within 24 hours.', 'First question back: what hurts most today — speed, quality, or tone? The fix is different for each.', 'ذهنِ ما جوابِ آماده را افتخار می‌داند و نسخهٔ اول را می‌فرستد؛ اما در سطحِ staff، سؤالِ برگردانِ شفاف‌ساز خودش امتیاز است — چارچوب و گوشِ دادن را هم‌زمان نشان می‌دهد و فرایندِ فکر را می‌فروشد، نه فقط جواب را.'),
  ],
  'drills': (
   'سطحِ staff یعنی جواب‌هایی که فرایندِ فکر را نشان می‌دهند؛ هر چهار را اول خودت بگو، بعد پاسخ را باز کن.',
   [
    'سؤال: «Should we put a cache or a queue in front of this service?» — جوابِ dependsِ دوتایی بده.',
    'داستانِ تو فقط یک تیم را گرفته، نه کلِ سازمان را. جملهٔ صداقت + تعمیم را بگو.',
    'مصاحبه‌گر: «How would you improve our code review process?» — با سؤالِ برگردان شروع کن.',
    'آزمایشِ دوسپرینتی‌ات جواب نداد. جملهٔ «اشتباهِ ارزان» را بگو.',
   ],
   [
    ('پاسخ تمرین ۱', '**"Depends on the read/write ratio — if it\'s read-heavy, I\'d cache first and measure the hit rate; if it\'s write-heavy, I\'d queue first and absorb the bursts."** گزینه + شرط + سنجش؛ همین ساختار، «طفره» را به «تحلیل» تبدیل می‌کند.'),
    ('پاسخ تمرین ۲', '**"Honestly, one team — but the pattern generalized: the staged-rollout checklist we wrote is now the default for three teams, and that\'s the part I\'d repeat anywhere."** دامنهٔ صادقانه، جملهٔ generalized و درسِ قابلِ انتقال؛ مصاحبه‌گرِ staff دنبالِ همین پُل از «یک تیم» به «سیستم» است.'),
    ('پاسخ تمرین ۳', '**"First question back: what hurts most today — speed, quality, or tone? The fix is different for each."** سؤالِ سه‌گزینه، امضای staff است: قبل از نسخهٔ تجویزی، فرایندِ تشخیص — همان‌طور که پزشکِ خوب اول می‌پرسد بعد نسخه می‌نویسد.'),
    ('پاسخ تمرین ۴', '**"Then I was wrong cheaply — two sprints, not two quarters. That\'s the whole point of small experiments: wrong fast, right eventually."** این جمله نشان می‌دهد برایِ اشتباه، بودجه و روش داری؛ ریسکِ محاسبه‌شده زبانِ روزمرهٔ سطحِ staff است.'),
   ],
  ),
  'challenge': 'یکی از تصمیم‌های فنیِ امسال را با فرمولِ دوتایی در دو جملهٔ انگلیسی بنویس و بلند بگو — «اگر الف، می‌کردم X؛ اگر ب، می‌کردم Y» — این قالب، جوابِ ثابتِ سؤال‌های «بستگی دارد»ی مصاحبه‌های آینده‌ات است.',
 },

 # ── درس ۸۹ ──────────────────────────────────────────────────────────────
 'english-continuous-learning': {
  'mistakes': [
   ('Yes, I know Kubernetes very well.', 'Conversational, not yet effortless — I ran our migration, but I\'m still working through the operator patterns.', '«بلدم» در فارسیِ مصاحبه‌ای رشد می‌کند و ذهن همان اطمینان را می‌فرستد؛ اما صداقتِ درجه‌دار حرفه‌ای‌تر است و در سؤالِ بعدی ریسکت را نمی‌سوزاند. ادعای very well، سؤالِ عمیق را دعوت می‌کند.'),
   ('I am learning English since two years.', 'I\'ve been learning English for two years — and it\'s starting to click.', 'فارسیِ «از دو سال پیش» با since + مدت ترجمه می‌شود؛ اما since فقط نقطهٔ زمان می‌گیرد (since 2023) و مدت با for می‌آید. و کاری که از گذشته تا حال ادامه دارد have been + ing می‌خواهد — زبانِ خودِ استمرارِ یادگیری.'),
   ('I watched forty tutorials this month — I am learning a lot.', 'I\'m turning my notes into a short post for the team channel — teaching it is how I check I really got it.', '«دیدم، خواندم، تمام شد» زبانِ مصرف است و ذهنِ فارسی یادگیری را با تعدادِ ورودی می‌سنجد؛ حرفه‌ایِ انگلیسی‌زبان از خروجی حرف می‌زند: پست، RFC، دموی کوچک. تولید، تنها مدرکِ فهمِ واقعی است.'),
  ],
  'drills': (
   'یادگیریِ پایدار، زبانِ خودش را دارد؛ هر چهار را اول خودت بگو، بعد پاسخ را باز کن.',
   [
    'در مصاحبه از Kubernetes می‌پرسند. سطحت را با صداقتِ درجه‌دار بگو.',
    'این جمله را درست کن: «I am learning English since two years.»',
    'جملهٔ خروجی بساز: به‌جایِ «I watched forty tutorials»، حرفِ یادگیرندهٔ تولیدکننده بزن.',
    'دربارهٔ چیزی که از پروژه‌ای یاد گرفتی — نه از دوره — جملهٔ picked up بساز.',
   ],
   [
    ('پاسخ تمرین ۱', '**"Conversational, not yet effortless — I ran our migration, but I\'m still working through the operator patterns."** درجه‌بندیِ صادقانه در سؤالِ بعدی گیرت نمی‌اندازد؛ بزرگ‌نمایی می‌اندازد — و اعتمادِ مصاحبه‌گر سرمایهٔ اصلی است.'),
    ('پاسخ تمرین ۲', '**"I\'ve been learning English for two years — and it\'s starting to click."** since فقط نقطهٔ زمان می‌گیرد (since 2023)، مدت با for می‌آید؛ و استمرارِ تا-امروز با have been + ing ساخته می‌شود.'),
    ('پاسخ تمرین ۳', '**"I\'m turning my notes into a short post for the team channel — teaching it is how I check I really got it."** مصرف را به تولید ترجمه کن؛ همین یک جمله، یادگیرندهٔ حرفه‌ای را از تماشاچیِ دوره‌ها جدا می‌کند.'),
    ('پاسخ تمرین ۴', 'نمونه: **"I picked up Kubernetes from the migration, not from a course — nothing teaches like carrying the pager."** یادگیریِ فرصت‌طلبانه در نگاهِ مصاحبه‌گر ارزنده‌ترین نوعش است؛ picked up را در معرفی‌ات بکار تا یادگیری‌ات داستانی و باورپذیر شود.'),
   ],
  ),
  'challenge': 'امشب «جملهٔ روز» را در دفترچه بنویس: یک جملهٔ انگلیسی که امروز توانستی و نود روز پیش نمی‌توانستی — و همین هفته یکی از یادداشت‌های خوانده‌شده‌ات را به یک پستِ دوپاراگرافی برایِ کانالِ تیم تبدیل کن.',
 },

 # ── درس ۹۰ ──────────────────────────────────────────────────────────────
 'english-final-roadmap': {
  'mistakes': [
   ('The course is finished, so now my English is complete.', 'The course is done — the habit is just starting. I\'m conversational, and the curve is still mine.', '«تمام شد» با «یاد گرفته شد» در ذهنِ فارسی یکی می‌شود؛ اما زبان عضله است نه کتاب — بستنِ دوره، بازکردنِ عادت است. جملهٔ درست، پایانِ دوره را جشن می‌گیرد و مسیر را باز نگه می‌دارد.'),
   ('I will practice more when I have free time.', 'My plan: full-English workweeks, one mock interview a month, one post a quarter — calendar-first, not mood-first.', '«وقتِ آزاد شد می‌خوانم» سرآغازِ هر برنامهٔ شکست‌خورده است؛ برنامهٔ زنده در تقویم می‌نشیند نه در انگیزه. انگلیسیِ حرفه‌ای برنامه را با زمان و عدد می‌گوید — when I have time در عمل یعنی هیچ‌وقت.'),
   ('My English is still weak — I must study much more.', 'Ninety days ago I rehearsed a coffee order; today I led a retro in English. That\'s the curve — and I\'m staying on it.', 'صدای «هنوز ضعیفم» عذرخواهیِ روزِ اول است و ادعای ضعف، انگیزه را می‌خورد؛ روایتِ رشد سه زمان را کنار هم می‌گذارد — نود روزِ پیش، امروز، بعد. همین پاراگراف، جوابِ «tell me about yourself» در مصاحبهٔ بعدیِ توست.'),
  ],
  'drills': (
   'درسِ آخر، آینه است: چهار تمرینِ بازاندیشانه را به انگلیسی و بلند برایِ خودت اجرا کن — این خودِ آزمونِ پایانِ دوره است، نه نمرهٔ پایان.',
   [
    'پاراگرافِ سه‌زمانه‌ات را بگو: نود روزِ پیش / امروز / فصلِ بعد.',
    'سه چیز را به انگلیسی بگو که نود روزِ پیش نمی‌توانستی و حالا می‌توانی.',
    'اگر بتوانی به «روزِ اولِ خودت» فقط یک جمله بگویی، چه می‌گویی؟ (به انگلیسی)',
    'قدمِ نودویکم را در یک جملهٔ تقویمی بگو: چه کاری، کِی، با چه عددی.',
   ],
   [
    ('پاسخ تمرین ۱', 'نمونه: **"Ninety days ago I couldn\'t order a coffee without rehearsing. Today I led a retro in English and joked in the standup. Next quarter I\'m going for the senior interview."** سه زمان، یک روایت — همین پاراگراف را تمیز نگه دار؛ جوابِ همیشگیِ «tell me about yourself» از اینجا می‌آید.'),
    ('پاسخ تمرین ۲', 'نمونه: **"I can run a standup, write an incident update under pressure, and push back politely in a review — none of that existed three months ago."** فهرست را بلند بگو؛ شنیدنِ صدای خودت روی این توانایی‌ها، سوختِ قدمِ نودویکم است.'),
    ('پاسخ تمرین ۳', 'نمونه: **"You won\'t need perfect grammar — you\'ll need the sentence you\'re willing to say badly."** جمله‌ای را انتخاب کن که واقعاً باورش داری؛ این جمله، امضای شخصیِ تو در پایانِ دوره است.'),
    ('پاسخ تمرین ۴', 'نمونه: **"Step ninety-one, tomorrow: full-English Monday — standup, one Slack thread, and my 1:1, all in English."** قدمِ اول باید تاریخ و عدد داشته باشد؛ برنامهٔ بی‌تقویم فقط آرزوست.'),
   ],
  ),
  'challenge': 'امروز پاراگرافِ سه‌زمانه‌ات را برایِ یک دوست ضبط کن یا در اپ ثبت کن، و فردا قدمِ ۹۱ را همان‌طور که نوشتی اجرا کن — دوره همین بود؛ بقیه مالِ خودت. That\'s the course — the rest is yours.',
 },
}

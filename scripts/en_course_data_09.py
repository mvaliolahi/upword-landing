# -*- coding: utf-8 -*-
"""Stage 1 · lessons 73-81 — فاز ۵: حرفه‌ای‌شدن (بخش اول)."""

LESSONS = [
# ───────────────────────────── درس ۷۳ ─────────────────────────────
{
 'slug': 'english-register-tone',
 'title': 'رجیستر و لحن؛ سه لایهٔ رسمیت که هر جمله‌ات را تعریف می‌کند',
 'desc': 'مهارتِ بالای گفتار: انتخابِ خودکارِ سطحِ رسمیت — به همکارت یکی بگو، به مدیرت نروンの دیگر، به مشتری سومی. با آزمونِ «جیبِ شلوار» و جدولِ جابه‌جاییِ جمله‌ها بین لایه‌ها.',
 'keywords': 'رجیستر زبانی, formal informal english, لحن کاری, formal vs casual',
 'answer': 'رجیستر یعنی «همان جمله، در لباس‌های مختلف»: Would you be able to review this? (رسمی) · Could you take a look? (نیمه) · Can you check this? (خودمانی). مهارتِ حرفه‌ای، نه دانستنِ سه لایه است؛ جابه‌جاییِ ناآگاهانهٔ آن‌هاست — که با آزمونِ «به چه کسی و در چه کانالی» تمرین می‌شود.',
 'intro': [
  'تا اینجا جمله‌ها را «درست» یاد گرفتی؛ از فاز ۵، «متناسب» را یاد می‌گیری — و متناسب‌بودن، همان چیزی است که در گوشِ مدیرِ ارشد، مشتری و همکار، صدای «یکی از خودمان» می‌دهد. در زبانِ مادری این کار خودکار است: با پدرت یک‌جور، با قاضی یک‌جور حرف می‌زنی. در زبانِ دوم باید ساخته شود — و خبرِ خوب: فقط سه لایه دارد و قواعدش قابل‌مشاهده.',
  'این درس، پایهٔ پنج درسِ بعدی است: هر جملهٔ جلسه‌گردانی، RFC، ارائه و مذاکره‌ای که در فاز ۵ می‌آید، اول از این درس «لباس» می‌گیرد.',
 ],
 'sections': [
  {'h2': 'سه لایه؛ جدولِ همان-جمله در سه لباس',
   'blocks': [
    ('table', ['خودمانی (کَنال/همکار)', 'نیمه‌رسمی (اسلک/جلسه)', 'رسمی (ایمیل/مدیر ارشد/مشتری)'],
     [['Can you check this?', 'Could you take a look when you get a chance?', 'Would you be able to review this at your convenience?'],
      ['I need this by Friday.', 'Could we target Friday for this?', 'Would it be possible to complete this by Friday?'],
      ['That won\'t work.', 'I\'m not sure that approach will hold up.', 'I have concerns about whether this approach will scale.'],
      ['Sorry, my bad.', 'Apologies — that one\'s on me.', 'I take full responsibility for the oversight.'],
      ['Ping me if anything.', 'Feel free to reach out with questions.', 'Please do not hesitate to contact me should you need anything.']]),
    ('p', 'سه نشانهٔ گرامریِ لایه‌ها: **۱) فعلِ مدرن-رسانه:** can → could → would be able. **۲) مجهول و فاصله:** در رسمی، فاعل دور می‌شود و «possibility/concern» می‌آید. **۳) علامت‌های چسبیده به خودمانی: حذفِ فاعل (Got it / Checking now), ایموجی، و exclamation — که در رسمی هر سه حذف می‌شوند. و آزمونِ انتخاب، آزمونِ «جیبِ شلوار» است: **این پیام را اگر روی کاغذ از جیبِ شلواری که پاره شده پیدا کنند، چند نفرِ رئیسِ تو باید بخواند؟** صفر → خودمانی. یکی-دو → نیمه. سه و بالاتر → رسمی.'),
   ]},
  {'h2': 'کجا اشتباه می‌کنیم؛ خطاهای رایجِ لایه',
   'blocks': [
    ('p', 'سه خطای پرتکرارِ غیرِبومی: **۱) رسمیِ بیش‌ازحد در اسلک:** "Dear Jack, I would like to kindly inquire…" — در چت، خشکِ عجیب است؛ همان "Hey Jack, quick question" درست است. **۲) خودمانیِ بی‌محتاط در ایمیلِ مشتری:** "No worries, we\'ll fix it asap 👍" — با مشتری: "Understood — we\'ll have the fix deployed today; I\'ll confirm once it\'s live." **۳) شوخیِ فروریخته در لایهٔ اشتباه:** طنزِ خودمانی در کانالِ مشتری/مدیرِ ارشد، حتی اگر بامزه باشد، ریسکِ بی‌فاصله‌ای دارد — شوخی را در جایی بگذار که رابطه اش می‌کشد. قاعدهٔ نجات: **در تردید، یک لایه رسمی‌تر از حدِ ظاهرِ محیط —** و هرگز دو لایه پایین‌تر.'),
    ('ex', 'Understood — the fix is in review now. I\'ll confirm once it\'s live in production. Thank you for your patience.', 'متوجه شدم — فیکس در ریلویوئه. بعد از لایو شدن در prod تأیید می‌دم. ممنون از صبرِ شما. (رسمی، حرفه‌ای، بدونِ لختی)'),
   ]},
  {'h2': 'لحنِ سازمانی؛ فرهنگِ شرکت را بخوان',
   'blocks': [
    ('p', 'هر شرکت یک «رجیسترِ سازمانی» دارد که در هفتهٔ اول می‌خوانی: استارتاپِ جوان = خودمانیِ گسترده حتی با مدیرعامل; بانک و ادارهٔ دولتی = نیمه‌رسمیِ پایه; مشاورهٔ بین‌المللی = رسمیِ مشتری-محور حتی داخلی. راهِ تشخیص، «نمونه‌برداری» است: نامه‌های عمومیِ مدیران و پیام‌های PRهای قدیمی را ببین و همان سطح را در پلهٔ خودت اجرا کن. و قانونِ طلاییِ انتخاب: **دست‌کم به اندازهٔ سطحِ متوسطِ محیط، خودمانی نکن و یک لایه محتاط‌تر بنویس؛ صدایت در طولِ زمان، خودش «اجازهٔ» پایین‌آمدن می‌گیرد.**'),
   ]},
 ],
 'takeaway': 'رجیستر، سه لباسِ یک جمله است: خودمانی (Can you check?), نیمه (Could you take a look?), رسمی (Would you be able to review?). نشانه‌ها: فعلِ could/would، فاصله‌انداختنِ فاعل، حذفِ ایموجی و کوتاه‌سازی. آزمونِ جیبِ شلوار سطح را می‌گوید و قانونِ طلایی: در تردید، یک لایهٔ رسمی‌تر. صدای حرفه‌ای، «درست» نیست؛ «متناسب» است.',
 'faq': [
  ('اگر لایه را اشتباه رفتم — مثلاً خیلی خودمانی نوشتم به مدیر ارشد؟',
   'بزرگش نکن: خطرِ واقعی، «پایین‌رفتنِ ارزیابی» نیست، «خوانده‌شدنِ جمله»ست. اصلاحِ ظریف: در همان رشته، سطح را بالا ببر بدونِ عذرخواهیِ بزرگ: بعد از پیامِ خودمانیِ نا‌خواسته، ادامه بده رسمی‌تر — گفتگو خودش متعادل می‌شود. اگر واقعاً گیر داد (شوخیِ بی‌جا به رئیسِ رئیس‌ها), یک جمله بس: **"Sorry — that came out more casual than I meant. The serious version: I\'m concerned about the timeline."** (ببخشید — خودمانی‌تر از منظورم دراومد. نسخهٔ جدی: به تایم‌لاینِ این کار نگرانم.) — عذرخواهیِ طولانی، خطا را بزرگ‌تر از خودش می‌کند.'),
  ('انگلیسیِ بریتانیایی و آمریکایی در رجیستر چه فرقی دارند؟',
   'بریتانیایی‌ها در لایهٔ رسمی نرم‌تر و غیرمستقیم‌ترند (ممکن است «that\'s interesting» یعنی مخالفند!) و «please do not hesitate» و «I would be grateful if» را بیشتر می‌آورند؛ آمریکایی‌ها حتی در رسمی، مستقیم‌تر و فعل‌محورترند («Let\'s get this done»). با مخاطبِ بریتانیایی، غیرمستقیمی را نشانهٔ بی‌حرفی نخوان — و با آمریکایی، مستقیم‌بودنش را نشانهٔ بی‌احترامی. برای تیم‌های بین‌المللی، سبکِ آمریکاییِ معتدل پیش‌فرضِ امن است.'),
 ],
},
# ───────────────────────────── درس ۷۴ ─────────────────────────────
{
 'slug': 'english-work-idioms',
 'title': 'اصطلاحاتِ کاری؛ بیست idiom که در هر جلسه‌ای می‌شنوی',
 'desc': 'اصطلاحاتِ محبوبِ دفاترِ انگلیسی‌زبان: low-hanging fruit, move the needle, get up to speed, in the loop — با معنی، مثالِ جلسه‌ای و ریسکِ استفادهٔ اشتباه.',
 'keywords': 'اصطلاحات کاری انگلیسی, business idioms, low hanging fruit, move the needle',
 'answer': 'جلسه‌های کاریِ این‌ها پر از اصطلاح است: "Let\'s grab the low-hanging fruit first" یعنی کارِ سادهٔ زودبازده را بزنیم؛ "keep me in the loop" یعنی در جریانم نگه دار. این درس بیست اصطلاحِ پرتکرار را با مثالِ واقعی می‌دهد — و قرمزترین خط: اصطلاح را که مطمئن نیستی، استفاده نکن؛ ساده‌بودن، بی‌اعتباریِ بومی-نما ندارد.',
 'intro': [
  'اصطلاحات، «چاشنیِ» گفتارِ کاری‌اند: دو کلمه که معنایی غنی می‌رسانند و غیبتشان، مکالمه را سالم اما «بی‌نوا» می‌کند. اما برای زبانِ دوم، دو رو دارند: فهمیدنشان ضروری است (وگرنه نصفِ جلسه را از دست می‌دهی), استفاده‌کردنشان ریسک دارد (کالِ تازه‌رسیده با دو idiomِ ناجا، بومی‌نمایِ خنده‌دار است).',
  'راهبردِ این درس: **همه را بشناس، سه-چهار تا را شخصی کن** — اصطلاح‌هایی که با لحنِ تو و فرهنگِ تیمت جورند و در جایِ درست، طبیعی از دهانت می‌آیند.',
 ],
 'sections': [
  {'h2': 'اصطلاحاتِ کار و برنامه؛ ده‌تای اول',
   'blocks': [
    ('table', ['اصطلاح', 'معنی', 'جملهٔ جلسه'],
     [['low-hanging fruit', 'کارِ سادهٔ زودبازده', 'Let\'s grab the low-hanging fruit first — the quick wins.'],
      ['move the needle', 'اثرِ واقعی گذاشتن', 'One banner ad won\'t move the needle for revenue.'],
      ['get up to speed', 'به‌روز شدن/جاافتادن', 'I\'m still getting up to speed on the payments system.'],
      ['in the loop', 'در جریانِ اطلاعات', 'Keep me in the loop on the migration, please.'],
      ['touch base', 'هماهنگیِ کوتاه', 'Let\'s touch base Monday about the launch.'],
      ['on the same page', 'هم‌نظر/هم‌برداشت', 'Before we build — are we all on the same page?'],
      ['ballpark figure', 'عددِ حدودی', 'Give me a ballpark — is this weeks or months?'],
      ['by the book', 'طبقِ قاعده', 'Security review has to be by the book on this one.'],
      ['go the extra mile', 'بیش از وظیفه', 'She went the extra mile and wrote the docs too.'],
      ['cover all the bases', 'پوششِ همهٔ جبهه‌ها', 'The test suite covers all the bases for refunds.']]),
   ]},
  {'h2': 'اصطلاحاتِ ریسک و زمان؛ ده‌تای دوم',
   'blocks': [
    ('table', ['اصطلاح', 'معنی', 'جملهٔ جلسه'],
     [['at the eleventh hour', 'در آخرین لحظه', 'We fixed it at the eleventh hour — phew.'],
      ['behind the eight ball', 'در وضعیتِ بد', 'The team\'s behind the eight ball after the outage.'],
      ['a blessing in disguise', 'خیری در ظاهرِ بد', 'The failed launch was a blessing in disguise — we found the data bug.'],
      ['cut corners', 'زیرکاری/بی‌کیفیت‌کاری', 'We can\'t cut corners on the audit — no way.'],
      ['think outside the box', 'خلاقانه فکرکردن', 'The budget\'s fixed, so let\'s think outside the box.'],
      ['back to the drawing board', 'بازگشت به طرحِ اول', 'The vendor pulled out — back to the drawing board.'],
      ['on the back burner', 'اولویتِ پایین', 'The redesign is on the back burner until Q3.'],
      ['a steep learning curve', 'یادگیریِ سختِ سریع', 'Kubernetes has a steep learning curve — plan for it.'],
      ['learn the ropes', 'قواعدِ اولیه را یادگرفتن', 'Two weeks in, I\'m still learning the ropes here.'],
      ['raise the bar', 'استاندارد را بالا بردن', 'That PR raised the bar for the whole team.']]),
    ('p', 'نکتهٔ استفاده: اصطلاح، «فشردهٔ فرهنگی» است — جای درستش جمله را کوتاه و قوی می‌کند (به‌جای «بی‌مورد» اسم‌آوردن). اما دو خطای مرگبار: **دو اصطلاحِ باهم‌نچسب در یک جمله** («Let\'s touch base and grab the low-hanging fruit to move the needle» — سالادِ اصطلاحی!) و **اصطلاحِ نیمه‌یاد در موقعیتِ رسمی.** راهِ تثبیت: هر هفته فقط یک اصطلاح را «مالِ خودت» کن — در سه موقعیتِ واقعی استفاده‌اش کن و بعد برو سراغِ بعدی.'),
   ]},
 ],
 'takeaway': 'بیست اصطلاح را بشناس تا هیچ جلسه‌ای در سکوتِ فهمیدنی نماند؛ سه-چهار تا را مالِ خودت کن تا گفتارت لهجهٔ دفتر بگیرد. اولویتِ شخصی‌سازی: get up to speed, in the loop, ballpark, on the same page — چهارتای پرکاربردِ بی‌ریسک. و قانون: هرگز سالادِ اصطلاحی نساز و اصطلاحِ نیمه‌یاد را به جلسهٔ مهم نبر.',
 'faq': [
  ('اصطلاح را که می‌گویم و کسی نمی‌خندد/جا نمی‌افتد — یعنی درست بوده؟',
   'اصطلاحِ درست، معمولاً «بدونِ واکنش» می‌گذرد — چون طبیعی است؛ خنده یا ابرو، معمولاً خبرِ ناجایی است. برای سنجش، دو محک: ۱) در جای مشابه، آدم‌های محترمِ تیمت هم همین را می‌گویند؟ ۲) جمله با حذفِ اصطلاح هم می‌ایستد اما طولانی‌تر می‌شود؟ اگر هر دو بله، استفاده‌اش درست بوده. و بهترین آزمایشگاه: کانالِ اسلکِ خودمانیِ تیم — idiom را آنجا امتحان کن، نه جلسهٔ بزرگ.'),
  ('از کجا idiomهای تازه را دنبال کنم بدونِ غرق‌شدن؟',
   'سه منبعِ درجه‌یک: ۱) **جلسه‌های خودت** — هر اصطلاحِ ناشناسی را همان روز به آپورد بیفزا (متن + معنی + جملهٔ خودت). ۲) پادکست/ویدئوی industry: Lex Fridman برای فنی، اپیزودهای leadership برای مدیریتی. ۳) خبرنامه‌های اکتشافی مثل HBR یا TLDR که idiomهای تازهٔ کاری را در متنِ واقعی می‌آورند. قاعده: هفته‌ای حداکثر سه اصطلاحِ تازه — بیشتر از آن، ورودی است نه یادگیری.'),
 ],
},
# ───────────────────────────── درس ۷۵ ─────────────────────────────
{
 'slug': 'english-phrasal-verbs-work',
 'title': 'Phrasal verbs کاری؛ فعل‌های دوتکه‌ای که دفتر را می‌چرخانند',
 'desc': 'phrasal verbsِ پرکاربردِ کار: follow up, run into, point out, plug in — با جدولِ prepositionهای خائن (look over vs overlook) و الگوی «یک هفته، سه فعل».',
 'keywords': 'phrasal verbs, فعل های عبارتی, follow up, work phrasal verbs',
 'answer': 'phrasal verb یعنی فعل + حرفِ اضافه = معنای تازه: give + up ≠ «دادن بالا»؛ یعنی «تسلیم‌شدن». در دفترِ انگلیسی، این دوتکه‌ای‌ها همه‌جا هستند: follow up, point out, run into, sort out. این درس بیست تا را می‌دهد و تلهٔ جدی را می‌خواباند: یک حرف، کل معنا را عوض می‌کند.',
 'intro': [
  'phrasal verbs، رؤیای بدِ زبان‌آموزان و ناگزیرِ گفتارِ کاری‌اند: انگلیسی‌زبان‌ها حتی وقتی فعلِ ساده هست، دوتکه‌ای را ترجیح می‌دهند — «contact me» نه، **reach out to me**؛ «postpone» نه، **push back the deadline**. برای تو، راه‌حلِ فاز ۵: گروه‌بندیِ معنایی + استفادهٔ کنترل‌شده — همین‌طور که در درس ۷۴ با اصطلاحات کردیم.',
  'قاعدهٔ امیدوارکننده: بیست فعلِ این درس، احتمالاً در هر روزِ کاری‌ات حداقل پنج بار صدا می‌شوند. بلندشدنِ آن‌ها، «گفتارِ دفتری» تو را یک پله بومی‌تر می‌کند — با کمترین هزینهٔ گرامری.',
 ],
 'sections': [
  {'h2': 'گروهِ ارتباط و پیگیری؛ شش فعلِ هر روز',
   'blocks': [
    ('table', ['فعل', 'معنی', 'جمله'],
     [['follow up (on)', 'پیگیری‌کردن', 'I\'ll follow up on that ticket today.'],
      ['reach out (to)', 'تماس‌گرفتن/رجوع‌کردن', 'Reach out to the platform team if it persists.'],
      ['point out', 'اشاره‌کردن/متذکرشدن', 'She pointed out a flaw in the migration plan.'],
      ['run into', 'به مشکل/آدم برخوردن', 'I ran into an issue with the sandbox.'],
      ['get back to (someone)', 'بازگشتن با جواب', 'Let me check and get back to you by 3.'],
      ['loop in', 'اضافه‌کردن کسی به گفتگو', 'Looping in Sara — she owns the billing service.']]),
   ]},
  {'h2': 'گروهِ کار و مشکل؛ هفت فعلِ اجرا',
   'blocks': [
    ('table', ['فعل', 'معنی', 'جمله'],
     [['sort out', 'حل‌وفصل‌کردن', 'We\'ll sort out the permissions tomorrow.'],
      ['work out', 'جواب‌دادن/حل‌شدن', 'The numbers work out — we can ship.'],
      ['set up', 'راه‌انداختن', 'Set up the staging DB before the demo.'],
      ['roll out', 'عرضه/پخش‌کردن', 'We\'ll roll out to 5% of users tonight.'],
      ['scale up', 'بزرگ‌کردن ظرفیت', 'The autoscaler scales up on traffic spikes.'],
      ['break down', 'خراب‌شدن/تجزیه', 'The migration breaks down into three steps.'],
      ['take on', 'به‌دوش‌کشیدن کار', 'I can\'t take on another project this quarter.']]),
    ('p', 'و گروهِ زمان/مذاکره: **push back** (عقب‌انداختن/مخالفت‌کردن — معنی دوگانه‌ی مفید: "I have to push back on that timeline" = مخالفت؛ "Let\'s push back the launch a week" = جابه‌جایی), **hold off** (مکث: "Let\'s hold off until the audit"), **put off** (به تعویق‌انداختن: "Don\'t put off the upgrade — debt grows"), **call off** (لغوکردن: "They called off the migration").'),
   ]},
  {'h2': 'تله‌ها؛ حرفِ اضافه همه‌چیز است',
   'blocks': [
    ('p', 'سه جفتِ خائن که در ایمیل‌های واقعی فاجعه می‌سازند: **look over vs overlook:** "Please look over the doc" = لطفاً مرورش کن؛ "Please overlook the doc" = لطفاً نادیده‌اش بگیر (چرا؟!) — **go over vs go overboard:** مرورکردن vs زیاده‌روی‌کردن. **carry out vs carry on:** اجراکردن vs ادامه‌دادن/شلوغ‌کردن. و ساختِ گرامری: اگر مفعول ضمیر کوتاه است، وسط می‌آید: **follow it up** ✓ (نهِ follow up it ✗)؛ اما اسم، هر دو جا: follow up the ticket / follow the ticket up. جدی‌ترین توصیهٔ این درس: هر phrasal verb تازه را با «جملهٔ کامل» به آپورد اضافه کن نه با ترجمهٔ تنها — معنایش در preposition است و جمله، تنها قفسِ امنش.'),
   ]},
 ],
 'takeaway': 'بیست فعلِ دوتکه‌ای: گروهِ پیگیری (follow up, get back to, loop in, reach out) + گروهِ اجرا (sort out, set up, roll out, scale up, take on) + گروهِ زمان (push back, hold off, put off, call off). تله‌ها یک‌حرفی‌اند: look over ≠ overlook. و مفعولِ ضمیر، وسط می‌نشیند: follow it up. یادگیری: هفته‌ای سه فعل با جملهٔ کامل — گفتارِ دفتری‌ات بعد از یک ماه، صدای دیگر می‌دهد.',
 'faq': [
  ('چرا انگلیسی این‌قدر phrasal verb دارد؟ راه‌پله نیست؟',
   'تاریخش جواب است: انگلیسی سه لایهٔ واژگانی دارد — آنگلوساکسنی (ساده), فرانسوی (رسمی), لاتینی (علمی) — و phrasal verbs، لایهٔ «سادهِ قدیم»‌اند: give up (آنگلوساکسنی) هم‌معنای surrender (فرانسوی) و capitulate (لاتینی). در دفتر، لایهٔ عام و دوستانه همان دوتکه‌ای‌هاست؛ لایهٔ لاتینی برای متن‌های حقوقی و آکادمیک. پس انتخاب‌ات را آگاهانه کن: ایمیلِ رسمی می‌تواند postpone بگوید، اسلک همان put off را دوست دارد.'),
  ('جدا-نویسی و خط تیره در phrasal verbs؟',
   'قاعدهٔ ساده: فعل و اضافه جدا می‌نویسند (follow up ✓ نهِ followup)، اما اسم‌شده‌اش می‌چسبد یا خط تیره می‌گیرد: "a follow-up", "the rollout", "a sign-off". در ایمیلِ رسمی، اسم‌ها را با خط تیره ببین: follow-up, sign-off, back-up — سبک‌ها کمی فرق دارند اما خط تیره هیچ‌وقت خطا نیست. و ضمیرِ کوتاه وسط: "I\'ll follow it up" — همین دو قاعده، نود درصدِ نگارشیِ phrasal verbs را پوشش می‌دهد.'),
 ],
},
# ───────────────────────────── درس ۷۶ ─────────────────────────────
{
 'slug': 'english-leading-meetings',
 'title': 'جلسه‌گردانی؛ از «بزنیم شروع» تا «جمع‌بندی و اکشن‌ها»',
 'desc': 'زبانِ رهبریِ جلسه: بازگشاییِ هدفمند, مدیریتِ انحراف (let\'s park that), دادنِ کلمه (Ali, you\'ve dealt with this — thoughts?), و بستنِ با خلاصه + مسئول + ضرب‌الاجل. اولین قدمِ حرفه‌ایِ رهبریِ فنی.',
 'keywords': 'جلسه گردانی, leading meetings, meeting phrases, مدیریت جلسه انگلیسی',
 'answer': 'جلسهٔ خوب سه بند دارد: باز (Here\'s the goal for the next 30 minutes), بدنه (مدیریتِ انحراف و مشارکت), بند (Let me summarize: Ali owns X by Friday). جمله‌های طلایی: "Let\'s park that for now" (انحراف را کنار می‌گذارد), "I want to make sure we hear from everyone", و "What\'s the decision — A or B?"',
 'intro': [
  'جلسه‌گردانی، همان جایی است که مهارتِ فنی به رهبریِ کلامی ترجمه می‌شود — و اولین مسئولیتی که در آن صدای «فوقِ خودت» را می‌شنوی. برای زبانِ دوم، نکتهٔ رهایی: جلسهٔ خوب، گفتارِ خیره‌کننده نمی‌خواهد؛ ساختارِ صریح می‌خواهد — و ساختار، از حفظ‌شدنی‌ترین چیزهاست.',
  'این درس پنج موقعیتِ کلیدی را می‌دهد: شروع، انحراف، مشارکت، تصمیم و بستن — همه با دو-سه جملهٔ قالب. درس ۷۷ (RFC و نوشتار) و ۷۸ (ارائهٔ اجرایی) رهبریِ کلامی را به سطوحِ دیگر می‌برند.',
 ],
 'sections': [
  {'h2': 'بازگشایی؛ هدف و قاعده در ۶۰ ثانیه',
   'blocks': [
    ('ex', 'Thanks everyone. Goal for the next 30 minutes: decide how we handle the migration downtime. I\'d like us to leave with a decision, not just options. Let\'s start with two minutes of context from Sara.', 'ممنون از همه. هدفِ این ۳۰ دقیقه: تصمیم دربارهٔ توقفِ مایگریشن. می‌خوام با تصمیم بیرون بریم، نه فقط گزینه. با دو دقیقه زمینه از سارا شروع کنیم.'),
    ('p', 'قالبِ بازگشایی = تشکرِ یک‌ثانیه‌ای + هدفِ مشخص + محصولِ مطلوب + مسیر: **"Goal: X. I\'d like us to leave with Y. Agenda: five minutes of context, then options, then a call."** این سی‌کلمه، نصفِ جلسه را از بی‌هدفی نجات می‌دهد. اگر جلسه را تو نگذاشتی و می‌خواهی رهبریش کنی (فرصتِ طلاییِ غیررسمی): **"Can I suggest a quick agenda so we get through this?"** — پیشنهادِ ساختار، محترمانه‌ترین تصاحبِ جلسه است.'),
   ]},
  {'h2': 'بدنه؛ انحراف، مشارکت، تصمیم',
   'blocks': [
    ('p', '**انحراف:** "That\'s an important point — can we park it for the next sync? I\'ll add it to the doc." (مهمه — کنارش بذاریم برای جلسهٔ بعد؟ تو داک می‌نویسمش.) «پارک» با ثبتِ مکتوب، انحراف را بی‌زخم می‌خواباند. **مشارکت:** "Ali, you\'ve dealt with this system — what\'s your read?" (علی، تو با این سیستم سر و کله زدی — ارزیابیت چیه؟) — سوالِ مستقیمِ محترمانه، سکوت‌های ناامن را می‌شکند و آدم‌های ساکت را وارد می‌کند. **تصمیم‌گیری:** "We have two viable options. What do we need to know to pick one?" و بندِ تصمیم: **"Straw poll — quick thumbs up or down on Option A?"** (رأیِ سرانگشتی — موافقِ گزینهٔ A؟) — «straw poll» یعنی رأیِ سریعِ غیرِرسمی؛ ابرازِ رأی در جلسه را نرم می‌کند.'),
   ]},
  {'h2': 'بستن؛ خلاصه + مالک + ضرب‌الاجل',
   'blocks': [
    ('p', 'قالبِ بستنِ معجزه‌گر (سه‌بندی): **"Let me summarize: we\'re going with the blue-green deployment (تصمیم). Ali owns the runbook (مسئول), due Thursday EOD (زمان). Sara flags the blockers in the channel as they come up (پایش). Anything I missed?"** — جملهٔ آخر همیشه بیاید: "Anything I missed?" — پرسشِ نهایی، حرفه‌ای‌بودن را با فروتنی کامل می‌کند. بعد از جلسه، همین سه بند را در پیام/ایمیل بفرست: **"Recap: decision, owners, deadlines — corrections welcome."** جلسه‌ای که recap دارد، ادامهٔ حادثه نیست؛ زنجیرهٔ تصمیم است.'),
    ('ex', 'We\'re at time. Let me recap the three action items — Ali, the runbook by Thursday; Sara, the alert thresholds; I\'ll book the go/no-go for Monday. Thanks all — good meeting.', 'وقت تموم شد. بذار سه تا اقدام رو جمع‌بندی کنم — علی، ران‌بوک تا پنجشنبه؛ سارا، آستانه‌های هشدار؛ من هم جلسهٔ گو/نو-گو رو برای دوشنبه می‌ذارم. ممنون همه — جلسهٔ خوبی بود.'),
   ]},
 ],
 'takeaway': 'رهبریِ جلسه = بازگشاییِ سه‌تکه (هدف + محصول + مسیر) + ابزارِ انحراف (park it + ثبت) + مشارکت (سوالِ مستقیم: what\'s your read?) + تصمیم (straw poll) + بستنِ سه‌بندی (خلاصه + مالک + ضرب‌الاجل) + recapِ پس‌جلسه. هیچ‌کدام بلاغت نمی‌خواهد؛ ساختارِ ازحفف — و همین ساختار است که تو را «آدمِ جلسه‌ها» می‌کند.',
 'faq': [
  ('در جلسه، یک نفر همه‌جا حرف می‌زند و بقیه ساکت‌اند!',
   'سه ابزارِ محترمانه: **۱) بریدنِ نرم و برگرداندن:** "That\'s a solid take, Jack. Sara, your team feels this directly — what\'s your view?" **۲) گردشِ ساختاریافته:** "Let\'s go around quickly — one sentence each." (سری بزنیم — هر نفری یک جمله.) **۳) کانالِ جایگزین:** "Let\'s hear from the quiet side of the table first." (اول بشنویم از سمتِ ساکتِ میز.) هیچ‌وقت نفرِ پرحرف را «ساکت شو» نکن — همان جملهٔ بریدنِ نرم، صد بار امتحان‌شده است و روحیهٔ جلسه را نگه می‌دارد.'),
  ('جلسه‌های من همیشه «چت» می‌شوند و تصمیمی نمی‌گیرند!',
   'قبل از جلسه، خودت را مسلح کن به «ماهیتِ جلسه»: type را اعلام کن — "This is a decision meeting" (جلسهٔ تصمیم), "This is a brainstorm" (طوفانِ فکری), یا "This is a status sync" (هماهنگیِ وضعیت). اعلامِ نوع در دقیقهٔ اول، رفتارِ همه را قالب می‌کند. و اگر وسطِ تصمیم، بحث داغِ جانبی سبز شد: "This feels like a new topic — separate 15 minutes, or take it to the thread?" جلسه‌های بی‌تصمیم معمولاً «جلسه‌های بی‌نوع»‌اند؛ نوع‌گذاری، درمانِ نود درصد است.'),
 ],
},
# ───────────────────────────── درس ۷۷ ─────────────────────────────
{
 'slug': 'english-writing-rfcs',
 'title': 'RFC و پروپوزال فنی؛ متنی که تصمیمِ بزرگ را می‌سازد',
 'desc': 'نوشتارِ تصمیم‌ساز: ساختارِ RFC (context, proposal, trade-offs, alternatives), لحنِ «مستند نه متکبر», و چرخهٔ بازخورد — از draft تا decision. جایی که فاز ۴ (ADR) به مقیاسِ سازمانی می‌رسد.',
 'keywords': 'rfc, پروپوزال فنی, technical proposal, design document',
 'answer': 'RFC، «پیشنهادِ تصمیم» به شکلِ سند است: زمینه (چرا الان؟), طرح (چی می‌سازیم), بدیل‌ها (چرا نه این‌ها؟), پیامدها (چه چیزی بهتر/بدتر می‌شود). فرمولِ لحن: مستند و بی‌لحنِ شخصی — "The trade-off section is where the document earns its keep." سندِ خوب، بحث را از اتاقِ جلسه به متنِ داوری‌پذیر می‌برد.',
 'intro': [
  'در شرکت‌های فنیِ بزرگ، تصمیم‌های معماری در «سند» گرفته می‌شوند نه در جلسه: کسی یک RFC می‌نویسد (Request for Comments — درخواستِ نظر), تیم چند روز کامنت می‌گذارد، و تصمیم با سابقه‌ی مکتوب متولد می‌شود. برای تو، دو دلیلِ یادگیری: اول، نوشتنِ RFC، پلهٔ رهبریِ فنی است — سندِ تو، صدای تو را در اتاق‌هایی می‌برد که درشان نیستی. دوم، خواندنِ RFCهای دیگران، نصفِ درکِ فرهنگِ فنیِ هر شرکت است.',
  'این درس، RFC را با همان چارچوبِ گفتاریِ درس ۶۸ (مخالفتِ فنی) پیوند می‌زند — با این تفاوت که این‌جا همه‌چیز نوشتاری، سرد و داوری‌پذیر است.',
 ],
 'sections': [
  {'h2': 'ساختارِ پنج‌بندی؛ استخوانِ هر RFC',
   'blocks': [
    ('p', '**۱) Summary — یک پاراگراف:** "This RFC proposes moving session storage from Redis to DynamoDB, to remove the single-region limit before the EU launch." (این RFC انتقالِ session از Redis به DynamoDB را پیشنهاد می‌دهد تا محدودیتِ تک-ریجن قبل از عرضهٔ اروپا رفع شود.) **۲) Context — چه مسئله‌ای، چرا الان:** داده بیاور: "EU users see +180ms; churn in that cohort is up 2%." **۳) Proposal — چی می‌سازیم:** بلوک‌به‌بلوک، با شکل. **۴) Alternatives considered — بدیل‌ها و چرا نه:** مهم‌ترین بندِ سند (از نظرِ خواننده‌های سنیور!). **۵) Consequences and risks — پیامدها و ریسک‌ها:** چه چیزی ساده‌تر و چه چیزی سخت‌تر می‌شود؛ migration و rollback کجاست. و بندِ صفرِ فرهنگی: **Status: Draft** و **author + reviewers + deadline for comments** بالای سند.'),
    ('ex', '## Alternatives considered\n1. **Redis Global Datastore** — rejected: still a single write region; failover is manual.\n2. **Client-side tokens** — rejected: logout-everywhere and revocation become a distributed-systems problem.\n3. **Do nothing until EU revenue justifies it** — rejected: the latency is measurable today.', 'بدیل‌های بررسی‌شده — هر کدام با یک خطِ «ردشده» و دلیلِ یک‌جمله‌ای. همین بند، نیمی از کامنت‌های تکراری را قبل از نوشتن‌شدن می‌کُشد.'),
   ]},
  {'h2': 'لحن؛ مستند، فروتن، بیِ «منِ پیروز»',
   'blocks': [
    ('p', 'سه قاعدهٔ لحن: **۱) معیار، نه سلیقه:** به‌جای "Redis is bad at this" — "Redis single-region writes cap our failover time at ~90s (see load test, appendix A)." **۲) پیروزی را به بدیل هم بده:** "Option 1 would be reasonable if our EU traffic stays under 10% — it doesn\'t (34% and growing)." **۳) نقاطِ نفوذ را اعلام کن:** "The strongest objection I anticipate is team X\'s on-call load; mitigation is in §6." — پیش‌بینیِ مخالفت و پاسخِ مقدماتی‌اش، تو را از دوجنگِ کامنت‌ها نجات می‌دهد. و یک قاعدهٔ طلاییِ متنِ تصمیم: **جملهٔ پرسش‌دار در RFC ممنوع — یا می‌دانی و می‌نویسی، یا در بخشِ open questions با پاسخ‌گِ نامزد می‌آورد.**'),
   ]},
  {'h2': 'چرخهٔ بازخورد؛ از Draft تا Decision',
   'blocks': [
    ('p', 'آیینِ انتشار: پیش‌نمایشِ خصوصی به دو-سه نفرِ کلیدی (**"Early feedback welcome — is the framing right?"**), بعد انتشارِ عمومی با ضرب‌الاجل: "Comments open until Friday EOD; after that we decide." پاسخ به کامنت‌ها — هنرِ ظریفِ RFC: هر کامنتِ معقول را با نام‌برکردن جواب بده (**"Good point — added a mitigation paragraph in §4.2"**) و مخالفتهای بنیادین را نه با جوابِ تک‌خطی، که با دعوت به گفتگو: **"This deserves more than a comment reply — 30 minutes this week?"** بندِ پایانیِ تصمیم: **"Decision: proceeding with the proposal, with the amendments from the review. Owner: platform team. Revisit: after EU launch metrics, ~3 months."** — سندی که این بند را دارد، بسته شده؛ بقیه، پیش‌نویسِ جاودان‌اند.'),
   ]},
 ],
 'takeaway': 'RFC = Summary یک‌پاراگرافی + Context با داده + Proposal بلوک‌به‌بلوک + Alternatives با «ردشده: دلیل» + Consequences و rollback. لحن: معیار نه سلیقه، حقِ بدیل، پیش‌پاسخِ مخالفتِ پیش‌بینی‌شده. چرخه: پیش‌نمایشِ خصوصی → انتشار با ضرب‌الاجل → پاسخِ نام‌برده به کامنت‌ها → بندِ Decision. متنِ خوب، جلسه را به داوریِ سرد تبدیل می‌کند — و برنده‌اش، تیم است.',
 'faq': [
  ('RFC و ADR چه فرقی دارند؟ کجا کدام؟',
   'ADR، دفترِ ثبتِ تصمیم‌هایِ «گرفته‌شده» است: کوتاه، بی‌بحث، آرشیوی (درس ۵۹). RFC، فرایندِ «گرفتنِ» تصمیم است: بلند، بحث‌خور، اجتماعی. مسیرِ رایج: RFC بحث و جمع می‌شود → نتیجه‌اش به شکلِ ADR ثبت می‌شود. در شرکتِ کوچک، RFC ممکن است همان یک‌صفحه‌ی design doc باشد؛ در بزرگ، سندِ چندصفحه‌ای با reviewers رسمی. تو همیشه با همان چارچوبِ پنج‌بندی شروع کن و اندازه را با فرهنگِ جای‌گذاشتنت تنظیم کن.'),
  ('اولین RFCام را دربارهٔ چه بنویسم؟',
   'بهترین اولین RFC، کوچک و واقعی است: چیزی که خودت می‌خواهی در سه ماه آینده بسازی. قالبِ پیشنهادی برای شروع: «ارتقای X از نسخهٔ Y به Z» یا «افزودنِ ابزارِ L به پایپ‌لاین» — زمینه‌اش داده‌پذیر است و بدیل‌هایش مشخص. از معماریِ کلانِ سیستم شروع نکن: سندِ بزرگِ اول، هم اعتبارت را در گروی تجربه می‌گذارد هم بازخوردش سخت می‌شود. RFC موفقِ اول = سندِ هفت‌صفحه‌ایِ «کوچکِ تمام‌شده»، نه چهل‌صفحه‌ایِ «بزرگِ نیمه‌تمام».'),
 ],
},
# ───────────────────────────── درس ۷۸ ─────────────────────────────
{
 'slug': 'english-exec-presentations',
 'title': 'ارائه برای مدیران؛ پنج دقیقه، سه عدد، یک تصمیم',
 'desc': 'سخت‌ترین مخاطب: مدیرِ عاملِ بی‌وقت. ساختارِ ارائهٔ اجرایی: نتیجه اول (answer first), سه عدد, ریسک‌ها و درخواستِ مشخص — و هنرِ سوالِ «خلاصه‌اش چیه؟» که تو از قبل جوابش را داده‌ای.',
 'keywords': 'ارائه اجرایی, executive presentation, ارائه برای مدیران, answer first',
 'answer': 'مدیرِ ارشد، مهندسِ حضانت نیست: در پنج دقیقه، نتیجه و عدد و تصمیم می‌خواهد. فرمول: نتیجه اول ("We can cut checkout latency 40% by March — it needs one engineer for six weeks"), سه عددِ پشتیبان, ریسکِ صادقانه, و درخواستِ مشخص. جزئیات؟ ضمیمه و سوالِ «می‌خواهید عمیق شوم؟»',
 'intro': [
  'ارائهٔ اجرایی، پرخطرترین پنج دقیقهٔ حرفه‌ایِ توست: مخاطب، روزی ده تصمین می‌گیرد، حوصلهٔ «چطور ساخته شد» ندارد و اگر در سی ثانیهٔ اول نتیجه را نشنود، گوشش خاموش می‌شود. اما همین مخاطب، بهترینِ دنیا در «شنیدنِ ساختار» است: اگر نتیجه-اول و عدد و درخواست بدهی، حتی در کوتاه‌ترین زمان، تو را دعوت به لایهٔ بعدی می‌کند.',
  'این درس، قالبِ ارائهٔ اجرایی و سه صحنهٔ مرزی (قطع‌شدن، سوالِ «خلاصه‌اش؟», وسوسهٔ ورود به جزئیات فنی) را می‌دهد — تکمیل‌کنندهٔ درس ۶۴ (دمو) و ۵۳ (توضیحِ غیرِفنی).',
 ],
 'sections': [
  {'h2': 'نتیجه اول؛ سی ثانیهٔ سرنوشت‌ساز',
   'blocks': [
    ('ex', 'Short version up front: we can cut checkout latency by 40% before the March launch. It costs one engineer for six weeks and no new infrastructure. I\'ll walk you through why I\'m confident — and what I\'d need from this group.', 'نسخهٔ کوتاه اول: می‌تونیم تأخیرِ تسویه رو ۴۰٪ کم کنیم قبل از عرضهٔ مارس. هزینه‌ش یک مهندس برای شش هفته‌ست و هیچ زیرساختِ جدید نمی‌خواد. می‌گم چرا مطمئنم — و از این جمع چی می‌خوام.'),
    ('p', 'فرمولِ سی‌ثانیه: **نتیجه + هزینه + درخواست**. مخاطبِ اجرایی با همین سه، تصمیمش را قالب می‌کند؛ بقیهٔ ارائه، «باز کردنِ» همین سه است. اگر عددِ کلیدی داری، در همین سی ثانیه بیاور: "40%" یا "2.1 million" — عددِ بزرگِ اول، انگشتِ ذهنِ مدیر را قفل می‌کند. و توصیهٔ حرفه‌ای: همین پاراگراف را **در اسلایدِ اول** هم بگذار؛ مدیرِ عمدتاً-اسلایدی، خلاصه را از صفحه می‌خواند نه از دهان.'),
   ]},
  {'h2': 'سه عدد و یک ریسک؛ بدنهٔ پنج‌دقیقه‌ای',
   'blocks': [
    ('p', 'بدنه = سه عدد + یک ریسک + یک مقایسه. **سه عدد:** امروز چیست؟ (p99 = 1.4s) · بعد از کار چه می‌شود؟ (0.8s) · چه چیزی می‌سازد؟ (هر ۰/۱ ثانیه سریع‌تر = ۰/۷٪ بیشترِ تسویهٔ کامل — بر اساسِ A/B ربعِ قبل). **ریسکِ صادقانه:** "The risk is the migration window: two weekends of read-only mode for the reports page. Mitigation: we ship behind a flag and roll back in minutes if conversion dips." (ریسک، پنجرهٔ مایگریشنه: دو آخرِ هفته فقط-خواندنی برای صفحهٔ گزارش‌ها. جبران: پشتِ فلگ عرضه می‌کنیم و اگر نرخِ تبدیل افت کرد، در دقیقه‌ها برمی‌گردونیم.) — اعلامِ ریسک با جبران، امضای حرفه‌ای‌هاست؛ مخاطبِ اجرایی از ارائهِ «بی‌ریسک» می‌ترسد، نه از ریسکِ گفته‌شده.'),
   ]},
  {'h2': 'درخواست و صحنه‌های مرزی',
   'blocks': [
    ('p', 'درخواستِ پایانی، سه‌سنجه: **"The ask: approve the six-week assignment this week. Decision needed by Friday so we make the March freeze."** (درخواست: تخصیصِ شش‌هفته‌ای این هفته تأیید شود. تصمیم تا جمعه، تا فریزِ مارس را بگیریم.) صحنه‌های مرزی: **سوالِ «خلاصه‌اش چیه؟» وسطِ ارائه:** "The one-liner: 40% faster checkout, one engineer, six weeks — and my ask is the approval." (خلاصه در یک خط: ...) — پاسخِ آماده‌ی تو از قبل، نجات است. **قطع‌شدن:** "Absolutely — I\'ll land the plane here: the ask stands." (کاملاً — همین‌جا فرود میام: درخواست سرِ جاشه.) **وسوسهٔ جزئیات:** اگر سوالِ فنیِ عمیق شد: "Great question — short answer now, appendix has the deep dive. Happy to schedule a tech session with your team." — ارائهٔ اجرایی، بلیتِ جلسهٔ فنیِ بعدی هم هست.'),
   ]},
 ],
 'takeaway': 'ارائهٔ اجرایی = نتیجه+هزینه+درخواست در سی ثانیه + سه عدد و یک ریسکِ جبران‌دار + درخواستِ تاریخ‌دار. سوالِ «خلاصه؟» را خودت جواب داده‌ای؛ جزئیات را به ضمیمه و جلسهٔ فنی بفرست. مخاطبِ ارشد «چطور» نمی‌خواهد؛ «چند» و «چه‌زمان» و «چه‌ریسکی» می‌خواهد — و تو همان‌ها را در همان ترتیب می‌دهی.',
 'faq': [
  ('مدیران فنی هم همین قالب را می‌خواهند؟',
   'مدیرِ فنیِ خوب، همان قالب را با ضخامتِ بیشتر می‌خواهد: نتیجه اول را می‌شنود، بعد سه عدد، بعد می‌پرسد «چطور» — و این‌جا جای ورودِ فنی توست: دو-سه اسلایدِ معماریِ مقدماتی، آماده در ضمیمه. اشتباهِ رایج، شروعِ ارائه از معماری برای مدیرِ فنی است؛ او هم اول «چرا و چند» می‌خواهد، بعد «چطور». قالب یکی است؛ فقط عمقِ لایهٔ سوم فرق می‌کند.'),
  ('جلسهٔ exec من پنج دقیقه هم نیست — سی ثانیه در راهرو است!',
   'نسخهٔ راهرویی (elevator pitchِ اجرایی)، همان سی‌ثانیهٔ اول است که فقط: **"We can make checkout 40% faster before March — one engineer, six weeks. Can I book 15 minutes for the numbers?"** (می‌تونیم تسویه رو تا مارس ۴۰٪ تندتر کنیم — یک مهندس، شش هفته. ۱۵ دقیقه برای اعداد رزرو کنم؟) درخواستِ کوچکِ جلسه، بلوکِ سازندهٔ راهرو است. تمرینش: همین یک جمله را برای سه پروژهٔ واقعیِ خودت بنویس و بلند بگو — «راهرو»، استیجِ تمرینِ رایگانِ هر شرکتی است.'),
 ],
},
# ───────────────────────────── درس ۷۹ ─────────────────────────────
{
 'slug': 'english-salary-negotiation',
 'title': 'مذاکرهٔ حقوق؛ عدد، سکوت و «بستهٔ کامل»',
 'desc': 'گفتارِ پول: جابه‌جاییِ رنج (What\'s the range for this role?), شمارشِ معکوسِ پیشنهاد (Is there flexibility?), و مذاکرهٔ محترمانهٔ بسته (base, equity, sign-on, remote) — با دیالوگِ کامل و جملهٔ طلاییِ سکوت.',
 'keywords': 'مذاکره حقوق انگلیسی, salary negotiation, job offer negotiation, compensation',
 'answer': 'مذاکرهٔ حقوق سه گفتگو دارد: قبل از عدد (رنج را از آن‌ها بگیر: What range is budgeted for this role?), روی عدد (Is there flexibility? + سکوت), و روی بسته (equity و sign-on و remote هم مذاکره‌اند). جملهٔ طلایی: "I\'m really excited about the role — I\'m confident we can align on the numbers." مذاکره، جدال نیست؛ هم‌راستاسازی است.',
 'intro': [
  'پول، ناتوان‌کننده‌ترین موضوعِ گفتاریِ حرفه‌ای است — در هر زبانی؛ در زبانِ دوم، دو برابر. اما حقیقتِ بازارِ انگلیسی‌زبان: مذاکرهٔ محترمانه، انتظار است نه جسارت؛ پیشنهادِ اول معمولاً جایِ حرکت دارد؛ و «بله»ی بی‌مذاکرهٔ تازه‌واردان، ده‌ها هزار دلارِ مسیرِ حرفه‌ای را یک‌جا می‌سوزاند.',
  'این درس، سه مرحله را با دیالوگِ واقعی می‌دهد + دو مهارتِ غیرِزبانیِ حیاتی: سکوتِ بعد از عدد و کلمه‌گذاریِ «excited» که بحث را از تقابل به هم‌راستایی می‌برد.',
 ],
 'sections': [
  {'h2': 'قبل از عدد؛ رنج را از آن‌ها بگیر',
   'blocks': [
    ('ex', 'Recruiter: What are your salary expectations? — You: I\'m flexible for the right fit. Could you share the range budgeted for this role? That\'s the fastest way to see if we align.', 'کارگزین: انتظارِ حقوقیت چنده؟ — تو: برای جایِ درست انعطاف دارم. رنجِ بودجه‌شده برای این نقش رو می‌گید؟ سریع‌ترین راهِ هم‌راستایی همینه.'),
    ('p', 'قاعدهٔ اول: **عددِ اول را تو نگو.** جملهٔ برگردانِ استاندارد: **"I\'d rather not anchor first — could you share the range for the position?"** و اگر اصرار کردند به عددِ تو: رنجِ واقعیِ خودت را با «بستهٔ کامل» بگو نه عددِ خشک: **"Based on the market and my experience, I\'m looking at 130 to 150 base, plus equity — and I\'m open to creative structures."** (رنجِ ۱۳۰-۱۵۰ پایه به‌علاوهٔ سهام — و به ساختارهای خلاقانه هم بازم.) رنج بده، نه یک عدد؛ سقفش را هم بالاتر از هدفِ واقعی‌ات بگذار چون مذاکره سقف را می‌شکند.'),
   ]},
  {'h2': 'روی عدد؛ انعطاف، سکوت، شمارشِ معکوس',
   'blocks': [
    ('p', 'پیشنهاد آمد (مثلاً ۱۲۰). سه‌قدمیِ پاسخ: **۱) گرمی:** "Thank you — I\'m genuinely excited about this role." **۲) قلابِ انعطاف:** "Based on my research and the scope we discussed, I was targeting the 140-150 range for base. Is there flexibility on your side?" **۳) سکوت.** — سکوتِ بعد از سوالِ مذاکره‌ای، سنگین‌ترین ابزارِ توست: دو-سه ثانیهِ مکث، فضایِ «فشارِ فکر» را به آن‌ها منتقل می‌کند؛ زبانِ دوم‌ها از ترسِ سکوت، سریع جملهٔ بعدی را می‌گویند و عدد را می‌بخشند. اگر گفتند «رنجِ محدودی داریم»: **"Understood. What about the other levers — sign-on bonus or an equity refresh? Together those could close the gap."** (متفانم. اهرم‌های دیگه چطور — پاداشِ استخدام یا سهامِ تکمیلی؟ اونا با هم می‌تونن شکاف رو ببندن.)'),
    ('ex', 'If the base is fixed at 120, could we look at a 10k sign-on and a review at six months with agreed raise criteria? That would work for me.', 'اگه پایه روي ۱۲۰ قفله، می‌شه سراغِ ۱۰هزار پاداشِ استخدام و بررسیِ شش‌ماهه با معیارهایِ توافقِ حقوقی بریم؟ برام جواب می‌ده.'),
   ]},
  {'h2': 'بستهٔ کامل و بستنِ محترمانه',
   'blocks': [
    ('p', 'پنج اهرمِ مذاکره: **base** (پایه), **equity/stock** (سهام — پرسشِ کلیدی: "What\'s the vesting schedule?" — زمان‌بندیِ تعلق), **sign-on bonus** (پاداشِ استخدام — اهرمِ محبوبِ پرکردنِ شکافِ پایه), **remote/relocation** (ریموت، روزهای هفتگی، جابه‌جایی), و **review clause** (بندِ بررسی: "Can we agree on a six-month review with a raise to X if I meet the goals we set?"). بستن: هرگز live قبول/رد نکن: **"Thank you — this is a big decision. Could I get this in writing and come back by Thursday?"** (ممنون — تصمیمِ بزرگیه. می‌شه مکتوبش رو بفرستید تا پنجشنبه جواب بدم؟) و اگر رفتی که قبول کنی: **"I accept with pleasure — I\'m excited to start. Just to confirm in writing: 130 base, 10k sign-on, first review in June."** — قبولِ مکتوب‌شده، بیمهٔ سوءتفاهمِ اولینِ حقوق است.'),
   ]},
 ],
 'takeaway': 'مذاکره = رنج را از آن‌ها بگیر (عدد اولِ مهمانی نگو) + پاسخِ سه‌قدمی به پیشنهاد (گرمی → قلابِ انعطاف → سکوت) + اهرم‌های پنج‌گانه (base, equity, sign-on, remote, review) + هیچ‌وقت live قبول نکن، مکتوب بگیر و مکتوب قبول کن. لحنِ همیشه: «excited + align» — مذاکرهٔ حرفه‌ای، رقابتِ دوطرفه برای ساختنِ یک پیشنهادِ «بله»-پذیر است.',
 'faq': [
  ('از من «عددِ فعلی‌ام» را پرسیدند — بگویم؟',
   'در اکثرِ بازارهای انگلیسی‌زبان (به‌جز کالیفرنیا و چند ایالتِ آمریکایی که قانوناً ممنوعش کرده), پرسش رایج است و دروغ‌گویی ریسکِ فسخ دارد. سه پاسخِ امن: ۱) انحرافِ استاندارد: **"My current package isn\'t really comparable — different market and role. The range I\'m targeting for THIS role is…"** (بستهٔ فعلیام قابلِ مقایسه نیست — بازار و نقشِ فرق داره. رنجِ هدفم برای «این» نقش…) ۲) صداقتِ هدفمند اگر می‌خواهی بگویی: عددِ کلِ بسته (پایه+سهام+پاداش) را بگو نه پایهٔ تنها. ۳) اگر قانونِ محل از پرسش جلوگیری می‌کند: «I believe that question isn\'t allowed under the local pay-transparency law» — جملهٔ آرامِ حفاظتی.'),
  ('پیشنهادِ عالی بود و خجالت دارم مذاکره کنم!',
   'قاعدهٔ تجربیِ مربیانِ شغلی: حتی بهترینِ پیشنهادها هم یک اهرمِ بی‌هزینه دارند — تاریخِ شروع، روزهای دورکاری، بودجهٔ یادگیری، عنوانِ شغلی. یک مذاکرهٔ سبکِ «همه‌گیرِ محترمانه»: **"I\'m thrilled with the offer. Two small things before I sign: could I start on the 15th instead of the 1st, and is there a learning budget attached to the role?"** (از پیشنهام فوق‌العاده خوشحالم. قبل از امضا دو نکتهٔ کوچیک: شروع از ۱۵ام ممکنه؟ و بودجهٔ یادگیریِ نقش هست؟) — این «مذاکرهٔ نمادین»، عضلهٔ مذاکره را برای روزِ پیشنهادِ بعدی می‌سازد و هیچ پیشنهادی را خراب نمی‌کند. سکوتِ همیشگی، عادتِ خطرناکِ حرفه‌ای است؛ مذاکرهٔ کوچک، واکسنِ مذاکرهٔ بزرگ است.'),
 ],
},
# ───────────────────────────── درس ۸۰ ─────────────────────────────
{
 'slug': 'english-remote-async',
 'title': 'کارِ ریموت و async؛ نوشتاری‌بودنِ حرفه‌ای',
 'desc': 'زبانِ تیمِ پخش‌درجهکان: پیامِ بلندپایه (over-communicate), داکِ تصمیم‌ساز, ساعاتِ هم‌پوشانی و احترامِ timezoneها, و آدابِ «بیدار ببینمت» در فرهنگِ ناهم‌زمان — remote انگلیسیِ خودش را می‌خواهد.',
 'keywords': 'کار ریموت انگلیسی, async communication, remote work phrases, timezone etiquette',
 'answer': 'در تیمِ ریموت، نوشتارِ تو صدایت است: over-communicate (بیش از حد شفاف بنویس), هر تصمیم را داک کن, و timezone را در هر پیام احترام کن (I\'ll be offline from 3pm CET). سه جملهٔ کلیدی: "Here\'s my take — async comments welcome until tomorrow 10am CET." async حرفه‌ای، تصمیم را به «سند» و توافق را به «ضرب‌الاجلِ مکتوب» می‌سپارد.',
 'intro': [
  'ریموت و async، آیندهٔ بخشِ بزرگی از کارِ فنی‌اند — و برای زبانِ دوم، دو خبر: سخت‌تر است چون نوشتارِ مداوم می‌خواهد (هر «آه» و «لبخندِ» گفتاری از دست می‌رود), و آسان‌تر است چون زمانِ فکر، کاملاً مالِ توست: پاسخ‌هایت، بهترین نسخهٔ جمله‌هایت می‌توانند باشد.',
  'این درس، سه مهارتِ async را می‌دهد: نوشتارِ شفاف (پیامِ کامل + زمینه + درخواست + ضرب‌الاجل), مدیریتِ timezone (احترامِ اعلامی), و آیینِ «حضورِ معنادار» در کانال‌ها — همان چیزهایی که در دفتر، خودکار جبران می‌شدند.',
 ],
 'sections': [
  {'h2': 'پیامِ بلندپایه؛ فرمولِ over-communication',
   'blocks': [
    ('p', 'پیامِ asyncِ خوب، چهاربندی: **زمینه:** "The payment service started timing out after last night\'s deploy (context)." **وضعیت:** "I\'ve rolled back and errors are back to baseline (status)." **اقدام:** "Investigating the connection-pool theory — will know more by 14:00 UTC (action)." **درخواست:** "No action needed from you yet; flagging for visibility (ask)."** — بندِ آخر، طلایی است: «visibility» (رؤیت) بدونِ «اکشن»، تیم را بی‌دردسر در جریان می‌گذارد. قاعدهٔ async: هر پیام باید «تنها» بتوانِ فهمیدنش — readerای که تازه بیدار شده و اعلان‌های ۴۰تایی دارد. و ضرب‌الاجلِ نظرخواهی: **"Comments welcome until 10:00 CET tomorrow — silence = agreement."** (تا ۱۰ صبح فردا نظرات، سکوت = موافقت) — جملهٔ پایانی، تصمیمِ async را از «بی‌پایان» نجات می‌دهد.'),
   ]},
  {'h2': 'Timezone و آدابِ حضور؛ ساعت را احترام کن',
   'blocks': [
    ('p', 'سه آیینِ timezone: **۱) اعلامِ ساعت با منطقه:** "I\'m offline 15:00-21:00 CET (school pickup + dinner)." — ساعتِ محلیِ تو + دلیلِ کوتاه، هم‌پوشانی را می‌سازد. **۲) پرسشِ هم‌پوشانی:** "What\'s a good 2-hour overlap for us? I\'m flexible mornings." **۳) تحویلِ بستهٔ در خواب:** "Tagging you before I log off — no rush, it\'s for tomorrow morning your time." (قبل از لاگ‌اوف تگت می‌کنم — عجله‌ای نیست، برای صبحِ شماست.) و در تقویم: ساعت‌های focus و offline خودت را بگذار و کانالِ عمومی را درباره‌شان آگاه کن: "Deep-work blocks 09:00-12:00 — Slack responses will be slow." async حرفه‌ای، ساعت‌هایش را با دیگران تقسیم می‌کند، نه فعالیتش را.'),
    ('ex', 'Apologies for the late reply — your message landed at 2am my time. Answered above; and for the future, the thread works great for me!', 'عذر می‌خوام جواب دیر شد — پیامت ۲ بامداد وقتِ من رسید. بالا جواب دادم؛ و برای آینده، thread برای من عالیه!'),
   ]},
  {'h2': 'تصمیم و داک؛ همان جلسه، اما نوشتاری',
   'blocks': [
    ('p', 'جای جلسه در async، سند است: هر تصمیمِ واقعی، یک رشته/داک با جمع‌بندی: **"Decision: we\'re going with the queue-based approach (rationale in the RFC). Owners: @sara (infra), @ali (client). Deadline: Friday EOD CET. Dissent window: 24h — speak now or commit."** (تصمیم: صف‌محور می‌رویم — دلایل تو RFC. مالک‌ها… ضرب‌الاجل… مهلتِ مخالفت ۲۴ ساعت — حالا بگویید یا متعهد شوید.) — «speak now or commit»، اصطلاحِ محبوبِ async برای همان disagree-and-commitِ درس ۶۸ است. و آیینِ صوتیِ هدفمند: وقتی متن داغ شد، ویدئو بگیر نه چت: **"This is getting heated in text — 15 minutes of video now?"** — async حرفه‌ای، ابزار را با «دامنهٔ احساسِ» پیام عوض می‌کند.'),
   ]},
 ],
 'takeaway': 'async حرفه‌ای = پیامِ چهاربندی (زمینه/وضعیت/اقدام/درخواست) + «visibility, no action» برای خبرِ بی‌درز + ضرب‌الاجلِ نظر با «silence = agreement» + احترامِ اعلامیِ timezone + تصمیمِ داکی با «speak now or commit». نوشتارِ تو، صدای توست — پس بیش از حد شفاف بنویس: در ریموت، over-communication، ادب است نه افسارگسیختگی.',
 'faq': [
  ('احساس می‌کنم در تیمِ ریموت «نامرئی» شده‌ام!',
   'نامرئی‌شدن، بیماریِ خاموشیِ async است و درمانش «روایتِ عمومیِ پیشرفت» است: آپدیتِ هفتگیِ سه‌خطی در کانالِ تیم: **"Week recap: shipped retry v2 (PR#841); stuck on the vendor sandbox — ticket open; next week: load test. Good week, all things considered."** (جمع‌بندیِ هفته: retry نسخهٔ ۲ شِپ شد؛ روی سندباکسِ فروشنده گیرم — تیکت بازه؛ هفتهٔ بعد: تستِ بار.) به‌علاوه، حضورِ حادثه‌ایِ کوچک: کامنتِ واقعی روی PRها و پیروزی‌ها، مشارکتِ کوتاه در threadها — ده دقیقه در روز، تو را در «رادار» نگه می‌دارد. مدیرِ ریموت، همیشه بیشتر از کارِ تو، «روایتِ» کارِ تو را می‌بیند — پس روایت را تو بنویس.'),
  ('async برای من یعنی «همیشه آنلاین»! حد مرز چیه؟',
   'مرز را «اعلام‌شده» کن تا احترام‌شده شود: ساعتِ لاگ‌اوف را در پروفایل/وضعیت بگذار ("Offline after 18:00 CET — will respond tomorrow"), پیام‌های غیرِاورژانس را برای فردا جمع کن نه جوابِ شبه‌شبانه, و انتظارِ پاسخِ فوری را با قالبِ اعلام، آموزش بده: "Not urgent — whenever you\'re online." (فوریتی نیست — وقتی آنلاین شدی.) و ابزارِ قوی: در تنظیمات، ارسالِ پیام را schedule کن به ساعاتِ کاریِ گیرنده — پیامِ ساعتِ ۲ بامدادِ تو، ساعتِ ۹ صبحِ او می‌رسد؛ مرزِ او را هم رعایت کرده‌ای. async حرفه‌ای، هم مرز می‌گیرد هم می‌دهد.'),
 ],
},
# ───────────────────────────── درس ۸۱ ─────────────────────────────
{
 'slug': 'english-cross-team-politics',
 'title': 'ارتباطِ بین‌تیمی و سازمان؛ نفوذِ بدونِ اختیار',
 'desc': 'مکالمهٔ سازمانی: گرفتنِ وقتِ تیمِ دیگر (asynchronous ask), حلِ وابستگیِ متوقف‌کننده, «سیاستِ» بی‌آلودگی (map the players), و مکالمهٔ skip-level که سالم اجرا شود — مهارتِ مهندسِ تأثیرگذار.',
 'keywords': 'ارتباط بین تیمی, cross team collaboration, سازمان, influence without authority',
 'answer': 'کارِ بزرگ، هرگز تنها انجام نمی‌شود — و تیمِ دیگر، زیرِ دستِ تو نیست. زبانِ نفوذ: درخواستِ زمینه‌دار (We\'re blocked on X — what works for your team?), اعتبارِ پرداختی (I\'ll owe you one review), و نقشهٔ افراد (who owns what, who trusts whom). جملهٔ کلیدی: "What would make this easy for your side?"',
 'intro': [
  'وقتی کار از مرزِ تیم می‌گذرد، زبانِ تو دو چالشِ تازه می‌گیرد: اول، «اختیار» نداری — تیمِ دیگر به تو گزارش نمی‌دهد و باید با نفوذ ببری، نه دستور. دوم، «زمینه» ندارند — آن‌ها نمی‌دانند چرا کارِ تو مهم است و تو باید داستانش را بفروشی، کوتاه و منصفانه.',
  'این درس چهار موقعیتِ محوری را می‌دهد: درخواستِ بین‌تیمی، وابستگیِ متوقف‌کننده، disagreementِ بین‌تیمی، و skip-level. «سیاست» را هم بی‌رنج می‌خوانیم: نقشهٔ افراد و منافع، همان‌قدر معماری است که دیاگرامِ سرویس‌ها.',
 ],
 'sections': [
  {'h2': 'درخواستِ بین‌تیمی؛ زمینه + اندازه + معاوضه',
   'blocks': [
    ('ex', 'Hi team — we\'re two weeks from the EU launch, and we\'re blocked on the rate-limit config (one-line change on your side, I\'ve drafted the PR). What\'s the smoothest way to get 15 minutes of your review time this week? Happy to trade a review of yours.', 'سلام تیم — دو هفته تا عرضهٔ اروپا مونده و روی کانفیگِ rate-limit بلاکیم (یک‌خطی تغییر سمتِ شماست، PRش رو نوشتم). نرم‌ترین راه برای گرفتنِ ۱۵ دقیقه ریلویوی شماها این هفته چیه؟ درِ عوضش یه ریلویوی شما رو می‌کنم.'),
    ('p', 'فرمولِ درخواستِ نفوذی: **زمینهٔ یک‌جمله‌ای** (چرا مهم است — برایشان، نه برایت) + **اندازهٔ واقعی کار** (one-line change / 15 minutes — کوچک‌نماییِ صادقانه) + **کارِ انجام‌شده از طرفِ تو** (PR آماده، داک نوشته) + **معاوضه** (review-for-review, docs, credit). و اعلامِ deadline با دلیل: "…this week, because the config freeze is Friday." — درخواستِ خوبِ بین‌تیمی، کارِ فکریِ نصف‌شده را تحویل می‌دهد، نه «نیازِ خام».'),
   ]},
  {'h2': 'وابستگیِ گره‌خورده؛ تشدیدِ محترمانه',
   'blocks': [
    ('p', 'وقتی درخواست بی‌جواب یا بی‌نتیجه ماند، نردبانِ تشدید (هر پله، یک هفته): **۱) یادآوریِ کانال:** "Just bumping this — is there anything blocking it on your side?" **۲) کانالِ دوم/سومی:** "Sharing this in your team channel for visibility." **۳) مدیریت‌به‌مدیریت:** "I\'ve looped in our managers to help us find a slot — nothing dramatic, just calendar math." (مدیرها رو آوردم که یه وقت پیدا کنیم — خبری نیست، فقط حسابِ تقویم.) **۴) مسیرِ جایگزین:** "If this week truly doesn\'t work, we\'ll ship the feature flag off and turn it on when the config lands — flagging the trade-off to the PM." — پلهٔ چهارم، هنرِ بزرگ است: نشان بده که راهِ بسته را با مسیرِ جایگزین باز می‌کنی؛ این «بدنه»، بیشترین نفوذ را می‌سازد و کمترین دشمنی. هرگز از پلهٔ یک چهار را رد نکن.'),
   ]},
  {'h2': 'نقشهٔ بازیگران و skip-level سالم',
   'blocks': [
    ('p', '**نقشه:** برای هر پروژهٔ بین‌تیمی، سه ستون یادداشت کن: چه کسی تصمیم می‌گیرد (decision-maker), چه کسی اجرا می‌کند (doer), چه کسی نظرش وزن دارد (influencer) — و برای هرکدام: «چه چیزی برایش مهم است؟» (پایداری؟ سرعت؟ کاهشِ کارِ دستی؟). درخواستت را با «مهمِ او» ترجمه کن: برای تیمِ پلتفرم، امنیتِ دسترسی را نگران نکن — بگو «این یه فلگ اضافه نمی‌کنه، دو فلگ کم می‌کنه». **Skip-level سالم** (درس ۶۷ را یادت باشد): سه سوالِ بی‌خطر + صفر شکایت از مدیرت + یک تعهدِ دوطرفه: "Great to sync — I\'ll share our roadmap constraints with my team so they plan around them." — نفوذِ بدونِ اختیار، از «فهمیدنِ نقشه» شروع می‌شود و با «حل‌کردنِ مشکلِ دیگری» تکمیل.'),
   ]},
 ],
 'takeaway': 'نفوذِ بین‌تیمی = درخواستِ زمینه‌دار با اندازهٔ صادقانه و معاوضه + نردبانِ تشدیدِ چهارپله (bump → کانال → مدیرها → مسیرِ جایگزین) + نقشهٔ تصمیم‌گیر/اجراکننده/تأثیرگذار و «مهمِ» هرکدام. skip-level با سه سوالِ امن و بدونِ شکایت. جملهٔ کل: "What would make this easy for your side?" — و اعتبار، ارزِ رایجِ بین‌تیمی است: امروز ریلویو بده، فردا دستِ گره‌گشاده بگیر.',
 'faq': [
  ('تیمِ دیگر «حُکمِ» خودش را دارد و برای ما کاری نمی‌کند — حق هم دارند؟',
   'بله، و پذیرفتنش اولین قدمِ نفوذ است. حرکتِ بعدی: درخواستت را به «اولویتِ خودشان» بچسبان: "This unblocks the SSO cleanup you mentioned in the last review — same area." یا از مدیرِ خودت بخواه در برنامهٔ فصلیِ دو تیم، وابستگیِ مشترک ثبت شود: "Can we get this on the quarterly cross-team plan? It keeps falling through the cracks." — چیزهایی که در نقشهٔ رسمی می‌نشینند، «حکم» می‌شوند؛ چیزهایی که فقط در پیام می‌مانند، داوطلبی‌اند.'),
  ('اختلافِ فنی با تیمِ دیگر داغ شد — در جلسه یا در متن؟',
   'قاعدهٔ تجربی: اختلافِ «مفهومی» در متن خوب می‌شود (RFC و کامنت، زمانِ فکر می‌دهد — درس ۶۸ و ۷۷); اختلافِ «شخصی‌شده» فقط در ویدئو خوب می‌شود. اگر thread گرم شد: "I think we\'re closer than the text makes it look — 15 minutes of call?" (فکر کنم nearer از چیزیه که متن نشون می‌ده — ۱۵ دقیقه تماس؟) و در تماس، اولِ کار، فرمولِ نرم‌کردن: "For the record: I think your team\'s constraint is legit — my worry is only about the failure mode." — اختلافِ بین‌تیمیِ مدیریت‌شده، معمولاً به «معماریِ بهتر از هر دو طرف» ختم می‌شود؛ مدیریت‌نشده، به سنگرهای دوطرفه.'),
 ],
},
]

# -*- coding: utf-8 -*-
"""Stage 1 · lessons 55-63 — فاز ۴: استندآپ، کدریویو، دیباگ و مصاحبه‌های فنی."""

LESSONS = [
# ───────────────────────────── درس ۵۵ ─────────────────────────────
{
 'slug': 'english-daily-standup',
 'title': 'استندآپ صبحگاهی؛ ۹۰ ثانیه که روزِ کاری تو را تعریف می‌کند',
 'desc': 'اسکریپتِ جلسهٔ روزانه: سه‌گانهٔ yesterday/today/blockers با بلوک‌های آماده, ادبِ «شنوندهٔ خوب» و سوال‌های پس از استندآپ — روزی ده دقیقه که همهٔ تیم صدای تو را می‌شنوند.',
 'keywords': 'استندآپ, daily standup phrases, yesterday today blockers, جلسه روزانه انگلیسی',
 'answer': 'استندآپ فقط سه جمله دارد: دیروز چه کردم (I finished the login tests), امروز چه می‌کنم (I\'m working on the caching issue), چه چیزی گیرم انداخته (I\'m blocked on the staging access). کوتاه، مشخص، بدونِ داستان — جزئیات بعد از جلسه در وِرچالِ جدا.',
 'intro': [
  'استندآپ، اولین «صحنهٔ عمومیِ» روزانهٔ تو در تیم است: همه ایستاده‌اند (یا در تماسِ ویدیویی)، دور ۱۰-۱۵ دقیقه، هر نفر ۳۰-۹۰ ثانیه حرف می‌زند. برای زبانِ دوم، این کوچک‌ترین اما پرتکرارترین ارائهٔ عمرت است — و چون هر روز تکرار می‌شود، بهترین باشگاهِ فنیِ گفتاری هم هست.',
  'سه خطای رایجِ تازه‌واردان: گزارشِ خیلی طولانی (استندآپ، جلسهٔ حل مسئله نیست), گزارشِ مبهم («رو یه چیزی کار می‌کنم»), و پنهان‌کردنِ blocker به‌خاطرِ خجالت. هر سه در همین درس قالبِ درست را می‌گیرند.',
 ],
 'sections': [
  {'h2': 'سه‌گانهٔ کلاسیک؛ yesterday / today / blockers',
   'blocks': [
    ('p', 'قالبِ کاملِ ۹۰ثانیه‌ای: **"Yesterday I finished the migration script and reviewed Sara\'s PR. Today I\'m deploying it to staging and starting the rollback tests. No blockers — I\'m good."** نکته‌های ساختاری: فعل‌های گذشته برای دیروز (finished, reviewed), استمراری برای امروز (I\'m working on…), و بلوکر با صداقتِ شفاف (I\'m blocked on… — با «روی» نه «توسط»). اگر کاری شروع نشده: **"I haven\'t started the API docs yet — that\'s my next task after today\'s fix."**'),
    ('table', ['بخش', 'جمله‌های آماده', 'لحن'],
     [['Yesterday', 'I finished… / I wrapped up… / I spent most of the day on…', 'گذشتهٔ ساده'],
      ['Today', 'I\'m working on… / I\'ll start… / My focus is…', 'استمراری + آینده'],
      ['Blockers', 'I\'m blocked on… / I\'m waiting on… / Nothing blocking me.', 'صادق و کوتاه'],
      ['پایان', 'That\'s me. / Over to you, Jack.', 'تحویل به نفرِ بعد']]),
    ('ex', 'Quick one today: yesterday was mostly meetings, so today I\'m catching up on the PR comments. No blockers.', 'امروز کوتاه: دیروز بیشتر جلسه بود، پس امروز دارم روی کامنت‌های PR جمع می‌کنم. بلوکری نیست.'),
   ]},
  {'h2': 'بلوکر‌ها؛ صداقتی که امتیاز است',
   'blocks': [
    ('p', 'فرمولِ گزارشِ بلوکر: **چی + چقدر تلاش کردی + از که کمک می‌خواهی**: "I\'m blocked on the AWS credentials — I opened a ticket with DevOps, but if anyone can speed it up, that\'d unblock me." (روی AWS گیرم — تیکت زدم به DevOps، ولی اگه کسی می‌تونه تندترش کنه، من آزاد می‌شم.) سه درجهٔ بلوکر را هم بشناس: **blocked** (کاملاً متوقف), **slowed down** (کند شده), **waiting on** (منتظرِ کسی). پنهان‌کردنِ بلوکر در فرهنگِ سالمِ اسکرام، تخلف است — چون یک روزِ گم‌شدهٔ تو، روزِ گم‌شدهٔ تیم است.'),
    ('ex', 'I\'m not fully blocked, but the flaky test is slowing me down. I\'ll timebox it to an hour after lunch.', 'کاملاً بلاک نیستم، ولی تستِ بی‌ثباتی کندم کرده. بعدازظهر یه ساعت سقفِ وقت می‌ذارم روش.'),
   ]},
  {'h2': 'شنونده و پس‌استندآپ؛ ادبِ جلسهٔ کوتاه',
   'blocks': [
    ('p', 'قواعدِ نانوشته: موبایل نیاور (یا دوربین روشن — برای ریموت), وقتی حرفِ دیگری، عقب نشسته‌باش — جوابِ سریع و کوتاه بده (Nice! / Sounds good / Good catch), و اگر بحثِ طولانی شد، جملهٔ حرفه‌ایِ جداسازی: **"Can we take this offline? Jack and I will sync after standup."** (آفلاین ادامه بدیم؟ من و جک بعد از استندآپ همگام می‌شیم) — offline در زبانِ کاری یعنی «بیرونِ این جلسه»، نه بی‌اینترنت! و سوالِ پس از استندآپ اگر نکته‌ای گرفتی: **"Hey Sara, quick question about the migration — got 5 minutes?"**'),
   ]},
 ],
 'takeaway': 'استندآپ = دیروز (گذشتهٔ ساده) + امروز (استمراری) + بلوکر (صداقتِ سه‌تکه: چی + تلاش + کمک‌خواهی). بلوکر را پنهان نکن؛ گزارشش امتیاز است. بحثِ بلند را با «let\'s take this offline» از جلسه بیرون ببر و سوالِ شخصی را با «got 5 minutes?» جدا کن. هر روز ۹۰ ثانیه — بهترین تمرینِ گفتاریِ حرفه‌ایِ دنیا.',
 'faq': [
  ('استندآپ من خیلی تکراری می‌شود — هر روز یکی است!',
   'تکرار، طبیعتِ استندآپ است؛ کوتاه بگو و رد شو. اما سه تکنیکِ زنده‌کردنش: ۱) نتیجه را بگو نه فعالیت را: نهِ «رو تست‌ها کار می‌کنم»، که «امروز تست‌ها سبز می‌شن». ۲) یک قلابِ تیمی بگذار: «اگه کسی تو staged دیده — یه چشم بیندازه ممنون می‌شم». ۳) آپدیتِ واقعی بده: اگر روزِ قبل گفتی فلان را شروع می‌کنی، امروز بگو تمام شد یا چرا نشد — استندآپ، زنجیرِ روزهاست نه لیستِ لحظه‌ای.'),
  ('ریموت و async استندآپ چه فرقی دارد؟',
   'در async، استندآپِ نوشتاری در اسلک است — همان سه‌گانه، اما با ساعت‌گذاری و ایموجیِ خنثی و @منشنِ بلوکر: «:mega: standup — yesterday: shipped retry logic. today: staging deploy. blocker: waiting on DevOps @jack any news on the credentials?» سقفِ زمانِ جواب‌دادنِ تیم را رعایت کن (مثلاً تا ۱۰ صبح) و به کامنتِ بلوکرِ دیگران، جوابِ سریع بده — ادبِ async همین است.'),
 ],
},
# ───────────────────────────── درس ۵۶ ─────────────────────────────
{
 'slug': 'english-code-review',
 'title': 'کدریویو؛ دادنِ بازخوردِ فنی و گرفتنش بدونِ زخم',
 'desc': 'هنرِ گفتارِ ریلویو: قالب‌های سه‌درجه‌ای (must-fix, suggestion, nit), عبارت‌های نرمِ فنی (would you consider…?), و پاسخِ حرفه‌ای به کامنت — از «good catch» تا «خب، پس چرا خودت این‌طور ننوشتی!»',
 'keywords': 'کدریویو, code review phrases, بازخورد فنی, nit suggestion',
 'answer': 'کدریویو دو نیمهٔ جداشدنی ندارد — دادن و گرفتنِ نظرِ فنی، هر دو با قالب می‌آیند. دادن: دسته‌بندیِ کامنت‌ها (nit / suggestion / blocking) و سوال‌بستن به‌جای حکم (Would you consider…?). گرفتن: thanks, good catch — و جداکردنِ «کد» از «خود».',
 'intro': [
  'کدریویو، حساس‌ترین مکالمهٔ فنی است: می‌خواهی به همکارت بگویی کدش بد است، بدونِ این‌که بگویی خودش بد است — و برعکس، بخوری «این غلط است» را بدونِ دفاعِ شخصی. فرهنگِ تیم‌های انگلیسی‌زبانِ سالم برای همین، قالب‌های دقیقی دارد؛ قالب‌ها هم مؤدب‌اند هم کارآمد.',
  'برای زبانِ دوم یک خبرِ خوب: کامنتِ ریلویو، مکالمهٔ کوتاهِ نوشتاری است — زمانِ فکر دارد. همین درس را نه فقط بخوان، بلکه template کن؛ اولین ریلویوی جدی‌ات، از دل همین قالب‌ها بیرون می‌آید.',
 ],
 'sections': [
  {'h2': 'دادنِ کامنت؛ سه درجه و دو قالب',
   'blocks': [
    ('table', ['درجه', 'واژه', 'جملهٔ نمونه'],
     [['اصلاحِ ضروری', 'blocking / must-fix', 'Blocking: this breaks on empty input — we need a guard clause.'],
      ['پیشنهاد', 'suggestion / could consider', 'Suggestion: we could extract this into a helper — up to you.'],
      ['جزئی', 'nit (nitpick)', 'Nit: trailing space here. Not blocking.'],
      ['ستایش', 'praise / this is nice', 'This is a really clean solution — learned something!'],
      ['سوال', 'question', 'Question: why array over set here? Genuine curiosity.']]),
    ('p', 'دو قالبِ طلاییِ نرم‌کردن: **۱) سوال به‌جای حکم:** نهِ «This is wrong» — که **«Would you consider using a set here? Lookups would be O(1).»** ۲) **«ما» به‌جای «تو»:** **«What if we extracted the validation into its own function?»** — «ما»، کامنت را از امتحانِ شخصی به تصمیمِ مشترک می‌برد. و قانونِ «praise در جا»: اگر چیزی خوب بود، همان لحظه بنویس — ریلویو فقط شکارِ اشکال نیست.'),
    ('ex', 'Nit: could we name this `retryCount` instead of `n`? Future-us will thank us.', 'جزئی: می‌شه اسمش retryCount باشه نه n؟ خودِ آینده‌مون ممنون می‌شه.'),
   ]},
  {'h2': 'گرفتنِ کامنت؛ سه پاسخِ حرفه‌ای',
   'blocks': [
    ('p', '**۱) پذیرشِ گرم:** "Good catch — fixing now." (دقتِ خوبی بود — همین الان درستش می‌کنم) **۲) توضیح + بازگشایی:** "Fair point. I kept it sync because the caller needs the value immediately — but I\'m open if you see a cleaner way." **۳) مخالفتِ مستند:** "I see it differently — with the new cache, the extra query costs almost nothing. Happy to discuss on a call if you\'re not convinced." — هر سه: کوتاه، بی‌حالتیِ دفاعی، و برنده. قاعدهٔ طلایی: هر کامنت را یک نظرِ فنی ببین نه حکمِ شخصی — جملهٔ یادگاریِ صنعت: **"Review the code, not the coder."**'),
    ('ex', 'Thanks for the thorough review! Addressed everything except the last point — added a comment in the PR explaining why.', 'ممنون بابت ریلویوی کامل! همه رو اعمال کردم جز آخرین نکته — تو PR توضیحش رو نوشتم.'),
   ]},
  {'h2': 'جریانِ ریلویو؛ درخواست تا merge',
   'blocks': [
    ('p', 'زبانِ جریان: **"Could you take a look when you get a chance?"** (درخواست) · **"Left a few comments — nothing blocking."** (جوابِ ریلویور) · **"Pushed the changes — PTAL."** (اعمال شد؛ PTAL = please take another look — مخففِ محبوبِ گیت‌هاب) · **"LGTM!"** (looks good to me — یعنی تأیید؛ سه حرفِ شیرینِ هر PR) · **"LGTM with nits."** (تأیید — با همین جزئی‌های کوچیک). ادبِ زمان: ریلویوِ PRِ دیگران را همان روزی که می‌خواهی خودت ریلویو شوی بده — اقتصادِ متقابلِ تیم‌های سالم است.'),
   ]},
 ],
 'takeaway': 'دادن: درجه‌گذاری (blocking / suggestion / nit / praise) + سوال به‌جای حکم (Would you consider…?) + «we» به‌جای «you». گرفتن: Good catch / Fair point / مخالفتِ مستند با پیشنهادِ تماس. جریان: PTAL و LGTM — دو مخففِ دنیای ریلویو. و یادت باشد: کامنت، هدیهٔ فنی است؛ قالبش را همین درس داده.',
 'faq': [
  ('ریلویور تندگوی است و کامنت‌ها زخم‌اند — چه کنم؟',
   'سه پله: ۱) قالب را از خودت نگیر: «This is wrong» را به «رو کد نظر می‌ده» ترجمه کن — و جوابِ سردِ حرفه‌ای بده (بالاتر). ۲) اگر لحنِ واقعاً بی‌ادبانه تکرار شد، خصوصی و آرام: **"Hey, your technical points are always solid — the tone sometimes makes it hard to process. Could we keep it a bit softer?"** ۳) اگر ادامه کرد، مدیر/لید را در جریان بگذار — تیمِ سالم، تیکتِ لحن هم دارد. اما ۹۰٪ موارد، همان پلهٔ یک کافی است: جوابِ آرامِ بی‌دفاعی، خودش لحن را بعد از دو-سه ریلویو نرم می‌کند.'),
  ('چطور ریلویوگرِ خوبی شوم وقتی جونیورم؟',
   'سه امانتِ ریلویوگرِ جونیور: **۱) سوال بپرس** — سوالِ واقعی، کامنتِ محترم است: «Curious — why not use the standard library here?» **۲) چیزی که یاد گرفتی را بگو**: «TIL you can do this with pattern matching — nice.» **۳) تست و UX را چک کن** — چشمِ تازه، خطاهایی می‌بیند که چشمِ خبره عادت کرده است. جونیورِ ریلویوگرِ فعال، سریع‌ترین مسیرِ ارتقای فنی-اجتماعی است.'),
 ],
},
# ───────────────────────────── درس ۵۷ ─────────────────────────────
{
 'slug': 'english-debugging-talk',
 'title': 'دیباگ به انگلیسی؛ توصیفِ مشکل، فرضیه‌سازی و «found it!»',
 'desc': 'زبانِ شکارِ باگ: گزارشِ دقیق (steps to reproduce), فرضیه‌ها (my theory is…), جست‌وجوی کمک (has anyone seen this?), و شعرِ پیروزیِ «found it — it was the cache».',
 'keywords': 'دیباگ انگلیسی, debugging phrases, steps to reproduce, bug report',
 'answer': 'دیباگِ گفتاری سه فاز دارد: توصیفِ دقیق (It happens when…, I can reproduce it in 3 steps), فرضیه‌سازی (My theory is the cache is stale), و جمع‌بندی (Found it — the fix is one line). با گزارشِ ساختاریافته، کمکِ تیم نصفِ عمرِ باگ را کم می‌کند.',
 'intro': [
  'باگ، پنهان‌ترین گفتگوی روزانهٔ فنی است: کسی چیزی نمی‌داند، شما چیزی را می‌بینید، همه جمله‌های نصفه رد و بدل می‌شود. تفاوتِ تیمِ حرفه‌ای و خسته، در «زبانِ باگ» است: گزارشِ ساختاریافته و فرضیهٔ شفاف، دو-سه ساعتِ شکار را نصف می‌کند — و تو را از «فردِ اذیت‌شده» به «مهندسِ مسئله» ارتقا می‌دهد.',
  'این درس علاوه بر جمله‌ها، فرمولِ گزارشِ باگ را می‌دهد که در Jira و GitHub issue هم همان است — یعنی سرمایه‌گذاریِ یک‌بار و بازدهیِ هرروزه.',
 ],
 'sections': [
  {'h2': 'توصیفِ دقیق؛ گزارشی که خودش نصفِ حل است',
   'blocks': [
    ('p', 'فرمولِ گزارشِ کامل: **۱) انتظار vs واقعیت:** "Checkout should show the total, but it shows zero." **۲) بازسازی:** "Steps to reproduce: add two items, apply the discount code, go to checkout — total is zero." **۳) دامنه:** "Only on production, only for logged-in users. Staging is fine." **۴) زمان:** "Started after yesterday\'s release — worked fine before." — همین چهار بند، ۸۰٪ سوال‌های اولیهٔ helpers را جواب می‌دهد و به آن‌ها «شروعِ گرم» می‌دهد. واژه‌ها: **reproduce** (بازسازی), **expected behavior** (رفتارِ موردِ انتظار), **actual behavior** (رفتارِ واقعی), **consistent / intermittent** (همیشه / گاهی‌به‌گاه — باگِ بی‌ثبات را intermittent بگو، خدایانِ دیباگ قربانی می‌خواهند: **flaky** برای تست‌ها).'),
    ('ex', 'It\'s intermittent — maybe one in ten requests. I can\'t reproduce it on demand, but here\'s a log snippet from the last time it happened.', 'گاهی‌به‌گاهه — شاید یک در ده درخواست. به‌دست نمی‌آیدش بازسازی کنم، ولی این تکه‌لاگِ دفعهٔ قبلشه.'),
   ]},
  {'h2': 'فرضیه‌سازی؛ بلند فکرکردنِ منظم',
   'blocks': [
    ('p', 'قالب‌های فرضیه: **"My theory is the cache is stale — the config changed but the TTL is long."** · **"I suspect a race condition: two workers pick the same job."** · **"It\'s either the token expiring or the clock drift — let me check the logs."** (It\'s either A or B — قالبِ دوگانهٔ شکار) و مراحلِ حذف: **"I\'ve ruled out the network — same behavior on localhost."** (شبکه رو حذف کردم — روی لوکال هم همینه.) زبانِ حذفِ گزینه‌ها، به تیم نشان می‌دهد که شکارِ سیستماتیک در جریان است نه گیرزدنِ کور.'),
    ('ex', 'Working theory: the migration left the old index in place, and the query planner picks it. Dropping it should fix the slow queries.', 'فرضیه: مایگریشن ایندکسِ قدیمی رو گذاشت و پلنِ کوئری همونو برمی‌داره. حذفش باید کوئری‌های کند رو درست کنه.'),
   ]},
  {'h2': 'کمک‌خواهی و جمع‌بندی؛ جامعهٔ شکار',
   'blocks': [
    ('p', 'کمک‌خواهیِ هدفمند: **"Has anyone seen this error before? `Connection reset by peer` — first time for me."** · **"Jack, you know the payments service best — got 10 minutes to pair on this?"** و جمع‌بندیِ دو حالت — پیروزی: **"Found it! The discount was applied twice — fixing now, PR in 30 minutes."** (پیداش کردم! تخفیف دوبار اعمال می‌شد — الان درستش می‌کنم، PR تا ۳۰ دقیقه) و شکستِ موقت: **"No luck today. I\'ve narrowed it to the webhook handler. Picking it up fresh tomorrow."** — هر دو، جمله‌هایِ حرفه‌ایِ پایانِ شیفتِ شکارند. و بعد از فیکس: **"Added a regression test so it never happens again."** — بستنِ حلقه، امضای مهندسِ بزرگ.')
   ]},
 ],
 'takeaway': 'گزارشِ باگ چهاربندی: انتظار/واقعیت + steps to reproduce + دامنه + زمان. فرضیه‌سازی با قالب: my theory is… / I suspect… / it\'s either A or B / ruled out. کمک: has anyone seen this? / got 10 minutes to pair? بستنِ حلقه: Found it + regression test. باگِ بی‌ثبات = flaky/intermittent — و توصیفِ دقیق، نصفِ راهِ حل است.',
 'faq': [
  ('چطور در GitHub issue گزارشِ خوب بنویسم؟',
   'همان فرمولِ چهاربندی + عنوانِ رفتاری: نهِ «Bug!!!»، که **"Checkout total shows 0 when discount code is applied"**. اضافه‌ها: لاگ و اسکرین‌شات (code block با ```), نسخه‌ها (browser, OS, app version), و **severity**: «Blocks checkout for ~5% of users — high priority.» الگوی رایجِ متنِ باز: تیکهٔ «Environment» و «What I\'ve tried» — نوشتنِ «چه کردم»، دوستِhelpers است.'),
  ('«prod is down» واقعاً پیش می‌آید؟ چه بگویم؟',
   'می‌آید — و برایش درسِ جدا داریم (۸۲: incident). پیش‌نمایشِ جمله‌های بحرانی: اعلام (Pagers are going off — checkout is down), دعوت (Starting a bridge call — join if you can), وضعیت (It\'s regional, only EU. Rollback is running), و تثبیت (Traffic is back. Writing the postmortem). آرامشِ این جمله‌ها در فاز ۵ کامل می‌شود — فعلاً ساختار را بشناس که روزِ سخت، غافلگیر نشوی.'),
 ],
},
# ───────────────────────────── درس ۵۸ ─────────────────────────────
{
 'slug': 'english-agile-scrum',
 'title': 'اسکرام و اژایل؛ واژگانِ sprint، backlog و retrospective',
 'desc': 'واژه‌های چرخهٔ اسکرام به انگلیسی: sprint و backlog, story points و velocity, و جلسه‌های سه‌گانه — به‌علاوهٔ جمله‌های retrospective که همه دوست دارند و ازش می‌ترسند.',
 'keywords': 'اسکرام انگلیسی, agile vocabulary, sprint backlog, retrospective phrases',
 'answer': 'اژایل، زبانِ مدیریتِ کارِ فنی است: کارها story و task می‌شوند، sprintها دو-هفته‌ای‌اند، تخمین story point دارد و جلسه‌ها نام‌های خاص: planning, review, retro. این درس نقشهٔ کامل را با جمله‌های روزِ sprint می‌دهد — از «بگیرم این استوری را؟» تا «در رترو، یک نکتهٔ خنده دارم:».',
 'intro': [
  'اژایل/اسکرام، دینِ رایجِ تیم‌های نرم‌افزاری است — و مثل هر دینی، واژگانش را باید از روزِ اول درست بلد باشی وگرنه جلسات، به آیینِ ناشناخته می‌مانند. خبرِ خوب: مفهوم‌ها ساده‌اند و جمله‌هایشان ثابت؛ خبرِ سخت: تفاوتِ «معنیِ درست» حیاتی است — مثلاً «spike» هیچ ربطی به سیخ ندارد!',
  'این درس، فرهنگِ اسکرام را ترجمه نمی‌کند (آن کارِ درسِ دومِ اسکرام در تیم است) — واژه و جمله را می‌دهد تا در اولین planning، رأی و نظر بدهی نه فقط تماشا کنی.',
 ],
 'sections': [
  {'h2': 'واژه‌نامهٔ اسکرام؛ از backlog تا velocity',
   'blocks': [
    ('table', ['واژه', 'معنی', 'جمله'],
     [['backlog', 'انبارِ کارهای در انتظار', 'Let\'s groom the backlog before planning.'],
      ['sprint', 'چرخهٔ کارِ ۱-۴ هفته‌ای', 'This sprint ends on Friday.'],
      ['story / user story', 'یک واحدِ کارِ کاربر-محور', 'I\'ll pick up the login story.'],
      ['story points', 'واحدِ تخمینِ سختی', 'It\'s a 5-pointer — mid complexity.'],
      ['velocity', 'سرعتِ متوسطِ تیم در sprint', 'Our velocity is around 40 points.'],
      ['scope creep', 'وسیع‌شدنِ بی‌ضابطهٔ کار', 'Careful — that\'s scope creep.'],
      ['spike', 'تحقیقِ کوچکِ زمان‌دار', 'Let\'s do a one-day spike on the new queue.'],
      ['epic', 'استوریِ بزرگِ چندپاره', 'Payments is an epic — we\'ll split it.'],
      ['acceptance criteria', 'معیارهای پذیرش', 'The story meets the acceptance criteria.'],
      ['carry-over', 'کارِ به‌عقب‌افتاده از sprint قبل', 'Two carry-overs from last sprint.']]),
    ('p', 'جمله‌های روزِ sprint: برداشتنِ کار: **"I\'ll take the notifications story."** · پیشنهادِ کوچک‌کردن: **"This story is too big — can we split it?"** · اعلامِ خطرِ وقت: **"I don\'t think this fits in the sprint — can it move to next?"** و خطرِ اضافه‌کاری: **"Adding this now means dropping something — what do we cut?"** — جملهٔ آخر، مقدس‌ترین جملهٔ اژایل سالم است.'),
   ]},
  {'h2': 'جلسه‌های سه‌گانه؛ planning, review, retro',
   'blocks': [
    ('p', '**Planning (برنامه‌ریزی):** تخمین و برداشتنِ sprint. جمله‌های تو: **"How many points is this, ballpark?"** (بالاترین حدوده چقدره؟) · **"I\'m at capacity — anything more and quality drops."** **Review (نمایش):** دموی کارِ تمام‌شده. جمله: **"Today I\'ll demo the new checkout — two minutes, no slides."** **Retro (بازاندیشی):** چه خوب بود/بد/بهتر؟ سه قالبِ محترمانه: **"One thing that worked: the pairing sessions."** · **"One thing to improve: our standups are drifting into problem-solving."** · **"One experiment for next sprint: let\'s try async standup twice a week."** — «worked / to improve / experiment»، سه‌لایهٔ رتروی بی‌اتهام.'),
    ('ex', 'In the retro I\'d like to raise one thing: the flaky tests are eating our time. Suggest we timebox a fix-sprint.', 'توی رترو می‌خوام یه نکته مطرح کنم: تست‌های بی‌ثبات وقتِ ما رو می‌خورن. پیشنهاد می‌کنم یه اسپرینتِ فیکس با سقفِ وقت بذاریم.'),
   ]},
  {'h2': 'کلماتی که فقط در اژایل زندگی می‌کنند',
   'blocks': [
    ('p', 'چهار اصطلاحِ قبیله‌ای که بیرونِ اسکرام معنا ندارند اما داخلش هر روز می‌آیند: **grooming/refining the backlog** (مرتب‌کردنِ انبار — شکستنِ استوری‌های بزرگ و روشن‌کردنِ مبهم‌ها), **swarming** (همه روی یک استوری سقوط می‌کنند تا تمام شود), **blocker bash** (جلسهٔ سریعِ رفعِ بلوکرها), و **chicken and pig** (تفکیکِ قدیمیِ «درگیر vs ذی‌نفع» — امروزه کمتر گفته می‌شود ولی در رتروهای قدیمی می‌شنوی). و امانتِ ترجمه: **sprint را ترجمه نکن** — «اسپرینت» بگو؛ این واژه‌ها در فارسیِ فنی هم همین‌طور زنده‌اند.'),
   ]},
 ],
 'takeaway': 'نقشهٔ اسکرام: backlog→sprint→review→retro; کارها story/task، تخمین points، سرعت velocity، تحقیق spike، بزرگ epic. جمله‌های سه‌گانه: "I\'ll take…" / "This story is too big — split?" / "Adding means cutting." رترو با قالبِ three-layers: worked / to improve / experiment. و sprint هرگز ترجمه نمی‌شود.',
 'faq': [
  ('Kanban هم یاد بگیرم؟',
   'Kanban سبکِ دیگرِ اژایل است: بدونِ sprint، با بردِ ستون‌دار (To do / In progress / Done) و حدِ کارِ هم‌زمان (WIP limit). اگر تیمت Kanban است، جمله‌ها ساده‌ترند: "This card is ready for review" · "Should we raise the WIP limit? Things are queuing." مفهومِ مشترک‌ها همان‌هاست — تخمین، تحویلِ کوچک، رترو — پس این درس برایت نصف‌کاره نمی‌ماند.'),
  ('«Definition of Done» چیست و چرا همیشه می‌گویندش؟',
   'چک‌لیسِتوافقِ تیم برای «تمام»: کد ریلویو شده، تست سبز، داکِ آپدیت، دپلوی روی staging. جمله‌های مربوطه: "This isn\'t done-done — it\'s not deployed." (تمامِِ واقعی نیست — دپلوی نشده) یا "Let\'s agree on a DoD for spikes." تعریفِ done، جنگِ سلطعِ «تقریباً تمام» است — و تیم‌ها هرچند وقت یک بار در رترو تازه‌اش می‌کنند.'),
 ],
},
# ───────────────────────────── درس ۵۹ ─────────────────────────────
{
 'slug': 'english-technical-writing',
 'title': 'مستندسازی؛ README، کامنت و داکِ دور',
 'desc': 'نوشتارِ فنیِ کوتاه: README که آدم را راه می‌اندازد, کامنتی که «چرا» را می‌گوید نه «چه», و داکِ تصمیم (ADR) — سه لایه‌ای که دانشِ تیم را زنده نگه می‌دارد.',
 'keywords': 'مستندسازی انگلیسی, technical writing, readme, code comments',
 'answer': 'داکِ خوب انگلیسی سه ویژگی دارد: کوتاه (رهبرِ جمله فعلِ امری است: Run the script), اسکن‌پذیر (سرتیتر و لیست), و مخاطب‌دار (این برای کیست؟). کامنتِ خوب فقط «چرا» را می‌گوید؛ «چه» را کد خودش می‌گوید. این درس قالب‌های هر سه لایه — README, کامنت, ADR — را می‌دهد.',
 'intro': [
  'مستندسازی، دومین مهارتِ «پنهان اما ارزیابی‌شده» فنی است: کسی ا overt شاخص نمی‌گذارد، اما داکِ خوب، سال‌ها بعدِ رفتنِ تو هم به تو اعتبار می‌دهد — و داکِ بد، هر روز از وقتِ همه را می‌خورَد. برای زبانِ دوم، نکتهٔ طلایی این است که نوشتارِ فنی از هر متنی ساده‌تر است: جمله‌ها کوتاه‌اند، لحن امری است، و واژه‌ها تکرار می‌شوند.',
  'این درس مقدمهٔ فنی است؛ نسخهٔ حرفه‌ای‌تر (RFC و پروپوزال) در فاز ۵ می‌آید. قالب‌های امروز را در ریپوی خودت امتحان کن — اولین READMEای که با همین درس بنویسی، بهترین داکِ عمرت خواهد بود.',
 ],
 'sections': [
  {'h2': 'README؛ در چهار بلاک',
   'blocks': [
    ('p', 'قالبِ استانداردِ README: **۱) یک جمله: این چیست؟** "A tiny Python library for turning CSVs into charts." **۲) Quickstart:** سه فرمانِ تا نتیجه: `pip install x` ← `import x` ← خروجی. **۳) چرا این؟** یک بلاکِ تفاوت: "No dependencies. Works offline. 10x faster than Y for small files." **۴) Contributing + License.** قاعده‌های زبانی: جمله‌های زیرِ ۲۰ کلمه، دوم‌شخص (you), فرمان‌ها در code block با `‎`، و بدونِ تبلیغِ اضافی — داکِ خوب، خودش را با «کارکردن» می‌فروشد نه با صفت.'),
    ('ex', '## Quickstart\n1. `pip install upword-charts`\n2. `import upword_charts as uc`\n3. `uc.from_csv("data.csv").save("out.png")`\n\nThat\'s it — no config file, no account.', 'شروعِ سریع — همین؛ نه فایلِ کانفیگ، نه اکانت.'),
   ]},
  {'h2': 'کامنت؛ «چرا» نه «چه»',
   'blocks': [
    ('p', 'کامنتِ بد: `i++; // add one to i` (کد خودش می‌گوید). کامنتِ خوب، سه چیز را می‌گوید: **۱) چرا:** `// Retry 3x: the payment API drops ~0.1% of requests under load.` **۲) هشدار:** `// NOTE: changing this breaks the mobile client (v2). Ask the mobile team first.` **۳) لینکِ منشأ:** `// See ADR-12 for why we chose gRPC over REST here.` — و برای کدِ موقت: `// TODO(alip): remove after the 2026-02 migration. Tracking in TICKET-841.` قالبِ TODO با اسم و تاریخ و شماره، کامنتِ زنده می‌سازد نه سنگ‌قبرِ فراموشی.'),
   ]},
  {'h2': 'داکِ تصمیم و داکِ دور؛ ADR و postmortem',
   'blocks': [
    ('p', '**ADR (Architecture Decision Record):** یک تصمیمِ فنی در چهار بند: **Context** (وضعیت), **Decision** (تصمیم), **Consequences** (پیامدها), **Alternatives** (بدیل‌های ردشده). نمونه: "We will use Postgres for the event store. Context: team knows it, ops tooling exists. Consequences: no replay performance tuning like Kafka; we accept this for now." و **postmortem** (بازبینیِ حادثه) با بی‌اتهام‌ترین قالبِ دنیا: **"What happened / Impact / Timeline / Root cause / Action items"** — جملهٔ کلیدی: **"X caused Y" نهِ "Ali caused Y"** — در داکِ سالم، عاملیت با سیستم است نه با آدم.'),
    ('ex', 'Root cause: the retry logic created duplicate charges when the response was slow but successful. Action item: idempotency keys on all payment endpoints (owner: payments team, due: next sprint).', 'ریشه: منطقِ retry موقعِ کندی، پرداختِ تکراری می‌ساخت. اقدام: کلیدِ idempotency روی همهٔ endpointهای پرداخت (مسئول: تیمِ پرداخت، ضرب‌الاجل: اسپرینتِ بعد).'),
   ]},
 ],
 'takeaway': 'README چهاربلاک: چیست (یک جمله) + Quickstart (سه فرمان) + چرا (تفاوت) + Contributing. کامنت فقط «چرا/هشدار/لینک» — هرگز «چه» — و TODO با اسم و تاریخ و تیکت. ADR: Context/Decision/Consequences/Alternatives; postmortem بی‌اتهام: "X caused Y". داک، فقط نوشتن نیست؛ نگه‌داشتنِ دانشِ تیم است.',
 'faq': [
  ('مخاطبِ داک را کجا می‌فهمم؟',
   'سؤالِ «این برای کیست؟» را قبل از نوشتن جواب بده و در همان بندِ اول بنویس: "This guide is for new backend devs joining the payments team. If you\'re looking for the API reference, see /docs/api." داکِ بی‌مخاطب، همه‌کاره می‌شود و همه‌کاره یعنی هیچ‌کاره. قاعدهٔ عملی: یک داک، یک مخاطب، یک کار — و لینک برای بقیه.'),
  ('زبانم را داک‌نویسی بهتر می‌کند یا داک‌خوانی؟',
   'هر دو، اما با نسبتِ متفاوت: بخوان تا الگو ببینی (READMEهای محبوبِ گیت‌هاب را بخوان — ساختارشان همین درس است) و بنویس تا عضله بسازی. تمرینِ عملی: پروژهٔ شخصی‌ات را با قالبِ امروز README کن و به یک دوستِ فنی بده — اگر بدونِ سوالِ تو راه افتاد، داکِ تو سبز است. نوشتنِ برای «خوانندهٔ واقعی»، سریع‌ترین معلمِ ساده‌نویسی است.'),
 ],
},
# ───────────────────────────── درس ۶۰ ─────────────────────────────
{
 'slug': 'english-slack-communication',
 'title': 'اسلک و چتِ کاری؛ لحن، thread و هنرِ «پینگ» زدن',
 'desc': 'زبانِ نوشتاریِ فوری: آغازگرهای نرم (quick question), علامت‌گذاری و thread, پینگ‌زدن به موقع (پس از ۲۴ ساعت)، و ایموجی‌های فرهنگی — چتِ کاری، خودش یک لهجه دارد.',
 'keywords': 'اسلک انگلیسی, slack phrases, workplace chat, thread ping culture',
 'answer': 'چتِ کاری، زبانِ سوم است: نه گفتارِ کامل، نه ایمیلِ رسمی. قواعدش: آغازگرِ نرم (Quick question — / Hey, when you have a sec…), thread برای ادامهٔ بحث (بدونِ بمبارانِ کانال), @منشن با مسئولیت, و ایموجی به‌موقع — خندهٔ کاریِ بی‌صدا.',
 'intro': [
  'اسلک، جایی است که بیشترِ «مکالمه‌های» روزانهٔ فنی‌ات اتفاق می‌افتد — و محلِ اولین سوءتفاهم‌های زبانی هم هست: پیامی که در فارسیِ ذهنت «صمیمی» بود، در انگلیسیِ خشکِ بی‌لحن «دستور» خوانده می‌شود. قواعدِ این درس، همان بستهٔ شлокِ فرهنگی است: با آن، پیام‌هایت هم گرم‌اند هم حرفه‌ای.',
  'قاعدهٔ کلیدی که همه‌چیز رویش می‌چرخد: چتِ کاری، «متنِ گفتار» است نه «متنِ مقاله» — جمله‌های کوتاه، امریِ نرم، و بخش‌خوردنِ پیام به‌جای دیوارِ متن.',
 ],
 'sections': [
  {'h2': 'آغازگرها و درخواست‌ها؛ نرم‌کردنِ پیام',
   'blocks': [
    ('table', ['موقعیت', 'بگو', 'نه'],
     [['سوالِ سریع', 'Quick question: …', 'سلام. حالت چطوره؟ (و بعد ۵ دقیقه سکوت)'],
      ['درخواستِ وقتمدار', 'Hey Jack, when you get a sec — could you look at the PR?', 'Jack! PR! الان!'],
      ['قطع‌کردنِ مکالمه', 'Sorry to jump in — quick note on that.', 'مستقیم وسطِ thread دیگران'],
      ['فوریتِ واقعی', 'This is time-sensitive — prod issue. Need a hand now.', 'همه‌چیز را urgent بنویسی'],
      ['پس گرفتن', 'False alarm — solved it. Thanks though!', 'پیامِ رها‌شدهٔ بی‌جواب']]),
    ('p', 'و قاعدهٔ «هی» محض: اگر سوالت یک‌خطی است، سلام و سوال را در همان یک پیام بفرست: **"Hey Sara — do you know if the staging DB is up? Getting timeouts."** سلامِ تنها + انتظارِ جواب، در فرهنگِ چتِ انگلیسی نامهٔ ناتمام است! (Hi Sara… [۲۰ دقیقه سکوت] …sara?)'),
    ('ex', 'Morning! Quick one: does anyone know why the build is red? I\'ve restarted it twice.', 'صبح بخیر! سوالِ کوتاه: کسی می‌دونه بیلد چرا قرمزه؟ دوبار ری‌استارت کردم.'),
   ]},
  {'h2': 'Thread، @منشن و کانال‌ها؛ آدابِ فضایِ عمومی',
   'blocks': [
    ('p', 'سه امانتِ فضا: **۱) Thread:** جوابِ هر پیام، داخلِ thread همان پیام — کانالِ عمومی برای اعلامِ کوتاه است نه گفتگوی دونفره. **۲) @منشن:** فقط وقتی «این آدمِ مشخص، برای این پیام لازم است» — و در کانالِ عمومی، @here برای همهٔ حاضران و @channel برای همه (بمبِ اتمی؛ فقط برای حادثه و خبرِ مهم). **۳) کانال درست:** قبل از فرستادن بپرس: سوالِ عمومی است؟ (#team-public) یا شخصی؟ (DM). جملهٔ انتقالِ محترمانه: **"Moving to a thread so we don\'t spam the channel 🧵"** — همین یک پیام، تو را شهروندِ نمونهٔ اسلک می‌کند.'),
   ]},
  {'h2': 'لحن و ایموجی؛ نمکِ چتِ کاری',
   'blocks': [
    ('p', 'ایموجی‌های فرهنگی که معنای واقعی دارند: **👍** = «دیدم/تأیید» (نه بی‌احترامی!), **🙏** = «ممنونم» (در Asia-پسندِ مودبانه), **👀** = «جالبه، دنبال می‌کنم», **🔥** = «عالی بود», **🎉** = جشنِ تحویل — و ** GIF/react** به‌جای جوابِ بلند وقتی فقط «همم، تأیید» می‌خواهی بگویی. لحنِ پیامِ زخم‌دار را نرم‌کن: **"This is the third time the build breaks here 😅 — can we add a check?"** — ایموجیِ درست، منتقدِ سخت را هم انسانی می‌کند. و امضا: تایپ‌کوتاه‌ها — **ty** (thanks), **np** (no problem), **np!**، **lgtm**, **afk** (away from keyboard), **brb** — فرهنگِ چت را در دو حرف می‌فهمی.'),
    ('ex', 'Shipped it 🎉 Big thanks @sara for the late-night review! 🙏', 'تحویلش دادم 🎉 ممنون از سارا بابت ریلویوی نیمه‌شب! 🙏'),
   ]},
 ],
 'takeaway': 'چتِ کاری = گفتارِ نوشتاری: آغازگرِ نرم + سوالِ در همان پیام + thread برای ادامه + @منشنِ مسئولانه (و @channel فقط برای حادثه). ایموجی، لحنِ نوشتاری توست: 👍 تأیید، 🙏 ممنون، 🎉 جشن. hi محض + سکوت، نامهٔ ناتمام است — و «False alarm, thanks though!» محترم‌ترین پایانِ حلِ خودجوش است.',
 'faq': [
  ('پیامم بی‌جواب ماند — چند بار یادآوری کنم؟',
   'ریتمِ مؤدبانه: ۲۴ ساعت صبر، بعد بغد: **"Just bumping this in case it got buried — no rush!"** (فقط بالا میارمش شاید لای زیر رفته باشه — عجله‌ای نیست!) — کلمهٔ bump یعنی «بالا آمدنِ پیام». اگر فوری است، پیامِ دوم با زمینه: **"Bumping because the demo is tomorrow — need the credentials by EOD."** فوریت را با دلیل اعلام کن، نه با تکرارِ خشمگین.'),
  ('DM بزنم یا کانال؟',
   'قاعدهٔ پیش‌فرض: سوالِ کاری، در کانال — چون جوابش برای فردا هم دیده می‌شود و دانش عمومی می‌شود. DM فقط برای: شخصی/حساس، انتقادِ خصوصی، یا درخواستِ زمانیِ خاص. جملهٔ خوبِ آغازِ DM: **"Hey — asking here since it\'s a bit personal: could we chat about my ramp-up feedback?"** و در کانال اگر بحثش شخصی شد: **"Moving to DMs — I\'ll summarize the outcome back here."** — این جمله‌ی جمع‌بندی، امانتِ فضایِ عمومی را کامل می‌کند.'),
 ],
},
# ───────────────────────────── درس ۶۱ ─────────────────────────────
{
 'slug': 'english-interview-coding',
 'title': 'مصاحبهٔ فنی ۱؛ حلِ مسئله با صدای بلند',
 'desc': 'مرحلهٔ coding interview: درکِ سوال (clarifying questions), فکرکردنِ بلند (thinking out loud), پیچیدگی و تست, و جمله‌های نجاتِ گیرکردن — با دیالوگِ کاملِ یک مسئله.',
 'keywords': 'مصاحبه فنی, coding interview, clarifying questions, thinking out loud',
 'answer': 'در مصاحبهٔ coding، ارزیابی‌شده «صدای فکرِ» توست نه فقط کد: سوال‌های شفاف‌ساز بپرس, بلند فکر کن, پیچیدگی را بگو (O(n log n)), و تست بنویس. جملهٔ نجاتِ گیرکردن: "Let me step back and rethink the approach" — بازگشتِ آبرومند، مهندسی است.',
 'intro': [
  'مصاحبهٔ coding، ترسناک‌ترین ۴۵ دقیقهٔ هر برنامه‌نویسِ غیرِ بومی است: مسئله + کد + انگلیسی، هم‌زمان. اما ساختارش کاملاً بازی‌پذیر است: مصاحبه‌گرها یک روبکِ ارزیابی ثابت دارند (communication, problem solving, coding, testing) و بلند-فکرکردنِ ساختارمند، امتیازِ همان روبریک را می‌گیرد — حتی وقتی جوابِ نهایی ناقص است.',
  'این درس، مسیرِ کامل را با دیالوگ می‌دهد: از «ببخشید، سوال را دقیق‌تر بخواهم» تا «اجازه بده تستش کنم». درسِ بعد system design است؛ درس ۶۳ رفتاری (behavioral).',
 ],
 'sections': [
  {'h2': 'درکِ مسئله؛ سوال‌های شفاف‌ساز',
   'blocks': [
    ('p', 'قبل از کد، سه-چهار سوال بپرس — همین سوال‌ها اولین امتیازِ توست: **۱) ورودی/خروجی:** "So the input is a list of integers, and I should return the indices — right?" **۲) لبه‌ها:** "Can the list be empty? Can it have duplicates?" **۳) اندازه:** "How big can n get? — That tells me if O(n²) is fine or I need better." **۴) مفروضات:** "Is the input sorted? Can I modify it in place?" — و جمع‌بندِ بازگویی: **"So to confirm: given an unsorted list and a target, return any pair that sums to it. Empty list means no answer."** بازگویی، تو را از نصفِ خطاهای مصاحبه دور نگه می‌دارد.'),
    ('ex', 'That\'s a great clarification — so duplicates are possible. That changes my approach: I\'ll use a hash map of value → index.', 'توضیحِ خوبی بود — پس مقدارِ تکراری ممکنه. رویکردِ من عوض می‌شه: از hash map مقدار→ایندکس استفاده می‌کنم.'),
   ]},
  {'h2': 'بلند فکرکردن؛ قالب‌های مسیرِ حل',
   'blocks': [
    ('p', 'سه قالبِ صدای فکر: **۱) رویکرد اولیه:** "My first instinct is the brute force — two nested loops, O(n²). It works, but let me see if I can do better." (همیشه از brute force شروع کن — صداقتِ فنی است) **۲) بهبود:** "I can trade space for time: one pass with a hash map — O(n) time, O(n) space." **۳) تصمیمِ نوشتن:** "I\'ll code the hash-map version — it\'s clean and n can be a million." و جمله‌های میانِ کد: "I\'m writing a helper for…" · "This part assumes the input is not null — I\'ll add a guard." · "Let me name it clearly — `findFirstPair`." اسمِ خوب و کامنتِ «چرا»، امتیازِ نوشتارِ فنی‌ات است.'),
    ('ex', 'Let me think out loud for a second… the tricky part is the wrap-around case. I\'ll handle it by taking the modulus.', 'بذار یه لحظه بلند فکر کنم… قسمتِ پیچیده، حالتِ دور-زدنه. با باقیماندهٔ تقسیم هندلش می‌کنم.'),
   ]},
  {'h2': 'تست، پیچیدگی و گیرکردن؛ سه‌گانهٔ پایان',
   'blocks': [
    ('p', '**تست (بعد از کد):** "Let me trace through an example: input 2, 7, 11 — target 9. First iteration stores 2, second finds 7\'s complement… returns 0,1. Looks right. Edge case: empty list — returns null, as agreed." **پیچیدگی:** "Time is O(n) — single pass. Space is O(n) for the map. If memory were tight, the sorted two-pointer approach gives O(1) extra space at O(n log n) time." و جمله‌های نجاتِ گیر: **"Hmm, this doesn\'t handle the negative case. Let me step back and rethink."** · **"I\'m going in circles here — can I get a hint? I\'d rather ask than stall."** — درخواستِ hint با این صراحت، در روبریکِ communicationِ بیشترِ شرکت‌ها امتیاز دارد نه جریمه: گیرِ بی‌صدا جریمه دارد، گیرِ شفاف نه.'),
   ]},
 ],
 'takeaway': 'روتینِ مصاحبهٔ coding: شفاف‌سازها (ورودی/لبه/اندازه/مفروضات) + بازگویی + بلند-فکر (brute force → بهبود → تصمیم) + تستِ ردیابی + پیچیدگی (O(n)/O(n²) را راحت بگو). گیر که خوردی: "Let me step back" یا درخواستِ صریحِ hint. صدای فکر، همان چیزی است که مصاحبه‌گر می‌خرد.',
 'faq': [
  ('انگلیسی‌ام وسطِ فکر قطع می‌شود و سکوت می‌کنم!',
   'سکوتِ فکری، مشکلِ همه است — حتی بومی‌ها. تفاوت در مدیریتش: جمله‌های پرکنندهٔ فکر را از حفظ کن: **"Give me a second to think…"** · **"I\'m weighing two approaches here…"** · **"Bear with me — this is the tricky part."** — همین سه جمله، سکوتِ آبرومند می‌سازند. و برای قطعیِ جدی‌تر: **"Sorry, I lost my thread — where were we?"** مصاحبه‌گرها این‌ها را روزی ده بار می‌شنوند؛ هیچ‌کدام امتیازِ منفیِ واقعی ندارند، فقط سکوتِ مرده دارد.'),
  ('چهار 公司类型ِ مصاحبهٔ coding را بشناسم؟',
   'چهار چهرهٔ رایج: **۱) الگوریتمیِ کلاسیک** (همین درس — CoderPad/Google Doc), **۲) take-home** (مسئله را می‌بری خانه، ۲-۳ روز): جمله‌اش در ایمیلِ تحویل: "A few notes on the design choices are in the README — happy to walk through them." **۳) pair-programming** (با کارمند): "Want me to drive first, or you?" (من تایپ کنم اول یا تو؟) **۴) live debugging**: کدِ ناقصِ عمدی می‌دهند — درس ۵۷ (دیباگ) همان ادبیاتش است. برای هر چهار، صدای فکر یکسان است؛ فقط ظرف عوض می‌شود.'),
 ],
},
# ───────────────────────────── درس ۶۲ ─────────────────────────────
{
 'slug': 'english-interview-system-design',
 'title': 'مصاحبهٔ فنی ۲؛ system design از «یک میلیون کاربر» به بالا',
 'desc': 'چارچوبِ گفتاریِ طراحیِ سیستم: نیازمندی‌ها و scale, بلوک‌های پایه (load balancer, cache, queue), trade-offها (CAP, consistency), و دیالوگِ کاملِ «URL shortener را طراحی کن».',
 'keywords': 'مصاحبه سیستم دیزاین, system design interview, trade offs, scalable design',
 'answer': 'در system design، سوال همیشه یک جمله است («یک URL shortener طراحی کن») و جواب، یک گفتگوی چهل‌دقیقه‌ای. چارچوبِ گفتاری: نیازمندی‌ها و اعداد (million users? writes or reads?), طراحیِ بلوک‌به‌بلوک, trade-offها با «بسته به…», و جمع‌بندی. کارتِ امتیازِ تو: پرسیدنِ «چند؟» قبل از گفتنِ «چطور».',
 'intro': [
  'system design، مصاحبهٔ «معماریِ گفتاری» است: هیچ کدی نوشته نمی‌شود؛ تو و مصاحبه‌گر روی تخته‌سفید (یا Excalidraw) یک سیستم می‌کشید و می‌سازید. برای زبانِ دوم، خبرِ خوب این است که واژگانش بسته و ثابت است — ده-پانزده بلوک که همهٔ سوال‌ها با آن‌ها ساخته می‌شوند — و سخت‌ترین بخش، «صحبتِ پیوسته در حینِ طراحی» است که قالب‌های همین درس می‌سازندش.',
  'این درس یک سوالِ معروف (URL shortener) را کامل طی می‌کند؛ چارچوبِ گفتاری برای ۹۰٪ سوال‌های دیگر همین است: چون همهٔ سیستم‌ها، همان بلوک‌ها را با اعدادِ متفاوت می‌چینند.',
 ],
 'sections': [
  {'h2': 'گام ۱؛ نیازمندی‌ها و scale — سوال قبل از طرح',
   'blocks': [
    ('p', 'قالبِ آغاز: **"Let me clarify the requirements first. Functional: users submit a long URL and get a short one; redirects should work forever. Non-functional: low latency on redirect — that\'s the hot path. Scale: how many reads are we talking about? 100 million redirects a day is ~1,000 per second — that\'s actually modest."** (اول نیازمندی‌ها رو روشن کنم… ۱۰۰ میلیون ریدایرکت در روز یعنی حدهٔ ۱۰۰۰ در ثانیه — در واقع ناچیز است.) — این پاراگرافِ آغازین، امتیازِ کلِ گامِ اول است: تو داری «مسئله را تعریف» می‌کنی، و مصاحبه‌گر دنبالِ همین سیگنال است. اعداد را بلند بگو و جمع‌بندی کن: **"So we\'re read-heavy — 100 reads per write. That shapes everything."** (خوانا-محوره — صد خواندن به‌ازایِ هر نوشتن. این همه‌چیز رو شکل می‌ده.)'),
   ]},
  {'h2': 'گام ۲؛ بلوک‌ها — طراحیِ واژه‌به‌واژه',
   'blocks': [
    ('table', ['بلوک', 'جملهٔ معرفی‌اش', 'چرا می‌آید'],
     [['API layer', 'The API receives the create request and validates it.', 'درِ ورودی'],
      ['ID generator', 'We need short IDs — base62 of a counter, or a hash.', 'شناسهٔ کوتاه'],
      ['Database', 'A key-value store fits: short ID → long URL.', 'نگه‌داریِ نگاشت'],
      ['Cache', 'Hot URLs should never hit the DB — Redis in front.', 'خواناییِ سریع'],
      ['Load balancer', 'LB in front of the API tier, stateless behind it.', 'پخشِ بار'],
      ['Queue', 'Analytics can be async — drop events in a queue.', 'کارِ پشتِ صحنه'],
      ['CDN', 'Not much to cache here — mostly for any static pages.', 'رسانهٔ ایستا']]),
    ('p', 'جمله‌های اتصالِ بلوک‌ها — موتورِ گفتاریِ تو: **"So the flow is: the client hits the LB, the LB routes to an API node, the node checks Redis first, falls back to Postgres, and returns the redirect."** و برای هر تصمیم، trade-off بگو: **"Base62 counter gives short, sortable IDs but a single point of failure — I\'d shard the counter or use Snowflake-style IDs. Trade-off: a bit more complexity for availability."** — کلمهٔ «trade-off» را نچپانی؛ همان چیزی است که مصاحبه‌گر دنبالش می‌گردد.'),
   ]},
  {'h2': 'گام ۳؛ رشد، خرابی و جمع‌بندی',
   'blocks': [
    ('p', 'سوال‌های گامِ آخر که خودت طرح کن (امتیازِ senior): **"What breaks at 100x? The DB — I\'d shard by ID hash."** (چی می‌شکنه اگر صد برابر شود؟ دیتابیس — hash-ID شارد می‌کنم.) · **"Single region or multi? Multi-region adds replication lag — for a redirector, eventual consistency is fine."** و فنّ بقای مشهور — **"There\'s no single right answer here — it depends on the read/write ratio and the ops budget."** جملهٔ «بسته به…» در system design حکمِ «بستنی در گرما» را دارد: هر جا شک کردی، trade-off را با «بسته به» بگو و دو گزینه با قیاس بیاور — همین، پاسِ صحیحِ ۹۰٪ سوال‌هاست. جمع‌بندیِ پایانی: **"So: stateless API tier, Redis cache for the hot path, sharded KV store, async analytics. Happy to go deeper on any piece."**'),
    ('ex', 'If I had more time, I\'d dig into the ID generator — that\'s the most interesting trade-off in this design.', 'اگه وقت بیشتری بود، می‌رفتم سراغِ تولیدکنندهٔ ID — جالب‌ترین trade-off این طراحیه.'),
   ]},
 ],
 'takeaway': 'چارچوبِ system design: نیازمندی‌ها و اعداد (سوالِ «چند؟» اول) → بلوک‌ها با جمله‌ی اتصال (the flow is…) → trade-off با «بسته به…» → رشد و خرابی (what breaks at 100x?) → جمع‌بندی. واژه‌های پولساز: hot path, read-heavy, shard, eventual consistency, single point of failure. کد نمی‌نویسی؛ «معماری حرف می‌زنی».',
 'faq': [
  ('تجربهٔ واقعیِ system design ندارم — از کجا شروع کنم؟',
   'سه منبعِ عملی: ۱) کتابِ طراحیِ معروف (DDIA — Designing Data-Intensive Applications) با خواندنِ آهسته — حتی دو فصلِ اول، نصفِ واژگانِ این درس را عمیق می‌کند. ۲) تمرینِ «طراحیِ بلند به خودت»: هر سرویسی که روزانه استفاده می‌کنی (اسنپ‌فود، تلگرام) را ده دقیقه با بلوک‌های این درس توضیح بده — به خودت یا به اپِ مکالمهٔ آپورد. ۳) دیالوگِ همین درس را با نقشِ تو حفظ کن: چارچوبِ گفتاری، نصفِ نمره است.'),
  ('مصاحبه‌گر وسطِ حرفم مسیر را عوض کرد — چه کنم؟',
   'خوش‌حال باش — یعنی درگیرِ گفتگو شدی! جوابِ چابک: **"Good point — that changes the storage layer. Let me redo that piece."** و بعد از بازسازی، جمع‌بندِ کوچک: **"So the new constraint is X — I\'ve adjusted the cache strategy accordingly."** تغییرِ مسیرِ وسطِ جلسه، اتفاقِ طراحیِ واقعی است؛ نشان‌دادنِ «انعطافِ بازطراحی» همان چیزی است که تیم‌های واقعی روزی چند بار انجام می‌دهند و مصاحبه‌گر می‌خواهد ببیند.'),
 ],
},
# ───────────────────────────── درس ۶۳ ─────────────────────────────
{
 'slug': 'english-behavioral-interview',
 'title': 'مصاحبهٔ رفتاری؛ STAR در عمل و سوال‌های فرهنگیِ شرکت',
 'desc': 'عمیق‌کردنِ درس ۴۷ برای سمتِ فنی: پنج سوالِ رفتاریِ پرتکرارِ مهندسی با پاسخ‌های STARِ نمونه, سوال‌های culture fit, و امضای «من + تیم» که کارفرمای فنی می‌خرد.',
 'keywords': 'مصاحبه رفتاری, behavioral interview, STAR, culture fit questions',
 'answer': 'مصاحبهٔ رفتاریِ فنی، همان STAR است با موضوع‌های مهندسی: تعارضِ فنی (we disagreed on the framework), شکستِ prod, همکاریِ cross-team, اولویت‌بندی, و بازخورد گرفتن. سوال‌های فرهنگی هم آینه دارند: "Tell me about a time you disagreed with a decision" — و جوابِ خوب، مخالفتِ محترمانه + پیروی از تصمیمِ نهایی را نشان می‌دهد.',
 'intro': [
  'شرکت‌های فنیِ انگلیسی‌زبان، «شخصیتِ کاری» را به همان اندازهٔ «مهارتِ کد» می‌سنجند — و ابزارش مصاحبهٔ رفتاری است: چهل‌دقیقه سوال‌های «یک موقعیت بگو…». تازه‌واردِ غیرِبومی دو خطر دارد: جواب‌های خیلی کوتاه (چون زبان دیر می‌آید) و جواب‌های انتقاد-محور از کارفرمای قبلی (چون راستش را می‌گوید بدونِ قالب!). این درس هر دو را درمان می‌کند.',
  'فرمولِ STAR را در درس ۴۷ گرفتی؛ اینجا همان فرمول، روی پنج موقعیتِ واقعیِ مهندسی پیاده می‌شود — و هر کدام را با تجربهٔ خودت بازسازی می‌کنی (پنج داستانِ پشتیبان، پوششِ همهٔ سوال‌های رفتاریِ رایج).',
 ],
 'sections': [
  {'h2': 'پنج موقعیتِ طلایی؛ داستان‌هایی که باید داشته باشی',
   'blocks': [
    ('table', ['سوالِ نوعی', 'داستانِ پشتیبانِ تو', 'نکتهٔ امضا'],
     [['تعارضِ فنی', 'بر سرِ framework/معماری با همکار', 'نتیجه: «همِ دیتا/لید تصمیم گرفت» — نهِ «من بردندم»'],
      ['شکست/حادثه', 'باگی که شکار کردی یا ساخت که شکست', 'مالکیت کامل + درسِ سیستمی'],
      ['ضرب‌الاجلِ سخت', 'تحویلِ under pressure', '«چه حذف کردی» بگو — نهِ «چقدر خواب کم کردم»'],
      ['همکاریِ cross-team', 'با design یا QA یا محصول', 'زبانِ مشترکِ ساختی — ترجمهٔ فنی'],
      ['مخالفتِ با تصمیم', 'دیدگاهت گفته شد و تصمیم برخلاف رفت', 'disagree and commit — و جمله‌اش']]),
    ('p', 'نمونهٔ STARِ کاملِ تعارضِ فنی: **S:** "We were choosing the state library for the app — I pushed for X, my tech lead for Y." **T:** "We had a week to decide, and the whole sprint was waiting on it." **A:** "Instead of debating in comments, I built a one-page prototype with each option and we ran our two hardest screens through both. I also asked two seniors from another team for a sanity check — openly, so it wasn\'t me vs him." **R:** "The data clearly favored Y — I was wrong about the ergonomics. We shipped Y, and I documented the trade-offs so the next team wouldn\'t relitigate it. Honestly, it made me a better engineer." — داستانِ کاملِ امضادار: پروتوتایپ به‌جای جنگ، پذیرشِ داده، و مستندسازی. مسیرِ جواب، از «چه کسی برد» به «چه چیزی یاد گرفتم» رفت.'),
   ]},
  {'h2': 'سوال‌های فرهنگی؛ «آینه»های شرکت',
   'blocks': [
    ('p', 'سه سوالِ culture-محور و جوابِ امضادار: **"Why are you leaving your current job?"** — همیشه به‌سمت: "I\'ve grown a lot there, but the problems I want to work on — scale, payments, big traffic — live at a bigger pond. This role is exactly that." (از هیچ‌کس فرار نکردم؛ به چیزی می‌روم) **"What\'s your ideal work environment?"** — صادق و مشخص: "Clear goals, honest code review, and room to focus — I do my best work in deep-work blocks with async collaboration." **"How do you handle stress?"** — با سیستم نه با قهر: "I triage: what\'s the user impact, what can wait, who needs to know. Then I communicate early — stress shrinks when it\'s shared." — هر جواب، یک «شیوهٔ کارِ» تو را تبلیغ می‌کند؛ سوالِ فرهنگی، بیلبوردِ حرفه‌ای‌ بودن است.'),
    ('ex', 'I\'d rather flag a risk early and look cautious than stay quiet and look confident. That\'s saved two releases in my last job.', 'ترجیح می‌دم زود خبرِ خطر رو بدم و محتاط به نظر بیام تا ساکت بمونم و مطمئن. این دوتا ریلیزِ شغلم رو نجات داد.'),
   ]},
  {'h2': 'پایانِ مصاحبهٔ رفتاری؛ سوال‌های تو و امضا',
   'blocks': [
    ('p', 'سه سوالِ شاخص از تو (برای مصاحبهٔ رفتاری): **"How does the team handle disagreements — what does a healthy debate look like here?"** (بحثِ سالم این‌جا چه شکلیه؟ — سوالِ فرهنگیِ هوشمندانه) · **"What do engineers who thrive here have in common?"** (مهندس‌هایی که این‌جا کمر می‌شکنند چه وجهِ مشترکی دارن؟) · **"What\'s the biggest challenge the team is facing this year?"** — و جملهٔ بستنِ هر مصاحبه: **"Thanks for the conversation — it made me more excited about the role. I hope to hear from you soon."** مصاحبهٔ رفتاری، گفتگوی «آیا با هم کار می‌کنیم؟» است؛ سوال‌های خوبِ تو، نصفِ جوابِ «بله» است.'),
   ]},
 ],
 'takeaway': 'پنج داستانِ STAR از قبل بساز: تعارضِ فنی، شکست، ضرب‌الاجل، cross-team، مخالفتِ تصمیم — هر کدام با نتیجهٔ یادگیری نه پیروزی. سوال‌های فرهنگی را با شیوهٔ کارت جواب بده (به‌سمت، نه فرار؛ سیستمِ استرس، نه قهر). سه سوالِ آینه‌ای از تیم بپرس و با جملهٔ بستنِ گرم، امضا کن. مهندسی، کارِ تیمیِ سنجیده است — مصاحبهٔ رفتاری، سنجشِ همین جمله.',
 'faq': [
  ('«Disagree and commit» یعنی چه و چرا همه می‌گویندش؟',
   'اصلِ مشهورِ آمازون/اپل: مخالفتت را کامل و صریح بگو، اما وقتی تصمیمِ نهایی شد، تمامِ Presenceات پای اجرای آن باشد — نه خرابکاریِ نرم. جمله‌اش در مصاحبه: **"I argued for the queue-based approach, we chose the cron-based one — I documented my concern and then implemented the chosen path fully. Turned out fine, and my concern never materialized."** همین داستان، دقیقاً همان چیزی است که «colleague-ی که می‌خواهم باشی» را می‌سازد.'),
  ('از مدیرِ قبلی‌ام بد حرف نزدم اما راستش هم بد بود!',
   'قاعدهٔ حرفه‌ای: هیچ‌وقت دربارهٔ آدم‌ها بد نگو؛ دربارهٔ سیستم‌ها صادق باش. قالبِ طلایی: **"The leadership style there was very top-down — I work best with more autonomy. That\'s what I\'m looking for, and it\'s exactly how you described this team."** (سبکِ مدیریتشون خیلی از-بالا-به-پایین بود — من با استقلالِ بیشتر بهتر کار می‌کنم. دنبالِ همینم و دقیقاً همین‌طوری تو تیمِ شما رو توصیف کردید.) — همان واقعیت، بستهٔ حرفه‌ای: تو را بزرگ می‌کند نه انتقادجو.'),
 ],
},
]

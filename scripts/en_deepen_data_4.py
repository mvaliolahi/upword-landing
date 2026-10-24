#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""گسترش درس‌به‌درس (v-deepen) · درس‌های ۵۵ تا ۷۲ — اشتباه‌های رایج + تمرین + چالش."""

DEEPEN = {
 # ── درس ۵۵ ──────────────────────────────────────────────────────────────
 'english-daily-standup': {
  'mistakes': [
   ('Yesterday I am working on the payment bug and I am fixing it.', 'Yesterday I worked on the payment bug and fixed it.', 'فارسی زمان را با قید نشان می‌دهد نه با فعل؛ وقتی «دیروز» را اولِ جمله می‌گذاری، مغز فعل را همان شکلی رها می‌کند که در ذهنش بود. قیدِ yesterday کل جمله را به گذشته می‌بَرد: worked، fixed.'),
   ('I am blocked by the staging credentials.', "I'm blocked on the staging credentials.", 'ترجمهٔ ذهنیِ «بلاکِ من توسطِ دسترسیِ staging است» by می‌گذارد؛ اما اصطلاحِ ثابتِ استندآپ blocked on است — آنچه بلاکت کرده، روی آن نشسته. by فقط وقتی درست است که فاعلِ انسانی کارِ بلاک‌کردن را انجام داده باشد.'),
   ('Today I am working on finish the retry tests.', "Today I'm working on finishing the retry tests.", 'فارسیِ «روی تمام‌کردنِ تست‌ها کار می‌کنم» بعد از حرفِ اضافه فعلِ خام می‌گذارد؛ بعد از working on یا اسم می‌آید یا فعلِ ing — finishing. «رویِ» فارسی با مصدرِ عریان می‌نشیند، on انگلیسی نه.'),
  ],
  'drills': (
   'چهار تمرینِ استندآپِ امروز؛ هر پاسخ را در سه ثانیه و با صدای بلند بگو، بعد باز کن و مقایسه کن. اگر سه تا از چهار را درست گفتی، درس سوخت.',
   [
    'جای خالی را پر کن: «Yesterday I ___ (finish) the pricing fix and ___ (ship) it.»',
    'حرفِ درست را انتخاب کن و دلیلش را بگو: «I\'m blocked ___ the vendor sandbox.» (by یا on؟)',
    'جملهٔ تحویل را کامل کن: «…I\'ll report by EOD. ___ — over to you.»',
    'ترجمه کن و بلند بگو: «دیروز روی باگِ CI کار کردم. امروز تست‌های retry را می‌نویسم. هنوز منتظرِ دسترسیِ staging هستم.» — سه‌جمله‌ایِ کلاسیکِ استندآپ.',
   ],
   [
    ('پاسخ تمرین ۱', '**finished … shipped** — **"Yesterday I finished the pricing fix and shipped it."** قیدِ yesterday هر دو فعل را گذشته می‌کند؛ دو فعلِ گذشته در یک نفس، ستونِ «دیروز»ِ استندآپ است.'),
    ('پاسخ تمرین ۲', '**on** — **"I\'m blocked on the vendor sandbox."** blocked on یعنی «دردم از این طرف است»؛ این حرفِ اضافه، بلوکر را در صفِ حل‌کردن می‌گذارد، نه در دادگاهِ متهمان.'),
    ('پاسخ تمرین ۳', '**That\'s me** — **"…I\'ll report by EOD. That\'s me — over to you."** جملهٔ تحویل، سکوتِ «تمام شد؟» را از استندآپ حذف می‌کند؛ تردیدِ آخرین ثانیه، دردسرِ اولین دقیقهٔ بعدی است.'),
    ('پاسخ تمرین ۴', '**"Yesterday I worked on the CI bug. Today I\'m writing the retry tests. I\'m still waiting on the staging access."** — دیروز با گذشته، امروز با استمرار، انتظار با still؛ سه زمانِ درس در سه جملهٔ ده‌ثانیه‌ای.'),
   ],
  ),
  'challenge': 'امشب استندآپِ فردایت را سه‌جمله‌ای بنویس — دیروز/امروز/بلوکر — و فردا در جلسه فقط همان سه جمله را بگو. استندآپِ خوب از قبل جوش خورده است، همان لحظه آب‌نشده.',
 },
 # ── درس ۵۶ ──────────────────────────────────────────────────────────────
 'english-code-review': {
  'mistakes': [
   ('This code is wrong, please fix it.', 'This swallows the error — could we log and rethrow here?', 'فارسیِ «این کد غلطه» نقد را با قاطعیتِ حکم می‌فرستد؛ کامنتِ ریلویوی حرفه‌ای رفتارِ کد را هدف می‌گیرد نه «درستی»ِ نویسنده را، و با could we نرم می‌شود. wrong حکم است؛ swallows the error مشاهده است.'),
   ('Please do the necessary changes.', 'Two nits: rename `data2` to `pricingSnapshot`, and this loop could be a helper — non-blocking.', 'ترجمهٔ اداریِ «تغییراتِ لازم را اعمال فرمایید» تهِ کامنت خالی است؛ «تغییراتِ لازم» دقیقاً همان چیزی است که ریلویو باید اسمش را ببرد. کامنتِ خوب = فهرستِ مشخص + برچسبِ درجه (Nit/Blocking).'),
   ('There is a problem in this line.', "I think there's an issue on line 42 — the loop starts at 1 instead of 0.", '«مشکل دارد» بدونِ حرفِ تعریف می‌ماند و «در خطِ چهل‌ودو» با in ترجمه می‌شود؛ قراردادِ ریلویو on line 42 است، مثلِ شماره‌گذاریِ صفحه. و مشکل را دقیق و بی‌تهدید توصیف کن، نه با لفظِ کلی.'),
  ],
  'drills': (
   'چهار تمرینِ ریلویو-نویسی؛ هر پاسخ را اول بلند بگو و بنویس، بعد باز کن — کامنتِ خوب، آینهٔ ذهنِ منظم است.',
   [
    'این کامنت را نرم و فنی‌اش کن: «This loop is bad. Delete it.» — با برچسب و مودالِ مشورتی.',
    'جملهٔ شرطیِ دوم را کامل کن: «If this ___ (be) a public API, I ___ (rename) it.»',
    'به PRی که فقط یک Nit دارد جوابِ کوتاهِ کامل بده — دو جمله، با رأیِ روشن.',
    'ترجمه کن: «نمی‌دانم چرا این بررسی لازم است. اگر ورودی خالی باشد چه می‌شود؟» — با برچسبِ Question.',
   ],
   [
    ('پاسخ تمرین ۱', 'نمونه: **"Question: do we need this loop at all? A hash map would do the job in one pass."** — «bad» رفت، برچسب آمد، مودال نشست؛ همان نقد، بدونِ زخم.'),
    ('پاسخ تمرین ۲', '**were … I\'d rename** — **"If this were a public API, I\'d rename it."** were با همهٔ سوژه‌ها و \'d برای نتیجهٔ فرضی؛ این است نرم‌ترین صدای ریلویو.'),
    ('پاسخ تمرین ۳', 'نمونه: **"Just the one nit, then LGTM — ship it."** رأیِ نهایی را با برچسب بده؛ «خوبه ولی…» مرج را معلق می‌کند.'),
    ('پاسخ تمرین ۴', '**"Question: I\'m not sure why we need this check — what happens if the input is empty?"** برچسب + عدمِ قطعیتِ صادقانه + سؤالِ مشخص؛ سه لایهٔ کامنتِ بی‌جنگ.'),
   ],
  ),
  'challenge': 'در ریلویوی بعدی‌ات یک کامنت را با قالبِ سه‌لایه بنویس: برچسب (Nit/Question/Blocking) + رفتارِ مشخص + مودالِ مشورتی؛ اگر ریلویویی در راه نیست، یکی از کامنت‌های قبلی‌ات را بازنویسی کن.',
 },
 # ── درس ۵۷ ──────────────────────────────────────────────────────────────
 'english-debugging-talk': {
  'mistakes': [
   ('This bug is from three days.', "It's been failing for three days.", 'فارسیِ «سه روزه است» با از/from ترجمه می‌شود؛ مدتْ for است — from نقطهٔ شروع را نشان می‌دهد نه طولِ دوره را. و «سه روزه جان می‌دهد» در انگلیسیِ زنده با حالِ کامل گفته می‌شود: It\'s been failing.'),
   ('The error is happen only when the server is busy.', 'The error only happens when the server is under load.', '«اتفاق می‌افتد» ذهنِ فارسی را به is + فعلِ خام می‌کشاند؛ happen فعلِ کاملِ ساده است. و قیدِ only چسبیده به فعل می‌نشیند، نه پراکنده در جمله. under load هم همان «بارِ زیاد»ِ تیم‌هاست.'),
   ('I tested it, it works in my machine.', 'I tested it — it works on my machine.', 'دو گرهِ معروف در یک جمله: ویرگولِ چسبنده (comma splice) که با خطِ تیره حل می‌شود، و in به‌جای on — «روی ماشینِ من» یعنی on my machine؛ همین جمله ضرب‌المثلِ دنیای دِو است، دست‌کم درستش بگو!'),
  ],
  'drills': (
   'زبانِ شکارِ باگ، زنجیرهٔ حدس و حذف است؛ چهار تمرین را بلند اجرا کن و بعد پاسخ‌ها را باز کن — استنتاجِ نصفه‌گفته، استنتاجِ نصفه‌فروخته است.',
   [
    'زنجیرهٔ استنتاج را کامل کن: «It ___ (can) be the DNS — localhost fails too. It ___ (must) be the connection pool.»',
    'ترجمه کن: «خودِ کوئری را حذف کردم؛ پس فقط کانفیگِ اتصال می‌ماند.» — با قالبِ ruled out / leaves.',
    'حالتِ بی‌ثباتِ معروف را گزارش کن: در staging کار می‌کند، در prod می‌میرد، لوکال هم بازسازی نمی‌شود.',
    'نتیجه را برای تیکت بنویس: «معلوم شد رِیس بین دو retry بود — هر دو قبل از تمام‌شدنِ اولی شلیک شدند» + بگو تستِ regression برایش چه می‌شود — با It turned out.',
   ],
   [
    ('پاسخ تمرین ۱', "**can't … must** — **\"It can't be the DNS — localhost fails too. It must be the connection pool.\"** استنتاجِ منفی با can't، استنتاجِ قوی با must؛ جفتِ مقدسِ دیباگ."),
    ('پاسخ تمرین ۲', '**"I\'ve ruled out the query itself — that leaves the connection config."** ruled out + that leaves: حذفِ مرحله‌ای، مسیرِ فکرت را برای هم‌تیمی شفاف می‌کند؛ شکارِ باگ رؤیای دیدنی نیست، گزارشِ راه‌رفته است.'),
    ('پاسخ تمرین ۳', 'نمونه: **"It works in staging but dies in prod — I can\'t reproduce it locally, even under the same load."** کنتراست + بازنشدنیِ صادقانه؛ همین یک قید، نصفِ تیم را به سمتِ درستِ مشکل می‌فرستد.'),
    ('پاسخ تمرین ۴', '**"It turned out to be a race between the two retries — both fired before the first one finished. I\'ve added a regression test so it can\'t sneak back in."** پایانِ هر شکار turned out to be است و بیمه‌اش regression test؛ نوشته‌شده در تیکت، دانش می‌ماند.'),
   ],
  ),
  'challenge': 'باگِ بازِ فعلی‌ات را برای یک همکار در سه جمله روایت کن: نشانه، حذف‌شده‌ها، حدسِ بعدی — و زنجیره را همان‌جا در تیکت کامنت کن.',
 },
 # ── درس ۵۸ ──────────────────────────────────────────────────────────────
 'english-agile-scrum': {
  'mistakes': [
   ('We will discuss about the scope in the planning.', "We'll discuss the scope in planning.", 'فارسیِ «درباره‌اش بحث می‌کنیم» about را به فعل می‌چسباند؛ discuss فعلِ گذراست و مستقیم مفعول می‌گیرد — discuss about در جلسه، امضای تازه‌واردِ فارسی‌زبان است. talk about درست است، discuss about نه.'),
   ('This story has five points.', "We pointed this story at five — it's a five.", 'فارسیِ «پنج امتیاز دارد» have می‌سازد؛ امتیاز در پوکرِ پلنینگ هویتِ استوری است نه ملکِ آن: it\'s a five. و فعلِ رسمیِ جلسه point است: we pointed it at five.'),
   ('I became volunteer for the SSO story.', 'I volunteered for the SSO story.', '«داوطلب شدم» فعلِ شدن دارد و مغز مستقیم became + volunteer می‌سازد؛ انگلیسیِ زنده volunteered برای خودش فعلِ کامل است. داوطلب‌شدن در انگلیسی یک‌کلمه‌ای اتفاق می‌افتد.'),
  ],
  'drills': (
   'پلنینگ، پوکرِ واژه‌هاست؛ چهار تمرین را بلند اجرا کن — انگار جلسهٔ پلنینگِ فرداست — و بعد پاسخ‌ها را باز کن.',
   [
    'جای خالی: «We pointed this story ___ five — it\'s a five.»',
    'اختلافِ پوکر را اعلام کن: «من ۳ دادم، او ۸.» — با قالبِ درس، گفتگوی دو‌دقیقه‌ای پیشنهاد بده.',
    'درجهٔ اطمینان را اعتراف کن: «حدسِ من پنج است — داده ندارم.» — با جفتِ gut یا data.',
    'ترجمه کن: «تایم‌اوتِ SSO را یک روز سقف می‌گذارم؛ اگر بیشتر خورد، چهارشنبه بازپلنینگ می‌کنیم.»',
   ],
   [
    ('پاسخ تمرین ۱', '**at** — **"We pointed this story at five — it\'s a five."** point به at چسبیده است؛ و امتیاز با is می‌آید نه have: امتیازْ هویتِ استوری است، نه چیزی که در جیبش دارد.'),
    ('پاسخ تمرین ۲', '**"We\'re a 3 and an 8 apart — let\'s talk for two minutes."** عددِ اختلاف + پیشنهادِ زمان؛ نه اصرار بر عددِ خود، نه سکوتِ سرشکن.'),
    ('پاسخ تمرین ۳', 'نمونه: **"Ballpark five — but that\'s gut, not data. If we want data, I\'d spike it for a day first."** اعتراف به منبعِ حدس، در پلنینگ اعتبار می‌سازد؛ حدسِ خودنما، تخمینِ دروغ است.'),
    ('پاسخ تمرین ۴', '**"I\'ll timebox the SSO timeout to a day — if it eats more, we re-plan on Wednesday."** timebox + شرطِ بازپلنینگ؛ پذیرفتنِ ریسک با سقف، زبانِ پلنینگِ بالغ است.'),
   ],
  ),
  'challenge': 'در پلنینگِ بعدی برای استوریِ مبهمْ سؤالِ «پرریسک‌ترینش کجاست؟» را بپرس و جواب را با یک تایم‌باکس ببند — یک سؤال، یک سقف، تمام.',
 },
 # ── درس ۵۹ ──────────────────────────────────────────────────────────────
 'english-technical-writing': {
  'mistakes': [
   ('You should run the script after you copied the config file.', 'Run the script after copying the config file.', 'داک جایِ ادبِ فارسیِ «بهتر است اجرا کنید» نیست؛ امریِ خنثیِ دوم‌شخص استانداردِ داک است — کوتاهی در داک بی‌احترامی نیست، احترام به وقتِ خواننده است. should باید برود.'),
   ('For install the app, run this command.', 'To install the app, run this command.', '«برایِ نصب» مستقیم با For + فعل ترجمه می‌شود؛ انگلیسیِ هدف to + مصدر می‌سازد. for فقط اسم می‌گیرد (for the setup) — فعل را نمی‌پذیرد.'),
   ('It is necessary that you do not edit this file.', 'WARNING: do not edit this file directly.', 'ترجمهٔ نامهٔ اداریِ «لازم است که…» رؤیای هشدار را می‌خواباند؛ هشدارِ داک با Do not + برچسبِ WARNING دو کلمه است و خواننده را بیدار می‌کند.'),
  ],
  'drills': (
   'داک‌نویسی، تمرینِ قیچی است؛ چهار تمرین را با برش‌های دقیق و بلند اجرا کن، بعد پاسخ‌ها را باز کن.',
   [
    'این جمله را امریِ داک کن: «You should probably copy .env.example to .env before you start.»',
    'غلطِ معروفِ for را اصلاح کن: «For run the tests, use this command.»',
    'برچسب را انتخاب کن و دلیلش را بگو: «داده‌های اولیه عمداً فیک‌اند» — WARNING یا NOTE؟',
    'سه گامِ راه‌اندازی را شماره‌دار بنویس: clone کردنِ ریپو، اجرای docker compose، بازکردنِ localhost — هر گام یک فعلِ امری.',
   ],
   [
    ('پاسخ تمرین ۱', '**"Copy `.env.example` to `.env` before you start."** — should probably حذف شد؛ امری + ترتیبِ گام. داکِ خوب مثل کامنتِ گیت است: کوتاه و قابلِ اجرا.'),
    ('پاسخ تمرین ۲', '**"To run the tests, use this command."** هدف با to + فعل: To run. for فقط اسم می‌گیرد — for the test run می‌شود، for run the tests هرگز.'),
    ('پاسخ تمرین ۳', '**NOTE** — **"NOTE: the seed data is fake by design."** WARNING برای فاجعه است و NOTE برای نکتهٔ غیرمنتظرهٔ بی‌خطر؛ برچسبِ اشتباه، آژیرِ بی‌اعتبار می‌سازد و آژیرِ بی‌اعتبار، آژیرِ مرده است.'),
    ('پاسخ تمرین ۴', 'نمونه: **"1. Clone the repo. 2. Run `docker compose up`. 3. Open `localhost:3000`."** — سه گام، سه فعلِ امری، هر گام زیرِ بیست کلمه؛ مقدمه لازم نیست.'),
   ],
  ),
  'challenge': 'برای کاری که امروز انجام دادی یک داکِ سه‌گامی بنویس — امریِ خنثی، بی‌مقدمه — و در ویکی یا فولدرِ مستنداتِ تیم بگذارش.',
 },
 # ── درس ۶۰ ──────────────────────────────────────────────────────────────
 'english-slack-communication': {
  'mistakes': [
   ('Hi. (تنها این — و سؤال، پنج دقیقه بعد در پیامِ جدای)', 'Hey Sara — quick one: is staging up?', 'ادبِ پیامِ فارسی یعنی سلامِ تنها و انتظار؛ در چتِ کاریِ انگلیسی سلام و خواسته در یک پیام می‌آیند — سلامِ تنها نامهٔ ناتمام است و دریافت‌کننده را در هیزم‌شکستنِ «سلام؟ …سلام؟» می‌گذارد.'),
   ('Did you saw my message?', 'Did you see my message?', 'فارسیِ «دیدی پیاممو؟» گذشتهٔ صرف دارد و ذهن saw را بعد از did نگه می‌دارد؛ did تمامِ گذشته را می‌خورد و فعل به شکلِ ساده برمی‌گردد. این خطا از چتِ روزانه تا مصاحبه گره می‌زند.'),
   ('I am sending it, please wait.', 'On it — will send in five.', 'ترجمهٔ اداریِ «دارم می‌فرستم، منتظر بمانید» در چت خشک و سنگین است؛ چتِ زنده فشرده است: On it / will send in five — فاعل حذف، زمانِ مشخص. please در هر جمله هم لحن را مصنوعی می‌کند.'),
  ],
  'drills': (
   'چت، زبانِ فشرده و کامل است؛ هر تمرین را اول خودت به‌سبکِ پیامِ واقعی بنویس، بعد پاسخ را باز کن.',
   [
    'سلامِ تنها را نجات بده: «Hi» + سؤالِ staging را در یک پیامِ درست بنویس.',
    'اصلاح کن و دلیل بگو: «Did you saw my message?»',
    'فشرده کن: «I am going to send it to you, please wait.» — حداکثر پنج کلمه.',
    'یک bump با دلیل بنویس: PRِ دیروز، تیکتِ مایگریشن منتظرش است، عجله هم نیست.',
   ],
   [
    ('پاسخ تمرین ۱', 'نمونه: **"Hey Sara — quick one: is staging up?"** سلام + نام + برچسبِ quick one + سؤال؛ چهار لایه در یک خط، هیچ‌وقت سلامِ تنها.'),
    ('پاسخ تمرین ۲', '**"Did you see my message?"** — did فعل را به ساده برمی‌گرداند: see. چکِ سه‌ثانیه‌ایِ ذهنی: اگر did در جمله است، فعل دیگر s و ed نمی‌گیرد.'),
    ('پاسخ تمرین ۳', '**"On it — will send in five."** فاعل حذف شد، going به will فشرده شد، زمان مشخص شد؛ چتِ حرفه‌ای، تلگرامِ انتظار نیست.'),
    ('پاسخ تمرین ۴', 'نمونه: **"@sara just bumping the PR from yesterday — it\'s holding the migration ticket. No rush, an LGTM unblocks us!"** bump + دلیل + نرمی؛ سه لایه‌ای که درخواستِ تکراری را بی‌آبرو نمی‌کند.'),
   ],
  ),
  'challenge': 'سه پیامِ کاریِ امروزت را بازنویسی کن: سلام و خواسته در یک خط، با یک نرم‌کننده (no rush / when you get a sec) — و فردا همان سبک را در اسلکِ واقعی بفرست.',
 },
 # ── درس ۶۱ ──────────────────────────────────────────────────────────────
 'english-interview-coding': {
  'mistakes': [
   ('I will solve it with hash map.', "I'd solve it with a hash map.", 'دو گره در یک جمله: فارسی حرفِ تعریف ندارد و a جا می‌افتد؛ و will قول می‌دهد — مصاحبه راه‌حلِ ذهنیِ در-دستِ تکامل می‌خواهد، I\'d پیشنهاد می‌دهد. حلِ مسئله با شرطیِ نرم شروع می‌شود نه با قول.'),
   ('The time of this solution is n square.', 'This runs in O(n²) time — quadratic.', '«مربعِ n» مستقیم n square می‌شود؛ نشانهٔ استاندارد O(n²) است و خواندنش «او-ان-اسکوئر» یا quadratic — مصاحبه‌گر فقط زبانِ استاندارد را می‌شنود، n square صدای ترجمه است.'),
   ('Let me to think a moment.', 'Let me think for a second.', '«بگذار یک لحظه فکر کنم» بعد از let me مصدرِ با to می‌سازد، چون «اجازه‌یِ دادن» در ذهن با to گره خورده؛ بعد از let me فعلِ خام می‌آید — let me think، بدونِ to.'),
  ],
  'drills': (
   'مصاحبهٔ کدنویسی، گفتارِ حینِ فکرکردن است؛ چهار تمرین را بلند و با وقفهٔ طبیعی اجرا کن، بعد پاسخ‌ها را باز کن.',
   [
    'برای مسئلهٔ «اولین کاراکترِ یکتا» دو سؤالِ شفاف‌ساز دربارهٔ ورودی بپرس.',
    'پیچیدگیِ راهِ بی‌رحمانه را کامل بگو: دو حلقهٔ تو-در-تو — زمان و فضا، هر دو.',
    'جملهٔ معاوضه را کامل کن: «I can trade ___ for ___: one pass with a hash map gives…»',
    'ردیابی را بلند اجرا کن: برای رشتهٔ swiss شمارش‌ها را بگو و پاسِ دوم را گزارش کن.',
   ],
   [
    ('پاسخ تمرین ۱', 'نمونه: **"Quick clarifications — can the string be empty? And is it case-sensitive?"** شفاف‌سازی امتیازِ مستقلِ مصاحبه است؛ سکوتِ شروعِ فوری، نمرهٔ communication را می‌سوزاند.'),
    ('پاسخ تمرین ۲', '**"The brute force is O(n²) — two nested loops, and constant space."** دو بُعدِ پیچیدگی همیشه با هم گفته می‌شوند؛ جملهٔ نصفه در مصاحبه، فکرِ نصفه شنیده می‌شود.'),
    ('پاسخ تمرین ۳', '**"...trade memory for speed: one pass with a hash map gives O(n) time at O(n) space."** معاوضه با trade X for Y — «حافظه را با سرعت»؛ for یعنی «به‌عوضِ»، نه «به».'),
    ('پاسخ تمرین ۴', '**"Let me trace: swiss — counts are s:3, w:1, i:1. The second pass finds w."** ردیابیِ بلند هم تستِ ذهنی است هم نمایشِ ذهنِ منظم؛ نمره، مسیرِ فکر را هم می‌خرد.'),
   ],
  ),
  'challenge': 'امروز یک مسئلهٔ سادهٔ برنامه‌نویسی را بلند حل کن — شفاف‌سازی، طرح، ردیابی، همه با صدا. مصاحبه از گوشِ تمرین‌ندیده عبور نمی‌کند.',
 },
 # ── درس ۶۲ ──────────────────────────────────────────────────────────────
 'english-interview-system-design': {
  'mistakes': [
   ('I will use from Redis for the cache.', "I'd put Redis in front of the database for caching.", 'فارسیِ «استفاده از Redis» حرفِ اضافهٔ از را به فعل می‌چسباند؛ use گذراست و مستقیم مفعول می‌گیرد — use from صدای ترجمهٔ نسل‌هاست. و در طراحی، Redis جلوی دیتابیس می‌نشیند: in front of، نه فقط use.'),
   ('This system can handle one million user.', 'The system can handle a million users.', 'بعد از عددِ بزرگ، اسم جمع می‌شود: a million users؛ فارسیِ «یک میلیون کاربر» بدونِ s می‌ماند و حرفِ تعریفِ a هم غالباً جا می‌افتد. مقیاسْ شمرده می‌خواهد: عدد + جمع + حرفِ تعریف.'),
   ('If the traffic increases, we increase the servers.', 'If traffic grows, we scale horizontally — add more nodes behind the load balancer.', '«سرورها را بیشتر می‌کنیم» با increase تکرار می‌شود؛ مقیاس در انگلیسیِ سیستم‌ها فعلِ خودش را دارد: scale horizontally / scale up. increase the servers صدای گزارشِ فارسی است، scale زبانِ طراحی است.'),
  ],
  'drills': (
   'طراحیِ سیستم، گفتارِ trade-off است؛ چهار تمرین را با صدای مصاحبهٔ واقعی بگو — عدد، گزینه، معاوضه — بعد باز کن.',
   [
    '«بستگی دارد» را با دو گزینه ببند: نسبتِ خواندن/نوشتن ۱۰۰:۱ — چه می‌کنی؟ (دو جمله)',
    'عدد را بلند حساب کن: «۵۰ میلیون کاربر در روز، یعنی چند درخواست در ثانیه؟»',
    'جملهٔ سازگاری را کامل کن: «برایِ دسترس‌پذیری، سازگاریِ نهاییِ شمارنده‌ها را در عوضِ آن ___ می‌کنیم.»',
    'افتِ مؤدبانه را توضیح بده: p99 پرید — کاربر چه می‌بیند؟ (دو جمله)',
   ],
   [
    ('پاسخ تمرین ۱', 'نمونه: **"It depends on the read/write ratio — at 100:1 I\'d cache aggressively; if writes were heavy, I\'d shard first."** depends بدونِ گزینه دوری است؛ با دو گزینه، تحلیل است.'),
    ('پاسخ تمرین ۲', '**"Fifty million a day is about 600 requests per second — call it a thousand at peak."** حسابِ بلندِ عدد، تُردِ شروعِ طراحی است؛ عددِ شمرده، درِ بحث را باز می‌کند.'),
    ('پاسخ تمرین ۳', '**"...we accept eventual consistency on the counters in exchange for availability."** قالبِ ثابت: accept X in exchange for Y. معاوضهٔ فنی «در عوضِ» با in exchange for گفته می‌شود، نه با ترجمهٔ زیروروی instead of.'),
    ('پاسخ تمرین ۴', 'نمونه: **"If p99 spikes, we degrade gracefully — serve the cached page with a \'cached\' badge rather than an error."** افتِ مؤدبانه یعنی بخشی می‌میرد، کل نمی‌میرد؛ همین جمله، بلوغِ طراحی را نشان می‌دهد.'),
   ],
  ),
  'challenge': 'یک سیستمِ آشنا (فیدِ شبکهٔ اجتماعیِ محبوبت) را در سه جمله برای دوستِ غیرفنی طراحی کن: نسبتِ خواندن/نوشتن با عدد، یک trade-off با I\'d — و بعد بپرس چه چیزی گیرش کرد.',
 },
 # ── درس ۶۳ ──────────────────────────────────────────────────────────────
 'english-behavioral-interview': {
  'mistakes': [
   ('In my previous job I was responsible of the payments.', 'In my last role, I owned the payments service.', 'فارسیِ «مسئولِ» را مغز با responsible of می‌فرستد؛ درستش responsible for است — اما در مصاحبهٔ رفتاری، مالکیت قوی‌تر است: owned. مالکیت، زبانِ رشد است؛ مسئولیت، زبانِ شرحِ شغل.'),
   ('I learned many things from this experience.', 'That incident taught me two things I still use: the canary rule and the postmortem habit.', '«چیزهای زیادی یاد گرفتم» جملهٔ مردهٔ مصاحبه‌هاست؛ مصاحبه‌گر منتظرِ درسِ نام‌بردنی است: دو چیزِ مشخص که هنوز استفاده می‌کنی. STAR بدونِ Rِ شمرده، قصهٔ بیکسری است.'),
   ('We should wait, my manager said.', 'My manager said we should wait. I said: give me one day.', 'فارسی نقل را تهِ جمله می‌گذارد («…گفت») و ترتیب را برعکس می‌چیند؛ انگلیسی گوینده اول می‌آید و said بعد. و داستانِ رفتاری با گفت‌وگوی مستقیم جان می‌گیرد: He said / I said.'),
  ],
  'drills': (
   'سه داستانِ آماده، سرمایهٔ مصاحبهٔ رفتاری‌اند؛ چهار تمرین را با داستانِ واقعیِ خودت پر کن و بلند بگو، بعد باز کن.',
   [
    'S و T را بگو: وسطِ لانچ بودید که… — دو جمله با گذشته.',
    'جملهٔ ضعفِ در-درمان را کامل کن: «I used to over-commit; now I consciously…»',
    'R را با اثرِ ماندگار ببند: چک‌لیستی که نوشتی هنوز merge check است — یک جمله.',
    'نقلِ گفتگو را درست بگو: مدیر گفت عقب بیندازیم؛ تو گفتی یک روز بده — قالبِ درست را به‌کار ببر.',
   ],
   [
    ('پاسخ تمرین ۱', 'نمونه: **"We were mid-launch when the payment provider started timing out — Black Friday week."** موقعیت + تنگنا در دو جمله؛ گذشتهٔ ساده، زمانِ داستان است.'),
    ('پاسخ تمرین ۲', '**"...now I consciously say: \'If I take this, what moves out?\' — out loud, in planning."** قالبِ سه‌ضلعی: used to + آگاهانه + جملهٔ عملی؛ ضعفِ بدونِ سیستمِ جدید، اعترافِ بی‌پایان است.'),
    ('پاسخ تمرین ۳', 'نمونه: **"We shipped on time — and the canary checklist we wrote is still a merge check today."** R دو لایه دارد: نتیجهٔ آن روز و اثرِ مانده. still در استفاده، طلای مصاحبهٔ رفتاری است.'),
    ('پاسخ تمرین ۴', '**"My manager said we should wait. I said: give me one day."** گوینده اول، said دوم؛ نقلِ مستقیمِ کوتاه، ضربانِ قصه است. ترتیبِ فارسی را برنگردان.'),
   ],
  ),
  'challenge': 'امشب یکی از سه داستانت (تعارض/شکست/ددلاین) را ۹۰ ثانیه ضبط کن — با نقلِ گفتگو و Rِ ماندگار — و یک بار بازشنو؛ جایی که لحن مکث کرد، تمرینِ فرداست.',
 },
 # ── درس ۶۴ ──────────────────────────────────────────────────────────────
 'english-demos-presentations': {
  'mistakes': [
   ('Now I want to show you a small thing.', 'Watch what happens when I click here.', '«می‌خواهم چیزی نشانتان دهم» مقدمهٔ مؤدبانهٔ فارسی است؛ دموی زنده با امریِ خنثی شروع می‌شود: Watch / Notice — چشمِ تماشاگر را به صفحه می‌چسباند، نه به حافظهٔ گوینده.'),
   ('You should wait some seconds.', "Give it a second — it's computing on the fly.", '«چند ثانیه صبر کنید» مستقیم wait some seconds می‌شود؛ some با ثانیه‌های شمرده غریب است. جملهٔ زنده: give it a second — سکوتِ محاسبه را به بخشی از دمو تبدیل می‌کند، نه به عذرخواهیِ خشک.'),
   ('This bug is normal, don\'t worry.', "And… that's a bug. Good catch by the demo gods — this is exactly why we demo.", 'انکارِ باگ («عادیه، نگران نباشید») در دمو اعتماد را می‌کُشد؛ جملهٔ آمادهٔ حرفه‌ای‌ها لحظه را با شوخیِ فرایند به اعتبار تبدیل می‌کند. باگِ دموی زنده شکستِ تو نیست؛ آزمایشِ قبلِ شِپ است.'),
  ],
  'drills': (
   'دمو، اجرای زنده است؛ چهار تمرین را انگار جلوی تیم ایستاده‌ای بلند اجرا کن، بعد پاسخ‌ها را باز کن.',
   [
    'نگاه را به صفحه ببر: یک جملهٔ امری با Watch یا Notice برای کلیکِ دکمهٔ Add بنویس.',
    'انتظار و واقعیت را بگو: «انتظارِ لودینگ داشتی — به‌جایش آنی بود.»',
    'جملهٔ نجاتِ لحظهٔ کرش را آماده کن — با شوخیِ فرایند.',
    'دمو را ببند: دو کلیک، ۳۰۰ میلی‌ثانیه، خطای زیرِ ۰/۱٪ — و درخواستِ go/no-go.',
   ],
   [
    ('پاسخ تمرین ۱', '**"Watch the top bar — I\'m adding three items now."** امری + استمرارِ همزمان؛ دستورِ دیدن، تماشاگر را از شنونده به شاهد تبدیل می‌کند.'),
    ('پاسخ تمرین ۲', '**"You\'d expect a spinner there — instead, it\'s instant."** قالبِ دولایه: you\'d expect + instead؛ زبانِ دمو برای گفتنِ «چه چیزی عادی بود و چه چیزی عجیب».'),
    ('پاسخ تمرین ۳', '**"And… that\'s a bug. Good catch by the demo gods — this is exactly why we demo before shipping."** جملهٔ آمادهٔ لحظهٔ سکوت؛ خرابیِ جشن‌گرفته، اعتمادِ تماشاگر را بالا می‌برد نه اعتبارِ تو را پایین.'),
    ('پاسخ تمرین ۴', '**"So: two clicks, 300ms, error rate under 0.1% on staging. We\'re ready for the next rollout — I\'d love your go/no-go."** سه عدد + یک درخواست؛ دموی بی‌درخواست، تماشاست نه تصمیم.'),
   ],
  ),
  'challenge': 'یک فیچرِ واقعی را برای یک دوست پنج دقیقه دمو بده: با جملهٔ امری شروع کن و با عدد و درخواست ببند — بعد از او بپرس کدام جمله در ذهنش ماند.',
 },
 # ── درس ۶۵ ──────────────────────────────────────────────────────────────
 'english-estimations-deadlines': {
  'mistakes': [
   ('This work needs two weeks time.', 'This will take about two weeks, give or take.', '«دو هفته زمان می‌برد» با needs + time ترجمه می‌شود؛ فعلِ استانداردِ تخمین take است — it takes two weeks — و about / give or take بازه را صادقانه می‌کند. تخمینِ بی‌بازه، قولِ قایم‌شده است.'),
   ('I will finish it until Friday.', "I'll finish it by Friday.", 'جفتِ مرگبارِ until/by: فارسیِ «تا جمعه» هر دو را یکی ترجمه می‌کند؛ ددلاین with by — until ادامهٔ رخداد می‌خواهد (the flaky sandbox stays until Friday). این یکی، مرزِ تخمینِ حرفه‌ای و آماتور است.'),
   ('Everything is going good, no problem.', "We're on track — no risks so far.", '«کارها خوب پیش می‌رود» going good می‌سازد — قید well است نه good؛ و no problem مستقیم از «مشکلی نیست». وضعیتِ اسپرینت اسم دارد: on track / at risk / slipping — نام‌گذاریِ وضعیت، نصفِ مدیریتِ پروژه است.'),
  ],
  'drills': (
   'تخمین، زبانِ بازه و شرط است؛ چهار تمرین را با جمله‌های کامل و شمرده بلند بگو، بعد پاسخ‌ها را باز کن.',
   [
    'بازه بده: مایگریشن — حدوداً سه روز، ± یک روز، با فرضِ خوب‌رفتاریِ سندباکس.',
    'اصلاح کن و توضیح بده: «I will finish the migration until Friday.»',
    'سه برچسبِ وضعیت را در سه جملهٔ جدا بیاور: on track / at risk / slipping — با استوری‌های واقعی از ذهنت.',
    'خبرِ بد را با سه گزینه بده: دیتای قدیمی از نمونه کثیف‌تر است، دمو جمعه — قالبِ درس.',
   ],
   [
    ('پاسخ تمرین ۱', '**"Ballpark: three days, give or take a day — assuming the vendor sandbox behaves."** بازه + give or take + assuming؛ سه لایهٔ تخمینِ قابلِ دفاع.'),
    ('پاسخ تمرین ۲', '**"I\'ll finish the migration by Friday."** ددلاین با by است؛ until یعنی «تا وقتی که جمعه بیاید ادامه دارد» — برای وضعیت‌هاست، نه برای لحظهٔ تحویل.'),
    ('پاسخ تمرین ۳', 'نمونه: **"The retry tests are on track. The SSO timeout is at risk — I\'m 60% through and the data is dirtier than we sampled. The demo is slipping — I\'d move it to Monday."** سه برچسب، سه وضعیتِ واقعی؛ نام‌گذاری، مسیرِ گفتگو را با مدیر هموار می‌کند.'),
    ('پاسخ تمرین ۴', 'نمونه: **"Heads-up: the import is at risk. Three options — cut the historical import, slip the demo to Monday, or I hero it overnight, which I don\'t recommend. My call: option one."** خبرِ بد + سه گزینه + یک پیشنهاد؛ مدیر با گزینه حرف می‌زند، با فاجعه فقط فریاد.'),
   ],
  ),
  'challenge': 'برای کاری که همین حالا درگیرش هستی یک تخمینِ سه‌لایه بنویس (بازه + فرض + ریسک) و برای همکارت در چت بفرست — امروز، در خطِ واقعی.',
 },
 # ── درس ۶۶ ──────────────────────────────────────────────────────────────
 'english-product-client-talks': {
  'mistakes': [
   ('This feature is very easy, I do it in one day.', "This is a small change — I can have it out in a day or two.", '«خیلی راحته!» در گفتگو با محصول/مشتری ارزشِ کار را می‌کُشد: کارِ آسانْ ارزان می‌شود. زبانِ حرفه‌ای small/simple است و بازهٔ یک-دو روز جایِ قولِ دقیقِ یک‌روزه — فروتنی، بی‌پول‌کردن نیست؛ قیمت‌گذاریِ درست است.'),
   ('This is not possible from technical view.', "It's technically possible — but it would push the release back a week. Here's the trade-off.", '«از نظرِ فنی» مستقیم from technical view می‌شود؛ قیدِ درست technically است. و «غیرممکن» در گفتگو با غیرفنی یعنی درِ بسته؛ مهندسِ حرفه‌ای possible را نگه می‌دارد و هزینه را جلوی چشم می‌آورد.'),
   ('Sorry, it is not possible.', "That's not doable this week — but here's what I can do by Friday.", 'جوابِ «نمی‌شود» در ذهنِ فارسی ما کامل است؛ انگلیسیِ خدمات «نه» را هرگز تنها نمی‌فرستد: نه + آنچه می‌شود. what I can do قابِ نجاتِ رابطه است.'),
  ],
  'drills': (
   'گفتگو با غیرفنی، ترجمهٔ فعل به اثر است؛ چهار تمرین را بلند اجرا کن — انگار PM جلوی تو ایستاده — بعد باز کن.',
   [
    'اثر را بگو نه فعل: «این سوییچِ کوچک در واقع دیتابیس را درگیر می‌کند» — با touches.',
    'دو گزینه بده و تصمیم را بسپار: A این هفته شِپ می‌شود ولی برای حرفه‌ای‌ها می‌شکند؛ B دو هفته می‌برد و برای همه کار می‌کند — با Your call.',
    'برای مشتریِ بی‌حوصله یک جملهٔ کامل بگو: فیکس امشب لایو؛ اگر فردا صبح چیزی خراب بود، مستقیم زنگ بزن.',
    '«نه» را با پیشنهاد بفرست: گزارشِ فردا واقع‌بینانه نیست — گزارشِ کامل جمعه + یک‌خطِ خلاصه امشب.',
   ],
   [
    ('پاسخ تمرین ۱', '**"This \'tiny toggle\' actually touches the database — the cheap version only applies to new users."** touches، فعلِ درستِ «درگیر می‌کند»؛ و راهِ ارزان را همان‌جا کنارِ مشکل بگذار — مشکل + راهِ فرار در یک نفس.'),
    ('پاسخ تمرین ۲', '**"Option A ships this week but breaks for power users; Option B takes two weeks and works for everyone. Your call."** دو گزینهٔ متقارن + Your call؛ سپردنِ تصمیم با دو گزینه، همکاری است نه فرار.'),
    ('پاسخ تمرین ۳', '**"The fix goes live tonight — if anything looks wrong tomorrow morning, call me directly."** چه می‌شود + چه زمانی + اگر خراب شد چه؛ یک جمله، تمامِ آرامشِ لازم.'),
    ('پاسخ تمرین ۴', '**"Tomorrow isn\'t realistic — but here\'s what I can do: the full report Friday, plus a one-line summary tonight."** «نه» تنها نمی‌رود؛ what I can do همان قابی است که «نه» را قابلِ شنیدن می‌کند.'),
   ],
  ),
  'challenge': 'یک درخواستِ غیرفنیِ این هفته را با قالبِ «واقعیت + دو گزینه + Your call» در یک پیامِ واقعی بنویس — حتی اگر مخاطبش فقط یک دوستِ فنی باشد، لحن را بساز.',
 },
 # ── درس ۶۷ ──────────────────────────────────────────────────────────────
 'english-one-on-ones-feedback': {
  'mistakes': [
   ('You are always giving late updates.', "When updates land after the fact, I can't plan around them.", '«همیشه دیر خبر می‌دهی» always روی شخص می‌نشیند و جمله را اتهام می‌کند؛ قالبِ حرفه‌ای رفتار + اثر است: When X, I can\'t Y. بازخوردِ رفتاری آینه است — نه چاقو.'),
   ('I have a feedback for you.', 'I have a piece of feedback for you.', 'feedback مثل information غیرقابل‌شمارش است؛ فارسیِ «یک بازخورد» a feedback می‌سازد — همان قدِ «یک informations». قطعه‌اش را بگوییم: a piece of feedback یا some feedback.'),
   ('Thank you for your good words.', "Thanks — that's really good to hear.", '«ممنون از حرف‌های خوبت» مستقیم good words می‌شود و خشک می‌نشیند؛ جوابِ زنده good to hear است — و بعدش بازخورد را با سؤال ادامه بده تا گفتگو شود، نه گواهیِ پایان‌یافته.'),
  ],
  'drills': (
   '1:1، گفتگوهای کوچکِ بزرگ است؛ چهار تمرین را با قالب‌های درس و لحنِ گرم بلند اجرا کن، بعد باز کن.',
   [
    'بازخورد را با قالب بساز: «وقتی آپدیت‌ها دیر می‌رسد، برنامه‌ریزیِ من می‌شکند — جمعه دو خط جمع‌بندی بگذاریم؟»',
    'اصلاح کن و توضیح بده: «I have a feedback for you.»',
    'بازگویی کن: مدیر گفت «ساکت می‌شوی، بعد همه‌چیز یک‌جا می‌آید» — با So the pattern is…',
    'دو سؤالِ آینه را بپرس: یکی برایِ ادامه‌دادن، یکی برایِ تفاوت — با واژهٔ one.',
   ],
   [
    ('پاسخ تمرین ۱', '**"When updates land after the fact, I can\'t plan around them — could we end Friday with a two-line recap?"** رفتار + اثر + درخواستِ مشخص؛ سه‌ضلعیِ بازخوردِ قابلِاجرا.'),
    ('پاسخ تمرین ۲', '**"I have some feedback for you."** (یا a piece of feedback) — feedback شمرده نمی‌شود؛ a feedback در جملهٔ اولِ 1:1، اولین برچسبِ غیربومی‌سازی است.'),
    ('پاسخ تمرین ۳', '**"So the pattern is: silence, then a flood — did I get that right?"** بازگوییِ الگو با جملهٔ خودت + چک؛ دفاع جای بازگویی نیست.'),
    ('پاسخ تمرین ۴', '**"What\'s the one thing I should keep doing? And what\'s the one thing I should do differently?"** keep + differently، دو سؤالِ آینهٔ هر 1:1؛ one آن را از آرزو به برنامه می‌رساند.'),
   ],
  ),
  'challenge': 'در 1:1 بعدی دو سؤالِ آینه را واقعی بپرس و جواب‌ها را یادداشت کن — و یک بازخورد را با قالبِ When + اثر + درخواست بده، همین هفته.',
 },
 # ── درس ۶۸ ──────────────────────────────────────────────────────────────
 'english-disagreeing-technically': {
  'mistakes': [
   ("I don't agree with this approach, it will fail in the weekend traffic.", "I'm not convinced this handles the weekend traffic — can we look at the numbers?", 'مخالفتِ فارسی دوقطبی می‌سازد: موافقم/نمی‌موافقم؛ مخالفتِ سنیور قانع‌نشدن را می‌گوید — I\'m not convinced — و بلافاصله داده می‌طلبد. «شکست می‌خورد» پیشگویی است و پیشگویی در اتاقِ فنی، ادب نیست؛ سؤال است.'),
   ('Your idea is good but my idea is better for this case.', "Your point about replay is real — my worry is the ops load this quarter.", 'مالکیتِ ایده‌ها — your idea / my idea — جنگِ دوقطبی می‌سازد؛ مخالفتِ حرفه‌ای اول نکتهٔ طرف را می‌خرد (your point is real) و بعد نگرانی‌اش را با my worry نشان می‌دهد. مالکیت حذف می‌شود، مسئله می‌ماند.'),
   ('If we start from zero, I choose the queue.', "If we were starting fresh, I'd go with the queue — but given the migration, the cron version buys us more.", 'شرطیِ دومِ مخالفت با were و I\'d ساخته می‌شود؛ فارسیِ «اگر از صفر شروع کنیم» حالِ واقعی می‌ماند و لحنْ حکم می‌گیرد. were فرض را فرض نگه می‌دارد — همان نرمیِ گفتاریِ مهندسانِ سنیور.'),
  ],
  'drills': (
   'مخالفتِ فنی، مهارتِ گفتنِ «نه» با باز-گذاشتنِ در است؛ چهار تمرین را با لحنِ آرام و بلند اجرا کن، بعد باز کن.',
   [
    'با شرطیِ دوم مخالفت بگو: «اگر کاغذِ سفید بود، صف را برمی‌داشتم — ولی با این مایگریشن، کرون بیشتر می‌خرد.»',
    'اول نکتهٔ طرف را بخر، بعد نگرانی‌ات را بیاور: اعتبارِ replay + بارِ اپس — دو جمله.',
    '«قانع نیستم» را با داده بگو: ترافیکِ آخرِ هفته — قبل از تعهد، به اعداد نگاه کنیم؟',
    'فسخِ مؤدبانه را پیشنهاد بده: «سه ماه بعد با دیتای واقعی دوباره ببینیمش.» — با revisit.',
   ],
   [
    ('پاسخ تمرین ۱', '**"If this were a clean slate, I\'d go with the queue — but given the migration, the cron version buys us more."** were + \'d: فرض، فرض می‌ماند؛ لحنْ مشورت است نه حکم.'),
    ('پاسخ تمرین ۲', '**"Your point about replay is real — I\'m not dismissing it. My worry is the ops load this quarter."** خریدنِ نکته + نامیدنِ نگرانی؛ دو حرکتِ نخستِ هر مخالفتِ محترمانه.'),
    ('پاسخ تمرین ۳', '**"I\'m not convinced this handles the weekend traffic — can we look at the numbers before we commit?"** قانع‌نشدن + درخواستِ داده؛ نه «موافق نیستم»، نه سکوت.'),
    ('پاسخ تمرین ۴', '**"Let\'s revisit this in three months with real data."** revisit + قیدِ زمان: مخالفتِ امروز را به حقِ بازگشتِ فردا تبدیل می‌کند — بحث بسته می‌شود، در باز می‌ماند.'),
   ],
  ),
  'challenge': 'در بحثِ فنیِ بعدی فقط روی لحن تمرکز کن: اول نکتهٔ مخالف را با یک جمله بخر، بعد نگرانی‌ات را با my worry بگو — لحنْ حتی وقتی حق با توست، امتحان می‌شود.',
 },
 # ── درس ۶۹ ──────────────────────────────────────────────────────────────
 'english-joining-new-team': {
  'mistakes': [
   ('I am new here and I don\'t know anything.', "I'm still building the map — I don't have the context yet.", '«هیچی نمی‌دانم» ترجمهٔ زیروروی صدای ناامید می‌دهد؛ زبانِ ادغامِ حرفه‌ای جهل را موقت جا می‌زند: still building the map، هنوز زمینه ندارم (yet). ندانستنِ ماهِ اول عیب نیست؛ خام‌گوییِ آن عیب است.'),
   ('Can you explain me why this service is separate?', 'Could you explain why this is a separate service?', 'فارسیِ «برام توضیح بده» فعل را مستقیم به آدم می‌چسباند؛ explain در انگلیسی to می‌خواهد — explain it to me — یا مفعولِ انسانی را کلاً حذف کن و با Could نرم بفرست. explain me صدای ترجمهٔ دقیق است.'),
   ('What means this flag in the config file?', 'What does this flag in the config mean?', 'فارسیِ «این یعنی چی؟» ترتیبِ واژه‌ها را تکان نمی‌دهد و سؤال با What means شروع می‌شود؛ انگلیسی فعلِ کمکی does لازم دارد و فعلِ اصلی ته می‌نشیند. این خطا در چتِ تیمِ تازه هر روز دیده می‌شود.'),
  ],
  'drills': (
   'ادغام، تمرینِ سؤالِ درست و اعترافِ دقیق است؛ چهار تمرین را مثل روزهای اولِ تیمِ جدید بلند اجرا کن، بعد باز کن.',
   [
    'زمینه را نرم بخواه: «چرا این‌جوری ساخته شده؟» — با قالبِ walk me through.',
    'حدس را با بیمه بگو: «اگر اشتباه می‌کنم اصلاح کن، ولی به‌نظرم بعد از جاافتادنِ مایگریشن می‌شود دوباره دیدش.»',
    'شکافِ بازت را گزارش کن: نقشهٔ کدبیس این هفته جا افتاد؛ پایپ‌لاینِ دپلوی را دیده‌ام ولی نرانده‌ام.',
    'بازخوردِ اولین برداشت را درخواست کن: پنج دقیقه — چشمِ تازه زود کم‌رنگ می‌شود.',
   ],
   [
    ('پاسخ تمرین ۱', '**"Could you walk me through why it\'s built this way?"** walk me through یعنی «برایم قدم‌به‌قدم روایت کن»؛ سؤالِ چرا با این قالب، تاریخ را بی‌محکمه بیرون می‌کشد.'),
    ('پاسخ تمرین ۲', '**"Correct me if I\'m wrong, but it feels like something we could revisit once the migration settles."** بیمهٔ پیشِ حدس + نرمیِ could: حدسِ تازه‌وارد را محترم و بی‌خطر می‌کند.'),
    ('پاسخ تمرین ۳', '**"The codebase map clicked this week. My open gap is the deploy pipeline — I\'ve watched it, never driven it."** بردِ کوچک + شکافِ صادقانه؛ دقت، زبانِ ماهِ اول است، بلاغت نیست.'),
    ('پاسخ تمرین ۴', '**"Could I get five minutes of first-impression feedback? Fresh eyes fade fast."** درخواستِ مشخص + دلیلِ زمانی: چشمِ تازه کالای فاسدِ سه‌ماهه است!'),
   ],
  ),
  'challenge': 'به همکاری که بیش از شش ماه است در تیم است سه سؤالِ walk me through بپرس و پاسخ‌ها را یادداشت کن — یادداشت‌هایت، داکِ اولین بردِ توست.',
 },
 # ── درس ۷۰ ──────────────────────────────────────────────────────────────
 'english-mentoring-juniors': {
  'mistakes': [
   ('This is good, continue.', 'The retry logic here saved the timeout case — keep doing this.', '«خوبه، ادامه بده» تعریفِ بی‌شاخص است؛ ستایشِ رشدساز سه لایه دارد: دقیقاً چه (retry logic)، چه اثری (saved the timeout case)، چه چیزی تکرار شود (keep doing this). continue امریِ سردِ گزارشِ کار است، نه مربی‌گری.'),
   ('Don\'t be shy to ask questions.', 'No such thing as a bad question here — ask early, ask often.', '«خجالت نکش سؤال بپرس» ترجمهٔ مستقیمِ don\'t be shy است و در انگلیسیِ منتورینگ ناهماهنگ به گوش می‌رسد — گفتمنِشان ممنوعیتِ خجالت نیست، اجازهٔ زودهنگامی است: ask early, ask often.'),
   ('I will learn you how the pipeline works.', 'Let me walk you through how the pipeline works.', 'فارسیِ «یادت می‌دهم» فعلِ یاد-دادن را با learn جابه‌جا می‌کند؛ learn گرفتن است و یاد-دادن teach/show/walk through. این جابه‌جایی از قدیمی‌ترین خطاهای کلاسِ زبانِ ایران است — اولین بارِ صدایش در تیمِ بین‌المللی خنده‌دارتر از خطرناک است؛ همان یک بار کافی است.'),
  ],
  'drills': (
   'منتورینگ، زبانِ سؤالِ هدایتگر است؛ چهار تمرین را بلند اجرا کن — انگار جونیور جلوی تو نشسته — بعد باز کن.',
   [
    'سه سؤالِ سقراطی پی‌درپی بپرس: تست‌ها رندوم fail می‌شوند — تا حالا چی امتحان کرده؟ خطا دقیقاً چه می‌گوید؟ الگوی «رندوم» چه شکلی است؟',
    'ستایشِ «This error handling is good» را سه‌لایه کن: اثر + قابلِ تکرار.',
    '«نمی‌دانم»ِ حرفه‌ای را بگو: چرا روت باید آن‌جا ثبت شود — نظریه دارم؛ با هم پیدا کنیم و بنویسیم؟',
    'سؤالِ مقدسِ سوم را به‌کار ببر و بعد سکوت کن: «اگر من نبودم چه می‌کردی؟»',
   ],
   [
    ('پاسخ تمرین ۱', 'نمونه: **"What have you tried so far? What does the error say, exactly? Does it fail every third run, or only on CI?"** سؤال‌های سقراطی، مسیرِ شکار را از خودِ جونیور بیرون می‌کشند؛ جوابِ آماده، جوابِ مرده است.'),
    ('پاسخ تمرین ۲', '**"This error handling is good — the retry logic saved the timeout case. Keep doing this."** سه لایه: چی، چه اثری، چه تکرار شود. This is good فقط نصفِ تعریف است.'),
    ('پاسخ تمرین ۳', '**"Honest answer: I don\'t fully know — I have a theory. Want to find out together and write it down? That\'s doc gold."** نمی‌دانم + نظریه + دعوت؛ جسارتِ ندانستن، منتور را صادق و جونیور را شجاع می‌کند.'),
    ('پاسخ تمرین ۴', '**"What would you do if I weren\'t here?"** — و بعد سکوت. سکوتِ منتور، فضای تصمیمِ جونیور است؛ پر کردنِ آن، دزدیِ رشد است.'),
   ],
  ),
  'challenge': 'امروز یک چیز را با سؤال یاد بده نه با جواب: به یک جونیور یا دوست، سه سؤالِ سقراطی بپرس، سکوت کن، و در آخر ستایشِ سه‌لایه بده.',
 },
 # ── درس ۷۱ ──────────────────────────────────────────────────────────────
 'english-conferences-networking': {
  'mistakes': [
   ('I know you from the conference.', 'Great meeting you at DevOpsConf — your backpressure talk stuck with me.', '«از کنفرانس یادت می‌آید» مستقیم know you from می‌شود؛ پیامِ بعدِ رویداد، سلامِ گرم + جزئیاتِ یادماندنی می‌خواهد. know you from سرد است و هویتِ گفتگو را گم می‌کند — جزئیات، شناسهٔ توست.'),
   ('Can you introduce me to a job?', 'Would you be comfortable referring me for the backend role?', '«برایِ کار معرفی‌ام کن» با introduce to a job مستقیم می‌شود؛ معرفیِ شغلی فعلِ خودش را دارد: refer — و با would you be comfortable پرسیده می‌شود. راحتیِ طرف، شرطِ ادبِ درخواستِ بزرگ است.'),
   ('I will send you the link, don\'t forget me.', "Here's the incident-review template I mentioned — coffee next time you're in the city, my treat!", '«یادت نره» وفاداریِ فارسی است اما در انگلیسی فشارِ بی‌اعتبار می‌سازد؛ زبانِ پیگیری: قول را در همان پیامِ اول اجرا کن (Here\'s…) و دعوتِ بعدی را با دعوتِ واقعی ببند — مهمانِ من یعنی my treat.'),
  ],
  'drills': (
   'شبکه‌سازی، زبانِ جزئیات و وعده‌های کوچکِ اجراشده است؛ چهار تمرین را اول خودت بنویس، بعد پاسخ‌ها را باز کن.',
   [
    'سؤالِ جزئیِ بعد از ارائه بساز: ارائهٔ backpressure — یک جزئیاتِ مشخص + یک سؤالِ عددی.',
    'پیامِ پیگیری را بنویس: DevOpsConf، داستانِ مهندسیِ آشوب، و قالبِ بازبینیِ حادثه که قولش را داده بودی.',
    'معرفی را مؤدبانه بخواه: نقشِ بک‌اند — با would you be comfortable.',
    'پیشنهادِ کمکِ طرف را مؤدبانه قبول کن: «ماهِ بعد استفاده کنم؟» — با take you up on.',
   ],
   [
    ('پاسخ تمرین ۱', 'نمونه: **"Your \'queue as shock absorber\' line clicked for me — at what scale did you flip from sync to async?"** جزئیاتِ مشخص + سؤالِ عددی؛ از صفِ «متشکرم» یک پله بالاتر و در حافظه.'),
    ('پاسخ تمرین ۲', '**"Hi Dara — great meeting you at DevOpsConf! Your chaos-engineering story stuck with me. As promised, here\'s the incident-review template."** سلامِ گرم + جزئیاتِ یادماندنی + قولِ اجراشده در همان پیامِ اول؛ سه لایه، یک خط.'),
    ('پاسخ تمرین ۳', '**"Would you be comfortable referring me for the backend role? Happy to send anything that makes it easy."** راحتیِ طرف اول، سبک‌کردنِ بار دوم؛ referring نه introducing — هر مفهوم فعلِ خودش را دارد.'),
    ('پاسخ تمرین ۴', '**"That\'s very kind — could I take you up on that next month?"** take you up on یعنی «از لطفت استفاده می‌کنم»؛ قبولِ مؤدبانه با تاریخ، پیشنهاد را زنده نگه می‌دارد.'),
   ],
  ),
  'challenge': 'امروز یک پیامِ پیگیریِ واقعی بفرست: جزئیاتِ مشخص از یک گفتگوی این هفته + یک قولِ کوچکِ همین‌جا-اجرا — قانونِ ۲۴ ساعتِ شبکه‌سازی است.',
 },
 # ── درس ۷۲ ──────────────────────────────────────────────────────────────
 'english-level4-review': {
  'mistakes': [
   ('This week I finished the spike, I pushed the fix, I am on the flaky test now and I will demo tomorrow.', "I finished the spike, I've pushed the fix, I'm on the flaky test today, and I'll demo tomorrow.", 'روایتِ هفته، چهار زمانِ جدا می‌خواهد: گذشتهٔ ساده برای دیروز، حالِ کامل برای اثرِ تازه (I\'ve pushed)، استمرار برای امروز، will برای فردا. فارسی زمان را با قید نشان می‌دهد و مغز هر چهار فعل را یک‌شکل رها می‌کند.'),
   ('For the record, my action item is to I will fix the flaky queue.', 'For the record, the action item is mine: fix the flaky queue by Friday.', 'بعد از to جملهٔ کاملِ با I will نمی‌آید؛ اقدامْ اسمِ مصدر می‌خواهد: fix the flaky queue. و دو نصفهٔ گمشدهٔ هر action item مالک و ددلاین است — mine + by Friday.'),
   ('Bottom line of my week is good, we did many works.', 'Bottom line: the retry spike is done, the fix is live, and the flaky queue is down from fourteen to five.', '«خلاصه اینکه خوب بود، کلی کار کردیم» جمع‌بندیِ مرده است؛ bottom line سه واقعیتِ شمرده می‌خواهد. و works جمع نمی‌شود — کارْ غیرقابل‌شمارش است: much work، نه many works.'),
  ],
  'drills': (
   'این جمع‌بندیِ فازِ ۴ است — یک روایتِ کاملِ اسپرینت؛ چهار تمرین را پشت‌سرهم و بلند اجرا کن، مثل گزارشِ جمعهٔ واقعی، بعد پاسخ‌ها را باز کن.',
   [
    'هفته را در چهار جمله روایت کن: اسپایک (گذشته)، پیاده‌سازی (حالِ کامل)، تستِ بی‌ثبات (امروز)، دمو (فردا) — چهار زمان، چهار جمله.',
    'گزارشِ استندآپ را بده: دیروز با سارا روی باگِ قیمت پِر شدیم و درستش کردم؛ امروز بیشتر روی تست‌های retry هستم؛ هنوز منتظرِ دسترسیِ staging هستم ولی بلاکم نکرده.',
    'دو برچسب را به‌کار ببر: یک کامنتِ ریلویو با Nit + یک اعلامِ وضعیت با at risk.',
    'رترو را با متریک ببند: یک چیز که جواب داد + یک پیشنهاد با مالک و عدد.',
   ],
   [
    ('پاسخ تمرین ۱', 'نمونه: **"I finished the retry spike on Monday, I\'ve pushed the implementation, I\'m on the flaky test today, and I\'ll demo tomorrow."** چهار زمانِ زنده در چهار جمله؛ همین روایت، امتحانِ فازِ ۴ بود.'),
    ('پاسخ تمرین ۲', '**"Yesterday I paired with Sara on the pricing bug and we fixed it. Today I\'m mostly on the retry tests. Still waiting on the staging credentials, but it\'s not blocking me yet."** گذشته، استمرار، بلوکرِ درجه‌بندی‌شده — سه جمله، ده ثانیه؛ روتِ هر صبحِ دنیای دِو.'),
    ('پاسخ تمرین ۳', 'نمونهٔ ریلویو: **"Nit: rename `data2` to `pricingSnapshot` — non-blocking."** نمونهٔ وضعیت: **"Heads-up: the migration is at risk — realistically one more day, maybe two."** برچسب‌ها زبانِ مشترکِ فازِ ۴؛ Nit و at risk را از امروز در جمله‌هایت بگذار.'),
    ('پاسخ تمرین ۴', 'نمونه: **"Worked: the pairing on the retry — fastest fix I\'ve shipped here. Improve: the flaky-test queue — proposal: one fix-sprint, one owner, from fourteen open to under five."** رترویِ اقدام‌محور: پیشنهاد + مالک + متریک؛ با همین جمله‌ها به فازِ ۵ پرواز کن!'),
   ],
  ),
  'challenge': 'یک گزارشِ جمعهٔ واقعی بنویس و بلند بخوان: bottom line در سه عدد، for the record با یک ریسک، و action item با مالک و ددلاین — نمای کاملِ فازِ ۴ در یک پیام؛ اگر کارِ واقعی نداری، همین هفتهٔ تمرینی‌ات را روایت کن.',
 },
}

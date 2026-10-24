# -*- coding: utf-8 -*-
"""Stages 2+3 · lessons 55-72 — گفتگو + گرامرِ عمیق + نکات مکالمه."""

EXPANSIONS = {
 'english-daily-standup': {
  'grammar': ('گرامرِ عمیق‌تر: زمانِ استندآپ — سه‌گانه‌ی دقیق', [
    ('p', 'استندآپ، تمرینِ «انتخابِ زمان» است: دیروز با **Past Simple** (I finished, we shipped), امروز با **Present Continuous** برایِ در-جریان (I\'m working on) یا **going to/will** برایِ برنامه (I\'ll start), و بلوکر با **حالِ سادهٔ توصیفی** (I\'m blocked on — استمراریِ وضعیت). دو قیدِ طلایی: **mostly** (بیشتر: «Mostly meetings, to be honest») و **still** (هنوز: «I\'m still waiting on access»). و جملهٔ تحویل: **"That\'s me — over to you."** (این از من — با تو).'),
    ('ex', 'Yesterday I paired with Sara on the pricing bug and we fixed it. Today I\'m mostly on the retry tests. Still waiting on the staging credentials, but it\'s not blocking me yet.', 'دیروز با سارا روی باگِ قیمت پِر شدیم و درستش کردیم. امروز بیشتر روی تست‌های retry هستم. هنوز منتظرِ اعتبارنامه‌های staging هستم، ولی فعلاً بلاکم نکرده.'),
  ]),
  'extra_sections': [
    {'h2': 'گفتگو: استندآپی که بحثش کش آمد', 'blocks': [
      ('ex', 'You: …and I\'m seeing random timeouts in the CI. — Lead: That\'s the third time this week — is it the runner or the code?', 'تو: …و توی CI تایم‌اوت‌های اتفاقی می‌بینم. — لید: سومین بار این هفته‌ست — از رانِرئه یا کد؟'),
      ('ex', 'You: Not sure yet — I\'ll dig in after standup. — Lead: Sounds like it needs its own thread. Let\'s take it offline — you, me, Dara.', 'تو: مطمئن نیستم — بعد از استندآپ می‌کنم. — لید: به نظر می‌رسه threadِ خودش رو می‌خواد. آفلاین ببریمش — من، تو، دارا.'),
      ('ex', 'You: Agreed. So: today, retry tests plus the CI mystery — I\'ll report by EOD. That\'s me. — Lead: Thanks — over to Dara.', 'تو: اوکی. پس: امروز، تست‌های retry به‌علاوهٔ معمای CI — تا آخرِ روز گزارش می‌دم. این از من. — لید: ممنون — با دارا.'),
    ]}],
  'tips': [
   ('That\'s me — over to you', 'جملهٔ تحویلِ ۲ثانیه‌ای؛ استندآپ را بی‌سکوتِ خطرناک نگه می‌دارد.'),
   ('بلوکر را با درجه بگو', 'blocked (کاملاً متوقف) / slowing me down (کند) / waiting on (منتظر) — سه درجه، سه واکنشِ متفاوت از تیم.'),
   ('فعلِ yesterday را اول بگذار', '«Yesterday: shipped X. Today: Y.» — آغازِ برچسب‌دار، تمرکزِ شنونده را در سه ثانیه قفل می‌کند.'),
  ]},
 'english-code-review': {
  'grammar': ('گرامرِ عمیق‌تر: مودالِ ریلویو — should و could و نرمیِ شرطی', [
    ('p', 'ریلویو، زبانِ **مودال‌های مشورتی** است: **should** (پیشنهادِ قوی: this should be async), **could** (گزینه: we could extract a helper), **might** (احتمال: this might break on empty input) — و نرم‌ترینِ همه، **شرطیِ دوم**: **If this were a public API, I\'d rename it** (اگر API عمومی بود، اسمش رو عوض می‌کردم) — were/\'d، فرمِ مؤدبانهٔ نقدِ فرضی! و برای درجه‌گذاریِ نظری به لحنِ نوشتاری: **Blocking:** (بلاک‌کننده), **Nit:** (جزئی), **Question:** (سوال) — سه برچسبِ اولِ کامنت، ریلویو را از گفتگو به سندِ تصمیم می‌برد.'),
    ('ex', 'Question: do we need this loop at all? If it were just a lookup, a hash map would do the job in one pass — happy to be wrong here!', 'سوال: اصلاً به این حلقه نیاز داریم؟ اگه فقط جستجو بود، یه هش‌مپ توی یه پاس کافیه — خوشحال می‌شم اشتباه کرده باشم!'),
  ]),
  'extra_sections': [
    {'h2': 'گفتگو: بحثِ ریلویو در thread و جمع‌بندی', 'blocks': [
      ('ex', 'Reviewer: Blocking — this swallows the error, and we just got burned by that in payments. — You: Fair. I\'ll log and rethrow. — Reviewer: That\'s all I wanted.', 'ریلویوئر: بلاک — این خطا رو قورت می‌ده، و تازه تو پرداخت از همین سوخته بودیم. — تو: درسته. لاگ می‌کنم و دوباره می‌اندازمش. — ریلویوئر: همین می‌خواستم.'),
      ('ex', 'Reviewer: Nit: this name, `data2`… future-us will suffer. — You: Ha! Renamed to `pricingSnapshot`. — Reviewer: LGTM with that one nit.', 'ریلویوئر: جزئی — این اسم، data2… خودِ آیندهٔ ما زجر می‌کشه. — تو: ها! به pricingSnapshot تغییرش دادم. — ریلویوئر: LGTM با همین جزئی.'),
      ('ex', 'You: Pushed — PTAL. And thanks for the burn-mark story, honestly — context like that is why I\'d rather have reviews than ship blind. — Reviewer: Same. That\'s the whole job.', 'تو: پوش شد — یه نگاه دیگه. و ممنون از داستانِ سوختگی — زمینه‌ی این‌جوری دلیلِ ترجیحِ ریلویو به شِپِ کوره. — ریلویوئر: منم. کلِ کار همینه.'),
    ]}],
  'tips': [
   ('Happy to be wrong', 'پایانِ کامنتِ نظر-محور: «happy to be wrong here» — علامتِ آگاهیِ تیمی؛ نظر می‌دهی، جنگ نمی‌کنی.'),
   ('پاسخِ بلند ننویس', 'پاسخِ کامنت: یک-دو خط یا یک commit. بحثِ طولانی در thread = جلسهٔ پنهان — بردارش به تماس.'),
   ('رایِ نهایی را با برچسب بده', 'پایانِ ریلویو: «LGTM» یا «LGTM with nits» — ابهامِ «خوبه ولی…»، مرج را معلق می‌کند.'),
  ]},
 'english-debugging-talk': {
  'grammar': ('گرامرِ عمیق‌تر: زبانِ حدس و حذف — might و must و رِجاکسیسم', [
    ('p', 'دیباگ، گرامرِ **احتمال** دارد: **might** (شاید — احتمالِ ضعیف), **could** (ممکن است — امکان), **must** (حتماً — استنتاجِ قوی: «The user must have double-clicked» — حتماً دوبار کلیک کرده), **can\'t** (نمی‌تواند باشد — استنتاجِ منفی: «It can\'t be the DNS — localhost fails too»). برای حذف: **I\'ve ruled out X** (X رو حذف کردم), **That leaves Y** (پس فقط Y می‌مونه), **It works until it doesn\'t** (کار می‌کنه تا لحظه‌ای که نمی‌کنه — جملهٔ مقدسِ intermittentها!). و نتیجه: **It turned out to be X** (معلوم شد X بود).'),
    ('ex', 'It can\'t be the network — localhost fails too. It must be the pool size under load. I\'ve ruled out the query itself; that leaves the connection config. Let me test with a bigger pool.', 'نمی‌تونه شبکه باشه — لوکال هم می‌خوابه. حتماً سایزِ پول زیرِ باره. خودِ کوئری رو حذف کردم؛ پس فقط کانفیگِ اتصال می‌مونه. با پولِ بزرگ‌تر تست می‌کنم.'),
  ]),
  'extra_sections': [
    {'h2': 'گفتگو: جفت‌شکارِ سی‌دقیقه‌ای', 'blocks': [
      ('ex', 'You: Got 30 minutes to pair? The payments retry is haunted — works in staging, dies in prod. — Colleague: Haunted, my favorite kind. Show me the logs.', 'تو: ۳۰ دقیقه وقت داری پِر شیم؟ retryِ پرداخت جن‌زده‌ست — تو staging کار می‌کنه، تو prod می‌میره. — همکار: جن‌زده، نوعِ موردعلاقه‌ام. لاگ‌ها رو نشونم بده.'),
      ('ex', 'Colleague: See this gap? Two retries, same millisecond. — You: Oh. It\'s a race — both fire before the first one finishes. — Colleague: There it is.', 'همکار: این فاصله رو می‌بینی؟ دو retry، همون میلی‌ثانیه. — تو: او. یه رِیسه — هر دو شلیک می‌شن قبل از اینکه اولی تموم شه. — همکار: پیداش کردیم.'),
      ('ex', 'You: I\'ll add an idempotency key so the second one becomes a no-op. Regression test too. — Colleague: And I\'ll write the runbook entry — "millisecond retries" — so the next haunted case dies faster.', 'تو: کلیدِ idempotency اضافه می‌کنم که دومی بی‌اثر شه. تستِ رگرسیون هم. — همکار: و من ران‌بوکش رو می‌نویسم — «retryهای میلی‌ثانیه‌ای» — تا جنِ بعدی زودتر بمیره.'),
    ]}],
  'tips': [
   ('can\'t → must → leaves', 'زنجیرهٔ استنتاج را بلند بگو: «نمی‌تونه X باشه… حتماً Yئه… پس فقط Z می‌مونه» — شنونده، مسیرِ فکرت را می‌خرد نه فقط جواب را.'),
   ('Can\'t reproduce را با جزئیات بگو', '«Can\'t reproduce locally — works with 100 users, fails at 10k» — همین یک قید، نصفِ تیم را به سمتِ درستِ مشکل می‌فرستد.'),
   ('It turned out to be را ثبت کن', 'پایانِ هر شکار را در تیکت بنویس: «Turned out to be a race between X and Y» — دانشِ پیدا‌شده، فقط وقتی ماندگار است که نوشته شود.'),
  ]},
 'english-agile-scrum': {
  'grammar': ('گرامرِ عمیق‌تر: رجیسترِ تخمین و پرسشِ planning', [
    ('p', 'پلنینگ، زبانِ **پرسشِ کارشکن** است: **How big is this, ballpark?** (بالایِ سرِ‌حرفِ چند؟), **What\'s the riskiest part?** (پرریسک‌ترینش کجاست؟), **What\'s our confidence — gut or data?** (اطمینانمون چقدره — حدسه یا داده؟). برای تخمینِ جمعی: **Let\'s play planning poker** (پوکرِ پلنینگ بازی کنیم) و اختلاف: **"We\'re a 3 and an 8 apart — let\'s talk for two minutes."** و پذیرشِ استوری: **"Definition of done — tests, docs, deployed to staging"** — جملهٔ پذیرش، قراردادِ ریزِ هر اسپرینت است.'),
    ('ex', 'This story looks small, but the riskiest part is the vendor\'s undocumented API. I\'d rather spike it for a day than commit to points we can\'t defend.', 'این استوری کوچیک به نظر می‌رسه، ولی پرریسک‌ترینش API بی‌داکِ فروشنده‌ست. ترجیح می‌دم یه روز اسپایکش کنم تا اینکه امتیازی بدم که قابلِ دفاع نیست.'),
  ]),
  'extra_sections': [
    {'h2': 'گفتگو: پلنینگ و سوالِ اسکوپ', 'blocks': [
      ('ex', 'PM: Can we fit the export feature this sprint? — You: Ballpark, five points on its own. Adding it means dropping the bugfix batch — which one wins?', 'PM: فیچرِ خروجی رو می‌شه این اسپرینت جا داد؟ — تو: حدوداً پنج امتیازِ تنها. اضافه‌کردنش یعنی حذفِ دستهٔ فیکس‌ها — کدوم ببره؟'),
      ('ex', 'PM: Bugs first — the support queue is on fire. — You: Agreed. So export moves to next sprint, and I\'ll write the story today so it\'s ready.', 'PM: اول باگ‌ها — صفِ پشتیبانی آتیشه. — تو: موافقم. پس خروجی می‌ره اسپرینتِ بعد، و امروز استوری‌ش رو می‌نویسم که آماده باشه.'),
      ('ex', 'Lead: Good call. Anything risky in the bug batch? — You: One — the SSO timeout. I\'ll timebox it to a day; if it eats more, we re-plan Wednesday.', 'لید: تصمیمِ خوبی بود. توی دستهٔ باگ‌ها چیز پرریسکی هست؟ — تو: یه دونه — تایم‌اوتِ SSO. یه روز سقفش می‌ذارم؛ اگه بیشتر خورد، چهارشنبه بازپلنینگ می‌کنیم.'),
    ]}],
  'tips': [
   ('سوالِ کدوم-بَرَد', 'هر «اضافه» را با «کدوم برنده باشه؟» جواب بده — این سوال، تو را از فنیِ منفعل به شریکِ تصمیم تبدیل می‌کند.'),
   ('رِیسک را با تایم‌باکس بپذیر', '«I\'ll timebox it to a day» — پذیرفتنِ ریسک با سقف، زبانِ بلوغِ پلنینگ است.'),
   ('استوریِ امروز برای اسپرینتِ فردا', 'استوری‌های نصفه‌کاره را همین امروز بنویس — پلنینگِ فردا، از استوریِ آماده شروع می‌شود نه از «یادم نیست».'),
  ]},
 'english-technical-writing': {
  'grammar': ('گرامرِ عمیق‌تر: زبانِ دستورالعمل — امریِ خنثی و مخاطبِ you', [
    ('p', 'داک، زبانِ **امریِ بی‌فاعلِ دوم‌شخص** است: **Run the script.** (اسکریپت را اجرا کن) · **Do not edit this file directly.** (این فایل را مستقیم ویرایش نکن) — بدونِ «you should» و بدونِ لطفِ اضافی. برای هشدار: **WARNING:** / **NOTE:** / **TIP:** — سه برچسبِ استاندارد. و برای گام‌ها: **First… Next… Finally** یا شماره. جملهٔ کوتاهِ داک زیرِ ۲۰ کلمه؛ مخاطبِ داک همیشه **you** — حتی اگر داک را «ما» نوشته باشند، خواننده «you» است. برای چیزهای اختیاری: **Optionally, you can…** — برچسبِ درست، همیشه مؤدب‌تر از حذف‌کردن است.'),
    ('ex', '## Setup\n1. Clone the repo and copy `.env.example` to `.env`.\n2. Run `docker compose up`.\n3. Open `localhost:3000` — you should see the demo dashboard.\n\nNOTE: the seed data is fake by design. Do not use real customer info locally.', 'راه‌اندازی — … نکته: داده‌های اولیه عمداً فیک‌اند. اطلاعاتِ واقعیِ مشتری را لوکال استفاده نکنید.'),
  ]),
  'extra_sections': [
    {'h2': 'گفتگو: رترویِ داک — «داکِ ما چه احساسی دارد؟»', 'blocks': [
      ('ex', 'Lead: Retro item: our onboarding docs. New people keep asking the same five questions. — You: Because the answers live in five different places. I counted.', 'لید: بندِ رترو: داک‌های onboarding ما. آدم‌های جدید همون پنج سوال رو می‌پرسن. — تو: چون جواب‌ها تو پنج جای مختلفه. شمردم.'),
      ('ex', 'Lead: Proposal? — You: One page, five answers, one owner — me, this sprint. "New joiner FAQ" with links to the deep docs.', 'لید: پیشنهاد؟ — تو: یه صفحه، پنج جواب، یه مالک — من، همین اسپرینت. «سوالاتِ پرتکرارِ تازه‌وارد» با لینک به داک‌های عمیق.'),
      ('ex', 'Lead: Love it — small, owned, done. — You: And the experiment: we track the five questions for two weeks. If they stop, the doc worked; if they move, the doc learns.', 'لید: عالیه — کوچیک، مالک‌دار، تمام‌شده. — تو: و آزمایش: دو هفته همون پنج سوال رو رصد می‌کنیم. اگه قطع شدن، داک جواب داد؛ اگه جابه‌جا شدن، داک یاد می‌گیره.'),
    ]}],
  'tips': [
   ('داک را با سوال بساز', 'هر بندِ داک، جوابِ یک سوالِ واقعی است — سوال‌های تکراریِ تیم، فهرستِ فصل‌های داکِ بعدی‌ات‌اند.'),
   ('یک صفحه، یک مالک، یک تاریخ', 'داکِ بی‌مالک، مردهٔ متولد‌نشده است؛ اسمِ مالک و تاریخِ آخرین بازبینی بالای هر صفحه.'),
   ('امریِ خنثی بنویس', '«Run…» به‌جایِ «You should probably run…» — کوتاهیِ داک، احترام به وقتِ خواننده است نه خشکی.'),
  ]},
 'english-slack-communication': {
  'grammar': ('گرامرِ عمیق‌تر: کوتاه‌سازی‌ها و لحنِ مودبانهٔ چت', [
    ('p', 'چت، گرامرِ فشرده دارد: **gonna** (going to), **wanna** (want to), **gimme** (give me — خیلی خودمانی!), **dunno** (don\'t know), **tbh** (to be honest — راستش), **imo** (in my opinion), **nvm** (never mind — بی‌خیال), **fyi** (برایِ اطلاع), **ttyl** (talk to you later). لحنِ درخواست در چت با **pls** (please) اما نه در هر جمله — please در هر پیام، لحن را مصنوعی می‌کند؛ نرم‌کننده‌ی چت واقعی، ساختار است: «when you get a sec»، «no rush». و ایموجیِ لحن‌ساز: 🙏 (ممنونم), 😅 (احساسِ «اوه»), 👀 (دیدم، دنبال می‌کنم).'),
    ('ex', 'fyi the staging deploy is done ✅ tests green. gonna start the load test now — no rush on the review, by EOD is fine 🙏', 'برایِ اطلاع: دپلوی staging تموم شد، تست‌ها سبز. الان تستِ بار رو شروع می‌کنم — ریلویو عجله‌ای نداره، تا آخرِ روز کافیه.'),
  ]),
  'extra_sections': [
    {'h2': 'گفتگو: bump و false alarm در کانال', 'blocks': [
      ('ex', 'You: @sara just bumping the PR from yesterday — it\'s holding the migration ticket. No rush on comments, an LGTM unblocks us!', 'تو: سارا، فقط بالا میارم PR دیروز رو — تیکتِ مایگریشن منتظرشه. کامنت فوریتی نیست، یه LGTM آزادمون می‌کنه!'),
      ('ex', 'Sara: On it in 10 — standup ran long, sorry! — You: No worries at all — thanks!', 'سارا: تا ۱۰ دقیقه روشم — استندآپ طول کشید، ببخشید! — تو: هیچی، ممنون!'),
      ('ex', 'You: Update: false alarm on the cache bug — it was my local clock 🙈 PR closed, ticket resolved. Thanks everyone for the eyes!', 'تو: آپدیت: زنگِ خطرِ باگِ کش بی‌دلیل بود — ساعتِ لوکالِ خودم بود 🙈 PR بسته شد، تیکت حل شد. ممنون از چشم‌های همگی!'),
    ]}],
  'tips': [
   ('Hi محض ممنوع', 'سلام + سوال در یک پیام: «Hey Sara — quick one: is staging up?» — سلامِ تنها + سکوت، نامهٔ ناتمام است.'),
   ('bump با دلیل', 'هر bump با یک قید: «holding the migration» یا «demo is tomorrow» — bumpِ بی‌دلیل، زنگِ بی‌اعتبار می‌سازد.'),
   ('false alarm را جشن بگیر', '«False alarm — solved it, thanks though!» — حلِ خودجوش را اعلام کن؛ سکوتِ بعدِ حل، نصفِ وقتِ کمک‌کنندگان را هدر می‌دهد.'),
  ]},
 'english-interview-coding': {
  'grammar': ('گرامرِ عمیق‌تر: زبانِ پیچیدگی و زمانِ مصاحبه', [
    ('p', 'مصاحبهٔ کدنویسی، جمله‌های ثابتِ فنی دارد: **"This runs in O(n) time and O(1) space."** (این با زمانِ O(n) و فضای O(1) اجرا می‌شه) — دو بعدِ پیچیدگی را همیشه با هم بگو. **"I can trade memory for speed"** (می‌تونم حافظه رو با سرعت عوض کنم) — قالبِ بهبود. **"The naive approach is O(n²); I can do better with a hash map."** و برای تست: **"Let me trace through an example"** (بذار با یه مثال ردیابی کنم) — ردیابیِ بلند، امتیازِ تستِ ذهنی است. و سوالِ شفاف‌سازِ ابدی: **"Can the input be empty?" / "Are duplicates possible?"**'),
    ('ex', 'The brute force is O(n²) — two nested loops. I can trade memory for speed: one pass with a hash map gives O(n) time at O(n) space. Given n up to a million, that trade pays for itself.', 'راهِ بی‌رحمانه O(n²)ئه — دو حلقهٔ تو در تو. می‌تونم حافظه رو با سرعت معاوضه کنم: یه پاس با هش‌مپ، زمانِ O(n) با فضای O(n). با n تا یک میلیون، این معامله خودش رو می‌کنه.'),
  ]),
  'extra_sections': [
    {'h2': 'گفتگو: چهار دقیقهٔ اوجِ مصاحبهٔ کدنویسی', 'blocks': [
      ('ex', 'Interviewer: Find the first unique character in a string. — You: Quick clarifications — empty string? Case-sensitive? Unicode?', 'مصاحبه‌گر: اولین کاراکترِ یکتا در رشته. — تو: دو سه تا شفاف‌سازی — رشتهٔ خالی؟ حساس به حروفِ بزرگ/کوچک؟ یونیکد؟'),
      ('ex', 'Interviewer: Non-empty, case-sensitive, ASCII. — You: So my plan: one pass to count, one pass to find — O(n) twice, O(1) space since the alphabet is fixed. Writing it now.', 'مصاحبه‌گر: غیرخالی، حساس، ASCII. — تو: پس نقشه‌م: یه پاس شمارش، یه پاس پیدا کردن — دوبار O(n)، فضای O(1) چون الفبا ثابته. می‌نویسمش.'),
      ('ex', 'You: Let me trace: "swiss" — counts are s:3, w:1, i:1. Second pass finds w. Edge case: all repeated — return -1. That\'s the contract.', 'تو: ردیابی کنم: «swiss» — شمارش‌ها s:3, w:1, i:1. پاسِ دوم w رو پیدا می‌کنه. حالتِ لبه: همه تکراری — -۱ برمی‌گردونیم. قرارداد همینه.'),
      ('ex', 'Interviewer: Solid. What if the string is a stream — can\'t hold it? — You: Then a second pass is impossible — I\'d need a different structure… honestly, this smells like a bounded queue problem. Can I think out loud?', 'مصاحبه‌گر: محکم. اگه رشته استِرِم باشه — نگهش نداشتیم؟ — تو: اون‌وقت پاسِ دوم غیرممکنه — ساختارِ متفاوتی لازمه… راستش بوی مسئلهٔ صفِ محدود می‌ده. می‌شه بلند فکر کنم؟'),
    ]}],
  'tips': [
   ('شفاف‌سازی = امتیاز', 'سه-چهار سوالِ آغازین، امتیازِ مستقلِ مصاحبه است — سکوتِ شروعِ فوری، نمرهٔ communication را می‌سوزاند.'),
   ('Blind blind را بلند بگو', '«Let me trace through an example» — ردیابیِ بلند، هم تست است هم نشانهٔ ذهنِ منظم؛ سکوتِ ایده‌آل، سکوتِ فکر شمرده می‌شود نه ابهام.'),
   ('گیر کردی؟ مثل حرفه‌ای بگیر', '«Let me step back and rethink the approach» یا «Can I get a hint? I\'d rather ask than stall» — درخواستِ hint با این صراحت، امتیاز است.'),
  ]},
 'english-interview-system-design': {
  'grammar': ('گرامرِ عمیق‌تر: زبانِ trade-off و مقیاس', [
    ('p', 'طراحیِ سیستم، زبانِ **بسته به** و **سپردن** است: **It depends on the read/write ratio** (به نسبتِ خواندن/نوشتن بستگی داره), **I\'d shard by user ID** (شناسهٔ کاربر شارد می‌کنم), **We accept eventual consistency for availability** (برای دسترس‌پذیری، سازگاریِ نهایی رو قبول می‌کنیم). اعدادِ مقیاس: **QPS** (queries per second), **p99 latency** (تأخیرِ ۹۹ درصدی), **read-heavy / write-heavy** (خوانا-محور/نوشتا-محور). و فعل‌های محبوب: **scale horizontally** (افقی مقیاس کن — ماشینِ بیشتر), **cache aggressively** (جسورانه کش کن), **degrade gracefully** (افتِ مؤدبانه — وقتی قطعه‌ای خوابد، کل نمی‌خوابد).'),
    ('ex', 'The system is read-heavy — roughly 100 reads per write — so I\'d cache aggressively and accept eventual consistency on the counters. If p99 spikes, we degrade gracefully: show cached counts with a "cached" badge.', 'سیستم خوانا-محوره — تقریباً صد خواندن به هر نوشتن — پس جسورانه کش می‌کنم و سازگاریِ نهاییِ شمارنده‌ها رو می‌پذیرم. اگه p99 پرید، افتِ مؤدبانه می‌کنیم: شمارشِ کش‌شده با نشانِ «کش» رو نمایش می‌دیم.'),
  ]),
  'extra_sections': [
    {'h2': 'گفتگو: پنج دقیقه از میانِ طراحیِ news feed', 'blocks': [
      ('ex', 'Interviewer: Design a news feed for 10 million users. — You: First, shape: read-heavy? The scrolling is reads; posting is writes — I\'d guess 100:1. Confirmable?', 'مصاحبه‌گر: یه فید برایِ ۱۰ میلیون کاربر طراحی کن. — تو: اول شکل: خوانا-محوره؟ اسکرول خواندنه، پست‌گذاشتن نوشتن — حدسم ۱۰۰:۱. تأیید می‌شه؟'),
      ('ex', 'Interviewer: Close enough — say 50:1. — You: Then the feed is a materialized list per user, updated async. The hot path is only reads from cache — Redis in front of the store.', 'مصاحبه‌گر: نزدیک — مثلاً ۵۰:۱. — تو: پس فید یه لیستِ از پیش‌ساخته برای هر کاربره که async آپدیت می‌شه. مسیرِ داغ فقط خواندن از کشه — ردیس جلوی ذخیره.'),
      ('ex', 'You: The interesting trade-off is fan-out: push on write is fast to read but expensive for celebrities. Hybrid: push for normal users, pull for the famous ones. — Interviewer: That\'s the answer I was fishing for. — You: Ha! I\'ve been burned by a celebrity\'s fan-out before — never again.', 'تو: trade-offِ جالب fan-oute: push رویِ نوشتن، سریع‌تر برایِ خواندن ولی برای سلبریتی‌ها گرونه. هیبرید: push برای کاربرهای عادی، pull برای معروف‌ها. — مصاحبه‌گر: همون جوابیه که دنبالش بودم. — تو: ها! یه بار فن‌اوتِ یه سلبریتی من رو سوخته — دیگه هرگز.'),
    ]}],
  'tips': [
   ('عددِ اول را خودت بگو', 'قبل از طراحی، اعداد را بلند حساب کن (QPS, ratio) — «صد میلیون در روز یعنی هزار در ثانیه» — عددِ شمرده، درهای مصاحبه را باز می‌کند.'),
   ('It depends را با دو گزینه ببند', 'هر «بستگی داره» را با «گزینهٔ A برای حالتِ X، B برای Y» کامل کن — dependsِ بدونِ گزینه، دوری است نه تحلیل.'),
   ('تجربهٔ سوخته را داستان کن', '«I\'ve been burned by X before» — سوختگیِ واقعی + درسش، محک‌ترین اعتبارِ طراحیِ توست.'),
  ]},
 'english-behavioral-interview': {
  'grammar': ('گرامرِ عمیق‌تر: زمانِ STAR و نقلِ گفتگو', [
    ('p', 'STAR در انگلیسی، زمانِ منظم دارد: **S/T با گذشته** (We were mid-launch when…), **A با گذشتهٔ اول‌شخص** (I isolated, I proposed — «I» در داستانِ رفتاری آزاد است، برخلافِ رزومه!), **R با گذشته + اثرِ ماندگار** (We shipped on time — and the checklist we wrote is still in use). برای نقلِ دیالوگ در داستان: «He said we should delay. I said: give me one day.» — said ساده، نقلِ مستقیم کوتاه؛ گفتگو در داستانِ رفتاری، جانِ قالب است. و جملهٔ ضعفِ در-درمان: **«I used to X; now I consciously Y.»** (قبلاً X؛ حالا آگاهانه Y.)'),
    ('ex', 'Honestly, I used to over-commit — I\'d say yes to everything and pay for it at night. Now I consciously say: "If I take this, what moves out?" — and I say it out loud in planning. It made my estimates boring — and my weekends real.', 'راستش قبلاً بیش‌ازحد قول می‌دادم — به همه بله می‌گفتم و شب‌ها جریمه‌اش رو می‌دادم. حالا آگاهانه می‌گم: «اگه این رو بگیرم، چی بیرون می‌ره؟» — و بلند می‌گمش تو پلنینگ. تخمین‌هام رو خسته‌کننده کرد — و آخرِ هفته‌هام رو واقعی.'),
  ]),
  'extra_sections': [
    {'h2': 'گفتگو: سوالِ سختِ آخرِ مصاحبه', 'blocks': [
      ('ex', 'Interviewer: Tell me about a time you failed — a real one. — You: Real one: I shipped a config change on a Friday afternoon, without the canary. It took payments down for forty minutes.', 'مصاحبه‌گر: از یه شکستِ واقعی بگو — یه شکستِ راست. — تو: شکستِ راست: یه تغییرِ کانفیگ رو جمعه بعدازظهر شِپ کردم، بدونِ کانری. پرداخت رو چهل دقیقه انداخت.'),
      ('ex', 'You: I owned it in the incident channel, wrote the postmortem myself, and pushed for the canary rule to be a merge check — not a guideline, a check. — Interviewer: And the rule survived?', 'تو: تو کانالِ حادثه مالکش شدم، پست‌مورتم رو خودم نوشتم، و رفتم که قانونِ کانری بشه چکِ مرج — نه راهنما، چک. — مصاحبه‌گر: و قانون موند؟'),
      ('ex', 'You: It survived me, the next release, and two new hires. I still hate that Friday — but I\'m weirdly proud of the check. — Interviewer: That\'s the kind of failure we hire for.', 'تو: از من موند، از ریلیزِ بعد، و از دو تازه‌وارد. هنوز از اون جمعه متنفرم — ولی عجیب‌ِِ پرَوَدم به اون چک. — مصاحبه‌گر: شکستِ این‌جوری رو برایِ همین استخدام می‌کنیم.'),
    ]}],
  'tips': [
   ('شکست را با سیستم‌سازی ببند', 'شکستِ قصه = مالکیت + تغییرِ سیستمی (checklist, چکِ مرج) — شکستی که سیستم نسازد، در مصاحبهٔ سنیور، حرفه فقط نصف است.'),
   ('He said / I said', 'داستان را با نقل‌قول‌های دو‌خطی جان بده — گفتارِ زنده، امتیازِ جداگانهٔ communication دارد.'),
   ('سه داستان، نه سی', 'تعارض + شکست + ددلاین — سه داستانِ تمرین‌شدهٔ ۹۰ثانیه‌ای، پوششِ کاملِ رفتاری؛ بلند تمرین‌شان کن.'),
  ]},
 'english-demos-presentations': {
  'grammar': ('گرامرِ عمیق‌تر: امریِ دمو و زمانِ روایت', [
    ('p', 'دمو، زبانِ **امرِ خنثی + حالِ استمرار** است: **Watch what happens when I click here.** (ببین وقتی این‌جا کلیک می‌کنم چی می‌شه) · **Notice there\'s no page reload.** (دقت کن ری‌لود نداریم) · **I\'m now switching to the checkout screen.** (الان می‌رم صفحهٔ تسویه). برای انتظار vs واقعیت: **You\'d expect a spinner — instead, it\'s instant.** (انتظارِ لودینگ داری — به‌جاش آنیئه). و برای خرابی: **"And… that\'s a bug. Good catch by the demo gods."** — جملهٔ آمادهٔ لحظهٔ سکوت! نکتهٔ زمانی: دموی زنده با حالِ استمرار پیش می‌رود و نتیجه‌ها با گذشتهٔ تازه می‌آیند: **"It loaded in 300ms — under our target."**'),
    ('ex', 'Watch the top bar — that\'s where the status lives. I\'m adding three items now… and… done. You\'d expect a spinner there; instead, the total updated instantly.', 'به نوارِ بالا نگاه کن — وضعیت همون‌جاست. الان سه تا آیتم اضافه می‌کنم… و… تمام. اون‌جا انتظارِ لودینگ رو داری؛ به‌جاش جمعِ کل فوراً آپدیت شد.'),
  ]),
  'extra_sections': [
    {'h2': 'گفتگو: دمو، سوالِ زنده، و بستن', 'blocks': [
      ('ex', 'PM (mid-demo): Can it handle a hundred items? — You: Great question — parking it for after the demo so I don\'t lose the thread. Spoiler: yes, but there\'s a story.', 'PM (وسطِ دمو): با یه صد تا آیتم کنار میاد؟ — تو: سوالِ خوبیه — کنارش می‌ذارم برای بعد که رشته‌ام نره. اسپویل: آره، ولی داستان داره.'),
      ('ex', '(demo crashes) You: And… that\'s a bug. Good catch by the demo gods — this is exactly why we demo before shipping. Let me show you the fallback path.', '(دمو کرش) تو: و… این یه باگه. خدایانِ دمو خوب شکار کردن — دقیقاً برای همین قبلِ شِپ دمو می‌گیریم. بذار مسیرِ جایگزین رو نشونتون بدم.'),
      ('ex', 'You: So: two clicks, 300ms, error rate under 0.1% on staging. We\'re ready for the next 5% rollout — I\'d love your go/no-go in the review. — PM: Consider it given. Nice demo.', 'تو: پس: دو کلیک، ۳۰۰ میلی‌ثانیه، خطای زیرِ ۰/۱٪ تو staging. آمادهٔ بازکردنِ ۵٪ بعدی‌ایم — جوابِ بله/نه‌تون رو تو ریویو می‌خوام. — PM: بله رو بگیر. دموی قشنگی بود.'),
    ]}],
  'tips': [
   ('رشته را با park نگه‌دار', 'سوالِ وسطِ دمو: «parking it for after» + اسپویلِ یک‌کلمه‌ای — نه جوابِ بلند، نه بی‌احتراسی.'),
   ('خرابی را جشنِ فرایند کن', '«This is exactly why we demo» — جمله‌ای که کرش را از شکستِ تو به جویِ تیم تبدیل می‌کند.'),
   ('بستن = عدد + درخواست', 'دمو را با سه عدد و یک go/no-go ببند — دموی بی‌درخواست، تماشاست نه تصمیم.'),
  ]},
 'english-estimations-deadlines': {
  'grammar': ('گرامرِ عمیق‌تر: قالب‌های عددیِ تخمین', [
    ('p', 'تخمین، زبانِ **بازه و شرط** است: **two to three days** (دو تا سه روز), **a week, give or take** (یه هفته، مثلاً — give or take یعنی ±), **assuming X** (با فرضِ X), **unless X** (مگر اینکه X). برای ابهامِ صادقانه: **"I can\'t give you a real number blind — give me half a day."** و برای بازنگری: **"It\'s behaving like an eight, not a two."** (هشتایی رفتار می‌کنه، دوتایی نیست). و جفت‌های اعلام: **on track** (طبقِ برنامه), **at risk** (در خطر), **slipping** (می‌خوره عقب) — سه‌تایی که همهٔ وضعیت‌های sprint را پوشش می‌دهند.'),
    ('ex', 'Ballpark: three days, give or take a day — assuming the vendor sandbox behaves. If the sandbox is flaky, all bets are off and I\'ll flag it within a day.', 'حدوداً سه روز، مثلاً ± یک روز — با فرضِ اینکه سندباکسِ فروشنده آدم‌حرف باشه. اگه سندباکس بی‌ثبات بود، همه‌چیز قید می‌شه و ظرفِ یه روز خبر می‌دم.'),
  ]),
  'extra_sections': [
    {'h2': 'گفتگو: اعلامِ خطرِ زودهنگام', 'blocks': [
      ('ex', 'You: Heads-up — the migration is at risk. I\'m 60% through, but the legacy data is dirtier than we sampled. — PM: How dirty?', 'تو: خبر — مایگریشن در خطره. ۶۰٪ جلو اومدم، ولی دیتای قدیمی کثیف‌تر از نمونه‌ایه که دیدیم. — PM: چقدر کثیف؟'),
      ('ex', 'You: Think "duplicate IDs with different casing." Realistically one more day, maybe two. — PM: The demo is Friday. Options?', 'تو: چیزی مثل «شناسه‌های تکراری با حروفِ متفاوت». واقع‌بینانه یه روزِ دیگه، شاید دو. — PM: دمو جمعه‌ست. گزینه‌ها؟'),
      ('ex', 'You: Three: cut the historical import (demo works on fresh data), slip the demo to Monday, or I hero it overnight — which I don\'t recommend. My call is option one: the demo still lands, the import becomes its own ticket. — PM: Agreed — cut it. And thanks for flagging early, not Friday at five.', 'تو: سه تا: حذفِ ایمپورتِ تاریخی (دمو با دیتای تازه کار می‌کنه)، جابه‌جاییِ دمو به دوشنبه، یا من شب‌قهرمانش کنم — که توصیه نمی‌کنم. پیشنهادِ من اولیه: دمو میمونه، ایمپورت تیکتِ جدا می‌شه. — PM: موافقم — حذفش. و ممنون که زود خبر دادی، نه جمعه ساعتِ پنج.'),
    ]}],
  'tips': [
   ('سه‌گزینه بده، نه گلوله', 'هر خبرِ بد با سه گزینه و یک پیشنهاد — مدیر با گزینه حرف می‌زند؛ با فاجعه فقط فریاد.'),
   ('heads-up روزِ دوم، نه روزِ آخر', 'شاخصِ ۶۰٪/خطر را که دیدی اعلام کن — دیرتر گفتن، تمامِ گزینه‌ها را می‌کُشد.'),
   ('give or take و realistically', 'دو قید را در جمله‌های تخمین بکار — صداقتِ بازه، اعتمادِ عدد را می‌سازد.'),
  ]},
 'english-product-client-talks': {
  'grammar': ('گرامرِ عمیق‌تر: زبانِ نتیجه و ارزش برای غیرِفنی', [
    ('p', 'گفتگو با محصول/مشتری، ترجمهٔ **فعل→اثر** است: **slows down** (کند می‌شه), **risks losing users** (خطرِ ازدست‌دادنِ کاربر داره), **buys us speed later** (بعداً سرعت می‌خره), **invisible to users** (برای کاربر نامرئیه). و قالب‌های قیاسِ دو-گزینه‌ای برای تصمیمِ PM: **"Option A ships Friday but breaks for power users; Option B takes two weeks and works for everyone. Your call."** (گزینهٔ A جمعه می‌رسه ولی برای کاربرهای حرفه‌ای می‌شکنه؛ B دو هفته می‌بره و برای همه کار می‌کنه. انتخاب با شما.) — «Your call» با احترام، توپ را می‌گذارد کجاست: نزدیکِ مدیرِ محصول.'),
    ('ex', 'Quick reality check: this "tiny toggle" actually touches the database. Cheaper version: the setting only for new users — old users keep the current behavior. That ships this week and is invisible to 95% of users. Your call.', 'واقعیت‌چکِ سریع: این «سوییچِ کوچیک» واقعاً دیتابیس رو درگیر می‌کنه. نسخهٔ ارزون‌تر: تنظیمِ فقط برایِ کاربرهای جدید — قدیمی‌ها همین‌جوری بمونن. این هفته شِپ می‌شه و برایِ ۹۵٪ کاربر نامرئیه. انتخاب با شما.'),
  ]),
  'extra_sections': [
    {'h2': 'گفتگو: مشتری خسته و دموهای بی‌وقت', 'blocks': [
      ('ex', 'Client: Just make it work — I don\'t need the details. — You: Understood — one sentence, then I\'ll leave you alone: the fix goes live tonight, and if anything looks wrong tomorrow morning, you call me directly.', 'مشتری: فقط کار کنه — جزئیات نمی‌خوام. — تو: متوجه‌ام — یه جمله، بعد رهات می‌کنم: فیکس امشب لایو می‌شه، و اگه فردا صبح چیزی خراب بود، مستقیم به من زنگ بزنید.'),
      ('ex', 'Client: That\'s all I wanted to hear. — You: Perfect. I\'ll send a one-line confirmation email after the deploy — so you have it in writing.', 'مشتری: همین رو می‌خواستم بشنوم. — تو: عالیه. بعد از دپلوی یه ایمیلِ یک‌خطیِ تأیید می‌فرستم — که مکتوب داشته باشیدش.'),
      ('ex', 'PM (after): How did you calm him down? — You: He didn\'t need calm — he needed an owner. "You call me directly" does both.', 'PM (بعد): چطور آرومش کردی؟ — تو: آروم نمی‌خواست — مالک می‌خواست. «مستقیم به من زنگ بزنید» هر دو رو می‌کنه.'),
    ]}],
  'tips': [
   ('یک جمله برای بی‌حوصله‌ها', 'برای مشتریِ بی‌حوصله: یک جملهٔ «چه می‌شه + چه زمانی + اگر خراب شد چی» — و رها کن؛ مالکیت آرامش می‌فروشد.'),
   ('مکتوب‌کردنِ قولِ شفاهی', 'بعد از هر قولِ تلفنی: «I\'ll send a one-line confirmation» — سوءتفاهمِ مشتری، از همین یک خط بیمه می‌شود.'),
   ('Your call را با دو گزینه بیاور', 'تصمیم را که به PM می‌سپاری، دو گزینهٔ روشن بده — سپردنِ بی‌گزینه، فرار است؛ سپردنِ دوگزینه، همکاری.'),
  ]},
 'english-one-on-ones-feedback': {
  'grammar': ('گرامرِ عمیق‌تر: زبانِ بازخوردِ قابلِاجرا', [
    ('p', 'بازخوردِ خوب، فرمولِ «رفتار + اثر + درخواستِ مشخص» دارد: **When X happened, the team lost Y — could we Z?** برای مثالِ رفتاری: **"When the updates land after the fact, I can\'t plan around them."** (وقتی آپدیت‌ها بعداً می‌رسه، نمی‌تونم براش برنامه بچینم) — نقطهٔ «رفتار» نهِ «شخصیت». و جملاتِ حرفه‌ایِ گرفتن: **"What\'s the one thing I should keep doing?"** / **"What\'s the one thing to do differently?"** — دو سوالِ آینه که هر بازخوردی را قابلِاجرا می‌کنند: «keep» + «differently» = رشدِ دو-جهته.'),
    ('ex', 'Can I ask for something specific? In our 1:1s, when you give feedback, could we end with one concrete action? "Communicate more" is hard to act on — "post a Friday recap" is a plan I can run.', 'می‌تونم یه چیزِ مشخص بخوام؟ توی 1:1هامون، وقتی بازخورد می‌دید، می‌تونیم با یه اقدامِ مشخص تموم کنیم؟ «بیشتر خبر بده» عملی نیست — «جمعه‌ها یه جمع‌بندی بذار» یه برنامه‌ست که می‌تونم اجرا کنم.'),
  ]),
  'extra_sections': [
    {'h2': 'گفتگو: بازگوییِ بازخوردِ سخت و بستنِ حلقه', 'blocks': [
      ('ex', 'Manager: One thing I\'d flag: your updates go quiet when you\'re deep in a problem — then everything lands at once. — You: So the pattern is: silence, then a flood. Let me check I got that right?', 'مدیر: یه چیز رو پرچم می‌زنم: وقتی توی مسئله عمیق می‌شی، آپدیت‌هات ساکت می‌شن — بعد همه‌چیز یه‌جا میاد. — تو: پس الگو اینه: سکوت، بعد سیل. بذار مطمئن شم درست گرفتم؟'),
      ('ex', 'Manager: Exactly. — You: That\'s fair, and it\'s useful. Here\'s my fix: a two-line Friday recap, even mid-forest — "deep in X, next visible step Y." Does that close the gap?', 'مدیر: دقیقاً. — تو: منصفانه‌ست و به‌دردبخوره. راه‌حلم: جمعه‌ها دو خط جمع‌بندی، حتی وسطِ جنگل — «عمیق توی X، گامِ بعدیِ Y». شکاف رو می‌بنده؟'),
      ('ex', 'Manager: It does. — You: Then that\'s the experiment — four Fridays, then we check. Thanks for saying it straight, by the way — I\'d rather know early.', 'مدیر: می‌بنده. — تو: پس آزمایش همینه — چهار جمعه، بعد چک می‌کنیم. به‌هیچ‌حال ممنون که رک گفتی — ترجیح می‌دم زود بدونم.'),
    ]}],
  'tips': [
   ('بازگوییِ الگو، نه دفاع', 'جوابِ بازخوردِ سخت: خلاصه‌اش را با جملهٔ خودت بگو («So the pattern is…») — بازگویی، نصفِ اصلاح است.'),
   ('keep + differently', 'دو سوالِ هر 1:1: چه چیزی ادامه بدم + چه چیزی متفاوت — با «یکی» محدودش کن تا قابلِاجرا شود.'),
   ('آزمایش با تاریخِ چک', 'هر اصلاح را به‌صورتِ آزمایش با تاریخِ بازبینی ببند — بازخوردِ بی‌تاریخ، آرزوست.'),
  ]},
 'english-disagreeing-technically': {
  'grammar': ('گرامرِ عمیق‌تر: شرطیِ دوم برای مخالفتِ نرم', [
    ('p', 'نرم‌ترین مخالفتِ فنی، **شرطیِ دوم** است: **"If we were starting fresh, I\'d go with X — but given the migration, Y buys us more."** (اگر از صفر شروع می‌کردیم X را برمی‌داشتم — اما با این مایگریشن، Y بیشتر می‌خره.) ساختار: if + گذشته + would. برای چالشِ مستقیم: **"I\'m not convinced this handles the weekend traffic — can we look at the numbers before we commit?"** (مطمئن نیستم ترافیکِ آخرِ هفته رو هندل کنه — قبلِ تعهد به اعداد نگاه کنیم؟) و برای فسخِ محترمانهٔ تصمیم: **"Let\'s revisit in three months with real data."** — جمله‌ای که مخالفتِ امروز را به حقِ بازگشتِ فردا تبدیل می‌کند.'),
    ('ex', 'If this were a clean slate, I\'d pick the queue too — it\'s the textbook answer. But we\'re mid-migration with one ops engineer; the cron version is boring, and boring ships. Let\'s revisit the queue when the team doubles.', 'اگر کاغذِ سفید بود، من هم صف رو برمی‌داشتم — جوابِ کتابه. ولی وسطِ مایگریشنیم با یه اپس؛ نسخهٔ کرون خسته‌کننده‌ست، و چیزِ خسته‌کننده شِپ می‌شه. وقتی تیم دوبرابر شد، سراغِ صف برمی‌گردیم.'),
  ]),
  'extra_sections': [
    {'h2': 'گفتگو: مناظرهٔ پنج‌دقیقه‌ای و بستن', 'blocks': [
      ('ex', 'Lead: I still think the queue is worth the complexity. — You: And your point about replay is real — I\'m not dismissing it. My worry is ops load this quarter. What if we timebox the debate to today, you make the call, and we all commit?', 'لید: هنوز فکر می‌کنم صف ارزشِ پیچیدگیش رو داره. — تو: و نکته‌ات دربارهٔ replay واقعیه — ردش نمی‌کنم. نگرانیم بارِ اپسِ این فصله. اگه بحث رو تا امروز سقف کنیم، تصمیم با تو، و همه متعهد شیم؟'),
      ('ex', 'Lead: Deal. My call: cron now, queue in the roadmap. — You: Then that\'s the decision — and for the record, I\'ll write the trade-off into the ADR so future-us knows both paths.', 'لید: توافق. تصمیمم: کرون الان، صف توی رودمپ. — تو: پس تصمیم همین — و برایِ ثبت، trade-off رو تو ADR می‌نویسم که خودِ آینده‌مون هر دو مسیر رو بدونه.'),
      ('ex', 'Lead: Perfect — disagree, commit, document. — You: The holy trinity! See you at the demo — I\'ll make the cron sing.', 'لید: عالی — مخالفت، تعهد، مستندسازی. — تو: تثلیثِ مقدس! دمو می‌بینیمت — کرون رو می‌خونونم!'),
    ]}],
  'tips': [
   ('مخالفت را با «قاعده» بگو نه «سلیقه»', '«With one ops engineer» — دلیلِ مخالفتِ داده‌محور، تصمیم را از «چه کسی بلندتر» به «چه چیزی درست» می‌برد.'),
   ('سقفِ بحث را پیشنهاد بده', '«Timebox to today, your call, we commit» — پیشنهادِ فرایند، نشانهٔ senior‌ترین آدمِ اتاق است.'),
   ('ADR را خودت بنویس', 'پیشنهادِ «I\'ll write the ADR» — مستندکردنِ تصمیمِ جمع، صاحبش را هم بی‌تلاش باهوش‌تر نشان می‌دهد هم یادگارِ محترم.'),
  ]},
 'english-joining-new-team': {
  'grammar': ('گرامرِ عمیق‌تر: زبانِ «جاافتادن» و سطحِ اطلاعات', [
    ('p', 'ادغام، زبانِ **آگاهی از جهلِ موقت** است: **I\'m still building the map** (هنوز دارم نقشه رو می‌سازم), **I don\'t have the context yet** (هنوز زمینه ندارم), **Correct me if I\'m wrong, but…** (اگه اشتباه می‌کنم اصلاح کن، اما…). برای درخواستِ زمینه: **Could you walk me through why it\'s built this way?** (می‌شه بگی چرا این‌جوری ساخته شده؟) — سوالِ «چرا»، آینهٔ history است. و قاعدهٔ رجیستر: جمله‌های ادغامْ ساده و کوتاه — «Got it» / «That makes sense» / «One more question» — ادغام، جایِ بلاغت نیست؛ جایِ دقت است.'),
    ('ex', 'I don\'t have the context yet — is this a hard requirement or a legacy default? Correct me if I\'m wrong, but it feels like something we could revisit once the migration settles.', 'هنوز زمینه ندارم — این نیازمندیِ سختِه یا پیش‌فرضِ قدیمی؟ اگه اشتباه می‌کنم اصلاح کن، ولی چیزیه که وقتی مایگریشن جا افتاد می‌تونیم دوباره ببینیمش.'),
  ]),
  'extra_sections': [
    {'h2': 'گفتگو: ماهِ دوم — اولین برد و بازخوردِ مقدماتی', 'blocks': [
      ('ex', 'You: I picked up the docs cleanup ticket — I\'ve been taking notes since week one, so it\'s half done already. — Lead: That\'s the fastest doc we\'ve ever shipped!', 'تو: تیکتِ مرتب‌سازیِ داک‌ها رو گرفتم — از هفتهٔ اول یادداشت داشتم، پس از قبل نصفش آماده بود. — لید: سریع‌ترین داکیه که تا حالا شِپ کردیم!'),
      ('ex', 'Lead: Now the real question — how\'s the ramp-up feeling? — You: Good. The codebase map clicked this week. My open gap: the deploy pipeline — I\'ve watched it, never driven it.', 'لید: حالا سوالِ اصلی — جاافتادن چه حسی داره؟ — تو: خوب. نقشهٔ کدبیس این هفته جا افتاد. شکافِ بازِ من: پایپ‌لاینِ دپلوی — دیدمش، ولی هنوز خودم نراندهمش.'),
      ('ex', 'Lead: Then Friday\'s deploy is yours — I\'ll sit next to you. — You: Perfect. And one ask: after it, could I get five minutes of "first impression feedback"? Fresh eyes fade fast.', 'لید: پس دپلوی جمعه مالِ توئه — کنارت می‌شینم. — تو: عالیه. و یه درخواست: بعدش پنج دقیقه «بازخوردِ اولین برداشت» می‌گیرم؟ چشمِ تازه زود کم‌رنگ می‌شه.'),
    ]}],
  'tips': [
   ('بردِ اول را «نیمه‌آماده» بیاور', 'اولین برد را از کارتِ پیش‌ موجود بردار (داک، تستِ شکسته، اسکریپت) — بردِ زودهنگام، اعتبارِ صدایی می‌سازد.'),
   ('Fresh eyes fade fast', 'بازخوردِ «اولین برداشت» را در ماهِ اول بگیر — بعد از سه ماه، چشمِ تو هم عادت‌کرده و بی‌صدا می‌شود.'),
   ('Correct me if I\'m wrong', 'پیش‌قولِ هر حدسِ بزرگ در تیمِ تازه — هم احترام است هم بیمهٔ خطا.'),
  ]},
 'english-mentoring-juniors': {
  'grammar': ('گرامرِ عمیق‌تر: زبانِ سوالِ هدایتگر و feedbackِ رشد', [
    ('p', 'منتورینگ، زبانِ **سوالِ سقراطی** است: **What have you tried so far?** (تا حالا چی امتحان کردی؟) · **What does the error say, exactly?** (خطا دقیقاً چی می‌گه؟) · **What would you do if I weren\'t here?** (اگه من نبودم چیکار می‌کردی؟) و بازخوردِ رشد: **praise در سه‌لایه**: «This is good» (ضعیف) / «This error handling is good» (بهتر) / «The retry logic here saved the timeout case — keep doing this» (قابلِ تکرار!). قاعدهٔ نسبتِ طلایی: **two appreciations per improvement** — دو ستایشِ واقعی به هر نکتهٔ بهبود؛ ریلویوی تمام‌نقد، جونیور را ساکت می‌کند نه بهتر.'),
    ('ex', 'Before I jump in — walk me through what you\'ve tried. You said the tests fail randomly… what does "randomly" look like? Every third run? Only on CI? The answer shapes the whole hunt.', 'قبل از اینکه بیام وسط — بگو چی امتحان کردی. گفتی تست‌ها رندوم fail می‌شن… «رندوم» چه شکلیه؟ هر سومین اجرا؟ فقط توی CI؟ جواب، کلِ شکار رو شکل می‌ده.'),
  ]),
  'extra_sections': [
    {'h2': 'گفتگو: سُرخِ زاویه و جرئتِ «نمی‌دانم»', 'blocks': [
      ('ex', 'Junior: Why does the framework need the route registered there? — You: Honest answer: I don\'t fully know — I have a theory. Want to find out together and write it down? That\'s doc gold.', 'جونیور: چرا فریم‌ورک لازمه روت اون‌جا ثبت شه؟ — تو: جوابِ صادقانه: کامل نمی‌دونم — یه نظریه دارم. می‌خوای با هم بفهمیم و بنویسیمش؟ اون داکِ طلاییه.'),
      ('ex', 'Junior: So it\'s okay to say "I don\'t know"? — You: It\'s required past a certain level. "I don\'t know, but here\'s how I\'d find out" — that sentence is half of engineering.', 'جونیور: پس گفتنِ «نمی‌دونم» اوکیه؟ — تو: از یه سطحی به بالا واجبه. «نمی‌دونم، ولی این‌طوری پیداش می‌کنم» — این جمله نصفِ مهندسیه.'),
      ('ex', 'Junior: You looked it up slower than I can google. — You: Ha! True — but notice what we wrote down: not the answer, the way to the answer. Next time, you\'re the one writing the doc.', 'جونیور: تو کندتر از من گوگلش رو پیدا کردی! — تو: ها! درسته — ولی دقت کن چی نوشتیم: جواب رو نه، راهِ رسیدن به جواب رو. دفعهٔ بعد، داک رو تو می‌نویسی.'),
    ]}],
  'tips': [
   ('نمی‌دانمِ حرفه‌ای', '«I don\'t know — here\'s how we\'d find out» — جمله‌ای که جونیور را جسور و منتور را صادق نگه می‌دارد؛ به‌علاوه: با هم بنویسیدش.'),
   ('ستایش را «قابلِتکرار» کن', '«keep doing this» بعد از هر ستایشِ مشخص — ستایشِ بی‌راهنما، خوشمزه است؛ با راهنما، ابزارِ رشد.'),
   ('سوالِ سومِ مقدس', '«What would you do if I weren\'t here?» — این یکی، اعتمادبه‌نفسِ تصمیمِ مستقل را در جونیور باز می‌کند.'),
  ]},
 'english-conferences-networking': {
  'grammar': ('گرامرِ عمیق‌تر: زبانِ پیگیریِ شبکه', [
    ('p', 'شبکه‌سازی، زبانِ **اشارهٔ مشترک + ارزشِ کوچک** است: پیگیری: **"Great meeting you at [رویداد] — that chat about X stuck with me."** (از آشنایی تو … خوشحال شدم — اون بحثِ X تو ذهنم موند) و لینکِ مقدس: **"Here\'s the [قالب/لینک] I mentioned."** (این همون چیزیه که گفتم.) برای درخواستِ معرفی: **"Would you be comfortable referring me?"** (راحتی داری منو معرفی کنی؟) و جوابِ گرمِ پیشنهادِ کمکِ دیگران: **"That\'s very kind — could I take you up on that next month?"** (لطف کردید — می‌تونم ماهِ بعد استفاده کنم؟) — take up on یعنی «استفاده‌کردن از پیشنهاد».'),
    ('ex', 'Hi Dara — great meeting you at DevOpsConf! Your chaos-engineering story stuck with me. As promised, here\'s the incident-review template I mentioned. Coffee next time you\'re in the city — my treat!', 'دارا سلام — از آشنایی تو DevOpsConf خیلی خوب شد! داستانِ مهندسیِ آشوبت تو ذهنم موند. همون‌طور که قول دادم، این قالبِ بازبینیِ حادثه‌ست که گفتم. دفعهٔ بعد که اومدی شهر، قهوه — مهمانِ من!'),
  ]),
  'extra_sections': [
    {'h2': 'گفتگو: خطِ بعد از talk و دعوتِ بی‌سوژه', 'blocks': [
      ('ex', 'You: Your backpressure talk was the best one today — the "queue as shock absorber" line clicked for me. Quick question: at what scale did you flip from sync to async? — Speaker: Around 2k RPS. Are you near that?', 'تو: ارائه‌ات دربارهٔ backpressure بهترینِ امروز بود — اون جملهٔ «صف مثلِ کمک‌فنر» برام جا افتاد. یه سوال: با چه مقیاسی از sync به async رفتید؟ — سخنران: حدودِ ۲۰۰۰ RPS. تو نزدیکی؟'),
      ('ex', 'You: Closer to 500 — but growing. — Speaker: Then you have time. Ping me in six months if the numbers bite — genuinely curious.', 'تو: نزدیکِ ۵۰۰ — ولی در رشد. — سخنران: پس وقت داری. شیش ماه دیگه پیام بده اگه اعداد گاز گرفتن — واقعاً کنجکاوم.'),
      ('ex', 'You: Deal — and let\'s connect now so I don\'t lose you in the crowd. — Speaker: Ha — the oldest networking trick in the book. Done!', 'تو: توافق — و الان وصل بشیم که تو جمع گمت نکنم. — سخنران: ها — قدیمی‌ترین ترفندِ شبکه‌سازیِ دنیا. شد!'),
    ]}],
  'tips': [
   ('سوالِ جزئیِ بعد از talk', 'یک جزئیاتِ مشخص از ارائه را بردار و سوال کن — از صفِ «متشکرم» یک پله بالاتر می‌روی و در حافظه می‌مانی.'),
   ('وعدهِ کوچک را اجرا کن', 'گفتی «قالب رو می‌فرستم»؟ ۲۴ ساعت — قولِ کوچکِ اجراشده، اعتبارِ شبکه‌اتست؛ قولِ بزرگِ اجرانشده، پدرِ آبروت.'),
   ('علاقه را با تاریخ دنبال کن', '«Ping me in six months» — چنین جوابی را با یادآورِ تقویم پیگیری کن؛ شبکه، با پیگیری‌های مؤدبانه زنده می‌ماند.'),
  ]},
 'english-level4-review': {
  'grammar': ('گرامرِ عمیق‌تر: زبانِ یک هفتهٔ واقعی در زمان‌ها', [
    ('p', 'اسپرینتِ کامل، تمرینِ «رفعِ زمان» است: برنامه با going to (I\'ll spike it), روایتِ روز با استمرار (I\'m implementing), خبرِ دیروز با گذشته (I finished the spike), تجربه با Perfect (I\'ve pushed the fix), و دمو با امری (Watch what happens). و سه قالبِ جمع‌بندی: **for the record** (برایِ ثبت), **bottom line** (خلاصهٔ کلام), **action items** (اقدام‌ها). هفتهٔ واقعی، هر پنج زمان را در پنج جملهٔ طبیعی می‌خواهد — امتحانِ فاز ۴ همین است.'),
    ('ex', 'Bottom line of my week: I finished the retry spike, I\'ve pushed the implementation, I\'m on the flaky test today, and I\'ll demo tomorrow. For the record: the flaky test is the last risk — action item is mine, due Friday.', 'خلاصهٔ هفته‌م: اسپایکِ retry رو بستم، پیاده‌سازی رو پوش کردم، امروز روی تستِ بی‌ثباتم، و فردا دمو میدم. برایِ ثبت: تستِ بی‌ثبات آخرین ریسکه — اقدامش مالِ منه، تا جمعه.'),
  ]),
  'extra_sections': [
    {'h2': 'گفتگو: رتروی جمعه و یک نکتهٔ محترمانه', 'blocks': [
      ('ex', 'Lead: Retro time — one thing that worked, one to improve? — You: Worked: the pairing on the retry — fastest fix I\'ve shipped here. Improve: honestly, our flaky test queue. It\'s eating hours.', 'لید: وقتِ رترو — یه چیزی که جواب داد، یه چیزی برایِ بهتر؟ — تو: جواب‌داد: پِر شدنِ retry — سریع‌ترین فیکسیه که این‌جا شِپ کردم. بهتر: راستش، صفِ تست‌های بی‌ثباتمون. ساعت‌ها رو می‌خوره.'),
      ('ex', 'Lead: It\'s been on the backlog forever. — You: Because it\'s nobody\'s job — that\'s the real bug. Proposal: one fix-sprint, one owner, and a rule — no new flaky test merges. — Lead: You just volunteered, haven\'t you?', 'لید: از همیشه توی بک‌لاگه. — تو: چون کارِ هیچ‌کسه — این خودش باگِ واقعیه. پیشنهاد: یه اسپرینتِ فیکس، یه مالک، و یه قانون — مرجِ تستِ بی‌ثباتِ جدید ممنوع. — لید: الان داوطلب شدی، نه؟'),
      ('ex', 'You: Guilty — happy to own it. Next retro, my own metric: flaky queue from fourteen open to under five. — Lead: That\'s the kind of volunteer we never stop.', 'تو: مقصرم — با کمالِ میل مالکش می‌شم. رتروِ بعد، متریکِ خودم: صفِ بی‌ثبات از چهاردهٔ باز به زیرِ پنج. — لید: داوطلبِ این‌جوری رو هیچ‌وقت نگه نمی‌داریم… یعنی می‌داریم!'),
    ]}],
  'tips': [
   ('رترو را با متریک پیشنهاد بده', 'هر نکتهٔ رترو را با «پیشنهاد + مالک + متریک» ببند — رتروی شکایت‌محور، فقط بوی سالمی می‌دهد؛ رتروی اقدام‌محور، تغییر می‌دهد.'),
   ('پنج‌جملهٔ جمع‌بندیِ هفته', 'جمعه‌ها پنج جمله بنویس: گذشته/استمرار/تازه/برنامه/ریسک — همان قالبِ «bottom line» رترو و گزارش.'),
   ('داوطلبشویِ محاسبه‌شده', 'مالکیتِ مسئلهٔ مزمنِ کوچک، ارزان‌ترین سرمایهٔ اعتبار در فاز ۵ است — رترو، ویترینِ داوطلبان است.'),
  ]},
}

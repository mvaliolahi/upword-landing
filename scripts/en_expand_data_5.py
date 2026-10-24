# -*- coding: utf-8 -*-
"""Stages 2+3 · lessons 73-90 — گفتگو + گرامرِ عمیق + نکات مکالمه."""

EXPANSIONS = {
 'english-register-tone': {
  'grammar': ('گرامرِ عمیق‌تر: نرم‌کننده‌های رسمی و جابه‌جاییِ لایه', [
    ('p', 'فاصلهٔ لایه‌ها با **سه ابزار** ساخته می‌شود: **۱) مودال‌های زنجیره‌ای:** could → would be able to → I would appreciate it if you could… (هر پله، یک درجه رسمی‌تر). **۲) تغییرِ فاعل:** «I need this Friday» (خودمانی) → «Would Friday be workable for the deadline?» (رسمی — سوال از زمان، نه دستور به آدم!). **۳) اسم‌سازی:** «fix it» → «the resolution of this issue» — اسم‌ها، فاصلهٔ اداری می‌سازند. و جادوی دو-جهته: جملهٔ رسمی را با یک حذف به نیمه برمی‌گردانی: «Thanks so much for the quick turnaround» (نیمه) ← «Thank you for your prompt response» (رسمی).'),
    ('ex', 'Formal: I would appreciate it if the revisions could be finalized by Thursday. / Casual-nice: Would be great if the fixes land by Thursday — no stress if it slips to Friday!', 'رسمی: متشکر می‌شوم اصلاحات تا پنجشنبه نهایی شود. / خودمانی-مهربان: عالی می‌شه فیکس‌ها تا پنجشنبه بیفته — اگه رفت جمعه هم استرس نیست!'),
  ]),
  'extra_sections': [
    {'h2': 'گفتگو: یک پیام، دو مشتری، دو لایه', 'blocks': [
      ('ex', '(to the client) We appreciate your patience — the fix is in final review and will be deployed today. I will confirm once it is live.', '(به مشتری) از صبرِ شما ممنونیم — فیکس در ریلویوی نهاییه و امروز دپلوی می‌شه. بعد از لایو شدن تأیید می‌کنم.'),
      ('ex', '(to the teammate, same minute) same news, other register: Fix is in review — should ship today 🤞 will ping the client when it\'s green.', '(به همکار، همان لحظه، رجیسترِ دیگر) همین خبر، لایهٔ دیگر: فیکس تو ریلویوئه — امروز شِپ می‌شه 🤞 سبز که شد به کلاینت می‌گم.'),
      ('ex', 'You: Two messages, two registers, one truth. The client hears calm; the teammate hears speed.', 'تو: دو پیام، دو لایه، یک حقیقت. مشتری آرومی می‌شنوه؛ همکار سرعت.'),
    ]}],
  'tips': [
   ('رجیستر را با «گیرنده» انتخاب کن', 'قاعدهٔ ده‌ثانیه‌ای: این پیام را فردا چه کسی غیر از گیرنده می‌تواند بخواند؟ هرچه بیشتر، لایه بالا؛ فقط خودش، پایین.'),
   ('اسم‌سازی، ابزارِ رسمی‌سازیِ فوری', 'فعل را به اسم بگردان: fix → the resolution; decide → the decision — همان جمله، یک لایه رسمی‌تر.'),
   (' Thanks را با نتیجه بچسبان', '«Thank you for X — as a result, Y» در لایهٔ رسمی: تشکرِ خالی، سرد است؛ تشکرِ پیوندخورده، حرفه‌ای.'),
  ]},
 'english-work-idioms': {
  'grammar': ('گرامرِ عمیق‌تر: بافتِ اصطلاح‌ها و افعالِ همراه', [
    ('p', 'هر اصطلاح، فعلِ همراهِ خودش را می‌خواهد — اینجاست که فهمیدن کافی نیست، استفاده باید درست باشد: **grab the low-hanging fruit** (می‌چینی/برداشتن), **move the needle** (عدد را جابه‌جا می‌کند), **keep someone in the loop** (نگه‌داشتن), **touch base with someone** (کوتاه‌هم‌پوشی‌کردن با), **hit the ground running** (از همان اول با سرعتِ کامل دویدن — اصطلاحِ محبوبِ شروعِ کار!), **pay off technical debt** (پرداختِ بدهیِ فنی — off را نگه دار). و هشدارِ ظریف: idioms با s و the و a سفت‌وبسته‌اند: **move the needle** همیشه با the؛ **on the same page** همیشه با the — حرفِ تعریفِ درونِ اصطلاح را همان‌طور که شنیدی نگه دار.'),
    ('ex', 'The goal for month one: hit the ground running, grab the low-hanging fruit in the backlog, and keep the stakeholders in the loop with Friday recaps.', 'هدفِ ماهِ اول: از همان اول با تمام‌قد بدو، میوه‌های پایینِ بک‌لاگ رو بچین، و ذی‌نفع‌ها رو با جمع‌بندی‌های جمعه در جریان نگه‌دار.'),
  ]),
  'extra_sections': [
    {'h2': 'گفتگو: جلسه‌ای که سه idiom نجاتش داد', 'blocks': [
      ('ex', 'Manager: The board wants visible progress by June. — You: Then we should grab the low-hanging fruit first — the sharing feature is a week of work and it\'s user-visible.', 'مدیر: هیئت‌مدیره تا ژوئن پیشرفتِ دیدنی می‌خواد. — تو: پس اول میوه‌های پایین رو بچینیم — فیچرِ اشتراک‌گذاری یک هفته کاره و برای کاربر دیده می‌شه.'),
      ('ex', 'Manager: Will it move the needle though? — You: Alone, no. But three small user-visible wins together? That\'s a needle-mover for perception.', 'مدیر: ولی سوزن رو جابه‌جا می‌کنه؟ — تو: تنها، نه. ولی سه بردِ کوچیکِ دیدنی با هم؟ برای «برداشت»، سوزن‌جابه‌جاکُنه.'),
      ('ex', 'Manager: I\'d rather over-deliver on one big thing. — You: Fair. Then let\'s be on the same page about what we\'re NOT doing this quarter — that\'s half the delivery.', 'مدیر: من ترجیح می‌دم روی یه چیزِ بزرگ بیش‌تحویل بدم. — تو: منصفانه. پس دربارهٔ چیزی که این فصل «نمی‌کنیم» هم‌نظر باشیم — نصفِ تحویل همینه.'),
    ]}],
  'tips': [
   ('سه اصطلاحِ شخصی‌ات را انتخاب کن', 'low-hanging fruit · in the loop · touch base — سه‌تای کم‌ریسکِ پرکاربرد را این هفته در سه موقعیتِ واقعی بکار؛ بعد سه‌تای بعدی.'),
   ('حرفِ تعریفِ درونِ idiom', 'the needle, the loop, the same page — the را حذف نکن؛ idiom با حذفِ حرفش می‌شکند.'),
   ('هرگز دو idiom در یک جمله', 'سالادِ اصطلاحی، بومی‌نماییِ خنده‌دار می‌سازد؛ یکی در جمله، سقفِ سلیقه است.'),
  ]},
 'english-phrasal-verbs-work': {
  'grammar': ('گرامرِ عمیق‌تر: جدا-پذیریِ phrasal verbs و شکلِ اسمی', [
    ('p', 'قاعدهٔ طلاییِ «ضمیر وسط»: اگر مفعول **ضمیرِ کوتاه** است، میانِ فعل و اضافه می‌نشیند: **call it off** ✓ (نهِ call off it ✗), **look it over**, **sort them out**. اگر اسم است، هر دو جایز است: **call off the meeting = call the meeting off.** و اسم‌سازی: خیلی از این‌ها اسم می‌سازند برای ایمیل: **the rollout** (عرضه), **a follow-up** (پیگیری), **a setup** (راه‌اندازی), **a sign-off** (تأیید), **a write-up** (مستند/گزارش) — در متنِ رسمی، اسم‌ها را می‌بینی: **"Pending sign-off on the write-up"** (در انتظارِ تأییدِ گزارش).'),
    ('ex', 'The rollout plan needs a sign-off, so let me walk you through the write-up — then you can sign off on it and we can roll it out Friday.', 'پلنِ رول‌اوت تأیید می‌خواد، پس بذار گزارش رو براتون باز کنم — بعدش تأییدش می‌کنید و جمعه رولش می‌کنیم.'),
  ]),
  'extra_sections': [
    {'h2': 'گفتگو: پنج phrasal verb در یک sync', 'blocks': [
      ('ex', 'Lead: Where are we on the migration? — You: We ran into a snag with the old indexes, but we sorted it out this morning — the fix is in the PR.', 'لید: مایگریشن کجاست؟ — تو: با ایندکس‌های قدیمی به یه گره خوردیم، ولی امروز صبح حلش کردیم — فیکس توی PRئه.'),
      ('ex', 'Lead: Good. The client is pushing back on the timeline though. — You: Then let me follow up with a revised plan — I\'ll lay out what we cut and what it buys us.', 'لید: خوبه. ولی مشتری روی تایم‌لاین می‌خواد عقبش بندازه. — تو: پس با یه پلنِ اصلاح‌شده پیگیریش می‌کنم — می‌نویسم چی رو حذف کردیم و چی می‌خره بهمون.'),
      ('ex', 'Lead: Do that today, and loop in Dara. — You: On it — I\'ll reach out to Dara and get back to you by EOD.', 'لید: همین امروز، و دارا رو هم بیار تو حلقه. — تو: روشم — به دارا می‌رسم و تا آخرِ روز برمی‌گردم بهت.'),
    ]}],
  'tips': [
   ('هفته‌ای سه فعل، با جملهٔ کامل', 'run into · sort out · loop in — هر کدام را با یک جملهٔ واقعی در اسلک بکار؛ فعلِ بی‌جمله در جلسه نمی‌آید.'),
   ('اسم‌های ریزِ ایمیل را بشناس', 'a follow-up, a sign-off, a write-up, the rollout — در متنِ رسمی، phrasalها به اسم تبدیل می‌شوند؛ دو فرهنگِ یک خانواده.'),
   ('look over ≠ overlook', 'مرور کن ≠ نادیده بگیر — یک حرفِ فاصله، دو دنیا معنا؛ در ایمیلِ مهم، این یکی غلطِ گران است.'),
  ]},
 'english-leading-meetings': {
  'grammar': ('گرامرِ عمیق‌تر: امریِ نرمِ جلسه‌گردانی و سوال‌های بسته', [
    ('p', 'جلسه‌گردان، ابزارهای «کنترلِ محترمانه» دارد: **Let\'s…** (بذارید…: Let\'s park that), **I\'d like us to…** (دوست دارم باهم…), **Why don\'t we…?** (چرا… نکنیم؟ — پیشنهادِ نرم). برای جمع‌بندیِ تصمیم: **"So, the decision is X — Ali owns Y by Friday. Anything I missed?"** — و برای سوالِ بسته‌ی سریع: **"Quick show of hands — who\'s used the new tool?"** (یه دست‌بلندکردنِ سریع — کی ابزارِ جدید رو استفاده کرده؟). و بستنِ محترمانه: **"We\'re at time — let me land the plane."** (وقت شد — بذار هواپیما رو بنشانم!) — جملهٔ جمع‌کردنِ محبوب.'),
    ('ex', 'We\'re at time, so let me land the plane: decision is the hybrid rollout, Sara owns the runbook, review next Thursday. Thanks all — solid meeting.', 'وقت شد، پس بذار هواپیما رو بنشانم: تصمیم، رول‌اوتِ هیبریده؛ سارا مالکِ ران‌بوک؛ بازبینی پنجشنبهٔ بعد. ممنون همه — جلسهٔ محکمی بود.'),
  ]),
  'extra_sections': [
    {'h2': 'گفتگو: جلسه‌ای که تو راندی — از باز تا بند', 'blocks': [
      ('ex', 'You: Thanks all. Goal for the next 25 minutes: pick the rollback strategy — leave with a decision, not options. Agenda: five minutes of context, then trade-offs, then the call.', 'تو: ممنون از همه. هدفِ این ۲۵ دقیقه: انتخابِ استراتژیِ رول‌بک — با تصمیم بیرون بریم، نه گزینه. دستور: پنج دقیقه زمینه، بعد trade-offها، بعد تصمیم.'),
      ('ex', 'Dara: Actually, can we talk about the alert thresholds too? — You: Important — let\'s park it and I\'ll add it to Thursday\'s sync. Sara, context first?', 'دارا: راستش، آستانه‌های هشدار هم صحبت کنیم؟ — تو: مهمه — کنارش می‌ذارم، پنجشنبه اضافه‌اش می‌کنم. سارا، اول زمینه؟'),
      ('ex', 'You: Straw poll — rollback to the last stable vs. hotfix forward? … Two for rollback, one hotfix. Rollback it is — Sara owns the runbook, due Thursday. Anything I missed?', 'تو: رأیِ سرانگشتی — رول‌بک به آخرینِ پایدار یا هات‌فیکس به جلو؟ … دو رول‌بک، یکی هات‌فیکس. پس رول‌بک — سارا مالکِ ران‌بوک، تا پنجشنبه. چیزی از قلم افتاد؟'),
    ]}],
  'tips': [
   ('وعدهٔ شروع: هدف + محصول', 'دو جملهٔ اول: «هدف X — با Y بیرون می‌رویم» — جلسه‌های بی‌وعده، بی‌پایانند.'),
   ('park با ثبت', 'هر park را جایی بنویس (داک/پیام) — پارکِ بی‌ثبت، حذفِ مؤدبانه است؛ طرف می‌بیند و اعتمادش می‌ریزد.'),
   ('land the plane را یاد بگیر', '«وقت شد — بذار بنشانمش» — بستنِ جلسه با این جمله، تمامِ خروجی‌ها را در دو ثانیه جمع می‌کند.'),
  ]},
 'english-writing-rfcs': {
  'grammar': ('گرامرِ عمیق‌تر: زبانِ بی‌طرفِ سند و بخش‌های استاندارد', [
    ('p', 'سندِ تصمیم، زبانِ «سوم‌شخصِ بی‌هیجان» دارد: **This document proposes…** (نهِ «I think we should…»), **The system currently…** , **We considered three alternatives; Option B was rejected because…** — فاعلِ «ما/سیستم»، نهِ «من». و ساختارِ سرفصل‌های استاندارد: **Summary / Background / Proposal / Alternatives Considered / Consequences / Open Questions** — شش‌تایی که خوانندهٔ سنیور، دنبالشان می‌گردد. برای ریسک‌ها: **"The main risk is X; mitigation is Y."** (ریسکِ اصلی Xئه؛ جبرانش Y.) — ریسکِ بی‌جبران، در سند، یعنی ناتمامی.'),
    ('ex', '## Alternatives Considered\n1. **Keep the current queue** — rejected: the p99 doubles every quarter as traffic grows.\n2. **Move all events to the streaming platform** — rejected for now: requires a team we don\'t have until Q3.\n3. **Shard the current queue** — chosen: keeps the ops surface familiar while fixing the hot partition.', 'بدیل‌های بررسی‌شده — ۱) نگه‌داشتنِ صفِ فعلی: رد؛ چون p99 هر فصل با رشدِ ترافیک دوبرابر می‌شه. ۲) انتقالِ همه به پلتفرمِ استریم: فعلاً رد؛ تیمی که نداریم تا Q3 رو می‌خواد. ۳) شاردکردنِ صفِ فعلی: انتخاب؛ سطحِ عملیاتی آشنا می‌مونه و پارتیشنِ داغ حل می‌شه.'),
  ]),
  'extra_sections': [
    {'h2': 'گفتگو: بازخورد روی RFC و پاسخِ نام‌بر', 'blocks': [
      ('ex', 'Reviewer: The consequences section undersells the ops load — sharding isn\'t free. — Author (you): Fair — adding a paragraph: on-call gets a new runbook and two new dashboards, called out in §5.2.', 'ریلویوئر: بخشِ پیامدها بارِ اپس رو کم‌فروش می‌کنه — شاردکردن مجانی نیست. — نویسنده (تو): درسته — یه پاراگراف اضافه می‌کنم: آن‌کال ران‌بوکِ جدید و دو داشبوردِ جدید می‌گیره، در §5.2 مشخص.'),
      ('ex', 'Reviewer: And I\'d question the Q3 assumption for option 2 — hiring might slip. — You: Good challenge — softening that line to "pending hiring" instead of a hard Q3. More honest.', 'ریلویوئر: و فرضِ Q3 گزینهٔ ۲ رو زیر سوال می‌برم — استخدام ممکنه بخوره عقب. — تو: چالشِ خوبیه — اون خط رو به «در انتظارِ استخدام» نرم می‌کنم به‌جای Q3ِ قطعی. صادقانه‌تر.'),
      ('ex', 'Reviewer: With those two changes, I\'m a clear yes. — You: Perfect — updating now, and tagging you in the diff. Decision deadline stands: Friday EOD.', 'ریلویوئر: با همین دو تغییر، جوابم کاملاً بله‌ست. — تو: عالیه — آپدیت می‌کنم و تو دیف تگت می‌کنم. ضرب‌الاجلِ تصمیم سرِ جاشه: جمعه آخرِ روز.'),
    ]}],
  'tips': [
   ('بدیل‌ها را با دلیلِ رد بنویس', '«rejected because…» — بخشِ بدیل‌ها، جایی است که سندِ تو «تولی» را جواب می‌دهد؛ نصفِ اعتبارِ RFC همین‌جاست.'),
   ('پاسخِ کامنت با شمارهٔ بخش', '«added in §5.2» — پاسخِ نام‌بر و محل‌دار، بازخورد را از گفتگو به ساختار می‌برد.'),
   ('ضرب‌الاجلِ تصمیم در خودِ سند', '«Decision deadline: Friday EOD» — سندِ بی‌ضرب‌الاجل، پیش‌نویسِ جاودان است.'),
  ]},
 'english-exec-presentations': {
  'grammar': ('گرامرِ عمیق‌تر: زبانِ عددِ اجرایی و جملاتِ کش‌دار', [
    ('p', 'ارائهٔ اجرایی، سه قالبِ عددی دارد: **cut X by Y%** (X رو Y درصد کم کن: cut latency by 40%), **takes Z weeks** (Z هفته می‌بره — نهِ «will be taking approximately» — کوتاه بگو!), **costs one engineer** (هزینه‌ش یک مهندسه). برای درخواست: **"The ask: approve X this week — decision needed by Friday."** — ask به‌عنوانِ اسمِ رسمیِ «درخواستِ مدنی» در این سطح خانه کرده. و برای قطع‌شدن: **"I\'ll land the plane here"** (همون بنشانیدنِ جلسه) یا ساده‌تر: **"The one-liner: X, Y, Z — and my ask stands."**'),
    ('ex', 'The one-liner, in case the elevator stops early: 40% faster checkout, one engineer for six weeks, no new infrastructure. The ask: approval by Friday so we make the March freeze.', 'نسخهٔ یک‌خطی، برای اگر آسانسور زود وایسه: تسویهٔ ۴۰٪ سریع‌تر، یک مهندس برای شش هفته، بدونِ زیرساختِ جدید. درخواست: تأیید تا جمعه تا فریزِ مارس رو بگیریم.'),
  ]),
  'extra_sections': [
    {'h2': 'گفتگو: سه دقیقه با مدیرعامل و سوالِ خلاصه', 'blocks': [
      ('ex', 'CEO (interrupting): I have three minutes, not five. — You: Then I\'ll start at the end: 40% faster checkout by March, one engineer, six weeks, no new infra. The ask is approval this week.', 'مدیرعامل (می‌پرد): سه دقیقه وقت دارم، نه پنج. — تو: پس از آخر شروع می‌کنم: تا مارس تسویهٔ ۴۰٪ سریع‌تر، یک مهندس، شش هفته، بدونِ زیرساختِ جدید. درخواست، تأییدِ همین هفته‌ست.'),
      ('ex', 'CEO: What\'s the risk? — You: One: two weekends of read-only reports. Mitigation: feature flag, rollback in minutes. Users never see it.', 'مدیرعامل: ریسکش چیه؟ — تو: یه دونه: دو آخرِ هفته گزارش‌ها فقط-خواندنی. جبران: فیچر-فلگ، رول‌بک در دقیقه‌ها. کاربر هیچ‌وقت نمی‌بیندش.'),
      ('ex', 'CEO: Fine — approved. Send me the one-liner in writing. — You: Will do — in your inbox in ten minutes. Thank you!', 'مدیرعامل: باشه — تأیید. همون یک‌خطی رو مکتوب بفرست. — تو: می‌فرستم — تا ده دقیقه توی اینباکس. ممنون!'),
    ]}],
  'tips': [
   ('اولِ خبر، اولِ سوالِ خلاصه', 'هر ارائهٔ اجرایی را با «پایانش» شروع کن — مدیرعاملِ عجول، سوالِ «خلاصه چیه؟» را با سکوتِ خودِ تو از پیش جواب می‌گیرد.'),
   ('the ask با تاریخ', '«Approval by Friday» — درخواستِ بی‌تاریخ، آرزوست؛ در این سطح، تاریخِ تصمیم را تو تعیین کن.'),
   ('یک‌خطی را مکتوب بفرست', 'مدیرعامل گفت «بفرست»؟ ده دقیقه — همان یک‌خطی در ایمیل؛ اجرایی‌ها، حافظه‌شان اینباکس است.'),
  ]},
 'english-salary-negotiation': {
  'grammar': ('گرامرِ عمیق‌تر: زبانِ معاوضهٔ مؤدب و شرطیِ نرم', [
    ('p', 'مذاکرهٔ حرفه‌ای، سه قالبِ زبانی دارد: **۱) شرطیِ دوطرفه:** «If the base is fixed, could we look at the sign-on?» (اگر پایه ثابته، می‌شه سراغ پاداشِ استخدام رفت؟). **۲) مجموع‌سازی:** «Together those close the gap» (این‌ها با هم شکاف رو می‌بندن) — اهرم‌ها را جمع کن، نه تک‌تک. **۳) بازکردنِ پنهان:** «What flexibility is there on the overall package?» (روی کلِ پکیج چقدر انعطاف هست؟) — package به‌جای salary، در مذاکره، در را گشاد می‌کند. و جملاتِ مقدسِ ردِ محترمانه: «I\'d love to make this work» (دوست دارم جورش کنم) — پیش از هر عددِ سختی که می‌گویی.'),
    ('ex', 'I\'d love to make this work. If the base is fixed at 120, could we look at the sign-on and a six-month review with agreed raise criteria? Together, those close the gap for me.', 'دوست دارم این جواب بده. اگه پایه روي ۱۲۰ قفله، می‌شه سراغِ پاداشِ استخدام و بازبینیِ شش‌ماهه با معیارهایِ حقوقیِ توافقی بریم؟ این‌ها با هم، شکاف رو برای من می‌بندن.'),
  ]),
  'extra_sections': [
    {'h2': 'گفتگو: سه رفت‌وبرگشتِ مذاکره و بستن', 'blocks': [
      ('ex', 'Recruiter: Our offer is 120 base. — You: Thank you — I\'m genuinely excited about this team. Based on the market and scope, I was targeting 140-150. Is there flexibility?', 'کارگزین: پیشنهادمون پایهٔ ۱۲۰ئه. — تو: ممنون — واقعاً برای این تیم ذوق دارم. بر اساسِ بازار و حجمِ نقش، هدلم ۱۴۰-۱۵۰ بود. انعطافی هست؟'),
      ('ex', 'Recruiter: 120 is our cap for the level. — You: Understood. Then the other levers — sign-on and equity refresh: could those move, so together we close the gap?', 'کارگزین: ۱۲۰ سقفِ سطحِ ماست. — تو: متوجه‌ام. پس اهرم‌های دیگه — پاداشِ استخدام و تکمیلِ سهام: اونا می‌تونن حرکت کنن که با هم شکاف رو ببندیم؟'),
      ('ex', 'Recruiter: Ten thousand sign-on is doable. — You: Then let\'s do it: 120 base, ten thousand sign-on, and a six-month review. Could I get that in writing by Thursday? Excited to sign.', 'کارگزین: ده هزار پاداشِ استخدام شدنیه. — تو: پس همین: پایهٔ ۱۲۰، ده هزار پاداش، و بازبینیِ شش‌ماهه. تا پنجشنبه مکتوبش رو می‌گیرم؟ ذوق دارم امضا کنم.'),
    ]}],
  'tips': [
   ('excited قبل از عددِ سخت', '«I\'m genuinely excited…» همیشه پیش از قلابِ انعطاف — مذاکره را از تقابل به حلِ مسئله می‌برد.'),
   ('سکوتِ پس از سوال', 'پرسیدی و تمام — دو-سه ثانیه سکوت؛ زبانِ دوم‌ها با پرکردنِ سکوت، عددِ خودشان را می‌بخشند.'),
   ('مکتوحش کن، نه حافظه را', '«Could I get that in writing?» — هر عددِ نهایی، تا مکتوب نشود امضا نیست؛ جمله‌اش را با تاریخ بگو.'),
  ]},
 'english-remote-async': {
  'grammar': ('گرامرِ عمیق‌تر: زبانِ timezone و پیامِ self-contained', [
    ('p', 'پیامِ async باید **self-contained** (خودبسنده) باشد: زمینه + وضعیت + درخواست + ضرب‌الاجل، همه در یک پیام — چون خواننده شاید شش ساعت بعد و بدونِ حافظهٔ گفتگو بیدار می‌شود. و زبانِ timezone: **CET/UTC/EET** (منطقهٔ ساعت را کوتاه بنویس: 14:00 CET), **my EOD vs your EOD** (آخرِ روزِ من و تو فرق دارد!), **overlap hours** (ساعت‌های هم‌پوشانی). قالبِ درخواستِ نظرِ async: **"Comments welcome until 10:00 CET tomorrow — silence = agreement."** — سه‌لایه: مهلت + منطقه + قانونِ سکوت.'),
    ('ex', 'Quick async decision needed: retry policy v2 or v3? Context in the RFC, summary in this thread. Comments welcome until 10:00 CET tomorrow — silence = agreement, and I\'ll post the outcome either way.', 'یه تصمیمِ async لازمه: خط‌مشیِ retry نسخهٔ ۲ یا ۳؟ زمینه تو RFC، خلاصه تو همین thread. تا ۱۰ صبحِ CET فردا نظرات — سکوت یعنی موافقت، و نتیجه رو به‌هرحال اعلام می‌کنم.'),
  ]),
  'extra_sections': [
    {'h2': 'گفتگو: ریموت — دست‌انداختن و برخاستن', 'blocks': [
      ('ex', 'You: Heads-up: I\'m offline 15:00-21:00 CET today (school pickup + dinner). Ping-worthy stuff before 15:00 gets a fast answer.', 'تو: خبر: امروز ۱۵ تا ۲۱ CET آفلاینم (تحویلِ مدرسه + شام). چیزِ پیج‌طورِ قبلِ ۱۵ جوابِ سریع می‌گیره.'),
      ('ex', 'Teammate: Quick one — the staging link, is it up? — You: Yep — pinned in the channel. And not urgent, tomorrow works too!', 'همکار: یه سوالِ کوتاه — لینکِ staging بالاست؟ — تو: آره — تو کانال پین شده. و فوری نیست، فردا هم جواب می‌ده!'),
      ('ex', 'Teammate: Perfect, enjoy the pickup! — You: Thanks! Back online 21:00-ish — and the deploy can go without me, Sara has the keys.', 'همکار: عالیه، تحویلِ مدرسه رو دلپذیر باش! — تو: ممنون! حدودِ ۲۱ برگردم آنلاین — و دپلوی بدونِ من هم می‌ره جلو، سارا کلیدها رو داره.'),
    ]}],
  'tips': [
   ('هر پیام، یک جزیرهٔ کامل', 'زمینه/وضعیت/اقدام/درخواست در یک پیام — خوانندهٔ نیمه‌شب نباید به سه پیامِ قبل برگردد.'),
   ('ساعت با منطقه', 'همیشه CET/UTC بنویس — «سه‌شنبه ساعتِ سه» در تیمِ ریموت، یعنی هیچ ساعتِ قطعی.'),
   ('silence = agreement را استفاده کن', 'مهلتِ نظر با قانونِ سکوت — تصمیمِ async را از بی‌پایانی نجات می‌دهد؛ فقط حتماً نتیجه را اعلام کن.'),
  ]},
 'english-cross-team-politics': {
  'grammar': ('گرامرِ عمیق‌تر: زبانِ نفوذِ بی‌اختیار', [
    ('p', 'نفوذِ بی‌اختیار، سه قالبِ محترمانه دارد: **۱) سوالِ ساده‌ساز:** «What would make this easy for your side?» (چی این رو برایِ طرفِ شما آسون می‌کنه؟) — توپ را با احترام می‌اندازی. **۲) پیشنهادِ معاوضه:** «I\'ll trade you a review» (یه ریلویو در ردش می‌دم) — اعتبار، ارزِ بین‌تیمی است. **۳) اعلامِ مسیرِ جایگزین:** «If this week truly can\'t work, we\'ll ship it flag-off and turn it on later» — بستن بدونِ بلوک‌کردن. و جملهٔ مدیریتِ انتظار: **"I don\'t own your roadmap, so I\'m asking, not assigning"** (برنامهٔ شما مالِ من نیست، پس درخواست می‌کنم نه دستور) — شفاف‌ترین امانتِ بین‌تیمی.'),
    ('ex', 'I don\'t own your roadmap, so I\'m asking, not assigning: we\'re blocked on the rate-limit config — a one-line change, PR drafted. What would make this easy for your side? Happy to trade a review of your queue.', 'برنامهٔ شما مالِ من نیست، پس درخواست می‌کنم نه دستور: رویِ کانفیگِ rate-limit بلاکیم — تغییرِ یک‌خطی، PRش نوشته شده. چی این رو برایِ شما آسون می‌کنه؟ ریلویوی صفِ شما رو در ردش می‌دم.'),
  ]),
  'extra_sections': [
    {'h2': 'گفتگو: وابستگیِ گره‌خورده و نردبانِ تشدید', 'blocks': [
      ('ex', 'You (their channel): Bumping this from last week — the EU launch is waiting on it. Anything blocking it on your side I can help with?', 'تو (کانالِ اون‌ها): از هفتهٔ پیش بالا میارمش — عرضهٔ اروپا منتظرشه. چیزِ بلاک‌کننده‌ای سمتِ شما هست که بتونم کمک کنم؟'),
      ('ex', 'Platform lead: Honestly, it fell off the list — sprint\'s packed. — You: Understood. Can I bring our managers in for ten minutes of calendar math? Nothing dramatic — we just need a slot this week.', 'لیدِ پلتفرم: راستش از لیست افتاد — اسپرینت پُره. — تو: متوجه‌ام. می‌تونم مدیرها رو بیارم برایِ ده دقیقه حسابِ تقویم؟ خبری نیست — فقط این هفته یه جا لازم داریم.'),
      ('ex', 'Platform lead: Let\'s try the flag-off path instead — I\'ll do the config next sprint. — You: Deal — flag-off it is, and the PR stays open for you. I\'ll note the trade-off to the PM so it\'s a decision, not a surprise.', 'لیدِ پلتفرم: بیا مسیرِ فلگ-بسته رو بریم — کانفیگ رو اسپرینتِ بعد می‌کنم. — تو: توافق — فلگ-بسته می‌ره، و PR برایِ شما باز می‌مونه. trade-off رو به PM می‌گم که تصمیم باشه، نه سورپرایز.'),
    ]}],
  'tips': [
   ('درخواستِ بی‌مالک با «asking, not assigning»', 'شفاف‌سازیِ قاعدهٔ بازی در اولِ درخواست — بین‌تیمی‌ها همین یک جمله، جبههٔ نرم می‌سازد.'),
   ('مسیرِ جایگزین = بردهٔ بی‌دشمنی', '«Flag-off path» را همیشه در جیب داشته باش — نشاندادنِ راهِ بسته‌نشدن، تو را از معترض به حل‌کننده ارتقا می‌دهد.'),
   ('اعلامِ trade-off به PM', 'هر جابه‌جاییِ بین‌تیمی را مکتوب به ذی‌نفع — تصمیمِ بی‌اعلام، بعداً خودت را مقصر می‌کند.'),
  ]},
 'english-incident-management': {
  'grammar': ('گرامرِ عمیق‌تر: زبانِ فشردهٔ حادثه', [
    ('p', 'حادثه، سه قالبِ چهارخطی دارد: **اعلام:** «P1 — [system] is down/degraded for [X%] of users since [time]. Channel: #inc-NNN.» **بریف:** «STATUS / CAUSE (working theory) / ACTION / NEXT UPDATE at [time].» **پایان:** «All-clear: metrics back to baseline. Postmortem [day] at [time].» — و زمانِ فعل‌ها: ادامهٔ حادثه با استمرار (users are seeing 5xx), اقدام با استمرار (we\'re rolling back), نتیجه با ساده (errors dropped). و پرچم‌های فکری: **working theory** (هنوز حدس), **confirmed** (تأیید شد), **ruled out** (حذف شد) — سه برچسبِ جلوگیری از قاطی‌شدنِ حدس و واقعیت.'),
    ('ex', '14:20 STATUS: 5xx at ~30% of EU users, started 14:02. CAUSE (working theory): last deploy\'s DB pool change. ACTION: rollback running, 3/12 pods done. NEXT UPDATE: 14:30.', '۱۴:۲۰ وضعیت: خطای 5xx برای ~۳۰٪ کاربرهای اروپا، از ۱۴:۰۲. علت (فرضیهٔ در حالِ کار): تغییرِ پولِ دیتابیس در آخرین دپلوی. اقدام: رول‌بک در جریانه، ۳ از ۱۲ پاد تمام. آپدیتِ بعدی: ۱۴:۳۰.'),
  ]),
  'extra_sections': [
    {'h2': 'گفتگو: در کانالِ جنگ — ده دقیقهٔ خاموش‌گیر', 'blocks': [
      ('ex', 'IC (you): Facts first: 5xx at 30%, EU-heavy, started 14:02. Dara on metrics, Sara on customer comms, I run the bridge. Theories to the thread, actions to me.', 'فرمانده (تو): اول واقعیت‌ها: ۵xx در ۳۰٪، اروپا-محور، از ۱۴:۰۲. دارا روی متریک‌ها، سارا روی ارتباطِ مشتری، من پل رو می‌رانم. فرضیه‌ها تو thread، اقدام‌ها پیشِ من.'),
      ('ex', 'Dara: Working theory — the pool change didn\'t account for EU failover. — You: Noted as theory. Rollback\'s running; if errors drop when it lands, we upgrade it to confirmed.', 'دارا: فرضیه — تغییرِ پول، فِیل‌اوورِ اروپا رو حساب نکرده بود. — تو: به‌عنوانِ فرضیه ثبت شد. رول‌بک روونه؛ اگه با فرودش خطاها افت کرد، به «تأییدشده» ارتقاش می‌دیم.'),
      ('ex', 'You: 14:30 — rollback complete, errors at baseline, p99 normal. Monitoring 30 min, then all-clear. Postmortem Friday 10:00 — blameless, bring timelines.', 'تو: ۱۴:۳۰ — رول‌بک کامل، خطاها عادی، p99 نرمال. ۳۰ دقیقه پایش، بعد اعلامِ امنیت. پست‌مورتم جمعه ۱۰ — بی‌اتهام، تایم‌لاین‌هاتون رو بیارید.'),
    ]}],
  'tips': [
   ('فرضیه را برچسب بزن', '«working theory» و «confirmed» را قاطی نکن — اعلامِ حدس به‌عنوانِ واقعیت در حادثه، خطای هفت‌ساله می‌سازد.'),
   ('هر بریف با زمانِ آپدیتِ بعدی', '«NEXT UPDATE 14:30» — وعدهٔ آپدیت، وحشتِ سکوت را می‌کُشد؛ حتی خبرِ «تغییری نیست» را بده.'),
   ('نقش‌ها را با اسم اعلام کن', '«Dara on metrics, Sara on comms» — حادثهٔ بی‌نقش، حادثهٔ بی‌مسئولیت است؛ اولین جملهٔ فرمانده همین است.'),
  ]},
 'english-performance-reviews': {
  'grammar': ('گرامرِ عمیق‌تر: زبانِ شواهد و درخواستِ معیار', [
    ('p', 'review، زبانِ «شاهدِ مکتوب» است: ردیفِ اثر با **فعل + عدد + دامنه**: «Led X — Y happened — adopted by Z». برای جمع‌بندی: **bottom line** (خلاصهٔ کلام: «Bottom line: my strongest quarter here.») و برای درخواستِ معیار: **"What would \'exceeds\' have looked like on that project?"** (اون پروژه «فراتر از انتظار» چه شکلی می‌بود؟) — سوالِ معیار، بحث را از «نمرهٔ من» به «تعریفِ سیستم» می‌برد. و جملهٔ شروعِ مذاکرهٔ ارتقا: **"I want to grow toward senior — from my read, the gap is X. Can we turn that into a plan?"**'),
    ('ex', 'Bottom line: my strongest quarter here — the retry redesign shipped two months early, cut failures 38%, and two teams adopted the pattern. For next year, I want to grow toward senior; from my read, the gap is cross-team influence. Can we turn that into a plan?', 'خلاصهٔ کلام: قوی‌ترین فصلِ من این‌جا — بازطراحیِ retry دو ماه زودتر شِپ شد، خطاها ۳۸٪ کم شد، و دو تیم الگو رو به کار بردن. برایِ سالِ بعد می‌خوام به سمتِ سنیور; از برداشتم، فاصله نفوذِ بین‌تیمیه. می‌تونیم تبدیلش کنیم به یه برنامه؟'),
  ]),
  'extra_sections': [
    {'h2': 'گفتگو: دفاعِ محترمانه دربارهٔ نمره', 'blocks': [
      ('ex', 'Manager: Overall: meets expectations. — You: Thanks — I want to understand the gap. The retry project: shipped early, 38% fewer failures, two teams adopted it. What would "exceeds" have looked like there?', 'مدیر: جمع‌بندی: در حدِ انتظار. — تو: ممنون — می‌خوام فاصله رو بفهمم. پروژهٔ retry: زودتر شِپ شد، ۳۸٪ خطای کمتر، دو تیم استفاده کردن. اون‌جا «فراتر از انتظار» چه شکلی می‌بود؟'),
      ('ex', 'Manager: Honestly? The visibility outside the team. Two teams adopted it, but you didn\'t broadcast the pattern. — You: That\'s a fair gap — and it\'s concrete. Proposal: I write it up as an internal RFC-style post next quarter. Does that count as the "exceeds" shape?', 'مدیر: راستش؟ دیده‌شدن بیرون از تیم. دو تیم استفاده کردن، ولی الگو رو نشر ندادی. — تو: فاصلهٔ منصفانه‌ایه — و مشخصه. پیشنهاد: فصلِ بعد به شکلِ RFCِ داخلی می‌نویسمش. همون شکلِ «فراتر»ه؟'),
      ('ex', 'Manager: Exactly that shape. — You: Then we have a deal — and I\'ll log it in our 1:1 doc so the next review starts from the plan, not from memory.', 'مدیر: دقیقاً همون شکل. — تو: پس توافق کردیم — و تو داکِ 1:1هامون ثبتش می‌کنم که رِویوی بعدی از برنامه شروع بشه، نه از حافظه.'),
    ]}],
  'tips': [
   ('دفاع با سوالِ معیار', '«What would exceeds have looked like?» — هر نمرهٔ بحث‌برانگیز را با همین سوال بپرس؛ پاسخش، نقشهٔ سالِ بعدِ توست.'),
   ('ردیف‌ها را با لینک بده', 'هر ادعای بزرگ با PR/داشبورد/داک — خودارزیابیِ بی‌لینک، سلیقه است؛ لینک‌دار، سند.'),
   ('دفترِ بردها، ماهی سه ردیف', 'اولین پنجشنبهٔ هر ماه — review از انتخابِ ردیف‌ها شروع می‌شود، نه از یادآوریِ دسامبر!'),
  ]},
 'english-cultural-pragmatics': {
  'grammar': ('گرامرِ عمیق‌تر: understatement و زبانِ غیرمستقیمِ بریتانیایی', [
    ('p', 'فرهنگِ انگلیسی‌زبان، به‌خصوص بریتانیا، عاشقِ **understatement** (کم‌گویی) است: «a bit of a problem» می‌تواند یعنی «فاجعه»؛ «not ideal» یعنی «خیلی بد»؛ «I\'m slightly concerned» یعنی «به‌شدت نگرانم»! جدولِ ترجمهٔ بریتانیایی: «That\'s a brave proposal» = احتمالاً «دیوانه‌ست» · «With the greatest respect…» = «به نظرم اشتباه می‌کنی» · «Very interesting» = «مشکوکم». و زیرِ understatement، قاعدهٔ عملی: هرچه جملهٔ بریتانیایی خنثی‌تر و آرام‌تر، پیامِ زیرین احتمالاً جدی‌تر — و جوابِ حرفه‌ای: دقیق بپرس: **"When you say \'interesting\' — is that a concern I should address, or genuinely interesting?"**'),
    ('ex', 'British colleague: The new rollout plan is… interesting. — You: I\'m still learning the local dial — when you say "interesting", is that a real concern I should hear now, or a compliment I\'m misreading?', 'همکارِ بریتانیایی: پلنِ رول‌اوتِ جدید… جالبه. — تو: هنوز دارم صفحه‌محلیِ این‌جا رو یاد می‌گیرم — وقتی می‌گی «جالب»، یه نگرانیِ واقعیه که الان باید بشنوم، یا تعریفه که دارم اشتباه می‌خونم؟'),
  ]),
  'extra_sections': [
    {'h2': 'گفتگو: سه فرهنگ، یک ایمیل، سه واکنش', 'blocks': [
      ('ex', 'You write: "This timeline is quite aggressive." — US teammate: "Agreed — let\'s cut scope." (took it literally)', 'تو می‌نویسی: «این تایم‌لاین خیلی جسورانه‌ست.» — همکارِ آمریکایی: «موافقم — اسکوپ رو کم کنیم.» (ساده فهمید)'),
      ('ex', 'UK teammate: "A little optimistic, perhaps?" (means: it will not happen) — You: catching it — "So that\'s a no on the timeline from you too? Good — two votes for renegotiating."', 'همکارِ بریتانیایی: «یه‌جورایی خوش‌بینانه، شاید؟» (یعنی: اتفاق نمی‌افته) — تو: می‌گیری — «پس از سمتِ تو هم رویِ تایم‌لاین نُه؟ خوبه — دو رأی برایِ بازمذاکره.»'),
      ('ex', 'Canadian teammate: "This is maybe fine, but sorry — could we maybe revisit the dates?" (soft, but the point stands) — You: "Taking all three: we revisit. Thanks for the honest reads, team."', 'همکارِ کانادایی: «شاید اوکیه، ولی ببخشید — می‌شه شاید تاریخ‌ها رو دوباره ببینیم؟» (نرم، ولی جدی) — تو: «جمعِ هر سه: بازبینی می‌کنیم. ممنون از برداشت‌های صادقانه، تیم.»'),
    ]}],
  'tips': [
   ('صفحهٔ بریتانیایی: هرچه آرام‌تر، جدی‌تر', 'کم‌گوییِ بریتانیایی را دست‌کم نگیر — سوالِ دقیق بپرس تا قالبِ زیرین بیرون بیاید.'),
   ('sorryِ کانادایی را سلب حق مگیر', '«Sorry — quick question» — عذرخواهیِ فرهنگی است نه اقرار؛ تو هم قالبش را بردار؛ در کانادا آدم را دوست‌پذیر می‌کند.'),
   ('سه‌نسخه‌ایِ پیامِ مهم', 'پیام‌های حساس را برای سه فرهنگ در ذهن سه‌بار بخوان — ساده برای US، نرم برای CA، غیرمستقیم‌فهم برای UK؛ در تردید، خودت شفاف‌ساز کن.'),
  ]},
 'english-humor-banter': {
  'grammar': ('گرامرِ عمیق‌تر: زبانِ شوخیِ سالم — خود-هدفی و اغراقِ مهربان', [
    ('p', 'طنزِ کاریِ سالم دو گرامرِ ثابت دارد: **۱) خود-هدفی با زمانِ گذشته/استمرار:** «I spent 40 minutes on a typo — truly at the peak of my powers» (۴۰ دقیقه روی یه تایپو — واقعاً در اوجِ قدرتم) — قلمرویی که همیشه امن است: خودت، ابزارها، موقعیت. **۲) اغراقِ مهربان:** «This legacy code predates the internet. I think Linus reviewed it» (این کد قدیمی‌تر از اینترنته — فکر کنم لینوس ریلویوش کرده!) — اغراقِ بی‌هدفِ انسانی. و علامت‌های لحنِ متن: 😅 و 🙃 و «to be fair» (به‌انصاف — قبلِ شوخیِ ملایمِ نقدِ خودت) — شوخیِ بی‌لحن در متن، سرد خوانده می‌شود؛ ایموجی، لبخندِ صدای توست.'),
    ('ex', 'to be fair, the bug was technically mine — I wrote it, I debugged it for an hour, and I high-fived myself when the fix was one line. Peak engineering 😅', 'به‌انصاف، باگ از نظرِ فنی مالِ من بود — من نوشتمش، یه ساعت دیباگش کردم، و وقتی فیکس یک خط بود به خودم پنج زدم. اوجِ مهندسی 😅'),
  ]),
  'extra_sections': [
    {'h2': 'گفتگو: banter در استندآپ و مرزِ آرام', 'blocks': [
      ('ex', 'Teammate: Ali, the flaky test beat you again? — You: Beat me? We\'re in a committed relationship at this point. I\'m naming it in my will 😄', 'همکار: علی، تستِ بی‌ثقال باز برد؟ — تو: برد؟ ما الان تو یه رابطهٔ جدی‌ایم. تو وصیت‌م هم ذکرش می‌کنم 😄'),
      ('ex', 'Teammate: Ha! You\'re的速度 legendary. — You: Legendary was yesterday — today I\'m just consistent. Consistency is my brand!', 'همکار: ها! سرعتت افسانه‌ایه. — تو: افسانه دیروز بود — امروز فقط «ثابتم». ثبات برندِ منه!'),
      ('ex', 'You (later, privately): Hey, the "speed" joke lands fine, but could we keep my English out of the banter? The code, sure — roast the code all day. — Teammate: Totally fair — sorry! Code it is.', 'تو (بعداً، خصوصی): هی، شوخیِ «سرعت» اوکیه، ولی می‌شه لهجه/انگلیسی‌م رو بیرون از banter نگه داریم؟ کد رو بله — کلِ روز کبابش کن. — همکار: کاملاً منصفانه — ببخشید! پس کد.'),
    ]}],
  'tips': [
   ('هدف: خودت، کد، موقعیت', 'هرگز آدم‌های مشخص، ظاهر، قومیت — سه هدفِ امن، یک خطِ قرمزِ پنج‌تایی؛ روستِ کد، قانونِ بومیِ تیم‌های فنی است.'),
   ('جوابِ banter با banter', 'سکوتِ خشک، بازی را می‌شکند — «We\'re in a committed relationship» نوعی جوابِ قلابی؛ بردار و شخصی‌ساز.'),
   ('مرز را خصوصی و آرام بگو', 'شوخی از خط گذشت؟ همان فرمولِ درس ۸۵: خصوصی + آرام + «keep it to my code» — ۹۰٪ همان‌جا تمام.'),
  ]},
 'english-technical-leadership': {
  'grammar': ('گرامرِ عمیق‌تر: زبانِ قاب‌گذاری و واگذاریِ مالکیت', [
    ('p', 'رهبریِ فنی، دو جمله‌ی پُربار دارد: **قاب‌گذاری:** «The real problem here isn\'t X — it\'s Y» (مسئلهٔ واقعی X نیست — Yئه) / «What matters most this quarter is…» — فعلِ سوم‌شخصِ حکم‌مانند، بیِ «I think». **واگذاری:** «You own this — I\'ll unblock you» (مالکش تویی — من راه رو باز می‌کنم) — owns در این سطحِ جمله، حکمِ اعتماد است. و برای تصمیم‌ها: «This is reversible — let\'s try it» (این برگشت‌پذیره — امتحانش کنیم) در برابرِ «This deserves an RFC» (این لایقِ RFCئه) — تفکیکِ هزینهٔ تصمیم، گرامرِ روزانهٔ tech lead است.'),
    ('ex', 'Let me reframe: the bug queue isn\'t a testing problem — it\'s an ownership problem. Nobody owns flaky. So: Sara, you own the flaky queue this quarter — not to fix every test, to own the system that kills them. I\'ll unblock you with time and air cover.', 'بذار قاب رو عوض کنم: صفِ باگ، مشکلِ تست نیست — مشکلِ مالکیته. هیچ‌کس مالکِ بی‌ثبات‌ها نیست. پس: سارا، این فصل مالکِ صفِ بی‌ثقالی — نه برایِ درست‌کردنِ تک‌تکِ تست‌ها، برایِ مالک‌بودنِ سیستمی که می‌کُشتشون. من هم با وقت و پوششِ هوایی راه رو باز می‌کنم.'),
  ]),
  'extra_sections': [
    {'h2': 'گفتگو: نمودارِ داغ و چکِ گلوگاه', 'blocks': [
      ('ex', 'Lead: Everyone\'s blocked on something. — You: Then today I\'m the bottleneck-checker — everyone, one line: what are you waiting on and who has it?', 'لید: همه روی یه چیزی بلاکن. — تو: پس امروز من چکرِ گلوگاهم — همه، یک خط: منتظرِ چی هستید و پیش کیه؟'),
      ('ex', 'Teammate 1: Staging credentials — DevOps. — You: Mine now, back in 10. — Teammate 2: Design review of the empty states. — You: Designer\'s back Thursday — let\'s timebox a 10-min async review today instead.', 'همکارِ ۱: اعتبارنامه‌های staging — DevOps. — تو: پیشِ من، ده دقیقه برمی‌گردم. — همکارِ ۲: ریلویوی طراحیِ حالت‌های خالی. — تو: طراح پنجشنبه برمی‌گرده — بذارید امروز ده دقیقه ریلویوی async بذاریم به‌جاش.'),
      ('ex', 'Lead: Three bottlenecks, three unlocks, twelve minutes. — You: That\'s the job. I\'ll do this every Monday — it\'s cheaper than a retro about why the week stalled.', 'لید: سه گلوگاه، سه بازکردن، دوازده دقیقه. — تو: کار همینه. هر دوشنبه این رو می‌کنم — از رترو دربارهٔ «چرا هفته لنگ زد» ارزون‌تره.'),
    ]}],
  'tips': [
   ('قاب را در سه جمله بکش', '«The real problem is…» — بیش از سه جمله، سخنرانی است؛ قابِ خوب، کوتاه و حکم‌دار.'),
   ('مالکیت را با پشتیبانی بده', '«You own it + I\'ll unblock you» — واگذاریِ بی‌پشتیبانی، سپردنِ شکست است؛ دو جمله، همیشه با هم.'),
   ('دوشنبه‌های گلوگاه', '«What are you waiting on and who has it?» — یک جمله، ده دقیقه — ارزان‌ترین جلسهٔ رهبریِ فنی که می‌شناسی.'),
  ]},
 'english-open-source': {
  'grammar': ('گرامرِ عمیق‌تر: زبانِ محترمانهٔ متن‌باز — مؤدبانه‌های داوطلبانه', [
    ('p', 'متن‌باز، زبانِ «داوطلبِ محترم» دارد: **I\'d like to take a shot at this** (دوست دارم روشش کار کنم — نهِ «I will do it» — تواضعِ مشارکت), **Happy to adjust** (با کمالِ میل اصلاح می‌کنم — جوابِ استانداردِ کامنتِ ریلویو), **Not sure if this is a bug or intended behavior — happy to close if it\'s a duplicate** (نمیدانم باگه یا عمدی — اگر تکراریه با کمالِ میل می‌بندمش). و سنجاقِ اول: **"First time contributing here — let me know if I\'m missing conventions"** (اولین مشارکتم این‌جاست — اگر قراردادی را از قلم انداختم بگویید) — همین یک جمله، نصفِ قضاوتِ مثبتِ maintainer را می‌سازد.'),
    ('ex', 'First time contributing here — let me know if I\'m missing any conventions. I\'d like to take a shot at the docs rewrite for the CLI section; I\'m a daily user, and the current examples tripped me up on my first day. Happy to adjust the scope however fits the roadmap.', 'اولین مشارکتم این‌جاست — اگه قراردادی رو از قلم انداختم بگید. دوست دارم روی بازنویسیِ داکِ بخشِ CLI کار کنم؛ کاربرِ روزانه‌ام و مثال‌های فعلی روزِ اول لالاییم کرد. با کمالِ میل دامنه رو هر جور که با رودمپ بخونه تنظیم می‌کنم.'),
  ]),
  'extra_sections': [
    {'h2': 'گفتگو: issue، PR و یک مرجِ خوش‌یمن', 'blocks': [
      ('ex', 'Maintainer: The PR looks solid, but we prefer tests in a separate file. — You: Makes sense — moved, and pushed. Happy to adjust anything else that doesn\'t match the house style.', 'نگه‌دارنده: PR محکمه، ولی تست‌ها رو تو فایلِ جدا می‌پسندیم. — تو: منطقیه — منتقل و پوش شد. هر چیزِ دیگه‌ای هم که با سبکِ خونه جور نبود، با کمالِ میل اصلاح می‌کنم.'),
      ('ex', 'Maintainer: Merged. Thanks for the clean contribution — and for reading the contributing guide first! — You: It\'s a good guide! Honestly, the "small PR" section saved us both a review round.', 'نگه‌دارنده: مرج شد. ممنون بابت مشارکتِ تمیز — و اینکه اول CONTRIBUTING رو خوندی! — تو: راهنمای خوبیه! راستش بخشِ «PR کوچک» یه دورِ ریلویو رو از هر دومان گرفت.'),
      ('ex', 'You: If the docs rewrite sounds useful, I\'ll open an issue this weekend to scope it — no rush. — Maintainer: Yes please — docs contributions are our favorite kind of surprise.', 'تو: اگه بازنویسیِ داک به‌دردبخور به نظر میاد، آخرِ هفته برای تعیینِ دامنه‌ش issue می‌زنم — عجله‌ای نیست. — نگه‌دارنده: لطفاً — مشارکتِ داکی، محبوب‌ترین سورپرایزِ ماست.'),
    ]}],
  'tips': [
   ('CONTRIBUTING را قبل از کد بخوان', 'ده دقیقه آیین‌خوانی، یک هفته ریلویو می‌خرد — و جمله‌اش را در PR بگو؛ نگه‌دارنده می‌بیند و اعتماد می‌کند.'),
   ('first time contributing را سنجاق کن', 'اعلامِ تازگی + پرسیدنِ قرارداد — عذرخواهی نه، صادقانه‌کاریِ حرفه‌ای؛ لحنِ کلِ گفتگو را نرم می‌کند.'),
   ('داک، دروازهٔ مرج', 'اولین مشارکتِ جدی‌ات را داکی بگذار — سریع‌ترین مرج، بی‌ترین بحث، و اسمت در contributors.'),
  ]},
 'english-staff-interviews': {
  'grammar': ('گرامرِ عمیق‌تر: زبانِ «بسته به» و اثرِ سیستمی', [
    ('p', 'سطحِ staff، دو جمله‌ی نشانه‌دار دارد: **۱) بسته به + دو گزینه:** «Depends on the read/write ratio — if it\'s read-heavy, I\'d cache first; write-heavy, I\'d queue first» (به نسبتِ خواندن/نوشتن بستگی داره — خوانا-محور بود، اول کش؛ نوشتا-محور، اول صف) — dependsِ بدونِ گزینه، دوری است؛ dependsِ دوتایی، تحلیل. **۲) اثرِ سیستمی:** «The pattern generalized: we later used it for two more teams» (الگو قابلِ تعمیم بود — بعداً برایِ دو تیمِ دیگه هم استفاده شد) — هر داستانِ staff باید «تعمیم» را نشان دهد: از من، به سیستم؛ از یک تیم، به چند تیم.'),
    ('ex', 'Was it org-wide? Honestly, one team — but the pattern generalized: the staged-rollout checklist we wrote is now the default for three teams, and that\'s the part I\'d repeat anywhere.', 'سازمانی بود؟ راستش، یه تیم — ولی الگو قابلِ تعمیم بود: چک‌لیستِ عرضهٔ مرحله‌ای که نوشتیم الان پیش‌فرضِ سه تیمه، و همون قسمتیه که هر جا تکرارش می‌کنم.'),
  ]),
  'extra_sections': [
    {'h2': 'گفتگو: سوالِ فرضیِ فرایندی — «فرایندمانندِ محصول»', 'blocks': [
      ('ex', 'Interviewer: How would you improve our code review process? — You: First question back: what hurts most today — speed, quality, or tone? The fix is different for each.', 'مصاحبه‌گر: فرایندِ کدریویو ما رو چطور بهتر می‌کنی؟ — تو: اول یه سوالِ برگردان: امروز چی بیشتر اذیت می‌کنه — سرعت، کیفیت، یا لحن؟ درمانِ هر کدوم فرق داره.'),
      ('ex', 'Interviewer: Say speed — PRs sit for days. — You: My guess: they\'re too big. But I\'d confirm with data before changing anything — a two-sprint experiment: PR cap at 300 lines, measure merge time. If it moves, keep; if not, next hypothesis. Process is product.', 'مصاحبه‌گر: فرض کن سرعت — PRها روزها می‌شینن. — تو: حدسم: زیادی بزرگن. ولی قبل از هر تغییری با داده تأییدش می‌کنم — آزمایشِ دو-اسپرینته: سقفِ PR رویِ ۳۰۰ خط، اندازه‌گیریِ زمانِ مرج. جابه‌جا شد، نگه می‌داریم؛ نه، فرضیهٔ بعدی. فرایند، محصوله.'),
      ('ex', 'Interviewer: And if the data says size isn\'t the problem? — You: Then I was wrong cheaply — two sprints, not two quarters. That\'s the whole point of small experiments: wrong fast, right eventually.', 'مصاحبه‌گر: و اگه داده گفت اندازه مشکل نیست؟ — تو: اون‌وقت ارزون اشتباه کردم — دو اسپرینت، نه دو فصل. کلِ نکتهٔ آزمایشِ کوچیک همینه: سریع اشتباه، آخرش درست.'),
    ]}],
  'tips': [
   ('سوالِ برگردانِ سه‌گزینه', '«Speed, quality, or tone?» — در هر سوالِ فرضیِ فرایندی، اول پرسشِ شفاف‌ساز؛ فرایندِ فکر، امتیاز است نه جوابِ فوری.'),
   ('wrong cheaply را بفروش', '«اشتباهِ ارزون» — ارزان-آزمایش‌کردن، شعارِ سطحِ staff است؛ جمله‌اش را در سوالِ فرضی بکار.'),
   ('داستان‌ها را «تعمیم‌محور» کن', 'هر داستانِ رفتاری، یک جملهٔ «و الگو برایِ X هم رفت» بخواه — از تیم به سازمان، پلِ امتیازِ staff.'),
  ]},
 'english-continuous-learning': {
  'grammar': ('گرامرِ عمیق‌تر: زبانِ یادگیریِ پایدار — عادت و بازده', [
    ('p', 'یادگیریِ مستمر، سه جملهٔ ثابت دارد: **«I\'m working through…»** (دارم … رو می‌خونم/کار می‌کنم — کتاب/دوره), **«I picked up X from Y»** (X رو از Y برداشتم — یادگیریِ فرصت‌طلبانه!), **«It\'s starting to click»** (شروع شده جاافتادن — لحظهٔ اتصال!). و برای توصیفِ سطحِ خودت در مصاحبه: **«Conversational, not yet effortless»** (گفتاری، هنوز بی‌زحمت نه) — صداقتِ درجه‌دار، از بزرگ‌نمایی حرفه‌ای‌تر است. و برای خروجی: **«I\'m turning notes into a post»** (یادداشت‌هام رو دارم تبدیل می‌کنم به یه مطلب) — زبانِ تولید، پایانِ زبانِ مصرف است.'),
    ('ex', 'I\'m working through the data-engineering book — chapter a week. The consistency stuff finally clicked last night. I\'m turning my notes into a short post for the team channel — teaching it is how I check I really got it.', 'دارم کتابِ دیتا-انجینیرینگ رو می‌خونم — هفته‌ای یه فصل. بحثِ ثبات دیروز شب بالاخره جا افتاد. یادداشت‌هام رو می‌کنم یه پستِ کوتاه برای کانالِ تیم — تدریس‌کردنش روشِ منه که مطمئن شم واقعاً فهمیدمش.'),
  ]),
  'extra_sections': [
    {'h2': 'گفتگو: ورودی، خروجی و «یک جمله در روز»', 'blocks': [
      ('ex', 'Friend: What are you listening to these days? — You: A backend podcast on the commute — twenty minutes a day, no heroics. And one engineering newsletter with morning coffee.', 'دوست: این روزا چی گوش می‌دی؟ — تو: یه پادکستِ بک‌اند تو مسیر — بیست دقیقه در روز، بدونِ قهرمانی. و یکی خبرنامهٔ مهندسی با قهوهٔ صبح.'),
      ('ex', 'Friend: And it\'s working? — You: The daily sentence is my metric: yesterday I said «at the end of the day» correctly mid-meeting, unprompted. Last month I\'d have said… nothing, honestly.', 'دوست: و جواب می‌ده؟ — تو: متریکم «جملهٔ روز»ه: دیروز وسطِ جلسه، بی‌هیچ مقدمه، «at the end of the day» رو درست گفتم. ماه پیش، راستش، هیچی نمی‌گفتم.'),
      ('ex', 'Friend: Unprompted is the win. — You: That\'s the whole game — from thinking in Persian and translating, to thinking in English and just… speaking.', 'دوست: بی‌هیچ مقدمه، همون بردِ واقعیه. — تو: کلِ بازی همینه — از فکر-به-فارسی-و-ترجمه، به فکر-به-انگلیسی-و-ساده-گفتن.'),
    ]}],
  'tips': [
   ('معیارِ «یک جمله در روز»', 'هر شب یک جملهٔ واقعی پیدا کن که «امروز توانستی، ماه پیش نمی‌توانستی» — شمارشِ کوچک، سوختِ مسیرِ بلند.'),
   ('picked up را در معرفی بکار', '«I picked up Kubernetes from the migration, not a course» — یادگیریِ واقعیِ حرفه‌ای همین است؛ در مصاحبه بفروش.'),
   ('تدریس، آزمونِ فهم است', 'هر چیزی را که خواندی، در دو پاراگراف برای تیم بنویس — نوشتنِ ساده، تنها مدرکِ فهمِ واقعی است.'),
  ]},
 'english-final-roadmap': {
  'grammar': ('گرامرِ عمیق‌تر: زبانِ جمع‌بندیِ مسیر — گذشته تا آینده در یک پاراگراف', [
    ('p', 'درسِ آخر، زبانِ «روایتِ رشد» را می‌خواهد: **بازگشتِ کلّ مسیر در سه زمان:** «Ninety days ago I started with to be — today I ran a sprint review in English — next quarter I\'m going for the senior interview.» (نود روز پیش با to be شروع کردم — امروز جلسه‌ریویو رو به انگلیسی رفتم — فصلِ بعد می‌رم سراغِ مصاحبهٔ سنیور.) و جملهٔ بستنِ درس‌ها: **"That\'s the course — the rest is yours"** (دوره همین بود — بقیه مالِ خودته). برای هر بازگشت به این صفحه: جملهٔ ورودت آماده باشد: **"I\'m back for the review lesson — week four of my plan."**'),
    ('ex', 'Ninety days ago I couldn\'t order a coffee without rehearsing. Today I led a retro in English, joked in the standup, and wrote an RFC people actually read. The course is done. The habit — one day, one sentence — is just starting. That\'s the course; the rest is mine.', 'نود روزِ پیش نمی‌تونستم بدونِ تمرینِ قبلی قهوه سفارش بدم. امروز یه رترو رو به انگلیسی رفتم، تو استندآپ شوخی کردم، و RFCای نوشتم که آدم‌ها واقعاً خوندنش. دوره تموم شد. عادت — یه روز، یه جمله — تازه شروع شده. دوره همین بود؛ بقیه مالِ خودمه.'),
  ]),
  'extra_sections': [
    {'h2': 'گفتگو: درون‌گفتگوی پایانی — تو و نسخهٔ ۹۰روزِ پیشِ خودت', 'blocks': [
      ('ex', 'You (day 90): If I could tell day-one-me one thing? "You won\'t need perfect grammar. You\'ll need the sentence you\'re willing to say badly." — I said everything badly for a month. It worked.', 'تو (روزِ ۹۰): اگه بشه به روزِ-اولِ خودم یه چیز بگم؟ «به گرامرِ کامل نیاز نخواهی داشت. به جمله‌ای نیاز داری که حاضری بد بگیش.» — یه ماه همه‌چی رو بد گفتم. جواب داد.'),
      ('ex', 'You: The plan for the next ninety: week one — the full-English week, no Persian at work. Week two — mock interviews. Week three on — one RFC a month, one post a month, one stranger a month.', 'تو: نقشهٔ نودِ بعدی: هفتهٔ یک — هفتهٔ کاملِ انگلیسی، بدونِ فارسی سرِ کار. هفتهٔ دو — مصاحبه‌های تمرینی. از هفتهٔ سه — ماهی یک RFC، یک پست، یک غریبه.'),
      ('ex', 'You: And the last page of the notebook says it best: "Step ninety-one, tomorrow." — Onward.', 'تو: و آخرین صفحهٔ دفترچه بهتر از همه می‌گه: «قدمِ نودویکم، فردا.» — به راه.'),
    ]}],
  'tips': [
   ('پاراگرافِ سه‌زمانه‌ات را بنویس', 'نود روزِ پیش / امروز / فصلِ بعد — یک پاراگراف، روایتِ رشدت؛ در هر مصاحبهٔ بعدی، این پاراگراف جوابِ «tell me about yourself» توست.'),
   ('قدمِ ۹۱ را بلافاصله بردار', 'فردای درسِ ۹۰، اولین قدمِ نقشهٔ سال را اجرا کن — شتابِ پایان، سوختِ ادامه است.'),
   ('دوره را به کسی توصیه کن', 'توضیحِ درس‌ها به یک دوست، هم هدیه به اوست هم آزمونِ تو — آخرین تمرینِ دوره، تدریسِ آن است.'),
  ]},
}

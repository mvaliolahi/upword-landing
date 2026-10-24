# -*- coding: utf-8 -*-
"""Stage 1 · lessons 64-72 — فاز ۴ (بخش پایانی): ارائه، تخمین، مشتری و شبکه‌سازی."""

LESSONS = [
# ───────────────────────────── درس ۶۴ ─────────────────────────────
{
 'slug': 'english-demos-presentations',
 'title': 'دموی فنی و ارائه؛ «دو دقیقه، بدون اسلاید»',
 'desc': 'زبانِ دمو: باز کردنِ گرم (Today I\'ll show you…), روایتِ زندهٔ محصول (watch what happens when…), و بستنِ پیام‌دار (So what we learned is…). به‌علاوهٔ اجرای سوال‌های دمو و قلاب‌های مرگبارِ «این چرا کرش کرد؟».',
 'keywords': 'دمو انگلیسی, demo presentation, ارائه فنی, show and tell',
 'answer': 'دموی خوب سه دقیقه دارد: وعدهٔ شروع (Today I\'ll demo the new checkout — it takes two clicks now), روایتِ زنده (watch this — I click here, and it\'s done), و نتیجه (That\'s 40% fewer clicks). اگر دمو کرش کرد: "And this is why we demo before shipping — let me show the fallback." آرامشِ لحظهٔ خرابی، خودش قابلیتِ نمایشی است!',
 'intro': [
  'دمو (demo)، پرقدرت‌ترین ابزارِ ارتباطِ فنی است: هیچ اسلایدی مثل «کارکردنِ چیزِ واقعی» نمی‌فروشد. و در همان حال، پرخطرترین لحظهٔ زبانی توست: باید هم‌زمان کلیک کنی، روایت بدهی و جوابِ سوال‌های زنده بدهی. راه‌حلِ حرفه‌ای‌ها: روایتِ دمو را از قبل «نوشته و بلند تمرین» می‌کنند — متنِ دمو، مثل متنِ تئاتر است.',
  'این درس هم روایتِ زندهٔ دمو را می‌دهد و هم موقعیت‌های مرزی (کرش، سوالِ سخت، وقتِ کم) — همه با جمله‌های ثابت. sprint review، معرفیِ محصول به مدیران، و مصاحبه‌های «پروژه‌ام را نشان بده» از همین جا تغذیه می‌شوند.',
 ],
 'sections': [
  {'h2': 'باز و روایت؛ قالبِ نمایشِ زنده',
   'blocks': [
    ('ex', 'Hi everyone — two minutes of your time. Today I\'ll demo the new checkout flow: it\'s two clicks now, down from five.', 'سلام همه — دو دقیقه از وقتتون. امروز فلوِ جدیدِ تسویه رو دمو می‌کنم: الان دو کلیکه، از پنج کلیک کم شده.'),
    ('ex', 'Watch what happens when I hit "Pay": the spinner takes half a second, and we\'re done. That\'s the whole flow.', 'ببینید وقتی «پرداخت» رو می‌زنم چی می‌شه: نیم‌ثانیه لود می‌شه و تمام. کلِ فلوی کار همینه.'),
    ('p', 'جمله‌های روایتِ زنده — مولاژِ دمو: **مسیر:** "First, I\'ll open the app as a new user." **کانون:** "Keep an eye on the top bar — that\'s where the status lives." **تعلیق:** "And now for the interesting part…" **تأکید:** "Notice there\'s no page reload — it\'s all local state." (دقت کنی page reload نداریم — همه state محلیه.) — مخاطب را همیشه بگو کجا نگاه کند؛ دموی بی‌راهنمایِ نگاه، نصفش هدر است.'),
   ]},
  {'h2': 'خرابی و سوالِ زنده؛ صحنه‌های مرزی',
   'blocks': [
    ('p', '**دمو کرش کرد:** آرام بگو: "And… that\'s a bug. Good catch by the demo gods — let me show you what it should do." (و… این یه باگه. خدایانِ دمو شکارش کردن — بذار چیزی که باید اتفاق بیفته رو نشونتون بدم.) و بعد: "I\'ll file it right after this — that\'s exactly why we demo." هیچ‌وقت عذرخواهِ طولانی نشو؛ اعتمادِ مخاطب با آرامشِ تو برمی‌گردد نه با شرمِ تو. **سوالِ وسطِ دمو:** "Great question — let me park it and take it after the demo, so I don\'t lose the thread." (سوالِ خوبیه — کنارش می‌ذارم بعد از دمو جواب بدم که رشته‌ام گم نشه.) **وقتِ کم شد:** "We\'re at time — let me jump to the good part." — جملهٔ حرفه‌ایِ بی‌وحشتِ ساعت.'),
    ('ex', 'Everything you just saw is behind a feature flag — we can ship it dark and open it to 5% whenever we\'re ready.', 'همهٔ چیزی که دیدید پشتِ فیچر-فلگه — می‌تونیم تاریک شِپش کنیم و هر وقت خواستیم برای ۵٪ بازش کنیم.'),
   ]},
  {'h2': 'بستن و پیامِ دمو؛ سه جملهٔ آخر',
   'blocks': [
    ('p', 'بستنِ دمو با «معنا» نه «خلاصه»: **"So: two clicks, half the latency, and the error rate is under 0.1% in staging. We\'re ready for the next 5% rollout — I\'d love your go-no-go in the review."** (پس: دو کلیک، نصفِ تأخیر، خطای زیرِ ۰/۱٪. آمادهٔ بازکردنِ ۵٪ بعدی‌ایم — نظرتون رو در ریویو می‌خوام.) و جملهٔ جمعِ استوریِ زنجیره‌ایِ sprint reviewها: **"Last demo we showed the search; today the checkout — next sprint, the mobile flow closes the loop."** — دموی خوب، قسمتِ بعدیِ سریال را هم می‌فروشد.'),
   ]},
 ],
 'takeaway': 'دمو = وعدهٔ دو‌دقیقه‌ای + روایتِ راهنما (watch this / keep an eye on / notice) + مدیریتِ صحنه‌های مرزی (کرش: good catch by the demo gods; سوال: park it; وقت: jump to the good part) + بستنِ پیام‌دار با عدد و درخواستِ تصمیم. روایتِ دمو را بنویس، بلند تمرین کن، و پشتِ فلگ ایمنش کن — سه ضامنِ دموی خوابِ راحت.',
 'faq': [
  ('دموی آنلاین/ریموت چه فرقی دارد؟',
   'سه قانونِ ریموت: اشتراکِ صفحه را از قبل امتحان کن (و فقط پنجرهٔ لازم را share کن نه کلِ دسکتاپ!), صدا به اپ نه به سیستم (می‌کرُفونِ هدفون), و یک «شریکِ پشتیبان» داشته باش که اگر نت قطع شد، دمو را ادامه دهد: "If I drop, Sara will take over — Sara, you have the staging link." جملهٔ قطعِ وسطِ دمو: "Sorry, my connection hiccuped — where was I? Right, the payment step." — ریموت، اجرایِ آرامِ پیش‌بین می‌خواهد نه اجرایِ نابغه.'),
  ('دمو برای مدیرانِ غیرِفنی چطور؟',
   'همان درس ۵۳ (توضیح برای غیرِفنی) + قالبِ دمو: وعده را با «زندگیِ کاربر» باز کن نه با معماری: "This demo shows how our users will pay in two taps instead of five." عددِ کسب‌وکار بیاور (fewer taps = more completed orders) و از فنّ داخلی (feature flag, staging) فقط وقتی بگو که سوال شد. برای این مخاطب، «چه شد» مهم است نه «چطور ساختیم» — درس ۷۸ همین را به سطحِ اجرای سازمانی می‌برد.'),
 ],
},
# ───────────────────────────── درس ۶۵ ─────────────────────────────
{
 'slug': 'english-estimations-deadlines',
 'title': 'تخمین و ددلاین؛ «این چقدر طول می‌کشه؟» بدونِ دروغ و بدونِ جنگ',
 'desc': 'هنرِ گفتاریِ تخمین: three-point estimate, سقفِ شفاف (I\'d say three days, assuming the API is ready), گفتنِ «نه»ی حرفه‌ای به اسکوپِ اضافه, و مذاکرهٔ ددلاین با گزینه‌ها نه گلوله.',
 'keywords': 'تخمین زمان انگلیسی, estimation phrases, deadline negotiation, scope creep',
 'answer': 'سوالِ «چقدر طول می‌کشه؟» سه جوابِ حرفه‌ای دارد: بازه (two to three days), مفروضات (assuming the docs are ready), و گزینه‌های معاوضه (by Friday if we cut the export feature). فرمولِ گفتنِ «نه»: never بدونِ گزینه — "We can do that, if we push the migration to next sprint."',
 'intro': [
  'تخمین، جایی است که دو فرهنگ به هم می‌خورند: فرهنگِ «هرچیزی سریع انجام می‌شود» (فشارِ مدیر/بازار) و واقعیتِ مهندسی (کار، زمانِ خودش را می‌خواهد). برنامه‌نویسِ تازه‌وارد معمولاً یکی از دو خطا را می‌کند: زیرتخمین از خجالت، یا جوابِ «نمی‌دانم» خشک. مهندسِ حرفه‌ای هیچ‌کدام را نمی‌گوید — «بازه + مفروض + معاوضه» می‌گوید.',
  'این درس، جمله‌های تخمین را با منطقِ پشتشان می‌دهد؛ نیمهٔ دومِ درس، مدیریتِ همان تخمین در طولِ sprint است: اعلامِ زودهنگامِ خطر، که تفاوتِ «ددلاین سوخت» و «ددلاین جابه‌جا شد» است.',
 ],
 'sections': [
  {'h2': 'قالبِ تخمین؛ بازه + مفروض + معاوضه',
   'blocks': [
    ('ex', 'Ballpark: two to three days — assuming the payment API sandbox is ready and there are no surprises in the old data.', 'حدوداً دو-سه روز — با فرضِ اینکه سندباکسِ API پرداخت آماده باشه و توی دیتای قدیمی چیزی عجیب نباشه.'),
    ('ex', 'Realistically, that\'s a week of work. If you need it by Friday, we\'d have to cut the admin dashboard from this release.', 'واقع‌بینانه یه هفته کاره. اگه تا جمعه لازمش دارید، باید داشبوردِ ادمین رو از این ریلیز حذف کنیم.'),
    ('p', 'واژه‌های تخمین که باید راحت بگویی: **ballpark** (حدودِ کلی), **rough estimate** (تخمینِ خشن), **a couple of days** (دو-سه روز), **a week-ish** (یه هفته‌ی حدودی), **timebox** (سقفِ وقت: "Let\'s timebox it to two days and see how far we get"), **ideal vs elapsed time** (زمانِ خالصِ کار vs زمانِ تقویمی با جلسه‌ها). و سه‌نقطه‌ایِ کلاسیک: **"Best case two days, most likely three, worst case five if the vendor API misbehaves."** — همین یک جمله، تخمینِ حرفه‌ایِ کامل است.'),
    ('table', ['موقعیت', 'جوابِ حرفه‌ای'],
     [['سوالِ سریعِ راهرو', '"Ballpark, three days — let me sanity-check after standup."'],
      ['جلسهٔ planning', '"I\'d say five points. Unknown: the legacy schema — I\'ll spike it first."'],
      ['فشارِ مدیر برای تاریخِ زود', '"We can hit Friday if we drop the export. Otherwise Tuesday is realistic."'],
      ['کارِ واقعاً ناشناخته', '"I can\'t estimate blind — give me a half-day spike and I\'ll come back with a number."']]),
   ]},
  {'h2': 'نه گفتن به اسکوپ؛ هنرِ معاوضه',
   'blocks': [
    ('p', 'هر «بله» به کارِ جدید، یک «نه» به کارِ دیگری است — و جملهٔ حرفه‌ای همین را شفاف می‌کند: **"Sure, we can add batch import. That pushes the bugfix release by three days — which one wins?"** (می‌تونیم ایمپورتِ گروهی اضافه کنیم. این ریلیزِ فیکس‌ها رو سه روز عقب می‌ندازه — کدومش برنده باشه؟) قالب‌های معاوضه: **«…if we push X to next sprint»** · **«…if someone else takes the support tickets»** · **«…with a smaller first version — v1 without reports»**. و مخالفِ مقدس: قولِ «می‌سازمش خیلی سریع، شب کار می‌کشم» — زیرِ هر ددلاینِ جادویی، یک خطای تخمین است که بعداً صورت‌حساب می‌دهد؛ حرفه‌ای‌ها به‌جای شب‌کاریِ قهرمانانه، معاوضهٔ شفاف می‌دهند.'),
   ]},
  {'h2': 'مدیریتِ تخمین؛ اعلامِ خطرِ زودهنگام',
   'blocks': [
    ('p', 'تخمین، تازه آغازِ ماجراست؛ پایانِ حرفه‌ای‌اش، اعلامِ به‌موقعِ انحراف است — **نه در ضرب‌الاجل، در اولین نشانه**: **"Heads-up: the migration is slower than estimated. I\'m 60% through — realistically I need one more day. Do we push the demo or cut the scope?"** (خبر: مایگریشن از تخمین کندتره. ۶۰٪ جلو اومدم — واقعاً یه روز دیگه می‌خوام. دمو رو عقب بندازیم یا اسکوپ رو کم؟) سه واژهٔ نجاتِ این مکالمه: **heads-up** (هشدارِ مؤدبانه), **at risk** (در خطر: "The release is at risk"), **slip** (جابه‌جا شدن: "The date might slip by a day"). و قانونِ فرهنگِ سالم: خبرِ بدِ زودهنگام، امتیاز است؛ خبرِ بدِ آخرین لحظه، شکستِ مشترک.'),
    ('ex', 'The ticket looked like a two, it\'s behaving like an eight. I\'ve split out the scraping part — new estimate: two days for the core, one for scraping.', 'تیکت دوتایی به نظر می‌رسید، هشتایی رفت. بخشِ اسکرپ رو جدا کردم — تخمینِ جدید: دو روز برای هسته، یک روز برای اسکرپ.'),
   ]},
 ],
 'takeaway': 'تخمین = بازه (two to three days) + مفروض (assuming…) + معاوضه (if we cut X). واژه‌ها: ballpark, timebox, at risk, slip, spike. هر بلهِ جدید را با «کدوم می‌بره؟» بپیچ و انحراف را با heads-up در اولین نشانه اعلام کن. حرفه‌ای‌ها قولِ شب‌کاری نمی‌دهند؛ گزینه می‌دهند.',
 'faq': [
  ('مدیر عدد را «بالا» می‌داند و پایین می‌کِشد!',
   'سه حرکت: ۱) عدد را با تجزیه بفروش: "Two days isn\'t a feeling — one for the API, one for the UI and tests. Where would you cut?" (دو روز حس نیست — یکی برای API یکی برای UI و تست. کجاش رو کم کنیم؟) ۲) تاریخِ جایگزینِ صادقانه بده: "If it must be Thursday, I\'d rather ship without the export." ۳) اگر باز پایین کشید، سوابق را داوطلبانه ثبت کن: "Let\'s log this estimate — I\'ll report the actuals in retro so we both calibrate." — این جمله، گفتگو را از چانه‌زنی به داده می‌برد؛ و بعد از دو-سه retro، عددِ تو با احترام خوانده می‌شود.'),
  ('تخمینم همیشه کم است — چطور اصلاح کنم؟',
   'سه ضربِدرِ دو قانونِ شناخته‌شده: تخمینِ اولت را **دو برابر** کن (کارِ واقعی همیشه «یک چیزِ دیگر» هم دارد), بعد **ضریبِ تقویم** (جلسه‌ها، context switch): سه روزِ کاریِ خالص = چهار-پنج روزِ واقعی. و تمرینِ data-driven: دو هفته، تخمین و واقعیتت را کنارِ هم بنویس؛ ضریبِ شخصیِ تو (مثلاً «من همیشه ۱/۷ برابر تخمینم طول می‌کشم») را پیدا کن و در planning همان را اعلام کن: "My historical factor is about 1.7 — so I\'m putting five days." — مهندسِ آماریِ تخمین، موردِ احترامِ همهٔ مدیرهاست.'),
 ],
},
# ───────────────────────────── درس ۶۶ ─────────────────────────────
{
 'slug': 'english-product-client-talks',
 'title': 'گفتگو با محصول و مشتری؛ ترجمهٔ فنی و «چرا نه»ی مشتری‌پسند',
 'desc': 'پلِ فنی-غیرِفنی: ترجمهٔ محدودیت‌ها برای PM (this isn\'t a toggle, it\'s a schema change), گفتنِ «نه» با گزینه (not now, here is the cheap version), و جلسهٔ requirement که سوال‌های درستش را تو بایستی بپرسی.',
 'keywords': 'گفتگو با مدیر محصول, client communication, ترجمه فنی, requirements meeting',
 'answer': 'با محصول و مشتری، تو «مترجمِ دواژه» هستی: زبانِ فنی را به اثر (impact) و زبانِ خواسته را به پیچیدگی. سه جملهٔ پل: "What problem are we solving for the user?", "That\'s a week because it touches the database schema", و "We can\'t do all three by Friday — which one buys us the most?"',
 'intro': [
  'مرزِ فنی-محصول، جایی است که بیشترِ سوءتفاهم‌های کاری زاده می‌شوند: PM می‌گوید «فقط یه سوییچ اضافه کن»، تو می‌بینی schema را عوض می‌کند; تو می‌گویی «تکنیکال دِبت زیاده»، PM می‌شنود «نمی‌خواهد کار کند». حرفه‌ای‌ها این مرز را با «ترجمهٔ دوگانه» اداره می‌کنند — و این درس، جعبه‌ابزارِ ترجمه است.',
  'برای مشتریِ خارجی، همان قواعد با لحنِ سرویس‌مندتر: تو نمایندهٔ اعتمادِ فنیِ شرکت هستی. درس ۷۸ ارائه برای مدیران را تکمیل می‌کند؛ اینجا پایه‌ی گفتگوی دوطرفه است.',
 ],
 'sections': [
  {'h2': 'ترجمهٔ فنی به اثر؛ زبانِ آینه‌ای',
   'blocks': [
    ('p', 'هر محدودیتِ فنی را با «اثرِ روی کاربر/کسب‌وکار» بگو، نه با نامِ فناوری: **نهِ** "That requires a schema migration" — که **"That means the whole checkout slows down for a week while data moves — unless we do it gradually. The gradual path takes three weeks but users never notice."** (یعنی یه هفته تسویه کند می‌شه تا داده جابه‌جا شه — مگر کم‌کم انجامش بدیم. مسیرِ کم‌کش سه هفته‌ست اما کاربر هیچ‌وقت نمی‌فهمه.) واژه‌های اثر: **slows down / breaks / risks / invisible to users / buys us speed later** — PM با این‌ها تصمیم می‌گیرد؛ با "schema" نه.'),
    ('ex', 'Quick reality check: this "tiny toggle" actually touches the database. Cheaper version: a setting for new users only — old users keep the current behavior. Deal?', 'یه واقعیت‌چکِ سریع: این «سوییچِ کوچیک» واقعاً دیتابیس رو درگیر می‌کنه. نسخهٔ ارزون‌تر: تنظیمِ فقط برای کاربرهای جدید — قدیمی‌ها همین‌طور بمونن. اوکیه؟'),
   ]},
  {'h2': 'نه گفتن با گزینه؛ هنرِ PM-پسند',
   'blocks': [
    ('p', 'سه قالبِ «نه»ی مشتری/PM-پسند: **۱) نه الآن + دلیلِ درستِ زمانی:** "Not in this release — the payment rewrite is touching the same code, and doing both at once doubles the risk." **۲) بله با نسخهٔ کوچک:** "We can\'t do the full dashboard by Friday, but I can ship read-only charts Monday — full version two weeks later." **۳) بله با معاوضهٔ صریح:** "Sure — that becomes the priority. Which of these three should I drop?" — هر سه قالب، پیامِ پنهانی دارند: «من به تو کمک می‌کنم بُبر، نه این‌که چانه بزنم». و سوالِ معروفِ هر requirement: **"What problem is this solving for the user? There might be a cheaper way to the same outcome."** — پرسیدنِ «چه مسئله‌ای؟» محترمانه‌ترین کوتاه‌کردنِ راه است.'),
   ]},
  {'h2': 'جلسهٔ requirements؛ سوال‌هایی که تو باید بپرسی',
   'blocks': [
    ('p', 'پنج سوالِ استانداردِ شروعِ هر فیچر: **۱)** "Who is this for — new users, power users, internal?" **۲)** "What does success look like — what number moves?" **۳)** "What\'s the deadline driving this — a launch, a contract, a promise?" **۴)** "What\'s explicitly out of scope?" **۵)** "Is there an example of how you imagine it working?" و در جلسهٔ مشتری: زبانِ سرویس: **"Absolutely — let me make sure I understand the requirement correctly…"** (بازگویی قبل از تعهد!) و بستن: **"I\'ll summarize this in writing today — corrections welcome before I start."** — خلاصهٔ مکتوبِ همان روز، بیمهٔ سوءتفاهم است؛ جمله‌اش فقط یک ایمیلِ پنج‌خطی دارد.'),
   ]},
 ],
 'takeaway': 'تو مترجمِ دوزبانهٔ فنی-محصولی: فنی را به اثر برگردان (slows down / risks / invisible to users) و خواسته را به سوالِ مسئله (What problem are we solving?). «نه» را با گزینه بگو: not now + دلیل، نسخهٔ کوچک، یا معاوضه. هر فیچر را با پنج سوالِ requirement باز کن و جمع‌بندیِ مکتوبِ همان روز بفرست — بیمهٔ سوءتفاهم.',
 'faq': [
  ('«مشتری اشتباه فنی می‌خواهد — جوابش را چی بدهم؟',
   'هرگز «غلطه» تنها نه — سوالِ هدف بپرس و بدیلِ فنی بده: **"Just so I build the right thing — is the goal to stop duplicate orders? Then instead of manual approve/reject, I can add idempotency keys: same outcome, zero extra clicks for your team."** (هدف جلوگیری از سفارشِ تکراریه؟ پس به‌جای تأییدِ دستی، کلیدِ idempotency می‌ذارم: همون نتیجه، بدونِ کلیکِ اضافه.) مشتری «راه‌حلِ درست» را نمی‌خواهد؛ «نتیجهٔ درست» را می‌خواهد — و تو حرفه‌ات تبدیلِ راه‌حلِ درست به نتیجهٔ درست است.'),
  ('PM-ام فنی را نمی‌فهمد و همیشه عجله دارد!',
   'سه ترفندِ سازگاری: ۱) عدد را به «تجربه» ترجمه کن: نهِ «دیگ‌ریشن ۴۸ ساعته» — که «کاربرها پنجشنبه صبح لاگین نمی‌تونن». ۲) انتخاب را سه‌گانه بده نه دو قطبی: سریع/کامل/ایمن — «یکی رو انتخاب کن». ۳) سابقه بساز: هر بار که «پیچیده بود و من گفتم و درست از آب دراومد» را در داک نگه دار — بعد از دومین بار، تخمینت دیگر بحث نمی‌شود؛ اعتماد، داده می‌خواهد و تو داری می‌سازیش.'),
 ],
},
# ───────────────────────────── درس ۶۷ ─────────────────────────────
{
 'slug': 'english-one-on-ones-feedback',
 'title': 'جلسهٔ 1:1 و بازخورد؛ دو گفتگوی مسیرِ حرفه‌ای',
 'desc': 'قالب‌های جلسهٔ یک‌به‌یک با مدیر: agenda خودت, سوال‌های رشد (What should I improve?), و گفتنِ نارضایتیِ حرفه‌ای. به‌علاوهٔ گرفتنِ بازخوردِ سخت و پیگیریِ آن — گفتگوهایی که مسیرِ تو را تعریف می‌کنند.',
 'keywords': 'جلسه یک به یک, one on one questions, بازخورد کاری, asking for feedback',
 'answer': 'جلسهٔ 1:1 مالِ توست نه مدیر: agenda خودت را بیاور (two things I want to discuss), سه سوالِ همیشگیِ رشد بپرس, و بازخورد بخواه که قابل‌اجرا باشد (What is one thing I should do differently?). نارضایتی را با فرمولِ «مشاهده + اثر + درخواست» بگو — ۱:1 جای گفتنِ حرف‌های نیمه‌گفته است.',
 'intro': [
  'جلسهٔ 1:1 (هر هفته یا دو هفته، ۳۰ دقیقه با مدیرت)، تنها جلسهٔ تقویم است که دستورِ روزِ آن «تو» هستی — و بیشترین بازدهی حرفه‌ای را دارد اگر صاحبش شوی. برای تازه‌واردِ غیرِبومی، دو چالش: سکوتِ «همه‌چیز خوبه» و ناتوانی از گفتنِ نارضایتی. این درس هر دو را قالب می‌کند.',
  'نیمهٔ دومِ درس، سویِ دیگرِ سکه است: گرفتنِ بازخورد — که در فرهنگِ انگلیسی‌زبانِ سالم، کسی که بازخورد نمی‌گیرد، «جای خودش را در رشدش خالی» گذاشته. جمله‌های درخواست و هضمِ بازخورد، مهارتِ مادام‌العمرِ فاز ۵ هم هستند.',
 ],
 'sections': [
  {'h2': 'مالکیتِ جلسه؛ agenda و سه سوال',
   'blocks': [
    ('ex', 'I put a quick agenda in our doc: first, an update on my ramp-up; second, I\'d love your read on the API project — am I going deep enough?', 'یه议程ِ سریع تو داکِ جلسه گذاشتم: اول آپدیتِ جاافتادنم؛ دوم نظرت رو دربارهٔ پروژهٔ API می‌خوام — به‌اندازهٔ کافی عمیق می‌رم؟'),
    ('p', 'سه سوالِ همیشگیِ رشد — هر 1:1 یکی‌شان را بپرس: **۱)** "What\'s one thing I did well this week that I should keep doing?" (چه چیزیش رو این هفته خوب انجام دادم که ادامه بدم؟) **۲)** "What\'s one thing I should do differently — not more, differently?" (یه چیز رو «متفاوت» بکنم — نه بیشتر؟) **۳)** "Where do you see me in six months? What\'s the gap between here and there?" (شیش ماه دیگه منو کجا می‌بینی؟ فاصله تا اون‌جا چیه؟) — و در ماه‌های اولِ کار: **"Am I where you expected me to be at this point? Be honest — I\'d rather know early."** (اون‌جایی هستی که انتظار داشتی باشم؟ صادق باش، دوست دارم زود بدونم.)'),
   ]},
  {'h2': 'گفتنِ نارضایتی؛ فرمولِ سه‌تکه',
   'blocks': [
    ('p', 'فرمولِ «مشاهده + اثر + درخواست»: **"Lately I\'ve been pulled into three different projects (observation). I\'m context-switching so much that everything is slower (impact). Could we pick my top priority for the next month, so I can push back on the rest? (request)"** — بدونِ اتهام، بدونِ هیجان، با مسیرِ حل. نسخه‌های دیگر: نارضایتی از تخمین‌ها: **"Estimates keep getting cut in planning, and then we miss the cut dates. Could we try logging estimates vs actuals for one sprint?"** و سوالِ مسیرِ حقوق/ارتقا (فاز ۵ کامل می‌شود): **"I\'d like to understand the path to the next level — what would \'yes\' look like in the next review cycle?"**'),
    ('ex', 'Can I share something that\'s been bothering me? It\'s not a complaint — I want to fix it early.', 'می‌تونم یه چیزی بگم که ذهنم رو درگیر کرده؟ شکایت نیست — می‌خوام زود درستش کنیم.'),
   ]},
  {'h2': 'گرفتنِ بازخورد؛ سخت را شیرین کن',
   'blocks': [
    ('p', 'سه قدمِ حرفه‌ایِ هضمِ بازخورد: **۱) بازخوریِ فعال:** "So the main theme is: I should communicate earlier when things slip — did I get that right?" (پس مضمون اینه که زودتر خبر بدم وقتی کار عقب میفته — درست گرفتم؟) **۲) جداسازی:** خودت را از کار جدا کن — جملهٔ یادگاری: **"That\'s hard to hear, and it\'s useful. Let me sit with it and come back with a plan."** (شنیدنش سخت‌ه اما به‌دردبخوره. بذار هضمش کنم با یه برنامه برگردم.) **۳) پیگیریِ مکتوب:** یک هفته بعد: **"Last time you flagged my updates were too sparse. I\'ve started posting Friday recaps — did the last one land better?"** — همین جریانِ «گرفتن-بازگویی-اقدام-پیگیری»، تو را در نگاهِ مدیر از «جونیورِ خوش‌برخورد» به «مهندسِ در حالِ رشدِ سریع» می‌برد — و هیچ‌کدامش جمله‌های پیچیده‌ای نمی‌خواهد.'),
   ]},
 ],
 'takeaway': '1:1 مالِ توست: agenda بیاور، سه سوالِ رشد را چرخش بپرس (keep doing / differently / six-month gap), و نارضایتی را با «مشاهده+اثر+درخواست» بگو. بازخورد را با بازگویی هضم کن، خودت را از کار جدا کن، و با پیگیریِ مکتوب حلقه را ببند. این سی دقیقهٔ هفتگی، طولانی‌ترین تصمیمِ حرفه‌ایِ سالِ تو را می‌سازد.',
 'faq': [
  ('مدیرم 1:1 را لغو می‌کند و همیشه «مشغول» است!',
   'دو حرکت: ۱) درخواستِ فرمتِ جایگزین: **"I know Thursdays are packed — would a written update every Friday plus 15 minutes biweekly work? I\'ll bring the agenda."** (جمع‌بندیِ مکتopicنی‌شهای جمعه + ۱۵ دقیقهٔ دوهفته‌ای؟ agenda رو من میارم.) ۲) اهمیت را برایش ترجمه کن: **"These 30 minutes save us hours of misalignment later — that\'s the ROI."** مدیرِ فراری معمولاً از 1:1های بی‌دستور می‌فرسد؛ دیرِ درسِ این — agenda — خودش نصفِ مشکل را حل می‌کند. اگر باز لغو شد، به بالادستِ منابع (skip-level) درست نگاه کن: درس ۸۱ برمی‌گردد.'),
  ('«Skip-level» چیست؟ با مدیرِ مدیرم هم حرف بزنم؟',
   'بله — در شرکت‌های سالم حتی تشویق می‌شود: سه‌ماهه یک بار، ۱:1 کوتاه با مدیرِ بالادست. سه سوالِ امنِ این جلسه: **"What does the org need from my team this year?"** · **"How is my manager doing — anything I can do to make their job easier?"** (بله، این سوالِ وفاداریِ سالم است!) · **"What would make me a strong candidate for the next level?"** — skip-level، هم رؤیت می‌دهد هم حمایت؛ اما قاعدهٔ طلایی: هرگز جای شکایت از مدیرت نیست — مدیرِ خوب خودش جلسه را پیشنهاد می‌کند.'),
 ],
},
# ───────────────────────────── درس ۶۸ ─────────────────────────────
{
 'slug': 'english-disagreeing-technically',
 'title': 'مخالفتِ فنی؛ جنگِ ایده‌ها بدونِ جنگِ آدم‌ها',
 'desc': 'پیشرفتِ درس ۴۴ برای میدانِ فنی: قالب‌های قویِ چالش (I\'m not convinced — can we look at the data?), disagree and commit, و بحث‌های معماری که حلقه‌شان با تصمیمِ مستند بسته می‌شود.',
 'keywords': 'مخالفت فنی, disagreeing at work, architectural debate, disagree and commit',
 'answer': 'در بحثِ فنی، مخالفتِ محترمانه = داده + گزینه + تعهد: "I\'m not convinced — what if we measured it first?" و بعدِ تصمیم: "I\'ll fully back the chosen path — and I\'ll document my concern so we can revisit it with data." بحثِ سالم را با «قابلِ فسخ بودنِ تصمیم» ببند: "Let\'s revisit in three months with real numbers."',
 'intro': [
  'بحث‌های فنی (فریم‌ورک، معماری، نام‌گذاری!) از گرم‌ترین لحظه‌های تیم‌اند — و از خطرناک‌ترین لحظه‌های زبانیِ تازه‌وارد: یا ساکت می‌مانی و «موافق» به نظر می‌رسی، یا لحنت را گم می‌کنی و «تند» به نظر می‌رسی. هیچ‌کدام لازم نیست: مخالفتِ حرفه‌ای، قالبِ مشخص دارد و در فرهنگِ تیم‌های خوب، actively تشویق می‌شود.',
  'این درس، چهار قالبِ مخالفتِ فنی + آیینِ بستنِ بحث را می‌دهد. درس ۴۴ قواعدِ عمومیِ مخالفت را ساخت؛ اینجا همان پل‌ها در ارتفاعِ فنیِ بالا طی می‌شوند — جایی که یک مخالفتِ خوب، سال‌ها هزینه را صرفه‌جویی می‌کند.',
 ],
 'sections': [
  {'h2': 'چهار قالبِ چالش؛ از نرم تا قوی',
   'blocks': [
    ('table', ['شدت', 'قالب', 'کی'],
     [['نرم', 'Have we considered…?', 'گزینه‌ای که شاید دیده نشده'],
      ['نرم', 'I wonder if… might bite us later.', 'ریسکِ آینده را روشن کن'],
      ['متوسط', 'I\'m not convinced this handles X — can we check?', 'شکِ مشخص با آزمون'],
      ['متوسط', 'My experience has been the opposite — in [مثال].', 'تجربه + شاهد'],
      ['قوی', 'I disagree with this approach — here\'s why: …', 'مخالفتِ صریحِ مستدل'],
      ['قوی', 'I\'d like to flag a real risk before we commit.', 'هشدارِ پیش از تعهد']]),
    ('p', 'نکتهٔ ساختاریِ هر چهار قالب: **همیشه «چیزی» بعد از مخالفت می‌آید** — گزینه، ریسک، آزمون یا مثال. «I disagree» تنها، در فرهنگِ فنیِ این‌ها فقط عصبانیت است؛ «I disagree — because»، نظرِ فنی است. و قوی‌ترین کارتِ زبانِ دوم: **آهسته‌تر و شفاع‌ بگو** — مخالفتِ آرام و مشخص، در شنیدارِ انگلیسی‌زبان، جدی‌تر از مخالفتِ تندِ شتاب‌زده است.'),
    ('ex', 'I\'m not convinced the queue is worth it — we\'d add a moving part for maybe 50 requests a second. Can we measure the actual load first?', 'مطمئن نیستم صف ارزشش رو داشته باشه — یه قطعهٔ متحرک اضافه می‌کنیم برای شاید ۵۰ درخواست در ثانیه. اول لودِ واقعی رو اندازه بگیریم؟'),
   ]},
  {'h2': 'بحث را جلو ببر؛ ابزارهای ساختار',
   'blocks': [
    ('p', 'سه ابزارِ حلِ بن‌بستِ بحث: **۱) آزمونِ کوچک:** "We\'re going in circles — how about a two-day spike on both options and decide with numbers?" (دو روز اسپایک روی هر دو گزینه و با عدد تصمیم؟) **۲) مرجعِ عادل:** "Let\'s ask the platform team — they\'ve run both at scale." **۳) زمان‌سنجِ تصمیم:** "Let\'s timebox this debate to today, then whoever owns the call makes it — and we all commit." — جملهٔ آخر، مالکیتِ تصمیم را روشن می‌کند: بحثِ بی‌مالک، بی‌پایان است. و پیشنهادِ بستنِ ماندگار: **"Let\'s write this up as an ADR either way — so future-us knows why."** (درس ۵۹ یادت هست — ADR همان صلح‌نامهٔ بحث‌های فنی است.)'),
   ]},
  {'h2': 'بعد از تصمیم؛ disagree and commit در عمل',
   'blocks': [
    ('p', 'وقتی جمع خلافِ نظرِ تو تصمیم گرفت، سه جملهٔ تعهدِ حرفه‌ای: **"Alright — the data was thin either way. I\'m in."** (خب — داده هر دو طرف ناکافی بود. من هستم.) · **"I\'ll document my concern in the ADR, and if the p99 doubles in three months, we revisit."** (نگرانی‌ام رو تو ADR می‌نویسم و اگه سه ماه دیگه p99 دو برابر شد، دوباره بررسی می‌کنیم.) · **"For the record: I lost this one happily. Let\'s make it succeed."** — و بدیهی‌ترین اما نادرترین رفتار: بعد از جلسه، در پیاده‌سازی تمام‌قد بجنبی. نصف-اجرا کردنِ تصمیمی که با آن مخالف بودی، سریع‌ترین راهِ سوزاندنِ اعتبارِ توست — برعکسش: تعهدِ کاملِ شفاف، اعتمادِ «مخالفتِ بعدی‌ات را جدی می‌گیرند» می‌سازد.'),
    ('ex', 'I still think the cron approach was the better bet — but the decision\'s made, and I\'m going to make it work beautifully.', 'هنوز فکر می‌کنم مسیرِ کرون انتخابِ بهتری بود — ولی تصمیم گرفته شده و من کاری می‌کنم بی‌نقص کار کنه.'),
   ]},
 ],
 'takeaway': 'مخالفتِ فنی = قالبِ چهارشدتی + همیشه «چیزی» بعد از آن (گزینه/ریسک/آزمون/مثال). بن‌بست را با ابزار حل کن: spike دو-روزه، مرجعِ عادل، مالکِ مشخصِ تصمیم — و بستنِ ADR. بعد از تصمیم: مستند کن نگرانی را، تعهد کن اجرا را، و سه ماه بعد با داده برگرد. مخالفتِ محترمانه، ارزان‌ترین بیمهٔ کیفیتِ تیم است.',
 'faq': [
  ('همکارم لحن بحث را تند می‌کند؛ من آرام بمانم یا جواب بدهم؟',
   'آرام بمان — و لحن را «بازیابی» کن: **"I think we actually agree on the goal — let\'s separate the person from the approach for a sec."** (فکر کنم رویِ هدف موافقیم — یه لحظه آدم رو از روش جدا کنیم.) یا با ابزارِ ساختار: "Let\'s write both options down and compare side by side." — نوشتن، هم اتوکشیسیونِ سرد می‌کند هم بحث را قابلِ داوری. اگر لحنِ تند الگوی دائمی و شخصی شد، مکالمهٔ خصوصیِ صادق (درس ۵۶) و اگر ادامه کرد، سراغِ مدیر — اما در خودِ بحثِ فنی، آرامشِ تو سلاحِ توست، نه ضعف.'),
  ('مخالفتم «از جنس سلیقه» است — بگویم یا نگه دارم؟',
   'قاعدهٔ سه‌پرسشیِ سلیقه: هزینهٔ تصمیم چقدر است؟ برگشت‌پذیر است؟ داده‌ای می‌تواندش عوض کند؟ اگر جواب‌ها «کم/بله/نه» — سلیقه‌ات را یک بار بگو (نقطه‌ات ثبت شود) و بعد تمام‌قد به انتخابِ جمع. جمله‌اش: **"Pure taste call, but I\'d name it `buildProfile`. Your call — and I\'m fine either way."** سلیقه‌ی ابرازشدهٔ آمرزیده، اعتبارِ مخالفت‌های بزرگِ بعدی‌ات را بالا می‌برد: تو «مخالفِ همیشگی» نیستی، «بازبینِ هدفمند» هستی.'),
 ],
},
# ───────────────────────────── درس ۶۹ ─────────────────────────────
{
 'slug': 'english-joining-new-team',
 'title': 'ورود به تیمِ جدید؛ سه ماهِ اول در سه گفتگو',
 'desc': 'چارچوبِ ادغامِ حرفه‌ای: ماهِ اول (سوال و سیا learning), ماهِ دوم (اولین بردِ مستقل), ماهِ سوم (بردِ دومی + قلمرو). با جمله‌های asking for context و «قانونِ دو هفتهٔ جونیورها».',
 'keywords': 'ورود به تیم جدید, joining new team, اولین ماه کاری, ramp up',
 'answer': 'سه ماهِ اولِ هر تیمی سه مأموریت دارد: ماهِ اول — بپرس و یادداشت (Where does the code lie? Who owns what?); ماهِ دوم — اولین بردِ مستقل (first win); ماهِ سوم — بردِ بزرگ‌تر + قلمروی مشخص. جملهٔ طلاییِ ادغام: "Can you walk me through how this works? I\'m still building the map."',
 'intro': [
  'ورود به تیمِ جدید — شرکتِ جدید یا فقط تیمِ داخلی — مسیرِ حرفه‌ای هر مهندس را دوباره می‌سازد: ناشناخته‌ها زیاد است و اعتبار، صفر. اما ادغام، بازیِ طراحی‌شده است: تیم‌های سالم برای همین «ramp-up» دارند و جمله‌های درست، ماه‌های اول را از «سرگردانیِ مؤدبانه» به «جذبِ سریع» تبدیل می‌کند.',
  'این درس، نقشهٔ سه‌ماهه با جمله‌های هر مرحله را می‌دهد. اگر تازه‌واردِ کاری هم هستی، این درس روی درس ۴۸ (روزِ اول) سوار می‌شود؛ اگر باتجربه‌ای و فقط تیم عوض می‌کنی، همین درس به‌تنهایی نقشهٔ توست.',
 ],
 'sections': [
  {'h2': 'ماهِ اول؛ نقشه را بکش، سوال را بلند بپرس',
   'blocks': [
    ('p', 'چهار سوالِ نقشه‌کشِ هفتهٔ اول — از پنج نفرِ مختلف بپرس (جواب‌ها کنارِ هم می‌سازندِ نقشه): **"How does the system work end to end — can you draw it for me?"** · **"Where\'s the dangerous code — the part everyone touches carefully?"** (کدِ خطرناک کجاست؟) · **"What do people here value in code review?"** · **"What\'s the team\'s definition of done?"** و آیینِ شخصیِ ثبت: **دفترِ ادغام** — هر توضیحِ جدید را با یک جمله و یک نمودارِ کوچک بنویس؛ این دفتر، سه ماه بعد، «سندِ تو» می‌شود و حتی به مستنداتِ تیم هدیه می‌دهی. جملهٔ جاافتادگیِ محترمانه: **"Sorry if this is a basic question — I\'m still building the map."** (ببخشید اگه سوالِ پایه‌ایه — هنوز دارم نقشه رو می‌سازم.)'),
    ('ex', 'Could you walk me through the auth flow? I\'ll take notes — happy to turn them into a doc for the next new hire.', 'می‌شه فلوِ احراز رو برام بگی؟ یادداشت می‌کنم — خوشحال می‌شم تبدیلش کنم به یه داکه برای نفرِ بعدی.'),
   ]},
  {'h2': 'ماهِ دوم؛ اولین بردِ مستقل',
   'blocks': [
    ('p', 'اولین برد (first win) را عمداً کوچک و مشهود انتخاب کن: باگی که همه آزارش می‌دهند، داکِ ناقصی که همه ازش گله دارند، اسکریپتی که کارِ تکراری را می‌کُشد. جمله‌ی درخواستش در planning: **"I\'d like to take the docs cleanup — I\'ve been taking notes anyway, and it\'s my way of giving back early."** (داک‌ها رو مرتب می‌کنم — به‌هرحال یادداشت داشتم؛ این روشِ زودبازده‌ستِ من.) و بعد از تحویل، بازخوردِ مقدماتی بخواه (درس ۶۷): **"That was my first solo slice here — one thing I should keep doing, one thing to change?"** — اولین برد + بازخوردِ سریع، معادلِ سه ماهِ اعتبار است.'),
   ]},
  {'h2': 'ماهِ سوم؛ قلمرو و بردِ بزرگ',
   'blocks': [
    ('p', 'از ماهِ سوم، از «کسی که یاد می‌گیرد» به «کسی که قلمرو دارد» حرکت کن: **"I\'ve noticed I keep ending up in the payments code — I\'d love to own the retries part, if the team\'s okay with it."** (دقت کردم مدام سراغِ کدِ پرداخت می‌رم — دوست دارم مالکِ بخشِ retryها باشم، اگه تیم اوکیه.) و در 1:1: **"For the next quarter, I\'d like my name next to something — which area needs an owner?"** جمله‌ی جمع‌بندیِ سه‌ماهه با مدیر: **"Ninety days in: I\'ve shipped X, own Y, and my open question is Z. How does that match your expectations?"** — این جلسه، چراغِ سبزِ رسمیِ «ادغامِ کامل» است؛ صدقانه‌اش را بخواه، حتی اگر جوابش تند باشد: **"Tell me the version you\'d say if I weren\'t in the room."** (اون نسخه‌ای رو بگو که اگه من نبودم می‌گفتی!)'),
   ]},
 ],
 'takeaway': 'سه ماهِ ادغام: ماهِ ۱ — نقشه با چهار سوالِ تکراری + دفترِ یادداشت («still building the map»); ماهِ ۲ — اولین بردِ کوچکِ مشهود + بازخوردِ مقدماتی; ماهِ ۳ — قلمروی اعلام‌شده + جلسهٔ ۹۰روزه. سوالِ «basic» با عذرخواهیِ قالبی، در هر تیمی عادی است — سکوتِ شش‌ماهه نیست.',
 'faq': [
  ('تیمِ جدیدم فنی‌تر از سطحِ من است — کم می‌آورم؟',
   'احساسِ « everybody smarter than me» در ماهِ اول، تقریباً قانونِ طبیعتِ تیمِ خوب است. دو ترفندِ ذهنی: ۱) مقایس را با «خودِ سه‌ماههٔ قبلِ خودت» کن، نه با «ده‌سالهٔ همکارت». ۲) سهمِ تو در این مرحله «چشمِ تازه + سوالِ بی‌خجالت» است — هر دو، خودش‌ها دارایی‌اند. و صداقتِ مفید: **"This stack is new to me — I\'ll ramp slower than usual, but I\'ve done this twice before with other stacks."** (این استک برام جدیه — کندتر از معمول جا می‌افتم، ولی با دو استکِ دیگه دو بار این کار رو کردم.) مدیریتِ انتظار، نصفِ اعتبارِ ادغام است.'),
  ('ریموت شروع می‌کنم — ادغامم سخت‌تر می‌شود؟',
   'سخت‌تر اما با نسخهٔ خودش: ۱) جلسهٔ آشناییِ ۱۵دقیقه‌ای را خودت با هر نفر بگذار (درس ۴۸). ۲) در کانال‌ها «حضوری» باش: کامنتِ سوال‌محور، PRهای سریع، و آپدیتِ هفتگیِ یک‌خطی: **"Ramp-up week 3: finished onboarding docs, debugging the checkout sandbox. Next: my first small PR."** ۳) از pair-programmingِ داوطلبانه بگیر: **"Could we do a 30-minute pairing on your area? I learn way faster watching than reading."** — ریموت، ادغامِ خاموش می‌سازد؛ تو با «روایتِ عمومیِ پیشرفت» جبرانش می‌کنی.'),
 ],
},
# ───────────────────────────── درس ۷۰ ─────────────────────────────
{
 'slug': 'english-mentoring-juniors',
 'title': 'منتورینگ؛ یاد دادن به جونیورها به انگلیسی',
 'desc': 'گفتارِ خوبِ یاد‌دادن: سوالات هدایتگر (What have you tried so far?), تشریحِ مسیر به‌جای جوابِ مستقیم, بازخوردِ محترمانهٔ سطحِ جونیور, و مرزِ «راهنمایی» با «کارکردن به‌جای».',
 'keywords': 'منتورینگ, mentoring phrases, یاد دادن, junior developer',
 'answer': 'منتورِ خوب سه جمله می‌چرخاند: What have you tried? (همیشه اول!), That\'s a good attempt — now let\'s look at… (تأیید + جهت), و Walk me through your thinking (مسیرِ فکرش را بیرون می‌کشد). قاعدهٔ طلایی: جواب نده — مسیر بده؛ جوابِ فوری، امروز را نجات می‌دهد و فردا را می‌سوزاند.',
 'intro': [
  'منتورینگ، اولین قدمِ رهبریِ فنی است — و جایی که مهارتِ زبانیِ تو از «حرف‌زدن در جلسه» به «ساختنِ آدم» ارتقا می‌یابد. برای زبانِ دوم، خبرِ شیرین: گفتارِ یاددادن، آهسته‌ترین و ساختاریافته‌ترین گفتگوی فنی است — بهترین میدانِ تمرینِ تو هم هست.',
  'این درس سه موقعیتِ محوری را می‌دهد: پاسخ‌دادن به «گیر کردم»، بازبینیِ کدِ جونیور، و دادنِ بازخوردِ رشد. و یک خطِ قرمزِ فرهنگی: تو «جواب‌دهنده» نیستی، «همراهِ مسیر» هستی — همین چرخش، منتور را از «کسی که کار را می‌گیرد» جدا می‌کند.',
 ],
 'sections': [
  {'h2': 'پاسخ به «گیر کردم»؛ سه‌گانهٔ سوالِ هدایتگر',
   'blocks': [
    ('p', 'وقتی جونیور گفت «blocked شدم»، ترتیبِ سه‌گانه: **۱)** "What have you tried so far?" — همیشه اول؛ جوابش، نقشهٔ ذهنش را نشان می‌دهد. **۲)** "What does the error actually say — walk me through it." (خطا دقیقاً چی می‌گه — بخونش برم.) **۳)** "What would you try if I weren\'t here?" (اگه من نبودم چی رو امتحان می‌کردی؟) — این سومین، جادویی است: اعتماد به خودش را فعال می‌کند. بعد از شنیدن، قالبِ جهت‌دهی: **"Good instinct. Next time the error mentions a port, what\'s usually the first suspect?"** (غریزه‌ت خوبه. دفعهٔ بعد که خطا از port گفت، اولین مظنون معمولاً چیه؟) — سوال، جواب را از خودش بیرون می‌کشد؛ جوابِ مستقیم فقط امروز را خاموش می‌کند.'),
    ('ex', 'You\'re close — the bug isn\'t in your logic, it\'s in the assumption. Read line 12 again: what type is that variable really?', 'نزدیکی — باگ تو منطقت نیست، تو فرضته. خط ۱۲ رو دوباره بخون: این متغیر واقعاً چه نوعیه؟'),
   ]},
  {'h2': 'کدِ جونیور را بازبینی کن؛ بازخوردِ رشد‌ده',
   'blocks': [
    ('p', 'ریلویویِ منتورانه سه لایه دارد (فرمولِ درس ۵۶، نسخهٔ رشد): **۱) ستایشِ مشخص:** "This error handling is better than most senior code I see — you thought about the retry." **۲) یک نکتهٔ بلند-اثر، نه ده نکتهٔ خرد:** "The one thing I\'d focus on this month: naming. `handleData` could be `parseInvoice` — names are the cheapest documentation." (چیزی که این ماه روش تمرکز کن: اسم‌گذاری — اسم‌ها ارزون‌ترین داک‌اند.) **۳) دعوت به فکر:** "Why do you think the framework wants us to register the route there?" — سوالِ «چرا»، جونیور را از «کدنویس» به «مهندس» جابه‌جا می‌کند. و قاعدهٔ نسبت: به‌ازای هر «بهترش کن»، یک «این خوب بود» — جونیورِ ریلویوشدهٔ خالص، یادگرفتن را با ترس اشتباه می‌کند.'),
   ]},
  {'h2': 'مرزِ منتورینگ؛ کمک بدونِ جا‌زدن',
   'blocks': [
    ('p', 'سه مرزِ سالم: **۱) پنج‌دقیقه قاعده:** "Let\'s timebox this pairing to 15 minutes — if we\'re not unstuck, we regroup tomorrow with fresh eyes." (نیم‌ساعت سقف؛ اگر باز نبود، فردا با چشمِ تازه.) **۲) نه به کارکردن به‌جای:** وقتی وسوسه شدی خودت بنویسی: "If I write it, you\'ll debug my code next time. If you write it, you\'ll debug yours — and you\'ll only get faster. I\'ll sit with you." **۳) منشأِ واقعی را بپر:** اگر سه بار به یک موضوعِ مشابه گیر کرد، مشکل باگ نیست، مفهوم است: **"I think we\'re fixing symptoms. Let\'s spend 30 minutes on async/await itself — no ticket, just the concept."** — منتورِ بزرگ، گاهی از بلیت عبور می‌کند تا مفهوم را بسازد؛ جمله‌اش همین است.'),
   ]},
 ],
 'takeaway': 'منتورینگ = سوالِ هدایتگر (What have you tried? / walk me through / if I weren\'t here?) + ریلویویِ یک‌نکته‌ایِ ستایش‌دار + مرزِ سقفِ وقت و «نوشتن نکردن». جوابِ مستقیم، بدهیِ فردای تیم است؛ سوالِ درست، سرمایه. و هر مفهومِ تکرار-گیر، جای جلسهٔ مفهومیِ سی‌دقیقه‌ای است — منتورِ خوب گاهی از بلیت عبور می‌کند.',
 'faq': [
  ('خودم جونیورم؛ می‌توانم منتور باشم؟',
   'بله — و اسمش «peer mentoring» است: مهارتِ برایت تازه و به‌روزترین چیزِ تیم است؛ جونیورِ تازه‌تر از تو، از تو ساده‌تر می‌گیرد. سه موقعیتِ امنِ جونیور-منتوری: آنboarding همراه (به نفرِ تازه‌تر بگو «منم دو هفته پیش همین‌جا گیر کردم»), داک‌نویسی (چیزی که یاد گرفتی را مستند کن), و سوال‌های محیط (نه معماری). جملهٔ شروع: **"I\'m no expert, but I fought this same error last week — want me to show you what worked?"** — «متخصص نیستم اما همین خطا رو هفتهٔ پیش باهاش جنگیدم» — صادقانه، مفید، و از همین امروز ممکن.'),
  ('جونیورم بیش‌ازحد سوال می‌پرسد و وقتِ من را می‌خورد!',
   'سه‌لایه‌ایِ راه‌حل: ۱) آیینِ «بفرستِ-اول، بپرسِ-بعد»: **"Before you ask me, spend 15 minutes on it and write down what you tried — then ask. You\'ll be surprised how often that solves it."** (قبل از سوال، ۱۵ دقیقه بجنگ و بنویس چه کردی — بعد بپرس.) ۲) ساعاتِ دفترِ باز: **"I\'m blocking 3-4pm for questions — bring them all then; outside that, I\'m heads-down."** ۳) برای سوال‌های تکراری، داک بساز: هر سوالِ دوم را به doc بفرست: "Check the onboarding notes, section 3 — and tell me if it\'s unclear, I\'ll fix the doc." — منتورینگِ مقیاس‌پذیر، سوال را یک‌بار جواب می‌دهد و صد بار لینکش می‌دهد.'),
 ],
},
# ───────────────────────────── درس ۷۱ ─────────────────────────────
{
 'slug': 'english-conferences-networking',
 'title': 'کنفرانس و شبکه‌سازی؛ از badge تا follow-up',
 'desc': 'زبانِ رویدادهای فنی: شروعِ گفتگو در لابی (What did you think of the talk?), معرفیِ سی‌ثانیه‌ای در میکسِ حضوری, تبادلِ کارت و LinkedIn, و پیگیریِ چهارخطی که شبکه را می‌سازد.',
 'keywords': 'کنفرانس, networking انگلیسی, elevator pitch, follow up email',
 'answer': 'شبکه‌سازی در کنفرانس سه برخورد دارد: شروعِ سبک (How did you find the keynote?), معرفیِ سی‌ثانیه‌ای (I\'m Ali — backend at a fintech, obsessed with event pipelines), و پیگیریِ ۴۸ساعته (Great meeting you at ReactConf — the chat about retries stuck with me). هیچ‌کدام نبوغ نمی‌خواهد؛ قالب می‌خواهد.',
 'intro': [
  'کنفرانس‌ها، میدانِ شبکه‌سازی‌اند — و شبکه، نصفِ فرصت‌های حرفه‌ایِ بازارهای انگلیسی‌زبان. اما برای غیرِبومی، لابیِ کنفرانس سخت‌تر از سخنرانی است: باید با غریبه شروع کرد، با وقار قطع کرد و بعد از رویداد پیگیری کرد. خبرِ خوب: همه در لابی کمی خجالتی‌اند — بومی‌ها هم! قالبِ شروع، مشکلِ ۹۰٪ را حل می‌کند.',
  'این درس، سه برخورد + دو موقعیتِ خاص (سوال‌پرسیدن بعد از talk و صحبت با بوت) را می‌دهد. هدفش فقط «کارت جمع کردن» نیست: دو-سه آشناییِ واقعی از هر رویداد، بیشترین بازده را دارد.',
 ],
 'sections': [
  {'h2': 'لابی و میکس؛ شروعِ گفتگو با غریبه',
   'blocks': [
    ('p', 'چهار آغازگرِ امنِ لابی — همه دربارهٔ «هم‌تجربهٔ همین‌جا»: **"First time at this conference?"** · **"What did you think of the keynote?"** · **"Which talks are you hitting next?"** · **"Is this your seat? Mind if I join?"** (سرِ میزِ ناهار). بعد از شروع، معرفیِ ۳۰ثانیه‌ای (نسخهٔ رویدادیِ درس ۴): **"I\'m Ali — backend at a payments startup. I\'m here mostly for the distributed-systems track. What\'s your corner of the world?"** (من علی‌ام — بک‌اند در یه استارتاپِ پرداخت. برای ترکِ سیستم‌های توزیع‌شده اومدم. گوشهٔ دنیای تو چیه؟) — سوالِ آخر، توپ را برمی‌گرداند و گفتگو زنده می‌ماند.'),
    ('ex', 'This is my first DevOpsConf — I mostly came for the chaos-engineering talks. How about you?', 'اولین DevOpsConf منه — عمدتاً برای تاک‌های مهندسیِ آشوب اومدم. تو چطور؟'),
   ]},
  {'h2': 'بعد از talk و در بوت؛ دو موقعیتِ طلایی',
   'blocks': [
    ('p', '**سوال بعد از سخنرانی** (خط ازدحام بی‌خطر نیست، فرصت است): **"Thanks for the talk — the part about backpressure really clicked for me. In your experience, what\'s the first signal you\'re in trouble?"** (ممنون از ارائه — بخشِ backpressure برام جا افتاد. از تجربه‌ات، اولین سیگنالِ به‌خطرافتتن چیه؟) — سوالِ مشخصِ جزئی‌محور، تو را از صفِ «تشکرگویان» جدا می‌کند. **بوت‌ها** (booth): اگر فرصتِ شغلی می‌خواهی: **"I\'m a backend dev, mostly Python — are you hiring for the platform team? Who\'s the right person to talk to?"** (توسعه‌دهندهٔ بک‌اندم، عمدتاً پایتون — برای تیمِ پلتفرم استخدام می‌کنید؟ با کی صحبت کنم؟) — پرسیدنِ «who\'s the right person» حتی وقتی جوابِ منفی است، مسیرِ درست را می‌سازد.'),
   ]},
  {'h2': 'پایان و پیگیری؛ جایی که شبکه واقعاً ساخته می‌شود',
   'blocks': [
    ('p', 'قطعِ گفتگو با وقار: **"It was great meeting you — I\'m going to catch the next talk, but let\'s connect on LinkedIn?"** (از آشنایی خوشحالم — می‌خوام برسونم تاکِ بعدی، ولی لینکد‌این وصل شیم؟) و جملهٔ تبادل: **"Do you have a card, or is LinkedIn easier?"** — امروز لینکداین، پیش‌فرض است. و پیگیریِ ۴۸ساعته — مهم‌ترین جملهٔ این درس: **"Hi Sara — great meeting you at DevOpsConf yesterday! That chat about on-call rotations stuck with me; here\'s the incident-review template I mentioned. Coffee next time you\'re in the city?"** (سارا سلام — دیروز تو کنفرانس خیلی خوب شد! بحثِ شیفت‌های on-call تو ذهنم موند؛ اینم قالبِ بازبینیِ حادثه که گفتم. دفعهٔ بعد که اومدی شهر، قهوه؟) — چهار جزء: یادآوریِ محل، اشارهٔ مشخص به موضوعِ مشترک، ارزشِ داده‌شده (لینک/قالب), درخواستِ کوچکِ بعدی. همین یک پیام، آشنایی را به شبکه تبدیل می‌کند.'),
   ]},
 ],
 'takeaway': 'شبکه‌سازیِ رویدادی = آغازگرِ هم‌تجربه (Which talks are you hitting?) + معرفیِ ۳۰ثانیه‌ای با «گوشهٔ دنیای تو چیه؟» + سوالِ جزئی‌محور بعد از talk + «who\'s the right person» در بوت + پیگیریِ ۴۸ساعته با چهار جزء. هدف: سه آشناییِ واقعی، نه سی کارت. و پیگیری، خودِ شبکه‌سازی است — بقیه مقدمه‌اند.',
 'faq': [
  ('کنفرانس حضور نمی‌یابم؛ شبکه آنلاین چطور؟',
   'همان فرمول در بسترِ متن: توییتر/لینکداین — جوابِ thoughtful به پستِ کسی (نهِ «Great post!» که «Your point about X matches what we saw — in our case the trigger was Y»), شرکتِ واقعی در کامیونیتی‌های فنی (اسلک‌های اپن‌سورس، Reddit), و «مجازی‌سازیِ رویداد»: meetupهای آنلاین و استریم‌ها که همان لابی را دارند: کانالِ چت! جملهٔ شروعِ آنلاین: **"Joining from Tehran — great question in the Q&A about schema migrations. Anyone here dealt with zero-downtime ones?"** — شبکهٔ آنلاین، پیگیریِ ۴۸ساعته‌اش هم پیش‌فرض است: DM همان ایمیلِ چهارجزری است.'),
  ('مصاحبهٔ شغلی هم «شبکه» است؟ به معرفی‌ها چطور برسم؟',
   'معرفی (referral) مهم‌ترین کانالِ استخدامِ بازارهای انگلیسی‌زبان است و جمله‌اش همین درس است: به آشنای درونِ شرکت: **"Hey Sara — I saw the senior backend opening on your careers page. I\'ve been following your team\'s blog for a while and it\'s exactly the kind of work I want to do. Would you be comfortable referring me? Happy to send my CV and a short blurb to make it easy."** (سارا سلام — جایگاهِ سنیورِ بک‌اند رو تو صفحهٔ استخدامتون دیدم. مدتیه بلاگِ تیم‌تون رو دنبال می‌کنم و دقیقاً همین کار رو می‌خوام. راحتی داری من رو معرفی کنی؟ رزومه و چند خط معرفی می‌فرستم که راحت باشه.) — «راحتی داری» و «که راحت باشه» نصفِ جوابِ مثبت‌اند: درخواستِ معرفی، کار را برای معرفی‌دهنده سبک می‌کند.'),
 ],
},
# ───────────────────────────── درس ۷۲ ─────────────────────────────
{
 'slug': 'english-level4-review',
 'title': 'جمع‌بندی فاز ۴ + شبیه‌سازیِ «یک اسپرینتِ کامل»',
 'desc': 'مرورِ ۲۲ درسِ فنی در یک اسپرینتِ پنج‌روزهٔ زنده: planning، استندآپ‌ها، کدریویو، حادثهٔ کوچک، دمو و رترو — و چک‌لیستِ «مهندسِ گفتاریِ آماده».',
 'keywords': 'جمع بندی فاز ۴, شبیه سازی اسپرینت, مرور انگلیسی فنی, sprint simulation',
 'answer': 'فاز ۴ تمام شد اگر می‌توانی یک اسپرینتِ کامل را — از planning تا retro — به انگلیسی راند کنی. این درس همان هفته را روزبه‌روز می‌سازد: دوشنبه planning، سه‌روز استندآپ و ریلویو، پنجشنبه حادثهٔ کوچک، جمعه دمو و رترو.',
 'intro': [
  'بیست‌ودو درسِ فاز ۴، «دفترِ کارِ فنیِ» تو را ساخت: از واژگانِ پایه تا مصاحبه‌های system design و رفتاری. حالا سومین «دوختِ بزرگِ» دوره: یک اسپرینتِ کامل — دقیقاً همان چیزی که هفتهٔ آیندهٔ شغلت شبیهش خواهد بود. هر صحنه به درسِ پشتوانه‌اش وصل است؛ برای تستِ خودت، بدونِ برگشتن جلو برو.',
  'این آخرین ایستگاهِ قبل از فازِ حرفه‌ای‌سازی است: درس‌های ۷۳ به بعد، لحن و قدرت را بالا می‌برند — رهبریِ جلسه، مذاکرهٔ حقوق، مدیریتِ حادثه و فرهنگِ عمیقِ مکالمه. پایه را اینجا محکم ببند.',
 ],
 'sections': [
  {'h2': 'دوشنبه؛ planning و برداشتنِ کار',
   'blocks': [
    ('ex', 'Team lead: This sprint: payments retry and the checkout bugs. Who takes retries? — You: I can take it. Ballpark three days, assuming the sandbox is stable. I\'ll spike the idempotency part first.', 'لید: این اسپرینت: retryِ پرداخت و باگ‌های تسویه. retries کیه؟ — تو: می‌گیرمش. حدوداً سه روز، با فرضِ پایداریِ سندباکس. اول بخشِ idempotency رو اسپایک می‌کنم.'),
    ('ex', 'PM: Can we also fit the export feature? — You: Adding it means cutting the bugfixes. Which one wins?', 'PM: فیچرِ خروجی‌گرفتن رو هم جا می‌شه؟ — تو: اضافه‌کردنش یعنی حذفِ فیکس‌ها. کدوم برنده باشه؟'),
    ('p', 'صحنهٔ planning، تمرکزِ درس‌های ۵۸ (اسکرام) و ۶۵ (تخمین) است: برداشتنِ کار با تخمینِ قالب‌دار (ballpark + assuming), سقفِ شفاف، و سوالِ «کدوم می‌بره» برای اسکوپِ اضافه. سه جمله که دوشنبه‌ها صدایت می‌کنند: **"I\'ll take it."** · **"Let me spike it first — I\'ll come back with a number."** · **"Adding means cutting — what do we drop?"**'),
   ]},
  {'h2': 'سه‌شنبه تا چهارشنبه؛ استندآپ، ریلویو، جنگِ کوچک',
   'blocks': [
    ('ex', 'Standup: Yesterday I finished the retry spike — it\'s a one-pager in the docs. Today I\'m implementing the backoff. No blockers, but the flaky payment test is slowing me down.', 'استندآپ: دیروز اسپایکِ retry رو بستم — یک‌صفحه‌ای تو داک‌هاست. امروز backoff رو پیاده می‌کنم. بلوکری نیست، ولی تستِ بی‌ثباتِ پرداخت کندم کرده.'),
    ('ex', 'Review comment on your PR: "Nit: magic number here — could we name it?" — You: Good catch — replaced with MAX_RETRIES. Pushed.', 'کامنتِ ریلویو: «جزئی: این عددِ جادولیه — اسم‌گذاریش کنیم؟» — تو: دقتِ خوبی بود — با MAX_RETRIES عوضش کردم. پوش شد.'),
    ('p', 'روزهای میانی، درس‌های ۵۵ (استندآپ), ۵۶ (ریلویو) و ۵۷ (دیباگ) در هم می‌آمیزند: گزارشِ سه‌تکه، کامنت‌های درجه‌دار، و اگر باگِ عجیب زود کرد: **"It\'s intermittent — one in ten. My theory is a race between the retry and the status check. I\'ve ruled out the network."** (گاهی‌به‌گاهه. فرضیه‌ام: رقابتِ retry و چکِ وضعیت. شبکه رو حذف کردم.) — همین جمله، در دنیای واقعی، یعنی «این آدم حرفه‌ای شکار می‌کند».'),
   ]},
  {'h2': 'پنجشنبه؛ حادثهٔ کوچک و مدیریتش',
   'blocks': [
    ('ex', 'Heads-up team: the retry I shipped yesterday doubled one charge in staging. I\'ve reverted the rollout, writing the fix now — PR in an hour, with a regression test.', 'خبر تیم: retryِ دیروز تو staging یه پرداخت رو دوباره کرد. رول‌اوت رو برگردوندم، الان فیکسش رو می‌نویسم — PR تا یه ساعت، با تستِ رگرسیون.'),
    ('p', 'نسخهٔ کوچکِ درس ۸۲ (مدیریتِ حادثه): اعلامِ فوری (heads-up), اقدامِ محدودکننده (revert), تعمیرِ شفاف (PR + regression test), و بعداً در رترو: **"The lesson: retries need idempotency keys — I\'ve added it to the checklist so it\'s systemic, not personal."** — حادثهٔ کوچکِ مدیریت‌شده، اعتبار می‌سازد؛ حادثهٔ پنهان‌شده، اعتبار می‌سوزاند. جمله‌ی طلایی: **"I\'d rather flag it early."**'),
   ]},
  {'h2': 'جمعه؛ دمو و رترو + چک‌لیستِ فاز ۴',
   'blocks': [
    ('ex', 'Demo: Two minutes — watch the failed payment retry itself: three attempts, no double charge, user never notices. That\'s the sprint goal, done.', 'دمو: دو دقیقه — ببینید پرداختِ شکست‌خورده خودش رو امتحان می‌کنه: سه تلاش، بدونِ پرداختِ دوباره، کاربر متوجه نمی‌شه. هدفِ اسپرینت همین بود — انجام شد.'),
    ('ul', [
      'استندآپِ سه‌تکه را بدونِ فکر روان می‌گویم (درس ۵۵)',
      'کامنت‌های ریلویو را درجه‌دار می‌دهم و با قالب جواب می‌گیرم (۵۶)',
      'باگ را با گزارشِ چهاربندی و فرضیه می‌شکنم (۵۷)',
      'planning را با تخمینِ بازه+فرض و سوالِ معاوضه می‌رانم (۵۸+۶۵)',
      'داک و کامنتِ «چرا» می‌نویسم (۵۹)',
      'اسلک: نرم، threadدار و ایموجی-موuz (۶۰)',
      'مصاحبه‌های coding/system/رفتاری را با صدای فکر می‌رانم (۶۱-۶۳)',
      'دمو می‌دهم و لحظهٔ خرابی را مدیریت می‌کنم (۶۴)',
      'با PM ترجمهٔ دوطرفه می‌کنم: اثر و مسئله (۶۶)',
      '1:1 را با agenda و سوالِ رشد می‌رانم (۶۷)',
      'مخالفتِ فنی را با داده + گزینه + تعهد می‌دهم (۶۸)',
      'منتورینگ با سوالِ هدایتگر می‌دهم و مرزش را می‌دارم (۷۰)',
      'در رویدادها با آغازگر و پیگیریِ ۴۸ساعته شبکه می‌سازم (۷۱)']),
    ('p', 'و از درسِ بعد، فاز ۵: حرفه‌ای‌شدن — لحن و اصطلاحات، جلسه‌گردانی و RFC، ارائه برای مدیران، مذاکرهٔ حقوق، مدیریتِ حادثهٔ بزرگ و فرهنگِ مکالمه. مسیرِ «مهندسِ خوب» تمام شد؛ مسیرِ «مهندسِ تأثیرگذار» شروع می‌شود.'),
   ]},
 ],
 'takeaway': 'اسپرینتِ کامل = planning با تخمینِ قالب‌دار + استندآپ‌های سه‌تکه + ریلویوی درجه‌دار + مدیریتِ حادثهٔ کوچک با heads-up + دموی پیام‌دار + رتروی بی‌اتهام. چک‌لیست را صادقانه بزن؛ هر تیکِ خالی، همان یک درس است. فاز ۵ در انتظار توست: از «کاری که انجام می‌دهی» به «اثری که می‌گذاری».',
 'faq': [
  ('این همه مکالمهٔ فنی را بدونِ تیمِ انگلیسی چطور تمرین کنم؟',
   'سه لایه: ۱) **تئاترِ تنهایی:** نقش‌ها را در مشیِ درس ۱۵ بازی کن — تو هم لید باش، هم PM، هم خودت؛ صدای هر نقش را عوض کن. ۲) **اپِ مکالمهٔ آپورد:** سناریوها را «سprint» بگذار — استندآپ، ریلویو، حادثه؛ AI بازیِ طرفِ مقابل را می‌کند و تو را نمره می‌دهد. ۳) **تیمِ فارسی‌زبانِ خودت:** هفته‌ای یک استندآپ و یک رترو را «فقط انگلیسی» کنید — خنده‌دار می‌شود، بعد عادی، بعد ماهرانه. زبان در تیمِ تمرینِ امن می‌روسد، نه در جلسهٔ سردِ اول.'),
  ('فاز ۴ را برای مصاحبه لازم دارم، نه کارِ فعلی — اولویت چیه؟',
   'اگر هدفِ نزدیک‌ات مصاحبه است: درس‌های ۶۱-۶۳ (مصاحبه‌ها) + ۵۲ (واژگان کد) + ۵۳ (توضیح کد) را عمیق کن و ۶۵ (تخمین) را برای سوال‌های سیستم‌های واقعی بخوان؛ استندآپ و ریلویو بعد از استخدام می‌آیند و همان موقع با این درس‌ها آماده‌ای. مصاحبه گفتارِ تک‌نفره است و تمرینش با اپ و آینه کامل می‌شود — از همین امروز روزی بیست دقیقه.'),
 ],
},
]

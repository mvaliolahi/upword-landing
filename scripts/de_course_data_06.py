# -*- coding: utf-8 -*-
"""دورهٔ ۹۰ روزهٔ آلمانی — فایل دادهٔ ۶ (درس‌های ۴۶ تا ۵۴: پایان فاز ۳ + شروع فاز ۴)."""

LESSONS = [

# ── درس ۴۶ ─────────────────────────────────────────────────────────────────
{
    'slug': 'german-one-on-one',
    'title': 'جلسهٔ یک‌به‌یک؛ بازخورد با مدیر به آلمانی',
    'desc': 'گفتگویِ رشد با تیم‌لید: قالبِ جلسهٔ ۱:۱، پرسیدنِ بازخورد، شنیدنِ نقدِ آلمانی و درخواستِ رشد.',
    'keywords': 'جلسه یک به یک, بازخورد آلمانی, 1:1 آلمان, گفتگو با مدیر آلمان, رشد شغلی آلمان',
    'answer': 'جلسهٔ ۱:۱ آلمانی سه‌پارچه است: وضعیت (Wie läuft’s bei dir?)، بازخورد (دو طرف!) و رشد (Ziele). جملهٔ طلاییِ پرسیدنِ بازخورد: „Ich würde gern dein Feedback hören — was kann ich besser machen?“ و پاسخِ حرفه‌ای به نقد: „Danke, das nehme ich mit“ (ممنون، این را با خودم می‌برم).',
    'intro': [
        'جلسهٔ یک‌به‌یک، مقدس‌ترین گفتگویِ کاری‌ات است: نیم‌ساعتِ ماهانه که فقط برای توست! در آلمان این جلسه جدی گرفته می‌شود — آماده بیا، سؤال بیاور، بازخورد بگیر و بده.',
        'این درس هر دو سمتِ میز را می‌سازد: تو به‌عنوان دریافت‌کنندهٔ بازخورد (شنیدنِ نقدِ مستقیمِ آلمانی بدونِ دل‌شکستگی!) و به‌عنوان رهبرِ رشدِ خودت (درخواستِ چالش، آموزش، مسیرِ پیشرفت). جمله‌های این درس، سرمایهٔ سال‌هایِ کاریِ آینده‌ات‌اند!'
    ],
    'sections': [
        {
            'h2': 'قالبِ جلسه؛ سه پارچهٔ ثابت',
            'blocks': [
                ('table', ['پارچه', 'سوالِ مدیر', 'نقشِ تو'],
                    [['وضعیت', 'Wie läuft’s bei dir? Alles gut mit der Arbeitslast?', 'صادقانه: gut + یک چالش'],
                     ['بازخورد', 'Hast du Feedback für mich / für das Team?', 'بده! قالب: مثبت + نکته + پیشنهاد'],
                     ['رشد', 'Wo willst du in einem Jahr stehen?', 'هدف + درخواستِ مشخصِ حمایت']]),
                ('p', 'آدابِ آلمانیِ ۱:۱: **صادقانه و کوتاه** — «alles gut»ی خالی، وقت‌تلف‌کردن است؛ یک چالشِ واقعی بگو. و جلسه‌ی خودت است: agenda بیاور! جملهٔ شروعِ حرفه‌ای: „Ich habe mir drei Punkte notiert“ (سه نکته را یادداشت کرده‌ام.)')
            ]
        },
        {
            'h2': 'پرسیدن و گرفتنِ بازخورد',
            'blocks': [
                ('ex', 'Ich würde gern dein Feedback hören. Was läuft gut, was kann ich besser machen?', 'دوست دارم بازخوردت را بشنوم. چه چیز خوب پیش می‌رود، چه چیزی را می‌توانم بهتر انجام بدهم؟ — سوالِ دو‌لایه: مثبت + قابلِ بهبود!'),
                ('ex', 'Du bist sehr selbstständig — das ist stark. Und: Frag im Zweifel früher, bevor du zu tief in die falsche Richtung läufst.', 'خیلی مستقلی — این قوتت است. و: در شک، زودتر بپرس قبل از آن‌که عمیق در جهتِ غلط بروی. — الگویِ بازخوردِ آلمانی: قوت + نکتهٔ رشد!'),
                ('ex', 'Danke, das nehme ich mit. „Früher fragen“ — merke ich mir.', 'ممنون، این را با خودم می‌برم. «زودتر پرسیدن» — یادداشتش می‌کنم. — جوابِ حرفه‌ای: تشکر + تکرارِ نکته (نشانهٔ دریافت!)'),
                ('p', 'سه جوابِ ممنوع به بازخوردِ آلمانی: دفاعِ فوری («ولی…»)، توضیحِ طولانیِ چرا-این‌طور-بود و بی‌تفاوتی. فرمولِ طلایی: **تشکر + تکرارِ نکته + اقدام** — همین!'),
            ]
        },
        {
            'h2': 'گفتگو: یک ۱:۱ کامل — از وضعیت تا هدف',
            'blocks': [
                ('ex', 'Teamlead: Hi Ali! Wie läuft’s? Du bist jetzt zwei Monate dabei.', 'سلام علی! چطور پیش می‌رود؟ الان دو ماه است که هستی.'),
                ('ex', 'Du: Insgesamt gut. Ich komme gut mit der Codebase klar. Eine Herausforderung: die Domäne ist neu für mich — ich lese abends noch viel Doku.', 'در کل خوب. با کدبیس خوب جا افتاده‌ام. یک چالش: دامنه برایم تازه است — شب‌ها هنوز داکیومنتِ زیادی می‌خوانم. — die Herausforderung = چالش؛ واژهٔ طلاییِ ۱:۱!'),
                ('ex', 'Teamlead: Das ist normal. Frag ruhig Sarah — sie kennt die Domäne am besten.', 'طبیعی است. با خیال راحت از سارا بپرس — دامنه را بهترین می‌شناسد. — ruhig = با خیال راحت؛ نرم‌کنندهٔ آلمانی!'),
                ('ex', 'Du: Mache ich. Noch was: Ich würde gern mehr Responsibility übernehmen — zum Beispiel die Betreuung der Testumgebung.', 'می‌کنم. یک چیز دیگر: دوست دارم مسئولیتِ بیشتری بگیرم — مثلاً نگهداریِ محیطِ تست. — درخواستِ رشدِ مشخص!'),
                ('ex', 'Teamlead: Guter Gedanke! Lass uns das als Ziel für den nächsten Sprint aufschreiben.', 'فکرِ خوبی است! بیا به‌عنوانِ هدف برای اسپرینتِ بعد بنویسیمش. — هدفِ مکتوب = دستاوردِ واقعیِ ۱:۱!')
            ]
        },
        {
            'h2': 'گرامرِ عمیق‌تر: رؤیا با «Ich würde gern…» — شکلِ مؤدبِ آرزو',
            'blocks': [
                ('p', 'هر درخواستِ رشد با **Ich würde gern …** شروع می‌شود — مؤدبانه‌ترین شکلِ «می‌خواهم» که با könnte از درس ۴۰ خانواده است: „Ich würde gern mehr Verantwortung übernehmen“ (دوست دارم مسئولیتِ بیشتری بگیرم)، „Ich würde gern einen Kurs über Architektur machen“ (دوست دارم دوره‌ای دربارهٔ معماری بگذرانم)، „Ich würde gern irgendwann Teamlead werden“ (دوست دارم روزی تیم‌لید شوم). این قالب، آرزو را «درخواستِ قابلِ بحث» می‌کند — نه مطالبه! و جوابِ مدیر معمولاً: „Lass uns einen Plan machen“ (بیا یک برنامه بریزیم) — دو جمله که مسیرِ رشدت را می‌سازند.'),
            ]
        },
        {
            'h2': 'اشتباه‌های رایجِ فارسی‌زبان‌ها در همین درس',
            'blocks': [
                ('p', 'این بخش را با یک قرارداد بخوان: هر ❌ یعنی «مغزِ فارسی‌زبانت این را می‌سازد و طبیعی است»، و هر ✅ یعنی «این همان چیزی است که گیرندهٔ آلمانی‌زبان می‌شنود». با هر جفت بلند تکرار کن تا شکلِ درست در گوشت نشست کند.'),
                ('ex', '❌ Alles gut! (تنها جوابِ «چطوره؟»)', '❌ پاسخِ خالی، جلسه را می‌کُشد — حداقل یک قوت + یک چالش!'),
                ('ex', '✅ Insgesamt gut. Gut läuft X, herausfordernd ist Y.', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.'),
                ('ex', '❌ (نقدِ مدیر) Aber das war weil… die Zeit… und der Kollege…', '❌ دفاعِ سه‌دلیلی! نقد را بگیر، تشکر کن، بعد اگر لازم است یک جملهٔ توضیح!'),
                ('ex', '✅ Verstehe. Hintergrund war: … — Ich mache es künftig anders.', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.'),
                ('ex', '❌ Ich will mehr Geld. (در ۱:۱، بدونِ زمینه)', '❌ بحثِ حقوق، جلسهٔ خودش را می‌خواهد (درس ۴۷!)؛ در ۱:۱ اول رشد و مسئولیت — بعد پول!',),
                ('ex', '✅ Ich würde gern mehr Verantwortung übernehmen.', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.')
            ]
        },
        {
            'h2': 'تمرین‌های این درس — چهار قدم، بی‌عجله',
            'blocks': [
                ('p', 'تمرین: ۱:۱ بعدیِ خودت را از قبل بساز:'),
                ('ol', [
                    'سه نکتهٔ agendaٔ خودت را بنویس: وضعیت + یک بازخوردخواهی + یک درخواستِ رشد.',
                    'یک بازخوردِ خیالی را با الگویِ قوت + نکته بنویس — برای یک همکارِ واقعی.',
                    'سه جملهٔ «Ich würde gern …» برای آرزوهای واقعیِ کاری‌ات بساز.',
                    'دیالوگِ کاملِ ۱:۱ را اجرا کن — هر دو نقش؛ جملهٔ پایانیِ هدفِ مکتوب!'
                ]),
                ('faq', [
                    ('پاسخ تمرین ۱', '„1) Status: Gut eingearbeitet, Domäne ist noch neu. 2) Feedback: Wie siehst du meine Code-Reviews? 3) Wunsch: Ich würde gern die Testumgebung betreuen.“ — سه‌نکته‌ایِ کاملِ ۱:۱؛ این را در نوت بنویس و ببر!'),
                    ('پاسخ تمرین ۲', '„Du fragst gute Fragen im Daily — das hilft allen. Ein Tipp: In Reviews könntest du konkreter auf Tests eingehen.“ (سوال‌های خوبی در دیلی می‌پرسی — به همه کمک می‌کند. یک نکته: در ریویوها می‌توانی دقیق‌تر روی تست‌ها بروی.) — قوت + نکتهٔ رشد؛ الگویِ بازخوردِ سالم!'),
                    ('پاسخ تمرین ۳', 'نمونه‌ها: „Ich würde gern Frontend dazulernen.“ · „Ich würde gern einen Vortrag im Team halten.“ · „Ich würde gern irgendwann Senior werden.“ — سه آرزو با یک قالب؛ مؤدب، واضح، قابلِ برنامه‌ریزی!'),
                    ('پاسخ تمرین ۴', 'اجرای کامل با هر دو نقش — و جملهٔ پایانی: „Lass uns das als Ziel aufschreiben.“ این جمله را به خودت هم بگو: هر آرزو، هدفِ مکتوبِ با تاریخ باشد!')
                ])
            ]
        },
        {
            'h2': 'چالشِ امروز',
            'blocks': [
                ('quote', '🎯 امروز سه نکتهٔ ۱:۱ بعدی‌ات را واقعاً بنویس — در نوت، به آلمانی: وضعیت، بازخوردخواهی، آرزو. جلسهٔ ماهانهٔ بعدی، از قوی‌ترین جلسه‌هایِ کاریِ زندگی‌ات شروع می‌شود!')
            ]
        },
        {
            'h2': 'نکات مکالمهٔ واقعی که کتاب‌ها کم می‌گویند',
            'blocks': [
                ('ul', [
                    '**«Feedback ist ein Geschenk» — بازخورد هدیه است** — فرهنگِ آلمانیِ مهندسی، بازخورد را дар می‌داند نه حمله. این جمله را مدیرها واقعاً می‌گویند؛ تو هم باورش کن: هر نقد، نقشهٔ رشدِ رایگان است!',
                    '**۱:۱ جایِ «من خبرهای خوب دارم» نیست — جایِ گفتگویِ واقعی است** — اگر چیزی برای گفتن نداری، از خودت بپرس: از چه چیزی ناراحتی؟ چه چیزی را می‌خواهی؟ سوالی که جلسه را نجات می‌دهد: „Hättest du 5 Minuten für ein Thema, das mich beschäftigt?“ (۵ دقیقه برای موضوعی که ذهنم را مشغول کرده داری؟)',
                    '**جلسهٔ ۱:۱ حقوق و ارتقا، جدا از ۱:۱ ماهانه است** — سالی یک‌بار (یا نیم‌سال) گفتگویِ Gehaltsgespräch (گفتگوی حقوق) و每个人都 Jahr گفتگویِ Leistungsbeurteilung (ارزیابیِ عملکرد) برگزار می‌شود. آرزوها را در ۱:۱ بکار، در جلسهٔ حقوق بردار کن — ترتیبش قانونِ رشدِ مالیِ آلمان است!'
                ])
            ]
        },
    ],
    'takeaway': '۱:۱ = وضعیتِ صادقانه + بازخوردِ دوطرفه + آرزوهای würde-دار. نقد را با «تشکر + تکرار + اقدام» بگیر و هر آرزو را به هدفِ مکتوب تبدیل کن: „Lass uns das als Ziel aufschreiben!“ بازخورد هدیه است — در آلمان این را باور کن!',
    'faq': [
        ('اگر مدیری که ۱:۱ نمی‌گیرد؟', 'خودت بخواه! جملهٔ طلایی: „Ich würde gern monatlich ein kurzes 1:1 etablieren — 30 Minuten, mit meiner Agenda.“ (دوست دارم ماهانه یک ۱:۱ کوتاه برقرار کنیم — ۳۰ دقیقه، با دستورِ جلسهٔ من.) — مدیرِ آلمانیِ خوب این پیشنهاد را دوست دارد؛ مدیرِ شلوغ، یادش می‌آید!'),
        ('چطور به مدیرم بازخورد بدهم بدونِ ریسک؟', 'فرمولِ SBI: موقعیت + رفتار + اثر: „Im Meeting Montag, als du meine Frage unterbrochen hast, bin ich den Faden verloren.“ (در جلسهٔ دوشنبه، وقتی سوالم را قطع کردی، رشتهٔ کلامم را گم کردم.) — بدونِ «تو همیشه…»، بدونِ قضاوت؛ فقط یک واقعه + اثرش. بازخوردِ واقعه‌محور، در آلمان امن‌ترین و مؤثرترین است!')
    ],
},

# ── درس ۴۷ ─────────────────────────────────────────────────────────────────
{
    'slug': 'german-contract-salary',
    'title': 'قرارداد و حقوق؛ خواندنِ Arbeitsvertrag و مذاکره',
    'desc': 'زبانِ قراردادِ کارِ آلمانی: بندهای کلیدی، Brutto و Netto، ساعات و مرخصی و مذاکرهٔ مؤدبانهٔ حقوق — با واژگانِ حقوقیِ ضروری.',
    'keywords': 'قرارداد کار آلمان, حقوق آلمان, Brutto Netto, مذاکره حقوق آلمان, Arbeitsvertrag',
    'answer': 'قراردادِ آلمانی را با پنج بند بخوان: Probezeit (دورهٔ آزمایشی — معمولاً ۶ ماه با اخراجِ آسان!)، Arbeitszeit (ساعات — معمولاً ۴۰)، Urlaub (مرخصی — حداقلِ قانونی ۲۰ روز، خوب: ۲۸-۳۰!)، Kündigungsfrist (مهلتِ لغو) و Gehalt (حقوقِ Brutto — ناخالص!). مذاکره: „Auf Basis meiner Erfahrung halte ich X für angemessen“ — مؤدب + مستند!',
    'intro': [
        'امضای Arbeitsvertrag، مهم‌ترین سندِ مهاجرتِ کاری‌ات است — و آلمانی‌اش پر از واژگانِ حقوقیِ دقیق است که باید بفهمی، نه فقط امضا کنی! این درس پنج بندِ حیاتی را با زبانِ ساده باز می‌کند و جدولِ Brutto→Netto را می‌دهد که «عددِ واقعیِ» حقوقت را روشن کند.',
        'و قسمتِ دوم: مذاکرهٔ حقوق! فرهنگِ آلمانیِ مذاکره، مستند و کم‌احساس است: بازاره را بگو، تجربه‌ات را بشمار، عدد بده و دلیل بیاور — «انشاءالله زیاد می‌شود» و «لبخند بزن کم بگیر» این‌جا کار نمی‌کند؛ «حقِ خود را با ادب بخواه» کار می‌کند!'
    ],
    'sections': [
        {
            'h2': 'پنج بندِ حیاتیِ قرارداد',
            'blocks': [
                ('table', ['بند', 'معنی', 'چک کن'],
                    [['die Probezeit', 'دورهٔ آزمایشی (تا ۶ ماه)', 'اخراج با ۲ هفته notice! دو هفتهٔ اولِ قرارداد را جدی کار کن'],
                     ['die Arbeitszeit', 'ساعاتِ کار (معمولاً ۴۰/هفته)', 'Überstunden (اضافه‌کاری) چطور حساب می‌شود؟'],
                     ['der Urlaub', 'مرخصیِ سالانه', 'قانون: حداقل ۲۰ روزِ کاری؛ خوب: ۲۸-۳۰. با هایلایتِ بندانگشتی!'],
                     ['die Kündigungsfrist', 'مهلتِ لغو', 'رایج: ۴ هفته تا ۳ ماه. برای تو هم هست نه فقط شرکت!'],
                     ['das Gehalt (Brutto)', 'حقوقِ ناخالص', '۱۳ امساخره? نه! Weihnachts-/Urlaubsgeld چک شود']]),
                ('p', 'و سه سوالِ پیش از امضا: „Gibt es eine Gehaltsrevision — wann?“ (بازنگریِ حقوق کی است؟)، „Wie ist die Gehaltsstruktur — Grundgehalt, Bonus, Sachbezüge?“ (ساختارِ حقوق؟) و „Wer ist mein disziplinarischer Vorgesetzter?“ (مدیرِ اداری‌ام کیست؟)'),
            ]
        },
        {
            'h2': 'Brutto به Netto؛ ریاضیِ آلمانیِ حقوق',
            'blocks': [
                ('p', 'حقوقِ قرارداد Brutto است؛ دستت را Netto می‌رسد — و فرقش، سه کسرِ بزرگ است: **Sozialversicherungsbeiträge** (بیمه‌های اجتماعی — نصفش کارفرما!)، **Lohnsteuer** (مالیاتِ حقوق — بسته به Steuerklasse) و گاهی **Kirchensteuer** (مالیاتِ کلیسا — فقط اگر عضو! «Ich bin konfessionslos» یعنی معاف!). قاعدهٔ سرانگشتیِ ۲۰۲۶ برای مجردِ بدونِ بچه (Steuerklasse 1):'),
                ('table', ['Brutto/ماه', 'Netto تقریبی', 'نکته'],
                    [['3.000 €', '~1.950 €', 'شروعِ جونیورِ شهرِ کوچک'],
                     ['4.000 €', '~2.500 €', 'میدلِ عادی'],
                     ['5.500 €', '~3.300 €', 'سنیورِ شهرِ متوسط'],
                     ['7.000 €', '~4.100 €', 'سنیورِ برلین/مونیخ/فرانکفورت']]),
                ('p', 'این اعداد تقریبی‌اند (بیمه و شهر کمی فرق می‌کند) — برای عددِ دقیق، ماشین‌حسابِ Brutto-Netto آنلاین با Stadt و Steuerklasse بزن. جملهٔ طلایی: „Was bleibt netto übrig?“ (خالص چند می‌ماند؟)')
            ]
        },
        {
            'h2': 'مذاکرهٔ حقوق؛ قالبِ مستندِ آلمانی',
            'blocks': [
                ('ex', 'Auf Basis meiner Erfahrung — fünf Jahre Backend, plus Cloud — halte ich 65.000 Euro für angemessen.', 'بر اساسِ تجربه‌ام — پنج سالِ بک‌اند به‌علاوهٔ کلود — ۶۵ هزار یورو را مناسب می‌دانم. — عدد + دلیل؛ بدونِ التماس و بدونِ غر!'),
                ('ex', 'Meine Research zeigt: für diese Rolle in Berlin liegen 65 bis 72. Ich bin bei 68 flexibel.', 'تحقیقم نشان می‌دهد: برای این نقش در برلین ۶۵ تا ۷۲ است. من روی ۶۸ منعطفم. — بازار + بازهٔ خودت!'),
                ('ex', 'Wenn das Grundgehalt fix ist: Gibt es Spielraum bei Bonus, Weiterbildung oder Urlaubstagen?', 'اگر حقوقِ پایه ثابت است: در بونوس، آموزش یا روزهایِ مرخصی جا داریم؟ — مذاکرهٔ چندبعدی! آلمانی‌ها این هوشمندی را دوست دارند.'),
                ('p', 'و دو جوابِ موقعِ «نه»: „Ich verstehe. Was müsste ich zeigen, damit diese Zahl in einem Jahr möglich ist?“ (می‌فهمم. چه چیزی باید نشان دهم تا این عدد در یک سال ممکن شود؟) — مذاکرهٔ نرفته، مسیرِ سالِ بعد را می‌سازد!'),
            ]
        },
        {
            'h2': 'گفتگو: پیشنهادِ کاری — و مذاکرهٔ محترمانه',
            'blocks': [
                ('ex', 'HR: Wir würden Ihnen gerne die Stelle anbieten. Das Jahresgehalt wäre 62.000 Euro.', 'دوست داریم این جایگاه را به شما پیشنهاد کنیم. حقوقِ سالانه ۶۲.۰۰۰ یورو می‌شود. — das Angebot = پیشنهاد؛ anbieten = پیشنهاد‌دادن'),
                ('ex', 'Du: Vielen Dank, das freut mich sehr! Darf ich einen Tag über das Angebot nachdenken?', 'خیلی ممنون، بسیار خوشحالم! می‌توانم یک روز روی پیشنهاد فکر کنم؟ — درخواستِ فکر — همیشه حقِ توست و حرفه‌ای بودنت را نشان می‌دهد!'),
                ('ex', 'HR: Natürlich. — Du (فردا): Ich bin begeistert von der Rolle. Ehrlich gesagt: Meine Erwartung lag bei 68. Gibt es hier etwas Spielraum?', 'البته. — من از نقش شگفت‌زده‌ام. راستش: انتظارم روی ۶۸ بود. این‌جا جایی هست؟ — اشتیاق + عددِ صادقانه + سوالِ نرم!'),
                ('ex', 'HR: Ich kann 64 anbieten, plus 2.000 Weiterbildungsbudget. — Du: Das klingt sehr gut. Ich nehme an!', '۶۴ می‌توانم، به‌علاوهٔ ۲.۰۰۰ بودجهٔ آموزش. — خیلی خوب است. قبول می‌کنم! — جلسهٔ برد-برد؛ جملهٔ پایانیِ متعهد!')
            ]
        },
        {
            'h2': 'گرامرِ عمیق‌تر: زبانِ قرارداد — Modalverbenِ حقوقی',
            'blocks': [
                ('p', 'قراردادها با فعل‌هایِ مُدالیِ دقیق نوشته می‌شوند و فرقشان حقوقِ توست: **müssen** (باید — الزامِ قانونی)، **sollen** (باید — تکلیفِ قراردادی)، **dürfen** (مجاز است — حقِ داده‌شده: „Der Arbeitnehmer darf Homeoffice beantragen“ کارمند حق دارد درخواستِ دورکاری بدهد)، **können** (می‌تواند — امکان). جملهٔ خواندنِ قرارداد: هر مُدال را دورخط بکش و بپرس: این حقِ من است یا وظیفه‌ام؟ «darf» = حقِ تو؛ «muss» = وظیفه‌ات — دو کلمه‌ای که نیمی از قرارداد را معنا می‌کنند!'),
            ]
        },
        {
            'h2': 'اشتباه‌های رایجِ فارسی‌زبان‌ها در همین درس',
            'blocks': [
                ('p', 'این بخش را با یک قرارداد بخوان: هر ❌ یعنی «مغزِ فارسی‌زبانت این را می‌سازد و طبیعی است»، و هر ✅ یعنی «این همان چیزی است که گیرندهٔ آلمانی‌زبان می‌شنود». با هر جفت بلند تکرار کن تا شکلِ درست در گوشت نشست کند.'),
                ('ex', '❌ Ich brauche mehr Geld, das Leben ist teuer.', '❌ دلیلِ شخصی-هزینه‌های زندگی، در مذاکرهٔ آلمانی حرفِ روز نیست — دلیل: بازار + ارزشِ فنی!'),
                ('ex', '✅ Auf Basis des Marktes und meiner Erfahrung halte ich X für angemessen.', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.'),
                ('ex', '❌ (جوابِ فوریِ «بله» به اولین عدد)', '❌ یک شبِ فکر، حقِ توست و امتیازآور — «Darf ich darüber schlafen?» نه فقط برای عاشق‌ها؛ برای قراردادها هم!'),
                ('ex', '✅ Vielen Dank! Darf ich bis morgen dazu Stellung nehmen?', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.'),
                ('ex', '❌ Warum ist mein Gehalt so wenig? (به HR)', '❌ «چرا کمه؟» لحنِ شکایت است؛ سوالِ درست، سوالِ ساختار است!'),
                ('ex', '✅ Wie setzt sich das Gehalt zusammen — Grundgehalt, Bonus, Extras?', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.')
            ]
        },
        {
            'h2': 'تمرین‌های این درس — چهار قدم، بی‌عجله',
            'blocks': [
                ('p', 'تمرین: قراردادِ رویایی/واقعی‌ات را تحلیل و مذاکره کن:'),
                ('ol', [
                    'پنج بندِ حیاتی را برای یک قراردادِ خیالی چک کن — با یک سوالِ دقیق برای هرکدام.',
                    'Brutto خودت را حساب کن: عددِ قرارداد → تخمینِ Netto با جدول — و جملهٔ آلمانی‌اش.',
                    'یک مذاکرهٔ سه‌جمله‌ای بنویس: تشکر + عددِ مستند + سوالِ Spielraum.',
                    'سه سوالِ پیش از امضا را به آلمانی بنویس — برای قراردادِ واقعیِ آینده‌ات!'
                ]),
                ('faq', [
                    ('پاسخ تمرین ۱', '„Wie lang ist die Probezeit? · Wie viele Urlaubstage habe ich? · Gilt Überstunden-Ausgleich? · Welche Kündigungsfrist gilt für mich? · Wann ist die erste Gehaltsrevision?“ — پنج سوالِ قراردادِ آگاهانه!'),
                    ('پاسخ تمرین ۲', 'نمونه: 65.000 im Jahr ≈ 5.400 Brutto/Monat ≈ ~3.200 Netto (Klasse 1). جمله: „Also bleiben monatlich etwa 3.200 netto übrig.“ (پس ماهانه حدود ۳.۲۰۰ خالص می‌ماند.) — عددِ زندگیِ واقعی‌ات!'),
                    ('پاسخ تمرین ۳', '„Vielen Dank für das Angebot! Auf Basis meiner Erfahrung und der aktuellen Marktlage halte ich 68.000 für angemessen. Gibt es hier etwas Spielraum?“ — سه‌جمله‌ایِ کاملِ مذاکرهٔ آلمانی!'),
                    ('پاسخ تمرین ۴', '„Ist die Gehaltsrevision jährlich? · Wie ist der Bonus strukturiert? · Gibt es ein Budget für Weiterbildung und Deutschkurse?“ — سه سوالِ پیش‌امضا؛ سومی، سوپرقدرتِ مهاجرِ زبان‌آموز است!')
                ])
            ]
        },
        {
            'h2': 'چالشِ امروز',
            'blocks': [
                ('quote', '🎯 امروز ماشین‌حسابِ Brutto-Netto آنلاین را باز کن و حقوقِ هدفِ خودت را حساب کن — بعد جمله‌اش را بلند بگو: „Von X Brutto bleiben mir etwa Y netto.“ عددِ خالصِ ماهانه، عددِ تصمیم‌گیریِ زندگی‌ات است!')
            ]
        },
        {
            'h2': 'نکات مکالمهٔ واقعی که کتاب‌ها کم می‌گویند',
            'blocks': [
                ('ul', [
                    '**عددِ سالانه بگو، نه ماهانه — فرقِ فرهنگیِ مهم!** — در آلمان حقوقِ سالانه (Jahresgehalt) گفتنی است: „68.000 Jahresgehalt“ نه «۵.۶۰۰ در ماه». عددِ ماهانه را HR برایت حساب می‌کند؛ تو سالانه مذاکره کن!',
                    '**«Ich nehme an!» جملهٔ پایانیِ متعهدانهٔ پیشنهاد است** — بعدش: قرارداد می‌آید، امضا، روزِ اول! و اگر رد می‌کنی: „Vielen Dank für das Angebot — ich habe mich für einen anderen Weg entschieden.“ (ممنون از پیشنهاد — راهِ دیگری را انتخاب کرده‌ام.) — ردِ حرفه‌ای، پلِ آیندهٔ آلمان را خراب نمی‌کند!',
                    '**Probezeit دوطرفه است!** — در دورهٔ آزمایشی، تو هم با ۲ هفته می‌توانی بروی — این آزادیِ مهاجرِ پیشنهادِ بهتر! و کارفرمای جدی، Probezeit را دورهٔ «معرفیِ واقعی» می‌بیند نه تله؛ با کارِ خوب، حتی اولین ماه هم مهم نیست — آلمانِ کاری، امنیتِ شغلیِ واقعی بعد از Probezeit شروع می‌شود!'
                ])
            ]
        },
    ],
    'takeaway': 'قرارداد را با پنج بند بخوان: Probezeit، Arbeitszeit، Urlaub (۲۸+ خوب!)، Kündigungsfrist، Gehalt. Brutto→Netto با کسرِ بیمه و مالیات حساب کن (~۶۰-۶۵٪ می‌ماند). مذاکره = عددِ سالانه + دلیلِ بازار + „Gibt es Spielraum?“ و جوابِ نهایی: „Ich nehme an!“',
    'faq': [
        ('Gehaltsgespräch سالانه چطور کار می‌کند؟', 'معمولاً بهار/پاییز، HR بودجهٔ افزایش را می‌آورد. جملهٔ شروعِ تو: „Ich würde gerne über meine Entwicklung und eine Gehaltsanpassung sprechen.“ (دوست دارم دربارهٔ رشدم و تعدیلِ حقوق صحبت کنم.) + دستاوردهایِ مکتوبِ سال! ارقامِ رایجِ افزایش: ۳-۶٪ عادی، ۸-۱۲٪ با ارتقا/نقشِ جدید.'),
        ('۱۳ امساخره و عیدی در آلمان؟', 'Christmas bonus (Weihnachtsgeld) و عیدیِ تعطیلات (Urlaubsgeld) در بعضی قراردادها/شرکت‌ها هست — قانونیِ الزامی نیست! در قرارداد چک کن: بندهای Zusatzleistungen. اگر نیست، همان حقوقِ سالانهٔ تو کلِ عدد است — پس مذاکرهٔ سالانه را جدی بگیر!')
    ],
},

# ── درس ۴۸ ─────────────────────────────────────────────────────────────────
{
    'slug': 'german-leave-sick',
    'title': 'مرخصی و بیماری؛ Urlaub و Krankmeldung',
    'desc': 'دو راحت‌ترین حقوقِ کاریِ آلمان به آلمانی: درخواستِ مرخصی، Krankmeldung (گواهیِ استعلاجی)، قانونِ بیماری و جمله‌های تماسِ صبحگاهی.',
    'keywords': 'مرخصی آلمان, Krankmeldung, گواهی استعلاجی آلمان, Urlaub آلمان, بیماری کاری آلمان',
    'answer': 'مرخصی: زود بپرس („Ich würde gern vom 3. bis 10. Urlaub nehmen — passt das?“)، در سیستم ثبت کن و قبل از رفتن کارها را بسپار. بیمار شدی؟ روزِ اول اطلاع بده (قبل از ۹!)، از روزِ چهارم گواهیِ دکتر الزامی است (Arbeitsunfähigkeitsbescheinigung) و دستمزدت ادامه دارد — قانون!',
    'intro': [
        'آلمان، سرزمینِ مرخصی و بیماریِ انسانی است: ۲۰-۳۰ روزِ مرخصی، بیماریِ پرداخت‌شده و قانونِ سختِ «ساعتِ اطلاعِ صبحگاهی»! این درس هر دو را با جمله‌های عملی می‌سازد — چون اولین سرماخوردگی‌ات، درِ ورود به این سیستم است.',
        'دو قانونِ طلایی از همین حالا: **۱)** مرخصی را زود و کتبی بخواه — حقوقِ قانونی‌ات است ولی برنامه‌ریزیِ تیم، مهربانیِ توست! **۲)** بیماری = روزِ اولِ اطلاعِ فوری + گواهی از روزِ چهارم (خیلی شرکت از روزِ اول می‌خواهد — قرارداد را چک کن!).'
    ],
    'sections': [
        {
            'h2': 'درخواستِ مرخصی؛ سه قدم',
            'blocks': [
                ('ex', 'Ich würde gern vom 12. bis 20. Juli Urlaub nehmen. Passt das für das Team?', 'دوست دارم ۱۲ تا ۲۰ ژوئیه مرخصی باشم. برای تیم مناسب است؟ — سوالِ اول: زود و نرم!'),
                ('ex', 'Ich trage den Urlaub jetzt im System ein. (Ich habe ihn schon eingetragen.)', 'الان مرخصی را در سیستم ثبت می‌کنم. (ثبتش کرده‌ام.) — der Urlaub eintragen = ثبتِ مرخصی؛ فعلِ جدانشدنیِ اداری!'),
                ('ex', 'Vor dem Urlaub übergebe ich meine offenen Tasks an Timo und dokumentiere den Stand.', 'قبل از مرخصی، تسک‌هایِ بازم را به تیمو می‌سپارم و وضعیت را مستند می‌کنم. — übergeben = سپردن؛ آیینِ خداحافظیِ حرفه‌ای!'),
                ('p', 'و سه آدابِ طلایی: مرخصیِ تابستان را ماه‌ها قبل بگو (همه می‌خواهند!)، در هفتهٔ ریلیز نه! و جملهٔ بازگشت: „Ich bin zurück — wie lief’s?“ (برگشتم — چطور گذشت؟)')
            ]
        },
        {
            'h2': 'بیماری؛ قانون و آیینِ صبحِ بیمار',
            'blocks': [
                ('table', ['موقعیت', 'بگو/بکن', 'نکته'],
                    [['روزِ اول — قبل از ۹', 'Ich bin heute krank und kann nicht arbeiten.', 'تماس یا پیام — قبل از شروعِ ساعتِ کاری!'],
                     ['چقدر؟', 'Ich hoffe, morgen wieder da zu sein.', 'حدس بگو؛ لازم نیست قطعی باشد'],
                     ['از روزِ چهارم', 'Arbeitsunfähigkeitsbescheinigung (AU)', 'گواهیِ دکتر — الکترونیک به بیمه و کارفرما می‌رود!'],
                     ['بیمار در مرخصی', 'Ich war im Urlaub krank — zählt das?', 'بله! با گواهی، روزهایِ بیماری به مرخصی برمی‌گردند — قانون!'],
                     ['فرزندِ بیمار', 'Kind-Krank-Tage', 'روزهایِ مراقبتِ بچه — تا ۱۰ روز در سال!']]),
                ('ex', 'Guten Morgen, hier ist Ali. Ich fühle mich nicht gut und bleibe heute zu Hause. Ich melde mich, wenn es besser wird.', 'صبح بخیر، علی هستم. حالِ خوبی ندارم و امروز خانه می‌مانم. وقتی بهتر شد خبر می‌دهم. — پیامِ بیماریِ کامل: نام + وضعیت + برنامه!'),
            ]
        },
        {
            'h2': 'گفتگو: یک هفتهٔ بیماری — از تماس تا بازگشت',
            'blocks': [
                ('ex', 'Tag 1 (an Teamlead): Ich bin seit heute Morgen krank — Fieber. Ich melde mich morgen früh wieder.', 'روزِ اول (به تیم‌لید): از صبح مریضم — تب. فردا صبح دوباره خبر می‌دهم.'),
                ('ex', 'Tag 2: Kein Fieber mehr, aber ich brauche noch einen Tag. — Gute Besserung! Melde dich einfach.', 'روزِ ۲: تب رفته ولی یک روزِ دیگر لازم دارم. — بهبودی! فقط خبر بده. — Gute Besserung! آرزویِ سلامتِ مقدس!'),
                ('ex', 'Tag 4 (an HR): Ich war heute beim Arzt — hier ist die Krankmeldung bis Freitag.', 'روزِ ۴ (به HR): امروز نزد دکتر بودم — این گواهیِ استعلاجی تا جمعه. — die Krankmeldung: واژهٔ رسمیِ مختصرِ AU!'),
                ('ex', 'Rückkehr: Danke für die Genesungswünsche! Ich bin wieder da und fange mit dem Review an.', 'بازگشت: ممنون از آرزوهای سلامت! برگشتم و با ریویو شروع می‌کنم. — die Genesung = بهبودی؛ جملهٔ بازگشتِ گرم!')
            ]
        },
        {
            'h2': 'گرامرِ عمیق‌تر: حالتِ دفعی در جمله‌های اداری —请假َم را با Akkusativ بسپار',
            'blocks': [
                ('p', 'جمله‌هایِ این درس، بهترین تمرینِ Akkusativ واقعی‌اند: „Ich trage **den Urlaub** ein“ (مرخصی را ثبت می‌کنم — der→den!)، „Ich übergebe **die Tasks**“، „Ich brauche **die Krankmeldung**“. و یک فعلِ مخصوصِ مرخصی: **beantragen** (درخواست‌دادنِ رسمی: „Ich beantrage Urlaub für Juli“ — برای ژوئیه مرخصی درخواست می‌کنم). فعلِ beantragen، درخواستِ اداریِ همه‌چیز است: Urlaub، Visum،Krankengeld — با آن، هر فرمِ آلمان جمله می‌شود!'),
            ]
        },
        {
            'h2': 'اشتباه‌های رایجِ فارسی‌زبان‌ها در همین درس',
            'blocks': [
                ('p', 'این بخش را با یک قرارداد بخوان: هر ❌ یعنی «مغزِ فارسی‌زبانت این را می‌سازد و طبیعی است»، و هر ✅ یعنی «این همان چیزی است که گیرندهٔ آلمانی‌زبان می‌شنود». با هر جفت بلند تکرار کن تا شکلِ درست در گوشت نشست کند.'),
                ('ex', '❌ Ich bin krank. tomorrow hoffe ich besser. (مخلوطِ انگلیسی)', '❌ جملهٔ نصفه‌انگلیسی را کاملِ آلمانی کن — سه جملهٔ پیامِ بیماری را از حفظ!'),
                ('ex', '✅ Ich bin krank und bleibe heute zu Hause. Ich melde mich morgen.', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.'),
                ('ex', '❌ (تماسِ ساعتِ ۱۱!)', '❌ اطلاعِ دیر، در آلمان بی‌برنامگی است — قبل از ۹، حتی اگر ۷ باشد!'),
                ('ex', '✅ (پیامِ ۸:۳۰) Ich bin leider krank und komme heute nicht ins Büro.', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.'),
                ('ex', '❌ Mir geht es schlecht aber ich komme. (کارِ قهرمانیِ فرهنگیِ ما!)', '❌ کارِ بیمار در آلمان، بی‌احترامی به سلامتِ عمومی است! خانه بمان، بهتر شو — همین قانونِ فرهنگی!'),
                ('ex', '✅ Ich bleibe heute zu Hause, damit ich schneller gesund werde.', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.')
            ]
        },
        {
            'h2': 'تمرین‌های این درس — چهار قدم، بی‌عجله',
            'blocks': [
                ('p', 'تمرین: یک مرخصی و یک بیماری را کامل اجرا کن:'),
                ('ol', [
                    'درخواستِ مرخصیِ ۲ هفته‌ای را با هر سه قدم اجرا کن: سوال، ثبت، سپردن.',
                    'پیامِ صبحِ بیماری را برای تیم‌لید بنویس — با نام و برنامهٔ خبر.',
                    'دو جملهٔ بیماریِ طولانی بساز: وضعیت + گواهی (Krankmeldung!).',
                    'جملهٔ بازگشت را با Genesungswünsche اجرا کن — و اولین کارت را مشخص کن!'
                ]),
                ('faq', [
                    ('پاسخ تمرین ۱', '„Ich würde gern vom 3. bis 17. August Urlaub nehmen — passt das? Ich trage es ins System ein und übergebe vorher meine offenen Tickets an Timo.“ — سه‌جمله‌ایِ کاملِ مرخصیِ حرفه‌ای!'),
                    ('پاسخ تمرین ۲', '„Guten Morgen Timo, hier ist Ali. Ich fühle mich nicht gut und bleibe heute zu Hause. Ich melde mich morgen früh wieder. Entschuldige die kurze Info.“ — پیامِ کامل: سلام+نام، وضعیت، برنامه، مؤدبیت!'),
                    ('پاسخ تمرین ۳', '„Ich war beim Arzt — die Krankmeldung läuft bis Freitag.“ · „Ich brauche diese Woche noch Ruhe, nächste Woche bin ich wieder da.“ — دو جملهٔ بیماریِ طولانیِ اداری!'),
                    ('پاسخ تمرین ۴', '„Danke für die Genesungswünsche! Ich bin wieder da und fange mit dem offenen Review an — was hat sich verändert?“ — بازگشتِ گرم + شروعِ مشخص + سوالِ وضعیت — بهترین بازگشتِ ممکن!')
                ])
            ]
        },
        {
            'h2': 'چالشِ امروز',
            'blocks': [
                ('quote', '🎯 امروز پیامِ بیماری‌ات را از حفظ کن — سه جمله، کامل، بدونِ فکر! اولین صبحِ بیماریِ آلمانی‌ات، این پیام آماده است و تو فقط دکمهٔ send را می‌زنی.')
            ]
        },
        {
            'h2': 'نکات مکالمهٔ واقعی که کتاب‌ها کم می‌گویند',
            'blocks': [
                ('ul', [
                    '**«Gute Besserung!» را خودت هم بگو** — همکار خبرِ بیماری داد؟ این جمله + یک ایموجی کافی است. فرهنگِ آلمانی، احساسات را کوتاه و مؤدب ابراز می‌کند — این جمله، کلِ آن است!',
                    '**روزهایِ بیماری، مرخصی نیستند — جدا حساب می‌شوند!** — ۶ هفتهٔ بیماری = دستمزدِ کامل از کارفرما؛ بعدش Krankengeld از بیمه! سوالِ رایجِ مهاجرها («مرخصی کم می‌شود؟») — نه! کاملاً جداست. جملهٔ اطمینان: „Krankheitstage gehen nicht vom Urlaub ab“ (روزهایِ بیماری از مرخصی کم نمی‌شوند).',
                    '**Urlaub را می‌شود منتقل کرد — تا ۳۱ مارس!** — روزهایِ استفاده‌نشده تا مارسِ سالِ بعد معمولاً معتبرند (قرارداد چک!). و قانونِ طلاییِ فرهنگی: آلمانیِ درست، مرخصی‌اش را می‌گیرد! «سالانه ۵ روز نگه‌دارم برای تیم» نه — قانون و تعادلِ زندگی، جدی گرفته می‌شوند!'
                ])
            ]
        },
    ],
    'takeaway': 'مرخصی: زود و نرم بخواه („Passt das für das Team?“)، در سیستم ثبت و کارها را بسپار. بیمار؟ قبل از ۹ اطلاع بده، از روزِ چهارم Krankmeldung، و روزهایِ بیماری از مرخصی کم نمی‌شوند! «Gute Besserung!» آرزویِ مقدس و «Ich beantrage …» فعلِ هر درخواستِ اداری است.',
    'faq': [
        ('مرخصیِ ساعتی و «Termine in Arbeitszeit»؟', 'بله — Termin اداری/دکتر در ساعتِ کار:块钱 برو و وقتت را برگردان یا Flexible Zeit بگیر. جمله: „Ich habe morgen einen Behördentermin — ich mache die Stunde am Abend nach.“ (فردا نوبتِ اداره دارم — ساعتش را عصر جبران می‌کنم.) — شفافیت، همه‌چیز است!'),
        ('بیمارِ دورکار (Homeoffice)?', 'همان قانون: اطلاعِ صبح + گواهی از روزِ چهارم. «حالا که خانه‌ام…» نه! بیمار، بیمار است — استراحت کن. فرهنگِ آلمانیِ سالم، مرزِ کار/بیماری را جدی نگه می‌دارد و کارفرمایِ درست، از تو نمی‌خواهد بیمار کار کنی!')
    ],
},

# ── درس ۴۹ ─────────────────────────────────────────────────────────────────
{
    'slug': 'german-tech-interview',
    'title': 'مصاحبهٔ فنی؛ سوال‌های تکنیکال به آلمانی',
    'desc': 'مصاحبهٔ فنیِ آلمانی: معرفیِ پروژه، سوال‌هایِ فنیِ رایج، سوال‌هایِ رفتاری (STAR) و جواب‌های ساختارمند — با واژگانِ مصاحبه.',
    'keywords': 'مصاحبه فنی آلمان, مصاحبه آلمانی, سوال فنی آلمانی, STAR مصاحبه, Vorstellungsgespräch',
    'answer': 'مصاحبهٔ فنیِ آلمانی سه بخش دارد: Vorstellung (معرفی — ۲ دقیقه، ساختارمند!)، Fachfragen (سوال‌های فنی — جواب با «سه‌لایه: تعریف + تجربه + مثال») و Verhaltensfragen (رفتاری — قالبِ STAR: موقعیت، وظیفه، اقدام، نتیجه). جملهٔ طلاییِ زمانِ فکر: „Darf ich kurz nachdenken?“ (می‌توانم لحظه‌ای فکر کنم؟)',
    'intro': [
        'به یکی از مهم‌ترین درس‌های دوره رسیدیم: مصاحبهٔ فنی به آلمانی! واقعیتِ دلگرم‌کننده: مصاحبه‌گرِ آلمانی، زبانِ سادهٔ دقیق و ساختارِ فکر را بیشتر از بلاغت می‌خواهد — جوابِ ساختارمندِ ساده، بهتر از جوابِ شلوغِ روان است!',
        'این درس هر سه بخشِ مصاحبه را می‌سازد: معرفیِ دوقیقه‌ای، الگویِ جوابِ فنی (تعریف + تجربه + مثال) و قالبِ STAR برای سوال‌هایِ رفتاری — با جمله‌هایِ نجاتِ «زمانِ فکر» و «تکرارِ سوال». سلاح‌هایی که مصاحبهٔ بعدی‌ات را آلمانی می‌کنند!'
    ],
    'sections': [
        {
            'h2': 'معرفی؛ دوقیقه‌ایِ ساختارمند',
            'blocks': [
                ('p', 'سوالِ «Erzählen Sie von sich» (از خودتان بگویید) با چهار پارچه جواب می‌شود: **بنیان → مسیر → تخصص → چرا این‌جا**:'),
                ('ex', 'Ich bin Backend-Entwickler mit fünf Jahren Erfahrung, zuerst in Teheran, seit zwei Jahren in Deutschland.', 'توسعه‌دهندهٔ بک‌اند با پنج سال تجربه، اول در تهران، از دو سال پیش در آلمان. — بنیان + مسیر!'),
                ('ex', 'Mein Fokus: verteilte Systeme und APIs. Zuletzt habe ich eine Event-Pipeline mit Kafka aufgebaut.', 'تمرکزم: سیستم‌های توزیع‌شده و APIها. اخیراً یک پایپ‌لاینِ رویداد با کافکا ساخته‌ام. — تخصص + دستاورد!'),
                ('ex', 'Auf Ihre Stelle bin ich aufmerksam geworden, weil Sie an Datentriebwerken arbeiten — genau mein Thema.', 'به جایگاهِ شما توجه کردم چون روی موتورهای داده کار می‌کنید — دقیقاً موضوعِ من. — چرا این‌جا + ارتباطِ واقعی!'),
                ('p', 'چهار جمله = دو دقیقه. تمرین کن با تایمر! و هیچ‌وقت زندگی‌نامه‌ی کامل نخوان — مصاحبه‌گر رزومه را خوانده؛ او «داستانِ» می‌خواهد نه «فهرست» را.'),
            ]
        },
        {
            'h2': 'سوال‌های فنی؛ الگویِ سه‌لایه',
            'blocks': [
                ('table', ['سوالِ رایج', 'لایهٔ ۱: تعریف', 'لایهٔ ۲: تجربه'],
                    [['Was ist Ihre Erfahrung mit …?', 'Kurz: … ist …', 'Ich habe damit … gebaut'],
                     ['Wie würden Sie … lösen?', 'Zuerst würde ich klären: …', 'Ähnliches hatte ich bei …'],
                     ['Was ist der Unterschied X/Y?', 'X ist …, Y dagegen …', 'Ich wähle X, wenn …'],
                     ['Erklären Sie …!', 'Das Konzept ist …', 'Beispiel aus meinem Projekt: …']]),
                ('ex', 'Frage: Wie behandeln Sie Race-Conditions? — Antwort: Erst definiere ich: gleichzeitige Zugriffe auf geteilten Zustand. Dann prüfe ich: Braucht man wirklich Parallelität? In meinem letzten Projekt lösten wir es mit optimistischem Locking.', 'سوال: Race-Condition را چطور مدیریت می‌کنید؟ — جواب: اول تعریف می‌کنم: دسترسی‌های همزمان به وضعیتِ مشترک. بعد می‌پرسم: واقعاً موازی‌سازی لازم است؟ در پروژهٔ اخیرمان با قفل‌گذاریِ خوش‌بینانه حل کردیم. — سه‌لایهٔ کامل: تعریف + روش + مثال!')
            ]
        },
        {
            'h2': 'سوال‌های رفتاری؛ قالبِ STAR',
            'blocks': [
                ('p', 'سوال‌هایِ «نشان بده که چطور» (Erzählen Sie von einem Konflikt / einem Fehler / einer Herausforderung) با **STAR** جواب می‌شوند: **S**ituation (موقعیت)، **T**aufgabe (وظیفهٔ تو)، **A**ktion (اقدام — قلبِ جواب!)، **R**esultat (نتیجه + درس):'),
                ('ex', 'Ein Beispiel für einen Konflikt: (S) Im Release-Stress meinte der PO, das Feature ohne Tests zu shippen. (T) Ich sollte die Qualität sichern. (A) Ich habe einen Kompromiss vorgeschlagen: Feature-Flag plus automatische Smoke-Tests. (R) Der Release lief — und seitdem ist der Test-Check Standard.', 'مثالی از تعارض: (S) در فشارِ ریلیز، PO می‌گفت فیچر بدونِ تست برود. (T) من باید کیفیت را تضمین می‌کردم. (A) سازش پیشنهاد کردم: فیچرفلگ + تست‌های خودکارِ دودی. (R) ریلیز رفت — و از آن موقع چکِ تست، استاندارد شد. — STAR کامل در چهار جمله!')
            ]
        },
        {
            'h2': 'گفتگو: لحظه‌های سختِ مصاحبه',
            'blocks': [
                ('ex', 'Interviewer: Sie haben das Thema erwähnt — können Sie das vertiefen?', 'آن موضوع را گفتید — می‌توانید عمیق‌ترش کنید؟ — vertiefen = عمیق‌ترکردن؛ سوالِ عاشقِ مصاحبه‌گرهایِ آلمانی!'),
                ('ex', 'Du: Gerne. Darf ich kurz anhand eines Beispiels erklären?', 'با کمال میل. می‌توانم کوتاه با یک مثال توضیح دهم؟ — anhand von = به‌کمکِ/با — جملهٔ شروعِ توضیحِ حرفه‌ای!'),
                ('ex', 'Interviewer: Kennen Sie unser Produkt? — Du: Ja, ich habe die Doku und euer Tech-Blog gelesen. Eine Frage dazu: …', 'محصولمان را می‌شناسید؟ — بله، داکیومنت و بلاگِ فنی‌تان را خوانده‌ام. یک سوال در این باره: … — تحقیق + سوالِ هوشمند = امتیازِ دوگانه!'),
                ('ex', 'Du (پایان): Ich habe zwei Fragen: Wie sieht die Teamstruktur aus? Und: Wie messen Sie Erfolg in dieser Rolle?', 'دو سوال دارم: ساختارِ تیم چطور است؟ و: موفقیت را در این نقش چطور می‌سنجید؟ — سوالِ آخرِ تو = امضای حرفه‌ای!'),
                ('p', 'و جملهٔ پایانیِ مصاحبه: „Vielen Dank für das Gespräch — ich freue mich von Ihnen zu hören!“ (ممنون از گفتگو — خوشحال می‌شوم از شما بشنوم!)'),
            ]
        },
        {
            'h2': 'گرامرِ عمیق‌تر: زمانِ حالِ مطمئن در مصاحبه — فعل‌های اول‌شخص',
            'blocks': [
                ('p', 'مصاحبه، صحنهٔ «Ich kann / Ich habe / Ich bin» است — اما دو ظرافتِ آلمانی: **۱)** برای دستاورد گذشته، Perfekt ساده: „Ich habe … gebaut“ (ساخته‌ام) — بدونِ مبالغه؛ **۲)** برای توانایی، می‌توانی/تسلط: „Ich arbeite seit fünf Jahren mit …“ (پنج سال است با … کار می‌کنم) — حالِ استمراریِ اعتبار‌ساز! و خطرِ همیشگی: nicht «Ich bin gut in Java» بلکه «Ich arbeite professionell mit Java» — فعلِ کار، ادعا را به واقعیت می‌بَرد!'),
            ]
        },
        {
            'h2': 'اشتباه‌های رایجِ فارسی‌زبان‌ها در همین درس',
            'blocks': [
                ('p', 'این بخش را با یک قرارداد بخوان: هر ❌ یعنی «مغزِ فارسی‌زبانت این را می‌سازد و طبیعی است»، و هر ✅ یعنی «این همان چیزی است که گیرندهٔ آلمانی‌زبان می‌شنود». با هر جفت بلند تکرار کن تا شکلِ درست در گوشت نشست کند.'),
                ('ex', '❌ (سکوتِ طولانی بعد از سوالِ فنی)', '❌ سکوتِ بلاتکلیف، گیج‌کننده است — جملهٔ زمانِ فکر بگو!'),
                ('ex', '✅ Gute Frage — darf ich kurz nachdenken?', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.'),
                ('ex', '❌ Ich bin experte. Ich kenne alles von Kubernetes.', '❌ ادعایِ مطلق، در فرهنگِ مصاحبهٔ آلمانی زنگِ خطر است — دامنه + تجربه بگو!'),
                ('ex', '✅ Ich arbeite seit drei Jahren produktiv mit Kubernetes — tief bin ich vor allem in Networking.', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.'),
                ('ex', '❌ Das kann ich nicht. (به چیزی که بلد نیستی)', '❌ «نمی‌توانم»ی خالی، درِ بسته! فرمولِ درست: صداقت + یادگیری!'),
                ('ex', '✅ Damit habe ich noch nicht gearbeitet — aber das Konzept kenne ich und lerne schnell.', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.')
            ]
        },
        {
            'h2': 'تمرین‌های این درس — چهار قدم، بی‌عجله',
            'blocks': [
                ('p', 'تمرین: مصاحبهٔ بعدی را همین امروز شروع کن:'),
                ('ol', [
                    'معرفیِ دوقیقه‌ایِ خودت را بنویس و با تایمر اجرا کن — چهار پارچه!',
                    'سه سوالِ فنیِ حوزهٔ خودت را با الگویِ سه‌لایه جواب بده.',
                    'یک STAR کامل بنویس: تعارض/اشتباه/چالشِ واقعی از کارِ خودت.',
                    'سه سوالِ آخرِ خودت را از شرکتِ رویایی‌ات آماده کن — سوالِ امضا!'
                ]),
                ('faq', [
                    ('پاسخ تمرین ۱', 'چهار پارچه: بنیان+مسیر → تخصص+دستاورد → مهارتِ زبان → چرا این‌جا. با تایمرِ ۱۲۰ ثانیه اجرا کن؛ اگر جا ماندی، حذف کن نه اضافه — کوتاهِ کامل، برندهٔ مصاحبه است!'),
                    ('پاسخ تمرین ۲', 'نمونه: „Was ist CAP?“ → „Kurz: Konsistenz, Verfügbarkeit, Partitionstoleranz — man kann zwei wählen. Ich habe das beim Event-Store genutzt: wir wählten AP mit eventual consistency.“ — تعریف + کاربرد؛ سه‌لایهٔ فشرده!'),
                    ('پاسخ تمرین ۳', 'STAR خودت: یک ماجرای واقعی — با اعداد! „(S) Der Release drohte zu kippen. (T) Ich war für die Pipeline. (A) Ich priorisierte die kritischen Tests und zog ein Pair-Review vor. (R) Release pünktlich, Fehlerquote halbiert.“ — چهار جمله، یک داستانِ کامل!'),
                    ('پاسخ تمرین ۴', 'سه سوالِ پایانی: „Wie arbeitet das Team — sync oder async?“ · „Was ist die größte technische Herausforderung gerade?“ · „Wie sieht Erfolg nach sechs Monaten aus?“ — سوال‌هایِ هوشمندِ دوطرفه؛ مصاحبه، گفتگوست نه بازجویی!')
                ])
            ]
        },
        {
            'h2': 'چالشِ امروز',
            'blocks': [
                ('quote', '🎯 امروز معرفیِ دوقیقه‌ای‌ات را ضبط کن — به آلمانی، با تایمر. سه بار گوش بده، بهتر کن، دوباره ضبط. این دو دقیقه، درِ همهٔ مصاحبه‌هایِ آینده‌ات است!')
            ]
        },
        {
            'h2': 'نکات مکالمهٔ واقعی که کتاب‌ها کم می‌گویند',
            'blocks': [
                ('ul', [
                    '**مصاحبهٔ آلمانی = گفتگوی حرفه‌ای، نه نمایش** — مصاحبه‌گرِ آلمانی، صداقتِ «نمی‌دانم + می‌آموزم» را بیشتر از ادعایِ همه‌چیز می‌خواهد. جملهٔ طلایی: „Das habe ich noch nicht gemacht — so würde ich rangehen“ (این را نکرده‌ام — این‌طور جلو می‌رفتم) — راهِ حل، مهم‌تر از دانشِ فعلی است!',
                    '**«Haben Sie Fragen?» = بله، همیشه!** — بدونِ سوال، علاقه‌ات زیر سوال می‌رود! سه سوال از قبل در جیب: تیم، چالش، موفقیت. سوالِ خوب، نیمِ امتیازِ مصاحبه است — آلمانی‌ها این را جدی می‌دانند.',
                    '**بعد از مصاحبه: ایمیلِ تشکرِ کوتاه** — در آلمان، ۴-۵ جمله: تشکر + یک نکتهٔ مشخص از گفتگو + علاقه. „Vielen Dank für das gute Gespräch. Besonders unser Thema Event-Sourcing ist mir in Erinnerung geblieben. Ich freue mich auf Ihre Rückmeldung.“ — شانسی را که هست، چند درصد بالا می‌برد!'
                ])
            ]
        },
    ],
    'takeaway': 'مصاحبهٔ فنی: معرفیِ چهارپارچه (۲ دقیقه!)، جوابِ فنی سه‌لایه (تعریف + روش + مثال)، رفتاری با STAR و جمله‌های نجات: „Darf ich kurz nachdenken?“ «Damit habe ich noch nicht gearbeitet — so würde ich rangehen.» سوالِ آخرِ خودت را داشته باش و ایمیلِ تشکر بفرست!',
    'faq': [
        ('مصاحبه به آلمانی می‌افتد یا انگلیسی؟', 'بسته به شرکت: استارتاپ‌هایِ بین‌المللی معمولاً انگلیسی + یک گفتگویِ «زبان و فرهنگ» آلمانی؛ شرکت‌هایِ سنتی و مشتری‌محور: آلمانی. آمادهٔ هر دو باش و در اولین تماس بپرس: „In welcher Sprache findet das Gespräch statt?“ (گفتگو به چه زبانی برگزار می‌شود؟) — خودِ این سوال، حرفه‌ای بودنت را نشان می‌دهد!'),
        ('Live-Coding به آلمانی؟! چطور آماده شوم؟', 'کامنت‌گذاری و گفتارِ حینِ کدنویسی: „Ich beginne mit dem Interface… jetzt der happy path… dann die edge cases.“ (با اینترفیس شروع می‌کنم… حالا مسیرِ خوش… بعد حالت‌های خاص.) — الگویِ فکرِ بلند (laut denken) را تمرین کن: کد انگلیسی، گفتار آلمانی — دقیقاً معکوسِ استندآپِ تو! سه بار تمرین با تایمر و صدای بلند.')
    ],
},

# ── درس ۵۰ ─────────────────────────────────────────────────────────────────
{
    'slug': 'german-cv-cover-letter',
    'title': 'رزومهٔ آلمانی؛ Lebenslauf و Anschreiben',
    'desc': 'رزومه و انگیزه‌نامهٔ استانداردِ آلمانی: ساختارِ Lebenslauf (با عکس؟ بدون؟!)، قالبِ Anschreiben و جمله‌هایِ فروشِ مهربانِ خودت.',
    'keywords': 'رزومه آلمانی, Lebenslauf, Anschreiben, انگیزه نامه آلمان, درخواست کار آلمان',
    'answer': 'Lebenslauf آلمانی: یک‌صفحه‌ایِ تمیز، ترتیبِ زمانیِ معکوس، **بدونِ عکس** (از ۲۰۱۹ معمول و قانوناً از ۲۰۰۶ ممنوعِ درخواست!)، با تاریخ‌های دقیق و مهارت‌های مشخص. Anschreiben (انگیزه‌نامه): یک صفحه با چهارپارچه — چرا شما، چرا من، چرا حالا، سلام! هر ادعا، با یک مثال!',
    'intro': [
        'بازارِ کارِ آلمان، رزومهٔ استانداردِ خودش را دارد: Lebenslaufِ یک‌صفحه‌ایِ ساختارمند و Anschreibenِ مؤدب — و رزومهٔ آمریکاییِ سه‌صفحه‌ایِ پر از accomplishments-metrics، این‌جا «زیاد» خوانده می‌شود! این درس هر دو سند را می‌سازد.',
        'خبرِ مهم برای مهاجرها: خالی‌بودنِ «آلمانیِ flawless» در رزومه، نقطهٔ ضعفِ پنهان نیست — سطحِ واقعی + مسیرِ یادگیری بنویس، صداقت در آلمان امتیاز است! و قاعدهٔ طلاییِ هر دو سند: هر جمله‌ای که می‌نویسی، باید بتوانی در مصاحبه درباره‌اش پنج دقیقه حرف بزنی!'
    ],
    'sections': [
        {
            'h2': 'Lebenslauf؛ ساختارِ استانداردِ آلمانی',
            'blocks': [
                ('table', ['بخش', 'چه بنویسی', 'نکته'],
                    [['Persönliche Daten', 'نام، آدرس، تلفن، ایمیل، لینکدین/گیت‌هاب', 'بدونِ تاریخِ تولد و وضعیتِ تأهل — جدید: حتی غیرمجازِ درخواست!'],
                     ['Berufserfahrung', 'مسیرِ کاری — زمانیِ معکوس', 'هر شغل: ۲-۳ بولت: چه ساختی + با چه ابزاری'],
                     ['Ausbildung', 'تحصیلات', 'دانشگاه + رشته؛ نمرهٔ final لازم نیست'],
                     ['Kenntnisse', 'مهارت‌ها — دسته‌بندی‌شده', 'Sprachen / Technologien / Sonstiges (مثلاً «Persisch: Muttersprache»!)'],
                     ['Weiterbildung', 'دوره‌ها و گواهی‌ها', 'آلمانیِ در حالِ یادگیری این‌جا درخشش می‌کند!']]),
                ('p', 'سه قانونِ طلایی: **یک صفحه** (جونیور/میدل؛ سنیور: دو)، **فعل‌های دقیق**: entwickelt، aufgebaut، verantwortet (توسعه‌داده، ساخته، مسئول‌بوده) نه «مسئولِ … بودم»، و **تاریخ‌های دقیق**: 03/2023 – 06/2025 (MM/YYYY). آلمانی‌ها تاریخ‌های ناقص را «مشوّش» می‌خوانند!'),
            ]
        },
        {
            'h2': 'Anschreiben؛ چهارپارچهٔ انگیزه',
            'blocks': [
                ('ex', 'Betreff: Bewerbung als Backend-Entwickler — Referenz 4521', 'موضوع: درخواست برای توسعه‌دهندهٔ بک‌اند — کدِ ۴۵۲۱ — Betreff دقیق با شمارهٔ آگهی!'),
                ('ex', 'چرا شما: Ihre Tech-Blog-Posts über Event-Sourcing haben mich auf Ihre Stelle aufmerksam gemacht.', 'نوشته‌های بلاگِ فنی‌تان دربارهٔ ایونت‌سورسینگ مرا به جایگاه‌تان کشاند. — تحقیقِ واقعی، نه تعریفِ کلی!'),
                ('ex', 'چرا من: In meinem aktuellen Projekt habe ich eine Kafka-Pipeline für 2 Mio. Events pro Tag gebaut.', 'در پروژهٔ فعلی‌ام پایپ‌لاینِ کافکا برای ۲ میلیون رویداد در روز ساخته‌ام. — دستاورد + عدد!'),
                ('ex', 'چرا حالا: Ich möchte in einem Team arbeiten, das Data-Engineering ernst nimmt — und Deutsch ist für mich Teil des Weges.', 'می‌خواهم در تیمی کار کنم که مهندسیِ داده را جدی می‌گیرد — و آلمانی برایم بخشی از مسیر است. — انگیزهٔ دوسویه: آن‌ها + تو + زبان!')
            ]
        },
        {
            'h2': 'گفتگو: ایمیلِ ارسالِ درخواست',
            'blocks': [
                ('ex', 'Sehr geehrte Damen und Herren,\nanbei sende ich meine Bewerbung als Backend-Entwickler. Lebenslauf und Zeugnisse finden Sie im Anhang.\nMit freundlichen Grüßen, Ali Moussavi', 'احترام‌دار خانم‌ها و آقایان،\nبدین‌وسیله درخواستم برای توسعه‌دهندهٔ بک‌اند را می‌فرستم. رزومه و مدارک در پیوست‌اند.\nبا احترام — anbei sende ich = بدین‌وسیله می‌فرستم؛ فرمولِ مقدسِ ایمیلِ درخواست!'),
                ('p', 'سه واژهٔ پیوست: **der Anhang** (پیوست)، **anbei** (به‌پیوست)، **die Bewerbung** (درخواستِ کاری — کلِ مجموعه!). و نکتهٔ فنی: PDF واحد بهتر از چند فایل — «Lebenslauf_Ali_Moussavi.pdf» با نامِ فایلِ تمیز و لاتین!'),
            ]
        },
        {
            'h2': 'گرامرِ عمیق‌تر: فعل‌های رزومه — Perfektِ کوتاه و قدرتمند',
            'blocks': [
                ('p', 'رزومهٔ آلمانی، فعل‌های Perfektِ فشرده می‌خواهد (بدونِ haben/sein!): **entwickelt** (توسعه‌داده)، **aufgebaut** (ساخته/راه‌اندازی‌کرده)، **verantwortet** (مسئولِ آن بوده)، **optimiert** (بهینه‌کرده)، **migriert** (مهاجرت‌داده)، **reduziert/erhöht** (کاهش/افزایش‌داده — با عدد!). قالبِ بولتِ کامل: „**Kafka-Pipeline aufgebaut** — 2 Mio. Events/Tag, Latenz um 40% reduziert“ — فعل + عدد + اثر. هر بولتِ بدونِ عدد، فرصتِ ازدست‌رفتهٔ اثبات است!'),
            ]
        },
        {
            'h2': 'اشتباه‌های رایجِ فارسی‌زبان‌ها در همین درس',
            'blocks': [
                ('p', 'این بخش را با یک قرارداد بخوان: هر ❌ یعنی «مغزِ فارسی‌زبانت این را می‌سازد و طبیعی است»، و هر ✅ یعنی «این همان چیزی است که گیرندهٔ آلمانی‌زبان می‌شنود». با هر جفت بلند تکرار کن تا شکلِ درست در گوشت نشست کند.'),
                ('ex', '❌ (عکسِ رسمی در رزومه)', '❌ عکس، سنتِ قدیمی است — امروز اختیاری و برای مهاجرها گاهی منفی (تمایزِ ناخواسته)! رزومهٔ بدونِ عکس = مدرن و استاندارد!'),
                ('ex', '✅ (بدونِ عکس، با لینکِ گیت‌هاب و لینکدین)', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.'),
                ('ex', '❌ Ich bin verantwortlich für alles.', '❌ «مسئولِ همه‌چیز» — حرفِ کلیدیِ مشکل‌سازِ ترجمهٔ مستقیم؛ دقیق و فنی بگو!'),
                ('ex', '✅ Ich habe die CI-Pipeline verantwortet und die Deploy-Zeit halbiert.', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.'),
                ('ex', '❌ Deutsch: gut (وقتی A1 هستی!)', '❌ سطحِ متورم در رزومهٔ آلمانی، بمبِ ساعتی است — اولین تماس، آشکارش می‌کند!'),
                ('ex', '✅ Deutsch: B1 (laufend), Englisch: fließend', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.')
            ]
        },
        {
            'h2': 'تمرین‌های این درس — چهار قدم، بی‌عجله',
            'blocks': [
                ('p', 'تمرین: هر دو سند را همین امروز بساز:'),
                ('ol', [
                    'پنج بولتِ رزومه برای شغلِ آخرت بنویس — با فعلِ Perfekt + عدد!',
                    'بخشِ Kenntnisse را بساز: سه دسته، سطح‌های صادقانه.',
                    'پاراگرافِ «چرا شما» را برای یک شرکتِ واقعی بنویس — با یک جزئیاتِ واقعی از آن‌ها!',
                    'ایمیلِ ارسالِ درخواست را کامل بنویس — چهار جملهٔ ثابت!'
                ]),
                ('faq', [
                    ('پاسخ تمرین ۱', 'نمونه: „Event-Pipeline aufgebaut — 2 Mio. Events/Tag“ · „Latenz um 40% reduziert“ · „Team von 4 Entwicklern fachlich geführt“ · „Postgres auf TimescaleDB migriert“ · „Onboarding-Doku erstellt — Ramp-up von 6 auf 2 Wochen“ — پنج بولت، پنج عدد، پنج اثر!'),
                    ('پاسخ تمرین ۲', '„Sprachen: Persisch (Muttersprache), Englisch (fließend), Deutsch (B1, laufend) · Technologien: Kotlin, Spring, Kafka, Postgres, K8s (Grundlagen) · Methoden: Scrum, TDD, Clean Code“ — سه دسته، سطح‌های واقعی؛ laufend = در حالِ ادامه!'),
                    ('پاسخ تمرین ۳', '„Ihre Stellenanzeige nennt ‚Event-Driven Architecture first‘ — genau dort habe ich die letzten zwei Jahre gearbeitet: eine Kafka-Pipeline, die heute 2 Mio. Events am Tag verarbeitet.“ — جزئیاتِ آگهی + دستاوردِ متصل؛ پاراگرافِ برندهٔ «چرا شما»!'),
                    ('پاسخ تمرین ۴', '„Sehr geehrte Damen und Herren, anbei sende ich meine Bewerbung als Backend-Entwickler (Ref. 4521). Lebenslauf und Zeugnisse finden Sie im Anhang. Für Rückfragen stehe ich gerne zur Verfügung. Mit freundlichen Grüßen, Ali Moussavi“ — چهار جمله؛ ایمیلِ درخواستِ آمادهٔ ارسال!')
                ])
            ]
        },
        {
            'h2': 'چالشِ امروز',
            'blocks': [
                ('quote', '🎯 امروز یک بولتِ واقعی به رزومه‌ات اضافه کن — با فعلِ Perfektِ آلمانی و یک عدد. حتی اگر فعلاً به انگلیسی داری برای آلمان درخواست می‌دهی، بولت‌های عدددارِ آلمانی، آرزو را برنامه می‌کنند!')
            ]
        },
        {
            'h2': 'نکات مکالمهٔ واقعی که کتاب‌ها کم می‌گویند',
            'blocks': [
                ('ul', [
                    '**Arbeitszeugnis! سنتِ منحصربه‌فردِ آلمان** — با هر خروجی از شرکتی، حقِ داری «گواهیِ کار» بگیری: سندِ رسمیِ مهرشده با نقش و عملکرد. جملهٔ درخواست: „Ich würde gern ein qualifiziertes Arbeitszeugnis erhalten.“ (دوست دارم گواهیِ کارِ کیفی بگیرم.) — در رزومهٔ بعدی‌ات می‌نشیند و آلمان عاشقش است!',
                    '**Keywordها را از آگهی بردار** — سیستم‌هایِ ردیابیِ متقاضی (ATS) آلمانی هم کلمه‌ها را می‌شمارند! پنج کلیدواژهٔ فنیِ آگهی را عیناً در رزومه/انگیزه بگذار — با شرحِ صادقانه. جملهٔ کلاسیک: „Soll-Kriterien aus der Anzeige erfülle ich wie folgt …“ (معیارهایِ آگهی را این‌طور دارم …)',
                    '**نسبتِ Anschreiben واقعی: ۶۰٪ دربارهٔ آن‌ها** — انگیزه‌نامهٔ بد: «من من من»؛ خوب: نصفش دربارهٔ شرکت و نقش! اگر پاراگرافِ اولت بدونِ نامِ شرکت هم خوانده شود، مشکل داری — شخصی‌سازی، خطِ آغازینِ عشقِ آلمانیِ HR است!'
                ])
            ]
        },
    ],
    'takeaway': 'Lebenslauf: یک صفحه، بدونِ عکس، تاریخِ دقیق، فعل‌های Perfekt (aufgebaut، optimiert) و عدد در هر بولت. Anschreiben: چرا شما (جزئیاتِ واقعی!)، چرا من (دستاورد+عدد)، چرا حالا. ایمیل: „Anbei sende ich meine Bewerbung…“ و Arbeitszeugnis حقِ توست — بخواهش!',
    'faq': [
        ('از کجا بفهمم شرکتِ خوبی است؟', 'سه منبع: kununu.com (نقدِ ناشناسِ کارمندان — آلمانی‌ها عاشقش‌اند!)، گلاسدورِ آلمان و بلاگِ فنیِ خودِ شرکت. جملهٔ مصاحبه: „Ich habe die Bewertungen auf Kununu gelesen — wie beschreiben Sie selbst die Kultur?“ — تحقیق + سوالِ دوطرفه!'),
        ('حداقلِ مدارک برای درخواست؟', 'سه‌تاییِ استاندارد: Lebenslauf + Anschreiben + Zeugnisse (دانشگاهی/کاریِ موجود). برای مهاجرها: مدرکِ زبانِ آلمانی اگر هست و پاسپورت/اجازهٔ کار در مرحلهٔ بعد. جملهٔ اطمینانِ اولیه: „Mein Visum ist in Arbeit — Start könnte ab März sein.“ (ویزام در جریان است — شروع می‌تواند از مارس باشد.) — شفافیتِ وضعیتِ ویزا، پرسشِ HR را پیش می‌بَرد!')
    ],
},

# ── درس ۵۱ ─────────────────────────────────────────────────────────────────
{
    'slug': 'german-linkedin-networking',
    'title': 'شبکه‌سازی؛ لینکدین و میت‌آپ به آلمانی',
    'desc': 'شبکه‌سازیِ حرفه‌ای در آلمان: پروفایلِ لینکدینِ آلمانی‌پسند، پیامِ سرد (Kurznachricht)، رویدادها و جمله‌های «دنبالم کن»!',
    'keywords': 'شبکه سازی آلمان, لینکدین آلمان, XING, میتاپ آلمان, networking آلمانی',
    'answer': 'شبکه‌سازیِ آلمانی = محتوا + برنامه + پیگیری: پیامِ سردِ کوتاه (۳ جمله: کیستی، چرا او، چه می‌خواهی)، حضورِ منظم در Meetupهایِ فنی و پیگیریِ دو روزِ بعد («Schön, Sie getroffen zu haben!»). XING هم هنوز در آلمان زنده است — پروفایل‌های هر دو را داشته باش!',
    'intro': [
        '«شبکه‌سازی» در آلمان کلمهٔ بدی نیست — فقط آلمانی‌تر است: کم‌تر «پارتیِ بیزینس»، بیشتر «گفتگویِ محتوا‌محور و پیگیرانه»! این درس ابزارهایش را می‌سازد: پیامِ سردِ محترمانه، گفتگو در رویداد و پیگیریِ بعدش.',
        'و یک واقعیتِ بازارِ آلمان: خیلی از فرصت‌ها هرگز آگهی نمی‌شوند — از شبکه می‌آیند (عبارتِ معروف: „Vitamin B“ — B یعنی Beziehungen: روابط!). برای مهاجرِ تازه، شبکه = پلِ میانِ «خارجیِ بااستعداد» و «همکارِ شناخته‌شده»!'
    ],
    'sections': [
        {
            'h2': 'پیامِ سرد؛ سه‌جمله‌ایِ طلایی',
            'blocks': [
                ('ex', ' Hallo Sarah, ich bin Backend-Entwickler und lese Ihre Posts zur Event-Architektur seit Monaten — besonders der über Outbox-Pattern war stark.', 'سلام سارا، توسعه‌دهندهٔ بک‌اندم و ماه‌هاست نوشته‌هایتان دربارهٔ معماریِ رویداد را می‌خوانم — مخصوصاً آن یکی دربارهٔ الگوی اوت‌باکس قوی بود. — جملهٔ ۱: که هستم + دلیلِ واقعیِ نوشتن (جزئیات!)'),
                ('ex', 'Ich ziehe gerade meine Pipeline von RabbitMQ auf Kafka um — Ihre Erfahrung würde mir sehr helfen.', 'در حالِ انتقالِ پایپ‌لاینم از ربیت‌به کافکا هستم — تجربهٔ شما خیلی کمکم می‌کند. — جملهٔ ۲: درخواستِ مشخصِ کوچک!'),
                ('ex', 'Hätten Sie 15 Minuten für einen kurzen Austausch — oder darf ich Ihnen zwei konkrete Fragen schicken?', '۱۵ دقیقه برای یک گفتگویِ کوتاه دارید — یا می‌توانم دو سوالِ مشخص بفرستم؟ — جملهٔ ۳: گزینهٔ سبک + بی‌فشار!'),
                ('p', 'سه ممنوعهٔ پیامِ سردِ آلمانی: متنِ بلندِ بی‌هدف، درخواستِ «به من کار بده» در پیامِ اول و کپی-پیستِ بی‌شخصی. فرمول: **جزئیاتِ واقعی + درخواستِ کوچک + گزینه‌ها**!'),
            ]
        },
        {
            'h2': 'در رویداد؛ سه جملهٔ شروعِ گفتگو',
            'blocks': [
                ('ex', 'Welchen Vortrag fandest du am besten? — Den über WASM — die Demos waren stark!', 'کدام ارائه را بهتر liked کردی؟ — آن یکی دربارهٔ وسم — دموهاش قوی بود! — سوالِ بازِ استانداردِ هر رویداد!'),
                ('ex', 'Woran arbeitest du gerade? — An einer Matching-Engine — und du?', 'روی چی کار می‌کنی؟ — روی یک موتورِ تطبیق — و تو؟ — سوالِ طلاییِ درس ۳۱، این‌بار در نسخهٔ رویدادی!'),
                ('ex', 'Bist du zum ersten Mal hier? Ich auch — lass uns zusammen durch die Poster laufen!', 'اولین بارت این‌جاست؟ من هم — بیا با هم استندها را بگردیم! — جملهٔ دوست‌یابیِ رویدادی — شروعِ هم‌سفری!')
            ]
        },
        {
            'h2': 'گفتگو: بعد از رویداد — پیگیریِ دو روزه',
            'blocks': [
                ('ex', 'Hallo Timo, schön, dich gestern beim Java-Meetup getroffen zu haben!', 'سلام تیمو، خوشحالم که دیروز در میتاپِ جاوا تورا دیدم! — die Vergangenheit: getroffen haben — شروعِ استانداردِ پیگیری!'),
                ('ex', 'Dein Tipp zu Virtual Threads hat mir schon geholfen — ich habe ihn heute ausprobiert.', 'نکته‌ات دربارهٔ ویرچوال‌تردها کمکم کرد — امروز امتحانش کردم. — ارزشِ واقعی: نکته را به‌کار بردن!'),
                ('ex', 'Wenn du magst: Kaffee oder ein kurzer Call zum Thema Load-Testing? Ich zeige dir dafür unsere Setup.', 'اگر دوست داشتی: قهوه یا کالِ کوتاه دربارهٔ تستِ بار؟ من هم ستاپمان را نشانت می‌دهم. — پیشنهادِ دوطرفه — شبکه = داد و ستد!'),
                ('p', 'و روی لینکدین، جملهٔ نهاییِ قبولِ کانکشن: „Danke für die Vernetzung!“ (ممنون از وصل‌شدن!) — چهار کلمه که مؤدبیتِ آلمانیِ دیجیتالت را امضا می‌کند.'),
            ]
        },
        {
            'h2': 'گرامرِ عمیق‌تر: گذشتهٔ گفتگو در پیام‌ها — Perfektِ شبکه',
            'blocks': [
                ('p', 'پیام‌هایِ شبکه، پر از «دیروز/آن موقع … کردم» هستند و موتورشان Perfekt است (درس ۷۳ کاملش می‌کند؛ فعلاً سه قالبِ پرکاربرد): **getroffen haben** (دیده‌بودن: „schön, Sie getroffen zu haben“)، **gesprochen haben** (حرف‌زده‌بودن: „Wir haben kurz über X gesprochen“)، **geschickt/bekommen haben** (فرستاده/گرفته‌بودن: „Danke für das Paper, das Sie geschickt haben“). این سه + جملهٔ «Ich habe es ausprobiert» (امتحانش کردم) = کلِ بازاریابیِ شخصیِ پیگیری‌هایت!'),
            ]
        },
        {
            'h2': 'اشتباه‌های رایجِ فارسی‌زبان‌ها در همین درس',
            'blocks': [
                ('p', 'این بخش را با یک قرارداد بخوان: هر ❌ یعنی «مغزِ فارسی‌زبانت این را می‌سازد و طبیعی است»، و هر ✅ یعنی «این همان چیزی است که گیرندهٔ آلمانی‌زبان می‌شنود». با هر جفت بلند تکرار کن تا شکلِ درست در گوشت نشست کند.'),
                ('ex', '❌ Hi, please check my profile. I need job.', '❌ پیامِ مستأصلانهٔ کپی‌شده — در آلمان فوراً بلاک می‌شود! فرمولِ سه‌جمله‌ای را اجرا کن!'),
                ('ex', '✅ Hallo [Name], ich bin … und lese Ihre Posts zu X. Hätten Sie 15 Minuten für einen Austausch?', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.'),
                ('ex', '❌ (بعد از رویداد: سکوت!)', '❌ رویداد بدونِ پیگیری = سرمایه‌گذاریِ فراموش‌شده! دو روز بعد پیام بده — سه جمله!'),
                ('ex', '✅ Schön, dich gestern getroffen zu haben! Dein Tipp hat mir geholfen.', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.'),
                ('ex', '❌ Können Sie mir einen Job geben? (مستقیم به رئیسِ شرکتِ ناشناس)', '❌ درخواستِ مستقیمِ کار از شبکهٔ سرد، در فرهنگِ آلمانی «فشار» است؛ درخواستِ «گفتگو» کن — کار خودش می‌آید!'),
                ('ex', '✅ Ich baue gerade mein Netzwerk in Berlin auf — ein kurzer Austausch wäre für mich wertvoll.', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.')
            ]
        },
        {
            'h2': 'تمرین‌های این درس — چهار قدم، بی‌عجله',
            'blocks': [
                ('p', 'تمرین: این هفته سه پیامِ واقعی بفرست!'),
                ('ol', [
                    'یک پیامِ سردِ سه‌جمله‌ای بنویس — به یک نفرِ واقعی از حوزه‌ات (لینکدین!).',
                    'سه جملهٔ رویدادی را تمرین کن — برای میتاپِ بعدیِ شهرت.',
                    'یک پیامِ پیگیری بنویس — بعد از آخرین گفتگوی/رویدادِ واقعی‌ات.',
                    'پروفایلِ لینکدینت را آلمانی‌بینی کن: عنوان (Headline) دو‌زبانه — بنویسش!'
                ]),
                ('faq', [
                    ('پاسخ تمرین ۱', '„Hallo [Name], ich bin Backend-Entwickler aus Berlin und lese Ihre Posts zu Kafka seit einiger Zeit — besonders der über Consumer-Rebalancing war hilfreich. Ich migriere gerade eine Pipeline und hätte zwei kurze Fragen. Hätten Sie 15 Minuten — oder soll ich die Fragen einfach hier schicken?“ — سه‌جمله‌ایِ کاملِ سردِ محترمانه!'),
                    ('پاسخ تمرین ۲', '„Welchen Vortrag fandest du am besten?“ · „Woran arbeitest du gerade?“ · „Bist du zum ersten Mal hier?“ — سه جمله = یک شبِ گفتگو در هر میتاپ!'),
                    ('پاسخ تمرین ۳', '„Hallo [Name], schön, dich gestern getroffen zu haben! Dein Tipp zu X hat sofort geholfen — danke dafür! Wenn du magst, treffen wir uns mal auf einen Kaffee: ich zeige dir dafür unser Setup zu Y.“ — پیگیریِ کامل: خاطره + ارزش + پیشنهادِ دوطرفه!'),
                    ('پاسخ تمرین ۴', '„Backend-Entwickler | Kotlin & Kafka | offen für neue Rollen in Berlin | Deutsch B1+“ — عنوانِ دو‌زبانه؛ کلمهٔ offen für neue Rollen (باز برای نقش‌های جدید) عبارتِ استانداردِ «جویندهٔ کار» در لینکدینِ آلمان است!')
                ])
            ]
        },
        {
            'h2': 'چالشِ امروز',
            'blocks': [
                ('quote', '🎯 امروز یک پیامِ سردِ واقعی بفرست — سه جمله، به یک نفرِ واقعی، با یک جزئیاتِ واقعی از کارهایشان. شبکه با یک پیام شروع می‌شود — امروز!')
            ]
        },
        {
            'h2': 'نکات مکالمهٔ واقعی که کتاب‌ها کم می‌گویند',
            'blocks': [
                ('ul', [
                    '**XING هنوز در آلمان زنده است!** — در بازارهایِ سنتی (HR، صنعت، مشاوره) XING جدی است؛ در فنی، لینکدین پادشاه. اگر صنعتِ سنتی را می‌خواهی، هر دو پروفایل — جملهٔ ساده: «Sie finden mich auch auf XING» (مرا در زیکس هم پیدا می‌کنید)',
                    '**«Kennst du jemanden, der …?» جادوی شبکهٔ آلمانی است** — آلمانی‌ها معرفی‌گری را دوست دارند: „Kennst du jemanden, der Erfahrung mit Data Contracts hat?“ (کسی را می‌شناسی که با قراردادهای داده تجربه داشته باشد؟) — این سوال در پست/پیام، شبکه را باز می‌کند!',
                    '**رویدادهایِ فنیِ آلمان، رایگان و صمیمی‌اند** — Meetup، user groups (Java, Kotlin, Rust…) و کنفرانس‌هایِ محلی؛ نکتهٔ طلایی: بعد از هر رویداد، دو نفرِ آشنای جدید + یک پیامِ پیگیری = قانونِ سه‌تاییِ رشدِ شبکه. ثبات > شدت: ماهی یک رویداد، سالی دوازده رویداد، صدها آشنایی!'
                ])
            ]
        },
    ],
    'takeaway': 'شبکه‌سازیِ آلمانی: پیامِ سردِ سه‌جمله‌ای (کیستی + جزئیاتِ واقعی + درخواستِ کوچک)، سه جملهٔ رویداد (کدام ارائه؟ روی چی؟ اولین بار؟) و پیگیریِ دو روزِ بعد با «Schön, dich getroffen zu haben!». عنوانِ لینکدین دو‌زبانه و «Kennst du jemanden, der …?» جادوی شبکه است.',
    'faq': [
        ('چطور بپرسم آیا جایی خالی است — بدونِ رودربایستی؟', 'قالبِ نرمِ آلمانی: „Ich suche gerade nach neuen Herausforderungen als … — falls in Ihrem Team etwas Passendes ansteht, würde ich mich über einen Chat freuen.“ (این روزها دنبالِ چالشِ جدیدی به‌عنوانِ … هستم — اگر در تیمِ شما چیزی مناسب در راه است، از یک گفتگو خوشحال می‌شوم.) — نه درخواستِ مستقیم، نه پنهان‌کاری؛ همون «درِ باز»!'),
        ('میتاپ‌ها را کجا پیدا کنم؟', 'meetup.com (دستهٔ Tech شهرت)، رویدادهایِ dev.io/devtalks محلی، و LinkedIn Events. در برلین/مونیخ/هامبورگ هر هفته ده‌ها رویدادِ فنی است! جملهٔ اولِ ورود، از درسِ امروز: „Hi, ich bin Ali — ich bin neu in der Community.“ (سلام، علی‌ام — تازه به این جمع آمده‌ام.) — صداقتِ تازه‌وارد، بهترین یخ‌شکنِ دنیاست!')
    ],
},

# ── درس ۵۲ ─────────────────────────────────────────────────────────────────
{
    'slug': 'german-phase3-review',
    'title': 'جمع‌بندی فاز ۳؛ یک هفتهٔ کاریِ کامل به آلمانی',
    'desc': 'هرچه در نوزده درسِ فازِ کاری ساختی، در پنج روزِ یک هفتهٔ واقعیِ کاری جمع می‌شود — از استندآپِ دوشنبه تا Feierabendِ جمعه.',
    'keywords': 'جمع بندی فاز سه, آلمانی کاری, هفته کاری آلمان, مرور آلمانی فنی, محیط کار آلمان',
    'answer': 'فاز ۳ تمام شد و تو «همکارِ کاملِ آلمانی‌زبان» هستی: استندآپ می‌دهی، ایمیل و چت می‌نویسی، ریویو می‌کنی، در جلسه نظر می‌دهی، وضعیت و تأخیر را صادقانه می‌گویی، باگ را گزارش می‌کنی، مذاکره می‌کنی و… این درس، همه‌اش در یک هفتهٔ پیوسته!',
    'intro': [
        'نوزده درسِ فاز ۳ تمام شد — فازِ‌ای که این دوره برایش ساخته شد! وقتِ آزمونِ نهایی است: یک هفتهٔ کاریِ کامل، دوشنبه تا جمعه، فقط با جعبه‌ابزارِ همین فاز. هر روز سه صحنه، هر صحنه از یک درس.',
        'اگر هفته روان اجرا شد، فاز ۴ (مهاجرت و اداره) برایت فقط «مکملِ بوروکراتیک» است و نه مانع — چون تو الان زبانِ کار را داری. اگر جایی گیر کردی، همان درس را سه روز مرور کن؛ سرمایهٔ فاز ۴، همین هفتهٔ فاز ۳ است!'
    ],
    'sections': [
        {
            'h2': 'چک‌لیستِ فاز ۳؛ چهارده ابزارِ کاری',
            'blocks': [
                ('table', ['ابزار', 'قالبِ نمونه'],
                    [['معرفی', 'Ich bin Ali, ich fange heute als … an.'],
                     ['استندآپ', 'Gestern habe ich … , heute möchte ich … , kein Blocker.'],
                     ['ایمیل', 'Könntest du …? / Nur eine kurze Nachfrage …'],
                     ['چت', 'Hast du kurz Zeit? / Das könnte an … liegen.'],
                     ['ریویو', 'Man könnte … / Aus Neugier: warum …?'],
                     ['جلسه', 'Ich sehe das anders, weil … / Ich würde vorschlagen …'],
                     ['وضعیت', 'Ich bin bei 70 Prozent — ich rechne mit Donnerstag.'],
                     ['تأخیر', 'Es sieht nach Verzögerung aus — neuer Termin: …'],
                     ['باگ', 'Erwartet: X. Tatsächlich: Y. Reproduktion: …'],
                     ['دیپلوی', 'Wir fahren hoch — keine Merges! Alles grün!'],
                     ['گیت', 'Ich pushe / Ich rebase auf main.'],
                     ['۱:۱', 'Ich würde gern mehr Verantwortung übernehmen.'],
                     ['قرارداد', 'Halte ich für angemessen — Gibt es Spielraum?'],
                     ['مصاحبه', 'Darf ich kurz nachdenken? / Damit habe ich noch nicht gearbeitet, aber so würde ich rangehen.']]),
                ('p', 'چهارده ابزار = چهارده صحنهٔ هفته. حالا هفته را اجرا کنیم!'),
            ]
        },
        {
            'h2': 'دوشنبه؛ شروعِ هفته',
            'blocks': [
                ('ex', 'Guten Morgen! Gestern habe ich die Tests gefixt, heute arbeite ich am Ticket 452. Kein Blocker.', 'استندآپِ دوشنبه — سه‌جمله‌ایِ استاندارد!'),
                ('ex', 'Nach dem Daily: Hallo Sarah, hast du kurz Zeit? Kurze Frage zum API-Contract.', 'بعد از دیلی: سوالِ چتیِ محترمانه — جفتِ «کوتاه»!'),
                ('ex', 'Mittags: Wir gehen Mittagessen — kommst du mit? — Klar! Guten Appetit!', 'ناهار: دعوت + آرزویِ غذایی — زندگیِ اجتماعیِ کار!'),
                ('ex', 'Nachmittags: Ich habe einen Bug gefunden: Erwartet 200, tatsächlich 500. Ich kann ihn reproduzieren.', 'بعدازظهر: گزارشِ باگِ چهارپارچه — فشرده!')
            ]
        },
        {
            'h2': 'سه‌شنبه تا چهارشنبه؛ اوجِ هفته',
            'blocks': [
                ('ex', 'Dienstag: Ich sehe das anders — die Microservices kosten uns mehr Betrieb. Ich würde einen modular Monolith vorschlagen.', 'سه‌شنبه: جلسهٔ معماری — مخالفتِ سه‌پارچه!'),
                ('ex', 'Dienstag: Status: Ich bin bei 80 Prozent, Restarbeit ca. 3 Stunden. Ich rechne mit morgen früh.', 'وضعیتِ دقیق با عدد — سرمایهٔ اعتبار!'),
                ('ex', 'Mittwoch: Review von Timos PR: Sauber! Zwei Anmerkungen: Man könnte die Funktion aufteilen, und aus Neugier — warum kein Early-Return?', 'چهارشنبه: ریویو — تعریف + نقدِ نرم + سوالِ کنجکاو!'),
                ('ex', 'Mittwoch: Der Build ist rot — ich rebase auf main und fixe den Konflikt.', 'گیتِ روزمره در دو فعل!')
            ]
        },
        {
            'h2': 'پنجشنبه تا جمعه؛ پایانِ هفته',
            'blocks': [
                ('ex', 'Donnerstag: Wir fahren um 17 Uhr hoch — bitte keine Merges bis 18! … Deploy ist durch, alles grün! 🎉', 'پنجشنبه: دیپلویِ کامل — از freeze تا جشن!'),
                ('ex', 'Freitag: Im 1:1: Insgesamt gut. Ich würde gern die Testumgebung betreuen — lass uns das als Ziel aufschreiben.', 'جمعه: جلسهٔ ۱:۱ — وضعیت + آرزویِ هدف‌دار!'),
                ('ex', 'Freitag: Ich nehme mir das Wochenende frei — schön, dass der Sprint gut gelaufen ist.', 'مرخصیِ رضایت‌بخشِ پایانِ اسپرینت!'),
                ('ex', 'Freitag, 17 Uhr: So, Feierabend! Schönen Feierabend euch allen — bis Montag!', 'جملهٔ مقدسِ ساعتِ پنجِ جمعه — پایانِ هفتهٔ کاملِ آلمانی!')
            ]
        },
        {
            'h2': 'گرامرِ عمیق‌تر: هفته‌ات در یک پاراگرافِ Perfect',
            'blocks': [
                ('p', 'کلِ هفته را در یک پاراگرافِ گذشته ببند — این پاراگراف، آزمونِ عملیِ فاز ۳ و پیش‌نمایشِ درس ۷۳ (Perfekt) است:'),
                ('ex', 'Am Montag habe ich einen Bug gemeldet und die Tests gefixt. Am Dienstag habe ich in der Architektur-Diskussion einen Modular-Monolithen vorgeschlagen. Am Mittwoch habe ich Timos PR gereviewt und einen Merge-Konflikt gelöst. Am Donnerstag haben wir die neue Version deployed — alles grün. Am Freitag habe ich im 1:1 ein neues Ziel vereinbart und dann: Feierabend!', 'دوشنبه باگی را گزارش و تست‌ها را فیکس کردم. سه‌شنبه در بحثِ معماری مونولیتِ ماژولار پیشنهاد دادم. چهارشنبه PR تیمو را ریویو و یک تضادِ مرج را حل کردم. پنجشنبه نسخهٔ جدید را دیپلوی کردیم — همه‌چیز سبز. جمعه در ۱:۱ هدفِ جدیدی توافق کردم و بعد: Feierabend! — هفتهٔ کامل، دهها فعلِ Perfekt!')
            ]
        },
        {
            'h2': 'اشتباه‌های رایجِ فارسی‌زبان‌ها در همین درس',
            'blocks': [
                ('p', 'این بخش را با یک قرارداد بخوان: هر ❌ یعنی «مغزِ فارسی‌زبانت این را می‌سازد و طبیعی است»، و هر ✅ یعنی «این همان چیزی است که گیرندهٔ آلمانی‌زبان می‌شنود». با هر جفت بلند تکرار کن تا شکلِ درست در گوشت نشست کند.'),
                ('ex', '❌ Am Montag, ich habe einen Bug gemeldet. (جای فعل!)', '❌ قانونِ جای دوم، در گذشته هم زنده است: Am Montag habe ich …'),
                ('ex', '✅ Am Montag habe ich einen Bug gemeldet.', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.'),
                ('ex', '❌ Ich habe gefixt der Bug. (ترتیبِ مفعول)', '❌ مفعول قبل از particip: den Bug gefixt!'),
                ('ex', '✅ Ich habe den Bug gefixt.', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.')
            ]
        },
        {
            'h2': 'تمرین‌های این درس — چهار قدم، بی‌عجله',
            'blocks': [
                ('p', 'تمرینِ جمع‌بندیِ فاز ۳: هفتهٔ خودت را بساز و اجرا کن:'),
                ('ol', [
                    'پنج روزِ هفتهٔ آینده‌ات را با یک جملهٔ آلمانیِ کاری برنامه‌ریزی کن.',
                    'چهار صحنهٔ سختِ این درس را جدا و دوبار اجرا کن.',
                    'چک‌لیستِ چهارده‌ابزاری را ببند: هر ردیف بدونِ نگاه، یک بار.',
                    'پاراگرافِ هفته را دربارهٔ هفتهٔ واقعیِ پیشِ رو بازسازی کن.'
                ]),
                ('faq', [
                    ('پاسخ تمرین ۱', 'نمونه: „Am Montag: Standup + Bug-Report. Am Dienstag: Architektur-Meeting. Am Mittwoch: Code-Reviews. Am Donnerstag: Deploy. Am Freitag: 1:1 und Feierabend!“ — پنج روزِ فنی با پنج جمله؛ تقویمِ کاریِ آلمانیِ تو!'),
                    ('پاسخ تمرین ۲', 'صحنه‌های سختِ رایج: مخالفتِ جلسه، اعلامِ تأخیر، ریویوی نقدِ سنگین و مذاکره — هرکدام را با دقتِ دوبرابر اجرا کن؛ این‌ها صحنه‌هایِ اعتبارِ آلمانی‌ات‌اند!'),
                    ('پاسخ تمرین ۳', 'چهارده تیک = فاز ۳ مُهرِ کامل. کمتر از ده؟ هفتهٔ آینده، هر روز دو ابزار را در موقعیتِ واقعی به کار ببر — فازِ کاری، در کار ساخته می‌شود نه در کتاب!'),
                    ('پاسخ تمرین ۴', 'پاراگرافِ آینده‌ات را بنویس، ضبط کن، نگه دار — و در پایانِ هفته، با واقعیت مقایسه‌اش کن! این تمرینِ «پیش‌بینی + مقایسه»، سریع‌ترین راهِ دیدنِ پیشرفتِ زبانی است!')
                ])
            ]
        },
        {
            'h2': 'چالشِ امروز',
            'blocks': [
                ('quote', '🎯 امروز پنج جملهٔ پنج روزِ هفتهٔ آینده‌ات را بنویس و در تقویم/نوت بگذار — از فردا صبح با استندآپِ آلمانی شروع می‌شود. فاز ۴ (اداره‌ها و مهاجرت) منتظرِ توست — با جعبه‌ابزارِ کاری‌ای که الان داری!')
            ]
        },
        {
            'h2': 'نکات مکالمهٔ واقعی که کتاب‌ها کم می‌گویند',
            'blocks': [
                ('ul', [
                    '**فاز ۳ را «مسالهٔ حل‌شده» بدان — و هر روز تمرینش کن** — کار، کلاسِ زبانِ رایگانِ روزانهٔ توست: استندآپ، چت، ریویو. هر هفته‌ای که با دقتِ زبانی کار کنی، یک پله؛ هفته‌ای که نه، یک هفتهٔ تلف‌شدهٔ زبانی!',
                    '**آلمانیِ کاری‌ات، «لهجهٔ آلمانیِ» تو را می‌سازد** — بعد از ماه‌ها، جمله‌هایت خودکار می‌شوند و مغزت آلمانیِ فنی را «زبانِ اولِ حرفه‌ای» می‌بیند — جایی که خواب می‌بینی کد می‌زنی و… حرف می‌زنی به آلمانی! این نقطه واقعی است و به نزدیکیِ توست!',
                    '**فاز ۴ از فردا: اداره‌ها، ویزا، مالیات** — جایی که مهاجرِ زبان‌آموخته از مهاجرِ گم‌شده جدا می‌شود: Ausländerbehörde، Termin، Steuer-ID، اقامت. همه با آلمانیِ محترمانهٔ تو — و جالب‌تر: خیلی از جملاتش را همین حالا بلدی (möchte، Termin، Unterlagen…)! ادامه بده!'
                ])
            ]
        },
    ],
    'takeaway': 'فاز ۳ تمام: استندآپ، ایمیل، چت، ریویو، جلسه، وضعیت، باگ، دیپلوی، گیت، ۱:۱، قرارداد و مصاحبه — چهارده ابزارِ همکارِ آلمانی‌زبان. هفته‌ات را بنویس، اجرا کن و پاراگرافِ هفته را بساز — فاز ۴ (اداره‌ها) با همین جعبه‌ابزار باز می‌شود.',
    'faq': [
        ('فاز ۴ را چقدر جدی بخوانم — کار دارم دیگر!', 'جدی! فاز ۴ همان جایی است که مهاجرها بیشترین استرس را می‌خورند — نه چون سخت است، چون زبانش ناشناخته است. نامه‌های اداری، Terminها، مالیات و اقامت — این درس‌ها با آلمانیِ ساده و قالب‌های آماده، «ترسِ بوروکراسی» را حل می‌کنند؛ ساعت‌ها زمان و انرژی نجات می‌دهد!'),
        ('برای مصاحبهٔ شغلیِ واقعی چقدر آماده‌ام؟', 'اگر درس‌های ۴۹ و ۵۰ را با تمرینِ واقعی رد کردی (معرفیِ دوقیقه‌ای + سه STAR + رزومهٔ عدددار)، هستی! مرحلهٔ بعدی: مصاحبهٔ تمرینیِ واقعی — با دوستِ آلمانی‌زبان یا اپِ مکالمهٔ آپ‌ورد در نقشِ «مصاحبه‌گرِ آلمانی». سه دورِ تمرینیِ واقعی، آمادگیِ ۹۰٪ می‌سازد!')
    ],
},

# ── درس ۵۳ ─────────────────────────────────────────────────────────────────
{
    'slug': 'german-visa-types',
    'title': 'ویزا و بلوکارت؛ نقشهٔ اقامتِ برنامه‌نویس',
    'desc': 'فاز ۴ شروع می‌شود: مسیرهایِ اقامتیِ توسعه‌دهنده در آلمان — از جست‌وجوی کار تا بلوکارت و اقامتِ دائم — با واژگانِ کلیدیِ هر مرحله.',
    'keywords': 'ویزا آلمان, بلوکارت, Blue Card آلمان, اقامت آلمان, ویزای کار آلمان',
    'answer': 'سه مسیرِ اصلی برای برنامه‌نویس: ۱) ویزایِ جست‌وجوی کار (Chancenkarte/جست‌وجو — ۱۲ ماهِ پیدا‌کردنِ کار!)، ۲) Blue Card (بلوکارت — با قراردادِ آلمانی و حقوقِ معین: مسیرِ سریعِ اقامتِ دائم!) و ۳) ویزایِ کاریِ معمول (§18a). قاعدهٔ طلایی: صفحهٔ سفارت + ابزارهای آنلاین را همیشه چک کن — سقفِ حقوقِ بلوکارت هر سال عوض می‌شود!',
    'intro': [
        'به فاز ۴ خوش آمدی — فازِ مهاجرتِ واقعی! و هیچ نقطهٔ شروعی بهتر از نقشهٔ اقامت نیست: مسیرهایِ قانونیِ ماندن در آلمان، هرکدام با واژگان، شرط‌ها و مراحلِ خودش. این درس نقشه را می‌کشد — با زبانِ ساده، نه زبانِ قانونی!',
        'نکتهٔ مهمِ روحیه: بوروکراسیِ آلمان ترسناک به نظر می‌رسد اما قاعده‌مند است — هر سند، هر Termin و هر فرم، جوابِ مشخصی دارد. مهاجری که نقشه را می‌فهمد (و جمله‌هایش را بلد است!)، از ۹۰٪ اضطرابِ این فاز خلاص می‌شود. بیا نقشه را ببینیم!'
    ],
    'sections': [
        {
            'h2': 'سه مسیرِ اصلی؛ نقشهٔ اقامت',
            'blocks': [
                ('table', ['مسیر', 'برای چه کسی', 'نکتهٔ کلیدی'],
                    [['Chancenkarte (کارتِ فرصت)', 'فارغ‌التحصیلِ خارج ازِ آلمان با امتیازِ کافی', '۱۲ ماهِ جست‌وجوی کار + کارِ پاره‌وقتِ ۲۰ ساعته!'],
                     ['Blaue Karte EU (بلوکارت)', 'با پیشنهادِ کاریِ آلمانی + حقوقِ سقف', 'مسیرِ سریعِ اقامتِ دائم (۲۱-۲۷ ماه!) + همسر بی‌قیدِ کار!'],
                     ['Visum zum Arbeiten (§18a/b)', 'با قرارداد + تأییدِ آژانسِ کار', 'مسیرِ کلاسیک؛ آهسته‌تر ولی برای همهٔ حقوق‌ها'],
                     ['(بعداً) Niederlassungserlaubnis', 'بعد از سال‌ها کارِ پرداختِ مالیات', 'اقامتِ دائم — درس ۷۱!'],
                     ['(بعداً) Einbürgerung', 'بعد از ۵ سال + B1', 'تابعیت — درس ۷۱!']]),
                ('p', 'سقفِ حقوقِ بلوکارت هر اولِ سال تنظیم می‌شود (برای ۲۰۲۶ حدود ۴۸-۵۳ هزار یورو بسته به شغلِ کم‌بودن — اعدادِ دقیق را در سایتِ official چک کن!): برنامه‌نویس‌ها معمولاً در شاخهٔ «کم‌بودنِ نیرو» (Engpassberuf) هستند و سقفِ پایین‌تر می‌گیرند!'),
            ]
        },
        {
            'h2': 'واژگانِ کلیدیِ هر مرحله',
            'blocks': [
                ('table', ['واژه', 'معنی', 'جمله'],
                    [['das Visum / die Aufenthaltserlaubnis', 'ویزا / اجازهٔ اقامت', 'Ich beantrage eine Aufenthaltserlaubnis.'],
                     ['die Arbeitsgenehmigung', 'اجازهٔ کار', 'Die Arbeitsgenehmigung liegt dem Antrag bei.'],
                     ['der Arbeitgeber', 'کارفرما', 'Mein Arbeitgeber unterstützt den Antrag.'],
                     ['die Anerkennung', 'احرازِ مدرک', 'Ist eine Anerkennung meines Abschlusses nötig?'],
                     ['die Frist', 'مهلت', 'Die Frist endet am 30. Juni.'],
                     ['die Beantragung', 'درخواست‌دادنِ رسمی', 'Wo findet die Beantragung statt?'],
                     ['der Bescheid', 'پاسخِ رسمیِ اداره', 'Der Bescheid kommt per Post.'],
                     ['die Niederlassungserlaubnis', 'اقامتِ دائم', 'Nach 27 Monaten kann ich die Niederlassung beantragen.']]),
            ]
        },
        {
            'h2': 'گفتگو: در سفارت — ویزایِ اول',
            'blocks': [
                ('ex', 'Guten Tag! Ich beantrage ein Visum zur Arbeitsaufnahme. Hier sind meine Unterlagen.', 'سلام! ویزایِ شروعِ کار درخواست می‌کنم. این‌ها مدارکم است. — سه واژهٔ مقدس: beantragen (درخواستِ رسمی)، die Arbeitsaufnahme (شروعِ کار)، die Unterlagen!'),
                ('ex', 'Haben Sie einen Arbeitsvertrag? — Ja, einen unbefristeten Vertrag als Softwareentwickler.', 'قراردادِ کاری دارید؟ — بله، قراردادِ نامحدود به‌عنوانِ مهندسِ نرم‌افزار. — unbefristet = نامحدود؛ واژهٔ طلاییِ هر سفارت!'),
                ('ex', 'Ihr Abschluss muss eventuell anerkannt werden. Das prüft die ZAB.', 'مدرکتان شاید باید احراز شود. ZAB بررسی‌اش می‌کند. — die ZAB (Zentralstelle für ausländisches Bildungswesen) — احرازِ مدارکِ خارجی!'),
                ('ex', 'Wie lange dauert die Bearbeitung? — In der Regel sechs bis zehn Wochen.', 'پردازش چقدر طول می‌کشد؟ — معمولاً شش تا ده هفته. — die Bearbeitung = پردازش؛ سوالِ مقدسِ هر درخواست!')
            ]
        },
        {
            'h2': 'گرامرِ عمیق‌تر: زبانِ ادارهٔ ویزا — مجهولِ مؤدبِ اطلاعات',
            'blocks': [
                ('p', 'اداره‌های آلمان، خبرها را با مجهول می‌دهند — «بررسی می‌شود»، «ارسال می‌شود»، «خواهد شد» — و شناختش، نصفِ درکِ نامه‌های اداری‌ات است: **Ihr Antrag wird geprüft** (درخواستتان بررسی می‌شود)، **Der Bescheid wird Ihnen zugesandt** (پاسخ برایتان ارسال می‌شود)، **Die Frist kann verlängert werden** (مهلت را می‌توان تمدید کرد). فاز ۵ مجهول را کامل باز می‌کند؛ امروز این سه قالبِ پرتکرارِ نامه‌هایِ ویزا را قفل کن — هر نامهٔ ABH که باز کردی، آنها را می‌بینی!'),
            ]
        },
        {
            'h2': 'اشتباه‌های رایجِ فارسی‌زبان‌ها در همین درس',
            'blocks': [
                ('p', 'این بخش را با یک قرارداد بخوان: هر ❌ یعنی «مغزِ فارسی‌زبانت این را می‌سازد و طبیعی است»، و هر ✅ یعنی «این همان چیزی است که گیرندهٔ آلمانی‌زبان می‌شنود». با هر جفت بلند تکرار کن تا شکلِ درست در گوشت نشست کند.'),
                ('ex', '❌ Ich will ein Visum. (در سفارت)', '❌ want سفارت جواب نمی‌دهد — beantragen کنید: درخواستِ رسمی!'),
                ('ex', '✅ Ich möchte ein Visum beantragen.', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.'),
                ('ex', '❌ Mein Visum ist tot. (منقضی شد!)', '❌ «مرده» را برای ویزا نمی‌گویند — abgelaufen (منقضی‌شده)!'),
                ('ex', '✅ Mein Visum läuft am 30. Juni ab. / ist abgelaufen.', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.'),
                ('ex', '❌ (سکوت تا آخرِ مهلتِ تمدید!)', '❌ تمدید، هفته‌ها قبلِ انقضا شروع می‌شود — قانونِ طلاییِ اداره: زود برو، آرام باش!'),
                ('ex', '✅ Ich möchte meinen Aufenthaltstitel verlängern. Was brauche ich dafür?', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.')
            ]
        },
        {
            'h2': 'تمرین‌های این درس — چهار قدم، بی‌عجله',
            'blocks': [
                ('p', 'تمرین: پروندهٔ اقامتِ خودت را بساز:'),
                ('ol', [
                    'مسیرِ اقامتیِ خودت (یا نقشهٔ آرزو) را انتخاب کن و به آلمانی بگو: چه ویزایی، چه شرطی، چه مدت؟',
                    'هشت واژهٔ جدول را در سه جملهٔ واقعی به کار ببر — beantragen، Frist، Bescheid!',
                    'دیالوگِ سفارت را اجرا کن — با مدارکِ واقعیِ خودت (لیستشان را بگو!).',
                    'سه قالبِ مجهولِ نامه‌های اداری را با وضعیتِ خودت بازنویسی کن.'
                ]),
                ('faq', [
                    ('پاسخ تمرین ۱', 'نمونه: „Ich beantrage die Blaue Karte EU: unbefristeter Vertrag, Gehalt über der Schwelle, Beruf als Softwareentwickler. Nach 27 Monaten kann ich die Niederlassungserlaubnis beantragen.“ — نقشهٔ بلوکارتِ کامل در سه جمله!'),
                    ('پاسخ تمرین ۲', '„Ich beantrage …“ · „Die Frist endet am …“ · „Der Bescheid wird zugesandt.“ — سه جمله = سه ستونِ هر مکالمهٔ ویزا!'),
                    ('پاسخ تمرین ۳', 'مدارکِ رایج: der Pass، der Arbeitsvertrag، die Gehaltsabrechnung (فیشِ حقوقی!)، das Foto، die Krankenversicherung (بیمهٔ درمان)، ggf. das Diplom (دیپلم). جملهٔ ارائه: „Hier sind mein Pass, mein Arbeitsvertrag und der Nachweis der Krankenversicherung.“ — شش سندِ بستهٔ کامل!'),
                    ('پاسخ تمرین ۴', '„Mein Antrag wird geprüft.“ · „Die Unterlagen werden per Post zugesandt.“ · „Die Frist kann verlängert werden.“ — سه قالبِ مجهول با «من» به‌عنوانِ موضوع — زبانِ واقعیِ پروندهٔ اداری‌ات!')
                ])
            ]
        },
        {
            'h2': 'چالشِ امروز',
            'blocks': [
                ('quote', '🎯 امروز «پروندهٔ اقامت»ی خودت را شروع کن: یک برگه، دو ستون — وضعیتِ فعلی (ویزا/قرارداد/حقوق) و قدمِ بعدی با تاریخ. جملهٔ آلمانی‌اش را هم بنویس: „Mein nächster Schritt: …“ — نقشهٔ روشن، نصفِ آرامش!')
            ]
        },
        {
            'h2': 'نکات مکالمهٔ واقعی که کتاب‌ها کم می‌گویند',
            'blocks': [
                ('ul', [
                    '**«Machen Sie bitte im Original und zwei Kopien» — قانونِ جیبیِ سفارت** — هر سند: اصل + دو کپی! آلمانی‌ها عاشقِ نسخه‌های آماده‌اند؛ با خودکپی‌نگرفتن، صف دو بار می‌روی. جملهٔ نجات: „Darf ich hier kopieren?“ (می‌توانم این‌جا کپی بگیرم؟)',
                    '**بلوکارت = سوپرقدرتِ خانواده** — با بلوکارت، همسرت بدونِ شرطِ زبان و بدونِ سقفِ کار، اجازهٔ کارِ کامل می‌گیرد! جملهٔ پرونده: „Meine Frau erhält Zugang zum Arbeitsmarkt.“ (همسرم دسترسی به بازارِ کار می‌گیرد.) — برای برنامه‌نویس‌هایِ متأهل، بلوکارت بهترین مسیرِ خانوادگی است!',
                    '**تاریخ‌ها را با حروفِ بزرگِ تازه یاد بگیر: „zum 30. Juni“, „ab dem 1. Juli“** — نامه‌های اداری با این قالب‌های زمانی پر شده‌اند: zum (تا/در تاریخِ)، ab (از تاریخِ)، bis (تا تاریخِ). هر نامهٔ آینده‌ات، سه بارِ این‌ها را دارد — بشناسشان!'
                ])
            ]
        },
    ],
    'takeaway': 'سه مسیر: Chancenkarte (جست‌وجو، ۱۲ ماه)، بلوکارت (قرارداد + سقفِ حقوق — سریع‌ترین اقامتِ دائم + همسرِ آزاد!) و §18. واژگانِ ستون: beantragen، Frist، Bescheid، Unterlagen. نامه‌های اداری با مجهول نوشته می‌شوند: „Ihr Antrag wird geprüft“ — و سقفِ بلوکارت را هر سال چک کن!',
    'faq': [
        ('از کجا اعدادِ دقیقِ امسال را پیدا کنم؟', 'سه منبعِ رسمی: make-it-in-germany.com (پرتالِ دولتیِ انگلیسی/آلمانی!)، سایتِ سفارتِ آلمان در تهران (برای درخواستِ اول) و سایتِ ABH شهرِ مقصد. جملهٔ جست‌وجوی آلمانی: „Blaue Karte EU Gehaltsgrenze [سال]“ — و همیشه دو منبع را با هم چک کن؛ قاعدهٔ طلاییِ مهاجرتِ آگاهانه!'),
        ('اگر بین دو مسیر ماندم؟', 'سوالِ طلایی از وکیب/مشاور/HR: „Welcher Weg ist für meine Situation besser — die Blaue Karte oder §18a?“ (کدام مسیر برای وضعیتِ من بهتر است؟) — HRِ شرکت‌های آلمانی معمولاً تجربهٔ پرونده‌های قبلی را دارد و خوشحال می‌شود کمک کند؛ سفارت هم در ایمیل جوابِ کوتاه می‌دهد. سوالِ درست، نیمِ مسیر است!')
    ],
},

# ── درس ۵۴ ─────────────────────────────────────────────────────────────────
{
    'slug': 'german-auslaenderbehoerde',
    'title': 'Ausländerbehörde؛ مکالمهٔ ادارهٔ foreigners',
    'desc': 'مهم‌ترین ادارهٔ مهاجرها: Termin گرفتن از ABH، گفتگوی باجه، مدارکِ تمدید و جملاتِ نجاتِ هر وضعیت.',
    'keywords': 'Auslanderbehorde, اداره foreigners آلمان, تمدید اقامت آلمان, Termin ABH, اداره مهاجران آلمان',
    'answer': 'ABH (ادارهٔ امورِ خارجیان) سه قانون دارد: ۱) Termin = طلای ناب — آنلاین/تلفن بگیر، صبحِ زود چک کن؛ ۲) مدارکِ کامل با کپی: پاسپورت، اجازهٔ اقامت، قرارداد، فیشِ حقوق، بیمه، ثبت‌آدرس؛ ۳) جملهٔ نجاتِ هر باجه: „Ich bin neu in Deutschland — können Sie mir bitte helfen?“ مهاجرِ مؤدبِ سوال‌پرس، محبوب‌ترین مشتریِ اداره است!',
    'intro': [
        'ادارهٔ امورِ خارجیان (ABH/Ausländerbehörde) — قهرمانِ کابوس‌های مهاجرها و در واقع: اداره‌ای قاعده‌مند با جواب‌های مشخص! رازِ آرامش در ABH سه چیز است: Terminِ درست، مدارکِ کامل و جمله‌هایِ آماده — و هر سه را همین درس می‌سازد.',
        'و یک واقعیتِ امیدوارکننده: کارمندانِ ABH روزی صدها مهاجر می‌بینند و با آلمانیِ ساده و مؤدب و سوالِ واضح، بهترین رفتار را می‌کنند. مهاجرِ آماده، مشتریِ آسان است — و مشتریِ آسان، سریع‌ترین جواب‌ها را می‌گیرد!'
    ],
    'sections': [
        {
            'h2': 'Termin گرفتن؛ هنرِ صبرِ فعال',
            'blocks': [
                ('ex', 'Ich möchte einen Termin zur Verlängerung meiner Aufenthaltserlaubnis. Haben Sie in den nächsten Wochen etwas frei?', 'می‌خواهم نوبتِ تمدیدِ اجازهٔ اقامتم بگیرم. هفته‌های نزدیک چیزی خالی دارید؟ — die Verlängerung = تمدید؛ فعلِ مقدسِ ABH!'),
                ('ex', 'Mein Aufenthaltstitel läuft am 15. August ab. Wann sollte ich den Termin machen?', 'اجازهٔ اقامتم ۱۵ اوت منقضی می‌شود. کِی باید نوبت بگیرم؟ — سوالِ طلاییِ زمان‌بندی — جوابِ رایج: ۶-۸ هفته قبل!'),
                ('ex', 'Ist ein Notfalltermin möglich? Meine Frist endet in zwei Wochen.', 'نوبتِ اضطراری ممکن است؟ مهلتم دو هفته دیگر تمام می‌شود. — der Notfalltermin — برای روزهای سخت!'),
                ('p', 'ترفندِ واقعیِ Terminِ ABH: سایتِ رزروِ شهر، صبحِ زود (۷-۸!) و روزهایِ وسطِ هفته چک شود — لغو‌شدن‌ها همین‌جا پیدا می‌شوند!'),
            ]
        },
        {
            'h2': 'بستهٔ مدارکِ ABH؛ چک‌لیستِ طلایی',
            'blocks': [
                ('table', ['سند', 'آلمانی', 'نکته'],
                    [['پاسپورت', 'der Pass', 'معتبر + کپی'],
                     ['اجازهٔ اقامتِ فعلی', 'der Aufenthaltstitel', 'کارتِ پلاستیکی (eAT)'],
                     ['ثبت‌آدرس', 'die Meldebescheinigung', 'جدیدتر از ۳ ماه!'],
                     ['قراردادِ کار', 'der Arbeitsvertrag', 'کپی + اصل'],
                     ['فیشِ حقوقِ ۳ ماه', 'die Gehaltsabrechnungen', 'سه ماهِ اخیر!'],
                     ['بیمه', 'die Krankenversicherung', 'تأییدیه از بیمه'],
                     ['عکسِ بیومتریک', 'das Passfoto', 'مخصوصِ کارتِ جدید'],
                     ['فرمِ درخواست', 'das Antragsformular', 'از سایتِ ABH — پرشده!']]),
                ('p', 'قانونِ بسته: **همه‌چیز با کپی + مرتب در پوشه** — کارمندِ ABH ورق می‌زند، می‌بیند، تأیید می‌کند. پوشهٔ مرتب = جلسهٔ کوتاه!'),
            ]
        },
        {
            'h2': 'گفتگو: روزِ Termin در باجهٔ ABH',
            'blocks': [
                ('ex', 'Guten Tag! Ich habe einen Termin um 10 Uhr — hier ist meine Terminbestätigung.', 'سلام! ساعت ۱۰ نوبت دارم — این تأییدیهٔ نوبتم است. — die Terminbestätigung؛ سندِ ورود به هر اداره!'),
                ('ex', 'Was ist der Grund Ihres Besuches? — Die Verlängerung meiner Blauen Karte.', 'دلیلِ مراجعه‌تان چیست؟ — تمدیدِ بلوکارتِ من. — der Grund des Besuches؛ سوالِ اولِ هر باجه!'),
                ('ex', 'Sehr gut. Ich sehe: Alles ist vollständig. Die Bearbeitung dauert ca. 6 Wochen — Ihre Karte kommt per Post.', 'خیلی خوب. می‌بینم: همه‌چیز کامل است. پردازش حدود ۶ هفته — کارت‌تان با پست می‌آید. — بهترین جملهٔ دنیا: alles vollständig!'),
                ('ex', 'Und bis die neue Karte kommt? — Sie bekommen eine Fiktionsbescheinigung.', 'و تا کارتِ جدید بیاید؟ — یک گواهیِ موقت می‌گیرید. — die Fiktionsbescheinigung: سندِ طلاییِ فاصلهٔ بینِ دو کارت — با آن سفر و کار قانونی است!')
            ]
        },
        {
            'h2': 'گرامرِ عمیق‌تر: درخواستِ اداری با «Ich hätte gern» و تفاوتِ möchte',
            'blocks': [
                ('p', 'در باجه‌ها دو قالبِ درخواست داری و هر دو مؤدب‌اند: **Ich möchte … beantragen** (می‌خواهم … درخواست بدهم — عام) و **Ich hätte gern …** (می‌خواستم … — نرم‌تر و اداری‌تر!). برای بسته‌های اداری، hätte gern کامل است: „Ich hätte gern eine Fiktionsbescheinigung“ (یک گواهیِ موقت می‌خواستم)، „Ich hätte gern das Formular für die Verlängerung“ (فرمِ تمدید را می‌خواستم). این hätte از خانوادهٔ Konjunktivِ درس ۳۷ است — بستهٔ اداریِ مؤدبِ حرفه‌ای!'),
            ]
        },
        {
            'h2': 'اشتباه‌های رایجِ فارسی‌زبان‌ها در همین درس',
            'blocks': [
                ('p', 'این بخش را با یک قرارداد بخوان: هر ❌ یعنی «مغزِ فارسی‌زبانت این را می‌سازد و طبیعی است»، و هر ✅ یعنی «این همان چیزی است که گیرندهٔ آلمانی‌زبان می‌شنود». با هر جفت بلند تکرار کن تا شکلِ درست در گوشت نشست کند.'),
                ('ex', '❌ Ich brauche neue Visum. (روزِ آخرِ اعتبار!)', '❌ کارِ اداری، روزِ آخر نمی‌شود — ۶-۸ هفته قبل شروع کن؛ «Ihr Titel läuft ab» را ببین، برو!'),
                ('ex', '✅ Mein Aufenthaltstitel läuft bald ab — ich möchte ihn verlängern.', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.'),
                ('ex', '❌ (بدونِ کپی، اصل‌ها را می‌دهی و منتظرِ می‌مانی!)', '❌ اصل + کپی قانونِ اداره است — بدونِ کپی، جلسه دو برابر!')
                ,
                ('ex', '✅ Hier ist das Original und zwei Kopien.', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.'),
                ('ex', '❌ Warum dauert das so lange?! (به کارمند)', '❌ کارمندِ باجه، تصمیم‌گیرنده نیست — بی‌احترامیِ کوچک، پرونده را کُند می‌کند! صبرِ اداری، قانونِ آلمان است!'),
                ('ex', '✅ Danke für die Information. Wann kann ich mit dem Bescheid rechnen?', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.')
            ]
        },
        {
            'h2': 'تمرین‌های این درس — چهار قدم، بی‌عجله',
            'blocks': [
                ('p', 'تمرین: پروندهٔ ABHِ خودت را کامل آماده کن:'),
                ('ol', [
                    'چک‌لیستِ هشت‌سندی را با وضعیتِ واقعی‌ات پر کن: چی داری، چی لازم است؟',
                    'دیالوگِ باجه را اجرا کن — با نقشِ کارمند هم!',
                    'سه جملهٔ اداریِ hätte gern را برای سه درخواستِ واقعی بساز.',
                    'برنامهٔ زمانیِ اقامتی‌ات را بنویس: انقضا، Terminِ هدف، شروعِ اقدام — با تاریخِ واقعی!'
                ]),
                ('faq', [
                    ('پاسخ تمرین ۱', 'جدولِ هشت‌سندی + وضعیت: ✅ پاسپورت ✅ قرارداد ✅ بیمه ⬜ فیش‌های ۳ ماه (بگیر!) ⬜ عکسِ بیومتریک … — هر ⬜ یک «کارِ این هفته» است؛ پروندهٔ آماده، آرامشِ اداری!'),
                    ('پاسخ تمرین ۲', 'اجرای دو نقش — و در نقشِ کارمند، سوال‌هایش را بشناس: „Was ist der Grund? Seit wann arbeiten Sie? Ist der Vertrag unbefristet?“ — چهار سوالِ هر باجهٔ تمدید!'),
                    ('پاسخ تمرین ۳', '„Ich hätte gern das Antragsformular.“ · „Ich hätte gern eine Fict… Fiktionsbescheinigung.“ · „Ich hätte gern eine Bestätigung für meinen Arbeitgeber.“ — سه درخواستِ واقعیِ هر پرونده!'),
                    ('پاسخ تمرین ۴', 'نمونه: „Titel läuft ab am 15. August. Termin-Ziel: Ende Juni. Ich rufe jede Woche dienstags an und checke online täglich um 8 Uhr.“ — برنامهٔ زمانی + برنامهٔ تلاش: همان چیزی که مهاجرِ حرفه‌ای از مهاجرِ دل‌شوره‌ای جدا می‌کند!')
                ])
            ]
        },
        {
            'h2': 'چالشِ امروز',
            'blocks': [
                ('quote', '🎯 امروز تاریخِ انقضای اجازهٔ اقامتت (یا تاریخِ هدفِ درخواست) را در تقویم بگذار + یادآورِ ۸ هفته قبل. و چک‌لیستِ مدارکت را پرینت کن. ABHِ آماده = ABHِ آرام!')
            ]
        },
        {
            'h2': 'نکات مکالمهٔ واقعی که کتاب‌ها کم می‌گویند',
            'blocks': [
                ('ul', [
                    '**هر شهر ABHِ خودش را دارد — و هرکدام فرهنگِ Terminِ خودش!** — برلین (LEA — سخت‌ترینِ Termin‌ها!)، مونیخ، شهرهای کوچک (سریع‌تر!). جملهٔ اولِ هر شهرِ جدید: „Wo ist die Ausländerbehörde und wie bekomme ich einen Termin?“ — از Büro für Migration یا حتی Google Maps شروع کن!',
                    '**Fiktionsbescheinigung را بشناس — و ازش نخواه در سفرِ خارج!** — گواهیِ موقت برای «بودن و کار در آلمان» است؛ سفرِ خارجی با آن پیچیده است (بندِ §81![سخت]) — سوالِ قبل از سفر: „Darf ich mit der Fiktionsbescheinigung reisen?“ (با گواهیِ موقت می‌توانم سفر کنم؟) — جوابش را از کارمندِ خودت بگیر، نه از فروم‌ها!',
                    '**«Ich verstehe das nicht ganz» حقِ توست و کارِ اداری را دقیق می‌کند** — جملهٔ طلاییِ هر سندِ امضایی: „Können Sie mir diesen Punkt bitte erklären?“ (می‌توانید این بند را برایم توضیح دهید؟) — آلمانی‌ها از پرسشِ دقیق خوششان می‌آید؛ امضای بدونِ فهم، ممنوعِ فرهنگی و منطقی است!'
                ])
            ]
        },
    ],
    'takeaway': 'ABH سه قانون دارد: Terminِ زود (۶-۸ هفته قبلِ انقضا!)، بستهٔ کامل با کپی و جمله‌های مؤدب: „Ich möchte … beantragen / Ich hätte gern …“. Fiktionsbescheinigung پلِ بینِ دو کارت و «Alles ist vollständig» بهترین جملهٔ دنیاست. سوالِ ناشناخته را بپرس: „Können Sie mir das erklären?“',
    'faq': [
        ('اگر Termin نگرفتم و مهلتم نزدیک است؟', 'سه راه: ۱) Notfalltermin بپرس (مهلتی کمتر از ~۲ هفته!)؛ ۲) حضوریِ صفِ صبح (برخی ABHها دارند!)؛ ۳) تماسِ تلفنیِ مستمر + ایمیل با ثبتِ همه‌چیز: „Ich habe am … und … angerufen“ (در تاریخِ … و … زنگ زده‌ام) — سندِ تلاش، در بحرانِ Termin نجات‌دهنده است!'),
        ('کارمند آهسته/بی‌حوصله بود؟', 'آرام بمان، مؤدب باش، دقیق جواب بده — و اگر واقعاً بی‌انصافی: درخواستِ «Vorgesetzten sprechen» (با مدیرِ بخش صحبت کنم) حقِ توست! ۹۹٪ مواقع لازم نمی‌شود: پوشهٔ مرتب + آلمانیِ ساده + صبر، جادویِ ABH است — از تجربهٔ هزاران مهاجر!')
    ],
},
]

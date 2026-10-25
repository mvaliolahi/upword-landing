# -*- coding=utf-8 -*-
# -*- coding: utf-8 -*-
"""دورهٔ ۹۰ روزهٔ آلمانی — فایل دادهٔ ۹ (درس‌های ۷۳ تا ۸۱: فاز ۵، گرامرِ قدرت)."""

LESSONS = [

# ── درس ۷۳ ─────────────────────────────────────────────────────────────────
{
    'slug': 'german-perfekt',
    'title': 'Perfekt؛ روایتِ «دیروز چی شد؟»',
    'desc': 'زمانِ گذشتهِ گفتاریِ آلمانی: haben/sein + Partizip — ساختِ آن، فعل‌های sein‌دار و روایتِ کاملِ روز و پروژه.',
    'keywords': 'Perfekt آلمانی, گذشته آلمانی, Partizip, haben sein گذشته, گرامر آلمانی',
    'answer': 'Perfekt = زمانِ روایتِ گفتاری: „Ich habe gearbeitet“ (کار کردم) / „Ich bin gefahren“ (رفتم). فرمول: haben یا sein (جای دوم!) + مفعول + Partizip (آخر!). حرکت/تغییرِ حالت = sein؛ بقیه = haben. با Perfekt، هر «چی شد؟» زندگی‌ات جواب می‌گیرد!',
    'intro': [
        'به مهم‌ترین درسِ گرامریِ فازِ ۵ رسیدیم: Perfekt — زمانِ گذشته‌ای که در گفتار (و استندآپ و چت و قهوه!) همه‌جا هست! تا حالا صد بار «Ich habe … gemacht» را استفاده کردی و دیدی — حالا قواعدش را کامل باز می‌کنیم تا روایت‌هایت آزاد شوند.',
        'دو خبرِ خوب: اول — Perfekt با فعل‌های جدا-شدنی و مفعول‌ها، ساختارِ ساده‌ای دارد و دردسرهای اصلی‌اش فقط «haben یا sein؟» است. دوم — بعد از این درس، هر داستانِ روز، پروژه و سفر را می‌توانی تعریف کنی: از «was hast du gestern gemacht؟» تا روایتِ کاملِ مهاجرت!'
    ],
    'sections': [
        {
            'h2': 'فرمولِ Perfekt؛ سه تکهٔ ثابت',
            'blocks': [
                ('p', '**[فاعل] + [haben/sein — جای دوم!] + [مفعول/زمان/…] + [Partizip — آخر!]**'),
                ('table', ['جمله', 'تفکیک'],
                    [['Ich habe den Bug gefixt.', 'Ich | habe | den Bug | gefixt'],
                     ['Wir haben gestern deployt.', 'Wir | haben | gestern | deployt'],
                     ['Ich bin zum Amt gefahren.', 'Ich | bin | zum Amt | gefahren'],
                     ['Sie ist sehr müde geworden.', 'Sie | ist | sehr müde | geworden']]),
                ('p', 'قانونِ جایگاه: فعلِ کمکی (haben/sein) جای دومِ جمله و Partizip حتماً آخر — حتی با قیدها وسط! „Ich habe gestern den ganzen Tag gelernt.“ (دیروز تمام روز را درس خواندم.)')
            ]
        },
        {
            'h2': 'haben یا sein؟ قاعدهٔ حرکت و تغییر',
            'blocks': [
                ('table', ['sein با…', 'مثال', 'haben با…', 'مثال'],
                    [['حرکتِ مکان', 'fahren، gehen، kommen، fliegen', 'همهٔ فعل‌هایِ با مفعول', 'essen، lesen، machen'],
                     ['تغییرِ حالت', 'aufwachen (بیدارشدن)، werden (شدن)', 'فعل‌هایِ ذهنی', 'denken، wissen'],
                     ['بودن/ماندن', 'bleiben، sein', 'رفتار', 'arbeiten، spielen'],
                     ['(استثناها!)', 'sein! haben در خودش!', '…', 'haben: hab-en']]),
                ('p', 'ترفندِ سریع: **جابه‌جایی یا عوض‌شدنِ وضعیت = sein؛ بقیه = haben.** و ده فعلِ پرکاربردِ sein‌دار را حفظ کن: **gehen، fahren، kommen، fliegen، aufstehen، bleiben، werden，sein，umziehen (اسباب‌کشی!)，einschlafen (خوابیدن)**'),
                ('ex', 'Ich bin um 7 aufgestanden, habe gefrühstückt und bin zur Arbeit gefahren.', 'ساعت ۷ بیدار شدم، صبحانه خوردم و به کار رفتم. — روایتِ صبح در سه فعل! از این به بعد هر روزت را این‌طور روایت کن!')
            ]
        },
        {
            'h2': 'ساختِ Partizip؛ سه قالب',
            'blocks': [
                ('table', ['گروه', 'قالب', 'مثال'],
                    [['ضعیف (منظم)', 'ge + ریشه + t', 'gemacht، gearbeitet، gefixt'],
                     ['قوی (بی‌قاعده)', 'ge + ریشهٔ عوض‌شده + en', 'gelesen، geschrieben，gefahren'],
                     ['خارجی/-ieren!', 'بدونِ ge: ریشه + t', 'studiert، deployt، installiert (چون -ieren!)'],
                     ['جدا-شدنی', 'ge وسط: ریشه + ge + پیشوند', 'auf-ge-räumt، an-ge-rufen، ein-ge-kauft']]),
                ('p', 'نکتهٔ طلاییِ برنامه‌نویس‌ها: هر فعلِ انگلیسیِ واردشده (deployen، testen، pushen) قالبِ «خارجی» می‌گیرد: **deployt، getestet? نه — getestet درست است ولی test-en آلمانی است! deploy-en خارجی → deployt**. و جدا-شدنی‌ها: **Ich habe den Tisch auf**ge**räumt** — ge می‌آید وسط!'),
            ]
        },
        {
            'h2': 'گفتگو: «Wie war dein Wochenende؟» — روایتِ کامل',
            'blocks': [
                ('ex', 'Wie war dein Wochenende? Was hast du gemacht?', 'آخرِ هفته‌ات چطور بود؟ چه کردی؟ — سوالِ مقدسِ هر دوشنبه!'),
                ('ex', 'Ich bin samstags zum See gefahren. Wir haben gegrillt und sind geschwommen.', 'شنبه به دریاچه رفتم. کباب کردیم و شنا کردیم. — سه فعلِ sein‌دارِ حرکتی!'),
                ('ex', 'Am Sonntag habe ich nur relaxt — ich bin im Bett geblieben und habe Serie geschaut.', 'یکشنبه فقط استراحت کردم — توی تخت ماندم و سریال دیدم. — relaxen خارجی → relaxt (بدونِ ge)!',
                ),
                ('ex', 'Und du? — Ich habe Besuch gehabt. Meine Familie ist aus dem Iran gekommen!', 'و تو؟ — مهمان داشتم. خانواده‌ام از ایران آمدند! — Besuch haben + gekommen sein — خبرهایِ بزرگ با Perfekt!'),
            ]
        },
        {
            'h2': 'اشتباه‌های رایجِ فارسی‌زبان‌ها در همین درس',
            'blocks': [
                ('p', 'این بخش را با یک قرارداد بخوان: هر ❌ یعنی «مغزِ فارسی‌زبانت این را می‌سازد و طبیعی است»، و هر ✅ یعنی «این همان چیزی است که گیرندهٔ آلمانی‌زبان می‌شنود». با هر جفت بلند تکرار کن تا شکلِ درست در گوشت نشست کند.'),
                ('ex', '❌ Ich habe gegangen. (با haben!)', '❌ gehen حرکت است — sein! «Ich bin gegangen» — رایج‌ترین خطای Perfektِ دنیا!'),
                ('ex', '✅ Ich bin gegangen. / Ich bin gefahren.', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.'),
                ('ex', '❌ Ich habe gestern gearbeitet den ganzen Tag. (Partizip وسط!)', '❌ Partizip همیشه آخر! قیدها وسط می‌مانند.'),
                ('ex', '✅ Ich habe gestern den ganzen Tag gearbeitet.', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.'),
                ('ex', '❌ Ich habe gestudiert. (ge اضافه به -ieren!)', '❌ فعل‌هایِ -ieren هیچ‌وقت ge نمی‌گیرند! studiert، installiert، telefoniert.'),
                ('ex', '✅ Ich habe in Teheran Informatik studiert.', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.')
            ]
        },
        {
            'h2': 'تمرین‌های این درس — چهار قدم، بی‌عجله',
            'blocks': [
                ('p', 'تمرینِ Perfekt = روایتِ واقعی! هر تمرین را دربارهٔ خودت انجام بده:'),
                ('ol', [
                    'دیروزت را در پنج جمله روایت کن — با مخلوطِ haben و sein.',
                    'آخرین پروژه‌ات را روایت کن: چه ساختی؟ چه جایی گیر کردی؟ چطور حل شد؟',
                    'هفتهٔ گذشته‌ات را با پنج فعلِ sein‌دار تعریف کن.',
                    'سه فعلِ خارجی (-ieren/انگلیسی) و دو جدا-شدنی را در Perfekt به کار ببر.'
                ]),
                ('faq', [
                    ('پاسخ تمرین ۱', 'نمونه: „Ich bin spät aufgestanden und habe gefrühstückt. Ich habe den Morgen gelernt. Nachmittags bin ich Sport gegangen? NEIN — Ich habe Sport gemacht! Abends habe ich gekocht und bin früh eingeschlafen.“ — چهار haben + سه sein؛ روایتِ کاملِ روز!'),
                    ('پاسخ تمرین ۲', '„Wir haben ein Notification-System gebaut. Wir haben zwei Wochen daran gearbeitet. Ein Problem hat uns aufgehalten — aber wir haben es gelöst. Am Ende haben wir deployt und alles hat funktioniert.“ — روایتِ پروژه در Perfekt — دقیقاً استندآپِ دوشنبه‌ات!'),
                    ('پاسخ تمرین ۳', '„Ich bin zweimal ins Büro gefahren. Ich bin zum Arzt gegangen. Ich bin einkaufen gegangen? — Ich bin einkaufen gewesen / Ich war einkaufen! — حفظ: einkaufen sein + Partizip II: bin … gewesen در Perfektِ محاوره! (یا همان Präteritum: war!) Abends bin ich spät heimgekommen.“ — حرکت‌هایِ هفته در sein!'),
                    ('پاسخ تمرین ۴', '„Ich habe mein Laptop installiert neu? NEIN: Ich habe neu installiert / das OS neu installiert.“ · „Wir haben die Pipeline optimiert.“ · „Ich habe Sarah angerufen.“ · „Ich habe den Tisch aufgeräumt.“ — خارجی‌ها بدونِ ge، جدا-شدنی‌ها با ge وسط!')
                ])
            ]
        },
        {
            'h2': 'چالشِ امروز',
            'blocks': [
                ('quote', '🎯 امروز شب، روزت را در پنج جملهٔ Perfekt بلند روایت کن — به خودت، به دوست، به آپ‌ورد! این پنج جملهٔ شبانه، در یک ماه، ماشینِ Perfekt‌ات را بی‌صدا می‌سازد.')
            ]
        },
        {
            'h2': 'نکات مکالمهٔ واقعی که کتاب‌ها کم می‌گویند',
            'blocks': [
                ('ul', [
                    '**آلمانیِ گفتاری فقط Perfekt می‌گوید — حتی برای «بودن»!** — نوشتارِ رسمی «war» (Präteritum) می‌آورد ولی گفتار: „Ich war…“ هم هست! قاعدهٔ طلاییِ گفتاری: haben-فعل‌ها → Perfekt؛ sein/modal/wissen → Präteritumِ کوتاه (war، hatte، konnte!) — درسِ بعد کاملش می‌کند!',
                    '**«Warst du schon mal in München?« — Perfekt-سوال‌هایِ همیشگی** — سه سوالِ روایتِ زندگی: „Was hast du studiert?« (چه خواندی؟) · „Wo hast du vorher gearbeitet?« (قبلاً کجا کار کردی؟) · „Wie bist du nach Deutschland gekommen?« (چطور به آلمان آمدی؟) — سه جمله = گفتگوی کاملِ آشنایی!',
                    '**Partizip به‌عنوانِ صفت!** — خیلی از Partizipها صفت می‌شوند: „ein gut gelöster Bug« (باگی خوب-حل‌شده!)، „das neu installierte System« (سیستمِ تازه-نصب‌شده). این «صفتِ Partizipi» در ریویو و داکیومنت فراوان است — ساختارش را بشناس: Partizip I (…end: laufend در حالِ اجرا!) و Partizip II (ge…: gelaufen اجرا-شده!)'
                ])
            ]
        },
    ],
    'takeaway': 'Perfekt = haben/sein (جای دوم) + … + Partizip (آخر!). sein با حرکت و تغییر (gehen، fahren، werden!)؛ haben با بقیه. -ieren و فعل‌هایِ خارجی بدونِ ge؛ جدا-شدنی‌ها با ge وسط. با Perfekt، هر «دیروز/آخر هفته/پروژه» داستان می‌شود — روایتِ زندگی‌ات آزاد است!',
    'faq': [
        ('Perfekt و Präteritum دقیقاً چه فرقی دارند؟', 'Perfekt = گذشتهِ «گفتاری» (مکالمه، چت، ایمیلِ دوستانه)؛ Präteritum = گذشتهِ «نوشتاری/رسمی» (کتاب، خبر، نامهٔ اداری) و فعل‌هایِ خاص در گفتار (war/hatte/konnte/wollte). قاعدهٔ عملیِ طلایی: هرجا حرف می‌زنی Perfekt — به‌جزِ این چهار فعل که همیشه Präteritumِ کوتاه: sein→war، haben→hatte، können→konnte، wollen→wollte. درسِ بعد، کلِ Präteritum را باز می‌کند!')
    ],
},

# ── درس ۷۴ ─────────────────────────────────────────────────────────────────
{
    'slug': 'german-prateritum',
    'title': 'Präteritum؛ بود و نبودِ رسمیِ گذشته',
    'desc': 'گذشتهٔ نوشتاری: war، hatte، konnte و روایت‌های رسمی — فرمولِ ساده و مرزِ استفاده با Perfekt.',
    'keywords': 'Präteritum آلمانی, war hatte konnte, گذشته رسمی آلمانی, گرامر آلمانی, روایت رسمی',
    'answer': 'Präteritum در گفتار فقط برای چهار فعلِ مقدس است: **war** (بود)، **hatte** (داشت)، **konnte** (می‌توانست)، **wollte** (می‌خواست) — و در نوشتارِ رسمی، همه‌ی فعل‌ها. ساختِ منظم: ریشه + te + پایانه (ich machte، du machtest…). با همین چهار کلمه، نیمی از روایت‌هایِ محاوره‌ای‌ات رسمی و روان می‌شود!',
    'intro': [
        'رازِ کوچکِ گفتارِ آلمانی: بومی‌ها برای «بود/داشت/توانست/خواست» هرگز Perfekt نمی‌گویند — همیشه war/hatte/konnte/wollte! تو هم با همین چهار کلمه، محاوره‌ات یک‌شبه بومی‌تر می‌شود.',
        'و در نوشتار (نامهٔ اداری! خبر! داستان!) Präteritum پادشاه است. این درس هر دو دنیا را می‌سازد: چهار مقدسِ گفتار + ساختِ منظمِ نوشتار — با مرزِ دقیقِ «کجا کدام».'
    ],
    'sections': [
        {
            'h2': 'چهار مقدسِ گفتار؛ war، hatte، konnte، wollte',
            'blocks': [
                ('table', ['ضمیر', 'sein', 'haben', 'können', 'wollen'],
                    [['ich', 'war', 'hatte', 'konnte', 'wollte'],
                     ['du', 'warst', 'hattest', 'konntest', 'wolltest'],
                     ['er/sie/es', 'war', 'hatte', 'konnte', 'wollte'],
                     ['wir/Sie', 'waren', 'hatten', 'konnten', 'wollten'],
                     ['ihr', 'wart', 'hattet', 'konntet', 'wolltet']]),
                ('ex', 'Ich war gestern krank und hatte keinen Termin. Ich wollte kommen, konnte aber nicht.', 'دیروز مریض بودم و نوبتی نداشتم. می‌خواستم بیایم، ولی نمی‌توانستم. — چهار فعلِ مقدس در یک روایتِ کامل!')
            ]
        },
        {
            'h2': 'ساختِ منظم؛ ریشه + te + پایانه',
            'blocks': [
                ('p', 'برای نوشتارِ رسمی، Präteritumِ منظم ساده است: ریشه + **te** + پایانهٔ آشنا: ich machte، du machtest، er machte، wir machten… و بی‌قاعده‌های مهم (در نوشتار!): **ging** (رفت)، **kam** (آمد)، **sah** (دید)، **gab** (داد)، **nahm** (گرفت)، **schrieb** (نوشت)، **sprach** (گفت)، **dachte** (فکر کرد).'),
                ('table', ['گفتارِ روزمره (Perfekt)', 'نوشتارِ رسمی (Präteritum)'],
                    [['Ich habe das gemacht.', 'Ich machte das.'],
                     ['Wir haben deployt.', 'Wir deployten.'],
                     ['Er hat nichts gesagt.', 'Er sagte nichts.'],
                     ['Ich bin zur Bank gegangen.', 'Ich ging zur Bank.']]),
                ('p', 'می‌بینی؟ در گفتار، Perfekt طبیعی‌تر؛ در نامه و گزارش و خبر، Präteritum. قاعدهٔ عملی: **دهان = Perfekt (به‌جزِ چهار مقدس)؛ قلمِ رسمی = Präteritum!**'),
            ]
        },
        {
            'h2': 'گفتگو: روایت با چهار مقدس — مصاحبهٔ رفتاری!',
            'blocks': [
                ('ex', 'Interviewer: Erzählen Sie von einer schwierigen Situation.', 'از یک موقعیتِ سخت بگویید. — سوالِ STAR از درس ۴۹ — این‌جا با Präteritumِ محاوره!'),
                ('ex', 'Ich wollte ein Feature rechtzeitig liefern, aber der Test-Server war down und ich hatte keinen Zugriff.', 'می‌خواستم فیچری را به‌موقع تحویل بدهم، ولی سرورِ تست از کار افتاد و دسترسی نداشتم. — wollte + war + hatte در دو جملهٔ واقعی!'),
                ('ex', 'Ich konnte nicht warten — also habe ich lokal eine Alternative aufgebaut und die Tests parallel laufen lassen.', 'نمی‌توانستم صبر کنم — پس محلی یک جایگزین ساختم و تست‌ها را موازی راندم. — Präteritumِ مقدس + Perfektِ عادی: ترکیبِ طبیعیِ گفتار!'),
                ('ex', 'Am Ende war das Release pünktlich und der Chef war zufrieden. — Starke Geschichte!', 'آخرِ کار ریلیز به‌موقع بود و رئیس راضی بود. — داستانِ قوی! — روایتِ رفتاریِ کامل!')
            ]
        },
        {
            'h2': 'اشتباه‌های رایجِ فارسی‌زبان‌ها در همین درس',
            'blocks': [
                ('p', 'این بخش را با یک قرارداد بخوان: هر ❌ یعنی «مغزِ فارسی‌زبانت این را می‌سازد و طبیعی است»، و هر ✅ یعنی «این همان چیزی است که گیرندهٔ آلمانی‌زبان می‌شنود». با هر جفت بلند تکرین کن تا شکلِ درست در گوشت نشست کند.'),
                ('ex', '❌ Ich habe krank gewesen. (گفتارِ چفت!)', '❌ برایِ «بودن» هیچ‌وقت Perfekt در گفتار — همیشه war! «bin gewesen» فقط در جنوبِ آلمان! 😄'),
                ('ex', '✅ Ich war krank.', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.'),
                ('ex', '❌ Ich habe machen müssen. (در گفتارِ معمول)', '❌ جمله درست است ولی در گفتار راحت‌تر: musste! «Ich musste das machen» — مودال‌ها در گفتار Präteritum!'),
                ('ex', '✅ Ich musste das machen. / Ich wollte fragen.', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.'),
                ('ex', '❌ (Präteritumِ کامل در گفتارِ روزمره: „Ich kaufte…“)', '❌ آلمانیِ کتابیِ ۱۸۰۰! در گفتار: Ich habe gekauft — قاعدهٔ دهان/قلم!'),
                ('ex', '✅ Ich habe gestern eingekauft. (gesprochen) / Ich kaufte gestern ein. (geschrieben)', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.')
            ]
        },
        {
            'h2': 'تمرین‌های این درس — چهار قدم، بی‌عجله',
            'blocks': [
                ('p', 'تمرین: چهار مقدس را روان کن + بنویس و بگو:'),
                ('ol', [
                    'صرفِ چهار مقدس را برای هر شش ضمیر بلند بگو — دو راند!',
                    'یک STAR رفتاری روایت کن — با سه فعلِ مقدس در گفتار.',
                    'همان STAR را «نوشتاری» کن: سه جمله با Präteritumِ منظم!',
                    'مرز را تمرین کن: هر جمله را در هر دو زمان بگو و «طبیعی‌ترین» را انتخاب کن.'
                ]),
                ('faq', [
                    ('پاسخ تمرین ۱', 'war/warst/war/waren/wart/waren · hatte/hattest/hatte/hatten/hattet/hatten · konnte… · wollte… — چهار ستون، هر کدام شش شکل؛ ده بار پشت‌سرهم = مالکِ همیشگیِ گفتار!'),
                    ('پاسخ تمرین ۲', '„Ich wollte das Sprint-Ziel erreichen. Wir hatten einen kritischen Bug und ich war die einzige Person mit Kontext. Ich konnte das Problem isolieren und wir haben rechtzeitig geliefert.“ — چهار مقدس + یک Perfekt؛ روایتِ رفتاریِ بومی!'),
                    ('پاسخ تمرین ۳', '„Ich wollte das Sprint-Ziel erreichen. Wir hatten einen kritischen Bug. Ich isolierte das Problem und wir lieferten rechtzeitig.“ — همان داستان، نُسخهٔ نوشتاری: wollte/hatte (بی‌قاعده) + isolierte/lieferten (منظم + بی‌قاعده!)!'),
                    ('پاسخ تمرین ۴', 'جفت‌ها: „Ich war müde / Ich bin müde gewesen“ → گفتار: war! · „Ich machte / Ich habe gemacht“ → گفتار: Perfekt! · „Er sagte / Er hat gesagt“ → گفتار: Perfekt! — قانونِ دهان/قلم را با گوش انتخاب کن!')
                ])
            ]
        },
        {
            'h2': 'چالشِ امروز',
            'blocks': [
                ('quote', '🎯 امروز هر جا می‌خواستی بگویی «habe … gehabt/ gewesen/ gewollt/ gekonnt»، جایگزینش کن: hatte/war/wollte/konnte — پنج بار در روز، هفت روز: محاورهٔ چهار-مقدسِ تو، خودکار می‌شود!')
            ]
        },
        {
            'h2': 'نکات مکالمهٔ واقعی که کتاب‌ها کم می‌گویند',
            'blocks': [
                ('ul', [
                    '**«damals» و «früher» — دو کلمهٔ قفلِ Präteritum** — وقتی می‌شنوی: „Damals war alles anders!« (آن‌موقع همه‌چیز فرق داشت!) یا „Früher hatten wir keine Handys« (قبلاً موبایل نداشتیم!) — روایتِ قدیم، همیشه با چهار مقدس شروع می‌شود؛ این دو کلمه را بشناس و خودت هم بگو!'
                ])
            ]
        },
    ],
    'takeaway': 'گفتار: Perfekt برای همه — جزء چهار مقدس: war، hatte، konnte، wollte (+ sollte/musste/durfte!). نوشتارِ رسمی: Präteritum (machte، ging، sagte). مرز: دهان=Perfekt/چهارمقدس؛ قلم=Präteritum. «Ich war krank und hatte keinen Termin» — روایتِ طبیعیِ محاوره!',
    'faq': [
        ('مودال‌های دیگر (müssen، dürfen، sollen) هم در گفتار Präteritum می‌شوند؟', 'بله — کلِ خانوادهٔ مودال در گفتارِ طبیعی، Präteritumِ کوتاه می‌گیرند: musste (مجبور بودم)، durfte (اجازه داشتم)، sollte (باید می‌شد)، mochte (دوست داشتم). «Ich habe machen müssen» گرامری است اما سنگین و کمی آلمانیِ شرقی! 😄 قاعدهٔ طلاییِ گفتار: مودال + sein + haben → همیشه Präteritum کوتاه!')
    ],
},

# ── درس ۷۵ ─────────────────────────────────────────────────────────────────
{
    'slug': 'german-cases-deep',
    'title': 'چهار حالت در عمل؛ Nominativ تا Dativ',
    'desc': 'نقشهٔ کاملِ حالت‌ها: چه چیزی چه چیزی را به چه کسی می‌دهد — با جدولِ تعریف‌ها و الگوهایِ واقعیِ کاری و روزمره.',
    'keywords': 'حالت های آلمانی, Kasus آلمانی, Nominativ Akkusativ Dativ, گرامر آلمانی, جدول حالت',
    'answer': 'چهار حالت = چهار نقش: Nominativ (فاعل — کی؟)، Akkusativ (مفعول مستقیم — چه را؟)، Dativ (مفعول غیرمستقیم — به چه/کی؟)، Genitiv (مالک — چه کسی؟). تعریف‌ها فقط در مذکرِ مفرد عوض می‌شوند (der→den→dem→des)؛ بقیه تقریباً ثابت! با سه الگوهایِ «Hauptwort-مثل-حافظه»، جادوی حالت‌ها باز می‌شود.',
    'intro': [
        'به قلهٔ معروفِ «وحشتِ آلمانی» رسیدیم: حالت‌ها! اما با یک نگاهِ مهندسی، سیستمِ فوق‌العاده‌ای می‌بینی: چهار نقشِ جمله، فقط یک نقطهٔ تغییر (مذکرِ مفرد!) و منطقِ پنهانِ حروفِ اضافه. از حالا، هر جملهٔ آلمانی که می‌سازی، نقشهٔ حالتِ روشنی دارد!',
        'خبرِ خوبِ بزرگ: تو از درس‌های اول داشته‌ای حالت می‌ساختی — einen Termin (Akkusativ!)، zum Amt (Dativ!)، ohne Grund… این درس فقط نقشه را کامل و قاعده‌مند می‌کند — و آخرش، سه قالبِ حافظه که همه را به هم وصل می‌کند!'
    ],
    'sections': [
        {
            'h2': 'نقشهٔ کامل؛ جدولِ طلایی',
            'blocks': [
                ('table', ['حالت', 'نقش', 'der (مذکر)', 'die (مؤنث)', 'das (خنثی)', 'die (جمع)'],
                    [['Nominativ', 'فاعل — کی؟چه؟', 'der Termin', 'die Frage', 'das Ticket', 'die Tickets'],
                     ['Akkusativ', 'مفعول مستقیم — چه را؟', '**den** Termin', 'die Frage', 'das Ticket', 'die Tickets'],
                     ['Dativ', 'غیرمستقیم — به چه؟', '**dem** Termin', 'der Frage', 'dem Ticket', '**den** Tickets (+n!)'],
                     ['Genitiv', 'مالک — چه کسی؟', '**des** Termin(e)s', 'der Frage', 'des Tickets', 'der Tickets']]),
                ('p', 'می‌بینی؟ **فقط مذکرِ مفرد واقعاً عوض می‌شود** (der→den→dem→des) + جمعِ Dativ یک n می‌گیرد! نیمی از «وحشتِ حالت‌ها» همین‌جا تمام می‌شود!'),
            ]
        },
        {
            'h2': 'حروفِ اضافهٔ قفل‌کننده؛ هرکدام حالتِ خودش',
            'blocks': [
                ('table', ['همیشه Akkusativ', 'همیشه Dativ', 'هر دو (جهت/مکان!)'],
                    [['durch، für، gegen، ohne، um', 'aus، bei، mit، nach، seit، von، zu', 'in، an، auf، über، unter، vor'],
                     ['ohne Grund (بدونِ دلیل)', 'mit dem Team (با تیم)', 'in die Stadt (به شهر — حرکت!) / in der Stadt (در شهر — مکان!)'],
                     ['für den Test (برایِ تست)', 'zu dem Arzt → zum Arzt', 'an den Schreibtisch (به میز) / am Schreibtisch (سرِ میز)']]),
                ('p', 'و قانونِ طلاییِ «in/an/aufِ دو‌حالته»: **حرکت (wohin?) = Akkusativ؛ مکان (wo?) = Dativ** — „Ich stelle das Buch **auf den** Tisch“ (کتاب را روی میز می‌گذارم — حرکت!) ولی „Das Buch liegt **auf dem** Tisch“ (کتاب روی میز است — مکان!)'),
            ]
        },
        {
            'h2': 'سه فعلِ Dativ‌دارِ پرکاربرد',
            'blocks': [
                ('p', 'چند فعلِ آلمانی، مفعولِ Dativ می‌گیرند — معروف‌ترین‌ها: **helfen** (کمک‌کردن: „Ich helfe **dem** Kollegen“)، **danken** (تشکرکردن: „Ich danke **dir**“)، **gefallen** (خوش‌آمدن: „Das gefällt **mir**“)، **gehören** (مالِ بودن: „Das gehört **der** Firma“)، **antworten** (جواب‌دادن: „Ich antworte **ihm**“). این پنج فعل را با Dativ قفل کن — «Ich helfe dir gerne!» (با کمال میل کمکت می‌کنم!) جملهٔ محبوبِ همکاری!'),
            ]
        },
        {
            'h2': 'گفتگو: سه حالت در یک صحنه — تحویلِ تسک',
            'blocks': [
                ('ex', 'Der Teamlead gibt dem neuen Entwickler eine Aufgabe.', 'تیم‌لید به توسعه‌دهندهٔ جدید تسکی می‌دهد. — سه حالت در یک جمله: Der (Nominativ) + dem (Dativ — به چه کسی؟) + eine (Akkusativ — چه را؟)!'),
                ('ex', 'Der Entwickler dankt dem Teamlead und nimmt die Aufgabe an.', 'توسعه‌دهنده از تیم‌لید تشکر می‌کند و تسک را قبول می‌کند. — danken + Dativ؛ annehmen + Akkusativ + جدانشدنی!'),
                ('ex', 'Er hilft dem Team mit der API und gibt ihm Feedback.', 'به تیم با API کمک می‌کند و به او بازخورد می‌دهد. — helfen + Dativ (dem Team)؛ mit + Dativ (der API)؛ geben + Dativ (ihm) + Akkusativ (Feedback)!'),
                ('p', 'می‌بینی؟ جمله‌هایِ واقعی، حالت‌ها را طبیتی مخلوط می‌کنند — و تو با نقشهٔ جدول، هر کدام را می‌خوانی!'),
            ]
        },
        {
            'h2': 'اشتباه‌های رایجِ فارسی‌زبان‌ها در همین درس',
            'blocks': [
                ('p', 'این بخش را با یک قرارداد بخوان: هر ❌ یعنی «مغزِ فارسی‌زبانت این را می‌سازد و طبیعی است»، و هر ✅ یعنی «این همان چیزی است که گیرندهٔ آلمانی‌زبان می‌شنود». با هر جفت بلند تکرار کن تا شکلِ درست در گوشت نشست کند.'),
                ('ex', '❌ Ich helfe dich.', '❌ helfen همیشه Dativ: dir! «مغزِ فارسی» مفعولِ مستقیم می‌سازد — آلمانیِ helfen، «به کسی» می‌دهد!'),
                ('ex', '✅ Ich helfe dir. / Ich helfe dem Team.', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.'),
                ('ex', '❌ Ich gehe zu der Arzt.', '❌ Arzt مذکر است + zu + Dativ: zum Arzt! «zu der» هم گرامری است ولی هیچ‌کس نمی‌گویدش — zum!'),
                ('ex', '✅ Ich gehe zum Arzt. / zur Schule.', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.'),
                ('ex', '❌ Das Buch ist auf den Tisch. (مکان!)', '❌ «بودن» مکان است → Dativ: auf dem Tisch! حرکت (stellen/legen) → Akkusativ!'),
                ('ex', '✅ Das Buch liegt auf dem Tisch. / Ich lege das Buch auf den Tisch.', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.')
            ]
        },
        {
            'h2': 'تمرین‌های این درس — چهار قدم، بی‌عجله',
            'blocks': [
                ('p', 'تمرین: حالت‌ها را در جمله‌های خودت پیدا کن:'),
                ('ol', [
                    'پنج جملهٔ واقعی بنویس که در هرکدام، هر سه حالتِ Nominativ/Akkusativ/Dativ حاضر باشد.',
                    'جدولِ حروفِ اضافه را با پنج جملهٔ خودت تست کن: دو Akkusativ، دو Dativ، یک دو-حالته (هر دو versión!).',
                    'سه فعلِ Dativ‌دار را در سه جملهٔ واقعی به کار ببر: helfen، gefallen، gehören.',
                    'جملهٔ «der neue Entwickler gibt dem Team das Feedback» را با تمامِ جایگشت‌هایِ معنایی بازی کن — نقش‌ها را عوض کن و دوباره بساز!'
                ]),
                ('faq', [
                    ('پاسخ تمرین ۱', 'نمونه‌ها: „Der Manager gibt dem Praktikanten eine Aufgabe.“ · „Die Firma bietet den Mitarbeitern einen Kurs.“ · „Ich schicke meiner Kollegin das Dokument.“ — سه نقش در هر جمله؛ حالت‌ها را با سوال‌ها چک کن: چه؟ (Nom) چه را؟ (Akk) به چه کسی؟ (Dat)!'),
                    ('پاسخ تمرین ۲', '„Ich kaufe das für den Test.“ (für+Akk) · „Ohne den Kollegen geht das nicht.“ (ohne+Akk) · „Ich fahre mit dem Rad.“ (mit+Dat) · „Seit dem Montag bin ich krank.“ (seit+Dat) · „Ich gehe in die Stadt / Ich bin in der Stadt.“ — پنج جمله، پنج قفلِ حرفِ اضافه!'),
                    ('پاسخ تمرین ۳', '„Ich helfe dem Team bei der API.“ · „Die Wohnung gefällt mir total.“ · „Das Laptop gehört der Firma.“ — سه فعلِ Dativ؛ اگر این سه جمله روان آمدند، بزرگ‌ترین تلهٔ فارسی‌زبان‌ها را رد کردی!'),
                    ('پاسخ تمرین ۴', 'بازیِ جایگشت: „Der Praktikant gibt dem Manager das Feedback.“ (عمل معکوس!) · „Das Feedback hilft dem Team.“ (حالتِ عوض‌شده!) — هر جملهٔ جدید، نقش‌ها را جابه‌جا می‌کند و تو باید تعریف‌ها را دوباره چک کنی — بهترین ورزشِ مغزِ حالتی!')
                ])
            ]
        },
        {
            'h2': 'چالشِ امروز',
            'blocks': [
                ('quote', '🎯 امروز هر جملهٔ آلمانیِ مهمی که گفتی/نوشتی، یک بار «حالت‌سنجی» کن: فاعل چه بود؟ مفعولِ مستقیم؟ Dativ از کجا آمد؟ — پنج جمله، پنج چک؛ مغزِ حالتی‌ات روشن می‌ماند!')
            ]
        },
        {
            'h2': 'نکات مکالمهٔ واقعی که کتاب‌ها کم می‌گویند',
            'blocks': [
                ('ul', [
                    '**Genitiv در حالِ مرگِ محاوره‌ای است!** — گفتارِ روزمره، Genitiv را با «von + Dativ» عوض می‌کند: „Das Auto von meinem Kollegen» (ماشینِ همکارم) به‌جایِ „des Kollegen». نوشتار و رسمیت: Genitiv زنده و محترم! تو: در گفتار von + Dativ، در نامه Genitiv — هر دو درست، هر جای خودش!'
                ])
            ]
        },
    ],
    'takeaway': 'چهار حالت، چهار نقش: Nominativ فاعل، Akkusativ چه-را، Dativ به-چه‌کسی، Genitiv مالک. فقط مذکرِ مفرد عوض می‌شود (der/den/dem/des) + جمعِ Dativ با n! حروفِ قفل: mit/zu/bei/seit/von→Dativ؛ für/ohne/gegen→Akkusativ؛ in/an/auf→حرکت‌/مکان. helfen/gefallen/danken→Dativ!',
    'faq': [
        ('چطور بدون فکر، حالتِ درست بیاید؟', 'سه مرحلهٔ واقعی: ۱) عادتِ «با-تعریف-حفظ‌کردن» (هر اسم با der/die/das!) از درس ۱۰؛ ۲) سوالِ سریع: چه را؟ → Akkusativ؛ به کسی؟ → Dativ؛ ۳) فراوانی — هر جمله‌ای که می‌خوانی/می‌شنوی، حالت‌هایش را زیر ذهنی نگیر! بعد از ماه‌ها، ۹۰٪ حالت‌ها «شنیداری» می‌شوند — همان‌طور که فارسیِ «را» را بدونِ قاعده می‌گذاری!')
    ],
},

# ── درس ۷۶ ─────────────────────────────────────────────────────────────────
{
    'slug': 'german-prepositions',
    'title': 'حروفِ اضافه؛ mit، zu، bei، nach و نقشهٔ جهت',
    'desc': 'نقشهٔ حروفِ اضافهٔ آلمانیِ روزمره: جهت و مکان و زمان — با الگوهایِ «فعل + حرف» که نیمی از مکالمه‌ات را می‌سازند.',
    'keywords': 'حروف اضافه آلمانی, پیشوند آلمانی, mit zu bei nach, جهت آلمانی, گرامر آلمانی',
    'answer': 'حروفِ اضافه، «memberهای اتصالیِ» جمله‌اند: mit (با + Dat)، zu (به + Dat)، bei (نزد/در + Dat)، nach (به سمتِ + شهر/بعد از)، von (از)، in (در/به)، an (روی/کنار)، auf (رو). و قانونِ طلایی: هر فعلِ جدانشدنی، حرفِ اضافهٔ همیشگی‌اش را دارد — «warten auf»، «denken an»، «sich freuen über» — فعل+حرف را با هم حفظ کن!',
    'intro': [
        'حروفِ اضافهٔ آلمانی، کوچک‌ترین کلمات و بزرگ‌ترین تله‌ها! «به»ی فارسی، در آلمانی چهار شکل دارد (zu، nach، in، auf — بسته به مقصد!) و هر فعل، حرفِ همیشگیِ خودش را می‌خواهد!',
        'این درس دو نقشه می‌دهد: نقشهٔ «جهت و مکان و زمان» (به کجا؟ کجا؟ کِی؟) و نقشهٔ «فعل + حرف» (واژگانِ اتصالی) — با ۱۲ جفتِ پرکاربرد که نیمی از گفتارِ روزانه‌ات را می‌پوشانند. حروفِ اضافه، آخرین قطعه‌های پازلِ جمله‌هایت‌اند!'
    ],
    'sections': [
        {
            'h2': 'نقشهٔ «به کجا؟»؛ چهار «به»ی آلمانی',
            'blocks': [
                ('table', ['حرف', 'چه مقصدی؟', 'مثال'],
                    [['nach', 'شهر/کشورِ بدونِ تعریف + خانه!', 'nach Berlin، nach Iran، nach Hause!'],
                     ['zu (+Dat)', 'جای مشخص/شخص/اداره', 'zum Arzt، zur Arbeit، zu Sarah'],
                     ['in (+Akk برای حرکت!)', 'داخلِ جایی که «در»ش می‌روی', 'ins Büro، ins Kino، in die Stadt'],
                     ['auf', 'رویداد/بازارِ روباز', 'auf die Arbeit? نه! — auf einen Markt، aufs Amt (بعضی شهرها!)']]),
                ('ex', 'Ich gehe nach Hause, nachdem ich zum Supermarkt und zur Bank gegangen bin.', 'خانه می‌روم، بعد از آن‌که به سوپرمارکت و بانک رفتم. — پس بعد از آن‌که: بعداً! — چهار حرفِ جهت در دو جمله!')
            ]
        },
        {
            'h2': 'نقشهٔ «کجا؟» و «کِی؟»',
            'blocks': [
                ('table', ['سوال', 'حرف‌ها', 'مثال'],
                    [['Wo? (کجا — Dat)', 'in، an، auf، bei', 'im Büro، am Tisch، auf dem Stuhl، bei der Firma'],
                     ['Woher? (از کجا)', 'von، aus', 'von der Arbeit، aus dem Iran، aus Berlin'],
                     ['Wann? (کِی)', 'um، am، im، nach، vor، seit', 'um 9 Uhr، am Montag، im Mai، nach dem Essen، vor dem Meeting، seit einem Jahr']]),
                ('p', 'سه ستونِ «مکان/منبع/زمان» — و نکتهٔ طلاییِ زمان (از درس ۱۴): **um** ساعت، **am** روز، **im** ماه/سال، **nach/vor** بعد/قبلِ فعل‌اسمی، **seit** از-پیش-تا-حال! حروفِ اضافه، ساعتِ تقویمیِ تو هستند.'),
            ]
        },
        {
            'h2': 'فعل + حرف؛ ۱۲ جفتِ طلایی',
            'blocks': [
                ('table', ['فعل + حرف', 'معنی', 'جمله'],
                    [['warten **auf** +Akk', 'منتظرِ … بودن', 'Ich warte auf das Feedback.'],
                     ['denken **an** +Akk', 'فکر‌کردن به', 'Ich denke an das Meeting.'],
                     ['sich freuen **über** +Akk', 'خوشحال‌شدن از', 'Ich freue mich über das Ergebnis.'],
                     ['sich freuen **auf** +Akk', 'بی‌صبری‌برایِ آینده', 'Ich freue mich auf das Wochenende.'],
                     ['sich interessieren **für** +Akk', 'علاقه‌مندی به', 'Ich interessiere mich für Architektur.'],
                     ['sprechen **über** +Akk', 'صحبت‌کردن دربارهٔ', 'Wir sprechen über das Deploy.'],
                     ['fragen **nach** +Dat', 'پرسیدن از/دربارهٔ', 'Ich frage nach dem Termin.'],
                     ['teilnehmen **an** +Dat', 'شرکت‌کردن در', 'Ich nehme am Meeting teil.'],
                     ['helfen **bei** +Dat', 'کمک‌کردن در', 'Ich helfe bei der Migration.'],
                     ['sich bewerben **um** +Akk', 'درخواست‌دادنِ (شغل)', 'Ich bewerbe mich um die Stelle.'],
                     ['abhängen **von** +Dat', 'وابسته‌بودن به', 'Das hängt vom Budget ab.'],
                     ['verzichten **auf** +Akk', 'چشم‌پوشی‌کردن از', 'Wir verzichten auf den Bonus.']]),
                ('p', 'دو دشمنِ مشهور که باید از هم جدا شوند: **sich freuen über** (از گذشته/حال: خوشحالم از خبر!) در برابرِ **sich freuen auf** (برای آینده: دلم برای آخرِ هفته تنگ است!) — و **warten auf** (منتظرِ X) نه «warten für»!'),
            ]
        },
        {
            'h2': 'گفتگو: یک روزِ پر-حرفِ اضافه',
            'blocks': [
                ('ex', 'Morgens gehe ich zur Arbeit. Im Büro warte ich auf das Daily und spreche mit dem Team über das Wochenende.', 'صبح‌ها به کار می‌روم. در دفتر منتظرِ دیلی می‌مانم و با تیم دربارهٔ آخرِ هفته حرف می‌زنم. — zur + im + warten auf + mit + über: پنج حرفِ اضافه در دو جمله!'),
                ('ex', 'Nach dem Lunch denke ich an das Ticket und freue mich auf den Feierabend.', 'بعد از ناهار به تیکت فکر می‌کنم و برایِ فایرآبند بی‌تابم. — nach + denken an + freuen auf!'),
                ('ex', 'Abends gehe ich nach Hause und freue mich über den Tag.', 'شب‌ها خانه می‌روم و از روزم خوشحالم. — nach Hause + freuen über: همان جفتِ دشمن، در دو جملهٔ پشت‌سرهم!')
            ]
        },
        {
            'h2': 'اشتباه‌های رایجِ فارسی‌زبان‌ها در همین درس',
            'blocks': [
                ('p', 'این بخش را با یک قرارداد بخوان: هر ❌ یعنی «مغزِ فارسی‌زبانت این را می‌سازد و طبیعی است»، و هر ✅ یعنی «این همان چیزی است که گیرندهٔ آلمانی‌زبان می‌شنود». با هر جفت بلند تکرار کن تا شکلِ درست در گوشت نشست کند.'),
                ('ex', '❌ Ich warte für das Feedback.', '❌ ترجمهٔ مستقیمِ «منتظرِ» — آلمانی: warten **auf**! «für» قربانیِ رایجِ فارسی‌زبان‌هاست!'),
                ('ex', '✅ Ich warte auf das Feedback.', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.'),
                ('ex', '❌ Ich gehe zu Berlin.', '❌ شهرِ بزرگِ بی‌تعریف: nach! zu برای جای مشخص است (zum Bahnhof).'),
                ('ex', '✅ Ich fahre nach Berlin. / Ich fahre zum Flughafen.', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.'),
                ('ex', '❌ Ich freue mich auf das Geschenk. (که گرفتی!)', '❌ گرفتی و خوشحالی = über! auf فقط برایِ آیندهٔ در-راه!'),
                ('ex', '✅ Ich freue mich über das Geschenk — danke!', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.')
            ]
        },
        {
            'h2': 'تمرین‌های این درس — چهار قدم، بی‌عجله',
            'blocks': [
                ('p', 'تمرین: نقشه‌های حرفِ اضافه را با زندگیِ خودت تست کن:'),
                ('ol', [
                    'مسیرِ امروزت را با چهار «به» بگو: شهر؟ جای مشخص؟ داخلِ جا؟',
                    'پنج جملهٔ زمان با پنج حرف بساز: um، am، im، nach، seit.',
                    'شش جفتِ فعل+حرف را در شش جملهٔ واقعیِ کاری/روزمره به کار ببر.',
                    'دشمنِ über/auf را با سه جفتِ جواب-سوال تمرین کن: «خوشحالی از چی؟ برای چی؟»'
                ]),
                ('faq', [
                    ('پاسخ تمرین ۱', '„Ich fahre nach München, gehe zum Hotel, dann ins Restaurant und später auf den Weihnachtsmarkt.“ — چهار «به» در چهار مقصدِ واقعیِ یک روز!'),
                    ('پاسخ تمرین ۲', '„Um 9 beginnt das Meeting. Am Dienstag habe ich Termin. Im Dezember fliege ich. Nach dem Essen gehe ich. Seit einem Jahr lerne ich Deutsch.“ — پنج جملهٔ زمانیِ کامل!'),
                    ('پاسخ تمرین ۳', '„Ich warte auf den Review.“ · „Wir sprechen über die Architektur.“ · „Ich nehme am Workshop teil.“ · „Das hängt vom Team ab.“ · „Ich helfe beim Deploy.“ · „Ich interessiere mich für K8s.“ — شش جملهٔ کاریِ پرکاربرد!'),
                    ('پاسخ تمرین ۴', '„Ich freue mich über das gute Feedback.“ (از خبرِ رسیده) در برابرِ „Ich freue mich auf den Urlaub.“ (برای آینده) — سه جفتِ سوالی برایت بساز و هر بار، جهتِ زمان را چک کن: گذشته/حال → über؛ آینده → auf!')
                ])
            ]
        },
        {
            'h2': 'چالشِ امروز',
            'blocks': [
                ('quote', '🎯 امروز سه فعل+حرفِ جدیدِ این درس را در جمله‌های واقعی به کار ببر — و یک «گوگل-چک» بکن: هر فعلِ آلمانیِ جدید که یاد می‌گیری، حرفِ اضافه‌اش را هم گوگل کن! «abhängen von»، «sich bewerben um» — از این به بعد، فعل‌ها را «تک» یاد نگیر، «جفت» یاد بگیر!')
            ]
        },
        {
            'h2': 'نکات مکالمهٔ واقعی که کتاب‌ها کم می‌گویند',
            'blocks': [
                ('ul', [
                    '**«bei» رفیقِ اداریِ توست** — bei der Firma (در شرکت)، beim Arzt (نزدِ دکتر)، bei der Arbeit (سرِ کار)، bei mir (پیشِ من!) — «bei» یعنی «در محدودهٔ کاری/خدماتیِ» — و سه جملهٔ خانه: „Komm bei mir vorbei!“ (به من سر بزن!)'
                ])
            ]
        },
    ],
    'takeaway': 'جهت: nach شهر/Hause، zu جای-مشخص (zum/zur)، in داخل، auf رویداد. مکان: in/an/auf/بِی + Dat؛ منبع: von/aus؛ زمان: um/am/im/nach/vor/seit. فعل+حرف را جفت حفظ کن: warten auf، denken an، freuen über/auf، sprechen über، teilnehmen an، helfen bei — دو دشمنِ über/auf را با زمان جدا کن!',
    'faq': [
        ('حروفِ اضافه را چطور «با فعل» یاد کنم؟', 'سه ترفندِ واقعی: ۱) هر فعلِ جدید را در جملهٔ نمونه یاد بگیر (نه تنها فعل!) — در آپ‌ورد: «warten auf — Ich warte auf dich!»؛ ۲) گروه‌سازی: حرفِ «auf» با انتظار و آینده (warten auf، freuen auf، sich vorbereiten auf)؛ ۳) فراوانی — هر جمله‌ای که خواندی، فعل+حرف را دورخط کن! مغز، الگو را از فراوانی می‌گیرد نه از لیست!')
    ],
},

# ── درس ۷۷ ─────────────────────────────────────────────────────────────────
{
    'slug': 'german-adjectives',
    'title': 'صفت‌ها پیش از اسم؛ انتهای‌های …',
    'desc': 'جدولِ معروفِ صفت‌ها: بعد از der/die/das و ein و بدونِ تعریف — با ترفندهای حافظه و الگوهایِ پرکاربرد.',
    'keywords': 'صفت آلمانی, Adjektivdeklination, انتهای صفت آلمانی, گرامر آلمانی, صفت قبل اسم',
    'answer': 'صفتِ پیش از اسم، «انتهایِ حالت» می‌گیرد — و سه سناریو دارد: ۱) بعد از der/die/das: -e یا -en (ساده‌ترین!)؛ ۲) بعد از ein/kein/mein: انتهایِ «تعریف‌گونه» (der gute Mann → ein guter Mann!)؛ ۳) بدونِ تعریف: انتهایِ کاملِ تعریف! قاعدهٔ طلایی: «انتهایِ صفت، خالیِ تعریف را پر می‌کند» — der → -e، einen → -en، ein → -er!',
    'intro': [
        'جدولِ صفت‌ها، «آپوکالیپسِ» کتاب‌هایِ آلمانی است — چهار جدولِ شش‌خانه‌ای! اما نگاهِ مهندسی بهش بده: سه سناریو، دو الگو و یک ایدهٔ مرکزی: «انتهایِ صفت، نقشِ تعریفِ غایب را بازی می‌کند»!',
        'خبرِ خوبِ بزرگ: ۸۰٪ صفت‌هایِ زندگیِ روزمره فقط دو شکل می‌بینند: **-e** (مفردِ با تعریف: der gute Mann) و **-en** (جمع و مفعول: die guten Leute!). اگر این دو را قفل کنی و قاعدهٔ «جای خالیِ تعریف» را بفهمی، بقیه‌ی جدول، منطقی می‌شود!'
    ],
    'sections': [
        {
            'h2': 'سناریوی ۱: بعد از der/die/das — آسان‌ترین!',
            'blocks': [
                ('table', ['حالت', 'مذکر', 'مؤنث', 'خنثی', 'جمع'],
                    [['Nominativ', 'der gut**e** Mann', 'die gut**e** Frage', 'das gut**e** Ticket', 'die gut**en** Ideen'],
                     ['Akkusativ', 'den gut**en** Mann', 'die gut**e** Frage', 'das gut**e** Ticket', 'die gut**en** Ideen'],
                     ['Dativ', 'dem gut**en** Mann', 'der gut**en** Frage', 'dem gut**en** Ticket', 'den gut**en** Ideen']]),
                ('p', 'الگو: **مفردِ اولِ جمله → -e؛ هرچیزِ دیگر → -en!** فقط دو شکل! „Der neue Kollege ist nett. Ich mag den neuen Kollegen. Ich helfe dem neuen Kollegen.“ — سه حالت، دو انتهای!'),
            ]
        },
        {
            'h2': 'سناریوی ۲: بعد از ein/kein/mein — «تعریف‌گونه»',
            'blocks': [
                ('p', 'اینجا جادو اتفاق می‌افتد: ein نمی‌تواند «جنس» را نشان بدهد — پس صفت، جای خالی‌اش را پر می‌کند! قاعده: **انتهایِ صفت = انتهایِ تعریفِ هم‌نقش**!'),
                ('table', ['حالت', 'مذکر', 'مؤنث', 'خنثی'],
                    [['Nominativ', 'ein gut**er** Mann (جایِ der!)', 'eine gut**e** Frage', 'ein gut**es** Ticket (جایِ das!)'],
                     ['Akkusativ', 'einen gut**en** Mann', 'eine gut**e** Frage', 'ein gut**es** Ticket']]),
                ('ex', 'Ich habe einen neuen Laptop mit einem schnellen Prozessor und einer guten Tastatur.', 'لپ‌تاپِ جدیدی با پردازندهٔ سریع و کیبوردِ خوب گرفتم. — drei صفت در سه حالت: neuen (Akk مذکر)، schnellen (Dat مذکر)، guten (Dat مؤنث)!')
            ]
        },
        {
            'h2': 'سناریوی ۳: بدونِ تعریف — کامل‌ترین',
            'blocks': [
                ('p', 'بدونِ تعریف، صفت «همه‌چیز» را نشان می‌دهد — انتهایِ کامل: „**Guter** Kaffee!« (قهوهٔ خوب!)، „**Kaltes** Wasser, bitte« (آبِ سرد لطفاً)، „mit **guten** Ideen« (با ایده‌هایِ خوب — Dat جمع!). این سناریو در منو، آگهی و تعریف‌هاست: „Suche günstige Wohnung« (خانهٔ ارزان می‌گردم!)'),
                ('ex', 'Frisches Brot, heißer Kaffee, guter Start in den Tag!', 'نانِ تازه، قهوهٔ داغ، شروعِ خوبی برای روز! — سه صفتِ بی‌تعریف: شروعِ آگهیِ هر نانواییِ آلمان!')
            ]
        },
        {
            'h2': 'گفتگو: در جلسهٔ خریدِ تجهیزات',
            'blocks': [
                ('ex', 'Ich brauche einen schnellen Rechner mit einer großen Festplatte.', 'کامپیوترِ سریعی با هاردِ بزرگ لازم دارم. — einen schnellen (Akk مذکر + en!) + einer großen (Dat مؤنث + en!)'),
                ('ex', 'Was halten Sie von dem kleinen Modell? — Das kleine ist günstiger, aber das große ist leiser.', 'نظرتان دربارهٔ مدلِ کوچک چیست؟ — کوچکی ارزان‌تر است ولی بزرگی آرام‌تر. — صفت به‌عنوانِ اسم!: das Kleine/das Große!'),
                ('ex', 'Nehmen Sie das große — mit dem schnellen Prozessor. Das ist eine gute Entscheidung!', 'بزرگ را بگیرید — با پردازندهٔ سریع. این تصمیمِ خوبی است! — drei صفت در سه قالبِ متفاوت — جمله‌هایِ واقعیِ خرید!'),
            ]
        },
        {
            'h2': 'اشتباه‌های رایجِ فارسی‌زبان‌ها در همین درس',
            'blocks': [
                ('p', 'این بخش را با یک قرارداد بخوان: هر ❌ یعنی «مغزِ فارسی‌زبانت این را می‌سازد و طبیعی است»، و هر ✅ یعنی «این همان چیزی است که گیرندهٔ آلمانی‌زبان می‌شنود». با هر جفت بلند تکرار کن تا شکلِ درست در گوشت نشست کند.'),
                ('ex', '❌ Ich habe ein neuer Laptop.', '❌ ein + مذکرِ Akkusativ → neuen! «ein neuer» فقط در Nominativ (Ein neuer Laptop kam an! [لپ‌تاپِ جدیدی رسید!])'),
                ('ex', '✅ Ich habe einen neuen Laptop gekauft.', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.'),
                ('ex', '❌ die guten Mann (مذکرِ مفرد + جمع‌گونه!)', '❌ مفردِ مؤنثِ Nominativ → gute؛ جمع → guten — der gute Mann / die guten Männer!'),
                ('ex', '✅ der gute Mann · die gute Frage · die guten Ideen', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.'),
                ('ex', '❌ heißer Wasser! (مؤنث: heiß**es**!)', '❌ Wasser خنثی است: heißes Wasser! قفل: جنسیت را با اسم یاد بگیر (درس ۱۰!) — صفت، از جنسیت پیروی می‌کند!'),
                ('ex', '✅ heißes Wasser · kaltes Bier · frisches Brot', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.')
            ]
        },
        {
            'h2': 'تمرین‌های این درس — چهار قدم، بی‌عجله',
            'blocks': [
                ('p', 'تمرین: صفت‌ها را با وسایلِ واقعیِ خودت بساز:'),
                ('ol', [
                    'سه جمله با «der/die/das + صفت + اسم» در سه حالت بساز (Nom/Akk/Dat).',
                    'سه جمله با ein/mein/kein + صفت — در سه جنسیتِ متفاوت!',
                    'سه جملهٔ بی‌تعریف بساز: تعریفِ محبوب (قهوه؟ خانه؟ شروعِ روز؟).',
                    'جدولِ «-e/-en» را با یک صفتِ واقعیِ خودت (schnell؟ groß؟) کامل صرف کن.'
                ]),
                ('faq', [
                    ('پاسخ تمرین ۱', '„Der alte Rechner ist langsam. Ich verkaufe den alten Rechner. Ich helfe dem alten Rechner? — NEIN: Ich werfe den alten Rechner weg!“ 😄 — سه حالت با -e/-en!'),
                    ('پاسخ تمرین ۲', '„Ein neuer Monitor hilft. Ich brauche einen neuen Monitor. Meine neue Tastatur ist da. Kein altes Kabel brauche ich mehr.“ — چهار جمله، سه جنسیت، هر سه قالبِ ein-دار!'),
                    ('پاسخ تمرین ۳', '„Guter Kaffee macht den Code besser.“ (قهوهٔ خوب، کد را بهتر می‌کند!) · „Ruhiges Büro, klare Gedanken.“ (دفترِ آرام، فکرِ روشن.) · „Neues Leben, neue Stadt!“ — سه جملهٔ بی‌تعریفِ پوستری! 😄'),
                    ('پاسخ تمرین ۴', 'schnell: der schnelle Server · den schnellen Server · dem schnellen Server · die schnellen Server — یک صفت × چهار خانه؛ بعد یک صفتِ دیگر — دو صفتِ کامل، قالبِ مغزِ تو!')
                ])
            ]
        },
        {
            'h2': 'چالشِ امروز',
            'blocks': [
                ('quote', '🎯 امروز پنج «اسم+صفتِ» واقعی از محیطِ کار/خانه‌ات را بلند توصیف کن — با تعریفِ درست و حالتِ درست: „der schnelle neue Server«، „mit meinem alten Kopfhörer«… — پنج جمله، پنج انتهایِ صحت‌سنجی‌شده!')
            ]
        },
        {
            'h2': 'نکات مکالمهٔ واقعی که کتاب‌ها کم می‌گویند',
            'blocks': [
                ('ul', [
                    '**صفتِ بعد از فعلِ sein/haben/werden هیچ انتهایی نمی‌گیرد!** — „Der Server ist schnell« (سرور سریع است) — نه «schneller Server»! انتهای فقط وقتی است که صفت «پیش از اسم» بنشیند! این «صفتِ predicates» رایج‌ترین جاست — و ساده‌ترین!',
                    '**مقایسه و تفضیل هم صفت‌اند!** — „Der schnellere Server« (سرورِ سریع‌تر)، „die schnellste Lösung» (سریع‌ترین راه‌حل) — درس ۲۰ مقایسه را داد؛ این‌جا انتهایش: مثل صفتِ ساده! „Ich nehme den schnelleren Server« (سرورِ سریع‌تر را می‌گیرم — Akk + en!)'
                ])
            ]
        },
    ],
    'takeaway': 'صفتِ پیش از اسم، انتهای می‌گیرد: بعد از der/die/das فقط -e/-en؛ بعد از ein/kein/mein «تعریف‌گونه» (ein guter، einen guten!)؛ بی‌تعریف: کامل. قاعدهٔ طلایی: انتهایِ صفت، جایِ خالیِ تعریف را پر می‌کند! صفتِ بعد از sein بی‌پسوند است — „Der Server ist schnell.«',
    'faq': [
        ('آیا باید «همه‌ی جدول‌ها» را حفظ کنم؟', 'نه! سه‌گانهٔ واقعی: ۱) الگوی -e/-en را قفل کن (۸۰٪ استفاده!)؛ ۲) سه‌جفتِ طلاییِ ein-دار را حفظ کن: ein guter/einen guten/ein gutes؛ ۳) بقیه را از فراوانی — هر جمله‌ای که می‌خوانی، صفت‌ها را نگاه کن! مغزِ زبانی، جدول‌ها را از متن می‌سازد نه از حفظِ کور — و تو، ماه‌هاست که داري از متن می‌خوانی!')
    ],
},

# ── درس ۷۸ ─────────────────────────────────────────────────────────────────
{
    'slug': 'german-konjunktiv2',
    'title': 'Konjunktiv II؛ مؤدب‌ترین ابزارِ زبانِ آلمانی',
    'desc': 'جهانِ «می‌شد و اگر»: würde، könnte، hätte — شکل‌هایِ مؤدبِ درخواست، آرزو، پیشنهاد و فرض — زبانِ نرمِ طلاییِ آلمانی.',
    'keywords': 'Konjunktiv 2 آلمانی, würde könnte hätte, مؤدب آلمانی, شرطی آلمانی, گرامر آلمانی',
    'answer': 'Konjunktiv II، زبانِ «غیر-واقعیِ مؤدب» است: würde + مصدر (می‌کردم)، könnte (می‌توانستم)، hätte (می‌داشتم)، wäre (می‌بودم). کاربردش: درخواستِ مؤدب (Könnten Sie…؟)، آرزو (Ich hätte gern…)، پیشنهاد (Wie wäre es mit…؟) و فرضِ شرطی (Wenn ich Zeit hätte، würde ich…). سه کلمهٔ würde/könnte/hätte — نصفِ مؤدب‌بودنِ آلمانی!',
    'intro': [
        'به شیرین‌ترین درسِ گرامریِ دوره رسیدیم! Konjunktiv II، همان چیزی است که از درس‌های اول لمسش کردی: möchte، hätte gern، Könnten Sie… — حالا کلِ ماشینش را باز می‌کنیم!',
        'چرا «شیرین‌ترین»؟ چون این درس، شخصیتِ زبانی‌ات را می‌سازد: از «Ich will!» (می‌خواهم!) به «Ich würde gerne…» (دوست می‌ داشتم…) — از سفارش به درخواست، از امر به همکاری. آلمانیِ مؤدب، آلمانیِ حرفه‌ای است — و این درس، جعبه‌ابزارِ کاملش است!'
    ],
    'sections': [
        {
            'h2': 'شکل‌ها؛ چهار ستونِ طلایی',
            'blocks': [
                ('table', ['مصدر', 'Konjunktiv II', 'معنی', 'جمله'],
                    [['werden', 'würde', 'می‌کردم/می‌بود', 'Ich würde das machen.'],
                     ['können', 'könnte', 'می‌توانستم/می‌توانم (مؤدب)', 'Könntest du helfen?'],
                     ['haben', 'hätte', 'می‌داشتم/داشتم‌باشد', 'Ich hätte eine Frage.'],
                     ['sein', 'wäre', 'می‌بودم/بودی‌باشد', 'Das wäre super!'],
                     ['mögen', 'möchte', 'دوست می‌داشتم', 'Ich möchte bestellen.']]),
                ('p', 'نکتهٔ ساختِ بقیهٔ فعل‌ها: **würde + مصدر** جایگزینِ همه می‌شود! „Ich würde gehen« (می‌رفتم) — آلمانیِ گفتاری، würde را به همه‌ی فعل‌ها می‌دهد؛ فقط این چهار-پنج فعلِ بالا، شکلِ خودشان را دارند و ترجیح می‌شوند!'),
            ]
        },
        {
            'h2': 'چهار کاربرد؛ درخواست، آرزو، پیشنهاد، فرض',
            'blocks': [
                ('ex', 'درخواستِ مؤدب: Könnten Sie mir bitte helfen? — Ich hätte da eine kurze Frage.', 'می‌توانستید لطفاً کمکم کنید؟ — یک سوالِ کوتاه می‌خواستم. — könnte + hätte: جفتِ طلاییِ شروعِ هر گفتگویِ اداری!'),
                ('ex', 'آرزو: Ich würde gern mehr Zeit fürs Lernen haben. / Ich wäre gern dabei!', 'دوست داشتم زمانِ بیشتری برای درس داشته باشم. / کاش آنجا بودم! — würde gern + wäre gern: زبانِ آرزوهایِ مؤدب!'),
                ('ex', 'پیشنهاد: Wie wäre es mit einem Kaffee? / Wir könnten das gemeinsam machen.', 'چطوره یک قهوه؟ / می‌توانستیم این را با هم بکنیم. — Wie wäre es mit…؟ قالبِ پادشاهِ پیشنهاد!'),
                ('ex', 'فرضِ شرطی: Wenn ich mehr Zeit hätte, würde ich Deutsch bis B2 lernen.', 'اگر زمانِ بیشتری داشتم، آلمانی را تا B2 یاد می‌گرفتم. — Wenn + [Konjunktiv]، [würde + مصدر] — جملهٔ رؤیاهایِ زبانی!')
            ]
        },
        {
            'h2': 'گفتگو: جلسهٔ مؤدب — همه‌چیز Konjunktiv!',
            'blocks': [
                ('ex', 'Könnten wir kurz über den Deploy sprechen? Ich hätte einen Vorschlag.', 'می‌توانستیم کوتاه دربارهٔ دیپلوی حرف بزنیم؟ یک پیشنهاد می‌خواستم بدهم. — könnte + hätte: دو جملهٔ اولِ حرفه‌ای!'),
                ('ex', 'Wie wäre es, wenn wir den Deploy auf Morgen verschieben? Wir hätten dann mehr Testzeit.', 'چطوره دیپلوی را به فردا ببریم؟ آن‌وقت زمانِ تستِ بیشتری می‌داشتیم. — Wie wäre es، wenn + hätte: پیشنهادِ کاملِ سه‌بخشی!'),
                ('ex', 'Das wäre eine Option. Ich könnte die Tests heute Nacht vorbereiten.', 'این یک گزینه بود. می‌توانستم تست‌ها را امشب آماده کنم. — wäre + könnte: پاسخِ همکاری‌محور!'),
                ('ex', 'Wäre es für Sie okay, wenn ich das Ticket übernehme?', 'برایتان اوکی بود که تیکت را من برعهده بگیرم؟ — Wäre es okay، wenn…؟ مؤدب‌ترین درخواستِ کاریِ دنیا!')
            ]
        },
        {
            'h2': 'اشتباه‌های رایجِ فارسی‌زبان‌ها در همین درس',
            'blocks': [
                ('p', 'این بخش را با یک قرارداد بخوان: هر ❌ یعنی «مغزِ فارسی‌زبانت این را می‌سازد و طبیعی است»، و هر ✅ یعنی «این همان چیزی است که گیرندهٔ آلمانی‌زبان می‌شنود». با هر جفت بلند تکرار کن تا شکلِ درست در گوشت نشست کند.'),
                ('ex', '❌ Ich will einen Kaffee. (در کافه)', '❌ درست اما «کودکانه-سفت»! بزرگِ مؤدب: möchte/hätte gern!'),
                ('ex', '✅ Ich hätte gern einen Kaffee. / Ich möchte einen Cappuccino.', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.'),
                ('ex', '❌ Wenn ich Zeit habe، würde ich … (فرضِ غیر-واقعی با زمانِ حال!)', '❌ فرضِ کاذب نیاز به Konjunktiv در «اگر» هم دارد: Wenn ich Zeit HÄTTE!'),
                ('ex', '✅ Wenn ich Zeit hätte، würde ich kommen. / Wenn ich reich wäre…', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.'),
                ('ex', '❌ Kannst du mir helfen؟ (درست است ولی…)', '❌ نه غلط! فقط «ساده» — سطحِ بالاترِ مؤدب: könntest! در اداره و مشتری: Könnten Sie؟'),
                ('ex', '✅ Könntest du mir kurz helfen? — Könnten Sie mir bitte helfen?', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.')
            ]
        },
        {
            'h2': 'تمرین‌های این درس — چهار قدم، بی‌عجله',
            'blocks': [
                ('p', 'تمرین: مؤدب‌ترین خودت را بساز!'),
                ('ol', [
                    'سه درخواستِ روزمره‌ات را «ارتقا» بده: از wollen/können به würde/könnte/hätte.',
                    'سه پیشنهاد با «Wie wäre es mit…» بساز — برای امروز، آخرِ هفته، تیم.',
                    'دو جملهٔ شرطیِ رؤیایی بنویس: Wenn ich … hätte/wäre، würde ich …',
                    'دیالوگِ جلسهٔ مؤدب را کامل اجرا کن — با هر نقش!'
                ]),
                ('faq', [
                    ('پاسخ تمرین ۱', '„Ich will Kaffee → Ich hätte gern einen Kaffee.“ · „Kannst du helfen؟ → Könntest du kurz helfen?“ · „Ich brauche Hilfe → Ich hätte da eine Frage“ — سه ارتقای مؤدبِ شخصیتی!'),
                    ('پاسخ تمرین ۲', '„Wie wäre es mit einem Spaziergang?“ · „Wie wäre es mit Samstags?“ · „Wie wäre es، wenn wir das als Team machen?“ — سه پیشنهاد در سه قالبِ متفاوت!'),
                    ('پاسخ تمرین ۳', '„Wenn ich mehr Zeit hätte، würde ich Klavier lernen.“ · „Wenn ich in Wien wäre، würde ich jeden Tag Kaffeehäuser besuchen.“ — دو رؤیای شرطی؛ برای هرکدام ادامه بساز!'),
                    ('پاسخ تمرین ۴', 'اجرای کامل با نقش‌ها — و بعد، خودت را ضبط کن: «Könnten wir…، Ich hätte…، Wie wäre es…» — این سه جمله، صدای حرفه‌ایِ تو در هر جلسهٔ آلمانی‌اند!')
                ])
            ]
        },
        {
            'h2': 'چالشِ امروز',
            'blocks': [
                ('quote', '🎯 امروز هر درخواستی که داشتی، یک‌بار با Konjunktiv بگو — wäre/könnte/hätte/würde! سه بار در گفتگو، سه بار در چت — مؤدب‌ترین روزِ زبانیِ عمرت!')
            ]
        },
        {
            'h2': 'نکات مکالمهٔ واقعی که کتاب‌ها کم می‌گویند',
            'blocks': [
                ('ul', [
                    '**«hätte» بدونِ «gern» هم آرزوست!** — „Ich hätte eine Frage« (سوالی می‌خواستم…) — hasِ مؤدبِ عالی! و با gern: „Ich hätte gern…» = سفارشِ طلایی. این یک کلمه، ده‌ها جملهٔ لایقِ مؤدب می‌سازد!'
                ])
            ]
        },
    ],
    'takeaway': 'Konjunktiv II = زبانِ مؤدبِ غیر-واقعی: würde + مصدر، könnte، hätte، wäre (+ möchte!). چهار کاربرد: درخواست (Könnten Sie؟)، آرزو (hätte gern)، پیشنهاد (Wie wäre es mit…؟)، فرض (Wenn … hätte، würde ich …). از «Ich will» به «Ich hätte gern» — شخصیتِ زبانیِ حرفه‌ای!',
    'faq': [
        ('Konjunktiv II و «möchte» چه رابطه‌ای دارند؟', 'möchte خودش Konjunktiv IIِ «mögen» است — قدیمی‌ترین و محبوب‌ترینش! تو از درس ۲۳ داشتش! حالا خانواده‌اش را دیدی: möchte (دوست‌داشتم)، könnte (می‌توانستم)، hätte (می‌داشتم)، wäre (می‌بودم)، würde (می‌کردم) — پنج‌قلوهایِ مؤدبِ طلاییِ زبانِ آلمانی!')
    ],
},

# ── درس ۷۹ ─────────────────────────────────────────────────────────────────
{
    'slug': 'german-passive',
    'title': 'مجهول؛ گزارش‌های فنی و نامه‌های رسمی',
    'desc': 'Der Code wird geschrieben… — ساختِ مجهولِ حال و گذشته، و جایگاهش در داکیومنت، نامهٔ اداری و گفتگوی حرفه‌ای.',
    'keywords': 'مجهول آلمانی, Passiv آلمانی, wird gemacht, گرامر آلمانی, مجهول رسمی',
    'answer': 'مجهولِ آلمانی: **werden + Partizip** — „Der Code wird geschrieben» (کد نوشته می‌شود)، „wurde deployt» (دیپلوی شد)، „ist veröffentlicht worden» (منتشر شده). مجهول، زبانِ داکیومنتِ فنی و نامه‌های اداری است: بدونِ «من»، فقط فرایند — از «Ich habe deployt» به «Das Deployment wurde durchgeführt».',
    'intro': [
        'مجهول در آلمانی، «زبانِ بی‌شخصِ حرفه‌ای» است: نامه‌های اداری، داکیومنتِ فنی، گزارش‌ها و اخبار — همه‌جا! و تو از درس‌های ۵۳ و ۶۱ قالبش را لمس کردی: „Ihr Antrag wird geprüft» — حالا کاملش را می‌سازی!',
        'دو کاربردِ طلایی: ۱) رسمیتِ اداری (بدونِ من!)؛ ۲) تمرکز روی فرایند نه فاعل — در ریویو و داکیومنتِ فنی، مجهولِ مؤدبِ «این حل می‌شود» به‌جای «من حلش کردم»! این درس، آخرین ابزارِ بزرگِ گرامریِ زبانِ رسمیِ توست!'
    ],
    'sections': [
        {
            'h2': 'ساختِ مجهول؛ سه زمانِ پرکاربرد',
            'blocks': [
                ('table', ['زمان', 'ساخت', 'مثال'],
                    [['حال', 'wird/werden + Partizip', 'Der Bug wird gefixt. (باگ فیکس می‌شود)'],
                     ['گذشته', 'wurde/wurden + Partizip', 'Der Deploy wurde verschoben. (دیپلوی به تعویق افتاد)'],
                     ['کامل', 'ist + Partizip + worden', 'Die Version ist veröffentlicht worden. (نسخه منتشر شده است)'],
                     ['با مودال!', 'muss/kann + … + werden', 'Das muss heute noch werden? — Das muss noch gefixt werden! (باید هنوز فیکس شود)']]),
                ('ex', 'Der Antrag wird geprüft. Die Unterlagen wurden überprüft. Der Bescheid ist verschickt worden.', 'درخواست بررسی می‌شود. مدارک بازبینی شدند. جواب ارسال شده است. — سه زمانِ مجهول در سه جملهٔ اداریِ واقعی — دقیقاً نامه‌هایی که می‌گیری!'),
            ]
        },
        {
            'h2': 'فاعلِ مجهول؛ «von» و «durch»',
            'blocks': [
                ('p', 'اگر فاعل را بخواهی بگویی: **von + Dativ** (شخص!) یا **durch + Akkusativ** (وسیله/سبب!): „Der Code wurde **von Sarah** reviewed« (کد توسطِ سارا ریویو شد) — „Der Fehler wurde **durch einen Timing-Bug** verursacht» (خطا به‌واسطهٔ یک باگِ تایمینگ ایجاد شد). در نامهٔ اداری و پست‌مورتم: von + شخص، durch + علت — دو حرفِ ردیابِ دقیق!'),
            ]
        },
        {
            'h2': 'گفتگو: پست‌مورتم و داکیومنت — مجهولِ حرفه‌ای',
            'blocks': [
                ('ex', 'Bericht: Am Freitag wurde die Version 2.5.0 deployed. Kurz danach wurde eine erhöhte Fehlerquote festgestellt.', 'گزارش: جمعه نسخهٔ ۲.۵.۰ دیپلوی شد. مدتی بعد نرخِ خطایِ بالاتری مشاهده شد. — feststellen در مجهول: «مشاهده شد» — بی‌نفرِ رسمی!'),
                ('ex', 'Der Rollback wurde innerhalb von 20 Minuten durchgeführt. Die Ursache wurde durch die Log-Analyse identifiziert.', 'رول‌بک در عرضِ ۲۰ دقیقه انجام شد. علت از طریقِ تحلیلِ لاگ شناسایی شد. — durchgeführt + identifiziert: دو فعلِ رسمیِ گزارشِ حرفه‌ای!'),
                ('ex', 'Es wurde beschlossen، den Check in die Pipeline zu integrieren. Damit kann das künftig vermieden werden.', 'تصمیم گرفته شد که چک را در پایپ‌لاین یکپارچه کنیم. بدین‌ترتیب می‌توان از این در آینده اجتناب شد. — «Es wurde beschlossen» (تصمیم گرفته شد) + مجهولِ مودالی: می‌توان اجتناب شد — گزارشِ کاملِ بی‌جنگ!'),
            ]
        },
        {
            'h2': 'اشتباه‌های رایجِ فارسی‌زبان‌ها در همین درس',
            'blocks': [
                ('p', 'این بخش را با یک قرارداد بخوان: هر ❌ یعنی «مغزِ فارسی‌زبانت این را می‌سازد و طبیعی است»، و هر ✅ یعنی «این همان چیزی است که گیرندهٔ آلمانی‌زبان می‌شنود». با هر جفت بلند تکرار کن تا شکلِ درست در گوشت نشست کند.'),
                ('ex', '❌ Der Code ist geschrieben. (به‌عنوانِ مجهولِ حال!)', '❌ ist + Partizip حالتِ «کامل/نتیجه» است (Zustandspassiv!) — مجهولِ فرایندِ حال: wird geschrieben!'),
                ('ex', '✅ Der Code wird jetzt geschrieben. / Der Code ist fertig geschrieben.', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.'),
                ('ex', '❌ Ich wurde geprüft von der Polizei. (ترتیب + معنا!)', '❌ در «من بررسی شدم» معنا غلط می‌شود! مفعولِ جمله باید «موضوع» باشد: Der Antrag wurde geprüft!'),
                ('ex', '✅ Mein Antrag wurde geprüft. / Ich wurde gefragt. (من سوال شدم — درست!)', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.'),
                ('ex', '❌ Das muss werden gemacht.', '❌ مودال + Partizip + werden — ترتیبِ آخرِ جمله! «muss … gemacht werden»!'),
                ('ex', '✅ Das muss noch gemacht werden. / Das kann nicht geändert werden.', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.')
            ]
        },
        {
            'h2': 'تمرین‌های این درس — چهار قدم، بی‌عجله',
            'blocks': [
                ('p', 'تمرین: گزارش‌نویسِ حرفه‌ای شو!'),
                ('ol', [
                    'پنج جملهٔ «من»محور را مجهول کن: از Ich habe… به … wurde …!',
                    'یک گزارشِ سه‌جمله‌ایِ پست‌مورتم بنویس — فقط مجهول!',
                    'سه جملهٔ مجهولِ مودالی بساز: muss/kann/sollte … werden.',
                    'یک پاراگرافِ داکیومنتِ فنی بنویس: «این ماژول برای X استفاده می‌شود…»'
                ]),
                ('faq', [
                    ('پاسخ تمرین ۱', '„Ich habe den Bug gefixt → Der Bug wurde gefixt.“ · „Wir haben deployt → Es wurde deployt / Das Deployment wurde durchgeführt.“ · „Ich habe die E-Mail geschickt → Die E-Mail wurde verschickt.“ — سه «من» به سه «فرایند» — زبانِ رسمی!'),
                    ('پاسخ تمرین ۲', '„Am Montag wurde die neue Version deployed. Am Dienstag wurde ein Fehler in der Bezahl-API festgestellt. Der Fix wurde am Mittwoch ausgerollt.“ — سه جملهٔ مجهولِ گزارشِ واقعی!'),
                    ('پاسخ تمرین ۳', '„Das muss bis Freitag gemacht werden.“ · „Das kann online beantragt werden.“ · „Das sollte im nächsten Sprint verbessert werden.“ — سه جملهٔ مودالیِ مجهولِ اداری-فنی!'),
                    ('پاسخ تمرین ۴', '„Dieses Modul wird für die Nutzer-Authentifizierung verwendet. Die Tokens werden automatisch erneuert. Konfigurationen können über die env-Datei geändert werden.“ — سه جملهٔ داکیومنتِ واقعیِ READMEِ آلمانی! 😄')
                ])
            ]
        },
        {
            'h2': 'چالشِ امروز',
            'blocks': [
                ('quote', '🎯 امروز سه جملهٔ روزت را «مجهولِ حرفه‌ای» کن — در چت، در ذهن، در یادداشت: «Das wurde gemacht، das wird geprüft، das kann erledigt werden» — صدای رسمیِ آلمانی‌ات، از امروز!'),
            ]
        },
        {
            'h2': 'نکات مکالمهٔ واقعی که کتاب‌ها کم می‌گویند',
            'blocks': [
                ('ul', [
                    '**«Es wird …» — درِ هر جملهٔ بی‌فاعل!** — Es wird geprüft، es wird davon abgesehen، es wird empfohlen… — «Es wird» آغازگرِ جمله‌هایِ رسمیِ بی‌شخص است؛ در نامه‌ها و خبرها همه‌جاست! جملهٔ ثبتِ رسمی: „Es wird darauf hingewiesen، dass…» (بدین‌وسیله توجه داده می‌شود که…)'
                ])
            ]
        },
    ],
    'takeaway': 'مجهول: werden + Partizip — wird geprüft (حال)، wurde deployt (گذشته)، ist … worden (کامل)، muss … werden (مودال). فاعل: von + Dativ (شخص) / durch + Akk (علت). «Es wurde beschlossen»، «Das kann beantragt werden» — زبانِ رسمیِ بی‌شخصِ گزارش، داکیومنت و نامهٔ اداریِ تو!',
    'faq': [
        ('مجهولِ «sein» و «werden» چه فرقی دارند؟', 'werden-Passiv = فرایند (Der Laden wird geschlossen [فروشگاه بسته می‌شود — در حالِ بسته‌شدن!])؛ sein-Passiv = نتیجه/وضعیت (Der Laden ist geschlossen [بسته است!]). اولی داری اتفاق می‌افتد، دومی تمام شده! در نامه: „Das Formular ist unterschrieben worden» (امضا شده) vs. „Das Formular ist unterschrieben» (امضاشده است/بی‌نقص!)'),
    ],
},

# ── درس ۸۰ ─────────────────────────────────────────────────────────────────
{
    'slug': 'german-subordinate-clauses',
    'title': 'جمله‌های وابسته؛ weil، dass، damit — فعل به آخر!',
    'desc': 'قانونِ بزرگِ آخر: در جملهٔ وابسته، فعل می‌رود آخر! — با weil (چون)، dass (که)، damit (تا)، wenn (اگر/وقتی) و obwohl (هرچند).',
    'keywords': 'جمله وابسته آلمانی, weil dass, فعل آخر آلمانی, Nebensatz, گرامر آلمانی',
    'answer': 'قانونِ طلاییِ جملهٔ وابسته: **فعلِ صرف‌شده می‌رود آخر!** — „Ich lerne Deutsch، **weil ich in Berlin arbeiten will**» (آلمانی یاد می‌گیرم چون می‌خواهم در برلین کار کنم — will آخر!). چهار پیوندِ طلایی: weil (چون — دلیل!)، dass (که — فکر/گفتار!)، damit (تا — هدف!)، wenn (اگر/وقتی) + obwohl (هرچند). با این درس، جمله‌هایت از «ساده» به «واقعی» می‌روند!',
    'intro': [
        'مشهورترین قانونِ آلمانیِ باقی‌مانده: «در جملهٔ وابسته، فعل آخر می‌رود» — قانونی که اول عجیب می‌آید و بعد، منطقِ قشنگش را می‌بینی: جملهٔ وابسته، «کاسهٔ کاملِ» فکر است و فعل، درِ بستهٔ آخرش!',
        'تا حالا «weil را با فعلِ جای دوم» شنیده‌ای (چون می‌گفتی: weil ich will arbeiten? نه!) — این درس، کلِ ماشین را می‌سازد: پنج پیوندِ طلایی + قانونِ جای فعل + جای جدا-شدنی‌ها و مودال‌ها. بعد از این درس، می‌توانی هر «چون/که/تا/اگر»ی را آلمانی بگویی — آخرین درِ بزرگِ جمله‌سازیِ تو باز می‌شود!'
    ],
    'sections': [
        {
            'h2': 'قانونِ طلایی؛ فعلِ آخر',
            'blocks': [
                ('table', ['جملهٔ اصلی', 'جملهٔ وابسته (فعل آخر!)'],
                    [['Ich will in Berlin arbeiten.', '…، weil ich in Berlin arbeiten **will**.'],
                     ['Ich habe gestern deployt.', '…، dass ich gestern deployt **habe**.'],
                     ['Ich mache einen Test.', '…، damit wir sicher sein können? — können + sein (دو فعل: کمکی آخرِ آخر!)'],
                     ['Ich lerne jeden Tag.', 'Wenn ich Zeit habe، lerne ich jeden Tag. (وابسته اول → فعلِ اصلی بعدش جای دوم!)']]),
                ('p', 'دو الگوی چیدمان: **[اصلی]، [وابسته با فعلِ آخر]** یا **[وابسته با فعلِ آخر]، [اصلی با فعلِ جای دوم]** — „Weil ich krank bin، bleibe ich zu Hause» (چون مریضم، خانه می‌مانم) — عبارتِ وابسته اول بیاید، جملهٔ اصلی بعدش، مثلِ زمانِ اول (درس ۸) فعلش جای دوم می‌نشیند!'),
            ]
        },
        {
            'h2': 'پنج پیوندِ طلایی',
            'blocks': [
                ('table', ['پیوند', 'معنی', 'جملهٔ کامل'],
                    [['weil', 'چون (دلیل!)', 'Ich komme später، weil ich noch einen Termin habe.'],
                     ['dass', 'که (فکر/گفتار!)', 'Ich denke، dass das eine gute Idee ist.'],
                     ['damit', 'تا (هدف — فعلِ جدا!)', 'Ich dokumentiere alles، damit du weitermachen kannst.'],
                     ['wenn', 'اگر/وقتی', 'Wenn der Build rot ist، fixe ich ihn zuerst.'],
                     ['obwohl', 'هرچند', 'Obwohl es schwer ist، mache ich weiter.']]),
                ('p', 'تفکیکِ دو دشمن: **weil** (چون — دلیلِ واقعی: جوابِ «warum؟») در برابرِ **dass** (که — محتوای فکر/گفتار: بعد از denken/glauben/sagen/finden!) — „Ich glaube، **dass** es klappt» (فکر می‌کنم که جواب می‌دهد) ≠ „Ich bin müde، **weil** ich spät arbeite» (خسته‌ام چون دیر کار می‌کنم)!'),
            ]
        },
        {
            'h2': 'گفتگو: جلسهٔ «چون-ها» — همه‌چیز وابسته!',
            'blocks': [
                ('ex', 'Warum verschieben wir den Deploy? — Weil der kritische Bug noch nicht gefixt ist.', 'چرا دیپلوی را عقب می‌اندازیم؟ — چون باگِ حیاتی هنوز فیکس نشده است. — weil + مجهولِ وابسته: gefixt ist (فعل آخر!)!'),
                ('ex', 'Ich denke، dass wir morgen trotzdem deployen können، wenn die Tests heute grün sind.', 'فکر می‌کنم که با این حال فردا می‌توانیم دیپلوی کنیم، اگر تست‌ها امروز سبز باشند. — dass + können + wenn — دو وابسته در یک جملهٔ حرفه‌ای!'),
                ('ex', 'Ich schreibe die Doku heute، damit du morgen übernehmen kannst، obwohl ich eigentlich Feierabend machen wollte.', 'داکیومنت را امروز می‌نویسم تا فردا بتونی برش داری، هرچند راستش می‌خواستم فایرآبند کنم. — damit + obwohl + wollte (فعلِ چهارمقدسِ آخر!) — جملهٔ سه‌وابسته‌ایِ واقعی!')
            ]
        },
        {
            'h2': 'اشتباه‌های رایجِ فارسی‌زبان‌ها در همین درس',
            'blocks': [
                ('p', 'این بخش را با یک قرارداد بخوان: هر ❌ یعنی «مغزِ فارسی‌زبانت این را می‌سازد و طبیعی است»، و هر ✅ یعنی «این همان چیزی است که گیرندهٔ آلمانی‌زبان می‌شنود». با هر جفت بلند تکرار کن تا شکلِ درست در گوشت نشست کند.'),
                ('ex', '❌ Weil ich habe keine Zeit.', '❌ کلاسیکِ کلاسیک‌ها! در weil، فعل آخر: „…weil ich keine Zeit **habe**.» — و «weil + فعلِ جای دوم» حتی بینِ جوان‌های آلمانی شوخی‌شده است!'),
                ('ex', '✅ …، weil ich keine Zeit habe. / …، weil ich krank bin.', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.'),
                ('ex', '❌ Ich denke، weil das gut ist. (به‌جای dass!)', '❌ «فکر می‌کنم چون خوب است» ≠ «فکر می‌کنم که خوب است»! فکر+محتوا → dass؛ فکر+دلیل → weil!'),
                ('ex', '✅ Ich denke، dass das gut ist. / Ich bin froh، weil es gut ist.', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.'),
                ('ex', '❌ Ich lerne Deutsch، weil ich will in Deutschland arbeiten.', '❌ فعلِ مودال هم آخر می‌رود: arbeiten will!'),
                ('ex', '✅ Ich lerne Deutsch، weil ich in Deutschland arbeiten will.', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.')
            ]
        },
        {
            'h2': 'تمرین‌های این درس — چهار قدم، بی‌عجله',
            'blocks': [
                ('p', 'تمرین: جمله‌های پیچیدهٔ واقعی بساز!'),
                ('ol', [
                    'پنج جملهٔ «چون» دربارهٔ تصمیم‌های واقعیِ امروزت بنویس — weil + فعلِ آخر!',
                    'سه جملهٔ «فکر» با dass بنویس: دربارهٔ کار، دوره، آلمان.',
                    'دو جملهٔ هدف با damit بساز: برای چی کار می‌کنی؟',
                    'یک جملهٔ سه‌پیوندی بساز: wenn + dass/obwohl + فعلِ اصلی — مثلِ دیالوگِ درس!'
                ]),
                ('faq', [
                    ('پاسخ تمرین ۱', '„Ich trinke Kaffee، weil der Tag lang wird.“ · „Ich verschiebe den Termin، weil ich noch eine Frage habe.“ · „Ich lerne abends، weil ich tagsüber arbeite.“ — سه «چون»ی واقعی با فعلِ آخر!'),
                    ('پاسخ تمرین ۲', '„Ich glaube، dass das klappt.“ · „Ich finde، dass der Kurs super ist.“ · „Ich hoffe، dass ich im Sommer B1 schaffe.“ — سه «فکر» با dass — جمله‌هایِ نظرِ حرفه‌ای!'),
                    ('پاسخ تمرین ۳', '„Ich schreibe alles auf، damit ich es nicht vergesse.“ · „Ich übe täglich، damit die Sprache sitzt.“ — دو جملهٔ هدفِ واقعیِ یادگیری!'),
                    ('پاسخ تمرین ۴', '„Wenn ich mehr Zeit hätte، würde ich glauben، dass ich alles schaffen könnte.“ 😄 — wenn + würde + dass + könnte — چهار لایه؛ اگر این جمله را روان گفتی، دکترایِ جمله‌سازی‌ات تمام است!')
                ])
            ]
        },
        {
            'h2': 'چالشِ امروز',
            'blocks': [
                ('quote', '🎯 امروز هر «چون»ی که می‌گویی، با weilِ درست بگو — سه بار در روز، فعل آخر! «weil-Bug» بزرگ‌ترین باگِ زبانیِ مهاجرهاست — امروز فیکسش می‌کنی!'),
            ]
        },
        {
            'h2': 'نکات مکالمهٔ واقعی که کتاب‌ها کم می‌گویند',
            'blocks': [
                ('ul', [
                    '**«weil» و «denn» — دو برادرِ دلیل!** — weil = وابسته (فعل آخر!)؛ denn = هم‌تراز (فعل جای دوم!): „Ich bleibe zu Hause، denn ich bin müde» (خانه می‌مانم، چون خسته‌ام — فعل وسط!) — هر دو درست؛ denn راحت‌تر برای شروع! در گفتارِ روزمره، آلمانی‌ها وقتی «عجله» دارند denn می‌گویند — و وقتی دقیق‌اند، weil!'
                ])
            ]
        },
    ],
    'takeaway': 'جملهٔ وابسته = فعلِ صرف‌شده آخر — weil (دلیل)، dass (فکر)، damit (هدف)، wenn (اگر/وقتی)، obwohl (هرچند). دو چیدمان: [اصلی]، [وابسته-فعلِ-آخر] یا [وابسته]، [اصلی-فعلِ دوم]. weil ≠ dass: دلیل ≠ محتوا! «…، weil ich keine Zeit habe.» — باگِ بزرگِ زبانی، فیکس شد!',
    'faq': [
        ('چطور مطمئن شوم جمله‌ام «وابسته» است؟', 'سه نشانه: ۱) بعدش کاما آمده و جمله «ناقص» می‌ماند؛ ۲) یکی از پیوندها (weil/dass/wenn/damit/obwohl/der…) سرِ آن است؛ ۳) اگر جوابِ «چرا/که/اگر» یک جملهٔ کامل است — وابسته است! تستِ طلایی: فعلِ صرف‌شده را به آخرِ عبارتِ بعد از کاما ببر — اگر طبیعی خواند، درستش همان است!')
    ],
},

# ── درس ۸۱ ─────────────────────────────────────────────────────────────────
{
    'slug': 'german-relative-clauses',
    'title': 'جمله‌های نسبی؛ توضیحِ فنی به سبکِ بومی',
    'desc': 'der، die، das به‌عنوان پیوند: «که …» — ساختِ جملهٔ نسبی با حالتِ درست و توضیحِ هر چیزی، از باگ تا خانه.',
    'keywords': 'جمله نسبی آلمانی, Relativsatz, که آلمانی, گرامر آلمانی, توضیح آلمانی',
    'answer': 'جملهٔ نسبی = «که»ی توضیحی: der Bug، **der gestern auftrat** (باگی که دیروز رخ داد) — قاعدهٔ طلایی: پیوندِ نسبی (der/die/das/den/dem…) از **جنسیت و عددِ اسم** می‌آید و **حالتش از نقشِ داخلِ جملهٔ نسبی**! و مثلِ هر وابسته‌ای: فعلِ آخر! با نسبی، توضیح‌هایت از «دو جملهٔ کوتاه» به «یک جملهٔ حرفه‌ای» می‌رسد!',
    'intro': [
        'آخرین ابزارِ بزرگِ جمله‌سازی: جملهٔ نسبی — «که»ی توضیحی که دو جمله را به هم می‌دوزد! «باگی دیدم. آن باگ دیروز آمد.» → «باگی دیدم که دیروز آمد» — حرفه‌ای‌تر، کوتاه‌تر، بومی‌تر!',
        'و نکتهٔ مهندسیِ قشنگ: پیوندِ نسبی «کایمِرا» است — نصفش تعریف (جنسیت/عدد از اسمِ قبلی!) و نصفش ضمیر (حالت از کارِ داخلِ جمله!)! با این یک قاعده و فعلِ آخر (که از درس ۸۰ بلدی!)، هر توضیحِ دنیا — فنی، اداری، احساسی — یک‌جمله‌ای می‌شود!'
    ],
    'sections': [
        {
            'h2': 'قاعدهٔ دو-نیمه؛ جنسیت + حالت',
            'blocks': [
                ('table', ['اسم', 'پیوند (به نقشِ جملهٔ نسبی!)', 'جمله'],
                    [['der Bug (مذکر)', 'der (فاعل) / den (مفعول) / dem (Dativ)', 'der Bug، der auftrat / den wir fixten / dem wir folgten'],
                     ['die Frage (مؤنث)', 'die / die / der', 'die Frage، die du stelltest / die ich beantwortete'],
                     ['das Ticket (خنثی)', 'das / das / dem', 'das Ticket، das offen ist / dem wir uns widmen'],
                     ['die Kollegen (جمع)', 'die / die / den + n!', 'die Kollegen، die halfen']]),
                ('p', 'رمزِ ساده: **جنسیت/عدد را از اسمِ توضیح‌شده بگیر؛ حالت را از شغلی که پیوند داخلِ جملهٔ نسبی دارد!** — «Der Kollege، **dem** ich geholfen habe» (همکاری که بهش کمک کردم — Kollege مذکر؛ helfen = Dativ → dem!)'),
            ]
        },
        {
            'h2': 'چهار قالبِ آماده؛ برای هر روز',
            'blocks': [
                ('ex', '…، der/die/das … ist. — Die App， die ich benutze، ist toll. (اپی که استفاده می‌کنم عالی است.)', 'قالبِ توصیفِ محبوب — دو جمله به یک جمله!'),
                ('ex', '…، den/die/das ich … habe. — Den Termin، den ich hatte، wurde verschoben. (نوبتی که داشتم، عقب افتاد.)', 'روایتِ اداری!'),
                ('ex', '…، wo (جایی که!) / wann (زمانی که!) — Das Büro، wo ich arbeite، ist neu. / Die Zeit، wann wir anfangen، ist flexibel.', 'wo/wann برای مکان و زمان — ساده‌تر ازِ در/das!'),
                ('ex', '…، was (چیزی که!) — Das， was du gesagt hast، war gold richtig! (چیزی که گفتی کاملاً درست بود!)', 'was برای جمله‌های کلی — «آنچه»ی طلایی!')
            ]
        },
        {
            'h2': 'گفتگو: توضیحِ فنی — نسبیِ کامل',
            'blocks': [
                ('ex', 'Der Bug، den wir gestern entdeckt haben، liegt in dem Modul، das für die Authentifizierung zuständig ist.', 'باگی که دیروز کشف کردیم، در ماژولی است که مسئولِ احراز هویت است. — den (مفعول!) + das (فاعلِ نسبیِ بعدی!) — دو نسبیِ زنجیره‌ای!'),
                ('ex', 'Der Kollege، der das geschrieben hat، ist im Urlaub — aber die Doku، die er hinterlassen hat， ist gut.', 'همکاری که این را نوشته، مرخصی است — ولی داکیومنتی که گذاشته خوب است. — der + die: دو جملهٔ نسبیِ روان!'),
                ('ex', 'Alles， was wir brauchen، ist ein Test، der das reproduziert.', 'همه‌چیزِ آنچه لازم داریم، تستی است که این را بازتولید کند. — was + der: جملهٔ جمع‌بندیِ فنی!')
            ]
        },
        {
            'h2': 'اشتباه‌های رایجِ فارسی‌زبان‌ها در همین درس',
            'blocks': [
                ('p', 'این بخش را با یک قرارداد بخوان: هر ❌ یعنی «مغزِ فارسی‌زبانت این را می‌سازد و طبیعی است»، و هر ✅ یعنی «این همان چیزی است که گیرندهٔ آلمانی‌زبان می‌شنود». با هر جفت بلند تکرار کن تا شکلِ درست در گوشت نشست کند.'),
                ('ex', '❌ Der Bug، der wir gefunden haben (به‌جای den!)', '❌ داخلِ نسبی، «باگ» مفعول است (پیدایش کردیم) → den! جنسیت فقط شکلِ پایه را می‌دهد، حالت از نقش!')
                ,
                ('ex', '✅ Der Bug، den wir gefunden haben. / Der Bug، der auftrat. (فاعل → der!)', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.'),
                ('ex', '❌ Die Kollegin، die ich geholfen habe. (helfen = Dativ!)', '❌ helfen به Dativ می‌گیرد: der ich geholfen habe! فعل + حالت را با هم چک کن (درس ۷۵!)!'),
                ('ex', '✅ Die Kollegin， der ich geholfen habe.', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.'),
                ('ex', '❌ Der Termin، wo morgen ist. (زمان ≠ مکان!)', '❌ wo فقط مکان است! زمان: wenn/der Tag، an dem… — «der Termin، der morgen ist»!')
                ,
                ('ex', '✅ Der Termin， der morgen ist. / Das Büro， wo ich sitze.', '✅ شکل درست را دو بار بلند بگو؛ حالا یک بار در یک جملهٔ خودت.')
            ]
        },
        {
            'h2': 'تمرین‌های این درس — چهار قدم، بی‌عجله',
            'blocks': [
                ('p', 'تمرین: توضیح‌دهندهٔ حرفه‌ای شو!'),
                ('ol', [
                    'پنج «اسم + جملهٔ نسبی» از زندگیِ روزمره‌ات بساز: اپ، همکار، خانه، درس، غذا!',
                    'سه جملهٔ نسبیِ مفعولی بساز (den/die/das + فعلِ با مفعول!): چیزی که گرفتی/دیدی/فهمیدی.',
                    'با wo/was دو جملهٔ توضیحی بساز: جایی که کار می‌کنی، چیزی که یاد گرفتی.',
                    'یک جملهٔ زنجیره‌ایِ دو-نسبیِ فنی بساز — مثلِ دیالوگِ درس!'
                ]),
                ('faq', [
                    ('پاسخ تمرین ۱', '„Die App， die ich täglich nutze، heißt UpWord.“ · „Der Kollege， der neben mir sitzt， kommt aus Wien.“ · „Das Zimmer， das ich miete， ist klein aber hell.“ — سه جملهٔ نسبیِ واقعیِ روزمره!'),
                    ('پاسخ تمرین ۲', '„Der Kurs， den ich mache， ist fast fertig.“ · „Die Frage، die du gestellt hast， war wichtig.“ · „Das Feedback， das ich bekommen habe， war fair.“ — سه نسبیِ مفعولی (den/die/das) با فعلِ آخر!'),
                    ('پاسخ تمرین ۳', '„Das Büro， wo ich arbeite， liegt im dritten Stock.“ · „Alles， was ich heute gelernt habe، ist: Relativsätze!“ — wo برای مکان، was برای کلیات — دو قالبِ طلایی!'),
                    ('پاسخ تمرین ۴', '„Das Ticket， das wir heute fixen， betrifft einen Bug， der nur nachts auftritt.“ — دو نسبی + یک صحنهٔ فنیِ واقعی — جملهٔ امضایِ دیباگرِ آلمانی‌کَش! 😄')
                ])
            ]
        },
        {
            'h2': 'چالشِ امروز',
            'blocks': [
                ('quote', '🎯 امروز سه «دو جملهٔ کوتاه» از گفتارت را با جملهٔ نسبی یکی کن: «مردم را دیدم. مردم خندیدند» → «مردمی را دیدم که خندیدند» — سه دوزِ حرفه‌ای؛ جمله‌هایت از امروز دو-طبقه می‌شوند!'),
            ]
        },
        {
            'h2': 'نکات مکالمهٔ واقعی که کتاب‌ها کم می‌گویند',
            'blocks': [
                ('ul', [
                    '**نسبی، «ژستِ حرفه‌ایِ» توضیح است!** — در مصاحبه و جلسه، جملهٔ نسبی نشانهٔ زبانِ کامل است: «Ich suche eine Rolle， in der ich wachsen kann» (نقشی می‌جوییم که در آن بتوانم رشد کنم — in der + Dativ!) — یک جمله = مصاحبهٔ سطحِ بالا!',
                    '**«wer … ، der …» — نسخهٔ عمومی!** — „Wer zuletzt lacht، lacht am besten» (هر که آخر بخندد، بهتر می‌خندد!) — قالبِ ضرب‌المثل‌های آلمانی! «Wer rastet، der rostet» (هر که آسودگی کند، زنگ می‌زند!) — با این قالب، حکمت‌گو شده‌ای!'
                ])
            ]
        },
    ],
    'takeaway': 'جملهٔ نسبی: پیوند از جنسیت/عددِ اسم + حالت از نقشِ داخل — و فعلِ آخر (همیشه!). der/die/das/den/dem + wo (مکان) + was (کلیات). «Der Bug， den wir fanden، lag in dem Modul، das …» — زنجیره‌های نسبی، امضای زبانِ حرفه‌ایِ آلمانی‌اند!',
    'faq': [
        ('نسبی و وابسته چه فرقی دارند؟', 'هر دو «فعل آخر» — ولی نسبی، «اسمِ قبلی را توضیح می‌دهد» (der Bug، der… — که!) و وابسته، «کل جمله را به هم می‌دوزد» (weil/dass/wenn… — چون/که/اگر). تست: اگر پیوند جای اسم می‌نشیند → نسبی؛ اگر پیوندِ منطقیِ دو جمله است → وابسته. هر دو آخرِ مهارتِ جمله‌سازی‌ات‌اند — و حالا هر دو داری!')
    ],
},
]

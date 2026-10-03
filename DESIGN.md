# UpWord design system — v2 (Deep Green Glass)

## 1. Direction
The landing mirrors the Android app itself: a deep emerald-green world with glassmorphism surfaces, floating ambient orbs, and the turtle mascot. Persian (fa, RTL) is the default experience; English (en, LTR) is one toggle away and fully translated. The visitor journey: hero promise → languages → learning path → feature deep-dives (piece by piece) → supporting features bento → app preview → free-vs-premium → learner evidence → FAQ → download (Cafe Bazaar + Myket).

Vanilla HTML/CSS/JS, no framework. All mockups are live HTML, clearly illustrative.

## 2. Color
Primary green #22C55E (buttons, rings, progress), light #4ADE80, pale #A7F3D0, glow rgba(34,197,94,.42). Backgrounds: #04231A → #051D13 deep gradient with fixed blurred orbs (green, teal, butter). Ink #EAF6EF, soft #BFDCCB, mute #86A896. Butter #F5E7AE marks feedback/gems/best-choice accents; lilac and per-family icon tints (teal/purple/orange/indigo) stay secondary inside bento icon tiles only. Green buttons always carry dark text (#04271A) for AA contrast.

## 3. Typography
Vazirmatn (fa body + display, 800/900 for titles, line-height 1.4–2.1), Inter (en body), Space Grotesk (en display via html[lang="en"] overrides with tighter tracking). Hero title clamp(38px…68px); section titles clamp(26…40px); body 13–16px; mockup micro-type 9.5–13px. No all-caps Persian; balanced headings.

## 4. Spacing & layout
Container 1200px, gutters 24px (20 mobile). Sections clamp(72…112px) block padding. Radii: 36 (hero art/CTA), 28 (cards/plans), 20 (inner), 14 (tiles). Breakpoints 1080 / 980 / 680. Feature rows alternate text/visual via .flip order swap; bento spans 2-of-4 columns. Logical properties (inset-inline, margin-inline) throughout so RTL mirrors automatically.

## 5. Components
- Glass family: linear-gradient(165deg, rgba(255,255,255,.09/.055)), 1px rgba(255,255,255,.13) border, backdrop-blur 12–22px; raised variants add deep drop shadows and green glows.
- Hero visual (v3): the app's own hero-card tutor (assets/images/hero-tutor.webp, alpha) on a deep-green aurora scene, with white greeting bubbles (Hello! / 你好! / Привет!) like the app's home hero card. og-cover.png (1200×630) composites the same tutor for social sharing.
- Phone frame: 300px (preview phones 316px + min-height 660px screen — taller, realistic proportions), radius 50, dark hardware gradient, punch-hole camera, inner screen emerald gradient; content is real HTML (courses with circular SVG progress rings, AI chat with correction feedback card, gamification profile with XP bar, gems, Iranian-week streak calendar, achievements). Preview screens end in a bottom tab bar (Home/Lessons/Chat/Profile) mirroring the app's navigation.
- Floating hero glass cards: Android-style practice-reminder notification, streak chip, XP chip — gently drifting, disabled under reduced motion.
- Journey: 4 numbered glass steps over a dashed track with the swimming turtle Lottie.
- Premium: free vs premium plan cards; premium carries a gradient border, glow, "most popular" badge and tier chips (monthly / 6-month / yearly·best / lifetime). No hardcoded prices — the note points to the in-app store panel.
- Reviews: 3 verbatim Cafe Bazaar quotes (Persian original + translation) + a summary card linking to the store.
- FAQ: native details/summary, one open at a time (JS), rotating + icon.
- Buttons: primary green gradient (dark text, glow shadow), ghost/glass secondary; 44px+ targets.

## 6. Motion & interaction
Reveal-on-scroll via IntersectionObserver + WAAPI (650ms, stagger 75ms max 3), cancelled by keyboard focus or prefers-reduced-motion. Orbs drift 26–38s; float cards bob 5.5–7s; waveform bars pulse; pill dot pulses once per 2.4s. Turtles (swimming/success/meditation) play once when visible, pause offscreen/background, static 40% frame under reduced motion. Native anchors smooth-scroll with navbar offset.

## 7. i18n mechanism
223 data-i18n / data-i18n-html / data-i18n-alt keys, mirrored fa+en dictionaries in js/main.js. The language strip and copy list only the six languages the app actually ships (English, Persian, Chinese, Russian, German, Arabic — the app's SupportedLanguages catalog). Pre-paint script applies the stored language (default fa/RTL) before first render; toggling persists in localStorage 'upword-lang'. Persian strings use Persian digits; English dictionary switches mockups to Latin digits automatically. `html[lang="en"]` drives font/line-height/tracking overrides and hides the redundant English topic subtitle.

## 8. Accessibility constraints
WCAG AA contrast on dark green, visible focus rings, skip link, aria-labels on nav/switcher/toggle, aria-hidden decorative mockups, Escape closes menu/dropdown, reduced-motion kills all perpetual animation. Static HTML ships with full Persian content so the page works without JS.

## 9. Content honesty
Free tier = first A1 topic (3 lessons). Premium prices are store-panel-defined, never hardcoded. AI conversations need internet + user-connected provider (no free AI credit implied). Real reviews kept verbatim with attribution; current ratings deferred to the store page. Illustrations and mockups explicitly labelled as illustrative.

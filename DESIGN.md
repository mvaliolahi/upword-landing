# UpWord design system

## 1. Direction
An encouraging language-learning companion for adults. Bright green (#22C55E) owns primary actions and learning accents. Ivory-white breathing room and charcoal typography keep the green distinctive. Cards share white surfaces and restrained mint accents. Preserve the turtle brand and English/Persian content. The visitor journey is confidence → practice tools → first steps → app preview → learner evidence → questions → download.

Extracted primitives: container, button variants, section heading, feature card, phone frame, testimonial, native FAQ disclosure, navigation and language switcher. This is an existing vanilla HTML/CSS/JS project; no framework is needed.

## 2. Color
Main green #22C55E, dark #15803D, darker #173F32, light #4ADE80, lighter #86EFAC, background #DCFCE7, soft #F0FDF4. Page #FCFCF8, alternate #F4F5F0, white #FFFFFF; border #E2E5DE; primary text #202B25, secondary #566159, muted #667168. Accent butter #F5E7AE and lilac #E9E4F3 are secondary only. Bright green surfaces use dark text for contrast; green text on light surfaces uses the dark shade. Translucent white rims and green-tinted shadows add dimension to the hero and elevated notes.

## 3. Typography
Hero direction: editorial split composition with a 56–72px medium-weight headline and an italic Georgia accent for the English second line. Georgia is a deliberate third, system-provided family used only for this short display phrase; Persian stays Vazirmatn. Primary brand green remains #22C55E. A wide, upright white conversation panel replaces the tilted phone and floating stickers. The panel uses a deep-green café scene, legible chat bubbles, and an integrated practice footer. Its intrinsic height accommodates Persian text. Proof numbers form a quiet inline row. Hero CTAs have rounded ends, with one filled action and one text link. Existing reveal animations target the full preview.

Inter for English, Vazirmatn for Persian. Display 40–76px, 800 weight, 1.08 leading, -.055em tracking in English. Persian display 40–64px, 1.45 leading, no negative tracking. Section heading 30–48px, body 16px, lead 18px, small 14px, preview metadata 12px. Use balanced headings; no all-caps Persian.

## 4. Spacing & layout
4px base. Steps 4/8/12/16/20/24/32/40/48/64/80/96. Container 1200px with 24px gutters (20px on phones). Split hero with text first at every size; stack below 980px. Sections 80–96px desktop and 64px mobile. Radius 10/16/24/32px. Breakpoints 680/980px. Document owns scrolling.

## 5. Components
- Shared card family: radius 24px, inner/compact radius 16px, padding 32px desktop and 24px below 980px, grid gap 24px (16px mobile). Border 1px #E2E5DE; resting shadow 0 2px 4px #173F3203 plus 0 12px 28px -20px #173F3226. Raised hero shadow 0 4px 8px #173F3205 plus 0 24px 64px -24px #173F3233. Shared titles 20px/700/1.4 and body 14px/1.8. Base rules group existing semantic classes instead of adding a parallel component framework.
- Card variants: features/steps/reviews use the base surface; review summary uses mint; FAQ and nested app cards use compact radius and padding; hero preview uses raised elevation with an 8px inset; final CTA uses the same outer radius with a charcoal surface and larger section-level padding. Noninteractive cards do not lift on hover; disclosures get visible open and keyboard-focus states.
- Step illustrations: retain the shared 110px layout box. Scale the first animation's wrapper by 1.6 to compensate for its canvas padding; keep scaling off the SVG because Lottie owns its inline transform.
- Buttons: primary bright green with dark text and subtle green shadow, secondary outlined white, final bright green on a charcoal panel; 44px minimum target, hover/pressed transform, visible focus outline. Real store links only.
- Navigation: logo, anchor links, language disclosure, download. Mobile menu closed/open via button with expanded state; Escape closes. Language options preserve preference and RTL.
- Section headings: eyebrow + balanced title + supporting copy. Features left-aligned; other explanatory sections centered.
- Feature cards: consistent white surfaces, mint icon tiles, dark-green icons. Shared icon/title/body structure, no hover motion on noninteractive cards.
- Phone frame: dimensional dark frame containing real HTML examples; explicitly labelled as illustrative, not a working app. Conversation is English practice in either page locale.
- Language strip: six noninteractive language names from the existing supported-language list.
- Testimonials: preserve original quotes and attribution, separate translated text. No invented social proof.
- FAQ: native details/summary, keyboard operable, plus indicator, one open at a time.

## 6. Motion & interaction
Motion tokens: micro 200ms; reveal 650ms; stagger 75ms (maximum three steps); reveal distance 24px; easing cubic-bezier(0.16, 1, 0.3, 1). Native scrolling and a transform-based reading-progress indicator follow the beui.dev scroll-animation mechanism without adding Lenis. Hover/focus arrow movement and a 0.97 press scale adapt beui.dev expanding-arrow-button feedback using CSS.

Hero content and section groups reveal once on entering view through IntersectionObserver and the Web Animations API. Content stays visible if animation APIs or JavaScript are unavailable; keyboard focus cancels any containing reveal. Reduced-motion changes immediately cancel reveals. Native FAQ answers reveal on opening. Navigation gets a sliding underline on hover/focus, and primary buttons a single sheen per hover/focus.

Turtles play once when visible, pause offscreen or in a background tab, and show a static 40% frame for reduced motion. No perpetual movement or new animation dependency. Existing anchors respect reduced motion. Manual browser review is owned by the user; automated browser checks are explicitly excluded.

## 7. Depth & surface
Mixed system: shared card borders and shadows separate white surfaces from neutral section backgrounds. The upright hero conversation panel has raised elevation and a restrained mint glow. Phone frames retain dark hardware with consistent white nested cards. The language strip uses an inset neutral panel. The final charcoal CTA shares the card corner radius and has a green halo behind the turtle, with content aligned to the reading edge on desktop and centered on mobile. No perpetual decorative animation.

## 8. Accessibility constraints & verification
Target WCAG AA contrast, visible keyboard focus, text-first mobile hierarchy, semantic main, skip link, labelled menu state, no hidden mobile links in tab order, RTL support and reduced motion. Test English/Persian at 375/768/1280px, language persistence, menu and Escape, FAQ, anchor and store destinations. Existing product claims and review counts are retained, not newly independently verified. Mock app controls remain clearly labelled illustrations.

## 9. Conversation-first redesign — September 2026

This revision follows the existing brand and vanilla component system, informed by the Android repository's release-readiness review. Audience: adult learners who know some words but hesitate to speak, including Persian-speaking Android users. Decision path: understand the benefit → see a worked correction → explore practice tools → understand setup → download. Retain original attributed reviews as historical quotes, without claiming current ratings or verified counts.

The signature composition is a large editorial headline beside a dark-green practice desk with an inset white conversation sheet. A numbered practice/feedback/review strip replaces vanity statistics. Feature cards use an asymmetric 2-column composition: conversation and missions lead; supporting tools follow. Butter and lilac surfaces distinguish learning feedback and recall. Gamification supports practice, never promises mastery from XP.

New primitives: learning-loop strip (static ordered steps); lesson example (native details disclosure, closed/open, focus-visible, English practice text isolated LTR); readiness note (visible provider/internet requirement); feature proof snippet (noninteractive example); practice section (split editorial copy and worked example). All are live HTML, not screenshots. Existing button, card, disclosure, navigation and language states are reused. Native details keeps the example available without JavaScript. Existing rendered primitives serve as the state harness before these compositions are changed.

Tokens added: space-1 4px, space-3 12px, space-5 20px, space-10 40px, space-20 80px; type-caption 12px, type-small 14px, type-body 16px, type-lead 18px, type-display clamp(44px, 5.4vw, 76px). Practice desk uses existing green-darker, green-bg, surface and card-shadow-raised; paper inset uses existing card-radius-inner. No new fonts or dependencies. Layout retains 680/980 breakpoints; all new grid children use minmax(0,1fr), logical spacing and intrinsic height.

Content contract: AI needs internet and compatible provider credentials; provider costs and data policies vary. Level is learner-selected. Voice support depends on engine/provider. No automatic placement, guaranteed outcomes, precise pronunciation scoring, free AI quota, offline audio guarantee or unsupported payment tier. Illustrations and worked examples are explicitly labelled. Current app features and proposed release improvements must not be conflated.

Verification: the user explicitly requested manual visual review and no further automated browser checks. Automated browser work was stopped on that instruction; final design approval belongs to the user. Source syntax and whitespace checks remain in scope. Manually inspect English/Persian layouts, keyboard focus, disclosure states, mobile menu, language persistence, anchors and reduced motion. No deployment is part of this task. Remaining product release gates belong to the Android review, not this landing-page update.
